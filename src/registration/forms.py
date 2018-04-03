from django import forms
from .models import Event, MyUser, MyGroup
from django.core.exceptions import ValidationError

def check_for_valid_mobile_number(value):
    try:
        int(value)
        if len(value) != 10:
            raise ValidationError("Incorrect Mobile No.")
        if value[0] not in ('7', '8', '9'):
            raise ValidationError("Incorrect Mobile No.")
    except:
        raise ValidationError("Incorrect Mobile No.")

class MyEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"


class MyUserForm(forms.ModelForm):
    mobile = forms.CharField(validators=[check_for_valid_mobile_number])
    registered_events = forms.ModelMultipleChoiceField(queryset=Event.objects.filter(event_reg_type=1), widget=forms.CheckboxSelectMultiple(), required=True, error_messages={'required': 'Please select an event to register!'})
    class Meta:
        model = MyUser
        fields = "__all__"
'''
    def __init__(self, *args, **kwargs):
        super(MyUserForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['registered_events'].queryset = Event.objects.filter(event_reg_type=1)
'''


class MyGroupForm(forms.ModelForm):
    mobile = forms.CharField(validators=[check_for_valid_mobile_number])
    registered_events = forms.ModelMultipleChoiceField(queryset=Event.objects.filter(event_reg_type=2), widget=forms.CheckboxSelectMultiple(), required=True, error_messages={'required': 'Please select an event to register!'})
    persons = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'omg'}))
    class Meta:
        model = MyGroup
        fields = "__all__"
'''
    def __init__(self, *args, **kwargs):
        super(MyGroupForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['registered_events'].queryset = Event.objects.filter(event_reg_type=2)
'''

class MyContactForm(forms.Form):
    c_name = forms.CharField(label="Name:")
    c_email = forms.EmailField(label="Email ID:")
    c_message = forms.CharField(label="Message:", widget=forms.Textarea(attrs={'rows': 5, 'style': 'resize: none;' }))

