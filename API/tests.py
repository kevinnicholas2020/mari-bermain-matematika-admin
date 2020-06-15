from django.test import TestCase
from .models import Player
from .serializers import PlayerSerializer
import json
import os

# Create your tests here.
class PlayerDummyCreate(TestCase):

    player_json_dummy = []

    def setUp(self):
        """Create player data dummy"""
        json_data = open(os.path.dirname(__file__)+'/DataDummy/PlayerDummy.json')
        self.player_json_dummy = json.load(json_data)
        # player_json_dummy = json.dumps(player_json_dummy)
        json_data.close()
        

    def create(self):
        for player in self.player_json_dummy:
            # print(json.dumps(player))
            serializer = PlayerSerializer(data=player)
            if serializer.is_valid():
                print("Inserted")
                serializer.save()
            else:
                print(serializer.errors)
