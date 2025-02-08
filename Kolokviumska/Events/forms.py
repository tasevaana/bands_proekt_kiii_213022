from django import forms
from Events.models import Event


class AddForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['user']
        widgets = {

        }

    def __init__(self, *args, **kwargs):
        super(AddForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            if visible.name == "isOpen":
                visible.field.widget.attrs["class"] = "form-check-input"
