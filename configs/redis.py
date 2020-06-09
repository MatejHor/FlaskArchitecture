import os
import redis
import subprocess
import sys

from flask_script import Command
from rq import Connection, Queue, Worker

REDIS_URL = os.getenv("REDIS_URL") or 'redis://localhost:6379'
CONNECTION = redis.from_url(REDIS_URL)
QUEUE = Queue(connection=redis.from_url(REDIS_URL))


class RedisWorker(Command):
    def run(self):
        with Connection(CONNECTION):
            qs = sys.argv[1:] or ['default']
            redis_instance = redis.Redis()
            queue = Queue('redis_queue')

            # Start a worker with a custom name
            worker = Worker([queue], connection=redis_instance, name='RedisWorker')
            worker.work()


class RedisServer(Command):
    def run(self):
        subprocess.Popen([os.path.join("bin", "redis-server")])
