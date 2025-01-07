# Execution Layer Meeting #202
### Meeting Date/Time: Dec 19, 2024, 14:00-15:30 UTC
### Meeting Duration: 1hour 30 minutes
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1209)
### [Video of the meeting](https://youtu.be/XtdJ2G8yST4)
### Moderator: Tim, Alex
### Notes: Alen (Santhosh)

| Decision Item | Description                                                              | 
| ------------- | ------------------------------------------------------------------------ | 
| 202.1 | **Pectra Testnet and Devnets** EF Developer Operations Engineer Parithosh Jayanthi said Mekong is still up and running. Mekong is the public Pectra testnet based on Pectra Devnet 4 specifications that was launched last month in November. Client teams are making headway in their implementations for Pectra Devnet 5. Jayanthi said that Besu and Teku are the farthest along in terms of testing, with Lodestar not far behind. Once Pectra Devnet 5 specifications are finalized and more client implementations pass local testing, Jayanthi said developers can then launch Pectra Devnet 5. There is no specific date for the devnet launch yet, though developers are aiming for some time in late December or early January.
| 202.2 | **Pectra Devnet 5 Specifications** Developers discussed several updates to Pectra Devnet 5 specifications impacting the design of EIP 7742, EIP 7702, EIP 2537, and EIP 2935.
| 202.3 | **EIP 7742** EIP 7742, uncouple blob count between CL and EL, will be replaced by EIP 7840, blob counts configured at genesis. This was a decision made on the previous ACD call, ACDC #147, that was reaffirmed on this week’s call. EIP 7840 is a simpler way to implement a change to the blob capacity. EIP 7742 was removed from Pectra due to implementation complexity and concerns that the code change would delay the Pectra upgrade. Beiko affirmed later in the meeting that EIP 7840 should be included in Pectra Devnet 5 specifications.
| 202.4 | **EIP 7702** The latter ensures that the chain_id size is not unnecessarily limited to the “uint64” value type. Using a larger “uint256” type ensures more forward compatibility and interoperability with other chain configurations. Developers agreed to move forward with making the chain_id uint256 in Pectra Devnet 5.As for the former change, removing chain_id in authorization tuple, the author of the proposer Geth developer Felix Lange said that he would close this pull request for now and come back to the group once he has thought through other changes he would like to propose for EIP 7702.
| 202.5 | **EIP 2537** Nethermind developer Marek Moraczyński shared the final pricing model for EIP 2537, precompile for BLS12-381 curve operations.
| 202.6 | **EIP 2935** Geth developer “Lightclient” shared updates from an independent audit conducted on all system contracts required for Pectra. One of these contracts is for EIP 2935, serves historical block hashes from state. Lightclient said the audit suggests small changes to the EIP to bring it in line with the structure of other system contracts in Pectra. Developers agreed to also include these changes for testing in Pectra Devnet 5.
| 202.7 | **EIP 2935** Jayanthi asked if there were any updates to the builder API. Stokes said that updates were in progress and close to finalization. He added that that efforts to update the builder API for Pectra can happen in parallel to devnet progress and should not be a blocker to Devnet 5 launch.
| 202.8 | **EIP 4444** Developers are preparing for a partial rollout of EIP 4444, history expiry. As discussed on ACDE 201, client teams are preparing to prune and stop serving history data from before September 2022 when the Merge upgrade was activated. Client teams are preparing alternative pathways for their users to retrieve this pre-merge history data such as through the use of the Portal Network. Beiko said that developers should hammer out a testing strategy for clients as they work on supporting the new networking protocol version, eth/70, and dropping older versions. Lightclient recommended incorporating testing for EIP 4444 with Pectra testing. Developers debated how exactly to go about doing this. Beiko recommended discussing the matter asynchronously from the call on Discord. He said that if developers cannot reach consensus on Discord, they can schedule a breakout meeting after the holidays to finalize the path forward for testing EIP 4444.
| 202.9 | **Decoupling Gas Price from Payload Size** Nimbus developer “Arnetheduck” presented a few solutions to issues with the gas and gossip limits. As discussed on ACDC #147, the gas limit on the execution layer may create blocks larger than what the consensus layer can propagate. The maximum size of blocks is restricted by a gossip limit on the consensus layer that is subject to change only by client teams. However, the gas limit on the execution layer is subject to change by validator node operators. Arnetheduck shared a few solutions to ensure that only blocks valid according to both fork choice rules and network rules can be propagated. One of these solutions recommended deriving the gossip limit from the gas limit. Lightclient resurfaced an EIP to set a maximum gas limit that validators cannot change. Developers debated the merits of different approaches to addressing the gas and gossip limit interdependencies.
| 202.10 | **Reverting Removal of NewBlock(Hashes) in eth/69** Beiko said that he had to leave the meeting early and handed over moderation for the rest of the call to Stokes. The next topic of discussion was about a change to eth/69. Erigon developer Andrew Ashikhmin recommended keeping fields related to new block hashes that were deprecated in Ethereum clients after the Merge upgrade in eth/69. Ashikhmin said removing these fields is unnecessary since the fields are not used and keeping them would support compatibility of eth/69 with other blockchains that have not activated the Merge upgrade such as the Polygon blockchain. Lange said that he is not opposed to keeping the fields. Later in the call, Besu developer Justin Florentine wrote in the Zoom chat that he is opposed to keeping the fields “forever” and would follow up on this discussion asynchronously.
| 202.11 | **EIP 7503** A Github user by the screen name “0xwormhole” requested feedback on his additions to EIP 7503, zero knowledge wormholes. Stokes asked developers on the call to take a look.
| 202.12 | **EIP 7808** EF Researcher Carl Beekhuizen proposed reserving a range of transaction types from 0x40 to 0x7f for use by rollup teams. The motivation for this is like the motivation for reserving a range of precompile addresses for rollups. For rollups to use new transaction types, it is necessary to ensure that there are no conflicts between transaction types used on rollups and Ethereum Layer 1. There was no opposition to Beekhuizen’s proposal.
| 202.13 | **EIP 4803** The next meeting agenda item was about EIP 4803, limit transaction gas to a maximum of 2^63-1. Lange said that the EIP has already been retroactively applied in all clients and the executable specifications should be updated to reflect this change. It was unclear what action item if any was needed from developers about this agenda item. Lange recommended that any developers wishing to change the behavior of EIP 4803 or further restrict transaction gas should create a new EIP instead of commenting on or trying to make a change to EIP 4803.
| 202.14 | **Announcements** The changes to the EIP approval process discussed on ACDC #147 have been finalized. EIPs labeled as “Considered for Inclusion” or CFI will be considered EIPs that developers plan on including in a devnet, any future devnet, for an upgrade. EIPs labeled as “Scheduled for Inclusion” or SFI will be considered EIPs that developers plan on including in the next immediate devnet for an upgrade.
| 202.15 | **Announcements** EF Researchers Davide Crapis and Ansgar Dietrichs proposed the creation of an “EVM Resource Pricing Working Group” to coordinate efforts across different Ethereum research groups on benchmarking and repricing EVM opcodes. Developers on the call were largely in favor of this proposal.
| 202.16 | **Announcements** The first redefines the categorization of meta EIPs, EIPs that detail information about Ethereum’s governance process. It has also been used for EIPs that offer a comprehensive list of all code changes included in a network-wide upgrade. The first item recommends restricting the “meta” EIP category to only process-related EIPs and excluding EIPs summarizing hard forks.
| 202.17 | **Announcements** The second item recommends removing the list of retroactively applied EIPs from EIP 7675 and instead listing these EIPs in their own section in a hard fork summary EIP. Stokes asked developers to review both changes and offer feedback if any on them.

