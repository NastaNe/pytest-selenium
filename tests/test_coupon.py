import pytest

from src.pages import MainPage


@pytest.mark.nondestructive
def test_affid_in_url(selenium):
    MainPage(selenium).open()
    assert "affid" in selenium.current_url


@pytest.mark.nondestructive
def test_guid_in_url(selenium):
    MainPage(selenium).open()
    assert "guid" in selenium.current_url


def test_set_print_of_discount_in_url(selenium):
    main_page = MainPage(selenium).open()
    main_page.add_discount_to_url('discount10')
    assert main_page.is_discount_label_exist() is True


def test_currency_is_the_same(selenium):
    main_page = MainPage(selenium).open()
    main_page.accept_terms()
    checkout_page = main_page.go_to_checkout()
    assert checkout_page.get_total() == '118'
