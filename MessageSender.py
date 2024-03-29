import os
import subprocess
from twilio.rest import Client

def execute_CodeForces_Info(file_path):
    try:
        completed_process = subprocess.run(['python',file_path],capture_output=True,text=True)
        if completed_process.returncode == 0:
            print("Successfully Exicuted")
            return completed_process.stdout
        else:
            print(f"Error: Failed to execute'{file_path}'.")
            print(f"Error Output:")
            print(completed_process.stderr)
    except FileNotFoundError:
        print(f"Error: The file'{file_path}' does not exist.")

file_path = "C:\\Users\\karth\\OneDrive\\Desktop\\Contest Reminder\\ContestInfo\\codeforces.py"
account_sid = 'ACafd4d15e6c064ba01364c1735bf7865f'
auth_token = '7209b3a932621ad118e908802549feef'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body= execute_CodeForces_Info(file_path),
  to='whatsapp:+917075832552'
)

print(message.sid)
