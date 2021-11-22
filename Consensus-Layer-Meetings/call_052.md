# **Ethereum 2.0 Implementers Call 52 Notes**

### **Meeting Date/Time: Thursday 2020/11/12 at 14:00 UTC**

### **Meeting Duration: 1 hr**

### [**GitHub Agenda**](https://github.com/ethereum/eth2.0-pm/issues/184)

### [**Audio/Video of the meeting**](https://youtu.be/yFjs_tB6I-Y)

### **Moderator: Danny Ryan**

### **Notes: William Schwab**

--------------------



# **Contents**

- [1. Testing and Release Updates](#1-testing-and-release-updates)
- [2. Testnets](#2-testnets)
- [3. Client Updates](#3-client-updates)
  - [3.1 Nimbus](#31-nimbus-mamy)
  - [3.2 Lodestar](#32-lodestar-cayman)
  - [3.3 Prysm](#33-prysm-terence)
  - [3.4 Lighthouse](#34-lighthouse-paul)
  - [3.5 Teku](#35-teku-anton)
- [4. Research Updates](#4-research-updates)
- [5. Networking](#5-networking)
- [6. Spec Discussion](#6-spec-discussion)
- [7. Open Discussion/Closing Remarks](#7-open-discussion-closing-remarks)

## Action Items

Action Item | Description
--|--

- **52.1**: 

------------------------------

#
# **1. Testing and Release Updates**

| **Video** | [2:58](https://youtu.be/yFjs_tB6I-Y?t=178) |
| --- | --- |

**Danny Ryan**: The v1 release is pretty much the same as the candidate release except for some additional testing. Hsaio-Wei, myself, and proto (a bit) are looking to revamp the way the test factors are output which will be some changes on your end about how you induct them in, but will greatly reduce test generatiopn time and reduce the disk footprint, which will hopefully allow to greatly extend the number of test vectors, throw in more random things and lots more operations. Still in work, probably not a huge priority to ship this in the next few weeks, will probably be in like 4-6 weeks. Maybe we'll wait and get mainnet out first, then change the tests.

**Mehdi Zerouali**: (Beacon Fuzz update) Over the least few weeks we've been running out structural differential fuzzer, and found two consensus bugs in Prysm, the first is an off-by-one bug in the committee index valuation of the attestation process, and the second was basically using the wrong epoch when validating slashings to propose slashings. These are all fixed now. There was also one minor non-exploitable spec divergence for Teku in the proposed slashing, pretty much the same as the one with Prysm a few weeks ago. We started working with a future EF member joining the DevOps team, esssentially automate our deployment and monitoring of the fuzzers on our AWS infrastructure. He's built a bunch of pretty handy Ansible scripts, they're pretty much ready, should be done today or tomorrow. Concerning the work on the custom fuzzing engine, it's working, but we only got the mutation-based version working, actually structured inputs, the next thing that we're working on is adding that structural part for that custom fuzzer. I'll be writing this up in a blog post, hope to push that out over the next couple of days, that's pretty much it.

**Justin Drake**: There are two people who are going to be joining the Ethereum Foundation for security, we are still looking for talent, if you know anyone or are interested, please email eth2security@ethereum.org

**Danny**: Additionally, I think we're going to put on some RFPs, first to try to find some more external teams to help wiht testing, network testing, load testing, chaos testing, that kind of stuff, so if you're keen on that kind of stuff, keep your eyes peeled.


#
# **2. Testnets**

| **Video** | [6:52](https://youtu.be/yFjs_tB6I-Y?t=412) |
| --- | --- |

**Danny**: proto has been getting testnets up, got Toledo up which had 100% attestation/participation. There's been conversation (past 36 hours) about what to do about larger scale testnets. proto has prepared a track with 100k validators ans keys, and I think the intent is to share them between the client teams and EF to kick this off, ideally next week so we can get this going firmly before mainnet launch. There's a lot of talk about what that actually means, what the fate of Pyrmont will be, looks like we will open it ourselves, then open it up, make the config available for others to join in order to test configurations and stuff, and to have that at least through genesis, and then circle back on the conversation afterwards about what a sustainable testnet should look like in the long run, should we up the ejection balance, should we change the q-limits for sustainability and user experience.

That said, we haven't decided when to kick this off, the deposit contract is there, we just need to set the config, we can tune the genesis time however we want at this time. Proto, what do you think?

**protolambda**: The original idea was to launch Tuesday, with Toledo running and the efforts involved in getting another testnet up and running, so if I could just get some feedback from clients, and if they could confirm Tuesday, or we could move it a few days.

**Paul Hauner**: Tuesday is fine, we could use more time, but we could do it. **terence** echoes this 

**Ben Edgington**: I'm good with Tuesday for Teku, wouldn't say no to a few more days. (_notetaker's note_: I think someone else echoed this, but I can't see who)

**protolambda**: So I'm hearing Tuesday, although would work better if it's a bit later, we could do Wednesday just as well, so let's just go for Wednesday. (**Danny** agrees) I'll set the configuration for Wednesday. I assume we can do the same genesis time. (general agreement)

**Danny**: If this is going to be a utility to validators over the next couple of weeks, maybe stay in your Discord to not be overzealous on the amount of Goerli ETH they dump into this thing. One whale could block up the queue at the current limits, maybe encourage validators to try one or two. Obviously it's not in our control, but hopefully it can be a utility for validators in the coming weeks.

**protolambda**: Toledo will be running for at least a few more days. I want to give a shoutout to the beacon chain explorer for helping me get more insight into this. It seems to be performing relatively well. In the last few days I wanted to test some miscellaneous things, now that we have a net that we control and have good insight in, can test pretty well.

**Danny**: For Pyrmont we'll get a launch pad up in a subdomain, and for Medalla, I think we're going to publically sunset support for it next week, some will likely run nodes to test non-finality and some other edge cases, I think publically it will fully degrade. Is anyone opposed to stopping active support and sunsetting?

**Vitalik**: One thing to keep in mind is that I think that validators want to have some kind of environment to test their validators in. If it's not Medalla, what do we direct people to?

**Danny**: Pyrmont. We're going to kick that off with validators we control, and next week also open it up for deposits.

**Vitalik**: And we would be committing to run Pyrmont run for some longer amount of time?

**Danny**: At least through mainnet genesis, after which we'll have a conversation about what we might fdo to make a testnet more sustainable and user-friendly. For Medalla, anyone in the activation queue can keep running their nodes, and they will get activated because of the way the queue works.

**Dankard Feist**: Maybe for the new testnet we could make the queue faster so people can get in more quickly?

**Danny**: I'm not terribly opposed, especially if the reason is just to test configuration.

**Jacek Silea**: I would prefer really plain mainnet parameters, just to make sure we're testing the right thing, especially during launch.

**Danny**: Again, I'm going to try to convince the community to try a validator or two.

**Paul Hauner**: I'd also lean towards having the mainnet conf for now. I think it's heplful for understanding the wait times they can expect on mainnet. We could also ask people to exit voluntarily, that would also help if people exit cleanly instead of just shutting down their nodes. **Danny** agrees, says he'll put it in.

**protolambda**: We're working on some shorter-lived testnets that are just focused on genesis, so that we can have a config file that's ready to go into clients through genesis, and then repeated over and over again ideally. This is something we can run in parallel, that we want to run genesis more often and to enable us to configure the clients without changing the internals.

**Danny**: That looks like `--datadir` in Lighthouse, a very specific testnet configuration? What do you think, do you want to do one very short-lived genesis every week until genesis?

**protolambda**: Sounds good, right now we'll focus on the Pyrmont genesis. After that it does help to repeat genesis more often.

**Danny**: We've seen time and time again that genesis can be brittle, we've seen minor issues pop up in our testnets, so that's the motivation right there.

**Jacek**: Sure testing genesis is good, but there's no expectaiton that we'll launch mainnet wihtout a baked-in mainnet in time. I think everyone is baking in and expecting people to run with this baked-in state on 1.0 day.

**Danny**: But we've also seen other issues, following eth1 issues, state mismatch issues, bootnode issues, I think those are the major ones, and general not finding peers issues. Maybe not every week, but I would want to get another couple in.

**Jacek**: But it is super important that people should know to update their clients close to genesis.

**Danny**: I agree. If you're validating at genesis, you should expect to be updating and to be very active at that time. Sigma Prime's communications in their blog post were very good, if you want to communicate to your users in a similar way, that would be very valuable.

**Dankard**: To remind everyone, I think I posted this in everyone's issues, to have some way of quickly updating all of your users so that even if you want to push something like an hour beofre genesis then you get all the stakers, and don;t just leave it to chance, I think everyone should have an email list for critical issues. **Danny** agrees


#
# **3. Client Updates**

| **Video** | [19:10](https://youtu.be/yFjs_tB6I-Y?t=1150) |
| --- | --- |


# **3.1 Nimbus (Mamy)**

Very busy last two weeks starting with networking we have improved resource tracking, so in the past it was futures and memories, now we're tracking streams and channels. We also fixed some gossipsub audit issues, this was done late because goissipsub wasn't tested enough 3 weeks ago when it was time to be audited, so we tested it later. On the coparts we had a Toldeo release, we are using gossipsub 1.1, a lot of documentation changes. Regarding Infura, some said they didn't like being forced onto websockets, we now have https support. We have also significantly improved eth1 chain sync and monitoring and we prereleased 0.6 two days ago with prebuilt linux binaries, planning to do a new release today. With that we are gradually moving away from makefiles, and will provide precompiled executables for all major platforms. Right now it's Linux, but we also plan for Windows and ARM builds.

We are also significantly reworking release management for mainnet. We are creating sanity checklists. We will create mailing lists. Some monitoring and coverage plan for team members, and we have lessons leraned from directroy rename, all permissions changed for security because it created trouble for users that were holding databases used in systemd automated scripts and don't work after changes we've made. We'll improve how we deal with breaking changes. Also we used to have a way to create and validator keys in Niumbus to avoid confusion and scam attempts this is now undocumented and developers only, only one way to deposit, and it would be the EF launchpad.

# **3.2 Lodestar (Cayman)**

We have not yet released a new release of Lodestar. We've been trying to get to a full-spec 1.0 candidate, and at this point we've got it down to everything other than discv5.1, that's what we'll be focusing on this week. We finished with a rough draft of our BLST integration, we may hold off on that until we can address the browser compatability issue, because right now it only works in Node.js. We've gotten about 80% of the standard API, almost everything other than validator status endpoints which are possibly in play, and our validator is using the standard API, which is good.

# **3.3. Prysm (terence)**

In the last two weeks we have closed all issues from our Trail of Bits audit. The audit report should be online. We've made improvements to our initial syncing process, we've made it better at exploring forks during non-finality. Currently working on conforming to the ETH2 standard APIs, and working on testing peer scoring as well, also on the slasher interchange format. The most important thing we're working on for our mainnet release is a set of issues that we want to close before Nov 24, you can track those in the milestones within the repo.

# **3.4 Lighthouse (Paul)**

Last week we published our plans for a 1.0 release. We're encouraging everyone to update in the week before genesis, so they can get genesis state, and don't have to listen to ETH1. If you're going to be using Lighthouse, I  encourage everyone to read the blog post. we're also working on the standard API, plan on providing feedback to the spec. Our implementation is quite close, we're working on events right now. Slasher is in final review stage, release next week is likely. We're running 8 slashers on Toledo. We're setting up a production staking and monitoring structure. Our second Lighthouse security review has been completed, no criticals were found, working on issues that were raised before genesis, and we're feeling pretty confident about genesis, everyone working hard to make it.

# **3.5 Teku (Anton)**

We have published a mainnet-ready release, and will be making default in the updates next week.  Common API is mostly completed, and are going to duplicate the legacy API in the next weeks. We have completed almost all spec release candidate updates, last one remaining is gossip messageID, now ready to be merged, will be in next release. We added a feature to support snapshot sync from a state alone, it's actually very effective, allows to get up and running in a few minutes. We have made significant improvements to memory consumption by utilizing proto array more widely. We also have some serious issues one related to out-of-memory after long periods of non-finalization, another one is related to stability of Geth on Eth1 mainnet, and also a workaround transaction size limitation in Infura.

#
# **4. Research Updates**

| **Video** | [28:05](https://youtu.be/yFjs_tB6I-Y?t=1685) |
| --- | --- |

**Aditya Asgaonkar**: About weak subjectivity. Lighthouse, Prysm, Teku, and Nimbus support weak subjectivity sync starting form a block root, and we have at least one block explorer who will be an ETH2 weak subjectivity supporter from genesis, that's Etherscan, beaconcha.in will do it slightly after launch. I'll be making a release for the weak subjectivity server that everyone is encouraged to run, it's a great job everyone. ETH2 will have weak subjectivity security from day 1.

**Vitalik**: On data availability sampling phase 1, I wrote up kind of a pre-spec of 2 versions of data availability. One basically assumes the beacon proposer is the bottleneck for all blocks, and another that assumes the shard proposers are the ones with the main responsibilities. We're still in the process of discussing them and understanding what the tradeoffs are, understanding what the tradeoffs of having a formal in-protocol chaining of blocks versus not bothering with that, and a bunch of other finer-grained tradeoffs. Generally moving forward and trying to get to a concrete spec as soon as that makes sense. In addition, there are still small research questions, data availability sampling popping up, how to verify proofs of a block size as efficiently as possible, so just working through those two. Another spec related thing I've started to do, I did a draft PR separating out the light client spec into its own file, theoretically independent of phase 1. The goal is to modularize the phase 0 thing so we're not hamstrung into a particular order, and we can do things in whatever order they're ready. The light client changes are very simple, should be able to do those fairly easily, so the PR exists.

**Mikhail Kalinin**: TXRX has a small update, we're working on the executable beacon chain proposal, enshrining Eth1 execution into the beacon chain, making it a first-class citizen with regards to consensus. Compared to Eth1 shards significantly reduces the communication complexity between execution and data shards, and opens an opportunity for advanced use cases like instant deposits and withdrawals, and other use cases that require synchronous processing of ETH1, document is almost ready, and will be published soon.

**Leo (BSC)**: (shares screen) we did a short experiment with all 5 clients, wanted to see how they would behave in terms of resources and syncing with the chain. Time is in the x-axis, we would run them for 1-2 days, sometimes even close to 3 days sometimes they would crash. The y-axis current slot in thousands. We can see for example that Lighthouse and Prysm are faster for syncing, Lodestar takes four hours to begin syncing. Lighthouse has a couple of flat moments in hours 10-12, I'll come back to that. We also montior the number of peers, Teku is connected on average to the most around 70, Lighthouse around 50, but there are hours where it drops sometimes, something happened at this point, not sure what, we'll come back to that. Prysm is always around 30, very stable, then Lodestar and Nimbus are also kind of stable, between 20-40 peers.

We analyzed disk usage, double y-axis because we wanted to check how disk usage interacts with syncing the chain. We see Teku has an interesting behavior, a kind of zigzag repeated regularly, believe there is some kind of cleaning provess that makes this pattern, maybe one of them can explain this better. Nimbus and Prysm have pretty low disk usage. A weird thing happens in Lighthouse that it spikes after hour 3, then drops again, increases until hour 19 or 20, it may be a cleaning process. It arrived at the point that it consumed the whole disk, it crashed at that point, then flat lines. All clients were running on the same node, but at different times.

When we go to CPU usage, Prysm, Nimbus and Loedstar usually around 50% CPU usage. This is a node with one core but two tracks.  Teku and Lighthouse on the other hand have about 100% utilization of the CPU except in the moments where the synchroniztion load becomes flat, we see there is a clear single core usage of CPU at that point. That also happens for Prysm at some point, maybe hour 35, the syncing line became flat and there was serious CPU usage for one hour or so. 

We also measured memory, Teku and Prysm use more memory. We had about 5GB memory. We see a periodic sharp decrease in Prysm, don't know if it's some kind of state cleaning or something else. Nimbus is really made for light hardware and requires little memory usage, and in between we have Lighthouse and Lodestar, again Lighthouse has these flat lines when there are desynchronization issues.  When disk usage starts to increase we can see memory also increases until hour 24 when it becomes flat and memory decreases and becomes sort of flat. We also analyze network, but I'm going to stop here to try and keep this short. We plan on publishing, so if client teams can provide explanations for osme of these things, please reach out and discuss. I'm going to post a first draft in chat.

**Mamy**: When did you test?

**Leo**: Mainly last week, we can provide exact dates and which version of the clients we used. It's not in the draft I'm going to link right now, but we can add it.

**Danny**: In the future instead of going over it live, post before, and then we can jump straight into questions.

#
# **5. Networking**

| **Video** | [40:32](https://youtu.be/yFjs_tB6I-Y?t=2432) |
| --- | --- |

**Danny**: Thank you for the feedback of the issue I posted a few weeks ago, I've had my hands full with things, but I have a work-in-progress PR to update based off of that conversation, and I'll get that up today, that's about how to handle block sync and weak subjectivity and some edge cases there.

**Adrian Manning**: We've tested some of the scoring parameters that were being suggested for Toldeo, seem to be working well, we've merged it down to master, in case anyone is looking for scoring paramters.

**Danny**: Have you run an adversarial node there to see what happens?

**Adrian**: Not yet, I'd like some validators, I'm going to talk to proto about that.

**Danny**: You were working on making a modification to a client to make it evil, is that still in progress?

**Adrian**: Yes, but it's currently on hold because we're focusing on mainnet, but I should take that up and get it back in to test the scoring.


#
# **6. Spec Discussion**

| **Video** | [42:17](https://youtu.be/yFjs_tB6I-Y?t=2537) |
| --- | --- |

**Vitalik**: What do people think of unbundling the post-0 items more and treating them as separate components with no sense ofsequential-ness. The ones I'm thinking of are sharding, light clients, and the merge.

**Danny**: I'm pro, especially because on sharding and the merge there is a lot of R&D going on, timelines are unclear. I think it would be good to have light clinet infrastructure begin to be developed before.

**Mikhail**: I think it is a very good idea.

**Ansgar**: Wasn't the point that there should be light client infrastructure before the merge? You could basically continuously have light client support for Eth1.

**Vitalik**: Light client support before the merge is strongly preffered, but I'm not so worried because out of the three, light client support is by far the easiest. I'm even recommending we put it into the first fork after genesis, five months after or whatever if we can.

**Danny**: From a consnesus standpoint, light client support is extremely minimal and resuses infrastructure we've been using, gossip and a committee. The complexities of supporting we can build on after. But getting that native support into consensus is easy, and it should ship ASAP.

**Ansgar**: Do we still think phase 2 will have any meaningful instantiation, or is it an outdated term?

**Danny**: It is probably an outdated term in that it implies that it will happen. I tihnk we have enough on our plate with data availability, sharding, and a merge to get done and see how the rest of the ecosystem develops. If in the meantime the use of data availability for scaling is a total, unbelievable flop, it would be information for moving forward with a phase 2, but in terms of R&D efforts, definately on ice right now. **Ansgar** concurs


#
# **7. Open Discussion/Closing Remarks**

| **Video** | [46:10](https://youtu.be/yFjs_tB6I-Y?t=2770) |
| --- | --- |

**Danny**: EF grant stuff (long)
The EF announced a staking community grants round, anything that enhances and supports things beyond core client infrastructure, so if you're listening and you're building stuff that makes the validation experience more delightful or want to build something in that domain, I'll put it in my blog. Client teams, if there are things you want to see that aren't on that list or teams you want to get involved, please share.

**Aditya**: I wanted to bring attention to the slashing database regeneration bloom, which seems especially important to people staking at home, and on unreliable storage media like SD cards on Raspberry Pi. Does anyone have any idea how hard it might be to implement and what it might take to get it through?

**Danny**: So this is specifically looking at consensus and constructing the slashing database from messages that got on-chain?

**Aditya**: Yes, this is for the condition where you have backups for your validator keys and everything, but the storage media that you are using for the machine running your validator fails, so you lose your slashing database, but you have your keys so you can restart your validator, and you would have to regenerate your slashing databse from on-chain data.

**Danny**: Which potentially gets you in a good place, but not guaranteed. This could be done independent of the clinets now that we have this interchange format, maybe we want to support a script that uses the common API independently and then you can bring it in to any client, instead of asking all the clients to implement it at this point.

**aditya**: I'm asking for opinions about how tough or easy this is, and what the best path is.

**Paul**: If we're going to regenerate it from on-chain, we're neevr going to get things from way in the future, like a few hours from now, we're only going to get things up to the time now, because they're the only things that exist on-chain. Maybe we just use the slashing interchange format with a low watermark from now or the last epoch instead of going through the history and collecting everything. And from now or last epoch just never produce an attestation again.

**Danny**: That makes sense. The format does have this minimal format where it says don;t do anything before now.

**Dankard**: That stops you from joining a chain, it's not finalizing. Most of the time it solves the problem, but there are times where you would want something more.

**Danny**: If justification isn't advancing you wouldn't be able to produce an attestation.

**Dankard**: It's never going to be perfect, it could be someone got an attestation and never published it, and they just use it to slash you later, but I would guess this is very rare, most of the time you just innocently lost your storage.

**Paul**: That's a good point, you could also argue that if there's not much finalization there's potentially a lot of forking , and it's not super safe in that case.

**Dankard**: An ideal implementation would search mempools and block explorers.

**Danny**: I suppose a block explorer could provide it as a service. I have a question related to that, Paul mentioned if you sign things far in the future and broadcast them, and that in particular is an issue, becuase you can create these surround conditions, Dankard brought it up in ethresear.ch, a small note from the validator guide made it into therecent release, essentially a validator should protect itself from signing things that advance time in unexpected ways in the future to prevent these inescapable message signing that create really bas surround conditions. Are clients aware of that, and is there any effort to try and protect users against this case?

**Paul**: Not from our end, and it gets into some hairy territory, you're in to timing territory, you can't trust your system. I wasn't aware of it, and I'm not aware of any work to mitigate it.

**Dankard**: I would recommend to refuse to start the validator client if the last entry in the slasher databse was x hours in the future, like six hours, which shouldn't happen in operation, and if you're restarting after an outage then there should be an operator present, and they should be able to set a flag that says 'yeah, I know, start it anyway'. That should be a simple solution that should cover pretty much anything.

**Danny**: The issue is concerning, if someone gets you to sign the last epoch of all time, then you've created the ultimate surround condition for yourself. Client teams think about it, and we'll bring it up in internal chat, how we can protect the users there.


--------------------------------------

# **Appendix**

## **Resources Mentioned**
- https://blog.ethereum.org/2020/11/13/eth2-quick-update-no-20/
- https://blog.sigmaprime.io/beacon-fuzz-09.html
- https://raw.githubusercontent.com/leobago/BSC-ETH2/master/report/Clients_behaviour_report.pdf




## **Attendees**

- Aditya Asgaonkar
- Adrian Manning
- Alex Stokes
- Anton
- Ben Edgington
- ben@sigp
- Carl Beekhuizen
- Cayman Nava
- Dankrad Feist
- Danny Ryan
- Hsiao-Wei Wang
- Jacek Sieka
- Jospeh C
- Justin Drake
- Leo BSC
- lightclient
- Mamy
- Mehdi Zerouali
- Mikhail Kalinin
- Paul Hauner
- Protolambda
- Raul Jordan
- Sacha Saint-Leger
- Terence (prysmatic)
- Vitalik Buterin
- William Schwab
- zahary

## **Next Meeting Date/Time**

Thursday, October 26, 2020, UTC 1400
