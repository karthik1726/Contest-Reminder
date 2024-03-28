from twilio.rest import Client
import subprocess
import os

def execute_python_file(file_path):
   try:
      completed_process = subprocess.run(['python', file_path], capture_output=True, text=True)
      if completed_process.returncode == 0:
         message = client.messages.create(
         from_='whatsapp:+14155238886',
         body=completed_process.stdout,
         to='whatsapp:+918790888152'
         )
      else:
         print(f"Error: Failed to execute '{file_path}'.")
         print("Error output:")
         print(completed_process.stderr)
   except FileNotFoundError:
      print(f"Error: The file '{file_path}' does not exist.")


account_sid = 'ACafd4d15e6c064ba01364c1735bf7865f'
auth_token = '7209b3a932621ad118e908802549feef'
client = Client(account_sid, auth_token)
file_path = 'CodeForces.py'
execute_python_file(file_path)

print(message.sid)
