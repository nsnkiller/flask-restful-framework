#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
import importlib

app = Flask(__name__)
api = Api(app)


def register(process_class, url, endpoint_prefix):
    """
    register the url and the mapping process class to the flask framework.
    :param process_class: the class name of your resource
    :param url: url routes to match for the resource process class
    :param endpoint_prefix: endpoint name prefix

    """
    module, rst = process_class.rsplit('.', 1)
    python_module = importlib.import_module(module)
    rst_class = getattr(python_module, rst)
    api.add_resource(rst_class, url, endpoint=endpoint_prefix + rst_class.__name__.lower())


def run():
    ip = "0.0.0.0"
    port = "5000"
    app.run(host=ip, port=port, threaded=True, debug=True)
