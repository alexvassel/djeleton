# encoding: utf-8
from fabric.api import *
#!
dev = 'dev'

#!
env.user = 'user'
env.hosts = (dev,)
#!
env['password'] = 'password'

PROJECT_NAME = '{{project_name}}'


@hosts(dev)
def update_remote(branch='master', restart=False):
    """
    Checks out given branch, pulls then pushs on localhost
    and pulls on dev + reloads uwsgi

    :branch: branch to checkout on localhost.
    :restart:  restart uwsgi?
    """
    puts('Checkout branch %s on localhost' % branch)
    local('git checkout %s' % branch)
    puts('Pull on localhost')
    local('git pull origin %s' % branch)
    puts('Push from localhost')
    local('git push origin %s' % branch)
    puts('Pull on %s' % dev)
    env['cwd'] = '/home/' + env.user + '/projects/' + PROJECT_NAME + '/source/'
    puts('Checkout branch %s on %s' % (branch, dev))
    run('git checkout %s' % branch)
    run('git pull origin %s' % branch)
    puts('Restart uwsgi on %s' % (dev))
    if restart:
        run('touch /home/' + env.user + '/projects/' + PROJECT_NAME + '/')