# Intro
**Tim**
* Thank you. Welcome, everyone to ACDE number 202. We have a pretty packed agenda today, as you've hopefully all seen. and also a quick heads up. I'll have to jump out at the hour, and Alex will take over for the last 30 minutes. assuming we go for more than 60 minutes, with the current agenda, which I believe we likely will. so, we'll talk about how things are going with tech implementations.
* Ideally, get to a spot where we finalize the spec. I've tried to list all of the outstanding issues, at least the ones I could find. if we get through that, I think that'll be good. And then a bunch of other things to cover. So stick around 4444s, gas pricing and, transaction or payload sizes, a bunch of other EIPs and then a few announcements at the end. I guess to kick us off, do we have Parithosh or Barnabus to give a quick update on Devnets. Yes. 

**Parithosh**
* Yeah. So we have Mekong still live and what people are actually using to test on. that's still based on Pectra nets for specs. And client teams are slowly making headway into implementing. Devnet specs. There's been a consensus specs release already. And on the interop channel. On the Eth R&D chat, I have linked a kurtosis config for Besu as well as Teku. they're able to, produce blocks for Pectra with the net five specs, including over six blobs as the max.
* So in case anyone else is ready and it seems like Loadstar might actually be, we can start expanding that, expanding that file and testing more and more interop. I think that's the current status. Once we have all the open PRs merged, I think the testing team will, update tests as well as make a test EL release, and then we should have everything locked in for that. 

**Tim**
* Thank you. yeah. Nice to see there's at least the first client pair on the network. Any other client team or anyone have other thoughts? Comments about Mekong or Devnet 5. 

**Felix**
* Yeah. Big quick question. Which branch are you going to be using for get? 

**Parithosh**
* For now we're using lightclient branch. But if you tell me which branch to use, I can change that. It's true. We do not. 

**Felix**
* So we have every I think we have basically everything for Devnet five on the master branch, except for the 7702 transaction pool. So basically you cannot submit 7702 transactions through Geth right now on the master branch. It would still be interesting to run it though. Like if you guys could like run it like just, you know, like or maybe I can just try myself, but basically if you want to, I have no idea. Also like how up to date Geth branches, but I guess, yeah, we can figure it out. Yeah, no. 

**Parithosh**
* Worries, I can try it out and let you know what happens. 

# EIP-7742 replacement [6:23](https://youtu.be/XtdJ2G8yST4?t=380)
**Tim**
Okay. Anything else on testnet? Okay, then, let's move into the spec, discussions. 
so first one I have, is, this replacement for 7742, we agreed to remove 7742 on last week's call. and then on the discord discussed instead, passing some configurations in Genesis, like client has an EIP for it, which, it seems like most teams were in support of. but because it was introduced last week, we wanted to wait and see if there were any objections. I guess. Yeah. Anyone have concerns about the EIP or. yeah. An objection to moving forward with it as the way to pass the blob configurations. 
Okay. If not, then I guess we should get this merge and add this to the specification. and this will be the way that we include, or that we pass the blobs, to the El. Any other questions? Comments? And I guess maybe one thing there is, do we want to have this? I guess we we put this towards Devnet six and not Devnet five. Correct. Given that we already have some clients launch for Devnet five. Okay, I'll take the silence as a yes. great. So okay, I'll add, I'll add the EIP to the texture spec, after the call, if possible. It'd be nice to get this actually merged. as I don't seem, it doesn't seem like there's any issues with the PR as it stands. And yeah, we can get this added to that. Devnet 5. 


# EIP-7702 auth.chain_id [8:02](https://youtu.be/XtdJ2G8yST4?t=482)
**Tim**
* Okay. Next up, 7702. So there was a proposal by, proto to make, the chain ID,  u-256. this came up on Eth magicians. I can't open the PR. 
* And then there was a separate proposal, by Felix to just remove the chain ID idea altogether. I don't know if anyone has an update or context on this and, strong preferences. it seems like Geth had some objection, to this. 

**Justin**
* Besu leaning towards proto suggestions, but it sounds like he may have had a change of heart looking at the chat. Yeah. Go ahead proto. 

**Protolambda**
* Yes, I think the solution by Felix is more elegant, where I was mostly looking to preserve some functionality, with the entity size, but Felix has a suggestion to remove it altogether. And so then you rely on the chain ID in the outer transaction, and that generally has the right size. So then there's no problem. 

**Felix**
* Yeah. So I mean, maybe some context about my proposal. So I mean, it seems there was also maybe a bit of a misunderstanding about it. So, yeah, it's, I just literally raised this proposal because I thought it's a bit silly to, you know, have such large changes repeated, over the course of, like, many authorizations when they're literally all going to be the same value or zero. So that's basically where my proposal comes from. But I don't think I mean, ultimately we do need these, large we do need support for like large chain IDs anyways. So that's the thing. There isn't really any way around that. Anyone here from breath to actually. Yeah I think. 

**Tim**
* Roman. 

**Roman**
* Yes. so the the pushback regarding the U-236 ID, like it felt like the increase is unnecessary with the motivation that was provided. And I do have a and you can read the comment to get more context. I do have a pushback regarding, the excluding the change from authorization. The pushback being that we're introducing a new primitive, that is akin to the transaction, but we're making it context dependent. So, for example, if I have some kind of authorization router and I have bundler for different things like, and I want to see for which changed the authorization was signed. And in my view, it doesn't make sense to exclude it from the object itself. Yeah. 

**Felix**
* Yeah. So either way, it's I'm really sorry for, like, maybe raising my proposal because I was kind of hoping that we would just, you know, be able to finalize this back. But it seems this is more complex than I thought. So I. 

**Tim**
* Guess the. Yeah. So Proto's original proposal is a relatively simple change, as I understand it just changes the like. Yeah, the way we cast this value does. If there are concerns with your approach, Felix, like, does anyone have concerns with Proto's suggestion? 

**Felix**
* I mean, the thing is, we can literally just change it now for whatever. Like, I guess for Devnet five is already too late because we're literally just launching it, so we're not going to have it there. So for sure there will be another dev net before we go. Like, what the ? I guess, like, so let's just aim for the next devnet to figure out the whole signature situation, and I do have some other stuff in the pipeline for the signature as well that we're just discussing as we speak. So I do think that, you know, there may be another change coming to the 7702 signature stuff anyways. So that's the thing.
* Like, it really all depends on like where we settle in the end, but it's very uncontroversial now to just accept that we will enlarge the chain ID to you. U256 is very easy change to make. So we can just agree to that today. And then the issue will be gone. But I will be back with more changes to the 7702 anyway. So yeah. 

**Tim**
* I would, I would prefer to get us as close to final as possible. And so if there's no objections for the U256 change, I would move forward with that one. And then yeah, if there are other things you want to discuss after we like, we can but yeah. Anyone oppose then to, moving forward with the basically this would be  Lightclients PR let me put it in the chat here, but to basically make this value U-256 and then we'll just close Felix's PR. 

**Felix**
* Yeah, we can do that for now. But as I said, I will be back. So anyways, we we may revisit this for the next one. Okay. 

**Tim**
* Yeah. Perry, the PR just linked 9143 is the U-256 PR and that's what we'd go for. And then, 9152 is Felix's PR, which we will close. 

**Lightclient**
* Did we agree to do that for devnet five? That was my understanding. But I just want to make sure everybody else was in agreement there. 

**Tim**
* So I guess Besu this base you already have this in because they're live on devnet 5. I guess in practice we will not hit this limit unless we explicitly try to like spam it. 

**Parithosh**
* Just to maybe clarify a bit, there is no devnet 5 yet which is doing local tests, so it's just a kurtosis. 

