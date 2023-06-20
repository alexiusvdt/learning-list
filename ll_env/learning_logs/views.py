from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm

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

def new_topic(request):
    """add a new topic"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = TopicForm()
    else:
        # POST submitted; process
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
        
    # display blank/invalid
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
