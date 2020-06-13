# All Core Devs Meeting 89 Notes
### Meeting Date/Time:  Friday 12 June 2020, 14:00 UTC
### Meeting Duration: ~1 hr
### [GitHub Agenda](https://github.com/ethereum/pm/issues/180)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=c_JmTqeQkU4&feature=youtu.be)
### Moderator: Hudson Jameson
### Notes: Pooja Ranjan

---

# Summary

## EIP Status

EIP | Status
--|--
2315, 2537 | Accepted for Berlin and YOLOv1 testnet|
2565 | EFI, proposed for Berlin, currently not included in YOLO|
2046 | Proposed for Berlin. Under Discussion to evaluate for adding to Yolo|

## Decisions Made

Decision Item | Description
--|--
**89.1** | For the testing static call in client, James will follow up with Martin and the different teams over the next week and then can be discussed in the next core devs call or on the Gitter and then maybe decision to include it in the Yolo will be made.
**89.2** | EIP-2565 moving to EFI, officially.
**89.3** | Alex S. and team to look into another security audit for Eth 2.0 Deposit Proxy Contract that utilizes EIP-2537. Anyone interested, reach out to Hudson or Alex S. 

## Actions Required

Action Item | Description
--|--
**89.1** | Kelly will share the test vectors with Tomasz and others on Gitter so they can run them.

---

# Agenda

