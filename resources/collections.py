from mongoengine import Document, StringField, IntField

class ChistesCollection(Document):
    number = IntField(unique=True)
    chiste_texto = StringField(max_length=500)