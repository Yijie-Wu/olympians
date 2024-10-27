from datetime import datetime

from sqlalchemy.orm import relationship, Session
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DateTime, Text, Table

from app.extensions import Base
from app.settings import Settings

settings = Settings()

# 创建关联表
user_roles = Table(
    'user_system_roles',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('role_id', Integer, ForeignKey('system_roles.id'), primary_key=True)
)


class SystemRoles(Base):
    __tablename__ = 'system_roles'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    name = Column(String(60), unique=True)
    logo = Column(String(256), default='')
    description = Column(String(600), default='')
    create_at = Column('create_at', DateTime, default=datetime.now)
    update_at = Column('update_at', DateTime, default=datetime.now, onupdate=datetime.now)

    # 反向关系
    users = relationship('User', secondary=user_roles, back_populates='system_roles')


class Roles(Base):
    __tablename__ = 'roles'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    name = Column(String(60), unique=True)
    logo = Column(String(256), default='')
    description = Column(String(600), default='')
    create_at = Column('create_at', DateTime, default=datetime.now)
    update_at = Column('update_at', DateTime, default=datetime.now, onupdate=datetime.now)
    users = relationship('User', back_populates='role')


class User(Base):
    __tablename__ = 'user'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    nt = Column('nt', String(200), default='')
    email = Column('email', String(200), default='')
    avatar = Column('avatar', String(200), default='avatar.png')
    status = Column('status', String(200), default='空闲')
    status_info = Column('status_info', String(500), default='')
    username = Column('username', String(254), default='')
    password_hash = Column('password_hash', String(200), default='')
    last_login = Column('last_login', DateTime)
    last_login_by = Column('last_login_by', String(10))
    ldap_authed = Column('ldap_authed', Boolean, default=False)
    email_confirmed = Column('email_confirmed', Boolean, default=False)
    gitlab_authed = Column('gitlab_authed', Boolean, default=False)
    receive_email = Column('receive_email', Boolean, default=True)
    receive_system_notification = Column('receive_system_notification', Boolean, default=True)
    receive_test_notification = Column('receive_test_notification', Boolean, default=True)
    receive_bug_notification = Column('receive_bug_notification', Boolean, default=True)
    receive_article_notification = Column('receive_article_notification', Boolean, default=True)
    tokens = Column('tokens', Text, default='[]')
    created_at = Column('created_at', DateTime, default=datetime.now())
    updated_at = Column('updated_at', DateTime, default=datetime.now(), onupdate=datetime.now)
    role_id = Column('role_id', Integer, ForeignKey('roles.id'))
    role = relationship('Roles', back_populates='users')
    # 反向关系
    system_roles = relationship('SystemRoles', secondary=user_roles, back_populates='users')

    def init_role(self, db: Session):
        if self.role is None:
            if self.username.lower() == settings.APP.ADMIN_USERNAME.lower():
                self.role = db.query(Roles).filter_by(name='超级管理员').first()
            else:
                self.role = db.query(Roles).filter_by(name='普通用户').first()
            db.commit()


class Product:
    __tablename__ = 'product'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    name = Column('name', String(200))
    logo = Column('logo', String(200))
    description = Column('description', Text)
    creator_id = Column('creator_id', Integer)
    updater_id = Column('updater_id', Integer)
    created_at = Column('created_at', DateTime, default=datetime.now())
    updated_at = Column('updated_at', DateTime, default=datetime.now(), onupdate=datetime.now)


class Testcase:
    __tablename__ = 'testcase'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    creator_id = Column('creator_id', Integer)
    updater_id = Column('updater_id', Integer)
    created_at = Column('created_at', DateTime, default=datetime.now())
    updated_at = Column('updated_at', DateTime, default=datetime.now(), onupdate=datetime.now)


class TestSuits:
    __tablename__ = 'testsuits'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    creator_id = Column('creator_id', Integer)
    updater_id = Column('updater_id', Integer)
    created_at = Column('created_at', DateTime, default=datetime.now())
    updated_at = Column('updated_at', DateTime, default=datetime.now(), onupdate=datetime.now)


class TestRunner:
    __tablename__ = 'testrunner'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    creator_id = Column('creator_id', Integer)
    updater_id = Column('updater_id', Integer)
    created_at = Column('created_at', DateTime, default=datetime.now())
    updated_at = Column('updated_at', DateTime, default=datetime.now(), onupdate=datetime.now)


class Task:
    __tablename__ = 'task'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    name = Column(String(60), unique=True)
    status = Column('status', String(20), default='初始化')
    progress = Column('progress', Integer, default=0)
    message = Column('message', Text)
    details = Column('details', Text)
    logs = Column('logs', Text)
    creator_id = Column('creator_id', Integer)
    updater_id = Column('updater_id', Integer)
    created_at = Column('created_at', DateTime, default=datetime.now())
    updated_at = Column('updated_at', DateTime, default=datetime.now(), onupdate=datetime.now)


class ArticleCategory:
    __tablename__ = 'article_category'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    creator_id = Column('creator_id', Integer)
    updater_id = Column('updater_id', Integer)
    created_at = Column('created_at', DateTime, default=datetime.now())
    updated_at = Column('updated_at', DateTime, default=datetime.now(), onupdate=datetime.now)


class ArticleTag:
    __tablename__ = 'article_tag'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    creator_id = Column('creator_id', Integer)
    updater_id = Column('updater_id', Integer)
    created_at = Column('created_at', DateTime, default=datetime.now())
    updated_at = Column('updated_at', DateTime, default=datetime.now(), onupdate=datetime.now)


class Article:
    __tablename__ = 'article'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    creator_id = Column('creator_id', Integer)
    updater_id = Column('updater_id', Integer)
    created_at = Column('created_at', DateTime, default=datetime.now())
    updated_at = Column('updated_at', DateTime, default=datetime.now(), onupdate=datetime.now)


class Notification:
    __tablename__ = 'notification'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    created_at = Column('created_at', DateTime, default=datetime.now())


class Bugs:
    __tablename__ = 'bugs'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    creator_id = Column('creator_id', Integer)
    updater_id = Column('updater_id', Integer)
    created_at = Column('created_at', DateTime, default=datetime.now())
    updated_at = Column('updated_at', DateTime, default=datetime.now(), onupdate=datetime.now)


class Config(Base):
    __tablename__ = 'config'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    name = Column('name', String(100))
    content = Column('content', Text, default="{}")
    create_at = Column('create_at', DateTime, default=datetime.now)
    update_at = Column('update_at', DateTime, default=datetime.now, onupdate=datetime.now)
    creator_id = Column('creator_id', Integer)
    updater_id = Column('updater_id', Integer)
    created_at = Column('created_at', DateTime, default=datetime.now())
    updated_at = Column('updated_at', DateTime, default=datetime.now(), onupdate=datetime.now)
