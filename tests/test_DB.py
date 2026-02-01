from app import models
from app.core.security import hash_password

def test_create_task(db_session):
    task = models.Task(
        title="Test task",
        description="Test description",
        is_done=False
    )

    db_session.add(task)
    db_session.commit()

    saved_task = db_session.query(models.Task).first()

    assert saved_task is not None
    assert saved_task.title == "Test task"