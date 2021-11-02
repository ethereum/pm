# All Core Devs Meeting 104 Notes
### Meeting Date/Time: Friday, January 22 2021, 14:00 UTC
### Meeting Duration: 45 mins
### [GitHub Agenda](https://github.com/ethereum/pm/issues/237)
### [Audio/Video of the meeting](https://youtu.be/3xNfGNnQ5Vs)
### Moderator: Hudson Jameson
### Notes: William Schwab

# Summary 

## EIP Status
EIP | Status
--|--

- 2937: | Draft

## Decisions Made

Decision Item | Description
--|--

- **104.1**: YOLOv3 to be launched when ready
- **104.2**: async conversation about fork block to commence after YOLOv3 launch
- **104.3**: Ice Age delay will not be included in Berlin


## Actions Required

Action Item | Description
--|--

- **104.1**: Martin Holst Swende and Rai Sur to get YOLOv3 running
- **104.2**: James Hancock to write EIP for Ice Age delay


---

# Agenda

<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 bullets:1 updateOnSave:1 -->
- [1. YOLOv3 & Berlin client updates](#1-yolov3-berlin-client-updates)
- [2. Other EIPs or Discussion Items](#2-other-eips-or-discussion-items)
    - [2a. Ice Age & Future network upgrade](#2a-ice-age-future-network-upgrade)
    - [2b. EIP-2937 Update](#2b-eip-2937-update)
- [3. Closing Remarks](#3-closing-remarks)

# 1. Yolov3 & Berlin client updates
Video | [2:30](https://youtu.be/3xNfGNnQ5Vs?t=150)
-|-

**Hudson Jameson**: If you click on Yolov3 (_in the agenda, linked above_ - notetaker's note), it will take you to the client spec (_link is to [here](https://github.com/ethereum/eth1.0-specs/blob/master/client-integration-testnets/YOLOv3.md) - notetaker), and there is also a new spec document that James and Micah have worked on for Berlin, I'll post that in chat (link is to [here](https://github.com/ethereum/eth1.0-specs/blob/master/network-upgrades/berlin.md) - notetaker), that goes through a checklist and a client readiness checklist. We'll get some of that confirmed today, so I'll give this to James to talk about.

**James Hancock**: This is a lot like the hardfork EIPs we had in the EIP repo, but are now in the 1.0 specs repo because we're keeping those worlds separate, and if you go through it, where we are is the final EIPs implemented into Geth and deploying YOLOv3, getting a security greenlight and proposing a fork block for testnets. I was hoping to get an update for status on 2718/2930 testing and implementation.

**Peter Szilagyi**: My repsonse will be a bit underwhelming: I don't know. Martin was mostly the one who pioneered these parts, and I was mostly focusing on getting our next release out.

**Rai Sur**: I can speak to a little bit of it. We've been working on it. We've been working on general unittest-style stuff, but he just updated transaction tn8tool to support the new transaction type, so hopefully we can referenec tests soon.

**James Hancock**: 2930 is a new transaciton type, so it would make sense that you would have different tests that we haven't had before? Is that what's going on?

**Rai**: Yes. Actually, Danno - we would need to support something on our end, right? We need to support tn8tool?

**Danno Ferrin**: We support retesteth, that's the original spec, and that's what we were running off of. I don't know if the retesteth tools support the rpcs or not, that's to be determined. If Geth is not interested in supporting retesteth then we should move to the ?.

**Martin Holst Swende**: We do support retesteth, just not the api.

**Danno**: The one that was originally specced, with the http stuff? You have the TA and CLI? I consider those two separate things.

**Martin**: retesteth is a tool, but you're referring ot the API specification? The tool is now able to use a binary like the state transition tool like a backend instead of the rpc api.

**Danno**: Becasue you wouldn't support the legacy api, so that's why we're moving there.

(**Rai** clarifies that this was his only testing update)

**James Hancock**: We've focused on getting this done to go for YOLOv3, but I'm thining it would be good as a group to consider looking at setting fork blocks for testnets in a prallel path. Previously it was a linear path, like we'd do YOLOv3 and wait a while and then do the fork blocks, but I would open to feedback to independently start talking about fork blocks and when we could set them.

**Martin Holst Swende**: I would kinda agree that it might be good to try to schedule something. This approach about rolling it out when it's ready, I had high hopes for it, but I'm ont sure it's goingto pan out as I hoped, so it might be fine to try and schedule something.

**Tim Beiko**: Say we scheduled a testnet block, so it needs to be a few weeks away anyway, obviously the finished work, but even past that you need to put out a release and people need to download the release, it feels like in parallel to when that release is being deployed and adopted we can also have YOLOv3 and fuzz test. Does that make sense? (**Martin** concurs.)

**James Hancock**: Is there a sense for how we should start thinking about it? Anything from two weeks to two months, something that given your knowledge of what's left or what needs to be done in order to look for targets?

**Martin**: It's kind of a chicken and egg problem.

**Rai Sur**: Theoretically we could set them in parallel to YOLO, would you feel more comfortable setting them after YOLO? (**Martin** concurs.)

**Hudson Jameson**: We can do after YOLO's launch, but we could after do it after we know YOLO is launching.

**James Hancock**: When the features are ready, however that's defined.

**Martin Holst Swende**: Should we then decide when to launch YOLOv3?

**Hudson**: That sounds good as long as we have a fairly confident estimate of whne the rest of the EIPs and Geth would get done, because I think that was just reviewing stuff that had aready been written. (**Martin** asks for clarification) EIP 2718 and 2930 in Geth, those are implemented, just not reviewed?

**Martin**: That goes hand in hand, there is still implementation ongoing, and it is being reviewed as well. And 2930's latest PR is from last night.

**Hudson**: In that case, as to your question about setting a date for YOLOv3, I think we could, because then if things mess up and we have to change it, tha's not too bad to change, and it at least sets us a goal and expectation.

**Rai**: We don't need to need to set a date, right? As soon as it goes up, it goes up, and once we're comfortable, we could set fork blocks. We don't need to say "we're going to launch YOLO on this date", just launch it and people will join.

**Tim Beiko**: We can also decide on the fork block async, right? I think once we're in a spot where we can launch YOLO, which means that the work is basically merged in Geth, I think we could probably say something like 4 weeks from there for the testnet fork block gives two-ish weeks for the clients to ship a release, and two-ish weeks after that for people to update their nodes. We should obviously confirm this on a call, but we can make the decision.

**Martin**: I would like to at least set an expectation. Rai, I tihnk it would be really cool if we could get the testing and get the YOLOv3 version runinng in the coming week, if we work together. (**Rai** agrees that this is reasonable) Not necessarily into mainline Geth as a PR, but I think it's enough if it runs as a PR, and might need more tweaks to actually get it merged into mainnet.

**Rai**: In your model, what's your dependency structure between the reference tests and launching YOLO? Maybe that one week is not realistic if we need to do extra support for tn8tool?

**Martin**: Right, but the reference tests won't be shipped \[as a part of] YOLOv3.

**Rai**: That's what I was asking, I just wanted to knowif you saw that as a dependency or not.

**James Hancock**: That will be a goal for next Friday, and then for next call we can talk async as we know more aout things for fork blocks, and talk about next All Core Devs.

**Hudson**: Just so I understand, though, we're going to launch YOLOv3 when we launch it, as far as the async convo for fork block, it can be immidiately after YOLO's launch, is that what we're doing , or do we want it to run for a little bit first?

**James Hancock**: I'd say let's focus on having YOLOv3 be the launch for this next week, and then the week after that is when we can start bringing it up. The following week we should start thinking and talking about it.

**Hudson**: Any other comments? (_silence_)

## Decisions Made
**104.1**: YOLOv3 to be launched when ready
**104.2**: async conversation about fork block to commence after YOLOv3 launch

## Actions Required
**104.1**: Martin Holst Swende and Rai Sur to get YOLOv3 running

# 2. Other EIPs and Discussion Items
Video | [15:15](https://youtu.be/3xNfGNnQ5Vs?t=915)
-|-

# 2a. Ice Age & Future network upgrade
Video | [15:15](https://youtu.be/3xNfGNnQ5Vs?t=915)
-|-

**Hudson Jameson**: lightclient is here to discuss EIP-2937, but first let's talk about the Ice Age and future network upgrades. The gist of the request (_notetaker's note_: on the meeting agenda [here](https://github.com/ethereum/pm/issues/237#issuecomment-762513550)) is that according to EIP-2384 the Ice Age will be back around July 2021, will there be another hard fork, I would love to hear what the Core Devs think.

**Tim Beiko**: I confirmed the number over the past work with TJ Rush from QuickBlocks \[TrueBlocks], the July 2021 number is accurate.

**Micah**: In the past, when there has been a significant gas swing which has significantly affected the guess, does that play a role here, because I'm surprised that the guess is still right.

**Hudson**: Just to be clear, what does price have to do with it?

**Tim Beiko**: More miners come in, and so for the time during which... the hashrate goes up quicker than the difficulty adjusts, so it creates blocks quicker for a short period of time. I guess if you get multiple price swings, you get multiple phases.

**James Hancock**: Not just that, but if your hashrate is higher you can artificially keep the Ice Age \[from] happening by pushing out when the Ice Age would show and when it would be too far, because it uses the hashrate as a funciton in the Ice Age formula. So if you have a big hashrate, the Ice Age will be smaller longer.

**Danno Ferrin**: It'll move it out at best 2-4 weeks.

**James Hancock**: It would be great to see the calculations.

**Tim Beiko**: I'll share the repo in the comments (_notetaker's note_: couldn't read comments, believed to be [this link](https://github.com/TrueBlocks/tokenomics/tree/main/explorations/difficulty) found in ACD), it's what we used lat time, I believe. It seems like as of now there is no acceleration, but this could change.

**Hudson**: If anyone has comments, speak up, I don't believe this would be going into Berlin at this point, I think there would be another hard fork which would happen later on before the Ice Age would hit, or as it's hitting, and basically doing our best to estimate when we can get a hard fork in which has some significance and isn't just an Ice Age delay.

**Artem Vorotnikov**: Can't we just disable the Ice Age once and for all and not bring up this topic in the future? (_diagreement from multiple parties, perhaps Danno Ferrin and Tim Beiko, maybe others_)

**Tim Beiko**: I strongly disagree. One, we've found it useful as a forcing function for forks in the past. Two, with the transition to Proof-of-Stake happening in The Merge I think we want it. It creates a barrier for anyone who wants to not upgrade when there is an upgrade that they need to maintain a fork and remove the difficulty bomb, and they don't get to just stay on the network and block progress. I think both for us as the Core Devs it helps us ship stuff, but I think for anyone who wants to oppose, it creates a not very high but a barrier to entry because you have to fork the client and remove the Ice Age, and share whatever changes they want.

**James Hancock**: And you can always make an EIP and we can talk about it. I would agree that we should keep it, and we should address it when it's showing up.

**Tim Beiko**: There probably is a EIP already. I remember talking about this last time.

**Micah**: (_notetaker's note: couldn't understand, may have been a reference to EIP-1227)

**Peter Szilagyi**: I just wanted to add some comments. I don't think we should add it to Berlin because if it's not urgent then it's fine ot have a second fork. The other good part of delaying it a bit and forcing another hard fork is that there is some potential with 1559 and a few EIPs, there are some conflicts on Twitter, not everyone is fully agreeing with 1559, and people have different opinions, different rationalizations, there are some fears that 1559 could cause some trouble. Actually having the Ice Age forcefully happening in a few months can help us to solve some issues. Generally, 1559 legit introduces some issues, I don't know which ones now, but if we legit have some issues, and the Ice Age gives us an opportunity to handle that issue really quickly. Versus if it's just one of those annoying issues and we don't have anything to force miners or people to upgrade, and it's a lot harder to address. So I think in our current position it might be valuable to not touch the Ice Age for Berlin.

**Artem Vorotnikov**: You understand that the Ice Age delay is like a one-line change in the code, I'm pretty sure that all dissenting parties have the resources to change that one line and live without the Ice Age on the fork chain.

**Tim Beiko**: I think you're underestimating the distribution. Yes, it's easy to change in the code, but then you need to get that release to users, and they need to adopt it.

**James Hancock**: That code needs to live somewhere, and people need to be able to find it, and need to be able to trust it...

**Micah**: Trust, I think, is the hardest part. If it's just some random dude on the internet who's anonymous, how many miners around the world are going to download it.

**Hudson**: Eevry hard fork we've had all kinds of scams, some of them are actually smart contracts that people go and check on, and people actually hand over their private keys, so I'm on the anti-scam side of things, whatever can be done to most prevent that.

**Peter Szilagyi**: All in all, if we think about the Ice Age long-term, I kind of agree with everybody. The original purpose of the Ice Age was to force Eth to switch over to Serenity, it seems weird to kill the Ice Age right before actually getting to that point, so if we stuck it out for five years, we might as well go all and just leave it.

**Hudson**: I am curious, Artem, because the original purpose of this is still set and it's still doing what its purpose was, is your argument that it's annoying and forcing people into something they don't need to be forced into?

**Artem**: It causes us to waste time, on discussions, on fixing, on delaying Ice Age, on doing an emergency hard fork when we forget about Ice Age...

**Hudson**: At least that isn't likely to happen this time because we're early enough in the process and have figured out the date. As long as we get it right and it doesn't shift drastically, but nothing's guaranteed.

**James Hancock**: We haven't forgotten about it today.

**Hudson**: I'm seeing most of us saying that we're not going to put the Ice Age into Berlin definitely, and we need to evaluate in the future when another hard fork \[would happen], depending on which EIPs are out there, since I guess an EIP would be need to be made for delaying the Ice Age versus disabling versus anything else people have ideas about.

**Micah**: Does anyone want to volunteer to make an EIP to deplay the Ice Age, just to get the conversation started?

**James Hancock**: I can do it. To your point (_notetaker's note_: I believe this refers to a comment Micah made in chat) if the price of ETH goes up, it's more likely for the Ice Age to be delayed further than to accelerate.

**Hudson**: Are there any more comments? (_silence)

## Decisions Made
**104.3**: Ice Age delay will not be included in Berlin

## Actions Required
**104.2**: James Hancock to write EIP for Ice Age delay

# 2b. EIP-2937 Update
Video | [25:58](https://youtu.be/3xNfGNnQ5Vs?t=1558)
-|-

**lightclient**: There are two people who have been working on \[EIP-2937], I don't think they made it to the meeting today, I know Artem had some comments on it last time, and there is a discussion on Eth Magicians still, I think ironing one part of it out, there's a PR to adjust the specification, so I don't know if nayone had any comments on this EIP.

**Martin Holst Swende**: I posted some questions in the forum, and was it you who answered?

**lightclient**: It wasn't me.

**Martin**: I couldn't figure out if the answers were the canonical answers, they were like "I think that...", and I'm wondering what the actual answer is. Based on the current specification I could not implement this in Geth if I wanted to, there's too much that isn't explicitly said.

**lightclient**: The person who repsonded is one of the people who wrote an implementation for it. During implementation there were a few changes to the specification from how Vitalik originally wrote it. It was originally written with a global variable that stored every address that called indestructible within the transaction call graph, and they decided to scope it to the frame of execution and also propogate up these DELEGATECALL or CALL or whatever they were called. It should be updated on the spec [on a pull request](https://github.com/ethereum/EIPs/pull/3186), but Vitalik hasn't been able to improve it yet.

**Martin**: What is supposed to happen if I DELEGATECALL a contract which immidiately says set indestructible? That's the intent - you're not supposed to be able to destroy a library, so every well-behaving library will do this.

**lightclient**: So if you DELEGATECALL into it, it should not allow the address that the code is executed at to self-destruct. If you were ever to call the library directly, where its address is the executing context and that is set indestructible, ? that address.

**Ansgar Dietrichs**: Martin has a point, if we implement that way, if you assume that your contract relies on using self-destruct at some point, you could not use libraries that start with set indestructible, at least not if they're a part of every execution path (_notetaker's note_: may have misunderstood previous) because then you can't be self-destructible, and maybe that shouldn't happen.

**Martin**: That becomes a bit problematic because in the EVM execution context you have the address which is the current executing address, and one thing you may not always have is the current address where I pick the code, but am not executing under. But what the EIP says is that if you run into set indestrucible and the code is from somewhere else and not from the address where you are currently executing then you should ignore it.

**Ansgar**: I think right now the EIP said the opposite? If you DELEGATECALL somewhere else and then that call set indestructible then the call context becomes set indestructible for the duration of the call?

**Martin**: That's vague in the EIP, and what I tried to ask. It says the current callee, but who is the current callee in a DELEGATECALL.

**lightclient**: That's a good point, and we can make it more clear. That's also a good point wiht the libraries, I wasn't really sure how most contracts implement self-destruct functionality, are they always DELEGATECALLing into something, and this has all the funcitonality, in which case it doesn't really work, because then you aren't able to self-destruct ever.

**Ansgar**: Just to be clear, the [PR](https://github.com/ethereum/EIPs/pull/3186) that I also put in the chat that lightclient mentioned indeed clarifies some of the language around callee, that whole sentence with callee is removed, and it's very explicit what happens in the case of a DELEGATECALL. It's still an open question if this is the behavior we'd want to happen, but at least I would say that it is well-specified now in the PR.

**Hudson** Anything else on this?

**lightclient**: I think that's it, we'll work on getting it better specified and how to address the issue with using libraries and how self-destruct...

**Martin**: I think it would be good if the specification was written more hands-on with well-defined terms such as address and current executing contract, even the PR now says "if contract X does DELEGATECALL(c) && selfdestruct", but that's a bit too high-level in my opinion. It's good for a high-level desciption, but there should also be a lower-level technical specification so that at any point you know exactly what to do, and not have to figure out if you arrived by DELEGATECALL.

**Micah**: Can we get a channel in Discord for each EIP that is going into an upcoming hard fork? By the time we get to the hard fork we're usually down to 2 or 3, so I don't think it'll be too big of a burden on channels, and we can delete them afterwards, but I think it would be nice to have a place, like when Martin wanted answers, that he could just pop in to that channel, and the right people are there.

**Martin**: I think it's fine with the forum, except when the forum goes stale, but if the forum goes stale, the Discord would probably go stale.

**Hudson**: I think it's a good idea for certain major EIPs for sure, beyond that I'm skeptical of the value kinda like Martin is saying. But we can always try it when we have a medium-sized EIP or one that's having a lot of ACD discussion, no problem trying it out in the future, but this one sounds like it's active enough in the forums.

# 3. Closing Remarks
Video | [35:28](https://youtu.be/3xNfGNnQ5Vs?t=2128)
-|-

**Tim Beiko**: As people know, I'll be taking over All Core Devs from Hudson soon. One of the things I've been doing in the meantime is reaching out to folks involved in the process to get their feedback about how it's going and how we can improve it, and their thoughts in general about All Core Devs. If you have strong opinions or want to chat about it, please reach out, happy to take some time to chat. Over the next couple of weeks I'll try to put most of the feedback I've received together, and share it back here.

**Hudson Jameson**: So they can probably reach you on Discord, if not Discord then Telegram, if not Telegram then Twitter DM, and if not Twitter then ham radio?

**Tim Beiko**: Discord and Twitter are the best, DMs are open on Twitter, I'm on the Eth R&D Discord.

## Attendees
- Adria Massanet
- Afri Schoe
- Alex Vlasov 
- Artem Vorotnikov
- Danno Ferrin
- Dragan Rakita
- Eugene Danilenko
- Guillaume
- Hudson Jameson
- James Hancock
- lightclient
- Martin Holst Swende
- Micah Zoltu
- Peter Szilagyi
- Pooja Ranjan
- Rai Sur
- SasaWebUp
- Tim Beiko
- Tomasz Stanczak
- Trent Van Epps

## Next Meeting Date/Time

Friday, December 11 2020, 14:00 UTC
