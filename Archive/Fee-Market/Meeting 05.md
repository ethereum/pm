# EIP-1559 Implemnters Call 5 Notes

### Meeting Date/Time: Thursday, Oct 8th, 14:00 UTC

### Meeting Duration: 57 minutes

### [GitHub Agenda](https://github.com/ethereum/pm/issues/209)

### [Audio/Video of the meeting](https://youtu.be/SHVfypwL5W8)

### [All Meetings](https://github.com/ethereum/pm/tree/master/Fee%20Market%20Meetings)

### Moderator: Tim Beiko

### Notes: Alita Moore

---

# Summary

## Actions Required

| Action Item | Description                                                                                                                                             |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **5.2.1**   | Abdel to look into if a block explorer endpoint already exists in Besu (for example) and then if it can be standardized to accomodate 1559 transactions |
| **5.2.2**   | Micah to add the 1559 change to reporting miner or user gas fee to the security considerations section on the EIP                                       |
| **5.2.3**   | Tim to give someone the task of writing the specs for the new EIPs (transaction by hash, block by hash, and send transaction, block by number)          |
| **5.2.4**   | Abdel to write the EIPs                                                                                                                                 |
| **5.2.5**   | Setup a single client proof of work testnet the follow with more clients                                                                                |

## Actions Required

