from fabric.api import *
from fabric.contrib.project import *

env.hosts = ['pivotfinlandcom@pivotfinland.com']

def deploy():
    local('npm run build')
    local('cp dist/static/favicon.ico dist/favicon.ico')
    rsync_project(
        local_dir='./dist/',
        remote_dir='/home/pivotfinlandcom/www_calendarevent/',
        delete=True
    )
    rsync_project(
        local_dir='./api/',
        remote_dir='/home/pivotfinlandcom/app_calendarinvitation',
        delete=True,
        exclude=['db/*.sqlite3', 'vendor/bundle', '.bundle', 'log', 'tmp']
    )
    with cd('/home/pivotfinlandcom/app_calendarinvitation'):
        run('bundle install --deployment --without development test')
        run('bundle exec rake assets:precompile db:migrate RAILS_ENV=production')
        # run('bundle exec passenger-config restart-app /home/pivotfinlandcom/app_calendarinvitation')
