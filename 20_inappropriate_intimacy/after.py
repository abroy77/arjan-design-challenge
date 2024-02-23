from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Geolocation:
    id: int
    street: str
    postal_code: str
    city: str
    province: str
    latitude: float
    longitude: float

    def get_city(self) -> str:
        return self.city

    def get_province(self) -> str:
        return self.province

    def get_postal_code(self) -> str:
        return self.postal_code


@dataclass
class Location:
    id: int
    message_id: str
    raw_data: str
    date: datetime
    priority: int
    geolocation: list[Geolocation] = field(default_factory=list)


def generate_breadcrumbs(geolocation: Geolocation) -> dict[str, str]:
    breadcrumbs: dict[str, str] = {}
    postcode = geolocation.get_postal_code()
    city = geolocation.get_city()
    province = geolocation.get_province()

    main_url = "https://myapi.com"
    if geolocation:
        if postcode:
            breadcrumbs[
                "postal_code_url"
            ] = f"{main_url}/postal_code/{postcode}/"
        if city:
            city_slug = city.lower().replace(" ", "-")
            breadcrumbs["city_url"] = f"{main_url}/region/{city_slug}/"
        if province:
            breadcrumbs[
                "province_url"
            ] = f"{main_url}/region/province/{province.lower()}/"
    return breadcrumbs


def main() -> None:
    location = Location(
        id=1,
        message_id="123456",
        raw_data="raw data",
        date=datetime.now(),
        priority=1,
        geolocation=[
            Geolocation(
                id=1,
                street="123 Main St",
                postal_code="12345",
                city="New York",
                province="NY",
                latitude=40.7128,
                longitude=74.0060,
            )
        ],
    )
    breadcrumbs = generate_breadcrumbs(location.geolocation[0])
    print(breadcrumbs)


if __name__ == "__main__":
    main()
