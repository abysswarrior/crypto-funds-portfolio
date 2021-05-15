from django.urls import path
from django.views.generic import TemplateView

app_name = 'doc'

urlpatterns = [
	path('', TemplateView.as_view(
			template_name='docs/index.html',
			extra_context={'schema_url': 'redoc/schema.yml'}
		), name='redoc'),
]
