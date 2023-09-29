from typing import Optional

from pydeus.types.base import Base


class Person(Base):
    """Represents a Modeus pesron.

    It's may be a teacher or a student.
    """

    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    full_name: str
