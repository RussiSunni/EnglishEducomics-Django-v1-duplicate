from django import forms


class TradeForm(forms.Form):
    trade = forms.CharField(label='You respond', max_length=100)