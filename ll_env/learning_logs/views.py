from django.shortcuts import render


def index(request):
    """the home page for learning log"""
    # take the request and render at this path
    return render(request, 'learning_logs/index.html')