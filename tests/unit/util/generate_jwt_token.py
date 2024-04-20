import asyncio

from src.util.create_jwt_token import create_access_token


async def main():
    print(await create_access_token(customer_id="06c2acac-7810-4dd8-8722-54bdb05fb9e4"))


aw = asyncio.get_event_loop().run_until_complete
aw(main())
