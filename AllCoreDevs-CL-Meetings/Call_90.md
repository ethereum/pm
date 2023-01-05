## Meeting Date/Time: Thursday 2022/06/30 at 14:00 UTC (10:00 ET)
### Meeting Duration: 1 hour
### [GitHub Agenda](https://github.com/ethereum/pm/issues/555)
### [Audio/Video of the meeting](https://youtu.be/Fid8hTxkRHM)
### Moderator: Danny Ryan
### Notes: Rory Arredondo
—----------------------------

## Merge and Other Client Updates
**Danny Ryan (05:51):** Stream is transferred if you can hear us in the chat on YouTube let us know. Ok. Consensus Layer call number 90 issue 555 PM Repo. Looks like we will chat about anything Merge related. Any sort of client updates you want to share MeV discussion point, a couple of discussion points from Afri and then open discussion. On the Merge, I don't have any particular action items. Is there anything people want to go over today?

**Mikhail Kalinin (06:38):** I have a couple of things related to the Merge but not directly. Something like big or that kind of thing? Yeah, so we can just go ahead right now or.

**Danny Ryan (06:57):** Yes go for it. 

**Mikhail Kalinin (07:00):** Okay. Okay, cool. Okay. So first one was the issue with Teku and Erigon on the shadow fork number seven, was a deadlock, where Teku was sending fixtures of data to Erigon and Erigon didn't respond in time and then Teku timed out of this request, and after that, Teku just stopped sending anything to Erigon and Erigon was not responding because of syncing and looking for a block. Yeah, that's a bug in Erigon and small issue in Teku. The issue related to these timeouts and whether to send again the request or not to send. I think that made a discussion with Pari. And I think we should add a recommendation to this spec. Now the spec currently says that Consensus state client may retry the call, if it was timed out, or they think it should retry, especially in some particular situation. When, for instance, CL client is syncing, and it sends the fixtures updated or new payload, and EL went offline, and for some reason, didn't respond in time and this request timed out. And CL should retry this request, once again, because it is processing the block and it wants to get the response to proceed with this sync process. Otherwise, the sync just gets stuck. So I think that's a good recommendation, in this spec it does make sense. I would also like to make a notice of this kind of thing to CL client developers so they can think about it and take this into account of how the sync process on their side is designed and how this work with respect to goals to execution. So they won't be stuck in this kind of situation.

**Danny Ryan (9:22):** Got it. Can you open up a suggestion in the execution API's along with a detail of the scenario so that we can read a bit more on it?

**Mikhail Kalinin (9:34):** Yea sure. I think I will just need the PR. It's a tiny change and that will describe this particular situation.

**Danny Ryan (9:42):** Thanks. Any questions for Mikhail?

**Terence (9:47):** Prysm currently doesn't do this, but it should not be very hard to add this. So yeah.

**Enrico Del Fante (10:00):** Just an update from from Teku side. So since this has been seen in the Teku Erigon pair, we already merged fix for ensuring that we are going to resend for choice updated no matter what. So even if we got stuck somewhere with the same (inaudible) update data, for whatever reason, at some point after a while we will try to send it back to the execution layer, even if it times out or whatever response we had in the past. We will try to ensure that we continue sending something in any case.

**Mikhail Kalinin (10:45):*8 Yea and I think what's also important is not only sending this but also if it's in process, if CL process depends on the response. So that the response eventually should inform this process.

**Enrico Del Fante (11:05):** So yeah, definitely when we receive a response we're feeding back the result to the rest of the (inaudible) modules, but we still want to have a more clear situation. What happened yesterday with regards of the sync process, probably tomorrow we will discuss it with Dimitri as well and have more analysis on what's the real root cause of the stuck on the syncing process yesterday and connect to PR ID today if we need to do something to ensure that the same process doesn't get stuck.

**Danny Ryan (12:08):*8 Thanks. Anything else on this one? Mikhail, you had another one?

**Mikhail Kalinin (12:19):*8 Yeah, another thing is, they have been a bit analyzing and evaluating the latest solid hash thing and how it's important for the network and for clients to implement and one thing that I'm wondering is, it's not explicitly specified in the optimistic sense specification. But I guess that clients agree on the exact behavior around not validated blocks and what happens. Just a reminder, not validated block according to the optimistic sense stack is a block that responded with a syncing or accepted from the outside and, what I'm wondering is the clients clients behavior, CL clients behavior, after restoring it. Will they replay this not validated blocks and will they try to resend the new payloads and the (inaudible) to CL clients for this particular blocks after the restart? I was just making this question, posting it in the chat and in the internal of discord channel that's just requesting some attention to it.

**Danny Ryan (13:47):** Yeah, not sure. I would assume they continue to insert blocks on the tip that they had not had. Inserting on the tip will either return accepted syncing or eventually valid or invalid, rather than replaying whole stretches of uncertain blocks, but I'm not sure how its engineered exactly.

