from django.forms import ModelChoiceField

class CouponModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name + " | -" + str(obj.discount) + "%"