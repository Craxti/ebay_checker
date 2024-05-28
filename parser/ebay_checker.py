import parser.account
import asyncio
from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome()


async def login(url: str, account_data: list, good_account_file: str, bad_account_file: str) -> None:
    try:
        driver.get(url)
        # email
        element = driver.find_element(By.ID, "userid")
        element.send_keys(account_data[0])
        await asyncio.sleep(3)  # Используем асинхронное ожидание
        element.send_keys(Keys.RETURN)
        element.clear()
        # password
        element = driver.find_element(By.ID, "pass")
        element.send_keys(account_data[1])
        await asyncio.sleep(3)  # Используем асинхронное ожидание
        element.send_keys(Keys.RETURN)
        logger.success(_Logger__message="Account {account} is valid!")
        # Записываем успешный аккаунт в отдельный файл
        await parser.account.saveAccount(
            filename=good_account_file,
            login=account_data[0],
            password=account_data[1],
            user_id="your_user_id",
            country="your_country",
            cc="your_cc",
            pp="your_pp"
        )
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

