# Ethereum 2.0 Implementers Call 45 Notes

### Meeting Date/Time: Thursday 2020/8/6 at 14:00 UTC
### Meeting Duration:  1 hr
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/171)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=DVePZUQOyFk&feature=youtu.be)
### Moderator: Danny Ryan
### Notes: Alita Moore


-----------------------------

# Contents

- [1. Testing and Release Updates](#1-Medall-testnet-launch-postmortem-and-status-update)   
- [2. Testnets](#2-Testing release updates)   
- [3. Client Updates](#3-client-updates)   
   - [3.1 Lodestar](#31-lodestar)   
   - [3.2 Nimbus](#32-nimbus)   
   - [3.3 Teku](#33-teku)   
   - [3.4 Prysm](#34-prysm)     
   - [3.5 Trinity](#35-trinity) 
   - [3.6 Lighthousee](#36-lighthousee)   
   - [3.7 Nethermind](#37-nethermind)   
- [4. Research Updates](#4-research-updates)   
   - [4.1 Secret Single Leader Election and Zero Knowledge Proofs](#41-Secret-Single-Leader-Election) 
- [5. Networking](#5-networking)   
- [6. Spec Discussion](#6-Spec-discussion)   
- [7. Open Discussion/Closing Remarks](#7-open-discussion)   

-----------------------------

# Summary

## Decisions Made:

Decision Item | Description
-|-
**45.1.1** |Discuss potential launch-pad issues by either reaching out to Carl directly or by submitting issues on the repo |
**45.1.2** |Delay the launch from Genesis to 96 hours; this has many benefits |
**45.1.3** |lacking traits of the current debugging suites:
                - The ability to visualize vaults building in real-time ~ this will allow for the extraction of non-standard data structures
                - Ability to understand why clietns aren't performing optimally |
**45.1.4** |Nimbus timeline updates
                - switch to dlst next week due to medalla groups overwhelming
                - audit on second phase on the becon node will start in ten days|
**45.1.5** |Zero knowledge proofs may allow single leader election possible in phase 1 |
**45.1.6** |Dankrad is working on implementing secret shared validators, look for updates on the secret shared validator channel on discord for updates |
**45.1.7** |Leave the client information in because it doesn't add tangible benefit to security but adds value to the debugging teams |
**45.1.8** |Review the discussion on including client versions later |

# Action items

Action Item | Description
-|-
**45.2.1** |Do at least one full production simulation dress rehearsal on a testnet with a lower minimum eth requirement and a stated end of life from the genesis block of approximately 3 days |
**45.2.2** |Danny will spread the word about other clients when they become more stable over the next couple of weeks. The goal here is to reduce prysm's dominance on the network |
**45.2.3** |Keep your eyes out for changes to the peer scoring protocol in the next week or so |
**45.2.4** |Decide on a recommendation for if the signed peer record collection functionality should be on or off for gossip 1.1 |


# 1. Medalla testnet launch postmortem and status update
Video | [3:06](https://youtu.be/DVePZUQOyFk?t=186)

(Danny) - Welcome, everyone! Congratulations on the node launch, lots of fun, but things are looking stable; I also note that we have ongoing issues being work on by the client team. The first thing on the agenda is to just talk through and kind of enumerate what happened leading up to the launch to better understand some of the things that went wrong and what went well. So that we can keep our eyes out moving forward. Based off of this call, I'll circle back and fill in more details in the document, and if there's just for reference and maybe highlight a few points / sticking points that we should double check next time that we go through this. I did write up a few of the things so I'll go through that document; pretty much we have prelaunch and post launch the week before the launch we definetely had a number of issues with launch-pad. Primarily around installation and usage python. There was an effort to get binaries prepared but that was not completed in time for this round. I think that would solve a lot of issues, and those probably makes us question if python is a reasonable choice at all. Lots of feedback has been heard and there's kind of rapid changes based on that feedback. We expect better UX in the future. ? was found at 17:27 august second, clients agreed it's good, but after geen simpo was found that's when clients started appearing. We noticed a range of issues at this point. This is what I remembered and we can find in our documents, but the light house boot node was down, the prysm boot nodes had the wrong ports and so could not be contacted, the prysm release until august third around 13:30 did not actually have boot nodes set and so those peers that had turned their nodes on early had zero peers. I believe the boot node included by Teku was just quite simply the wrong epoch; those issues led to a mildly stressful sunday for some, scrambling to try and debug, and it also led to a number of required updates by node operators to be able to appear the general system. The ideal is to get a boot node running, connect to peers, and we're good. We did not hit that ideal. Some of this is prety obvious, getting the boot nodes correctly included. And there was a prysm Teku meta-data issue. I don't know exactly what was going on here, I know there were a lot of errors going on at this time. I know there were plenty of other small changes going on (last minute things). Does anyone have anything to add to the pre-launch discussion?

(Justin) - One thing that I noticed was some people were making deposits for 64 ETH for 96 ETH, my guess is that maybe a bit more education should be made to say that if you make a large deposit that doesn't mean you'll have multiple validators.

(Danny) - I think we should find those; if you look at prysm's faucet channel, we can track down why they made that mistake. was it a took or a misunderstanding? Let's make a note of that and try to track down some of those users.

(Ben) - In my case there was a bug in launch pad that made a double deposit for a validator which was a bit of a surprise.

(Danny) - Gotcha, so that was two discrete deposits rather than a 64 deposit

(Ben) - correct, two seperate 32 deposits, I left it at the time

(Carl) - the launch pad wouldn't allow you to upload the same deposit data

(Ben) - Yeah, I did it once, I had 64; I was doing 64 deposits at once. this took 45 minutes, 65 of them must have appeared, I had 65 deposits of 32 ETH with one validator having two deposits. I followed it exactly as designed. (with metamask)

(Alex) - I used metamask, so maybe it's something with that. I had the same thing happen to me, if it was maybe a transaction go confirmed and then got sent twice or something.

(Danny) - because of the way that knox works that like a double signal for metamask to create two transactions so it's not possible

(Dankrad) - One thing could be to talk to metamask to fix that UI bug where it opens like all the windows at once

(carl) - one thing we're trying to address on the launch pad side now is to wait until the callback comes back from whatever you've done on the metamask side before initiating the nest transaction so it'll just be linear. Once you click confirm or reject it will load up the next transaction for you.

(Danny) - Thank you Ben for the potential bug. Let's table the rest of the launch-pad discussions, maybe Carl where's the best place to have these discussions? Or we could have a call to discuss more stuff, but I don't want to delay on the launch pad too much right now.

(Carl) - Yeah, either hit me up directly, or issues on the repo are the best places to address those.

45.1.1 | Video | [10:46](https://youtu.be/DVePZUQOyFk?t=646)

    Discuss potential launch-pad issues by either reaching out to Carl directly or by submitting issues on the repo

(Danny) - Other pre-launch things that I missed?

(Terence) - It seems like from my experience that genesis of two days may be short; does anyone feel the same way? I felt that delaying the genesis more might be a good ideal

(Danny) - I was thinking 96 hours, 4 days minimum. I've said that sometimes in other channels but I haven't made it abundantly clear. I think for the VU1 release, which I think will primarily just have some mainnet parameter changes (like configuration changes) 96, you could argue a week.

(Terence) - Yeah, I'd agree with that

(Danny) - Another nice thing and I think some clients are doing that, is cutting the release when the genesis parameters are known with genesis state. So, most if not all valid users are following an ETH 1 chain, but there's also a class of users whom aren't validating and whom don't have to follow the ETH 1 chain. So it's nice to have them, have the state, to not have anyone with hours to have them process a log. So there's a lot of benefits there.

45.1.2 | Video | [12:15](https://youtu.be/DVePZUQOyFk?t=735)

    Delay the launch from Genesis to 96 hours; this has many benefits

(Danny) - Other prelaunch items that we learned? Okay, great so then leading up to the launch, thanks again eth seaker guys that was a really well organized call and doing something like that for mainnet will make a lot of sense. I posted some quick things that we would be looking for on that call; very kind of end-user things that people can look for: early blocks, participation are the main things. The initial epochs came out, we got early blocks, we definetely had some sparseness in those blocks but like we weren't tracking that to the T, we were just kind of saying there's some blocks here without an exact percentage, but it became obvious after epoch zero we ran some it against the APIs that we had. I think maybe 57% on the initial epoch, but during epoch 0-4 we had something similar to 52-58% so after a couple of epochs it became clear that were not going to have justification of finality out of the gate; at which point we began scrambling in different position. I think caymen on the call said that gossip was overwhelming load-star.. at least that was the declaration at the time, I'm sure there's other justifications since, Zaher was also saying I think in an Eth node chat that they saw problems with our nodes and were investigating, at 21 after the hour meran said he was running a validator node successfully but he was lacking peers so only one ? got included. We had some client errors on both load-start and nimbus which accounted for at least 10% of the network just from the client team. Each client team was runing about 10% of validators so there's some of it. But we also began to look through the gorallia mediia whale deposits that we tracked before and we noticed there were a handful of about 5% users that were offline. Participation began to start climbing to about 62% at the end of epoch 5; I was able to reach out and contact one of the 5% users to do the prysm-faucet tracking, they responded with "just started them up, shoudl be going now, slight time-zone hiccup on my side" I suspected that maybe he had prysm running but it didn't appear so due to the lack of boot nodes from a couple days ago but I had not investigated that theory. At the end of epoch 6 we had participation of about 69%; I believe at the end of epoch 8 or 9 we finalized epoch 6. So we had finality and another thing I noted was that at about 14:30 caymen confirmed that the load-start validators moved to our virtual lightstar node contributing to an additional percentage. We saw definetely over the first handful of hours waves of participation and we were getting into the low 80%. Which is the highest we've been, and over the night I think many lighthouse users went offline, and so we saw early in the morning in the US there was some drop in percentage likely due to lighthouse failures. I believe these are still under investigation. At the same time there were around that morning the second day, there were a number of prysm nodes that had a sequence of maybe 6 to 10 epochs with no actionzations[?] I'm not certian, I believe there was a couple of critical fixes introduced by prysm that morning, I don't know if they've had any issues since that morning. There are ongoing investigations with load-start and nimbus, the network generally looks healthy, there's a ton of stuff going on that's not immediately noted here, but I noted primarily the things that affected here during the launch. Generally, things look stable, Congratulations all around, we are learning a lot. Is there anything to add to just that sequence of events or just the discussion around them?...

(Danny) okay, so honestly I think there's a lot of take-aways from the prelaunch, the post-launch there's the technical issues there are quite frankly just things we need to work through and we need to find stability in the next couple of weeks. I am considering between now and mainnet launch doing one or two production launch simulations or full production launches. But on testnets that have a lower minimum eth requirements and a stated end of life of approximately 3 days so that we can give users a chance to have another dress rehearsal and have us work through any emmergent issues in the genesis process that might come up. I think doing at least one of these makes sense, any feedback or ocmments on that?

45.2.1 | Video | [18:44](https://youtu.be/DVePZUQOyFk?t=1124)

    Do at least one full production simulation dress rehearsal on a testnet with a lower minimum eth requirement and a stated end of life from the genesis block of approximately 3 days

(Justin) - That sounds great to me, one minor prelaunch thing that I forgot to mention was like sometimes it feels like people are making the assumption that the minimum gensis date or whatever the account is [cuts out] as apposed to that being predicated or there being sufficient validators. So maybe there needs to be more education on highlighting that possibility.

(Danny) - I agree, we are definetely, even internally, just planning on saying this is very likely the date, and I think we all know that this isn't necessarily the date but even giving a four to seven day lead time also helps with the communication around that too. [THIS REFERENCES 45.1.2]

(Mamy) - Also it would be good to have a training tree and nevermind frozen next launch because we didn't participate in this one, so I suppose they'd also want to try their hands at being an early validator. 

(Danny) - I can't speak for those teams, I know that they're both in a .. yes, but they're certainly welcome to join if and when they're ready. [references chat] Does anyone have anything to add just in general about medalla testnets?

(Justin) - One thing that we all saw was that the prysm is dominating the network it seems. At least maybe according to the ether nodes dot org, like significantly over 50%; I guess maybe we should be putting more effort to try and reduce thise dominance just for the health of the network? 

(Danny) - I agree, I think that a lot of people are trying to communicate on twitter and to get the word out about different clients. Then as these other clients stabilize over the next couple weeks I will do the same.

45.2.2 | Video | [22:14](https://youtu.be/DVePZUQOyFk?t=1334)

    Danny will spread the word about other clients when they become more stable over the next couple of weeks. The goal here is to reduce prysm's dominance on the network

(Justing) - The other thing that I kind of.. this is a question for people, do you feel when there were issues during launch that you had the sufficient debugging tools to investigate them and understand where they were coming from sufficiently quickly? Or do we still have significant work to do there as well?

(Nishant) - Can you clarify what you mean by debugging?

(Danny) - Insight into the network and the clients; the tools that we use, API endpoints, peer store dumps, metrics.. anything that we use, and this is from my understanding kind of overgrowing and as we have issues the tools are overexpanding, but does anyone have any insight on that?

(Zohary) - We have been planning to devote a similar tool to ermanny [?] for quite some time and I think it's true that the client keeps specific data structures that are in the terminal but they also have some common structures that would be useful to visualize in real-time to visualize how the vaults are building in real-time and if there's a common tool or something like a dashboard that is using the RPC interface and displaying this information then it would be helpful.

(Danny) - Yeah, I agree; It seems from my understanding that the most opacity that we have is on the gossip and probably specifically on once my nodes say that I have sent napistation what was actually happening, because frequently I think that once basic stability has happened there's then the question of okay then why is my client not performing optimally, we really don't have much.. I don't think we have a good way of viewing that right now. 

(Terence) - A tool that has been really helpful for the block explorer is the huge map validator IDE to your eth 1 address which you also match to your username. Which, I am not advertising this for mainnet of course because of validator privacy, but this has been useful for finding out which validators are online and whom to talk to.

(Danny) - And being able to traceback faucets to users has been very very useful in the past.

45.1.3 | Video | ~[24:30](https://youtu.be/DVePZUQOyFk?t=1470)

    lacking traits of the current debugging suites:
        - The ability to visualize vaults building in real-time ~ this will allow for the extraction of non-standard data structures
        - Ability to understand why clietns aren't performing optimally

# 2. Testing release updates
Video | [25:40](https://youtu.be/DVePZUQOyFk?t=1544)

(Danny) - testing release updates, I don't think we have a lot here; there was a d0120[?] release maybe right after the last call, most of you were very aware of that. There were a number of gossips of v1.1 params that were related, primarily peer scoring that have defaults that are generally built into the protocol, but we are investigating these parameters so if there are any changes then it would be zero twelve three would be in order in the next week or so, so keep your eye on that.

45.2.3 | Video | [26:23](https://youtu.be/DVePZUQOyFk?t=1583)

    Keep your eyes out for changes to the peer scoring protocol in the next week or so

# 3. Client updates
Video | [26:30](https://youtu.be/DVePZUQOyFk?t=1590)

## 3.1 Lodestar
(Danny) - **load-star**

(Cayman) - So, we're basically working through some of the issues we saw in madalla launch, namely gossip validation and peering. We're seeing some issues where we don't see many peers and maybe some of is that we're not starting gossip immediately and peers are taking us because we're not supporting that protocol out of gate; but we're basically working through these stability issues, and we're thinking we'll be ready / back at the testnet in a few weeks when we nail everything down. 

(Danny) - So you're seeing high load maybe from gossip verifications; so those conditions that you decide before you forward things

(Cayman) - No, it was probably bugs in our lock-verifications where things were silently failing so seeing things like we weren't getting blocks maybe when we were or and then that also we didn't have very many peers so we weren't getting many gossips anyway; It was the opposite of getting chocked, we were thirst for gossip.

## 3.2 Nimbus

(Danny) - **nimbus**

(Mamy) - So we've been working on the madalla; we have identified 4 issues, there might be more, and we fixed two. The first one is that an increased number of attestations within limits in the gluecode between lipitooky and coney nodes [?]; in particular, in the pred of non-finality we are doing the same one multiple times when we receive the same attestations from the same block multiple times. So we fixed this. This was a source for high slowness, and number one is an attestation processing bug. We want it to optimize the data base loading by delaying the de-attestation of the public keys and signatures. We explored two approaches and unfortunately the first one that emerged had a significant impact on sync; it was reverted and we are not using the second approach. Which, gives the expected benefits but has no impact on the resources tank. So this is fixed too. As two of our bugs are still being investigated, so number one is medalla blocks are often filled to the maximum of 128 attestations, and we are reaching the limit of medalla groups. So we will switch to dlst next week; otherwise we also have race-condition on incoming and outgoing requests from the same peer. Which, led to issues for example with lighthouse. Also, we have multiple reports of low peer counts but expect it is due to the long times spent on processing orvell's attestations. And this makes us node-less reponsive to the network; then we get kicked by peers. So this is for medalla, otherwise on the audit side; our auditors finished the first phase of our audit which focused on networking. We are also fixing the issues raised during the audit and the second phase which will be on the becon node. We start in ten days.

45.1.4 | Video | [31:08](https://youtu.be/DVePZUQOyFk?t=1868)

    Nimbus timeline updates
        - switch to dlst next week due to medalla groups overwhelming
        - audit on second phase on the becon node will start in ten days

## 3.3 Teku

(Danny) - **Teku**

(Ben) - That is me; so we finished integrating the blast dls library and we merged it in. It is showing some very useful speed upgrade over our previous melagro jvm version which was particularly so. So we're getting about a 7x speed up, we are going to keep the jvm version around just in case we come across architectures that the blast library doesn't support. But one day we might deprecate it. Basic slashing protection is done now at the individual validator level; internally, we're working on splitting out the validator process from the becon node process so that works into news well. As we go on with that we are implementing the new API endpoints as they become relevant. We've been migrating a lot of our storage APIs from synchronous to asynchronous and improving the robustness of the networking the face of the johnny attack. that is, handling denial service attempts more gracefully. And just dealing with a whole bunch of bugs, usability bumps, general overall improvements everwhere. Finally, we're just closing out our security assessment RFP. We've got a good range of responses and we're interviewing vendors this week with the view of appointing someone at the beginning of next week. That's it!

## 3.4 Prysm

(Danny) - **prysm**

(Terence) - Over the last two weeks before genesis we shipped a coms management V2; which contends implementation of direct riot and revolt key managers. We also integrated that with the launchpad steps and made sure this is documented and well tested. Up to genisis we have mostly just seen bugs and issues that came from that. We also had a few becon node related bug fixes since genesis as well. We found a few defficiencies around that part. After genesis we have seen a surge of users join our discord and asking questions. Most of their questions are regarding what to do when you rob validators, and how can you tell if the validator is running a test for that. So therefore we have also updated our dars portals as well to document all the steps on like what to step for when things are running correctly. That all folks!

## 3.5 Trinity

(Danny) - **Trinity**

(Alex) - the main thing for us has been looking at sync performance for the becon node; we were working with altona and of course nomadosha, we sped up things by like a couple orders of magnitude mainly with updates to the state transition which was really nice. The bottleneck now is dls performance, so we're looking at integrating dlst. Then otherwise just a bunch of miscellaneous networking things and p2p we've seen. While working to sync these different testnets. 

## 3.6 Lighthouse

(Danny) - **Lighthouse**

(Paul) - A lot of people were just working on fixing the things that we found during medalla; stability issues that we're working on that should increase the gestation inclusion; at least it should remove an edgecase that might not be included. We have a slasher functioning in isolation and looking to turning that on the real network soon (hopefully in the coming weeks). We have been working with the dlst people to ensure that bessy massive consensus, and also if we can make it a bit more portable so that it can run on many machines. We're still in talks about that but we're running dlst on medalla and it's going pretty well. We're staring on testing and working for weak-subjectivity stuff -- we have someone fulltime on that now. We are progressing with our validator user interface, we have a basic visual identity down for lighthouse, and hopefully we can a pub with us for some of that soon. That's it for me.

## 3.7 Nethermind

(Danny) - **Nethermind** .. okay moving on.

# 4. Research updates
Video | [36:29](https://youtu.be/DVePZUQOyFk?t=2189)

(Justin) - No research updates persay, but stuff that I've been doing for [?] zero is pushing forward the blast library and trying to resolve the edge-cases that have been found and also pushing for more optimizations and for more verifications are also in the works. I'm very pleased with all the results so far. The other thing I'm working on right now is trying to build a security team for eth 2.0; to start with basically finding bugs in the eth 2.0 client implemntations. The idea here is that eth 2.0 security is a public good and it makes sense for the EF to provide resources there for all the clients. I've had about 40 applications so far, and we're going to be doing interviews in the coming days and weeks. If you have folks whom you think we should consider please send an email to eth2security@ethereum.org;

(Mamy) - Is there a call for the security team because I expect my own security team would be eager to participate or even help you screen some of the applicants. So, our teams would be interested as well to collaborate on the scope of the role of this and how it interacts with our clients.

(Justin) - I'm more than happy to get people involved with this; at this stage, it's very early days, and it was; the message that was sent out was very broad and we're looking for all kinds of different types of people. So I guess we'll do a first round of filtering internally, and then when it comes to final hiring decisions we'll be interfacing with the existing security team at a different foundation that's currently focusing on ETH 1.0, and it also makes sense to focus with the security folks at the eth 2.0 teams. I have also been chatting with just security researchers in the broader ethereum ecosystem, for example people that have been doing that and things like that. There's definetely lots of people to get feedback from, and different folks have different opinions but the plan is provide more transparency as the funnel kind of becomes more refined. Feel free to shoot me a message on telegram for more information.

(Danny) - Other research updates?

## 4.1 Secret Single Leader Election

(Justin) - I don't know if I mentioned this last time, but there's basically been a pretty significant breakthrough for the secret single leader election; the most promising approach, which was the approach by dan bernay; which was very elegant, simple, and effective; basically he had two ways to be instantiated, either with zero knowledge proofs or with full proofs, the cleaner way forward is with the zero knowledge proofs. But the zero knowledge proof infrastructure is still somewhat nascent. There's still questions about trusted setup and things like that. It turns out that we believe that there's basically a talored zero knowledge proof for the very specific statement so we don't need general purpose zero purpose technology and the specific proof is built using discrete log assumptions. There's no trusted setup as with pairing groups. So this is an effort mostly from mary from a different foundation. It's making secret single leader election really promising. Potentially even for inclusion in phase 1 if things go well.

45.1.5 | Video | [42:21](https://youtu.be/DVePZUQOyFk?t=2541)

    Zero knowledge proofs may allow single leader election possible in phase 1

(Dankrad) - about secret shared validators: so we had a tech recall a couple of weeks ago [?], we are currently thinking about how to implement this, I think that one of the questions that I have is which of the client's teams might be interested in pushing ahead and implementing the api; which hasn't been specified yet. But I think that we will try that in the next couple of weeks, and it should only be some small changes to the validator api. But it will be nice to actually have one client that implements it so that we can get a prototype out there. If you're interested please contact me, I think it shouldn't be too much effort if you have that sort of capacity I think it would be really great if someone could do that.

45.1.6 | Video | [43:30](https://youtu.be/DVePZUQOyFk?t=2610)

    Dankrad is working on implementing secret shared validators, look for updates on the secret shared validator channel on discord for updates

# 5. Networking
Video | [43:40](https://youtu.be/DVePZUQOyFk?t=2629)

(Jonathan) - I had a comment / question; there's been some discussion around client distribution, and I think in general people are curious about what clients are being run, what version of software is being run; I know you opened an issue about potentially disabling the identify protocol. So I'm curious what the motivation for that is. Are we concerned about actually leaking what version of the client and what type of client is actually being run? If not, is it..

(Danny) - The reason I threw that up there was that it's an explicit confirmation that does not immediately provide a lot of utility to the network. It adds a lot of utility to us in debugging.

(Dankrad) - I wonder if in practice.. I would assume that building a scanner that could identify which client is running is not that hard. You find some characteristic of each client and then.. So are we actualy gaining anything by not providing that information

(Danny) - Yeah, you can do that..

(Dankrad) - So maybe we just leave it out there so this might be security by obscurity, and we are just removing a channel that we have to learn more about the network and do things like correct for client imbalances and things like that. 

45.1.7 | Video | [45:00](https://youtu.be/DVePZUQOyFk?t=2700)

    Leave the client information in because it doesn't add tangible benefit to security but adds value to the debugging teams

(Danny) - John you've discussed that you think the EFI protocol is a dos factory, do you want to talk about that?

(Jonathon) - I think it's just speculation, we were talking about how it's not necessarily anything more than a dos factory as maybe other requests, but yeah. I can repeatedly use rumor for example to generate a peer ID connect, hit you with an identify request, disconnect regions for another peer id, and it's possible I don't even need to continuously generate peer ids. So the question is 1) do we want to disable it for that reason? If that's the case should we throw it with that information in the agent strings useful should we put it in the EMR, if not then in general how far do we want to go with DOS protection in clients. With these repeated requests we want to do some sort of.. we want to recommend some sort of rate limiting by IP? Is that out of scope for clients? How far do you want to go with that?

(Danny) - Does the identify protocol, do it serve to be anything more than a DOS factory than something like a status request?

(Jonathon) - Well it's implemented in the P2P so at least for things like metadata and status our clients could specifically catch it and apply some sort of rate limiting in the client logic. 

(Danny) - The identify protocol doesn't actually make anything call back to the client software so we don't have much flexibility there.

(Jonathon) - I'm not an expert, but that's my assumption. Can anyone else speak to that?

[Very loud noises that make ears bleed]

(Danny) - Justin, your mic is unintelligible, sorry. Do you have an alternate setup? [ technical difficulties ]

(Cayman) - While he's getting setup, I wanted to say that one of the things that identify giz is the sign peer records. I don't know if anyone's using this but gossip subs 1.1 has this alternate discovery mechanism where if you prune a peer you can send all the signed peer records from other peers that you've collected. So the pruned peer will have an oppurtunity to connect to other peers that they may not know about, and those signed records are sent in this identity. 

(Danny) - Does the proces of V1.1 use that as default or is that a configuration?

(Cayman) - It's configurable to be on or off, so I don't know if it's actually being used.

(Danny) - We should consider making a recommendation of that being on or off and that can be part of the decision when we identiy protocol.

45.2.4 | Video | [49:21](https://youtu.be/DVePZUQOyFk?t=2961)

    Decide on a recommendation for if the signed peer record collection functionality should be on or off for gossip 1.1

(Danny) - That information is given in the identifier protocol?

(Cayman) - Optionally, yes.

(Danny) - I'm relatively convinced that it's not really buy much by turning it off, I think we could put it as a "may" in the spec, but I think looking into how it's using lots of sub and identifying if some of these protocols .. One way that I'd use it to identify faulty versions of clients is to faulty versions of clients and DOS specifically. Yeah, absolutely, that's definetely the concern there, if it makes it signficantly easier to identify clients. I suppose the identify protocol could be overwritten to provide less specific information about version.

(Cayman) - Yeah we could just change the agent string and just say something like "prysm lighthouse", "noscar" etc. in this and then you know the version. So that in particular would be fairly easy to fix, but we're concerned about knowning what the actual client is. 

(Danny) - Knowing the version is kind of nice, but it does provide more specific information. Like I haven't updated my node in 5 months and there's a known issue then someone can go and find it. Likely, I could potentially find that through some other type of information but maybe not as.

(Nishant) - Is this true for ETH 1? Like you can peg to different clients. This doesn't seem like a big issue for that.

(Danny) - Where is the information?

(Nishant) - Currenlty in EtTH 1.0 you can add in defy peers by their relative versions. So, it doesn't seem like a big issue because it's currently in ETH 1.0;

(Jacek) - Maybe we're asking the question the wrong way. Should we have a bar where we say that anything goes except for the things that we haven't decided a way to break. Or should our bar be that this bar has this particular use which motivates adding it, and if we will cut it that way, then will providing a graph on the webpage with client stats.. I don't know if that' really a strong enough motivation to add something which makes it cheaper at least to attack the network.

(Dankrad) - I disagree, this has much bigger benefits in knowning the distribution on the network for security reasons. So I think we gain more than an attacker does from it. Because an attacker can always make the investement if they're willing to break a client, then they can be invested enough to identify clients as well. I just don't think it's difficult.

(Danny) - In Jiah, both default ports just totally leaked the information at this point because the default ports are different. So we kind of already have that information there. 

(Jonathon) - Dankrad you make a good poitn about the version information, you know them being able to identify which version and them being able to attack them, but I would also argue that us having that information allows us to raise awareness; so for example we see that a lot of people are still running an old version of the client and we need to get the word out that the version should be upgraded. So in some ways it kind of balances it out.

(Dankrad) - I think it's in our favor to have that information

(Justin) - There is some power in removing it because it gives more power to the attacker. So an attacker could forge these things, and it would give the network a false sense of transparency and maybe people would become complacent and not develop the scanning tools that Dankrad was mentioning because they rely on this information that could trivially be forged.

(Jacek) - I would also say that we should be making the assumption that our users are competent and invested in their nodes. That includes keeping themselves up to date and having a healthy network. 

(Dankrad) - Right, but one of the things that we want is to have a diversity of clients. How do our new users know that they are not running the same client as everyone else if we remove that information?

(Danny) - Right but at the same time if it's trivial for an attacker to figure this information out, then we could probably figure it out too.

(Jacek) - The second thing is like if we are interested in our clients to validate then we should also be interested in them to make this decision about whether or not they believe in if this multi-client is reasonable. It's still a choice that they make, and we give them this power to make a choice whether they are plant A, B, C, or D and the distribution that falls out of that; we kind of believe that that is kind of a good distribution by trusting..

(Dankrad) - Not if they are lacking the information

(Jacek) - Well then we give them the information that they should be diversifying their nodes

(Dankrad) - Well how would they know that if they don't know which clients are running on their networks.

(Mamy) - Should we maybe move that to a specific call dedicated to privacy?

(Jacke) - I think we've made our points, so now we can think about it

45.1.8 | Video | [56:30](https://youtu.be/DVePZUQOyFk?t=3390)

    Review the discussion on including client versions later

(Danny) - let's take a breath on this one. I do want to better understand how gossip does identify, it does feel strange that the identifier protocol is kind of overloaded in that sense. So I want to better understand that. I do think that we can trivial link client information so that should be under consideration both in the for and against identifier protocol usage. I do hear you and I agree jacek, just because it was the default in ETH 1.0 doesn't mean we shouldn't be considering turning it off. I need to think about this one, let's take a breath for now. It's not critical that we decide today. Then the conversation can continue on another stream. Any last words?.. Other networking items?

(Protolambda) - [..?] new things in our networking system, and we can discuss our livestreaming call, and a new [?] then after that, after that it's just some smarter notes used to debug p2p communication between manjos and lighthouse it's already live; if anyone is interested in helping out in debugging p2p networks they can ping us. 

(Danny) - Other networking items?

(Danny) - preston brought up concerns around EIP 2334, "I believe in this EIP" he's saying "see the sand penumonic is used to derive using an hd wallet, both withdrawal potentials and active signing keys. This is certainly convenient but deciding on how you decide to recover your withdrawal credentials, if you're not using this on an airgap machine and then transferring keystores out of it, then you're exposing potential secrets on a hot machine and there are certainly a debate here and seeing the niceness of going H-path. Carl you wrote the EIP would you like the chime in?

(Carl) - I'm largely in favor of a stance, but I do appreciate that: having seperate pneumonics does spill over into other safety things. There's a strong argument to be made for not rederiving keys on a hot system. If you are in a meeting, then you are really trying to avoid that. But I'm curious to hear the counter arguments.

(Danny) - I think there's demand for having an alternative where your withdrawal credentials are fully isolated from your active sign in keys. For example I believe even just using hardware wallets in this type of setup is going to require these two things being decoupled. My understanding is that there is no way to export private keys from a hardware wallet, nor will that.. I don't even think that could be programmed into a hardware wallets. Hardware wallets are actually secure. Well, assuming you're using a pneumonic. But at that point if you use your pneumonic outside of the wallet then you're not even..

(Dankrad) - What you could theoretically do is to ask hardware wallets to be able to export the validator keys. 

(Danny) - Can hardware wallets even export private information? 

(Dankrad) - In two years for sure, this is all logic, right?

(Danny) - Right but the secure information is on a secure onclave

(mamy) - They prevent you from accessing it at all

(Dankrad) - They can provide signatures, right? So there's some software that's running on there, and if that allows you to export a certain derivative of the key, then.. So I have no idea how they're currently implemented but I'm sure that if they're already implementing a new BLS software then this is 100% possible. If that should be done is another question.

(Mamy) - So the hardware wallets gives you the pneumonic to recover your key, but that's all.

(Dankrad) - I'm simply saying that there's a software running on the wallet that can generate a pneumonic, and if you could modify that software to also generate a validator key then it could work

(Danny) - I'm not sure that's possible, I don't know enough about secure enclaves to make a strong argument..

(Dankrad) - My understanding of that is that the software for that is not yet finished, so it would need to be in the software that runs in the secure enclave for sure. But if you put it in there there's no reason it couldn't do that, typcially that's not something you would want; for example the software is written in such a way that it would never export a private key.

(Danny) - My intuition on that is that it smells funny, and trying to convert hardware wallets to export private information intuitively seems like the long path.

(Carl) - Another comment here is that hardware wallets use their current instantiations, and I'm 90% sure that they're not powerful enough to implement the required password hardening as an S script or pvkdf. So they couldn't export the current keyscroll formats even if they wanted to. 

(Dankrad) - I'm convinced it's the right way to do it; I think that for example, the secret shared validators. You'd want to create those secrets on the actual validator machines. Like seperately, you'd never want to create one single sequence. So, to me it just feels like there should be a way to support two seperate pneumonics.

(Carl) - But on the secret validator scheme you're not going to know what your keys are or whether they exist in a tree anyway. Your keys are entirely dependent on what other people choose as their keys, as in other portions. So them talking about pneumonics doesn't really make sense in that context.

(Danny) - So I think that we should do some thought and due dilligence on how this EIP or another EIP might be modified to allow the optionality here. My understanding is that especially the more sophisticated users maybe staking providers are going to be having their cold storage keys decoupled from their hot keys. In that case, it's probably best to have a standard that can support that.

(Dankrad) - I was actually very surprised that there was only one password and pass request, I was like "which one is it?"

(Carl) - yeah, but that's a semi unrelated topic that we don't give withdrawal keys; so I did update the wording the EIP to say that if you have a sufficiently good reason to not be following this exact process you may. Or if you can't use the keys at this location then you may deviate from it. That you should try to stick to whatever is reasonable. So there's some scope for doing this kind of thing if you really would like to.

(Danny) - How does that manifest; does that make it easier, does that allowance.. but not a specific specification. Does that lead to issues in actually developing software to do this specific use case?

(Carl) - Well I think that part of the argument would be that if you derived a specific specification for having two pneumonics then you're only solving one small problems but then there's other different keys that aren't afforded by whatever this new standard is. 

(Danny) - I suppose the reason for the standard is to capture enough of the use cases without overly complicating things.

(Carl) - I'd also argue that by the time you start to introduce more pneumonics then there's a lot of room for confusion as to how the system works.

45.1.9 | Video | [1:07:00](https://youtu.be/DVePZUQOyFk?t=4067)

    The general consensus around having two pneumonics is that it's likely unsupported by hardware wallets and also inadvisable due to confusion and generally introduces more problems than it solves. Though, this point is still contentuous, and therefore should be continued in the discord. This topic should be revisted later.

(Carl) - I think that from a security standpoint it's worthwhile, but I'd definetely like that this not to be the standard flow.

(Danny) - I'm going to suggest that we take this into the discord in the security keys channel; does anyone have any further comment, I don't think we have a solution today.

# 6. Spec discussion

Video | [1:08:36](https://youtu.be/DVePZUQOyFk?t=4116)

(Danny) - Ongoing work on phase 1, I just fixed a bug yesterday and did some tests, vitalik do you have some comments

(Vitalik) - Yeah, I've been working on my own annotated spec for sometime and it's move to the point where it's sitting in a repo now. So, if people want to look at that I welcome feedback. 

(Danny) - [ shares link ] okay, other spec items?.. Great, during the madness of madasha, proto launched a new multi client attacknet that has Teku, prysm, and lighthouse on it; 4500 validators and 15 nodes with increased and more interesting and target bounties. The singo client attacknets still exist, and if you look at the rules are to be used for specific client things. I don't think anything's fallen out of that yet. People of the interet will break it. Okay anything else?

# 7. Open discussion
..

(Danny) - Great, well happy debugging and congratudations on madash launch. Take care everyone.

# Attendees
- Herman Junge
- Danny Ryan
- Paul Hauner
- Terence
- Mamy
- Sacha Saint-Leger
- Ben Edgington
- JosephC
- Carl Beekhuizen
- Aditya Asgaonkar
- Justin Drake
- Grant Wuerker
- Cayman
- Hsiao-Wei Wang
- Alex Stokes
- Jonathan Rhea
- Dankrad
- Zahary Karadjov
- Nishant
- Raul Jordan
- Vitalik Buterin
- Jacek Sieka
- Protolambda

# Next Meeting Date/Time
Thursday, August 20th, 2020
