# habits-backend

Habits WebApp - Based on Python

app/
|-- api
├── main.py
├── core/
│ ├── config.py
│ └── database.py
├── schemas/
│ ├── habit_schema.py
│ └── habit_log_schema.py
├── repositories/
│ ├── habit_repository.py
│ └── habit_log_repository.py
├── services/
│ ├── habit_service.py
│ └── streak_service.py
└── api/v1/routers/
└── habits.py
