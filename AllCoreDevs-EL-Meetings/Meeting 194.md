# Execution Layer Meeting #194
### Meeting Date/Time: Aug 15, 2024, 14:00-15:30 UTC
### Meeting Duration: 1.5 hour 
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1124)
### [Video of the meeting](https://youtu.be/tbxgYq8KmmM)
### Moderator: Stokes
### Notes: Alen (Santhosh)

| Decision Item | Description                                                              | 
| ------------- | ------------------------------------------------------------------------ | 
| 194.1 | **Pectra Devnets**  Pectra Devnet 2 is stable. There appears to be one outstanding issue on the Devnet 2 information page related to merging block builder specifications and testing them on devnets. EF Developer Operations Engineer Parithosh Jayanthi said there are also issues with Teku/Erigon nodes and the Prysm client.
| 194.2 | **Pectra Devnets**  Developers are aiming to launch Pectra Devnet 3 with updated specifications for EIP 7702 in two weeks. Developers plan on adding EOF to the devnet thereafter, Pectra Devnet 4, if all goes according to plan.
| 194.3 | **Pectra Devnets**  Geth developer Marius van der Wijden shared updated analysis on the gas costs for EIP 2537. As background, the EIP creates a new precompile for BLS12-381 curve operations. It enables smart contract developers to perform operations such as signature aggregation over the BLS12-381 curve in a cost-effective way. Van der Wijden proposed a repricing of the precompile based on benchmarks he and his colleague on the Geth team, Jared Wasinger, made for BLS operations and their gas usage on various machines. Van der Wijden encouraged other developers to run their own benchmarks on EIP 2537 gas usage to verify results.
| 194.4 | **EIP 7732**  Prysm developer “Potuz” shared updates on EIP 7732, an in-protocol solution to directly connect validators to third-party block builders. Since the Merge, validators have relied on intermediary actors called relays to receive blocks containing MEV rewards. EIP 7732 removes the need for relays so that validators can earn MEV in a more trustless manner. Potuz highlighted that the current design of EIP 7732 requires no changes to the execution layer (EL) or Engine API. He added that EIP 7732 is also compatible with inclusion lists, a proposal to enable validators to force inclusion of transactions in a block. More information about EIP 7732 can be found in this Google slide presentation.
| 194.5 | **Reducing Pre-Merge Tech Debt**  Since Ethereum’s transition to proof-of-stake, there are parts of the Ethereum codebase that are no longer useful or necessary. For example, the difficulty bomb, which was a mechanism to force development work on proof-of-stake by making it infeasible to create blocks through proof-of-work mining after a certain period. The following two proposals are aimed at removing such parts of the codebase to improve node performance and reduce protocol complexity.
| 194.6 | **Reducing Pre-Merge Tech Debt**  Erigon developer Giulio Rebuffo proposed the removal of the “totalDifficulty” field from the Execution API., Geth developer Marius van der Wijden proposed the remove of a few pre-Merge fields and messages from the Ethereum Wire Protocol. There was positive feedback on both proposals from other developers on the call. Developers agreed to review both in more detail asynchronously after from the meeting.
| 194.7 | **PeerDAS**  On the topic of PeerDAS, a Nimbus developer by the screen name “Dustin” proposed hastening the rebase of PeerDAS on top of Pectra EIPs instead of continuing to develop PeerDAS on top of Deneb. He acknowledged that there are EIPs in Pectra that are unstable and subject to change such as EIP 7702 and EOF. Dustin recommended rebasing PeerDAS on the subset of Pectra EIPs that are stable and excluding EIP 7702 and EOF transactions on PeerDAS devnets. Developers discussed other ways to start rebasing PeerDAS on Pectra. There was general support to start moving in this direction.
| 194.8 | **EIP 4444**  There were no major updates on EIP 4444, history expiry. Representatives from the Nethermind and Nimbus team said they are in the process of building out their integrations with the Portal Network, an alternative networking protocol for users to access expired history data.

