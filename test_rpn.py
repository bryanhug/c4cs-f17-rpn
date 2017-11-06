#!/usr/bin/env python3
import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2,result)

    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2,result)

    def test_divide(self):
        result = rpn.calculate("5 3 /")
        self.assertEqual(5/3,result)

    def test_mult(self):
        result = rpn.calculate("3 9 *")
        self.assertEqual(27,result)

    def test_mult(self):
        result = rpn.calculate("3 0 *")
        self.assertEqual(0,result)

    def test_div0(self):
        result = rpn.calculate("1 0 /")
        self.assertEqual(-1,result)

    # def test_bad_input0():
    #     #bad input in 0 posistion
    #     result =  rpn.calculate("q");
    #     self.assertEqual(-1,result);
    #
    # def test_bad_input1():
    #     #bad input in 1 posistion
    #     result =  rpn.calculate("1 r +");
    #     self.assertEqual(-1,result);
    #
    # def test_bad_input2():
    #     #bad input in 2 posistion
    #     result =  rpn.calculate("1 2 $");
    #     self.assertEqual(-1,result);

    print("ALL TESTS PASSED BUNDURU!!!!")
