from .models import Player
from .serializers import PlayerSerializer
import json
import os

class PlayerDummyCreate:

    player_json_dummy = []

    def __init__(self):
        """Create player data dummy"""
        json_data = open(os.path.dirname(__file__)+'/DataDummy/PlayerDummy.json')
        self.player_json_dummy = json.load(json_data)
        # player_json_dummy = json.dumps(player_json_dummy)
        json_data.close()
        

    def run(self):
        Player.objects.all().delete()
        for player in self.player_json_dummy:
            # print(json.dumps(player))
            serializer = PlayerSerializer(data=player)
            if serializer.is_valid():
                print("Inserted")
                serializer.save()
            else:
                print(serializer.errors)
        Player.objects.filter(gender='M').update(gender='L')
        Player.objects.filter(gender='F').update(gender='P')

playerFactory = PlayerDummyCreate()
playerFactory.run()