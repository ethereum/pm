# Ethereum Core Devs Meeting #152
### Meeting Date/Time: January 5, 2023, 14:00-15:30 UTC
### Meeting Duration: 1 hour 30 mins
### [GitHub Agenda](https://github.com/ethereum/pm/issues/700)
### [Video of the meeting](https://youtu.be/SmcMwdHZqg8)
### Moderator: Tim Bieko
### Notes: Alen (Santhosh)


| Decision Item | Description                                                              | 
| ------------- | ------------------------------------------------------------------------ | 
| 152.1 | **EIP-3860: Change the failure to OOG EIPs#6249:** Aragon and the Geth people both approved of this PR. So ready to be combined. Update the test, and the next step should include this change as well. | 
| 152.2 | **Shanghai Updates:** The client team has agreed that EOF should not be included in Shanghai. removing EOF from Shanghai while keeping the scope tight. So, yeah, so we don't put off withdrawals. | 
| 152.3 | **EIP-4844 updates:** No major updates, next we another community call. | 
| 152.4 | **Add hexary trie roots for lists in ExecutionPayloadHeader consensus-specs#3078**: EL dev needs to discuss this offline and come back, couldn't take descision over this call. | 
| 152.5 | **EIP-5483: **Author was not present in the call | 



**Tim Beiko**
* Good morning, everyone. Welcome to the first, All core dev Execution Layer Meeting. So 152, of these calls. yeah, most of the stuff today is around Shanghai.
* so getting some updates on the status of, withdrawal testing and DevNet. there was a spec change proposal for, the limit meter,  code EIP, and I'll go over and then, following up on EOF, see in both where clients are at, based on kind of the conversation from, from the last call. And, also going over like the, the different proposals that have come up, since then. then I can go over some testing stuff. 
* And, finally, there's EIP 4044, a proposal on the CL specs and two new EIPs to discuss. if we can get to those. 
* I guess to kick it off, does anyone from either the testing your client teams wanna give a quick update on where just, withdrawal testing is at, where the different implementations are and what things look like in terms of, of dev nets.

## Withdrawal Testing & Devnets updates [3.30](https://youtu.be/SmcMwdHZqg8?t=210)

**Barnabas Busa**
* Regarding the DevNet, I could, give an update. Yes. so we currently have a DevNet one running, and, we started, just before Christmas. 
* Currently we have all the different client combinations, running on it. And, some combinations, work well, others are naturally, I have the link, posted in the chat here. So here we can see that we are on block, 94,000 and, most of the, most of the notes are able to follow ahead. 

**Tim Beiko**
* Nice. and what's included in the, in the implementation? So I assume it's withdrawals and then these, other small EIPS, but not EOF, is that correct? 

**Barnabas Busa**
* That is correct, 

**Tim Beiko**
* Yes. Okay, sweet. Any other client team, anyone have, have thoughts on this or anything else you wanna share? Oh, okay. 
* And then Perry, yeah, posted the spec versions, we're targeting in the chat. so that's the CL spec, 13.0, alpha two, and then on the EL side, the withdrawal, EIP we're using commit 0FA D E C, Great. Anything else just on withdrawals or s for Shanghai? 

**Barnabas Busa**
* We would like to begin a new one with you included, but that is really up to the EL teams to be ready for that. 

**Tim Beiko**
* Got it. Yeah. Well, yeah. thank you. and I guess before we get into EOF, I just wanted to quickly cover this change. Powell had proposed, for EIP 3860. 
* That changes one of the failures, and it seems like, some get folks have, approved this. does anyone want to give a quick overview of what this is? 
* Marius, I will pick on you because you're the first one who approved it, and I can't find Powell on the call. 

## EIP-3860: Change the failure to OOG EIPs#6249 [5.58](https://youtu.be/SmcMwdHZqg8?t=357)

**MariusVanDerWijden**
* So basically, we have, different, failure modes, either,  out of gas or just, or just return a zero. So either like, either we like, terminate the transaction context or we return, a zero address. And if you look into the linked, if you look at Ethereum magician's thread, you can see that there are, these checks are like, they were like interwoven. 
* So we had, some out of gas, guest checks before, and then within a zero address return and then some other out of guest checks, and it would makes, it just makes more sense to have them in one block and then have the other. 
* And, the one that basically right now the way it was specified, the init code size limit check would return, address zero. but, it also conceptually makes more sense to return error there, because it means you, like you're running up against the, the init code size, limit. And, that's clearly an error to me. So, yeah. 

**Martin Holst Swende**
* Yeah, it can, it can also be seen semantically as if, I mean, you can deploy deploy and the cold size, but if you do it larger than, C 0 0 0 pipes, it costs the infinite amount of gas. 

**Tim Beiko**
* Great. Okay. any other I saw like, yeah, Geth folks approved this PR, Aragon as well. Any client team disagree with this? Okay. so perfect. I guess we can go ahead and merge this in the next, week or so and then, update the test and the next step that, should also include this, this change. Okay. Oh, oh, yes. 

**Pawel Bylica**
* Yeah, sorry for being late. I wonder if there's like any comments from like the, the other side, I mean thecontract from contract developers to, if they, if, if they see that as a kind of issue to handle 

**Tim Beiko**
* Does anyone on the call have an opinion about this contract slide? Do you wanna block merging this until we figure that out? Or, is it better to just

**Pawel Bylica**
* I'm also slightly in the, in the favor of the proposed change to as I think the client does Agreed. but I think the, the, the main reason it was the other way around was that, I think  the most, the common series of on this January, clever to return us as like user-friendly errors as possible.yeah, so that, I think what was the reason for the original design, yeah, I'm not sure like how much this applies here. but I wouldn't block it, but it are some concerns. Yeah, I don't know. 

**Tim Beiko**
* Yeah, I guess just because we want to, move forward with withdrawals and it's all kind of intertwined, I would move forward with the change if like, no client teams has an objection.
* I think if we learn in like the next few days or weeks that like there is a big pushback by contract devs, we could always revert it back. it's not, doesn't seem like a huge change. but yeah, I would try and go forward and, and merge it for now. Anyone disagree with that?

**Martin**
* I agree. 

**Tim Beiko**
* Okay. and  I'll try and, give a shout for contract devs to look at it. so maybe we can wait like, you know, until like late Friday or Monday to merge it in so it gives people at least a couple days, but assume it's going in. sweet. 

## EOF Status update & deadline [11:13](https://youtu.be/SmcMwdHZqg8?t=673)

**Tim Beiko**
* Okay. next thing is EOF. so I think there's like two things to like unpack here. So first is like the current status of the EOF one implementations, and it makes sense to go over that, and then we can discuss kind of the different proposals that'll have come out, since then. 
* So specifically Vitalik had a proposal about banning, code introspection on ETH magicians. And then, this morning Alex just shared kind of a view of how that could all fit in a broader EOF roadmap. but maybe, yeah, just to start, do any of the client teams wanna share kind of where they're at with their EOF implementations? 

