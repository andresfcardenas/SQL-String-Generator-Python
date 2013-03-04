#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andres F. Cardenas
# Email: akardenasjimenez@gmail.com
import unittest
from generator import select

class SelectTestCase(unittest.TestCase):
    def setUp(self):
        self.l1 = ['a', 'b', 'c']
        self.l2 = ['a', 2]
        self.s1 = 'Test1'
        self.s2 = 'Test2'

    def test_select(self):
        """Test select module
        """
        self.assertEqual(
            select.select(self.s1, self.l1, table_esp='a', sign='!=', value=3),
            'SELECT a, b, c FROM Test1 WHERE a!=3'
        )
        self.assertEqual(
            select.select(self.s2, self.l1, table_esp='b', value=10),
            'SELECT a, b, c FROM Test2 WHERE b=10'
        )
        self.assertEqual(
            select.select(self.s2),
            'SELECT * FROM Test2'
        )

    def tearDown(self):
        del self.l1
        del self.l2
        del self.s1
        del self.s2

if __name__ == '__main__':
    unittest.main()