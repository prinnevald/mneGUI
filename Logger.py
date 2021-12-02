import contextlib
import threading

class Logger():
    def logger_loop(self, logger):
        contextlib.redirect_stdout(logger)

    def __init__(self, logger):
        thread = threading.Thread(target = self.logger_loop, args = logger)
        thread.start()