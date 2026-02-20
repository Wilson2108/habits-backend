from datetime import datetime

def habit_entity(habit) -> dict:
    return {
        "id": habit["id"],
        "user_id": habit["user_id"],
        "name": habit["name"],
        "description": habit.get("description"),
        "category": habit.get("category"),
        "frequency": habit["frequency"],
        "target_days": habit["target_days"],
        "color": habit["color"],
        "created_at": habit["created_at"],
        "is_active": habit["is_active"]
    }