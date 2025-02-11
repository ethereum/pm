# Execution Layer Meeting #201
### Meeting Date/Time: Dec 5, 2024, 14:00-15:30 UTC
### Meeting Duration: 1h35m 
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1197)
### [Video of the meeting](https://youtube.com/live/Umh7ZKukmtY)





### Moderator: Tim
### Notes: June

| S No | Agenda | Summary |
| -------- | -------- | -------- |
201.1 | **Pectra updates: Mekong & devnet-5 updates** | Mekong testnet is operational ~97% attestation performance; minor issues to address, mostly good on Mekong front and focused on getting all the PRs merged for devnet-5; devnet doc has been updated by testing team to show where the status of tests are.
https://notes.ethereum.org/@ethpandaops/pectra-devnet-5
201.2 | **Pectra Scoping** | BLS gas pricing discussion of Marek's PR [here](https://github.com/marchhill/bls-precompile-benchmarks/blob/main/proposed-changes.md); Most client teams in production and on call agreed that the proposal works for them to move forward with for now; need confirmation from Besu async; can modify with more fine-grain anaylsis in the future.
201.3 | **Pectra Scoping** | Discussion on [EIP-7623](https://eips.ethereum.org/EIPS/eip-7623) inclusion and update with additional security considerations [EIPs#9086](https://github.com/ethereum/EIPs/pull/9086_); 7623 focuses on capping transaction payload sizes to improve network performance and security; client teams all agree it would be a small thing to implement and wouldn't significantly impact timelines; decision to move forward with 7623 on devnet-5 pending confirmation from testing team.
201.4 | **Pectra Scoping** | Discussion on [EIP-7762](https://eips.ethereum.org/EIPS/eip-7762) inclusion; proposes minimum blob price increase; disagreement on whether to include this in Pectra; deferred one week for feedback from rollups and testing.
201.5 | **[EIP-4444 & EIP-7639 rollout](https://hackmd.io/Dobc38YVQ1qmbbyI6LcFqA)** | Discussion and disagreement about best protocol versioning for this implementation and whether or not some clients should be able to provide historical blocks while others don't; concern about protocol fragmentation; Piper to compile notes and create discussion async.
201.6 | **[EIP-4803] (https://eips.ethereum.org/EIPS/eip-4803)** | This EIP is proposed to be enabled from genesis and it limits gas limits on transactions; no objections conceptually but won't be address until after Pectra testing; Alex to create a PR. 
201.7 | **[Potential ACD Improvements](https://ethereum-magicians.org/t/allcoredevs-network-upgrade-ethmagicians-process-improvements/20157/51)** | Agreement to add [Declined for Inclusion] status for EIPs that will not be included in the hard fork; EIPs still open for discussion and available for future hard forks; agreement to include all non-consensus protocol changes in list of hard fork changes to make sure everything is up to date for each hard fork.
201.8 | End of year coordination and holiday meeting schedule | Testing call on Dec 23, Cancel ACDE on Dec 26, Cancel testing call on Dec 30, Replace ACDC by testing call on Jan 2

### 201.1 | Pectra updates: Mekong & devnet-5 updates
**Tim**: Welcome everyone to ACDE #201. Couple things on the agenda today, most importantly we can hopefully finish the scope of Pectra and be able to move forward with the specs. After, some conversations around EIP4444 as well as 7639 about dropping history. Then there was an edge case to revist around capping transaction gas amount and then if we have time left, there are a couple ACD process improvements I wanted to cover.

Pari, Banabus, either of you want to give an update on testnets?

**Pari**: We have Mekong continuing to run-- we're at 97% attestatino performance. Grandine team has pushed a lot of fixes, mostly okay now. Some problems still with Ethereumjs and Nimbus EL, but mostly good on Mekong front and focused on getting all the PRs merged for devnet-5. 
PRs here: 
CL - https://github.com/ethereum/consensus-specs/pull/3800
CL - https://github.com/ethereum/consensus-specs/pull/4023
EL - https://github.com/ethereum/execution-apis/pull/574

Devnet doc has been updated by testing team to show where the status of tests are.
https://notes.ethereum.org/@ethpandaops/pectra-devnet-5


**Tim**: Any other EL PRs that you want to bring people's attention to?

**Ansgar**: Regarding [EIP-7691](https://eips.ethereum.org/EIPS/eip-7691), there was this open question of what exact update fraction we would go with and we chose the number that is the middle sensitivity between 3-6. We couldn't have 6 blobs less than the target or 3 blobs more than the target, so we picked the middle; now a very full block will have slightly less than 12% increase and a fully empty block will have slightly more than 12% decrease. 

**Toni**: Was just in the process of reviewing the EIP-7691 PR; only one small typo then we can merge.

**Paritosh**: lightclient brought up [7702 txpool](https://eips.ethereum.org/EIPS/eip-7702) in chat, maybe he wants to discuss?

**lightclient**: just checking again to see if anyone has looked into it or implemented it? We are in the process of implementing now.

**Marek**: Nethermind is looking into it, but others can comment on that.

**Anders**: Yes, we had a discussion on Discord [interop channel]. We had some suggestions but it seems the discusssion stalled. 

**Tim**: As people work on this, share any updates or designs in the discord chat.


-------------------------------------
### 201.2 | Pectra Scoping | BLS gas pricing

**Tim**: Moving on, it's worth chatting about Pectra scope changes. It feels like we're close to finalizing scope, it would be ideal if we could do so on today's call so we have a final set of specs to work with before the holidays. We can come back in January with a clear target to implement.

On CL, everything seems pretty resolved.

On EL, some major open questions: first is BLS gas pricing, second is whether to include EIP-7623, lastly is EIP-7762, an adjustment to the blob base fee.

Let's start with BLS one since it's already included in Pectra and needs to be fixed. Anyone with context on latest BLS pricing discussion? 

**Marek** I took all the numbers and opened a PR, in the [link here](https://github.com/marchhill/bls-precompile-benchmarks/blob/main/proposed-changes.md) we have Nethermind BLS pricing proposal and it would be great if it could be validated by other teams. I think Pawel had a different idea how to price MSM (multi-scalar-multiplication) operations but I don't fully understand, so we need to agree with Pawel about this.

**Tim**: Have any other teams reviewed or have any strong opinions?

**Kevaundray**: From the pricings, atleast from what we know from the current numbers, Nethermind for G1MSM would need to go up by 2.5x, Besu and Geth would need to go up by 2x, and evmone would need to go up by 3x. For G2, Nethermind is 1.5, Geth and evmone are 2x. We could go with these pricings but they're more costly than what we would like.

**Tim**: By 'these pricings,' you mean Marek's current PR?

**Kevaundray**: We took the worst case of what everyone has already given us in order to cover all of the clients. It's just a more coarse way to do the pricing.

**Tim**: Do you have a sense of the impact on users for having this more coarse pricing scheme?

**Kevaundray**: We don't know exactly because it depends on the use cases. My suggestion would be to commit to coarse pricing and we can use other tools to determine a new curve to use. At the moment, we haven't committed to any pricing. I would like to avoid the 3x that is there but it's the only one we've seen imperfectly that covers everyone else.

**Tim**: So I understand evmone was slow on some of these; that's the one that would be covered by 3x?

**Kevaundray**: Right, the next lowest would be the Nethermind proposal of 2.5x scaling.

**Tim**: Is evmone used in production by any clients?

**Andrew**: Not yet, but we would like to switch Erigon to evmone. At the moment it still uses GoLangEVM which is essentially the same as used in Geth. 

**Tim**: Nethermind uses the same library. I'm trying to understand why evmone is slower and does it make sense to put our worse case on an evm that is not beign used in production today or should we use whatever is already in production?

**Kevaundray**: To answer the first question, evmone is different and has issues even when using the same library because everyone is basing it off ez-recover, but that's not the same across every library.

**Radek**: This is not exactly about evmone, but about the blst library, which is used by Nethermind and Reth. This means that the speed is not only the case with evmone but with the library itself.

**Kevaundray**: Right, so Nethermind uses the same library but it's a 2.5x. This goes down to the issue of ez-recover not being the same across everyone because everyone is scaling based on ez-recover.

**Tim**: Anyone from Geth or Besu have time to review? Jared says Geth would be good with Nethermind's proposal. My sense is that if Besu is also good with it we should move forward, even if it is slightly underpriced for evmone.

**Kevaundray**: What do people think about the proposal to commit to 2.5x or 3x and then wait for a gas optimizer tool to possibly give us finer-grain numbers, but we commit to something for the time being?

**Tim**: Discussion in chat to agree async but before devnet-5. Marek, how much time do you think we need to agree to this? If we could get consensus on your PR as a basecase that we could modify later on, is there a reason to push this back async before we make the decision?

**Marek**: There is no clear number, we can discuss async, but we should decide before devnet-5.

**Tim**: It is fine to do it async, but recommend getting to a resolution on testing call Monday. Get us to as final of a pricing scheme as soon as possible.

**Stokes**: Kev's recommendation is a good way to make progress today. Sounds like this PR gets us directionally closer to what we all like.

**Tim**: If all of the production clients are fine with this number, we should go ahead and merge. Worth getting a sanity check from Besu, but assuming they can approve async today or tomorrow, we merge.

**Stokes**: If anyone has a BLS-signature verifier that works with the latest for Pectra, let me know on Discord. Would be nice to have a sense of end-to-end cost for this.

-------------------------------------
### 201.3 | Pectra Scoping | [EIP-7623](https://eips.ethereum.org/EIPS/eip-7623) inclusion and update discussion with additional security considerations [EIPs#9086](https://github.com/ethereum/EIPs/pull/9086_);

**Tim**: Next up is EIP-7623, Danno you raised some issues on EthMagicians and then Toni opened a PR to address them. Toni, do you want to give a quick recap on those changes?

**Toni**: We discussed on the consensus layer call last week as well. The main contention we always had with 7623 was not about the mechanism but the scope of Pectra itself. Regarding Danno's suggestions, I included them and incorporated them into the EIP. You can now find a more elaborated backwards compatibility section and security considerations, including the concerns we clarified that William raised about the gas sheltering. I would now propose that we include it and ship it in devnet-5, especially in light of current discussions in the community about potential gas limit increase and agreeing on the blob increase. I think it will be important to make sure we limit EL payload size.

**Tim**: This PR seems to address Danno's issues. Does anyone think we should *not* include this?

**Stokes**: I'd like to hear what EL client teams think in terms of implementation complexity? I think it has a lot of merit on the security front, but is it going to add weeks of delay to Pectra?

**Tim**: Reth, Besu, and Ethereumjs say in chat the impact should be low. Lightclient says it adds complexity to reasoning about tx cost and may introduce some weird gas sheltering schemes. 

Question from Pari: on the testing side, do we have a sense of how big of a lift this is to include?

**Mario**: No sense as of yet, but I think it is not going to be straightforward. i don't have a clear idea yet. We have made some preparations for this EIP in our repository, but still we need to check and see how long-- probably couple of weeks to implement this.

**Tim**: How do you feel about the rest of the fork so far? Is the rest of Pectra in a relatively good spot?

**Mario**: We have PRs for everything for devnet-5. It's looking good, we are probably going to be able to make a release soon. For 7623, I don't think that should be a blocker, but if anything comes up I can signal it.

**Daniel**: I just wanted to propose that maybe instead of including in devnet-5, we include it in devnet-6 to not block testing of devnet-5.

**Tim**: It depends on how fast we think devnet-5 will be finalized? If it's in the next week then sure, but if it's going to be a couple weeks then we can include this. I'd rather devnet-5 be the final devnet.

Does anyone think devnet-5 is ready for launch in the next week or two?

**Daniel**: We should discuss other EIP to get a good sense of full scope.

**Tim**: Regardless of devnet-5 or devnet-6, any strong objections to including 7623 so we can finalize the Pectra scope and spec?

**Barnabus**: The main blocker is 7742 still on the implementation side. If this is a small implementation on the EL side, then we might not even be ready with 7742 before we would be done with this new EIP. 

I haven't heard from any client teams that are 100% done with it on CL or EL.

**Tim**: Is anyone done? Reth and Besu say they are close, but not done. If teams are mostly done with 7742 and think this is doable, then we can move forward with it. We can discuss devnet-5 or devnet-6 after once we have a better sense. 

**Stokes:** Can we go ahead and include it now and then take it out in a week or two if it ends up being bigger than we think?

**Paritosh**: Maybe we give the testing some time to look into it? If they say it will take another 3 weeks to have the tests for 7623 then we don't want to block devnet-5 for this one EIP. 

**Mario**: We can have an estimate on Monday's testing call.


-------------------------------------
### 201.4 | **Pectra Scoping** | Discussion on [EIP-7762](https://eips.ethereum.org/EIPS/eip-7762) inclusion

**Tim**: Next on the agenda is EIP-7762, which is the minimum blob price increase. We discussed this as well on last week's call and couldn't quite come to a decision; anyone have thoughts about what to do there?

**Toni**: We also discussed on last week's Consensus Layer call. We agreed that we don't want to do *all* the changes that are proposed at once on Pectra. There were discussions about picking out minimum blob base fee and only shipping that. I'm indifferent about that one, but I think we should stick to *not* including all the base fee changes in Pectra.

**Ansgar**: The decision is indeed to not ship the big package.This EIP is only for minimum base fee increase -- a one line change-- and was modified last week to include excess gas reset. You can have a look at the EIP, it is still very smol and the excess gas reset is just one IF statement. One line change is eseentially a 4 line change now. 

Given that it is so tiny, and has a meaningful improvement to UX for rollups who have been signaling that this would be valuable for them, I am in favor of including this.

**Max**: Maybe one more thing in terms of complexity of test cases. If there are going to be changes to the update rule, I think the additional test cases from including this EIP-- along with the blob increase which will adjust the rate of change-- will be pretty minimal because you'll already have to change the test cases for that.

**Ansgar**: This is a really good point and one thing that came up in the update fraction change discussion. I think it makes testing slightly simpler even.

**Tim**: Have any EL teams reviewed this? Ethereumjs seems in favor. 

**Stokes**: Are we talking about just raising the minimum fee or the other things in this PR?

**Toni**: Only the minimum fees.

**Ansgar**: The decision is on the current state of the EIP, no open PRs.

**Stokes**: Okay, yes, this is much simpler. It does add another EIP and overhead of testing.

**Tim**: The downside of not doing this is that we stay in this awkward world where sometimes the blobs are effectively free and sometimes they get repriced very slowly relative to the market.

**Max**: The problem is more that they get repriced very slowly recently and when they reprice very slowly, every 20 hours, where we have a 3h period of price discovery and a 3hr period of going back down to less capacity overnight when there's less demand. In that 3hr period we're basically defaulting to first price fee market.

**Stokes**: And that's a problem because rollups don't want to think about volatile fee markets?

**Max**: It makes it so that if the rollups are charging for gas they have to do so based on a first-price fee market, which noone understands, versus says your gas on rollup is a function of blob fee on Ethereum today. Makes it much easier for rollups to read and provide gas pricing for their users when it's the number from the controller rather than number from controller + whatever else is happening in first-price fee market + whatever is happening in MEV land for that particular block.

**Stokes**: I think the strongest counter argument I've heard is what I've seen from lightclient in the chat, that it's just early and presumably we will in price discovery for the blobs and this issue will go away.

**Max**: We are at price discovery but the demand fluctuates. 

**lightclient**: I don't think we should orient the Ethereum fee market to be US-focused, which is what Max is saying.

**Tim**: It's more that whenever noone uses blobs or when people decide to use blobs again, we're too slow to adapt.

**lightclient**: It's still too early in the life of blobs for us to be meddling with the actual price mechanism. Let's revisit it again in the next fork if we're still having problems.

**Ben Adams**: Aren't we proposing doubling the blobs? That's just going to make it worse. It's not like we're not meddling.

**Max**: There are already several changes to the controller as well as the blob increase in this fork. We have very strong theoretical reasons why this would increase price discovery with very minimal changes. In total this is, at most, $100,000 a year change to the blob prices, but we think it will make the speed of price discovery much fast. We now see in the data that this is happening very often.

**lightclient**: We also thought that price discovery was just going to happen once before we implemented blobs, which was wrong. How can we know that this proposal would fix all these problems?

**Max**: That is not what the proposal claims to do. It claims to be an adjustment, which is low overhead, that we know will improve by some factor. It won't make the blob market perfect, but it will improve it.

**Ansgar**: I would really strongly recommend adding this EIP. It is a strong change and the situation will get significantly worse from today with this change in throughput. We now maximally can increase the block base fee by 8% per block instead of todays 12%. It takes significantly more time to ramp up...Rollups would prefer us adding this. Testing complexity is basically zero because you already need to run the tests.

**Paritosh**: Note that each EIP we add will delay Pectra. So the choice is more scaling faster or more EIPs + scaling slower. There is no world in which we can have more EIPs and things faster.

**Tim**: Even if the changes are small, and we have 12-15 of them in the fork right now, it will delay shipping Pectra. 

**Paritosh**: The question is whether the tradeoff is worth it.

**Max**: What Ansgar is saying is that the changes are 4 lines. Many of tests are overlapping with what is already taking place because of other rollup EIP.

**Tim**: What are the risks of not making decision today?

**Max**: The code itself is a 4-line change, but the tests will need to be rewritten and adjusted.

**Stokes**: Given that rollups are the user, it would be nice to hear from them directly. 

**Tim**: Ansgar says there is rollcall next week (but we already have signal that they really want this). We can bring this up in the call next week to get feedback and give ourselves time to have a better sense on testing.

If we finalize today, my sense is that we don't do this.

**Barnabus**: If we delay one more week, we will not finalize this year.

**Daniel**: Does this mean the proposal is not included and we would maybe have a devnet-6 for this one EIP?

**Paritosh**: Devnet numbers are made up, we can add more if we need to.

**Ansgar**: That seems like the worst option in this case. If we delay to next week, it might not make it to devnet-5 and then we might not want to open a new devnet for it. We are rolling the dice on whether or not to include it. 

**Tim**: We are strained with capacity. We need to evaluate what the impact is before making the decision.

**Ansgar**: But by delaying it, we change the cost. By next week it might be much larger because it would require a new devnet.

**Tim**: But I don't think we know today whether this would require a new devnet. 

**Ansgar**: It's fine if the decision is not to include, but we should make the decision today, not delay it to next week.

[ *disagreement in the chat about whether or not there's consensus around this decision; deferred to next week* ]


-------------------------------------
### 201.5 | [EIP-4444 & EIP-7639 rollout](https://hackmd.io/Dobc38YVQ1qmbbyI6LcFqA) |

**Tim**: Next up, history expiry. Piper you shared a document, do you want to give some context on this?

**Piper**: We made a decision at the R&D workshop and we have all the execution client teams on board for rolling out what we'll continue to call four 4s with a timeline of dropping a significant part of the history by May 1, 2025.

Document linked above gives summary of everything going on here. Official EIP number is [7639](https://eips.ethereum.org/EIPS/eip-7639). It specifies a new version of the Eth protocol (Protocol Version 71) for which clients will be allowed to stop responding to certain messages about history. The exact thing we agreed on was dropping block bodies and receipts only for pre-merge data, so that does not include the header chain or any data after merge. Loose estimates suggests this accounts for a couple hundred gigabytes of disc space, this gains us some amount of leeway here on that 4 terabyte hardrive limit.

The agreement in terms of what consensus was reached was strictly about clients no longer being required to respond to this data over devp2p after that drop date. The exact implementations that clients will be taking with respect to how they handle this data is up for grabs. Every client is able to make their own decisions. We still have clients implementing full syncs, executing all blocks from genesis, they'll be implementing their own plans for how they fetch, retrieve, deal with all that long history data. We have other clients who are going to be implementing Portal Network clients for the Portal Network history network in their clients for surfing things like json rpc.

That's the high-level overview for this. We met with all the client teams during Devcon, I think everyone knows what they're doing. The time to start working on this is now so that we're ready. Lightclient has pointed out that for this new protocol version we need to warm it up, not have it just turn on May 1st, but client teams should have versions of their clients out before then that allow for both old and new versions to exist at the same time.

**Andrew**: One comment is that we need to finalize Eth/69 and our side we have some concerns about its compatibility with Polygon. We need some time to prepare and maybe can discuss on next all core devs call.  

My other question is do we actually need a new protocol (Eth/71) to explicitly prohibit answering a historical block request. 

**Piper**: I was going to ask that same question. I don't have a strong opinion about this. Hopefully we could answer that today or async if other client teams want to weigh in.

**Ahmad**: Given that 3-4 other clients are going to implement 7801, 7801 is going to be Etha subprotocol and everyone can then see premerge history on eth protocol. The reason we want it to be a subprotocol so that eth protocol will not be affected by clients potentially calling clients that do not support 7801. Don't want to give the assumption that all clients are going to support serving historical blocks through 7801.

**Piper**: Correct, so that sounds like that's a little in favor of not implementing a new Eth subprotocol version. It seems like that could happen independent of whether we have a new eth subprotocol.

**Ahmad**: No, because when you implement a new eth subprotocol you declare that you support the new subprotocol. If you don't declare it, then no one will ask you for it.

**Piper**: I'm referring specifically to the new ETh protocol version (Eth/71), not whatever new protocol version 7801 goes on.

**Adhmad**: Since some clients are going to drop blocks and most nodes are going to drop pre-merge blocks, it wouldn't be fair to anyone to keep saying 'hey I might have the blocks or might not', so we say anyone who is in Eth/70 or 71 will stop serving pre-merge blocks. And if you want to serve pre-merge blocks, you implement the subprotocol.

**Piper**: Got it, so in your version, anybody who is on Eth/70 may or may not serve the block history and anyone on Eth/71 definitely doesn't serve the block history?

**Lightclient**: This is just for Eth/71--you *must* not serve pre-merge data on Eth/71 but we can make it clear that you could for earlier versions.

**Piper**: The endgame here is that we get a sharded Eth pro tocol between the clients that do and don't serve historical blocks; seems like a problems state for things to be in, where there's an option to stay on the old protocol and continuing to serve old blocks.

**Andrew**: Yeah, I don't like this bifurcation in protocols. Maybe we can make Eth/70 generic enough to allow for clients who don't want to store any historical blocks to explicitly say so.

**Ahmad**: If you don't put any 1s in your bitmask that means you don't have any history that you don't want to serve; it's easy to implement. If we want to encode the bitmask inside the ENR then that's different. I think I am fine with the handshake.

I think Geth team is still in favor of having it as a separate protocol regardless of whether we do it in this way, just because they want to keep the network uniform. 

We could change the language to say instead of 'cease serving history' we leave it to the client teams and not have a separate subprotocol (etha) for serving history. 

Lightclient: What is the argument against etha? Isn't it just a string within the handshake. I personally don't care etha versus another version, it's just a string.

Andrew: From my point of view, etha is fine, what I don't like is Eth/70 for this sharded block proposal and then Eth/71 for actually stimulating must not serve historical blocks because then we have a bifurcation in protocol.

**Ahmad**: Okay sorry maybe there's a confusion, which is why I asked lightclient to change his version to Eth/70. We are going to not use the 70 version since it's a new subprotocol, it does not conform to the same versioning scheme. 

**Piper**: To round this back up: 7801 goes on a different subprotocol, not part of the Eth protocol. Anyone who is doing 7801 things, it is on a new separate protocol and separate string. The question here is whether there is opposition to doing 4444 without bumping the Eth protocol version and keeping it at 70 with the dropoff date. 

**Lightclient**: We need to bump the version. We don't want to stop serving history on a specific version because then when you connect you won't know if they have the history or not. If you haven't updated your clients and are trying to bootstrap, you're going to try to download but if everyone else updated you won't be able to connect to the network.

**Piper**: Isn't that the same case though? Isn't the same case true whether we bump the protocol version or not? If you don't update and you connect to the network but everyone else is on the new protocol version and dropped the history, they're no longer serving the data.

I think we need to do a bit of async discussion on the exact roll out plan for this. It doesn't seem like we have clear consensus here today. I will try to get a write up posted of the two different approaches and see if people want to weigh in on.

**Tim**: What is the rationale for not having an explicit separation? What do you gain by not having an explicit tell that there's a different version people are running? 

**Piper**: 1. There isn't much of a difference in the actual protocol definition. The actual messages are all the same but the behavior of the request is different. 2. Added complexity and cross-network compatibility.

**Andrew**: 1. Protocol Eth/69 which we discussed but isn't finalized yet. It has some proposed merge clean ups and we realized it might not play nicely with polygon, so we need to think about it more and discuss again. Basically, Eth/69 is not relevant to 4444s; sequentially it's something that we should finalize if we're talking about Eth/70.

I also think that we need one single protocol that works for all nodes whether they're storing historical blocks or not. When you need to download historical blocks, it should be explicit with your peers, which blocks your peers have. 

If we do something like 7801 concurrently with a new version of the protocol that actually prohibits historical blocks that creates a bifurcation in the network. My strong preference is to have a single protocol that works for clients that decide to store historical blocks and those who don't.

**Tim**: Piper, if you want to write something up and post it on the Discord, we can continue this conversation async.

**lightclient**: If we decide to have this additional provider protocol, it is important that we roll this out with Prague. How do we add that to the Prague hard fork meta?

**Tim**: In general, we should start adding non-consensus changes to meta hard forks. We have done some things like this in the past, but it does feel important to signal. We can discuss at the end of this call.


-------------------------------------
### 201.6 | [EIP-4803] (https://eips.ethereum.org/EIPS/eip-4803) |

**Tim**: Next up, Axic shared this on the agenda: EIP-4803. A while back we discussed adding bounds to constants in the protocol. We did add a couple, but this one was never confirmed. 

**Alex**: The one we merged back a couple of years ago was 2681 (limiting the account nonce) and there was another larger EIP (1985), which was proposing bounds to pretty  much everything. At the time, we agreed to the account nonce limit and to split this 1985 into smaller individual changes; this EIP is one of them.

This EIP is proposed to be enabled from genesis and it limits gas limits on transactions. No transactions can have a gas limit higher than 2^63-1. The reason is that it allows simplifications in the EVMs, which using 2^63 it can be handled as a signed number and checking whether the out of gas condition is reached is a matter of checking if the gas became negative.

This can be enabled from genesis because most of the clients, including Go Ethereum, already do this internally. Additionally, it is expensive to create transactions with a limit higher than this because you need the funds available up front. 

Are there any strong reasons against this or should we consider spending more time discussing?

**Tim**: Why use a different constant for this than 2681?

**Alex**: The reason we should go with 63 is because then it can be a signed number and the out of gas check is simpler.

**Tim**: There's a comment from Barnabus around testing and inclusion in the fork. Even if we retroactively add this from genesis, we need some tests for this first. It feels like a bad time to add those tests given everything with Pectra. That aside, assuming we got to this once Pectra is done, is there feedback on design or conceptually?

**lightclient**: It would be helpful to see if there were examples for using this negative gas value. I kind of understand that it's possible to use this to indicate when out of gas, but if you could link to an example where a client is doing this and what the implication would be.

**Alex**: evmone was doing this; but the way you could do it, you just subtract the gas and check whether it is a negative value. Internally, CPUs would usually have specific instructions for the negativeness check, so technically it can be cheaper. 

The limit, 63 or 64 is a discussion to be had. Setting that aside, can we atleast agree conceptually that putting this limit is something people agree with or have reasons not to?

**Tim**: It seems like there are no objections. For next steps, Alex if you are able to open a PR, we have a meta EIP to track these retroactively applied EIPs, so open a PR to that EIP and list this one.
We don't have to merge the PR now, but can revisit post-Pectra testing.

**Alex**: Sounds good. Re: 7825 (comment from Ben)
7825 proposes to introduce a lower limit, a limit of 30 million. My comment was that the PR I'm proposing can be enabled retroactively whereas 7825 may not be able to be enabled retroactively. The two are related and essentially you could have both at the same time. One is an implementation whereas the other is a limit that we may or may not change over time.


-------------------------------------
### 201.7 | [Potential ACD Improvements](https://ethereum-magicians.org/t/allcoredevs-network-upgrade-ethmagicians-process-improvements/20157/51) | [Declined for Inclusion](https://github.com/ethereum/EIPs/pull/9056) update, Non-consensus changes in Meta EIPs, PFI → CFI → SFI & devnet inclusion

**Tim**: As we discussed in Bangkok, three ideas came out of the ACD Process Improvements Sessions: 

1. adding 'declined for inclusion' status to meta EIPs for hard forks -  
The idea is that we decide to accept things into hard forks but we don't have formal rejections for current fork. It doesn't mean we will never do the EIP, obviously someone can work on any EIP and are free to propose everytime there is a new fork, but we do spend a lot of time discussing EIP inclusion for each fork so having this status would be valuable. 

2. adding non-consensus changes to meta EIPs - 
We have meta EIPs for hard forks and it's clear why we need them because there are a set of changes that need to happen at a specific block. One challenge with that is that it means our process often biases toward things that have to activate at a specific block, e.g. spent years talking about 4444s but it doesn't get prioritized because it's not on the same list as everything else. The proposal is that we start including non-consensus changes at hard forks and for something that is not a non-consensus change (like 4444s), the implication is that clients will have this client feature shipped *at the latest* at the hard fork.

**Stokes**: That makes sense. One thing to note is that we still have the ability to ship non-consensus changes without a hard fork, but this is addressing the false positives.

**Tim**: Correct. We can ship things before and in practice this would look like compiling a list of previously activated changes to the specs for a hard fork. At this block, all these are active on the core protocol.

**Pooja**: Just wanted to make sure this is for proposals going to be shipped *before* the hard forks, and not those proposals which are going to be retroactively added.

**Tim**: Yes, I would keep those separate. The retroactively added EIPs, everyblock from block zero should implement those protocol rules. And we can only add those when it's true that in the entire history those conditions were not broken. Whereas something like dropping history, this was not true of the entire chain history. So it feels more accurate to say, 'as of this hard fork this change is live' even though it's not a consensus change.

My point is that we would add *all* protocol changes, whether or not their core EIPs, since the hard fork. We can both retroactively do this and we can decide to prioritize  proactively.


-------------------------------------
### 201.8 | End of year coordination and holiday meeting schedule | 
Testing call on Dec 23
Cancel ACDE on Dec 26
Cancel testing call on Dec 30
Replace ACDC by testing call on Jan 2

-------------------------------------
### Attendees
* Tim
* Lightclient
* Ognyan Genev
* Ruben
* Tomasz Stanczak
* Daniel Lehrner
* Ben Adams
* Pooja Ranjan
* Anders K
* Guru 
* Julian Rachman
* Ben Edgington
* Ameziane Hamlat
* Jihoon
* Danno Ferrin
* Paritosh
* Enrico Del Fante
* Ansgar Dietrichs
* Barnabus
* Kevaundray 
* Stokes
* Kolby Moroz Liebl
* Toni Wahrstätter
* Hadrien Croubois 
* Dave
* Arik Galansky
* Dragan Rakita
* Spencer
* Frencesco
* Frangio
* Matthew Whitehead
* Piotr
* Terence
* Scorbajio
* Mario Vega
* Mingming Chan
* Gajinder Singh
* Andrei
* Yiannis
* Łukasz Rozmej
* Trent
* Ignacio
* Richard Meissner
* Danceratopz
* Milos
* Guillaume
* Oliver (Reth)
* Karim
* Saulius
* Radek
* Andrew Ashikhmin
* Jared Wasinger
* Max Resnik 
* Hsiao-Wei Wang
* Somnath
* Mikhail Kalinin
* Yoav
* Luis Pinto
* Elias Tazartes


