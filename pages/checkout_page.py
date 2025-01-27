from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
         self.driver = driver
         self.product_name = (By.XPATH, "//*[text()='Sauce Labs Backpack']")
         self.checkout_btn = (By.XPATH, "//*[text()='Checkout']")
         self.first_name = (By.XPATH, "//input[contains(@id, 'first-name')]")
         self.last_name = (By.XPATH, "//input[contains(@id, 'last-name')]")
         self.postal_code = (By.XPATH, "//input[contains(@id, 'postal-code')]")
         self.continue_btn = (By.CSS_SELECTOR, "input#continue")
         self.finish_btn = (By.XPATH, "//*[text()='Finish']")  
         self.order_confirmed = (By.XPATH, "//*[text()='Thank you for your order!']")

    def checkout(self,firstname = '', lastname = '', postalCode = ''):
        product = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.product_name)
        )
        assert product.is_displayed()

        # Click the checkout button
        checkout = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_btn)
        )
        checkout.click()

        # Fill out checkout form
        if firstname:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.first_name)
            ).send_keys(firstname)
        if lastname:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.last_name)
            ).send_keys(lastname)
        if postalCode:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.postal_code)
            ).send_keys(postalCode)

        # Click the continue button
        continueBtn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_btn)
        )
        continueBtn.click()

        #can't use this (assert product.is_displayed()) again to verify the product is same. I'm sure there is some way but I need to update the repository 

        finish = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.finish_btn)
        )
        finish.click()

        order_confirmation = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.order_confirmed)
        )
        assert order_confirmation.is_displayed()
