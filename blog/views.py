from django.shortcuts import render, get_object_or_404

from blog.models import Project


def about(request):
	return render(request, 'about.html')

def projects(request):
	projects = Project.objects.all()
	context = {'projects': projects}
	return render(request, 'projects.html', context)

def project_detail(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	context = {'project': project}
	return render(request, 'project.html', context)
