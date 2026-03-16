import time

from agents.email_reader import get_emails
from graph import build_graph
from logger import get_logger

logger = get_logger(__name__)

app = build_graph()


def run_agent():
    logger.info("AI Email Agent started")

    while True:

        try:

            emails = get_emails()

            for email in emails:
                logger.info(f"Processing email--> {email}")

                result = app.invoke(
                    {
                        "email": email,
                        "analysis": "",
                        "action": ""
                    }
                )

                logger.info("Agent finished one run")

        except Exception as e:

            logger.exception("Agent error")

        # Wait before checking new emails
        time.sleep(300)  # 5 minutes


if __name__ == "__main__":
    run_agent()
