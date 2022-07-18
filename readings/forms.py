from django.forms import ModelForm, Textarea
from readings.models import Notepad


class NotepadForm(ModelForm):
    class Meta:
        model = Notepad
        fields = [
            "title",
            "note",
        ]
        widgets = {
            'note': Textarea(attrs={'cols': 80, 'rows': 20}),
        }