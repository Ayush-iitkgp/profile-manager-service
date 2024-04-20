import asyncio
import json
from datetime import datetime
from src.db.repositories.customer import CustomerRepository
from src.models.customer import InCustomerSchema
from src.db.session import async_session

aw = asyncio.get_event_loop().run_until_complete


async def main():
    with open('data/customer_export.json') as file:  # TO DO: Insert using the compressed file instead of the uncompressed file
        data = json.load(file)
        async with async_session() as db:
            async with db.begin():
                customer_repository = CustomerRepository(db_session=db)
                customer_data = data["pnl"]["MXN"]
                customer = InCustomerSchema(currency_code=customer_data["currency"])
                await customer_repository.create(values=customer, commit=False)

                await db.commit()

aw(main())