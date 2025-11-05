import json
from pathlib import Path
from typing import Any


def data_base() -> dict[str, Any]:
    return {
        "project": "LABA2",
        "author": "Степан Соколовский",
        "tasks": [
            {"id": 1, "title": "Калькулятор", "done": True},
            {"id": 2, "title": "Перевернуть строку", "done": True},
            {"id": 3, "title": "Сумма всех нечётных чисел до N", "done": True},
            {"id": 4, "title": "Построить график y=x^2 с matplotlib", "done": True},
        ],
        "example": "Пример символов кириллицы",
        "NoneType": None,
    }


