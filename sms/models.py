from django.db import models
from twilio.rest import Client

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=200)
    telephone = models.CharField(max_length=15)
    
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        '+233200036801' ==  self.telephone
        account_sid = "AC3a679509db2af4b65820824632cb092c"
        auth_token = '5a63db8ca25273cfc24fb7f0900221a8'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
        body=f"Congratulations {self.name} you have successfully created a new account",
        from_="+12708176451",
        to='+233200036801'
            )

        print(message.sid)
        return super().save(*args, **kwargs)