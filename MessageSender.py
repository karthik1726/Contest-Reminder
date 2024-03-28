from twilio.rest import Client

account_sid = 'ACafd4d15e6c064ba01364c1735bf7865f'
auth_token = '7209b3a932621ad118e908802549feef'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Your appointment is coming up on July 21 at 3PM',
  to='whatsapp:+918790888152'
)

print(message.sid)
