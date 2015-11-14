from fabric.api import *
from fabric.colors import red, yellow, green
import os

user = 'vagrant'
host = '10.10.10.5'

app_name = 'scrotio'
log_dir = '/var/log/{}'.format(app_name)

apt_packages = [
    'git',
    'vim',
    'nginx',
    'python-pip',
    'python-dev',
    'python3',
    'python3-dev',
    'postgresql',
    'postgresql-contrib',
    'postgresql-server-dev-all',
    'libffi-dev',
]
pip_packages = ['virtualenv', 'virtualenvwrapper']


def require_yes(answer):
    return answer.lower() == 'y' or answer.lower() == 'yes'


def print_msg(msg, success=False, warn=False, error=False):
    if success:
        print(green(msg))
    elif warn:
        print(yellow(msg))
    elif error:
        abort(red(msg))
    else:
        print(msg)

if os.path.isfile('dev_fabfile.py'):
    from dev_fabfile import *
else:
    print('No development fabfile.')
