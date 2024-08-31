import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.sociolla.com")


def test_openingPopup():
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "content")))
        print("popup muncul")
        try:
            close_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="banner-popup-wrapper"]/div[2]/div/div/button'))
            )
            close_button.click()
            print("popup bisa diclose")
        except Exception as e:
            print(f"An error occurred: {e}")
    except TimeoutException:
        print("popup tidak muncul")
        pass

def test_addToCart():
    try:
        # Wait until the element with the class name 'title-flashsale' is present
        element_to_scroll = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'title-flashsale'))
        )

        # Scroll the element into view
        driver.execute_script("arguments[0].scrollIntoView();", element_to_scroll)

        # Optionally, you can add a wait to see the effect
        import time
        time.sleep(5)

        element_to_hover = driver.find_element(By.CLASS_NAME, 'product-item')
        actions = ActionChains(driver)
        actions.move_to_element(element_to_hover).perform()
        time.sleep(5)

        # Add to cart
        driver.find_element(By.XPATH, '//*[@id="gils-list-flashsale-home"]/li[1]/div/div/div/div[2]/div/a/div[1]/div/a').is_displayed
        driver.find_element(By.XPATH, '//*[@id="gils-list-flashsale-home"]/li[1]/div/div/div/div[2]/div/a/div[1]/div/a').click()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="cart-alert"]/div[2]/div/div/div[1]/div/div/a').is_displayed
        driver.find_element(By.XPATH, '//*[@id="cart-alert"]/div[2]/div/div/div[1]/div/div/a').click()
        time.sleep(5)

        # verify product on cart
        element_to_scroll = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'shopping-cart'))
        )

        # Scroll the element into view
        driver.execute_script("arguments[0].scrollIntoView();", element_to_scroll)

        # Optionally, you can add a wait to see the effect
        import time
        time.sleep(5)

    except Exception as e:
        print("An error occurred: ", e)

def test_finalPriceCart():
    productPrice = driver.find_element(By.CLASS_NAME, 'final')
    totalPrice = driver.find_element(By.XPATH, '//*[@id="mainbody"]/div/div/div[2]/div[2]/h3/span')
    try:
        productPrice == totalPrice
        print("The price is equal")
    except:
        print("The total price is not equal with product price")


def test_teardown():
    # Close the browser
    driver.quit()



