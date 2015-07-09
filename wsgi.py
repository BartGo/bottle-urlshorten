#!/usr/bin/python
import os
import sys
print "*** wsgi.py starting"
virtenv                         = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv                      = os.path.join(virtenv, 'bin/activate_this.py')
py_version                      = os.environ['OPENSHIFT_PYTHON_VERSION']
py_cache                        = os.path.join(virtenv, 'lib', py_version, 'site-packages')
os.environ['PYTHON_EGG_CACHE']  = os.path.join(py_cache)
def show_evar(name):
    try:
        print name + " = " + os.environ[""+name+""]
    except:
        print name + " : not found"
        pass
    return
print "*** openshift environment variables:"
show_evar('OPENSHIFT_PYTHON_VERSION')
show_evar('PYTHON_EGG_CACHE')
show_evar('OPENSHIFT_PYTHON_DIR')
show_evar('OPENSHIFT_HOMEDIR')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
    print "*** succeeded venv activation: " + virtualenv 
except IOError:
    print "*** failed venv activation: " + virtualenv 
    pass
sys.path.append("lib")
from app import settings
print "*** app environment variables:"
print "*** config variables:"
SQA_DBENGINE=os.environ["OPENSHIFT_DATA_DIR"]
print PROJECT_PATH
print TEMPLATE_PATH 
print STATIC_PATH
print SQA_DBENGINE # 'sqlite:///data//sqlite.db'
print SQA_ECHO 
print SQA_KEYWORD 
print SQA_CREATE 
print SQA_COMMIT 
print SQA_USE_KWARGS
from app.routes import Routes as application
print "*** wsgi.py finished"
