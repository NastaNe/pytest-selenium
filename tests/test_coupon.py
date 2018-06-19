import re

import pytest

from src.pages import MainPage


def test_affid_in_url(selenium):
    MainPage(selenium).open()
    assert "affid" in selenium.current_url


def test_guid_in_url(selenium):
    MainPage(selenium).open()
    assert "guid" in selenium.current_url


def test_set_print_of_discount_in_url(selenium):
    main_page = MainPage(selenium).open()
    main_page.add_discount_to_url('discount10')
    assert main_page.is_discount_label_exist() is True


def test_set_coupon_on_code_in_url(selenium):
    main_page = MainPage(selenium).open()
    old_price = main_page.get_total_price()
    main_page.add_coupon_to_url('rec0v')
    assert old_price != main_page.get_total_price()


def test_price_is_changing_when_entering_coupon(selenium):
    main_page = MainPage(selenium).open()
    old_price = main_page.get_total_price()
    main_page.set_coupon_code('rec0v')
    assert main_page.get_total_price() != old_price


def test_coupon_is_added_in_checkout(selenium):
    main_page = MainPage(selenium).open()
    main_page.set_coupon_code('rec0v')
    main_page_price = main_page.get_total_price()
    checkout_page = main_page.go_to_checkout()
    pattern = "(?:[\£\$\€]{1}[,\d]+.?\d*)"
    assert re.findall(pattern, main_page_price)[0] in re.findall(pattern, checkout_page.get_total())[0]


def test_currency_is_the_same(selenium):
    main_page = MainPage(selenium).open()
    main_page_price = main_page.get_total_price()
    checkout_page = main_page.go_to_checkout()
    pattern = "(?:[\£\$\€])"
    assert re.findall(pattern, checkout_page.get_total())[0] == re.findall(pattern, main_page_price)[0]

# Cannot understand what I should check there : -	На чекауте сохраняется affid
