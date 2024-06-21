from .base import BaseMachine


class FunctionMachine(BaseMachine):
    def __init__(self, retries=3, timeout=1, **kwargs):
        self._retries = retries
        self._retries_remaining = self._retries
        self._timeout = timeout
        super().__init__(
            states=[
                {
                    "name": "Request",
                    "on_enter": ["_reset", "_request"],
                    "timeout": timeout,
                    "on_timeout": "_retry",
                },
                {
                    "name": "Retry",
                    "on_enter": "_request",
                    "timeout": timeout,
                    "on_timeout": "_retry",
                },
                {
                    "name": "Failure",
                    "on_enter": "_log_failure",
                },
                {
                    "name": "Success",
                },
            ],
            initial="Request",
            transitions=[
                {
                    "source": "Request",
                    "dest": "Retry",
                    "after": "_log_retry",
                    "trigger": "_retry",
                    "conditions": "_has_retries",
                },
                {
                    "source": "Retry",
                    "dest": "Retry",
                    "after": "_log_retry",
                    "trigger": "_retry",
                    "conditions": "_has_retries",
                },
                {
                    "source": "Request",
                    "dest": "Failure",
                    "trigger": "_retry",
                    "unless": "_has_retries",
                },
                {
                    "source": "Retry",
                    "dest": "Failure",
                    "trigger": "_retry",
                    "unless": "_has_retries",
                },
                {
                    "source": "Request",
                    "dest": "Success",
                    "trigger": "success",
                },
                {
                    "source": "Retry",
                    "dest": "Success",
                    "trigger": "success",
                },
                {
                    "source": "Failure",
                    "dest": "Request",
                    "trigger": "resume",
                },
            ],
            **kwargs,
        )

    def _request(self):
        self._retries_remaining -= 1
        self.request()

    def request(self):
        raise NotImplementedError("This method must be defined in a subclass")

    def _reset(self):
        self._retries_remaining = self._retries

    def _has_retries(self):
        return self._retries_remaining > 0

    def _log_failure(self):
        self._logger.warning(
            f"Transitioned to state {self.state} as an appropriate response was not recieved in {self._timeout}s."
        )

    def _log_retry(self):
        self._logger.warning(
            f"Retrying request in state {self.state} after {self._timeout}s."
        )
