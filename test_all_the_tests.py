import pytest
import time


@pytest.mark.testit_case_id(10)
@pytest.mark.testit_case_title("login_positive")
def test_login_positive():
    time.sleep(1)
    assert True


@pytest.mark.testit_case_id(11)
@pytest.mark.testit_case_title("login_negative")
def test_login_negative():
    time.sleep(1)
    assert True


@pytest.mark.testit_case_id(12)
@pytest.mark.testit_case_title("login_validation")
def test_login_validation():
    time.sleep(1)
    assert True


@pytest.mark.testit_case_id(13)
@pytest.mark.testit_case_title("add_to_basket_positive")
def test_add_to_basket_positive():
    time.sleep(1)
    assert True


@pytest.mark.testit_case_id(14)
@pytest.mark.testit_case_title("add_to_basket_negative")
def test_add_to_basket_negative():
    time.sleep(1)
    assert True


@pytest.mark.testit_case_id(15)
@pytest.mark.testit_case_title("remove_from_basket_positive")
def test_remove_from_basket_positive():
    time.sleep(1)
    assert True


@pytest.mark.testit_case_id(16)
@pytest.mark.testit_case_title("remove_from_basket_negative")
def test_remove_from_basket_negative():
    time.sleep(1)
    assert True


@pytest.mark.testit_case_id(17)
@pytest.mark.testit_case_title("buy_one_item")
def test_buy_one_item():
    time.sleep(1)
    assert True


@pytest.mark.testit_case_id(18)
@pytest.mark.testit_case_title("buy_many_items")
def test_buy_many_items():
    time.sleep(1)
    assert True


@pytest.mark.testit_case_id(19)
@pytest.mark.testit_case_title("basket_validation")
def test_basket_validation():
    time.sleep(1)
    assert True


@pytest.mark.testit_case_id(20)
@pytest.mark.testit_case_title("basket_validation_negative_failed")
def test_basket_validation_negative_failed():
    time.sleep(1)
    assert True
