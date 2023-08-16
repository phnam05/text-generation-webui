import extensions.api.blocking_api as blocking_api
import extensions.api.streaming_api as streaming_api
from modules import shared
import asyncio
import multiprocessing
import os

# Here
def runserv():
    os.system('ssh -o ServerAliveInterval=60 -R 80:127.0.0.1:5000 serveo.net')

def setup():
    blocking_api.start_server(shared.args.api_blocking_port, share=shared.args.public_api, tunnel_id=shared.args.public_api_id)
    streaming_api.start_server(shared.args.api_streaming_port, share=shared.args.public_api, tunnel_id=shared.args.public_api_id)
   # And here
    proc = multiprocessing.Process(target=runserv)
    proc.start()
