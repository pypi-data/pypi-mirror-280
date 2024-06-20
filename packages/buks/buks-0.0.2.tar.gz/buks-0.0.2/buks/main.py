from sqlmodel import Session, select
from buks.models import APIKey, QueryLog, User
from sqlalchemy.exc import NoResultFound
from datetime import datetime
from typing import Optional, Dict
import os
from dotenv import load_dotenv
from hashlib import scrypt
from sqlmodel import create_engine
from stripe import StripeClient


load_dotenv(override=True)
sqlite_url = os.getenv("DATABASE_URL")
engine = create_engine(sqlite_url, echo=True)


class Buks:
    def __init__(self):
        self.stripe = StripeClient(os.getenv("STRIPE_SECRET_KEY"))

    def log_usage(
        self, api_key: str, cost: int, label: str, details: Optional[Dict] = None
    ):
        with Session(engine) as session:
            try:
                # Find the API key record
                api_key_records = session.exec(select(APIKey)).all()

                # Verify the API key
                for record in api_key_records:
                    hashed_api_key = scrypt(
                        api_key.encode(),
                        salt=record.salt.encode(),
                        n=16384,
                        r=8,
                        p=1,
                        maxmem=0,
                        dklen=64,
                    ).hex()
                    if hashed_api_key == record.api_key:
                        api_key_record = record
                        break
                else:
                    raise NoResultFound("API key not found.")

                # Find the user associated with the API key
                user_record = session.exec(
                    select(User).where(User.user_id == api_key_record.user_id)
                ).one()

                self.stripe.billing.meter_events.create(
                    {
                        "event_name": "buks",
                        "payload": {
                            "value": cost,
                            "stripe_customer_id": user_record.customer,
                        },
                    }
                )
                # Create a new query log entry
                query_log = QueryLog(
                    query_name=label,
                    cost=cost,
                    timestamp=datetime.utcnow(),
                    details=details or {},
                    user_id=user_record.user_id,
                )

                # Add and commit the new log entry
                session.add(query_log)
                session.commit()

                print("Usage logged successfully.")
            except NoResultFound as e:
                print(e)
            except Exception as e:
                print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    logger = Buks()
    logger.log_usage(
        api_key="9b819de0267509adff869ca0d063a574f7489052645adc21f4a421b785504ef1",
        cost=100,
        label="test",
        details={"example": "data"},
    )
