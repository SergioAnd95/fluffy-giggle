# Creating tables
# Future creating migrations

import asyncio

from app import init_app

from accounts.models import User

loop = asyncio.get_event_loop()
serv_generator, handler, app = loop.run_until_complete(init_app(loop))

with app.objects.allow_sync():
    User.create_table(True)