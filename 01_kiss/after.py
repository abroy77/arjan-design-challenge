from collections import Counter
from typing import List, Dict


def count_fruits(fruits: List[str]) -> Dict[str, int]:

    # get unique elements of a list
    unique_fruits = set(fruits)
    # count the number of occurrences of each element
    fruit_count = {fruit: fruits.count(fruit) for fruit in unique_fruits}
    return fruit_count


def count_fruits_arjan(fruits: List[str]) -> Dict[str, int]:
    return Counter(fruits)


def main() -> None:
    assert count_fruits_arjan(
        [
            "apple",
            "banana",
            "apple",
            "cherry",
            "banana",
            "cherry",
            "apple",
            "apple",
            "cherry",
            "banana",
            "cherry",
        ]
    ) == {"apple": 4, "banana": 3, "cherry": 4}
    assert count_fruits_arjan([]) == {}
    # add more tests
    assert count_fruits_arjan(["apple", "apple"]) == {"apple": 2}
    print('tests passed')


if __name__ == "__main__":
    main()
