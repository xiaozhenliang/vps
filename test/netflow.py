#!/usr/bin/env python

import os
import sys
import _env
import conf
import time
from ops.netflow import read_proc
import unittest

if __name__ == '__main__':
    netflow_dict =  read_proc ()
    print netflow_dict['vps95']



# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 :
