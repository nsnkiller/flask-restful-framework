#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask_rest_mgr
from Modules import module_mgr


def main():
    module_mgr.register()
    flask_rest_mgr.run()


if __name__ == '__main__':
    main()

