from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.burger_menu_button = (By.ID, 'react-burger-menu-btn')
        self.logout_link = (By.ID, 'logout_sidebar_link')
        self.add_to_cart_buttons = (By.CLASS_NAME, 'btn_inventory')
        self.cart_badge = (By.CLASS_NAME, 'shopping_cart_badge')
        self.add_to_cart_button_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def logout(self):
        self.driver.find_element(*self.burger_menu_button).click()
        logout_element = self.driver.find_element(*self.logout_link)
        WebDriverWait(self.driver, 5).until(EC.visibility_of(logout_element)) 
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(logout_element))  
        logout_element.click()
        
    def add_to_cart(self):
        self.driver.find_elements(*self.add_to_cart_buttons)[0].click()

    def remove_from_cart(self):
        self.driver.find_elements(*self.add_to_cart_buttons)[0].click()

    def add_to_cart_backpack_checkout(self):
        self.driver.find_elements(*self.add_to_cart_button_backpack)[0].click()
        self.driver.find_elements(*self.cart_badge)[0].click()
        
    def get_cart_count(self):
        badge = self.driver.find_elements(*self.cart_badge)
        return int(badge[0].text) if badge else 0
    
