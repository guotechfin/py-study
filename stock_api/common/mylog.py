#!/bin/env python
# -*-coding:utf-8-*- 

import logging
import logging.config
import sys

logging.config.fileConfig("%s/common/logging.ini" % sys.path[0])
logger = logging.getLogger("root")
