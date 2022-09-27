# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import datetime as dt
from email import message
from html import entities
from typing import Any, Text, Dict, List
from database.Database import Database
from database.Subject import Subject
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import webbrowser
import requests
import smtplib, ssl
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

def send_mail(message, subject):
    sender_email = "wirtualnydziekanat2022@gmail.com"
    receiver_email = "weitichatbot@gmail.com"
    password = "bjxgyfgiifotttfp"
    port = 465  # For SSL
    msg = MIMEMultipart()
    # msg.set_content(message)
    msg.attach(MIMEText(message, 'plain', 'iso 8859-2'))
    now = datetime.now()
    msg['Subject'] = 'Brak intencji ' + now.strftime("%H:%M:%S")
    msg['From'] = sender_email
    msg['To'] = receiver_email

    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(sender_email, password)
    smtpserver.sendmail(sender_email, receiver_email, msg.as_string())


class ActionPokazCzas(Action):

    def name(self) -> Text:
        return "action_pokaz_czas"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=f"{dt.datetime.now()}")

        return []
class ActionPokazGodzinyOtwarciaDziekanatuTeraz(Action):

    def name(self) -> Text:
        return "action_pokaz_godziny_otwarcia_dziekanatu_teraz"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        switcher = {
            0: "Dzisiaj dziekanat jest czynny dla studentów w następujących godzinach: 12.00 - 15.00",
            1: "Dzisiaj dziekanat jest czynny dla studentów w następujących godzinach: 12.00 - 15.00",
            2: "Dzisiaj dziekanat jest nieczynny dla studentów",
            3: "Dzisiaj dziekanat jest czynny dla studentów w następujących godzinach: 12.00 - 15.00",
            4: "Dzisiaj dziekanat jest czynny dla studentów w następujących godzinach: 9.00 - 12.00",
        }

        dispatcher.utter_message(text=switcher.get(dt.datetime.now().weekday(), "Dzisiaj dziekanat jest nieczynny"))

        return []
class ActionPokazFilm(Action):

    def name(self) -> Text:
        return "action_pokaz_film"

    async def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        video_url="https://www.youtube.com/watch?v=G5PiaLphvdA&ab_channel=PolitechnikaWarszawska"
        dispatcher.utter_message("proszę czekać... trwa uruchamianie filmu")
        webbrowser.open(video_url)
        return []
class ActionGdzieWydzial(Action):

    def name(self) -> Text:
        return "action_gdzie_wydzial"

    async def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        video_url="https://www.google.pl/maps/place/Wydzia%C5%82+Elektroniki+i+Technik+Informacyjnych,+Politechnika+Warszawska/@52.2189181,21.0113078,298m/data=!3m1!1e3!4m5!3m4!1s0x471ecce91dd158b3:0x188bc853d7b6b561!8m2!3d52.2190346!4d21.0118585"
        dispatcher.utter_message("https://www.google.pl/maps/place/Wydzia%C5%82+Elektroniki+i+Technik+Informacyjnych,+Politechnika+Warszawska/@52.2189181,21.0113078,298m/data=!3m1!1e3!4m5!3m4!1s0x471ecce91dd158b3:0x188bc853d7b6b561!8m2!3d52.2190346!4d21.0118585")
        # webbrowser.open(video_url)
        return []
class ActionAktualnaPogoda(Action):

    def name(self) -> Text:
        return "action_aktualna_pogoda"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_key = "JBOP9BqZ362ajGKygFfM0r0bcrr8IoGA"
        base_url = "http://dataservice.accuweather.com/currentconditions/v1/274663?"
        complete_url = base_url + "apikey=" + api_key + "&language=pl-pl&details=false HTTP/1.1"
        response = requests.get(complete_url)
        x = response.json()

        current_temperature = x[0]['Temperature']['Metric']['Value']
        current_condition = x[0]['WeatherText']
        dispatcher.utter_message(text=f"Obecna pogoda w okolicach wydziału: {current_condition} , temperatura: {current_temperature} °C")

        return []

class ActionSearchSubjects(Action):

    def name(self) -> Text:
        return "action_search_subjects"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        for e in entities:
            if e['entity'] == 'subject':
                code = e['value']
                db = Database()
                subjects = db.get_subjects_by_code(code)
                amount_of_subjects = db.get_number_of_subjects_by_code(code)
                if amount_of_subjects == 0:
                    dispatcher.utter_message("Nie znaleziono żadnych przedmiotów")
                else:
                    dispatcher.utter_message("Liczba znalezionych przedmiotów: " + str(amount_of_subjects))
                    for subject in subjects:
                        text="Nazwa przedmiotu: " + subject[1] + "\nKod przedmiotu: " + subject[0] + "\nLiczba punktów ECTS: " + str(subject[3]) + "\nOpis przedmiotu: " + subject[2] + "\n"
                        dispatcher.utter_message(text)
                    return []

        dispatcher.utter_message("Nie znaleziono żadnych przedmiotów")
        return []

class ActionNoResponses(Action):

    def name(self) -> Text:
        return "action_no_response"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = tracker.latest_message['text']
        message = message.encode('iso 8859-2', 'ignore').decode('iso 8859-2')
        dispatcher.utter_message("Nie zrozumiałem, czy możesz zadać to pytanie w inny sposób")
        send_mail(message, 'Error')
        return []