**Stokes**
* Okay. Hey everyone, this is ACDE 194. There's the agenda in the chat. And yeah, let's go ahead and get started.
* So first up we have Pectra and we wanted to touch on devnet-2 & devnet-3. Would someone here be able to give an update on devnet-2? 


# Pectra [0.34](https://youtu.be/tbxgYq8KmmM?t=34)
**Paritosh**
* I think things have generally been going well, and yeah yeah, in general things are stable. We've updated a few images. 
I think there was an arrogant block production issue that's now been fixed. but besides that, things have been relatively stable and we haven't probed much. most of the times when spent on 

**Stokes**
* Anyway, so I know for Devnet-3, we wanted to touch on 7702. do we have any updates there? I think there were, like, some last minute spec things to address 

**Marius**
* Yeah, we what? I wrote on the agenda. We recently figured out that our implementation was, using multiple cores for the, MSM and for BLS 2381, which means that the current gas costs are too high for us and we would like to, increase them a bit, at least for the G one, multi exponentiation yeah, the G two looks fine to us because we baked in such a margin of error but the G one, now that we realized that we, we were using the library in a multi-core way or. 
* Well, the library internally was using multiple cores which it didn't really advertise, but, yeah. we would like to run some more benchmarks and increase the gas cost of one multi exponentiation 

**Stokes**
* Okay. This is something you want to put in devnet-3. 

**Marius**
* Ideally, yeah. Depends on when Devnet-3 is happening 

**Stokes**
* Yeah. Maybe you cut out, but I was asking about 7702. But it sounds like we're generally ready to go. in terms of the spec, are there any implementation points to touch on right now 

**Paritosh**
* I think we still need a execution spec release just so we can add the, add the version and besides that, also just wanted to surface one other point, 
* Barnabas. There is a Teku Aragon issue that's still live on Devnet-2. I'm not sure if either team's want to talk about that / fix it separately, and if that's a block of a devnet-3. 
* Yeah. so there's a Taco Aragon issue that Barnabas also mentioned in chat I forgot to bring up earlier.
* I wanted to see if anyone from either teams wanted to, talk about it or if we deal with it on discord and separately. I think we were waiting on an execution spec test release as well 

**Mario**
* Yeah. Regarding the execution spec test, we are ready with the tests for 7702. but the problem is that we need the, transition tool. 
* So that means that we need at least one implementation from the clients to fill the tests. That's the only thing that we're really waiting 

**Stokes**
* Okay, cool. Yeah. And it sounds like from the chat, they'll just take that to discord I'm trying to fix the sound on the YouTube stream, so apologies.but I don't know how to do that So anyway, we'll just keep going right. Okay. 
* So otherwise, yeah, it sounds like we're in a pretty good place for Devnet-3. we'll get execution, specs release, and. Yeah. Otherwise, do we want to talk about timing 

**Paritosh**
* Yeah, I think timing just depends on readiness. So the clients already have the 7702 changes implemented um to CL teams already have the new spec release implemented. 
* And yeah, depending on that I guess we can talk about scheduling 

**Stokes**
* So do we feel good saying like two weeks from now? Is that enough time 

**Stokes**
* We have one comment in the chat. Uh 

**Stokes**
* 7702 is not implemented yet. Okay. so yeah, maybe we'll just need to, wait for that. Unless we do want to try to set a date today is two weeks enough time for people to implement 7702. 

**Barnabas**
* Wouldn't it make more sense to push for EOF then before we do? 7702 if EOF is already implemented, then we can probably include that in Devenet-3 and then swap it around uh with 7702 for devnet-4. If 7702 still requires, implementation time and and assuming that EOF is ready to be tested already 

**Danno Ferrin**
* So eof the issue, we would need to have people integrated with the Prague network. I'm not sure that all the implementations have merged their EOF against their Prague. 
* A lot of them are still doing against Cancun, so that would be something that would take a little bit of time of moving EOF into Devnet three, because last week on the EOF call, we had some, I think it was Perry, someone from the DevOps team. and the plan we went with was to do it after 7702. So there's only one major change. I have seen it work in within Assertor on kurtosis. 
* So there, there is I've seen that work. That was my big hangup there. but I'm just concerned about, you know, getting it in two weeks. We probably could, but I would want to get feedback from the other EOF devs before we change the order 

