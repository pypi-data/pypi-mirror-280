from json import JSONDecodeError
from fastapi import HTTPException
import jwt
import requests
from starlette import status
from fastapi_keycloak import FastAPIKeycloak
from fastapi_keycloak.exceptions import KeycloakError


def return_secret(key: str):
    formated_key = f'-----BEGIN PUBLIC KEY-----\n{key}\n-----END PUBLIC KEY-----'
    return bytes(formated_key, "utf-8")


def logout_admin(idp: FastAPIKeycloak, access_token: str,  key: str, algorithm: str):

    #admin_token = get_admin_token(idp)

    payload = jwt.decode(access_token, key, audience="account", algorithms=[algorithm])

    username: str = payload.get('name')
    if username is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Could not validate user.')
    
    url = f'{idp.server_url}/admin/realms/{idp.realm}/users/{payload.get('sub')}/logout'

    headers = {
            "Content-Type": 'application/json',
            "Authorization": f"Bearer {idp.admin_token}",
        }

    requests.post(url=url, headers=headers)


def get_admin_token(idp: FastAPIKeycloak):
        
    token_url = f'{idp.server_url}/realms/{idp.realm}/protocol/openid-connect/token'
        
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "client_id": idp.admin_client_id,
        "client_secret": idp.admin_client_secret,
        "grant_type": "client_credentials",
    }
    response = requests.post(url=token_url, headers=headers, data=data, timeout=10)

    try:
        response.json()["access_token"]
    except JSONDecodeError as e:
        raise KeycloakError(
            reason=response.content.decode("utf-8"),
            status_code=response.status_code,
        ) from e

    except KeyError as e:
        raise KeycloakError(
            reason=f"The response did not contain an access_token: {response.json()}",
            status_code=403,
        ) from e
        

def send_verify_email(idp:FastAPIKeycloak, access_token: str, key: str, algorithm: str):
    
    payload = jwt.decode(access_token, key, audience="account", algorithms=[algorithm])

    username: str = payload.get('name')
    
    if username is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Could not validate user.')
    
    send_email_url = f'{idp.server_url}/admin/realms/{idp.realm}/users/{payload.get('sub')}/send-verify-email'

    headers = {
            "Content-Type": 'application/json',
            "Authorization": f"Bearer {idp.admin_token}",
        }

    requests.put(url=send_email_url, headers=headers)



def recover_password_email(idp:FastAPIKeycloak, email:str):

    user = idp.get_user(email=email)

    user_id = user.id

    send_email_url = f'{idp.server_url}/admin/realms/{idp.realm}/users/{user_id}/execute-actions-email'

    data = ["UPDATE_PASSWORD"]
    
    headers = {
            "Content-Type": 'application/json',
            "Authorization": f"Bearer {idp.admin_token}",
        }
    
    requests.put(url=send_email_url, headers=headers, data=data)
