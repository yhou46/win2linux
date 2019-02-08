import unittest
import sys
import os

# Get module file path
CURRENT_DIRECTORY = os.path.dirname( os.path.abspath(__file__) )
SRC_DIRECTORY = os.path.dirname(CURRENT_DIRECTORY)
sys.path.insert(0, SRC_DIRECTORY)

# Import module to be tested
import w2lHelper


class Test_linuxPathToWindows(unittest.TestCase):
    def test_with_spaces(self):
        linuxPath = "./abc\\ def/file"
        windowsPath = "\".\\abc def\\file\"" # windows path should be with quotes
        self.assertEqual( w2lHelper.linuxPathToWindows(linuxPath), windowsPath)

    def test_with_drive_symbols(self):
        linuxPath = "/mnt/c"
        windowsPath = "C:"
        self.assertEqual( w2lHelper.linuxPathToWindows(linuxPath), windowsPath)
        windowsPath = "F:\\workspace\\win2linux\\src\\unit_tests"
        linuxPath = "/mnt/f/workspace/win2linux/src/unit_tests"
        
        self.assertEqual( w2lHelper.linuxPathToWindows(linuxPath), windowsPath)

class Test_Custom(unittest.TestCase):
    def test_custom(self):
        num = 1
        self.assertEqual(num, 2)
        
        


if __name__ == "__main__":
    unittest.main()