- [1. Berlin EIPs - Integration Updates](#1-berlin-eips---integration-updates)
- [2. Call to discuss precompile repricing (EIP-2046: Reduced gas cost for static calls made to precompiles & EIP 2666: Repricing of precompiles and Keccak256 function)](#2-call-to-discuss-precompile-repricing-eip-2046-reduced-gas-cost-for-static-calls-made-to-precompiles--eip-2666-repricing-of-precompiles-and-keccak256-function)
- [3. YOLO Testnet Update](#3-yolo-testnet-update)
- [4. Eligible for Inclusion (EFI) EIP Review](#4-eligible-for-inclusion-efi-eip-review)
- [5. Update on Eth 2.0 Deposit Proxy Contract that utilizes EIP-2537](#5-update-on-eth-20-deposit-proxy-contract-that-utilizes-eip-2537)
- [6. Account Abstraction Research Update](#6-account-abstraction-research-update)
- [7. ethereum/PM calendar](#7-ethereumpm-calendar)
- [8. Testing Updates](#8-testing-updates)
- [9. Review Previous Decisions and Action Items](#9-review-previous-decisions-and-action-items)

**Hudson**: Hi everyone and welcome to Ethereum Core Dev meeting number 89. I'm your host Hudson and we're going to jump into the first agenda item which is the Berlin EIPs integration update. The first link is clickable and brings you to a Google spreadsheet that shows some updates from different client teams and what's the latest on there. So I'll pass it over to James who can give it update on that.

# 1. Berlin EIPs - Integration Updates

Video | [04:07](https://youtu.be/c_JmTqeQkU4?t=249) 
-|-

**Hudson**: Hi everyone and welcome to Ethereum Core Dev meeting number 89. I'm your host Hudson and we're going to jump into the first agenda item which is the Berlin EIPs integration update. The first link is clickable and brings you to a [Google spreadsheet](https://docs.google.com/spreadsheets/d/1BomvS0hjc88eTfx1b8Ufa6KYS3vMEb2c8TQ5HJWx2lc/edit#gid=0) that shows some updates from different client teams and what's the latest on there. So I'll pass it over to James who can give it update on that.

**James**:  So the update there is actually the Yolo network is syncing for most clients. Can you give an update on 2315 and 2537 for Nethermind.

**Tomasz**: It’s not merged, WIP. 

**James**: Can you give updates on 2315 and 2537?

**Tomasz**: WIP.

**James**: Besu merged in syncing on Yolo.

**Tim**: Yes.

**James**: Open Ethereum as well. 

**Artem**: Yes.

**James**: Geth? 

**Martin**: Yeah.

**James**: Obviously. 
**Hudson**: Trinity can give an update.  yeah I think I would be Jason if you're able to talk.

**Jason**:  I have been working on this project. It’s WIP. 

**James**: They are syncing, there will be some updates on that we can talk about it later.

**Hudson**: Item 3 is Yolo testnet update, so we can talk about how it actually didn't live once and a couple of other things. 

# 2. Call to discuss precompile repricing ([EIP-2046: Reduced gas cost for static calls made to precompiles](https://ethereum-magicians.org/t/eip-2046-reduced-gas-cost-for-static-calls-made-to-precompiles/3291) & [EIP 2666: Repricing of precompiles and Keccak256 function](https://github.com/ethereum/EIPs/pull/2666))
Video | [07:35](https://youtu.be/c_JmTqeQkU4?t=455)
-|-

**Hudson**: The second agenda item there was a call to discuss precompile repricing specifically the EIPs 2046 and 2666. I think that meeting happened and James I think you organize that if you want to talk a little about it or passed it over to someone to give a update.

**James**:  I did. Did Alex want to give an update on that?

**Alex V.**: I can  make a short summary of that.
*  A proposal to reprice static call to exactly 0 gas was **rejected**. I posted a GitHub issue link to the latest research like how we should actually reprice,  based on benchmark from existing clients.
* Martin made a test for Geth and I have run test for OpenEthereum. It looks like for geth, Static call should be priced around 40 and for open ethereum, it can be made around 30, most likely.
* It still doesn't take off 2666 from the list and 
* also it would be necessary to change prices in case if 2046 is accepted, even for some non zero value like 40.
It is a research in progress. 
 
**Martin**: Yes and **another thing that we agreed upon is**
*  to try to assemble around a set of good test vectors for benchmarking so that each client can try out the set of Benchmark vectors and see which ones perform the worst in their implementation and then do their analysis base from the worst-performing.
* Could we handle the proposed lowering the prices of these vectors and 
* instead of trying to compare every clients every clients just that each client gives a thumbs-up or thumbs-down basically if they can manage this supposed repricing. And I'm talking about the actual pre-compiles and not the threshold to the static call precompiles but the actual precompiles. 

* Alex V. has been collecting these vectors, I made a PR for Json format.
I think they're like four or five different precompiles with vectors and I think Vlasov is still working on. I have some other vectores for the remaining precompile. 
Next step would be client teams do their own benchmarking and tell us the status.

**Tim**: For Besu, at least that would be super valuable like we just didn't have the bandwidth to set up the benchmarks to do something like this. So, if something is up with you to work to make base you compatible with it and run it and report back but having someone else kind of setup the infrastructure is really a big help. 

**Martin**: It's not actually setting up an infrastructure because having both Rust, and go and Nethermind guys have. The language has a built-in benchmarking capabilities. 

**Tim**: Got it, thanks!

**Axic**:  I also think on the call **we kind of agreed that for Berlin, we target the static call repricing and maybe we don't focus on repricing every precompile and just get this one change in and then we should have all this process setup to do the repricing in further hardforks**. 

**James**:  yeah I remember it being it focused on static call and then identify any outliers through testing that also need to be addressed through that change through the static call change and then target those for being in Berlin and afterwards addressing other precompiles that could be repriced. This is kind of an open question at what point would we consider making a change for  a version of YOLO net to include down to 40 or 50 or something? 

**Martin**: I personally don't see any real problem with doing it pretty shortly because it's kind of a trivial change but maybe we should let Yolo live for a little while longer so people can actually interact with it. 

**James**: Do other clients have thoughts on them?

**Tomsaz**: I am executing the benchmarks for the static call repricing so I'll be able to most likely tell you the results today.

**James**:  Okay so we let's make it a point to talk in next all core devs call about it and decide.
Besu, you have any thoughts on that I don't know is there benchmarking in Java's or something like that becomes easy in the same way ?

**Rai**: Are you talking about benchmarking for the testing static call or the time per gas thing?

**James**: **For the testing static call in your client like the real cost of static call 
 I'll follow up with the different teams about this over the next week and then we can talk about it in the next core devs on Gitter and then maybe next week we can include it in the Yolo.**

**Rai**: done the benchmarking.

**James**: Great! I will still need to get you that call, I'll get that to you, today.

**Rai**:  Thank you!

**James**:  He was a little bit quiet so I'll repeat just what he said for everybody else that the call that they merged the tool recently for doing this kind of profiling and so they'll be able to get something pretty soon.
Anyways, that's good for that, Hudson, unless anyone has all the other updates.

**Hudson**: Sounds good to me. Thanks everyone.

## Decision Items
-**89.1**- For the testing static call in client James will follow up with the different teams over the next week and then can be discussed in the next core devs call or on the Gitter and then maybe decision to include it in the Yolo will be made.

# 3. YOLO Testnet Update
Video | [16:16](https://youtu.be/c_JmTqeQkU4?t=976)
-|-

The next one is the Yolo testnet update. 

**James**: One more thing. I'm happy to do more of these EIP specific calls, so  when someone has something that they think would fit for that please reach out to me and I can keep making those as we need them. I really like the format and it helped progressed EIP very well so we should do that. We should tend to do that as often as make sense.

**Hudson**: Yeah I agree. I think that's great that you're willing to step up on that and it helps us to better time management for these core devs call so we're not spending a large amount of time discussing specific EIPs all the time.

 Okay next up is the Yolo test that update. I don't know if we had a call since we launched it so if someone could give a brief overview of how the launch went any problems we've run into and where we're at right now with it.

 **Peter**: Yes. We launched Yolo on Monday. There have been a few problems. One of the problems was me trying to be over laziness and  just pushed every single component on the single machine. Martin set up the machine and obviously didn't notice the hard drive size. After about 3 days the whole thing blew up because it went out of disk.  We did fix that since then however we've seen something quirky. Mario started pushing lot of transactions, BLS test transactions,  junk transactions.
The interesting thing that happened was the signer went off on it’s own little world. The signer is creating blocks and not even geth is accepting the blocks created by the geth signer. So something was really quirky there. Originally, I had a hunch that somehow maybe something got corrupted, although it should really not happen. Anyway I saved the state of the signer for debugging and I nuked it and started resynced it and start signing again and it took about six blocks until it blew up again. YOLO again the signer in its own little world and no other node in the network is accepted. That's kind of means that there is some really quirky fault in geth, in the geth signing. The geth signer does something that is not accepted by the normal block processing. so I need to check that. Apart from that, may be a Martin has a bit more details. As far as I know Mario has managed to actually, he was running both an open Ethereum node and the besu node or Nethermind. I am not sure which one of the two on the Yolo testnet. I think both of them forked off at an earlier point so essentially we manage with three clients we managed to do a four-way split up the Yolo network. 

**Alex**: OE actually synced to 244-2154 block, to the same one as geth client has stopped syncing with his own world signer. OE and Geth broke off from the master at the same point. 

**Peter**: Okay cool!

**Alex**: I should also tell here that this behaviour is not due to BLS pre-compile, because after Mario has dumped all the test transactions to the smart contract. I know it’s a part of the contract, I deployed it. We both tested on different combinations and results, Geth using assembly engine and counter part using Rust implementation and there were no diversions in the results. It can not be due to BLS pre-compile. 

**Peter**: Yes, ofcourse! My point wasn’t that it was the BLS precompile who is at fault here. It was just a general statement that this thing happened and we don’t really know why and what’s the cause of it. 
Sorry I don't know about the other folks, maybe Martin has a bit more information about the other clients diverged, if they diverged, maybe it’s the same issue. 

**Martin**: I don’t have more information now. 

**Karim**: For Besu, it was the same. We stopped at the same block of Geth. 

**Peter**: Okay, maybe just our messages were different then. That is the status of Yolo. It works, but for some reason the signer is likes to screw everybody else, and I’ve no idea why. Because, this is not something that we’ve ever seen before. 

**Hudson**: Okay! Thanks for the update, Peter and everybody else. Anybody has anything else on Yolo or questions. 

**James**: Just an observation from watching discussions around Yolo. I’ve seen it’s been really helpful driving some more development conversations, just watching out core devs gitter and people talking about it so I'd say it is something we should consider doing more and possibly consider adding surely officially to the process of for getting things to mainnet.  Things just have moved a lot smoother since.

**Tim**:  Two things I want to add, one just to understand the signer issue, Peter, does that mean once you you fix the bug in the signer, we will have to restart YOLO or you just have to swap, the signer?

**Peter**: Maybe you don’t have to restart Yolo. If the signer just discards a few blocks that the signer created, and nobody accepts, those just go to the garbage can and otherwise the network will go forward. 

**Karim**: yes I can see Besu,  it's okay without restarting.

**Hudson**: Okay, anybody else? 

**Tim**: Yes, James second point about multiple ephemeral testnet, I think this is something we'll probably be looking at 1559 as well. Once we get more settled on this a little bit, they get this launch basically as soon as possible to get some feedback on it because it seems like a good way to get people actually using and see what breaks in a live environment.

**Hudson**:  I have a question 1559 real quick cuz it's not on the agenda but Tim or do you or anyone else know if there's like anybody working on a  mathematical paper saying like we need mathematical analysis or like economic analysis on it is that something that's happening ?

**Tim**: Good point, not that I am aware of, the closest thing we have right now is Barnaby from the EF working on different simulation models. We don’t have full theoretical analysis. I know Nick Jhonson has been pushing for that a lot. 
I guess it's the call, if that’s your background and you want to work on 1559, please ping me and I'll make sure to put you in touch with the right people to get this started, we also have a Discord channel on the R&D server. I think  I like to follow up with Nick a little more and then maybe have the next 1559 call at a time as he can attend so that we can recapture his concerns there.

**Hudson**: Hmm

**James**: That's a good idea.



# 4. [Eligible for Inclusion (EFI) EIP Review](https://eips.ethereum.org/EIPS/eip-2378)
[EIP-2565: Repricing of the EIP-198 ModExp precompile](https://eips.ethereum.org/EIPS/eip-2565)

Video | [25:23](https://youtu.be/c_JmTqeQkU4?t=)
-|-

**Hudson**:  We can go to the next item on the agenda this is the EFI EIP review EIP 2565 repricing the VEIP 198 mod exp precompile. Kelly?

**Kelly**: There's some final changes being made to the EIP draft, they were nothing really substantial, we are working through some final benchmarking to make sure that there are no issues with the pricing but we have the test vectors.  My estimate is that, that will be complete early next weekend and fina, and we will submit a PR to the EIP repository at that point.

**Hudson**: Okay, great!

**Tomasz**: One question here. Kelly that you’ve said that you’ve the test vectors and since over this weekend we’re to set up this benchmarking. Geth and Nethermind and I think, Alex has something for a parity. Can you share the test vectors so we can run them?

**kelly**: Absolutely. I guess we’ve two sets. The  current set of I think it's 8 to 10 test vectors that are used for the original EIP 198 right now and we have an expanded set of test vectors, which just going to be additional 100 with maybe a random parameter values. If one of those better to share with you guys than then the other and if you want the expanded set ones that are used by the clients today.

**Tomasz**: It would be great to include expanded sets to the repositories which have all the test vectors. 

**Kelly**: Fantastic, where's the best way to put that? Is it best to put like a gist file in the EIP directly or is it better to share?

**Tomasz**: I think just making it as simple as possible, just sharing a simple text file with the input, will be enough because Alex's format is just one of the formats and not the best ones. We can adjust it if you just give the inputs that you’re testing and you don't even have to get the results because it's just performance testing.

**Kelly**: Oh, perfect! And the best place to share that, is that Gitter?

**Tomasz**: Wherever you feel is the best. Gitter would be good. I can just set up some quick repo that can be shared with. 

**Kelly**: Fantastic, we will absolutely do that. 

**Alex**: Another question out of my curiosity, what did you decide on existing performance? Because I think you have spent some time to find a solution for ModExp.

**Kelly**: Unfortunately, the solution we arrived at with OE is just to modify the pricing formula without changing the underlying library. Artem did try the GMP version for the Rust, but unfortunately there are some compilation issues on windows. So, actually, there are no major changes to the underlined library for any of the clients, it’s just got to be the pricing formula change to better reflect the complexity. I believe there was a small version bump with OE recently but no major changes to the library. 

**Alex V.**: Thanks!

**Hudson**: Anybody else? Thanks, Kelly!

**James**:  I was talking and I was on Mute. So, the consensus is to go ahead with option two ? or the option one is now the version that they're doing ?

**Kelly**: **Option two is correct**. Unfortunately, we couldn’t go ahead with option 1 because OE was too slow in the implementation, so we are going with option 2.

**James**: Okay, and you will make an edit on the EIP to show that?

**Kelly**: Exactly, yeah that should be early next week.

**James**: I feel like we should move this into EFI because of the way the conversation has been going?

**hudson**: It’s already in the EFI.

**James**: I don’t know if we ever actually had a motion to have it happen. 

**Hudson**: We did, I forgot which meeting but yeah, it's in the EFI. Oh! you know what actually I'm looking at it right now the EIP is outdated but I just have to look at old meeting notes and see if it's motion to go in but I swear we did it at some point.

**James**:  I remember bringing it up last time saying they wanted to bring it up later but then we haven't actually had the motion of doing it, we just talked about the motion of doing it.

Video | [31:23](https://youtu.be/c_JmTqeQkU4?t=1883)

**Hudson**: Does anyone object to having this EIP as an EFI meaning that it has the go-ahead to be continued to be worked on and could make it into a hard fork, likely. 
I don't hear any dissent and we've been following this one for a while so and there's been a lot of good cooperation to really well-written EIP so I think that it's fine to go to EFI, so **that motion passes**. I guess we're calling it motions now. I just don’t remember ever calling it that. So just let's put in the EFI, sounds good.

## Action Items
- **89.1**- Kelly will share the test vectors with Tomasz and others on Gitter so they can run them.


## Decision Items
- **89.2**- EIP-2565 moving to EFI.

# 5. Update on Eth 2.0 Deposit Proxy Contract that utilizes EIP-2537
Video | [31:43](https://youtu.be/c_JmTqeQkU4?t=1903)
-|-

**Hudson**:  Next up item number 5
Awesome next up we have Alex Stokes talking about then update for the East 2.0 deposit proxy contract that utilizes the EIP 2537 the BLS curve operations. Alex, you can go ahead!

**Alex S.**: Yeah, hey everyone! pretty straightforward, there's an initial view on the contract. I'll go ahead and drop this in the [chat](https://github.com/ralexstokes/deposit-contract-verifying-proxy/blob/master/README.md). for those who aren't aware there's basically a really critical smart contract for Eth2, the deposit contract and basically that's how you enter into this new system is by putting a deposit of Eth along with some credentials into this deposit contract. There's a bit more to rationale in this read me that I just put in the chat but basically there's some verification that don't happen and not contract in order to kind of keep it,  a user to be correct, just given its importance. So,  this contract is a another one that wraps it, this proxy contract. **The important thing is that it uses the Berlin pre-compile**. So it's kind of a client other precompile switch. I think it's pretty nice to have it  ahead of time. Generally,  just wanted to let people know about the contract. I'm looking for any review so if you want to look at it like a security standpoint, please get in touch. I am working  to deploy it to YOLO. Although the signer issue we talked about earlier had a little trouble but it’s on my to do list and then also work and integrate it with the Eth2 Deposit tooling.  So that either every validator uses it for extra insurance, do they have the option to do so or something like this. So I'm happy to take them.

**Hudson**: Anyone have any questions?

**Tim**:  Just to make sure I understand this is really a proxy contracted not a verifier, right, where you actually send the funds through the Contract with the release them to the deposit contract rather than just verifying your inputs,  right?

**Alex S.**: Right. so the other different ways to break it up right now what the contract does is **you send to the full deposit along with the Eth** and so when I say full deposit I mean like their credentials that end up going into the Eth2 system. So all of that data plus the Eth goes to this contract. **This contract verifies the BLS signature to make sure that's correct** cuz that's what we've been seeing is that basically there's been some incorrect signature creation and then that leads to an invalid deposit and then the Eth is basically lost. This contract helps because it checks the BLS signature, if that all passes and it looks good and then does a call for you to the deposit contract itself, so it wraps in a sense. If it turns out that like it takes too much gas to do this way or something, we could actually split it out so that the verification lives along side but then the actual Call to the deposit contract is done by yourself, separately. 

**Tim**: Great okay that's really valuable and I guess my other question is, is there a plan for like a formal audit? I don't know who audited the deposit contract (original), is there a plan for similar security audits by the same folks /different folks.

**Alex S.**: Yeah, specially if we move ahead integrating this with more formal Eth2 deposit tool and then yeah I would want to look back at that pretty seriously. There's not currently a plan, there could be a plan. I think *Runtime verification*, I believe did the initial deposit contract, so we might reach out to them but yeah I really anyone who'd want to look at it. the upside is it's like pretty simple and straightforward so it's not not that wild.

**Hudson**: Other questions? there is a telegram Channel dedicated to this contract and looking for gas optimizations and bugs that are he has a handful of people in there from the solidity and security Community looking at it but it's very ad hoc right now, so we could definitely use more help just looking over it and if you're interested reach out to myself or Alex and we can add you to that or if you are listening in on the call and want to help reach out to us especially if you're someone who could do an audit for it and stuff like that. 

## Decision Item
- **89.3**- Alex S. and team to look into another security audit for Eth 2.0 Deposit Proxy Contract that utilizes EIP-2537. Anyone interested, reach out to Hudson or Alex S.  

# 6. Account Abstraction Research Update
Video | [36:30](https://youtu.be/c_JmTqeQkU4?t=2190)
-|-

**Hudson**: So, thanks for the update Alex and we can move on to the next item on the agenda number 6 account abstraction research update with Will, go right ahead.

**Will**: Hey everyone,  just want to give a quick update on our progress. 
The initial spec that Vitalik had put together, which has some limitations, 
we actually just finished putting an MVP or putting that together in Geth to be passing tests and internal AA tests right now. 
Additionally we have a tool that is propagating the transactions through and used as a measurement tools to work collecting metrics right now and cleaning up and doing everything around that. 
So we we plan on starting a bit more communication with Community soon around this, will likely have a have a call and we'll be doing a write-up in the next couple weeks, I'm especially looking at the data and the metrics that we get from this.
One thing to stress, this is overall feasibility study. We’d like to explore the possibility to bringing this into Eth1x but right now there's a feasibility study and of course there's no guarantee until we get a bit more people involved in discussing. We are  showing strong feasibility, this current time. So will be expanding this  shortly to go beyond what the initial proposal was and support multiple transactions per account. But we will be doing a bit more research and some write-ups and some updates on that soon. Just want to give you guys up today on with what we've been doing. I think we'll have a bit more meat for people to process and digest here in the next couple weeks and hopefully that should start a good discussion overall.
 
**Hudson**: Any questions or comments on that anybody?

**Will**:  We’ve also been exploring how that intersects with the general discussion in meta transactions as well and howaccount abstraction overlaps with that we've been involved in this discussion in the Eth research recently. We see it under the same umbrella as well. So, we've also been putting effort & time into it. 

**James**: Did you see the updated version of the oil and gas proposal from Alexey that talks about meta transaction research. 

**Will**: We did, we responded to that and then we posted a new post on Eth research that continues to experience some of these discussions as well.

**James**: Great!

**Hudson**: Alright and if anyone wants to go back over what Will just discussed or go to any of the links for the spec or the discussion on Eth research, it's in the agenda at the latest [comment](https://github.com/ethereum/pm/issues/180#issuecomment-643287338) that was posted about half an hour ago. Can you post a link in the agenda or on here to the spec you made,  Will? Which of the implementations you made it at the fork of geth?

**Will**:  Oh yeah, I can put a [link](https://github.com/quilt/go-ethereum/pull/13/).

**Hudson**:  Perfect, alright thanks for that and if there's nothing else will go to the next update.

# 7. ethereum/PM calendar
Video | [40:18](https://youtu.be/c_JmTqeQkU4?t=2418)
-|-

**Hudson**: This is James he made a calendar let's talk about it.

**James**:  I made a calendar, it started as being for the All core dev calls and then has since expanded to include Eth2 call and EIPIP  stuff and it's a public, followable calendar manage through Google. but you can use other clients to do it so anyone who wants to follow or be added on the list so you get emails to remind you to attend calls, I am happy to add you!


# 8. Testing Updates
Video | [41:02](https://youtu.be/c_JmTqeQkU4?t=2462)
-|-

**Hudson**:  Okay thanks for that. next up we have item8 testing updates anyone have anything testing wise that they want to discuss about their clients or the ecosystem?

**Martin**: One thing,  I would like to mention is that it would be really nice if we can do fuzz testing using status instead of shoving things to YOLO.I am not really sure about clients have implement some state test report for YOLO, Geth has. I am not sure if other clients. But it would be really nice if you guys can do that because it would make things a little more efficient. 

**James**: What would it take to do that?

**Martin**:  Good question. So State tests basically encapsulate the transformation from one state to the another state. They have the pre-state, they have the transactions that should be applied to said prestate. And they expected post they pass. 
The state test decides these things. I made a proposal I think maybe two years ago that clients should accept names on the forum Constantinople plus 2315. I am quite certain that no one actually implemented that, besides from us.
Second best alternative is, just add Yolo1, so we can have a status, but the network name is Yolo v-1 or whatever. And Yolo chain rules are active at the transactions.
 If you were to implement the state test, it would be fairly trivial to do this.

**Hudson**: Anyone else have questions or comments ?

**Tomasz**: I just wanted to add that we will be there probably quite soon because we wanted to finalize this hive work to execute the consensus test from hive and then I will be able to add the new test for new EIPs. I hope soon we'll have state test results for you.

**Martin**:  Much appreciated, thanks.

**James**: I think we should add some of that language to the Yolo EIPs, perhaps Martin. Something we could follow up on. Writing those out and then tracking state test based on per client.

**Hudson**: Anybody else?

# 9. [Review Previous Decisions and Action Items](https://github.com/ethereum/pm/blob/master/All%20Core%20Devs%20Meetings/Meeting%2088.md)
Video | [44:52](https://youtu.be/c_JmTqeQkU4?t=2682)
-|-

**Hudson**: All right next up we have review previous decisions made and action items. The notes have been merged. If you refresh the page, it should work, the link to the notes.

So for decisions made last time :

**88.1** is State tests for YOLO-v1 should be regenerated under that name (and should not carry the Berlin name)

**88.2** Opcode change proposal to be implemented -  that's a little vague we might want to be a little more specific about that one.

**Actions Required**

**88.1** James Hancock to continue to update the Berlin and YOLO EIPs, including commit hashes. That's been ongoing right, James ?

**James**: Yep, that happened.

**Hudson**:  

**88.2** Ephemeral testnet EIP to be merged several testnet EIP to be merged 

**James**: that has happened 

**Hudson**: 
**88.3** James Hancock to follow up with Open Ethereum, Axic, and Martin to discuss EIP-2315 after this call

**88.4** Axic to make a PR to update opcodes for EIP-2315
I believe that happened too. Did that happen too, Alex? 

**Axic**: Yes, Martin did it.

**Hudson**: 
**88.5** James Hancock to coordinate with Axic and interested parties about a precompile gas cost changes call. that happened.

**88.6** Kelly to continue working with Open Ethereum on EIP-2565. 
That has been resolved and the EIP will be updated, right Kelly?

**Kelly**:  Correct 

**Hudson**: I didn’t do a great job of writing down the decisions made it actions required today but it sounds like 
* EIP 2656 to be moved to EFI officially and the EIP to be updated.
*  James H. to follow up with Martin and others on State transition test for clients and how that relates to Yolo.
* (Next call) Evaluate adding EIP-2046 to Yolo

Other people: are there any decisions made or actions required for this meeting the people have?

**Tim**: Yes, I think there are two different things, the state test and test vectors for the precompile?

**James**: Test precompiles are going to whoever requested those, is that you Besu?

**Tim**: Yeah I will need to look into those and then we'll probably reach out as we're doing it.

**Hudson**: Okay, that's another one.
Anybody else?
Does anyone have any final agenda items that we haven't gone over things they want to say before we end the call super early?

**James**:  I'm on vacation next week so I'll likely get to this when I get back.

**Hudson**: Cool!

**Tim**:  Enjoy your vacation.

**James**:  Thank you!

### (Yolo update)

**Peter**: Very quick update on Yolo. I’ve been digging into what the issue might be. It turned out that **the signer was not Yolo enabled**. It was running on an old version of Geth. Apparently, for some reason, the NS resolution doesn’t work currently on  that machine and that's why the docker  actually failed to pull a fresh version of geth.  So fun fact that's why the signer went off on its own little world because it actually didn't have the Yolo fork enabled. So we're trying to fix that. 

**Alex V.**: This is super strange, because if it didn’t have Yolo enabled at all …(technical details that couldn’t be caught).. Maybe it did use some old version, but if it didn’t have Yolo versions at all, I’d expect those transactions to fail immediately. 

**Peter**: Yes, it’s complicated. Can I first finish, please?
 The signer when I originally deployed, I deployed at my own custom build. Then when whole thing went out of the disk, it  switched back to the default version of geth which was old and didn’t have it enabled. That’s why it started failing at 45,000 blocks. It’s only about the signer that was running the ancient version of geth that happens to be on the machine.

**Alex V.**: Oh, so it switched at some point, not at the start of the chain. 

**Peter**: No, it was in the middle when the whole network got stuck, we rebooted the signer then it switched to the old version. It didn’t occur to me that the Geth version on that  machine is ancient and since for some reason, DNS solution doesn't work on that machine, docker didn’t manage to pull  up fresh one. I just want to say that **we’re sorting it out**.

**Alex V.**:  Well then that explains perfectly. 

**Hudson**: Okay, anybody else have anything final ?

**James**: It’s a good reminder that Dapp developer should be looking at YOLO to test their things unless you are actively working on the EIPs, helping evaluate them or client integration test.

**Hudson**:  And you’re just saying that so people don't deploy their dapps and think it'll stick around, right?

**James**:  Yep I'm just sending it out many times. So eventually everybody understands.

**Hudson**: Yup,  that's why we call it an ephemeral testnet which is a very meta name.
Okay sounds like that’s everything. The next meeting is going to be June 26th at 1400 UTC thanks everyone for coming. This is a great meeting. Thank you !!

# Annex

## Attendees
* Alex (axic)
* Alex Vlasov
* Alex Stokes
* Ansgar Dietrichs
* Artem Vorotnikov
* Daniel Ellison
* David Mechler
* Edson Ayllon
* Guillaume
* Hudson Jameson
* James Hancock
* Jason Carver
* Karim Taam
* kelly
* Martin Holst Swende
* Peter Szilagyi
* Pooja Ranjan
* Rai
* Tim Beiko
* Tomasz Stanczak
* Will Villanueva

## Next Meeting Date/Time

Friday, Jun 26 2020, 14:00 UTC


## Zoom chat
**10:03:16**	 
From Pooja Ranjan : https://docs.google.com/spreadsheets/d/1BomvS0hjc88eTfx1b8Ufa6KYS3vMEb2c8TQ5HJWx2lc/edit#gid=0

**10:05:21**	 
From Tomasz Stanczak : Nethermind has not merged changes

**10:05:28**	 
From Tomasz Stanczak : not sure where it comes from

**10:05:49**	 
From Tomasz Stanczak : not merged

**10:15:54**	 
From Tomasz Stanczak : cannot hear

**10:17:53**	 
From Daniel Ellison : @Tomasz Audio is fine for others.

**10:18:35**	 
From Edson Ayllon : He meant for Rai. James gave a summary of what Rai said

**10:32:25**	 
From Alex Stokes : https://github.com/ralexstokes/deposit-contract-verifying-proxy/blob/master/README.md

**10:40:11**	 
From James Hancock : https://github.com/ethereum/pm/issues/180#issuecomment-643287338

**10:40:14**	 
From James Hancock : Wills Comment

**10:40:28**	 
From Matt : https://github.com/quilt/go-ethereum/pull/13/

**10:40:33**	 
From Matt : AA ^

**10:41:12**	 
From James Hancock : https://calendar.google.com/calendar/embed?src=ethereum.org_semftevk58vu53rv149mvkla78%40group.calendar.google.com

**10:47:36**	 
From Will Villanueva : Just updated the comment to link to our active WIP (diff) if you open it again.




