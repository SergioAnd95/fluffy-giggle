import peewee

from db.models import BaseModel

class User(BaseModel):

    username = peewee.CharField(unique=True, index=True, max_length=20, null=False)
    password = peewee.CharField(max_length=16, null=False)
    email = peewee.CharField(max_length=20, null=False)

    def __str__(self):
        return self.username