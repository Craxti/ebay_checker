from loguru import logger


async def getAccounts(filename: str) -> list:
    """ ### получаем все аккаунты в виде большого списка

    Args:
        `filename (str)`: местоположение файла

    Returns:
        `list`: `['login:password', 'login:password', 'login:password']`
    """
    with open(file=filename, mode="r", buffering=1) as file:
        accounts: list = file.read().split("\n")
        logger.info(
            "read new accounts ({acc} pcs)",
            acc=len(accounts),
        )
    return accounts


async def saveAccount(
        filename: str, login: str, password: str,
        user_id: str, country: str, cc: str, pp: str) -> str:
    """ ### сохраняет подходящие аккаунты
        в формате:
            `login:password / UserID:user_id / Country:country / CC:cc / PP:pp`
    Args:
        `filename (str)`: местоположение файла
        `login (str)`: логин
        `password (str)`: пароль
        `user_id (str)`: юзер айди
        `country (str)`: страна аккаунта
        `cc (str)`: cc
        `pp (str)`: pp

    Returns:
        `str`: `login:password / UserID:user_id / Country:country / CC:cc / PP:pp`
    """

    data: str = (
        f"{login}:{password} / "
        f"UserID: {user_id} / "
        f"Country: {country} / "
        f"CC: {cc} / PP: {pp}"
    )

    with open(file=filename, mode="w+", buffering=1) as file:
        file.write(data)

    logger.info(
        "new user({user}) has been recorded in {file}",
        file=file,
        user=login,
    )

    return data


async def saveBadAccount(filename: str, account: list) -> None:
    """ ### сохраняет плохие аккаунты

    Args:
        `filename (str)`: местоположение файла
        `account (list)`: данные аккаунта в формате `['login', 'pass']`

    Returns:
        _type_: _description_
    """
    with open(filename, "w+") as file:
        file.write(f"{account[0]}:{account[1]}\n")

    return logger.info(
        "bad account({user}) has been recorded in {file}",
        user=account,
        file=filename,
    )
