import logging


def config_logging() -> None:
    """
    Configures debugging log.
    """
    logging.basicConfig(
        filename="pyfilefinder_debugger.log",
        filemode="w",
        encoding="utf-8",
        level=logging.DEBUG,
    )
