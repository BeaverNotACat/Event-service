import uuid
from functools import lru_cache

import httpx
from fastapi import Header, HTTPException
from pydantic import TypeAdapter

from src.schemas.auth import UserProfileSchema, UserProfileSchemaId, UserSchema
from src.settings import get_settings


class AuthService:
    scheme_url = get_settings().auth_service_url
    headers = {"Content-Type": "application/json"}

    async def get_user(self, id: uuid.UUID) -> UserProfileSchema:
        response = httpx.post(
            self.scheme_url + "/api/v1/auth/authenticateId",
            headers=self.headers,
            json={"id": str(id)},
        )

        if not response.is_success:
            raise HTTPException(status_code=500, detail="Auth serivce error")

        return UserProfileSchema.parse_raw(response.text)

    async def get_users_list(self, ids: list[uuid.UUID]) -> list[UserProfileSchema]:
        users = [{"id": str(id)} for id in ids]
        response = httpx.post(
            self.scheme_url + "/api/v1/auth/userList",
            headers=self.headers,
            json={
                "users": users,
            },
        )
        if not response.is_success:
            raise HTTPException(status_code=500, detail="Auth serivce error")

        return TypeAdapter(list[UserProfileSchema]).validate_json(response.text)

    async def authenticate(self, token: str) -> UserSchema:
        response = httpx.post(
            self.scheme_url + "/api/v1/auth/authenticateToken",
            headers=self.headers,
            json={"token": token},
        )

        if not response.is_success:
            raise HTTPException(status_code=500, detail="Auth serivce error")

        return UserSchema.parse_raw(response.text)

    async def check_token(self, token: str = Header("")) -> UserProfileSchemaId:
        user_id = (await self.authenticate(token)).id

        return UserProfileSchemaId.parse_obj(
            (await self.get_user(user_id)).dict() | {"id": user_id}
        )


@lru_cache
def get_auth_service():
    return AuthService()
