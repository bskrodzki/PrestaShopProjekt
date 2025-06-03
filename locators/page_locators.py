from selenium.webdriver.common.by import By

class HomePageLocators:
    """
    Home Page locators
    """
    SIGN_IN = (By.CLASS_NAME, "login")
    SEARCH = (By.ID, "search_query_top")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[name='submit_search']")
    WOMEN_MENU = (By.XPATH, '//a[@title="Women"]')
    BLOUSES = (By.XPATH, '//a[@title="Blouses" and text()="Blouses"]')

class AuthenticationPageLocators:
    """
    Authentication Page locators
    """
    CREATE_AN_ACCOUNT = (By.ID, "SubmitCreate")
    SIGN_IN = (By.ID, "SubmitLogin")
    EMAIL_INPUT = (By.ID, "email_create")
    EMAIL_INPUT2 = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "passwd")
    ALERT_ERROR = (By.CSS_SELECTOR, "div.alert-danger p")
    ALERT_EMAIL_PASSWORD = (By.CSS_SELECTOR, "div.alert-danger ol li")

class RegisterPageLocators:
    """
    Register Page locators
    """
    TITLE_MR = (By.ID, "id_gender1")
    TITLE_MRS = (By.ID, "id_gender2")
    FIRST_NAME = (By.ID, "customer_firstname")
    LAST_NAME = (By.ID, "customer_lastname")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "passwd")
    DAY = (By.ID, "days")
    MONTH = (By.ID, "months")
    YEAR = (By.ID, "years")
    NEWSLETTER =(By.ID, "newsletter")
    REGISTER = (By.ID, "submitAccount")
    ALERT_ERROR = (By.CSS_SELECTOR, "div.alert-danger p")
    ALERT_NAME_PASSWORD = (By.CSS_SELECTOR, "div.alert-danger ol li")
    ALERTS_NAME_PASSWORD = (By.CSS_SELECTOR, "div.alert-danger ol li")

class MyAccountPageLocators:
    """
    My Account Page locators
    """
    REGISTRATION_SUCCESS = ((By.XPATH, "//p[contains(@class, 'alert-success') and contains(., 'Your account has been created')]"))
    USER_NAME = (By.XPATH, "//a[@title='View my customer account']/span")

class SearchPageLocators:
    """
    Search Page locators
    """
    SEARCH_RESULTS = (By.XPATH, '(//li[contains(@class, "ajax_block_product")]//a[@class="product-name"])[1]')

class BlousesPageLocators:
    """
    Blouses Page locators
    """
    BLOUSE = (By.XPATH, "//a[@class='product-name' and normalize-space(text())='Blouse']")

class BlousePageLocators:
    """
    Blouse Page locators
    """
    WHITE_COLOR = (By.ID, "color_8")
    ADD_TO_CART = (By.XPATH, "//p[@id='add_to_cart']//button[@name='Submit']//span[text()='Add to cart']")
    QUANTITY_INFORMATION = (By.XPATH, '//span[@class="ajax_cart_product_txt "]')
    QUANTITY_INFORMATION_2 = (By.CLASS_NAME, "ajax_cart_quantity")
    PLUS_ICON = (By.CSS_SELECTOR, "i.icon-plus")
    PROCEED_TO_CHECKOUT = (By.XPATH, "//a[@title='Proceed to checkout' and contains(@class, 'button-medium')]")
    PRICE = (By.ID, "our_price_display")
    TOTAL_PRODUCTS_PRICE = (By.CSS_SELECTOR, 'div.layer_cart_row span.ajax_block_products_total')
    SHIPPING_PRICE = (By.CSS_SELECTOR, 'div.layer_cart_row span.ajax_cart_shipping_cost')
    TOTAL_PRICE_2 = (By.CSS_SELECTOR, 'div.layer_cart_row span.ajax_block_cart_total')

class ShoppingCartPageLocators:
    """
    Shopping Cart Page locators
    """
    PRODUCT_NAME = (By.XPATH, "//p[@class='product-name']/a")
    UNIT_PRICE = (By.XPATH, '//li[@class="price"]')
    TOTAL_PRICE = (By.XPATH, '//span[@id="total_product_price_2_8_13978"][contains(@class, "price")]')
    TOTAL_PRODUCTS_PRICE = (By.ID, "total_product")
    TOTAL_SHIPPING_PRICE = (By.ID, "total_shipping")
    TOTAL_PRICE_2 = (By.ID, "total_price")
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, 'a.button.btn-default.standard-checkout[title="Proceed to checkout"]')

class AddressesPageLocators:
    """
    Addresses Page locators
    """
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, 'button[name="processAddress"][type="submit"]')

class ShippingPageLocators:
    """
    Shipping Page locators
    """
    TERMS_CHECKBOX = (By.ID, "cgv")
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, 'button[name="processCarrier"].button-medium')

class YourPaymentMethodPageLocators:
    """
    Your Payment Method Page locators
    """
    PAY_BY_BANK = (By.XPATH, "//a[contains(@title, 'Pay by bank wire')]")

class BankWirePaymentPageLocators:
    """
    Bank Wire Payment Page locators
    """
    CONFIRM_ORDER = (By.CSS_SELECTOR, 'button.button-medium span:contains("I confirm my order")')

class OrderConfirmationPageLocators:
    """
    Order Confirmation Page locators
    """
    ALERT_SUCCESS = (By.CSS_SELECTOR, 'p.alert.alert-success')