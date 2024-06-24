from typing import Optional, Union

import urllib3
from pydantic import BaseModel, validate_call

from .api_client import ApiClient
from .configuration import Configuration

__all__ = [
    'ClientAuthenticationOptions',
    'TokenAuthenticationOptions',
    'SpaceBlocksClientOptions',
    'SpaceBlocksClient'
]


class ClientAuthenticationOptions(BaseModel):
    api_key: str
    client_id: str
    client_secret: str
    scopes: Optional[str] = None


class TokenAuthenticationOptions(BaseModel):
    api_key: str
    access_token: str


class SpaceBlocksClientOptions(BaseModel):
    enable_dev_mode: Optional[bool] = False
    custom_cloud_uri_scheme: Optional[str] = None


class SpaceBlocksClient:
    api_client: ApiClient

    @validate_call
    def __init__(
            self,
            permissions_url: str,
            authentication: Union[ClientAuthenticationOptions, TokenAuthenticationOptions],
            options: Optional[SpaceBlocksClientOptions]
    ):
        if isinstance(authentication, TokenAuthenticationOptions):
            access_token = authentication.access_token
        else:
            access_token = self.get_access_token_from_client_credentials(
                authentication.api_key,
                authentication.client_id,
                authentication.client_secret,
                authentication.scopes,
                options.enable_dev_mode if options else None
            )

        self.api_client = ApiClient(
            Configuration(host=permissions_url)
        )

        self.api_client.default_headers['Authorization'] = f'Bearer {access_token}'
        self.api_client.default_headers['apiKey'] = authentication.api_key

    @staticmethod
    def get_access_token_from_client_credentials(
            api_key: str,
            client_id: str,
            client_secret: str,
            scopes: Optional[str] = None,
            enable_dev_mode: bool = False
    ) -> str:
        space_blocks_auth_domain = 'auth.dev.spaceblocks.cloud' if enable_dev_mode else 'auth.spaceblocks.cloud'

        data = {'client_id': client_id, 'client_secret': client_secret}

        if scopes is not None:
            data['scope'] = scopes

        response = urllib3.request(
            'POST',
            f'https://{space_blocks_auth_domain}/token-manager/token',
            json=data,
            headers={'apiKey': api_key}
        )

        return response.json()['access_token']
