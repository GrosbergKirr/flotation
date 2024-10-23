import sys

from loguru import *

def SetLogger(configService):
    logger.configure(handlers=[
        # {
        #     "sink": "file.log",  # Логирование в файл
        #     "format": "{time} {level} {message}",  # Формат логов
        #     "level": configService.logLevel,  # Уровень логирования
        #     "rotation": "10 MB",  # Ротация файла, если его размер превышает 10 MB
        #     "compression": "zip",  # Сжатие логов после ротации
        # },
        {
            "sink": sys.stdout,  # Логирование в консоль
            "format": "<green>{time}</green> <level>{message}</level>",
            "level": configService.logLevel,  # Уровень логирования для консоли
        }
    ])
    return logger
