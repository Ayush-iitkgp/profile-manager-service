import asyncio
import json
import logging

from pydantic import ValidationError

from src.db.repositories.customer import CustomerRepository
from src.db.session import async_session
from src.models.customer import InCustomerSchema

aw = asyncio.get_event_loop().run_until_complete
logger = logging.getLogger(__name__)


async def main():
    async with async_session() as db:
        with open(
            "data/customer_export.json"
        ) as file:  # TODO: Insert using the compressed file instead of the uncompressed file
            async with db.begin():
                for line in file:
                    try:
                        line = line.strip()
                        data = json.loads(line)
                        customer = InCustomerSchema(
                            customer_id=data["customer_id"],
                            email=data["email"],
                            country=data["country"],
                            language=(
                                data["language"]
                                if data.get("language") is not None
                                else None
                            ),
                        )  # TODO: Do batch insertion instead of doing one by one
                        customer_repository = CustomerRepository(db_session=db)
                        await customer_repository.create(values=customer, commit=False)
                    except ValidationError:
                        logger.warning(f"{line} is not valid JSON")
                    except Exception:  # TODO: Handle each exception individually
                        logger.warning(
                            f"Exception occurred for the record {line}", exc_info=True
                        )
        await db.commit()


# At the end of the insertion, we have around 99761 records in the table.

aw(main())
