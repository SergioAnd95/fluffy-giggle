import peewee
import peewee_async

db = peewee_async.PostgresqlDatabase(None)

class BaseModel(peewee.Model):

    """ Base model """

    class Meta:
        database = db