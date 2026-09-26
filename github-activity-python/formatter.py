def format_event(event):
    """Convert a GitHub event into a human-readable string."""
    event_type = event.get("type")
    repo_name = event.get("repo", {}).get("name", "unknown")
    payload = event.get("payload", {})

    if event_type == "PushEvent":
        commits = payload.get("commits", [])
        count = len(commits)
        word = "commit" if count == 1 else "commits"
        return f"Pushed {count} {word} to {repo_name}"

    if event_type == "IssuesEvent":
        action = payload.get("action", "did something with")
        return f"{action.capitalize()} a new issue in {repo_name}"

    if event_type == "WatchEvent":
        return f"Starred {repo_name}"

    if event_type == "ForkEvent":
        return f"Forked {repo_name}"

    if event_type == "CreateEvent":
        ref_type = payload.get("ref_type", "repository")
        return f"Created {ref_type} in {repo_name}"

    if event_type == "PullRequestEvent":
        action = payload.get("action", "did something with")
        return f"{action.capitalize()} a pull request in {repo_name}"

    if event_type == "IssueCommentEvent":
        return f"Commented on an issue in {repo_name}"

    if event_type == "DeleteEvent":
        ref_type = payload.get("ref_type", "ref")
        return f"Deleted {ref_type} in {repo_name}"

    return f"{event_type} in {repo_name}"