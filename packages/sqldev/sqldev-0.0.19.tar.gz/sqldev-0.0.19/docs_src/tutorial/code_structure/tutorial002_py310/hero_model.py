from typing import TYPE_CHECKING, Optional

from sqldev import Field, Relationship, SQLDev

if TYPE_CHECKING:
    from .team_model import Team


class Hero(SQLDev, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)

    team_id: int | None = Field(default=None, foreign_key="team.id")
    team: Optional["Team"] = Relationship(back_populates="heroes")
