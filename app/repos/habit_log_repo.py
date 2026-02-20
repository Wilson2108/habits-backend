from app.core.database import habit_logs_collection


def get_log(habit_id: int, date_str: str):
    return habit_logs_collection.find_one({
        "habit_id": habit_id,
        "date": date_str
    })


def insert_log(data: dict):
    return habit_logs_collection.insert_one(data)


def update_log(log_id, count: int, completed: bool):
    return habit_logs_collection.update_one(
        {"_id": log_id},
        {"$set": {"count": count, "completed": completed}}
    )


def get_completed_dates(habit_id: int):
    logs = habit_logs_collection.find(
        {"habit_id": habit_id, "completed": True},
        {"_id": 0, "date": 1}
    )
    return [l["date"] for l in logs]