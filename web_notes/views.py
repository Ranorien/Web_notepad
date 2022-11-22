from django.shortcuts import render, redirect
from .models import Topic, Note
from .forms import TopicForm, NoteForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

def index(request):
    """Homepage of application Web notes"""
    return render(request, 'web_notes/index.html')


@login_required
def topics(request):
    """shows topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('-date_added')
    context = {'topics': topics}

    return render(request, 'web_notes/topics.html', context)

@login_required
def topic(request, topic_id):
    """shows single topic and related notes"""
    topic = Topic.objects.get(id=topic_id)

    check_topic_owner(topic, request)
    
    # there are 2 ways to select data from the second table: note_set or filter(). 
    # "note" - is dymanic name, generated for object Note, described in models.py
    notes = topic.note_set.order_by('-date_added')

    # # get is limited to 1 result, if you're making a query that matches more than one element you should use filter
    # notes = Note.objects.filter(topic_id=topic.id)

    context = {'topic': topic, 'notes': notes}

    return render(request, 'web_notes/topic.html', context)

@login_required
def new_topic(request):
    """New topic creation"""
    if request.method != 'POST':
        # data was not sent, empty form
        form = TopicForm()
    else:
        # data was sent
        form = TopicForm(data=request.POST)
        if form.is_valid():
            newtopic = form.save(commit=False)
            newtopic.owner = request.user
            newtopic.save()
            return redirect('web_notes:topics')

    # show form
    context = {'form': form}
    return render(request, 'web_notes/new_topic.html', context)

@login_required
def new_note(request, topic_id):
    """creating of new notes"""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(topic, request)

    if request.method != 'POST':
        # data was not send
        form = NoteForm()
    else:
        # data was sent
        form = NoteForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('web_notes:topic', topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'web_notes/new_note.html', context)

@login_required
def edit_note(request, note_id):
    """editing of notes"""
    note = Note.objects.get(id=note_id)
    topic = note.topic
    check_topic_owner(topic, request)

    if request.method != 'POST':
        # data was not send
        form = NoteForm(instance=note)
    else:
        # data was sent
        form = NoteForm(instance=note, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('web_notes:topic', topic_id=topic.id)

    context = {'note': note, 'topic': topic, 'form': form}
    return render(request, 'web_notes/edit_note.html', context)

def check_topic_owner(topic, request):
    """check topic owner"""
    if topic.owner != request.user:
        raise Http404