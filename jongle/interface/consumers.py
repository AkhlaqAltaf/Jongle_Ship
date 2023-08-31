from channels.generic.websocket import AsyncWebsocketConsumer
import json

class NotificationConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print("In Connection Mode..........")
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        self.channel_layer.group_add(
             self.room_group_name,self.channel_name
        )
        print("After Channel Layers.....")
        await self.accept()
        print("If Accepted....")
        await self.send(text_data=json.dumps({'data': "Connected"}))
        print("If data send successfully...")

    async def disconnect(self, close_code):
        print("In Disconnect Mode..........")
        pass

    async def notify(self, event):
        print("In Notify Mode..........")
        await self.send(text_data=json.dumps(event))

    async def receive(self, text_data):
        print("In Receive Mode..........")
        pass  # Handle any additional logic here
