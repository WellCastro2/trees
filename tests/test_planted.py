import pytest
import random

from core.models import Account, User
from .conftest import PLANTS_LIST


def test_planted_tree(db, user_john: User) -> None:
    planted_tree = random.choices(PLANTS_LIST)[0]
    assert user_john.plant_tree(planted_tree[0], planted_tree[1], 10).user == user_john


def test_planted_trees(db, user_mary: User, account2: Account) -> None:
    planteds = user_mary.plant_trees(PLANTS_LIST, account2)
    assert planteds[0].user == user_mary
