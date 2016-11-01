#!/usr/bin/env bash

# this stops motionalarm
sudo ps -aux | grep motionalarm.py | awk {'print $2'} | xargs kill -2
