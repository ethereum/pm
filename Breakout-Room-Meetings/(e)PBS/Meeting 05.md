# (e)PBS Breakout Room #5

Note: This file is copied from [here](https://hackmd.io/@ttsao/epbs-breakout5)

### Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/1095

**Date & Time**: [July 19, 2024, 14:00-15:00 UTC](https://www.timeanddate.com/worldclock/converter.html?iso=20240213T140000&p1=1440&p2=37&p3=136&p4=237&p5=923&p6=204&p7=671&p8=16&p9=41&p10=107&p11=28)

**Recording**: https://youtu.be/pFJMqk5zkPQ


### Meeting notes:
#### Highlight:

- Quintus raised an issue regarding proposer IP leaks when requesting headers from the builder. Currently, proposers request headers from the relayer, who then has access to all IPs. The trust model might change when moving from the relayer to the builder. Validator IPs can also be easily detected today through aggressive spamming or bootnode activities. One potential solution is for proposers to recycle their IPs after block proposals. Due to limited discussion, we moved on from this topic.

- Potuz provided updates on his progress over the last two weeks. He is still focused on fixing consensus spec tests, reducing the number of failed tests from over 700 to 30. He is carefully reviewing each failed fork choice test to determine if they can be skipped.

- In the consensus spec, a bug was discovered and fixed related to caching state.latest_block_header.state_root. Currently, this is cached at process_slot, but in ePBS, a slot is split into consensus and execution parts where the state_root from the first part is used in the second part. Therefore, we need to cache the state root during process_execution_payload as well. However, we won't remove caching for process_slot because the execution payload could be empty.

- We discussed an EPF project on grading builder service. The IP discussion was not directly related to this project. The grading service will evaluate the builder's performance on whether the payload is valid, revealed on time, and other criteria.

- We reviewed who is implementing from EPF. There are/will be ongoing efforts on Nimbus, Teku, and Prysm, with more contributors welcome.
  
- The call was shorter today as most of the progress is focused on fixing spec tests and client implementation. More updates will be discussed in two weeks.