**lightclient**
* Maybe I can just give a really quick update also from the breakout rooms over the holidays, breakout rooms. Yeah So we did two breakout rooms over the holiday period, and there were two main spec outcomes from that, mostly from the first meeting. The first one was that we removed the jump F op code. 
* It was something that we felt we just needed to spend more time, have solidity, complete their implementation and make sure that this was the right, like the perfect type of, instruction that we were looking for. And so we removed it for now, so reduced the scope of EOF slightly by that. And then we also made the data section mandatory. 
* Previously it was optional, but making it mandatory made the parsing, marginally simpler. So those were the two main spec changes, a handful of things where other things were discussed. But those, those were the things that, that did make it into the spec. The Epson team spent a lot of time and I helped a bit with making, getting into the spec into a more finalized place. 
* I think we've like merged all of the outstanding PRs to the EOF EIPs. There's still a handful of like small things that, you know, small errors in the spec, some conflicting things between the four or five EIPs, but more or less like the EIPs are in a good place now with respect to the implementations and tests. 
* I think, you know, about a week and a half ago, a week ago, Martin started doing differential fuzzing across all of the clients. And that uncovered quite a few things. Initially, I think every client had at least like three, four bugs and, a lot of those things  have been resolved. And if Martin wants to talk more about the findings there, he, yeah, that would be great. 
* But we also have two sets of reference tests. I don't think either of them have been officially released yet, but the Epsilon team has been working on a set of tests in Ethereum slash tests, and Mario and I have been working on some tests in execution spec tests. Mario and I decided to not release them until we were able to integrate the, like Shanghai by Time Logic, but those tests are in this PR I put a tar ball up before the meeting. * I think like the reference tests are not as comprehensive as we like ultimately will want them to be, but they're in a place that we can start getting an idea of like where clients are. Unfortunately.
* I don't think that any clients other than, you know, the Geth client has run all the tests. I ran the Epsilon tests a couple days ago, passed all of them except for two or three, and obviously I filled the execution spec test. So we are passing all of those, so still need to get some clients to run, to run those things. yeah, I think that's mostly the update. I'm curious to hear what other client teams have to say about the progress of their implementations. 

**Tim Beiko**
* Maybe Dan, 

**Danno Ferrin**
* At Besu, we've started random reference tests. We haven't, there was spec change initially. You could go EOF 1 to legacy and willy-nilly, so I need to update that.
* So you can only create EOF1 out of EOF1. those are most of the tests that are failing. trying to hold off on, I'm doing too many merges until we to reduce the number of PRs that go into the actual mainline. 
* So I'm stacking most of these into an EOF five breakout branch that I have. but yeah, it's, we're basically in the, you know, checking all the boxes phases, making sure that it's all ready to go. So we got major work all done. 

**Tim Beiko**
* Got it. Thanks. anyone from Nethermind or argon? 

**Ahmad Bitar**
* So we are, we already have, complete implementations for EOF, tests, are still not finalized. We're not sure which PR to pull and to run against. We have ran against a couple of them, since that they're still not ready and, does not cohort to the spec. 
* So we just want we would like the test to be finalized. so we, before we start with the dev net, because if we start with the dev net before running the tests and resolving the issues, probably what will happen is that during the dev net we will have a lot of consensus issues and it'll take so much time to debug where these issues are. yeah, basically that's the status. But for implementation wise, we have done all of the implementations for all EIPs and, we are already passing the buzzer that like client was talking about. 

**Tim Beiko**
* Got it. Thank you. anyone from Argon? 

**Andrew**
* Yeah, for Argon, it's easy. We are going to piggyback on the Geth implementation by Lightclient. 

**Tim Beiko**
* Got it. thanks, Powell. I see you have your hand up. was that related to this? 

**Pawel Bylica**
* Yes, I, so actually I wanted to give update about the tests, a bit more specifically. So, the test cases I mean the state test, the execution test,  from Ethereum slash tests. So the test cases are still divided into five groups coming from original EIPs, because that we kind of defined most of them previously. but, what is the implementation is actually has all of the EIPs enabled. So the test case is kind of, like focused on like specific aspect of EOF, but you should expect all of the, all of other features also being enabled. 
* And the current status is that, this is like recent, we updated the, the first pack of that, and this is already in the, the main branch of tests. This is EIP 3540, yeah. so this we consider already, although, EVM one and Geth implementation, I think doesn't agree on one of the tests. So this is 1, 1, 1 thing that we need to take a look at on. But, 
* I think, it's almost, almost done this part and the next part, so then the second, set of tests are ready but not merged and,two others are in being, being in progress. And the final one is not started yet. So that's, well as the, yeah, the, the summary of the status. that's kind of trying to also answer the, one of the comments from one minute ago that, I think as of  today, you can, you can take a look on this first pack of test that's already in the main branch. 

**Tim Beiko**
* Got it. thank you. Any other thoughts on the current status or just the implementations or the tests? I don't know if Martin, you wanted to give a quick update on the fuzzing work you did? 

**Martin Holst Swende**
* Well, no I'm trying to make,  a bit more at once now, but essentially it's, four different clients that are, no, five different clients are being tested. four, sorry. and we have a pretty good, just, you know,  it turned out that the implementation of the container format and the validation is obviously fairly complex, judging by how many different types of implementation flaws were made. but also the,validation turn out to be very easy to test. and we define this test format, which just we can show bytes as input and we can compare the output. 
* So we keep get very good coverage of this. And I'm fairly confident that this type of testing will, be proved to be very efficient in the long term. what we have not tested is the actual semantics of running the code. So my passing has done the validation, of the code, but not the actual execution of code. So that's for, for a later stage. Yeah, with state test and stuff. Yeah, that doesn't matter to me. 

**Tim Beiko**
* Got it. Thank you. any, okay. Anything else on the current testing and implementations? 

**Mario Vega**
* Yeah, I would like to share? Yep. the perspective on the execution test. So I've been working alongside like line with the other, test suite for reference tests. And one thing that I really found is that, there it's not so easy to create, effective best case for EOF. So, and the problem is that there are a lot of pitfalls. 
* For example, if you want something to fail in a certain way in EOF, you have to be very specific and you have to make sure that the test doesn't fail somewhere else before reaching what you really want to test. So that matter, I think that it would be really valuable that we standardize the errors somehow so we can verify that our tests are actual testing, we are expecting them to test, likely had, draft of the errors, but I don't know if you want to share that that now or maybe, something later. But I, yeah, I didn't really think that it would be really valuable to have that standardized over all the clients that are improve in feedback. 

**Tim Beiko**
* Got it. Thanks. okay. And yet my client just shared, his notes  in the test with all, okay. With all of the different error codes there. anything else that, to add on this? 

**Danno Ferrin**
* I'd rather have the errors as readable strings so you can figure out what's going wrong rather than having to cross reference a table. That'd be one request, but standardizing the strings I think is fine. 

