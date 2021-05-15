from django.shortcuts import render


def doc(request):
	return render(request, 'doc/index.html', context={'schema_url': 'redoc/schema.yml'})