**Tim**
* So yeah. So then because this is such a small change, I would include this in Devnet five. Definitely not run another net just for this. Yeah. Any objections to including U-256 and net five. Okay cool. So let's move forward with that one. So again that's uh PR 9143 that will add to the Devnet 5 spec. Anything else on 7702. Okay. 

# BLS Pre-compile spec [15:58](https://youtu.be/XtdJ2G8yST4?t=958)
**Tim**
* Next up, we had a lot of movement on the BLS Pre-compile spec. Merrick, you've opened a lot of these PRS and have been kind of leading the discussion. do you want to give some context on your different PRS and where we're at with regards to BLS pricing? 

**Marek**
* Yes, of course. so we benchmarked BLS Precompiles and split it into three Prs to discuss them separately. Overall, the operations will be less expensive, and we benchmark it with a group of people from different teams and checked for EVMs. So EVM one Nethermind Basil and Jeff. And yeah, I guess we come up with the final best pricing. So please check those gas pricing. And the currently it is being merged, so we should include it in next Devnet. yeah. And that's mostly it about gas pricing. And there is one more PR from Pavel about BLS remove redundant multiplication precompiles. And the thing is that right now we have two operations with the same pricing that do the same thing.
* So multiplication and multi scalar multiplication for K = 1. And Pavel suggested that because of this the multiplication is not needed and can be removed. And generally six people express support for this. Personally I'm also weakly in favor of this change. it makes sense. And even if for some currently unknown reason we want to add multiplication in the future, it will be easier to add it later than to remove it, in the future when it was already added in EVM. Yeah. So that's mostly it. And, we can discuss this, multiplication, what people think about it. 

**Tim**
* Thank you. And before we do the, mold removal, does anyone have concerns with the gas prices that have been merged? Otherwise, we'll assume those are final, and we should include them in devnet five as well. But last call, if someone has objections or concerns. I know we've been discussing this for a few weeks now. Okay. Amazing. yeah. Again, thank you. Marek, for the PRs and everyone who's participated in the benchmarking conversations. removing them all. Precompiles anyone in opposition for this. If not, and I guess testing and like implementation wise, I assume it's fairly simple to remove these precompiles. But is there, I don't know, some like, complexity that yeah, people are concerned with. 

**Mario**
* I mean, the only thing is that we were ready to release before this. So I think it's going to be yet another delay for test release. It's fine. I mean, if it if it's has to go in, it has to go in. It's not a problem. 

**Tim**
* Thank you. Gary, I saw you come off mute quickly. 

**Gary**
* Oh, I was just going to say that, we would need to, shuffle the precompile, addresses and then, yeah. To Mario's point at least. What's blocking Besu is, is the not only the gas cost now, but also to the removal of mole from the reference tests. Yeah. 

**Tim**
* And so. Oh yeah. Because the PR, does the PR actually change? Oh, yes. Okay. So it changes like. Yeah. What's that 0XOF basically. And removes a couple. So yeah. So we need to make sure that we have the right precompiles at the right addresses. then. 

**Ben**
* And also add tests just to make sure that the precompiles aren't there after it as well. 

**Tim**
* Yes. We've had many devnet and mainnet issues due to adding and removing DLS precompiles, so definitely we want to test both that the ones we expect to be there, are there and working, and that the ones we previously removed are not there. yeah. But in general, I guess this is the right time if we are going to do such a change. yeah. Just to make sure that, we have Devnet 5 running with the final set of Precompiles with the final set of gas prices. So even though it's a non-trivial spec change, it does still want, like, one that's worth, yeah, including in the next devnet and even having a small delay in terms of, like, getting the test out if, yeah, if that's the version we're going to ship. 

**Roman**
* I think we have historically tried not to overload. Precompiles like this. I think the obvious caveat with this being just the number of precompiles in 2537. So if people like this change, let's go ahead and move forward with it. Okay? 

**Tim**
* Yeah. Last call. Yeah. Last call for objections. Otherwise, I think we can merge this one and track the PR for five as well. Okay. Sweet. Let's do it then. Again, thanks to everyone who helped. yeah. Finalize the spec in the past couple of weeks. I know there was a lot to do there. next up, IP 2935. There was an update to the system contract. like clients. Do you want to give some context on this? 

**Lightclient**
* Blue. so we had a handful of audits on these different system contracts, and not much was found. But for 2935 we had a few small changes, mostly just to bring them in line with the other system contracts that we had. So I think the main two changes was changing the buffer length from 8192 to 8191. This isn't as necessary for 2935, because the block number is always monotonically increasing by one. And instead of the timestamp, which is generally increasing by 12, but might possibly change at a different amount, sometimes it's skipped. So we just made this change more to be uniform across the board. The other big change was instead of returning zero like the block hash instruction currently returns, we revert when the argument.
* The argument for what block number you're requesting is out of balance with what's available. This is also, again, just to be more consistent with the other system contracts that we have and just improves the correctness a little bit so that it's clear that the response for this contract is, yeah, an error instead of responding with zero. So that's pretty much it. And that's just updated the address with the new code. 

**Tim**
* Thank you. Virginia. 

**Gajinder**
* Yeah. As one of the 2935, contract authors, I think 8192 to 8191 is okay. I mean, even though it's not really required, as you have already mentioned. but I didn't really get the reasoning for changing, if it's out of bounds, then, changing it to revert instead of returning zero. 

**Lightclient**
* I mean, there's kind of three responses when you return zero. There is return zero, revert or respond with the block hash, and this reduces the number of possible responses to handle to two. 

**Gajinder**
* So we are basically diverting away from the block hash behavior. 

**Lightclient**
* Which is fine because this is a system contract. And if we end up plugging this into the block hash, we can have an adapter that sort of handles this behavior and provides like the legacy behavior correctly. 

**Gajinder**
* So okay, so what you're suggesting is that if we come to that point where, for example, in seven. 709 we use system contract for resolving block hash. We basically can handle it on that level to return zero if we want at that point. 

**Lightclient**
* Yeah. I think it's pretty easy to do that. 

**Gajinder**
* Yeah. Okay. Makes sense. 

**Tim**
* And I saw also on this PR, there was a comment by Guillaume asking about the actual audits. So we got four done. I believe in the last one finished up, I think last week. and so yeah, we were hoping to maybe present the results today, but then putting everything together is taking a bit more time. So hopefully early January we can present. yeah. Present the different audits and yeah, share all the findings. But, yeah, for now, I think those were the most major changes that came out of it. Anything else on two, nine, three five? I guess one question is like, yeah, do we want to merge this PR in and have this also for Devnet five? yeah. Given it's still yeah, there's still some comments and, discussion or Yeah, it's better to wait a bit more on this one. 

**Gajinder**
* I think. Me like Client and Guillaume. We can just discuss and close this out. Maybe today or by tomorrow we can have it in five. 

**Tim**
* Okay. Okay, then. Yeah, let's do that. Let's try to get it merged by the end of the week, and then also include it for five. Anything else on 29? 35. Okay. If not, that was the last texture spec, update on the agenda. Anything else with regards to the texture specs that people wanted to discuss? Otherwise, then. Yeah, I think we're starting to look good. Perry has a question around the builder API. I don't know if anyone has updates on this. 

**Stokes**
* Yeah, I think I can speak to this. I think the main thing was just the SSZ standardisation as a transport. there's a PR and yeah, I think it's pretty close to merging. but that being said, it can kind of happen in parallel with all of this. I don't think we need to lock on a particular devnet

**Tim**
* Okay. Anything else about the Pectra spec? Okay. Nice. Well, yeah. Well done everyone. Hopefully this is, the beginning of the end of polishing the specs. yeah. Last call on Pectra before we move on. If not, Piper posted an update on EIP 4444. Piper, do you want to give some context on this? 

