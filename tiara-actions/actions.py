# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import requests
from rasa_sdk import Action
from rasa_sdk.events import SlotSet


class GetTodaysHoroscope(Action):
    def name(self):
        return "get_todays_horoscope"

    def run(self, dispatcher, tracker, domain):
        user_horoscope_sign = tracker.get_slot('horoscope_sign')
        base_url = 'http://horoscope-api.herokuapp.com/horoscope/{day}/{sign}'
        url = base_url.format(**{'day': "today", 'sign': user_horoscope_sign})
        res = requests.get(url)
        todays_horoscope = res.json()['horoscope']
        response = "Your today's horoscope:\n{}".format(todays_horoscope)

        dispatcher.utter_message(response)
        return [SlotSet("horoscope_sign", user_horoscope_sign)]


class GetRandomMathFact(Action):
    def name(self):
        return "get_random_mathfact"

    def run(self, dispatcher, tracker, domain):
        res = requests.get("http://numbersapi.com/random/year?json")
        fact = res.json()['text']
        response = "The fact is:\n{}".format(fact)

        dispatcher.utter_message(response)
        return []


