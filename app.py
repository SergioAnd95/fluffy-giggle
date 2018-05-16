import asyncio

from aiohttp import web
from aiohttp_session import session_middleware
from aiohttp_session.redis_storage import RedisStorage
import aioredis
import aiohttp_jinja2
import peewee_async

from settings import settings
from db.models import db


async def init_app(loop):
    """Initialize app"""

    redis_pool = await aioredis.create_pool(settings.REDIS, loop=loop)
    
    middlewares = [
        session_middleware(RedisStorage(redis_pool))
    ]

    db.init(**settings.DATABASE)
    app = web.Application(loop=loop, middlewares=middlewares)
    app.logger = settings.logger
    app.db = db
    app.db.set_allow_sync(False)
    app.objects = peewee_async.Manager(app.db)
    handler = app.make_handler(access_log=settings.logger)
    serv_generator = loop.create_server(handler, settings.HOST, settings.PORT)

    return serv_generator, handler, app


async def close_app():
    pass


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    serv_generator, handler, app = loop.run_until_complete(init_app(loop))
    server = loop.run_until_complete(serv_generator)

    try:
        settings.logger.debug('Start server')
        loop.run_forever()
    except KeyboardInterrupt:
        settings.logger.debug('Keyboard Interrupt ^C')
    finally:
        settings.logger.debug('Stop server begin...')
        loop.close()
        settings.logger.debug('Stop server end')