# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd
from rasa_sdk.events import SlotSet

class ActionFacilitySearch(Action):

    def name(self) -> Text:
        return "action_get_salary"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        df = pd.read_csv("../data/salary_dataset.csv")
        id_ = tracker.get_slot("id")
        dep = tracker.get_slot("department")
        print(id_,dep)
        salary = df[(df["EmployeeID"].astype(int).astype(str)==str(id_))&(df["Department"]==dep)]["Salary"].values[0]
        dispatcher.utter_message(text=f"Your pay is  {salary}")

        return []
