from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from backend.database.base import Base


class Campaign(Base):

    __tablename__ = "campaigns"

    id: Mapped[int] = mapped_column(primary_key=True)

    code: Mapped[str] = mapped_column(
        String(20),
        unique=True
    )

    name: Mapped[str] = mapped_column(
        String(100)
    )