**Stokes**
* Yeah, I think we keep things as planned. and then, yeah, I feel like I've heard, some news straightforward enough to implement that. Yeah, I think we'll just wait for that. do we want to wait then I guess yeah, either the next call or next CL, to check in there 

**Lightclient**
* I mean, why don't we just plan on launching in two weeks from now 

**Stokes**
* That works for me 

**Lightclient**
* Does anybody against that 

**Stokes**
* Okay, we got a thumbs up and other comments you know, I think if a client needs a little more time, I think we can still launch, you know, everyone else two weeks and go from there yeah. Sorry. I'm working on the sound with the stream, and it's It might just not happen today. Anything else on Devnet-2 or 3? 

**Barnabas**
* I'm not sure anyone from Prism is here to give an update. We've been having some issues with Prism Devnet-2. 

**James**
* Yeah, for prism Devnet two. there were some bugs with the, 7549 EIP that we implemented. We just merged in, some some fixes for the sync committee related items, and hopefully that'll improve things. other than that, we'll just, keep debugging  on Electra This is merged into latest develop 

**Stokes**
* Okay. Thanks So there was also a point on the agenda. We kind of touched on it, around EOF readiness. I think we've kind of said Devnet-4 is like a rough target. anything we should discuss now on the call? I'm not sure how implementation is going. anything like that 

**Danno Ferrin**
* So we have, we've run so we have some We wrote some EOF container fuzzers. and we have, there's a couple of outstanding bugs on a couple of the clients. And as the clients are implementing the old big EOF fuzzing interfaces we're doing runs through those. so we got fuzzing written there. we're, you know, always writing more tests. There's 

**Danno Ferrin**
* Always, more tests to be written. and the next step is going to be getting the, the execution fuzzing updated. so ideally, with all the testing that's going on,  devnet-4 is going to be fairly uneventful because we'll have tested so much of it. talk about this on the UF call, but I would like the other clients to make sure that they can run the, the creation transaction. And that's the real on ramp for EOF. So that's where the real change would happen. 
* When we go into a test, into a devnet from a local environment would just be the the actual live creation transaction that's going to, you know, see the EOF into the system, see some of those first contracts. but yeah, it looks, it looks fairly good. like I said, I was planning on targeting Devnet for not Devnet-3, so that's, you know, we could do Devnet-3 as possible, but if people are happy moving debit. three out, two weeks for 7702. I'm totally fine with that decision 

**Ben Adams**
* Never mind. all up to date for EOF. the only thing we have at the moment is, one of the tests 108, then have fixtures So it is possible we might fail some tests So we can't run this Okay. 

**Stokes**
* Would it be helpful to get test for that case 

**Ben Adams**
* Yeah, it's just the fixtures for the latest tests need to be included in the artifacts 

**Stokes**
* Gotcha. Is that part of the spec release or do we do that differently 

**Ben Adams**
* I think it's differently. It's just the the the test suite. Really 

**Ben Adams**
* So we're we can't test the latest updates to it 

**Stokes**
* Gotcha. Okay 

**Stokes**
* Right. So, yeah, just to echo us here in the chat, Perry says, maybe devnet-4, say, four weeks from now. maybe that's a little tight, but yeah, I think we can focus on Devnet-3 and aim for Devnet-4 on on roughly that timeline and probably on the next call, have a better sense of what makes sense Okay. Marius, was there any other point on the last benchmarking that we needed to bring up 

**Marius**
* Only that it would be really nice if other clients could also, run some benchmarks and see if they can hit the same numbers, that we proposed. I will I will do some more benchmarks and propose new numbers for for what we think the G1 MSM should 

**Marek**
* We plan to do so with our solution that you have seen, and but I'm not sure if we should target issue recover, but it is another discussion 

