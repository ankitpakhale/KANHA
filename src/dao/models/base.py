from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, DateTime
from datetime import datetime, timedelta, timezone
import uuid
from config import GeneralConfig


class BaseModel(DeclarativeBase):
    """
    Base Class For Declarative Models.
    All model classes should inherit from this base class.
    """

    id = Column(
        UUID(as_uuid=True) if GeneralConfig.ENV in ["local", "dev"] else String(36),
        primary_key=True,
        default=uuid.uuid4,  # generate a UUID automatically for new records
    )

    created_at = Column(
        DateTime,
        default=lambda: datetime.now(
            timezone(timedelta(hours=5, minutes=30))
        ),  # use IST (UTC +5:30)
        nullable=False,
    )

    # # updated_at & deleted_at FIELDS ARE NOT REQUIRED AT THIS MOMENT
    # updated_at = Column(
    #     DateTime,
    #     default=lambda: datetime.now(timezone.utc),  # set default UTC time on creation
    #     # update this field when the record is modified
    #     onupdate=lambda: datetime.now(timezone.utc),
    #     nullable=False
    # )

    # deleted_at = Column(
    #     DateTime,
    #     nullable=True,  # can be null if the record is not soft-deleted
    #     default=None
    # )

    # def soft_delete(self, session):
    #     """
    #     Marks the record as deleted by setting the `deleted_at` timestamp.
    #     This is a convenience method for soft-deleting records.
    #     """
    #     self.deleted_at = datetime.now(timezone.utc)
    #     session.commit()
