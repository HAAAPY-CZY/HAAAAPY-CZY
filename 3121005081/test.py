import unittest

import main


class MyTestCase(unittest.TestCase):
    def test_1(self):
        main.run("orig.txt","orig_0.8_add.txt","test1")

    def test_2(self):
        main.run("orig.txt","orig_0.8_del.txt","test2")

    def test_3(self):
        main.run("orig_0.8_del.txt","orig_0.8_dis_1.txt","test3")

    def test_4(self):
        main.run("orig_0.8_del.txt","orig_0.8_dis_10.txt","test4")

    def test_5(self):
        main.run("orig_0.8_del.txt","orig_0.8_dis_15.txt","test5")




if __name__ == '__main__':
    unittest.main()
