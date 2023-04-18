import random

from loguru import logger


async def getProxies(filename: str) -> list:
    """### получаем прокси

    Args:
        `filename (str)`: Расположение файла

    Returns:
        `list`: все прокси из указанного файла в виде большого списка
        `['ip:port', 'ip:port', 'ip:port']`
    """
    with open(file=filename, mode="r", buffering=1) as file:
        proxies: list = file.read().split("\n")
        logger.info(
            "read new proxies ({proxy} pcs)",
            proxy=len(proxies),
        )
    return proxies


async def splitProxy(proxy: str) -> list:
    """### разделяем прокси из формата `ip:port` в список

    Args:
        `proxy (str)`: прокси

    Returns:
        `list`: список `['ip', 'port']`
    """
    return proxy.split(":")


async def getProxy(
        file: str,
        split: bool = True,
        random_proxies: bool = False,
) -> str:
    """ ### Получаем прокси `(1шт)`

    Args:
        `file (str)`: файл c прокси
        `split (bool)`: по умолчанию True
        `random_proxies (bool)`: по умолчанию False

    Returns:
        `str:`
        если аргумент `split == True`, то получаем прокси в виде списка `['ip', 'port']`

        ecли аргумент `random == True`, то мы получаем рандом прокси в формате `ip:proxy`

        если аргумент `split и random == True`, то получаем рандом прокси в виде списка `['ip', 'port']`
    """
    proxies: list = await getProxies(filename=file)
    random_proxy: list = random.choice(proxies)

    if split and random_proxies:
        return await splitProxy(proxy=random_proxy)

    elif split:
        return await splitProxy(proxy=random_proxy)

    elif random_proxies:
        return random.choice(proxies)
