from celery.decorators import task

from .models import Mission


@task
def github_hook(repo, **kw):
    github_hook.get_logger(**kw).info('Running task for %s.' % repo)
    Mission.go(repo)
