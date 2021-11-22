
# Ethereum 2.0 Implementers Call 44 Notes

### Meeting Date/Time: Thursday July 23, 2020 at 14:00 UTC
### Meeting Duration:  1 hr
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/169)
### [Audio/Video of the meeting](https://youtu.be/MMNgoDYKvhQ)
### Moderator: Danny Ryan
### Notes: Pooja Ranjan

-----------------------------

# Contents

- [1. Testing and Release Updates](#1-testing-and-release-updates)   
- [2. Testnets](#2-testnets)   
- [3. Client Updates](#3-client-updates)   
   - [3.1 Lodestar](#31-lodestar)   
   - [3.2 Prysm](#32-prysm)   
   - [3.3 Teku](#33-teku)   
   - [3.4 Trinity](#34-trinity)   
   - [3.5 Nethermind](#35-nethermind)   
   - [3.6 Lighthouse](#36-lighthouse)   
   - [3.7 Nimbus](#37-nimbus)  
- [4. Research Updates](#4-research-updates)   
- [5. Networking](#5-networking)   
- [6. Spec Discussion](#6-spec-discussion)   
- [7. Open Discussion/Closing Remarks](#7-open-discussionclosing-remarks)   

-----------------------------


**Danny**: Agenda is on the chat, let's go and get started.

# 1. Testing and Release Updates

Video | [3:48](https://youtu.be/MMNgoDYKvhQ?t=228)
-|-

**Danny**: There are ongoing efforts by Lakshman and Proto,  to turn Rumor into chain tests. They can maybe give us an update on it. In terms of release, I’ve a pending release v0.12.2 and I’m working on getting it out today. There are very few minor PRs,  and nothing crazy, backward compatible, generally some clarifications and fixes primarily in the gossip conditions section of the P2P spec, we’re going to release that. Apparently, in v0.12.1, there were, 4 attestors, slashing tests that were not published and I think funny enough these were found in fuzzing, I think Nimbus maybe had the issue in index out of bound error or something. We do have tests for this and will be released in v0.12.2.

Proto and Lakshman do you want to give any update on your end?

**Proto**: For chain testing, we marked testnet tooling, deposit tooling. Spinning up or automating the deploymento of (?) testnet. Continue teh chain testing efforts.

**Lakshman**: Just a small update from me,  kind of prompted by there was a recent case where it was found it was like a DoS vector in Gossip if you propose blockset were not the descendants of a known by finalized block or something like. I've been kind of deep dive on other possible holes in Gossip validation that we can use to prevent other DoS vectors. I’ll have that put together in some issue soon. 

**Danny**: Cool! Thank you, Lakshman!


Video | [6:28](https://youtu.be/MMNgoDYKvhQ?t=388)
-|-

**Danny**:  Moving on to **testnets**. As you've hopefully seen there are  3 very small attacknets up and they're all single client there are 4 nodes each, they are 128 validators on each network.There's a repo that we posted that kind of shows the rules, bounties and things. I know Jhonny has been getting his hands dirty and hopefully others on this call or people listening to call might be interested. The plan is to ramp these up over the coming weeks to make them larger and put some bounties out there. White hat hackers please, come brake these. 

Okay any questions on the attack nets as they stand now or maybe where they’re going? 

**Proto**: Maybe something to emphasize that's right now it's your best chance to try and find easy test vectors. It is much harder to put testnet down with shared clients. 
**Danny**: Yeah,  absolutely. To be quite frank to anyone listening is call DoSing is viable especially in a 4 node network and probably cheaper than bounty, so someone should do it.

# 2. Testnets

Video | [8:15](https://youtu.be/MMNgoDYKvhQ?t=495)
-|-

**Danny**: Okay moving, Coindesk announced this yesterday. Afri do you want to talk about the testnet?

Afri: I have got a plan to talk about Altona and the Medalla.

## Altona

* After returning for vacation found Altona network in perfect conditions, 
* No major hiccups, liveliness pretty good.
* Some slashing events were being investigated but I didn’t follow too closely.
* Released Client benchmark last week, profiled all Genesis clients - LH, Prysm, Teku and Nimbus and compared there high-level performance metrics and published a small report
* The stability on Altona lead us to conclude that we want to do a very similar testnet but a public launch
* This was prepared last week and someone suggested calling it Medalla

## Medalla

* Targets v0.12.2 spec that is close to release
* Does not contain any breaking changes as far as we know, so we’re good to go to have client release for this very soon
* Spec is on Goerli Github, it contains mainnet spec. We will have a public launch. 
Did you publish a blog on how people get onboarded, Danny?

**Danny**: Yes, I just put out a [blog](https://ethresear.ch/t/ethereum-2-0-client-metrics-07-2020/7699) this morning. That is linked to some of the relevant stuff  and also linked to at least the 4 clients that we know will have genesis validators and encourage people to try them out. We also have an imminent release of the associated **Validator Launchpad**. It’s like an educational deposit UI that's expected to go live by Monday which if people are not familiar with this process and haven't tried out testnets befor that should be like a good portal to get started.

**Afri**: Min genesis time for Medalla is Aug 4, 1:00 PM  UTC in case we’ve enough deposit (needs 16000 deposits) otherwise it will happen after 48 hours of the last deposit.

**Danny**: We will know that  Sunday at 1 p.m. UTC if Tuesday at 1 pm UTC will be met. 

**Dankrad**: Maybe one input for this testnet, it would be great if we try to track 100% of the slashings. Bsically open an issue for each slashing that happens and make sure that we know exactly what happened because I feel like when we launched this is like a catastrophic failure for those who actually staked. So if we find these issues now we can just sweep them under the carpet.

**Danny**: Yeah certainly agree, I'm glad you brought it up on Altona, the ones that were unknown there. Any suggestion?

**Proto**: Another Eth2 client’s organization repository. I believe he already have 1 with UX you can make issues for (?)

**Danny**: Sounds good to me.

**Ivan**: It’d be great to have slashing recorded just to make sure that there are detected properly.

**Danny**:  yes 

**Dankrad**: Maybe in the repo we could have a table where everyone records which validator they run so that makes it easier to contact them and ask them hey what happens, can you have a look at the locks? 

**Danny**: I’ll open up a multiclient repo. thank you Dankrad. That would let people know when there is a slashing but that is very much something that we would like to avoid it on the mainnet. 
I imagine 99% going to be the UX failures or potentially education failures, not running the keys at multiple places thinking that’s a good idea which is also maybe a UX failure. 

**Dankrad**: Could clients detect that? Could your clients see an attestation in my name but my local store doesn't say that I signed it, I should probably inform the user of that other than one.  

**Mamy**: For slashing protection, you need to keep a local database of what you signed, so you see something signed with your public key but it's not local, it means that either you move your computer someone is using the same.

**Dankrad**: Exactly, but I expect that you may want to run it on another computer or you didn't notice that they made a copy of it actually or so I expect that that will be the reason for most slashing realistically. So,  if the client automatically detects that's like it’s just a test to scan say like check the latest at the station and see if that's the same as your local store says and just solve basically.

**Danny**: You could have added a validator client query. Given these are the attestations athat I know about if your query on node and ask if there's an unknown which could be a red flag.

**Ivan**: We kind of support that by connecting the validator client, the slasher. Since the slasher maintains a whole database of everything made and everything it sees but yeah that be a lot extra.

**Mammy**: Also there might be a raised condition, let’s say you have two clients and the try to vote booth and try not to work each other and then both deactivate themselves because they realize late that they both looking for the same attestation.

**Dankrad**: Right, this protection is not perfect ofcourse, I am just saying it could probably catch most cases. It doesn't catch the case that you accidentally stopped both at the same time.

**Danny**: I think this is probably a good pointer for normal beginner it’s going to be a very expensive query. There is specialized slashers being written which Prysm has one, LH is looking at one which creates an index like a more index database of the attestations but at that point also, at least for now pretty expensive operation around. 

**Dankrad**: Doesn’t the beacon node know the latest attestation that each validator signed? That maybe like 80-20 to look at that and see if that's the same as your store says. 

**Danny**: Yeah, you’re right. That could be like a **validator sanity check**, start-up, end-point which could I think to help with a lot of the common errors.
The next steps could be to think a little bit more about it and propose an endpoint to eth2.0-api repo.

**Dankrad**: Okay, I’ll make an issue. 

**Danny**: Thank you!

**Proto**: When we send a reference to the previous attestation along with the attestation you signed?

**Danny**: Meaning that then the node sanity checks that the previous attestation is valid? 

**Dankrad**: I didn't know it and it doesn't just need to check that that previous attestation  exists that needs to check that that was the last attestation that has from that validator. 

**proto**: Exactly, try an make an effort for the next trial just make it standards just to check these things?

**Jacek**: Does it need API technically in the Beacon node? The beacon node receives all sort of traffics. If there are two clients running or the two things on the network and while running one of these receives notification that a particular validator node is connected to you. As soon as a validator client creates the attestation, we will try to (?) 

**Danny**: Yeah I mean, a response from the Beacon node could be like a warning and a default reject something that was a protection measure.

**Jacek**: That would catch probably 80% running, there will be attesting. 

**Dankrad**: Once they are both on the network, it’s too late. Then you’re dead except if they happen to be exactly the same attestation, in which case you would not attest.  

 **Jacek**: Yeah you might get it to the network before the validator 

**Dankrad**: I guess what I am saying that if you didn’t start them exactly at the same time and if you’ve one running, you didn’t remember that it’s running and you think I'm going to start my node now and then that node will detect hey there wasn’t an attestation 6 minutes ago and it wasn’t me, so I'm better going to shut down, that's I guess what I'm suggesting.

**Danny**:  There’s like beginner rejecting if it seemed something for that thought already, seems like in most cases you might not unless there's like timing issues between your local times. 

**Dankrad**: I think that doesn’t matter, that protection can totally on Beacon node. 
Like in this case, since the validator node currently doesn't follow the Beacon chain, there's no difference in security so it could be the Beacon node doing that tech.

**Danny**: Lets take this to an issue in the API repo if that make sense. Okay, other testnet things, Afri do you have anything else?

**Afri**: No, not that I am aware of, I am excited.

**Danny**: Yeah, that is super exciting. Anything else, any other questions or comments?

**Mammy**: Let’s see expectation on client teams in terms of the number of Genesis validator, there was some discussion but I didn't see a conclusion.

**Danny**:  We were thinking on those 4 clients 1024 on each which is end up being significantly less than ⅓ of the validator and maybe leaving a chunk for some of EF and Afri to run still equaling less than one-third of the assumed 16k (which may very well be more) so somewhere between probably 1/3 and 1/6 of the Genesis validators. Does that seem reasonable to everyone? a nice background but not able to finalize really do much other than just be a strong percentage?

**Ben**:  sounds like a plan 

**Danny**: So, 4096 again that'll be if only minimum Genesis validators are hit, that will be 25% of the validators. and then EF and Afri will fill in the gap up to about 30% and other than that it might be smaller because we can very well have 20-30k validators. 

Okay other testnet things?


# 3. Client Updates

Video | [24:10](https://youtu.be/MMNgoDYKvhQ?t=1450)
-|-

**Danny**: Moving on to client update. Let’s start with Lodestar.

## 3.1 Lodestar

**Cayman**: 
* We’re finished with Gossip sub 1.1
* Writing a few more tests to bring inline with testing with Go implementation,
* should be releasing this with latest version of JS lib P2P 0.29 in the next few weeks,
* adding to our API, 
* we have minimal eth2 stats support.
* Trying to make sure the node is stable and it can transition between the initial sync and the regular sync.
* All hands on deck, trying to get ready for the testnet because 
* We’d like to be validating in some part but we also don’t want to break the testnet. 
* so we will make a call when it gets closer or whether or not we're going to be validating or worst case we can just spin up some client’s nodes. 

**Danny**: Yeah, we’re expecting to run some Lodestar node. Okay, Prysm?

## 3.2 Prysm

**Raul**: At Prysm we are working on
* accounts revamp, basically restructuring everything about how key management work,
* Making sure we are compliant with EIP standards in the derived wallets, 
* We’ve also finished up remote signing wallet, so people can basically connect to a remote signing server that’s one of the most requested functionalities in Prysm.
* Focused on Key management and User experience; so we've been focusing a lot of making it easier to use and making sure that it's up to standard. 
* Working a lot on fuzzing and finding bugs, using a tool **Cluster bugs**, found a lot of interesting bugs in the codebase and been fixing on that. 
* Been working a lot on Networking improvements, people don’t want to expect a lot of peers or any weird situation.
* We’re also confident about the new testnet and that’s where we are today. 

**Danny**: Great, and how does the Launchpad integration like if I get some keys on the launchpad, can I easily move it into the Prysm at this point?

**Raul**: You should be able to, we’ve to try it out. We do implemented the same Keystore standards so just need to make sure that format is all match up properly and nothing is weird. It’s updated, so we’d be able to try it today?

**Danny**: So yes Carl has a version that he's putting out for Medalla that should be up very soon and maybe helping you with the link.

**Raul**: Cool!

**Carl**: Yeah, I’ll send you a direct link. 


## 3.3 Teku

**Anton**: From Teku side, 
* Working on memory consumption, 
* JVM heap is small and stable, 
* Testing experience has some native memory leaks; suspect is RocksDB library. Currently, trying different options to eliminate these leaks. 
* A lot of peer mgmt improvement
* Some Sybil resistant in maintaining a minimum number of peers management
* Almost complete synchronization of Rust library integration
* It showing the preliminary that we will improves block import speed around 3 times. 
* Teku security assessment RFP is out. Closing date is August 3rd.

**Danny**: Great! Thank you, Anton!

## 3.4 Trinity

**Grant**: Right now 
* our main goal is to get to the Beacon node sync to Altona’s head. 
* Earlier last week we have finished up some interop work for connecting to the Altona testnet.
* Alex finished up Forkchoice refactor
* as of right now we're just trying to speed things up
* Alex added some logging, Monday, or Tuesday or something and found that we're Syncing - 0.2 slots per sec. After a few days just stopped optimizing thing,  bringing stuff from that to Fastback and also speeding up database operations were syncing at 13 slots /sec
* We've still a few issues that we have to work out at around like Epoch 256 but yeah 
* nothing too serious and hopefully we can get that fixed up pretty soon and then I'll be syncing to the head within maybe an hour or two.

**Danny**: On Epoch 256, was there a consensus error? 

**Grant**: it's a mismatch in the state in the next block. 

**Danny**: If you're passing over a consensus test, and you found a consensus error with your client codebase that would potentially lead to a hole in our test vectors, so you can document that case and that would be really helpful for people.

**Grant**: Okay as of right now I'm not running the state transition for all the dependent functions through those tasks so that’s probably not the case.

**Danny**: But you or anyone does that type of case, certainly report it. Thank you Grant!


## 3.5 Nethermind

**Danny**: Okay, do we have anyone from Nethermind?

## 3.6 Lighthouse 

**Age**: Hey everyone! Updates from us:
* New team member on board and his name is Benedict.
* Been working on Stability improvement. Same like Prysm, working on improving the key management system 
* Looking into some of the ATT inclusion in Altona, to make sure that all the attestation is getting included in block and finding edge case issues.
* Johnny found panicking in Disc V5, props to Johnny, which we fixed.
* Security hardening network infrastructure. 
* Preparing for Medalla testnet.

**Danny**: Great thank you! I saw that there is a Launchpad specific PR is still up, is that coming in the pipeline soon.

**Age**: Yeah, we should have that sorted before the testnet is ready.

**Danny**: Great thank you! Nimbus?

## 3.7 Nimbus

**Mamy**: 
* Started audit, 3 auditors - ConsenSys Diligence, Trail of Bits, NCC.
* Separated in 3 phases, 2 weeks audits, 2-3 weeks of  fixes
    * Networking
    * Beacon Core
    * Validator core
* Working on Beacon core on reducing memory usage, meaning smarter caching
* Working on sync speed, not satisfactory, but priority
* Nimbus on Altona - The main issue we have is ATT is not properly propagated, an issue on Gossip, working on this.
* Several improvement like better handling of state connections, Disc V 5 fixes. 
* On Beacon node  and validator split, we had several deposits but struggling with Finalization issue that’s fixed now
* Cryptography related to EIP2333 for keys, we can handle deposit from Ethereum launch pad that will be released soon. 
* Reviewed BLS backend.
* Blst is wrapped but not enabled. 
* Updated Milagro
* New blog post on running own validator

**Danny**: Your mike had some crazy static so maybe in the future, you’ll probably want to look into it.

**Mamy**: I think of same as one from the past two years so it's probably just my t-shirt.

**Dany**: okay I think we got everyone, right?

# 4. Research Updates

Video | [37:30](https://youtu.be/MMNgoDYKvhQ?t=2250)
-|-

**Dany**: moving on to research update anybody have anything you want to go to started with?

## TXRX

**Joseph**: TXRX are 

* working on attacknet stuff and just wanted to reiterate what you were saying earlier. I think if we're the only people working on this then you know I don't think we're going to have the level of security long-term. Right now the attacknets are kind of like the softest pieces of Lib P2P because they're really not able to produce attestations because we’re not validating on it. So yeah everybody likes to put a little bit of resource towards attacking the attacknets because if we don't they're not going to be secure long-term.
* Mikhail and G. Phase1 clients are connecting to Eth1 is pretty exciting news.

 **Danny**: Yeah, absolutely. If you all are going to have like hacker friends that might be interested in this kind of stuff, knock on their door.  Cool, Other research updates?
 
**Leo**: I can go, just an update on Snappy compression from last meeting we were have to do test from Ethereum 1 block to Ethereum 2 blocks, we did that. We downloaded 19 blocks  from Altona testnet and run test and time for each block, always obtaining the same result from each block. Ofcourse the compression time changes slightly. Overall we get a compression ratio of 1.6 more or less and a compression speed is about 911 megabytes per second. This is on  Intel i5 with four course. 

In comparison to Eth1 I presented previously, the compression ratio is lower, compressor pressure of Eth1  was 1.8 not with that 1.6 for Eth2 blocks. But on the other side the compression speed is higher, we have 900 vs 500 for Eth1 blocks. 

We also compared these results with standard benchmarks it came with a source code,  just to make sure that you know the numbers we were in line with the standard benchmark. We got about 789 megabytes per second speed of compression speed for the standard benchmark.

So the 900 MegaBytes/s that we are obtaining for the Eth2 is quite close to it. But these were from block to block. Some blocks get lower speed if any of the data. The lowest we had was so 476 Megabytes /second. The highest we had was about the 1255 Megabytes per second. These are the variance between blocks.

**Danny**: Do you know the compression ratio on the standard Benchmark data set?

**Leo**:  I don't have the numbers right now but  I can put it on the discord. I will put a spreadsheet link in  the chat that you can all look at the at the old address of all the data, in case somebody wants to check on them. 
Another thing that I wanted to mention is that we started validator node on the Altona network. We’re running the lighthouse client on a Raspberry Pi 4. We will be testing also for all the clients. We are trying to test different clients on the same node , same network to see if we see differences in symptoms of message received attestation etc. Sharing the link in the chat.

**Danny**: Thank you. My suspicions on the Eth1 blocks being more compressible is probably the 256 bit machine and all of the zeros that are often the most values, I don't know.

**Leo**: Yup, that makes sense.
 
**Danny**: Cool! Other research updates? 

# 5. Networking

Video | [43:15](https://youtu.be/MMNgoDYKvhQ?t=2595)
-|-

**Danny**: Like I said the v0.12.2 spec is primarily a minor modification of the networking spec. I’m  including some updates to recommending Gossip sub, check that out that will be out today.

**Proto**: In the immediate release to the mark of accepting changes that we're looking into any particular feature that differs in clients. Such as signature verification, and other related fields (origin, seq number, public key) - clients currently vary in their handling of all these things, but they are not used in the spec.
If you’re working on Gossip sub, you hopefully want to look into that [PR](https://github.com/libp2p/go-libp2p-pubsub/pull/359).

**Danny**: The TL;DR on that is that origin signature in Gossip Sub were not using them and so they're kind of all over the place and how implementation handle us not using them. better we're seeking to just have like a enable disabled flag and add (?) on any sort of edge cases. But if you want to dig deeper then probably look into the PR that we share on the chat. Thanks Proto!
Other networking things?

# 6. Spec Discussion

Video | [46:10](https://youtu.be/MMNgoDYKvhQ?t=2770)
-|-

**Danny**: Open spec discussion and just general open discussion anything else anyone else today?

(No discussion)

# 7. Open Discussion/Closing Remarks

Video | [46:30](https://youtu.be/MMNgoDYKvhQ?t=2780)
-|-

**Vitalik**: Do we want to talk about when and how we might wants to kick-start phase 1 and development or implementation?

**Danny**: Yeah, why not. My understanding right now is that some clients have done a little bit of due diligence on the spec, some are still looking at it, some are doing some prototypes. There’s a prototype in JAVA, that actually has a full simulator and Terrence has done some work on implementing the Phase1 spec and pushback into the specs a bit. And then my other understanding of the problem is that the heavier than engineering resources are primarily on shipping phase 0.  I think at some point in the next couple of months, that needs to change and resources probably need to begin to ship. But beyond that Vitalik, what are your particular thoughts here. 

**Vitalik**: Might it make sense that one of the client teams to kind of start pushing ahead into phase one earlier and especially the one that's whose clients are more or less ready for mainnet development?

**Terence**: Well my feedback is to have some sort of annotated phase 1 spec starting early because that just makes it easier to onboard new developers. On discord we have people that expressed interest in working on Phase1 stuff in Prysm. But it’s hard to onboard them without some annotated spec.  

**Joseph**: I'm sorry we are working on a Phase1 client. We’re  taking this back and transpiling it and then we're interfacing with that. we're only calling it a simulator because we're not going to following the slot tech that's expected. I'll drop a link in the chat.

**Danny**:  Yeah good point, Terence. I can do a quick version of Phase 0 for humans, just  like the high level. But there also going to be an effort on more annotation direction of the spec. We will be working more on writing specs in the coming weeks. 

**Hsiao**: I am currently working on some Phase 1 spec, I have some notes but I personally feel the spec itself could be simplified belore more teams to join. I will like to have a write up after some more simplification be done and that would be more proper for more teams to join 

**Danny**: Anything else on this discussion? Let’s make a note that in the coming calls, we will make it an explicit item to discuss on Phase 1 developments.

**Vitalik**: I’ve not forgotten my own promise to make a imitated phase 0 spec at some point. So, I’ll get to phase 1 after that’s done. Now that my couple of other articles have been pushed out yesterday, I can get to that very soon. 

**Danny**: Great!

**Ben**: Oh man! I get to finish mine before you get to it Vitalik!

**Vitalik**: The more the merrier!

**Hsiao**: BTW, the next release will be coming in maybe this week. The phase 1 test vector probably will be included in the next next release to help the things to fast but maybe we could just have a quick including only test in  next release.

**Danny**: Yeah I agree, as soon as test generation PR is merged, I will create a separate branch in Eth 0 repo for anyone who wants to take a look at. I will drop that in Discord once that is available. 

**Hsiao**: BTW, thanks to Terence and Mikhail to help doing the Phase 1 PRs.

**Danny**: Yeah absolutely and both have made substantial contributions to the spec itself.

Okay anything else today before we close? we will spend the next two weeks from now which will likely be two days after the launch of Medella. Take Care thank you very excited for the testnet!




------

# Annex

## Zoom Chat 

* **Terence**: https://ethresear.ch/t/ethereum-2-0-client-metrics-07-2020/7699
* Or we can record slashings here: https://github.com/goerli/medalla Either repo works
* Leo BSC: https://docs.google.com/spreadsheets/d/1SoXvmPfm1BRVcdDm7CuwaWDjxp5a3NzGMBLViQjBNqA/edit?usp=sharing
* https://altona.beaconcha.in/validator/a2b60b956869fd5dfe9874546b3cc4bc2ca42bcc3b9c48c8473b7881c4e94b4a57917b07bf0b22117c90daf2f59c2dde#overview
* Proto: https://github.com/libp2p/go-libp2p-pubsub/pull/359
* Joseph: https://github.com/txrx-research/teku/branches
* Terence: latest phase1 work on Prysm https://github.com/terencechain/prysm-phase1

## Attendees

* Ansgar D.
* Aditya Asgaonkar
* Afr Schoe
* Anton N.
* Age Manning
* Alex Stokes
* Ben Edgington
* Carl Beekhuizen
* Cayman
* Danny Ryan
* Dankrad
* Grant Wuerker
* Hsiao-Wei Wang
* Ivan M (Prysm)
* Jacek Sieka
* Jonathan Rhea
* Joseph Delong
* Leo BSC
* Lakshman Sankar
* Mamy
* Marin P.
* Matt Garnett
* Nishant 
* Pooja Ranjan
* Protolambda
* Raul Jordan
* Shay
* Sacha Saint-Leger
* Terence (prysmatic)
* Vitalik B.
* Zahary K.

## Next Meeting Date/Time

Thursday, Aug 06, 2020.
