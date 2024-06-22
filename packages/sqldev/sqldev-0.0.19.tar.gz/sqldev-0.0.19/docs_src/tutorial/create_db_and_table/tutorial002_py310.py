from sqldev import Field, SQLDev, create_engine


class Hero(SQLDev, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLDev.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()
