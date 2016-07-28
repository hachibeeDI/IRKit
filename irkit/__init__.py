from logging import getLogger, StreamHandler, Formatter, WARN

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(WARN)
handler.formatter = Formatter(
    fmt='%(levelname)s %(asctime)s: %(message)s',
    datefmt='%Y/%m/%d %p %I:%M:%S',
)
logger.setLevel(WARN)
logger.addHandler(handler)
