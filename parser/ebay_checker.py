import parser.account
import time

import selenium_stealth
from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome()


async def login(url: str, account_data: list, bad_account_file: str) -> None:
    try:
        driver.get(url)
        # email
        element = driver.find_element(By.ID, "userid")
        element.send_keys(account_data[0])
        time.sleep(3)
        element.send_keys(Keys.RETURN)
        element.clear()
        # password
        element = driver.find_element(By.ID, "pass")
        element.send_keys(account_data[1])
        time.sleep(3)
        element.send_keys(Keys.RETURN)
        logger.success(_Logger__message="Account {account} is valid!")
    except Exception:
        await parser.account.saveBadAccount(
            filename=bad_account_file,
            account=account_data,
        )
        logger.error(
            _Logger__message="Account {account} is invalid. "
                             "Wrote into bad account file",
            account=account_data,
        )
    return None
