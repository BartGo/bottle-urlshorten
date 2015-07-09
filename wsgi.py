#!/usr/bin/python
import os
import sys
print "*** wsgi.py starting"
virtenv                         = os.path.join(os.environ['OPENSHIFT_PYTHON_DIR'], 'virtenv')
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
show_evar('VIRTUAL_ENV')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
    print "*** succeeded venv activation: " + virtualenv 
except IOError:
    print "*** failed venv activation: " + virtualenv 
    pass
sys.path.append("lib")
from app import settings
print "*** config variables:"
settings.SQA_DBENGINE="sqlite:///"+os.path.join(os.environ["OPENSHIFT_DATA_DIR"], 'sqlite.db')
print "PROJECT PATH  = " + settings.PROJECT_PATH
print "TEMPLATE_PATH = " + settings.TEMPLATE_PATH 
print "STATIC_PATH   = " + settings.STATIC_PATH
print ""                 + str(settings.SQA_DBENGINE)
print ""                 + str(settings.SQA_ECHO) 
print ""                 + str(settings.SQA_KEYWORD) 
print ""                 + str(settings.SQA_CREATE) 
print ""                 + str(settings.SQA_COMMIT) 
print ""                 + str(settings.SQA_USE_KWARGS)
print "*** templates found:"
os.listdir(settings.TEMPLATE_PATH)
from app.routes import Routes as application
print "*** wsgi.py finished"