**Tim Beiko**
* Got it. Okay. I, and I guess the, so it's like two other things to talk about. So one is, you know, on the last call we, we said we might, remove EOF if it wasn't quite ready today. And,  same thing for the next call.
*  I think before we have that conversation, it's worth, talking about like the new EOF new proposals that came out, just so we kind of have that in context, when we, when we make that decision. so I don't know, maybe it makes sense. Vitalik you kind of posted this first one on these Eth magicians about code introspection, and then Alex, you just posted this morning kind of the, your plan based on that.
*  But, maybe Vitalik if you wanna go first, then we can do Alex. 

**Vitalik Buterin**
* Sure. are you guys hearing me okay? 

**Tim Beiko**
* Yeah, it's, it's pretty good. 

**Vitalik Buterin**
* Okay, great. so I think, what I wanted to start with is just, a bit of, kind of philosophical background behind, so where some of the things I was saying they were coming from, right? So the yeah, concern, like I think the difference between, Eth evolution and ongoing improvements of, any kinds to the EVM, at least as it's done so far, versus, ongoing improvements to the rest of the, Ethereum protocol is that in the evm it's much harder to remove things than it is to remove other futures, right? 
* So like last year we managed to successfully, remove a huge module, you know, the, entire proof of work, consensus system. And that only led to like very limited, back like backwards compatibility issues for, users and for applications. but on the other hand, with the EVM, like we, so we have added a couple of OP codes, but, when we have, tried to actually change things or even, remove things, it's, generally, yeah, it has happened a couple of times, but there have been very high costs, right? 
* So, like for example, removing the self-destruct op code is, you know, well on its way, but it's, definitely something that altogether is, probably taking five or 10 times longer than a, comparable change outside of the EVM would take. or even the gas cost increases from two or three years ago ended up, but it ended up taking quite a bit of time, right? and so the, reason for that is basically, you know, kind of obvious, right? 
* It's the, that the, you have applications that are written in E V M code, and if the EVM changes, then those applications can't change. Whereas if you're touching a part of the system that interacts with something on the outside that, like for example, if we eventually get rid of our LP transaction formats, then like that's, deals with something that's on the outside and, that, and that's something can change, right? and one of the things that I think would be, again, or one of my big worries with I improvements to the VM in particular is basically that because it's much harder to deprecate and actually remove stuff a yeah, a philosophy of the, of, kind of E V M developments that allows for large or basically a large amount of ongoing improvements and doesn't, commit to like something really close to ossification fairly soon would risk us basically creating a V2 and then creating a v3 and then creating a V4 and require, but still requiring like V1, V2, and V3 to still be part of the consensus code because we don't have good ways of removing them. And because there are applications that are written that depend on them, right? 
* And I, look, we kind of see this already with a call code is probably a good example. We added delegate call, which is obviously better, but, cool code is, is still around and the, general path that I, wanted to suggest as a way of, getting around this issue and as a way of, getting to the, basically letting us, make some improvements to the EVM over at the, over time, but at the same time actually achieving the objective of, making the EVM simpler and making the e EVM cleaner and make actually, you know, making the protocol more simple and more beautiful over time instead of just having this, kind of glob of, ever increasing, technical debt that we can get rid of is that if we're going to make a EVM version, that new VM version should be designed with the idea in mind that it's, of being very forward compatible to all kinds of upgrades that we want to do in the future, right? And the current EVM is totally not that in a whole bunch of ways, basically because the current EVM can like just has way too much introspection, right? So like, you know, you have code reading up codes and code reading up codes, like you, read specific bys of the code. you have the jump up code and the jump up code can take as arguments. A byte value then gets created by EVM execution. And so the jump destinations, like you can't actually rearrange them. You have to keep the same byte in the exact same byte. you have, no thing. 
* This like, contracts create creation and, you know, every, everything having to do with code being kind of closely referred to by it's code hash, there's like a whole bunch of, EVM property is estate gas is also, is also another one, right? Where the facts that all of these EVM internals get exposed means that it's my, in any attempts to change a whole bunch of things, how like just inevitably becomes a very backwards incompatible, right? 
* And so the idea is that if we make a V2 of the EVM where that V2 has the property, that it has much less introspection, then what we gained the ability to do is we gained the ability to forcibly upgrade old contracts, right? So if we, upgrade, let's say EV m V2 to at some point in the future, you know, V2 to v3, then we could have a protocol rule that says, oh, when a contract that is still V2 gets touched, then you can apply a transformation that converts V2 code into V3 code that has equivalent behavior. 
* And because there isn't all of this crazy introspection that it becomes actually possible to do that, right? So like for, just to give  a quick concrete example. Let's say in V3 we decide it's, you know, having shot three or Kak as an op code was a mistake from day one. So let's get rid of cash check acid up code and let's move it over and make it a briefing pile. Well, the problem with doing that is that you've replaced something which has one byte with something which has like 10 to 20 bytes. And you know, also you're gonna need a memory slice for it somewhere. 
* And so you're replacing a single byte with a byte sequence that's more complicated. And so that ends up changing the code copy output, and that ends up changing the positions of all the code. And like you could write out the transformation and do it, but only if all of this introspection doesn't exist, right? But if the introspection doesn't exist, then what you could do is like actually write the transformation, potentially even formally prove that the transforms code has the exact same behavior under the new version of the preformed code has the old version. And then after V you would have a transition period where EV M V two and E V M V3 are both available and eventually like, actually let v2, like make sure that all V2 contracts get poked and, moved over into v3. 
* And then once that happens, then it would be possible to eventually like upgrade again and do a V4 or something like that, right? And so what that would mean is that the number of EVM versions that clients at any points in time would have to actually support is, is kind of bounded at two, right? Like as once you go past three, then like, you know, version, the third oldest version could just be fully deprecated. And one of the nice things about E V E, EOF as it is, is that it has features that go in that direction, right? 
* So particularly getting rid of dynamic jumps, getting rid of dynamic jumps is like a great move in that direction because it enables these code transformations, right? Like if you can, if you have to make a code transformation that a voice has one byte with five bytes, then you can do that and you can translate all the coordinates. And you know that like the reason why you, you can translate coordinates is because there no longer is a way to jump that, where you pass in the V coordinate you're jumping to as an EOF generated variable, right? 
* And the inability to do that makes it, makes that kind of code transforming actually possible. so my suggestion is basically, well, you know, we could take the e ev EOF route, but extend it a little bit, ban introspection and like basically push it to the point where it goes, all the way it actually makes code, much more transferable. so I guess the, the things that I know look, that I would love to hear feedback on are like one, just the general direction and, the concept of, moving toward this, EVM approach where basically we're committing that the, the first goal of the, of, upgrades is to upgrade to some kind of code, which is, much more walks down and not intro respectable with the specific, goal of, being upgradeable more over time. 
* And then even like actually saying like, you know, we are going to only need to have two versions, supported by the like actual EVM clients at any one time unless they, really care about, you know, ex verifying the channel, all the way from history. And so that way we can keep upgrading and having things, be sustainable. and the second thing is, you know, specific pathways for doing this, right? So my proposal basically like would, would in practice involve delaying EOF, to the, and adding some signi, significant, stuff to EOF to make it, to make EOF itself, be to like be this. But you know, another path might be to have the kind of current proposed the EOF v2, and then have a v3. And I think, the V2 would still be transformable into V3 though, like you would've to pay some costs like doubling code size, but that would be fine. and then, you know, maybe there might, there might be some other pathways as well. so, you know, there we go. 

