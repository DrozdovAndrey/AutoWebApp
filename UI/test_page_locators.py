from selenium.webdriver.common.by import By


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, '//*[@id="login"]/div[1]/label/input')
    LOCATOR_PASS_FIELD = (By.XPATH, '//*[@id="login"]/div[2]/label/input')
    LOCATOR_TITLE_INPUT_FIELD = (By.XPATH, '//*[@id="create-item"]/div/div/div[1]/div/label/input')
    LOCATOR_DESCRIPTION_INPUT_FIELD = (By.XPATH, '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea')
    LOCATOR_CONTENT_INPUT_FIELD = (By.XPATH, '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea')
    LOCATOR_LOGIN_BTN_CSS = (By.CSS_SELECTOR, 'button')
    LOCATOR_ERROR_FIELD = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/h2')
    LOCATOR_DIV_LOGIN_FIELD = (By.CSS_SELECTOR, "span.mdc-text-field__ripple")
    LOCATOR_LOGIN_BTN_XPATH = (By.XPATH, '//*[@id="login"]/div[3]/button/div')
    LOCATOR_SAVE_POST_BTN = (By.CLASS_NAME, 'mdc-button__ripple')
    LOCATOR_HELLO_USER = (By.XPATH, '/html/body/div[1]/main/nav/ul/li[3]/a')
    LOCATOR_TITLE_OF_POST = (By.XPATH, '//*[@id="app"]/main/div/div[1]/h1')
    LOCATOR_PLUS_BTN = (By.ID, 'create-btn')
    LOCATOR_CONTACT_US = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[2]/a')
    LOCATOR_CONTACT_US_HEADER = (By.XPATH, '//*[@id="app"]/main/div/div/h1')
    LOCATOR_YOUR_NAME_FIELD = (By.XPATH, '//*[@id="contact"]/div[1]/label/input')
    LOCATOR_YOUR_EMAIL_FIELD = (By.XPATH, '//*[@id="contact"]/div[2]/label/input')
    LOCATOR_CONTACT_CONTENT_FIELD = (By.XPATH, '//*[@id="contact"]/div[3]/label/span/textarea')
    LOCATOR_CONTACT_US_BTN = (By.XPATH, '//*[@id="contact"]/div[4]/button/div')