*8Mikhail Kalinin (14:10):*8 Yeah I was thinking about two possible cases here. One is not to replay them at all and the other one is to replay them starting from the most recent just apply a checkpoint. So it was justified. Yeah, we're gonna assume that justified it. Every block is justified then the payload has been validated by the third of the network. So it's pretty safe to deem this payload is valid. But what happens next is up to a client of limitation definitely.

**Danny Ryan (14:48):** Does it matter, the distinction? Is there a case that you're concerned about?

**Mikhail Kalinin (14:53):** Yeah, the case that I'm concerned about is that if it's not replayed, looking in a very particular edge case, it could result in, probably in data availability issues, where EL clients, if there were a payload that isn't valid, EL clients can just drop it. And if CL tries to sync with the chain that contains an invalid payload and doesn't send this payload out to restart, then you EL never result from from visitation.

**Danny Ryan (15:35):** Assuming EL can't find those invalid blocks on the network. Is that the assumption?

**Mikhail Kalinin (15:40):** Yes, exactly. Exactly. And I think that this pretty reasonable assumption even EL (inaudible) they will not expose them to the rest of the network as a reason to ask them.

**Danny Ryan (16:01):** Right. If this node that's in some syncing state is either going to think that that invalid chain is the head for some reason, or get pulled onto a valid chain. And if they think that it's an invalid chain is the head for some reason, that means a lot of nodes and a lot of validators do and so, I think that actually, in that case, you probably don't have the data availability problem. But I guess depend on the particulars of why these invalid blocks exist to begin with 

**Mikhail Kalinin (16:40):*8 Yeah. 

**Danny Ryan (16:43):** I guess if your fork choice is anchoring you on an invalid chain, then there's a lot of nodes that are really happy about the invalid chain for some reason, likely serving it.

**Mikhail Kalinin (16:53):** Yeah, exactly. So that's the kind of probably the situation that we don't, that we shouldn't care about that much. But anyway.

**Danny Ryan (17:12):** Does any engineer have some insight on what's actually happening here on node restarts while the node is in optimistic mode?

**Paul Hauner (17:31):** So at Lighthouse we weren't trying to resend those optimistic payloads and they're not validated payloads. We might send an FCU (inaudible) updated for it when we boot but we're not going to try and replay any not validated box when we first start up again. We're just kind of keep them in node. We might send descendants for them. If we see them. P2P network or API.

**Danny Ryan (18:01):** I'm not certain this edge case would, in most scenarios result in data availability problem but if you want to think a bit more about it and write it down, I'd love to take a look.

**Mikhail Kalinin (18:20):** Ok cool. 

**Danny Ryan (18:24):** Other merge related items? Pari we have a shadow fork coming up. Anything anyone needs to know or do on that?

**Pari (18:37):** Currently, the nodes are just syncing. The Beacon Chain hasn't had Genesis yet but we aim to hit TTD around Tuesday. 

**Danny Ryan (18:49):** Great. And any update on Sepolia?

**Pari (18:59):** We have a TTD chosen. There was some hash rate fluctuations yesterday but as far as I know they've stabilized again and most, if not all the validators have already updated, so we should be prepared for the merge. Even if it happens earlier.

**Danny Ryan (19:17):** Good. Okay. Any other merge related discussions? 

**Marius Van Der Wijden (19:39):** Gray Glacier went fine by the way.

**Danny Ryan (19:44):** Yeah, I saw one message in All Core Devs about it, which was the signal that it went fine.

**Marius Van Der Wijden (19:55):** One important block on the bad chain. So less than 0.2% of hash rate.

**Danny Ryan (20:04):** Oh that's great. And major infrastructure providers, presumably fine, our exchanges, infuras, and wallets and things 

**Marius Van Der Wijden (20:22):** I don't know. 

**Danny Ryan (20:23):** Yeah, we might have heard.

**Marius Van Der Wijden (20:25):** I haven't seen anything yet.

**Danny Ryan (20:31):** Great. Okay, anything else related to the merge? Okay, are there any other client updates people want to share?

## MEV Boost
**Danny Ryan (21:07):** Okay, great. Moving on to MEV boost. MetaChris, can you give us the TLDR on the issue and what exactly you're requesting of this group?

**Chris Hager (21:23):** Sure. Hi, everyone. The TLDR is regarding the builder specs. Currently, the GetHeader request is not signed by the proposer, which means that everybody can request the current headers from the relay.

**Danny Ryan (21:40):** And getting a header, that's like a bid, right?

**Chris Hager (21:43):** A bid. Exactly. Assigned builder bid and having this open to everyone, message with the auction mechanics. So now it's turning out to be an open auction on the relay which incentivizes builders to bid low period relays and submit like incremental bids. Out bidding each other by small amounts. If people change this to a sealed bid auction, builders will be incentivized to bid on the high side. And no other builders would know about the builders about the bids of other builders. There was a lot of discussion on this GitHub issue. I can link it here again. The conclusion basically is that a sealed bid auction is strictly superior with the downside it needs an additional signature by the validator.

