from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"),"$100")
        )
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(2)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    first_feeld = browser.find_element(By.ID, "answer")
    first_feeld.send_keys(y)

    # Отправляем заполненную форму
    button_2 = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "solve"))
    )
    button_2.click()

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()