# EIP-4444 Rollout Plan [28:02](https://youtu.be/XtdJ2G8yST4?t=1700)

**Piper Merriam**
* Cool. just to quickly recap, we've got agreements on all clients for activating a partial for fours, which is a which is a drop of pre-merge data of just block bodies and receipts, from all execution clients. The timeline for that is May 1st, 2025. and we've got resolution on the things that weren't that were still a little bit fuzzy last time. we are going, clients will be bumping the ETH protocol version. the new protocol version can go live anytime between now and then. And the idea is that the date in which clients can stop supporting the old client protocol version is May 1st, 2025. this also kind of removes the concept of an activation date. This isn't that. May 1st is the activation date for the new protocol version.
* May 1st becomes kind of the date in which clients can stop supporting the other one. So this eliminates kind of the need for like a coordinated activation date. anybody who's planning on doing a 7801 based solution is going to do that in a completely separate and completely isolated sub protocol. and then the handful of and then the clients who are implementing portal for things like RPC or other things are kind of orthogonal to this because that is just sort of like external facing client behavior and isn't really related to the P2P related changes.
* So I think we have resolution on everything. anybody have any comments on that or anything that they want to throw in? Cool. The main thing here is that clients need to get going on getting their support for this, implemented and live on the network before that May 1st date so that we can have clients active on the network testing the new protocol version, kind of moving over onto it so that we don't have a big shift right at the at the May 1st timeline. That's all that I have. 

**Tim**
* Thank you. Roman. 

**Roman**
* Do you have any coordinated testing process rather than doing it on mainnet? Something like Devnet equivalent for the for the networking protocol change? 

**Piper Merriam**
* I don't have anything specific to share on that at the at this time. I will get with teams and see what kind of testing people want to make sure that they're doing. 

**Tim**
* I assume we should at least run this on the test nets before, um. And I'm pretty sure like we had sepolia at the merge, I think Hoskey launched post merge, if I recall correctly. yeah. 

**Piper Merriam**
* I don't have a strong opinion on this. The protocol version bump is a, it doesn't actually change anything in any of the message payloads. So we're not actually talking about any kind of change in sort in terms of, payloads going between clients. That doesn't suggest that we still shouldn't test this. but it is technically a very minor change. 

**Tim**
* Yeah. Okay. So we. Yeah, we can definitely discuss, Yeah, we should discuss, like, a rollout strategy. we can do this, async. actually, I guess, like, client says we should just make this part of spectra and run the devnet test nets. I don't know when the first test nets will fork, but obviously we're hoping it's before May 1st. would client teams feel comfortable? yeah. Combining this, or is it going to delay people's actual releases? 

**Lightclient**
* What I mean specifically is not immediately dropping history because we do want to get packed out before then, but to do the version bump where clients don't serve the history over the wire version 70, and they continue serving the history over the previous versions. So all the clients still have the history. They don't have to implement the actual history dropping in their database. it's just more like, how is the behavior of the client observed on the network? And I think that this is pretty easy to implement. But what it gives us is then at the point on like May 1st, whenever clients start actually dropping the data. They have a very good base of the network that they can start connecting to. Who will serve the protocol they expect. 

**Felix**
* So in that case, we might also think about adding like a flag in the air about this. It's definitely something we can consider because I mean, you don't really want to connect to all the peers just to figure out that, like there the other kind that you don't need. Like if you still need to download the history after the cut off date, which you shouldn't, then. Yeah, I mean, you can try to find peers, but it's just going to take you potentially a long time to iterate through all of them just to figure out that they have this new protocol version and you don't support. So this is kind of, for me, the counterargument to dropping the like to adding new protocol version. It's kind of useless for the clients which actually still rely on it.
* So yeah. I mean, I thought the consensus was like at the time when we made the decision.
* The consensus was that since we will, like any client, will be allowed to drop history, it's not safe to rely on history being available via ETH anymore after this cut off date. So that's the thing. You just have to have an alternative mechanism by that time. 

**Tim**
* Arnetheduck

**Arnetheduck**
* Yeah. I don't think we should burden this could be fine with this because it's really just a transition thing, like, you know, a year from now or two years from now or whenever, this will practically be all clients because they will have had to find a different way. Yeah. 

**Felix**
* That's okay. I mean, we can we can remove the flag. I mean, that's the thing about in art, like flags are free. They're I mean, it doesn't really cost as much. It's going to cost us like three bites, just adding like or maybe four. I don't know, just adding a simple flag like, I don't know h one or something. I don't know. No. 

**Arnetheduck**
* I mean I just think it's fine. Like we do this on the consensus side without a flag, and it kind of just works, you know? Nobody really bothers with this distinction. 

**Piper Merriam**
* So I think that the the thing here is that the clients that need the history still and are still trying to get it from the old protocol version, are the clients that didn't update, which are the clients who won't know about this flag? I think that that, this is solving a problem that we don't have. All of the clients are in agreement that they're going to to, to modify their clients so that they don't need to be able to download history over this. And if they do, then they need to find an alternate mechanism. So I'm not sure that there's a, if there's like somebody here who really needs that, maybe they can speak up. But I don't see that we should implement something for a problem that we potentially don't have. 

**Felix**
* Okay. But this is a good point with the with the non-updated clients that like they need to basically. I mean, at some point you will have to update anyway. But yeah, that's the kind of thing we can't just like force everyone to update right away. 

**Arnetheduck**
* And I think that's the same. 

**Piper Merriam**
* I think that's the argument for why this should potentially be included with Petra, because, my understanding is that there are some reasonable subset of clients in the network that only upgrade at fork boundaries. 

**Felix**
* But what should be included? Dropping history or. 

**Piper Merriam**
* Support for the new protocol version? It doesn't even have to include the full history drop, but just support for the new protocol version so that those that do choose to upgrade and implement the drop can get support for it. 

**Felix**
* But the thing is that it's kind of funny because it's kind of backwards. I mean, so when you, when, when you upgrade to a client that, like, drops the history before, then it's like you don't need the new version because you could just get the new history still from the old protocol, but it's like it's only for the clients which want to download. So these are the non-upgraded ones, you know what I mean? Like, I don't really get it. 

**Arnetheduck**
* Why I feel. Yeah. Likewise. I feel the new protocol version is equally useless to a discovery flag. 

**Felix**
* Yeah, you don't really need this new version, because when if you if your client tries to download history from the old version, then it doesn't speak the new protocol. So if we implement Eth 70 that, you know doesn't serve history before the merge, then the old clients can't use it. So they I don't. Yeah. 

**Piper Merriam**
* Correct. But the idea is that before the drop date, the clients will still be willing to serve the old protocol version as well. And after the drop date, some of the clients or all of them or none of them or whatever, can choose to stop serving the old protocol version. So the point is to get the new protocol version out. 

**Ahmed**
* If they opt to stop stopping to support, they just opt to stopping 69 and 68 and only support 70. If they don't want to stop supporting, then they just keep supporting 69. Sorry. 

**Roman**
* So everyone has strong opinions about this. Can we listen to Tim's message and either figure it out, they think, or on a breakout next year? 

**Tim**
* Yeah, it doesn't seem like we're going to resolve this in the next two minutes. And we do have a bunch of other things on the agenda. So yeah, I think we can try to move this to the history expiry channel. and then yeah, if two weeks async is not sufficient, then, let's find a time in January to schedule a breakout and dive into this more. anything else on history expiry aside from this issue that we haven't covered yet. Okay. next up then, there was a proposal on the consensus specs, with regards to, max payload sizes that could affect the execution layer. if we decide to limit the encoded transaction size, leave. yeah. Under that, you have the issue up. Do you want to give some context on this and how it affects the execution layer? 

