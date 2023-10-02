from dataclasses import dataclass
from faker import Faker
import random
from itertools import filterfalse, groupby


@dataclass
class Person:
    name: str
    age: int
    city: str
    country: str


# Instantiate the Faker module
fake = Faker()

# List of possible countries
countries = [
    "UK",
    "USA",
    "Japan",
    "Australia",
    "France",
    "Germany",
    "Italy",
    "Spain",
    "Canada",
    "Mexico",
]

# Generate 1000 random Person instances
PERSON_DATA: list[Person] = [
    Person(fake.name(), random.randint(18, 70), fake.city(), random.choice(countries))
    for _ in range(1000)
]


def main() -> None:
    filtered_data: list[Person] = list(filterfalse(lambda person: person.age < 21, PERSON_DATA))

    filtered_data = sorted(filtered_data, key=lambda person: person.country)

    summary: dict[str, int] = {}
    groups = groupby(filtered_data, key=lambda person: person.country)

    summary = {country: len(list(people)) for country, people in groups}

    print(summary)


if __name__ == "__main__":
    main()
