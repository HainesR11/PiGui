import logging

def logger():

        baseLogger = logging.getLogger("my logger")

        # link handler to logger
        baseLogger.addHandler(logging.StreamHandler())

        # Set logging level to the logger
        baseLogger.setLevel(logging.DEBUG) # <-- THIS!1

        return baseLogger


