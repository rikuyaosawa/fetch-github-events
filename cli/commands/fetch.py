import requests
from config import GITHUB_API_URL


def fetch_user_events(username: str, limit: int):
    url = f"{GITHUB_API_URL}/users/{username}/events"
    response = requests.get(url)

    if response.status_code == 200:
        events = response.json()[:limit]
        for event in events:
            if event["type"] == "WatchEvent":
                print(f"Starred {event['repo']['name']}")
            elif event["type"] == "PushEvent":
                print(
                    f"Pushed {event['payload']['size']} commits to {event['repo']['name']}"
                )

    else:
        print(f"Error: {response.status_code} - {response.json()}")
