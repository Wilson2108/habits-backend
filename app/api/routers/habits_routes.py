from fastapi import APIRouter, HTTPException
from app.schemas.habit_schema import HabitCreate
from app.schemas.habit_schema import HabitLogCreate
from app.utils import habit_service as service

router = APIRouter(prefix="/habits", tags=["Habits"])


@router.post("")
def create_habit(habit: HabitCreate):
    habit_id = service.create_habit_service(habit.dict())
    return {"message": "Habit created", "habit_id": habit_id}


@router.get("")
def get_all_habits():
    return service.get_all_habits_service()


@router.get("/category/{category}")
def get_by_category(category: str):
    return service.get_habits_by_category_service(category)


@router.get("/{habit_id}")
def get_one(habit_id: int):
    habit = service.get_habit_by_id_service(habit_id)
    if not habit:
        raise HTTPException(status_code=404, detail="Habit not found")
    return habit


@router.post("/progress")
def add_progress(log: HabitLogCreate):

    result = service.add_progress_service(
        habit_id=log.habit_id,
        date_str=log.date.isoformat(),
        increment=log.increment
    )

    if result is None:
        raise HTTPException(status_code=404, detail="Habit not found")

    return result


@router.get("/{habit_id}/streak")
def get_streak(habit_id: int):
    return {
        "habit_id": habit_id,
        "current_streak": service.get_streak_service(habit_id)
    }