import json

from django import http
from django.views.decorators.csrf import csrf_exempt

from decorators import require_post

from . import tasks


@csrf_exempt
@require_post
def github_hook(request, secret):
    repo = json.loads(request.raw_post_data)['repository']
    tasks.github_hook(repo['name'])
    tasks.github_hook.delay(repo['name'])
    return http.HttpResponse('ok')
