user_state = {}

def update_user(log):
    user = log["user"]

    if user not in user_state:
        user_state[user] = {
            "http_requests": 0,
            "cloud_job_visits": 0
        }

    user_state[user]["http_requests"] += 1

    url = str(log["url"]).lower()

    if any(site in url for site in [
        "dropbox",
        "drive.google",
        "mega",
        "box.com",
        "onedrive"
    ]):
        user_state[user]["cloud_job_visits"] += 1

    return user_state[user]