**Danny Ryan (22:42):** And entrusting the relay that they would not hand these out, because it's not encrypted or anything.

**Chris Hager (22:51):** Yes, I mean, this would just allow the relay to only serve the bid to the proposer. So it would, I suppose that relay (inaudible) implemented B for sure was implemented it would be superior for them on network. But there's no guarantees. But otherwise, the relays has no way of providing the bid to the proposers. Theoretically, they could still drive relays, if they misbehave.

**Danny Ryan (23:28):** Another way would be if nodes were pre registered as to what validators they have with the relay. Such that the relay would only give it to those pre registered nodes, rather than a more dynamic request. The signature only says who this thing is for and then I have to know who the Counterparty is correct?

**Chris Hager (23:55):** Yes, currently, the builder specs, there is just no signature on this request. So basically, we need to implement it this way. And this will not give the relay the opportunity to figure out if the request was coming from a proposal or from anyone else. Right so even like a white just would not help in this case. They relay couldn't distinguish, necessarily, because the relay is open to any proposer. There is no whitelisting or release for the proposers. That needs to provide the header to anyone who asks. I see Mikhail, you have your hand raised?

**Mikhail Kalinin (24:39):** Yea, I was just wondering what about the argument that's it (inaudible) the chat and there wasn't the comment to the issue about, if there will be a sealed auction. There will be a way for layers and layers to be bribed to provide this information. So what do you think about it and does it make sense to not make an unsealed in respect to this kind of vector?

**Chris Hager (25:20):** Maybe Step, you have the answer?

**Thegostep (25:23):** Yea. So maybe I have a few thoughts to contribute here. I think one of them is we should consider the design space that opens up if we have sort of an arbitrary message signing method on Consensus clients so I don't know if that's been considered before, but something like a prefixed message signing for just authentication. And then maybe, we can experiment with this sort of separately. I do think that for this question of leaking bids, it's tricky. Two things that come to mind to mention just the way that things work. Today with miners, so miners do have asymmetric information, they see all of the payloads that they receive from the flash bot system and the bids and they are trusted not to sort of use that. And if we sort of make the bids private and boost environment, it would be sort of replicating that, right. We'd be trusting the validators not to publish the bids for they're independent slots. Maybe that's better. But you know, perhaps not fully robust since they can still be sort of bribed to be used or they can use it themselves. So there's still some advantage to like a large validator pool, who's able to see bids from many different entities and then perhaps is able to beat it themselves. The final point to consider is, how does this fit with future PBS design? Does a future PBS design explicitly require bits to be public? And if so, like, maybe not, that's just the way that we should go. But I think that's still very much like an open research question. TLDR: Is there a way to like decouple, making changes to the Consensus client by just having a generic signing method that allows to build this without necessarily committing to open payments or closed payments?

**Danny Ryan (27:26):** On the large validator pool example, such an entity who is potentially also searching and as a validator, is can always beat the bids, right? Like that's, I mean, sorry, they they always have the opportunity to use their own block. So I don't know, does this change it? 

**Thegostep (27:50):** Does it change it. No, it doesn't change the ability of a single individual validator from (inaudible) whatever they wanted in their block.

**Danny Ryan (28:05):** Right.

**Paul Hauner (28:12):** In terms of an arbitrary message signing scheme. I think the challenge here is not how do we sign the data? It's more about how do we add that into the flow of producing a block so I'm not sure that having arbitrary signings scheme would help because you need to make sure that that any users can trigger requests to get assigned and all that kind of stuff. And that's probably the tricky thing.

**Mikhail Kalinin (28:40):** Yea. My main thoughts was, there is several fields in this request, right? Find record, (inaudible) the parent, hash, slot and pop key, the proposers pop key. So there could be a signature or structure containing these builds. And there's this signature may be this message and that signature may be submitted to MEV boost and then MEV boost may use this kind of, signature and data structure, sign data structure to all data from relay, so CL should just probably sign it once in the beginning of slots, or sorry, when it knows what's the header is because of the parent hash. That could work this way. Not sure if it's complicated or not. 

**Terence (Prysmatic Labs) (29:40):** I guess what my main concerns validated privacy, right? If you just have one relay and every validator respond to that relay. So that relay could do remap all the slots with the IP address. 

**Danny Ryan (29:54):** That's likely the case already, right?

**Chris Hager (24:58):** That's already the case because you'll need to get the payload and submit the signed block. So this is a call that is already mapped to the validator. 

**Danny Ryan (30:11):** Right. Micah.

