from django.shortcuts import render
def home(request):
    # This is Python data (later, this will come from your database)
    context = {
        'username': 'Victor',
        'active_courses': 3,
        'topics': ['Django ORM', 'REST APIs', 'PostgreSQL', 'Celery']
    }
    
    # Pass the context dictionary as the third argument
    return render(request, 'core/home.html', context)

# Create your views here.
from django.shortcuts import render

def home(request):
    # Django automatically looks inside the 'templates' folder of any installed app
    return render(request, 'core/home.html')