# Issuance policy session at Devcon 2024

### Summary 

This session will discuss the motivations, impacts and downsides of a change in issuance policy, deliberate on various endgames ("practical endgame"/"soft cap"/"hard cap"), and seek to build consensus on the preferred reward curve or its general range. We will also explore any other topic that participants feel are important to the conversation, including the viability of capping the issuance rate (e.g., at 0.5%), both as an intermediate solution and social commitment.

**Facilitator:** Anders and Ansgar

**Note Taker:** Nixo took the following [notes](https://efdn.notion.site/Issuance-10-Nov-24-L1-R-D-129d98955541806db131f0e15f4360bb).

### Pre-Reads

**Current state of research**

* [FAQ: Ethereum issuance reduction](https://ethresear.ch/t/faq-ethereum-issuance-reduction/19675)
* [Practical endgame on issuance policy](https://ethresear.ch/t/practical-endgame-on-issuance-policy/20747)
* [Endgame Staking Economics: A Case for Targeting](https://ethresear.ch/t/endgame-staking-economics-a-case-for-targeting/18751)

**[Optional] Chronological list of write-ups from the early debate**

* [Minimum Viable Issuance](https://notes.ethereum.org/@anderselowsson/MinimumViableIssuance); easy-to-read [follow up](https://notes.ethereum.org/@anderselowsson/Foundations-of-MVI).
* [Properties of issuance level: consensus incentives and variability across potential reward curves](https://ethresear.ch/t/properties-of-issuance-level-consensus-incentives-and-variability-across-potential-reward-curves/18448)
* [Initial Analysis of Stake Distribution](https://ethresear.ch/t/initial-analysis-of-stake-distribution/19014)
* [Reward curve with tempered issuance](https://ethresear.ch/t/reward-curve-with-tempered-issuance-eip-research-post/19171)
    * Also discussed in: [Electra: Issuance Curve Adjustment Proposal](https://ethereum-magicians.org/t/electra-issuance-curve-adjustment-proposal/18825)
* [Issuance Issues — Initial Issue](https://notes.ethereum.org/@mikeneuder/iiii)
* [Reward curve with capped issuance](https://notes.ethereum.org/@anderselowsson/Reward-curve-with-capped-issuance)
* [Issuance Issues — Subsequent Soliloquy](https://notes.ethereum.org/@mikeneuder/subsol)

**[Optional] See also**
* [Part 3: The Scourge](https://vitalik.eth.limo/general/2024/10/20/futures3.html)
* [Collection](https://issuance.wtf/) of material from the issuance debate.

## Agenda 

1. A 20 minute introduction by Anders on the current state of research, focusing on the motivations, impacts and downsides of a change in issuance policy, as well as the viability of a practical endgame. A 10-minute follow-up by Ansgar with a focus on stronger capping mechanisms (soft cap/hard cap).
2. The floor is open for addressing three key aspects of an issuance reduction in the following order
    a. Motivations (the why)
    b. Impacts (the what)
    c. Downsides (the why not)
3. The floor is then open for addressing aspects unrelated to a, b, and c. 
4. The preferred range of issuance among partcipants is finally discussed (the how).
This discussion will naturally relate to the different categories that are under consideration:
    * [Do nothing](https://ethresear.ch/t/faq-ethereum-issuance-reduction/19675#h-1-do-nothing-31): leave issuance as is.
    * [Mild tempering](https://ethresear.ch/t/reward-curve-with-tempered-issuance-eip-research-post/19171): for example capping issuance at an issuance rate of 0.5%.
    * [Practical endgame](https://ethresear.ch/t/practical-endgame-on-issuance-policy/20747): reducing issuance close to zero but retaining positive regular reward for solo staking.
    * [Soft cap endgame](): reward curve that reduces the issuance yield to zero when around half the ETH is staked, and then remains at zero. 
    * [Hard cap endgame](https://ethresear.ch/t/endgame-staking-economics-a-case-for-targeting/18751): capping the quantity of stake through issuance that goes to negative infinity.
    
## Notes 

# Issuance - 10 Nov ‘24 (L1 R&D)

ANDERS

- Hypothetical distribution of reservation yields
- Where does the supply curve meet the demand curve?
    - Seems to be ~60mil (0.5 stake ratio)
    - Half of that is sufficient to secure Ethereum
    - Overviews of negatives of too much stake ratio
- A lower reward curve creates a cost reduction that benefits all stakers (~$1bil)
    - Surplus moves from stakers to all ETH holders
- High stake participation puts pressure on
    - Consensus layer
    - App layer
        - Monopolistic pressure
        - Systemic risk if LST fails
- Downsides
    - Solo stakers don’t have economies of scale
    - LST holders may have lower reservation yield (solo stakers potentially exit first with lowering yields)
    - MEV is a bigger concern at lower issuance (increases reward variability for solo stakers)
    - Degrades consensus incentives under equilibrium
    - Complicates OrbitSSF incentives design
- Overview of “Practical Endgame” curves
    - 0.5% issuance rate should be sufficient to secure the chain - regardless of the curve under that, potentially could commit to that (unfortunately lots of community pushback)

Impact

- Anders illustrates w isoproportion graphs where stakers are same or better off at lower issuance depending on dilution

ANSGAR

- There’s really no skill limit / upper bound for those looking to liquid stake
- Solo staking has a semi fixed supply
- At higher stake, yield is being diluted, stakers earn less real yield, all ETH holders diluted and are pressured / forced to stake
- Larger operators benefit at higher stake ratio because of the economies of scale
- Taxes don’t care if your yield is real or nominal, they’ll still take their cut regardless of your dilution
- Risk of monopoly LST - systemic risks for Ethereum
- LST monopoly leads to network effects for the LST
    - decreases the ‘moneyness’ of raw ETH
- Do we want a policy of minimum viable issuance as a community?

Curve types

- Options as stake ratio increases: Go to zero? Simply decrease?
- Proposal: one time issuance reduction
    - Combine with a minEB reduction
    - Partial exits of all existing validators

Questions

- Social / political question: what have you learned from negative pusback?
    - A: Focusing on explaining the problem rather than the solution, leaving solutions open to discussion
    - More sensitive to individual stakeholders (e.g. DVT)