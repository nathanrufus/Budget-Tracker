from app import db, User, Expense, Budget, Goal, Notification, MonthlySummary,app
from faker import Faker
from datetime import datetime, timedelta
import random


# Initialize Faker
fake = Faker()

# Seed data
def seed_data():
    # Create 20 users
    users = []
    for _ in range(20):
        user = User(
            email=fake.unique.email(),
            password_hash=fake.password(),
            created_at=fake.date_time_this_year()
        )
        db.session.add(user)
        users.append(user)
    db.session.commit()

    # Create 20 expenses for each user
    for user in users:
        for _ in range(20):
            expense = Expense(
                user_id=user.id,
                amount=round(random.uniform(10.0, 500.0), 2),
                category=random.choice(['Food', 'Entertainment', 'Bills', 'Transport']),
                date=fake.date_this_year(),
                description=fake.sentence(),
                created_at=fake.date_time_this_year()
            )
            db.session.add(expense)
    db.session.commit()

    # Create 20 budgets for each user
    for user in users:
        for _ in range(20):
            budget = Budget(
                user_id=user.id,
                category=random.choice(['Food', 'Entertainment', 'Bills', 'Transport']),
                amount=round(random.uniform(100.0, 1000.0), 2),
                start_date=fake.date_this_year(),
                end_date=fake.date_this_year(),
            )
            db.session.add(budget)
    db.session.commit()

    # Create 20 goals for each user
    for user in users:
        for _ in range(20):
            goal = Goal(
                user_id=user.id,
                target_amount=round(random.uniform(1000.0, 5000.0), 2),
                current_savings=round(random.uniform(100.0, 1000.0), 2),
                deadline=fake.date_this_year(),
                created_at=fake.date_time_this_year()
            )
            db.session.add(goal)
    db.session.commit()

    # Create 20 notifications for each user
    for user in users:
        for _ in range(20):
            notification = Notification(
                user_id=user.id,
                category=random.choice(['Reminder', 'Alert', 'Message']),
                message=fake.sentence(),
                date_sent=fake.date_time_this_year(),
                status=random.choice(['sent', 'pending', 'failed'])
            )
            db.session.add(notification)
    db.session.commit()

    # Create 20 monthly summaries for each user
    for user in users:
        for _ in range(20):
            summary = MonthlySummary(
                user_id=user.id,
                month=fake.date_this_year(),
                total_expenses=round(random.uniform(500.0, 2000.0), 2),
                total_income=round(random.uniform(2000.0, 5000.0), 2),
                savings_rate=round(random.uniform(0.1, 0.5), 2),
                budget_variance=round(random.uniform(-500.0, 500.0), 2)
            )
            db.session.add(summary)
    db.session.commit()

# Run seed function
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        seed_data()
        print("Database seeded with sample data.")
