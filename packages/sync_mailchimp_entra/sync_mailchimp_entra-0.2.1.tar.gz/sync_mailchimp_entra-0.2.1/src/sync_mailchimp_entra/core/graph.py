from azure.identity.aio import ClientSecretCredential
from msgraph import GraphServiceClient
from kiota_abstractions.api_error import APIError
from msgraph.generated.users.item.user_item_request_builder import (
    UserItemRequestBuilder,
)
from kiota_abstractions.base_request_configuration import RequestConfiguration


class GraphClient(GraphServiceClient):
    _instance = None

    @staticmethod
    def get_instance(tenant_id=None, client_id=None, secret=None, scopes=None):
        if GraphClient._instance is None or (
            tenant_id is not None
            and client_id is not None
            and secret is not None
            and scopes is not None
        ):
            if (
                tenant_id is None
                or client_id is None
                or secret is None
                or scopes is None
            ):
                raise ValueError(
                    "Tenant ID, Client ID, Secret, and Scopes must be provided for the first initialization of GraphClient."
                )
            GraphClient._instance = GraphClient(tenant_id, client_id, secret, scopes)
            print("GraphClient created.")
        return GraphClient._instance

    def __init__(self, tenant_id=None, client_id=None, secret=None, scopes=None):
        if not hasattr(self, "initialized") or not self.initialized:
            credentials = ClientSecretCredential(tenant_id, client_id, secret)
            super(GraphClient, self).__init__(credentials=credentials, scopes=scopes)
            self.initialized = True

    async def get_user(self, id):
        query_params = UserItemRequestBuilder.UserItemRequestBuilderGetQueryParameters(
            select=["givenName", "surname", "companyName"],
        )

        request_configuration = RequestConfiguration(
            query_parameters=query_params,
        )

        try:
            return (
                await self.get_instance()
                .users.by_user_id(id)
                .get(request_configuration=request_configuration)
            )
        except APIError as e:
            print(f"Error: {e.error.message}")

    async def get_group_members(self, group_id):
        try:
            return await self.get_instance().groups.by_group_id(group_id).members.get()
        except APIError as e:
            print(f"Error: {e.error.message}")

    async def list_entra_emails(self, group_id):
        users = await self.get_group_members(group_id)
        members_entra_emails = []
        for user in users.value:
            members_entra_emails.append(user.user_principal_name)

        return members_entra_emails
