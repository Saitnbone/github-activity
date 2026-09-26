import sys
from api import fetch_events
from formatter import format_event


def terminal():
    if len(sys.argv) < 2:
        print("Usage: python main.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    events = fetch_events(username)

    if events is None:
        sys.exit(1)

    if not events:
        print(f"User '{username}' has no recent activity")
        return

    print(f"Recent activity for {username}:")
    for event in events:
        print(f"- {format_event(event)}")