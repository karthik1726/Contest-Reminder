import requests

# Replace 'YOUR_ACCESS_TOKEN' with your actual access token
access_token = 'YOUR_ACCESS_TOKEN'

# Specify the API endpoint URL
url = 'https://api.codechef.com/users/{username}'

# Replace '{username}' with the CodeChef username you want to retrieve information for
username = 'example_username'

# Define request headers with the access token
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# Make the GET request
response = requests.get(url.format(username=username), headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    user_data = response.json()
    # Do something with the user data
    print(user_data)
else:
    # Print an error message if the request was not successful
    print(f'Error: {response.status_code}')
