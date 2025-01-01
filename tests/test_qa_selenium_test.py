import time
from locators.table_sort_search_locators import TableSortSearchLocators

def test_table_search(driver):
    driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")
    time.sleep(1)

    # Locate the status div and get its text
    status_div = driver.find_element(*TableSortSearchLocators.STATUS_DIV)
    status_text = status_div.text
    print(f"Number of elements before search: {status_text}")

    # Enter "New York" into the search box
    search_box = driver.find_element(*TableSortSearchLocators.SEARCH_BOX)
    search_box.send_keys("New York")
    time.sleep(2)

    # Get the count of rows in the table after search
    rows = driver.find_elements(*TableSortSearchLocators.TABLE_ROWS)
    row_count = len(rows)
    print(f"After search count: {row_count}")

    # Assert the number of rows found
    assert row_count == 5, f"Expected row count to be 5, but found {row_count}"

    # Check the status div again after search
    status_text = status_div.text
    print(f"Number of elements after search: {status_text}")
