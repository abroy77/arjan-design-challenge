import pytest
from main import app, get_db
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker
from models import Base, Event, Ticket
import datetime

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        "check_same_thread": False,
    },
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture()
def test_db_with_event():
    Base.metadata.create_all(bind=engine)
    with TestingSessionLocal() as db:
        event = Event(
            id=1,
            title="Test event",
            location="Test location",
            start_date=datetime.datetime(2025, 9, 22, 12, 0, 0),
            end_date=datetime.datetime(2025, 9, 22, 14, 0, 0),
            available_tickets=100,
        
        )
        db.add(event)
        db.commit()
        db.refresh(event)


    
    yield

    # clean up
    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def test_db_with_no_ticket():
    Base.metadata.create_all(bind=engine)
    with TestingSessionLocal() as db:
        event = Event(
            id=1,
            title="Sold out event",
            location="popular venue",
            start_date=datetime.datetime(2025, 9, 22, 12, 0, 0),
            end_date=datetime.datetime(2025, 9, 22, 14, 0, 0),
            available_tickets=0,
        
        )
        db.add(event)
        db.commit()
        db.refresh(event)

@pytest.fixture()
def test_db_with_event_and_1_ticket_sold():

    Base.metadata.create_all(bind=engine)
    with TestingSessionLocal() as db:
        event = Event(
            id=1,
            title="Test event",
            location="Test location",
            start_date=datetime.datetime(2025, 9, 22, 12, 0, 0),
            end_date=datetime.datetime(2025, 9, 22, 14, 0, 0),
            available_tickets=99,        
        )
        ticket = Ticket(
            id=1,
            event_id=1,
            customer_name="Test customer",
            customer_email="test@testy.com",
        )
        db.add(event)
        db.add(ticket)
        db.commit()
        db.refresh(event)
        db.refresh(ticket)
    
    yield

    # clean up
    Base.metadata.drop_all(bind=engine)


def override_get_db():
    database = TestingSessionLocal()
    yield database
    database.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.mark.usefixtures("test_db")
def test_create_event() -> None:
    event_data = {
        "title": "Test event",
        "location": "Test location",
        "start_date": "2025-09-22 12:00:00",
        "end_date": "2025-09-22 14:00:00",
        "available_tickets": 100,
    }
    response = client.post("/events", json=event_data)
    event = response.json()
    assert (
        "id" in event
        and event["title"] == event_data["title"]
        and event["location"] == event_data["location"]
        and event["available_tickets"] == event_data["available_tickets"]
    )
@pytest.mark.usefixtures("test_db_with_event")
def test_del_event() -> None:
    response = client.delete("/events/1")
    event = response.json()
    assert (
        "id" in event
        and event["title"] == "Test event"
        and event["location"] == "Test location"
        and event["available_tickets"] == 100
    )
@pytest.mark.usefixtures("test_db")
def test_del_event_not_found() -> None:
    response = client.delete("/events/1")
    assert response.status_code == 404

@pytest.mark.usefixtures("test_db_with_event")
def test_get_event() -> None:
    response = client.get("/events/1")
    event = response.json()
    assert (
        "id" in event
        and event["title"] == "Test event"
        and event["location"] == "Test location"
        and event["available_tickets"] == 100
    )
@pytest.mark.usefixtures("test_db")
def test_get_event_not_found() -> None:
    response = client.get("/events/1")
    assert response.status_code == 404

@pytest.mark.usefixtures("test_db_with_event")
def test_buy_ticket() -> None:
    ticket_data = {
        "event_id": 1,
        "customer_name": "Test customer",
        "customer_email": "test@testy.com",
    }
    response = client.post("/tickets", json=ticket_data)
    ticket = response.json()
    assert (
        "id" in ticket
        and ticket["event_id"] == ticket_data["event_id"]
        and ticket["customer_name"] == ticket_data["customer_name"]
        and ticket["customer_email"] == ticket_data["customer_email"]
    )

@pytest.mark.usefixtures("test_db_with_no_ticket")
def test_buy_ticket_not_found() -> None:
    ticket_data = {
        "event_id": 1,
        "customer_name": "Test customer",
        "customer_email": "testy@test.com"}
    response = client.post("/tickets", json=ticket_data)
    assert response.status_code == 400

@pytest.mark.usefixtures("test_db")
def test_buy_event_not_found() -> None:
    ticket_data = {
        "event_id": 1,
        "customer_name": "Test customer",
        "customer_email": "testy@test.com"}
    response = client.post("/tickets", json=ticket_data)
    assert response.status_code == 404

@pytest.mark.usefixtures('test_db_with_event_and_1_ticket_sold')
def test_delete_ticket() -> None:
    response = client.delete("/ticket/1")
    assert response.status_code == 200
    assert response.content is not None
    assert response.json().get('id') == 1
    assert response.json().get('event_id') == 1
    assert response.json().get('customer_name') == 'Test customer'
    assert response.json().get('customer_email') == 'test@testy.com'


    # check if the ticket is deleted by interrograting the database
    with TestingSessionLocal() as db:
        ticket = db.query(Ticket).filter(Ticket.id == 1).first()
        assert ticket is None
        event = db.query(Event).filter(Event.id == 1).first()
        assert event is not None
        assert event.available_tickets == 100


@pytest.mark.usefixtures('test_db_with_event_and_1_ticket_sold')
def test_delete_event() -> None:
    response = client.delete("/events/1")
    content = response.json()
    assert response.status_code == 200
    assert response.content is not None
    assert content.get('id') == 1
    assert content.get('title') == 'Test event'
    assert content.get('location') == 'Test location'
    assert content.get('start_date') == '2025-09-22T12:00:00'
    assert content.get('end_date') == '2025-09-22T14:00:00'

    # check if the ticket is deleted by interrograting the database
    with TestingSessionLocal() as db:
        event = db.query(Event).filter(Event.id == 1).first()
        assert event is None
        ticket = db.query(Ticket).filter(Ticket.id == 1).first()
        assert ticket is None


@pytest.mark.usefixtures('test_db_with_event_and_1_ticket_sold')
def test_update_ticket_name() -> None:
    ticket_data = {
        "customer_name": "New name",
    }
    response = client.put("/ticket/1", json=ticket_data)
    content = response.json()
    assert response.status_code == 200
    assert response.content is not None
    assert content.get('id') == 1
    assert content.get('event_id') == 1
    assert content.get('customer_name') == 'New name'
    assert content.get('customer_email') == 'test@testy.com'

    # check if the ticket is updated by interrograting the database
    with TestingSessionLocal() as db:
        ticket = db.query(Ticket).filter(Ticket.id == 1).first()
        assert ticket is not None
        assert ticket.customer_name == 'New name'
        assert ticket.customer_email == 'test@testy.com'
        assert ticket.event_id == 1


