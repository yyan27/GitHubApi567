import unittest

from GetGitInfo import get_git_info

class TestGetGitInfo(unittest.TestCase):
    def test_valid_user(self):
        expected_output = ['User: yyan27',
                    'Repo: GitHubApi567 Number of commits: 1',
                    'Repo: Hello_world Number of commits: 3',
                    'Repo: inclass Number of commits: 23',
                    'Repo: react-native-delivery-app Number of commits: 30',
                    'Repo: SSW-567 Number of commits: 10',
                    'Repo: SSW567_HW01 Number of commits: 2',
                    'Repo: SSW810-Final_project Number of commits: 2',
                    'Repo: Triangle567 Number of commits: 22']
        self.assertEqual(get_git_info("yyan27"), expected_output)

    def test_bad_user_name(self):
        self.assertEqual(get_git_info("invalid_name"), 'unable to fetch repositories from user')


if __name__ == '__main__':
    unittest.main()