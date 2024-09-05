#!/usr/bin/env python
import sys
import rospy
from robotica_pkg.srv import *

def divide_two_numbers_client(x, y):
    rospy.wait_for_service('divide_two_numbers')

    try:
        devide_two_numbers = rospy.ServiceProxy('divide_two_numbers', divide_two_numbers)
        resp1 = devide_two_numbers(x, y)
        return resp1.result
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def usage():
    return """
    === The correct way to use it is: ===
    [x y] = %s
    """ % sys.argv[0]

if __name__ == '__main__':
    if len(sys.argv) == 3:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
    else:
        print usage()
        sys.exit(1)

    print "Requesting %s %s" % (x, y)
    print "%s / %s = %s" % (x, y, divide_two_numbers_client(x, y))