**Micah Zoltu (30:16):** So I think I'm missing something here. Who is signing something so the builder block sends over the relay. Who is signing it? The builder needs to sign it, the builders already signed it? Right?

**Danny Ryan (30:30):** Well, they're signing the header, the header which is a bid.

**Chris Hager (30:36):** Exactly (inaudible) question. It would be a signature by the validator to allow the relay to know that this request actually comes from the validator only and

**Micah Zoltu (30:44):** Oh I see. So the only the validators a bid early the next validator came to the next bid, not anyone password. Yes. So to answer Danny's question earlier, the large pool can put whatever they want in their own blocks. This allows that same large pool to potentially, I guess not. Ok. So yeah, so my general feelings are that I'm not a fan of obscuring the problem. The fundamental problem here is that there is some number of entities out there who know what the set of bids are. And those people have an advantage because they can really, they can outbid. I don't like the idea of saying, of saying that we solved the problem by just narrowing the set of entities who are allowed to have that information. It just means that it's now an unfair game. So you turn a fair game of a bidding war into an unfair game where the only person who can participate in the bidding war is the relay, and that feels like not the right solution to the problem. Like I understand like, we want a bidding war, but like we're not actually solving that we're just making it so that only certain people can play. And if you have like 10 relays, let's say those 10 relays get to play no one else gets to play. And so now the game is become a relay so you can get the flow. And once you have the flow, now you can participate in the bidding war with everybody else. And if you don't have a relay, you can't participate and so you're playing underhanded. And so I appreciate the problem and the need for a salute potentially for a solution. I don't think that giving relays privileged information is the right one.

**Danny Ryan (32:32):** Yea. And the, some sort of reputation on relays...

**Dankrad Feist (32:443):** What privileged information you mean, you mean like the actual blocks?

**Danny Ryan (32:46):** Seeing the bids.

**Micah Zoltu (32:48):** See the bid so if you're...

**Dankrad Feist (32:50):** But that's literally why we have relays so that they do that.

**Micah Zoltu (32:55):** If you're a builder and you want to submit the smallest bid possible and win, right? That's your goal because you get to keep the difference. And so if you can't see the bids, but someone else can see the bids. That means they're going to win more than you because they will be able to (inaudible) their lowers, they're going to make more money. And so as the relays that we say only the relay is to see the bids. No one else can see the bids. Then as a builder, the optimal strategy is to go become a relay. Because the relays win in the long game. The relays are the only ones who win. And so builders all you have to do...

**Dankrad Feist (33:31):** The relays have a trusted role in the setup. We know that mean that's just because right now we don't have proper PBS.

**Danny Ryan (33:36):** Correct, this disincentivizes people trusting new relays because all of a sudden being a relay gives you an advantage. So it's less likely that you're more willing to work with new relays.

**Dankrad Feist (33:55):** But that doesn't seem like a relay is a trusted rollup.

**Danny Ryan (34:02):** It's also a matter of...

**Dankrad Feist (34:03):** Basically, the builders trust with their flow and the validators trust that the relays publish their blocks before then.

**Micah Zoltu (34:17):** Do the relays in the current plan, do the relays see the whole block or only the bits?

**Danny Ryan (34:22):** They see the whole block, once a block is selected.

**Dankrad Feist (34:25):** They have to because they guarantee that the block becomes available, otherwise...

**Micah Zoltu (34:29):** But they don't see it until selection?

**Chris Hager (34:33):** No, because the relay also guarantees that the right fee is paid to the relative relay needs to simulate the builder bid and keep certain guarantees so the proposer as builders could just claim whatever they want.

**Micah Zoltu (34:47):** So it's not until full PBS that we actually turn relays into (inaudible) 

**Danny Ryan (34:52):** Correct.

**Dankrad Feist (34:54):** We don't need relays anymore for PBS they will just (inaudible)

**Danny Ryan (35:02):** Right. Relays serve as like, essentially what the protocol can give you.

**Dankrad Feist (35:08):** The current trusted intermediary, that solves the absence of PBS.

**Micah Zoltu (35:13):** So if I understand your argument here, Dankrad, you're basically saying that relays are already trusted. Very significantly. And this doesn't change that in a significant way.

**Dankrad Feist (35:24):** I mean, we know that, this is not news to me. I mean, this is clear that we built this process rolled into them. And the idea is that you can have that hopefully, like trustworthy individuals, organizations take on that role, so that people actually believe that Flashbots provides this or Etherscan provides this or someone and they will actually be trustworthy enough and if they aren't, then someone who can raise suspicion that they aren't then they can be kicked out.

**Danny Ryan (36:00):** I guess the question here for me is does the discussion of open versus closed bids change, drastically change the trust assumption that we're willing to put on relay? If not, then I think it does buy you something. If it does, then it doesn't.

**Dankrad Feist (36:18):** Like I mean, honestly, the (inaudible) isn't just the bids. I mean, they see the full block, they can just, they could just. If you don't trust them to do that, they can just take all the (inaudible) that you extracted in your block as a builder, reassemble it and make it their own block.

