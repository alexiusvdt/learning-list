from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def check_topic_owner(topic, request):
    if topic.owner != request.user:
            raise Http404    
        

def index(request):
    """the home page for learning log"""
    # take the request and render at this path
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """show all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    # when building page that uses data(db query), pass context var to render() as well as the request obj itself
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """show a single topic & its entries"""
    # queries the passed-in ID & returns the entry that matches, passes it to the correct route
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(topic, request)
    
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """add a new topic"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = TopicForm()
    else:
        # POST submitted; process
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            form.save()
            return redirect('learning_logs:topics')
        
    # display blank/invalid
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """add a new entry for a given topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # no data; blank form
        form = EntryForm()
    else:
        # POST data; process
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
        
    # display blank/invalid
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(topic, request)

    if request.method != 'POST':
        # no data; blank form
        form = EntryForm(instance=entry)
    else:
        # POST data; process
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
        
    # display blank/invalid
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)