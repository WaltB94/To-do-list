from django import forms


class AgregarTarea(forms.Form):
    tarea = forms.CharField()

class CompletarTarea(forms.Form):
    tareas_completadas = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        tareas = kwargs.pop('tareas', [])  # Obtener la lista de tareas del argumento 'tareas'
        super(CompletarTarea, self).__init__(*args, **kwargs)
        self.fields['tareas_completadas'].choices = [(i, tarea) for i, tarea in enumerate(tareas)]
