from googleapiclient.discovery import build

from auth import authenticate_gmail


def get_emails():
    creds = authenticate_gmail()
    service = build("gmail", "v1", credentials=creds)
    results = service.users().messages().list(
        userId="me",
        labelIds=["INBOX"],
        maxResults=5
    ).execute()

    messages = results.get("messages", [])

    emails = []

    for msg in messages:
        message = service.users().messages().get(
            userId="me",
            id=msg["id"]
        ).execute()

        # headers = message["payload"]["headers"]

        # for h in headers:
        #     if h["name"] == "Subject":
        #         emails.append(f"Subject: {h["value"]}, ")
        #                         "Content:"
        emails.append(message["snippet"])
    return emails

