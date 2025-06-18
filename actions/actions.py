# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker , FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted
import re

class ActionCourseDetails(Action):
    def name(self) -> Text:
        return "action_course_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        course_info = {
            "machine learning": "This course covers supervised and unsupervised learning, decision trees, SVMs, and model evaluation.",
            "deep learning": "It covers neural networks, CNNs, RNNs, and hands-on with PyTorch or TensorFlow.",
            "data mining": "You will learn clustering, association rules, and how to extract knowledge from large datasets.",
            "nlp": "Covers tokenization, POS tagging, named entity recognition, transformers, and Hugging Face libraries.",
            "optimisation for ai": "covers techniques to optimise the AI like loss fct optimisation ...",
            "game theory": "in this course you will learn normal form game and extensive form game",
            "reinforcement learning": "this course will teach you about Q learning...",
            "decision modeling:": "in this course you will learn convec function and marcov decision process"
        }

        entities = tracker.latest_message.get("entities", [])
        print(f"DEBUG entities after synonym mapping: {entities}")

        course = tracker.get_slot("course_name")
        print(f"DEBUG slot course_name: '{course}'")

        if course:
            course = course.lower().strip()
            if course in course_info:
                dispatcher.utter_message(text=f"{course.title()}: {course_info[course]}")
                return []
        
        dispatcher.utter_message(text="Sorry, I don't have details about that course yet.")
        return []
    

class ActionSayData(Action):
    def name(self) -> Text:
        return "action_say_data"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        first_name = tracker.get_slot("first_name")
        email = tracker.get_slot("email")

        print(f"DEBUG first_name: '{first_name}'")
        print(f"DEBUG email: '{email}'")
        if first_name and email:
            dispatcher.utter_message(text=f"Thanks {first_name}! We've recorded your interest and we will reserve your place in the program. We'll contact you at {email} to proceed in your application.")
        else:
            dispatcher.utter_message(text=f"Something went wrong try later")

        return []
        


class ValidateSimpleForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_simple_form"  # naming convention: lowercase with underscores

    def validate_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        
        email = slot_value
        print("🚨 VALIDATE EMAIL TRIGGERED")

        # Simple regex for validating an email
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if re.match(pattern, email):
            print(f"DEBUG valid email")
            return {"email": email}  # valid email, accept it
        else:
            print(f"DEBUG Invalid email")
            dispatcher.utter_message(text="That doesn't look like a valid email address. Could you re-enter it?")
            return {"email": None}  # reject and ask again
        


class ActionCustomFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response="utter_default")
        
        # Revert last user message so it doesn't affect the conversation
        return [UserUtteranceReverted()]
    

