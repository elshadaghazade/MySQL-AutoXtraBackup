from setuptools import setup
from os.path import expanduser
import os.path

backupdir = expanduser("~") + "/backup_dir";
confFilePath = 'general_conf/bck.conf';

datafiles = [('/etc', [confFilePath])]


if (!os.path.isfile(backupdir)):
    try:
        fp = open(confFilePath, 'r');
        content = fp.readlines();
        i = 0;
        for var in content:
            if (var.startswith("backupdir")):
                content[i] = "backupdir=" + backupdir + "\n"
            i += 1
        fp.close();

        fp = open(confFilePath, 'w');

        for var in content:
            fp.write(var)
        fp.close();
    except Exception as e:
        print e;
