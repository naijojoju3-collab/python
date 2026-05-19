from django.shortcuts import get_object_or_404, render

from .models import Project, Skill


DEFAULT_PROJECTS = [
    {
        'title': 'Portfolio Website',
        'description': 'A clean personal portfolio built with Django, HTML, CSS, and JavaScript.',
        'technology': 'Python, Django, HTML, CSS, JavaScript',
        'link': 'https://www.djangoproject.com/',
        'image_url': 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=900&q=80',
    },
    {
        'title': 'Task Dashboard',
        'description': 'A simple dashboard concept for tracking tasks, progress, and daily priorities.',
        'technology': 'Django, SQLite, CSS Grid',
        'link': '',
        'image_url': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=900&q=80',
    },
    {
        'title': 'Weather App',
        'description': 'A frontend weather interface with a responsive layout and interactive controls.',
        'technology': 'HTML, CSS, JavaScript',
        'link': '',
        'image_url': 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=900&q=80',
    },
]

DEFAULT_SKILLS = [
    {'name': 'Python', 'proficiency': 85},
    {'name': 'Django', 'proficiency': 80},
    {'name': 'HTML & CSS', 'proficiency': 90},
    {'name': 'JavaScript', 'proficiency': 75},
]


def index(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()

    if not projects:
        projects = DEFAULT_PROJECTS

    if not skills:
        skills = DEFAULT_SKILLS

    context = {
        'projects': projects,
        'skills': skills,
    }
    return render(request, 'portfolio/index.html', context)


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    context = {
        'project': project,
    }
    return render(request, 'portfolio/project_detail.html', context)
