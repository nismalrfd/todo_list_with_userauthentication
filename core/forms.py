from django.forms import ModelForm

from core.models import Todo


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title','complete']