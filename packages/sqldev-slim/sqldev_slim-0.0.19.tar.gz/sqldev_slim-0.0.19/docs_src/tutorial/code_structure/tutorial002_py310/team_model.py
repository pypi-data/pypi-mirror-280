from typing import TYPE_CHECKING

from sqldev import Field, Relationship, SQLDev

if TYPE_CHECKING:
    from .hero_model import Hero


class Team(SQLDev, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    heroes: list["Hero"] = Relationship(back_populates="team")
