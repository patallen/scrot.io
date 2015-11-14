from fabric.api import *
from fabric.colors import yellow
import fabfile as fab
import os

user = 'vagrant'
host = '10.10.10.5'

conn = "{}@{}".format(user, host)

venvs_dir = "~/.virtualenvs"
virtualenv = "{}/{}env".format(venvs_dir, fab.app_name)
python_path = "{}/bin/python".format(virtualenv)


@hosts(conn)
def dev_setup():
    if not prompt(
        yellow('Do you want to start development setup? (y/n):'),
        validate=fab.require_yes
    ):
        return

    sudo('apt-get update')
    sudo('apt-get upgrade -y')
    sudo('apt-get install {} -y'.format(' '.join(fab.apt_packages)))
    sudo('pip install {}'.format(' '.join(fab.pip_packages)))
    sudo('echo "WORKON_HOME={}" >> ~/.bashrc'.format(venvs_dir))
    sudo('echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc')


@hosts(conn)
def setup_virtualenv():
    try:
        sudo('mkdir {}'.format(venvs_dir))
    except:
        print("~/.virtualenvs already exists")
    sudo('virtualenv -p python3 {}'.format(virtualenv))
    sudo('chown {}:{} {}'.format(user, user, virtualenv))


@hosts(conn)
def setup_project():
    with cd('/var/{}'.format(fab.app_name)):
        run('source ~/.virtualenvs/scrotioenv/bin/activate')
        run('pip install -r requirements.txt')

@hosts(conn)
def runserver(port='8080'):
    with cd('/var/{}'.format(fab.app_name)):
        run('{} manage.py runverver 0:{}'.format(python_path, port))