**Stokes**
* Okay, there's some chat here. yeah, I think people are going to take a look. It sounds like But yeah. Thanks for bringing that up, Marius So cool. Anything else? on this core factor set that we should discuss now? Otherwise, we have some other things to discuss That. Yeah. Seemed like they fall a bit out of the devnet cycle right now Okay, cool. So the next we have, just wanted to bring up EIP 7732.
* I think POTUS is on the call. Although I don't see him Maybe he's not here 

# EIP-7732 [17:15](https://youtu.be/tbxgYq8KmmM?t=1035)

**Potuz**
* Here I am, but I'm not really sure if people can listen to me 

**Stokes**
* Okay 

**Potuz**
* Am I missing? Yeah. 

**Stokes**
* We can. We can hear you. Yeah, we can hear you. 

**Potuz**
* Okay, good. just managed to log in thanks to president that pointed to the browser version all right, so I don't want to take much time from you guys. I think most or all of the CL team already know about what EIP is. I just wanted to pitch, like, in 3 or 4 minutes. what? The EIP is, as part of the formal procedure to try to advance an EIP all right, so the the things that I don't have a slide or anything like this, so I'm just going to be just a quick pitch. 
* The things that I suspect El devs would like the most is that you don't need to do anything. The IP does not include any changes on the El side it's purely a consensus change. It doesn't even include changes on the engine API. So, as far as as far as I'm concerned, I think the If else if you guys want to, you might want to implement some changes on the builder API. 
* If you want to support being a builder Otherwise you don't need to change anything. So that's that's a good a good thing now, more into the actual changes, the most dramatic improvement that the CIP does has nothing to do with its original purpose. And it's the fact that we can get delayed execution validation without any changes on the El. So that's that's something that is nice. You don't need to change the El consensus algorithm. but only changing the CL consensus side you get for free that are testers that validators do not need to have two seconds to validate a block. 
* They now have around nine to 10s to validate a block. So this is because the testers only attest to the previous execution block and the current consensus block so I suspect that this is the most wanted change for most of the community the way we achieve this is by the mechanics of how the auction runs. SoPBS ultimately was about, reveal the rights to construct a block, to put transactions in a block and some builder that wants to buy those rights and prepare the block. 
* So the way this is going to work is that the proposer will gather bids by either contacting directly the builders or by gathering them from the P2P layer or by gathering it from its own El, and will send a block, a consensus block with a commitment to a bid from a builder The consensus layer is going to take care of, payments. So the builder will have to be staked and have to have at least money so that they can pay for that bid. And that money is deducted immediately as soon as you process the consensus block. 
* But the payload is only revealed later. It's only revealed later in the slot. If your home staker and you want to be your own builder, you can submit your block and immediately submit your payload at the same time if you're a builder, that are widely connected, you're going to see a block and immediately submit your payload. But you have the right to wait a little bit about three seconds and then submit your payload later when you feel comfortable that, that the block has been attested.
* So there's a second round of attestations, by a very small committee called the BTC or Payload Timeliness Committee. And this committee only attest quickly to having seen the build the the payload. 
* So instead of attesting to the validity of the payload during the current slot, this committee only says I have seen this payload and it has the right hash and it was by the right builder, so please don't reorg it. So that already gives it gives the builders a boost so that if the builder is honest and reveals the payload on time, the block will not be reworked and it cannot be unbundled for example, or unblinded also. 
* So what happens after this is that at test, the the next proposer will build on top of this, and a testers will now have to have already verified the execution of that payload if they want to attest on the child of that, on the descendant of that block. 
* So this is the way that you get, delayed, delayed execution for free because of as a corollary of the the way that we we have the mechanism What other changes? I might mention these changes are compatible with all the ways that we know now how to implement inclusion lists. there are some trade offs. for example, what I just told you that you get, like, nine seconds. That number might become smaller. 
* Or for the next proposal, you have, like, 96 seconds that my number might become smaller if we if we include inclusion lists, inclusion lists necessarily have changes on the CL side. And that's why we didn't include it on the EIP. 
* But, but this CIP is fully compatible with those modules. Small trade offs on timing there are also compatibilities with other designs for auctions. We can do immediately now with the same IP with small changes, we could do slot auctions. That means the builder does not commit to a particular payload hash. I urge you to go and look in the the meeting calls or in the RNG to see what is the discussion about advantages and disadvantages. I'll put some links if people haven't put them already in the in the chat, 
* I'll put some links to a notion document that Barnaby started with the blockers and the discussions on design decisions that we could still we could still have, as far as I know. 
* So prism is very advanced on the implementation of this, and we hope to have it completely working by, by Defcon this year Teku has started. Lodestar has started, implementing this, and Nimbus has started implementing this. As far as I know, I think only Grandin and Lighthouse are the ones that are that are not working on on having an implementation for this, but I'm very hopeful that we will have a proof of concept very soon. okay. And that's it. If you guys want to join us in the discussions, you're more than welcome 

**Stokes**
* Cool. Thanks. Yeah, this is in the combanition of many years of research at this point. So yeah, super exciting to see the EIP and how things move along. So yeah, if you have any information like slides or things, you could share in the chat, that'd be helpful. And otherwise. Yeah, I guess the signal for everyone here is start to get it on your radar Marios has a question. What are the downsides 

**Potuz**
* Yeah. So let me think about this. So if those questions were for me. Slides. I do have slides. I'll just post the link in a bit. as to downsides of this, I actually don't see any there are some, some there are some minor things. 
* For example, if we go with block auctions as it is now, the EIP vanilla EIP as it is now, the downside the downside is that if you submit a transaction after the payload was, the block was already signed and left and the payload is revealed. So that's the time that can take like three seconds, then your transaction cannot get in that payload. So once you submit a transaction in the global Mempool, your transaction can only be included in the next block if you are within those few seconds.
* So this may delay, the confirmation of a transaction on chain for a few seconds another, downside of this, I think from the point of view of the builder is a problem that they need to have, money on the CL.
* I've been told by the main builders that this is not an issue at all but I can see why builders might not want to, might not want to stake the validators so that's another minor downside. What other downside do I know? Complexity is I think it's as any change that was just an issue as any change, complexity is an issue. But this complexity gives us for free this, this scaling factor, which is the fact that we can we don't need to validate the execution, which I think is is worth it in itself, even without the the discussions of what the PBS itself 

**Marius**
* So, quick question, like if you need to stake a max bits, then like can you add max bit 32 or what's the can you, can you have like, no, you can, you can stake, you need to stake the minimum amount of your validator, which currently is, 16. 

**Potuz**
* But anyways, you're gonna have to put in at least 32 so that, so that you're active. So you need to be an active validator, but you can beat for whatever your balance is. So that means if you have any balance which is infinite. Now on the beacon chain, you can bid up to that balance. And with Max B, you're going to be getting returns on your balance 2048. Gajendar has a question about diversifying the builder set. I think this is quite an interesting question. 
* So, for example if you are an application now and you have transactions and you want to internalize that MeV from those transactions, what do you do? 
* So that's that I think is a is a good client for this for this diagram. 
* And there's plenty of, applications like this that gather transactions that have their own sort of like mempool, uh so what they could do today is deal with a trusted agent. You send those transactions, you sell those transactions, for someone else to exploit them 
* With this, applications can be their own builders can hold those transactions and submit bids on the P2P layer, because anyways, eventually they're going to win a block if they have enough MeV for them to be exploited Actually, and they don't need latency. If they want latency, they can open an endpoint and advertise themselves as builders. But so but without having any infrastructure, they can enter the game as builders, trustlessly without having to deal with relays or anything like this. 
* So I do suspect that the builder set will be, immediately we're going to start seeing more bids from like home stakers and organizations like prismatic itself is going to start sending bids. I do not expect the winning bids to change with today we have three builders that make most of the blocks. They hold most of the transactions because they're private, and I doubt that this is going to change. I think private transactions from Binance are still going to go to the same builder, and that builder most probably is going to continue winning the blocks So at least it doesn't make it worse by itself 

