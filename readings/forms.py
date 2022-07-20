from django.forms import ModelForm, Textarea
from readings.models import Notepad


class NotepadForm(ModelForm):
    class Meta:
        model = Notepad
        fields = [
            "title",
            "note",
            "note_type"
        ]
        widgets = {
            'note': Textarea(attrs={'cols': 80, 'rows': 20}),
        }