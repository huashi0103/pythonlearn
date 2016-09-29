import orm
from models import User,Blog,Comment
import asyncio
import sys


async def test(loop):
    await orm.create_pool(loop,user='www_data',password='www_data',db='awesome')
    u=User(name='Test',email='test@example.com',passwd='123456',image='about:blank')
    await u.save()


loop=asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
if loop.is_closed():
    sys.exit(0)
