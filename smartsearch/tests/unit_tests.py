"""
Tests to make sure that the client loads
"""
# Builtin imports
import unittest
import os
import json

# Internal imports
import smartsearch
from smartsearch import clients

# Load a wolfram key from the environment
wolfram_key = os.getenv("WOLFRAM_API_KEY")
print(wolfram_key)

if not wolfram_key:
    print("Wolfram key not defined")


@unittest.skipIf(not wolfram_key, "No wolfram API key available")
class WolframTests(unittest.TestCase):

    def test_invalid_key(self):
        """
        Load wolfram with an invalid key and assert that an exception is raised
        """
        wolfram_instance = clients.Wolfram("definitely-not-valid-key")
        with self.assertRaises(Exception):
            wolfram_instance.query("What's the meaning of life?")

    def test_valid_query(self):
        """
        Submit a valid key to wolfram and assert that it passes
        """
        print(wolfram_key)
        wolfram_instance = clients.Wolfram(wolfram_key)
        expected_response = "42\n(according to the book The Hitchhiker's Guide to the Galaxy, by Douglas Adams)"
        resp = wolfram_instance.query("What's the meaning of life?")
        self.assertEqual(resp, expected_response)


class GoogleTests(unittest.TestCase):
    google_instance = clients.Google()

    @classmethod
    def setUpClass(cls):
        print("Downloading NLTK modules for Google tests")
        smartsearch.nltk_download()
        print("Finishing downloading NLTK modules")

    def test_wikipedia_search(self):
        expected_value = "Barack Hussein Obama II (US:  bə-RAHK hoo-SAYN oh-BAH-mə; born August 4, 1961) is an American" \
                         " politician who served as the 44th President of the United States from 2009 to 2017. He is " \
                         "the first African American to have served as president. " \
                         "(https://en.wikipedia.org/wiki/Barack_Obama)"
        resp = self.google_instance.query("Who is Barack Obama?")
        print(resp)
        self.assertEqual(expected_value, resp)


class PackageTests(unittest.TestCase):
    """
    Test that the package loads
    """
    package_instance = smartsearch.Searcher(keys={"wolfram": str(wolfram_key) if type(wolfram_key) != str else wolfram_key})

    @unittest.skipIf(not wolfram_key, "No wolfram API key available")
    def test_query(self):
        expected_response = "42\n(according to the book The Hitchhiker's Guide to the Galaxy, by Douglas Adams)"
        resp = self.package_instance.query("What's the meaning of life?")
        self.assertEqual(resp, expected_response)

    def test_save_and_load(self):
        """
        Test the configuration saving and loading features
        """
        self.package_instance.save()
        self.assert_(os.path.isfile("search.conf"))
        # Check that loading search.conf with json doesn't throw an error
        j = json.load(open("search.conf"))
        self.assertIn("wolfram", j.keys())
        # Test loading it
        test_instance = smartsearch.Searcher(conf_file="search.conf")
        self.assertEqual(test_instance.clients, self.package_instance.clients)

