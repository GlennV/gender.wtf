import json

from channels.generic.websocket import AsyncWebsocketConsumer

class GuessConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # There is only one group, join it
        await self.channel_layer.group_add(
            'one',
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave group on disconnect
        await self.channel_layer.group_discard(
            'one',
            self.channel_name
        )

    async def guess(self, event):
        # Send guess to all consumers
        await self.send(text_data=json.dumps({
            'x': event["x"],
            'y': event["y"],
            'key': event["key"],
        }))