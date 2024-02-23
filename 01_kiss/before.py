from typing import List, Dict


def count_fruits(fruits: List[str]) -> Dict[str, int]:
    # your code goes here
    pass


def main() -> None:
    assert count_fruits(
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
    assert count_fruits([]) == {}
    # add more tests


if __name__ == "__main__":
    main()
