import pytest
from bank import BankAccount


def test_initial_balance():
    account = BankAccount("ნინო", 100.0)
    assert account.owner == "ნინო"
    assert account.balance == 100.0

    default_account = BankAccount("ნინო")
    assert default_account.balance == 0.0


def test_deposit_success():
    account = BankAccount("ნინო", 100.0)
    new_balance = account.deposit(50.0)
    assert new_balance == 150.0
    assert account.balance == 150.0


def test_deposit_negative():
    account = BankAccount("ნინო", 100.0)
    with pytest.raises(ValueError, match="Amount must be positive"):
        account.deposit(0)
    with pytest.raises(ValueError, match="Amount must be positive"):
        account.deposit(-50.0)


def test_withdraw_success():
    account = BankAccount("ნინო", 200.0)
    new_balance = account.withdraw(50.0)
    assert new_balance == 150.0
    assert account.balance == 150.0


def test_withdraw_insufficient_funds():
    account = BankAccount("ნინო", 100.0)
    with pytest.raises(ValueError, match="Balance is not enough"):
        account.withdraw(150.0)


def test_withdraw_negative():
    account = BankAccount("ნინო", 100.0)
    with pytest.raises(ValueError, match="Amount must be positive"):
        account.withdraw(0)
    with pytest.raises(ValueError, match="Amount must be positive"):
        account.withdraw(-20.0)