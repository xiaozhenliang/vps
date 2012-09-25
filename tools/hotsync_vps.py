#!/usr/bin/env python
# coding:utf-8

import sys
import os
import getopt
import _env
from lib.log import Log
import conf
from ops.migrate import MigrateClient
from ops.vps_ops import VPSOps


def hotsync_vps (vps_id, dest_ip):
    logger = Log ("vps_mgr", config=conf)
    try:
        vpsops = VPSOps (logger)
        client = MigrateClient (logger, dest_ip)
        vpsops.hotsync_vps (client, vps_id, dest_ip)
        print "%s ok" % (vps_id)
    except Exception, e:
        logger.exception (e)
        raise e
 
def usage ():
    print "usage: %s vps_id1  vps_id2 ... dest_ip " % (sys.argv[0])

def main ():
    optlist, args = getopt.gnu_getopt (sys.argv[1:], "", [
                 "help", 
                 ])

    for opt, v in optlist:
        if opt == '--help': 
            usage ()
            os._exit (0)
    
    if len (args) < 2:
        usage ()
        os._exit (1)
    vps_ids = args[0:-1]
    dest_ip = args[-1]
    for vps_id in vps_ids:
        hotsync_vps (vps_id, dest_ip)

if __name__ == '__main__':
    main ()

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 :