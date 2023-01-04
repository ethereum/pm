# Ethereum Core Devs Meeting #20
### Meeting Date/Time: Friday 7/14/17 at 14:00 UTC
### Meeting Duration 1.5 hours
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=hRQg_lHEKl4)
### [Reddit thread](https://www.reddit.com/r/ethereum/comments/6n71f6/live_stream_ethereum_core_developer_meeting_20_in/)
### [Reddit thread #2](https://www.reddit.com/r/ethereum/comments/6n9zmo/updates_from_todays_core_developer_meeting/)

# [Agenda](https://github.com/ethereum/pm/issues/18)

1. Metropolis updates/EIPs.
  **a. Any "subtleties" or questions we need to work out.**
        - Split metropolis into 2 forks? Leave out [EIP 86/208](https://github.com/ethereum/EIPs/pull/208#issuecomment-313872489) in fork #1.
  **b. Updates to testing.**
  **c. Details and implementations of EIPs.**
        1. Updates from client teams.
            - geth - https://github.com/ethereum/go-ethereum/pull/14337
            - Parity - https://github.com/paritytech/parity/issues/4833
            - cpp-ethereum - https://github.com/ethereum/cpp-ethereum/issues/4050
            - yellowpaper -  https://github.com/ethereum/yellowpaper/issues/229
            - pyethapp
            - Other clients
        2. Determining gas prices for new opcodes & pre-compiles [Martin HS/Everyone]
            - Martin H.S can't make it and says: "I'll try to consolidate the geth-benchmarks for opcodes later on, not much new to report since last time"
  **d. Review time estimate for testing/release.**

# Notes

[From this Reddit comment](https://www.reddit.com/r/ethereum/comments/6n71f6/live_stream_ethereum_core_developer_meeting_20_in/dk7t210/):

Main points to come out of meeting:

- Splitting Metropolis into 2 hard forks.
- Delaying EIP 86 until Metro HF 2.
- Likely adding miner block reward deduction to Metro HF 1.
- Block time estimates calculated today (subject to change):
    - 22 sec - end of July
    - 27 sec. - Aug. 26
    - 35 sec. - Sept. 27
    - 45 sec. - Nov. 6th

## Attendance
