from fastapi import FastAPI, HTTPException
from models import Event, Ticket, get_engine, reset_db
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime
import uvicorn
app = FastAPI()

DB_ENGINE = get_engine()
# Information needed to create an event


class EventCreate(BaseModel):
    title: str
    location: str
    start_date: str
    end_date: str
    available_tickets: int


# Information needed to create a ticket
class TicketCreate(BaseModel):
    event_id: int
    customer_name: str
    customer_email: str


@app.post("/events")
async def create_event(event_create: EventCreate):
    with Session(DB_ENGINE) as session:
        title = event_create.title
        location = event_create.location
        start_date: datetime = datetime.strptime(event_create.start_date)
        end_date: datetime = datetime.strptime(event_create.end_date)
        available_tickets = event_create.available_tickets

        new_event = Event(
            title=title,
            location=location,
            start_date=start_date,
            end_date=end_date,
            available_tickets=available_tickets

        )

        session.add(new_event)
        session.commit()
        return


@app.delete("/events/{event_id}")
def delete_event(event_id: int):
    with Session(DB_ENGINE) as session:
        event = session.scalar(select(Event).where(Event.id == event_id))
        session.delete(event)
        session.commit()
        return


@app.get("/events/{event_id}")
async def get_event(event_id: int):
    with Session(DB_ENGINE) as session:
        event = session.scalar(select(Event).where(Event.id == event_id))
        return event


@app.get("/events")
async def get_events():
    with Session(DB_ENGINE) as session:
        events: list[Event] = session.scalars(select(Event)).all()
        return events


@app.post("/tickets")
async def book_ticket(ticket_create: TicketCreate):
    # first get the event
    with Session(DB_ENGINE) as session:
        event = session.scalar(select(Event).where(Event.id == ticket_create.event_id))

        if event is None:
            raise HTTPException(status_code=404,
                                detail=f"Event with event id: {ticket_create.event_id} not found")

        if event.available_tickets < 1:
            raise HTTPException(status_code=404, detail=f"No tickets available for event id {ticket_create.event_id}")

        # make ticket
        ticket = Ticket(
            customer_name=ticket_create.customer_name,
            customer_email=ticket_create.customer_email,
            event_id=ticket_create.event_id
        )
        session.add(ticket)
        # update availability
        event.available_tickets -= 1

        session.commit()


@app.get("/tickets")
async def get_ticket(ticket_id: int):
    with Session(DB_ENGINE) as session:
        ticket = session.scalar(select(Ticket).where(Ticket.id == ticket_id))
        return ticket


def main():
    reset_db(DB_ENGINE)
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
