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
    if not os.path.exists(archive_path):
        return False

    try:
        archive_filename = archive_path.split("/")[-1]
        archive_basename = archive_filename.split(".")[0]
        release_dir = "/data/web_static/releases/{}".format(archive_basename)

        put(archive_path, "/tmp/")

        run("mkdir -p {}".format(release_dir))
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, release_dir))
        run("rm /tmp/{}".format(archive_filename))
        run("mv {}/web_static/* {}".format(release_dir, release_dir))
        run("rm -rf {}/web_static".format(release_dir))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_dir))

        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
