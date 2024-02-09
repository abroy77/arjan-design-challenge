from sqlalchemy import create_engine, Engine, ForeignKey
from datetime import datetime
from sqlalchemy.orm import (
    DeclarativeBase,
    mapped_column,
    Mapped,
    relationship)
from pathlib import Path


DB_PATH = Path("/Users/abhishekroy/code/arjan-design-challenge/"
               "challenge_22_sql_to_orm/events.db")


class Base(DeclarativeBase):
    pass


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    location: Mapped[str] = mapped_column(nullable=False)
    start_date: Mapped[datetime] = mapped_column(nullable=False)
    end_date: Mapped[datetime] = mapped_column(nullable=False)
    available_tickets: Mapped[int]


class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"), nullable=False)
    customer_name: Mapped[str] = mapped_column(nullable=False)
    customer_email: Mapped[str] = mapped_column(nullable=False)


def get_engine(path: Path = DB_PATH):
    return create_engine(f"sqlite:///{path}")


def reset_db(engine: Engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def main():
    engine = get_engine()
    reset_db(engine)

    return


if __name__ == "__main__":
    main()
