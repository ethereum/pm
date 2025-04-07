# PeerDAS Breakout Room #18

## Meeting info
- Date: 2025.02.18
- Agenda: https://github.com/ethereum/pm/issues/1295
- YouTube video: https://youtu.be/mzK83JuvbAA

>**ACTION**: For next week - we'll keep the same time 10am UTC to avoid clashing with FOCIL

## Consensus Client Team Updates
| Team | Updates |
|---------------|---------|
| Lighthouse | • Fixed delayed sync issue on devnet, and unsubscribe from blob topics from Fulu fork<br>• New test CLI flags to delay block and column publishing implemented and under review, will be ready soon<br>• Lion shared design doc on validator custody [here](https://hackmd.io/@dapplion/validator_custody_no_backfill) |
| Prysm | • Found bug due to Fulu state having the same fields as Electra<br>• Changed DB storage format for data columns<br>• Go-kzg has worse performance than c-kzg, working with Kev on this<br>• Working on validator custody, shared design doc |
| Teku | • Various bug fixes<br>• Fixed reconstruction logic |
| Nimbus | • Not on the call |
| Lodestar | • Syncing and working on peerdas-devnet-4<br>• Geth issue on devnet, more on this later<br>• Refactor and started validator custody |
| Grandine | • Fixed some sync bugs<br>• Tried syncing full node with devnet |

## Devnet / Testing Updates
| Topic | Details |
|---------|---------|
| Peerdas-devnet-4 | - Geth version got updated after devnet started, and we're no longer able to sync due to invalid block error at one of the slots<br>- Didn't seem like a PeerDAS issue - teams decided to reset devnet, and start again with a pinned geth version<br>- But Geth 14.13 worked for Lodestar, and they were able to sync without issue<br>- **ACTION**: Try testing sync with geth 14.13, if it doesn't work, launch a new devnet (devnet-5) |
| Manu testing scenarios | - Scenarios here<br>- Do we test these scenarios on peerdas-devnet or local devnet?<br>&nbsp;&nbsp;- Prioritise testing the sync scenarios that we were planning to test (checkpoint sync, genesis sync) on the devnet<br>&nbsp;&nbsp;- Unfinalized network syncing can be tested locally for now |

## EIP / Spec Updates and Discussions
| Topic | Subtopic | Details |
|-------|----------|---------|
| **Validator Custody** | Current Spec | - Nodes backfill and may choose to advertise new cgc once backfill is complete (may take up to a week) |
| | Proposal | - No backfill at all, and just update CGC after 4096 epochs |
| | Concerns | - Downside is we won't be able to use the new cgc until 18 days later |
| | Alternative | - Paul suggested a middleground: node to advertise its new cgc and effective timestamp<br>- Requires adding multiple new fields to metadata and ENR |
| | Next Steps | - Teams don't have further comment on this<br>- Will continue investigation and discuss async |
| **Proof Computation to tx sender** | Existing Transactions | - Besu: what do we do with the existing 4844 transactions? |
| | Transaction Type | - Do we need a new transaction type?<br>- No change to data being signed over, may not be worth it<br>- Do we need to support both formats? |
| | Nethermind Perspective | - Marcin: Network form is not compatible when sending between clients<br>- Do we want to support both forms? |
| | Suggested Approach | - RPC: accept both forms until after the fork<br>- Translate old format to new format before sending over p2p<br>- Only new format on the p2p network |
| | Specification Questions | - Does this change go to the execution spec (mempool)?<br>- Not sure, best thing to do is possibly create a PR to the existing EIP and raise it in ACD<br>- Is blob verification part of a spec?<br>- Not sure, same as above, start PR and start from there |
| | Resources | - Francesco's document on mempool covers some change needed: https://hackmd.io/@fradamt/mempool-change |
| | Action Item | - PR to the EIP as a first step and discuss in the next ACD |

## Open Discussions
#### Lodestar: Any other EL devs we can use in the devent for client diversity?
- Focus on testing peerdas for now, and stick with one client
- On future devnets, once we have tx sender computing the proofs, all ELs will participate anyway

## Links Shared
- https://github.com/ethereum/pm/issues/1295
- https://youtu.be/mzK83JuvbAA
- https://hackmd.io/@dapplion/validator_custody_no_backfill
- https://hackmd.io/@fradamt/mempool-change
