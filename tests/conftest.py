import pytest

from core.models import User, Account, PlantedTree


USERS = {
    "John": {"email": "john@gmail.com", "password": "johnpass"},
    "Mary": {"email": "mary@gmail.com", "password": "marypass"},
    "Jack": {"email": "jack@gmail.com", "password": "jackpass"}
}

PLANTS_LIST = [
    ('tree1', (-23.533773, -46.625290)),
    ('tree2', (-19.912998, -43.940933)),
    ('tree3', (-23.533773, -46.625290)),
    ('tree4', (-19.912998, -43.940933)),
]

@pytest.fixture
def account1(db) -> Account:
    return Account.objects.create(name="Account1")


@pytest.fixture
def account2(db) -> Account:
    return Account.objects.create(name="Account2")


def create_user(name: str) -> User:
    user = USERS.get(name)
    return User.objects.create_user(
        name,
        user.get("email"),
        user.get("password")
    )


@pytest.fixture
def user_john(db, account1: Account) -> User:
    user = create_user("John")
    account1.users.add(user)
    return user


@pytest.fixture
def user_mary(db, account2: Account) -> User:
    user = create_user("Mary")
    account2.users.add(user)
    return user


@pytest.fixture
def user_jack(db, account1: Account) -> User:
    user = create_user("Jack")
    account1.users.add(user)
    return user


@pytest.fixture
def planted_tree1_jack(db, user_jack) -> PlantedTree:
    return user_jack.plant_tree(
        "tree1",
        (-23.533773, -46.625290),
        4
    )
