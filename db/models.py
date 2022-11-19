from mongoengine import Document, StringField, IntField

class ChistesCollection(Document):
    number = IntField()
    chiste_texto = StringField(max_length=500)

    