**Danny Ryan (36:39):** Right. And thus, the trust assumption here isn't changed.

**Micah Zoltu (36:43):** I think we need to finish the conversation quickly because Dankrad is going to be different away to hear. Just falling away into the distance.

**Dankrad Feist (36:55):** Wait, oh, wait. My microphone setup correctly.

**Danny Ryan (37:02):** You thought you were using your headphones be really walking away from your computer mic. 

**Dankrad Feist (37:06):** Yes, it seems so.

**Danny Ryan (37:07):** We can still hear you though. Barely. I do want to point out in terms of, I just want to point out potential design here and and how to get the signature. I don't think it's necessarily a good idea but it is a design that we have not discussed before. Essentially when there's a register kind of validator message, which registers I think, the fee recipient, but other things can be put in there. So you could actually register another key. That's your kind of like MEV boost application key and that key could sign non consensus messages for authentication purposes. Rather than having to go into the validator client and go into, you know, a much more kind of privileged signing space on that, that validator key just tossing it out there.

**Chris Hager (38:11):** That's actually a possible approach that could be reused for other purposes. Remove additional signing. So I think I just wanted to point out one thing regarding the trust assumptions that are really it just changes the power or the transparency a little bit. So if it's a sealed bid auction, it gives the relay and the validator additional, especially misbehaving ones, additional negotiating power because they can then ask for bribes to reveal the current bids to close parties. And on the other side, it's probably leading to lower bids by the builders. So the evaluators could conceivably receive less rewards less MEV rewards.

**Micah Zoltu (39:01):** So if I understand correctly, the concern with the escalating bids is just, it's spammy right? Like if you have 1000 builders all building or even two, and they're racing each other. Can we address that similarly to how we address gas price escalation where like the replace by fee where you the next bid needs to be substantially higher than the previous one by percentage and so it's exponential pretty quick. And it will basically have a finite number of bids that can actually show up for any given block. And that would also encourage people to get in first because if the next bid has to be yours by let's say, 10%, then you're no longer incentivized to be as strongly to be last right. You want to be the first guy that bids 9% less than what anyone else can afford.

**Chris Hager (40:02):** Yes, that's also an option for well behaving relays to implement. Of course, there is nothing that can force this behavior on misbehaving relays, another thought.

**Danny Ryan (40:14):** Right. So a misbehaving relay could offer more maybe. 

**Micah Zoltu (40:27):** Misbehaving relay, I think can, it's more noticeable. So like if you submit a bid that you know, should have beaten the previous bid, and it never shows up and this happens a couple of times you notice it. Whereas if someone is if a relay is stealing bid flow and they're you know, outbidding people by just like, a tiny little bit, it's easier to mask like the relay can you know just (inaudible) how much they bid by and is they always they win coincidentally, you know, 70% of the time. And so I feel like be more noticeable is valuable, because proposals will stop giving to that relay, if they detect it. Whereas if you can't affect it, and you don't know that you need to stop giving relay you just feel like I'm losing a lot, I don't know why.

**Dankrad Feist (41:09):** But I mean, as a validator, what's the downside of like, I mean, basically I determine what I accept from the relay. I could say, Oh, I'm fine with 10% increase. I could say I wanted more granular 1% Because then I get better bids, right? Because otherwise you might be leaving 9% on the table. So like doesn't just create just a race to the bottom where validators will just decrease that constant?

**Micah Zoltu (41:43):** A race to the bottom, but in a way that is acceptable to all the parties involved, including the spam. So basically, relays will, you know, allow the race down to the point where the spam is too much for them to handle. Then they'll just say hey, we're not going to relay.

**Dankrad Feist (41:58):** I guess my concern is that like if you have a bigger part than you can handle more bids so that it's a downside for at home validators that they say like they can't handle 0.1% increase (inaudible) like professional operators can easily handle that and they don't care.

**Micah Zoltu (42:34):** Yeah, that's, that's fair. I guess. The relay isn't doing any sort of filtering before. Like a relay that is helpful to validators could do some of that (inaudible).

**Dankrad Feist (42:45):** Yeah that's true. I mean why else (inaudible) don't even need to send some bids. That's a good question. Right? Why can't relay simply send one bid exactly at the kind of point and say here this is it? And to all the (inaudible)

**Micah Zoltu (43:02):** Or at least you know, one bid every second, maybe.

**Dankrad Feist (43:05):** I mean, why does it need it? Why do you need another bid?

**Micah Zoltu (43:09):** I would assume there's value in getting one early just so you have a block prepared and you're ready? Last absolute second.

**Dankrad Feist (43:19):** Sure. Like there's no I see little value in a continuous you could say you can configure two time points but to relay you say like, I want one two seconds before and 100 milliseconds before, but there doesn't seem to be much value in a continuous flow.

