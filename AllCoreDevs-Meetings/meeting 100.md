# All Core Devs Meeting 100

### Meeting Date/Time: Friday, Nov 13th, 2020 14:00 UTC

### Meeting Duration: 1 hr 50 min

### [GitHub Agenda](https://github.com/ethereum/pm/issues/221)

### [Video of the meeting](https://youtu.be/5-614J9qNvY)

### Moderator: Hudson Jameson

### Notes: Alita Moore

### Summary

## Decisions Made

| Decision Item | Description                                                                                                                                                                                                                       |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **100.1.1**   | Taking discussion on how best to implement EIP 2976 through eth 65, 66, 67, 68 to eth magicians                                                                                                                                   |
| **100.1.2**   | Micah to update EIP 2972 to say that legacy transactions are no longer valid in blocks                                                                                                                                            |
| **100.1.3**   | Return back to discussion on 2930 and discuss the SSZ lake additional encoding and prepended signature scheme -- conversation started on 2976 eth magicians thread; Lightclient is going to schedule breakout room for this topic |

## Actions Required

| Action Item | Description                                                                                             |
| ----------- | ------------------------------------------------------------------------------------------------------- |
| **100.2.1** | include wrapped transaction format if it's included in 2718 or another EIP                              |
| **100.2.2** | EIP 2718 will include wrap format under EIP 2972 and will be included in YOLO V3                        |
| **100.2.3** | James is going to update documentation regarding CFI and add a document that tracks things that are CFI |

## Helpful Links

| Link | Description |
| ---- | ----------- |

