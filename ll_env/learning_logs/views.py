from django.shortcuts import render

from .models import Topic

# the various routes and how to process & render the right data
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

def topic(request, topic_id):
    """show a single topic & its entries"""
    # queries the passed-in ID & returns the entry that matches, passes it to the correct route
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
