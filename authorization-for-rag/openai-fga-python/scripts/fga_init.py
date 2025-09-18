"""
This initializes the FGA store with the necessary tuple data
it will use the openfga_sdk and read the configuration from the .config file
"""
import asyncio
import sys
import os
# Add the parent directory to the path so we can import from helpers
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers.config import config
from openfga_sdk import ClientConfiguration, OpenFgaClient
from openfga_sdk.credentials import Credentials, CredentialConfiguration
from openfga_sdk.client.models import ClientTuple, ClientWriteRequest


async def fga_setup(config):
    fga_config = ClientConfiguration(
        api_url=config["AUTH0FGA"]["FGA_API_URL"],
        store_id=config["AUTH0FGA"]["FGA_STORE_ID"]
    ) 

    fga_client = OpenFgaClient(fga_config)
    return fga_client


async def main():
    fga_client = await fga_setup(config)
    tuple_data = {"user":"user:jess", "relation":"viewer", "object":"doc:public-doc"}
    body = ClientWriteRequest(writes=[ ClientTuple(**tuple_data) ])
    await fga_client.write(body)
    await fga_client.close()


if __name__ == "__main__":
    asyncio.run(main())