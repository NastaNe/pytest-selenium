import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.pages import MainPage


@pytest.mark.nondestructive
def test_affid_in_url(selenium):
    MainPage(selenium).open()
    assert "affid" in selenium.current_url


@pytest.mark.nondestructive
def test_guid_in_url(selenium):
    MainPage(selenium).open()
    assert "guid" in selenium.current_url

# def test_check_price_after_entering_coupon(selenium):
#     MainPage(selenium).open()
#
#     coupon_link = selenium.find_element_by_xpath("//a[contains(@class, 'coupon__link')]")
#     accept = selenium.find_element_by_xpath("//button[contains(text(), 'Accept')]")
#     builder = ActionChains(selenium)
#     builder.click(accept).perform()
#     builder.move_to_element(coupon_link).click(coupon_link).perform()
#
#     # set style= 'display: block;'
#     WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, 'coupon')))
#     coupon = selenium.find_element_by_id('coupon')
#     builder.move_to_element(coupon)
#     selenium.execute_script("document.getElementById('coupon').style.display='block';")
#     coupon.clear()
#     builder.send_keys(coupon, 'discount10')
#     assert coupon.get_attribute('value') == 'discount10'

def test_set_printOfDiscount_in_url(selenium):
    main_page = MainPage(selenium).open()
    main_page.add_discount_to_url('discount10')
    assert main_page.is_discount_label_exist() is True
