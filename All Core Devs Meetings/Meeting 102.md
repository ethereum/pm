# All Core Devs Meeting 102

### Meeting Date/Time: Friday, Dec 11th, 2020 14:00 UTC

### Meeting Duration: 30 min

### [GitHub Agenda](https://github.com/ethereum/pm/issues/228)

### [Video of the meeting](https://youtu.be/EPbZ4tU4P5A)

### Moderator: Hudson Jameson

### Notes: Alita Moore

### Summary

## Decisions Made

| Decision Item | Description |
| ------------- | ----------- |
| **102.1.1**   | Serialize the type transaction by wrapping RLP bytes in byte array string |                                                                                                                               |
| **100.1.2**   | cancel dev stuff during week of 21st-25th because of holidays, potentially new years week; planning to continue work on implementations during the break and then have it mostly done by january 8th or so |                                                                                                                                        |

## Actions Required

| Action Item | Description                                                                                             |
| ----------- | ------------------------------------------------------------------------------------------------------- |
| **102.2.1** |  James to check in with clients next week and the 28th about implementation progress                           |

---

# 1. YOLOv3 & Berlin client updates
Video | [2:47](https://youtu.be/EPbZ4tU4P5A?t=167)

**Hudson** - Hello, everyone, and welcome to all core devs meeting No. 102. I'm your host, Hudson, and today we're going to be going over just a few agenda items. The first one is an update on YOLO V3 and the Berlin client updates. And also a topic of that is the outcome of the 2718 breakout room. So should we do the twenty seven eighteen breakout room first, do you think, James, just to figure out what's been decided there and then see what people have implemented from that, if anything, already.

**James** - Yeah, we'll start with that and then if there's any client stuff uncovered related, we'll move from there.

**Lightclient** - Ok, so basically the main thing we were trying to decide is how we wanted to serialize the type transactions. And we you know, we've already decided how they would be serialized over ending in consensus of the consensus protocol. And the question is how do we serialize it over the wire? And the main outcome of that was that we were going to wrap the transaction, our LP bytes in a byte string array. And so whenever it comes over the wire on that P2P, it will be wrapped as a byte string. And so we'll decode that by track and then decode the transaction. That was the main outcome. The other couple of decisions where everybody was mostly in agreement already.

**Hudson** - All right, any questions from anybody on that, is there anyone who needs some clarification on what this means for their client implementation?

**Artem** - Ok, I have a question, so I'm looking at the outcome, the final sterilization block and the decisions in the issue. And so is it correct that this will be RLP within RLP? Basically or what is the format for the byte string length?

**Lightclient** - Yeah, it's essentially RLP within RLP. We've got the transaction by the concatenated in front of the payload and the payload for the 2930 transactions are also RLP. So it's essentially, RLP encoded RLP.

**Artem** - And so about the motivation, why did you not opt for our RLP within SSZ.

**Lightclient** - I think the main reason we didn't do SSZ at this point, because people are a little fatigued of the SSZ - RLP  discussion. We need to ship 2929 and we need to ship it a few months ago. And so it's a lot faster to just go ahead and ship this with RLP now and figure out SSZ in 2021

**Guilallame** - Yeah, so our RLP is recursive and I'm sorry I didn't follow the conversation at all, but I'm just curious why do you do RLP within RLP and what like what do you have this intermediate step of turning it into a byte array where you just included directly 

**Rai** - I think it's better not to think of it as RLP in RLP, to just think of it as an opaque byte array. I think it ends up being kind of like that just because of the value of that the type byte is. But we could potentially have the typebyte concatenated with SSZ encoded thing or anything in the future. So, yeah, I think it is best to just think of it as an opaque byte array for now that just happened to have one twenty, not one transaction, which is 2930, which is our RLP in the spec. But there's no requirement for that in the future.

102.1.1 | Video | [7:37](https://youtu.be/EPbZ4tU4P5A?t=457)

    serialize the type transaction by wrapping RLP bytes in byte array string

**Hudson** - All right, thanks so much, Light Client, for that update, now that we have that decision outlined, we can go over YOLO v3 in the Berlin client updates. James, do you want to take that one on and go through all the teams.

## Berlin Client Updates

**James** - Yep. So just an update on where the implementations are. Just updates in general for the YOLO V3 spec for each client. Is there a client Berlin to go first? No, Besu, can you go, Tim?

**Tim** - Rai is actually the one working on the implementation, so he'll give a better update to me. All right.

**Rai** - So I'm still working on 2718 and 2930. Yeah, everything else is ready, but I'm still working on that.

**James** - Ok. And Geth, did Martin make it here?

**Lightclient** - I'm doing the implementation and geth so I can say that the implementation is mostly complete. The main thing that's missing is I'm still trying to work out this new serialization format for the list of transactions.

**Hudson** - I think Martin also is here, so you can both give updates. 

**Martin** - Yeah, I mean, it's mainly same as Besu; we're 2718/30 and then there is the big one, the one lightclient is working on.

**James** - and nethermind?

**Tomasz** - So the last time I worked on 2930, 2718, just to make sure that I have a feel of how they look on the implementation side, and that went very well. And then I just waited for a bit more clarity on the final serialization format. So it's about finishing in the testing, but I'm pretty confident it'll be fine because most of the burning items that were there before, we have already had them covered, implemented and tested with the consensus test. So 2930; 2718. If implemented, contested. 

**James** - OK, and OpenEthereum.

**Dragan** - Yeah, I mean, just yes, we merged 2718 on the dev branch and most of the...

**Hudson** - And then I think, is their Turbogeth here? Yeah, yeah.

**Artem** - Ok, I guess I can take that we have YOLO V2 and 2929 from Geth 1924. We made a release yesterday, so I think that's that.

**James** - And was TurboGeth planning on joining Berlin? I don't remember. They weren't planning on joining YOLO V2 or V3.

**Artem** - So we have merged what was in Geth basically. I'm not sure if anyone's tested it, to be honest. But perhaps we have that.

**James** - Ok, then, so most clients are on the tail end of finishing this, the last few changes based on the meeting, the update that we just had from lightclient. Is there.. So the holidays are coming up, launching YOLO V3, is that something we want to try to do in the next week or so or. What some general thoughts on that?

**Martin** - I don't really see how that can be done.

**James** - I don't I don't know, I don't have a grasp of the time we're left work like the time left, working for the last stuff, plus the holiday stuff's all going to be happening, so.

102.1.2 | Video | [11:53](https://youtu.be/EPbZ4tU4P5A?t=713)

    cancel dev stuff during week of 21st-25th because of holidays, potentially new years week; planning to continue work on implementations during the break and then have it mostly done by january 8th or so

**Hudson** - Yeah, I would say let's kill the whole week of the twenty first through twenty fifth as any kind of work week because some people will be traveling if you're able to, and then some some people will just be off for the holidays. And then of course, around New Year's, probably that's not a way to do it. And we could do a week of New Year's maybe if enough people are done like the twenty eighth, twenty ninth kind of a thing.

**Tim** - We can just launch yellow three, we don't need like a call or anything now like you, we can like if we don't have the next call was supposed to be on Christmas Day. Probably makes sense to skip that. So, you know, if we keep working on the implementations now, know whenever they're ready, they're ready. And I think, you know, we if if over the holidays or, you know, right after New Year's or whatnot, like people have bandwidth to set up the network, then great. And I guess worst case, I don't know, is it realistic to expect that, like, the implementations of the EPS will be mostly done by like what was it was like January 7th, January 8th would be the next call after this. And if we're lucky that maybe we sail up YOLO v3 before then.

[Can't hear Adrià]

**Adrià** - I think that we couldn't just adding clients. It's a test net, so no worries.

**Hudson** - Ok. And what we could do is let's have a date that we check in with all the clients on discord, and then from there, we can make other assumptions that might be better because it sounds like we don't have a good. Like consensus grasp on when things are going to get done across majority of clients. How does that sound, James? Just like we can pick a date, like in late December to, like, check back in.

102.2.1 | Video | [14:10](https://youtu.be/EPbZ4tU4P5A?t=850)

    James to check in with clients next week and the 28th about implementation progress

**James** - Yeah, I was going to say I can check in next week and I'll check in on clients next week just to see how it's going and then.

**Hudson** - The 28th would be good, too, because people might still be out, might be on the 28th, but some people will be here at least.

**James** - Yeah. So I'll check in next week and then on the twenty eight.

**Hudson** - Ok. Any comments or questions about the topic of Yolo V3 or Berlin or anything that needs to be cleared up?

**Pooja** - Yeah, just a quick reminder for the authors of the proposals included in YOLO v3, out of five, four proposals are still in draft. So we would like to see that in at least in Review, if not in Last Call. And the fifth proposal EIP 2565. That is in the last call. And I think the duration has been over so the author might want to move it to Final now.

**Hudson** - Yeah. And if you do that, contact me, Micha Zoltu or Lightclient to get that merged and we can help you with that.

# EIP-1559 Update
Video | [16:41](https://youtu.be/EPbZ4tU4P5A?t=1001)

**Hudson** - Other comments or anything. OK, next up, we have other Ipsen discussion items, Tim had an update on EIP-1559 and kind of a broader picture there, I think.

**Tim** - Yeah, I won't try to summarize too much of it here, but we had another 1559 call last week, I believe, and the big, I guess, take away or new thing was Tim Roughgarden who's a computer science and game theory professor from Columbia, released a paper analyzing 1559 from an economic perspective and trying to understand is it actually better than what we have today? I just shared the paper in the chat. It's pretty extensive and the 10 takeaways are shared in the third page. If you don't want to skim the 60 page paper, you can just read that. And overall, the paper is pretty positive, about 1559, which is nice. So just in terms of UX, he makes it clear that having the base fee as part of the network really helps kind of people converge on the optimal bids for their transactions. And that's a good thing. And that the incentives for miners to carry out the protocol as intended are the same under 1559 as under our current mechanism. The one I guess or sorry the two kind of more negative sections of the report was one around miners, where he highlights that today. There's a lot of negative behavior we could see from miners on the network that would theoretically be possible, but that doesn't happen and we don't have a good explanation for that. Aside from maybe the miners are eth holders or they care about their health of the networks that are somewhat altruistic. But he says, you know, that could potentially change under fifty nine. So if if for some reason miners decide to engage in behavior that today they could but don't pick up, that's a potential risk. And then the other this is a much more minor comment about it is the way that the update rule works. In 1559 we increase or lower the base fee by up to twelve and a half percent if we have a full block or empty block. And it's just a linear increase and decrease based on the gas used. And he says that this is maybe not like the optimal way to do this, given that once you if you have a very quick increase, you might then need to have a bunch of empty blocks to lower the base fee enough to reach the price that people are willing to pay. So it's not the end of the world, but it's that slightly inefficient. So we have someone who's looking into possibly just a better formula for that to have a smoother update. And yeah, so I guess I just recommend anybody who kind of cares about 1559 and its impact on the network to at least have a skim the report that was quite good in terms of other progress. We've been working we've been working on the implementation a lot. So there's a there's a draft PR against the geth code base that's that's up. The implementation still don't have EIP 2718. So none of them are kind of ready for, you know, being merged and trying to master. But they're there interop together. We have a small test net. So that's that's a good sign. And we've kind of held off implementing 2017 until it was it was done and clients were brought in. And I guess the last outstanding thing on the client side that we need to figure out is the transaction pool management. So because the Besu changes from block to block, like the naïf sorting of transactions in the transaction pool, if you take a naive approach, you can end up resorting to transaction pool every block, and that's a pretty bad outcome. So we're working to find some better heuristics about how we can efficiently manage transactions. And the Quil team is helping out with that. So I guess, yeah, at a very high level, I suspect in another month or two we should have, like most of these issues, figured out that the implementations ironed out with 2718, then there'll be a bunch of there's a bunch of like auxiliary work like updating the Jason RBC suspects and whatnot. But the, the bulk I think of the 1559 implementations should be done and one. Yeah. Sorry. One last thing we're working on is large datasets. So because one of the concerns was how would clients on Main Net handle fifteen fifty nine one part of that is like the database has a pretty huge stap it becomes harder to process, it might become harder to process blocks that are twice as big. So Abdel from our team has put together I've got a large state test generator which can generate a new network with an arbitrary number of accounts and storage slots in the contract. So we're we're setting up a new desktop now with one hundred million accounts and a contract with one hundred million storage slots, which is more or less what we have a mainnet. And then once we have all the clients kind of running on that network, we'll start with a bunch of 1559 transactions and see if the clients can handle the load for like half an hour an hour, which is the max upper bound of what you'd expect on mainnet. And that's pretty much it.

**Hudson** - Anybody have comments or questions on this?

**Rai** - Yeah, I just wanted to get people's general opinions on what we're going to do with are we going to introduce a new transaction type like twenty nine thirty that has the fifteen fifty nine gasfields. So it'd be like a different type. Or how are people envisioning those two interacting.

**Tim** - As I understood it, the plan was always, yeah, you create another 2718 transaction. We haven't defined it yet to be to be clear, but I think that's generally what people want to do.

**James** - The quilt team is the team that's that's tackling account abstraction right now and the Cat herders just did a peep an eip with them about abstraction stuff, so that's something else. If you're wanting to look into what they're doing in approach, it's a it's a good overview. And they did they did a deeper dive into like what are the transaction rules and things that make it safer or they're trying to make it as a safer thing. So for those that are interested, would be good to get an update on that.

**Pooja** - And the video would be released on Monday on the Ethereum Cat Herders Twitter.

**Hudson** - Ok, anybody else? And do we have any other agenda items or things that we missed out on or that people want to talk about before we jump off the call?

**Martin** - Some geth updates, so we today released what's hopefully the last of the ones online versions and the big stuff for us going forward is going to be the next race. We're going to launch the Snapp's. But what I wanted to mention really is the security process we have now started to include to publish our advisories by GitHub. And that means so to github up people and other like node operators, downstream projects can subscribe to the event feed and get notifications. And we're also pleasantly surprised by how easy it is to get TBD assignments for vulnerabilities to get the flow. So I can recommend that we also publish a vulnerability.json, to our github the pages on page of the best news then. And the new git version can I can do a version check. So that's just the latest from a bit of the info and checks it against itself. So a user can optionally do these kinds of personal checks and see if there are any security related vulnerabilities that they need to update and this vulnerability.json file was inspired by what's already been solitity, the format they use, whether they also include a regex for the vulnerability for the well, how to detect the vulnerability if it's present. So we did that as well. And this means that we could also use it on the fourth monitor. So if you go to four of these developers today, right now, you will see a couple of warnings for the computer and all the nodes and things like that. And check it would show the information which is best from the vulnerability info. And what I kind of wanted to highlight here is that. If any other clients decide to have a similar kind of vulnerability, release where they also publish a regex or check it against the reported node version, then we can integrate that as well in the ... And make it generally easier for these to be well, for everyone to check their security posture. So if you do start to work with something like this and implement it, please let me know and I'll add it to the corporate monitor.

**Hudson** - I just posted a link to the foreman and chat and yeah, it's really cool. Everyone go check it out and congrats on the update. Martin and geth team. Really cool.

**Tim** - this really cool, where is the JSON file.. is it in the code base?

**Martin** - Yes and no, because it lives on the GitHub pages branch. Oh, so there's a call underscored vulnerabilities and there's also vulnerabilities. Just minutes tick, which we use to verify the signature of it.

**Hudson** - Today, I learned it looks like CloudFlare rolls their own geth, is that right when it says CloudFlare dash Geth Martin? Yes. Yeah, cool. OK, anybody else have comments or anything else for the meeting?

**Pooja** - Yeah, I may have a kind of quick announcement regarding a 1559 oh, we are going to arrange the Cat Herders are going to arrange another peep an EIP session for 1559 that is scheduled on Tuesday. if people are interested to know about it and have questioned the Zoom link will be published on the ACD discord. And now that we are moving ahead with the Berlin and I know there are some proposals which are already ready and that would be seen in future upgrades, cat herders are collecting feedback from project and other infrastructure provided on their part on the network upgrade. I'm sharing the link in the chat. So we already have reached out to miners and people we know and we have contacts for. But if any project, they would like to leave their feedback about the network upgrade the frequency of what could be done to make it better. Here's a link and we would appreciate your answers to that.

**Hudson** - I'm on mute, thanks for that, Pooja, what time is that on Monday?

**Pooja** - Actually, it's on Tuesday, it's one thirty Eastern

**Hudson** - Anybody else have comments or things they want to talk about? I know lightclient mentioned in chat, maybe discussing what comes next after Berlin, I don't know if anyone had thoughts on that. I said in the chat that I kind of assume that today people wouldn't have that much on thinking about the order or anything like that. But if anyone does feel free to speak up or anything. If that's the if that's all, then I guess we can have a shorter meeting today. Congrats to the ETH 2 team they launched since our last meeting, the beacon chain. So I guess we'll just congratulate Danny and just say that he is representing the ETH 2 team today; horray on that. And yeah, that's about it. Thanks, everybody. The next meeting will be on January 8th at fourteen hundred UTC. And Happy Holidays, everyone.

## Attendees

- Rai Sur
- Hudson Jameson
- Pooja
- Lightclient
- Tim Beico
- Trent Van Epps
- James Hancock
- Dragan Rakita
- James Prestwich
- Adria Massanet
- Martin Holst
- Pawel Bylica
- Guillaume

## Next Meeting

January 8th, 2021 @ 1400 UTC
