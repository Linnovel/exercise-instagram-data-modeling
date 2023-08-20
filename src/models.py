import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    gender = Column(String(20), nullable=False)
    bio = Column(String(60), nullable=False)
    profile_picture = Column(String(50), nullable=True)

    post = relationship("post", back_populates="user", lazy=True)
    story = relationship("story", back_populates="user", lazy=True)
    comment = relationship("comment", back_populates="user", lazy=True)



class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    description = Column(String(500), nullable=False)
    date = Column(String(10), nullable=False)
    like = Column(Integer, nullable=False)
    comments = Column(String(250), nullable=False)

    comment = relationship("comment", back_populates="post", lazy=True)
    post = relationship("post", back_populates="user", lazy=True)
    user = relationship("user", back_populates="post", lazy=True)

class Story(Base):
    __tablename__ = 'story'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    caption = Column(String(250), nullable=False)
    image_or_videos = Column(String(250), nullable=False)
    created_at = Column(Integer, nullable=False)

    comment = relationship("comment", back_populates="story", lazy=True)
    post = relationship("post", back_populates="story", lazy=True)
    user = relationship("user", back_populates="story", lazy=True)
    

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"), nullable=False)
    story_id = Column(Integer, ForeignKey("story.id"), nullable=False)
    text = Column(String(250), nullable=False)


    

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
