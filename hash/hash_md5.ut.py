import unittest
import hash_md5


class TestMd5(unittest.TestCase):
    def setup(self):
        """Setup default variables for method

        Arguments:
            unittest {[type]} -- [description]
        """
        pass

    def test_hash_valid_string_reurns_hashvalue(self):
        result = hash_md5.hash("password")
        self.assertEqual(result,'5f4dcc3b5aa765d61d8327deb882cf99')

    def test_hash_none_value_throws_exception(self):
        result =  hash_md5.hash(None)
        self.assertIsInstance(result, AttributeError)

    def test_hash_number_reurns_hashvalue(self):
        result = hash_md5.hash(1)
        self.assertIsNotNone(result)
    
    def test_hash_empty_string_reurns_hashvalue(self):
        result = hash_md5.hash("")
        self.assertIsNotNone(result)
    
    def tearDown(self):
        """teardown after every method
        """
        pass

if __name__ == "__main__":
    unittest.main()
