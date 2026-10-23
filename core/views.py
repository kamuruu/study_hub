from django.shortcuts import render


def home(request):
    context = {
        'username': 'Victor',
        'active_courses': 3,
        'topics': ['Django ORM', 'REST APIs', 'PostgreSQL', 'Celery']
    }
    return render(request, 'core/home.html', context)
def about(request):
    return render(request, 'core/about.html')