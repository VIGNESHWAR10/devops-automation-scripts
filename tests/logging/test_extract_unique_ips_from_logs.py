import unittest
import sys
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct path to the 'scripts' directory
scripts_dir = os.path.join(current_dir, '../../scripts/logging')

# Add 'scripts/logging' directory to sys.path
sys.path.append(scripts_dir)


from extract_unique_ips_from_logs import find_unique_ips

class TestExtractUniqueIPs(unittest.TestCase):
    def test_extract_unique_ips(self):

        log_content = """
        2024-06-17 10:30:27 192.168.1.1 - GET /index.html HTTP/1.1
        2024-06-17 10:31:15 192.168.1.2 - POST /login HTTP/1.1
        2024-06-17 10:31:59 192.168.1.1 - GET /about.html HTTP/1.1
        2024-06-17 10:32:45 192.168.1.3 - GET /index.html HTTP/1.1
        2024-06-17 10:33:12 192.168.1.2 - GET /contact.html HTTP/1.1
        2024-06-17 10:34:01 192.168.1.1 - POST /submit-form HTTP/1.1
        2024-06-17 10:35:21 192.168.1.4 - GET /index.html HTTP/1.1
        """

        with open("test_log.log", "w") as file:
            file.write(log_content)
        
        result = find_unique_ips("test_log.log")

        expected_ips = ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4']
        
        self.assertCountEqual(result, expected_ips)

        # Clean up: Delete the temporary log file
        import os
        os.remove('test_log.log')

if __name__ == '__main__':
    unittest.main()