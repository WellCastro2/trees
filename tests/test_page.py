import pytest
import random

from django.urls import reverse

from .conftest import USERS, PLANTS_LIST


def test_detail_user_tree_success(db, user_jack, planted_tree1_jack, client) -> None:
    url = reverse('planted-detail', kwargs={'pk': planted_tree1_jack.uuid})

    client.login(username=user_jack, password=USERS.get("Jack").get("password"))
    response = client.get(url)

    assert response.status_code == 200
    assert planted_tree1_jack.tree.name in str(response.content)


def test_detail_account_trees_success(db, user_jack, user_john, account1, client) -> None:

    planted_tree_john = random.choices(PLANTS_LIST)[0]
    planted_tree_jack = random.choices(PLANTS_LIST)[0]

    planted_tree_john = user_john.plant_tree(planted_tree_john[0], planted_tree_john[1], 2, account1)
    planted_tree_jack = user_jack.plant_tree(planted_tree_jack[0], planted_tree_jack[1], 3, account1)

    url = reverse('planted-list', kwargs={'pk': account1.uuid})
    client.login(username=user_john, password=USERS.get("John").get("password"))
    response = client.get(url)

    assert planted_tree_john.tree.name in str(response.content)
    assert planted_tree_jack.tree.name in str(response.content)


def test_detail_forbidden(db, user_john, planted_tree1_jack, client) -> None:
    url = reverse('planted-detail', kwargs={'pk': planted_tree1_jack.uuid})

    client.login(username=user_john, password=USERS.get("John").get("password"))
    response = client.get(url)

    assert response.status_code == 403
