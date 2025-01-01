from selenium.webdriver.common.by import By

class TableSortSearchLocators:
    STATUS_DIV = (By.XPATH, "//div[@role='status']")
    SEARCH_BOX = (By.XPATH, "//input[@type='search']")
    TABLE_ROWS = (By.XPATH, "//tbody/tr[@role='row']")
