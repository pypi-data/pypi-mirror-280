from typing import Optional, Union

from .api import MemberGroupApi, PermissionApi, ResourceApi, RoleApi, TenantApi
from .space_blocks_client import (
    ClientAuthenticationOptions,
    SpaceBlocksClient,
    SpaceBlocksClientOptions,
    TokenAuthenticationOptions
)

__all__ = ['PermissionsClient']


class PermissionsClient:
    _space_blocks_client: SpaceBlocksClient
    member_group_api: MemberGroupApi
    permission_api: PermissionApi
    resource_api: ResourceApi
    role_api: RoleApi
    tenant_api: TenantApi

    def __init__(
            self,
            permissions_url: str,
            authentication: Union[ClientAuthenticationOptions, TokenAuthenticationOptions],
            options: Optional[SpaceBlocksClientOptions] = None
    ):
        self._space_blocks_client = SpaceBlocksClient(permissions_url, authentication, options)

        self.member_group_api = MemberGroupApi(self._space_blocks_client.api_client)
        self.permission_api = PermissionApi(self._space_blocks_client.api_client)
        self.resource_api = ResourceApi(self._space_blocks_client.api_client)
        self.role_api = RoleApi(self._space_blocks_client.api_client)
        self.tenant_api = TenantApi(self._space_blocks_client.api_client)

    @staticmethod
    def get_access_token_from_client_credentials(
            api_key: str,
            client_id: str,
            client_secret: str,
            scopes: Optional[str] = None,
            enable_dev_mode: bool = False
    ) -> str:
        return SpaceBlocksClient.get_access_token_from_client_credentials(
            api_key, client_id, client_secret, scopes, enable_dev_mode
        )
