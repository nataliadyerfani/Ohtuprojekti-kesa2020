
import sys
sys.path.append('./src')
import unittest
import cv2
from main import check_video

class TestMain(unittest.TestCase):
    def test_check_video(self):
        cap = cv2.VideoCapture(999)
        self.assertEqual(check_video(cap), False, 'Should return False.')

if __name__ == '__main__':
    unittest.main()