# Decoupling gas price from payload size consensus-specs#4064 [39:24](https://youtu.be/XtdJ2G8yST4?t=2364)

**Arnetheduck**
* I can quickly speak to it. I mean, I don't know. 

**Tim**
* Oh, I think we just lost you. we lost your audio. 

**Arnetheduck**
* You're back. And. Oh! Can you hear me? 

**Tim**
* Yeah, now we can. But you were gone for, like, the past 30s. 

**Arnetheduck**
* Oh, bummer. So, on the consensus layer, we have a limit for how much data we can send in a single frame. This limit is because we can't really validate our data synchronously. We can only validate some of the data synchronously. So we have like a maximum amount of data that we can send in one frame. And that limit is set at ten megabytes. And for blocks in particular that limit can get exceeded if the gas price goes up because the blocks can become very large. we're not there yet. We've like this. This limit was set in Bellatrix, and it was set assuming kind of a gas price of, gas limit of 30 million, I think, with a bit of, spare room.
* And if we want to increase the gas limit, well, then we need to increase this or do something about this limit. And the limit is the spam protection mechanism, basically. So in Petra, there is a gas schedule change that makes it more difficult to create these massive blocks. But, doing it this way kind of just kicks the can down the road. so there's an issue open in the consensus pack report that discusses a few ways in which we could fix this more permanently. the ones that are the most interesting right now are, to either let the consensus layer and the execution layer agree on the maximum size of the transaction list in the execution, payload. this basically means that block builders and mempools and so on have to Consider the size in bytes of the transaction when before they added to to the block. So this is effectively this is almost like multi-dimensional pricing, except you know, the currency is bytes. 
* The other solution that has been proposed is to kind of compute this limit from the current gas limit. that has a few downsides. It's very difficult to implement in the consensus layer. gossip in the consensus layer was never really meant to transmit, single chunks of data this large. It's part of the reason why we don't why we package blocks and blobs into separate messages. so the other alternative here is that we kind of agree on the limit. And then or we derived the limit from the gas limit, and then consensus clients will have to deal with it anyway. That opens up some technical complexity.
* So I would encourage everybody that's working on the execution client to think a little bit about this, like what it would mean for the mempool if the size, the total size of the transactions that are included in the block is given kind of like an upper bound in this upper bound would be, you know, hefty, but not too, too hefty, so that we actually have a fair chance of transmitting these blocks within what currently is the four second time limit. Now, when we reason about this on the consensus side, one of the things we think about is that, we have an amplification factor when blocks go out and then they have to pass through a number of hops before they get to the final destination. So you can basically say that like, you know, a ten megabyte block on the ten megabit line takes X amount of time to transmit in full before it can move to the next hop, and we need to squeeze all that in and some validation within for a second. So the practical kind of limits that we're talking about, like we probably should stay within. 
* You know, I think the theoretical maximum we thought about at the time was around 2.5 megs not sustained. And that would be one kind of limit that would happen. And just look at the issue and then. Take it from there. Yeah. 

**Tim**
* Thank you for sharing. yeah. The background here, Lightclient has a question in the chat asking around, asking about what the upper bound we're looking for is because, yeah, with 7623. We have a bounded block size. so like. Yeah. Is that sufficient or do we need to do something else? 

**Arnetheduck**
* 7623. Is that the gas repricing for data? 

**Tim**
* Yes. 

**Arnetheduck**
* Yeah. There's still no bound right. So there's the bound space. 

**Tim**
* Yes. There's a bound that's dependent on the gas limit. Yes. 

**Arnetheduck**
* Yeah. So it's this link between the gas limit and the size of the block. That is the problem. As long as the size of the block is determined by the gas limit, no matter what the gas limit is, then as long as we don't have an upper bound on where the gas limit can go, we also don't have an upper bound on where the block size can go. And this is the problem. so imagine we have, you know, bigger gas limit or whatever, right. And we have a massive block even with the electro change. And that's something that we should think about how to address in the longer term. 

**Tim**
* So I guess, yeah, one thing we have discussed on this topic in the past is bounding the gas limit and protocol, and having something like a max gas limit in protocol, still allowing validators to like, lower it if needed. but if there is like a specific point at which the, you know, the block size is concerning, that's another solution that's like a relatively minor consensus change. The obvious downside here is then expanding the gas limit beyond that is subject to. 

**Marek**
* Change. 

**Tim**
* Yeah. yeah. Let's do Ahmad first  

**Ahmed**
* Yeah. so one thing here is that even if you limit the transaction size, you can always add more transactions that has that add to the size. So unless like there is some mechanism to limit the size of the whole, like all of the transactions in the block, which is very hard to reason about, I don't think this approach will work. I think that transaction like gas limit is enough to reason about if we want to set a limit to a singular transaction size, then maybe we should limit the, like add the gas limit per transaction. like, I don't think any transaction should exceed 30 million gas or 20 million gas even, but, that is, definitely something to think about and analyze. but yeah, I don't think, setting a size 4444 the transaction,  is a solution. 

**Arnetheduck**
* Yeah, we're not talking about that. we're talking about the total list of transactions limiting a single transaction, which kind of inefficient. It's better to have a single large one than, you know, a thousand small ones. So I don't think that is an efficient way of addressing this particular problem. 

**Tim**
* The Potuz

**Potuz**
* Yeah. I wanted to mention that among all the options, it seems to me that it's limiting the size of the slices Jezek is suggesting. it's actually safer, and it's less back prone. we have two different limits. One is on the network gossiping, and the other one is on the gas limit. The gas limit is up to the community to decide. And it's in principle it should vary more often than the bandwidth requirements that we can handle on the consensus layer. It seems much easier to let the latest one up to core devs to decide this is how much clients can actually handle on the gossip side, and we are going to gossip up to this limit. And then it's easier to reason about that. The gas limit is handled by the EL, purely by the EL, and then the builder is going to refuse to build blocks that are larger than the consensus limit. So then you have these two guys that are actually separated. So you keep them logically separated limits. And you don't need to be doing like complicated computations.
* You just know that whatever the community decides for the gas limit they are allowed to do, but then the builder is never going to build a block that is not going to be propagated by the consensus network. 

**Tim**
* Okay, thanks. Lightclient

**Lightclient**
* It doesn't seem like we're really looking at looking deeply into the capping a single trans limit transaction size. But I just wanted to say that I definitely opposed to that approach. I think there's a possibility that in the next couple of years, we see a lot of consolidation in the number of transactions due to seven 702 and due to four, three, seven gaining more popularity. So you can imagine there only being a handful of transactions in a block. So in which case it would not be great to limit the transaction size. In general though, I feel that limiting the transaction size or transactions size arbitrarily in the consensus layer is pretty wonky, and would definitely prefer to either fix the gas limit so that these constants are uniform across the stack, or to make the message size some sort of product of the gas limit. 

**Tim**
* All right. Thanks. Let's do Ben. 

**Ben**
* So block building with the gas limits already an NP hard problem. And if you're also then throwing in the byte limit, you're making it computationally much, much harder. so if there is an easier solution, it would be better. 

**Tim**
* Thanks. and I don't know if your hand is still up or if you had one more comment. Yeah. 

**Arnetheduck**
* One more comment. Like, I will note that, we can pretty much compute the maximum sizes from the gas limit, which means that if we do impose maximum gas limit, then we're also effectively imposing a maximum block size. And then we've also solved the problem. and then the way that I imagined that this would work is that, you know, the maximum gas limit is set by developers and increases or decreases a Hogwarts or whatever it does. but it's almost the same thing, except that we don't have a bite limit or we have a derived bite limit. 

