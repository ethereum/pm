# FOCIL Breakout Room #07
Note: This file is copied from [here](https://github.com/ethereum/pm/issues/1408#issuecomment-2754104346)

### Meeting Info
- Agenda: https://github.com/ethereum/pm/issues/1408
- Date & Time: [March 25th, 14:00-15:00 UTC](https://www.timeanddate.com/worldclock/converter.html?iso=20240213T140000&p1=1440&p2=37&p3=136&p4=237&p5=923&p6=204&p7=671&p8=16&p9=41&p10=107&p11=28)
- Recording: [here](https://youtube.com/live/XwXeFMjzu4g)

## Meeting notes:

### Research
At the EF researcher offsite, FOCIL received significant positive attention regarding its potential role in the future of the protocol. Questions still remain about how to make FOCIL compatible with other proposals, but overall, the sentiment is highly favorable.

#### Protocol Research Call

- [The protocol research call](https://x.com/barnabemonnot/status/1904532092513354223) begins on April 2nd. Serving as a focal point for both researchers and developers, it aims to clarify Ethereum's goals and identify key research priorities. The first call will cover [decoupling throughput from local building](https://ethresear.ch/t/decoupling-throughput-from-local-building/22004), a topic closely linked with FOCIL. FOCIL introduces a new role, the "includer," dedicated to contributing to censorship resistance. This allows local builders to delegate block building externally for larger profits, while includers uphold censorship resistance by imposing constraints on external builders. This approach opens the door to discussions regarding raising network bandwidth and hardware requirements targeted toward external builders, who are expected to be more sophisticated, without compromising the network properties we aim to preserve. Please review the article, provide your feedback, and tune in the upcoming protocol research call.

### Development
#### Rebase onto Electra

- We initiated FOCIL development based on fulu fork to quicly run a local devnet with a pair of CL and EL within a month. Utilizing the existing fulu fork rather than creating a new one accelerated our progress, which was a great suggestion by Terence. Thanks to that approach, we were able to ship it on time. Now that we expect to have PeerDAS merged into fulu anytime soon, we want to get indenpendent from it. Clients have been working on rebasing onto electra.

- Since we will no longer depend on fulu fork, ELs have the option to either rebase onto prague or modify Kurtosis to set osaka when eip7805 fork is activated, or introduce and use eip7805 fork for EL, just like we're doing with CL. We prefer to use fork independent of other forks and Jihoon will talk to the Devops team to find the best solution.

#### Implementation Updates

- Prysm has been almost rebased onto electra and will be working on the CL interop.
- Teku is working on local interop with Prysm. Teku currently has some issue with Geth, and onse resolved, a Docker image will be published.
- Lodestar has been rebased onto electra and still has state root mismatch issue. Lodestar https://github.com/ethereum/consensus-specs/pull/4003#discussion_r1992375936. This will make FOCIL more flexible and compatible with other proposals such as SSF.
- Nethermind is working on engine APIs following the spec and will be working on the CL interop.
- Lighthouse has been onto electra and added IL beacon chain event. Lighthouse will be working on the CL interop.

#### Questions

* It seems Geth waits for a certain period into the slot before producing an IL. Is this behavior intentional? Jihoon will investigate this issue and make sure EL returns a specific response rather than just an empty list when it’s not ready.

### Metrics Dashboard
* Katya has built a blind dashboard and will collaborate with Jihoon to create a Docker image and run it locally. Once it's done, Thomas will join to help determine the best metrics for evaluating FOCIL.

### Test Scenarios
* Thomas has reached out to the STEEL team and is looking for people will be working on this. Jihoon and Marc have expressed their willingness to help.

### Mempool Visualization
* An initiative for mempool visualization has been launched. It aims to visualize transaction propagation and transaction acceptance across different clients. The team is looking for feedback on visualization methods and potential use cases. Visualizing ILs per slot and marking the included IL transactions will be part of their roadmap.

### FOCIL with Blobs
* Thomas will focus on researching FOCIL with blobs over the next few weeks. If you’re interested in contributing, please reach out.

### Links

- [Protocol research call](https://x.com/barnabemonnot/status/1904532092513354223)
- [Decoupling throughput from local building](https://ethresear.ch/t/decoupling-throughput-from-local-building/22004)
- https://github.com/ethereum/consensus-specs/pull/4003#discussion_r1992375936
- [Mempool Visualization](https://github.com/punkhazardlabs/txpool-viz)
