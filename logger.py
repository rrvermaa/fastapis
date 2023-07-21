import logging


logger = logging.getLogger("uvicorn.error")
logger.propagate = False

class NameFilter(logging.Filter):
    def filter(self, record):
        if record.name == 'uvicorn.error':
            record.name = 'fastapi'
        return True

name_filter = NameFilter()
# console_handler.addFilter(name_filter)

