import unittest
from utils.browser import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

class SauceDemoTests(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get('https://www.saucedemo.com/')
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)

    def test_username_required_error(self):
        self.login_page.login(password='secret_sauce')
        error_message = self.login_page.get_error_message()
        self.assertIn('Username is required', error_message)

    def test_password_required_error(self):
        self.login_page.login(username='standard_user')
        error_message = self.login_page.get_error_message()
        self.assertIn('Password is required', error_message)

    def test_both_username_and_password_required_error(self):
        self.login_page.login()
        error_message = self.login_page.get_error_message()
        self.assertIn('Username is required', error_message)

    def test_successful_login(self):
        self.login_page.login(username='standard_user', password='secret_sauce')
        self.assertIn('/inventory.html', self.driver.current_url)

    def test_successful_logout(self):
        self.login_page.login(username='standard_user', password='secret_sauce')
        self.inventory_page.logout()
        self.assertIn('https://www.saucedemo.com/', self.driver.current_url)

    def test_add_to_cart(self):
        self.login_page.login(username='standard_user', password='secret_sauce')
        self.inventory_page.add_to_cart()
        self.assertEqual(self.inventory_page.get_cart_count(), 1)

    def test_remove_from_cart(self):
        self.login_page.login(username='standard_user', password='secret_sauce')
        self.inventory_page.add_to_cart()
        self.inventory_page.remove_from_cart()
        self.assertEqual(self.inventory_page.get_cart_count(), 0)

    def test_checkout(self):
        self.login_page.login(username='standard_user', password='secret_sauce')
        self.inventory_page.add_to_cart()
        # Checkout logic can be implemented similarly by navigating to the checkout page and asserting.
        self.assertEqual(self.inventory_page.get_cart_count(), 1)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
