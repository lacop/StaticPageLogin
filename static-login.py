#!/usr/bin/python
import os, sys, cgi
password = 'changeme'

prefix = os.path.dirname(os.environ['SCRIPT_NAME'])
req = os.path.normpath(os.environ['REQUEST_URI'])
if os.path.commonprefix([prefix, req]) != prefix:
    sys.exit()

rel = req[len(prefix)+1:]
if rel == '' or rel == 'login.html':
    rel = 'index.html'

ct = 'text/html'
if rel[-4:] == '.css':
    ct = 'text/css'
elif rel[-3:] == '.js':
    ct = 'application/javascript'
else:
    form = cgi.FieldStorage()
    pwd = form.getvalue('password')
    if pwd is not None:
        if pwd == password:
            #print "Content-type: text/html\n"
            print "Set-Cookie:password=%s;" % pwd
        else:
            rel = 'login.html'
    else:
        found = False
        if os.environ.has_key('HTTP_COOKIE'):
            for cookie in os.environ['HTTP_COOKIE'].split(';'):
                k, v = cookie.strip().split('=')
                if k == 'password' and v == password:
                    found = True
        if not found:
            rel = 'login.html'

try:
    with open(rel, 'r') as f:
        print "Content-type: %s\n" % ct
        print f.read()
except:
    print "Content-type: text/html\n"
    print "Can't open %s!" % rel

