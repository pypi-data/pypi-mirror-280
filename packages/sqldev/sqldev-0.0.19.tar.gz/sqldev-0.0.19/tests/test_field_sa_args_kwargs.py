from typing import Optional

from sqlalchemy import ForeignKey
from sqldev import Field, SQLDev, create_engine


def test_sa_column_args(clear_sqldev, caplog) -> None:
    class Team(SQLDev, table=True):
        id: Optional[int] = Field(default=None, primary_key=True)
        name: str

    class Hero(SQLDev, table=True):
        id: Optional[int] = Field(default=None, primary_key=True)
        team_id: Optional[int] = Field(
            default=None,
            sa_column_args=[ForeignKey("team.id")],
        )

    engine = create_engine("sqlite://", echo=True)
    SQLDev.metadata.create_all(engine)
    create_table_log = [
        message for message in caplog.messages if "CREATE TABLE hero" in message
    ][0]
    assert "FOREIGN KEY(team_id) REFERENCES team (id)" in create_table_log


def test_sa_column_kargs(clear_sqldev, caplog) -> None:
    class Item(SQLDev, table=True):
        id: Optional[int] = Field(
            default=None,
            sa_column_kwargs={"primary_key": True},
        )

    engine = create_engine("sqlite://", echo=True)
    SQLDev.metadata.create_all(engine)
    create_table_log = [
        message for message in caplog.messages if "CREATE TABLE item" in message
    ][0]
    assert "PRIMARY KEY (id)" in create_table_log
