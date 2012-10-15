#!/usr/bin/env python
import sys
import os
import getopt
import _env
from lib.log import Log
import conf
from ops.migrate import MigrateClient
from ops.vps_ops import VPSOps


def migrate_vps (vps_id, dest_ip, speed=None):
    logger = Log ("vps_mgr", config=conf)
    try:
        vpsops = VPSOps (logger)
        migclient = MigrateClient (logger, dest_ip)
        vpsops.migrate_vps (migclient, vps_id, dest_ip, speed=speed)
        print "ok"
    except Exception, e:
        logger.exception (e)
        raise e

def usage ():
    print "usage: %s  [ --speed MByte/s] vps_id vps_id2 dest_ip" % (sys.argv[0])

def main ():
    optlist, args = getopt.gnu_getopt (sys.argv[1:], "", [
                 "help", "--speed"
                 ])

    for opt, v in optlist:
        if opt == '--help': 
            usage ()
            os._exit (0)
        if opt == '--speed':
            speed = float (v)
    
    if len (args) < 2:
        usage ()
        os._exit (1)
    vps_ids = map (lambda x: int(x), args[0:-1])
    dest_ip = args[-1]
    for vps_id in vps_ids:
        migrate_vps (vps_id, dest_ip, speed=speed)


if "__main__" == __name__:
    main ()




# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 :
