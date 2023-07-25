from django.db import models
from authentication.models import CustomUser


# def user_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     return "user_{0}/{1}".format(instance.user.id, filename)

class Document(models.Model):
    FORMAT_CHOICES = [
        ('pdf', 'PDF'),
        ('docx', 'DOCX'),
        ('txt', 'TXT'),

        # Add more format choices as needed
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    document_format = models.CharField(max_length=10, choices=FORMAT_CHOICES)
    folder_name = models.CharField(max_length=50, blank=True,null=True )
    file_field =  models.FileField(upload_to="media/")
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='owned_documents')
    shared_with = models.ManyToManyField(CustomUser, related_name='shared_documents', blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title