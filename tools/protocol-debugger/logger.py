"""
UMP Protocol Debug Logger

Provides lightweight logging for the protocol debugger.
"""

from datetime import datetime


class DebugLogger:

    def __init__(
        self,
        verbose: bool = False
    ):
        self.verbose = verbose

    def _log(
        self,
        level: str,
        message: str
    ):

        timestamp = (
            datetime.utcnow()
            .isoformat()
        )

        print(
            f"[{timestamp}] "
            f"[{level}] "
            f"{message}"
        )

    def info(
        self,
        message: str
    ):

        self._log(
            "INFO",
            message
        )

    def warning(
        self,
        message: str
    ):

        self._log(
            "WARNING",
            message
        )

    def error(
        self,
        message: str
    ):

        self._log(
            "ERROR",
            message
        )

    def debug(
        self,
        message: str
    ):

        if self.verbose:
            self._log(
                "DEBUG",
                message
            )
