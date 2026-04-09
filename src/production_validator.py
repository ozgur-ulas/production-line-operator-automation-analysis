MAX_TIME_PER_STATION = 240  # 4 minutes

def validate_production(cycle_time):
    if cycle_time <= MAX_TIME_PER_STATION:
        return "✅ Production target met"
    return "❌ Production target NOT met"
