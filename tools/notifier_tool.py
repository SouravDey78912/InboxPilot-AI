from plyer import notification

from logger import get_logger


logger = get_logger(__name__)


def notify_user(message):
    logger.info("Sending desktop notification")
    notification.notify(
        title="AI Email Agent",
        message=message,
        timeout=10
    )