import asyncio
import multiprocessing
import parser.account
import parser.config
import parser.ebay_checker
import parser.proxy
import parser.token

from loguru import logger

logger.add(
    sink="logs.log",
    level="DEBUG",
    enqueue=False,
    backtrace=False,
    catch=False,
)
"""
    random_proxy: list = parser.proxy.getRandomProxy(
        file=PROXY_FILE,
        split=True,
        random=True,
    )
"""


async def main(proxy, good_account_file: str) -> None:
    accounts: list = await parser.account.getAccounts(
        filename=parser.config.ACCOUNTS_FILE
    )
    for account in accounts:
        login_pass = account.strip().split(":")
        test = await parser.ebay_checker.login(
            account_data=login_pass,
            url=parser.config.EBAY_LOGIN_URL,
            bad_account_file=parser.config.BAD_ACCOUNTS_OUTPUT_FILE,
            good_account_file=good_account_file  # Передаем файл для записи успешных аккаунтов
        )
    return None


while __name__ == "__main__":
    logger.info("Parser started")
    thread: int = int(input("How many processes you need to run: "))
    use_proxy = input("Use proxy?(Y/n) ")
    if use_proxy == "Y":
        use_proxy = True
    else:
        use_proxy = False
    good_account_filename = input("Enter the filename for storing good accounts: ")

    if not isinstance(thread, int):
        print(f"Error input value ({thread})")

        if use_proxy == "Y" or "y":
            use_proxy = True
            break

        elif use_proxy == "N" or "n":
            use_proxy = False
            break

        else:
            print("Type Y or N")

        for _ in range(thread):
            multiprocessing.Process(target=asyncio.run(main(proxy=use_proxy, good_account_file=good_account_filename)))
            # asyncio.run(main())

    logger.warning("Parser shutdown")
