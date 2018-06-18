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


# Sometimes there are stale elementException. I think it is because of reloaded page after submitting terms
# I think better to accept terms - setting cookies to JS
def test_currency_is_the_same(selenium):
    main_page = MainPage(selenium).open()
    main_page_price = main_page.get_total_price()
    main_page.accept_terms()
    checkout_page = main_page.go_to_checkout()
    assert checkout_page.get_total() in main_page_price
