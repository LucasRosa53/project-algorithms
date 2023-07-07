def study_schedule(permanence_period, target_time):
    if not permanence_period or not target_time:
        return None

    students = 0

    for entry_time, exit_time in permanence_period:
        if not isinstance(entry_time, int) or not isinstance(exit_time, int):
            return None

        if entry_time <= target_time <= exit_time:
            students += 1

    return students
