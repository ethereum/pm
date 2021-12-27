# All Core Devs Meeting 128
### Meeting Date/Time: December 10, 2021, 14:00 UTC
### Meeting Duration: 1 hour 30 min
### [Github Agenda](https://github.com/ethereum/pm/issues/428)
### [Video of the meeting](https://youtu.be/Py1_Bw0frO0)
### Moderator: Tim Beiko
### Notes: Alen (Santhosh)

## Decisions Made / Action items
| Decision Item | Description | Video ref |
| ------------- | ----------- | --------- |
|128.1 | We still need to figure out the authentication mechanism between the, the,consensus and execution layer nodes - Tim.| [4.52](https://youtu.be/Py1_Bw0frO0?t=292)|
|128.2 | A broader discussion is needed to determine which takes precedence if it is 4488 vs merge. - Vub.| [50.37](https://youtu.be/Py1_Bw0frO0?t=3037)|
|128.3 | The merger takes place first, followed by 4444 and 4488, implying that a trade-off with Shanghai may occur.| [1.16.20](https://youtu.be/Py1_Bw0frO0?t=4532)|
|128.4 | The announcement to the community about Ethereum's chain history guarantees will no longer be available after the merge.| [1.26.20](https://youtu.be/Py1_Bw0frO0?t=5188)|


## Intro:

**Tim Beiko**
* Hi, everyone. Welcome to AllCoreDev 128. we have a few things on the agenda today. first Arrow Glacier went live yesterday, then, we can discuss Kintsugi and the merge and then finally, EIP-4488, which, yeah, we've discussed it over the past two weeks. 


## Arrow Glacier recap

**Tim Beiko**
I guess starting with Arrow Glacier, it seemed everything generally went well with the fork. One thing I noticed is there were two Chinese miners, I think, okay. X and he'll be that I did not upgrade. I was not able to check this morning to see if, if they had, I saw like two blocks mind on the old chain. I don't know if anyone has three more context on that or just anything else they wanted to share about the Arrow Glacier. Okay. yeah, I'll try and dig into this later today, to see, if, the two miners have, have upgraded, it's been a bit harder to get ahold of them since the mining ban in China. next up, 


## Kintsugi 

**Tim Beiko**
Kintsugi so we launched another devnet this week. does anyone have any kind of updates they want to share about their progress ? Generally? 

**Marek Moraczynski**
* I can give you an update. Yeah. So on Tuesday we started merge devnet. That is based on latest Kintsugi spec. Generally speaking, it's been successful. Nonetheless at the beginning, there was a little chaos, mainly because of renaming. However, all clients teams, quickly delivered fixes, and now we have stable network we've Geth, Nethermind,Besu,Lighthouse, Teko and there are has some issues that we should investigate together. I mean, Geth, Nethermind,  as far I know there is known bug and they are working on it. Mario's performed spamming, but he hasn't destroyed the network yet. in Nethermind, we continue working on, things, what is important. We updated instructions on how to run Nethermind with every consensus client, so everyone can try to sync with the devnet and that is still, I think.

**Tim Beiko**
* Cool. Anyone else? 

**Gary Schulte** 
* Yeah, I can speak to, Besu we, we're a little behind on the getting onto the dev nets, but, we're we have the B3 spec implemented and we're interrupting low inter-operating, locally with, emerging market and Teku. And, we're just waiting on one more PR before we're going to be, joining the devnet basically where we need to get our, backwards sync PR merged then. And as soon as we do, we, have the instructions and, get that out there so that other people can be working with that execution plan also. 

**Tim Beiko**
* Cool. Anyone else? okay. And I guess, yeah, more, more generally. I was talking with Mikhail yesterday helped me you're here. Yeah. it seems like, the, the kind of big buckets of things that are, that we still need to figure out are, optimistic sinks.So there's some work on specking that, and, kind of addressing some of the edge cases. One thing, that we also discussed that earlier on was basically the auth mechanism between the, the,consensus and execution layer nodes that's still kind of something we're going to need to figure out. And then Marius, you had found some issues with like the the fork choice, if there's competing proof of work, proof of work blocks, of the merge, that's still something that needs to be addressed in the spec and tests. so does it seem like the three kind of big, outstanding things, obviously testing all around, the more we can do the better, that said, it seemed this week when I was talking to people that, we should be able to launch Kintsugi of a more long live dev next week. Perry and his team were, were working towards that, that it seems like we have kind of all the infrastructure set up to not only launched Devnet, but have kind of a, a UI that, people who want to interact with it can use. so I guess we'll, we'll be doing that in the next week or so one thing that would be really helpful from client teams is, you know, having like some instructions about how connect your client to the devnets, even though it's not merging the master branch. And it's, it's maybe a bit, it maybe requires a bit of like manual wrangling. I think that's really something that, that would be good over the holidays so that people can kind of try out different kinds and see them working on, on Kintsugi. 

**Marius Van Der Wijden(M)** 
* Yep. So, yeah, go ahead. So, I have two small things. one thing was, when we launched Kintsugi when we launched a devnet 3, there was some issue with clients not proposing any blocks or not just proposing empty blocks after the merge. And so I was wondering, what's the correct behavior there, like, if you're like, I think that there's a case to be made for, for whether the data's just proposaling empty blocks. but, that could also be a case a case can be made for, for just not proposing a blog, because, you know, like you, like, you're valid data is, something's broken and you need to fix it. And, if you, like if you validate and you, if you test to, to a block, even if you know that this block should contain a payload, but it doesn't, then, it's better for the network because the network keeps on moving. but not really not everyone does it. So, yeah, I think like, I'm not sure 
* What's the best behavior to do, to do them if, like empty blocks, a proposed post-merge and so that's, that's probably, 

**Tim Beiko**
* What's the reason that empty blocks are proposed post-merger. Is that just when there's competing proof of work blocks or is that all the time? 

**Marius Van Der Wijden(M)**
* No, it was because the execution layers were not, or the consensus layers were not connecting to the execution layers correctly. Right. So they figured out that the merge was done, but they didn't produce, they didn't, call execute payload or prepare payload correctly. And, so they didn't didn't get any payloads. So they just, proposed empty blocks as far as far as I know, I, I don't know what really happened, but this is like, what I think have Empty means that no transactions testing Empty, I think empty meant that no  payload was in this block. 

**Mikhail Kalinin**
* You mean there Was zero payload, like, before the merge? 

**Marius Van Der Wijden(M)**
* Yes. 

**Mikhail Kalinin**
* Oh, then it means that, actually, if it happens, it's going to be considered as the merge has been done because the consensus of their clients, starts to, switch the logic, into the transition process. But once it sees a that to payloads, so these guys have very low odds. if, if, if the transition is already in progress, in the network, then, if this kind of block is published, with, the payload, with all the zeros, the owner's behavior is to reject this kind of blocks because this is not valid blocks anymore. So I, we can try to figure this out, like a fine that's. 

**Marius Van Der Wijden(M)**
* Yeah. That's, that's just what I wanted to say. And the other, the other thing is, yesterday night I had the great idea to just go ahead and shadow for curly, and I think we can, we can do that pretty easily. And, we plan to do, like, once the wants to devnet it's it's, it's merged, once the Kintsugi Testnet is running, then we're going to start trying to, create our own set of work of curly. And so if that is something that you're interested in joining and reach out to me, and, and, Perry, probably going to set this up, that's it. 

**Mikhail Kalinin**
* When do you want to do this? 

**Marius Van Der Wijden(M)** 
* After the Testnet is done. So I think it's, it's, it's probably a thing of like a day or so to figure it out. and it will, like, it will not impact the normal operation of curly. We, we will just send curly notes and then say that the term total terminal difficulty is reach, which means our, for our nodes we'll fork off of curly. And then we'll continue on the, on the merge chain

**Mikhail Kalinin**
* And your going to share the nipple with the curly nodes after the merge, after this. 

**Marius Van Der Wijden(M)**
* Yeah, let's say, Yeah, not really, because we will have different folk IDs. But, yeah, like at least for some point we will, we will still have some of the same transactions. but then the networks Will diverse probably. 

**Mikhail Kalinin**
* Okay. 

**Tim Beiko**
* That's pretty cool.  yeah, looking forward to seeing you at.

**Parithosh**
* Just continue on the Kintsugi planning, is everyone, can we have some consensus about, who's going to take part from the execution clinet side next week's testnet. And is it okay? Like, is everyone on track for Tuesday or should we be looking at delaying it to Thursday or something like that? We are okay with it yesterday. Okay. Sounds good. I just post a message about, features and things like that in the interrupt channel on Eth R&D. So just have a look whenever you guys are free, and then we can take a discussion there. 

**Tim Beiko**
* Yeah. And I saw your message on the R&D channel also paints the consensus layer teams. So that's definitely something we want to make sure. and yeah, it seems reasonable if, if delay in a couple of days makes an extra team kind of able to join the network, we probably should. 

**Parithosh**
* Exactly. Yeah. Yeah. We can discuss that on this call. I don't think we have to, unless someone has some specific point around the need to continue again. 

**Tim Beiko**
* Anything else about the merge in general? 

**Mikhail Kalinin** 
* Yeah. I have a small announcement. Yeah. I've opened up the proposal it's been mentioned during the previous call. it's the Geth the payloads, it's now a PR to the engine API spec. so, the Geth payload bodies function reflects the logic of the Geth blog bodies message of Eth protocol. This is actually the crux of this proposal. cause it's, apparently it's easy to be implemented. It's just basically it's just exposed in almost the same or literally the same logic, in the, in the other part of the client in the other API. So let's take a look. Any concerns, any issues that you feel that this proposal, go to the PRs comments and let's discuss, I'll keep it, I'll keep it open for a while and then just merge if not This thing you're talking about, where is that? Oh, yeah, I've just dropped in the chat. Can you see? Yeah. So, one of the concerns, there is an issue, there is, there is a discussion thread and the issue, one of the concerns, was like if we expose them base, methods, which, requests the payload bodies by a hash, it actually doesn't allow for using the linearity property of, blockchain. like it would be, we, we're requesting, those bodies by numbers, which doesn't allow for like, if the linear's appropriately is utilized, it allows for, more optimal requests for the same data to be done on disk terms of disc, queries. So that's what, that was one of the concerns. But as long as this reflects the ETH protocol message, I think it's okay.  probably not so worst worth taking a look at.

**Tim Beiko**
* And to be clear, this is not something we expect to have by Tuesday. Right. Like we would have this, I guess, in the post, the post, Kintsugi version. 

**Mikhail Kalinin**
* Yeah. Right. So it's not, it's like for, yeah. For after Kintsugi merge spec.

**Tim Beiko**
* Yep. That sounds good. 

**Martin Holst Swende**
* Just a quick, quick feedback  if you're, if you're worried about the, like optimality of this, thing. So this for Geth, we have the whole transactional thing store does RP and also as snap encoded and RLP, probably it doesn't make sense to like return. That's not been coded, but we could do return or LP list the way you propose that if we would have to, I guess marshal it and then say your license in some of the form, maybe it doesn't matter. Yeah. Quick thought. Nevermind. 

**Mikhail Kalinin**
* Yeah, I see. So yeah, the, the form, which these transactions are in the response and the response is actually the same form as they are in the execution payloads structure. So the consensus way, I can understand that it doesn't understand the ROP.

**Tim Beiko**
* Anything else on the merge. 
* Okay. so I guess next step, we had discussed on the last call EIP-4488, for people who, like don't have a ton of background that EIP proposed to decrease the call data, costs. So the extra data that's sent along all the transactions, from 60 and Gas per bytes to three gas, provide them to add a cap to the maxi another, call it on a blog, as well as a stipend for, transactions with only a small amount of call data. And the goal there was, it would make roll-up transactions cheaper because, they use a lot of call data at the settle, on, on main net. there was some concern raised about, the fact that, you know, roll-ups, aren't super cheap today already, and they might get more expensive. and, this EIP, you know, is, is a fairly simple change. And we could potentially do it even before the merge, if we want to do, and this way we would kind of future-proof ourselves with regards to costs on roll-ups, I'm talking, I talked to a bunch of people this week about this, and it seems like there were a lot of varied opinions about how we should approach it. I'm not a hundred percent sure where to start, but I guess, the Geth team shared kind of their position in writing this morning. So that's maybe a good place to start from, about this. oh, I see. And Scott, you raised your hand. Do you want to go first? 

**Ansgar Dietrichs**
* I was just wondering, because I would say the position is already kind of diving into the question of, should we go ahead with the fork for this owner and maybe it couldn't make sense to people that, to just briefly talk about the, the, kind of the analysis on undone, different levels of stipends and different minor profitability, because that's more like a neutral, neutral topic before we get into the details. 

**Tim Beiko**
* Yeah. Okay. I like that. yeah. So going, you've been spending a bunch of time in the past two weeks looking at that. Do you want to give some context and share your, your analysis? I think you had a link also, I, if you want to share this, Or if you even want to share your screen as you're going through it, whatever works best for you. 

**Ansgar Dietrichs**
* Sure, sure. I can do that me like one second. let's see. Okay. Can you see my screen? Yes,awesome. So, again, this is completely separate from the question of whether this patient go ahead or not, but to just, just in general, the, the question was, there was some concerns raised around, for one that now that we have two separate constraints on blocks, basically be that there's a type one call later, and then it's still a bit of a test limit cap, that mining could become more complicated. 
* And so if you run a simple mining algorithm, like you will probably find a geth or other execution climbs where the basically you might be out competed by, minus who, or who might run close to us, sophisticated algorithms. and then as part of that analysis, it turns out that the is also interesting for the questions around, specifically like, what, basically what level of stipend allows, what level of transactions to still be included on that. 
* And so, so basically, all I did here was just, sample, logs from, from mainnet, of, of, the, like the one month, one week prior to the analysis. and just kind of like physically simulated. what if, at the very beginning of a block, you would basically always already use up all the calls of, callbacks because they're complete, of course, we just want someone to say that complex always have only use a little bit of call it. And so if we just assume like those books, they call that would just never be reached. And so in order to simulate, what happens if the quality cups reach, they kind of just added a high call that affiliate transactions in the beginning, so that the, this one megabyte limit of the FPS already used, and you can also use the stipend to, to add all the other transactions. And then I went through the transactions and similarly to just put mining algorithms either, and specifically three different ones that I went here. 
* So there's a naive strategy where you just literally do the same thing that gets us today. You go through the, to the list of transactions sorted by how much they would pay you as a minor. And whenever you reach a transactions, that's not, includable because of the quality limit. You just skip it. so that's, that's physically, that, that was part of the, the guest prototype of the patient. We did, that's, that's the one line changed. then it turned out is part of this approach that this a slight modification of this that actually makes a lot of difference. And that's what we call the pipette club strategy. But basically instead of completely throwing away that transaction, if it doesn't fit, you just set it aside. 
* And then if right on, because of the stipends, because they kind of accumulate if they are not so used to that, it, at any point you have a little bit more room in the bucket and you just go look at your bike lock and you keep that partially sorted. So it's efficient and see if any of those that you had to skip initially and now become available again. And that way you don't have inefficiencies of just throwing away connections that might be includable doing the box. And then there's the benchmark to compare that against the optimal type of, so, so for that, I just end up using it and like solver to actually type the best thing, theoretically, optimal, and then looking at the results. And so basically this is as a function of the stipend size, which, which makes sense, right? Because if you basically don't have any stipend, then you just kind of include any transactions at all, wants to call it a limited reach. And it's, the stipend goes up, of course, at some point it just doesn't matter anymore. and, as you might expect, the optimal strategy kind of like starts with only being able to include basically that those are just purely Eastern fences, initially 40% or something of blocks. And then it goes up to close to a hundred percent as your race, the stipend size. And importantly, though, why then I Eth with . Beach, especially for small stipend sizes, it's a bit, like less efficient and being able to include all the inspections, the backup mechanism, which is still very simple to implement, almost like follows this optimal, perfectly, of course in the beginning, it's a little bit below, but right. 
* Then even if you go to the small stipend size is around 200 to 305, it's, it's basically it's within 1% of each other. So basically am I know who would run the backlog, strategy would, would not have set like at all noticeably as smaller profitability from mine. And then, is a, is, was staying basically part of the, as part of the analysis. It also like happened to come up the question of, how would this EIP affect the ability for normal transactions to still be included, in blocks and especially, maybe already relevant than when the Geth teams is going to talk about that in a second, because one of these concerns that, that right there was that basically transactions about the stipend. And again, the EIP right now assessed 300, but we might end up with something like 260 actually look better, even better because it's just sufficient maybe. so that any transaction above this two 60 bytes, you can call data would just not have to compete with, very high budgeted, roll-up transactions. But then the interesting kind of result of this is that actually, because you have this accumulating nature of the stipend, right? 
* If, if there are 10 transactions and they all only use a hundred calls, a hundred bytes of data, you always get this extra one and that accumulates. And so then you can have one a bit bigger transaction afterwards. and so, because, because of the, the nature of the accumulating, stipend, and actually even at say something like two 60, the backlog strategy lets you include over 99% of all transactions, within the next block that they can usually would, would end up in any way. And that already includes roll up protection. So like really big college transactions. And of course those, those, I mean, those would be the ones in the front of the book, but not the ones that have to compete in the back of the book. 
* So, it basically, if you exclude those, that means that all normal sized transactions would still be excludable SMO with, without any issues. And, I did look into the just now there's a bit more and basically found that two 60 specifically the median size of, of like the exclude, the transactions here was something right. 2,400 bytes, so that it gives you appealing for like really only these very big transactions would have, would basically have to now compete for these potentially more expensive parts of the block and everything else can just be included as normal. So I would say these kinds of consents, probably like, and ended up not being an issue with the EIP. but yeah, the enough other contents to, to, to continue talking about. But, but I think that that's all I have to say on this. any specific yeah. Specific questions, comments, Peter. 

**Speaker 01**
* Yeah, I do have a question. So, with this whole backlog mechanism, the ideas EIP is simple, but, it's, what's an interesting problem that can happen. Let's say that I have at the, I fill up the block space, visual loss, and then I have a high paying, but high guests use, sorry, high space usage transaction. Let's say I have a transaction action, which pays a lot of money, but it requires, say 10 kilobytes worth of data. And I have smaller transactions that are cheap, but they require, let's say only 500 bytes. Now, if I go with this backlog approach and what will happen is I will keep adding tiny transactions up until the point where I pre-op 500 bytes space. And at that point I wait to see that, oh, I have 500 bytes. I can shove in one of the more expensive transactions, but I will never actually consider the super expensive transaction because the super expensive one is eight kilobytes. And I'm never going to have that big of a gap because there will be always something smaller that will just gobble up that space. So it doesn't it's. So my, what I'm kind of afraid of is that, the deploying a contract will become this crazy expensive thing because it's going to be a lot for data. So you cannot use this backlog hack to just, stash it in somehow because you will always have somebody else will be, can use the function and the roll-ups will, theoretically for all us become popular, then we'll apps will consume the block space and they will have significantly more funds. So essentially if you want to, for whatever reason to deploy a very high Geth of certain, very high space using transaction on layer one, then you're going to get the big, not the big a loss. 
* Well, doesn't that just mean that the contract deploying transaction has to compete fairly with the roll-ups for clock space? Yes. Like, I guess I'm wondering why this is a problem. They might have to pay a little bit of a tip to get included with roll-up transactions.  I'm not of, I also mentioned this on the little document that you wrote down. I don't necessarily consider this a problem. This is just a rebalancing that people need to be aware of. So people need to be aware of that if we implement it 4488, but actually deploying contracts on level one will cost an arm and a leg, even though even now it costs an arm. So it's, it's going to potentially, it can make it more,

**Felix**
* Well, we should have been a bit clearer about this, basically. It's not. also there was, this, this point was also raised, about, it's maybe not written in the best way right now in the opposition. So basically the, it's not so much that there is no, you know, that, you know, like it's, it's, it's, it's not, you know, generally unfair that, you know, like big transactions have to, compete with other big transactions. It's more than because there is this limit, then, you know, like it's kind of like, it shifts really like, you know, sort of, you know, like what, what can you do kind of really depends on if your problem fits into the limit or not. We think that's just kind of something that, yeah, it may not be intended or I don't know, we just want it to highlight it because it wasn't really highlighted in the EIP was like one sentence or I don't know. 

**Dankrad Feist**
* Oh, so I guess in practice, what it means is that, con transaction with large call data might have to pay a bill for two, right? 

**Felix**
* That's the practical, They will be. They will become more expensive is what Peter is saying. 

**Dankrad Feist**
* And just, Well, I mean, but they also do profit from lowering of the call data, right? So bill, they become more expensive than now. 

**Felix**
* It's not For us. I think the main, we are not really trying to stress this point too much, for us it's like the main thing is we are just really, I can just, you know, summarize it really quick. So we are just afraid of the two dimension nature of this scheme. And this is the sole reason why we are complaining about, we feel that, you know, like there are, there can be like unforeseen consequences from that. And, we are trying to basically stress this point because we feel like, you know, it's already like, you know, something where it took us a bit of kind of figure out, you know, like what are the consequences of the scheme? it's just paper safety steering to formula and discussing. We kind of figure that, oh shit, you know, it's actually gonna mean that, contract deployment is gonna, you know, it may cost a lot more or, you know, it's, it's just, it's in a different, it just means you have to think about it like a lot more. We were just worried that this is, you know, like the status change. It's not really like, you know, super, it's not super clear what's going to happen. Like, I mean, obviously you guys are researching it right now, so, you know, I guess eventually we'll be, we'll be very clear what what's going to happen. 

**Dankrad Feist**
* Yeah. I mean, that's fair. I think as a practical comment though, we need to be also aware that the consequences of having roll-ups in practice means that it will always become more expensive to use the layer one itself because the roll-ups are just more competitive. Right. So roll-ups just make much more efficient use of it. So in, in the ultimate end game layer, one transactions will become more expensive to, to that, but I think that's okay. You should use all apps essentially. 

**Peter Szilagyi** 
* One counter argument is that the prolapse are so much more efficient than why subsidize them even further. 

**Ansgar Dietrichs**
* It given that this is already drifting into the moment of that kind of substantive substantive discussion on whether, like, if it makes sense, I'm not just, I want to just very briefly say this as well, that on like the, the specific aspect of this two dimentionality, book space constraints now, I would probably frame it a little bit, kind of like the other way around where currently there is no protection of say quote unquote, normal transactions against roll-up transactions. So as we were talking about like the very long term scaling a plan for Ethereum is for everything to move to roll-ups. And so like in the long run it, the e-tron execution will be more and more just roll up management. Of course the question is how long that'll take, but basically at some point it works start to just be full of roll-up transactions and that can already happened without this EIP. normal transactions would be more mild competed. the, of course the, the kind of the saving grace is that right now it's so expensive that, maybe roll up it up a little bit slow and we still, we have more time. Whereas if we introduced this EIP, it becomes cheaper. 
* And so roll up at option might speed up a little bit, but importantly, I think this is, again, this is what I would kind of want it to say is importantly, we, this , I understand it as a protection mechanism for not much sections because now With the call with the call, it alignment and B the second mechanism, basically the, once we reach the level of adoption for roll-ups, where they feel a significant portion of each block, they're basically limited to the first, like two to some part of the block with the EIP because of this call data limit. And so the rest of the block would be left untouched for normal protections. Whereas without the epi, if we don't increase the EIP, once we reached those adoption levels and basically not, the transactions just become completely unbuyable because all members would actually have to compete with road transactions. So it's physically once reach production without the EIP thing that we will be in a much worse state for normal transactions. That question is just might be a piece like, speed up adoption so much that on, on, on that it's still, it's still a benefit, but I think the EIP itself is better much of like a helpful, phenomenal, transactions. 

**Felix**
* Oh yeah. Thanks. 

**Tim Beiko** 
* Vitalic, you have your hand up. 

**Vub**
* Yeah. And I think one point I wanted to make on the economics and just on the issue of like, well, you know, if a roll ups are supposed to be cheap, one of these generations here is that there's a difference between like the first cost of data and the possessive cost of data. Right. And right now the small data gap has got scar primarily state-based, but based on the burst cost of data, input data. If we had 10 times more data than worst case blocks to really break that perspective. And the long run roadmap is that there's going to be this a dedicated data availability space. And I was like, there's going to be shards to hold this data. And so data more dense and like weird wild execution markets are going to be more separate. And that would actually like basically allow the cost. It would allow the, it would mean that the actual constant call data imposes on the network is much more based on what the persistent cost is because like there would be a target for layer one execution, and then there'll be a separate target for whole data consumption until you wouldn't have this much, this much volatility. So I guess like one way to another way of getting at this is basically to say, well, if right now from a burst active call data is priced correctly. But from a persistence perspective called data is overpriced. Then adding some kind of two dimensional limit basically is the way to make it more correctly priced from Asia, from Asia persists that perspective without mispricing it even more from a  burst perspective. but then of course, it's like, we have to ask, like, what should have like, well, like if we only care about the persistent issues, then, like, what would the correct, I guess, cost default data look like? and you know, what would it look like in the context of the EIP for 4441 when it's going to happen and all of these things. but like basically like one way to just the, otherwise they'd be economics of difference, but just start by asking the question of, if we only cared about burst issues, what would the , be if we only cared about persistent issues, what would the limit be? And if those two are aligned and that the message that the misalignment just needs, that there's a lot of applications that could run without verdict things, not being run through that. 

**Peter Szilagyi**
* It makes sense to try to shepherd, I guess, one thing that we should also consider. so if we just stayed at the costs and seeing about with sharding, the cost will be a lot better aligned, and so on. so one, one thing that is kind of bothersome about EIP we assign activities is that I of says about, 4444 will fix the stable problem. And, and that's, eventually I'm. So the advocate have said that portfolio should be accurate at the same time or soon thereafter. And this seems like a super hand wavy approach to drop two terabytes of data on the network every year, because it's not obvious how 4444 will be. It's not obvious one. If we start saying we deploy 4488 next year, early next year, then we, okay. Now we, again, have to make a decision. We will do admin clients for Southern focus on 4444 to avoid the chain growth issues, or do we focus on the work? So again, we, we just opened up some next set of problems that we. 
* So to avoid the chain growth issues or do we focus on the merge? So again, we, we just opened up some next set of problems that we need to solve. And, I don't know, at that one point is this whole capacity worth it to delay the merge so much, we're going to be more meaningful to push through the merge. And then we could focus on these ones. And especially, I guess if the merge is done, then Eth two clients can actually focus on sharding. And the old two things could somehow progress concurrently because I guess the ideal solution is for all of the raw data to be on the shards. So shouldn't, we rather focus on getting the shards up and running as soon as possible. 

**Felix**
* Yeah. We didn't really want to mention this in the document, but that is kind of like one of the things that like, if we, you know, are allowed to make like very far ahead sort of planning suggestions and we kind of feel like, you know, ultimately the place for roll-ups is, you know, shards. 

**Martin Holst Swende** 
* Yeah. Well, the thing also that we then add in this document, the change proposed is from 16 to 3, which is a pretty drastic change. normally I think historically when we like change some protocols, but maybe to change it to them in two X or 1.5 X or something, but this is a, it's a very large change. and one go. Yeah. 

**Ansgar Dietrichs**
* And just, just briefly on the question of what motivation, I think you were saying about, like, you think long-term shards should be the correct way to, to increase data throughput. And I think, that we all agree on that. The question is really just, do we want to incentivize the continued development of technologies that make use of this increased data throughput, by already giving them a little bit of that benefit in the short run? or do we want to just tell them, please continue developing this even though right now it's economically a little bit iffy because the long run it will become cheap. And I think that's actually, I don't, I think that's a good question. I don't, I don't think either, either one of those options is necessarily the better one, but I do think that, it make quite a bit of different say optimistically sharding could arrive in two years, but that already feels optimistic. some it's maybe two years, something like that. whereas this could really show through, I think it would be on mainnet in a couple of months. And so it would make a difference for one, two years, which I think would be enough of a justification if we think it's worth it. 

**Peter Szilagyi** 
* But that's not really true. So when you see that in two or three months, yeah, it could be a mainnet, but it also requires 4444, which will most definitely not be. So, I mean, just so this portray, it just makes, it makes things cheaper. And then it's kind of up to client developers to survive until 4444 eventually hits the pipeline. 

**Felix**
* Yeah, I guess we should make a more structured approach to talk about it because some people already said in the comments, can we just go through document? we have touched on basically all points now, I think, except for layer two readiness, which is maybe a topic on its own. the thing about, the 4444, we stat, we think it's not going to be so easy to implement. And, we have been talking it through multiple times, also over the last couple of years, like how to really achieve dislike, you know, historical data pointing. And I feel like the earliest good opportunity for this would be after the merge because, the merge specifically also binds us to the which subjectivity already. So it's like when, in order to participate, in the Ethereum network, after the merge one was accepted that we subjectivity initialization. So I feel like, you know, once we're past that point, we can think about how that initialization is going to look like for, for the for the execution layer, because at the moment it doesn't require this kind of initialization except, you know, implicitly with the Genesis block, which I guess everyone is accepted by now. So it's like, we, we need to make a solution for initializing the client with, you know, as snapshot, for example. And there are so many questions as sort of like, where are they going to get the snapshot from? And, how are they going to put it to the client? These things are like, it's, it's easier when there's already like the need to do it for the, for the, for the consensus layer.I think

**Marius Van Der Wijden(M)**
* So quick question, has anyone, is anyone really pushing for this to be included for the merge still because I like, I, I don't think that the proposal itself is, is bad. It has, a lot of question marks in my opinion, a lot of things that we have to, that we have to, to, to verify, to think about, doing these large changes without, too much data is, not an option for me. especially like taking, taking a look at, can the network even handle it, stuff like this. And so like, w we're not really, at least I'm not really arguing not to include this change in the future. I'm just arguing that, we don't have enough data, to meaningfully make a decision about it. And, we have enough, stuff on the timeline already, to work on, that, that, that is not 4488. So, I don't know, like I haven't heard anyone really pushing for this, before the merge yet.

**Dankrad Feist**
* So I would still be in favor of doing it before the merge.I think like, I mean, I agree with all the technical points here, but I still think that's, the economic and the UX, like, I guess like the future planning, pushing people towards prolapse, showing that they are the future like that, that side that when basically not really discussing here is I think still by very strong, but I would still be, That is right. 

**Felix**
* That is like a political reason then, especially like, when you say, you know, like showing you.

**Dankrad Feist**
* Yes, absolutely. This is, this is political, but like, I mean how to like the community as far as I see it is in favor of doing it. So I think it's fair to it to say that they're there to address this political reason. Right. And not only the technical parts. 

**Felix**
* So we have tried, you know, not to include changes based on political reason. 

**Vub**
* I think we should open up a broader discussion at some point. I do think that this distinction between political is overrated, but it's something that's probably worth having a, a longer Chat over at some point. 

**Tim Beiko**
* Yeah. And I, I don't, I spend a lot of my time trying to gauge to stuff. I, I think there's probably like some folks who feel strongly about the merge and, and, and some who feel strongly about like the reduction. I don't think you can make like a clear case either way that like, people really want 4488 before the merge or people really want the merge before. Obviously, you know, if you ask rolled up operators, they'll probably tell you that, like the have 4488 before, and if you ask other parts of the community who are more concerned about the environmental impact or, you know, the issuance of proof of work, they'll tell you that the merge is more important before. yeah. So I think it's, it's a hard call to make, like, it's, there's definitely, yeah, there's definitely folks on both sides. and not like a clear cut. 

**Dankrad Feist**
* I mean, I'm, I'm clearly against it if it would delay the merge by a month, but I just don't see a reason why it would.

**Peter Szilagyi**
* So two options, one of them is that, I don't think it's fair to, to debate whether we should do the merge first vs 4488 first because, actually we had a fixed timeline. So I think if, if we want to include 4488 before that then 4488 needs to have a very strong case as to why it's good, why it's important enough to, to replace the existing timeline. So I think it's not, if none of them were, would have been shadowed until now, then you can debate whether which one is more important or more urgent, but once a time in certain centrally, every team, both with your monthly themes, two teams are working on towards the merge. It's a bit weird to do some outright to hammer or pushing something in between. And, but again, what I still want to emphasize is that 4488 is only addressing the, the monetary problem. It does not address any technical problems related to chain growth. And so, I mean, honestly, I would say a 4488, and 4444 should be implemented together. It's it feels like, a very disingenuous thing to ship 4488, and then problem solve. And that if the client has problems on, on actually making 4488 eight viable afterwards. So if the, if the four for ACRP itself says that 4444 is kind of needed for it, then the need seems two EIP should go hand in hand. Not, not that we should, one of them now. And then the other one, maybe next year, probably not depending on how the merge goes. 

**Tim Beiko**
* I'm not sure who had their hand up next, but Martin Michela and scar, the three of you. 

**Martin Holst Swende**
* Okay. I got quickly, yeah, Dankrad sort of delays the merge by one month. I think it doesn't the work. I mean, we did the postponement of the difficult bomb and we've done that so many times now that we can basically do it in our sleep and forget about the fork that's coming up, because we know it's gonna kind of work. but this can change. I agree. It's not like very complex, but, such a change that would take non insignificant amount of, of, engineering and test it out on the test, after having done. So, and the fork is a roll out. Maybe there would also have to be additional resources, go into checking the, the, this increased network IO, and handling and the fallout from that and seeing do the boot notes KROQ. And what can we do about that? Because the others, you know, problems that might need to be solved in all the clients. so I do think that if we were to say, yeah, sure, we want to push through 4488, in a fork before the merge. I, I definitely think it would delay the merge. definitely. That's my take. That's it. 

**Tim Beiko**
* Thanks for sharing. Mikhail, you had your hand up for a while. 

**Mikhail Kalinin**
* Yeah, I just, yeah. Quick note, probably I'm missing something, but that's, for me, like one of the purposes of 4488 is like the end goal is to reduce the transaction fees. Is this correct? I mean, by, leveraged enrolled infrastructure. Yeah. 

**Micah Zoltu**
* I don't think that's quite correct. I think the goal of 4488 is to correct a mispricing for certain op codes or certain things called that in particular is arguably mispriced because it needs to be priced on several X please. And we basically chose the simplest mechanism to price on those axes originally. And we should fix that at some point. 

**Mikhail Kalinin**
* Okay. Let's see. Cause if, if this like the end goal, if this is what we will get in the end. Yeah. That's my, like this guide of change is very important, from our opinion, but thanks. 

**Peter Szilagyi**
* But you guys are saying that we're currently in a may surprise, but essentially currently you are being 16 gas for storing data indefinitely in the network. And you want to replace that with three gas for certain data geth net in the network. That's all. Yeah, he does. You are still, you are making is five times cheaper to store that the same data to return. 

**Micah Zoltu**
* Yes. With the minor caveat that, change history, you can go theoretically on a hard drive, not the SSD. 

**Peter Szilagyi**
* Yeah. 

**Micah Zoltu**
* Purely theoretical. And I understand not all clients actually put it that way. I, I do think from a gas pricing perspective state should be priced differently from, historic data just due to the access requirements. 

**Peter Szilagyi**
* Yes. Okay. But you would argue that, you or the chains three can go on the harddrive, but let's say, in next year in December, the chain history won't be 300 gigabytes rather. It was going to be three terabytes. So while everybody wants to sync, even if their client, whatever, they will have to wait two weeks on the downloads just to download three terabytes for them. That's going. That's going to kill it. 

**Micah Zoltu**
* I'm with you on yeah. I'm with you on the 4444 needs to come first. 

**Felix**
* Okay. Sorry, Felix, go ahead. Maybe I should, I should just try and say it. I think it would be good now kind of to come to sort of a like conclusion here regarding this, because obviously we are not going to settle this today. So, we are, we have, our physician is that we think it's not suitable for inclusion before the merge. We are not saying it's not suitable for inclusion ever. It's absolutely possible to do more research and figure out the hard questions. And then, you know, like implement something like 4444 You know, there is always the possibility of including this particular ebook. We feel like the necessary work is not possible to complete, before the merge. So that is our position. Other people feel differently. They feel strongly that it should be included because it's a good signal to the community that we are committed to a future where roll-ups are much more important and this, these things we cannot reconcile these points at all. And, so I just wanted to say that basically, I think, we need to have more in-depth technical discussions about the individual aspects of this, for sure. But I'm not sure if, you know, like this call is the best venue for Yeah. 

**Tim Beiko**
* I think that's reasonable. I think this call is, has it been valuable to like highlight the different concerns? there's all, you know, lightclient has organized like a 4444 call this week. And I think, you know, we, we definitely want to keep like a parallel tracks that to like solve the, you know, the different concerns. but yeah, I agree. We can't address all those on today's call. I think we've managed to highlight most of them on today's calls. today's call, sorry. and Ansgar, you've had your hand up a while and then Andrew is going to go after. 

**Ansgar Dietrichs**
* So yeah, I think I agree with Felix. the thing is practically speaking, given that I think it's, by now clear that we won't at least decide that we will do a pretty much uh on this call and still, I would say with vendor, the holidays in between the devastating, I think the window for even if the next four weeks or so, we will be, we would revisit this and which I said we would only do if there was some very significant change in circumstances or whatever, even then it's, it might already be too late for pre-merge folks. I so just practically speaking, this means we, we, we can point to that. I just would want to say maybe a few closing remarks. One, I think it's important to say given, given that client team seem to be very concerned about the worst case, that would become a practical with this EIP. That then that means that this would generally be a concern because the worst case without the EIP is even worse. It's just that it's maybe a little bit hot out because, roll-ups needs a bit more traction to actually feel con approx county because it's more expensive, but it's only, only more expensive by a factor of five. If you'll come for a little bed of roll-ups maybe in front of forestry and business might make a difference of a couple of months, but not more. So if, whatever, what kind of like terabyte separate terabytes  growth per year is a problem like this problem would survive without the EIP, maybe a few, few months later. So we still prefer that that's, that would be number one. And number two, I think is just that I would say going forward, we should continue the discussion around the role of allcoredev in relations with the rest of the community and like what decisions should be part of the alternatives process versus potentially other venues. Because I do think that it's kind of telling, as Marius was saying, no one on this call is really very strongly favor of the EIP. I mean, I know I myself as well, like of course like the EIP, but I think the people who really, really strongly on EIP just it's very broad set of people that you might find on Twitter, who just unrepresented he at all. And so have no voice in this process. And so I'd say going forward, we should really think about kind of how our governance on Ethereum 10 ideally kind of include all stakeholders. But I think for today that is students quickly go ahead with this. So that's fine. So, yeah. 

**Tim Beiko** 
* Andrew, sorry. Andrew's had his hand up for awhile. Yeah. 

**Andrew Ashikhmin** 
* Right. So, I think, we should, definitely agree on going with,  4444 along with a 4488, or like at least commit to 4444. And from Aragon perspective, it would be preferable to do 4488 after the merge, because it's most likely will delay the merge. And, it's so, to my mind, we should start like, discussing the shape of Shanghai a little bit. So we can perhaps standard to let's say that we are going to, to, at least start investigating 4444 alongside, 4488 in Shanghai. And there are also quite a few things that we wanted to do in Shanghai. So at least we can try think in terms of the priorities, in terms of what's more important, less important, but realistically should doing Shanghai investigate, prioritize and so on. So we should start thinking about post-merge scheduling and what's important there. 

**Tim Beiko**
* Yeah, I'd definitely agree with that. I tried not to bring it up to keep our focus on the merge. I think, you know, as we start wrapping up the merge, it makes a lot of sense to start looking at what's next and what the trade-offs are. for anybody kind of interested in just like the general things that have been proposed in Shanghai, the Ethereum/PM repo and the issues section has like a pretty good list of, I think, most EIP PS that are proposed for Shanghai. So if you just look at it, there's a bunch of proposals to include X in the Shanghai hard fork. There's actually not one for 4488. So if, one of the authors wants to just create one after this call, not necessarily for Shanghai, but just so we can kind of track it there, that would be valuable. And then the other thing that's not included in that list is beacon chain withdrawals, which is mostly, which mostly has to be implemented at the consensus layer, but there's still needs to be some mechanism obviously on the, the execution layer to credit those withdrawals. and, and that's also feels like a, a pretty high priority thing. but yeah, I think as the merge kind of wraps up, we definitely need to have that conversation. And, and if people want to start kind of forming opinions and discussing that now it's, it's, it's valuable. Peter, you have your hand up. 

**Peter Szilagyi**
* Yes. I just wanted to add one small request. So essentially nothing that perhaps some of the overdraft calls is not everybody from the ecosystem who might be impacted with one or the other is present here. So we might, it's hard for us to say whether is important, sorry, 4488 is important. how important it is and we should reach out to, or maybe organize it different values. one was, I agree with the general idea that, it's, it's nice to have feedback from the outside. I think, it's very, very important if we, if we reach out for some feedback, then obviously we say that, Hey, do you, or don't you want 4488. I mean, that's kind of, I'm asking, do you want to raise the gas limit by that X or not? So the low rate, our answer is that obviously everybody wants smaller fees. So if the gas price, if you started the gas that it goes up by internet speeds, go down by tenancy, everybody's happy. so except the clients who actually have to maintain it. So from that perspective, I think it's, it's fine to take 4488 out and ask the community whether it should be included or not. But I think if, if we do that with certainty at EIP than they are, it needs to be fully software. It doesn't, you cannot just take 4488 out and in or out of the equation because the two things go together. So I'm completely fine with the community saying that, do you, or do you not want 88 along with 44? So the two together, that's a valid thing that can be debated, but it's unfair to just ask, outsiders, whether EIP should be implemented. One. We clearly know that technically it's, it shooting yourself in the foot. And obviously we know what the answer will be from the outside. Yes, they wanted. 

**Dankrad Feist**
* So the question would have, probably have to be about whether 4444 should come sooner because eventually It will have to be a committed anyway. 

**Vub**
* I mean, I think we should try and find ways to ask you that, give entity to get a clear answer of like, what sacrifices are people willing to take. So, like, for example, if the question is, would you be willing to break the UI so that like, of applications that demands, things, that demand access to receipts older than a year, if that means that two X production and roll-ups, like that's like actually a question that includes both sides of the trade-off. Like, it's not necessarily that question, but like actually saying, you know, what do you find? What do you find more important is what are we actually going to sacrifice? Cause yeah. So like, if you're just asking, you know, do you want things to be cheaper? They'll say yes. but like, if we ask the question that includes a sacrifice, they might say yes. Even like, even when they know what the sacrifice is, or they might not, I would like, sorry, one second. 

**Felix**
* I'm sorry. I cannot raise my hand. I think so what I wondering is, since I'm not often in this call, I want to say, I would really prefer if in the foreseeable future, the, or quarters would stay to be like this forum where we, as the client implementers can like speak our mind about, you know, the issues and, you know, like keep that, keep that role in basically. I mean, if, if there's a way to figure out, you know, what the community, whoever that is once then it's like really good to have that represented here. And, we can for sure discuss it, but like, you know, this, this call is I think, a forum for client implementation. It has to stay this way. 

**Tim Beiko**
* Yeah. I think that's the reason. And we can't like, yeah, it's very easy to spend an hour and a half just having like random viewpoints on this and, and, and not, you know, not, discussing like basically having client implementers kind of be the ultimate I think it terms of trade off, you know, like another saying that I'll put out there that's worth, bringing it up is there's a world where like we do the merge and then we could decide to prioritize 4488, and 4444 as a top priority. And then the trade off there is maybe Beacon change withdrawals. Right. And that's another, another case where it's like, are you willing to wait an extra six to nine months where we can change to withdrawals if we could get, you know, 4488 to out before, and if transaction fees post-merger going to validators. and I think that's another kind of, kind of world where, like, it seems like the most complicated thing for Shanghai is probably the beacon chain withdrawals. It's probably the only thing that reaches across execution and consensus layer. so maybe having like an execution layer only upgrade prior to having something with withdrawals, it means we can ship it quicker and, and, you know, focus on something like 4444, and 4488. yeah. So that's another, another trade off basically. And, one where it's like valuable to get broader input that just at the presenters, sorry. 

**Ansgar Dietrichs**
* We just want him to say to Felix, to explain, because I think it's generally true and very important that, that like this venue specifically for most difficult client teams and other technical people who to discuss the technical aspects is, is important. I would just say then that it becomes problematic mostly when we spend, start to introduce somewhat political questions in here, because then it kind of, it tries to basically take the legitimacy of the technical competence and basically just implicitly uses that to make political decisions. And for example, that's why I was just, so for example, I really liked the, the get straight up on it kind of made me feel like all the, everything that, for example, there were also aspects in there that I would call political around decentralization of roll-ups and these kinds of things. and I would say this is at least we believe we have to be careful there, because if it is the users, the legitimacy of the, kind of the geth team as the, kind of the technical steward of the ecosystem, which in a sense, it kind of, at least it's an important role there to then old political points. Then I think again, then we started to get into these progressions of here, but then if we have also faced political topics, we really need to have broad participation of other people. So I think we have to do either way either just like stay only at the T on the technical points or have a broader venue, but then also include other people. 

**Felix**
* Yeah. So I can answer to this, that, as the Geth team, it is basically in our interest to be as neutral as possible regarding all possible uses of Ethereum. And this is a view that we have always held. So, we are never to discriminate against any particular use, you know, of, of, of the system. However, we also feel that it's important, basically to, to like stand up for that and basically say that, yeah, I mean, there, for sure there will also be, applications which are disadvantaged for example, by the 4488. And this is, maybe why we are taking this kind of stand now. Like the it's not, you know, like we, we don't really know that part is more, you know, like we just kind of feel like there's, it might put other people at a disadvantage and, you know, like we would like to speak up for those as well. And I think this is okay to have as a client in perimeter. 

**Ansgar Dietrichs**
* I agree. And I didn't mean it as criticism at all. It was just politically something sometimes it could pick up, but yeah, I think, I think you'll be all right. 

**Peter Szilagyi**
* Just one more Thing to add along those lines is that, I think we also mentioned in this spec that, there is this change. That is my preferred roll-ups over using, they are one, four for normal transactions, which is again fine. So there's nothing wrong with it. And there's nothing wrong to sort of say politically prefer will ask because if we decide that in the longterm, Ethereum should go lower. So lots because they scale. And that is a completely biased estimate. I think our perspective is just important that the EIP highlights the implications that it will have for layer one transactions. It's fine. We can say that, yes, we are going to make everybody else's life more expensive and we're going to take the heat for it. That's fine. We just need to be explicit about 

**Tim Beiko**
* Cool. So I guess to summarize, it seems like we're not going to do this prior to the merge. We keep the, as the next, next thing and our focus there. there's a lot of like technical concerns raised about, you know, how to best deploy this. I know like client, you've been kind of asking questions about that in the chat than others as well. Like what do we, what do we want to see specifically, 4448 to be kind of, you know, considered more. and then there's basically the solving the concerns around 4444. so that seems like something we, you know, pretty concrete we can work on as the, you know, merge work gets gets finalized. and along with that, we probably need to start thinking, about what Shanghai starts to look like in the trade-offs there between the different proposals. if, you know, we want to include 4444, yeah, if we're to get 4444, and 4488, shortly after the merge. yeah. Does this sound generally reasonable? Peter, you have a con 

**Peter Szilagyi**
* Yes. I just want us to add that essentially 4444 is kind of also incompatible with the current, invariance of the Etherum, because currently if your promises to keep all that data, and that's a promise that we set up once the merger is done, this promise is going to get BV evaluated because once you go towards roll-ups, if you want to go towards request status, clients, witnesses, etc, this promise needs to go. So it also feels a lot more natural 4444 to be implemented after the merge, because that it's not breaking any promises, just offloading the new invariants are the new version of

**Tim Beiko**
* Yeah. And Micah had a comment about that in the chat. do we have time to discuss, basically the, the post-merger historical guarantees for data? yeah. Happy to take the last 10 minutes to discuss that. If, if, there's nothing else on, on 4488 that people want to bring up. 

**Lightclient**
* I would, do you hope that the conversation focuses on what we can do now related to 4444? I know that talking about after the merge is important, but there's also like questions that are circulating right now about what we can do over the next three to six months to make it to the 444 forces in a place that clients are happy to implement Post-merger

**Tim Beiko**
* Yeah. I, a hundred percent agree with that. It has a big dip, and it's not just like something we can decide once the merger is done. Like, Hey, we're going to do 4444, because we're going to realize there's just a ton of work. So any work we can do in advance, you know, like the biggest area seems to be like, how do we actually standardize historical retrieval of blocks? You know, you need to prototype that tested and all that is kind of beyond the scope of like the consensus changes in a way. And we'd probably want that to be, if not like fully working at the verities prototype, by the time we decide to include 4444 into a specific upgrade. yeah, so there's, there's a lot of value in starting those, those efforts. 

**Protolambda**
* Now, Yesterday during the breakout call or four first, they already kind of concluded that's there are these stops, and you could think of it, the ability to import data in a standard formats into clients, without removing the ability to surface on the current network layer, then next the, experimentation with the distribution of the data. And then once those first two points are really solid, then you convergence, removal of the current, ability to serve the data. 

**Lightclient**
* It feels like most of the feedback from the breakout session yesterday is that people are not happy with the proposed solutions for distributing the data. And the, the main solution that we discussed was chunking blocks into certain ranges that have been pruned and providing them over some sort of BitTorrent. And that would be the solution until we have the portal network fully operational. But I, and I, I just generally see those two solutions as, complimentary in the future, rather than just relying on one thing. So it feels like that's the current biggest blocker. 
* And I would like to hear any feedback on, on That or ways of distributing the data that people are more comfortable with. 

**Micah Zoltu** 
* I would mildly prefer to keep that discussion in breakout rooms, mainly because we have six minutes left and I would personally prefer to discuss, Ethereum's chain history guarantees, which seems simpler. 

**Tim Beiko**
* So what do you think the chain history guarantees? 

**Micah Zoltu**
* I mean, yeah, So yeah, I'll send it up real quick. so right now, are you think chain history guarantees is basically that, for a client to be, you know, a correct clients and not all clients are, you should be serving change. You should be saving all of chain history and making it available to your users. And over gossip, the, this is not a sustainable strategy indefinitely. it is a sales strategy for some period of time and different people believe this full, last different amounts of time. And so the question is, is post-merger, can we change that guarantee and say that there is no longer a guarantee that Ethereum's chain history will be available forever. At some point it may disappear. It may disappear from some clients, but not others that may disappear from all clients. It may disappear from the face of the planet. we are not guaranteeing that if you want to keep that data, you can guarantee it some other way in some other mechanism. but the Ethereum clients, that's not their job. Their job is no longer to guarantee the chain history will be available forever. And so the reason if we can make that assertion and say, say that, and we agree that is a thing that we want to say going forward. Then it opened up up a number of doors for us. but we really need to tell users this far, far, far in advance of actually doing it long before we actually start dropping chain history, we need to make sure users are aware of it. So Daps need to stop using chain history as like their storage mechanism. Then like layer twos, like use their chain history as storage. Like that is how they do store storage and most layer twos. And so, I think with the merge and for a number of reasons, it's a good time to change that stance. And again, we're not putting a timeline on this. We're just saying at some point in the future, Chain history is no longer guaranteed by the hearing clients. You, if you want to guarantee you go elsewhere. And so I guess the first question is, is does anyone disagree with this? Is there anyone who thinks that we should continue to make strong guarantees about Chain history? 

**Felix**
* So we feel that with merge, we are already basically dropping this guarantee because the beacon chain also does not provide this guarantee. So it's like merge is of already the step where we are, you know, going away from this, you know, like history is available. We still have it, you know, formally available for the applications. But it's something that, you know, we have been working towards removing it for a long time. And I am strongly with you on this timeline to say that we should announce it. But at some point we got to make the announcement. So yeah. 

**Lightclient**
* Which part of history does the beacon chain up provider? 

**Felix**
* What I mean is that like the beacon chain fundamentally the way it's built, it's like, you know, it doesn't need all change history. 

**Lightclient**
* Okay. We don't, I didn't catch that. 

**Felix**
* No. 

**Lightclient**
* I mean, we don't need historical data for the execution clients either. 

**Felix**
* Well, yeah, but that's something that, you know, like at the moment you do kind of need it. 

**Mikhail Kalinin**
* So, yeah, for that's worse, after the merge, you don't need engine block headers to prove, that the chain is the valid one in terms of the proof of work sale, because we are on the, of stake and that uses Southern mechanisms. 

**Felix**
* Yeah. So at that point it's like basically optional. Like it's just a matter of, do you want to have it or not, and we're not going to drop it right at the moment, but yeah. 

**Peter Szilagyi** 
* Well, one thing I wanted to add is, that essentially, as far as we know other clients, or at least start skimping on, on change three, I might be wrong here, please, correct me, but I think Aragon doesn't serve, receipts and more, at least not by default, Nethermind implemented chain prunings. So you can just prove your own nodes. So essentially we are seeing that clients are leaning towards already pruning stuff that they might need, or at least making certain pruning mechanisms available by a flags and users will most probably the flags are available. They will most probably use it because, I mean, who wouldn't want the drop trail? It kicks up data from their hard drive. So it's essentially the desire is already there to get rid of all that data. And if we want to explore features that would grow this data significantly faster, like witnesses or, or roll-ups than the desire will be even stronger. So, I mean, we're going to end up in that point sooner or later. So might as well bite the bullet and do it properly instead of, interact that way, where everybody implements something else. 

**Tim Beiko**
* So it sounds like so far, everybody is mostly in agreement. 

**Micah Zoltu**
* Is, is there anybody who disagrees and we should keep these guarantees, if not, then I propose, we just start announcing to the community now that Hey, chain history is going to go away one day. 

**Peter Szilagyi** 
* I would miss a bit, however, I think it's super important for us to, to support. I mean, to have archives and to have a very strong, case on how, how we will still have some archives of that data. So it's fine to say that if your Etherum client will not have access to it, but I think, we can just say that well, it's everybody's problem sorted out. So that seems like with wavy way out. So it would be nice to also Say that. 

**Micah Zoltu**
* Yeah. Yeah. I think in my, in my mind we step one is we tell users, either in clients will want to guarantee chain history. And in step two, we probably go out and try to build something else like Torrance or portal network or whatever. And then eventually then we actually make good on our step one guarantee. that's just pragmatically. That's how I see things falling out, but I still think there's value in removing the guarantee first, or announcing the removal of the guarantee. even before we have a solution to archives nodes and all those things, but I do agree like someone should build up and that would be useful. And that'd be something that maybe even people in this room will build. 

**Peter Szilagyi** 
* So personally I think we should, as a solution, even if it's a dumb, simple solution, maybe it's just, an IPFS or whatever based solution with trend-based solution. I think it's important to have something, an idea, at least from the geth-go on how we could serve that data so that people won't be freaking out that we were just deleting the history. 

**Micah Zoltu**
* And as you're saying that when we make this announcement, you'd be more comfortable with making it, if we make it in, in the form of, if your implants were no longer guarantee chain history, however, before we removed that, we assure you that we will provide some alternative mechanism that you can use, voluntarily, but it just won't be harder that there are some clients necessarily such as we'll give them the, a BitTorrent or something like that. 

**Peter Szilagyi**
* So my personal, thing that I'm afraid of is that, we announced that that clients will not need to make it over not making history. And then all of a sudden clients will super aggressively start pruning it and adjust correct, referring to this notion that well, the promise was broken so they can just prune it. And then it will be up for the last client standing too, to keep that data before it gets lost. Yeah, it will cause an accident is what you're worried about. No, I mean the announcement, well, deep legitimacy for client Inlanders to very aggressively delete stuff and they might prematurely. 

**Tim Beiko** 
* We are already, sorry guys. I, I just see Felix has had his head up, for a while, so I dunno. Okay. so definitely continue those conversations. we can have them on, on discord, I think. Yeah. If you are listening, you know, clearly the guarantees around historical data's will change post-merge, it's a question of when and how rather than if, so, you know, I think there's a lot of th th there's a lot of, you know, room and how this can be implemented, but, it's something people should, should start paying attention to. I think it makes a lot of sense to spend time on 4444, going forward and making sure we continue to, to kind of flush that out and, you know, regularly kind of present, updates about it here, and then worth noting. This is the last Allcoredev for this year. The next one would have been on December 24th. We're going to cancel that. but next week there is a consensus layer call scheduled next Thursday at 1400 UTC. we will discuss, updates on the merge and Kintsugi you there. so if folks here want to show up there as well, the first part of the call will be, dedicated to Kintsugi. yeah, thanks a lot, everyone really appreciate also just like the tone of the discussion worth calling out. Like I know there were a lot of, strong feelings about 4488, and I appreciate everybody being respectful. I think we had like a really productive conversation and, yeah, this was a really good way to end the year, for Allcoredev as a thanks out everybody. 

**Felix**
* Thanks. 

**Lightclient**
* Thank you. 


## Attendees:
- Tim Beiko
- Danny
- Andrew Ashikhmin
- Ansgar Dietrichs
- Martin Holst Swende
- Barnabe
- Daniel Lehrner
- Fabio Di Fabio
- Fredrik
- George Kadianakis
- Giuliorebuffo
- Jose
- Karim T.
- Lightclient
- Marek Moraczynski
- MariusVanDerWijden
- Micah Zoltu
- Mikhail Kalinin
- Pooja R.
- Peter Szilagyi
- Trenton Van Epps
- Tomasz Stanczak
- Somu Bhargava
- Lukasz Rozmej
- Pawel Bylica
- Dankrad Feist
- Sam Wilson
- Alex Stokes
- Justin Florentine
- SasaWebUp

---------------------------------------

## Next meeting on: January 7, 2022, 14:00 UTC
[Agenda](https://github.com/ethereum/pm/issues/436)



