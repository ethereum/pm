import os
import sys
import pathlib
import unittest

# Add the project root to sys.path
current_dir = pathlib.Path(__file__).parent
project_root = current_dir.parent
sys.path.insert(0, str(project_root))

from scripts.handle_issue import parse_issue_for_time

class TestParseIssueForTime(unittest.TestCase):
    
    def test_parse_issue(self):
        test_cases = [
            {
                "description": "Format with separate duration",
                "issue_body": """
                # Rollcall ACDbot testing

                - We will not have a meeting on [Jan 16, 2025, 14:00 UTC](https://savvytime.com/converter/utc/jan-16-2025/2pm)
                - Duration in minutes
                - 90

                # Agenda 

                - Testing the discourse
                - Testing the telegram bot

                Other comments and resources
                """
            },
            {
                "description": "Format with start and end time",
                "issue_body": """
                # Rollcall ACDbot testing

                - We will not have a meeting on [Jan 18, 2025, 14:00-15:30 UTC](https://savvytime.com/converter/utc/jan-18-2025/2pm)

                # Agenda 

                - Testing the discourse
                - Testing the telegram bot

                Other comments and resources
                """
            },
            {
                "description": "Lowercase month without commas",
                "issue_body": """
                # Protocol call ACDbot testing

                - We will not have a meeting on [jan 18 2025 14:00 UTC](https://savvytime.com/converter/utc/jan-18-2025/2pm)
                - Duration in minutes
                - 90

                # Agenda 

                - Testing the discourse
                - Testing the telegram bot

                Other comments and resources
                EDIT TEST n°10
                """
            },
            {
                "description": "Lowercase month with duration line",
                "issue_body": """
                # Protocol call ACDbot testing

                - We will not have a meeting on [jan 18 2025 14:00-15:30 UTC](https://savvytime.com/converter/utc/jan-18-2025/2pm)

                # Agenda 

                - Testing the discourse
                - Testing the telegram bot

                Other comments and resources
                EDIT TEST n°10
                """
            },
            {
                "description": "Incorrect format",
                "issue_body": """
                # Protocol call ACDbot testing

                - We will not have a meeting on Jan 18, 2025 at 14:00 UTC
                - Duration in minutes
                - 60

                # Agenda 

                - Testing the discourse
                - Testing the telegram bot

                Other comments and resources
                EDIT TEST n°11
                """
            },
            {
                "description": "End time before start time",
                "issue_body": """
                # Protocol call ACDbot testing

                - We will not have a meeting on [Jan 20, 2025, 16:00-15:30 UTC](https://savvytime.com/converter/utc/jan-20-2025/2pm)

                # Agenda 

                - Testing the discourse
                - Testing the telegram bot

                Other comments and resources
                EDIT TEST n°10
                """
            },
            {
                "description": "Additional spaces and comas",
                "issue_body": """
                # Protocol call ACDbot testing

                - We will not have a meeting on [jan 19, 2025, 13:00 UTC](https://savvytime.com/converter/utc/jan-19-2025/2pm)
                -   Duration    in    minutes
                -    60

                # Agenda 

                - Testing the discourse
                - Testing the telegram bot

                Other comments and resources
                EDIT TEST n°11
                """
            },
            {
                "description": "Full month name with duration",
                "issue_body": """
                # Protocol call ACDbot testing

                - We will not have a meeting on [Wed February 05, 2025, 14:00 UTC](https://savvytime.com/converter/utc/feb-05-2025/2pm)
                - Duration in minutes
                - 45

                # Agenda 

                - Testing the discourse
                - Testing the telegram bot

                Other comments and resources
                EDIT TEST n°12
                """
            },
            {
                "description": "Full month name with start and end time",
                "issue_body": """
                # Protocol call ACDbot testing

                - We will not have a meeting on [Wed February 05, 2025, 14:00-15:15 UTC](https://savvytime.com/converter/utc/feb-05-2025/2pm)

                # Agenda 

                - Testing the discourse
                - Testing the telegram bot

                Other comments and resources
                EDIT TEST n°13
                """
            },
        ]

        for case in test_cases:
            with self.subTest(case['description']):
                try:
                    start_time, duration = parse_issue_for_time(case["issue_body"])
                    
                    # Define expected outputs based on description
                    if case["description"] == "Format with separate duration":
                        expected_start = "2025-01-16T14:00:00Z"
                        expected_duration = 90
                    elif case["description"] == "Format with start and end time":
                        expected_start = "2025-01-18T14:00:00Z"
                        expected_duration = 90  # 14:00 to 15:30 is 90 minutes
                    elif case["description"] == "Lowercase month without commas":
                        expected_start = "2025-01-18T14:00:00Z"
                        expected_duration = 90
                    elif case["description"] == "Lowercase month with duration line":
                        expected_start = "2025-01-18T14:00:00Z"
                        expected_duration = 90
                    elif case["description"] == "Incorrect format":
                        # Should raise ValueError
                        self.fail("Expected ValueError was not raised.")
                    elif case["description"] == "End time before start time":
                        # Should raise ValueError
                        self.fail("Expected ValueError was not raised.")
                    elif case["description"] == "Additional spaces and comas":
                        expected_start = "2025-01-19T13:00:00Z"
                        expected_duration = 60
                    elif case["description"] == "Full month name with duration":
                        expected_start = "2025-02-05T14:00:00Z"
                        expected_duration = 45
                    elif case["description"] == "Full month name with start and end time":
                        expected_start = "2025-02-05T14:00:00Z"
                        expected_duration = 75
                    else:
                        self.fail(f"Unknown test case description: {case['description']}")
                    
                    self.assertEqual(start_time, expected_start, f"Failed {case['description']} - Start Time")
                    self.assertEqual(duration, expected_duration, f"Failed {case['description']} - Duration")
                    
                except ValueError as ve:
                    if case["description"] in ["Incorrect format", "End time before start time"]:
                        self.assertTrue(True)  # Expected failure
                    else:
                        self.fail(f"Unexpected ValueError in {case['description']}: {ve}")

if __name__ == "__main__":
    unittest.main()
