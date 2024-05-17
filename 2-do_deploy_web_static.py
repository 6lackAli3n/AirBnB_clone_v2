#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers.
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['54.89.109.87', '100.25.190.21']


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.

    - Returns False if the file at archive_path doesn't exist.
    - Uploads the archive to the /tmp/ directory of the web server.
    - Uncompresses the archive to the folder
    /data/web_static/releases/<archive filename
    without extension> on the web server.
    - Deletes the archive from the web server.
    - Deletes the symbolic link /data/web_static
    /current from the web server.
    - Creates a new symbolic link /data/web_static/
    current on the web server, linked to the new version of the code.
    - Returns True if all operations have
    been done correctly, otherwise returns False.
    """
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False
