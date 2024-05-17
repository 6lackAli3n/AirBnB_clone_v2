#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive
from the contents of the web_static folder.
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    - All files in the folder web_static must be added to the final archive.
    - All archives must be stored in the folder versions.
    - The name of the archive created must be
    web_static_<year><month><day><hour><minute><second>.tgz.
    - Returns the archive path if the archive has
    been correctly generated, otherwise returns None.
    """

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None
