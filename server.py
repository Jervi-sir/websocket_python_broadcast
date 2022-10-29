import asyncio
import datetime
import random
import websockets

#send result like a UDP
async def time(websocket, name):
    while True:
        greeting = "you are a {}!".format(name)
        await websocket.send(greeting)
        # print("> {}".format(greeting))
        await asyncio.sleep(random.random() * 3)

#consume client input then
async def receive(websocket):
    name = await websocket.recv()
    # print("< client sent {}".format(name))
    print(websocket.remote_address)
    await time(websocket=websocket, name = websocket.remote_address)



start_server = websockets.serve(receive, "127.0.0.1", 5678)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
