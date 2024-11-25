# Ethereum Ethconomics

## [Ethereum Magicians Infinite Endgames Sessions 4](https://app.devcon.org/schedule/UFX3NX)

## Summary: 
Once again, Devcon will host Ethereum Magicians gatherings for the community to come together and discuss the most important topics in Ethereum's roadmap. Join us here to discuss the "infinite endgame" for Ethereum's economic model. We'll cover the role of Ether in the network's security, issuance proposals, out-of-protocol economic influences, and more! For more context, see: https://bit.ly/ethmag-sea

## Video: https://youtu.be/63w7kHh737w

## Panelists: 
Tim, Ansgar, Anders, Artem, Sacha

## Notes by:
June Manuel

## Devcon SEA - Nov 15, 2024

Context: compiling the folks who gave issuance talks during Devcon; give 5m tldr of talk and overall position; open for questions and community discussion

Ansgar: Gave a talk in the morning with Caspar on post published in February on why Ethereum should change it's issuance.
- Post had blow-back on twitter: feedback was that people needed to understand why issuance model needed to change
- talk focused on why model is currently unsustainable
- nominal v. real yield
- staking accounting anomalies; 1. accounting is indirect; 2. recipients are subset of same people who pay for it in the first place > leads to strange effect that you pay but then receive more money back
- for ethereum we are either on the side of a. small portion stakes with high yield or b. everyone stakes and no yield

Sacha: Researcher at Lido
- sympathetic to ansgars concerns; prefer if we were less radical about shifting the curve
- if we don't want to see another currency replace ETH, 50% is max we could go for ETH staked
- We should minimally change the reward curve until we can see how minimal changes affect the distribution of stake
- main concern is if we cut yields now at this staking ratio, we risk centralization
  

Artem: Researcher at Cyber Forum
- high-level view point: what do we optimize for and what framework should we use in thinking about this question?
-- if we want to do this in a coordinated, unified way, we need a framework/north star
--- network eth vs. asset eth vs. stakers
-- network first mentality: network eth is most important & stakers are v important bc they safeguard the network
-- there isn't a world where ethereum fails but ETH the asset succeeds 
- relative analysis: if you cut issuance, this happens, if you don't this happens. Need to be able to make informed decisions
- centralized exchange stakers v. LSTs 
- maximal viable security framework paper
-- private issuance is dangerous for network security

Anders: Case for removing issuance
- shift downward lowers amount of eth issued; reduces costs; increases surplus
- motivated by cost reduction, not surplus or increased rarity
- the rarity is always constant; 
- once we reduce issuance, without everyone staking, the consensus layer becomes better at protecting users

Tim: Question is, should we change the curve at all? If we change the curve, we degrade the hardness of the network because we change the assurances we've made to stakers and everyone else who rely on the protocol. What is the case for changing the curve, what should the burden of proof be, how do you respond to the risk of touching issuance at all?

Sacha: We all agree that there are macro level risks, where we disagree is burden of proof: how long do you wait for more real world data before shifting?

Ansgar: One big disagreement we keep running into is what should the precautionary principle be? What is the more risk averse thing to do?
- very worried about irreversible effects
- personally very concerned about parties only interested in maximizing profit 

Sacha: If we did have some sort of staking yield where we are sure it is not a centralized validator set; we don't know what that yield is for staking etfs to say they're not going to come in
- We could use more real world data, we have time (a few years) before getting to 50%

Artem: The fundamental disagreement is around precautions against what? It is not obvious what the problem is with large amounts of ETH staked;
- issuance cut will only exacerbate the issue, the precautionary move would be to *not* do that
- we need to do way more research and real world research with users; projecting what will actually happen
- what do panelist/audience feel like we need to optimize for?

Ansgar: one of the main reasons to POW > POS is because POS is massively more efficient;    

