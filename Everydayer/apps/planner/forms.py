from django import forms
from .models import Task


class DateInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class EditForm(forms.ModelForm):
    class Meta:
        model = Task
        widgets = {'my_datetime_field': DateInput()}
        fields = ('task_title', 'task_description', 'task_date')
