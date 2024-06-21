from collections.abc import Generator
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.database import engine
from .database import schemas, tables

from .services.auth import decode_access_token


def get_database_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


def get_oauth_scheme():
    return OAuth2PasswordBearer(
        tokenUrl="/auth/login",
        scopes={
            "su": "Super user",

            "auth:me": "Read and update information about the current user.",

            "role:list": "Read information about roles.",
            "role:info": "Read information about one role.",
            "role:create": "Create new role.",
            "role:update": "Update role.",
            "role:delete": "Delete role.",

            "user:list": "Read information about users.",
            "user:info": "Read information about one user.",
            "user:create": "Create new user.",
            "user:update": "Update user.",
            "user:delete": "Delete user.",

            "user_has_role:list": "Read information about user roles.",
            "user_has_role:info": "Read information about one user role.",
            "user_has_role:create": "Create user role.",
            "user_has_role:delete": "Delete user role.",

            "device:list": "Read information about devices.",
            "device:info": "Read information about one device.",
            "device:create": "Create new device.",
            "device:update": "Update device.",
            "device:delete": "Delete device.",

            "user_has_device:list": "Read information about user devices.",
            "user_has_device:info": "Read information about one user device.",
            "user_has_device:create": "Create user device",
            "user_has_device:delete": "Delete user device.",
        }
    )


databaseSession = Annotated[Session, Depends(get_database_session)]
tokenDependency = Annotated[str, Depends(get_oauth_scheme())]


async def get_current_user(
        db: databaseSession,
        security_scopes: SecurityScopes,
        token: tokenDependency,
):
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = "Bearer"
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )
    try:
        payload = decode_access_token(token)
        user_id: int = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
        token_scopes = payload.get("scopes", [])
        token_data = schemas.AuthTokenData(user_id=user_id, scopes=token_scopes)
    except Exception:
        raise credentials_exception

    stmt = (
        select(tables.User)
        .where(tables.User.deleted_at.is_(None))
        .where(tables.User.id.__eq__(token_data.user_id))
    )
    user = db.scalars(stmt).one_or_none()

    if user is None:
        raise credentials_exception
    for security_scope in security_scopes.scopes:
        if (security_scope not in token_data.scopes) and ("su" not in token_data.scopes):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": authenticate_value},
            )
    user.scopes = token_data.scopes
    return user
