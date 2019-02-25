# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 21:35:03 2018
Model for user, blog, comment
@author: yanyongyu
"""
__author__ = 'yanyongyu'
from orm import Model, StringField, BooleanField, FloatField, TextField
import time, uuid

def next_id():
    return '%015d%s000' % (int(time.time()*1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'
    
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    password = StringField(ddl='varcahr(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField('varchar(500)')
    created_at = FloatField(default=time.time)
    
class Blog(Model):
    __table__ = 'blogs'
    
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)
    
class Comment(Model):
    __table__ = 'comments'
    
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)
