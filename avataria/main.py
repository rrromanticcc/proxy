import asyncio

class Server:
    async def start(self):
        self.server = await asyncio.start_server(
            self.open_connection, "127.0.0.1", 8123)

    async def open_connection(self, reader, writer):
        self.reader, self.writer = reader, writer
        self.client = Client(self)
        asyncio.create_task(self.client.start())
        await asyncio.sleep(0.1)
        while (reader and writer):
            data = await reader.read(8192)
            if not data:
                break
            print(data)
            await self.client.send(data)

    async def send(self, message):
        self.writer.write(message)
        await self.writer.drain()

class Client:
    def __init__(self, server):
        self.server = server

    async def start(self):
        self.reader, self.writer = await asyncio.open_connection(
            "188.124.34.19", 8123)

        while (self.reader and self.writer):
            data = await self.reader.read(8192)
            if not data:
                break
            print(data)
            await self.server.send(data)

    async def send(self, message):
        self.writer.write(message)
        await self.writer.drain()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(Server().start())
    loop.run_forever()
