from twilio.rest import Client 
 
account_sid = [Accound_SID]
auth_token = [AuthToken]
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+15742064540',  
                              body='Helloooooo it\'s me again',      
                              to='+447398303046' 
                          ) 
 
print(message.sid)
