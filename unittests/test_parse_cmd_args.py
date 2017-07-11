#!/usr/bin/python3
import unittest

from src.parse_cmd_args import CmdArgumentsParser


class CmdArgumentsParserTestCase(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.args = ["main.py", "test_project", "-v", "GET"]

    def runTest(self):
        pass

    def test_creation_raises_exception(self):
        with self.assertRaises(Exception):
            args = ["main.py"]
            cmd_args = CmdArgumentsParser(args)

    def test_retrieve_project_name(self):
        # Arrange
        cmd_args = CmdArgumentsParser(self.args)

        # Assert
        self.assertEqual("test_project", cmd_args.project_name)

    def test_switched_keyword_verbose(self):
        # Arrange
        args = ["main.py", "test_project", "GET",  "-v"]

        # Act
        cmd_args = CmdArgumentsParser(args)

        # Assert
        self.assertEqual(True, cmd_args.verbose)
        self.assertEqual("GET", cmd_args.filter_keyword)

    def test_no_keyword(self):
        # Arrange
        args = ["main.py", "test_project", "-v"]

        # Act
        cmd_args = CmdArgumentsParser(args)

        # Assert
        self.assertEqual(True, cmd_args.verbose)
        self.assertEqual(None, cmd_args.filter_keyword)

    def test_no_verbose(self):
        # Arrange
        args = ["main.py", "test_project", "GET"]

        # Act
        cmd_args = CmdArgumentsParser(args)

        # Assert
        self.assertEqual(False, cmd_args.verbose)
        self.assertEqual("GET", cmd_args.filter_keyword)

    def test_no_verbose_and_nokeyword(self):
        # Arrange
        args = ["main.py", "test_project"]

        # Act
        cmd_args = CmdArgumentsParser(args)

        # Assert
        self.assertEqual(False, cmd_args.verbose)
        self.assertEqual(None, cmd_args.filter_keyword)