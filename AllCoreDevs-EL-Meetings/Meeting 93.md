# All Core Devs Meeting 93 Notes
### Meeting Date/Time: Friday, Aug 7 2020, 14:00 UTC
### Meeting Duration: 1:32 hrs
### [GitHub Agenda](https://github.com/ethereum/pm/issues/196)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=Riu-PqrJVH4)
### Moderator: Hudson Jameson
### Notes: William Schwab

---

# Summary

## EIP Status
EIP | Status


## Decisions Made

Decision Item | Description
--|--
**93.1**: No action to be currently taken to implement a standard maximum reorg cap
**93.2**: EIP-2046 not to be included in YOLO for the time being


## Actions Required

Action Item | Description
--|--
**93.1**: Alex Vlasov to gather more benchmarks for EIP-2046 from client teams, if possible
**93.2**: Uri Klarman to recheck prices and calculations for EIP-2780, will reach out to client devs to that end
**93.3**: Hudson to research ACD chat options and present at the next call


---

# Agenda

<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 bullets:1 updateOnSave:1 -->
- [1. Ethereum Classic Chain Split (client implications for Ethereum)](#1-ethereum-classic-chain-split)
- [2. YOLO / YOLOv2 & Berlin State Tests Update](#2-yolo-yolov2-and-berlin-state-tests-update)
- [3. EIP Disucssion](#3-eip-discussion)
    - [3a. Further work on EIP2046 and precompiles repricing (EIP2666) + Experiments on having ops like Montgomery multiplication for 384 bit modulus](#3a-further-work-on-eip-2046)
    - [3b. EIP-2780: Reduce intrinsic transaction gas](#3b-eip-2780-reduce-intrinsic-tx-gas)
- [4. How transaction selection happens in a client at the moment](#4-how-tx-selection-happens-in-a-client-at-the-moment)
- [5. Regenesis](#5-regenesis)
- [6. Change software for ACD chat?](#6.-change-software-for-acd-chat)
- [7. Review previous decisions and action items](#7-review-previous-decisions-and-action-items)

# 1. Ethereum Classic Chain Split

Video | [3:05](https://youtu.be/Riu-PqrJVH4?t=185)
-|-

**Wei Tang**: Focusing on the technical aspect. Basically ETC was 51% attacked twice. It seems the only really important technical aspect of the attacks is how far you can go and reorg over new blocks (_notetaker's note_: may have misunderstood previous). The first attack was detected partially because of a split between Open Ethereum and Geth clients, attack was first thought to be a bug, which caused the ETC team to ask everyone to switch to Geth clients. Later we figured out that it wasn't a bug, but differnet maximum reorg values for Open Ethereum and Geth. For this time there was an attacker chain and a normally mined chain. Since the Open Ethereum client has a fairly low maxiumum reorg value, they refused the attacker chain, whereas the Geth nodes immidiately reorged to the attacker chain. Since the attacker chain had an overall higher difficulty, it created a minority split off of the ETC nodes. If the netwrok maximum reorg cap would be lower, the attack would have happened differently, the attacker rewards would have been lost as well.

The second 51% attack happened after the ETC team had asked everyone to move off of the Open Ethereum miners, and everyone immidiately reorged. Later they actually tried to whitelist the legit chain for everyone to mine and ignore the attck chain, but because the reorg already happened, it was too late to implement such a thing. So both times the attacker successfully attacked.

What is maybe worth discussing is whether we want to coordinate for different values of the maximum reorg cap. There are many kinds of 51% attack that it won't be able to defend against (_notetaker's note_: may have misunderstood previous), but it may be able to defend against this simple 51% attack by setting a lower maximum reorg cap, and basically ignoring attack chains in this way.

After the second 51% attack on ETC, the ETC team realized and are implementing what they call an immutability threshold in their Geth clients, basically a maximum reorg cap which is lower than the current default value.

**James Hancock**: So is the suggestion to have a maximum reorg cap, a standard maximum reorg cap,or ont to have one?

**Wei Tang**: The attacks probably show that it would be better if we have a default maximum reorg cap standard across most clients.

**Peter Szilagyi**: The defult implemented in Geth is 3 epochs (90,000 blocks), and the reason why this was chosen is because 3 epochs is about two weeks. Based on the past (Byzantium updates when Geth and Parity went out of sync), we thought that if the chain goes off on a tangent for some reason and gets reorged, two weeks should be enough to sort out the issues. If two weeks have gone by and we haven't solved the issue, okay, we'll have to resync and do some weird things, but two weeks is enough time to let the chain sort itself out and let people get back to whatever is considered the canonical one. That's why we have it at 90K blocks, and not at a half hour or one hour.

**Martin Holst Swende**: Another thing to mention: If clients start introducing a shorter reorg cap, it still doesn't change that any client who does a past sync and selects the peer with the highest difficulty will sync to the wrong chain, which is an issue that also needs to be solved. Otherwise there will be this weird state where everyone who synced prior to a certain date, they went up one chain, but if they ever have to resync, it's going to be very messy and painful.

**Wei Tang**: Yes. I think this is mainly about an attack scenario where all the nodes have to act immidiately. If the reorg cap is lower, there will be a shorter period of time where the miners will not be on the chain with the highest difficulty. The thing is that after the attack is over, the legit chain will be quickly catching up to the attacker difficulty, and will overtake the attacker chain in a short period of time. It's kind of a tradeoff, but one argument I have is that by setting a maximum reorg cap we'd be more likely to prevent a wide disruption (_notetaker's note_: may have misunderstood previous), since miners are likely online during the attack time, and this zero transaction reorg is a big issue (_notetaker's note_: may have misunderstood previous), but if some new nodes sensing out the network during the attack time, yes, it's an issue, but it's not as big an issue, since they can resync after the attack.

**Alexey Akhunov**: There is another side of this. In Bitcoin Cash they had a similar issue where they were the minority chain and one of their main clients (Bitcoin ABC), they introduced a checkpointing mechanism at I think 10 blocks, which was very short. The security analysis of this particular chain is that even though it does reduce the chance of these reorgs, it can bring the possibility of another attack, where essentially the attacker might get different nodes into having different checkpoints, it's more complicated than that, but essentially you end up with different nodes checkpointing on different blocks, and you will never be able to reconcile again. So you'd have to manually intervene and reset the checkpoints. I don't know all the details, but I remember that there were downsides as well as upsides.

**Wei Tang**: Yes. I want to clarify that 51% attacks are basically unfixable, what I was trying to argue is just about how we can reduce the impact, and make sure that the least amount of damage is dealt.

**Artem Vorotnikov**: So the argument is that even if we expose ourselves to potential DDOS, then it may or may not be better becuase of the 51% attack?

**Tim Beiko**: I'd also be interested to know the dynamics of the hash power better, because a lot of the issues with Ethereum Classic don't apply to Ethereum because there's not an available supply of GPUs to rent as easily. Not sure how that changes the tradeoff.

**Peter Szilagyi**: The thing is that essentially ETC's security was broken down to zero, and someone managed to unilaterally mine a chain with a higher difficulty than the rest of the network, so my problem is that we can discuss different ways to minimize the damage, but the actual damage is that there is an entity which can always mine whichever block, and can always force itself on the netwrok. Then this entity can censor blocks, can mine blocks. Essentially, you can't have a single entity mine all the blocks in the network, or the whole network will be taken over in this scenario. So the question is: how much does it make sense to put that against this (_notetaker's note_: may have misunderstood previous)? Yes, you can protect funds from maybe the last 100 blocks from being reorged, but the entity could just as easily censor the network, or do whatever they want. So what's the point?

**Tim Beiko**: I agree. I'm not sure this is something that should be handled at the client level. Because again, if it's always possible for someone to NiceHash ETC for a couple $100K, it seems like it's a bigger concern than whatever the clients implement.

**Peter Szilagyi**: Another interesting attack: what you can do is just watch the DeFi exchanges for like 5 blocks, collect the transactions, and create 5 reorged side blocks in which you maximize your DeFi gains by simnply playing the offer transactions that you like, and simply counteroffer them. You can maximize your profits based on these decentralized exchanges, and there you don't need to reorg 1000 blocks or break the network, even 3 blocks is enough, and that would be enough. And that would be in acceptable in any client in a proof-of-work system.

**Hudson Jameson**: So is there anyone who thinks that there need to be changes at the client level? (**silence**) Okay, so it doesn't sound like it.

**James Hancock**: Should we agree on a block, like the 63 epoch block and just move forward with that?

**Hudson Jameson**: The reorg cap thingy? (_James agrees_) I don't know if it matters that much that they're the same across clients, does it?

**Alexey Akhunov**: I don't know if we have time for this, but in order to make these decisions, we also have to play in our mind what would happen if the clients have the same threshold, whether that outcome would've been better than what happened. Maybe we shouldn't really change anything.

**Tim Beiko**: I agree that we definitely shouldn't agree to change something now, I feel personally that thinking through the various scenarios needs to be done before we agree or disagree to change anything.

**Wei Tang**: I think this would mostly be an issue for miners and exchanges, but is not something that we probably need to do on the client side.

**Martin Holst Swende**: I'd also like to add that some of the external parties that are suffering are excahnges, and Peter also mentioned the whole DeFi protocols and movements, and I agree that on the platform level, a restrictive platform level, things work as they do, and if you need more robust guarantees about the order things are happening in your DeFi protocol, you can't just rely on the platform layer to not reorg, you have to be robust enough that it makes sense, potentially even in the face of large reorgs. So I think the layer 2 needs to be more robust.

**Peter Szilagyi**: Yeah, but the question is the user experience. The problem is that with decentralized exchanges, even if you introduce some delays, you would expect that if you want to make a trade, that it happens within a minute or two or three, and that is already quite large, in my opinion. Capping the reorg limit to 12 blocks is obviously not possible. Let's say 200 or 500 blocks, but that's still hours, meaning that you push a button to trade on a decentralized exchange, you come back an hour later to see if it went through. That's not really the best user experience.

Honestly, I'm not that familiar with all of these different kinds of exchanges, I just wanted to highlight that once you accept that there are 51% attacks on the network, a lot of things start breaking, because a lot of things are built on the assumption that reorgs like this don't happen. Every dApp is prepared to have a reorg depth of 1,2, or 3,  but a reorg depth of 200, then things will go wonky.

**Martin Holst Swende**: If we leave the reorg portion out of it, one could implement things like transactions which are only executable past a particular block hash. See a certian block hash, know the state, then say my transaction is only executable after this particular block.

Don't witnesses solve the same problem implicitly, since the transaction is only valid if the  witnesses are correct, and the reorg would remove them?

**Hudson Jameson**: It sounds like (just to time-box this) that we don't need to make any decisions about this today, if we even need to make any, since there are a lot of variables invlolved.

**Peter Szilagyi**: Yes, but I think these things need to be talked about. All of us hope we won't see something lie this on the Ethereum maninnet, but I don't think that it's a bad thing to talk about what would be the outcome if it did happen. My point is that although I am in favor of not changing anything for the moment, I am also in favor of keeping discussion going about what can go wrong, and what we can do about it.

**James Hancock**: Is there a place we see the depth of reorgs that are happening, because uncles are basically reorgs in its own way. Where can we see that information?

**Martin Holst Swende**: I don't know if there is any public dashboard of them, but they are present in the Geth logs, as a metric showing the length of the dropped blocks, dropped chain, and the length of the chain, so it can be pulled on Gafana. There is a flow on them, I think that they are swapped (_notetaker's note_: may have misunderstood previous).

**Alexey Akhunov**: Another way to keep them for historical analysis, that I think Geth already does: If a block passes certain criteria, such as the proof-of-work is correct and so on, has a parent, and things like that, the block is saved whether it's canonical or not, then later you can go through the blocks you've saved and chart all the reorgs since you've received all the blocks. It just takes a bit of development to make this visualization.

**Peter Szilagyi**: We could possibly ask Etherscan to add this to their charts, because I think that it's honestly more of their thing than our thing.

**Hudson Jameson**: That's not a bad idea.


**Decisions**:
- **93.1**: No action to be currently taken to implement a standard maximum reorg cap


# 2. YOLO / YOLOv2 & Berlin State Tests Update

Video | [26:53](https://youtu.be/Riu-PqrJVH4?t=1613)
-|-

**James Hancock**: This is coming off the break in July, and getting everyone synced. If anyone has updates, I'd appreciate it.

**Martin Holst Swende**: I don't have updates, but think it would make sense to have YOLOv2.

**Hudson Jameson**: You and Peter started YOLOv1 last time, is that right? (_Martin confirms_)

**Peter Szilagyi**: With v1 we kind of messed it up a few times, the VM dies in different ways, but if there's need, we can always reboot v2.

**Tim Beiko**: Do we want any more EIPs in v2, or just the same set?

**Artem Vorotnikov**: Let's do the same set.

**Hudson Jameson**: Okay, we can do the same set for now while we decide what other ones would go in and all. We could do a v3 for the next ones, I'm guessing.

**Martin Holst Swende**: In my mind, YOLOv1 was and always will be YOLOv1, it's a set of EIPs denominated by commit hash to that EIP, and any other version would be a separate set of EIPs or if the EIPs themselves have been modified. Someone proposed some changes to the BLS stuff, I don't know what happened with that. So if we want to restart v1, I think we should still call it v1.

**Tim Beiko**: I asked since I recall in a past Core Devs call EIP 2046 changed some gas costs that we discussed to be included in a later version of YOLO. I don't have a strong opinion either way.

**Hudson Jameson**: We can pick this back up after agenda item 3a, which talks about 2046, which is Alex Valsov's item, correct?

# 3. EIP Discussion

Video | [29:41](https://youtu.be/Riu-PqrJVH4?t=1781)
-|-


# 3a. Further work on EIP2046 and precompiles repricing (EIP2666) + Experiments on having ops like Montgomery multiplication for 384 bit modulus

Video | [29:41](https://youtu.be/Riu-PqrJVH4?t=1781)
-|-


**Alex Vlasov**: With the break in the way of development and Berlin being delayed, there is a timeframe where it would be possible to work out the details of 2046 or parts of 2666 with consistent pricing of precompiles with their current performance, so I was mainly interested in if some client developers had some time to run some benchmarks and maybe post some numbers.

**Martin Holst Swende**: I know that way back you produced some benchmark vectors, but not for all the precompiles. Have you produced all of them now?

**Alex Vlasov**: I didn't place the Modex (_notetaker's note_: may have misunderstood previous), since the Modex EIP is separate, but I have produced for hash funcitons and ? precompile, largely every precompile which is out there which may have been mispriced. I have seen that Nethermind has produced some benchmarks, but I haven't seen the numbers. As far as I understood from Gitter, Besu may or may have not run, but want to improve performance, perhaps because they ran them and they were way off and pose a potential security threat. I am at least interested in collecting the data, and even if the numbers in, for example 2666, maybe should be adjusted up a little bit in order to match the perfomrance of all clients, not just Geth and Open Ethereum, which I measured by myself. It's still necessary to know if there are contant factors which are off which are compensated with the large staticcall price right now which can become potential issues if 2046 is accepted. 2666 is a huge mix, it also proposes different error handling for precompiles, which is a completely separate question which can be discussed a different time, but to push 2046 and at least some consistent pricing for precompiles, I need the data from client developers.

**Martin Holst Swende**: I don't quite agree. What you need is a thumbs-up or thumbs-down from the client developers.

**Alex Vlasov**: There is a freedom in the choice of price parameters, maybe I just need to tune them upwards say 25% to account for all of the clients, not just one. (_Martin agrees_) Then it's reasonable to make an adjustment in the parameters, aforcing every client to do some hard optimizations to feed into performance.

**Martin Holst Swende**: For Geth we're on board that 2046 is reasonable, but the benchmarks for actual precompile pricing have not been performed by our team.

**Alex Vlasov**: I'm less worried about Geth and Open Ethereum, but don't have experience with the other clients or the languages that they're written in.

**Hudson Jameson**: So if Besu has any update...

**Tim Beiko**: I remember that we ran the benchmarks for 2046, and if I remember right we were good with the price for 100 and 40 was slightly to low, and I don't know about 2666, I don't think that we ran those benchmarks.

**Hudson Jameson**: (_checks for members of other clients - none present for Nethermind, Trinity_) So Geth is on board, Alex ran Open Ethereum.

**Alex Vlasov**: I ran Open Ethereum following Martin's way, and the safe number for Open Ethereum was more like 26 or 25, so there is some margin, so the proposal of 40 was fine for it.

**James Hancock**: Is it worth including 2046 into YOLOv2 so that we can get more numbers run?

**Martin Holst Swende**: Not really, since if we only do 2046... we could do it, but we could never roll it out on mainnet, because we need to erase some of them (_notetaker's note_: may have misunderstood previous). I think we lower it by 606 (_notetaker's note_: may have misunderstood previous) gas.

**James Hancock**: So we'll put a pin in that one.

**Martin Holst Swende**: We could roll it out if we just want to try out the implementation. I don't really have an opinion.

**Hudson Jameson**: It might be worth it to have more than one thing before we do that.

**Alex Vlasov**: The most potentialy dangerous part is that if there is large kind of constant cost in various precompiles that are covered by the staticcall price that won't be covered anymore, they could be partially identified, or not partially, let's just say just 1825 and 2666 (_notetaker's note_: may have misunderstood previous), so if client developers would be willing to run the benchmarks, and I can check that there are no such constant factors, then on the next call we can agree on a number for 2046 and just accept this, and do a separate EIP later with repricing the precompiles based on all clients' data. So I would try to get the data first, and then even try to select a number for 2046 or vote for it.

**Hudson Jameson**: So you'd like to have this done by next time?

**Alex Vlasov**: I would be willing to check the data if I can get it from devs, but it's not up to me.

**James Hancock**: We would need benchmarks from Besu, Nethermind, and Trinity.

**Hudson Jameson**: Not necessarily Trinity.

**Alex Vlasov**: Nethermind has the data, either it wasn't posted or I couldn't find it.

**James Hancock**: I remember that he ran the numbers and said something in All Core Devs, but I don't where that went.

**Alex Vlasov**: I'll try to search the history, but we still need more data points from Besu.

**Tim Beiko**: We can definitely do that before the next call.

**Hudson Jameson**: Is there anything else on th 3a point that you would like to discuss now Alex?

**Alex Vlasov**: If there are many other items in the schedule I can pass, but there was also a proposal to change error case gas pricing for precompiles and only for precompiles. It would be along discussion, I think, and very opinionated.

**Hudson Jameson**: We can come back if there's time at the end, do you want to do that?

**Alex Vlasov**: Sure.


**Decisions**:
- **93.2**: EIP-2046 not to be included in YOLO for the time being

**Actions Required**:
- **93.1**: Alex Vlasov to gather more benchmarks for EIP-2046 from client teams, if possible


# 3b. EIP-2780: Reduce intrinsic transaction gas

Video | [39:42](https://youtu.be/Riu-PqrJVH4?t=2382)
-|-

**Hudson Jameson**: Uri will speak abut this proposal, the agenda item is a clickable link for those interested. I think that Matt Garnet is involved.

**Uri Klarman**: Matt created EIP 2780, and to start with outlining the motivation, and move to if it's a good idea, what we should consider, and how to make a decision. The bottom line of this EIP is: can we reduce the cost of sending transactions from 21K gas to 7K gas. The motivation is that it became very costly even to send ETH around. The reason for that is competition with very time sensitive and very large transactions due to DeFi. It is a good thing that the chain is being utilized by the most valuable transactions, and that's by design, but the question is if we can allow for more transactions on chain without introducing negative externalities, or with very, very small ones that are worth the cost. If we were able to allow 1K transactions per second on chain and the only cost was the increase in state size by 001% and no added DDOS vector, we'd want to do it, and if it was the opposite, so the question is for the downside of reducing the intrinsic cost of sending a transaction. I want to review the different concerns, just to identify what is an issue, and what isn't, what is needed for the Core Devs to decide if this is something that should be done or not.

The main concerns are the implications of state size, which is already an issue. If we allow for something like that and it increases the rate at which state size increases, that's an issue. There was a concern, maybe by John Adler, if it allows for gas tokens to manipulate the price even further, and Vitalik brought up the uncle rate. These are the main concerns.

**Martin Holst Swende**: In the EIP it says that the creation of each account adds 20 bytes to chain state. This is very, very wrong.

**Uri Klarman**: That was a mistake. It was supposed to be more like 20KB.

**Martin Holst Swende**: That makes more sense. Secondly, with 10 million gas (_notetaker's note_: may have misunderstood previous) there is a max potentially of 476 transactions in a block, and wiht this it would be twice that, so 1400 transactions in a block, and even leaving state aside, it means blocks become huge, more load on the network, more load on disk and syncing. Today you have something like 5-600 million transactoins from genesis, maybe even more now, and if you consider that having been tripled, it's big. Looking inot this EIP I think the security considerations and externalities are very understated.

**Uri Klarman**: I generally agree with you, let's touch on this issue as well. When you say beocmes big, there's the question of them becoming big byte-wise, and also how does tripling transactions affect this side (_notetaker's note_: may have misunderstood previous), all of this needs to be seen. One aspect to add is the question of usage vs. attack. If usage increases due to this change, how does this affect, say, I/O load, and then there is also the question of if this change can be leveraged to make an attack. My main argument regarding the attack is can this attack be launched today? Could it have been launched a year ago? What would have been the cost of making such an attack? It should be further outlined in the EIP itself. What if someone utilizes this new vector, and attacks the block with many small transactions, how much will that cost today with DeFi, and how much did it used to cost? I think I had some disagreement with Peter about this on Twitter, should an attack vector should be considered only in terms of if it is possible, or should how costly it is also enter the discussion. Does this make sense?

**Martin Holst Swende**: I'm not sure.

**Alexey Akhunov**: We might be able to discuss the peculiarities of this particular proposal at a different time, but we have essentially this crisis moment with a lot of externalities relating to the core infrastructure of the internet, and I would look at the network as the core and the boundary. The boundary is where your transactions are coming from, they're where the DeFi sites are sitting. The core is essentially the nodes which propogate the transactions. The boundary is where the value is created and captured, and the core is what services the boundaries. At the moment, unfortunately, we've created a system where the boundary externalizes its costs into the core, and this is one of the reasons it can capture the value. We need to solve this problem, try to reduce the externalities so that the boundary participants have to incur higher costs, and the core infrastructure incurs lower costs. It might look logica to ask why are transactions so expensive, but if we make it cheaper, it will probably bring more users, but it will also make the crisis worse, to the point that we will be crippled by these externalities. I agree with you that in a different situation we could discuss the merits, but my opinion is that we need to step back from it for the moment. We know that the network is vulnerable to all sorts of DOS attacks, we don't want to make it worse until we have a clear way of fixing it.

**James Hancock**: Something that got clearer for me about the last few calls is another additional dimension. There's is it possible and is it likely, but then there's something that I don't tihnk we talk about as much, which is if it did happen, what can we do about it, what are the consequences. With state size and some of the other stuff, if something goes wrong... there isn't an undo button for these things, which makes it more leaning on the side of security, in my opinion.

**Uri Klarman**: I want to reply to all of these points, I'll start with James. I agree, and the previous discussion really touched on this idea. This is why I want to point out what is an issue and what isn't. The things which we consider to be an issue, how big an issue are they? Martin did a back of the envelope, asked about load on the network, Alexey talked about boundary and infrastructure, and as someone who is working with on the networking layer with the majority of the top 20 pools in Ethereum, I totally agree with that.

I do want to talk about the state size, the gas tokens, and the uncle rate, in order to say that if we did this, reduced the cost of sending a transaction 3x, even if we go with the extreme assumption that it would mean 3x more transactions, which is very unlikely. State size is a major issue, and it needs to be resolved regardless, but even if we did this, it turns out that if we did reduce the cost of sending a transaction, it would increase the growth by about 1%. If we had done this January 2020, the state size over the last eight months would have increased 0.5%.

**Peter Szilagyi**: Didn't you agree that the numbers in the EIP were flawed?

**Uri Klarman**: I'll redo them, I don't want to do this on the fly, I do think that the calculations were done using 20KB, but I don't want to give a conclusive answer on the fly.

**Peter Szilagyi**: 20KB equally doesn't make any sense just like 20 bytes. Essentially, the leaf of a plain account is 70 bytes, plus trie nodes which are 8 or 9, realistically there should be around 4KB or something. The numbers should really be checked out.

**Uri Klarman**: I really don't want to say something when I can't check it out, maybe it was supposed to be 2KB. Going back for a second, state size is an issue, but if we change this, does this open attack vector that we don't want to open. Usage-wise it doesn't seem to effect it much, even if usage does increase. Going back to motivation, when the Ethereum chain gets hard to use, and this isn't about bringing in new users, but about people getting frustrated that they can't build the things they want to build, or do the things they used to be able to do, it causes a leap to other chains, which is a shame.

**Hudson Jameson**: I thin the motivation isn't the key thing we need to be discussing. I think it's understood. I think risk should be the focus based on most of the questions. I also need to time-box this a bit, so my recommendation would be to sure-up the numbers a bit, and maybe cross-reference them offline with a client dev, especially about some of the numbers based on what Peter just said, the different parts of the chain that get 'sploded whenever there's a gas reduction like this. So, if you want to give a final summary, then we can move on. Sorry to time-box, but we need to move on.

**Uri Klarman**: That makes total sense, and I appreciate it, and I appreciate everybody's feedback.

**Alex Vlasov**: This EIP touches a point for which there is no data available, and from my perspective, purely technical, increasing the number of transactions by a factor of 2 should increase the amount of time it takes for a miner to actually process and create a block by twice the number of actions. In a previous call, maybe two calls ago, there was a number said by (_notetaker's note_: may have misunderstood previous) Alexey which might have been correct or just a random number in the chat that in order for a miner to be profitable, they can only spend something like 14ms to assemble the block. Trying to clarify this information would have separate value, since it could also affect other proposals, which could try to increase block size or introduce transactions that require more preprocessing. I don't know if the Core Devs have any information of this kind, or if it's classified.

**Uri Klarman**: I heard this 14ms number, and I actually think that it is wrong. Looking at the logs from miners it looks to sometimes be in the order of 200ms if you don't consider mining an empty block. I want to wrap up, you're bringing up a good point, does this affect the amount of time that a miner takes to mine a block, does it throw regular nodes off the chain, does it open up a DDOS vector, all of these I'd argue that it isn't, my goal was to bring up what is an issue and what isn't, but I'll take Hudson's advice and reach out to a few of the dev team here, thank you for being available to respond in advance, and come back on that EIP with more clarified numbers.

**James Hancock**: Numbers, but also the research to show that it's safe from the things you listed off would get you the farthest, I would suggest.

**Uri Klarman**: Doing a simulation is very not meaningful compared ot a testnet. My goal is not to convince people, but actually to test it and see if it could work.

**Martin Holst Swende**: Anything can work on an empty testnet.

**Hudson Jameson**: It would be hard to simulate. There's simulation software that I've heard has been developed for things like this, but the kind of testnet this group spins up do not have wide participation.

**Alexey Akhunov**: This is a pretty good example of linking to what we've been talking about over the last three calls, so it's hard to pass up. The first thing, after the last call I realized that we need to give opportunities to client teams to say they're not ready for something, otherwise the calls become pressure calls. Client teams should be able to say we're not ready, please wait, or if you don't want, collaborate with the other client, help them get around a bigger share, then we'll have to do that.

**Martin Holst Swende**: I agree.

**James Hancock**: If we need to have a bad guy, I'm happy to do it.

**Hudson Jameson**: You always are. (_laughter_) Sounds like we have some good next steps, Uri, thanks for bringing this up.


**Actions Required**:
- **93.2**: Uri Klarman to recheck prices and calculations for EIP-2780, will reach out to client devs to that end

# 4. How transaction selection happens in a client at the moment

Video | [1:02:03](https://youtu.be/Riu-PqrJVH4?t=3723)
-|-

**Peter Szilagyi**: This topic was brought up around the conversation of how to get around the spam on mainnet, make it more deterministic, and in Geth we did implement a first in first out sort order, and if multiple transactions have the same price, they will be sorted by arrival time. We will probaly release on Monday, and we'll see if this helps the network or not.

**Hudson Jameson**: Are any other clients planning on doing any transaction ordering?

**Artem Vorotnikov**: We are not working on it, and probably won't be for the foreseeable future.

**Alexey Akhunov**: Open Ethereum already has the logic that Geth just implemented, I know this because in 2017 Parity had a logic where if transactions had the same gas price, it would sort by transaction hash, which allowed people to get the first entry for a certain block, and was very important for things like the Status ICO where they essentially capped the gas price, so you needed to be able to get a low hash in order to be able to get in, and I reported it, and when I looked they sorted it like Geth did now, so I don't think there's anything to do unless something has changed.

**Hudson Jameson**: What about Besu?

**Tim Beiko**: It's not something we've looked at. It seems like a small-ish change, we're just waiting to see how things go on the network once Geth is out, which is a majority of miners.

**Rai**: Is the consensus to sort by arrival time?

**Alexey Akhunov**: It seems like the simplest option with few downsides.

**Peter Szilagyi**: We can definitely investigate different sorting methods, it doesn't really matter as long as it's deterministic. The other two proposals, sorting by transaction hash allows it to be mined, and sorting by account hash or addess also has a negative effect on the chain, that people will start to mine accounts, and weird things that someone left their GPU miner on it for a week and now has a priority in all transactions. I didn't like these approaches, which is why we went with firs in first out, the worst you can do is try to find a direct connection to the miners, or miners could sell a direct connection. At that point, they may as well sell priority regardless.

**Rai**: Makes sense to me.

**James Hancock**: You said that was going to be released on Monday, possibly? (Peter concurs) If there would be an effect, where would we look for it?

**Peter Szilagyi**: I have absolutely no idea.

**Martin Holst Swende**: The people who reported this initially I suspect were looking at the pools and analyzing transactions. But nothing is going to happen overnight, only when it no longer makes sense to do this spam will they stop, when it costs more than it's worth, and it'll probably be a couple of weeks before they can realize this.

**Peter Szilagyi**: The overall effect which we are looking for is that eventually enough miners upgrade, and these plays with a bunch of random transactions hoping that one is first will turn into needing to only send one transaction since it doesn't make sense to send more. People who are frontrunning will quickly realize that they are losing money, and that should actually drive the gas prices down, since there aren't millions of transactoins racing to be in a certain order. So the effect we're looking for is for the gas price to go down.


# 5. Regenesis

Video | [1:09:12](https://youtu.be/Riu-PqrJVH4?t=4152)
-|-

**Alexey Akhunov**: I recently wrote 'The regenesis plan', which is a more detailed plan about how we might implement this. Essentially, we logically split the state into two disjoint parts, we call one active state and the other inactive state. We do not change the way the state is merkelized, so we keep the existing way of computing state, merely introduce this logical distinction. Then we introduce the concept of regenesis events, they would occur regularly, maybe prescheduled times, or maybe by manual decision, for example, one million blocks, roughly six months, and what happens then is that the active state is reset to just the state wiht hash, and everything becomes inactive state. Between these two regenesis events, or during this six month period in the example, the rules of the game change in around four different ways. Transactions need an extra attribute, a witness, which is basically a string of bytes which includes some merkle multi-proof (_notetaker's note_: may have misunderstood previous). I'm not going to go into the details about how it works, but I have thought about it quite a bit. What happens when a transaction executes, we find any valid part of the proof, and activate those parts that are presented in the witness, and make them part of the active state. Then there's a block witness, which should be fairly small, which is introduced for the miners to prove their coinbase, otherwise they can't get their reward. It's attached to the block, and if the coinabse isn't in active state already, they should include it in the witness, and this block witness gets added to the active state before any transaction. We charge in the hard fork version, the only thing we need to hard fork is to include this transaction witness as chargeable data. At the moment you only charge for data, now you'd also charge for the witness. The nice thing is that compared to Stateless Ethereum design is that you don't have to figure out how to split the charge across multiple senders since it's only sent by one sender. The execution semantics of transactions change as well in a way that if the transaction runs and it's in an active state (_notetaker's note_: may have misunderstood previous) then it reverts and the gas up to that point is consumed, but any effect in the active state is preserved. There's also a proposal to change the chain ID so that after the regenesis anything that didn't make it won't fail, but it will need to be resubmitted (_notetaker's note_: may have misunderstood previous). The perceived benefit of this proposal is that if we regulate the regenesis events properly, say we target an active state size so, for example, modern machines can store in RAM or devices with very low latency and so that it can be gotten easily, that means that all the state accessing operations like sload balance and sload hash just read from RAM, and you don't have to keep adjusting their cost all the time. 

There is an implication for the transaction senders, that they need to acquire a snapshot of the state, but not the active state, acquiring a snapshot of the latest regenesis event, and that should be enough to generate a valid transaction, but if they want to minimize the witness, they'll need a more recent snapshot, at their cost. This is one of the more philosophical considerations of this regenesis is that it pushes the cost from the core to the boundary, basically the node which simply relays the blocks and verify things expend less resources, but the nodes that inject tranactions, and we assume these are boundaries where value can be captured, they'll need to optimize more, know how to download state, and if they want witnesses to be smaller, they'll need to get as fresh a state as they want. The main difference from the status quo is that the failure to optimize stops becoming this systemic problem. At the moment pretty much all optimization has to happen in the core, and if we fail to do continuous optimization it introduces systemic risk and the network can fail. With regenesis optimization will have to happen on the boundary, which doesn't have the same systemic risk because the boundary is more diverse and has more money around, and if one operator falls behind it will hurt, but it won't hurt the whole network.

I'm not going to go into the details about how we could roll it out, that would be a very technical discussion, I would like to invite everyone to the Eth R&D Discord, there is a special Regenesis channel. There is also an HTML file that I posted on Twitter about how we might possibly be able to transition to this thing, so I invite you to read that so we can get more technical discussion.

**Hudson Jameson**: A lot of the discussion is happening in the Eth R&D Discord.

**Martin Holst Swende**: About transactions needing only the state from the last regenesis event, wouldn't they possibly need data from earlier regenesis events?

**Alexey Akhunov**: No, they'll only need the last regenesis event or more recent. Basically, if they just produce the witness from the regenesis event, the only risk they run is that the element of the witness which is close to the root will be invalid, but they will be recognized as such, but these elements will already be in active state, so it will be easy to see what is valid and what is not. They don't need anything from prior, because regenesis doesn't depend on what happened in the previous regenesis, it simply slashes the active state and starts over, it doesn't matter what happened before. If you look at it this way, it probaly becomes clear that there is no historical memory in the process.

**James Hancock**: That's because the witness provides any information it would need?

**Alexey Akhunov**: No, because there is a convention that the witness could be considered if it originates from any block header from regenesis until now. Of course the root part will be invalidated, but it won't matter. If the witness is produced for an earlier snapshot, it is rejected. Maybe some of the bits would be valid, but it would be by chance. If you want to guarantee that it will be valid, you should include at least the regenesis.

**Rai**: I'm curious what's happening at this boundary, if there might be any incentive to play a game of chicken where you don't want to be the first to submit a transaction that touches state so that they include it in their witness so that you can assume the state is already there. Have you thought about this?

**Alexey Akhunov**: Yes. I don't know if it's going to be a problem for a few different reasons. I could be wrong, but one thing is that if you're a DeFi application and you run a smart contract, what you're probably going to do is run an empty transaction which will reveal the roots for the contract in order to ensure that everyone can submit cheaper transactions. But, for example, for some contract no one has used in three years obviously this won't happen.

A second feature which fell out almost randomly, since there is a block witness, they can use that potentially to repair transactions. A miner sees a transaction and it would fail since they didn't include the entire witness, but they can help them out and include the missing data at their own cost/risk and ensure the transaction will succeed. I think these two things put together can alleviate the risk that you're talking about. The miners in the transition period where people might forget to include the right witnesses can help, and then after this period can stop caring.

**James Hancock**: We'll talk about this in the next Eth1.x/Stateless meeting, which will likely be either this coming Tuesday or the one after that. (Wednesday in Australia time.) Will post in All Core Devs chat.

# 6. Change software for ACD chat?

Video | [1:21:57](https://youtu.be/Riu-PqrJVH4?t=4917)
-|-

**Hudson Jameson**: A lot of people, especially those normally active in the Core Devs chat, are now active in the Eth R&D Discord. I was thinking of talking to them about moving the All Core Devs chat from Gitter to Discord, and archive so that we don't only have one channel. I think we've outgrown the Gitter channel, there's spam sometimes, there's not great moderation. Any thoughts about slowly moving the chat into subgroups on Discord?

**Artem Vorotnikov**: I would say let's move today.

**James Hancock**: One nice thing about Gitter is that it and the public history is publicly available, whereas on Discord in can disappear pretty easily.

**Hudson Jameson**: I can make a bulk delete script on Gitter too, not just Discord.

**James Hancock**: Only the admins, though, Also, it's possible to link to a point in historical chat in Gitter, which doesn't exist in Discord.

**Martin Holst Swende**: James's point is good. Gitter is easy to scrape and search locacally. I don't kow how easy that is to do with Discord. If Gitter goes down, I have all the conversations I've ever been in, I assume it could be done on Discord as well.

**Hudson Jameson**: I'm looking at the permissions in Discord, and you can make it so that people can't delete messages, I believe. I think everyone can always delete their own messages, but can't delete others', which is like Gitter. As far as Discord vs. Gitter going down, who owns Gitter now? (consensus that it's GitLab) I wouldn't consider that more of a concern, we'd have the chance to archive and migrate out. A solution might be to have a bot in the Discord that anyone can ping to get a log file of all conversations for a channel, and that's more of long-term thing.

**James Hancock**: My two concerns are that a lot of these conversations are really important, and it would be a shame to see them disappear because someone ragequit and deleted them. And that Discord, although anyone can join it, as more people join it, they get more selective about who can join, so I have concerns about how public discussions would be and how much it would be shared with people outside the channel.

**Artem Vorotnikov**: Those are valid concenrs, and if they're paramount, then Discord is not the best option, and I'd consider Matrix. Parity is on Matrix, Wei can tell us about it.

**Wei Tang**: Matrix is pretty great. I actually wanted to raise a concern about Discord, about the archiving issue. There are bots for archiving, but it might be against Discord's Terms and Services, they might not allow archiving of a server's conversations because they somehow consider it to be private or something. Matrix's user experience has improved significantly, and they have a great chat app called Element. For decentralized, Element can set up a server and talk with any other server.

**Hudson Jameson**: The biggest thing in my mind is network effect and getting people to join. Just looking through the list on Eth R&D Discord every major client other than Nethermind is there, and Nethermind is present via a bridge to Telegram. We could ask them about moving over one of their people, too.

**James Hancock**: I would be fine if the discussion is happening on Discord, as long as it's mirrored somewhere that is then public and non-erasable.

**Hudson Jameson**: I could see options for that. Let me think about that and explore options either for bots or a bridge or things like that. I also need to talk to the admins there to see if it's possible to move this there, or if they think we need a whole new server. I'll research the details and come back without anything finalized next time.

**Tim Beiko**: I think there would be a lot of value in keeping a single channel, as opposed ot many channels in the destination, and maybe splitting later.


**Actions Required**:
- **93.3**: Hudson to research ACD chat options and present at the next call

# 7. Review previous decisions and action items

Video | []()
-|-

Out of time.


## Attendees
- Alex (axic)
- Alex Vlasov
- Alexey Akhunov
- Artem Vorotnikov
- Hudson Jameson
- James Hancock
- Karim Taam
- lightclient
- Martin Holst Swende
- Peter Szilagyi
- Pawel Bylica
- Pooja Ranjan
- Rai
- Tim Beiko
- Uri Klarman
- Vie Yang
- Wei Tang

## Next Meeting Date/Time

Friday, Aug 21 2020, 14:00 UTC