**Tim**
* Thanks. that's the downside. 

**Arnetheduck**
* Oh, sorry. Yeah. One more thing. The downside? Yeah. So the downside of that approach is that, one thing that we've noticed while investigating this is that there is a very big difference between what a practical transaction looks like and what a so-called attack transaction looks like. An attack transaction is all zeros, and it's very large and also entirely useless. There's no practical reason for sending these massive transactions today. the other thing that this limit poorly captures is the fact that we use compression While the limit is set on the uncompressed data. So and this is because you can play with compression bonds and things like this. So it's easier to define it in terms of the uncompressed data. But it kind of this representation doesn't 1 to 1 correspond to the actual network effect it has. So there's a little bit of complexity in choosing a number. And the final thing is that, it competes with uh blobs in terms of bandwidth.
* So when the block goes out we have to transmit both blocks and blobs. Any increase that we do to the block comes at the expense of the amount of network bandwidth that we have available for blobs in the design that we have today. Also interesting to keep in mind. 

**Peter**
* I'd just like to say that I think that this is something that needs to be done, using gas on the execution layer. I think various people have like played with like ideas of various sorts of special caps that could be imposed. I think imposing those sorts of caps is just going to create weird edge cases in the block building process and cause issues, and we have a mechanism for preventing people from using too many resources, which is that we charge them gas for the resources. And so I think we should focus on like gas based solutions. 

**Tim**
* Thanks. let's do okay voters and then move on from this and continue the conversation on the issue afterwards. 

**Potuz**
* All right. So there are a bunch of misunderstandings in the chat. so and I wanted to address this thing of like the Peter was mentioning. Of course, it seems that the best solution would be that if this is handled purely in terms of gas, but it's actually not trivial to do this like multi-dimensional gas does not address this directly. You have to have some sort of constraint by constraint based system for pricing. And this is actually complicated. Eventually we might get there. But as mentioned in several times, we have a gas limit that allows for this theoretical attack blocks that are very large, but most blocks are much smaller, even if we increase the gas limit a lot. so in principle, I don't see any problem in allowing the gas limit to increase, but preventing this attack blocks just by hard capping the size of the block. This can be done at the El in a fairly simple manner.
* And of course we can then see what is the right solution at the gas price level so that we avoid this with gas instead of like just hard capping the size of the block, but I think it's fair to allow for devs to hard cap the size of the block, because we're doing this already on the consensus layer anyways, and just leave the community to allow them to hard cap the gas limit, which are, and keep these two as separate as possible. 

**Tim**
* Okay, thanks. yeah. Let's continue this conversation. async. Clearly, there's much to discuss. hopefully we can, yeah, get to a resolution in the next few weeks. okay. Next up, we have a bunch of different EIP discussions. first off was Andrew from Aragon, that had concerns about removing new block hashes from Eth 69. Andrew, do you want to share that? Sure. 

# Reverting removal of NewBlock(Hashes) in eth/69: Update EIP-7642: don't remove NewBlock(Hashes) EIPs#9133 [56:14](https://youtu.be/XtdJ2G8yST4?t=3374)
**Andrew**
* So, like in Aragon, we support Ethereum and polygon and analysis chain. and polygon hasn't gone through the merge, although they use it like a kind of a proof of stake consensus. But it's different from that of Ethereum. And basically they still use new block and new block hashes messages. but and but uh is is is 69 potentially can still be beneficial to polygon because it drops the Bloomfield um and yeah. The, the total like drop like we can have a work around about like regarding dropping the total difficulty, but, we definitely need new block and new block hashes for polygon. And I'm arguing that we should not remove them from ETH 69 because it doesn't bring any benefits for Ethereum because they are already, they are already not used after the merge. So like if we remove them and we can potentially reuse the same opcodes, but it's just pointless, like it doesn't bring any benefits.
* So I'm arguing that we shouldn't do it because, yeah, it doesn't bring any benefits, but it, it introduces incompatibility and incompatibility with other blockchains such as polygon. 

**Felix**
* So I'm fine with not dropping them. I think it's it's totally reasonable to have these messages. The mechanism is very simple. I'm actually not sure if we have even deleted the implementation of it in Geth, I think. I mean, they are practically not used, but, yeah, It's. It doesn't hurt to have them in the protocol anyway. 

**Andrew**
* Yeah. And I understand that it is a balancing act that like, we we should care about Ethereum first and foremost, for sure. But I just think I'm thinking still, we have to be mindful of the broader ecosystem. And kind of if I'm pretty. 

**Felix**
* Happy that the P2P protocol is kind of shared, at least with some systems. So I do think that it's fine for me personally as the maintainer of the spec to, you know, like figure out ways to incorporate, you know, other systems needs a bit into these specs, as long as it's in the realm of, like what the protocol is designed for, which is, you know, like handling the chain, how we will do this the long term. I don't really know. But for now, just like keeping these messages in the protocol is not a big issue for the spec at all. It's literally not a lot of text. And yeah, like I would just keep it cool. 

**Tim**
* Okay. Thanks. Anyone opposed to keeping it? Okay, well, we can move forward with this. I will have to hop off, in the next minute or so. So we'll hand it over to Alex to run the the rest of the call. and maybe just introducing, like, the next thing we had on the agenda. there was an update to an EIP we discussed a while back. 

# EIP-7503 Feedback Request  [59:52](https://youtu.be/XtdJ2G8yST4?t=3593)
**Tim**
* The wormholes EIP asking for feedback. I don't think the person who did this is on the call. but, yes, I don't know if, we want to discuss this live on the call or people want to just review async. Think, if there's any comments concerns, we can discuss those now, but otherwise I think I'd just point people towards the yeah, the PR. And yeah, it's not something that, is like for the next fork. So yeah, it doesn't seem like the most urgent thing to discuss on the call. okay, we'll hand it over to Alex then, and. Yeah, take it from here. Thanks, everyone. 

**Stokes**
* Thanks, Tim. Let's see. So we covered that and. Right. So yeah, there was a comment here just to close the loop on this wormhole thing. it sounds like they're just looking for feedback, so. Yeah. take a look at this PR 9080 when you have a chance. Next up, 

**Peter**
* Sorry. Do you mind if I jump into something? A very quick thing that I point out. there is on the discussion of the wormhole, the EIP, a small a potential for legal risk, because obviously this sort of tech could be used for people to do money laundering stuff. and there have been cases where people have been prosecuted for developing anonymity tech. so I think if there is going to be a process where people want to implement this, we may need to like think about that issue, intentionally. 

**Stokes**
* Right. Yeah. I mean, I think there are a lot of additional considerations. It sounds like, from the comment here that they're just looking for technical feedback on the implementation. so, yeah, I mean, to start, if anyone's interested, we can just take a look at that. And yeah, like we were saying, I think it's probably quite a ways away from any particular hard fork. Conclusion. So these other questions are very, very important as you call out. but yeah, probably not something we need to handle right now. Thanks. right. Okay. 

# EIP-7808: Reserve Tx-Type Range for RIPs [1:02:19](https://youtu.be/XtdJ2G8yST4?t=3739)
* So next up we have EIP 7808. This wants to reserve part of the transaction type range for rips. the way this works is that EIP 2718 gives us transaction types that all of you, I think are very familiar with. And, yeah, essentially the EIP wants to claim the upper half of this range for rips. So essentially roll ups can use them for their own purposes. Let's see. This is from Karl Rove. Ansgar, do one of you want to add some more context? 

