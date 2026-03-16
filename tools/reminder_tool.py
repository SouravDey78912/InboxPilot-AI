import json

from logger import get_logger


logger = get_logger(__name__)


def create_reminder(text):
    logger.info(f"Riminder text --> {text}")
    with open("reminders.txt", "a") as f:

        if isinstance(text, dict):
            text = json.dumps(text)

        f.write(text + "\n")

    logger.info("Reminder saved")