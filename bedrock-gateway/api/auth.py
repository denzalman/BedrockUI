import os
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from api.settings import BEDROCK_GW_API_KEY

api_key = BEDROCK_GW_API_KEY
security = HTTPBearer()

def api_key_auth(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]):
    if credentials.credentials != api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key"
        )