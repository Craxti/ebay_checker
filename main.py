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


async def main(proxy: bool) -> None:
    accounts: list = await parser.account.getAccounts(
        filename=parser.config.ACCOUNTS_FILE
    )
    for number in range(len(accounts)):
        account: list = accounts[number]
        login_pass = account.split(":")
        test = await parser.ebay_checker.login(
            account_data=login_pass,
            url=parser.config.EBAY_LOGIN_URL,
            bad_account_file=parser.config.BAD_ACCOUNTS_OUTPUT_FILE,
        )
    return None


while __name__ == "__main__":
    logger.info("Parser started")
    thread: int = input("How many processes you need to run: ")
    use_proxy: str = input("Use proxy?(Y/n) ")

    if not isinstance(thread, int):
        print(f"Error input value ({thread})")

        if use_proxy == "Y" or "y":
            use_proxy: bool = True
            break

        elif use_proxy == "N" or "n":
            use_proxy: bool = False
            break

        else:
            print("Type Y or N")

        for i in thread:
            multiprocessing.Process(target=asyncio.run(main(proxy=use_proxy)))
            # asyncio.run(main())

    logger.warning("Parser shutdown")
