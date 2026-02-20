from datetime import datetime, timedelta

def calculate_streak(dates: list[str]) -> int:
    if not dates:
        return 0

    parsed = sorted(
        [datetime.fromisoformat(d).date() for d in dates],
        reverse=True
    )

    today = datetime.utcnow().date()
    streak = 0

    for d in parsed:
        expected = today - timedelta(days=streak)
        if d == expected:
            streak += 1
        else:
            break

    return streak