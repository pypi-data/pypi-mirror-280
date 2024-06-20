# -*- coding: utf-8 -*-
'''
# MAT-tools: Tools for Multiple Aspect Trajectory Data Mining \[MAT-Tools Framework\]

The present application offers a set of tools, to support the user in the data mining and analysis tasks for multiple aspect trajectories. It integrates into a unique platform the fragmented approaches available for multiple aspects trajectories and in general for multidimensional sequence classification into a unique web-based and python library system.

Created on Dec, 2021
Copyright (C) 2021+, License GPL Version 3 or superior (see LICENSE file)

@author: Tarlis Portela
'''
import sys, os 
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import dash
import dash_bootstrap_components as dbc

from flask import Flask, session
from matview.web.config import page_title, PACKAGE_NAME

# from flask_caching import Cache
# cache = Cache(app.server, config={
#     'CACHE_TYPE': 'filesystem',
#     'CACHE_DIR': 'app/cache'
# })

# Boostrap CSS.
external_stylesheets=[
    dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP
#     PACKAGE_NAME+'/assets/examples/css/notebook.css',
]

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets, prevent_initial_callbacks=True, 
#                 title=page_title, suppress_callback_exceptions=True)
# server = app.server

server = Flask(str(PACKAGE_NAME))

app = dash.Dash(str(PACKAGE_NAME), server=server,external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True
app.title = page_title
#app._favicon = 'img/favicon.ico'
app._favicon = '../assets/img/favicon.ico'


# SESSION CACHE - 30 MIN
import random, string
server.config['SECRET_KEY'] = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(20))
SESS_USERS = dict()

import uuid
import threading
class SelfDestUser:
    def __init__(self):
        self.UID = uuid.uuid4()
        self.data = dict()
        
        global SESS_USERS
        SESS_USERS[self.UID] = self

        self.start()

    def start(self):
        self.TTL = threading.Timer(30 * 60, self.__del__)
        self.TTL.start()

    def keep(self):
        self.TTL.cancel()
        self.start()
    
    def __del__(self):
        global SESS_USERS
        del SESS_USERS[self.UID]
        del self
      
    def sev(self, key, val):
        self.keep()
        self.data[key] = val

    def gev(self, key, default=None):
        self.keep()
        if key in self.data:
            return self.data[key]
        else:
            return default

def gu():
    global SESS_USERS
    if 'user' not in session or session['user'] not in SESS_USERS:
        U = SelfDestUser()
        session['user'] = U.UID
        
    return session['user']

def sess(key, val):
    global SESS_USERS
    SESS_USERS[gu()].sev(key, val)

def gess(key, default=None):
    global SESS_USERS
    return SESS_USERS[gu()].gev(key, default)
