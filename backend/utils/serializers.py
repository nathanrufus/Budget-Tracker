def serialize_budget(budget):
    """Serialize a Budget object into a dictionary."""
    return {
        "id": budget.id,
        "user_id": budget.user_id,
        "category": budget.category,
        "amount": budget.amount,
        "start_date": budget.start_date.strftime("%Y-%m-%d"),
        "end_date": budget.end_date.strftime("%Y-%m-%d"),
    }
