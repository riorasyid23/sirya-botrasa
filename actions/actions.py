# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionRespondWisata(Action):
    def name(self):
        return 'action_respond_wisata'

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message['intent'].get('name')

        # Menambahkan prefix 'utter_' ke intent untuk mendapatkan nama respons
        response = 'utter_' + intent

        dispatcher.utter_message(template=response)