**100.3.1**: [EIP 2972](https://eips.ethereum.org/EIPS/eip-2972)
**100.3.2**: [EIP 2976](https://eips.ethereum.org/EIPS/eip-2976)
**100.3.3**: [2976 eth magicians thread](https://ethereum-magicians.org/t/eip-2976-eth-typed-transactions-over-gossip/4610)

---

# 1. YOLO V3 & Berlin Client Updates

Video | [3:20](https://youtu.be/5-614J9qNvY?t=200)

**Hudson** - All right, hello, everyone, and welcome to ethereum core developer, meeting one hundred, woohoo, that's an accomplishment of sorts. I suppose we've been doing these since well, on a cadence. We've been doing them since about January 2017 with a few before then. So this is really cool that we've been doing it this long and it's been, you know, helping a theorem. So thanks to everyone who's been attending and has kept this going all this time. The first thing we have up on the agenda is YOLO V3 and Berlin client updates and there's also some subtopics in there. So I'll have James Handcock take it over. James.

**James** - Yep, we could get a an update on isolators YOLO V two is running in. Is running, can you just give the update that you gave me an earlier?

**Martin** - sure, as far as I know, there's basically nothing happening on it, and there was a there was some happenings when me and Mariusz, so I took the YOLO V one transactions on the road around. Damarys did some resealing around the one Europea to which you had so misapplying because it turned out that they there node was you with two compatible, but it was not actually configured to use the other way to rules. After that was fixed, everything worked fine. And Mariusz did some new transaction Vector's that they played but putt on the network and everything was fine for me, the best point about it was not so much the network, but the ability to trust the clients. And I run about one hundred thousand plus test cases targeting well, doing a lot of sub-routine stuff and cross contract calls. Which heavily hits the 2929 rules. And yeah, those first test cases have been a mix of Geth Besu and open a theory which I built of one of the branches from, although I must admit I don't think it's an M. But we are looking pretty good.

**James** - Thanks for moving things along, but doing those tests, the four YOLO V three, if you just go through the clients and we talked about last week the actual list for you week and decided on, it's just like an update of where we are as far as integrating for each client and ready to sink or just where you are in the process will start out with Besu.

## Besu

**Tim** - Sure. So we're in the progress of improvement in the process of implementing the EP, we got twenty nine twenty nine point five, six and five done. We're doing twenty seventeen now. Right on. The team is doing nothing to speak to how that's going. And we're we're obviously you wanted to have that done before we get twenty nine thirty started, as I suspect by the next call you should be mostly done.

**James** - OK, and Geth, can you go?

## Geth

**Martin** - so 1265 is merged, but not in a state where it can actually be activated, but the change is in there. And once we define YOLO V three, we can just activate it from the three. One, two, one, two, three, 15. No problem. Twenty nine point nine a.m.. And the ones that we're working on are 18 and 30. And yeah, that's why we raised a few issues today on the agenda. And so once we clear out those question marks, I think we can kind of go ahead. But there are also, as far as we see it, probably there needs to be some some more agreements about the network components, like how do we communicate these transactions to go for new eth protocol or do we use the existing one? Yeah, so it's not only implementation work left, I think there's a bit of specifications that need to happen.

**Micah** - Sorry, I think there actually is a spec for that. I totally forgot that that needs to be included if we're going to include 29 or 27, 18, although we find it for you.

## Nethermind

**Tomasz** - 2565 we've compiled the libraries have to connect them. Apart from that, it's just the gas price change not a problem to. 2315, so we already have it, I believe. So this is subroutines, right? Yeah. So we have subroutines all tested based on the systems that we had before. Twenty nine. Twenty nine. So I implemented that overnight and I'm ready to test. So I want to try to synchronize with all of these three when you're ready or if ready. Twenty seven Eighteen similar. Yes.

**Martin** - So I don't know if you know but the demitry regenerates the state test with the two definitions so if you on the Burlington's you can get pretty good coverage of all the 2929 stuff.

**Tomasz** - Ok, that's perfect. So we'll use it after the call to to test if everything behaves as expected. Thank you. Twenty seven Eighteen, I have the same feeling as, as Martin mentioned that I'm a bit confused about how it touches the network. So wait for me specification on the networking. Also a bit of the how the legacy transactions will behave and how we actually decode from from this new format, because it will be like. I think it may conflict with the RFP in some situations and twenty nine thirty, so this one was probably the simplest and it's more like as long as twenty seven is clarified, that should be fine. I just need to serialisation everything else at work. So I do repopulate the access list. Just do not serialized transactions transsactions. So, OK, ready for burning on the mind?

**James** - Great, thank you. Let's get we'll get back to twenty seven, eighteen, I want to give open in and have a chance to give an update first.

## Open Ethereum

**Dragan** - basically just march toward peace for you all to be genial and all that. But yeah, we have some basically, just as Thomas said, about if we're going to if that's actually going to be much to do, this is going to be much. There's the separate entity. It is basically a different way, but taking thing that small changes that need to synchronize basically on that B and that's A. We are basically ready for YOLO V2.

**James** - So, Hudson, do we want to go into 2718 now or oh

# 1.a EIP 2718

Video | [11:40](https://youtu.be/5-614J9qNvY?t=707)

**Hudson** - yeah, like has if Micah has it pulled up let's go into it since that's kind of on topic of right now,

**Micah** - I can answer half of the questions. I'm struggling to find the network EIP I created. But the other question I can answer with a request that is outstanding against twenty nine thirty. So that PR that was put into chat once that's merged twenty or twenty nine thirty should now be twenty seven. EIP compatible. It was just an oversight and the three at twenty nine thirty I believe. There's also in the discussion link, I have some other comments, I'm not a huge fan of the current format between 2930, but this is the minimal change required just to make it compatible with twenty seven eighteen, because everybody is correct that right now it's time.

**Hudson** - Ok, so that's that's you said that's half of it is the other half, what Peter posted in the agenda is a comment.

    100.3.1 | [EIP 2972](https://eips.ethereum.org/EIPS/eip-2972)

**Micah** - The other half is there's three halves sorry, so the second path is for legacy transactions, here is the EIP. Oh, thank you. No, I couldn't find that. So the one I just posted, 2972 is a proposal for wrapped legacy transactions, which we could, which I do think we should add at some point, but it is not critical to add right now. The separate question is, well, if we're not doing, how are converting between legacy and. I mean, let's take a step back, so there's there's two things to do with legacy transactions. One is the thing we need to do right now, which is when you get a legacy transaction, you need to. Oh, sorry, sorry. My head is in 1559, so I've been thinking about that all day. OK, so like I said, transaction's for now, we don't do anything with them. They're normal. They're just like a transactions. They have the first bite for legacy transaction will always be in the range C zero to C to F. I think because of the way our codes are least it always uses the basically the height those hibbits and so we don't need to worry about it. Conflicting with that. Twenty seven, eighteen transactionally. Twenty seven eighteen transactions are defined to always be below the C0 I believe. And that I think is specified in twenty seven eighteen if I'm not mistaken I'll check. Might be in the rationale section. So if someone missed it I do not blame them. Yeah. So legacy transactions will always start with zero X c0 or greater and twenty seven eighteen transaction types only go up to seven F so there is no possibility for conflict, which I believe is Pieter's issue. Is that correct?

**Peter** - It's that we have actually two ways of I think we have the legacy transactions, which is just whatever we have now without any encoding. And the EIP also mentions a draft version where you prefix it with, I don't know, zero or one or something.

**Micah** - So that's EIP Twenty nine seventy two. It doesn't have to be part of Berlin. If we don't want it to like in the future, we might want that because it gives us some consistency around transactions in the network. It makes signing tools easier to write, but it is, it is not necessarily required unless we want to. Is that something people want.

**James** - Can you specify what you mean by it or do you mean format part, yes.

**Micah** - Twenty nine. Seventy two. Basically, it just takes legacy transactions, retains the same signature format. So the signature will be backwards compatible, but gives them a new format for when they're included in a block or when they're included in a gossip or whatever. And so we can have consistency within a block or consistency within the network protocol. If we think that's valuable thing to have. I would I think it's nice. I would definitely be in favor of including twenty nine seventy two along with Yilu. I just have been pushing it because it seems like we've been really struggling to get Berlind out. And so I haven't. I want to add more to the plate of people. How about the twenty twenty nine, seventy two is the IPA for that?

**Peter** - Ok, so the reason I brought it up is because I think it's that maybe it's important in twenty seven, eighteen or whatever is the original one to specify the legacy transactions are untouched in any way, shape or form, way, shape or form. And then the second the EIP. I think that's a valid debate, honestly, long term. I think I'm also in favor of including it just because it's we have two different representations. However, I think it's also super important. So I haven't read the EIP because I haven't seen it until now. But one super important part is to to somehow avoid any ambiguity, because the problem, the legacy transaction is that even if we added this extra wrapping around it, there's no signature. So from a perspective of draft version or a non draft version is essentially the same thing. It's cryptographically the same. So why do you include it in the block? We need to define which version will be included in force. So you can't rely on clients trying to figure out whether it was originally for that.

**Micah** - So right now I believe when you say included in a block, are you referring to in the transactions routes and then therefore the Mercal trade associate with that? [yes] So the when you get a batch, what you can do is look at the first bite and if the first bite is C0 or higher than it is a legacy transaction, it's the first bite is zero to seven, then it is a type transaction you can use to type. So you think of the that type bite is still there and legacy transactions, it's just like it's a range because of the way RLP encodes down to that first bite is always going to be something big.

**Peter** - So I'm talking about the wrapped version, so as far as I understand, there was a suggestion to have legacy transactions. Also having this zero prefix.

**Micah** - Yep, and that would be the twenty nine seventy two, and if we decided to include that and leave legacy transactions included in the blocks apart of. So it's a little bit of a story around this. If we include twenty nine, seventy two, we could choose to, in a hard fork, say that legacy transactions in their historic legacy format are no longer allowed to be included in a block, and only the wrapped ones are, in which case we wouldn't have to worry about anymore. And like I said, I'm told that if that's what everybody else wants, I think that's very reasonable.

**Peter** - So in my opinion, that would be a hard requirement otherwise. So the problem is that clients are free to represent legacy transactions however they want within their code base. So in my opinion, it would be super easy to mess up where so you can have transactions coming from the network from a block from RPC. And it it's super supersensitive if you can actually push them into a block into content format and do different ways, because I'm certain that somebody or extra I'm certain every client to mess it up somehow and just not use the correct volume on this. That's why I would really be happy having only one format for it.

**Micah** - So right now we have a single consensus format, assuming we do not include twenty nine seventy two legacy transactions, really one for them there is no other. There's no wrapped way at the moment. If we decide to include twenty nine seventy two, then I agree with you that I think it would be wise to say the old format, it is no longer allowed in and maybe even not even not allowed to be broadcast over the Peer-to-peer network. I understand that's a little bit more complicated because you can have multiple versions live on network at a time. But yes, I think I agree with you. It's just up to the group whether we want to do twenty nine seventy two right now and make it that hard switch today or do that sometime in the future.

**Martin** - So can I just clarify for basically my own understanding? If we were to do it as Peter says, then when we put together the transaction root, we don't have to make differences between this type vs that type we just put the type and then we put the encoded transaction into the hasher. Whereas if we do it, like currently specified, we would have to look at the transaction type, see, oh, this is old type transaction do it just hash the RFP or alternatively concatenate a byte with the RFP that like the core of it.

**Micah** - Yeah, I believe that's the core of it. Yes. So if we, if we include twenty nine seventy two then everything is a type transaction that's in a block. If there's a transaction to block it is a type transaction just flat. We're done. There are different types of transactions. There is now the twenty nine thirty type and there's also the wrapped legacy types of the twenty nine seventy two type. And so you'll still have to do the code for twenty seven eighteen for just distinguishing on type before you decode the rest of it. But everything would be a type transaction if we went with twenty nine seventy two and followed the thing that Peter just described

**Martin** - would and I also have not read this of you were talking about, but it sounds like it could, couldn't that one be good in twenty seven eighteen be updated to include that and make the specification more so order.

**Micah** - Originally we did include twenty or seventy two and twenty eighteen were one thing where twenty seventeen defined the structure. So the new type transaction structure and along with that it defined the first type transaction which was just a wrapped legacy transaction. It was split out because there are some, I believe there is some push back. So two reasons. One, as everybody knows, I'm a big fan of smaller independent EIPs. And two, there was some pushback back against that originally where people were like, well, we don't really need the raft ones yet. We could just do twenty nine thirty or we could just do fifteen, fifty nine or we could just do twenty seven eleven. We don't actually need that. And so by splitting it out, maybe we can choose to not do that. I'm still like I said, I'm still in favour of doing them at the same time we could merge them into one. I don't know if it would buy us much really, but it's a possibility. Yeah. We know that people feel very strongly.

**Tomasz** - And I actually quite strongly think that we should keep the legacy transactions and never touch them and keep them always available for the blocks as long as possible.

**Micah** - So don't include 2972?

**Martin** - as long as long as we don't I mean, we still we're still not talking about. I mean, users will have to actually sign wrap transactions they don't have to up at this point, do they?

**Micah** - That is correct. The signature is the same for the new twenty nine seventy two transactions,

**Tomasz** - as long as it just wrapped with the number in front then it's fine.

**Martin** - we're talking about that, just the different way we can shape it differently in the consensus engine, but not actually making any changes for the user.

**Micah** - So the if you were going to do that in a client then you're Jason RPC Endpoint would likely still accept legacy transactions in the legacy format and then on receipt like as soon as they received it over. That's like Jason RPC immediately wrap it internally because the signature is still valid for Raptor versus legacy. And so you could do that just on receipt and then everywhere in your code base, you could deal with 2718 transactions only if that's the easiest way for a particular client to handle it.

**Tomasz** - Yeah, well, not what I meant was if there is any transaction that's already signed but not broadcast, then we should keep it valid. So if it can be later just wrapped in a different summarization format by adding a zero in front as the type of the transaction is perfectly fine. Yeah.

**Peter** - Yeah, I guess that was the plan.

**Tomasz** - Right, yes, there is a signature remains valid

**Micah** - it's one that is a hard requirement of this 2972 was to make sure the signature remains stable between legacy and wrapped legacy. So keep in mind, we're talking about this, and I suspect we'll then move on to talking about whether this will be included in YOLO V3 or whatever, the twenty nine seventy two, as currently described, does specify a slight change in the receipt format as well, because I believe twenty seven, eighteen specifies receipts. And so just be aware that that is code that needs to be written. It should be pretty easy if you've already planned it in 2718 anyways because receipts are just typed just like in 2718. So I don't think that's going to be hard, but I want make sure it's on everybody's mind while we're talking about this.

**Tomasz** - will there be network specs for the receipts in 2718 as well?

    100.3.2 | [EIP 2976](https://eips.ethereum.org/EIPS/eip-2976)

**Micah** - So, yes, so then getting into the third half of that discussion is the link that my client gave just above to 2976..

**James** - Can I just figure out where we are in the conversation. And then like so then as far as Peter's comment, like either use one or the other, but never both. Was there like a.. so, we want rapid transactions, but we also want to so we don't want both, but is there a sense of one or the other? So far.

**Peter** - So I guess this is something that this has had multiple fronts or multiple hostile area mostly discussing at the consensus level, so stuff that's included in blocks or whatever else is this format. They are my personal vote would be to bite the bullet and just roll out the rap format and just drop the legacy format because it keeps things simpler. Otherwise, if we're going to if I mean, I think most of us would agree if somebody doesn't feel free to shut up. But I think most of us would agree that it's better to have a single way of encoding stuff than to waste. So it's probably if we want to go down the type of transaction approach, it would be nicer to encourage all transactions of typed and not have special cases. And so if you're going to do wrapping for legacy transactions in the future hard fork, we might as well do it from the get go. That would be my my initial suggestion. I don't know if there are any tools out there or daps or systems or whatever that directly poke and blocks and that would maybe not survive changing the block format. So that's a question. For example, if we do this, will ether scan can die or not? I don't know. So this is something they should accept possibly.

**Tomasz** - So you will have problems, even if we introduce new transaction time, and those tools would fail anyway.

**Jame** - So then taking a second deposit, this decision here is there is there people that feel strongly that we shouldn't have the rap format introduced at the time of doing 2718? Or is that something we can just decide here, then have the later discussion?

**Tomasz** - I'm convinced that we can do it 2972 2976.

**Micah** - So just because I would rather this come up sooner rather than later, I'm going to bring it up now. There are contracts out there that receive block proofs and those block proofs include transaction proofs and receipt proofs. And those would break and those cannot be fixed. I don't know how many there are and I don't know how used they are, but I've seen code out there that exist like people have written contracts to do this. But I guess that will break even if we just introduce a new transaction type, so.

**Micah** - This is true depending on how they use it, like if I guess there's a question of like if they can still submit legacy transactions and the legacy format, then they can still prove that transaction. They just can't prove the new transactions where if we say those transactions cannot be included in the block anymore, then they can no longer get a transaction into the block chain that can be proven by their contract.

**Martin** - So I have a feeling that. He might not hear a lot about that.. [gets too quiet to hear, then debugging]

**James** - So that would that would tend to.

**Micah** - It's one of those things like we don't know if anyone actually does this, but it is a thing that I have seen code for because I happen to work in the space a little bit and I kind of I copy some of it was used as a reference that someone else wrote on some random GitHub repo somewhere. So I know someone has written this code.

**Martin** - Yeah, that's what I was going to say or trying to say is that I think we might not hear from those people who are might be affected from this until this hits, until we actually roll it out on Ropstein, etc. Because they might not be acting, I mean, lot two people might not be active in the discussions here. So maybe we should just do it and see what happens and how bad things break and how important this is.

**Micah** - Cross our fingers that they actually test on Ropstein etc.

**Peter** - Worst case scenario, we're going to have a shit show like we had two nights ago.

**James** - So then I would say it would be good to have a little more time on on testnets to give a chance to spend a little bit longer on a testnet. And it might be better given this change. Besu and open ethereum, Do you have thoughts on including the wrapped format in Berlin and just it sounds like eventually it's going to happen, so we might as well get to it.

**Rai** - it seems more elegant. I don't really understand the the proof transaction proof contracts that Michael was talking about. I'd like to learn some more about that. But from the consensus standpoint, yeah, I think it'd just be easier to represent them with in the type format.

**Dragan** - Basically, our biggest problem is if you're are going to break something with the tooling or something like that, but for the client perspective, we are fine to share one and call it the connection.

**Tomasz** - Yes, but could we also want to talk to people, please, is EIP 1816 because they used proof of transactions. So if something changes with transactions, that might be the first one that will notice what kind of problems it causes.

100.2.1 | Video | [33:29](https://youtu.be/5-614J9qNvY?t=2009)

    include wrapped transaction format if it's included in 2718 or another EIP

**James** - So then let's say for now, that wraps, that wrapped the wrap format is going to be included if it's in 2718 or in the other EIP, I don't really care however you want. But then. Barred community members coming in, figuring out some things that it should be that it should go in and we can count that as a decision and then move forward to the next part of the conversation.

**Hudson** - Yeah, so do you want to keep it in two separate EIP or just have one?

**Micah** - I think I said before, I have a preference for separate types, I like more modular pieces that can be picked and chose, just like if we decide, for example, we need to pull out twenty nine, seventy two, it'll be easier if there's a separate eyepiece from 2718.

**James** -So we keep so we keep them separate.

**Hudson** - so that would mean you add it to the spec sheet for V3, right, James? [yep]

**Martin** - I don't actually see what 1186 has to do with transaction performance.

**Micah** - It's about to prove you're just saying it's a way to make it just a way to identify who might be doing using proofs in general. And people who are using doing like rock groups tend to also do a comparison, sort of like the same kind of ears, looking for an easy way to find people, look for people using that if you have something in them.

**Martin** - So basically, the people that would be would be affected by this is a bit of like a relay like the RPC relay or seek out relays. On the other side, you have a you want to verify that the transaction was included in a history book. So you need to get the transaction in it and then you follow the RFP and try to get the route and.. I don't I don't see any direct connection with the 11 attacks, but there might be some folks.

**Hudson** - And real quick, Thomas, you said Ncube uses it, is that the Sloggett Block Chains LLC project? [yes] That'll be interesting to talk to them then to see how they use that, whoever's talking to people about that, maybe James or Mike, I forgot who.

**Micah** - there's the third half we put off in the third half is the network letting me get to the network side of of this, which is IP 2976. And it defines basically a fairly small change to the P2P protocol. Interestingly, the dev P2P protocol was sufficiently underspecified that we actually don't need this technically, but this change makes it more clear what happens.

**Artem** - Which EIP again?

**Micah** - I think, 2976 that will.

**Hudson** - So you're saying this is something that is not necessary, but a nice to have for clarity of the client's building, right?

**Micah** - It depends on what you define as necessary. I believe so. The spec for the P2P is like a wiki page. Basically, it's not super detailed and it was vague enough as currently written, or at least as last I looked at it, it was vague enough that technically these new transaction formats were allowed only because the P2P spec didn't actually specify what a transaction was. It just said there is an array of transactions and it didn't say what that meant. But I believe there's enough clients that kind of assumed that a transaction means a certain thing. And so we felt it was valuable to more clearly specify, OK, this is what it means to be a transaction and a P2P.

**Peter** - So I think this part is kind of important because so this is something that we want to bring up, and that is because there's so the thing is that all clients currently are some, even if the spec allows it, the client implantations, assume that the transaction is this sort of the thing. And then the thing here. An interesting question is how are we supposed to support new transaction types? So any code currently running eth, whatever. Sixty three, four, five, six will drop the connection if you try to send it to one of these type of transactions. So one approach can be to back work upgrade all the protocol versions so that these fields can all of a sudden handle a transaction. So essentially we are just doing it to EIP 64B EIP 63B etc.. And that seems like not the nicest thing to do, because then you're kind of overloading the protocol version, just trying to hack this thing in. Felix's suggestion was to just roll out EIP 647 with the transaction format, which from Gap's perspective is fairly easy to do. But if Client X doesn't support a sixty three, four, five, six, then that's going to be. A painful thing to do. So it's not obvious what the best thing to do.

**Artem** - I think we should just roll out EIP 67.

**Peter** - I mean, so so the thing I just realized, there's a second problem we could roll out at 67, which supports translating transactions, but we need to change the block format, too. So all of a sudden we have a block that contains a transaction that cannot be represented on any of the path eth protocol versions, which means that not only do we roll out EIP 67, we also drop everything else. So we need to stop supporting 60, three, four, five, six.

**Artem** - And that should be fine if everyone updates. [people talk about how the last launch went poorly] see, the problem was that basically parity laws was very much behind on the on the protocol stack, very much behind the current. So that was the amount of water before. Now, I believe open ethereum it is on track to support it or to support 64. There was at least a full request to support 65. It should be fairly easy to support 66. And 67 is very easy as well. I don't believe we are as held back before as held back as we were before.

**Martin** - So I think six to six, which is I don't suppose, yeah, that can be implemented pretty easily by just pretending to have identifiers but actually ignoring them and keep using whatever method we have before 65 for a client which have not yet started implementing it. And 65 is the, you know, transaction hashes and announcement. But again, I think that's a pretty big thing, actually. I don't know what's the status on that for other notes?

**Artem** - so right now, the both in both go century and century, so our baseline is sixty five, sixty four. But we also support sixty five and 66 should be fairly easy to support and six seven as well.

**Peter** - So I guess the important thing to note here is that with the eth sixty four the thing that that defines is transaction announcements so that the network doesn't shuffle around transactions and doesn't sound the same, doesn't get the same transactions 50 times. Rather, it just gets transaction hashes. This is a bit of a special protocol version in that it's not just adding some new extra features, but it's also taking the way it's taking away the default transaction propagation where we just send it to everybody. So the complexity here is that if a client starts speaking the eth 64 without actually fully implementing it, then there's a chance that they will not get all the transactions simply because most of the transactions will be just announced that, hey, here's a hash if you need to retrieve it, and then they actually need to implement this retrieval logic. Otherwise, law abiding transaction propagation will not work for them.

**Artem** - So one option option would be to retain it, to basically surge back to sixty five and six to seven and eight so everyone could just implement sixty seven. And when they are ready to change the management logic, basically they would bring some interesting, I guess because guess what, six to seven and eight. And you still have to rebroadcast transactions to average. But it would allow for..

**Peter** - Well, yeah, but in that case, essentially, you are doing what I said previously, that you were releasing sixty three, sixty four, sixty five B so that you might as well just extend the currently running protocols. So there's not particular. I mean, that would probably possibly be less messy than the. So the thing is that if, for example, I mean, we decided we want to upgrade all the protocols. Yes, I can rule out six, seven, eight, nine, 10. But will I immediately stop talking three, four or five, six? Because if yes, then that's kind of partitioning the network. If node and things have to be cleared, so that's that's why I wanted to bring this issue up, because it's not that obvious. There are a lot of solutions. The solutions are aren't particuarly hard to do, but just we need to figure out all the implications,

**Lightclient** - what was the argument against the you know, letting the decoder decode the transaction message that comes over the wire or the block that comes over the wire.

**Martin** - Yeah, I was going to go back to the same question, because if we are changing the consensus definition of a block. Then logically is sixty three should transmit. So should use that definition. So what what do we say, I mean, what what's the benefit of having to go through all of this instead of just changing the rule people so we can change?

**Peter** - I mean, we can retrospectively change or extend the protocol. The only thing will happen is that if somebody didn't, for example, implement this and get one point out of whatever, it doesn't matter if implemented in a gap and roll it out and this new gap will send such a package to an old guy, then the connection would be immediately torn down because it's a protocol violation. But in this case, all we do is we need to ensure that Geth will not transmit any new transaction to format until the fork actually passes.

**Martin** - right, because remember, when the fork actually passes, in that case, that other side won't be able to handle the block anyway, there's no use talking to him.

**Peter** - Yeah, but then the question is, what happens if that happens? We're already passed bar for one month in the future. And and then you have a new node that is sinking. And it's for some reason it's getting new format transactions from the network from someone. What happens then? It's a bit murky. Again, we could say that while we just discarded and we don't care about the things, I mean, we don't care about all those, but. Yeah, possibly that's a cleaner approach. We just need to handle this.

**Micah** - I think Chris will correct me if I'm wrong on a client team, but I think we actually would would want if 67 to go out before the hard fought block rate. We want people to be talking it so they can transmit new transactions over the network before the fourth block actually lands. Is that correct.

**Peter** - So if you roll out as eth sixty four, eight sixty seven, then it's completely fine to roll it out whenever the problem is that when the fog arrives, you need to stop talking. Three, four or five. And I don't get that. This doesn't have such a functionality that all of a sudden at a certain block number, you stop a networking protocol. So it's not the. If things start to become weird. So that's why I kind of also see that mark's suggestion of simply baking it into the current new release protocol versions might be less invasive because then you don't need to do these versions of things during one time.

**Micah** - If I understand that that proposal correctly, it's basically enshrining the under specification that we had previously. So right now the specification just says this is the transaction message is just an array of transactions. The specification doesn't actually say what those are internally. It just there's an array of transactions. And so technically, again, this is maybe just pedantic, but technically the specification as is, is what you just described. However, like you said earlier, I don't think anyone actually implemented it that way. I think all the clients implemented it as it expects that array to be an array of very specific structures.

**Lightclient** - Well, the thing is, I remember we talked about this in a prior breakout room and I thought that was the case. But, you know, I don't know if that is actually the case. I think that most clients have one representation of a transaction or whenever they try to dissimilarly something over the wire, they use that. And so if they didn't extend that transaction type like we've done it and go area to support transaction types, all of a sudden whenever you read transactions over the wire, you're reading both the transaction types. So I don't think that clients have two representations one for wire transactions and one for, you know, operating transactions and the rest of their infrastructure.

**James** - So maybe help me.. Let's let's go back a little bit and help me understand, there's the option of we go to eth sixty seven. And then stop everything previously. Or there's this other option that Martin was suggesting that Peter is kind of warming up to.

**Artem** - So having upgraded the open ethereum before from sixty three to sixty four, that gets to 65, basically the major blocker here really is that it's sixty five. It's it was a major upgrade to to the networking protocol that required a very specific change of behavior for the clients. Basically, the clients can no longer rely on the transaction propagation on the Gosta thing, but they have to actively pull transactions themselves. This is a major implement because not just an ordinary thing, changing the way they just describe or implementing support for a new message type. It requires actually changing the way transactions. You actually have to pull transactions from the network, basically gossiping. So my idea is that we should really split eth sixty five into two parts, basically retain like the new messages in the eth 65, but still provide for the fact that the clients that sixty five, they still propagate aspects of themselves and propagation requirements in this way we could make it better and everyone else to have been.

**James** - So, just so I understand. Well what clients aren't on to eth sixty five.

**Rai** - We still have a bug in our implementation, so we have not turned on in sixty five yet.

**Artem** - Open ethereum does not have the 65 yet. Only eth 64.

**James** - OK, so then the there's developed there's more development that would need to happen for all the clients to get to whatever ends up being 67.
If we were to make that choice of implementing all of the stuff and forgetting the rest of it.

**Peter** - Yes. In that case, my suggestion is to just just use the overloading approach and not rule out any version because it doesn't make sense to start rolling out multiple versions, hacked in various ways just so that it's easier for clients to roll out. I mean, rolling it out is a bit murky, but it's still a lot simpler than that, rolling out three more practical versions just so everybody can implement whatever they want.

**Artem** - I think that everyone should implement eth 67 and then eth 68 as soon as possible, the blocker this time is maybe not the best approach to the theoretical perspective. That's not the most elegant solution, but it is the most practical and workable one.

**Martin** - Which one is the practical one?

**Artem** - Basically, it's geth is that geth will propagate transactions even with [inaudible]. If we had that and everyone just partially implemented 65 at place and be compatible so open ethereum wouldn't have to test them to implement immediately the logic to pull transactions from the network. It could just still rely on gossiping.

**Martin** - Right, but so would the just overloading methods as well. Right. because if I understood the artem correctly, he's saying that we should roll out 67 and then like three more variants so that we can have Olstein transaction behavior in a more recent protocol format. And what we're saying is that we could just use this ambiguity about what is the transaction, um, and not roll out new protocol formats. And those who have not to implement the transaction fetching can still you can wait with that if they want to. So I think both ways forward here means that no one has to implement sixty five immediately.

**James** - Are you agreeing with what Martin saying, Thomas?

**Tomas** - One idea that just just a lot of it, I'm not sure if it will work, but we can do is that during the handshake we can specify the protocol question and civilization version. It might be very strange. He would say, you know, [inaudible].

**Peter** - now, but that would still require the exact same. I mean, you would need a new protocol. So then you're ending up with a sixty seven.

**Tomas** - No, no, no, you wouldn't need sixty seven or sixty five or sixty six, you could connect to sixty three old clients and just during the handshake, tell them that you'll be broadcasting things in the.

**Peter** - Well, there's no such thing as a handshake. How do you tell them.

**Tomas** - Yeah, this would require a change of handshakes [catch 22 because 65 is handshake]

**James** - We're getting kind of close on time on spending more than I think we should on this just a heads up.

100.1.1 | Video | [56:12](https://youtu.be/5-614J9qNvY?t=3372)

    Taking discussion on how best to implement EIP 2976 through eth 65, 66, 67, 68 to eth magicians

**Hudson** - Yeah, one thing we can do is take the entire thing to a magicians thread if someone would volunteer to write up these outstanding issues. And then we can talk about it on, there would be one solution, because I don't think we're going to figure it out today until we think about it more.

**Martin** - can we consider the hashing format slash consensus format to being tied up and down the block.

**Hudson** - It sounds like that was already consensus, roughly, what are you saying,

**Peter** - yes and no, so the problem is that we've kind of decided that we would go with the wrap format. But the problem is that the EIP defines wraps format and they are interchangeable.

**Micah** - interchangeable in what way?

**Peter** - So in twenty nine seventy two, as far as I see, it defines the zero and the one type. And it just swaps the signatures.

**Micah** - They shouldn't be malleable between each other. It's basically EIP 155 or PRE 155. It's like if you were signing pretty one fifty five, so you did not include that. You're only signing over six fields, then it's type zero if you're signing over nine fields and it's type one. We basically already have two not transaction signatures. Correct, unless you resign, they are not a signature, malleable they are, but they are basically sending the same information, just one has chain ID essentially.

**Peter** - Ok, OK then it's perfectly fine. I was just afraid that they are somehow interchangeable. You can convert between them.

**Micah** - no, they should not be and if someone discovers that is the case, please let me know, because that would be a mistake. I agree.

**James** - So then is that sufficient, Martin, for answering your question. I think so.

**Hudson** - Ok, so can we repeat the for the for the note taker for the summary, what is the answer or the conclusion conclusion for that piece.

100.2.2 | Video | [58:30](https://youtu.be/5-614J9qNvY?t=3510)

    EIP 2718 will include wrap format under EIP 2972 and will be included in YOLO V3

**James** - That it will include. That the 2718 will include the wrap format under the the other EIP number, 2972. and 2972 will be added to the YOLO V3 list.

**Hudson** - then Micah, you said legacy transactions won't be valid blocks anymore, right?

100.1.2 | Video | [58:50](https://youtu.be/5-614J9qNvY?t=3530)

    Micah to update EIP 2972 to say that legacy transactions are no longer valid in blocks

**Micah** - That is my understanding from this discussion. I will update the EIP 2972 to specify that I believe right now it does not specify that explicitly.

**Hudson** - Ok, and Micha, when you're done updating that, if you could let James now just over discord so he can update YOLO V3, because we don't want to update the three before you get done with that piece.

**Lightclient** - At some point, we should probably spend some time and actually look at the serialization format of 2972, because it does include some things we talked about in the past, such as the access to the SSZ lake additional encoding. And it does have the prepended signature scheme, which I know has been a topic of discussion before.

100.1.3 | Video | [59:55](https://youtu.be/5-614J9qNvY?t=3595)

    Return back to discussion on 2930 and discuss the SSZ lake additional encoding and prepended signature scheme -- conversation started on 2976 eth magicians thread; Lightclient is going to schedule breakout room for this topic.

100.3.3 | [2976 eth magicians thread](https://ethereum-magicians.org/t/eip-2976-eth-typed-transactions-over-gossip/4610)

**Micah** - Yeah, we do need to finish that discussion. The discussion actually started on twenty nine thirty and we need to finish it there as well.

**Hudson** - If someone can just that or James or someone in chat can just point to like the magician's thread that Michael posted and the Zoom chat and post it in the discord sometime later today or next week so that we can jump start a discussion on that in there. Would that be a good place?

**Lightclient** - Should we have a breakout session for this topic? If we want to get out Berlin out quickly and the faster we can solve this.

**Peter** - Yeah, I kind of agree on that, that this won't be solved by writing on the chat.

**Lightclient** - Ok, we will get that scheduled.

**Hudson** - Sounds good. All right, so light client work with the cat herders on that, I think usually pooches organized some of them before, so that can work out their. Anything else on that that we have hanging out that or the people are concerned about beyond what's going to happen in the breakout session? Ok, I think it was good that that discussion happened because it's making it's making things a little more complicated for Berlin, but it's important that we get it figured out

# 1.2 Final go/no-go for Berlin EIPs

Video | [1:01:20](https://youtu.be/5-614J9qNvY?t=3680)

**Hudson** - So that next thing is final go or no-go for Berlin EIPs. I don't think we can do that anymore, James, because we kind of have a lot of stuff in discussion.

**James** - We can say the BLS one is out of Berlin and we can say this one is 2718 plus this, the wrap transaction formats are they're pretty much just split out versions of the same EIP. So I think that still we just need to resolve that piece, but that's like the final piece to resolve. So that's that's almost of no final, no go, go.

**Hudson** - Ok, and after we have the YOLO well, YOLO V three implement implementing all this and YOLO V three will actually be the if we find a critical thing, we can say that's out for Berlin.

**Peter** - But I do know that in order to implement this logic, you'll only be we actually need the networking thing. Otherwise, there's no way to actually send over somewhere.

**Artem** - I think we can I think we can ask the networks and 65 to stay in this place.

**Hudson** - So the networking piece, can that be a sync over text or do people think that needs that need to be included in the breakout session?

**Artem** - Let's do async first, and if we don't have a solution, anything, then, OK?

# 2. Network Upgrade Process Update

Video | [1:03:00](https://youtu.be/5-614J9qNvY?t=3778)

**Hudson** - That sounds good. All right. Next up, we have a network upgrade process update. Pooja wrote a blog post that is in progress and that they posted in the and the all core devs chat to get feedback on its in the all core devs chat. There's a thread of magicians link to the contents of the blog post. And Pooja, I think you wanted to go over just some of the high level stuff. A lot of the stuff is, are things that we have talked about and the core dev calls previously but have never been codified or written and we've just been kind of flying by the seat of our pants with how we're doing some of these procedures and stuff like CFI and YOLOs and things like that. So Pooja, If you want to go ahead and kind of do an overview and see if people have any comments and or if we can take them to the magicians form either one.

**Pooja** - So I would just like to give a quick summary of whatever the process we are actually following right now for network upgrade. So there is this document. If it is fine, I can share my screen to show them...

**Pooja** - Ok, so earlier this year, the EIPIP group started discussing ways to decouple the process of EIPIP standardization and network upgrade, the process of documenting these recommended outcomes that came out of the EIPIP meeting to make it easily available for community. We are we will be posting it in a form of blog on Ethereum cat herders. One is the part one was the EIP standardisation process that has been added to EIP one recently with the help of the merged PR so people can find it here and the process. part two is in the network upgrade process for this a repository it's created at one that also the repository. So as we see in this diagram, the first stage when a proposal is ready, ready by ready, I mean that it's like in review stage or more from the draft. So and they intend to get included in any future hard fork. They have to first go ahead and make a request and create an issue in the at once but not all triple. That would be considered for inclusion and this will be also added to the I mean, I'm just going to show how it would look like so you have to just create see if I applied once it is done, that would be added to the project board, which is available here, and the EIPs will be listed. This network upgrade process is broadly divided into three phases considered for inclusion, Devnet and Mainnet. So once it is applied for inclusion, then it moves on to devnet. CFI approved is the process when it is approved by the people here in core devs meetings. All these terms are explained in the blog. Devnet waiting room is a list of buckets in which proposals are there. People are still trying to figure out if that should be included in the developer's testnet for now we have YOLO testnet. Active is a list of EIPs which are actually being tested by different clients testing green light I think James broadly spoke about it in the meeting today and then it comes to the public testnet face that would be POW testnet like Ropstein and the final deployment phase starts mainnet phase. There is this recommendation of EIP statuses as per different phases of network upgrade. This EIP standardisation process is now separate from the network upgrade, but we highly recommend that people should be following it. The places to go for it is like for the network upgrade process and lister proposal. The best place to go is the ETH one spec repository to track the process of any individual proposals. We can go to this project board and for question answer James Hancock is the hardfork Co-ordinator; the cat herders are also supporting them so you can always reach out to us. So that's about the process. We have this eth magician forum. If people have any questions that can be answered quickly here, I'm happy to do that. Otherwise, feel free to leave questions, comments on the eth magician.

**James** - And something that I'd like to do is move so there there is a list of of the EFI meta EIP and I'd like to move that list into the specs repo. And so that it's not just the project factor, but we have like an actual document that tracks the things that are CFI. And then update the documentation around CFI to include this kind of stuff.

**Hudson** - Ok, any other comments from anybody?

**James** - I wanted to bring it up here before I did those changes so we could agree if it's a good idea or not.

100.2.3 | Video | [1:08:46](https://youtu.be/5-614J9qNvY?t=4126)

    James is going to update documentation regarding CFI and add a document that tracks things that are CFI

**Hudson** - Sounds like for something like that, I think you can just go ahead because otherwise someone would have brought up something. Thanks to Axic for being one of the early people to help try to separate this process and organize it through some meta EIPs. And thanks to Tim, Pooja, and James for organizing the post Pooja is referring to that will be posted eventually and Pooja for writing the main parts of it.

# 3 Other EIPS

Video | [1:09:20](https://youtu.be/5-614J9qNvY?t=4160)

## EIP-2938 | Account Abstraction

**Hudson** - Ok, so if that's done, we can go to other EIPs. Let's set up account abstraction, get an update and see where we're at. It looks like they're using the process already and if you go to the specs repo, you can go into the issues and see that they are already CFI applied and their request to get fully CFI. So go ahead with the update. I think who's here from Account Abstraction?

**Sam** - hey, so not too much has changed since the last all core devs meeting on the EIP, we've been trying to solicit some review. I don't know if you've noticed people made of the post on the discord Channel a little while ago. We were just wondering, anybody had a chance to look at it so far.

**Martin** - Yeah, after reading it, I've only actually managed to do the single thing. And it's a lot of complexities around it, so I'm thinking, yeah, it's going to take a while to figure out all the communications and quirks and potential ways that things can go wrong. On a high level perspective, I have no kind of obvious objection.

**Sam** - Well, that's good to hear. Is there any part that you find particularly complex or.

**Martin** - No, I think there are a lot of it that might be a bit of like of describing error states and the like, what happens in certain conditions when things don't go according to plan? Things like that reference also some other EIPs, like destructible, I have to read up on certain destructible other stuff. What happens if I run as indestructible in the unit code or whatever? Yeah, there's a lot of complex mechanics both on the EVM level and kind of how would this be used and what are the possible consequences similar to when to use them.

**Sam** - Awesome. It's great to hear that, uh, you guys are reading it over and we really appreciate it.

**Hudson** - Ok, great. Is that the end of the update sam?

**Ansgar** - I think I think that's basically it. Maybe the question would just be, is there any way we could basically effectively kind of a.. If there is any questions and in discussion you would want to want to have maybe when reading that way, what would the best communication channel there would be if it just basically once you got through all that or anyone interested so that we can we can continue discussion and on one of the next calls or something.

**Hudson** - Yeah. So because we're kind of heads are really heads down in Berlin. I don't know if we're gonna get into a lot of advanced discussion on it. I know there's a full chat channel on the R&D discord the people can pop in to with their questions. And I know that's really helpful, but because this won't be going into Berlin, it probably won't have a lot of advanced discussion, I'm guessing, until after the holidays. But I mean, we can definitely keep putting it on the agenda and getting updates and pieces of feedback. And I'm open to other people's suggestions.

**Martin** - So I was, yeah, back pedaling here, so I just remembered that I have one actual practical question about it, which would be good to be clarified. So you are overloading the nonce of a contract to use it as the kind of the norms for executing this incoming abstract transaction. And I'm wondering, what if there is the creation being done? From this contract. Wouldn't that bump the nonce as well?

**Ansgar** - yes, so we thought about that and so like from our perspective, we didn't see an issue with that. So indeed, the behavior as specified right now would be that the nonce increases both. If you if a transaction and a transaction starts with the contract and once the contract users create or create two. We thought about, like disallowing that or something. But but we didn't see any issue with actually this special purpose, because the idea of, of course, the kind of protection and transaction uniqueness would still hold.

**Martin** - I think you should mention that this is a fact. So the casual reader can think a bit about it and see if there is some action, if there might be some consequence.

**Ansgar** - That makes sense. Maybe then and then that would be the last thing on this call. But like one like connected question that we were actually having is the one corner case we have to protect against is for the contract to to to self destruct and then be redeployed. And then basically Nonce also begin at once again. And so then you could actually have the same transaction with the same hash sent again and then be included again with the same transaction, which would violate transaction hash uniqueness. So one of the options we saw were to just enforce something like the second destructible. Again, that's another independent EIP. The other option was to look into maybe changing and self-destructive behavior in into not resetting the nonce of a contract. But we just don't have don't don't have the knowledge that if that is something feasible or not, it just in case anyone on this call happens to have any special insight into that, because I do think that when create 2 was introduced, there was discussion if that was desired behavior on that. But I'm not sure if that if anyone has any any thoughts around if it would be OK to basically for self not to reset the nonce of a contract or if that would have too many side effects or something. But if there's no one with any any immediate reaction, that's fine as well.

**Martin** - I mean, it would it would change the semantics of self destruct in a way that would screw with potential like upgrade patterns or whatever. It's obvious it's not obviously safe thing to do. obviously a dangerous thing, but it's not obviously the safe thing to do

**Ansgar** - That makes sense, though, we definitely have that as like a thing to look into if we were to to to try to push for that. So that's definitely not something. Yeah. That makes things thanks.

**Sam** - In regards to AA, We do have a community call coming up on November 20th. Uh, if you guys want to join the information on the ethereum cat herder's github

**Hudson** - I think it's at noon Eastern IP and UTC, Oh, and I'm running that call, I think.

**James** - So there is also an episode of Peep and EIP the cat herders did just on this a week or so ago or this week.

**Pooja** - Yes, that that episode will be released on Monday. I will share the link publicly on Monday also the detailed information about the community will be published on Monday, providing the information how people can join that community.

**Hudson** - I think that's wrapping up just about account abstraction unless Axic you had something.

**Axic** - Yeah, I'm trying to I'm trying to say something regarding the replay protection. Certainly, as you mentioned, that's a crucial thing which has to be fixed before AA is considered and there is an EIP for the second distractible and there was another EIP for removing self-destruct and there was, I think, proposed by Aleksi, but it didn't it wasn't even merged because he abandoned it. But I don't think the setting indestructible is championed too much. So maybe Sam and Anscar, if you if you if this is a prerequisite for AA, maybe you could consider championing one of those two options.

**Ansgar** - just for clarification, I think at least the set Indestructible actually came out of this consideration. So I think that that was created by Vitalik as part of our work prior to releasing the AA EIP. So I think so basically, if AA were to move forward, that would definitely then we would also champion champion them as well. And I think there are some people in the community just asking for the set indestructible to maybe be championed even in the case that AA would not be considered just because it might also just be a nice thing to have, to be able to them basically and create indestructible contracts.

**Axic** - I wonder, did the other EIP, which just removes self-destruct altogether? I'm not sure why it was abandoned, but it would be interesting to see because this self-destruct has been like such a mess..

**Lightclient** - I think that Alexey just decided that he didn't want to pursue it any further.

**Ansgar** - I think it's one of these things like Ungas, where it would probably be nice to have, but it might break so many things, existing things, that it might just be too, too big of a change to to push for. And that's that's just my opinion. But, yeah, I do think, like, looking back, it would have been better to never introduce self-destruct.

**Axic** - But if you if you do have the time, I would encourage you guys to to look a bit more into that. And then I personally would be happy to see her self-destruct be gone.

## EIP 2666 / BLS12-381

Video | [1:20:56](https://youtu.be/5-614J9qNvY?t=4856)

**Hudson** - Ok, thanks, everybody. I think the next thing we're going to do will have one minute on EIP two six six six because it's just a really short update. And then I want to skip to the geth bug and responsible disclosure discussion from Geth, because we've had a lot of previous meetings about BLS 12-381. And there is in the agenda a link to an explainer on the, I guess, comparison between EVM 384 and BLS12-381. Twelve three eighty one from Alex Vlasov. It's the second comment down. It's a pretty good explainer. As far as like content wise, I was able to understand why teams need it and stuff like that, this pre compile curve or whatever we end up putting in. So definitely check that out. And then, Alex, if you want to talk about two six six six real quick before we go into this discussion.

**Alex** - Yeah, well, basically that was just cleaned up and merged. It's now even in a smaller scope after improved version was merged into geth to so we can eliminate repricing of VM addition and multiplication pre-compiles. We compiled just basically three changes of the constants or six right from these one hundred and sixty pre compiles. Very simple ones, just the constants. Numbers are based on what clients has provided, as their benchmarks, just like low hanging fruit to implement and give some extra performance and also kind of ensure that resources which are paid for are actually that you actually pay for resources which were actually spent.

**Hudson** - Ok, thanks for the update. If anyone has questions, just reach out on Discord to Alex and again, check out the explainer. If anyone has any comments or rebuttals to that explainer, post about them in the discord in the all core devs chat and we will continue the discussion there. So for the last six minutes, let's have Geth go over kind of what happened the other day where part of the network went offline due to a bug that was revealed in a few blog posts the other day. Martin or Peter, if you want to go ahead.

## Responsible Disclosure / Geth Bug

Video | [1:23:08](https://youtu.be/5-614J9qNvY?t=4988)

**Peter** - Sure. So before I dive into that, I just wanted to give a quick heads up here to that yesterday. So about two weeks ago, we found a pretty serious issue in go and reported it upstream. And for the past about two weeks, we are going back and forth with Google on getting that fixed. And essentially that was fixed on release yesterday into security releases for upstream go. And we also did a release ourselves yesterday, mostly to to rebuild or release a docker or launch-pad, et cetera. We go one five, one fifty dot five. I just wanted to highlight that here, too, that this is actually an important release because it can be used without those can be taken offline remotely. I won't go into details on exactly how currently I can do that maybe in two weeks or four weeks or whatever when a decent chunk of the network is actually upgraded. So anyone running geth nodes, please make sure you are running with go 115.5. OK, so with that out of the way, essentially just a quick recap of what happened, I think two days ago in the morning, essentially there was a block that appeared in the network which did a small chain split within the mainnet. Now, it was a bit unusual in that it didn't do the chain split across different clients. Rather, the chain split was only between older versions of Geth and the rest of the network plus new versions of geth and the rest of the network were on the correct channel all gets dropped off. And essentially what happened is that about one year ago we did some optimizations which introduced a consensus bug and that consensus bug was dormant in our code base for, I don't know, seven months or even more or eight months or something. And somebody reported on the bounty list that they found this consensus bug. And we've patched and silently released a fix for it. Of course, this also meant that all of a sudden, since we changed the consensus, we fixed the consensus amongst all versions of the new versions of geth were not compatible with each other, even specifically crafted attack transactions. And usually we did this a couple of times previously too, just disclosure. And usually what we do, whatever we discover one of these bugs is that we try to evaluate them, what their impact is and what the probability of actually hitting them. And this particular case, the probability of somebody accidentally hitting this block, meaning that people just using ethereum and just hitting this bug is more or less impossible. So unless you very explicitly found the bug and very explicitly crafted an attack transaction, there was no way to to abuse this. And because of that, we've decided that it's better to silently roll out the fix and just get the network to eventually eject old nodes than to raise awareness to it. Yeah. And and have a potential attack. So the thing here to know is that it's essentially a one liner. So if you announce that, hey, we have a consensus issue, this is a consensus release. And here's the one liner fixed and that's a fairly large target. That's why we try to avoid. In general, I kind of feel it that this was the correct approach to take the problematic part, which I agree, was that even though I don't think we should have announced it during the release, so I think it was a good choice to keep it hidden in people on the Internet are right that retrospectively we should have made.Actually, a really strong suggestion that there was something wrong in a previous release and people should be on the new releases, since we didn't do that, a few people and projects were using old stable releases and since infro was one of them, yeah, that kind of blew up in our faces. So that was kind of the issue. As for we've in the past couple of days, we have been talking about this on and off on essentially. What better way we could have handled it. And as I said, I I'm still convinced that it's not you can't just unilaterally say that. Hey, here's the consensus. But this is a consensus race, everybody update now, you have five minutes because. That would be extremely strange. I mean, people cannot you cannot expect people to be in front of their computers. So one possible solution that we are thinking about. It will put a bit more strain on people, but maybe that's the correct solution anyway, is to still I mean, this is something that's fluid, it's so I mean, we're open for suggestions and input, but the idea would be that. We retain the right to decide to fix issues, but we try to commit to, for example, if we do such a such a fix in the future, then let's say we release it at one date and then we could commit to revealing maybe a month later that one specific release was a consensus, containing the critical consensus fix so that anybody not upgrading within the last month, they would have somehow an emergency notification that you might want to upgrade it a bit and then maybe after one additional month, we could also simply say that, OK, this was the bug. And at that point, if anybody didn't upgrade, then that's probably going to blow up. So we this is the the best thing that we could come up with that we could do, but it does so people. One of the reasons some people are kind of really angry at us that we didn't admit that there was a consent issue and what the issue was. We are open to. To disclosing these issues, but what everybody needs to be aware of is that these disclosures will act as the same barriers every time we do one of these disclosures that is an active risk for the network and for anybody who cannot operate. So. That's essentially that's the dilemma.

**Hudson** - Ok, so we're a little over time, but I do want to have people chime in on this, especially James Prestwich, who actually added this in part to the agenda. I think you're here, James. Right.

**James Prestwich** - Hey, how's it going? Hey, so I respect the amount of work that has gone into this, especially like this week with two major issues coming out of the guest team. I think that the interesting thing about this bug that caused a consensus failure is that it was found by a downstream team and who decided to go and test it on mainnet. The optimism team discovered this specifically and tested this because they were using a stable geth release as the base for the OVM and were not notified of the consensus issue privately. Typically in open source software, there is a disclosure policy that is a specific document that says who will be notified privately how and when on a discovery of a severe vulnerability like this. And I think downstream projects like the OVM, like Celo and like other people based on geth should be pretty high up that list because we tend to use older, stable releases rather than newer cutting edge things to minimize our engineering overhead. Early notification of downstream projects would have prevented this specific instance of a consensus failure, and early notifications of major stakeholders like infrastructure providers would have mitigated the impact. I'm not saying they should go to go ahead.

**Martin** - I think it's just just totally do not agree, because you're saying it's like if we had no downstream, then we would have avoided it. I mean, if they are the ones who exploit this particular instance, I don't agree with that reasoning.

**James Prestwich** - So Downstream notified me on Tuesday night and I gave them a tear down of the bug and what it would do. But that wasn't communicated to all of the engineers. And so another person who did not have this knowledge was testing to see what would happen if the knowledge of the bug and how it worked was communicated to him. This likely would not have happened. But I don't want to get into the specifics of this kind of weird circumstance right now. You know, my overall point is that it's common to have a disclosure policy that says, you know, based on risk and based on responsibility. Who gets notified and what order?

**Peter** - Yeah, so the problem here is that, for example. This, in theory, sounds nice, but in practice. OK, let's suppose I'm going to say that, OK, I'm going to notify Infera and I'm going to notify I don't know one of the mining pools that all of a sudden people will get angry kind of quickly with an outcome that they don't notify them. So, OK, I will add them to the list to then shallow and OBM and whatever will get angry that I notified them. OK, I will add them today to that pool. Then three other smaller mining pools will get angry that it's not fair. So I will add them to and eventually I will notify 100 projects and I might as well publish all the details because at that point it's so many people know about the consensus issue that it's what's the point of even keeping it private anymore? So the problem here is I think that there's. If I notify let's say I have three mining pools or I have identified 10 mining pools, then actually there is an incentive for one mining pool to to produce a block that breaks consensus simply because they will have the next 100 blocks. Or or something. So how can you control it once the details are out? How can you? How can you? See if there's somebody actual abuses in what do you do, you avoid that?

**James Prestwich** - Yeah, I definitely agree that there's a lot of judgment that the team has to exercise here about who gets disclosed close to and when and who can use this information responsibly and who is unlikely to. But, you know, the impact of these issues on other people is very large and could be mitigated by early disclosure to people that you believe can responsibly handle the information.

**Peter** - But in that case, we will still have some backlash from the people who didn't know about the issue.

**James Prestwich** - Yeah, I think that you are likely to have backlash regardless, unfortunately, and that really does suck because you guys put in a lot of work in order to keep things stable. I don't think that avoiding backlash should be a significant motivation in security policy

**Martin** - whatever we do, I mean, this is the basis for our security policy. It's got to be towards the mainnet. Everything else is secondary. So that's like number one. I do I mean, we could have some kind of downstream agreement, but we wouldn't..

**Tomasz** - I don't think there was any better solution than what you've done at Kath's. I mean, we can improve the notification, like how the bugs are reported so we can advertise security at ethereum dot org and tell everyone, if you notice something risky, send it over there so it can be transmitted and fixed silently.It's almost like it's just come back to the bug bounty program from the past and people stopped using it because they assume that everything will be stable. There is a difference between what the actual situation is and what people claim it is. And there was lots of people who are just complaining because they used it as an opportunity to make you feel worse, even as most likely this was the best solution. Fix it silently and then slowly wait and observe and see if everyone is switching, maybe, maybe paying more attention, Olavarria said. Like, who is on a very old version and and just suggesting it very delicately that they should have update recently because there were some very important performance changes or whatever, when it will be harder now.

**Alex** - What I'm inversions, which have wallet and everything else you call deprecated and say we don't guarantee anything. Exists in this way. I mean, you cannot obviously force someone to upgrade, but at least if you if you like publish such policy on the front page. Well, most likely people will pay attention.

**James Prestwich** - So earlier in this call, we had a very nice, polite, a security patch dropped, and you should go and upgrade your notes. I'm not asking for any more information than that. An early disclosure. But, you know, that amount of notification would have to endure two months ago would have prevented most of the impact of this specific consensus failure. Or that amount of disclosure to optimism would have prevented the specific consensus failure.

**Tomasz** - There's also a chance it would move it to moves forward. I mean, if that's what happened, I would the team does test and exploit one moment and then actually warns here against disclosure of those downstream. I mean, this is another minister's irresponsibility to do something like that.

**James Prestwich** - It is extremely irresponsible to do something like that and it should inform disclosure to that team in the future. But not to the general, it should not affect the general idea of downstream disclosure.

**James** - So it sounds like there's an amorphous list of what who would want to know at different levels of detail these kind of security things. Maybe if those people got together and said, we want to be on this list, it might be easier to talk about it.

**Peter** - Well, that's one of the problems that if it's a list that is maintained externally, then it will probably be the most horrible list because everybody will be on it who shouldn't be on it.

**James Prestwich** - Right. I definitely agree is that the geth team should is qualified to choose who is trustworthy to handle information like this.

**James Hancock** - yeah, but people could signal that they want to not have the geth team have to figure it out, have them having the like be able to choose, but not having to make the list might be is

**Hudson** - not putting the burden on the geth team, but at the same time having it available to them of people who are interested if they do decide to, and certain circumstances that might not be as dire as the bug that just happened. But in certain circumstances, say, hey, update.

**Peter** - So just a quick memo, which people would like to hate me for this people, I think in general the ethereum community is not really aware of how serious updates are. So over the past year, we've been releasing, even though we did, about two hundred geth release but I have no idea how many. I am fairly certain that a lot of them are super serious in that they maybe did not fix the network crash and the other one fix fix up a memory leak where again, if you know how to crash it, you can crash it. So generally all of these fixes, every time we fix some bugs, a lot of them can be exploited. Maybe it's super hard, maybe super convoluted, but they if you really want to, they may be able to exploit them. And now either our code is super shit, which I doubt, or my guess is that the same thing holds true for other clients, too, in that. When you are fixing bugs, those bugs have some effects and the effects can be pretty bad. So. You kind of people kind of need to be aware of that. The updates are useful.

**James Prestwich** - I think what I'm looking for is a communication channel where people can opt in to becoming aware of that much more quickly. A lot of people running infrastructure prefer to stay on older nodes to avoid new instability bugs. So I spent a lot of time on the phone yesterday with infrastructure providers like four different companies running significant amount of nodes, ensuring that they update to the new go version. They were largely unaware of the severity of that issue and were uniformly on older nodes. So I think like some sort of communication channel where you can tell these people that upgrading is important directly, would help a lot with that.

**Hudson** - Hmmm, well, the cat herders have a list of so in the event of an emergency or a hard fork or something, that has to happen very quickly, that's very public. We've used a list of exchanges, miners and infrastructure providers to reach out to them to make sure they upgrade. So we could have that list be the same list for any client, not just Geth, who would want to reach out, just poke the cat herders and say, hey, can you send this out to, you know, these subgroups of people, whether it be miners or exchanges or stackers or whoever, and let them know is that kind of what you're looking for, James, in a way, at least like part of partly.

**James Prestwich** - Was that list activated on Wednesday or Thursday this week,

**Hudson** - no, because we were not we don't have that system in place right now to be poked for that unless there's a very public like this. This has this like needs to happen right now to upgrade your node. Otherwise the network is going down kind of a thing.

**James Prestwich** - So if it wasn't activated on Wednesday or Thursday this week, I don't think that it meets our needs.

**Hudson** - So, I mean, we're still going to have that list, especially for eth2 to stuff coming up where it comes to like exchanges and stuff, not knowing about when or actually not eth2 to eth1 also where if exchanges need to know about an upgrade coming up, we use that list for even longer term, like this is coming up a couple of months from now or have you updated yet and stuff like that. So we're still going to use the list. But I understand your perspective that it might have not helped on Wednesday.

**Martin** - So just to clarify this, so in this for the critical fix, we did do an announcement a couple of days before and that went out on Reddit, discord, twitter and this is an old Skype group with a lot of exchanges in it. And the message was repeated. When we actually made the release, if there are if we have if there are other channels where we should do announcements or sound the alarms. Yeah, but of course, that would be good.

**Peter** - The thing to know is that, for example, yesterday's release that was not directed by us, that was scheduled by Google and essentially that's I mean, that was our part of the responsible disclosure in that we kind of take the lid off it faster because that issue affected an insane amount of infrastructure with the Internet, not just ethereum. And the moment they gave us a public day, I mean, the moment they actually announced that there's a security release coming, that we also try to maybe announce that half a day later that we are going to do a kind of security release. It was a bit weird that this just kind of overlapped with the concerns issues. So that made things a bit funky.

**James Prestwich** - Yeah, that is an unfortunate synchronicity.

**Hudson** - So just to wrap this up so we can all go. Are there any final comments on this? I mean, this conversation was more to have a conversation about it and to get word from Geth about how their policy works today and how they've kind of thought it over since getting feedback from the community. And so we've accomplished that. Are there any final words?

**James Hancock** - I have one thought so if if Geth did their suggestion of they like a month later or two months later said that this was a security release, make sure you do it. And there was like a way to publish to subscribe to that message being published. Does that fit in the middle of what works for you, James? So there could be so you could subscribe to that list so you might not have gotten the day zero because it wasn't determined to be significant enough for that. But you would have found out way earlier.

**James Prestwich** - Yeah, it would be helpful, you know, we're in somewhat the unfortunate position of having to coordinate validator upgrades when issues like this happen, which can take a significant amount of time. But any amount of notice that a security release happened would be very helpful.

**Hudson** - anybody else have final comments?

**Micah** - I have I have a one sentence thing for people to chew on, if you don't mind. just keep in mind that any sort of private list that we create creates a competitive advantage for large actors in the ecosystem and disadvantages small actors who can't get onto that list because there's a competitive advantage to being more less likely to crash in a consensus failure than someone else. And so any private list that we create that people can get into, we just need to be careful of that. Like we do not want that because that increases centralization or has potential to, I should say.

**Tim** - And it's what I just read that it's worth noting in Neferra also mentioned this in their post-mortem blog post. So know they seem to agree that they shouldn't get the preferential treatment over whatever the community gets.

**Hudson** - Oh, yeah, that's a really good thought, I think that that should shape some of what the Cat Herders do, including having that list, even if we the list needs to be either public semipublic or only used in situations where they're warning about an upcoming fork that's happening like a planned fork. So it's more and not an alert system for emergencies, but more of a notification system for times that things need to happen that are very public and that you might not hear about

**James Hancock** - like a pub sub notification system.

**Peter** - Well, this was kind of the reason why we were trying to go the path of just doing, for example, if we do, in fact, I'm doing a public announcement sometime later than this one if I find a private fix or a silent fix. But the idea of this opposed to reaching out to me project was specifically so that we don't end up in this weird situation where essentially the reason people use inferra is because they are surely not crashing, because they have insider information not to crash.

**Peter** - And I mean, it's definitely really horrible if it crashes. But yes, it is also unfair that the small operator who's nothing, they have no chance of competing on this front. I don't know. So essentially, yes, we are I would say we're open to suggestions. We agree that we could have handled this a lot better and we should have warned people and nudged people more aggressively towards upgrading. So that's something we need to work on. But we're kind of open to suggestions on how to do that fairly in a way that it's it's open to people without creating a possibility for abuse.

**Hudson** - Ok, thanks, Peter, and thanks to the geth team for working through all this and getting the fix out quickly and coordinating all this, and I know a ton of people, at least privately and publicly, have said that y'all y'all are heroes for that. So keeping the network up is always a good thing. Thanks, everybody, for coming. We are well over time. So the next meeting is November 27th. Fourteen hundred UTC. And again, Daylight Savings Time change. So that is an hour previous and a lot of places to where it has been the past months. So take note of that. Thanks, everyone, for coming. Have a good day.

## Attendees

- SasaWebUp
- Hudson Jameson
- Rai Sur
- James Hancock
- James Prestwich
- Danno Fertin
- Adria Massanet
- Alex Vlasov
- Dragan Rakita
- Pooja Ranjan
- Tim Beiko
- Lightclient
- Karim Taam
- Sam Wilson
- Tomasz Stanczak
- Peter Szilagyi
- Pawel Bylica
- Alex B. (axic)
- Marcelo Ruiz
- Trent Van Epps
- Martin Holst
- Artem Vorotnikov
- Micah
- Pawel Bylica
- Vub
- Ansgar Dietrichs
- Danny
- Karim Taam

## Next Meeting

November 27th 1400 UTC
