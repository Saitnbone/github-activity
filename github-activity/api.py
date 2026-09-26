import requests


def fetch_events(username):
    url = f"https://api.github.com/users/{username}/events"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "github-activity-cli",
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        if e.response.status_code == 404:
            print(f"User '{username}' not found")
        elif e.response.status_code == 403:
            print("GitHub API rate limit exceeded. Try again later.")
        else:
            print(f"HTTP error: {e.response.status_code}")
    except requests.Timeout:
        print("Request timed out")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    return None