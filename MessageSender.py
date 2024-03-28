from twilio.rest import Client
import subprocess

output = subprocess.check_output(["python", "other_script.py"], text=True)

account_sid = 'ACafd4d15e6c064ba01364c1735bf7865f'
auth_token = '7209b3a932621ad118e908802549feef'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body=output.script(),
  to='whatsapp:+918790888152'
)

print(message.sid)
