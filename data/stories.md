## interactive story 1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - check_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700", "budgetmax": "10000"}
    - slot{"budgetmin": "700"}
    - slot{"budgetmax": "10000"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"emailid": "rohitkale523@gmail.com"}
    - slot{"emailid": "rohitkale523@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive story 2
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - check_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - check_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700", "budgetmax": "10000"}
    - slot{"budgetmin": "700"}
    - slot{"budgetmax": "10000"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - utter_ask_email
* dont_send_email
    - utter_goodbye
    - action_restart

## interactive story 3
* greet
    - utter_greet
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - check_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - check_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "0", "budgetmax": "300"}
    - slot{"budgetmin": "0"}
    - slot{"budgetmax": "300"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - utter_ask_email
* dont_send_email
    - utter_goodbye
    - action_restart

## interactive story 4
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - check_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - check_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700", "budgetmax": "10000"}
    - slot{"budgetmin": "700"}
    - slot{"budgetmax": "10000"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_email{"emailid": "rohitkale523@gmail.com"}
    - slot{"emailid": "rohitkale523@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - check_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - utter_ask_budget


## interactive story 5
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - check_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700", "budgetmax": "10000"}
    - slot{"budgetmin": "700"}
    - slot{"budgetmax": "10000"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_email{"emailid": "rohitkale523@gmail.com"}
    - slot{"emailid": "rohitkale523@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart
