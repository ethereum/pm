# ACDbot

Bot for Ethereum protocol calls automation. Python scripts and github workflows for automatic meeting scheduling, EthMagicians posts, transcripts and more. 

## Features

- Creates Zoom meeting and Google calendar event based on GitHub issues using either the [Recurring Protocol Call](/.github/ISSUE_TEMPLATE/recurring-protocol-calls.md) or [One-Time Protocol Call](/.github/ISSUE_TEMPLATE/onetime-protocol-call.md) templates in [PM repo](github.com/ethereum/pm)
- Posts the call agenda from GH issue to EthMagicians forum 
- Uploads meeting recording to YouTube
- Fetches transcript from the Zoom meeting when it's ready and posts it to the forum
- Creates LLM summary of the meeting and posts it
- Enables email or telegram subscription for meetings, recordings, summaries 