**Carl**
* Yeah. So basically a bunch of the things that we would like to be able to, ship for L2's are constrained by this. many of the things surrounding, for example, account. Abstraction and trying to cut abstraction require new transaction types and L2's themselves would also like to have a more principled way about reasoning about transaction types. So, much like we discussed on a ACDE a few months ago with, EIP 7587, which reserved the upper half of the precompiled range for use by the, report, the RFPs. this would do the same for the transaction types. And just for context here, this range is, 128 transactions wide. So this would be assigning 64 to both. So we're nowhere near this limit on main net or something. So it's on L1. So there should be a constraint. 

**Stokes**
* Yeah. And it's hard to imagine we would have this many transaction types at L1, which, you know, maybe I'll have to eat my words someday, but this seems pretty. Pretty straightforward. 

**Carl**
* Yeah, and if need be, we can also become like supersede this EIP with something more concrete that that divides up the range more carefully if in the future. But for now, I think this is a a reasonable thing to do. 

**Stokes**
* Yeah. And it seems like we could merge this outside of any hard fork schedule. So essentially, yeah, I think we just need agreement on the idea. Anyone think we should not do this? Okay, I think the next step is maybe to move the CIP ship from draft to the next stage. but, yeah, sounds like there's no pushback, so. Thanks. Okay, next up, 

# EIP-4803: Limit transaction gas to a maximum of 2^63-1 [1:05:15](https://youtu.be/XtdJ2G8yST4?t=3915)
* We have EIP for 4803 lots of IP today. let me paste the link here. So yeah this was basically capping transaction gas. essentially there's no reason for it to be bigger than this. And let me see if there was a comment here. I'm not entirely sure why this was here. There's a note that says unclear what consensus was and if this PR should be reverted. Does anyone here have any more context on this IP? 

**Felix**
* I mean, the basic idea is pretty simple, right? It's just that the gas has a practical limit of 64 bits, so we can just treat it as that. This is something that all the client implementations have done as far as we know. Like just they treat it as a UN 64. So it's for all intents and purposes, it has been retroactively applied. 

**Stokes**
* Right. Okay. I'm not sure. Yeah. Apologies. I'm not sure what the action item here was. 

**Felix**
* I mean, I guess it has to be updated in the executable spec. 

**Stokes**
* Right? 

**Felix**
* So can someone from EL. Can you comment on this? Like, are you treating gas numbers as 64 bits in the spec or. 

**Danno**
* So there's debate whether it's a 64 or an I 64 signed or unsigned I think is one. And as written in the agenda, it's signed. 

**Peter**
* I can jump in on this. So, the current system, I think, in the spec, is that, I think we technically might actually treat gas, as an unbounded, signed integer, which is supported in Python. Um. This um and basically there's two sets of issues here. The first issue that happens here, is that there are some things that bounds that are impossible to hit in any plausible scenario, but that someone has to put a bound in the code.
* It's like the issue with like we've capped the nonce at, two to the 64 minus one. despite the fact that it's completely implausible that anyone is ever going to achieve a nonce on any account of two to the 64 minus one. the the second issue, which I think we're going to have to work on, is, dealing with the issue of, exactly how bounded, different like objects in things are.
* So we've had situations where people have written tests, that involve, rejecting transactions with nonces of two to the 64.
* And the problem we've had is that, those, those tests, like, they just don't process because some clients, when told to put, something greater than that, doesn't fit into a u64 into the transaction nonce field, just fail to pass, the, the field at all. so I think this is an area that needs like a sort of coherent thinking. It's something that I've been thinking about. I will write an issue on the execution specs repo and post it, probably in the all core devs channel. and we can sort of move from there because we don't really have a particularly coherent way of thinking about how fields are that are capped by size, are capped, and what's the consequence of those caps? 

**Stokes**
* Okay then. Yeah, just share the issue. Once you have it. Any other comments on this at the moment? Okay. Thanks. 

**Felix**
* I mean sorry 

**Stokes**
* Oh yeah. Go ahead. It was a bit late. 

**Felix**
* So notably I mean this is an EIP, which is basically it's it says it's in a review stage, but in practice it's like in the final stage. But since it is sort of final, if we want to make an update, we can just make another Eth that like further restricted or changes it or whatever. But I would say that, you know, like it doesn't feel so productive to resurrect these like super old eaps and try to change the status when literally they are in the past and like have been dealt with. 

**Stokes**
* So you're saying we should just ignore the EIP? 

**Felix**
* No, I mean, it's basically active, but what I mean is, like, we could. I mean, it just seems weird that we're discussing super old, even trying to change. Yeah, we could just make a new one. I mean. 

# Update EIP-7723: CFI/SFI & Devnets EIPs#9126 [1:10:38](https://youtu.be/XtdJ2G8yST4?t=4238)

**Stokes**
* Okay. Anything else on this? Okay, then we'll move to the next set here on the agenda. There's just a number of announcements and. Yeah, the first one here is 9216. 
* Let me grab a link for that one. And essentially yeah I think the update here is just that this has been merged. There was some language here updated in EIP 7723 around different statuses for parts of the apps throughout the process. just yeah, updating again how we use some of these things. There's this notion of CFI, SFI and then how they relate to devnets. we covered this I think last week on ACD. So yeah, should be pretty straightforward. And I think the update here is just that this has been merged. Okay. Next up, a new EVM resource pricing working group. So David and Ansgar, have an announcement here. I don't know if one of you on on the call. 

**Davide**
* We're both here, I think. Oh, hey. 

**Stokes**
* Yeah. Would you like to give. Yep, yep. 

**Davide**
* If I can share my screen for one minute. Also give more context. Yeah. So, this is, the gas schedule that was used initially to set gas prices and then like it was used once again, I think in Epe 150 and then, we didn't use it, anymore, but essentially like, what we are doing with Asgard is we are doing some research on resource pricing, focus on like multi-dimensional resource pricing. but we think that there is like some interesting, benchmarking modeling work that can be done. it will both, like, support the work we are doing and also potentially help us, with this repricing of opcodes that we want to do.
* So basically here, what was done is like, resource prices were set in a pretty principled way, right? Like you can already see that there is multiple People resources. Many of you have seen this, but like for who has not seen, I will just like go very quickly over it. and then for each resource there is an approximation of how much it will cost, right in like, for example, for compute uh in microseconds, history bytes, etc., etc.. And then there is a gas limit, which was 3 million in this case, and now it's much higher. But then there is also a gas limit for each resource. And then basically the full cost was computed by like um aggregating like all the resource costs. So this is already in line with what we want to do with resource pricing. so we think like, it would be really interesting to get like some, clients involved to help us basically refresh this.
* Like we've never, like, refreshed it, like there's been like some IPS that touched like specific opcodes that I also reported here, but, most of these are stale. I know that there is some interest in like, doing repricing. and I think this benchmark can also help doing more principal repricing as well. yeah. Most of the opcodes are on the compute side, but we are also quite interested on like, the ones on the IO side. And yeah. So this is kind of like the initial focus of the working group, but I believe Ansgar has also like 2 or 3 topics. I don't know if you want to add, Ansgar, more detail on that. 

