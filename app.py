import asyncio

from aiohttp import web
import aiohttp_session
import aiohttp_jinja2

import settings


async def init_app(loop):
    """Initialize app"""
    middlewares = []
    
    app = web.Application(loop=loop, middlewares=middlewares)
    app.logger = settings.logger
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