**Danny Ryan (43:39):** Is that how it's designed? A continuous flow and then MEV boosts filters rather than the relay pre filtering?

**Chris Hager (43:47):** No it's (inaudible) relay during a continuous flow of incoming flux, I think?

**Danny Ryan (43:54):** And then only giving the highest bid to MEV boosts?

**Chris Hager (43:59):** Yes at the point that the (inaudible) asks yea. 

**Danny Ryan (44:02):** Yeah. Okay. So that's, this isn't an issue. The continuous stream bombarding hobbyists validator is not an issue.

**Micah Zoltu (44:13):** It doesn't mean you can't be a hobbyist relay.

**Chris Hager (44:16):** Absolutely. I mean you'd also need to simulate the bids and like it's a lot of infrastructure to run and have the data availability also get published and punished. Running a relay is really hard.

**Micah Zoltu (44:29):** Yeah, and I think that having the design in place to allow relays to compete on that. Like, how much their (inaudible) the bid increment, I think is good because it encourages relays to be beefier and stronger and better and faster, etc. Because it allows them to reduce that a (inaudible) increment which gives more validators presumably listening to them, right. 

**Chris Hager (44:59):** Yes.

**Micah Zoltu (45:04):** But put in place the infrastructure to allow competition on that front.

**Chris Hager (45:12):** I mean I think the relay utilization and performance is not the main point necessarily, it's more like the (inaudible) structure and how (inaudible) the value of the bids because we expect to just have enough caching on the release to be able to handle compartment by entities asking for bids. I wonder if it's a consideration to be closely aligned with future PBS designs where bids would necessarily be public.

**Micah Zoltu (45:50):** Yeah, we would rather we'd rather not do a certain auction now and then change that once we have PBS if we don't have to, in terms of design.

**Danny Ryan (46:15):** Bypasses and make privileged connections with large validators to send them directly?

**Thegostep (46:22):** Correct. Yeah, so that you don't (inaudible).

**Danny Ryan (46:27):** They essentially act as a relay to privilege parties?

**Thegostep (46:35):** Yeah, I think it's somewhat inevitable that even if we have some public relays that there will be private connections directed to larger validators. And the question is, should this be the norm or the exception?

**Danny Ryan (47:01):** So it does look like there's a lively discussion going on in this issue. And I think there's now a number of people that are more informed and we've kind of explored the design a bit more. Can we take this to the issue? I don't think we're necessarily going to come to a conclusion on this call.

**Chris Hager (47:20):** Personally I'm happy with the outcome. It was a really interesting discussion and it's good to have everyone's thinking a little bit about the implications. And I think it's alright to continue the conversation on the other channels now.

**Micah Zoltu (47:36):** Is there are a discord room where this discussion is happening?

**Chris Hager (47:40):** I think the most closely will be on the ETH R&D, the block construction channel. And the issue is this one here which already has a bunch of comments.

**Danny Ryan (47:56):** Cool, thank you. 

**Chris Hager (48:00):** Thanks, everyone. 

**Danny Ryan (48:00):** Appreciate that. Since we're on the topic, is there any any other MEV boost updates or discussion points for this group?

**Chris Hager (48:13):** Just let me add, I'm pleased to test on Sepolia, our (inaudible) relays available. 

**Danny Ryan (48:23):** Great.

**Enrico Del Fante (48:24):** Yea, I have a question around this because, is the activation topic. So when we should start working shouldn't start requesting the builder. So there is this discussion around waiting 10 or 16 epochs after the first execution finalization and show what we should do and with this regard and for support, yeah, so I'm thinking that on the CL side, we should just relay on the 204 response. The relayer will give us if we are asking before this delay, and attribute nothing, what do you think?

**Chris Hager (49:18):** I think we can configure our relay on Sepolia to (inaudible) produce blocks for 60 (inaudible) which will be fine. We will return 205 

**Enrico Del Fante (49:31):** Yeah, perfect.

**Danny Ryan (49:37):** Okay. Other MEV boost discussion points? Great, Afri left a comment, I do not believe Afri is here. But I'll quickly go through it. A couple of conveniences as Afri said that we should be reviewing as we move towards the merge, pulling chain configurations from GitHub, the repositories we're planning to serve as a reference and there's security implications and pull inspection third party services, which are hard to gauge. In fact, we had kind of a weird GitHub issue on a repository name change that did lead to some potential issues that were not exploited and are now patched but. So that is a recommendation from Afri. We can discuss that recommendation if anybody feels otherwise.

**Dustin (50:51):** Well, so what I would be, is the proposal to remove them simply from GitHub, or is the proposal to not?

**Danny Ryan (51:02):** He's suggesting not to dynamically pull them in builds and instead, they're used as a reference, they're used as something you can integrate into your client but not to every time you build your client have to have that dependency. I think is the suggestion.