**Alex Beregszaszi**
* Yeah, I do. Yeah, I'm not sure if I should actually go through  the proposal, in depth. probably not because it's also like quite lengthy. but I wanted to start, Yeah, I mean, I wanted to start with, saying that we actually wanted to have a lot of these, features generally, which were mentioned. you know, going back, basically last year we did hope that some point to, reduce the introspection options, which also means like getting rid of, of, anything gas related. 
* We wanted to also revise maybe memory handling at some point, and we kind of felt like they're doing all of these in the same time, is extremely ambitious. and that was the reason we started to split up, all of these changes into steps. one interesting point, Vitalik mentioned, regarding static jumps, and code modification, there was actually one of the, the driving forces behind the, the relative jumps we have, proposed in EOF. the inspiration there was, optimisms code transformation where they were inserting, code, for external calls. 
* They were replacing that, with some kind of a guarded call. and basically that was the inspiration of how the, the jumps, are designed in EOF, which basically allow code notification, very easily. I think the main, the main disagreement may be in around the, the sheer size of these changes. 
* I think last year we never imagined that, we would get to this point that the EOF all of these changes are considered at the same time, because that many changes were never actually, at least it feels like this many changes were never applied in the same upgrade to the EVM and in the past, basically during December. I think the understanding is that we are probably at the, the limit of, the number of changes we can safely make.  it's not really just about, you know, testing time, but rather having confidence that we can cover all these changes. 
* And I think the, the changes we have in the current version are less related to how op codes operate. and they're more related into just the general container format and validation, you know, as a lot of this was already mentioned by, by Martin and others on this, this call, regarding that date. and so if we would, consider splitting, the kind of changes in the two parts. 
* The first part would be what we have currently under EOF three one, which mostly considers the, the container format and validation, but doesn't actually change, you know, a large number of op codes. it seems like we can, you know, with more confidence test these set of changes, and then implement and test the second set of changes which revamp.
* I think a significant number of op codes. in, in the document I shared, I took it actually further than, just account code introspection, because we had a number of, features, on the wish list, which are currently related. the reason coding introspection is needed  in contracts today, is basically twofold. Most of the time they want to read, data in the contract, and the data can be, you know, just predefined data, but it can be also, something called, immutables in solidity, which in practice are data fields which are populated during the creation time. 
* So during runtime they act as constant fields, but they're still fields which are right ones during creation. and the other case where there is some kind of an introspection happening is, is creation itself. because we have, we don't really have a specific transaction format or specific, separation of, of how code and construct arguments are handled. the way this works today is. 
* It is just a practice by solidity, by the solidity compiler that it depends the construc arguments at the end of the code. so the, basically the code has like three sections today. during creation, you have the DNET code, which is ran, and, and the, the counter creation context. Then there's like the runtime code concatenated after it, and, and finally it ends with any potential construct arguments. and this was already on the wish list to, to maybe we should revamp this. and I think this, this kind of ties into, account code introspection, but this requires potentially new transaction format changes to the creator codes. and if we do this kind of changes, then I would propose that we actually go one step further, and we also try to eliminate, you know, gas introspection, which, which then boils down to redesigning how the, the coal up codes operate. I give some rough ideas, regarding direction for all these changes in the document. but of course by no means these are, you know,  fuel and mature. yeah, I just want to conclude that.
* I think I see like three different paths we could go. one path obviously is, you know, just going with EOF 1s, it is without any changes, and then, working on EOF V2, which may mean that there, there may be, you know, a few number of op codes, which, would have to be supported in V1 and would be banned in v2. there is a second kind of path where we could decide that we disallow some OP codes like creation in v1, but we make a strong commitment that we want to make a decision on of how creation should work and by the next upgrade, or, you know, soon after. And then we can choose two paths. you know, we may end up thinking that the creation as it is, is good enough, so we just enable, the create codes sdr, or we could decide that we actually want to do this new version, which was proposed in the document and, and work on that instead. and the last path, what has been mentioned is, is yeah, practically delaying and, and, delaying V1 and thinking about how, whether we could integrate the, the two changes into a single rollout, or if not, then it has to be to two rollouts. 
* Again, I personally don't think there's any potential way to roll all of these changes out at once, as I explained earlier. so that would mean that, you know, this would be delayed for two, three, upgrades from today. I think that's my long explainer of the document. 

**Tim Beiko**
* Thank you. I guess, yeah, I'd be curious to hear people's thought about kind of this whole spilling of the, the roadmap, like with just any reactions to Vitalik and Alex's proposals? 

**Micah Zoltu**
* Yeah, I think unless we have a solution to the current EVM and making it go away, which I do not see a path for that we are always going to have to deal with at least this version of, even if we can make it so we only have to deal with this version of the evm and then the latest, but not everything in between.
* We still have to deal with this version of the evm, which is like the worst of all of the possible ebms we could come up with, right? Cause we, it was the first one, didn't get a perfect on the first try. 
* And as long as we have that problem, I feel like we have the general problem that we need to solve a multiple version of the evm. And if we've solved the general problem of multiple versions of the EVM in production, then it's not that big of a leap to just support all of the intermediate ones as well. Like, I don't feel like we're gaining that much unless we can get rid of the Currents version EVM, which, which again, I don't, I don't see a path to that. 

**Vitalik Buterin**
* I mean, inversions is a lot more than two though. Like, especially over assignment, especially over the 20 year long term. 

**Micah Zoltu**
* Sure. So inversions is definitely worse than two versions, but I think that the difference between one and two is, you know, massive, the difference between two and three is very marginal, and difference between three and 20 is a little bit more than marginal, but still nowhere near that first massive jump from one to two. And so the question then becomes, okay, so if we're not getting that big massive gain, we're only getting like a series of intermediate kind of marginal gains, then maybe they do add up to some amount. is it worth all the effort? Like, there's a lot of effort that goes in into this. 
* Like every single time we wanna upgrade, upgrade the evm, we have to think about, okay, how do we transform everything? Like we have to actually solve that transformation problem for every EVM change, which is not trivial. Whereas if we just accept, you know, we have all these evms, then we don't have to deal with that problem. 
* And so I'm just questioning is it worth the effort, which is pretty significant if we can't get that big gain from going from two to one, which I don't think we can get. 

**Tim Beiko**
* Dankrad, Oh, Not sure if you have a mic. 

