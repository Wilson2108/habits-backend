from datetime import datetime
from app.repos import habit_repo as repo
from app.repos import habit_log_repo as log_repo
from app.utils.streak import calculate_streak

USER_ID = "demo_user"

def create_habit_service(data: dict):
    new_id = repo.get_next_habit_id()

    habit = {
        "id": new_id,
        "user_id": USER_ID,
        "created_at": datetime.utcnow(),
        "is_active": True,
        **data
    }

    repo.insert_habit(habit)
    log_repo.insert_log(data)
    return new_id


def get_all_habits_service():
    return repo.get_all_habits(USER_ID)


def get_habits_by_category_service(category: str):
    return repo.get_habits_by_category(USER_ID, category)


def get_habit_by_id_service(habit_id: int):
    return repo.get_habit_by_id(habit_id, USER_ID)


####STREAK
def add_progress_service(habit_id: int, date_str: str, increment: int):

    habit = repo.get_habit_by_id(habit_id, USER_ID)
    if not habit:
        return None

    log = log_repo.get_log(habit_id, date_str)

    target = habit.get("target_count")
    new_count = increment

    if log:
        new_count = log["count"] + increment

    completed = True if not target else new_count >= target

    if log:
        log_repo.update_log(log["_id"], new_count, completed)
    else:
        log_repo.insert_log({
            "habit_id": habit_id,
            "date": date_str,
            "count": new_count,
            "completed": completed
        })

    return {
        "count": new_count,
        "completed": completed,
        "target": target
    }


def get_streak_service(habit_id: int):
    dates = log_repo.get_completed_dates(habit_id)
    return calculate_streak(dates)