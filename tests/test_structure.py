import unittest
import lithe.structure
import subprocess


TEST_DIR = 'tests/dir'
TEST_STRUCTURE = ['web', 'content', 'web/templates']


class TestStructureFunctions(unittest.TestCase):
    def setUp(self):
        for d in TEST_STRUCTURE:
            new_dir = '%s/%s' % (TEST_DIR, d)
            subprocess.call(['mkdir', '-p', new_dir])
            subprocess.call(['touch', ('%s/%s' % (new_dir, 'test.html'))])
            subprocess.call(['touch', ('%s/%s' % (new_dir, 'test2.yml'))])
            subprocess.call(['touch', ('%s/%s' % (new_dir, '_test.html'))])

    def test_get_files_from_path(self):
        """
            When requesting a filelist from a given (web) path,
            I expect a proper list with proper contents.
        """
        file_list = lithe.structure.get_files_from_path(
            '%s/%s' % (TEST_DIR, TEST_STRUCTURE[2])
        )

        self.assertListEqual(
            file_list, ['_test.html', 'test.html', 'test2.html'])

    def test_get_files_from_path_only_html(self):
        """
            Any .yaml file should have been renamed to .html
        """
        file_list = lithe.structure.get_files_from_path(
            '%s/%s' % (TEST_DIR, TEST_STRUCTURE[0])
        )

        for f in file_list:
            self.assertRegex(f, '.*\.html')

    def test_get_files_from_path_no_prefix_slash(self):
        """
            Filenames should never start with /
        """
        file_list = lithe.structure.get_files_from_path(
            '%s/%s' % (TEST_DIR, TEST_STRUCTURE[0])
        )

        for f in file_list:
            self.assertNotRegex(f, '^/')

    def test_get_static_html_files_only_returns_static(self):
        file_list = []
        lithe.structure.get_static_html_files(
            file_list, ('%s/%s' % (TEST_DIR, TEST_STRUCTURE[2])))

        for f in file_list:
            self.assertNotRegex(f, '^_')

    def tearDown(self):
        subprocess.call(['rm', '-Rf', TEST_DIR])

if __name__ == '__main__':
    unittest.main()
