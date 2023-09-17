import unittest

import main


class MyTestCase(unittest.TestCase):
    def test_1(self):
        main.run("D:\Project\HAAAAPY-CZY\HAAAAPY-CZY\\3121005081\data\orig.txt","D:\Project\HAAAAPY-CZY\HAAAAPY-CZY\\3121005081\data\orig_0.8_add.txt","D:\Project\HAAAAPY-CZY\HAAAAPY-CZY\\3121005081\\result\\test1")

    def test_2(self):
        main.run("D:\Project\HAAAAPY-CZY\HAAAAPY-CZY\\3121005081\data\orig.txt","D:\Project\HAAAAPY-CZY\HAAAAPY-CZY\\3121005081\data\orig_0.8_del.txt","D:\Project\HAAAAPY-CZY\HAAAAPY-CZY\\3121005081\\result\\test2")

    def test_3(self):
        main.run("D:\Project\HAAAAPY-CZY\HAAAAPY-CZY\\3121005081\data\orig_0.8_del.txt","D:\Project\HAAAAPY-CZY\HAAAAPY-CZY\\3121005081\data\orig_0.8_dis_1.txt","D:\Project\HAAAAPY-CZY\HAAAAPY-CZY\\3121005081\\result\\test3")

    def test_4(self):
        main.run("D:\Project\HAAAAPY-CZY\HAAAAPY-CZY\\3121005081\data\orig_0.8_del.txt","D:\Project\HAAAAPY-CZY\HAAAAPY-CZY\\3121005081\data\orig_0.8_dis_10.txt","D:\Project\HAAAAPY-CZY\HAAAAPY-CZY\\3121005081\\result\\test4")

    def test_5(self):
        main.run("D:\Project\HAAAAPY-CZY\HAAAAPY-CZY\\3121005081\data\orig_0.8_del.txt","D:\Project\HAAAAPY-CZY\HAAAAPY-CZY\\3121005081\data\orig_0.8_dis_15.txt","D:\Project\HAAAAPY-CZY\HAAAAPY-CZY\\3121005081\\result\\test5")




if __name__ == '__main__':
    unittest.main()
