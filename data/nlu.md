## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks

## intent:send_email
- ok [a.b@gmail.com](emailid)
- [lg@hotmail.com](emailid)
- sure my emailid is [rlkh@gmail.com](emailid)
- [rohitkale523@gmail.com](emailid)
- [rohitkale523@gmail.com](emailid)

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- hola
- hello!
- hwllo

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate]{"entity": "price", "value": "mid"} price range with [british](cuisine) food for [four]{"entity": "people", "value": "4"} people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- [Rs 300 to 700](price)
- [More than 700](price)
- [lesser than 300](price)
- [900](price)
- I'm hungry. Looking out for some good restaurants
- [bengaluru]{"entity": "location", "value": "bangalore"}
- Can you suggest some good restaurants in [Rishikesh](location)
- Okay. Show some in [Allahabad](location)
- Show me some in [delhi](location)
- In [mubaim](location)
- in [mumbai](location)
- [American](cuisine)
- Looking out for some good [chinese](cuisine) restaurants in [chandigarh](location)
- Looking out for some good [chinese](cuisine) restaurants
- [chennai](location)
- looking out for some good [chinese](cuisine) restaurant

## intent:send_mail
- yes. Please send it to [rohitkale523@gmail.com](emailid)

## synonym:4
- four

## synonym:Delhi
- New Delhi

## synonym:bangalore
- bengaluru
- Bengaluru

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:mid
- moderate

## synonym:vegetarian
- veggie
- vegg

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}
