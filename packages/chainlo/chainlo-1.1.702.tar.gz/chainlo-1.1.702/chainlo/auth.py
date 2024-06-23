import os
from datetime import datetime, timedelta
from typing import Any, Dict

import jwt
from chainlo.config import config
from chainlo.data import get_data_layer
from chainlo.oauth_providers import get_configured_oauth_providers
from chainlo.user import User

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from keycloak import KeycloakOpenID

reuseable_oauth = OAuth2PasswordBearer(tokenUrl="/login", auto_error=False)

TOKEN_URL = os.getenv("TOKEN_URL")
SERVER_URL = os.getenv("SERVER_URL")
CLIENT_ID = os.getenv("CLIENT_ID")
REALM_NAME = os.getenv("REALM_NAME")
CLIENT_SECRET_KEY = os.getenv("CLIENT_SECRET_KEY")


oauth2_scheme = OAuth2PasswordBearer(tokenUrl=TOKEN_URL)

# Configure Keycloak instance
keycloak_openid = KeycloakOpenID(
    server_url=SERVER_URL,
    client_id=CLIENT_ID,
    realm_name=REALM_NAME,
    client_secret_key=CLIENT_SECRET_KEY,
)


def get_jwt_secret():
    return os.environ.get("CHAINLIT_AUTH_SECRET")


def ensure_jwt_secret():
    if require_login() and get_jwt_secret() is None:
        raise ValueError(
            "You must provide a JWT secret in the environment to use authentication. Run `chainlit create-secret` to generate one."
        )


def is_oauth_enabled():
    return config.code.oauth_callback and len(get_configured_oauth_providers()) > 0


def require_login():
    return (
        bool(os.environ.get("CHAINLIT_CUSTOM_AUTH"))
        or config.code.password_auth_callback is not None
        or config.code.header_auth_callback is not None
        or is_oauth_enabled()
    )


def get_configuration():
    return {
        "requireLogin": require_login(),
        "passwordAuth": config.code.password_auth_callback is not None,
        "headerAuth": config.code.header_auth_callback is not None,
        "oauthProviders": get_configured_oauth_providers()
        if is_oauth_enabled()
        else [],
    }


def create_jwt(data: User) -> str:
    to_encode = data.to_dict()  # type: Dict[str, Any]
    to_encode.update(
        {
            "exp": datetime.utcnow() + timedelta(minutes=60 * 24 * 15),  # 15 days
        }
    )
    encoded_jwt = jwt.encode(to_encode, get_jwt_secret(), algorithm="HS256")
    return encoded_jwt

async def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        print(token)
        token_info = keycloak_openid.introspect(token)
        print("Token Info")
        print(token_info)
        
        if not token_info.get('active'):
            # The token is not active, try to refresh it
            refresh_token = keycloak_openid.refresh_token(token)
            print("Refresh Token")
            print(refresh_token)
            # if refresh_token:
            #     token_info = keycloak_openid.refresh_token(refresh_token)
            #     print("Refreshed Token Info")
            #     print(token_info)
            # else:
            #     raise HTTPException(status_code=400, detail="Invalid token")
        
        user_uuid = token_info.get("sub")
        return user_uuid
    except:
        raise HTTPException(status_code=400, detail="Invalid token")

async def authenticate_user(token: str = Depends(reuseable_oauth)):
    try:
        dict = jwt.decode(
            token,
            get_jwt_secret(),
            algorithms=["HS256"],
            options={"verify_signature": False},
        )
        print("########################### authenticate_user")
        print(dict)
        if dict.get("iss") is None:
            print(dict['metadata']['provider'])
            del dict["exp"]
            # {'identifier': 'fouad.omri@predapp.com', 'metadata': {'image': '', 'provider': 'keycloak'}, 'exp': 1720378949}
            user = User(**dict)
        else:
            await verify_token(token)
            user = User(
                identifier=dict.get("email"),
                metadata={"image": "", "provider": "keycloak"},
            )   
    except Exception as e:
        print("########################### IN EXCEPTION")
        uuid = await verify_token(token)
        print("########################### UUID")
        print(uuid)
        raise HTTPException(status_code=401, detail="Invalid authentication token")
    if data_layer := get_data_layer():
        try:
            persisted_user = await data_layer.get_user(user.identifier)
            if persisted_user == None:
                persisted_user = await data_layer.create_user(user)
        except Exception as e:
            return user

        return persisted_user
    else:
        return user


async def get_current_user(token: str = Depends(reuseable_oauth)):
    if not require_login():
        return None
    print("########################### get_current_user")
    print(token)
    # return None
    return await authenticate_user(token)
