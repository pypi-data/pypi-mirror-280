from asyncio import TimeoutError


class RequestTimeoutError(TimeoutError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        if args:
            self.log_message = args[0]
        else:
            self.log_message = "no log message"
        self._code = kwargs.get("code", 408)

    @property
    def code(self):
        return self._code

    def __str__(self):
        return self.log_message
