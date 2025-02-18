from dotenv import load_dotenv
from pathlib import Path
import os  # Import os BEFORE assertions

# Load .env from ACDbot directory
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)

# Verify loading
assert env_path.exists(), f"Missing .env at {env_path}"
assert os.getenv("ZOOM_ACCOUNT_ID"), "ZOOM_ACCOUNT_ID not loaded"
assert os.getenv("ZOOM_CLIENT_ID"), "ZOOM_CLIENT_ID not loaded"
assert os.getenv("ZOOM_CLIENT_SECRET"), "ZOOM_CLIENT_SECRET not loaded"

print(f"Loading env from: {env_path}")
print(f"File exists: {env_path.exists()}")

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
                "description": "Pooja bug - eth_simulate Implementers' Meeting [Feb 24, 2025]",
                "issue_body": """
                # eth_simulate Implementers' Meeting [Feb 24, 2025]

                - Date and time in UTC [Feb 24, 2025, 12:00 UTC](https://savvytime.com/converter/utc/feb-24-2025/12pm)
                - Duration in minutes: 60 minutes
                - Recording: [eth_multicall Playlist](https://www.youtube.com/playlist?list=PLJqWcTqh_zKECphjT_m7LVH4tusTtvory)
                [Zoom](https://us02web.zoom.us/j/83932094353?pwd=V2o4NG4yQy9MZFJGY2FKdGU1OFdaZz09)

                ### Resources
                <details>

                [Ideas for eth_simulateV2](https://hackmd.io/@xHso_0ENSqWWLKt_lOqVuA/S1KtbtYTA)
                [PEEPanEIP#135: Eth Simulate with Oleg and Killari](https://youtu.be/4uZyQQ6qz4U)
                https://eips.ethereum.org/EIPS/eip-4399
                https://docs.login.xyz/general-information/siwe-overview
                https://ethresear.ch/t/fork-choice-enforced-inclusion-lists-focil-a-simple-committee-based-inclusion-list-proposal/19870

                </details>
                # Agenda
                - [Notes from the last meeting]
                - Client Implementation update
                - Test
                - Discuss spec for [eth_simulateV2](https://hackmd.io/@xHso_0ENSqWWLKt_lOqVuA/S1KtbtYTA)

                Add more discussion items or async updates. 

                The next meeting is scheduled for March 3, 2025 at 12:00 UTC 

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
                - 60m

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
                -    60min

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
                - 45 mins

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
                    if case["description"] == "Pooja bug - eth_simulate Implementers' Meeting [Feb 24, 2025]":
                        expected_start = "2025-02-24T12:00:00Z"
                        expected_duration = 60
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
