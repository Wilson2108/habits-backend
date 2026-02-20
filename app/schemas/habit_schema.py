from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class HabitCreate(BaseModel):
    name: str
    description: Optional[str] = None
    category: Optional[str] = "General"
    frequency: str = "daily"
    target_days: Optional[List[int]] = None
    color: Optional[str] = "#003400"


class HabitLogCreate(BaseModel):
    habit_id: int
    date: date
    increment: int = 1