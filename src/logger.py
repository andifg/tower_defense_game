import logging

# create logger
logger = logging.getLogger('Pygame')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()

file = logging.FileHandler('src/logs/logging.example', mode='w', encoding=None, delay=False, errors=None)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')

# add formatter to ch
ch.setFormatter(formatter)
file.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)
logger.addHandler(file)
