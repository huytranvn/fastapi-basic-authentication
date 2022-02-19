from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
)
from fastapi.security import (
    OAuth2PasswordRequestForm,
)

from app.authentication.default import (
    get_current_active_user,
    fake_hash_password,
)
from app.crud.crud_user import fake_users_db
from app.models.user import User


app = FastAPI()


@app.post('/token')
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> dict[str, str] | None:
    user_dict: dict[str, str] = fake_users_db.get(form_data.username)

    if not user_dict:
        raise HTTPException(
            status_code=400,
            detail='Incorrect username or password',
        )

    user = User(**user_dict)
    hashed_password = fake_hash_password(form_data.password)

    if not hashed_password == user.hashed_password:
        raise HTTPException(
            status_code=400,
            detail='Incorrect username or password',
        )

    return {
        'access_token': user.username,
        'token_type': 'bearer',
    }


@app.get('/users/me')
async def read_users_me(current_user: User = Depends(get_current_active_user)) -> User | None:
    return current_user
