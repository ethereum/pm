# FOCIL Breakout Room #03

Note: This file is copied from [here](https://github.com/ethereum/pm/issues/1266)

### Meeting Info

**Agenda**: [ethereum#1266](https://github.com/ethereum/pm/issues/1266)

**Date & Time**: [January 28, 14:00-15:00 UTC](https://www.timeanddate.com/worldclock/converter.html?iso=20240213T140000&p1=1440&p2=37&p3=136&p4=237&p5=923&p6=204&p7=671&p8=16&p9=41&p10=107&p11=28)

**Recording**: [here](https://www.youtube.com/live/azvPMD2us0Y)

## Meeting notes:
## Meeting Summary  

The meeting had no formal presentation but focused on updates and discussions related to the implementation and testing of features for clients.  

## Key Highlights  
- **FOCIL as a Hard Fork**: Terence suggested making FOCIL its own hard fork instead of merging it into Fulu, improving tooling and testing flexibility.  
- **Testing Scenarios**: Initial tests covered transaction inclusion and basic functionalities, but censorship testing and equivocation scenarios still need exploration.  
- **Multiple EL Scenarios**: Challenges in handling various EL cases and ensuring comprehensive test coverage were discussed.  
- **Simulating Censorship**: Different methods, such as modifying mempools and controlled test environments, were considered.  
- **Testing Challenges**: Jihoon highlighted client variations in censoring and equivocating behaviors, suggesting tools like Kurtosis for reproducible scenarios.  
- **Interop Testing**: Additional insights on transaction handling and interop testing were shared.  

## Updates from Other Teams  
- **Lodestar**: 95% implementation progress, ongoing internal reviews, and successful initial P2P testing.  
- **Prysm**: Focus on testing and implementing inclusion-related features, particularly Beacon API improvements.  
- **Lighthouse**: Limited bandwidth, but taking over efforts to push implementation forward.  
- **Erigon**: P2P layers implemented, ongoing RPC work, aiming for a minimal working implementation in two weeks.  

## Tooling and Visualization  
- **Metrics Standardization**: Discussed efforts to standardize metric naming conventions.  
- **Mempool Visualizer**: Development in progress to help analyze and improve testing scenarios.  
- **API Improvements**: Suggestions made for additional API enhancements and streaming endpoints for inclusion lists.  

## Next Steps  
- Client teams aim to complete working FOCIL implementations before the next meeting.  
- Continued focus on interop testing across clients and refining real-world testing scenarios.  
- Future discussions on privacy for IL committee members and evaluating censorship resistance.  
- Acknowledgment of significant progress across teams, with results and metrics expected in upcoming sessions.  
- The next meeting is scheduled in two weeks for further updates on FOCIL implementations and interop testing.  


Links shared in meeting

- https://hackmd.io/@ttsao/focil-interop-test-cases

- https://hackmd.io/@jihoonsong/ByFgyGRDJg

- [Add EIP-7805 (FOCIL) endpoints beacon-APIs#490](https://github.com/ethereum/beacon-APIs/pull/490)

- https://github.com/ethpandaops/tooling-wishlist/blob/master/open-ideas/txpool-viz.md
- [Eth Magicians](https://ethereum-magicians.org/t/focil-breakout-3-january-28-2025/22704)
  