**Ansgar**
* Yeah, sure. And maybe you can keep your screen share on for a second, because I think people are curious to see that. And yeah, so, so so basically the idea is that like there's both now more active research again, going ongoing on the kind of the longer term path here. And, I mean, I feel like in a way, multi-dimensional pricing is almost a bit of a meme at this point. But it's it's actually I think it's not even going to be that big of a change once we actually are ready to to do the full thing, but that's definitely going to take a few, a few more hard work cycles and to to get there.
* So the idea was to just see because there's already a lot of like individual efforts ongoing right now of people thinking about individual bits and pieces of, hey, could we do like some sort of shorter term repricing with these ideas of just taking all of, like this, all of these basic compute ERP compute opcodes and setting their price to one. And I know people have been working actively on, on, on precompiled benchmarking. And so basically the idea would just be to, to have a to, to basically create a working group and to bundle all of these individual efforts and, and, make sure we can work towards something that, I mean, I would say my target would be to try to have something shippable for Osaka. I mean, of course, who knows? Osaka is already getting pretty full, so maybe it would be a plus one.
* But either way, basically like work on the more like short term shippable things. yeah. Is that what you were saying? The focus would be the kind of just a one time repricing and one time not, meaning we would never reprice things again.
* It just means like a static repricing. Not not the not the multi-dimensional. but there are also some other small things that I think could be part of, could be in scope for like short term changes around like block level pricing around, a few other tweaks like this, this gas sharing kind of, fix. So, so, so basically just all things for markets in like a more short term focus. and yeah, and the idea was just to give that a home. I think for now we were thinking the best thing to start would just be to say, create a telegram group. I think that we'd already created one. We can we could share the link in the channel and then take it from there. And then in the new year, maybe start with a a breakout call and, yeah, try to make progress. But yeah, I don't know if maybe if people have feedback.

**Stokes**
* There were some comments in the chat just about other threads here, but yeah, I think this sounds like a nice way forward. if you post a link to a group on discord and people can join and yeah, looking forward to any work that starts up here in January. 

**Ansgar**
* Right. And yeah, by the way, just, just I said because, Dan asked whether that's connected with these other efforts already ongoing. Yeah. So basically the point specifically is not for like us to like to basically start or lead this necessarily. and we were thinking maybe we can like basically help us like coordinators and with some, some of our own ideas. But, but, but the point is to, to just say, hey, there's already now several in several kind of several different groups in the code space right now are all working on, on some portions of this. So let's just make sure that all happens in a coordinated way. That's that's primarily the intention here. 

**Stokes**
* Yeah. Makes sense. Any questions from anyone here about this? Any other questions? Okay. Thank you. And to wrap up the agenda here. 

# Call for Input: Forcibly withdraw EIP-7675 ethcatherders/EIPIP#374 [1:18:11](https://youtu.be/XtdJ2G8yST4?t=4691)
**Stokes**
* Two calls for input. so yeah, again let me just grab the links here. So the first one is around changing essentially what meta means relative to the EIP and the EIP process. I'll just put the link here. let's see, Sam opened this. I'm not sure if he's on the call or if anyone else here would like to say anything more, but, yeah, I think ultimately just take a look. there's some conversation here, and I think the ask for this group right now is just to take a look at this. Okay. Otherwise, there's one more. let's see here. Forcibly withdraw. 7675. This is around retroactively activated EIPs. And yeah, again, just a call for input, for changing some of the semantics here. So, yeah, take a look at that. And otherwise. yeah. I don't know if anyone here has anything else you'd like to say about either of those. 

**Pooja Ranjan**
* Yeah, maybe I can add some context here. Generally we discuss some of the discussions. Those are happening on different forums, like all Core Dev Meeting or Fellowship of Ethereum Magician or even on discord. And if we collect some kind of questions and concerns from the community with respect to any proposal. We try to discuss those in EIPIP meeting and based on the discussion of EIPIP meeting, if editors want to make a, decision on that, we we invite people to share their comment on call for input. So this call for input is basically suggesting that whatever was discussed in the last EIPIP meeting, these changes could be implemented. We provide a one month time period for community to add their thoughts. So particularly talking about these two call for input. There is this one discussion that happened yesterday.
* It was with respect to how we are using meta EIP. Currently, meta EIP as defined in EIP one is mostly related to process processes.
* However it has been used as a upgrade meta. So this particular call for input is to  clarify that either we need to move all, upgrade EIP to informational, or we might want to update the EIP one. So whatever people feel good, they can go ahead and add their comment. And similarly the other one, as per the process, editors and the community do not want to maintain an active list of registries, and that's why there is this, call for input to forcibly close that particular proposal. So please take a look and add your feedbacks and comments to that. 

**Stokes**
* Cool. Thanks. Okay. I think we have covered everything on the agenda. any final comments from anyone? Otherwise we can go ahead and wrap up. I guess maybe just to call it out. There was a question in the chat around Devnet five timing, because I think that's probably a very relevant thing for everyone here. I think it will launch as soon as we have a sufficient number of clients ready. So I would treat the Devnet five launch date as imminent. Meaning? yeah. To the extent you can with the holidays. please make progress on the the Devnet five specs. Okay. Anything else? Otherwise, we'll go ahead and wrap up a few minutes early today. 

**Kevaundray**
* Is this working? 

**Stokes**
* Yeah. We can hear you. 

**Kevaundray**
* Yeah. I wrote in the chat. we've been working on sort of a hardware requirements doc for validators. That's sort of been sent around initially for some internal feedback. and it'd be good to sort of get feedback from the wider ACD and community. And this is like related to gas repricing because when you're benchmarking you sort of need to choose the hardware specs. Right? 

**Stokes**
* Right. Is there anything you'd like to share right now? 

**Kevaundray**
* I can share the link in the chat or in the, in the discord. 

**Stokes**
* Okay. yeah, I think discord would be good. When you're ready. Okay. Anything else? Otherwise, we'll close out for the day and. Yeah. Happy holidays, everyone. 

**Gary**
* Happy holidays. 

**Stokes**
* Bye bye. 


-------------------------------------
### Attendees
* Tim
* Stokes
* Mikhail Kalinin
* Marius
* Wesley
* Barnabas
* Saulius
* Danno
* Lightclient
* Pari
* Ethan
* Mario
* Tomasz
* Oleg 
* Kasey
* Marek
* Crypdough
* Fabio Di
* Terence
* Andrew
* Roman
* Marcin 
* Pop
* Guilaume
* Protolambda
* Carlbeek
* Mike
* Gajinder
* Stefan
* Hsiao-Wei
* Josh
* Phil Ngo
* Alexey
* Holger Drewes
* Dankrad
* Guillaume
* Proto
* Holder Drewes
* Peter Szilagyi
* Sean
* Micah Zoltu
* Jiri Peinlich
* Marius Van Der Wijden
* Potuz
* Evan Van Ness
* Moody
* Tynes
* Alex Beregszaszi
* Marek Moraczyński
* Justin Florentine
* Ben Edgington
* Lion Dapplion
* Mrabino1
* Barnabas Busa
* Łukasz Rozmej
* Péter Szilágyi
* Danno Ferrin
* Andrew Ashikhmin
* Hdrewes
* Crypdough.eth
* Ameziane Hamlat
* Liam Horne
* Georgios Konstantopoulos
* Mehdi Aouadi
* Bob Summerwill
* Jesse Pollak
* Stefan Bratanov
* Sara Reynolds
* Caspar Schwarz-Schilling
* Ahmad Bitar
* Marcin Sobczak
* Kasey Kirkham
* Sean Anderson
* Saulius Grigaitis
* Ruben
* George Kadianakis
* Dankrad Feist
* Andrei Maiboroda
* Gcolvin
* Ansgar Dietrichs
* Jared Wasinger
* Diego López León
* Daniel Celeda
* Trent
* Mario Vega
* Kamil Chodoła
* Ziogaschr
* Kevaundray
* Antonio Sanso
* Oleg Jakushkin
* Leo
* Nishant Das
* Pote
* Sam
* Tomasz K. Stanczak
* Matt Nelson
* Gary Schulte
* Rory Arredondo

-------------------------------------

## Next Meeting
[Jan 16, 2025, 14:00-15:30 UTC](https://github.com/ethereum/pm/issues/1227)
