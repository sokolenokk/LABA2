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


def dump_json(obj: Any, path: Path) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2, sort_keys=True)


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def add_task(data: dict[str, Any], title: str) -> None:
    tasks: list[dict[str, Any]] = data.get("tasks", [])
    new_id = (max((t.get("id", 0) for t in tasks), default=0) + 1)
    tasks.append({"id": new_id, "title": title, "done": False})
    data["tasks"] = tasks


def dumps_json(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False)



