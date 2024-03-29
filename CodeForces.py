import requests
from datetime import datetime

def get_upcoming_contests():
    # Codeforces API endpoint for contest list
    url = "https://codeforces.com/api/contest.list"
    # Make the GET request to fetch contest list
    response = requests.get(url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        contest_list = response.json()
        # Check if the response contains the list of contests
        if "result" in contest_list:
            # Filter contests to include only upcoming contests
            upcoming_contests = [contest for contest in contest_list["result"] if contest["phase"] == "BEFORE" and "Codeforces Round" in contest["name"] and "Div" in contest["name"]]
            #div2_rounds = [contest for contest in contest_list["result"] if "Codeforces Round" in contest["name"] and "Div" in contest["name"]]
            return upcoming_contests
        else:
            return None
    else:
        return None
# Get upcoming contests
upcoming_contests = get_upcoming_contests()



if upcoming_contests:
    print("Upcoming Contests:")
    for contest in upcoming_contests:
        # Convert Unix timestamp to datetime object
        start_time = datetime.fromtimestamp(contest["startTimeSeconds"])
        # Print contest name and start time
        print(f"{contest['name']}: {start_time}")
else:
    print("Failed to fetch upcoming contests.")
