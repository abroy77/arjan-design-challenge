
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import Ticket,Event, Base


app = FastAPI()

engine = create_engine("sqlite:///./events.db")

Session = sessionmaker(bind=engine)

# Information needed to create an event
class EventCreate(BaseModel):
    title: str
    location: str
    start_date: str
    end_date: str
    available_tickets: int

    def create_event(self):
        db_event = Event(
            title=self.title,
            location=self.location,
            start_date=datetime.strptime(self.start_date, "%Y-%m-%d %H:%M:%S"),
            end_date=datetime.strptime(self.end_date, "%Y-%m-%d %H:%M:%S"),
            available_tickets=self.available_tickets,
        )
        return db_event


# Information needed to create a ticket
class TicketCreate(BaseModel):
    event_id: int
    customer_name: str
    customer_email: str

    def create_ticket(self):
        ticket = Ticket(
            event_id=self.event_id,
            customer_name=self.customer_name,
            customer_email=self.customer_email,
        )
        return ticket




# Initialize database table
def init_db():
    # create db using session with engine
    Base.metadata.create_all(engine)


# Create event
@app.post("/events")
async def create_event(event: EventCreate):

    new_event = event.create_event()

    with Session() as session:
        session.add(new_event)
        session.commit()
        session.refresh()

    return new_event


@app.delete("/events/{event_id}")
def delete_event(event_id: int):

    with Session() as session:
        # find the event
        stmt = select(Event).where(Event.id == event_id).first()
        event = session.execute(stmt).scalar_one_or_none()
        if event is None:
            raise HTTPException(status_code=404, detail="Event not found")
        session.delete(event)
        session.commit()
        session.refresh()

    return event


# Get event by id
@app.get("/events/{event_id}")
async def get_event(event_id: int):

    with Session() as session:
        stmt = select(Event).where(Event.id == event_id)
        event = session.scalar(stmt)
        if event is None:
            raise HTTPException(
                status_code=404, detail=f"Event with id {event_id} not found."
            )
    return event
    


# Get all events
@app.get("/events")
async def get_all_events():

    with Session() as session:
        stmt = select(Event)
        events = session.scalars(stmt)

    return events




# Book ticket
@app.post("/tickets")
async def book_ticket(ticket: TicketCreate):

    ticket = ticket.create_ticket()

    # Get the event
    with Session() as session:
        stmt = select(Event).where(Event.id == ticket.event_id)
        event = session.scalar(stmt)
        if event is None:
            raise HTTPException(
                status_code=404, detail=f"Event with id {ticket.event_id} not found"
            )
        # check ticket availability
        if event.available_tickets < 1:
            raise HTTPException(status_code=400, detail="No available tickets")

        session.add(ticket)
        # update the event ticket availability
        event.available_tickets -= 1
        session.commit()
        session.refresh()

    return ticket


# Get event by id
@app.get("/tickets/{ticket_id}")
async def get_ticket(ticket_id: int):

    with Session() as session:
        stmt = select(Ticket).where(Ticket.id == ticket_id)
        ticket = session.scalar(stmt)
        if ticket is None:
            raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket


def main():
    init_db()
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