**Dankrad Feist**
* Oh, yeah. I, so I have a very, I mean, like,  I think it's very different. I think like every, like we should, like clearly already this jump from having to support, two to having to support three versions is like, yeah, 50% jump in effort, right? 
* So  I would say it,  yeah, I mean,  I can see, act six arguments unlike it is very hard to make such a big, version jump at once. So I agree that that is definitely a problem worth thinking about, but it's also, it's also really worth thinking about this, this continuous effort that's 50% more having support one extra version of the EVM if we implement, your Messages now. 

**Tim Beiko**
* So Oh, Vitalik. Yeah. 

**Vitalik Buterin**
* Yeah. I just wanted to kind of also again, reiterate that, like I, this is a big, this whole thing is a big decision and this whole thing involves irreversible decisions, and I think it, like, we should all remember that making the right decision for the 20 year, or, you know, 40 year long term is much more important than not delaying things by six, by six months or even one, or even one or two years, right? 
* So it's, look, this, this is definitely something that I think, whichever decision is the right one really, should be thought carefully about. And, if we can make an, irreversible commitment of any kind, like that commitment should, I think have in mind the idea of, like what the actual path is, going forward from there is going to be, I see. 
* Yeah. Like I said in the messages, right? Decision for 20 to 40 years is ossification. I think, you know, if that's true, then like that, what might even be an argument implying that the right dec that the right decision today is to actually, ossify and, basically say the EVM is not gonna change going, like start even starting tomorrow, right? But like, whatever the decision is, the long term should be.
* Yeah, I think really, thought about as the, the primary issue, right? 

**Andrew Ashikhmin**
* I think, I'm just afraid if we delay EOF, until it's perfect, then we'll lose. So none the opportunity to get actual feedback because, trying to make,we can't get something theoretically possible, perfect, before actually, putting it, to test and to real use, to my mind you have EOF v1 is on one side, it's big enough and on, the other, it delivers, good, good improvements, for, especially, especially it eliminates, dynamic, jumps. 
* So yeah, if we, if we try to make it perfect, then it'll be, like a neverending super project, especially , without feedback from, from real contracts, I would, I would deliver it in steps. 

**Tim Beiko**
* Thanks. Ansgar.

**Ansgar Dietrichs**
* Yeah, so, it, it seems to me that maybe one good path here would be, given that we are kind of shooting for a, for eight, for four fork, I don't know on the three, four months timeline after Shanghai that maybe it, it seems like enough people here have concerns about making a good decision that locks us in for the next 20 years on such a rush timeline. 
* Like, like for Shanghai, we would basically have to make that decision today, that maybe the best course of action would be to pull it out of Shanghai, 
* But kind of commit on kind of actively discussing this over the next few weeks. And then basically making a decision on if we wanna go ahead with V1 as is basically then bundle it with 4444, make that decision basically quickly enough so we can bundle it with that would've to mean decision in within the next three months or so. 
* And if we within that timeline basically are not comfortable with moving ahead, then we can delay it further. But, basically shooting for the, the 4, 4 4 bundle, because otherwise it could slip and then easily I think, or bets off could easily slip. Yes. 

**Tim Beiko**
* Yeah, I will emphasize that. I think if we don't want to delay withdrawal over this kind of like, we decided like whether or not V1 goes into Shanghai is a decision we basically have to make the day. I think if we don't commit to that, then it won't. and then we can figure out like what's the next step  if we don't do that. But yeah. 
* I guess I'd be curious to hear just like from the other client teams, how you all feel about this. I think, Geth, I'm not quite sure get, Mary you had some comments in the chats, but Matt as well, I sort of stopped following, but yeah. 

**MariusVanDerWijden**
* Yeah, so I think the Geth team is kind of split on this. I can only speak to my personal opinion. I feel kind of rushed. I think, and I feel kind of pressured into making a decision on EOF now, and, I don't think that's good. so from what I've, like, I have also not been following the process as closely as I maybe should have. 
* But from what I seen and heard there were like the spec was still changing or is still changing. and, the, the testing is not there where we would like to have it. And, especially, the fuzzing has found issues in, in multiple different clients, and usually we only find issues in like one or two, and then it's, yeah, just the amount of issues and the severity of issues, are kind of a concern to me generally. I think the, splitting into EOF one and EOF v2 is kind of a good idea. 
* But I am, I don't feel comfortable, putting EOF the one into Shanghai right now. That's just my personal opinion, and I think some people within the Geth team might disagree. 

**Tim Beiko**
* Does anyone in Geth wanna take the opposing point of view? 

**lightclient**
* I don't think I like fully oppose that point of view. I think that the reality  is that the timeline that we went for Shanghai is going to have to be extended a bit to support getting EOF testing into a place where people are comfortable making the upgrade.
* How long that is, I don't know, I don't think it's like more than maybe one month's time, but that still like brushes away the fact that we have these questions about code introspection and, you know, other small things that are irreversible and people generally feel rushed.
* And I felt maybe one and a half months ago that we, by doing EOF in Shanghai, we were pushing ourselves a bit as like a development group, but it was something that was like very much within our capacity. And now I feel  like we're kind of like reaching like what our capacity is to do. So if the timeline for Shanghai is not extended, then I don't think that EOF it is like that we can like responsibly ship this EOF upgrade. 
* It's, yeah, a question of whether it's important enough to talk about extending the Shanghai deadline a few weeks a month. 
* But if we're trying to do main net test net upgrades in the beginning of February, I don't think that we're going to be ready by then. 

**Tim Beiko**
* Got it. Thanks. Anyone from Nethermind or, or Besu want to share? Oh, Daniel. 

**Danno Ferrin**
* So for me, the part where I thought is probably gonna slip is when we, worked with Solidity and discuss the needs of them being able to attend their constructive parameters to the blocks. EOF was designed to be seal, it's not designed to be extended at deploy time. so there are d to be design changes to support that.
* We could do a hack and say that it can be extended for knit code only. Maybe we could enshrine that, but I think that's gonna take more testing and that, that discovery came fairly late in December. So that's, you know, this whole issue of introspection, may or may not have did come up kind of late. 
* I'm not sure if it's, you know,  what's the harm of making the entire initial deploy block the data block for it? I think there's ways around it that don't involve necessarily intro inspecting it and shutting down the copy. 
* But as far as an actual practical usability, the whole inability to append constructive parameters, especially array types, I think, is for me, what Warren's pushing it out to Cancun. 

**Tim Beiko**
* Got it. Thank you. Andrew? 

**Andrew Ashikhmin**
* Yeah, I think, that, verifies my initial concern that we do need, kind of a production ready solidity compiler into EOF so that we actually are sure that it's, it works fine  with solidity. So I'm currently thinking might be a good idea to delay EOF v2, Cancun and, and to make, like proper solidity compilation, a requirement. 

