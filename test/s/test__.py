from loguru import logger
import pathlib
import os

path = pathlib.Path(__file__).parent
os.chdir(path)


logger.add('log_test.log', format="{time:YYYY-MM-DD HH:mm:ss.SSS}, {level}, {message}",
                       rotation="128 KB",
                       compression='zip', encoding='cp1251')
logger.critical('hello')
