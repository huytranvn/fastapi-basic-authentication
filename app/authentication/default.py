from fastapi import (
    Depends,
    HTTPException,
    status,
)
from fastapi.security import (
    OAuth2PasswordBearer,
)

from app.crud.crud_user import CRUDUser
from app.models.user import User


# We might need to change the token later.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
crud_user = CRUDUser()


def fake_hash_password(password: str) -> str:
    return 'fakehashed' + password


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User | None:
    user = crud_user.fake_decode_token(token=token)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid authentication credentials',
            headers={'WWW-Authenticate': 'Bearer'},
        )

    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)) -> User | None:
    if current_user.disabled:
        raise HTTPException(
            status_code=400,
            detail='Inactive user',
        )

    return current_user
