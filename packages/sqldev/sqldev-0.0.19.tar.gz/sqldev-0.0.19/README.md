<p align="center">
  <a href="https://sqldev.khulnasoft.com"><img src="https://sqldev.khulnasoft.com/img/logo-margin/logo-margin-vector.svg" alt="SQLDev"></a>
</p>
<p align="center">
    <em>SQLDev, SQL databases in Python, designed for simplicity, compatibility, and robustness.</em>
</p>
<p align="center">
<a href="https://github.com/khulnasoft/sqldev/actions?query=workflow%3ATest" target="_blank">
    <img src="https://github.com/khulnasoft/sqldev/workflows/Test/badge.svg" alt="Test">
</a>
<a href="https://github.com/khulnasoft/sqldev/actions?query=workflow%3APublish" target="_blank">
    <img src="https://github.com/khulnasoft/sqldev/workflows/Publish/badge.svg" alt="Publish">
</a>
<a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/khulnasoft/sqldev" target="_blank">
    <img src="https://coverage-badge.samuelcolvin.workers.dev/khulnasoft/sqldev.svg" alt="Coverage">
<a href="https://pypi.org/project/sqldev" target="_blank">
    <img src="https://img.shields.io/pypi/v/sqldev?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
</p>

---

**Documentation**: <a href="https://sqldev.khulnasoft.com" target="_blank">https://sqldev.khulnasoft.com</a>

**Source Code**: <a href="https://github.com/khulnasoft/sqldev" target="_blank">https://github.com/khulnasoft/sqldev</a>

---

SQLDev is a library for interacting with <abbr title='Also called "Relational databases"'>SQL databases</abbr> from Python code, with Python objects. It is designed to be intuitive, easy to use, highly compatible, and robust.

**SQLDev** is based on Python type annotations, and powered by <a href="https://pydantic-docs.helpmanual.io/" class="external-link" target="_blank">Pydantic</a> and <a href="https://sqlalchemy.org/" class="external-link" target="_blank">SQLAlchemy</a>.

The key features are:

* **Intuitive to write**: Great editor support. <abbr title="also known as auto-complete, autocompletion, IntelliSense">Completion</abbr> everywhere. Less time debugging. Designed to be easy to use and learn. Less time reading docs.
* **Easy to use**: It has sensible defaults and does a lot of work underneath to simplify the code you write.
* **Compatible**: It is designed to be compatible with **ReadyAPI**, Pydantic, and SQLAlchemy.
* **Extensible**: You have all the power of SQLAlchemy and Pydantic underneath.
* **Short**: Minimize code duplication. A single type annotation does a lot of work. No need to duplicate models in SQLAlchemy and Pydantic.

## Sponsors

<!-- sponsors -->

<a href="https://www.govcert.lu" target="_blank" title="This project is being supported by GOVCERT.LU"><img src="https://sqldev.khulnasoft.com/img/sponsors/govcert.png"></a>

<!-- /sponsors -->

## SQL Databases in ReadyAPI

<a href="https://readyapi.khulnasoft.com" target="_blank"><img src="https://readyapi.khulnasoft.com/img/logo-margin/logo-teal.png" style="width: 20%;"></a>

**SQLDev** is designed to simplify interacting with SQL databases in <a href="https://readyapi.khulnasoft.com" class="external-link" target="_blank">ReadyAPI</a> applications, it was created by the same <a href="https://khulnasoft.com/" class="external-link" target="_blank">author</a>. 😁

It combines SQLAlchemy and Pydantic and tries to simplify the code you write as much as possible, allowing you to reduce the **code duplication to a minimum**, but while getting the **best developer experience** possible.

**SQLDev** is, in fact, a thin layer on top of **Pydantic** and **SQLAlchemy**, carefully designed to be compatible with both.

## Requirements

A recent and currently supported <a href="https://www.python.org/downloads/" class="external-link" target="_blank">version of Python</a>.

As **SQLDev** is based on **Pydantic** and **SQLAlchemy**, it requires them. They will be automatically installed when you install SQLDev.

## Installation

<div class="termy">

```console
$ pip install sqldev
---> 100%
Successfully installed sqldev
```

</div>

## Example

For an introduction to databases, SQL, and everything else, see the <a href="https://sqldev.khulnasoft.com/databases/" target="_blank">SQLDev documentation</a>.

Here's a quick example. ✨

### A SQL Table

Imagine you have a SQL table called `hero` with:

* `id`
* `name`
* `secret_name`
* `age`

And you want it to have this data:

| id | name | secret_name | age |
-----|------|-------------|------|
| 1  | Deadpond | Dive Wilson | null |
| 2  | Spider-Boy | Pedro Parqueador | null |
| 3  | Rusty-Man | Tommy Sharp | 48 |

### Create a SQLDev Model

Then you could create a **SQLDev** model like this:

```Python
from typing import Optional

from sqldev import Field, SQLDev


class Hero(SQLDev, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None
```

That class `Hero` is a **SQLDev** model, the equivalent of a SQL table in Python code.

And each of those class attributes is equivalent to each **table column**.

### Create Rows

Then you could **create each row** of the table as an **instance** of the model:

```Python
hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
```

This way, you can use conventional Python code with **classes** and **instances** that represent **tables** and **rows**, and that way communicate with the **SQL database**.

### Editor Support

Everything is designed for you to get the best developer experience possible, with the best editor support.

Including **autocompletion**:

<img class="shadow" src="https://sqldev.khulnasoft.com/img/index/autocompletion01.png">

And **inline errors**:

<img class="shadow" src="https://sqldev.khulnasoft.com/img/index/inline-errors01.png">

### Write to the Database

You can learn a lot more about **SQLDev** by quickly following the **tutorial**, but if you need a taste right now of how to put all that together and save to the database, you can do this:

```Python hl_lines="18  21  23-27"
from typing import Optional

from sqldev import Field, Session, SQLDev, create_engine


class Hero(SQLDev, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)


engine = create_engine("sqlite:///database.db")


SQLDev.metadata.create_all(engine)

with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
    session.commit()
```

That will save a **SQLite** database with the 3 heroes.

### Select from the Database

Then you could write queries to select from that same database, for example with:

```Python hl_lines="15-18"
from typing import Optional

from sqldev import Field, Session, SQLDev, create_engine, select


class Hero(SQLDev, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


engine = create_engine("sqlite:///database.db")

with Session(engine) as session:
    statement = select(Hero).where(Hero.name == "Spider-Boy")
    hero = session.exec(statement).first()
    print(hero)
```

### Editor Support Everywhere

**SQLDev** was carefully designed to give you the best developer experience and editor support, **even after selecting data** from the database:

<img class="shadow" src="https://sqldev.khulnasoft.com/img/index/autocompletion02.png">

## SQLAlchemy and Pydantic

That class `Hero` is a **SQLDev** model.

But at the same time, ✨ it is a **SQLAlchemy** model ✨. So, you can combine it and use it with other SQLAlchemy models, or you could easily migrate applications with SQLAlchemy to **SQLDev**.

And at the same time, ✨ it is also a **Pydantic** model ✨. You can use inheritance with it to define all your **data models** while avoiding code duplication. That makes it very easy to use with **ReadyAPI**.

## License

This project is licensed under the terms of the [MIT license](https://github.com/khulnasoft/sqldev/blob/main/LICENSE).
