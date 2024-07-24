from django import forms

from .cart import Cart

PRODUCT_QUANTITY = [(i,str(i)) for i in range(1,21)]



class ProductCartFormAdd(forms.Form):

    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY,
        coerce=int
    )

    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )