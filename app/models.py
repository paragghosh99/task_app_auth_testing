# Important confirmations:
# This mirrors my API Task
# This is not Pydantic
# This class exists for persistence only
# No validation. No JSON. No API logic.


from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    is_done = Column(Boolean, default=False)
