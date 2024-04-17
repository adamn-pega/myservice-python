import asyncio
import websockets

async def test():
    async with websockets.connect('ws://localhost:10000/myservice/exec') as websocket:
        print(await websocket.recv())
        print("Sending <ls> command")
        await websocket.send("<ls>")
        print(await websocket.recv())
        print("Sending <get file1.txt> command")
        await websocket.send("<get file1.txt>")
        print(await websocket.recv())
        print("Sending <get file2.txt> command")
        await websocket.send("<get file2.txt>")
        print(await websocket.recv())
        await websocket.send("<save file3.txt>")
        print(await websocket.recv())

asyncio.run(test())