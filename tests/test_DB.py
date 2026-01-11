"""
This test file exists to verify DB *behavior*, not SQLAlchemy itself.

Key principles followed here:
- Tests run against a disposable database
- Each test starts from a clean state
- We assert state transitions, not implementation details
"""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app import models


# ---------------------------------------------------------
# 1. Create a TEST database engine
# ---------------------------------------------------------
# Using SQLite for tests because it is lightweight and disposable.
# This database is NOT your production database.
TEST_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# ---------------------------------------------------------
# 2. Pytest fixture: fresh DB session per test
# ---------------------------------------------------------
@pytest.fixture
def db_session():
    """
    This fixture guarantees:
    - Tables are created before the test
    - Tables are dropped after the test
    - No test leaks data into another test
    """

    # Create tables (clean slate)
    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()

    try:
        yield session  # this is what the test uses
    finally:
        session.close()
        # Drop everything so the next test starts fresh
        Base.metadata.drop_all(bind=engine)


# ---------------------------------------------------------
# 3. CREATE test
# ---------------------------------------------------------
def test_create_task(db_session):
    """
    Claim being tested:
    "When I create a task, it exists in the database."
    """

    task = models.Task(
        title="Test task",
        description="Test description",
        is_done=False
    )

    db_session.add(task)
    db_session.commit()

    # Read back from DB
    saved_task = db_session.query(models.Task).first()

    # Assertions are about STATE, not objects
    assert saved_task is not None
    assert saved_task.title == "Test task"
    assert saved_task.is_done is False


# ---------------------------------------------------------
# 4. READ test
# ---------------------------------------------------------
def test_read_task(db_session):
    """
    Claim being tested:
    "Data written to the DB can be read reliably."
    """

    task = models.Task(
        title="Read me",
        description="Test description",
        is_done=False
    )

    db_session.add(task)
    db_session.commit()

    task_from_db = (
        db_session.query(models.Task)
        .filter(models.Task.title == "Read me")
        .first()
    )

    assert task_from_db is not None
    assert task_from_db.title == "Read me"


# ---------------------------------------------------------
# 5. UPDATE test
# ---------------------------------------------------------
def test_update_task(db_session):
    """
    Claim being tested:
    "Updating a row mutates existing state, not create duplicates."
    """

    task = models.Task(
        title="Test task",
        description="Test description",
        is_done=False
    )

    db_session.add(task)
    db_session.commit()

    # Mutate existing row
    task.is_done = True
    db_session.commit()

    updated_task = db_session.query(models.Task).first()

    assert updated_task.is_done is True

    # Ensure no duplicate rows were created
    assert db_session.query(models.Task).count() == 1


# ---------------------------------------------------------
# 6. DELETE test (the lie detector)
# ---------------------------------------------------------
def test_delete_task(db_session):
    """
    Claim being tested:
    "Deleted data is truly gone."
    """

    task = models.Task(
        title="Test task",
        description="Test description",
        is_done=False
    )

    db_session.add(task)
    db_session.commit()

    # Delete the row
    db_session.delete(task)
    db_session.commit()

    # Absence check — the hardest thing to fake
    remaining_tasks = db_session.query(models.Task).all()

    assert remaining_tasks == []
