from sqlalchemy.orm import Session
from fastapi import Request, Depends, HTTPException

from app.extensions import get_rdbms
from app.response import ResponseException
from app.models import User, Roles
from app.utils.password import hash_password, verify_password
from app.schemas.user.user import User as UserSchema, UserProfile, ChangePassword, UserAdd, UserEdit, ChangePassword, ChangeAvatar
from app.utils.token import extract_token


def get_current_user(request: Request, db: Session = Depends(get_rdbms)) -> dict:
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    if not token:
        raise ResponseException.HTTP_401_UNAUTHORIZED
    try:
        username = extract_token(token)
        user = db.query(User).filter_by(username=username).first()
        if user is None:
            raise ResponseException.HTTP_401_UNAUTHORIZED
        else:
            return {
                'id': user.id,
                'nt': user.nt,
                'role': user.role.name,
                'email': user.email,
                'avatar': user.avatar,
                'status': user.status,
                'username': user.username,
                'status_info': user.status_info,
                'last_login': user.last_login,
                'last_login_by': user.last_login_by,
                'ldap_authed': user.ldap_authed,
                'email_confirmed': user.email_confirmed,
                'gitlab_authed': user.gitlab_authed,
                'receive_email': user.receive_email,
                'receive_system_notification': user.receive_system_notification,
                'receive_test_notification': user.receive_test_notification,
                'receive_bug_notification': user.receive_bug_notification,
                'receive_article_notification': user.receive_article_notification,
                'created_at': user.created_at,
                'updated_at': user.updated_at,
                'system_roles': user.system_roles
            }

    except Exception as e:
        print(e)
        raise ResponseException.HTTP_401_UNAUTHORIZED


def get_admin_user(request: Request, db: Session = Depends(get_rdbms)) -> dict:
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    if not token:
        raise ResponseException.HTTP_401_UNAUTHORIZED
    try:
        username = extract_token(token)
        user = db.query(User).filter_by(username=username).first()
        if user is None:
            raise ResponseException.HTTP_401_UNAUTHORIZED
        else:
            role = db.query(Roles).filter_by(id=user.role_id).first()
            if role.name == '超级管理员':
                return {
                    'id': user.id, 'username': user.username,
                    'role': role.name, 'avatar': user.avatar
                }
            else:
                return ResponseException.HTTP_403_FORBIDDEN

    except Exception as e:
        print(e)
        raise ResponseException.HTTP_401_UNAUTHORIZED


def get_users(db: Session = Depends(get_rdbms)):
    users = db.query(User).all()

    return [
        {
            'id': user.id,
            'username': user.username,
            'role': db.query(Roles).filter_by(id=user.role_id).first().name,
            'role_id': user.role_id,
            'avatar': user.avatar,
            'created_at': user.created_at,
            'updated_at': user.updated_at
        }
        for user in users
    ]


def updateUserProfile(upf: UserProfile, user: UserSchema, db: Session):
    user_db = db.query(User).filter_by(username=user.get('username')).first()
    user_db.email = upf.email
    user_db.username = upf.username
    user_db.bio = upf.bio
    db.commit()
    db.refresh(user_db)

    return {
        'id': user_db.id,
        'username': user_db.username,
        'role': db.query(Roles).filter_by(id=user_db.role_id).first().name,
        'avatar': user_db.avatar,
        'role_id': user.role_id,
        'created_at': user_db.created_at,
        'updated_at': user_db.updated_at
    }


def changePassword(cp: ChangePassword, user: UserSchema, db: Session):
    user_db = db.query(User).filter_by(username=user.get('username', '')).first()
    if cp.new_password != cp.confirm_password:
        raise HTTPException(status_code=400, detail='两次密码输入不一致')

    if not verify_password(user_db.password_hash, cp.old_password):
        raise HTTPException(status_code=400, detail='原始密码错误')

    user_db.password_hash = hash_password(cp.new_password)
    db.commit()
    db.refresh(user_db)

    return {'detail': '重设密码成功'}


def addNewUser(cp: UserAdd, db: Session):
    user_db = db.query(User).filter_by(username=cp.username).first()
    if user_db:
        raise HTTPException(status_code=400, detail='用户名已经存在')

    new_user = User(username=cp.username, role_id=cp.role_id, password_hash=hash_password('Passw0rd!'))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def updateUserProfile(cp: UserProfile, user: UserSchema, db: Session):
    if user.get('username', '').strip().lower() == 'root':
        raise HTTPException(status_code=400, detail='用户名root不能修改')

    if cp.username.strip().lower() == 'root':
        raise HTTPException(status_code=400, detail='用户名不能为root, 不区分大小写')

    user_db = db.query(User).filter_by(id=cp.user_id).first()
    if not user_db:
        raise HTTPException(status_code=400, detail='用户不存在')
    else:
        user_db.username = cp.username
        db.commit()
        return user_db


def changePassword(cp: ChangePassword, user: UserSchema, db: Session):
    user_db = db.query(User).filter_by(username=user.get('username')).first()
    if not user_db:
        raise HTTPException(status_code=400, detail='用户不存在')

    if cp.old_password != cp.confirm_password:
        raise HTTPException(status_code=400, detail='两次密码不一致')

    if verify_password(user_db.password_hash, cp.old_password):
        raise HTTPException(status_code=400, detail='原始米密码错误')

    user_db.password_hash = hash_password(cp.new_password)
    db.commit()
    db.refresh(user_db)

    return {'detail': '更新密码成功'}


def changeAvatar(cp: ChangeAvatar, user: UserSchema, db: Session):
    user_db = db.query(User).filter_by(username=user.get('username')).first()
    if not user_db:
        raise HTTPException(status_code=400, detail='用户不存在')

    user_db.avatar = cp.avatar
    db.commit()
    db.refresh(user_db)

    return {'avatar': cp.avatar}


def editUser(id: int, cp: UserEdit, user: UserSchema, db: Session):
    user_db = db.query(User).filter_by(id=id).first()
    if not user_db:
        raise HTTPException(status_code=400, detail='用户不存在')

    user_check = db.query(User).filter_by(username=cp.username).first()
    if user_check and user_db.username != cp.username:
        raise HTTPException(status_code=400, detail='用户名已经存在')

    if cp.username.strip().lower() == 'root':
        raise HTTPException(status_code=400, detail='用户名不能为root, 不区分大小写')

    user_db.avatar = cp.avatar
    user_db.username = cp.username
    user_db.role_id = cp.role_id
    db.commit()
    db.refresh(user_db)

    return {
        'id': user_db.id,
        'username': user_db.username,
        'role': db.query(Roles).filter_by(id=user_db.role_id).first().name,
        'avatar': user_db.avatar,
        'role_id': user_db.role_id,
        'created_at': user_db.created_at,
        'updated_at': user_db.updated_at
    }
