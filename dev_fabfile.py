from fabric.api import *
from fabric.colors import yellow
import fabfile as fab

user = 'vagrant'
host = '10.10.10.5'

conn = "{}@{}".format(user, host)


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
