import logging

logger = logging.getLogger("component")


class DummyClient(object):
    def __init__(self, err):
        self.description = err

    def __getattr__(self, item):
        logger.warning(self.description)
        raise ModuleNotFoundError
