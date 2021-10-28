# All Core Devs Meeting 101 Notes
### Meeting Date/Time: Friday, November 27 2020, 14:00 UTC
### Meeting Duration: 1:30 hrs
### [GitHub Agenda](https://github.com/ethereum/pm/issues/224)
### [Audio/Video of the meeting](https://youtu.be/UGyqRoLwq1o)
### Moderator: Hudson Jameson
### Notes: William Schwab

# Summary 

## EIP Status
EIP | Status
--|--

- 2930: | included in Berlin
- 2718: | included in Berlin
- 2972: | not included in Berlin
- 2681: | Last Call

## Decisions Made

Decision Item | Description
--|--

- **101.1**: the decision is to put EIPs 2929, 2930, and 2718 in Berlin, and not EIP 2972 nor SSZ
- **101.2**: EIP-2681 to Last Call


## Actions Required

Action Item | Description
--|--

- **101.1**: Micah should touch EIPs that need to be changed, and make a PR to the Eth1 specs repo to update the commit hash for whatever needs to be put in for YOLOv3
- **101.2**: Micah and Martin to discuss RLP format for 2930 


---

# Agenda

<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 bullets:1 updateOnSave:1 -->
- [1. YOLOv3 & Berlin client updates](#1-yolov3-berlin-client-updates)
    - [1a. Outcome of EIP-2718, EIP-2972, and EIP-2976 break out discussion](#1a-outcome-of-rip-2718-eip-2972-and-eip-2976-break-out-discussion)
    - [1b. SSZ/wrapping legacy transactions](#1b-ssz-wrapping-legacy-transactions)
    - [1c. eth/6x support](#1c-eth-6x-legacy-support)
    - [1d. Final go/no-go for Berlin EIPs](#1d-final-go-no-go-for-berlin-eips)
- [2. Other EIPs](#2-other-eips)
    - [2a. EIP-2681](#2a-eip-2681)
- [3. Closing Remarks](#3-closing-remarks)

# 1. Yolov3 & Berlin client updates
Video | [4:12](https://youtu.be/UGyqRoLwq1o?t=252)
-|-


# 1a. Outcome of EIP-2718, EIP-2972, and EIP-2976 break out discussion
Video | [4:12](https://youtu.be/UGyqRoLwq1o?t=252)
-|-

**Hudson Jameson**: **Micah Zoltu** has written up comments which you can find in the comments to the agenda (_note taker's note_: on the GitHub issues page linked above). There's been breakout discussion and discussion on the various Discord channels, and he'll give us a summary of the outcomes. And we'll see if we can get a final go or no-go for Berlin.

**Micah Zoltu**: (_shares screen with SSZ tx doc linked in agenda_) This is a writeup by Piper, it basically goes over a little bit of why SSZ is nice and how it potentially integrates with typed transactions. The main thing I want to talk about with SSZ is to get everyone understanding each other and maybe on the same page of why there is value in switching to SSZ over RLP. The core of it comes down to two things. One, as of Eth2 (the merge), blocks will be in SSZ, and I believe that the Eth2 team is 100% on board with this, and the block hash will change to the SSZ merkle root for that SSZ encoded block. This gives us the intersting property that using a single proof and the latest block hash you can prove the contents of any ancestor of that block all the way back to where SSZ blocks are introduced, so as of the merge every block in history you'll be able to prove with a single block and the latest block hash. This is obviously very powerful. For example there is an EIP of saving all block hashes for proofs on blocks more than 256 blocks old, here we'd get that for free. On top of that you don't even need to transmit the block header like we do now. Now if you want to validate a block on chain you need to have the block header and parent hash or whatever. With SSZ we can prove individual pieces of data with just a proof, and no need to transmit the header.

What's more is that you can do this recursively down into transactions and receipts as well, you could do something like prove that there was a log with a certain index 10 million blocks ago, and with a single proof and the latest block hash you could get that. That is a very high-level view of why SSZ is valuable to us. There are other tangential benefits, if you have large data structures you want to split across multiple packets you can prove that a half payload is half and not DOS. That's minor, the big one is recursive proofs from the hash of the latest block.

In order to get that kind of recursive proof it is very valuable if the receipts routes and the transaction route is also SSZ instead of traditional NPT. If we have an SSZ hash inside the block, then once the merge happens we can do things like I described.

**Alex Vlasov** (_via chat_): Proof sizes are linear in history, so it's not too practical.

**Micah Zoltu**: No one has mentioned this in the last two weeks I've been talking about this. Let's move past it for now, we can research this more later.

From the people I've talked to I think most everybody is generally on board for most of our stuf to be SSZ: transactions, receipts, and the block itself. That brings us over to typed transactions. (_Micah switches screen share to the HackMD about typed transactions_) The document is a discussion of problems we've run into. This one is the interesting one. It comes down to wanting EIP-2929 in Berlin. It's important because it's the gas cost increase for state access opcodes which addresses some DOS vectors against Ethereum, and we want to launch Berlin., Those are two things we really want to do. We could do 2929 by itself, but the discussed disadvantage of not also doing 2930 is that there may be contracts that are unable to execute within the gas limit, or contracts that break because of the gas cost increase. Because of that we want 2930. The disadvantage of only doing 2929 and 2930 without 2718, then we end up with a bunch of technical debt because we introduce a new transaciton type, right now we have pre-155 and post-155 and they're kind of the same shape, but you switch on the v-value to determine what type it is. We'd now introduce a third without any type mechnism or versioning system. which means we'll have ot both switch on v for 155 and we'll switch on the number of items in the RLP-encoded array for that. We don't want to introduce all of that technical debt if we know we're going to introduce 2718 or something like it in the near future. That leads us to 2718. If we do that, transaction discrimination is dirty. Not as bad as without, but still dirty because you're switching on the first byte, and if it's different then you switch on v. Not too bad, not amazing, but not terrible. It also introduces technical debt, if we just introduce 2718 but not SSZ then we're basically saying that we agree that we're going to do SSZ down the road, and we're going to have change this new piece of code, which means a transition process for 2930 transactions, deprecating them dual-hashing, and stuff like that.

That leads to the next option, which is all three and SSZ. The big downside would be all the clients needing to include SSZ before Berlin. That's the big contention. Also, we're introducing SSZ, but only halfway. We aren't wrapping legacy transactions in SSZ, so we still have legacy RLP, and have this dual system, it's not terrible, but when you want to do tihngs like SSZ unions, which would be really convenient for swtiching and cleaning up the code for transaction type discrimination it gets awkward. We could technically do it because we could flag the three RLP transactions by their first byte, but we can't do SSZ at an earlier phase in the decoding process.

The next option is all of this and also 2972, which is wrapped legacy transactions as SSZ. We'd eat all the costs right now, and move over to SSZ transactions with BErlin. The nice thing is no technical debt, we even get rid of some like EIP-155. We'd be ready for the merge. Take on a lot of work right now so we don't introduce technical debt, and pay some down. Big disadvantage is that it's a lot of work, and another is thattransaction hash for legacy transactions would change. This isn't necessarly a showstopper by itself, but it can create some problems around the fork block. Someone can submit a transaction around the fork block, and the client says here's your transaction hash, but then it sits in the pending queue until after the fork block, and then gets mined, and that tx hash never got mined. There are some things we could do, storing both hashes in memory so we can send for whatever is asked for. I want to emphasize that this is a lot of work.

**lightclient** (_via chat_): We wouldn't be able to get rid of 155 since the transaction signature depends on it, correct?

**Micah Zoltu**: Yes and no. Yes we still have the signature, and will have to turn on that, but we can at least split out the two transaction types. So we can have in decoding and processing, everything except for signature validation and signing, we can actually distinguish them as two types. That's the advanage of 2972. We're not getting rid of all of the debt of 155, but I think we're getting rid of about half of it.

So the discussion is which one of these we're going to go with, or find something in the middle. My personal preference is that I'm an extremist, so I like either the first or the last. I don't like technical debt. I like something that doesn't increase technical debt, and/or pays it down. The first option doesn't introduce any since we only do 2929 and throw everything else out, the last pays some debt down and gets us closer to our final goal and so we don't add new technical debt that we'll have to pay down.

**Peter Szilagyi**: Couldn't clinets internally shuffle data structures via hash? Every time Geth does somthing with a transaction it does it via hash, every times it does something with a block it does it via hash. I cannot just simply start using a different hash. From a client implementation perspective, if we're saying the fork block will come and we need to swap out hashes, this means at some point in time when I start up Geth it needs to say okay I'm not using RLP hashes, I'm using SSZ, that would be fine, but then things start getting funky with the networking protocols, because all the Eth protocol jiust asks for hashes, via RLP hashes. It's definately doable, we could definately roll out a new protocol which speaks SSZ, and whether the hash is RLP or SSZ, you could maintain both for some period of time, and then somehow handle both, but it has quite big implications.

**Piper Merriam**: I look at this as a separate piece of technical debt, one that will problematic in any transition period. ReGenesis is an option on the table for dropping some of that historical technical debt, so if we do this and do ReGenesis afterwards we essentially get a chance to forget about some of that technical debt.

**Peter**: One objection of the whole ReGenesis thing is that in theory, yes, you can write a client which will only speak the protocol after the ReGenesis event adn won't handle anything else, but from the perspective of a Geth maintainer that's not something we can afford, we can't say from Geth version 2 you can't access Ethereum 1 anymore. It's problematic, and I don't think that approach helps us much. I don't have a problem with SSZ or transitioning into it, the point I want to make is that I don't think it's worth pushing it out to Berlin because it will delay it forever, and if we want SSZ we shold have something that focuses on SSZ, the next hard fork after Berlin, and then we can say that this fork will contain a new Eth protocol, or whatver. It seems that this is a whole new can of worms, and a very brave move to try to cram it in. 

**Piper** asks what other client devs think of this.

**Tim Beiko**: In the past we've discussed these closed hard forks where we focus on stuff that's already committed and whatnot, and I think the challenge is that priorities change so much thatin six months that it becomes an untenable promise. I don't disagree with anything Peter says, I also think SSZ is too big for Berlin, it can be priority number one after Berlin is out, but if it takes six months, other things might become high priority as well, we might not be able to do just an SSZ fork, but we may be able to do it with other stuff, or if it goes very fast to do by itself. I'm skeptical that we can freeze priority for six months given how many things are being worked on.

**Peter**: I don't think we're going to ship it earlier than the next half year.

**Tim**: I agree, and I think we should probably do SSZ after Berlin...

**James Hancock**: and 1559, and/or maybe account abstraction, and a binary tree...

**Tim**: it feels like there will also be something else as well. Someone in the chat (_notetaker's note_: Danno Ferrin) mentioned the Ice Age is coming in the next 6-9 months, we'll need to push it off, I'm just saying it's unreasonable to think SSZ will be the sole focus.

**Hudson** asks if there is anyone from any other client team.

**Dragan Rakita**: I agree with Peter. Even including SSZ partially is a big step. I would really like that if we would switch, we'd switch completely, partially switching receipts and leaving blocks could be problematic.

**Martin Holst Swende**: Peter, would your preference be Option 30? (_notetaker's note_: this is EIPs 2929, 2930, 2718, but no SSZ in Micah's doc)

**Peter**: My preference is everything and the kitchen sink but no SSZ.

**James Hancock**: I think that would be Option 50 minus SSZ.

**Peter**: I don't all the details of all the options, so I don't want to say 50 minus SSZ. I'd try to solve as many problems as possible without SSZ.

**James**: At the last All Core Devs we were at 2929, 2930, and 2718, and we discussed 2972 which kicked off this discussion. As far as Berlin, we are up to those three options, so the last one is can we do 2972 without SSZ and do everything else without SSZ.

**Micha**: We can add 2972 without SSZ. The caveat is that we're adding a wrapped transaction around legacy transactions that we're going to have to wrap later when we add SSZ. So we're introducing a new transaction type that we know we'll have to delete. That is an option, I didn't include it here because it seems weied to me to introduce a wrapped transaction when we're going to have to re-wrap it later.

**James**: Can we do 2718 without 2972? I thought we needed to wrap the transactions to be able to do it.

**Micah**: We can do 2718 without 2972 and without SSZ, the caveat is that transaction discrimination is awkward and uncomfortable. We also have technical debt because we introduce 2930 without SSZ when we know we're going to switch to it. It's basically Option 30.

**Peter**: Micah said one of the problems is needing to wrap legacy transactions a separate time, my suggestion would be to simply deprecate legacy transactions. For example, in the Berlin hard fork we could launch it, but we could say that legacy transactions will be dropped in the next hard fork, and you have one hard fork worth of time to transition from this wrapped legacy transaction thing into the proper way to encode transactions, and the next hard fork can simply drop it without a double wrap. 

The other thing is that the reason why I think SSZ will take a long time is because every client needs to roll it out at the same time. It's super dangerous, everything will go wrong, so the moment you add SSZ to the consensus it's a dangerous path. A more gradual transition could be to start upgrading, for example, the Eth protocol, you could launch eth60 which will run with SSZ. Geth could implement, then Trinity, and whatever can implement, and we don't have to roll it out at the same time. If we roll out this networking thing that yes this implicitly means that you need the RLP and SSZ hashes, the point could be that this could be going towards phasing out RLP and integrating SSZ without this hard flip that now everyone must speak perfect SSZ.

**Artem Vorotnikov**: Do we have a plan for the RLPx-transport protocol itself? It looks like if we pull a transition to SSZ, we'll still have RLPx-transport, which holds an RLP library, do we switch devp2p?

**Piper**: devp2p calls RLPx, but doesn't actually have anything that specifically makes things dependent on RLP.

**Artem**: Messages are RLP encoded, though?

**Piper**: I think Peter means using SSZ over devp2p for message encoding.

**Peter**: Yes. For example, what I would do for the first time is just switch over the Eth subprotocol so that the messages are SSZ. I haven't though about it too much, we could also bump the devp2p version number, and make it SSZx instead of RLPx. Geth can speak devp2p v4 and v5, we can launch a sixth one will RLP vs SSZ will be the big difference. And any client that has not yet implemented SSZ can do one thing, and everyone else another. So yes, there are a lot of challenges, but networking can be rolled out with errors, because you can make a fallback if someone disconnects with errors. If something feels weird, you just revert back to the current networking version and everything works fine. It allows you to make bugs and experiment without breaking the network.

**Rai Sur**: Regarding Micah's point about the transaction type discrimination being dirty: It is dirty, but only in one place, and it's quite simple for now. So there's a tradeoff here: it's not terribly dirty, it keeps Berlin moving, and we can get 2929 in without Option 10 (_notetaker's note_: the name of the option in Micah's doc for doing 2929 and nothing else) where we just do 2929, we at least pay down some debt, or at least prevent future debt. From the perspective of a client dev, Option 30 looks good.

**James**: Is that with wrapped transactions?

**Rai**: No, Option 30 without wrapping.

**Micah**: Is that true for other clients as well, that you feel that the discrimination is constrained?

**Hudson**: They might need to look at it.

**Martin**: I don't mind a little dirtiness somewhere if it makes us able to ship Berlin a lot faster and get these things in.

**Hudson**: Option 30 is everything other than 2972 and SSZ? (_confirms_) There are two cons: technical debt by needing to convert 2718 transaction to SSZ, more transaciton types need to go through transition later or be deprecated. Peter talked about deprecating legacy transactions at that time, and working towards SSZ iteratively - that's how I'm reflecting the conversation.

**Martin**: If it's Option 30, I think the current implementation of Go Ethereum is pretty close to done.

**Hudson**: Is there anyone who really wants SSZ in Berlin? (_no one speaks up_)

**Peter**: If we strongly feel SSZ in the future, fine, but I strongly feel we should introduce SSZ in non-consensus places first and then transition.

**Piper**: I like the idea of doing it in the networkig layer first, it's a way of doing it that is safer and lets the clients do it in a nice clean way.

**Micah**: Peter mentioned deprecating legacy transactions when launching Berlin. I got the impression that deprecation of a transaction type is about a two-year process.

**Peter**: We tell them that the signatures won't work once we ship SSZ, which will probably be in two years. (_Peter indicates this was a bit of a joke_) My point is we're not going to ship SSZ in a month. I hope it's not two years, half a year at best.

**Piper**: Hudson, do we have contact with hardware wallet manufacturers? Those seem like the hardest place to deal with deprecation. We don't have to talk about this right now, and can focus on other things more relevant to Berlin.

**Peter**: No, this is a super relevant point. We won't be able to get hardware wallet manufacturers to upgrade. Some might support, but it's a super-bad move to break someone's hardware wallet or upgrade firmware because we just... That's a super strong point against dropping legacy transactions.

**Piper**: Something that has been thought of is maintaining support for legacy transactions through a precompile, they may not be submissible on the protocol layer, but looking into ways for them still to be executable through submitting them to a precompile.

**Hudson**: But we can discuss this after Berlin.

**Micah**: The reason I want to bring it up now is because this technical debt is going to go away in a couple of years, maybe.

**lightclient**: What if we did something where we only use SSZ for the signature of the transaction, so when we determine what hash we're going to sign we use SSZ to calculate. That goes against not introducing SSZ at the protocol layer, but in my mind it's the one fixed constant, everything else can be shuffled around at the protocol to meet whatever we desire, we can modify the RPC endpoints to give whatever data people expect, but if we don't support SSZ in the transaction signature we will have to support RLP for end users. (_notetaker's note_: someone, maybe Martin, said something I couldn't make out.) We can't cahnge it for the legacy transactions, but as we ad new transactions if we use SSZ for their signing hashes it owuld be possible in the future to convert to 100% SSZ. (_this is reiterated for Micah, who dropped off due to Zoom audio issues_)

**Alex Vlasov**: Hardware wallets don't sign the hash, but the transaction is ?, so they expect the input of the transaction in the cold RLP-encoded, which they can decode some data, Ledger does a similar thing, and they don't just sign a hash, they recalculate the hash.

**Martin**: What he's saying is that would only work for the legacy transactions, for the new ones it would be SSZ, your hardware wallet wouldn't be able to sign something which ???. It's an interesting idea.

**Micah**: The con is that we're back into introducing SSZ then. We only have to introduce the serialization part, we don't have to introduce the SSZ merkelization part so the risk of consensus failure is lower, but it is still an introduction of new code, I don't know how a client would feel about a little bit of SSZ.

**lightclient**: This might be the SSZ format itself, but what if we have a transaction signing format, and we'll use it forever in the future, just an ephemeral format that we serialize and keccak. If we just say this is what it will be forever, we won't have to worry about another serialization scheme with all these great features, we've already said signatures will always be this.

**Micah**: We could use RLP for that. We could have SSZ transactions over the wires in blocks whatever, but when you get that SSZ transaction you decode it into some in-memory data structure and RLP encode in a very specific way and keccak that to get the hash which you then sign. It's possible, and we could do that without SSZ.

**Hudson**: Bringing this back to what we're going to do for Berlin. Peter has said everything other than SSZ. I want to make sure that Option 50 without SSZ is an option. Is that possible, Micah?

**Micah**: SSZ is not a hard requirement for anything, the only question is how much technical debt we want to incur by not doing it.

**Hudson**: Can anyone give pros and cons between Option 30 and Option 50 without SSZ? Does that change the picture at all?

**Tim** and **James** clarify that the only difference between the two is EIP-2972 (wrapped legacy transactions)

**Hudson** asks for opinions and time estimates to implement EIP-2972.

**Greg Colvin**: This is a meta comment, but we've had a number of EIPs ready to go for Berlin for along time, and more keep arriving. Is there a reason why any of this needs to go out now? Why can't we release what's been ready for many months? (**Peter** asks what's been ready for many months.) James can correct me, but certainly 2315, which I care about, and there were other things on the list at that time.

**James**: That one is independent and has been ready, and the gas change one. The rest of them are kinda together. As far as what's been talked about, everything has been talked about except 2972 wrapped legacy transactions, and will have this hopefully last conversation today to get the context if it needs to be in given SSZ will be something we'll tackle on the network layer first.

**Greg**: Is there an option that says all of this can wait? Let's get Berlin out and pick this up asap...

**Martin**: My take is that the most important thing to ship isn't the subroutines, but rather the denial-of-service protections in 2929.

**Greg**: I agree that 2315 is not the most important, but there's just been what seems like a number that have been ready for a long time. We're starting to look like Oracle on a three-year cycle.

**James**: The other part is typed transactions are important which are important given the context of what's coming next year.

**Tim**: and also if we don't want to break everything. We could ship 2315 and 2929 alone, but we might break smart contracts, and people would be mad that their stuff is broken, which means 2930, and then introducing that requires a new type of transaction... I understand 2315 has been ready for nearly a year, and I agree...

**Greg**: It breaks nothing.

**Micah**: Has any analysis been done \[on that]?

**Martin**: You kind of brought this on a tangent, I was hoping we could finish the discussion.

**James**: With the intent of discussing being meta-stuck, we have become stuck about being meta-stuck.

**Hudson**: Greg, to use the famous words from an earlier incident, we can discuss this offline. I think we're getting close to picking these. We're not doing SSZ, and the only thing seems to be seeing if anyone wants to advocate for putting 2972 in Berlin. (**James** agrees.) I think we should go with Option 30 unless someone advocates for it.

**James**: I don't totally understand what's more messy between doing it without 2972 or without with the context of deprecating old transactions in the next like nine months.

**Hudson**: We're starting to say we kinda can't do that anymore.

**lightclient**: My understanding was that the major push for 2972 was from the Geth team because of the way transactions were handled in their client especially in terms of creating the merkle-patricia root of the transaction has, but I'm not sure if that's still the case.

**Peter**: I don't think so. You actually wrote the PR which kind of works. Code-wise we have to maintain a transaction type anyway, whether a Go type, a type flag, or whatever, and then when you encode and calculate the hash it's fairly trivial to say that type 0 transactions are encoded with some special rule, and others with some other special rules. It doesn't really matter from an implementation perspective, it was more out of code cleanliness, not to have too many weird ? in the code. At this point I would say whatever is simpler and easiest is better. If 2972 introduces a lot of code complexity around legacy transactions, we might as well adjust to need legacy transactions as they are now and use special cases. This is a prehistoric thing in Ethereum, and we know it's a bit weird, but it's what Ethereum 1 was.

**Micah**: Looking at Micah's gas writeup, I think I'm misreading this, but it sounds like we don't really need 2930?

**Martin**: No, you're not misreading it. What you're reading is that on this small segment of blocks analyzed on Goerli there were no such blocks.

**Micah**: So this is more a fear of the unknown, we don't know if there exist things that will break, but it is possible that there are.

**Martin**: I said I'd rerun for a larger range of blocks on mainnet, but haven't had the time.

**Micah**: Dropping 2930 is by far the fastest and easiest way to get Berlin out. If we can analyze quickly if we need 2930, that may be a simple solution. But unless someone has tools ready to go, I'm guessing that's a big chunk of work.

**Martin**: Geth has tools built in. The thing is, okay, we analyze 500 blocks and find no such transactions, are we now okay with that? How sure do we need to be?

**Micah**: Can we run the tooling over the whole chain? (**Martin** indicates that this would be difficult at best.)

**Rai**: How long would it take to run it over the last million blocks?

**Martin**: I'm not sure.

**Piper**: Could we help run it over the last million blocks?

**Martin**: It's not just about running it over the blocks. Either there is some manual analysis that needs to be run afterwards, or the tooling needs to be refined to figure everything out on its own. If we run on a million blocks, I obviously want to minimize the manual.

**Piper**: It would be very unfortunate if we introduce a new transaction type moving forward that we have to deal with if it's not necessary.

**Rai**: A lot of the issues that are coming up here are because we're assuming we're definately going to include this new transaction type, and it would be great for the health of the network if we could get that DOS protection out.

**Piper**: Could we bounty this and say we will pay someone x-thousand dollars if you can show us a historical transactoin that would fail under these new rules, and commit to doing some analysis ourselves, and if no one can find it, then we don't do it. I get that the extremely bulletproof thing to do is to have this mechanism in place, but if we don't need it, it seems really unfortunate to implement it and deal with the debt it introduces.

**Tim**: I'm looking at the Magicians thread, and it seems that the CTO of Scale Labs is very unhappy with 2929 because of the gas cost changes. He didn't provide a specific example, but it might be somebody that can help. (_some conversation ensues_)

**Alex Vlasov**: As someone who is outside this a bit, and from a practical perspective, if storage is restructured and maybe binary merkelization is implemented then there is no need to increase the price because latency of accessing storage is going to be much lower than it is right now, as was demonstarted by the Turbo-Geth team. Maybe instead of this and three months of discussion it would be better to agree on decisions that it's oging to be a breaking change, and fix it from the ground up, and would make everybody happy except for the people who have to write it, but they would still have to write it at some point anyway.

**Hudson**: For EIP-2930, is it something we could leave out, and if we find out that there is a transaction that is broken we could implement it then, or is that significantly worse?

**Micah**: I believe we can do that, but we would still have to solve all those problems then instead of now.

**James**: And if we didn't have 2930, would we also remove typed transactions?

**Micah**: From Berlin, yes. If 2930 doesn't go in, we should cut all the stuff from my list. All of this would fall out with 2930. We'd implement 2929 and be done. We could release Berlin tomorrow.

**James**: Let's say a fork has 1559, typed transactions. Is there a good reason to take this work now and make they work before trying to do more things at once?

**Tim Beiko**: One thing that makes it easier is if typed transactions are already a thing on mainnet, then 1559 and the account abstraction folks can take it for granted that we can use those things, otherwise it's a bit of a chicken and egg, we don't want to change the 1559 spec to rely on 2718 because we don't want to add an extra dependency if it's not going to be on mainnet, so you're kind of circling... It's not the end of the world, but it makes it easier if it's already there on mainnet, and already used by other projects.

**Rai Sur**: I think that would be an issue if 2718 would be more controversial, but I think what's more controversial is just the timing of it. I think that it's safe for 1559 and other EIPs to rely on 2718 becuase we're pretty much all in favor of the idea of it. The problem is can we get Berlin out faster without...

**Piper Merriam**: Can we straw man that? If this was the beginning of the discussion of the next hard fork, and we were talking about putting something like proposal 50 \[the proposal with everything in it] is there anybody who would be speaking out against that and saying that they don't think it's a good use of our time? (_silence_) Silence here means that is maybe correct. (**Hudson** agrees.)

**Hudson**: I have an idea: we do analysis of however many million blocks, and there's a company that helped us with analysis the last time we thought we might break something. Martin, do you remember who it was?

**Martin**: I reached out to both of them a couple of months ago. Actually, the stuff built into Geth is better. It's going to be a lot of work, I can try to sort it out. I still think there's an additional benefit to 2930 that it provides an access list which can be used later on when we start witnesses.

**Hudson**: Looking all of this up will take time...

**Alex Vlasov**: You can make a contract and a transaction which will fail analysis today, so someone who wants to stop this from being implemented... it's kind of pointless, we can't guarantee this, the non-existence of such a contract which will not break because it's easy to make. (**Martin** agrees.)

**Piper**: We can call the cutoff yesterday, if it didn't exist yesterday.

**Alex Vlasov**: But if a new DeFi protocol hits then, and is popular in the next month, and is popular before the fork...

**Piper**: That's fair.

**Hudson**: Especially since Martin mentioned that there are other benefits to 2930, maybe Option 30 \[everything other than 2972 and SSZ] is the best?

**Micah**: Core Devs and security auditors and everybody has been screaming for the last year not to make transactions dependent on gas costs, they will change. At this point if you are writing contracts that depend on gas costs, it is your fault. We have done everything that is in our power to stop people from doing it. I sit in chat rooms all day, and people say 'I'm going to do this gas chack', and I say 'don't do that, here are 17 articles from Core Devs, security auditors, stop it', we have to cut people off at some point, and I think that point was six months ago. So while I agree that we should care about old transactions, I don't think we should care about transactions that were yesterday. They should know better.

**Martin**: I think you're forgetting something. It's not just about checking explicit gas costs, it's about contracts that use the Solidity send, it winds up with only 2300 gas at the recipient, and they try to do a check in sload, and the contract that did the deposit was hardcoded to only do a send, because that was the old-school Solidity best practice.

**Micah**: That's fair. It gets a bit murky, like half of us have also been screaming at people not to rely on the gas ? to be enough to do anything. The other half have been saying oh yeah use the gas ?, it's safe. You're right that there's been mixed messages from us and the auditors about that. It's getting better, I've seen more auditors saying not to do this, but there is more disagreement about that, so I'll concede.

**James Hancock**: Peter, earlier in the conversation you mentioned that Geth was close to basically Option 30 (minus 2972)?

**Martin**: I think lightclient knows best, actually.

**lightclient**: Yes. Are other clients in a similar position?

**Dragan Rakita**: Yes, from Open Ethereum.

**Alex Vlasov**: In a similar direction, there was a question before about what was called to ungas, make gas non-observable, in the EVM at all, and as far as I know it didn't go anywhere. Maybe the opposite would be better, to make it serveable. Yes, maybe people can hardcode 2300 gas for some kind of operation if they can get the data for what this operation will cost in real time, maybe it will solve their problems. It was never introduced in this direction, only in the opposite way.

**Martin**: It wouldn't solve any of these problems.

**Alex Vlasov**: In complex interactoin they obviously will not try to estimate specifically how much gas they want to specify in a call, but at least for a simple one where you can go to the log, single sstore and a single log and maybe 100 for additional expenses, they can at least do better than now.

**Martin**: It won't solve any existing problems.

**Hudson**: Let's try to stay focused on the stuff for today. I think someone is writing up Option 35 right now.

**Piper**: What we're circling on right now is if we can get by dropping access lists and transactions, is that right?

**Hudson**: That's the latest thing we're stuck on, once we're past that, I think it's all downhill from there.

**Piper**: What would people need to feel comfortable dropping that? It sounds like we're not going to get bulletproof knowledge that it's not going to break anything if we ran it over the last two thousand blocks, would there still be people who would still not be comfortable rolling out the gas increases wihtout the access lists transaction type?

**Hudson**: I think a part of it is that 2930 also has stuff that's beneficial beyond patching the problem.

**Piper**: Are you referring to what Martin mentioned about witnesses earlier? (**Hudson** confirms) I'm not saying we should never do 2930, I'm just saying that it's unfortunate to 2930 without 2718, and 2718 gets problematic because of SSZ and things like that. If we're pretty sure we're going to do 2718 coming up, then we just do 2930 with 2718 coming up, because if we don't need it now, then all of the sudden Berlin gets really easy.

**Hudson**: I think we can do 2930 and 2718 for Berlin and it wouldn't take a super long time, is that right?

**James Hancock**: We're closest, developmentally, to having that already ready.

**Tim Beiko**: I think that's true for Besu as well.

**Piper**: I'm not going to argue against that. What I'm suggesting is that if we don't need to do access list transaction type at this stage, then we can do it in a better way when we do SSZ-based 2718. We don't have any concrete reasons why we need access lists.

**Martin**: There are some concrete \[reasons]. If you look at the old EIP 1884 security analysis, there are a lot of contracts that were found (_lists some_) that were hit by 1084, and these would be hit again, and also similar like them.

**Hudson**: It seems like things are stacking more in favor of putting in EIP-2930 because the analysis alone will take weeks if not a month, and only then we'd be able to make a decision, and there's a chance that decision will be to keep it in, and if we want to put it in eventually anyway, even though putting it in right now might not be the best format...

**James**: The maximally safe thing that we can ship in the shortest timeline includes 2930 and 2718, and then maybe 2972, but I haven't heard many people say that we need it anymore. (**Hudson** concurs)

**Hudson**: I think I like Option 30 \[2929, 2930, 2718] going forward, and if we can declare that today, and update whichever YOLO we want to put it in...

**James**: Before that, I want to hear from every client that there isn't anything in 2972 that they see that we need, just to exclude that explicitly.

**Rai Sur**: We don't think it should be a blocker, Option 30 is probably the best.

**Martin**: I would agree.

**Rai Sur**: Tomasz \[Nethermind] said in All Core Devs that he would be okay with anything. (_**Tomasz** later confirmed in the chat that he was fine with Option 30._)

**James Hancock**: And Open Ethereum, you're okay dropping 2972?

**Dragan Rakita** and **Adria Massanet**: Yes.

**Hudson**: So let's go with Option 30 then.

**James Hancock**: Cool.

**Decisions**:
- **101.1**: After over an hour of epic discussion, the decision is to put EIPs 2929, 2930, and 2718 in Berlin, and not EIP 2972 nor SSZ. Much rejoicing and merrymaking upon consensus.


# 1b. SSZ/wrapping legacy transactions
Video | []()
-|-

_contained in above converation_

# 1c. eth/6x support
Video | [1:19:00](https://youtu.be/UGyqRoLwq1o?t=4740)
-|-

_(notetaker's note: this was discussed after the following item)_

**Hudson**: There is a conversation here about Option A vs. Option B (_supplies link to Discord in chat_). That's Peter talking about two options for rolling out the new networking protocol. People thumbed-up the post \[to signal support], Artem went for A, Open Ethereum looked at B, and I think those may be the only clients that spoke up.

**Tim Beiko**: Besu said B as well.

**Hudson**: What about Nethermind?

**Micah**: Nethermind is listening, but not here.

**Hudson**: Are there updates from the Geth team?

**Martin**: No, we heard people wanted Option B, so we'll do Option B.

**Hudson**: Barring a show-stopper, I really don't want to do Option B (_notetaker's note_: from context, I believe he meant to say Option A here) which would need a lot more discussion and changes, if we could go with Option B that would be good. (**James Hancock** recommends reading out the options) Option B is we allow typed transactions in earlier Eth protocol versoins, but 1) Geth will implement 66 request id before Berlin, so after Berlin all Geth nodes on the network will be guaranteed to speak 66, and Geth will drop eth 63 support this year, eth 64 by spring 2021, and eth 65 by summer 2021. Any questions or considerations?

**James Hancock**: Nethermind has said Option B is better from their point of view.

**Hudson**: So we'll go with Option B then.

**Decisions**
- **101.2**: Option B for eth66 support

# 1d. Final go/no-go for Berlin EIPs
Video | [1:15:38](https://youtu.be/UGyqRoLwq1o?t=4538)
-|-

**Hudson**: What needs to change in the specs repo for us to know where we're at on these EIPs that we just decided on?

**James**: I'll go through and check right now.

**Micah**: I'll fix whatever needs to be fixed, 2930 I believe will need to be touched.

**James**: The EIP might, but the specification list is still 2565, 2315, 2929, 2930, and 2718.

**Tim Beiko**: Does that mean YOLOv3 will be the list for Berlin? If so, I tihnk we still have the BLS precompile for YOLOv3, we should probably remove that so that the YOLOv3 spec is just this whole bundle that we discussed for Berlin.

**James**: It's gone, we already removed it.

**Tim**: So what's in the spec now is YOLOv3, and that's what we'll make official for Berlin.

**Hudson**: and also whatever was in v1 and v2, right?

**Tim Beiko**: No, YOLOv3 is the right list.

**James Hancock**: v1 and v2 have the BLS precompiles, v3 doesn't, it's these 5 EIPs.

**Tim Beiko**: If we can get that split up before the next All Core Devs call, then we'll have some preliminary data.

**Hudson**: So in terms of things to do, Micah should touch EIPs that need to be changed, and make a PR to the Eth1 specs repo to update the commit hash for whatever needs to be put in for YOLOv3.

**Micah**: I can update the EIPs, but don't know how to do that other thing.

**Hudson**: In YOLOv3, the specs page (I'll post it in chat), we have commit hashes for ones that were updated fairly recently, to link to what version to implement. We might need that for 2930.

**Micah**: I'll work with you or James to implement that. I think for 2930 the thing that led to this conversation was what the RLP format for 2930 is, I think there is still value in having that conversation, nothing contentious, just what order the fields should be in. I think Martin had some thoughts on that? If you have some time later, next week, like early next week, and we can hash that out? (**Martin** agrees)

**Actions Required**:
- **101.1**: Micah should touch EIPs that need to be changed, and make a PR to the Eth1 specs repo to update the commit hash for whatever needs to be put in for YOLOv3
- **101.2**: Micah and Martin to discuss RLP format for 2930

_The following is a discussion that happened later in the call at [1:22:23](https://youtu.be/UGyqRoLwq1o?t=4943), and will be placed here due to its relevance to this item

**Hudson**: Is there anything with YOLOv3 that we need to talk about?

**lightclient**: I don't know if we want to discuss this further, but I didn't get a clear answer on if there is any desire to look at changing the transaction signature serialization scheme.

**Hudson**: Is this SSZ or the thing we're doing in 2930?

**lightclient**: 2930. The serialization format that we choose for the signature hash is something we cannot change in the future, so I was hoping we could decide on one format to use in perpituity so it isn't a conversation that has to happen again. If we want to move everything to SSZ we don't have to discuss like 2930 singature hashes were built with RLP should we deprecate them, etc.

**Hudson**: What's the default, RLP or something?

**lightclient**: It's RLP right now, and I'm not opposed to that. It seems like it would be nice to break aprt what we understand as the serialization for the protocol and the special format we build these transaction signature hashes with. It seems like SSZ is the most simple serialization format we could think of and we could say even in the future in 20 years if we diecide SSZ is no longer appropriate in the protocol, it is very simple to serialize transactions and sign them, and so we will continue supporting those for a long time.

**Hudson**: I'm getting the feeling we might just be burnt out for conversation on that today, unless anyone has any comments. Bringing it up in Core Devs chat and putting it on the agenda for next time, we should be able to discuss that more.

# 2. Other EIPs
Video | [1:24:48](https://youtu.be/UGyqRoLwq1o?t=5088)
-|-

# 2a. EIP-2681
Video | [1:24:48](https://youtu.be/UGyqRoLwq1o?t=5088)
-|-

**Hudson**: There are only 4 minutes left, we'll give a quick overview. Lightclient propses to limit account nonce to 2^64-1.

**lightclient**: This is an EIP Alex \[Beregszszi] wrote earlier this year, the idea is that building the witness format, there is some comlexity dealing with these arbitrary length integers, and as currently specified the account nonce could theoretically grow to very large numbers. This EIP is basically retroactively saying that we'll limit account nonces to 2^64 -1. Right now, I looked up the current highest account nonce in the state trie, and it's approximately 29 million, it's the Ethermine coinbase account that sends out the dispersements, that's a lot of gas spent. I don't know what the proper way of doing an EIP like this that is retroactive, but it's a very small change, I think a lot of clients have already implemented, I think Geth already implemented. (**Martin** confirms) I think this is how many clients have done this. Is there any opposition?

**Martin**: I think we could mark this \[as] final.

**Micah**: My only minor request, and not enough to stop this from going through, would be 2^52 or lower so JavaScript number doesn't have problems, since 2^52 I think is way more than we're ever going to need, it's like end of the universe numbers. Again, I odn't want to hold back the EIP, but that would be a minor preference.

**Martin**: Does it really matter since in practice it's never going to reach either?

**lightclient**: We could do this in another couple of years. If choose 2^64 today, we could potentially reduce it in the future.

**Micah**: I believe that as soon as we put this into SSZ, it does matter. Since SSZ is fixed width, you need to set the number of bytes. but 52 and 64 are the same number of bytes?

**Piper**: Off by a byte, but they're close.

**lightclient**: So you're saying this could potentially become an issue by SSZ.

**Martin**: I don't agree that it would be an issue because it doesn't say anything about changing it to be a fixed-width 64 length thing, it's just limited to between 0 and this number.

**lightclient**: I guess I'm not sure what that means in terms of SSZ. IS there a representation for something that's arbitrary length?

**Micah**: If we say this is 64 bytes and encode it in Eth2 somehow and it needs to be SSZ-encoded for whatever reason...

**Martin**: But we don't say it's 64 bytes. Eth doesn't say that the field is always represented as 64 bytes, just that it's the maximum value.

**Micah**: I see. Like I said, my preference is 2^52 so JavaScript can use a number instead of a BigInt, again we don't have to talk about it here, and I won't hold up the EIP.

**Martin**: To clarify, if we were to say instead that thius is now a 64-byte thing, that would modify the consensus encoding in the trie for every account object, that would seriously mess with everything, so that is not what this is about.

**lightclient**: As the EIP is, not changing any representation, this is okay to move to final? (_general consensus_)

**Adria Massanet**: There are some JSON tests there that have some unmanaged numbers, we have some discrepencies with Geth with some tests, have some sane limits for this, it would be nice also.

**Tim Beiko**: Before moving to final, should we put it in last call for two weeks? I know there are some RSS feeds that fetch that, so maybe move it to final next All Core Devs if no one has stood up and blocked it. (_general consensus_)

**Decisions**:
- **101.2**: EIP-2681 to Last Call

# 3. Closing Remarks
Video | [1:31:00](https://youtu.be/UGyqRoLwq1o?t=5460)
-|-

**Hudson**: We're out of time, welcome lightclient as a new EIP editor, we've had some discussion, there was no dissent, so lightclient is going to be an EIP editor now.

## Attendees
- Adria Massanet
- Alex (axic)
- Alex Vlasov
- Artem Vorotnikov
- Danno Ferrin
- Dragan Rakita
- Greg Colvin
- Guillaume
- Hudson Jameson
- James Hancock
- lightclient
- Martin Holst Swende
- Micah Zoltu
- Pawel Bylica
- Peter Szilagyi
- Piper Merriam
- Pooja Ranjan
- Rai Sur
- SasaWebUp
- Tim Beiko
- Tomasz Stanczak
- Trent Van Epps

## Next Meeting Date/Time

Friday, December 11 2020, 14:00 UTC


