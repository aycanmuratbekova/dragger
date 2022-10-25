from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import TemplateView

from .models import Accessories


class ProjectIndexView(TemplateView):
    template_name = "project_index.html"

    def get_context_data(self, **kwargs):
        accessories = Accessories.objects.all()
        context = {
            'projects': accessories
        }
        return context


class ProjectDetailView(DetailView):

    model = Accessories
    template_name = "project_detail.html"
    context_object_name = 'project'

# def project_index(request):
#     accessories = Accessories.objects.all()
#     context = {
#         'projects': accessories
#     }
#     return render(request, 'project_index.html', context)
#
#
# def project_detail(request, pk):
#     accessor = Accessories.objects.get(id=pk)
#     context = {
#         'project': accessor
#     }
#     return render(request, 'project_detail.html', context)
