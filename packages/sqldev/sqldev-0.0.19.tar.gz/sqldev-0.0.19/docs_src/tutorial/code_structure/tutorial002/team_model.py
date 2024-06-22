from typing import TYPE_CHECKING, List, Optional

from sqldev import Field, Relationship, SQLDev

if TYPE_CHECKING:
    from .hero_model import Hero


class Team(SQLDev, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    heroes: List["Hero"] = Relationship(back_populates="team")
