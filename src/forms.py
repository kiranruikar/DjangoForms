from django import forms


class SearchForm(forms.Form):
    name = forms.CharField()
    boolean = forms.BooleanField()
    integer = forms.IntegerField(max_value=5)
    email = forms.EmailField()

    def clean_integer(self, *args, **kwargs):
        integer = self.cleaned_data.get("integer")
        if len(str(integer)) < 1:
            raise forms.ValidationError("length Less than 4")
        return integer
