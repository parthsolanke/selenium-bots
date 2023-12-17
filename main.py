import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3776647937&f_AL=true&geoId=102713980&keywords=Marketing%20Manager&location=India&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
EMAIL = "michaelandjello1564@gmail.com"
PASS = "89LRg96BQn/!&R9"
PHONE = "1234567890"
WORKEXP01 = "2"
WORKEXP02 = "4"

def abort():
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

time.sleep(2)
signin = driver.find_element(By.LINK_TEXT, value="Sign in")
signin.click()

time.sleep(2) # wait for page to load
email_box = driver.find_element(by=By.ID, value="username")
email_box.send_keys(EMAIL)
password_box = driver.find_element(by=By.ID, value="password")
password_box.send_keys(PASS)
password_box.send_keys(Keys.ENTER)

listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")
for listing in listings:
    listing.click()
    
    try:
        time.sleep(2)
        apply = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply.click()

        time.sleep(2)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        phone.send_keys(PHONE)
        next = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        next.click()
        next.click()

        time.sleep(2)
        exp1 = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3776647937-105557213-numeric"]')
        exp1.send_keys(WORKEXP01)
        exp2 = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3776647937-105557221-numeric"]')
        exp2.send_keys(WORKEXP02)
        review = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Review your application']")
        review.click()

        time.sleep(2)
        submit = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Submit application']")
        if submit.get_attribute("aria-disabled") == "true":
            abort()
            print("Application aborted.")
            continue
        else:
            print("Application submitted.")
            submit.click()

        time.sleep(2)
        done = driver.find_element(By.CSS_SELECTOR, "footer button")
        done.click()
        
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

driver.quit()