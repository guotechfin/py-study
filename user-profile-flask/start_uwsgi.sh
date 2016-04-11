#!/bin/bash
#===============================================================================
#
#          FILE:  start_uwsgi.sh
# 
#         USAGE:  ./start_uwsgi.sh 
# 
#   DESCRIPTION:  
# 
#       OPTIONS:  ---
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  chenbaiheng (), chenbh@jpush.cn
#       COMPANY:  Jpush
#       VERSION:  1.0
#       CREATED:  11/03/2015 11:09:13 AM CST
#      REVISION:  ---
#===============================================================================

uwsgi ./conf/flask.ini