**Dustin (51:18):** So this is my working assumption as one of the people who has been has updated these from time to time, is that nobody just blindly pulls it, that they have some kind of check, whether it's sort of pinning, some commit, whether it's with some modules or some other method. Nobody's at least shouldn't be blindly trusting before to begin with, so I'm not sure I understand the concern.

**Danny Ryan (51:50):** Then I'm not sure I understand how you're using the dynamic pull?

**Dustin (51:55):** Well, when you say dynamic...Because what I've seen Afri's GitHub issues, I don't know if there's NPR's on this yet. They are they are not limited in scope and dynamic pulls as I understand that phrase. They affect the repo, any use of the repo, so when you say dynamic pull, this is not necessarily run curl or Wget at build time per se and just accept whatever random garbage GitHub responds with.

**Danny Ryan (52:36):** Okay.

**Dustin (52:37):** There's a specific commit in say the Merge testnets or some ETH client

**Danny Ryan (52:41):** That you will point to.

**Dustin (52:42):** Yes. And to me that is and it's certainly possible to conduct down further usual methods, SHA hashes, whatever. But the point is, I don't see how at and there's certainly a risk of centralization, generically, that GitHub presents with any development approach.

**Danny Ryan (53:08):** I suppose GitHub is honoring a hash of a commit, then there's not much an attacker can do.

**Dustin (53:15):** Right. What I would suggest the open new attack surface. If there are other reasons to do this, and I know some of his previous issues have mentioned or alluded to this, for example, like just organizational issues. So maybe, you know, Sepolia or Proder while there's a proposal to say, well, maybe rather than have the sort of EL side on one repo and the CL config on another repo, to put them in the same repo. I mean, that kind of thing is a little different to me, but in terms of just pulling them from GitHub altogether, or discouraging even just kind of pinned pull as part of a belt. I don't see the value in that.

**Danny Ryan (54:10):** Yeah, I mean, I understand your argument. I something that we did see was a rename of repo, and then someone and GitHub honors redirects to the previous name or sorry, organization, the previous organization, unless somebody registers the new organization, which is clearly seems like a major issue with GitHub. But I think his abstract security implications of pulling specs from third party services are hard to gauge, probably, you know, when you start thinking about some of these weirder edge cases and the dependency on GitHub, that's probably the concern. I'm not making a claim, one way or the other on the suggestions of Afri but I just wanted to highlight them because he did put them in to the issue.

**Dustin (54:59):** Sure, and I would acknowledge that this is sort of an odd behavior, perhaps on the part of GitHub, exploitable for sure,

**Danny Ryan (55:07):** Yeah, especially if you're pointing to master. Right, rather than maybe a pinned commit. 

**Dustin (55:12):** Yes. Well, that's the other. That's the other part is that if you're not, if you're pointing to some specific commit, then this seems a little irrelevant, because it's the worst case is maybe they remove it but then the bill did fail. There's no, either the commit exists or doesn't. I mean, more broadly, I think there is an issue here but it's so it's kind of a weirdly specific fallout manifestation of what would be potentially borderline catastrophic. I mean, if the pin this on just simply network configs. I mean, there's so much else that people depend on GitHub for in terms of code and.

**Danny Ryan (55:59):** The dependencies.

**Dustin (56:58):** It seems like an odd target to me.

**Danny Ryan (56:03):** Okay, I would say when doing so, being careful, is important. Just given some of the weirdness we've seen also, but yeah, I'm not laying down the hammer on this one.

**Micah Zoltu (56:23):** I think the primary takeaway is don't use master, use a specific hash. As long as we're doing that we're mostly productive.

**Danny Ryan (56:32):** Right, barring some deeper GitHub bug or GitHub takeover problem.

**Micah Zoltu (56:38):** Even that should so if you're using gets it will actually validate the hashes for you so you can't actually (inaudible). Unless you're using just like, like raw dot GitHub user content or whatever. So I guess two things don't use master and use get don't use curl.

**Danny Ryan (57:01):** Okay, and the other thing was checkpoint sync from Infura. He suggests that we should be moving towards P2P state sync instead of checkpoint sync and providing alternatives or coming up with a piece of feasible P2P protocol and ensuring that users can provide their own checkpoints. I definitely respond to this. You know, it is requisite I think we all know to get out of band information perform in sync. Are there a checkpoint route or checkpoint state? But if you've already had to find the route from somewhere you trust maybe you might as well get the state and not add the P2P complexity. I think that's what we're kind of all operating on. But we are also probably relying pretty heavily on Infura as a single source of information rather than some sort of multi party, multi authority source of information. And I think we can and probably should do better, but I also believe that this group is still moderately bias towards not adding state retrieval inside of the P2P. I guess that's more of a response to Afri than to y'all but any question or any discussion points on this?