**Gajinder**
* And one last question for us, which I think you are also discussing in the pre pre conf channel is how basically how compatible is EBS to Pre-con for will it help or will it make it difficult 

**Potuz**
* That's a very that's a very tough question. there are many different designs for pre confirmations. some of them are obviously incompatible the question is how do you, the question is how do you enforce this confirmations if you are trying to use, for example, inclusion lists on protocol to do Precomps, I see strong indication that this is not going to be compatible with with PBS. So if you're trying to have the pre confirm being the proposer and using inclusion list for that, most probably this is not going to be 
* Compatible with the PBS. If, on the other hand, you want to enforce the pre comfort to be the builder, which is much easier because the builder is much more centralized, then this is immediately compatible with the PBS. So there are different designs for how the pre confirmations are going to work. And some of them are compatible, some of them are not 

**Stokes**
* Cool. Thanks If there's nothing else on PBS for the moment, thank you again. Very exciting to see. And next we can move to a request from Julio, to discuss this PR. Do you want to give us an overview? 

# Removed totalDifficulty from Blockschema execution-apis#570 [31:31](https://youtu.be/tbxgYq8KmmM?t=1891)
**Giulio**
* Yes. So can you all hear me? By the way Yep. Okay. So, basically, I would like just to propose to remove the data difficulty field from the block schema in the JSON RPC So the reason for this is because we can now get rid of some pre-merge depth, and also because kind of asking around, quite somewhat extensively, I was not able to find anybody with meaningful use for that specific field, at least regarding Ethereum 
* Except for Etherscan or Etherscan, which just display it, as kind of just a, just a block field. and additionally, I also thought a little bit about it, but when but this field probably will become obsolete with AP four force because, well, you cannot reconstruct the index if you for full nodes. Right. Because you miss some, you probably miss some blocks. So you don't have the difficulty for the entire chain. So, the idea is that since it will likely get removed anyway at some point, I just,
* I just think like, why not do it now? And also, yes, we need to get rid of it internally because we want to do some optimizations around it. But that's kind of, another thing Yeah. So yeah, this is kind of my, the main reasoning. so I think that the clients can I mean, in my opinion, they can keep it internally if they really want to, but I just would like maybe to, to standardize not having it in the JSON RPC and yeah, that's pretty much it Thanks 

**Stokes**
* Anyone have any immediate feedback? Otherwise, take a look at the PR Removed totalDifficulty from Blockschema execution-apis#570

**Lightclient**
* Generally seems okay to me 

**Stokes**
* Cool. Okay, thanks 

# eth/69 [33:43](https://youtu.be/tbxgYq8KmmM?t=2023)
**Stokes**
* So next then we have a discussion around ETH 69. So Marius, would you like to give us an overview of that 

