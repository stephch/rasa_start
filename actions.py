# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
import html
from rasa_core_sdk import Action
from rasa_core_sdk.events import BotUttered



logger = logging.getLogger(__name__)


class ActionJoke(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_joke"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        r = requests.get('http://api.icndb.com/jokes/random').json() #make an apie call
        joke = html.unescape(r['value']['joke'])
        #extract a joke from returned json response
        dispatcher.utter_message(joke) #send the message back to the user
        return [BotUttered(text = joke)]
