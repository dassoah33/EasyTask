from django.shortcuts import render, redirect
from feed.models import Task
from django.utils import timezone
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    if request.method == 'POST':
        title = request.POST['title']
        completed = 'completed' in request.POST  # Convertir en booléen
        user = request.user

        # Utilisateur par défaut si l'utilisateur n'est pas authentifié
        if request.user.is_authenticated:
            user = request.user
        else:
            user = User.objects.get(id=1)  # Utilisateur par défaut avec l'ID 1

        # Créer la tâche avec les informations récupérées
        Task.objects.create(title=title, completed=completed, user=user, created_at=timezone.now())

        return redirect('index')

    # Récupérer les tâches et les afficher dans l'ordre de création
    context = {}
    context['tasks'] = Task.objects.order_by('-created_at')

    return render(request, 'index.html', context=context)
