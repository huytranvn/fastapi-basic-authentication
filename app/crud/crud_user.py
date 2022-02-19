from typing import Any, Optional

from app.models.user import (
    User,
)


fake_users_db = {
    'foo': {
        'username': 'foo',
        'fullname': 'Foo User',
        'email': 'foo@example.com',
        'hashed_password': 'somepassword',
        'disabled': False
    }
}


class CRUDUser:
    def get_user(self, db: dict[str, Any], username: str) -> Optional[User]:
        if username in db:
            user_dict: dict[str, Any] = db[username]
            return User(**user_dict)

        return None

    def fake_decode_token(self, token: str) -> Optional[User]:
        # We will need to change this method in real project.
        user = self.get_user(fake_users_db, token)
        return user