**Tim Beiko**
* Okay. And then thank you. And then, Amen from, Nethermind has also said, I'd rather not have EOF, included now and, and would rather push it to Cancun. 
* I thumbs up from Lucas. So I think it's pretty clear that, yeah, not, like, not include in EOF in Shanghai seems to be the consensus. so anyone like strongly disagree with that. 
* Okay. so I think  it seems like because there's all these proposals that are kind of floating around, it's probably a bit early to make a decision about like if and what we include in Cancun. 
* I'd rather we at least wait like a call or two before deciding that. 
* And also just like, I think part of , the kind of issue that arose with EOF is like, we made the decision to include it partially in Shanghai, super early in the merge work, and then people were kind of caught off.Sort of included really early on. so I think it would be good to like not make the same mistakes here. 
* So, yeah, I, you know, maybe on the next call we can decide to put it in Cancun, but I think it's good to have at least two more weeks for people to discuss all of this. and, and whether or not they should be coupled with, with 4844 or, yeah. or a separate fork. I kind of saw you came off mute. 

**lightclient**
* Yeah, I mean, I was just gonna say that if we already had pretty good agreement to try and do EOF for Shanghai, I think it would be okay to just try and, you know, still have pretty good agreement that we're going to try and do it for Cancun. 
* And of course, like we can like make a call later on once we get closer and we realize like what the situation is. But I would be curious if anyone like, feels strongly that they don't want to make a commitment that we're trying to do EOF for Cancun. 
* Cuz I don't want to get into the situation where we had with EOF I don't think that we would've been able to like, realize these things about EOF without having all of the client teams implementing things and having as much momentum around EOF, having solidity like working on this implementation. And if we don't commit to it again in the future.
* Then we're gonna end up again the situation where we have just the Epsilon team working on it and then client teams look at it two months before they want to have it finalized and we like realize these things and Solidity starts working on two months before and we realize these things. 

**Tim Beiko**
* Right. Maris is how you had your hand up. 

**MariusVanDerWijden**
* Yes. I really don't like to do this, because I think,  has like kind of been pushing this, EIPtoo hard. but with u f out of Shanghai, I think we should, consider 1153 to move to Shanghai. It's  kind of a small change and, it might be possible to be Okay added to Shanghai. 

**Tim Beiko**
* Let's wait. Okay. We can discuss that in like five, 10 minutes. I just wanna make sure we wrap up EOF properly before, but Sure. We can discuss anyways. Yeah, let's discuss that right after. I think just to come back on what Matt said I think I agree that like the momentum and the client focus has been really valuable and, we should keep like, working on it as much as as possible. I just would not like, I just would not want to like, commit it to the like fork schedule, like right now. but if, I don't know if all the client teams feel strongly that we should, we can go ahead. yeah, I don't know if there's any more thoughts on that. 

**lightclient**
* I feel relatively strongly that we should make the commitment, but, I don't know if  others feel the opposite. 

**Andrew Ashikhmin**
* Andrew, I think that, we should, well my preference is still to split, like not to try to reach a perfect state of EOF. We can try it, but, I'm just afraid that too big a change, would be, would, so it's be, in my opinion, it's better to move  into smaller steps, but, I would commit EOF to, Cancun, but with the requirement that, like we have a fully working, solidity com compiler into EOF and that the Solidity team is happy with it and everything works fine, and if that's not ready by Cancun, then well delay it even more

**Ansgar Dietrichs**
* Yeah, just to say basically  I do think it is important that we still kind of keep an open mind as to this whole kind of B one split and whether or not we would even want to do this. 
* I think, I don't know, I thought actually had good, good points on why it might be a good idea, but like, I think basically what we should commit on was just we should make sure that for Cancun, UF does not, not get in because we are not ready again, like we should, at least if we, if we end up not including it, it should be just because we decided that actually ba bundling everything into a combined b2,  is the sensible thing to do. Like, there's enough time between now and Cancun I think that, that we should be able to fully explore and make that decision. So I think that's the commitment we should make. 

**Tim Beiko**
* Okay. and Moody, I see you have your hand up as well. 

**moody**
* Yeah, I just wanted to have a, I think it would be good to do some real world gas testing for EOF, just to actually measure the benefits before forcing out v1 just to make sure that there's an actual reason to use v1, and people won't just continue to use Legacy code. and I'm actually working with Daniel from Solidity to do that for v3. so hopefully we have some numbers there. 

**Tim Beiko**
* Got it. 

**Alex Beregszaszi**
* And yeah, Alex, Yeah, I mean Daniel from Solidity actually implemented, all of the EOF EIPS and grand benchmarks regarding gas and even with that having optimization steps, which means, you know, de duplicating and optimizing everything. Even without that I was using less gas. 

**Tim Beiko**
* Okay. I feel like okay. Just to not also spend the entire rest of the call on this. I think if here we wanna remove UF from Shanghai, I don't think waiting an extra two weeks to make a specific decision for Cancun will like, change anything or slow down the progress massively.
* I think, you know, it's clear that like client teams are working on this now and we, we should continue that. so I feel like we should kind of continue this conversation about like Cancun and V1 versus V2 on the next call, but kind of leave it at that for today unless anyone feels there's anything else we didn't cover that's like really important that we should go over now. 
* Okay. so I'll do that.I'll do the change, in the, the spec, right after this call. the next thing. Okay, so Marius, what you brought up, so if we do remove EOF from Shanghai, do we have the bandwidth to add anything else? * And if so, what should we add? so after your comment MIRIs, there were a couple comments in the chat about we should probably just be removing stuff at this point. yeah, so I guess I'd be just curious to hear from client teams, like how they feel like, does any client team feel strongly that we should add things or does everyone, does everyone prefer only removing things, at this point to keep the scope kind of  in check? 

**Danno Ferrin**
* Daniel, So the reason for  cutting it is so we don't delay things for withdrawals. And my concern is if we add anything that's something else that might delay withdrawals. Withdrawals is the driver of Shanghai, so whatever decision we make should be done with the point of getting withdrawals out as soon as possible. So based on that, adding things only adds risk. 

**Tim Beiko**
* Okay. So if there's more basic support for cutting only some get support for cutting only, I don't know, another minor gone any strong opinions? So this is about adding 1153 Or Yeah, potentially 1153, but just generally adding things at all. 

**tukasz Rozmej**
* Yeah, So if we want to add something, we should, have a fairly minimal impact. 1153 might be in that minimal impact. If every team like reviewed the code and the tests, then it might be a minimal impact thing. but otherwise probably we won't, we don't want to add it if it's not. So it depends if like every team can spend a bits of time reviewing it. 

**Tim Beiko**
* Got it. And argon No strong opinion on 1153. Fine. Either way. So, so okay. It seems like 1153 is like the only one that could be considered. 
* Is this something that we need to make a decision about today or would people be more comfortable like thinking about this in the next two weeks and potentially making the decision then? 

**lightclient**
* I feel like if we're targeting early February public test notes, we should make a decision now. 

**Tim Beiko**
* Okay. 

