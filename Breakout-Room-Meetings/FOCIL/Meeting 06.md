# FOCIL Breakout Room #06
Note: This file is copied from [here](https://github.com/ethereum/pm/issues/1363#issuecomment-2716867583)

## Meeting Info
- **Agenda**: https://github.com/ethereum/pm/issues/1363
- **Date & Time**: [March 11th, 14:00-15:00 UTC](https://www.timeanddate.com/worldclock/converter.html?iso=20240213T140000&p1=1440&p2=37&p3=136&p4=237&p5=923&p6=204&p7=671&p8=16&p9=41&p10=107&p11=28)
- **Recording**: [Here](https://youtu.be/i2K7TbOHeCk)

## Meeting notes:

### Research
In the EF retreat last week, there were many positive conversations about FOCIL. Many teams were happy with FOCIL and had the same opinion that it should be included in future fork.

### Stateless

* An interesting question has been raised: how can we design an extremely lightweight, stateless FOCIL node that could even run on a smartwatch? It may take some time to get to the stateless world, but we might one day be able to run nodes on smartwatches, propose ILs and synchronize in just a few minutes. It’s still early but it seems to be an interesting area of research.

### Privacy

* We’re looking for someone interested in working on the [zkFOCIL](https://ethresear.ch/t/zkfocil-inclusion-list-privacy-using-linkable-ring-signatures/21688) prototype. Our goal is to experiment with both SNARK and linkable ring signature schemes and to see if the ideas we have in mind are efficient. We also want to ensure the cryptographic methods we will introduce do not require intensive hardware resources so that zkFOCIL remains compatible with the stateless world.

### Compatibilities with Other Proposals

* As interest in FOCIL’s compatibility with other proposals continues to grow, exploring ways to make FOCIL and delayed execution fit together will be one of our primary focus areas.

### Dora the Explorer for FOCIL
* Jihoon modified Dora to listen to [IL events](https://github.com/ethereum/beacon-APIs/pull/490/files#diff-3cc6eaa800c1a4bd6adcd78f1722b466f7a24048a66e320c8f92872fbcd9eefbR156-R160) and store and display ILs. It will help debugging much easier and ~~we already found a buggy case that a slot with non-empty ILs has a block with empty transaction in Prysm-Geth interop. Prysm hasn't implemented reorg yet but still the block should have included all IL transactions.~~ (This turned out to be a bug in the Dora's IL implementation.)
* We will be able to see inclusion lists in each slot pages like this:

![Image](https://github.com/user-attachments/assets/e150c35a-3f48-480a-952f-3001f9ea0f21)

### Test Scenarios
* Writing out test scenarios as a reference would be quite helpful for development. Terence has already listed [basic cases](https://hackmd.io/@ttsao/focil-interop-test-cases) and we want to add more. Thomas will reach out to the Specs & Testing team to discuss how we can proceed with writing test vectors.

### Rebase on Electra
* Currently, eip7805 fork is scheduled to be activated after fulu fork, which is basically no-op at the moment. However, as we will be merging PeerDAS into fulu next week, we better rebase eip7805 onto electra. Doing so will save an entire epoch and make local testing easier, too.

### An Issue of State Root Mismatch
* Prysm and Lodestar were unable to inteorp and it turns out that Lighthouse is experiencing the same issue as well. Devs suspect a state root mismatch but it might be having two forks in consecutive epochs. Further investigation will take place after we rebase to electra.

### Metrics Dashboard
* Katya is working on metrics dashboard with Prysm and will be opening a PR of a list of metrics for review.

### Links
- [zkFOCIL: Inclusion List Privacy using Linkable Ring Signatures](https://ethresear.ch/t/zkfocil-inclusion-list-privacy-using-linkable-ring-signatures/21688)
- [FOCIL High-Level Test Cases](https://hackmd.io/@ttsao/focil-interop-test-cases)


