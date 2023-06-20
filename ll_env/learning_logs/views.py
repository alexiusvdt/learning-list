from django.shortcuts import render

from .models import Topic

def index(request):
    """the home page for learning log"""
    # take the request and render at this path
    return render(request, 'learning_logs/index.html')

def topics(request):
    """show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    # when building page that uses data(db query), pass context var to render() as well as the request obj itself
    return render(request, 'learning_logs/topics.html', context)