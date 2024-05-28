import aiohttp
import asyncio
import random
import time

from loguru import logger


async def testProxy(proxy: str) -> bool:
    """Проверка доступности прокси.

    Args:
        proxy (str): Прокси в формате 'ip:port'.

    Returns:
        bool: True, если прокси доступен, иначе False.
    """
    ip, port = proxy.split(":")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("http://example.com", proxy=f"http://{ip}:{port}") as response:
                if response.status == 200:
                    logger.info("Proxy {proxy} is working", proxy=proxy)
                    return True
                else:
                    logger.warning("Proxy {proxy} returned status code {code}", proxy=proxy, code=response.status)
                    return False
    except Exception as e:
        logger.error("Failed to test proxy {proxy}: {error}", proxy=proxy, error=str(e))
        return False


async def getProxies(filename: str) -> list:
    """Получаем список прокси из файла.

    Args:
        filename (str): Расположение файла с прокси.

    Returns:
        list: Список прокси в формате ['ip:port', 'ip:port', ...].
    """
    try:
        with open(filename, "r") as file:
            proxies = file.read().strip().split("\n")
            logger.info("Read {count} proxies from file {filename}", count=len(proxies), filename=filename)
        return proxies
    except FileNotFoundError:
        logger.error("File not found: {filename}", filename=filename)
        return []
    except Exception as e:
        logger.error("Failed to read proxies from file {filename}: {error}", filename=filename, error=str(e))
        return []


async def getAvailableProxies(filename: str) -> list:
    """Получаем доступные прокси из файла.

    Args:
        filename (str): Расположение файла с прокси.

    Returns:
        list: Список доступных прокси в формате ['ip:port', 'ip:port', ...].
    """
    try:
        proxies = await getProxies(filename)
        available_proxies = []
        for proxy in proxies:
            if await testProxy(proxy):
                available_proxies.append(proxy)
        return available_proxies
    except Exception as e:
        logger.error("Failed to get available proxies from file {filename}: {error}", filename=filename, error=str(e))
        return []


async def getRandomProxy(
    filename: str,
    split: bool = True,
    random_proxies: bool = False
) -> str:
    """Получаем случайный прокси.

    Args:
        filename (str): Файл с прокси.
        split (bool): Разделять ли прокси на ip и port.
        random_proxies (bool): Получить ли случайный прокси.

    Returns:
        str: Прокси в формате 'ip:port'.
    """
    proxies = await getProxies(filename)
    if random_proxies:
        proxy = random.choice(proxies)
    else:
        proxy = proxies[0]  # Берем первый прокси из списка
    if split:
        return proxy.split(":")
    return proxy


async def autoUpdateProxies(
    filename: str,
    update_interval: int = 3600  # 1 час
):
    """Автоматическое обновление списка прокси.

    Args:
        filename (str): Файл с прокси.
        update_interval (int): Интервал обновления в секундах.
    """
    while True:
        logger.info("Updating proxies...")
        proxies = await getAvailableProxies(filename)
        with open(filename, "w") as file:
            file.write("\n".join(proxies))
        logger.info("Proxies updated. Sleeping for {interval} seconds...", interval=update_interval)
        await asyncio.sleep(update_interval)

