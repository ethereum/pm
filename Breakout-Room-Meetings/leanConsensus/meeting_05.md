# leanConsensus (fka beam chain) call #5: research updates | APS (attester-proposer separation)

**Prev:** [Call 04](https://github.com/ethereum/pm/blob/master/Breakout-Room-Meetings/leanConsensus/meeting_04.md)

**Meeting Date/Time:** Friday 2025/5/2 at 14:00 UTC

**Meeting Duration:** 1 hour

[GitHub Agenda & Links to Presentations](https://github.com/ethereum/pm/issues/1447)

[Audio/Video of the meeting](https://youtu.be/5OOzMqCOoKM)

Moderator: Justin Drake

Facilitators: Ladislaus von Daniels & Will Corcoran
- Facilitator emails: ladislaus@ethereum.org // will@ethereum.org
- Facilitator telegrams: @ladislaus0x // @corcoranwill

## Agenda
| Agenda Item | Topic |
| --- | --- |
| 01 | Social Updates by @justindrake |
| 02 | APS Overview by @justindrake |
| 03 | APS (attester-proposer separation) by @Ma-Julian |


## 01: Social Updates by @justindrake

| Topic | Subtopic | Details |
| --- | --- | --- |
| Introduction | Context Setting | Call #5 on APS (Attester-Proposer Separation) with Julian as presenter. |
| | Upcoming Events | - Call #6 in two weeks with presentations by Vitalik (implemented 3SF in Python)<br>- Additional presentations by Roberto, Francesco, and Luca<br>- beam day Canne on June 29th |

## 02: APS Overview by @justindrake

| Topic | Subtopic | Details |
| --- | --- | --- |
| APS Goals | Zen Staking | The goal is to make stakers/validators as unsophisticated as possible by removing complexity. |
| Current Validator Problems | MEV Complications | - Validators need to install `mev-boost` middleware<br>- Must select relays (complicated depending on regulations)<br>- MEV spikes create unfriendly conditions for decentralization (b/c median validator will end up making less than the average validator)<br>- Median validator earns less than average validator due to jackpot distribution<br>- Incentivizes creation of smoothing pools (adds centralization and complexity)<br>- Timing games require sophisticated operation<br>- Moral dilemmas from receiving potentially unethical MEV (from hacks, sandwiching, etc.) |
| | Proposer Commitments | - Need to use `commit-boost` software, which allows proposers to opt into commitments; one of which is pre-confirmations<br>- Pre-confirmations require gateways (similar to relays)<br>- Need to add collateral to play pre-confirmation game<br>- All adds unwanted complexity to validators |
| APS Solution | Concept | - Separation of roles between testers and proposers<br>- All sophistication falls on proposers (separate entities)<br>- Testers can be simple entities running on minimal hardware (Raspberry Pis or smartwatches) |
| Derisking Progress: beam chain  | Most Derisked (5 out of 5) | - Smarter Issuance (e.g. stake cap) would be done either pre-beam or post-beam<br>- Strong Randomness (e.g. MinRoot VDF) would be done post-beam fork<br> |
| | Nearly Derisked (4 out of 5) | - Censorship Resistance (e.g. FOCIL) an EIP already exists, this could ship with Glamsterdam<br>- Faster Finality (e.g. 3SF)<br>- Chain Snarkification (e.g. Poseidon2 + zkVMs) making great progress w/ zkVMs (checkout [ethproofs.org](https://www.ethproofs.org)) and even if there was an issue with Poseidon2 you can just add more internal rounds to the hash function to boost the security.
| | Derisking (3 out of 5) | - Faster Slots (e.g. 4 second slots)<br>- Smaller Validator (e.g. rainbow staking / stake cap)<br>- Quantum Security(e.g. hash-based sigs)|
| | Least Derisked (2 out of 5) | - APS (attester isolation, e.g. execution tickets)<br>- APS has been derisked the least among proposed beam chain consensus layer improvements<br>- Multiple design candidates exist, but no clear winner<br>- Fundamental tradeoffs need to be made |


## 03: APS (attester-proposer separation) by @Ma-Julian

| Topic | Subtopic | Details |
|-------|----------|---------|
| Background | APS Definition | - APS is about "firewalling" attesters and proposers<br>- Changes how proposers are selected on Ethereum |
| | Current Selection Process | - Random validator selection via RANDAO<br>- Randomly selected validator typically chooses builder via `mev-boost`<br>- Validator sells execution proposing rights to builder |
| | APS Goal | - Allow Ethereum protocol to choose builder directly instead of indirectly |
| Initial APS Motivation | Timing Games | - Economic benefits from proposing after official deadline<br>- Creates geographic centralization (favors proposers near other proposers)<br>- Proposers in remote locations must propose earlier |
| Early APS Proposals | Execution Tickets | - Proposed by Justin in late 2023<br>- Fixed price tickets with flexible supply<br>- Tickets purchased in advance (e.g., 32 slots)<br>- Proceeds are burned<br>- Winner selection is probabilistic based on tickets purchased<br>- Separates beacon proposer from execution proposer |
| | Execution Options/Auctions | - Proposed by Barnabé<br>- Similar to `mev-boost` but with protocol-enforced highest bid<br>- Uses MEV-burn to enforce selection of highest bidder<br>- Auction proceeds are burned |
| Critiques of APS | Centralization | - Market becomes riskier (Quintus & Connor from Flashbots)<br>- No information means no specialization (multiple researchers)<br>- Execution tickets may be more decentralizing than auctions |
| | Multi-slot MEV | - More value can be extracted when optimizing across multiple blocks<br>- Unclear how significant multi-slot MEV actually is |
| APS Design Goals | Key Requirements | - Creating competitive builder market<br>- Avoiding multi-slot MEV extraction<br>- No MEV for validators (timing games)<br>- Pre-confirmation friendly |
| | Connection to EPBS | - EPBS (Enshrined Proposer Builder Separation) aims to remove relay role<br>- APS also removes relay role while addressing other goals |
| Proposed Solution | Just-in-Time Execution Tickets | - Execution tickets two slots ahead (not 32)<br>- Bids flow into smart contract as transactions<br>- Market closes after bids recorded<br>- Randomness revealed after previous block committed<br>- Winner selected proportional to ticket purchase |
| | Bidding Process | - Bids are regular transactions on execution layer<br>- Uses Fossil for censorship resistance<br>- Fixed price, flexible supply market (better for decentralization) |
| | Winner Selection | - Randomness revealed after block 99 committed<br>- Minimal look-ahead (prevents multi-slot MEV)<br>- Enables pre-confirmations |
| | Randomness Challenges | - Requires high-quality randomness<br>- Could use threshold committee (has liveness implications)<br>- Could use encrypted MEVs and post-state root |
| Alternative Approaches | Execution Tickets | - Optimizes for pre-confirmations<br>- Uses existing RANDAO<br>- Allows multi-slot MEV extraction<br>- Better for pre-confirmation market |
| | Just-in-Time Execution Auctions | - Optimizes against multi-slot MEV<br>- Auction in beacon block<br>- Less friendly to pre-confirmations<br>- Requires additional availability committee |
| Research Tracks | Possible Directions | - Investigate randomness options<br>- Evaluate importance of multi-slot MEV<br>- Assess pre-confirmation adoption<br>- Determine if APS is still needed (timing games currently small) |
| Current Status | Timing Games | - Currently not showing major profits (based on Toni's timing PIX)<br>- APS still valuable for removing relays and implementing MEV burn |
| Next Steps | Decision Points | - Make trade-off between preventing multi-slot MEV or supporting pre-confirmations<br>- Could prepare multiple APS subspecs and decide closer to beam fork<br>- Need more information on multi-slot MEV significance |



# Audience Questions and Discussion Topics

| Question/Discussion | Response/Notes |
|---------------------|----------------|
| 1) Does this assume SSF (Single Slot Finality)? | - APS does not assume SSF necessarily |
| 2) How do we deal with safety/equivocations without SSF? | - Block proposal equivocations aren't as consensus-critical as FFG equivocations<br>- Could use FOCIL approach (ignore equivocating blocks)<br>- Could implement slashing<br>- APS has less impact on fork choice than ePBS |
| 3) Does this assume delayed execution? | - Doesn't necessarily assume delayed execution |
| Do you need better randomness than RANDAO? | - Yes, the proposal relies on better randomness than current RANDAO |
| 4) What if the bid itself is front-run? | - Bids are simple objects (number of tickets at fixed price and winner ID)<br>- Orders are "order agnostic" - front-running has limited impact<br>- Encrypted MEVs could help with this issue |
| 5) Would there be timing games for bidding? | - Encrypted bids could help<br>- Nash equilibrium timing is not obvious (could be early or late)<br>- By assumption, no new information is revealed during bidding slot |
| 6) Can bids fill up FOCIL capacity? | - FOCIL doesn't increase gas supply<br>- 128 kilobytes available across 16 inclusion lists<br>- Should be enough space for all ticket transactions |
| 7) Does this mean we're only burning MEV from public MEV transactions? | - FOCIL is used for censorship resistance, not as MEV oracle<br>- Amount burned is tickets × price, independent of source |
| 8) Would the competitive execution proposer market still be satisfied in JiT execution auction? | - Competitiveness exists on a spectrum<br>- Execution tickets better than execution auctions for competition<br>- Just-in-time better than far in advance<br>- Trade-offs exist between timing and mechanism |
| 9) Are we trending toward pre-confirmations being a huge deal? | - Both pre-confirmations and multi-slot MEV have induced demand arguments<br>- Pre-confirmations have significant potential<br>- Early signs suggest multi-slot MEV might not be substantial |
| 10) Is access to flow more important for centralization than multi-slot MEV? | - Multi-slot MEV is also a user experience issue, not just centralization<br>- Even if not the dominant centralization factor, has negative functionality |
| 11) How close are we to having fancy randomness with VDFs? | - VDFs not suitable for low-latency randomness<br>- Threshold cryptography needed but has complications:<br>  - a) Requires fallback for liveness<br>  - b) Unclear how to do in post-quantum way<br>  - c) Attributability problems if collusion occurs |
| 12) Can we study real-world examples? | - Fast lane in Aron provides data on future prediction markets<br>- Solana has four slots in a row per proposer, may yield insights on multi-slot dynamics |
