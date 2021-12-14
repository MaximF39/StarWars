import pathlib

from . import *
import redis
from loguru import logger


class Player:
    id: int
    name: str
    passwd: str
    clan: str
    clan_id: int
    credit: int
    bonus: int
    planet: int
    location: int
    lvl_exp: int
    count_exp: int
    lvl_stat: int
    count_stat: int
    reg_bool: bool

    def __init__(self, name):
        self.name = name
        self._init_log()
        redis_ = self._redis_open()
        self.reg_bool = bool(redis_.get(name))
        self._redis_close(redis_)

    @staticmethod
    def _redis_open() -> redis.Redis:
        """config_redis.host config_redis.port config_redis.db"""
        return redis.Redis(host=host, port=port, db=db)

    @staticmethod
    def _redis_close(redis_client: redis.Redis) -> None:
        redis_client.close()

    def _init_log(self):
        logger.add(pathlib.Path(__file__).parent.joinpath('PlayerRes').joinpath(f'{self.name}.log'),
                   format="{time:YYYY-MM-DD HH:mm:test.SSS}, {level}, {message}",
                   rotation="16 KB",
                   compression='zip', encoding='cp1251')

    def entry(self, passwd: str) -> bool:
        redis_ = self._redis_open()
        passwd_original = redis_.get(self.name).decode()
        self._redis_close(redis_)
        if passwd == passwd_original:
            logger.debug(f'Пользователь {self.name} вошёл.')
            return True
        else:
            logger.info(f'Пользователь {self.name} не вошёл.')
            return False

    def reg(self, passwd: str) -> None:
        redis_ = self._redis_open()
        self.reg_bool = redis_.get(self.name)
        if self.reg_bool:
            raise 'Пользователь зарегестрирован'
        redis_.set(name=self.name, value=passwd)
        self._redis_close(redis_)
        self.name = self.name
        logger.critical(f'Пользователь {self.name} зарегистрирован')
        self.reg_bool = True

    def delete(self) -> None:
        redis_ = self._redis_open()
        redis_.delete(self.name)
        logger.critical(f'Пользователь {self.name} удалён')
        self._redis_close(redis_)

    def __del__(self):
        """ Выполняется код при удалений класса"""
        pass
