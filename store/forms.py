from django import forms

PAYMENT_CHOICES= (
    ('S','Stripe'),
    ('P','Paypal')
)

class CheckoutForm(forms.Form):
    payment_option=forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_CHOICES)
