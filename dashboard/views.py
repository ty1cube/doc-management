from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
from django.contrib.auth.decorators import login_required


class DashboardView(TemplateView):
    	template_name = 'dashboard/dashboard.html'

# class DashboardView(View):
#     def get(self, request, *args, **kwargs):
		
	# template_name = 'dashboard/dashboard.html'
	
# class DocumentView(TemplateView):
#     	template_name = 'dashboard/documents.html'

# class FileUploadView(TemplateView):
#     	template_name = 'dashboard/file-upload.html'