Anders: the risk if everyone stakes
- you increase number of attestations; if we decrease total number of aggregated attestations then we have a faster transactions
- single slot finality is bound by the number of attestations; if we reduce the quantity of stake then the number of attestations we have produce in aggregate reduces
- compromises consensus layer AND the app layer; 1-2 LSTs can have power over uses and applications
-- people are building on top of LST, not Ethereum, then we have an issue where the whole network is compromised

Tim: Why shouldn't we have an issuance curve that is sharp at the beginning and lowest at 50%?

Ansgar: How do we definancialize staking while keeping it attractive for solo stakers?
- could have a very narrow yield; keep reducing halving requirements; make it as friendly to solo stakers as possible
- ramp up corellation penalty even higher to deincentivize and make it unattractive to be a centralized staking party
- option: cut yield altogether and just require that anyone who holds eth has to stake

Artem: We should search for the end game, but I'm not sure if there is one.
- We want a decentralized validator set-- how do we achieve it?
-- the centralized options are very cheap, and the solo staker option is very expensive.
- we cannot hold that all professionals leave and enthusiasts leave; whatever is on the table majority will go to market and rest will go to enthusiasts leaving us with a similar, if not worse, distribution.
- Room for segmented model: decentralized and centralized staking

audience question 1: It is hard to predict things on past performance when we have bull/bear runs; hard to predict what will happen to staked ETF

on the question of negative issuance
- this would arise if we go beyond 50% stake

audience question 2: how is this any different than a central bank? changing the rules to 

Anders: We are trying to make a one-time, forever change based on community feedback that this is what people want; this isn't one group of people making a single decision.

audience question 3: We need to make sure that validators can bear the cost. Need to be absolutely certain that their costs are lower than Coinbase and Lido.
If you lower the issuance, then a greater percentage comes from MEV, which is even easier to centralize.

Ansgar: Yes, MEV is a huge problem and has been for a long time.
- Plan on ethereum roadmap to do MEV burn and MEV capture, would help to solve problems that MEV causes for solo stakers.

Tim: is there an upper bound that we could agree to commit to not exceeding?

Anders: In my talk I tried to pitch a social commitment to never exceeeding issuing 0.5% or 0.25% or 2^-8 (0.39%)of Eth 

Sacha: Foundationally, we don't agree with this change because it drastically changes the yields and we don't know what happens.

Ansgar: With the 50% range, we have a lot of consensus that a single staking LST is much more dangerous at this range.
We could wait, but the change will get more and more painful and harder to reverse if we wait.
There will be more staked eth the longer we wait.
- Any equilibrium close to 50% is still very uncomfortable

audience question 4: concerned that we are effectively trying to change the rules to control who the participants are.
why not have regulators control these sorts of things through taxing regimes?
essentially we're not going to change the rules but allow the participants to self-regulate.

Ansgar: the blockchain approach is to find the guarantees
we have to consciously make the decision that is best for the network; we can't do nothing and sit back and pray/
we have to be willing to design 

Artem: What we want is to save the decentralization of the validator set
- Is there a chance to save the decentralized part?
- We need to agree on the underlying mecahnism of currents.
-- Professionals will be there; we cannot hope that only enthusiasts will be there

audience question 5: is there a reason the design space is limited to only one issuance curve rather than partitioned?

Ansgar: 
- practical partition: rainbow staking vs. a future where we split off by duties: block production, attestations, censorship resistance participation, different subsets can be split off and incentivized differently.
- sometimes people offer that we should pay solo stakers more or geonodes from specific regions more-- not sustainable or would require increasing network complexity

audience6: solo staker
- if we reduce issuance, wouldn't it drive me to a lower cost alternative (e.g. liquid staking)?
- my fear is that this would drive everyone to pursue yield from other sources (restaking) and result in a worse outcome

Ansgar: if lower yield drives you to do that, 
yield pressues will become very very harsh even if we do nothing

audience7: reiterating concern about segmentation; one way is making sure anti-correlation penalties are very high


