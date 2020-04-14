from twilio.rest import Client



# DANGER! This is insecure. See http://twil.io/secure
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hi there!',
                              from_='+1twilioprovidednumber',
                              to='+1yournum'
                          )

print(message.sid)