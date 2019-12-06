from django.conf.urls import url
from . import views
app_name = 'common'
urlpatterns = [
    url(r'^onDocumentUploaded/$', views.document_uploaded.as_view(),name='Docment_Upload'),
    url(r'^onPDFUpload/$', views.pdf_uploaded.as_view(),name='PDF_Upload'),
]
