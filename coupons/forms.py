from django import forms
from account.models import Profile
from .models import Coupon
from .fields import CouponModelChoiceField



class CouponApplyForm(forms.Form):
	coupon = CouponModelChoiceField(queryset=None, required=False, empty_label=None)


	def __init__(self, *args, **kwargs):
		self.user = (kwargs.pop('user', None))
		super(CouponApplyForm, self).__init__(*args, **kwargs)
		self.fields['coupon'].queryset = Coupon.objects.filter(
											profiles=Profile.objects.get(
												user=self.user),
											level__lte = Profile.objects.get(
												user=self.user).level
											)


