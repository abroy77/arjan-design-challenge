from datetime import datetime
from typing import Any, Protocol

from models import Event, Ticket


class NoAvailableTickets(Exception):
    pass


class NotFoundError(Exception):
    pass

class EventAlreadyStarted(Exception):
    pass

class EventCreate(Protocol):
    title: str
    location: str
    start_date: datetime
    end_date: datetime
    available_tickets: int

    def dict(self) -> dict[str, Any]:
        ...


class TicketCreate(Protocol):
    event_id: int
    customer_name: str
    customer_email: str

    def dict(self) -> dict[str, Any]:
        ...

class TicketUpdate(Protocol):
    customer_name: str | None = None



class Database(Protocol):
    def add(self, instance: object, _warn: bool = True) -> None:
        ...

    def commit(self) -> None:
        ...

    def delete(self, instance: object) -> None:
        ...

    def query(self, instance: object) -> Any:
        ...

    def refresh(self, instance: object) -> None:
        ...


def create_event(event: EventCreate, database: Database) -> Event:
    db_event = Event(**event.dict())
    database.add(db_event)
    database.commit()
    database.refresh(db_event)
    return db_event


def delete_event(event_id: int, database: Database) -> Event:
    event = get_event(event_id, database)
    if not event:
        raise NotFoundError(f"Event with id {event_id} not found.")
    if event.started:
        raise EventAlreadyStarted(f"Event with id {event_id} has already started.")
    
    tickets = get_tickets_for_event(event_id, database)
    for ticket in tickets:
        database.delete(ticket)
    database.delete(event)
    database.commit()
    return event

def get_tickets_for_event(event_id: int, database: Database) -> list[Ticket]:
    tickets = database.query(Ticket).filter(Ticket.event_id == event_id).all()
    return tickets

def get_event(event_id: int, database: Database) -> Event:
    event = database.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise NotFoundError(f"Event with id {event_id} not found.")
    return event


def get_all_events(database: Database) -> list[Event]:
    events = database.query(Event).all()
    return events


def book_ticket(ticket: TicketCreate, database: Database) -> Ticket:
    event = get_event(ticket.event_id, database)
    if not event:
        raise NotFoundError(f"Event with id {ticket.event_id} not found.")
    if event.available_tickets < 1:
        raise NoAvailableTickets()

    db_ticket = Ticket(**ticket.dict())
    database.add(db_ticket)
    database.commit()
    database.refresh(db_ticket)

    event.available_tickets -= 1
    database.commit()
    database.refresh(db_ticket)

    return db_ticket


def get_ticket(ticket_id: int, database: Database) -> Ticket:
    ticket = database.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise NotFoundError(f"Ticket with id {ticket_id} not found.")
    return ticket

def delete_ticket(ticket_id: int, database: Database) -> Ticket:
    ticket = get_ticket(ticket_id, database)
    if not ticket:
        raise NotFoundError(f"Ticket with id {ticket_id} not found.")    
    
    event = get_event(ticket.event_id, database)
    if not event:
        raise NotFoundError(f"Event with id {ticket.event_id} not found.")
    if event.started:
        raise EventAlreadyStarted(f"Event with id {ticket.event_id} has already started.")
    
    event.available_tickets += 1
    database.delete(ticket)
    database.commit()
    return ticket
def update_ticket(ticket_id: int, update_ticket: TicketUpdate, database: Database) -> Ticket:
    ticket = get_ticket(ticket_id, database)
    if not ticket:
        raise NotFoundError(f"Ticket with id {ticket_id} not found.")
    event = get_event(ticket.event_id, database)
    if not event:
        raise NotFoundError(f"Event with id {ticket.event_id} not found.")
    if event.started:
        raise EventAlreadyStarted(f"Event with id {ticket.event_id} has already started.")
    
    if update_ticket.customer_name:
        ticket.customer_name = update_ticket.customer_name



    database.commit()
    database.refresh(ticket)
    return ticket