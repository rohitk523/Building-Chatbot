from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json
from email.message import EmailMessage
import requests
import smtplib
from concurrent.futures import ThreadPoolExecutor

ZomatoData = pd.read_csv('zomato.csv',encoding = 'latin1')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']

def RestaurantSearch(City,Cuisine,budgetmin,budgetmax):
    TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))]
    TEMP = TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]
    TEMP = TEMP[(TEMP['Average Cost for two']>=budgetmin) & (TEMP['Average Cost for two']<=budgetmax)]
    return TEMP.sort_values('Aggregate rating',ascending = False)

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		#config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budgetmin = int(tracker.get_slot('budgetmin'))
		budgetmax = int(tracker.get_slot('budgetmax'))
		results = RestaurantSearch(City=loc,Cuisine=cuisine,budgetmin=budgetmin,budgetmax=budgetmax)
		response=""
		if results.shape[0] == 0:
			response= "no results"
		else:
			for restaurant in RestaurantSearch(loc,cuisine,budgetmin,budgetmax).iloc[:5].iterrows():
				restaurant = restaurant[1]
				response=response + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Address']} with avg cost {restaurant['Average Cost for two']} \n\n"
				
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc),SlotSet('budgetmin',budgetmin ), SlotSet('budgetmax', budgetmax)]

class CheckLocation(Action):

    TIER_1 = []
    TIER_2 = []

    def __init__(self):
        self.TIER_1 = ['ahmedabad', 'bangalore', 'chennai',
                       'delhi', 'hyderabad', 'kolkata', 'mumbai', 'pune']
        self.TIER_2 = [ 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore',  'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Coimbatore', 'Guwahati', 'Jaipur', 'Nashik', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']
    def name(self):
        return "check_location"
    
    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        if not (self.verify_location(loc)):
            dispatcher.utter_message(
                "We do not operate in " + loc + " yet. Please try some other city.")
            return [SlotSet('location', None), SlotSet("location_ok", False)]
        else:
            return [SlotSet('location', loc), SlotSet("location_ok", True)]

    def verify_location(self, loc):
        return loc.lower() in self.TIER_1 or loc.lower() in self.TIER_2


class VerifyBudget(Action):

    def name(self):
        return "verify_budget"

    def run(self, dispatcher, tracker, domain):
        budgetmin = None
        budgetmax = None
        error_msg = "Sorry!! price range not supported, please re-enter."
        try:
            budgetmin = int(tracker.get_slot('budgetmin'))
            budgetmax = int(tracker.get_slot('budgetmax'))
        except ValueError:
            dispatcher.utter_message(error_msg)
            return [SlotSet('budgetmin', None), SlotSet('budgetmax', None), SlotSet('budget_ok', False)]
        min_dict = [0, 300, 700]
        max_dict = [300, 700]
        if budgetmin in min_dict and (budgetmax in max_dict or budgetmax > 700):
            return [SlotSet('budgetmin', budgetmin), SlotSet('budgetmax', budgetmax), SlotSet('budget_ok', True)]
        else:
            dispatcher.utter_message(error_msg)
            return [SlotSet('budgetmin', 0), SlotSet('budgetmax', 10000), SlotSet('budget_ok', False)]
        
        
class ActionSendEmail(Action):
    def name(self):
        return 'action_send_email'
        
    def run(self, dispatcher, tracker, domain):
        # Get user's email id
        to_email = tracker.get_slot('emailid')

        # Get location and cuisines to put in the email
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        budgetmin = int(tracker.get_slot('budgetmin'))
        budgetmax = int(tracker.get_slot('budgetmax'))
        
        d_email_subj = 'Top 5 {1} restautants in {0} '.format(loc,cuisine)
        d_email_msg = ''
        for index, row in RestaurantSearch(loc,cuisine,budgetmin,budgetmax).iloc[:5].iterrows():
            d_email_msg =d_email_msg +('\nRestaurant Name: {0}\nAddress: {1}\nAvg cost for 2: {2}\nRating: {3}\n '.format(row["Restaurant Name"], row["Address"], row["Average Cost for two"], row["Aggregate rating"]))

        # Open SMTP connection to our email id.
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login("rohitfoodie523@gmail.com", "Rohit@123")

        # Create the msg object
        msg = EmailMessage()

        # Fill in the message properties
        msg['Subject'] = d_email_subj
        msg['From'] = "rohitfoodie523@gmail.com"

        # Fill in the message content
        msg.set_content(d_email_msg)
        msg['To'] = to_email

        s.send_message(msg)
        s.quit()
        dispatcher.utter_message(" EMAIL SENT:)")
        return []