**Danno Ferrin**
* Early February test set is aggressive. Any new ads, I mean, taking a EOF is gonna be enough risk, warranted risk, but I think adding something else that hasn't been part of previous test match or structures, even if something as good as 1153 is, is unnecessary risk in my opinion, willing to be overridden, but I still think it's unnecessary risk. 

**Tim Beiko**
* Okay. And there's more comments from the other Nethermind and in the chat as well, so I think Okay. Then that's just focus on removing EOF from Shanghai, keeping the scope, tight. So, yeah, so we don't delay withdrawals. okay. 
* I think, I think that's pretty much it for Shanghai. Anything else on the fork that people wanted to discuss? Okay. If not, couple other agenda items. EIP-4844 updates. I know there's been a couple community calls. 
* I don't know if there's any updates that, people wanted to, to discuss. Okay. Nothing on for forward. There'll be another call, next week, where we can, where we can discuss this. there was a proposal, by Eaton on the status team, to Add hexary trie roots for lists in ExecutionPayloadHeader. Heather, I dunno if Ethan is on the call right now. 

**Etan (Nimbus)**
* Yes, I am. 

**Tim Beiko**
* Yes. Okay, awesome. 

**Etan (Nimbus)**
* So the problem there is, sort of related to Shanghai because it also affects withdrawal, but it's not, strictly necessary to solve it with that work as well. So, it is about light clients. they currently can follow a gossip topic to stay up to date with respect to the latest beacon block header from the consensus layer. 
* And we would like to extend to also include the EL blockhead so that you can follow that passive stream. And then when you detect the block contains for example, some locks that are relevant to your wallet, you can then, request a proof, hey, give me the token transfer that, it's related to that. I have prepared a little graphic here that I shared in the chat and this PDF file. right now the issue is that to get that EL block header, the CL block does not contain all the data. 
* There are two fields in the EL block, header, namely the transactions route and the withdrawals route that are hex, sorry, tri routes in the EL block header. But in the CL execution payload, those hex three tri route, they are just missing because in the CL blocks. 
* Ah, thank you. Yeah. For sharing that. so yeah, in the CL there is like the full transactions list and the full withdrawals list. The transactions, the individual transactions are still R LP while on withdrawals, the actual withdrawals objects are actually also ssc. 
* That also means that they are stored in little Indian, inte and in giga away while in the EL withdrawal route. It's named the same, but it's totally different. It's beacon and in way and it's A R L P N coding antenna hex tri root. 
* So it's, it's not the same data that we have here. And when we want to do a, proof for a transaction or a withdrawal, this then leads to a problem where the like client, it only has the CL execution payload header from that gossip stream. But when it wants to request a transactions proof from a EL, then the EL cannot give it that proof. So, yeah. And the other problem is that there is no way to validate that the block cash within the execution payload at a risk. Correct. Right now as it's used, not really a problem because, we sort of trust the sync committee to only sign valid execution payload headers. 
* But bill, if you just have the headers want to validate, this feels like a bug to me. Yes. if it's possible to fix in Shanghai Sure. For the transactions, like this is the first approach, can we sort of make it so that, that we use the same format everywhere? So for the transactions and the withdrawals that are currently stored on the CL as well, can we just use the same root on the EL side? That would mean adding support for the SSE format to the EL. 
* I'm not sure how the problem that is. right now the risk is nice wall where everything on the EL side is R L P and tax and every single on the CL side is ssc. but yeah, like if we can get it done to add this SSC library to the EL, then this would essentially eliminate everything just single format for the, for the same data. 
* If we do that, then we essentially need to find a way to get those additional hex routes from the CL servers to the CL live clients. And the way that I have here is essentially that the CL could recompute them from the CL block because it knows all the transactions and withdrawals, but that would mean like adding all that legacy code for R L P hex tries and the kza cash to the cls, which is kinda backwards in where we want to go. as far as I know, the S S C format is considered to be more modern. if there is, a implementation that absolutely cannot do that, it could also request the EL block, either VR engine API or the execution api. 
* It's the same, buzz, but that would then compete with, bus that is also used for validator duties. So it may interfere with actual real critical operations. I'm not sure how well that could be supported. the next slide, basically avoids having to compute those on the CL by just extending the execution pillar that we get from the engine api. to also include those hex route, as a route of the transactions is just a simple binary tree.
*  Yes, it is just a simple binary tree. And also as far as I know, those hex tri routes, they are not exposed to the E V M. So there is nothing in the E V M unless like someone re-implement it, like has their own transaction proof system. but I think right now there is no way to extract a transactions route from, from a smart contract. But anyhow, yeah, this, like this light here basically extends, extends the execution payload, the execution payload, Heather, it's an additional storage of 160 megabytes per year. Maybe not that big of a problem anymore with the 4 4 44 history pruning that, avoids adding libraries to the CL. 
* And this final slide says that we just ignore those two values at all. Like the, like instead of trying to get those transactions hex and withdrawal hex, we just have those four minimal items, the parent hash state root block number and block hash. We give it to the EL and the EL then issues another network request to obtain the EL block header based on then if it needs it. And then this, this, this sort of, solves the problem of having this mismatch, but it also means that to operate on the transactions and withdrawals, you need to request actively those additional fields from the server again. 
* So it adds load to the server. And it also means that you can no longer passively just follow the gossip to keep track of the latest text and El blockhead. 
* So yeah, I mean this, this, this, is probably the quickest to do without too much changes actually no changes at all. but it also just, is the least flexible and there is this EIP  4788 that will add the consensus layer stay true to, the el, EL block letter. 
* So it could in theory be possible to just, base transactions and withdrawal proofs on that one, but they would need to be served by a CL and no longer an EL. So you have this situation where for some data you need to ask an EL for a proof and for some other data you need to ask a CL for a proof because the, the EL doesn't know the entire beacon stated cannot create such a proof for a transaction. There may also be split block storage where the transaction is simply no longer there on the cl. 
* Yeah. And also this, this same issue reappears every time we add a new array, so transactions and with withdraw are the current two arrays that have this problem, but every time we add a new array, we have the same problem again. So yeah, that's what I wanted to bring up. And I mean the main question is can we just transition those arrays to A S S C route in the el Like is that something where, where there is like a risk or a pushback or

**Micah Zoltu**
* Yeah, I think the risk and pushback you're gonna get from that, is that external tooling might depend on that. So I need any tools to actually try to validate a block, for example, that aren't clients will all have to be fixed and changed deal with it. And that includes on chain contracts that do block validation. We break, Yes. 

**Etan (Nimbus)**
* I mean that's true for the transactions, but I mean the transactions, they could be sort of solved as a one-off workaround by just adding it to the payload as well. But I mean this is more about the new stuff, the withdrawals, anything in the future that could be an and and the receipts route. Actually it is a amputee, like it is a hex try in both the CL and d l. So that one is already consistent. 
* The received route would still be worth changing to a street route. Any layer two, that one to like access messages from a layer one reach these receipts. And so making it easier to verify would be a big win. Also like messaging between different layer twos. Any IFM chain really that emits an event that events could be ingested by another e m chain if the proof was just simple to verify. 

