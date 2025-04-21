from datetime import datetime

from sqlalchemy.orm import registry, Mapped, mapped_column

table_registry = registry()

@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    created_at: Mapped[datetime]