**Marius**
* Sure. Yeah. So, we're proposing ETH 69, which will drop some pretty much fields for example, we remove the total difficulty in the status message. we're removing the new block hashes and new block messages because we don't have block propagation on the execution layer anymore. And the big thing is, we're moving or we're modifying the way we encode receipts by dropping the bloomfilter the idea is right now, none of the clients are storing the bloomfilter. So every every receipt for every transaction for 2.5 billion transactions has this bloomfilter, which is a 256 byte field. and, no one like it can be regenerated from the locks. basically we just take the locks, put it into this bloomfilter. and so no one is actually storing it. 
* So whenever a new node sinks, the server that it sinks from has to or takes the, takes the receipts from database where it doesn't store the bloomfilter regenerates the Bloomfilter, sends the bloomfilter and the rest of the receipt over the wire, and the person syncing from it, receives it and re computes the receipt themselves, the bloomfilter themselves to verify the bloom filter, and then throws both bloom filters away, to store it into their database without the bloom filter all in all, this roughly means that the serving node will generate 530GB of data that will need to be sent over the network. 
* Fortunately, most of the bloom filters are kind of empty. So it compresses really well via snappy. the total amount of bandwidth is roughly 100GB. but these 500GB have to be, generated on the serving side. and then, yeah, regenerated on the receiving side. and we would just like to get rid of it. there is some something that we're currently discussing internally. we have these type receipts, and, uh the problem there is we are not storing the receipts in the database as type receipts. We're storing them as only the raw receipt. And so either we would need to pull them out of the database at the type and then send it over the network. Or we could send it over the network without the type. 
* And then the receiving node, which will get the type anyway from the transaction. would need to add the type from the transaction before verifying the receipt Yeah. This is currently an open question. Both of it, both schemes kind of work either sending the type or not sending the type we could ultimately also just decide to remove the type from the receipt, which would be the nicest. but it's very hard to do, because it's not backward compatible with old databases yeah. So I'm inviting everyone to yeah, engage in the discussions, whether we want to send the DT type or whether we don't want to send the DT type. and yeah, that's it thanks.

**Stokes**
* I don't know if there's any immediate feedback otherwise. Yeah. Marius, is there like a PR issue where we can continue the conversation 

**Marius**
* Not yet. I'm going to write up our or like, the discussions that we are having. On to the magician's thread, which is, linked in the EIP 

**Stokes**
* Okay, great 

**Marius**
* But it would be really nice to get rid of this because this is a lot of data, hundreds of gigabytes of data that we are, that nodes are sending right now, that they don't need to be sending. So a lot of bandwidth that we could, save users from.

**Stokes**
* Right. Yeah. I mean, that makes a lot of sense 

# PeerDAS in Pectra [39.37](https://youtu.be/tbxgYq8KmmM?t=2377)
**Stokes**
* Next up, we have an item to discuss. essentially rebasing PeerDAS in Pectra. and how that all fits together Let's see. Teku raised the point. Let's see if he's on the call 

**Dustin**
* Yep. 

**Stokes**
* Okay 

**Dustin**
* All right, so I'll start by saying the primary effect of this with with ELs, is that it's a testing consideration. So when, when looking at the next couple of Petra DB Netz 7702 and EOF are kind of penciled in as the default primary EIP's to test. And so and PeerDAS is another sizable EIP. And so one of the primary questions here is, is sequencing and how they interact. And therefore the salience to LS. And so PeerDAS in general is I mean I'll summarize very briefly. but this the details of it are actually not super relevant here. 
* It is an extension of, of blobs, in a way that they can be sampled. And so that unless you're proposing, you don't have to, kind of see every piece you can kind of reconstruct from, from partial data saves bandwidth and a lot of cases. All right. So, one can find extensive discussions of why people want it. So but the question here is so right now PeerDAS is still based on Deneb. the their specs, the, their devnet are based on Deneb. And this has been causing at least a couple of clients some issues because, yeah, it's it's it essentially it essentially makes it difficult to run without some kind of.
* Yeah. with certain client, architectures to, to run compatibly with, with current, so, with sort of with a deneb, with a current Deneb and the PeerDAS, quote unquote. Deneb. Right. So, so the proposal here is to rebase that to Electra, which is what it's going to be anyway. Right? That's when it's released over Electra. So the question is do people are what what concerns people might have here about. 
* So the the specific proposal is that we relatively near term rebase, PeerDAS on Electra and then but run the dev nets for the PeerDAS, deep nets without, actually using seven, 702 or EOF for a while because they're, they've proven kind of unstable in practice. 
* The devnets tend to have a dying tendency when when they're in there. and this the, the concern on the PeerDAS side is that it hinders PeerDAS testing. And we want to kind of avoid that. We want to PeerDAS testing to continue. So is this so this this is the question for people for from the EL side, does this seem like a are there concerns people have with this? does this seem like a reasonable approach 

**Stokes**
* So I think this yeah 

**Stokes**
* Marius 