**Etan (Nimbus)**
* Yeah. So there is this spectrum of only changing the new stuff, like only the withdrawals and the new array or also the transactions route because then we have all the fields covered where there is the inconsistency or even more than that, or also just nothing at all. So there is this entire scope and I'm not sure which of the approaches we should follow on. 

**Tim Beiko**
* Just because we're almost at time and we have other things, does it make sense to just move the conversation, to just move the conversation for this, on the issue? Maruis, we can fill over you and then Yeah. Wrap up on this. 

**MariusVanDen**
* Yeah, so I think we need somewhat time with the EL devs to, to discuss this, offline. Okay. But, yeah, so I, I don't think we can make a decision on it now. and it's also not that important I think to make a decision on it now. We can change it next two weeks maybe. Yeah. 

**Tim Beiko**
* Okay. yeah, let's, let's do that. Oh, Micah. Yeah. 

**Micah Zoltu**
* Doesn't I kind of go, go against the previous statement we made, which is we need to make decisions for what's in Shanghai today because by next week we're too late to make decision for Shanghai. 

**Marius**
* Yeah. But that change doesn't really ma like it only changes the, the block format. It doesn't change anything within the e VM or, Anything. 

**Micah Zoltu**
* Not, not all clients. Correct me, I'm wrong. Not all clients have ex not all execution clients have SSC capabilities yet, do they? 

**Marius**
* We don't. 

**Micah Zoltu**
* So Yeah. Right. So that feels like a sign potentially a significant delay. 

**Lukasz**
* For Nethermind we don't have, so we didn't have a s z implementation, but Alex is, working on something on EIP 4844. So that might be reasonable. 

**Andrew**
* I feel like it is an important question and, we shouldn't delay it. We, we, I mean we can discuss it offline, but because it pertains to Shanghai, it's, and it is, it is a design decision. It's quite urgent to my mind. 

**Tim Beiko**
* So how about, like, yes, I think it makes sense for client teams to think about this offline. we can use the issue to discuss, we can put it on the agenda also for the CL call next week. cuz it's also kind of relevant to them. and at the very latest have a decision, on the next All core dev for this. Does that make sense? 

**Andrew**
* Yeah. Yeah. But, like to my mind it's like because it is a design problem, I would, prioritize it and try to fix it, properly rather than, be left with, some technical debt for Right. 

**Loin**
* For Yeah. One, one note for hesitant execution layer labs, you don't really need to implement a generic s a z if you only implement for these types is much easier. 

**Tim Beiko**
* Got it. 

**Etan (Nimbus)**
* Okay. Yeah. Like you, you need to withdraw object and then you need those, list of  data basically that is the only support that you need. The transactions, they are still lp, it's just the actual three of transactions and the full withdrawals and they're three that needs Yeah. That, that, that would need to change. 

**Loin**
* And EIP 4444 already includes, manual s e manipulation anyway. 

## https://ethereum-magicians.org/t/eip-5483-evm-modular-arithmetic-extensions/12425  [1:24:29](https://youtu.be/SmcMwdHZqg8?t=5069)

**Tim Beiko**
* Okay. So yeah, let's discuss, let's like EL teams, if you can look at this like pretty soon and then, we'll make sure to add it on the agenda for next week's CL call and, and hopefully have the decision before the next All core devs put at the latest make, make a call then. okay. We have six minutes left and like two EIPs that people wanted to briefly introduce. So, let's try and take like three or four minutes on each of those and then we'll wrap up. first, Jared, you had EIP P 5 8 43, you wanted to chat about, are you here, Jared? okay, if not, then Abdel, you had N e I p e i p 5 9 88. Are you still here? 

## https://eips.ethereum.org/EIPS/eip-5988 [1:24:44](https://youtu.be/SmcMwdHZqg8?t=5084)

**Abdel** 
* So basically, it is, it works with a set of permutation, over prime field, and it makes it, very, well efficient for in, in ZK context. And, it'll enable, basically, a bunch of interesting,  use cases, obviously , for layer two and specifically, ZK and roll up. but not only, what kind of, use cases can enable. 
* So first, you can use it as, an efficient and cheap ways of doing some kind of, data availability solution with, using Poseidon, hash commitments. so obviously it's not as efficient of, as 4844 and the future data availability sampling solution, but still it is an alternative solution for, cheaper, data availability, using this new function. also, can use it as a their main function for the state commitments of their, of  the state of their rollups. it can also be used for, escape hatch. basically each time we want to prove, the storage proof like Merkel proof. It's very, expensive, on Ethereum because we don't have any, zk friendly, hash function. 
* So let's say for example, you want to implement, an SK patch, system where if the system, is frozen and you want to, let the possibility to users to, to restore their phones on the layer one, then you can use the system to implement, an escape hatch, system. This is what we plan to do for start net and score is also, planning to, to use it for their exit game, mechanism. and also maybe in the long term, we can use it, for it Ethereum itself, like, having the ability to, prove, Ethereum is history inside Ethereum. So this would be particularly, useful for, storage proofs and, and Lightclients. And also, a lot of use cases. So this is for the potential use cases are also, some, some interesting use cases, on the layer, on on the top level. But, mainly this is interesting for, rollup operators. one, important, design concern is about how generic can it be. this is a main problem of the pre empire, because with, with paramunt you can use it with, multiple parameters, and, many different actors are using different, parameters. 
* So we, we have multiple options, so either we can implement only a set of, known instances and add new instances with, hard forks, or we can try to make something generic. Anyway, this is, one thing to consider. Another, important aspect is, security, because, those, amatic hash functions are, are, are pretty new. So this is also something to consider. 
* So Vitalik, describe a bit, this thing in the PCG alternative article reward, a month ago or something like that. in terms of implementation, we already have a c assembly implementation for x, 86, architecture. we also started, arrest implementation. So, there already some, implementation that exists, like, for example, the Fcon one and others, but, they are not generic enough to fit with all the possible instances. so yeah, there is a generic city aspect, the security aspect, and, yeah, that's pretty much it to, to be short. So we have only one minute left, so I will stop there. 

**Tim Beiko**
* Thank you. yeah, Dankrad had your hand up. I think we can do your comment and then wrap up. 

**Dankrad** 
* Yeah, just a very short comment. So I would generally say as it's a bit early to enshrine any arithmetic hash function in the VM because of you, what you mentioned by the security concerns, and we just don't know enough about them. Yes. so  I would generally that's premature at this point. 

**Tim Beiko**
* Got it. and then there's the Eth magician thread linked to the EIP for people to, to discuss this further. 
* Yep. Anything else before we wrap up? Okay. And I guess, yeah, if people wanna check out, Jared's, EIPs Async, it has to do with EVM monitor or metrics, which was proposed a while back, as VM 384. so I just posted the link for that, in, in the chat as well. yeah, I guess that's it. thanks everyone for coming in and, see you all, on this week's CL call.Thank you. 


