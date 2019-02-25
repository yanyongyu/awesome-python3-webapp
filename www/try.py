# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 23:30:51 2018
try sql, orm
@author: yanyongyu
"""
__author__ = 'yanyongyu'
import orm, asyncio
from model import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop,user='root',password='yan011208',db='my_first_blog')
    user = User(name='Test', email='test@example.com', passwd='1234567890',image='about:blank')
    await user.save()
    
loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