**Marius**
* It sounds like it kind of sounds good to me. the only thing that I'm I worry about is because we have, like the idea behind pure is to have more data on chain. And how are we getting more data on chain, or is by sending blood transactions. And the block transactions right now are based on fuzzers. And these fuzzers accidentally hit some of the, some of the other pipes we could just send blob transactions, or we could modify the fuzzers in a way to send blob transactions without without, fast code so that they don't hit these edge cases. 
* Within like, I think the only, the only real concerns are EOF and maybe 7702 but because we're not it's, very unlikely to trigger EOF stuff. and it's even more unlikely to trigger 7702 stuff because we're not sending 7702 transactions. so I think it would be fine 

**Barnabas**
* Yeah. So the idea would be that PeerDAS devnet would still be, independent of the devnet, and we would just use an older version of the Fuzzer, something that is pre prog. So all the transactions that would show up would be only that specific transactions 

**Marius**
* But the thing is, RT fuzz can produce transactions that are like even the old versions can produce transactions that are now valid or that that are now triggering something I can modify it first to, sample transactions. I actually have some code to send block transactions that are just verify that the blob hashes are correct or something. so that do some small things with the blob hashes. So we verify that. But and we get a bunch of load on the network without triggering EVM execution at all
 
**Dustin**
* Is this configurable? Like can the can the fuzzer be told to sort of not do this? 

**Marius**
* Well, not right now, but I can implement it in like a few half an hour 

**Dustin**
* Okay. Right. Because  at some level the idea is to run to, to avoid. there was discussion in the chat. exactly. And it's absolutely warranted discussion whether it's 7702, which okay, maybe it's stabilized now, but it was a problem. And if EOF might be a problem in the future is essentially a way to avoid this to to run as Barnabas is kind of describing, kind of a a Deneb like version of, of Electra on the for as much as we can, except for, for PeerDAS itself. so that's it. The fuzzing introduced aspect seem eminently avoidable. Ideally 

**Barnabas**
* We can also just stop the in there. That way nobody can trigger transactions on new devnet. Only us 

**Paritosh**
* Yeah, just to clarify, probably just do that on PeerDAS side. Um yeah. Spectra regular can continue. So there'd be two devnet cycles as it is today. It's just a question of merging code bases or not 
* And since PeerDAS isn't necessarily a user focus like users don't have to interact with PeerDAS much. not having funds over there is not a big deal 

**Stokes**
* Yeah, that sounds like a good path forward Okay, cool Let's see So I think that was it on the agenda, I guess. Yeah. While we're here, then, I will call out, there's a Pectra interop testing call starting next Monday I think it's 2 p.m. UTC. Yep. That's right. So, yeah, keep that on your calendars and. Yeah, if there's anything else, we could move to open discussion. Otherwise, we can wrap up a little bit early today Right. So Perry's asking about 4444. anyone have any updates there 

**Piper Merriam**
* Has anyone looked into portal All of us over on the portal side are here and ready to answer questions, support client, new client implementations, that sort of thing if you have any questions, feel free to reach out 

**Nethermind**
* So Nethermind. Team is building portal integration. I don't have the latest update because I'm not really looking into it at the moment, but I think the update was that they were being able to connect and download blocks and maybe receipts. but I don't know the details. And, it was still a lot of work, like to optimize it and maybe refactor, etc., make more production ready. Maybe, maybe it was mostly happy path, but we were able to integrate something 

**Dustin**
* Nimbus has a portal client. fluffy, has for a while, and this is definitely our on our roadmap How we intend to build out the EL and all that. 

**Stokes**
* Okay, so it sounds like progress is underway and. Yeah, I mean, I think the main thing here is just to keep it on everyone's radars. I know there's a lot of things going on. but yeah, let's not forget about for 4444 
* Okay. Anything else? Otherwise we will close 

**Stokes**
* Okay. Sounds good. Then I'll see you all next time. Thanks for joining 

**Lightclient**
* Thank you.


-------------------------------------
### Attendees
* Stokes
* Pooja Ranjan
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



