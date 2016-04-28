from setuptools import setup
from os.path import expanduser

backupdir = expanduser("~");
confFilePath = 'general_conf/bck.conf';

datafiles = [('/etc', [confFilePath])]

try:
    fp = open(confFilePath, 'r');
    content = fp.readlines();
    i = 0;
    for var in content:
        if (var.startswith("backupdir")):
            content[i] = "backupdir=" + backupdir + "/backup_dir\n"
        i += 1
    fp.close();
    
    fp = open(confFilePath, 'w');
    
    for var in content:
        fp.write(var)
    fp.close();
except Exception as e:
    print e;
    

setup(
    name='mysql-autoxtrabackup',
    version='1.0',
    packages=['general_conf', 'backup_prepare', 'partial_recovery', 'master_backup_script'],
    py_modules = ['autoxtrabackup'],
    url='https://github.com/ShahriyarR/MySQL-AutoXtraBackup',
    license='GPL',
    author='Shahriyar Rzayev',
    author_email='rzayev.shahriyar@yandex.com',
    description='Commandline tool written in Python 3 for using Percona Xtrabackup',
    install_requires=[
        'click>=3.3',
        'mysql-connector-python>=2.0.2',
    ],
    dependency_links = ['https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-2.1.3.tar.gz'],
    entry_points='''
        [console_scripts]
        autoxtrabackup=autoxtrabackup:all_procedure
    ''',
    data_files = datafiles,
)