| Helpful Link Item | Link                                                                                                               |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ |
| **5.3.1**         | [blockchain pricing investigation](https://github.com/ethereum/research/blob/master/papers/pricing/ethpricing.pdf) |

### Agenda

- Status updates from implementers and researchers
  - Decision on the merged transaction pool PR: ethereum/EIPs#2924, incl. the transition from legacy to 1559-style transaction and the transition period.
- Thoughts on EIP-2718?
- Mainnet readiness checklist
- Ethereum Cat Herders' Community Outreach
- Anything else (please leave a comment)

# 1. Status updates from implementers and researchers

**someone** - So we are recording to the cloud. Thanks, everyone, for coming to the fifth 1559 implementors call joshed agenda in the chat. Basically, there were a couple of things I wanted to cover today. First, just to get kind of a status update on both the implementors and researcher's side, I think Abdul and Barnabei can help cover it up. And we had to merge transaction proper to talk about what I've got this guy today saying. So that's already merged in. And the two other things I guess I'd like that to get people's thoughts here on are the survey I just shared last night, which gave a lot of, I guess, projects concerns about 1559. I'm mostly interested in like the stuff that relates to implementors around Jason, our bases and our codes and whatnot. And if people have suggestions of how we can plan to just include that to make it easier for projects to test. And then there was another document like the main net readiness checklist, just kind of walk through what are the things we'd like to see from 1559 before it gets ready to bring back the accord. Assuming that considerations. I know last time we had talked about moving like a proof of work testnet so I'm curious to get everyone's thoughts on that and what the best next step is from where we are right now. Yeah, so maybe we can start with updates abdel do you want to just give a kind of overview like I think it's been like a month since the last call. So what you and the other implementers have been working on?

    Geth

**Abdel** - Yeah. So we have been working on implementing the latest changes from the specification. So the computation basically has been changed and we have achieved its implementation. Currently we are deployed the testnet from scratch and we were able to sync also with the nethermind clients, which is great. And now I'm finalizing the remaining changes, the removal of the transition period and also the use of single transaction. So that will be available, I hope, tomorrow and I will restart to refresh this net with certainly a version aligned with the latest specification we are also aligned with about the gas price behavior. So nicasio made the PR and the I approved it and it has been merged. So we decided that the gas price OPCODE should return the effective price the user will pay. Actually this is a minimum between hiccup and miner bribe plus the basic and yeah this is it. And yeah, I was able to sponge the network and reach almost the maximum block elasticity. So I was able to target thirty eight million gas blocks and everything was fine. So this is pretty good. That's it.

**someone** - That's great. Do you know you mentioned like you're working on the latest changes of the spec, do you know where the go implementation and implementation are at with regards to that?

**Abdel** - I think lightclient is on the call, so maybe he can give an update about nethermind. But I know that geth people, So Vulcanize is still investigating the consensus issue. So I'm giving them some help using the transaction center to to try to produce a consensus issue.

**Tim** - do you know about nethermind?

**Abdel** - Yeah, I said that I think that there is someone.

**Tim** - I don't think so, light client is not from nethermind.

    Nethermind

**Abdel** - Oh, sorry. OK, sorry. So, yeah. Yeah. I mean, so they are also aligned on the basic computation. And I saw in the charts that he already removed the transition period. So that should be fine. When I will be able to deploy these nodes, we should be able to sync again.

**Tim** - Great. I know someone kind of jumped in to say something while you were talking. OK, cool, Barnabei, do you want to give a quick update on the R&D side?

5.3.1 | [blockchain pricing investigation](https://github.com/ethereum/research/blob/master/papers/pricing/ethpricing.pdf)

**Barnabe** - So, yeah, um, so Basnet published a new book on strategic users that was the latest, let's say, a public release. The idea behind it was to kind of look at this idea that, uh, well, 1559 is useless because anyway's users will keep competing on the cheap. And I think what the new book really shows is that, uh, you can have this sort of strategic behavior, but it doesn't last very long when the network is not subject to wide, let's say, shifts in demand, which is most of the time. So yeah, that was published. Maybe I can draw a link in the chat. we've been working with Fred, who's on the call, uh, looking at the transition period out of the legacy transactions into 1559. So trying to model it, trying to simulate it and even trying to look at an idea that was floated around with the discord channel, uh, to have some kind of tax on legacy transaction where the tax is increasing over time, uh, which is kind of like the stick to the carrot of making users, uh, shift out of using the legacy transaction and into, uh, 1559. So we intend to to model it. And then another new book on the floating escalator or the combination between 50 and 59, an escalator. So trying to understand a bit better, like what it looks like. Uh, I know that the escalator hasn't been talked about for some time, and I feel the consensus is more like, okay, we should just go ahead with 1559 and not really bother with the escalator. But anyways, I think it's still interesting in the in terms of like research, even as it's an extension to this strategic behavior notebook. So that's under review and it should be published also fairly soon. And the last one that I've been working on and that I think is quite nice. So when the, let's say, strategic review tackles this idea that, uh, 1559 is just going to degenerate into like a first price auction, you're learning users. I'm trying to tackle the idea that, uh, 1559 is a UX improvement. So this I think is not really understood really well by users or by whoever is looking at 1559. Like what do we mean by UX improvement. Exactly. And so what this learning agent is trying to show is that uh, over time agents learn to you will be you will take the price that 1559 is giving them. So basically the base fee or leave. Not, not, not even until the Q and in that sense is an improvement because over time you're learning to just become like a price taker. So the market is just quoting you, OK, it's 100 wei to get in now take it or leave it. And that's it most of the time. So on and so on. You see over time with is learning new skills. But after a while I understand that, OK, I should I should probably just take it or leave it. And you can really see even, uh, like this idea of UX improvement dynamically, let's say, appearing just from the interactions of the user. So I think it's quite, quite interesting. And then related to that, um, I think it's something I discussed. I mean, the discussion about looking at what it defaults. So this idea that most of the time you're a price taker, but sometimes the base fee is shifting very rapidly. So you have like units were launching that token or something, and then you might not want to be a risk taker anymore. Then you might want to revert back to this, uh, strategic behavior, which I look at in the first book. And in that case, probably you also want your wallet to kind of shift from this price taker or this price quoter mode to a mode where it gives you more flexibility to say, no, I really want this transaction to go in quickly. So I'm willing to pay a much higher premium. So when should that be like when should you switch from one to the other and what should the default be in the wallet? So most likely default will look like what you currently have, like free, like fast, medium, slow, something like this. But how should we set this parameters? Yeah, that's that's kind of where I'm at at the moment. Yeah.

**Tim** - That's great, yeah, that's a lot. So I had a couple of questions, I guess the first one around like that, the transition period, do you think are you like that still makes sense if we've, like, removed it from the EIP with the with because recent PR,

**Barnabe** - I should have specified that the transition period we're looking at is Mike SBL So I'm not looking at the previous model. I'm looking at Migues where you guessed the legacy transactions into the 1559.

# 2. Ethereum Cat Herder's Community Outreach

Video | [10:53](https://youtu.be/SHVfypwL5W8?t=653)

**Tim** - Okay, yeah. OK, got it. I'm. Yeah, anyone have thoughts, comments, questions? Ok, and in that case, yeah, I guess I can share my screen real quick, so Cruger myself and a couple other folks from cat herders spent the past few weeks reaching out to a bunch of projects to get their thoughts on 1559. So there was a lot of feedback. We shared a report detailing most of it. And I'm not sure most of it is relevant for this call. But the bit about the implementation really is. And so I was curious to get people's thoughts about how we can address kind of. How we could address the things that people mentioned would help them prioritize 1559 support. So we asked project what would make your life as easy as possible to support this? And obviously, the first thing that came up or the thing that came up the most often was having a public testnet, but especially having one that's suitable for like end user applications to use. So that has Jason RBC support for 1559. And and it was also mentioned that it would be great if this was kind of standardized across clients so that there's not like any major differences between besu and.. Go ahead

**Abdel** - Yeah, I would suggest something about that. Instead of implementing our points in each client, I to suggest that we implement only one micro surface dedicated to that. That will take, if it's interesting, transaction parameters and will create and sign the transaction and submit them to ethereum client unless we think we will have it in production on mainnet. But I'm not sure I think we can do that and avoid that every client to implement it.

**Tim** - So that would work for sending. But would it also work for reading transactions? Because I think that was one of the other concerns that came out, like just being able to query, you know, the transactions and whatnot on the network. Uh. I see, yeah, like how do you expose them right now in the block Explorer?

**Abdel** - Basically. Oh, yeah, maybe we can update the Front-End actually and implement the decoding logic, actually. Yeah, so that will be easier actually to display eth 1559 transactions in the explorer.

**Tim** - Yeah, but I guess what I'm wondering is how does the Explorer get the data from basically right now, like how does it query it?

**Abdel** - Oh, I don't remember the exact endpoint, but..

**Tim** - OK, because there is such that I feel like if there's something already in Besu that at least the block explorer we have used, maybe that's a good first starting point for something we can, like, standardize across clients and just make a bit more explicit. So it might be worth looking into that.

5.2.1 | Video | [13:22](https://youtu.be/SHVfypwL5W8?t=807)

    Abdel to look into if a block explorer endpoint already exists in Besu (for example) and then if it can be standardized to accomodate 1559 transactions

**Abdel** - OK, yeah, I will do that.

**Tim** - So just taking a quick note, yeah, and then obviously the other thing people mentioned was like having to be part of a network upgrade. I'm not sure we're quite there yet. And then this might be interesting to you, Barnabei, but the incentive, like a couple of projects mentioned, like if there was any incentives with regards to gas prices, specifically the U.S., 1559, they say they would prioritize it. I think Micah's PR kind of gets us part of the way there at least right where if you can keep using legacy transactions, you'll just pay a higher tip to the miners. So the I guess the converse of that is like if you use 1559, you'll pay a lower, lower price. Yeah, I think that's maybe sufficient to start but I'm curious if other people have thoughts about that.

**Banabei** - Do we understand from that that the project is incentivized to implement it so that its users get to.

**Tim** - Yes. And that was like, I guess the common theme for the projects who are most willing to implement nine as soon as possible, are projects who really cared about, like their users gas price experience. So I think that, yeah, having having their end to end users of someone like Argent or Bitcoin be able to pay a lower gas price was a good motivation for them.

**Banabei** - Ok, that makes sense, not incentives to to pay them to implement.

**Tim** - No, no, no, no, no. Yeah, it's like the net. Yeah, the transaction is all right. Yeah. Um, um. Yeah, and the other thing is, so the other thing that was mentioned, it's like having obviously like the basic library, so if there's a jazz band with three jazz support, this as soon as possible would help because lot other projects basically just rely on that. So that Ether's suggests maintainer said it should be pretty easy for him to add support for it. The other thing that was mentioned is that just having like a clear opcode definition. So a lot of projects, smart contracts rely on transactions that gas price. I think we need to understand what are the implications of changing that. So right now, from what I understand, the change that was made would only affect 1559 style transactions, which shouldn't break anything that exists. But I don't know if there's some weird kind of, I don't know, second order effects for contract developers that the API changes what it returns based on the type of transaction. I don't know if anyone has thoughts on that.

**Micah** - I believe we're pretty safe on that front, the way we ended up selling gas price for 1559 transactions makes it so it's basically still the same thing. So it means this is the gas price that the user paid. The one caveat is previously for legacy transactions. The gas price a user paid and the gas price a miner received are the same and 1559, the gas price that a user paid and the gas price a miner received are different. And so previously the gas price of code could have been used to identify how much a miner received for the transaction theoretically, and also use to identify how much the user paid for the transaction was one, two three 1159. It only represents how much the user paid for the transaction. Now, I don't I don't know of any applications that care about how much the miner got paid. They there are many that care about how much the user paid. And so that's why they went with that.

5.2.2 | Video | [~17:26](https://youtu.be/SHVfypwL5W8?t=1046)

    Micah to add the 1559 change to reporting miner or user gas fee to the security considerations section on the EIP

**Tim** - Is that worth adding to like the security considerations section of the EIP? I feel like I'm the backwards compatibility section.

**Micah** - Yes. Send me a message after this and I can go at it.

**Tim** - Ok, I'll write a note for that. Yeah, I feel like somebody might look at that and find some something with but that makes sense. And I guess the other thing we discuss in the past is like the base fee opcode. That's not part of the EVF, right.

**Micah** - It is not and and there is a push where, you know, there's there's a push currently in the from the courts for various reasons to actually get rid of gas and respectability in general from the EVM. And so that would probably hurt our chances of inclusion if we're adding things that make it so people can inspect gas stuff.

**Tim** - And I guess so right now, the only way to get the Opcode is to get the blockheader right?

**Micah** - Yeah, you could so you could prove it on-chain, so you could get the transaction proof and then prove it based on the block hash if you really wanted to. But that could only be done afterwards. So that could be the next block that you can do that.

**Tim** - Yeah, and I think that kind of relates to the next point is people would like to see kind of an API that takes that tells you what the base fee will be for this block. So you take the previous block, you calculate how full it was and therefore you estimate what the next block base fee will be. I'm not sure this falls within the skills of people in this group, but something like that, the sort of gas station like API that just does that that much for them is something people mentioned that would make it easier for them to to add support for 1559.

**Micah** - I don't think that will be particularly difficult. And do they want that from the clients or do they want that just like a place they can go on the Internet

**Tim** - A place they can go on the internet. And, yeah, this call is recorded and will be uploaded to YouTube. So maybe somebody picks this up, eth gas station if you're listening. Yeah, that was I was brought up and then yeah. Obviously the rest was kind of pretty standard. But, you know, just having good documentation like we just mentioned, I think around the the opcodes and explaining with the changes in behaviours are communicating changes to the EIP and whatnot and having channels for support. And I think with the discord there, it's been kind of a decent place so far. If if, like the volume grows, we can maybe move this to some other place for for support specifically. But yeah, that was kind of the gist of what what would help various projects kind of implement the EIP. One thing that was nice in this survey as well as there was like a pretty yeah. There was like a pretty smooth distribution of like when projects would start would want to start working on the EIP. So I feel like as this develops, we'll probably get more and more users who are slowly kind of trickling in and are interested. So it's nice to just start with kind of a smaller batch of people who are like very interested in this and want to see it done ASAP and then slowly reach out to more projects.

# 3. Mainnet readiness checklist

Video | [20:53](https://youtu.be/SHVfypwL5W8?t=1253)

**Tim** - So that's basically what I had on that, and then the last thing I wanted to bring up was just this kind of Mainnet readiness checklist. So I think a lot of people in the community had been asking for a date for 1559 because that's obviously impossible to give to people. The other approach is to give them a list of things to do and and try to obviously updated as we learn new information and and we make progress on it. So in short, obviously, we'd need all clients to have an implementation right now geth, besu, and nethermind are working on it; nethermind, I believe is still hiring someone as well to do this. So if you're watching this and you're interested, you can you can click the link and apply for the job open. Ethereum and Turbogeth are fine with joining the implementation later. Talk with them. And I think they don't have as much interest in implementing every incremental version of the EIP. But once it's actually done and settled, it should be a major challenge for them to implement it, especially with the the recent changes to the transaction poll and whatnot. That makes it a bit a bit simpler for trying to implement in terms of like the open issues. I think the biggest one we discussed this on all core devs, but is the denial of service risk? I mean, that this is something I don't think I can address head on. There's a couple efforts that are being done to address this. So there's EIP 2929, Geth is working on snapshots, besu is working on another flat database approach that that that makes these denial of service attacks less likely. Turbogeth is optimized to deal with that as well. And so I don't think again, 1559 can directly address that. When I asked about changing the block limit, people didn't seem to think that would make big enough of a difference. So going from one point five to X instead of two X didn't seem like it would, it would make 1559 much more likely to be adopted sooner. But it's really more about having my client level basically databases that sort of state in a flat format instead of a tri and everything that goes around that. I don't think it should have a major impact in terms of timelines if given that there's still work left on 1559, that it won't be in the berlin upgrade. I think it should probably land the upgrade after that. And that also gives time to the clients to work on that. And then next up, the transaction pool management. This is basically moot due to Micah's PR so I'll update that. transaction encoding decoding was the other big question. And I know Abdel you've mentioned in the past that EIP 2718 would make this easier. I'm not sure what actually is the status on 2718. It's it seems like it's kind of in limbo for Berlin. I don't know if anyone has kind of a better view on it than to me.

**Micah** - It's in limbo for Berlin. I almost certainly will go in with or prior to 1559. I don't see really any reasonable path where it doesn't go in. There's enough things depending on it, that it's going to go in either Berlin or immediately after.

**Tim** - Ok, and does it make sense to, I guess, keep doing what we're doing for now and once it's accepted, we at that point in time to support it?

**Micah** - I don't think so. I if it were me, I would just switch everything over to 18 so we don't have to deal with it later. I think the odds are 2718 not going in are so low that we should just move forward with it personally. But I'm not an implemenator so.

**Abdel** - We could do something like if if we don't want to delay security audits and all that stuff, validation of the economy, then we can deploy public test net with the actual implementation, because the type transaction, until we don't change any of those results and on the integration integration test, that we could start implementing it. Maybe we can do this.

**Tim** - oh, so have like two versions of it once. So once we have like a more public GasNet, then we get that up. [yeah], I think, yeah, maybe that makes sense, and it also gives us a couple of weeks to see what happens on the core devs side and if it gets accepted in the next all core devs call, which is next week, I believe, then it'll be a bit clearer where things are at. Ok, and then the last thing was the transition period. This is also kind of, I guess. Micah, your PR means that there's no more transaction period at all, correct? [yeah] That's just we convert legacy transactions that 1559 and we allow that forever or we interpret them as 1559 and then we allow that forever.

**Micah** - Yeah, or forever means TBD. we don't have a currently built mechanism for getting rid of them, at least not in 1559. But some future EIP probably will maybe.

**Barnabe** - I think there is another thing that came out from the discussion -- replaced by fee. I don't know if we want to talk about that now, so I don't.. I think Micah has some ideas about how to deal with that, adding some transaction parameters. Can you explain that quickly?

**Micah** - So there's a few options. The I think I lost track so Barnabe may know more. But the one I think the first question is we need to establish exactly what everybody expects from the replaced by fee protection. So do you replace by fee naively? And you just say, hey, it's like the fees higher than you can replace it, you can replace a transaction with one ado eth. So one way gas price increase and that's effectively a no op, but it will force the whole network to copy your transaction and this is dead analysis of the attack vector where you can just bump the transaction by insignificant amounts forever and just keep hammering the network and the network will continue to accept your transactions. So we want to avoid that. The problem is that with 1559, if you bump just the miner bribe, there's no guarantee that the miner bribe will be taken because you could be hitting the speaker. And in fact, it is most likely that if your transaction is pending for more than a block, you are blocked by your block, but not by your miner. And so if you're the miner bribe, then we end up with the same situation where someone can just my miner bribe and not actually change their transaction at all if you're not paying anymore. And so there's some concerns about Denial-of-service attack vector. And if just bumped the fee cap, similarly, if your transaction is not pending because you're blocked, then that also does nothing like you pay the base fee. And if a base fee is below your fee cap, you can bump that to 40 million, then you're still going to pay the base fee. So something that doesn't actually change anything. So the the last option is, well, what if we bump both, I think this does work in most scenarios. I think there's some edge cases where it's possible to not have your actual fee change when you bump both. But arguably, we don't care that much about those edge cases because they're not really strong attack vectors. And as long as we have a minimum increase, then it also doesn't matter too much. The last option is to just say that, nodes will not propagate any transaction who's fee cap?.. Maybe fee cap + miner bribe, I'm not sure which, but probably just fee cap -- is less than the current base fee. This is a novel idea that we think needs a little more time thinking about. But in theory, if we did this, then all transactions that were being propagated should be able to be included in a block almost immediately. The only reason they can't be included in a block is potentially because they're too small. What this what this does tell us, though, which we also need to talk about is if the miner bribe is zero, let's say. we currently don't have a mechanism for pushing that out of the pending pool. It is possible to set a miner bribe that is below the miner bribe that every miner is accepting but have a cap that is higher than the base fee fee cap. Should that transaction be allowed to propagate? And if so, how do we define what the minimum miner bribe is to allow for a transaction to propagate? Do we do it like we do currently where we just say every every node in the network has a propagation variable, where that we were willing to propagate any transaction that has a miner bribe of this or higher? That's my simple solution. And we just hope those are generally set in line with miners? These are all things to think about and discuss. I'm currently favoring that last option where we say the nodes will not propagate any transaction that has a base fee lower than the current block base fee plus miner bribe set per node at startup. So each node can define what their miner bribe and they'll propagate everything else.

**Abdel** - So we don't propagate transactions on the [?], but we do accept them on the RPC end point if the price is below base fee?

**Micah** - Yeah, that would be my assumption, so that way your local node will always accept your transactions from you, you're talking directly to your own node, it's going to accept everything just like you just think it does right now, I believe,

**Abdel** - OK, it's not the case in this implementation. So I reject this action, but I will update the petition.

**Micah** - Ok, so I think I believe the other clients, at least open ethereum and geth and I'm pretty sure nethermind, if you were talking directly to RPC, will accept anything because it treats you as kind of a privileged user when it comes to what it accepts. And so we will accept it. And I think they all actually have a separate pending pool sort of where transactions are protected from being ejected from the vending pool on that node if the node received that node from RPC not on RPC.

**Abdel** - there are some rules, there is a minimum gas price and also minimum BAMF percentage, if the transactions comply with those rules, it will be accepted. And this is what we do for legacy transaction that we implemented the different behavior for each transaction. But OK, I see what you mean.

**Micah** - So like I said, that's that's my current preference, is that we go with the we basically just don't propagate anything that's got a miner bribe that the node thinks is too low or if fee cap that's too low. And then we can basically I think we can allow basically almost any strategy for free bumping for replace by fee, because the things that are being propagated are all things that should really probably be my next block. Like it is very likely that the thing that's being propagated is going to be mined very soon because the base fee is high enough and the miner bribe is high.

**Ahdel** - Ok, that makes sense. Thank you.

**Micah** - Do other people have thoughts on strategies, there?

**Barnabe** - But you could still increase your fee cap indefinitely, even if it's above a base fee, right? Again, I agree with this idea that you drop transactions where the cap is lower than base fee. But how does that prevent? How does that alone prevent me sending a thousand transactions with just a little bump into the fee cap every time that you still need the bribe and then..

**Micah** - So I think we still do need a minimum percentage, just like we have currently on the network, which is I think 12.5 percent for open ethereum, I think. But I think it matters less whether that's a fee bump or a base fee bump. Or both. That's right, right, bump or if he kept them or both of them. Like, if we're kicking out transactions that aren't likely to be mined soon and we have something that the user has to keep increasing. I guess it does have a miner bribe, doesn't it, because if it's base fee, then they can spam.

**Barnabe** - Yeah, I think you still need that. Yeah, OK, it's fine to have, like the base fee greater Loevy, you figure. But I think it's some kind of, uh, don't, uh. Yeah.

**Micah** - So the miner bribe has to be bumped by some percentage so we can keep it the same twelve point five percent and then the fee cap can stay the same. But if the cap of a transaction is lower than the last block's base fee, then they'll propagate it over the network.

**Barnabe** - That sounds good. Yeah.

**Micah** - So I suspect as soon as we tell this to the client developers, they're going to tell us that they're going to grumble about the P2P layer currently doesn't. Isn't synched with blocks for lack of a better term, like they because of rollbacks and whatnot, the P2P layer doesn't really know what the current state of the network is. And so client implementors historically have been very pretty loath to create a dependency there where the P2P layer needs to understand what the state of network is, because you can get out of sync like two clients can not agree on the current state network. So client will say, hey, I've got a new transaction. It's got a base fee that matches or is higher than sorry. It's got a fee cap that is higher than the base fee. You know, what you're sending it to, however, sees a different view of the network. And so they say, no, it doesn't. You're lying to me and you're now a bad peer. And so we have the problem network. How do we tell whether a peer is bad or a peer is just have a different view of the network? And so I think for that reason, historically, P2P layer has not it's correlated with blocks at all. Like they they they try really hard to not care about what the current state of network is.

**Tim** - Yeah, yeah, that feels like it would make things much more complicated if we needed to add it depended like if we needed to change kind of the statefulness of the protocol.

**Abdel** - But I mean, the higher layer you can do that in the transaction pool or something like that. You can select the transaction as not eligible for inclusion in the P2P network or can you. Yeah, I think it's manageable.

**Tim** - Yeah. I guess what I'm saying is I would push for similar to how you mentioned, you know, like I think the base fee opcode kind of goes against the current of the devs. With regards to the gas observability. I would try to. To keep things somewhat like philosophically compatible with P2P But if we can if we can do that verification just at the client level before we propagate it, I think that makes sense.

**Micah** - I think it works as long as as long as we don't it's not a condition for flagging a pear as bad, I believe the clients all have mechanisms for flagging a peer as bad, and eventually disconnect from them. We would need to make this a condition where you say thank you for the transaction. I still trust you, but I reject your transaction. And I don't know if we have that concept at the moment anywhere else. Like, it's usually either you either that you receive something that is very valid and you can assert this is good, thank you. Or your system is bad, in which case you say you're a liar and I'm kicking off of the network or disconnecting from you. I don't know what the client does I don't I don't know if we have anything that's kind of wishy washy like that, you know.

**Abdel** - This is bad that we don't have to geth people on the call, We should have some.

**Tim** - Yeah, we we can follow up offline with them and with other clients to see what they think. But clearly, the whole, I guess, replaced by fee is kind of a big open question. We still need to figure out

**Barnabe** - I want to point out as well that everything's going to be there's going to be some amount of complexity, even if you don't want to do the state Senate when you manage your transaction and when you want to check, like if you don't have a rule, for instance, that says refuse any transaction where the fee cap is not high enough, you still need to look at your transaction queue And update the order based on where the base fee is and how that might change the actual tip that you receive as a miner. So at some point in time, I think you do need to take into account the fact that this is moving and that the transactions that it is depending on.

**Tim** - But we can do that at the client level, right? Like, we don't need to do that over P2P.

**Abdel** - And also you can manage a delta between because you know that the best thing can go up or down, up to one on eight. So you can have an idea about how many blocks it would take to, in best case, catch up with the transaction price and you can evict or reject transactions that are really far from the base fee.

**Barnabe** - Yeah, I guess you can have like many different strategies as a client. [yea] But their P2P is not consider part of the client, is that right? [yea] That's what I was saying.

**Tim** - So at least part of the client. But it's a different spec...

**Barnabe** - It's not practical.

**Tim** - Whereas yeah. And whereas the transaction pool is kind of left to, there's no rules about what clients have to do with it each time they can do whatever they want and they don't need to agree with each other about how they handle it, even though even though like, you know, in practice most of their behavior ends up being the same, at least we don't have to write a spec for it that says this is how the transaction pool works. So so this is what makes it easier to do it there than an in-depth P2P.

**Tim** - Ok, cool, so I'll add that and try to summarize this conversation here. The open issues. A couple of things that were just on the list of the testing in general, I think we haven't spent much time on. I know, Abdel, you mentioned like we we should maybe start thinking about like reference tests and whatnot. I'm not sure if that EIP is, like, stable enough for that yet or Yeah, but what are your thoughts on that.

**Abdel** - I think the, for example, the basic computation is stable enough to start some kind of reference test because otherwise each client team will implement. Yeah, we will not leverage the work. And that would be good to have this kind of test to ensure that. And it will also help other teams when they will want to implement as a spec, let's say, when turbogeth and open ethereum to implement that. That will help them also.

**Tim** - Yeah, I think we can we can probably start slowly writing, I mean, some and yeah, like you mentioned, I think on the parts that are finalized. And then, yes, so we kind of discussed this already with the community testing, basically the Jason RPC Abdul, you said in the chat, I think that right now the block explorers using you can get transaction by hash. So that already supports 1559.

**Abdul** - No.

**Tim** - So how so? So I guess I don't understand how does the block explorer get the transaction information

**Abdul** - currently as looking only display is legacy. So for example, you have zero gas price for you; we need to update this end point to to miner bribe and probably even the base fee and that will be..

**Tim** - So the base fee is in the block header, right?

**Abdul** - Yes, but we have the block hash as the responsive end point so we can query to return to retrieve the block header.

**Tim** - And I think there what would probably be best is to just come up with a spec that both we vulcanize and nethermind agree on before we implement it, because again, that came up like I know with a lot of like the tracing APIs and whatnot. Clients have very different behaviors. And and that's part of the 1559 conversations that came up like it would be great if the behavior here was the same. So I think it might make sense to just see if no one has, like, superstrong divergent opinions, we should just come up with a spec.

**Abdel** - And currently for legacy transactions, we have the same output. So, yeah, we can. It was the same for the two new parameters just aligned on the names and we can just take the names from the stake.

**Micah** - So just the idea is just get transaction by hash will still work as normal. It's just it will also include 1559 transactions and they will have a couple of different fields.

**Abdel** - Exactly

**Tim** - Yeah, I guess, yeah, let's just ask our clients before we commit to that, but that seems reasonable to me.

**Micah** - And would that also eth block with the true flag for full blocks. The one that returns all transactions, I think it's eth get block by hash? [yes], I believe it's only two that return transactions, right?.

**Abdel** - Yes, I believe

**Micah** - Do we have plans at the moment to introduce or support 1559 transactions for eth sym transaction?

**Abdul** - So this is what I talked about earlier, so my my opinion on that if this is only for testnet then I would suggest that we implement a common service for that and we just deploy it in the same infrastructure as the testnet so that a client implementer, not client, but providers and people can start playing with that without waiting for meta mask to ads in your field and for. Yeah, I guess if you want to use that on mainnet, you will have to implement a new endpoint to submit your transaction unless you use an external signer. But yeah.

**Micah** - Would it make sense to have eth send transaction, just support either

**Abdul** - yeah, it'd be best to have it be optional.

5.2.3 | Video | [45:45](https://youtu.be/SHVfypwL5W8?t=2745)

    Tim to give someone the task of writing the specs for the new EIPs (transaction by hash, block by hash, and send transaction, block by number)

**Micah** - It would probably be good Tim to have someone write the specs for those three and it'll be three new EIPs.

**Tim** - Oh, so the change. Yeah, the changes to the jason RPC have to be separate EIPs.

**Micah** - Yeah, well they should be. you don't have to I guess of course. Ideally yes there would be there'd be an EIP for each of them that justifies the changes that are being made to the adjacent RPC and then from their clients can implement it and while its providers can implement etc.

**Abdel** - I thought they were out of scope, oh they're not core EIPs

**Micah** - They'd be interface EIPs

**Tim** - Ok, so and so we basically need one EIP per Jason RPC call.

**Micah** - Yeah, I believe there's three of them that we need to get transaction by hash. Get block by hash and some transaction. There might maybe get block by number as well.

**Abdel** - Yeah, because you want to add to the base EIP well. Yeah, get block by hash and get block by number as well, because you you need to add the base fee header for 1559 blocks.

**Tim** - how about eth and roth transactions? Does that have to change as well?

**Micah** - No, I don't have to because you're not just sending a byte array. It's already signed. OK, so ignore it.

**Tim** - So there's four of them and we need an EIP for each of those.

**Micah** - Yeah. People that in the past have done one monolithic one as an editor I recommend separate. They go through smoother.

5.2.4 | Video | [48:02](https://youtu.be/SHVfypwL5W8?t=2882)

    Abdel to write the EIPs

**Tim** - Ok, so unless somebody on the call right now wants to commit to it, I can follow up on that. I guess, yeah, I'm just a bit cautious because Abdel is a person and he is here to throw it on him

**Abdel** - I can some, that would be an occasion to start my first EIP.

**Tim** - I mean, sure. If you want to do it. So we'll have you write those EIPs.

**Abdel** - OK, nice.

**Tim** - Ok, so I think this covers Jason RPC, I see a public test net we already kind of I think is dependent on having this Jason RPC a bit more fleshed out. And the the other bit, I guess, in terms of testing that this I'm curious right now, we have the POA network. It seems like there's some small changes that make to the spec before everybody's kind of all syncing and happy. There is that we're to discuss the proof of work network now or do we still need like a couple of weeks before that because of the changes and of I don't get is still having the consensus issue on on the POA which.

**Micah** - Is nethermind already done.

**Tim** - Yeah, I think nethermind is syncing it may be like with some recent changes to the EIP, there's some small tweaks to do, but I suspect like in the next week. Yes. And that nethermind at least should be should be on the same network and up and running. I don't know if nethermind supports mining.

**Abdul** - Not yet at all. Or 1559 mining. You know, not 1559.

**Tim** - OK, so I think that's something we probably want at least like are having more than one client support mining before we launch a proof of work this net so we can actually try to find blocks in two different clients and make sure that they all come out the same and can work.

**Abdul** - Yeah. And in parallel, maybe we can start because we were thinking also about launching a single client testnet so that could be a single client proof of work testnet, and that would be the candidate to add other client's next, for example, the one to validate the economic Madinah.

**Tim** - And do you think we could do that with Besu already? Is there anything we need to change the Besu to do that?

**Abdul** - No, that should be fine. We can do that.

5.2.6 | Video | [50:22](https://youtu.be/SHVfypwL5W8?t=3022)

    Setup a single client proof of work testnet the follow with more clients

**Tim** - Ok, so maybe it makes sense to just start off a small Besu proof of work testnet to make sure at least everything works, that we can produce blocks and we can run your transaction generation script on it. And in the meantime, we'll see over the next couple of weeks how other clients gets ready and what the extent of their their mining support is. Cool, and then, yeah, just worth mentioning, I guess nethermind was using 1559 as part as I believe, like a private network or a network they're working on with one of their clients. So I think they might have some data to share on that in the next few weeks or months. And then Falcone and Cee both have 50. 1559 falco and devs have joined our slack or discord. Sorry. So if people have questions for them about how the network has gone, they're there and they can they can answer those. And I guess, yeah, in terms of R&D, the biggest thing that also came out in the survey with the community is kind of the lack of a proper not like even economic analysis of the EIP, but kind of just like a proper description of the mechanism that people, because a lot of people's concerns when they were opposed to the EIP was there's not even something to to critique. Right. There's just like this EIP, which specifies the behavior, but it doesn't kind of express the intuition behind it and whatnot. I'm not sure. Who could help with that, but to me, that feels like something that would be valuable, having a sort of I'm not I don't have a background in economics, so I don't know how this stuff is usually done that sort of like econ spec version of the EIP that kind of explains why this will actually be better. I know that Tim Rothgarden is working on a comparison of fifty to fifty nine versus our current model, so I'm not sure how much of it will be covered by that, but I don't know if anyone here has thoughts about how that can be done or your ways. Just those concerns about not having something that specifies the economic properties of the mechanisms that can be shared broadly.

**Baranbe** - I mean, I can say that just like the paper introduces 15, 59 has some motivation and some modelling, and I think it's been a bit overlooked by people who say there'll be no economic analysis. That's where it comes from first. And the EIP was written, which. Arguably has less, let's say, economic or at least macroeconomic motivation for and inventing rather than I think is, yeah, his anger is really much to say. Well, what do we bring, like, by having EIP Fifty nine. How does it change? Why is it better than the current model that we have and how do we even quantify what better means. Right. So yeah, I do expect that his report will be very enlightening in terms of framing it. But as I said before, the discourse, I don't expect it will be like, yes, we should do it or no, we should do more. Like what is even the correct way to think about this? One of the metrics we care about, what do we mean when we say to us in these sorts of things? Yeah.

**Tim** - Yeah, and I think that's good, actually, I don't think people are looking for like a justification as much as a description and and and I think it's probably easiest to describe by contrasting with what we have today. Do you have a link to the paper if you can send it to the Chatel added to that list there? Cool, and then the last bit, I guess, Barnabei, I can link some of your notebooks here, but in terms of simulations you mentioned, you obviously kind of all the stuff you're working on right now. Is there anything you still think, like, is missing after that? Is there like other big areas you'd want us to have simulations on that you think we haven't we haven't addressed yet or have had the bandwidth to start working on.

**Baranbe** - Right. So, I mean, there's a few things I discussed at the very beginning of the call, what I'm working on. So one big thing that I left out, but it's in my design is this idea of miner collusion. It's something that we do plan to simulate or at least try to get a broader understanding of what the behavior is. The reason I'm not focusing on this at the moment is because I do think the analysis by team will be at least a useful starting point. you know, I mean, it's it's kind of trivial to define something where it fails or succeeds automatically, but I think it's not going to bring that to the discussion. So. Yeah. And the fallout from that. Yeah. I think I should probably help you feel that because you think that's the thing that I can think is something OK.

**Tim** - And I'll add I'll add all the stuff you mentioned at the beginning of the call as well. So we will have at least some some meat there. And then the last bit was the community outreach just is still out of date. We published a report yesterday. One of the big things that we mentioned in the report is there was a very small number of exchanges and wallets that started. So I think if we do more outreach, I'd personally like to focus on those two groups. Yeah. So to just get more wallets, perspectives, I feel like exchanges are probably less affected by this and they tend to be pretty reluctant to share data publicly. So I'm not sure how realistic that is. But I think on the wallet side, we can definitely reach out to a few more folks and get their perspective on it. So we'll keep on doing that. And the cat hearders will probably have an updated version of the report. I don't want to give a date, but like in a few weeks to a month or something. Yeah, once we once to talk to a bit more people on that end. And that's all I had on the agenda, I don't know, is there anything else people feel we should discuss? Ok, well, in that case, yes, thanks a lot, everybody. This is really good. We'll have full notes for the report and for the meeting and I'll share a summary on Twitter in the next hour or so. Thank you, guy. Thanks, everybody.

### Attendees

- Tim Beiko
- Abdulhamid Bakhta
- Baranbe Monnot
- Micah Zoltu

### Next Meeting

TBD
