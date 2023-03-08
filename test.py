import unittest
from correspondance import db_list
from app import get_nearest_volume_index

class TestVolumeLevels(unittest.TestCase):

    def test_volume_level(self):

        value = get_nearest_volume_index(-19.828153610229499)
        self.assertEqual(value, 27)

if __name__ == '__main__':
    unittest.main()