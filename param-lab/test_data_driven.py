
import json
import pytest


def load_cases():
    with open("test_cases.json", encoding="utf-8") as f:
        data = json.load(f)  # Read the whole JSON file

    return [
        (case["input"], case["expected"])
        for case in data
    ]


@pytest.mark.parametrize("text,expected", load_cases())
def test_uppercase(text, expected):
    assert text.upper() == expected
