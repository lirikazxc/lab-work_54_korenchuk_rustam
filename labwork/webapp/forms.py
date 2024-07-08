from django import forms


class ProductSearchForm(forms.Form):
    query = forms.CharField(label='search', max_length=54)
