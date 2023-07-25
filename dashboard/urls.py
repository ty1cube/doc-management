from django.urls import path
from dashboard.views import DashboardView

app_name='dashboard'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard-page'),
    # path("documents/", DocumentView.as_view(), name='document'),
    # path("file-upload/", FileUploadView.as_view(), name='file-upload'),
]
