'''
#测试orm用的
from orm import create_pool, select
import asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(create_pool(host='localhost', port=3306,user='root', password='password',db='test', loop=loop))
rs = loop.run_until_complete(select('select * from user',None))
#获取到了数据库返回的数据
print("heh:%s" % rs)

#测试models.py模块是否正常插入数据
import orm
from models import User, Blog, Comment
import asyncio
loop = asyncio.get_event_loop()
async def test():
    await orm.create_pool(loop,host='localhost',user='www-data', password='www-data', db='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    await u.save()


#把协程丢到事件循环中执行
loop.run_until_complete(test())
'''