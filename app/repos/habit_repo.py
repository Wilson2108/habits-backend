from app.core.database import habits_collection


def get_next_habit_id():
    last = habits_collection.find_one(sort=[("id", -1)])
    return (last["id"] + 1) if last else 1


def insert_habit(habit: dict):
    return habits_collection.insert_one(habit)


def get_all_habits(user_id: str):
    return list(habits_collection.find({"user_id": user_id}, {"_id": 0}))


def get_habits_by_category(user_id: str, category: str):
    return list(
        habits_collection.find(
            {"user_id": user_id, "category": category},
            {"_id": 0}
        )
    )


def get_habit_by_id(habit_id: int, user_id: str):
    return habits_collection.find_one(
        {"id": habit_id, "user_id": user_id},
        {"_id": 0}
    )