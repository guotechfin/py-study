#!/bin/env python
# -*-coding:utf-8-*- 

import logging
import logging.config
import os

logging.config.fileConfig("%s/conf/logging.ini" %
        os.path.abspath('.'))
logger = logging.getLogger("root")
