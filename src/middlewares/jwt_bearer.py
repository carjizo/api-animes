from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from utils.jwt_manager import Utils

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = Utils().validate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="Credenciales son invalidas")