**Arnetheduck (58:21):** I just wanted to briefly go back to the previous one. But one thing that we haven't specified is the format of those repositories, really, we haven't documented what should be in there. We have a couple of things in there we have like a Genesis state the boot nodes. We have a deposit contract Merkle tree hash thing that helps avoid some deposit downloads, like there's a bunch of stuff and now we're adding (inaudible) to the mix as well. I think there are incompatibilities between clients there as well or at least it used to be. So maybe it's worth an effort to actually document what's in that repo and then sort of even more decreases the risk of having it in any one particular location because at least like agreed on what should be in there. And then that also helps people launch their own testnets and stuff. With all clients supporting the same thing.

**Danny Ryan (59:35):** Yeah, I don't disagree. Is there confusion or disparity in how we specify the information here or is it just not is we usually do it in the same way but it's just not a standard?

**Arnetheduck (59:54):** There's two formats for boot nodes and two formats for ETH one Genesis, if I remember right, vaguely from interrupt events.

**Marius Van Der Wijden (1:00:07):** I think that's even more it on Genesis format. Okay, I mean, these so the big ones are Besu, Nethermind and Geth, I guess, but Besu was also a bit different than Geth. 

**Arnetheduck (1:00:25):** Yeah, so like, if we move this into one repo and some it's like an obvious thing to do in the same.

**Marius Van Der Wijden (1:00:34):** The problem is that we like the different clients have different use cases and different things. So for for Geth, it's like we only need to support the hard forks basically in our in our Genesis, because we're already following mainchain, mainnet. But for other clients, they want to have a more granular approach to the to the Genesis block basically they want to enable or disable EIPs one by one, and that's why they have a different Genesis. And they needed for their use cases that they have next to Ethereum mainnet.

**Danny Ryan (1:01:36):** I would presume the more configurable format is convert is has all the information to be converted into Geth format, just from my understanding?

**Marius Van Der Wijden (1:01:54):** Kind of, probably. We don't have this EIP to to hard fork mapping anywhere in the code.

**Danny Ryan (1:02:15):** OK. So there are potentially some issues in trying to unify. Nonetheless, if somebody wants to take the charge, by all means.

**Arnetheduck (1:02:34):** Cool. To the point about states I think there's two things to point out like checkpoint sync in itself isn't inherently more or less secure than syncing from Genesis right? Unless you trust your source but I think in general, we're moving towards this world where you need to have one point of reference, like (inaudible) and SSH and then where we get states from is a bit of an open problem. What's nice about this particular problem is that once you have a hash, it's very easy to verify the data error getting. I mean, it's just dumb data. So I think one reason why we haven't really worked very hard to solve this is because we envision a fairly easy solution once, like should this ever become a real problem.

**Danny Ryan (1:03:40):** Yeah, I agree. Nonetheless, if we don't create some sort of standard, encourage a bit more adoption we will continue to rely on a single provider, which you could definitely argue the damage that such a provider can do is actually very limited but still there's damage that can be done.

**Arnetheduck (1:04:11):** Well I could use my error file plug here.

**Danny Ryan (1:04:18):** What is the state of the error file?

**Arnetheduck (1:04:22):** We actually have community members running servers to provide error files. We can also use them in (inaudible) database. So the way that we're using them right now is that we have multiple, what's called multiple beacon nodes. They can share the block storage for providing blocks via P2P using error files. So we have something like I think 12 Beacon nodes running on a server and it uses the space of one. So I would say the format is fairly good, fairly stable. I'd encourage others to take a look at it. It's there it's possible to use. I'm like always like one week away from writing in the IP actually and then something else pops up.

## Open Discussion, Research, Spec, etc. 
**Danny Ryan (1:05:42):** Alright, anything else on Afri's checkpoint sync comments? If he joins us in a call or two, we can discuss more with him. Okay, next item on the agenda, open discussion, spec, research anything else? Okay, thank you. Happy Sepolia, Happy Shadow Fork. Happy Gray Glacier. Talk to you soon.

### Attendees
* Marius Van Der Wijden
* Danny Ryan
* Mikhail Kalinin
* Stefan Bratanov
* Chris Hager
* Sean Anderson
* Pooja Ranjan
* Saulius Grigaitis
* Terence (Prysmatic Labs)
* Enrico Del Fante
* Paul Hauner
* Thegostep
* Phil Ngo
* Ben Edgington
* Carl Beek
* Hsiao- Wei Wang
* Trenton Van Epps
* Dustin
* Caspar Schwarz-Schill…
* Gajinder lodestar
* Lion Dapplion
* Andrew Ashikhmin
* Fredrik
* Mamy
* Micah Zoltu
* Pari
* Stokes
* Cayman Nava
* Mario Vega
* Arnetheduck
* elopio
* Dankrad Feist
* Viktor
* Preston Van Loon
* James He
* Marek Moraczynski
* Saulius
