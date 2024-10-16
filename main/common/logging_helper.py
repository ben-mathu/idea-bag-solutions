import logging.handlers
from logging import getLogger, DEBUG, WARN, INFO, ERROR, Formatter

TRACE = 5  # TRACE log level


def main():
    # default_handler = logging.handlers.BufferingHandler(3)  # buffers logging records in memory
    logger = getLogger(__file__)  # Creates a logger
    level = DEBUG
    # 
    # formatter = Formatter("%(message)s\n")
    # 
    default_handler = logging.StreamHandler()  # logger for streams
    default_handler.setLevel(level)
    # default_handler.setFormatter(formatter)
    logger.addHandler(default_handler)
    # 
    # # def trace(self, message, *args, **kwargs):
    # #     if self.isEnabledFor(TRACE):
    # #         self._log(TRACE, message, args, **kwargs)
    # # 
    # # logging.addLevelName(TRACE, "TRACE")
    # # logging.Logger.trace = trace
    # 
    # logging.Logger.warn = logging.Logger.warning
    
    logger.debug("This is an important message from the past!")
    logging.debug("This is an important message from the past!")
    print("Help please")


if __name__ == "__main__":
    main()
    