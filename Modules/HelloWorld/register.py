#!/usr/bin/env python
# -*- coding: utf-8 -*-

import  resource_url_mapping
import flask_rest_mgr


def register(module):
    for resource, path in resource_url_mapping.resource_url_mapping.items():
        flask_rest_mgr.register(resource, path, module)
