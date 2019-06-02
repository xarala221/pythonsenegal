from django.views.generic.list import ListView
from .models import Utility


class ResourceListView(ListView):
    template_name = 'resources/resource-list.html'
    queryset = Utility.objects.all()
    context_object_name = 'resources'
