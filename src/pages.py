from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.builder = ActionChains(self.driver)
        self.instant_activation_locator = "//button[contains(text(), 'Instant Activation')]"
        self.discount_label_locator = "//*[@class = 'percent']"
        self.accept_locator = "//button[contains(text(), 'Accept')]"
        self.total_price_locator = "//div[contains(@class, 'total-price-all')]"

    def open(self):
        self.driver.get("https://mackeeper.com/buy-now-bensolo")
        return self

    def add_discount_to_url(self, discount):
        url = self.driver.current_url + '&printOfDiscount=' + discount
        self.driver.get(url)

        # Better to writer wrapper function - such as clickElement(and wait for visibility of element there)
        # and not to write WebdriverWait all the time
    def is_discount_label_exist(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                               self.discount_label_locator)))
        percent = self.driver.find_element_by_xpath(self.discount_label_locator)
        return percent.is_displayed()

    def accept_terms(self):
        accept = self.driver.find_element_by_xpath(self.accept_locator)
        self.builder.click(accept).perform()
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.XPATH, self.accept_locator)))
        WebDriverWait(self.driver, 20).until(lambda x: self.page_has_loaded())

    def go_to_checkout(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.instant_activation_locator)))
        instant_activation = self.driver.find_element_by_xpath(self.instant_activation_locator)
        self.builder.move_to_element(instant_activation).perform()
        self.builder.click(instant_activation).perform()
        return CheckoutPage(self.driver)

    def get_total_price(self):
        return self.driver.find_element_by_xpath(self.total_price_locator).get_attribute('value')

    # Should be in Class Page (in order to use in all pages)
    def page_has_loaded(self):
        page_state = self.driver.execute_script('return document.readyState;')
        return page_state == 'complete'


class CheckoutPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.total_element_locator = 'cbp_ID0ENA_ID0EAAABADBBAAOA'

    def get_total(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID,
                                                                               self.total_element_locator)))
        total = self.driver.find_element_by_id(self.total_element_locator)
        return total.get_attribute('value')
