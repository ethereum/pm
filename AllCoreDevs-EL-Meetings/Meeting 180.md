# Execution Layer Meeting #180
### Meeting Date/Time: Feb 1, 2024, 14:00-15:30 UTC
### Meeting Duration: 1.5 hour 
### [GitHub Agenda](https://github.com/ethereum/pm/issues/943)
### [Video of the meeting](https://youtu.be/KE4VH-lSfHg)
### Moderator: Tim Bieko
### Notes: Alen (Santhosh)

| Decision Item | Description                                                              | 
| ------------- | ------------------------------------------------------------------------ | 
| 180.1 | **Besu** Matt Nelson shared details about an outage of roughly 70% of Besu Ethereum nodes on Ethereum in early January. A full [postmortem](https://wiki.hyperledger.org/pages/viewpage.action?pageId=117440824) about the event has been shared by the Besu team on their blog. Nelson explained that the outage was due to a bug in Besu’s Bonsai state storage format, specifically, how Bonsai encoded state changes. A hotfix to the Besu client has been rolled out and Nelson emphasized his appreciation for EL client diversity through the event on January 6. Because a diversity of other clients such as Geth, Nethermind, and Erigon, are being run by Ethereum node operators, the outage of Besu nodes did not materially impact network health or disrupt network activity.
| 180.2 | **Dencun Updates** Parithosh Jayanthi shared an update on the Sepolia hard fork, which occurred on Tuesday, January 30. Jayanthi said, “It was an uneventful fork. We saw [network] finality, as well as blobs showing up exactly where we wanted them to.” Beiko reminded teams that the Holesky hard fork is scheduled to activate next Wednesday, February 7. Holesky will be the last public Ethereum testnet to be upgraded before Ethereum mainnet.
| 180.3 | **Dencun Updates**  Dencun upgrade aside from the Holesky fork, Nethermind developer Łukasz Rozmej said that his team is investigating a bug in their client that caused the blob mempool to grow beyond its specified limits. During further investigation on Devnet-12, the Nethermind team spammed the network with blob transactions and noticed that validator participation rates dropped by over 20% due to this bug. The team is planning on spamming the Goerli testnet with blob transactions as a next step. EF Developer Operations engineer Barnabas Busa requested that the Nethermind team wait until the churn limit increase is tested on Goerli before moving ahead with blob spam.
| 180.4 | **Dencun Updates** Nethermind bug, Prysm developer “Potuz” said that his team is investigating unusual activity regarding a late block proposal on Sepolia that did not include any blob transactions.
| 180.5 |  **Dencun Updates** As these two outstanding items that developers need to investigate related to Dencun, developers agreed to hold off from setting a mainnet activation date for the upgrade until the next ACD call, which is scheduled for next Thursday, February 8. Potuz added that he would like to see more feedback on the Dencun upgrade from Layer-2 rollup teams before mainnet activation. Beiko agreed.
| 180.6 |  **Prague Proposals - Verkle** Joshua Rudolf and Guillaume Ballet presented their latest work on Verkle, which is a major overhaul to the way data is stored and retrieved on Ethereum. They highlighted areas of the upgrade that still need research, such as the Verkle sync and gas schedule updates. Based on preliminary tests, they estimate that the conversion to Verkle will take roughly two weeks and make transaction execution times about 10% slower. Rozmej commented that these preliminary tests should be taken “with a grain of salt” as they have yet to be tested through a more fully-fledged mainnet shadow fork.
| 180.7 |  **Prague Proposals - Verkle** complexity of Verkle and the need for more research about its implementation, Rozmej and other developers expressed concerns about committing to shipping the code changes for the Prague upgrade. Ballet agreed that Verkle would not likely be ready for implementation in Prague but expressed concerns that if Verkle is not scheduled for an upgrade, either Prague or Osaka, then client teams would have little motivation to work on it at all. Ballet said that the Ethereum state grows by roughly 25% per year and the longer developers wait to execute Verkle on mainnet, the more legacy data there is to overhaul during the Verkle transition.“It’s still way over a year to deliver in my opinion,” said Rozmej.
| 180.8 |  **Prague Proposals - EOF** Danno Ferrin shared updates on the development of EOF, which is a bundle of code changes to the Ethereum Virtual Machine (EVM) that developers had punted from inclusion in the prior Shanghai and then Cancun upgrades. “We’ve been moving into ‘ship it’ mode. We’re trying to close the door on as many of the spec possibilities that are out there,” said Ferrin. Developers working on EOF have started an implementation matrix to assess the final statuses of EOF-related Ethereum Improvement Proposals (EIPs) and finalize their corresponding reference tests.
| 180.9 |  **Prague Proposals - EOF** They are targeting Q3 2024 for activation of EOF on testnets for a hopeful mainnet activation during Devcon in Q4 2024. “I feel that these fundamental changes for fixing a lot of the technical debt of the EVM is kind of existential for the EVM in the next couple of years. All the complaints we see about things like, ‘We can’t increase the code size,’ these fundamental problems are fixed in the way EOF works,” said Ferrin. Erigon developer Andrew Ashikhmin expressed his support of including EOF for Prague. Ballet said that he would first like to see EOF working on a Verkle-activated testnet to see how the two upgrades would interact with each other. Reth developer Dragan Rakita said he did not agree there was necessarily a dependency between the two, adding that, “EOF in general seems a better fit for the Verkle tracking than legacy [EVM].”
| 180.10 | **History Expiry**  Kolby Moroz Liebl presented on history expiry. As defined by EIP 4444, history expiry means that EL clients would stop serving historical block headers, bodies, and receipts on the peer-to-peer layer after a certain period such as one year. Instead, this data would be serviced for users through an alternative decentralized network called the Portal Network. Liebl has published an FAQ document about Portal.
| 180.11 | **Specify Client Versions on Engine API execution-apis #517**  This is an open PR to improve tracking of what EL clients are used by validator node operators. At present, because most validators use MEV-Boost software, there is no way to analyze block data to ascertain the type of EL client used by the node operator. Therefore, accurate reporting on EL client diversity requires node operators to self-report. The PR recommends embedding by default in the “graffiti” field of nodes the client and version used to run the node. This is a practice already implemented by a few CL clients. Beiko encouraged client teams to review this PR and chime in with their thoughts.
| 180.12 | **EIP-7523: Empty accounts deprecation**  As discussed on ACDE #173, there is an EIP to reduce technical debt on Ethereum testnets caused by empty accounts. EF developer Paweł Bylica raised questions about the next steps for this EIP. Beiko encouraged Bylica to share these questions in the Ethereum R&D Discord channel.
| 180.13 | **EIP-7587 - Reserve Precompile Address Range for RIPs**  As discussed on ACDE #178, developers are planning on reserving a set of precompile addresses for use by Layer-2 rollup teams. The EIP reserving a precompile address range for rollups is moving into a “last call” phase. Beiko encouraged developers to speak up in case they had any last-minute comments or objections to the EIP.


**Tim Beiko**
* Welcome to ACDE 180.  so we have a bunch of stuff to cover today.  including a very last minute addition about, blob spamming, breaking down at 12.  but. Yeah. So first,  we wanted to chat about the Besu main net event, and we have Besu main net bug. Sorry. And,  yeah, we've been pushing this back for a call or two now, so I put that at the top so we can get through it.  then let's chat about Dancun, and we'll do the dev net,  conversation as part of that. And then obviously sort of reflect on how,  Sepolia went.
* And,  after that, hopefully the bulk of the call we can spend,  going through the three big things we've been discussing as potential candidates for Prague and potentially the fork after,  so  EOF and 444, four.  and then lastly, there's three small things people wanted to talk about. We'll see if we have time. But  worst case, we'll just,  at least point to them and folks can chat async about it.  but yeah, I guess to kick it off,  is Matt on the call? Yeah. Matt, do you want to give some context on the Besu agenda item? 

# Besu Jan 6th Mainnet Event & Reddit AMA performance numbers [4:05](https://youtu.be/KE4VH-lSfHg?t=245)
**Matt Nelson**
* Yeah, absolutely.  so as many of you know,  January 6th of this year, we had a halting event with Besu nodes on main net. It was not all of the Besu nodes on main net, it was probably somewhere between 60 and 70% of the nodes.  we of course, have shared a pretty detailed postmortem.  so if someone is in the chat for my team, would love to pace the full length, that would be great, but I'll give a quick overview of what's going on.  that we kind of discovered,  what we uncovered was that a lot of kind of.
* Freshly funded accounts were experimenting with metamorphic contract deployment in a way that was exposing some edge cases in Besu's implementation of the state database called Bonsai.  you know, we've we've shared tons of information on Bonsai in the past, but,  we viewed a few of these kind of iterations of metamorphic contract deployment. When I say iterations, it means that they're they're intentionally different edge cases that we noticed.
* You know, that we had been kind of also slowly patching in various releases. So we first noticed,  these things happening on some of our Canary nodes on Goerli and Sepolia,   prior to the January 6th event. So we noticed again, some of our canaries going down on on those other networks.  you know, we would we were noticing some issues, and then we were patching them as we were going along. But on the main event on main net on block one, 18,947,983.  that was the big event for what we triggered that caused kind of the the the the big halt.
* What was happening that we noticed was that the preimage that was being created,  for some of the. Block or, excuse me, the preimage for that specific block. Was being written incorrectly for the trilogues. 
* And the way that Trilogues work in bonsai is that it's a delta between, you know, the state and one block to the next. And we were incorrectly writing a preimage in that for storage that was self-destructed to the trilogue. So when the block was rolled from one state to the next, that would be considered invalid state.
* We were not parsing that correctly, and then we were considering the block invalid in some cases, which would cause the Besu nodes to go off on a fork. And then in some cases we were just simply halting the node.  we noticed again that this was happening. We provided some mitigations for users on mainnet,  asking them to rethink their node in some cases to avoid that kind of problematic trilogue since we're not generating trilogues,  as we kind of do the world state sync.
* So if you were able to sync past the problematic block, you weren't writing that incorrect preimage to those bonds I trilogues, which means you weren't applying them as you rolled the block,  from the previous good block to the problematic block. This was all well and good. We had again mitigations in place. We were able to put out a patch. How we were able to discover this was was kind of a kind of collaborative effort, which was really exciting to see. We were able to get traces of this block from some other teams. So that was absolutely great.
* We were working with Nethermind team. We were also able to use  archive consensus layer nodes to create kind of initial states at the block right before,  the problematic blocks that we were able to, again, kind of exercise that trilogue rolling from the, the the last good block to the problematic block. 
* We were able to capture that preimage and see what was happening with the self-destructed,  contract storage. So we again generated that initial beacon state observed that state change,  viewed the bug that we were able to find,  with the implementation of bonsai,  and being able to again, put out fixes for that. 
* So it was very interesting.  in that sense, it was also interesting that these, again, these transactions were from freshly funded accounts that were playing with these kind of metamorphic contract flows.  they were coming all from exchanges with no KYC.  but at the end of the day, you know, there the, you know, kind diversity angle kind of works here.  there were no additional kind of, you know, correlated penalties triggered for a bunch of Besu nodes.  and again, the kind of client diversity aspect worked and it showed that there can be issues beyond just the EVM implementation.  
* So we were very happy to have support from some other teams.  we were very happy to be able to kind of pass or to parse some of those self-destruct issues that have been playing us for a little while. And we're also very happy that when we ship,  the fork on mainnet, the self-destruct will no longer be something that we have to worry as much about.
* So,  that was a super quick overview. Again, it really had to do with the way that metamorphic contract deployment interacts with Pre-images in our state implementation.  I encourage you to go down the rabbit hole,  if you want. We have shared the link in the chat.  and maybe we'll do one second 30s for questions because I know we have a super packed agenda today. 
* And, Tim, frankly, the the second part of the discussion around performance numbers, I don't think we need to get too deeply into that because there's been tons of, you know, public discussion about this at this point. And, you know, there's been a lot of,  frankly, benefit coming out of that discussion. So I don't feel the need to rehash,  the what went down regarding execution layer,  minority client performance.  but but that's basically all I have for, for that agenda item this morning. 

**Tim Beiko**
* Yeah, thanks for sharing and for sharing the link in the chat with all the details as well. Any questions? Comments thoughts? 

**Marius**
* I would,  just quickly like to say sorry again for for sharing those numbers on Reddit, those were old numbers and on outdated versions of the clients. And I should have checked with the client teams before sharing them. And,  yeah, but I'm glad that,   there was a discussion about it and we have some very nice numbers now.  and everything looks kind of good.  with regard to, like, the worst case EVM execution that, that we that we can do at the moment. 

**Matt Nelson**
* Yeah. Thank you for that. That's great. And we appreciate that. 

**Tim Beiko**
* Thank you. Any other comments? Questions? Okay. Well, yeah. Thanks again, Matt, for,  sharing,  the overview.  yeah. Moving on to Dencun.  

# Dencun Updates - Sepolia Fork [11:07](https://youtu.be/KE4VH-lSfHg?t=667)
**Tim Beiko**
* First we had Sepolio fork two days ago. Now,  does anyone want to give a quick update,  about how that went?  overall, it seems to have gone super smoothly. 

**Gballet**
* Yeah. So we have the Sepolio here for,  couple days ago. And,  all the valid or most of the validators had updated their clients. So it was an uneventful fork. We saw finality as well as blobs showing up exactly when we wanted them to. 

**Tim Beiko**
* Anything. Anyone notice that was weird or unexpected? Okay, well, I guess that,  says it all. Yeah, it looked good.  and then a Husky is,  forking next Wednesday, I believe.  so, yeah, that'll be your last one.  the before midnight, and I believe early next week, the blobs should start expiring on Goerli as well. So I know that was something we wanted to,  see on the test nets, obviously, before,  upgrading to main net.  so, yeah, it seems like,  things are progressing smoothly.  that said,  Lukasz, you posted,  something about Devnet 12,  saying that the blob spam broke its. Do you want to chat about that? 

**Lukasz**
* Yes. So I will maybe leave,  merging in the field.  in the second. Just,  we are we are hunting one bug in. Nethermind which caused the potentially the blob pool to grow,  beyond the limit we set and Martin was doing a test,  like, two hours ago,  and spamming the devnet with blob messages and participation rates went down from over 80 to below 60, so over 20%. And it haven't recovered yet. So we need to definitely investigate devnet. 12. And we want to also do similar spamming on test nets.  probably we'll start with goerli.
* So we want to coordinate with DevOps and the community,  about this because  maybe we can make some problems there too. So I don't know.  and I think we need to like, look into this before we can, for example, schedule main net date,  because,  this is troubling that it happened.  Martin, do you want to add? Anything?

**Marcin**
* Yes. I used to,  do,  such spamming experiment a few times before, but I was always sending six block transactions. So,  in Nethermind. In Nethermind, we are limiting it to 16 K of transaction. Doesn't matter how many blocks they have.  so we had this 16,000. And,  like other client, we know that gap is limiting by the size, like on disk space. So,  if there was only six block transactions, then they had like,  13,000, something like that. And today I changed it a bit and I sent a mix of six block transaction and one block transaction.
* So,  in Nethermind, we still have 16 K, but other clients,  have above,  20,000 transactions.
* And  seems like it may be a problem, but,  I'm not sure. It's just like, like guessing. So for the first time, the number of transactions sent in spamming experiment was,  so high. 

**Tim Beiko**
* And Barnabas, you have your hand up. 

**Barnabas**
* Yeah. Just want to mention that before we start blobbing on Goerli, we should wait a few more days,  before we can test the maximum  turn limit. Because it's possible that we will not recover from that. And,  we only need we only need a few more days to reach the turn limit test. 

**Lukasz**
* Okay, sure we can. I'm on it. 

**Danny**
* Ideally, we figure out what happened to dev 12 before we. Yeah. Break the next testnet. Just. Yeah, sure. 

**Tim Beiko**
* And then,  POTUS has a comment in the chat as well saying,  there's some block proposals that came late and didn't have blobs in them, and it's unclear if it's a prism or a relay issue.  this is on Sepolia. So I guess based on all of this,  it does seem like we have a few different things to investigate.  and then we'll obviously see a whole Holskey for Kenya,  later this week or early next week.  does it make sense to wait until ACDC to potentially set a main net date?
* Assuming that,  a week from now, we've,  assuming that a week from now we've figured out what's going wrong with Devnet 12, we've seen the churn,  limit activate on goerli. We've seen the blobs expire on goerli, and, Yeah. Have a better understanding. Alex is asking to set a provisional date today. I don't know if people would prefer to do that. Yeah. I mean, we can set a tentative date today and confirm it next week. But then if we realize in the next week or so that things are going to take longer,  we're going to have to push it back. So I don't know what people's preference is there. 

**Lukasz**
* My preference is not to say the date,  right now, because we don't know if we have some kind of,  issues in the clients to fix.  so before we are resilient to,  to this kind of DDoS attacks,  I don't think it's a good time to set a date. 

**Tim Beiko**
* Fair enough.  okay. And a plus one,  from Terrance on prism.  any other thoughts? 

**Marius**
* Now, I would be fine with setting a date, but we can also  the thing is, like, we kind of need the. Execution layer focus to set the date as well. 

**Tim Beiko**
* So yeah. So okay, so what I would do is then if we're going to set it next week, like again, assuming that we've diagnosed and like understand the issues by next week.  then yes, EL folks, please show up on the call next week or you're just going to have to live with whatever date gets set there.  But I think, yeah, it's probably more reasonable to wait until we have a better view of things and then, yeah, aim to set a date for main net on next week. Call if those issues are fixed, or we at least know when things are going to be fixed.
* Yeah. And I guess if for whatever reason, some EL teams can't make the call next week.  just leave a comment in the agenda if you have strong preferences around, I guess. What's the earliest you could have a release out for main net?  yeah, we can discuss that on ACDC. 

**Danny**
* Yeah. And if you don't have representation also, you know. Within 24 hours in the chat if you have any. Further discussion. Maybe, I don't know. 

**Tim Beiko**
* Okay. And then there's a comment as well about getting some L2 feedback.  I know there was a roll call yesterday. I don't know if there was any feedback given there.  otherwise it's something we can. 

**Danny**
* Starkware is testing as well, right? Yeah, yeah. 

**Tim Beiko**
* Starkware has some,  yeah. Starkware has posted some blobs. Yeah. Um. But yeah, that's maybe something we can do as well. Before next week's call is just try to tally up,  the different,  different L-2 status updates. Okay. Anything else on Dencun? Okay, then. 

# Prague/Electra Proposals [21:33](https://youtu.be/KE4VH-lSfHg?t=1293)
**Tim Beiko**
* Moving on.  so,  next up, the main thing  we wanted to discuss today are the three potential big things that we could do in either the next fork or the one after and potentially try to get to a decision about,  what we prioritize when.  so the three,  to recap, were Verkle trees,  EOF and then EIP-4444 even though the last one doesn't quite meet a fork,  we could decide to just do a small fork and put extra engineering cycles into,  4444.
* So yeah, I guess maybe to kick it off,  I believe the Verkle folks have a quick update on their work, and we can do questions and kind of dive deeper into it after that.
* I don't know, Guillaume or Josh, which one of you is giving the update? Yep. Hello? 

**Matt Nelson**
* Can you hear me? Okay.
  
**Joshua**
* One second. Let me share my screen if I can. Oof! I'm getting an error here. Um. Can I drop a link and maybe Tim, you could share for me. Sure. 

**Tim Beiko**
* Yeah.

**Joshua**
* No worries. Um. One second. I'll just drop it in chat and. Yeah. 

**Tim Beiko**
* Okay.  let me open this up and try to share this. Okay, I'll leave it like this though, because I think if I go full screen, it'll break my. Oh, actually. Wait.  I need to change something on the stream. Oh. Mike says he thinks he can share. Yeah. The problem. So it was visible on YouTube. But it seems like when I start sharing my screen there, the sound just stops coming in. Okay, Peter. Thank you. Peter saved us. 

**Joshua**
* Thank you. Peter. Okay.  so we were on slide four, I believe. Perfect. We can go back up one previous. Yes. Cool. Thank you. I saw a comment from Lucas as well.  a good clarification that it does not solve, but the state growth problem, but does provide.  I guess it's a partial solution there. We can get more into this.  so, yeah, so not spending too much time on the why on Verkle, but just making sure we don't lose track here of of why, why we're doing the work we're doing.  the decentralization benefits, I think are pretty clear and have been gone through a bunch,  perhaps the most direct, but many other reasons why all of this work is valuable.
* Of course. Instant sync again, probably pretty easy to understand for people.  any new node can theoretically spin up receive a block. And the witness, assuming the witnesses are in the blocks,  and instantly start validating,  on the performance and scalability front.  perhaps a bit more theoretical, but still, I'd say a fairly clear benefit in reducing disk. IO for example, for Non-builders.  and I think just overall, the Tldr here is that statelessness, small enough execution witnesses that can be passed over the network,  this will all unlock a lot of cool new things.  so we can go to the next slide. So, Peter, I don't know if we're having more. Okay. Cool. Thanks.
* Here we have a high level overview of what's changing with Verkle, just sort of at a glance to give a sense for why there are so many moving pieces. A lot going on here, and we will spend time,  diving into each of these a bit. 
* Next slide.  so yeah, before we dive into each element, here is just a slightly different view of the main ingredients needed for Verkle and how we are doing so far on each of them.  I guess as a note,  on this, on the progress indicators you see below each item, this isn't really intended or this may not accurately reflect the progress of each individual client,  but is more so intended to give a very sort of approximate sense for how far along we are,  on each item. Don't want to give an impression that there isn't still a lot of work to be done. Of course.
* But it's helpful, I think. Hope,  to understand how much progress has been made on each of these fronts.  these numbers could certainly still go up or down a bit over the coming weeks.  but overall, I think we can be fairly optimistic that they are all trending in the right direction.  cool. So now we can quickly go into each of these one by one. The next slide. Peter.  So, yeah,  going through these, we tried to organize each into three sections. Hopefully that's clear section,  three sections, what's already been completed, what's left to do. And then at the bottom, trying to anticipate where we might get surprised to the downside.
* The tree structure is one of the items that is the most far along.  Next up here, as a to do, is the Shawdow fork,  which will give us more data and even more confidence in our approach.  and this should be complete. Fingers crossed. Really?  any day now. Uh. Next slide. The cryptography also rather far along thanks to Kev. 
* Gotty, D'ancora and many others for their long standing work.  we have two main implementations Go and Rust Nim also catching up with their own work.  On the. I suppose on the potential surprises front, we are interested to get more data on performance and potential impacts of 4844, and this may be a good topic for Q&A at the end. But yeah. Next slide. Gas schedule updates. Making progress here recently. Still a good bit of work and testing to do to understand things, and one of the next big milestones here will be getting more DApps, other large contracts deployed on testnet so we can continue to learn anything else here.
* I think we can move on. Yep.. Thank you. Transition.  clearly, I think people understand one of the most complex and trickiest parts of all of this,  but has also been our highest focus area, namely,  Guillaume and Ignacio and others, for some time,  really solid progress. We believe we have a viable migration plan, which is a lot,  and we'll know more once we complete our shadow fork.  again, thanks to Perry DevOps for all the work there.  next up on the to do is just sort of finalizing the plan.  yes. Sorry on the transition and,  locking that in,  reviewing that and a big piece of that will be,  the finalizing the preimage distribution strategy..
* Next slide. Witness generation verification,  live on the testnet is used in the current version  of Verkle sync. Main thing here perhaps is finalizing the actual distribution strategy. Where are people going to get the proofs from,  included in blocks or distributed in some other way out of blocks? 

**Joshua**
* Yeah. So I think that's it for witness generation. Go on to the next slide. And the fact sheet. So Guillaume and Ignacio helped to put this together. And actually. Guillaume available to you here if you're able. 

**Gballet**
* Right. So,  yeah, the the thing is, we wanted to present some, some numbers, but we're a lot of them depend on the success of a shadow fork, which is,  stopping us a bit. Has been stopping us a bit for for a couple of months.  but so what we have to offer are mostly educated,  estimates.  so, for example, the the average, we estimate that,  the average witness size should be around 150kB,  the tree size. So,  this is actually an upper limit, right? I just want to make that clear.  it would be 80% of the current,  tree size as of yesterday. Like when I did this dump. And,  what needs to be.
* Yeah. So what what's not specified here is that we we haven't optimized the compression in the database yet, so there's there's a lot more to scratch,  like there's a, there's this is just the surface. And we, we need to scratch deeper,  execution time. So we ran that. So this is actual data.  we ran that on,  somewhat older version of the database.  So there could always be a surprise there, but,  yeah, from what we can tell in terms of,   of performance, of executing a block, it's like 10% slower.
* Of course, once we have the the shadow fork running, we can get more current numbers.  we did not really try to measure,  the time it takes to to produce a proof,  because, well, there's there are several reasons, but one of them is we could still decide to go without the proof in the first,  in the first iteration of the fork. Or we could decide to distribute them differently. 
* But once again, like, once we have the shadow fork, we'll,  we'll be able to get numbers both the time and the size, actually. And,  yeah, I think the most,  worrisome part for people is how long it would take to, to do the conversion. So we tested on a fairly slow machine. Right.  how old is that machine pairing?  the rocks  rocks. No, sorry, not the rock fiveb the other one. three generations. 
* Three generations old. Right. And,  we also tested indeed on the rock fiveb, which is, which is quite slow. So we are able to handle 10,000 leads, move per block, and it takes about one extra second.  so we and more importantly, it can be done before,  before the block,  before the slot starts. So that's,  that's quite convenient.  and we estimate right now based on the estimated number of leaves and,  in the future that we could be, we would be able to do the just the copying part within two weeks. Then there's a buffer.
* There's a required buffer of one week to distribute the pre-images.  but yes, that's, that's we should be able to, to handle that under a month basically. And yeah, that's pretty much it. 

**Joshua**
* We can go to the next slide. Almost finished here.  yeah. And this is pretty much it.  I just wanted to bookend this by quickly recapping again. Benefits of Verkle why we believe it's a powerful upgrade.  comes, of course, with a good deal of complexity. But thanks to everyone's efforts here, making very solid progress and,  confident it'll be ready for prime time soon.  so. Yeah. Thank you all. Any questions? I think we can. Yeah. In the next slide is just Q&A. So,  we can take those now, assuming we are okay on time. 

**Tim Beiko**
* Yeah. Let's do question now if there if there are. 

**Joshua**
* After the change slides that we want to go back to. Sorry if it was too quick. 

**Tim Beiko**
* And I know there's been a ton of discussions in the chat.  some back and forth there. Either more questions or concerns people want to discuss. 

**Gajinder**
* Hey, Josh so the execution time that I think someone also mentioned this in chat,  that you had mentioned over there, is it,  the block production time or is it an execution time by a full,  not maintaining Verkle trees? Or is it a stateless execution time? 

**Joshua**
* More, the latter stateless execution time. 

**Tim Beiko**
* Okay.  Lucas has some questions as well. 

**Lukasz**
* So I just want to comment on the discussion there that,  not to extrapolate, for example, Holesky performance on main net performance if we do Holesky shadow fork. And I'm talking this directly from our,  Nethermind,  experience because we are currently trying to move to a path based storage. And one of,  our  tries on that worked very well on Sepolia, for example, which is a lot smaller, but when scaled to mainnet,  it actually didn't scale well. So until we have like a shadow fork on main net and some performance numbers from there. Like, just keep that performance numbers with a grain of salt that,  it's not,  not something to make any decisions based on it. 

**Gballet**
* So to be clear, the 10% performance is mainly data. 

**Lukasz**
* Okay,  So sounds sounds interesting. but, after you do the shadow walk, I would be very eager to see, like, mainnet shadow walk. 

**Lukasz**
* Yeah. Cool. 

**Ameziane**
* Yeah, but I guess it's mainly data. Stateless data. Right. It's. It's only like the cryptographic overhead.  no, no. 

**Gballet**
* No, it's not, it's,  actual writing to the database. In fact, that's where a lot of the performance goes. 

**Ameziane**
* Right. Okay. 

**Tim Beiko**
* Okay. Any other questions? Comments? 

**Peter**
* Can I ask about the status of this? So if we go back,  a few slides, you had this sort of status situation. Based on this, are we in a position where we're ready to do this in the next fork? Like, I've just sort of like, if Verkle sync is only five out of ten, like done, is there a risk that if we allocate this to the next fork, that we're going to get delayed on that fork because we have like research needs on the Verkle sync? And would it be better to push it one more fork so that like Verkle can be like basically done when people are ready to start implementing it? 

**Gballet**
* I am not sure Understood the question, actually. Do you? Which fork are you talking about? Pushing it back to Osaka or,  what would that be? 

**Tim Beiko**
* I guess he's asking about Prague versus. Like if we decided this was the main priority today. Is it even in a state where,. It's valuable to have all the clients shift to prioritize that. Or is it better to potentially have a few more cycles around development where,  we sort of get something like this sync from five to an eight, and then at that point we prioritize it, you know, for, some other fork. . 

**Gballet**
* Right. The problem with this is that,  if you don't care, as long as you don't prioritize it, people will not work on it. This is exactly what happened with Dancun.  you know, it went. It went ahead. No one looked at Verkle. I mean, no one. Of course some people did.  that's why we're here. But,  it didn't get the attention because it was that thing up in the air that people,  think they will work on when it's scheduled. So,  my understanding is that it should be scheduled. It doesn't really make a difference whether or not you schedule it for Prague or
*  What matters is that,  people start looking at it as if it was the next fork. And,  because if you don't, you're always going to look at to.

**Tim Beiko**
* You're gonna focus on the other thing that's important. So okay, so you're saying like it's not necessarily the most urgent thing to deploy on the network, but it is urgent to get team's attention on this and like significant engineering resources in order to actually make progress on all those things. And, . Yeah. 

**Gballet**
* Sorry. Let me qualify that.  it is quite urgent to deploy it on the network. I mean, of course, we should not rush, but we have,  the current state that is growing. The more we wait, the more the conversion is going to take longer. Which means we have this area of time that is a bit more risky than the rest of the normal operation.  so it is quite urgent to to deploy it on, on the test.  sorry, on the test. Well, also on the test net, but on main net especially. 

**Tim Beiko**
* Got it. Thanks.  I believe Enrico, you had your hand. 

**Enrico**
* Yeah. He just. He just covered the right now. Because my question was, if we postpone this too much, is the state growing too much and then affect the transition that makes from maybe two weeks to to maybe one month, because the state now is too big, and the transition will be very painful, especially for little boxes. 

**Gballet**
* So, so far, what we see is that.  The state grows by roughly 25% each year. If we extrapolate, hopefully it stays this way.  We have a little bit of time also machines or nodes on the network are going to get faster and faster, right?  the rock  is probably not going to be there forever. There will be more powerful versions, if that's what we want to keep,  running of or supporting. I mean,  so, yeah, it's not like it's super urgent, but what you have to realize as well is that it's not just,  it's not just the transition itself. It's every full sync you're going, you're going to do in the future.
* And right now, or more like June, about June this year,  you will already add about one day to a full sync, just in terms of pure computation. If you wait much longer, you're making your foot sink more and more impractical. So now it doesn't sound like very interesting to most people, but full sync is excellent for testing new code or new. Yeah, new code. So this is quite useful for for core devs. 

**Tim Beiko**
* Lucas and Dankrad

**Lukasz**
* So a few things I want to cover. So I disagree that we cannot work in parallel because we work on 4844 itin parallel. Very well. And we had the test nets of 4844 way, way before we deliver Shang-Chi.  so and we already have some test nets on Verkle trees, so kind of working parallel kind of works.  Secondly, I am against for going this in Prague, if I already were talking about schedule.  because of two things, I think like,  while the maybe Geth implementation might be maturing enough.
* I think like each each client has its own implementation, and it's a very hard thing to do, in my opinion.  like for me, for myself, like the state management and state tree is the hardest part in the code base.
* And if we want to have multiple client implementations polished to the level of,  what they are comfortable with,  I think it will take a long time.  So, just because of that, I'm against  and again, talking from experience for over a year, we are working on our.  we haven't delivered it yet.  hopefully we can deliver something in the first half of this year. But it's taking a long time, and it's delaying and delaying. And,  like I said, for me, it's the hardest part in the code base. And we don't want only one client to be have it implemented in the implemented. Well, we want to have all clients to have it implemented well and  on good enough,  level.
* So I don't see that happening early. And I'm talking this as a client that has a Verkle tree implementation already that has joined the testnet and that has Verkle sync prototyped in it. 
* So I would say that Nethermind. It's pretty decent on the, on the level of implementation, but I am really, really worried about, for example,  main net performance numbers or. Nethermind, I think they would be very, very bad. So a lot of work.  need to go there.  yeah. So I don't see this coming in months. It's still way over a year to deliver, in my opinion. 

**Tim Beiko**
* Okay. Dankrad

**Dankrad**
* Yeah. I just had a quick question about the,  transition, which is,   what is what is the limiting factor? Is it  bound, is it CPU bound?  like,  that might be interesting to know for knowing, like what to expect when it first like how which which hardware do we need to watch when we say, like,  is it gonna get faster because we get better hardware and like, also like, yeah, how much worse it gets when the state gets bigger. Do you know that? Gwilhum. 

**Gballet**
* I'm just trying to enroll everything. Yeah. So the hardware,  hardware wise,  yeah.  from it's definitely both,  it's,  io bound because the the rock  is extremely,  is extremely slow in,  when it comes to IO, it's also CPU. If we get better CPU,  we can indeed pack more leaves, but, Yeah. My I'm trying to remember  to be honest, but I think the, the biggest problem was,  was indeed io. Do you remember,  Ignacio? 

**Ignacio**
* Yeah, I would say it's,  mostly CPU bound, to be honest. And also depends. Yeah.  right. Because, like, it kind of depends which is the, the lowest hardware setup that we are trying to push for.  because there's a huge difference between rock vibe and any other like normal machine. 

**Gballet**
* Yeah, exactly. Now, I remember because Rock Fivb I think had extremely slow io, which is why the performance was bad. But your average machine is actually CPU bound. That's. 

**Dankrad**
* And how many, how many seconds is those 10,000 leaves on your average machine. 

**Gballet**
* One second ish. 

**Dankrad**
* And that's parallelized or not. 

**Gballet**
* Yeah.  I also need to.  I mean, I would like to answer if, 

**Tim Beiko**
* Yeah, yeah.  Let's do that. And then maybe let's move on to the next ones. Yeah. 

**Gballet**
* Right. So I wanted to.  To clarify,  two things. So I agree that  Verkle is, is a bit,  far off. But that's, that's exactly the point I'm making. It needs to be looked at so far.  you know, it's just,  it's just a fairly small team trying to to make a gigantic thing happen.  yes.  I'm not claiming it will be there.  in. I mean, I never claimed it's been,  it's going to be there within a month.  I still think a year is realistic. Maybe. Maybe not, but,  but it's definitely not going to happen until every client starts looking at it.
* This being said, there's been a lot of optimizations that have already been worked on that you can immediately import in other clients. So a lot of the the work,  when it comes to optimization has been done. The second thing  I wanted to say is it's true that,  4844 and  withdrawals were worked  on in parallel. But that's the point. The withdrawals were extremely easy from an EL,  point of view. What,  what I'm saying here is if you schedule some very, very light,   yeah. Items for,  for Prague.
* And then we come in to do Verkle in Osaka. That's no problem. Those things can be parallelized if you start doing something way more complicated.  you're not going to be able to do,  to do anything in parallel. So, yeah, that's,  just one point. I wanted to to clarify. 

**Tim Beiko**
* Thanks. And. Yeah, I guess. Yeah. Before we start,  going into, like, more planning discussion, I think it's worth going over EOF and 48444. So we have the full picture. Yeah. Peter, I don't know if you can stop sharing your screen.  so we can move on to the EOF folks. Thank you.  Yeah. EOF I'm not sure who's the main person.  giving an update here. 

# EOF [48:15](https://youtu.be/KE4VH-lSfHg?t=2895)

**Danno**
* Is Alex on? I don't see Alex from any of the other crew. Okay,  I'll go ahead and give an update.  we've been,  moving into ship it mode.  we're trying to close the door on as many of the spec possibilities as are out there. There is one,  out there lingering with regard to,  whether we're going to use variable length instructions.  probably not, just because of scheduling issues, irregardless of the merits.  it seems like we could get some value out of it.  but as far as the main issues  with EOF, it's very derivative of big EOF that we try to ship about this time last year, and it was about this time last year that we pulled it out of Shanghai.
* It was going to be another big feature in Shanghai.  because of,  solidity couldn't get some of its,  constructor stuff working. So over the past year, we added some more stuff to,  add a couple of big high level features.  we remove,  introspection.  code introspection from EOF.  so you and,  which was a major ask from a high level,  people in Ethereum and also we removed gas introspection and those two things are going to do things like make,  gas schedule changing nl2 is much easier.  so let me paste this into the chat. So we are starting a just started this yesterday we started an implementation matrix to get final status on some of these specific,
* EIPs and nailing down some of the reference tests. We have reference tests for a lot of these. Again, these are very derivative of what we had this time last year. So we got a kind of good head start on, on some of this  some of this featuring  so of course, you know, my pitch, like I mentioned back in I'm October, November.
* I would like EOF to ship as part of Prague,  targeting Q3 to ship in a test nets so that we are on main net by the time we get to Devcon Southeast Asia. And I think it's achievable where we're at with the spec, if we ship the spec as we have it today, we don't do any major changes.  and you know my pitch, if you talk to me, I'll probably go way to far the details of it. But I feel that these fundamental changes for,  fixing a lot of technical debt in EVM is kind of existential for the EVM in the next couple of years.  all the complaints we see about things like,  we can't increase the, the code size,  the problems, the fundamental problems that are fixed in the way EOF works.
* And there's a lot of other things that are going in, you know, the, you know, why can't we have,  EVM. Max, we really need a meta arguments. Why can we have immediate arguments? And it's just it's like the hole in the bucket song.  we just need to fix a lot of things at once. And this container format fixes it with container without fundamentally changing  the way the EVM works, we still have frames, we still have halts, we still have accounts, we still have storage. And,  probably the last thing I'll say is,  the engineers that have been working on EVM stuff tend to be different engineers that work on the data stuff.
* So I don't think this would stop any work on Verkle from going forward.  I don't think it would impact in steel any resources from that effort. So. 

**Tim Beiko**
* Thank you. Yeah. Great overview. Any questions? Comments? Andrew. 

**Andrew**
* Yeah. So my preference is to schedule EOF,  for Prague and Verkle for Osaka. I,  yeah. 

**Tim Beiko**
* Thanks.  yeah. Before we get into the scheduling, just any technical questions? On what Daniel shared or on EOF specifically. Oh, yeah., Perry or whoever that is. 

**Gballet**
* Yeah. I'm not sure if it's a question or,  more like a a feasibility.  well, I guess it's a question. Did you I mean, we talked about this,  in on telegram yesterday.  there's some kind of understanding how EOF is going to impact Verkle.  what I would like to see before I, we make this kind of decision of putting EOF before Verkle is to ensure that it runs on the virtual test net.  as long as we like.
* The reason for this is because there's this whole chunking thing happening  in virtual  EOF does the chunking differently, meaning we have two code bases to like that that have never been tried before, that have to be tested,  in parallel. I am not comfortable,  going with EOF first, as long as I don't see the feasibility. It's not just the ability to do it.
* I agree that EOF can be done faster than Verkle, that's for sure. The question is, can it be done in parallel with virtual? That's a different story.  but if it does go first, I need to make sure that there's no,  that we don't ship something and paint ourselves in a corner realizing, oh, actually, we broke something. So I would say even to before we even try to solve this question of who goes first, I mean, clearly, probably Verkle is not going in Prague, right?  do we,  can we get some actual data as to what's how well they work together, basically. 

**Tim Beiko**
* And then and then your main concern, just to make sure I understand is about the way EOF does code chunking and  how Verkle then chunks that differently to put data as part of the the tree. 

**Gballet**
* Right. It's just that, Basically they do it differently. And I want to make sure that both path, both both code path that are going to be entirely new work fine. If not, or if we can't get enough confidence, I think EOF should go afterwards. If we can get that confidence then no problem. But I don't want to make your claim and I don't want us to commit to ship eof before Verkle as long as we haven't answered that question. 

**Danno**
* So the code chunking with with EOF is going to be basically the same on the code sections are going to work exactly the same, like legacy code sections. We're just going to add a little extra bit of logic to make sure that we bring the right parts of the header in, and making sure that we can execute EOF code in a chunked environment has been a discussion in several of the past different EOF implementers calls. It's been something that we've been aware of. It's been something that we're building some things design around.
* One example that you might it might be worth pointing out is the current chunking plan has an overhang byte and then 31 bytes. And that's because of legacy jump test analysis. for EOF code, we don't need that hang over byte.  because every code is valid, you don't need to do jump test analysis.
*  If it hits main net, then the code is valid because we only deploy valid code and all the jumps are going to hit legitimate places. So in that sense we could save a little bit of space with EOF. But it's going to work. It'll work within the current chunking system. We just need to add some extra analysis to make sure all the appropriate parts of the header are brought in, and that shouldn't be terribly hard. 

**Gballet**
* I don't want shoots. That's the thing. I want to see it working.  I mean, I'm sorry. I don't want to sound extremely rude.  all I'm saying is shoots are fine. What I'm afraid of is that we paint ourselves in a corner, and we only realize too late. That's all. That's all I'm asking. 

**Danno**
* And before we can put it in a test net,  Verkle. We need to have it working in clients. 

**Danno**
* Exactly. So we need to implement a clients, which is why where we're at with the implementation readiness matrix. 

**Gballet**
* Right. But do you have any client that has implemented it? That's my question. You say you say it's going to be fast, right? Did I understand that correctly? 

**Danno**
* What was the claim? 

**Gballet**
* My understanding of your claim is that you say it's,  it can be done quite easily by,  different people. 

**Danno**
* Yes, it'll be done by different people. Right. And Besu I have no I do not work on any of the the tree stuff. I only work on the EVM stuff. And my understanding is that's the same on a couple of the other clients. 

**Gballet**
* But how quickly can you slap together? And once again, I'm not trying to be I'm just trying to see where you fits. Is does it fit before or after Verkle?  can it can you slap together something to run on the Verkle testnet in, like a matter of a couple of months? 

**Danno**
* Yes. 

**Danno**
* Okay, cool. We're finishing the spec. That's the implementation readiness matrix is for writing reference tests for this.  Geth would need it probably is the most advanced Verkle. So we would need to have Geth,  dig up and update theirs.  whoever was contributing that,  or we could have EVM one do it through,  the EVM C but,  yeah, I mean, this does seem like you're moving the goalposts, to be honest. That's how it feels. 

**Gballet**
* Once. Again, just making sure we're not painting ourselves into a corner because I fear that's what's. 

**Tim Beiko**
* Okay. And, yeah, I think we have a good,  next step here, but, yeah, just,  make sure we don't cycle around this over and over. Yeah, let's move on. Andrew. 

**Andrew**
* Yes. So can we like,  commit,  to EOF in Prague, but with the caveat that, we will have to run a vocal testnet that includes EOF and also spend some brain cycles on the compatibility. And if it turns out that there is an incompatibility, we just decide then we don't ship EOF in Prague. 

**Danno**
* Just like Shanghai. Yeah. 

**Tim Beiko**
* Yeah. Let's hold that.  again, I want to make sure we get to 4844 us as well before we do the scheduling stuff, but, Dragon. 

**Draganrakita**
* I just wanted to say that storing the bytecode and using the bytecode are totally different things. And how we store it be that in the Verkle, be that in the Merkle is totally different than how we are going to use it inside EVM. So I don't see that as the like cutting point or dependency between those two. Just wanted to mention that you have in general seems better fit for the vocal tracking than it's for the legacy. 

**Gballet**
* Just a quick answer. In a stateless context, it is the same thing. 

**Draganrakita**
* Yeah, but for the stateless context, we will have at least 2 or 3 hard forks to come to that. But even for that, it's better to have UF than the legacy because the bytecode is a little bit smaller. 

**Lukasz**
* Yes - Question mark about EOF and Verkle. Because if we start,  coding chunks in Verkle wood, accessing it  would be potentially. Would we have to revise the cost of accessing this code? And from the tree, like,  just to,  on the 

**Danno**
* That's one of the EIPs that was posted a little bit ago. So yes, that's in Verkle plan. 

**Tim Beiko**
* But we're going to need to revise access costs regardless, right? This is not an EOF specific thing. 

**Pawel Bylica**
* And I don't think that matters because you just count like 32 bytes chunks. And yeah, so like you have execution probably will need less of these chunks. But that's the only effect. 

**Tim Beiko**
* Okay. Let's move on from EOF. I want to make sure we also have time to cover for fours.  and I guess on that front,  I know we had someone from portal to give an update on their history network.  so maybe we can start there. And then if there's any other updates on for fours, we can do those. 

**Kolby**
* Yeah. For sure.  I'll share my screen quick. Okay.  I wrote an FAQ for this, but I'm probably just going to go over, like, the highlights and what I think I should share to just, like, kind of make clear what portal is and what our goals are. So a quick tldr The Ethereum Portal Networks is a collection of separate peer to peer DHT networks built on disc v5. The current goal is making execution layer data accessible utilizing minimal resources. Currently, we're working on three different portal subnetworks history, Beacon and State, each with their own timelines and when they're expected to be online.
* Portal has a verification first approach for Ethereum mainnet data, and this plays a big part into our guarantees over generic solutions. We currently are building three clients, but we have been in talks with a few other of the EL teams.
* Some have expressed interest and we have also heard of like other third party teams who aren't really in layer one, who have who have expressed interest.
* The portal history network, which will be the main like 4444 this network which will provide,   headers, block bodies and receipts.  we kind of have three major milestones for this. When it says quarters, we mean we're planning to get it out by the end of the quarter.  The first milestone would be validating all pre-merge block history. So this would be like the first 15.5 million blocks and we're planning to hopefully get that done in Q2.  The thing holding us back from launching that is mainly just,  like, asynchronous,  bugs in our code base.
* And. Yeah, The second most interesting one, I'd say, is about being able to provide and validate all up to the latest, everything but the latest epoch of blocks. 
* We're hoping to get that in Q3 and providing that validation.  people will also have to run a portal beacon client. What is what is a portal beacon client? Basically, it's just a portal network which provides all the data to validate post merge data will be using it in both the state network and the history network.  it's more of just like,  getting the stuff you need to validate stuff network. And then in Q1 of 2025. We plan to be able to provide all the historical data. Is portal, the thing I turn on when I need history or should it be run continuously?
* We expect users to do both, but we really hope people do leave it on in the background.  portal is meant to be a very resource efficient, so we're hoping that it shouldn't really be an issue.  hopefully in terms of resources, it's on the lines or a little bit more than running a disk five client, as that's what we're built on. So that's a little, I guess, reference point. Of course, the clients may be storing or,  storing data or collecting data to store on their node, but that can be limited,  to how much it does, like a max basically connection count.  we use an XOR metric. So lookups for data on the network are in log n time.  do individual portal network nodes store all the block history?  in normal cases, no.
* And we really recommend against this because if you store all the block history,  people won't be really able to find it easily on the DHT because we use,  metric on how close data is to a node. And we'll ask the closest node first. 
* Every person who runs portal will be able to configure their own amount of disk space they want to allocate, so it's completely opt in. Is the portal network robust? What if a node goes offline? So the main way the portal like a portal network gets robustness is through replication values on the network.  how will this look like? Let's say you have 400GB of you only need 400GB to store all the history on the network, but you have like a terabyte of total space on the network. You would have a roughly around 2.2.5 replications of the data.
* The more replications you have, the,  the less likely of a chance that all the nodes that have the data go offline.  I believe I've seen a year ago a graph IPFs had, but also other DHT networks had on metrics on like how long nodes set.  which is kind of interesting. I should post that. Oh, what? 

**Tim Beiko**
* Yeah. Sorry. There's a question in the chat. I think,  that might be useful in this context is,  if you can talk a bit, maybe about the incentives of running portal,  whether or not there are any. And  if there aren't,  like, what is the plan?  to get this, you know, up and running at scale so that,  like, the execution layer can eventually depend on it? 

**Kolby**
* Yeah. For sure. So I was actually just about to get there. So there's this big question.  do you assume nodes will store the data altruistically?  the assumption is there's inherent value in this data itself.  there's also intrinsic value in having access to this block history and the cost of running a portal node being extremely low, as in, you should be able to run our client and you wouldn't even notice it's there.  So we are planning to have no monetary incentives. And one of the major reasons for this is because when you bring monetary incentives, like into the frame, it's kind of like a race to the bottom who can provide this data the cheapest and normally normally those kind of incentives don't really align with the health of the network.
* But who can like basically min max the reward for what you need to provide? 
* So realistically over time, as the network gets bigger, the amount of like default storage a node will use will look lower more and more, and that will just decrease the cost of running portal.  like as the network grows, assuming people actually want want this data. So yeah so who do we expect to run these clients? Well, probably we would expect, like, maybe an EL client who wants to provide a good json-rpc experience.  let's say you have a post 4444 this node, and someone queries,  transaction receipt from block 5 million. If they're running a portal client, they would be able to just,  take that call.
* They check their database, it would be a missing hit, but they could check portals to see if that receipt ever existed, and then they could return an actual, like the actual receipt. 
* Instead of saying, I have no idea if this block ever existed for people who are going to run portal altruistically,  we expect,  like we expect to like bundle like a portal client with like,  the, I guess the BitTorrent clients. What are going to be hosting,  era one files,  era one files for anybody who doesn't know is the,  it's just the archival format for pre merged data. And yeah, so we expect portal nodes to be ran alongside those as they are providing pretty much the same data. 
* So the cost overhead to run a portal node alongside that is also extremely low.  I hope I answered that. But yeah, I'm going to avoid like any like deep things. But on the history network we provide a headers block buys and receipts. 
* We also provide a header like header epoch accumulators which can be used on Pre-emerge to get a block number to block hash indexes. This is like kind of a fuzzy thing. We're going to have it for a certain amount of time.  but we can talk about that in detail on other time. So we have that roadmap the beacon client is in that. And then let's see. I think the last thing I just want to say is, does EIP for FAS include,  EIP 4844 blobs.  blobs? No.  blobs are supposed to be transient. EIP 4444 is a proposal for the expiry of Ethereum mainnet. Headers block wise and receipts.  not blob expiry.
*  I just wanted to mention that as I seen some confusion on like, what will that include?  and then,  I guess I would just want like, client to talk about Aero one because he's kind of like the spearhead of that. 
* And if anyone wants access to Air one to experiment with, I guess like the file archival format for pre-merge.  we have some posted in the history expiry channel, but if there's any questions asked me, I'm happy to answer them offline. And I'll provide a link to the FAQ and expand it whenever I get more questions. But that is everything I wanted to go over. Just like a high level overview of what portal is and trying to focus on any of the main confusing points or pain points.  thank you. 

**Tim Beiko**
* Yeah, there were a couple of questions in the chat, but I think we covered the biggest ones. It's probably worth. Yeah. Matt, giving you an update on the aero files and then doing more questions after that. 

**Lightclient** 
* Hey,  era the era one format, just to be clear, slightly different than the era format, which you might have heard of in relation to this format that, I mean, both formats have sort of been developed by the Nimbus team, but the ERA format is focused specifically on providing consensus layered data, which Post-merge has the execution layer data as well. And so the ERA one format is really just focused on all of the data that we need to provide for historical purposes that occurred before the merge. And so the format of it is execution layer data only. So blocks, bodies, receipts, the total difficulty of the chain, etc..
* As for the format, it's more or less been specked out for the last year, and in the last year there hasn't been a lot of discussion or changes on things. It seems relatively stable.
* I think the biggest thing that came up over the last few weeks is we're realizing that the compression format that we're using, snappy, is relatively platform specific, or at least implementation specific in terms of its byte for byte guarantees. And so we can't take a a simple hash of the ERA file format to get a checksum. It ends up changing whether you export with Nethermind or geth. And that threw a bit of a wrench into the situation, but I don't think that it's necessarily any kind of deal breaker. I think that generally we should go forward with the format as is, and we should rely on this accumulator data structure, which Colby talked about.
* This is something that the portal network has come up with, and it's basically just an SSD object that allows us to quickly share a route that represents the accumulation of all of the pre-merge blocks. 
* So their format has this thing. It does verify across all of the platforms. And that will be the main way of validating that the data you download is correctly. I think if client teams want to provide a checksum for convenience, we can do that. But,  it's not going to be the recommended way to verify everything in terms of like next steps for error one. I think we're we've got some implementations in Nethermind, other people are looking at implementing into clients. We really just need to go ahead and, you know, put the stamp on the spec and then go ahead and ship it and then start trying to get providers to provide this data because the spec itself exported, the data is great.
* Verifying the data is great, importing the data is great, but until the data is available, we can't actually move forward with removing the data on the P2P network. 
* So I'm thinking in the next 1 to 2 months we'll see era PR start to get merged, and then we'll get the data out on BitTorrent. We'll try and find some people to serve the data, and we'll have to give it around a year or so to make sure that the availability is to the degree that we want it. And then, you know, maybe sometime next year we can discuss actually turning off the sharing of pre merged data over dev P2P. And it doesn't necessarily need to go into a hard fork, but I think we're probably going to want to roll it out in unison. So it would be a upgrade of the Eth wire protocol most likely. That is all the updates I have for everyone. Happy to answer any questions on that or if you have questions on portal. 

**Lukasz**
* So I have one question about  okay. It's fairly straightforward. What would happen if a client,  user would want to have the whole history? He can download zero one files from either portal or, or,  like a BitTorrent at once and get it.  but I'm a bit interesting in the more interactive,  like  lightclient  use case. Right. Especially with Verkle now with,  with portal network and 4444 you can store potentially very small amount of history.  but how would an l client, existing EL client interact with a portal,  network?  would it be through a different process on portal network client, or do we expect it to, like, bundle in process?  like, this is like an open question. What? What do you think about it?  how how what would be the best approach? 

**Kolby**
* I think clients will do both.  depending on, like, what they want and the use cases they want to support.  for portal, we're probably not going to be bundling era 1 files into, like, our architecture ourself. We're going to be supporting a lookup model where you use a block hash and an index of the type of data you want to fetch from the network.  one of the reasons for this is to have nodes would have really low requirements.  I believe the biggest one is like 600 MB. 

**Kolby** 
* So yeah, I guess the question would be the answer would be like both. We'll probably end up saying. 

**Lukasz**
* Okay, so,  two more questions about it.  one, I haven't seen in the document a lookup from transaction hash to, for example, block body or something. So without with having just only transaction hash we cannot find anything in portal network. 

**Kolby** 
* I think in regards to that, so you said you would need a transaction hash to block hash lookup. 

**Lukasz**
* Yeah, something like that. Mhm. 

**Kolby**
* I believe how we're going to be supporting that use case is we're going to most likely make a new portal network just for storing those indexes. So then you could do a quick look up there and, and then you could do a quick lookup on the history network. Would is how I believe we would implement that functionality.  but I could look into that specific use case more and get back to you offline. 

**Lukasz**
* And last question, if I for example in Nethermind want to prototype integration with portal network for this use case of interactive one. Just looking up things on the fly.  how problematic is it. Do I need to implement like the full portal network protocol or only some parts of it to doing the lookup and how,  would it,  affect the network if I would be only doing the easier part for the lookup? Right. Because I'm EL and I'm not really interested in, like, maybe doing everything. Yeah. Leaching. Exactly. 

**Kolby**
* Okay. I can't,  I think I heard all your questions, so,  I think it would be. So basically, implementing portal is just cloning. Is cloning,  the cloning, the basic routing table and parts from disk v5. And then just calling that portal. So implementing portal in that way is pretty simple for I guess in like prototyping with a client.  the recommended thing I would think is bundling, like,  an already built portal client with your client and interfacing it using IPC, I believe.  we have Json RPC endpoints to provide the data. We have some lower level like portal ones, and we're also planning to provide like,  actual Ethereum Json RPC endpoints. But I'm assuming that,  like layer one, clients would want to like access the lower level calls.
* But yeah, probably something like that IPC for prototyping. And then if you find it's worth the investment then looking to build your own client and. Yeah. 

**Ognyan**
* Well in in Portland we have a different types of overlay networks. And for example, to access the the history network data. You don't need to run all Of the overlay networks that that where we are going to implement. For example, for the history network, you will need only the beacon portal network, which is used to track the the head of the chain. And then if we decide to implement this transaction,  history,  overlay network,  you will need that to,  to be able to hook up for a history data by using only, A transaction hash. So it will be transaction index, overlay network. And for example to access the state network data. Then you will need to run   the Beacon network and the History Network,  alongside the  state network.
* So. You have some kind of choice to make there, which networks you want to run based on what data exactly you want to access? 

**Tim Beiko**
* Okay. We only have about five minutes left.  I think we probably have enough context on portal to at least have a rough idea of, like, where it fits in.  I guess probably the most valuable thing at this point would be to hear from the different EL teams.  Yeah. How they're feeling about basically EOF Verkle and 4444.And I think for for Prague specifically, there's a bunch of small EIPs that were all considering. So,  you know, we already have three that are slotted in.  So it's probably not worth going into, like all the small things we can do in addition in Prague, but just,  yeah, with regards to EOF, with regards to Verkle and with regards to, 4444 like are those things we want to prioritize for Prague, do we want to pre-commit something like Verkle in the Osaka fork?  yeah. How the EL teams feel about that.
* Do you feel like ready to make a decision? You have a strong view, or do you want to spend more time thinking about this and going over stuff,  outside the call? 

**Lightclient** 
* I'm just curious if other client teams feel similarly to me here on 4444, it feels like 4444 is pretty orthogonal to a lot of the changes we want to make on main net, and it's something that's somewhat pressing for teams. I mean, the history is growing hundreds of gigabytes of a year. And it's this isn't a really big lift to just like continue working in that direction to actually start lowering the history requirements. We're, you know, one year away from doing that. Probably. So I think it's extremely high priority and really low touch for teams to be putting some resource to that today and getting down that path. 

**Tim Beiko**
* It seems like. Nethermind and Besu. Okay. So and I mean, yeah, the work is already happening, so,  it doesn't seem like there's a reason to stop it. And it's just worth being mindful that, like, the time and effort we spent on that obviously reduces bandwidth for other stuff. But if it is a minimal lift, then teams are already working on it. We can we can keep that going. 

**Lightclient** 
* I really think we're like looking at around one month of effort now ish, and we don't have to have every client team. I think if we have two, maybe three client teams do this, that's really what we need to start bootstrapping this arrow one distribution network. And we can, you know, I can go off and try and work with some people on what to do for the future for ERA, but I think getting ERA one off, like we're very close to it and there's not a lot of work that needs to be done at this point. So if client teams are good with, you know, I think Nethermind is working on I'm gonna talk to Basu later. If we're good with doing that, then let's just get that out and then we can come back in 6 or 8 months and figure out how things are going. 

**Tim Beiko**
* Andrew. 

**Andrew**
* Yeah.  4444. So in, in Aragon, we actually have to do a major release first.  and we call it Aragon three because in Aragon two, we need to re-execute all the blocks from Genesis.  and for that, we of course, need all the blocks. Right?  yeah. So Aragon three is a few months away. So for us, like after that, 4444 , will be easy. But beforehand we've we have to do a mammoth engineering effort.  yeah. And in terms of EOF and work, work, I've already said that my preference is to commit to EOF in Prague, with the caveat that if it's not compatible with vocal, we don't ship it. And to commit to vocal in Osaka. 

**Tim Beiko**
* Okay. Thank you. And there was a comment by Nethermind as well around,  committing to Verkle in Osaka and like a weaker view on EOF in Prague.  And then obviously from the Besu side,  there was a desire to do,  EOF in, in Prague. Um. I guess, and we sort of have a minute to end on here.  it feels like EOF sort of has to be considered a bit more in parallel with the other potential EIPs for Prague.  whereas the decision for Verkle in Osaka is a bit more independent. So do people want, I guess? Does anyone object to committing to have Verkle be the main thing for Osaka?  and figuring out on the next call a bit more,  the exact scope of Prague and what we want to include there.  knowing that, like, we already committed to Verkle for Osaka. Last chance. If there's objections. Otherwise, I'll open a PR for the Osaka spec,  later today. 

**Ansgar**
* It makes a lot of sense. But I do think just given that it's a, relatively rare that we are planning. For features that are basically a year plus,  out still and just kind of from historical experience that sometimes things slips quite a bit. We should at least be open to say revisiting this in 6 to 12 months. If by that time, for some unfortunate reason, it turns out that just vocal takes massively longer than planned. I mean, I don't very much don't expect that.  but I'm just saying we should not be a hard commitment. 

**Tim Beiko**
* Yeah, I think that's reasonable. And I think basically the the thing we also can commit to is like working on it in parallel to shipping Prague, like we did for the past two forks.  which means that, you know, in,. You know, in the in the time until like the next 12 months will build up our confidence towards like, is this thing  actually ready to ship rather some issues. We didn't, but,  yeah, I think, you know, based on a lot of like, the Verkle folks comments and what teams want to prioritize flagging this explicitly as the main priority for the fork after,  Prague and having teams start to or, I guess, mostly continue to invest engineering resources and develop, this probably is what makes the most sense. Yeah. Any other comments? Concerns? Okay.
* And we're already one minute over time, so  I'll just give a quick shout to the other three,  agenda items, but I don't think we we have the time to go over them.  first one was,  specifying the client versions on the engine API. The idea here is that it would maybe help.  it would maybe help identify,  what what else are working on? There's a lot of conversations on the thread already, but if people want to,  go there, hopefully we can get it merged in the next couple of weeks.  then, uh. Peter,  you had something around or actually. Yeah, someone asked to review 523, but I'm pretty sure we agreed to this a while back. Um. 
* So. Yeah. Powell. Maybe,  if you want to chat in the RnD discord, exactly what the ask was. But I'm pretty sure we had agreed to the empty accounts,  because we'd already cleared everything on L1. And then last one,  Carl,  asked,  about just reconfirming,  the decision we'd made around reserving the precompile range for L2 precompile.  I believe there were no objections to that last time, but if there are any,  maybe just raise them on the Eth magicians thread for this in the next couple days. Otherwise the EIP is going to move to last call and,  be finalized. Yeah, I think that covers everything.  and then next call, let's focus on the various,  potential EIPs for,  Prague and try to scope that out a bit more. Anything else before we wrap up? 

**Mark**
 * So I just wanted to point out that there's a new PR in the engine API. We're trying to get some data so that we can measure execution layer client diversity, which is crucial as we move into the Dencun fork.  so if you haven't seen it, please check it out. Way in trying to get more awareness. Thanks. That's all. 

**Tim Beiko**
* That's 517, right? 

**Mark**
* Yeah, it's in the notes. It's in the notes for the meeting. 

**Tim Beiko**
* Sweet. Well, okay.  Let's wrap up then.  yeah. Thanks everyone. And,  also, yeah, if everything goes well on the test set, we figure out these,  these bugs,  will be setting the date for main net,  next week on ACDC. So please show up there to discuss that. Yeah. Thanks, everyone. 


-------------------------------------
### Attendees
* Tim Beiko
* Danny Ryan
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
* Stokes
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

-------------------------------------
Next meeting on Feb 15, 2024, 14:00-15:30 UTC

