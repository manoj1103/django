from django import forms


from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'EMP_ID',
            'EMPLOYEE_NAME',
            'SALARY',
            'DEPARTMENT',
            'DOB',
            'DOJ',



        ]
