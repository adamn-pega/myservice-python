import asyncio
import websockets

mem = ['file1.txt', 'file2.txt']
data = [
"""
This is file1 content
# comments starts with #
data1 = "###"
""",
"""
This is file2 content
data2 = "ddd#"
"""
]

# create handler for each connection
async def exec(ws, p):
    await ws.send("Hello")
    async for m in ws:
        print('command: ' + m)
        if m == "<ls>":
            files = ""
            for f in mem:
                if len(files) == 0:
                    files += f
                else:
                    files += ", " + f
            await ws.send(files)
        elif m.startswith("<get "):
            file = m.split("<get ")[1][:-1]
            d = ""
            for l in data[mem.index(file)].split('\n'):
                if l.startswith("#"):
                    pass
                else:
                    d += l + "\n"
            await ws.send(d)
        else:
            await ws.send("<unknown command>")


class ServerProtocol(websockets.WebSocketServerProtocol):
    async def process_request(self, p, rh):
        if rh['Upgrade'] != 'websocket':
            return 400, [], b'Bad Request.\n'
        if p != '/myservice/exec':
            return 400, [], b'Bad Request.\n'
        
    
print('Server is running on port 10000')
start_server = websockets.serve(exec, "localhost", 10000, create_protocol=ServerProtocol)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()