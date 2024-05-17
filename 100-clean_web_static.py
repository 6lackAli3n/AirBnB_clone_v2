#!/usr/bin/python3
""" Fabric script to delete out-of-date archives """
from fabric.api import env, run, local, hosts
from datetime import datetime
import os

env.hosts = ['35.185.45.12', '35.185.41.80']


def do_clean(number=0):
    """ Deletes out-of-date archives """
    number = int(number)
    if number < 2:
        number = 1
    else:
        number += 1

    archives_path = "/data/web_static/releases/"
    with hosts(env.hosts):
        local_archives = sorted(os.listdir("versions"))
        server_archives = run("ls -tr {} | grep 'web_static'".format(archives_path)).split()

        for i in range(len(local_archives) - number):
            local("rm versions/{}".format(local_archives[i]))

        for i in range(len(server_archives) - number):
            run("rm {}{}".format(archives_path, server_archives[i]))
