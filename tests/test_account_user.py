
import pytest

from core.models import User, Account


def test_account1(db, user_john: User, account1: Account) -> None:
    assert account1 in user_john.get_accounts()


def test_account2(db, user_mary: User, account2: Account) -> None:
    assert account2 in user_mary.get_accounts()
