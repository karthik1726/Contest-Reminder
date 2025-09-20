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

file_path = "CodeForces.py"
account_sid = 'YOUR ACCOUNT ID'
auth_token = 'YOUR AUTENTICATION TOCKEN'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp: TWILIO SANDBOX NUMBER',
  body= execute_CodeForces_Info(file_path),
  to='whatsapp: YOUR MOBILE NUMBER'
)

print(message.sid)
