# Standard libraries
import pdb # Python debugger

# Django Core
from django.shortcuts import render
from django.http import HttpResponse, response, JsonResponse

# Utilities
import json
from datetime import datetime

# Create your views here.
posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]

def list_posts(request):
    content = []
    for post in posts:
        content.append(f"""
            <p><strong>{post['name']}</strong></p>
            <p><small>{post['user']} - <i>{post['timestamp']}</i></small></p>
            <figure><img src="{post['picture']}"/></figure>
        """)
    return HttpResponse('<br>'.join(content))

def list_posts_test(request):
    posts = ['a', 'b', 'c']
    result = {
        'posts': posts,
    }
    return JsonResponse(result, safe=True)

    # posts = ['a', 'b', 'c']
    # return JsonResponse(posts, safe=False)
    
def template_testing(request):
    return render(request, 'feed.html', {'context': 'ViewContext testing', 'posts': posts})