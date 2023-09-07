from loguru import logger
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
log_file = "log.log"

logpath = f"{os.path.abspath('log')}/{log_file}"

logger.add(
	logpath,                    				# - имя файла
	colorize=True,
	format="{time} {module} {level} {message}",  	# - формат записи
	level="DEBUG",                     				# - уровень действия
	rotation="100 KB",                   			# - барьер для действия
	compression="zip",                   			# - зиповать по достижению барьера
#	serialize=True                      			# - сохранять в формат json
)

info = logger.info
error = logger.error