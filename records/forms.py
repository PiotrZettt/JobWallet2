from django import forms
from .models import Operation, Part, Customer, Wallet


class AddOperationModelForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = (
            'operation_name',
            'comments',
            'operation_status'
        )


class CreateJobWalletModelForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = (
            'order_number',
            'order_quantity',
            'customer_name',
            'part_FG',
            'part_id',
            'pack_number',
            'traceability_required'
        )


class SearchForm(forms.Form):
    # customer = forms.CharField(required=False)
    # part_FG = forms.CharField(required=False)
    serial_number = forms.CharField(required=False)
    # operator = forms.CharField(required=False)
    # date = forms.CharField(required=False)



