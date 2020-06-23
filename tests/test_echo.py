#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Implements a test fixture for the echo.py module

Students are expected to edit this module, to add more tests to run
against the 'echo.py' program.
"""

__author__ = "Kenneth Pinkerton"

import unittest
import echo
import subprocess


class TestEcho(unittest.TestCase):
    def setUp(self):
        self.parser = echo.create_parser()

    def test_help(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        with open("USAGE") as f:
            usage = f.read()

        self.assertEqual(stdout.decode("utf-8"), usage)

    def test_lower_short(self):
        """Check if short option '-l' performs lowercasing"""
        args = ["-l", "HELLO WORLD"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.lower)
        result = echo.main(args)
        self.assertEqual(result, "hello world")

    def test_lower_long(self):
        """Check if short option '-l' performs lowercasing"""
        args = ["--lower", "HELLO WORLD"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.lower)
        result = echo.main(args)
        self.assertEqual(result, "hello world")

    def test_upper_short(self):
        """Check if short option '-l' performs lowercasing"""
        args = ["-u", "hello world"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.upper)
        result = echo.main(args)
        self.assertEqual(result, "HELLO WORLD")

    def test_upper_long(self):
        """Check if short option '-l' performs lowercasing"""
        args = ["--upper", "hello world"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.upper)
        result = echo.main(args)
        self.assertEqual(result, "HELLO WORLD")

    def test_title_short(self):
        """Check if short option '-l' performs lowercasing"""
        args = ["-t", "hello world"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.title)
        result = echo.main(args)
        self.assertEqual(result, "Hello World")

    def test_title_long(self):
        """Check if short option '-l' performs lowercasing"""
        args = ["--title", "hello world"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.title)
        result = echo.main(args)
        self.assertEqual(result, "Hello World")

    def test_all(self):
        """Check if short option '-l' performs lowercasing"""
        args = ["-utl", "hello world"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.title)
        result = echo.main(args)
        self.assertEqual(result, "Hello World")

    def test_two_args(self):
        """Check if short option '-l' performs lowercasing"""
        args = ["-ul", "hello world"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.lower)
        result = echo.main(args)
        self.assertEqual(result, "hello world")

    def test_no_args(self):
        """Check if short option '-l' performs lowercasing"""
        args = ["Hello"]
        result = echo.main(args)
        self.assertEqual(result, "Hello")


if __name__ == '__main__':
    unittest.main()
