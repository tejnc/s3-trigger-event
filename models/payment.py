from mongoengine.fields import DateTimeField, DictField, IntField, StringField
from mongoengine_goodjson import Document


# Payment information of meroshare and demat
class Payment(Document):
    amount = IntField()
    medium = StringField(
        choices=("Khalti", "Esewa", "EPay"),
    )
    years = IntField(default=1)
    pay_for = StringField(choices=("demat", "demat_with_meroshare", "meroshare"))
    extra = DictField()
    created_at = DateTimeField()
    updated_at = DateTimeField()
    meta = {"collection": "payments"}
