import asyncio

from src.db.repositories.customer import CustomerRepository
from src.db.session import async_session
from src.models.customer import InCustomerSchema

aw = asyncio.get_event_loop().run_until_complete


async def main():
    async with async_session() as db:
        with open(
            "data/customer_export.json"
        ) as file:  # TODO: Insert using the compressed file instead of the uncompressed file
            async with db.begin():
                for line in file:
                    line = line.strip()
                    print(line)
                customer = InCustomerSchema.parse_raw(
                    line
                )  # TODO: Do batch insertion instead of doing one by one
                customer_repository = CustomerRepository(db_session=db)
                await customer_repository.create(values=customer, commit=False)
            await db.commit()


aw(main())
