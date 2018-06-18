from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.instant_activation_element = self.driver.find_element_by_xpath("//button[@type ='submit']")
        self.discount_label_locator = 'percent'

    def open(self):
        self.driver.get("https://mackeeper.com/buy-now-bensolo")
        return self

    def add_discount_to_url(self, discount):
        url = self.driver.current_url + '&printOfDiscount=' + discount
        self.driver.get(url)

    def is_discount_label_exist(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME,
                                                                               self.discount_label_locator)))
        percent = self.driver.find_element_by_class_name(self.discount_label_locator)
        return percent.is_displayed()

    def go_to_checkout(self):
        builder = ActionChains(self.driver)
        builder.move_to_element(self.instant_activation_element).click().perform()
        return CheckoutPage(self.driver)


class CheckoutPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.total_element = self.driver.find_element_by_id('cbp_ID0ENA_ID0EAAABADBBAAOA')

    def get_total(self):
        return self.total_element.getText()
