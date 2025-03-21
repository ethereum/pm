# Eth_Simulate Meeting Meeting 40
Note: This file is copied from [here](https://github.com/ethereum/pm/issues/1330)

### Meeting Info

- Agenda: [ethereum#1330](https://github.com/ethereum/pm/issues/1330#issue-2882886091)
- Date & Time: March 03, 2025, 12:00 UTC
- Recording: [here](https://youtu.be/uQeN-oem-r0)
## Notes
## Eth_Simulate Implementers Call Summary  

## Overview
The team discussed progress on estimations, tracing endpoints, and debugging efforts. Key topics included a write-up on two estimation approaches (global vs. core level flag), with a follow-up needed to confirm if Sina shared it. Updates were provided on the implementation of endpoints, debugging Nethermind, and tracing functionality, which is nearing completion but requires minor modifications. The team also highlighted the need to decide on the estimation approach and address failing tests once the tracing endpoints are finalized. Action items include pushing the estimation decision to the board, completing endpoint modifications, and sharing updates on Telegram.
## Key Discussion Points

A write-up was prepared last week regarding two approaches to estimations: the global estimation flag and the core level estimation flag.

- The write-up aims to simplify discussions about the two options, allowing the team to proceed without Sina's direct involvement if necessary.
- The team needs to decide which approach to adopt (global or local flag) for the simulate and estimate gas functionality.

---

## Updates on Endpoints and Debugging

### Rohit's Update:
- Worked on implementing three endpoints but identified some issues.
- Currently modifying the implementation, with an expected completion by the end of the day.
- Will post updates on Telegram once done.

### Nethermind Debugging:
- Progress was made on debugging Nethermind, though it was noted to be slightly challenging.
- A PR will be created to modify Olex's previous PR for debugging with Nethermind Hive tests.
- Once the trace endpoints are finalized, focus will shift back to addressing failing tests.

---

## Tracing Endpoints (Eth Simulates)

- The implementation of tracing endpoints is nearly complete but requires modifications as per feedback from Lucas.
- Expected completion: Today or tomorrow.
- An intern, working with Tansu, was initially assigned to this task, but the responsibility has since been taken over by another team member.

---

## Other Updates

- The primary focus remains on resolving the estimations discussion and completing the tracing endpoints.

---

## Next Steps:
- Confirm with Sina regarding the write-up on estimation flags.
- Finalize the decision on the global vs. local flag approach.
- Complete modifications to the tracing endpoints and share updates on Telegram.
- Address failing tests after the trace endpoints are finalized.
