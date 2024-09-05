#!/usr/bin/env python

from robotica_pkg.srv import divide_two_numbers, divide_two_numbersResponse
import rospy

def handle_divide_two_numbers(req):
    print("Returning[%s / %s = %s" % (req.number1, req.number2, (req.number1 / req.number2)))
    return divide_two_numbersResponse(req.number1 / req.number2)

def divide_two_numbers_server():
    rospy.init_node('divide_two_numbers_server')
    s = rospy.Service('divide_two_numbers', divide_two_numbers, handle_divide_two_numbers)
    print("Ready to divide two numbers")
    rospy.spin()

if __name__ == '__main__':
    divide_two_numbers_server()

