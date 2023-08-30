from datetime import timedelta

from django import forms

from .models import ToDoItem


class ToDoItemForm(forms.ModelForm):
    class Meta:
        fields = ['description', 'label', 'comment', 'dashboard_column',
                  'start_date', 'due_date', 'time_estimate_hours']
        models = ToDoItem

    def clean(self):
        start_date = self.cleaned_data.get('start_date')
        due_date = self.cleaned_data.get('due_date')
        estimated_hours = self.cleaned_data.get('time_estimate_hours')

        if start_date and due_date:
            if start_date > due_date:
                raise forms.ValidationError(
                    'Start date should be before due date!!')

        if start_date + timedelta(hours=estimated_hours) > due_date:
            raise forms.ValidationError('Inconsistent dates and estimation. '
                                        'start_date + time_estimate_hours goes '
                                        'after due_date')

        return self.cleaned_data
