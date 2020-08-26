# All Core Devs Meeting 94 Notes
### Meeting Date/Time: Friday, Aug 21 2020, 14:00 UTC
### Meeting Duration: 1:32 hrs
### [GitHub Agenda](https://github.com/ethereum/pm/issues/200)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=q6bIeSu7r9o&t=2835s)
### Moderator: Hudson Jameson
### Notes: Alita Moore
  
---
  
# Summary
  
## EIP Status
EIP | Status
  
  
## Decisions Made
  
Decision Item | Description
--|--
**94.1.1**: Discuss the possibility of launching a Prog POW on a test net next week in line with the Ben's compromise
**94.1.2**: Move further discussion on precompile to ETH Magicians forum [here](https://ethereum-magicians.org/t/evm384-feedback-and-discussion/4533)
  
  
  
## Actions Required
  
Action Item | Description
--|--
**94.2.1**: Decide, by next meeting, whether to go with Axic's and update the sources that say we're going with EIP 2537
**93.2.2**: Vitalik to start coordinating a writeup on the impact of the gas limit increase (what will it break)
**93.2.3**: revisit the discussion on EIP 384
  
  
## Helpful Links
Link | Description
--|--
**94.3.1**: [EIP 2666 analysis results](https://github.com/ethereum/pm/issues/200#issuecomment-678115862)
**93.3.2**:  [Context on 1884](https://github.com/holiman/eip-1884-security/)
  
---
  
# Agenda
  
<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 bullets:1 updateOnSave:1 -->
- [1. Progress on EIP-1057](#-1)
- [2. Ewasm Team: Findings on "evm384"](#-2)
- 3 EIP Discussion
    - [3a. Vitalik's Idea](#3)
- [4. YOLO / YOLOv2 & Berlin state tests update](#4)
- [5. Raw benchmarks for EIP 2666](#5)
- [6. EIPIP Meeting: New EIP Statuses](#6)
- [7. Ethereum Cat Herders Survey Results](#7)
- [8. Migration from ACD Gitter to Eth R&D Discord](#8)
- [9. Review previous decisions made and action items (if notes available)](#9)
  
---
  
# 1 Progress on EIP-1057
  
Video | [3:56](https://youtu.be/q6bIeSu7r9o?t=236)
  
**Hudson** - Hello and welcome to a theorem poor developer meeting No. 94, I'm your host, Hudson, and we're going to go to the first item on the agenda. Greg wants to give an update on the progress of EIP 10 57. So, Greg, if you want to admit and go through that real quick, that'd be great.
  
**Greg** - Yeah, we've been reviewing it. Oh, gosh. Since about April. We had a small suggestion from. Beast authority on the light evaluation attack and kick found a and exploit in.. there's actually a bug in its hash that crockpot W made just barely maybe exploitable in some future time. But within a few days we had a fix and by about May the fix was pretty well reviewed and tweaked so that it didn't have a performance impact. And soon enough I'll be pointing to a better reference implementation of the the latest for for the WIPA. And it's it's very readable right now. There's some stuff to do, maybe patching up links and things like that, so at the next meeting, I want to actually take that up way back. In meeting EIGHTY-ONE, we published a decision to move forward with it, in 82 we backed off and it was unclear, but the overall consensus was to go with with bans, compromise of just getting it up on tests, nets and keeping it ready, but not making an immediate decision on whether to deploy it. Just keep on it, keep an eye on the state of the network. So two weeks from now is when I want to discuss that. And by the end of the weekend, I'll put up some links to two places to do that.
  
**Hudson** - great. I do want to ask I'm not seeing in the decisions made section in the notes anything about us definitely spinning up testnets for prog pow or spinning up Ropstein or anything specific like that. Did we in your recollection, was there like a specific tests that we talked about spinning up for it, or was it Ropstein or what?
  
**Greg** - No doubt in two weeks, those are the sorts of details we can discuss if we decide to move forward.
  
**Hudson** - Ok, I would say, like I disagree that it is a decision made that we are spinning up tests. That's for that, because from before the meeting, looking through notes and meeting eighty two and eighty one, I, I'll need to look through the videos, but I didn't see any definitive consensus around that. And you even I think you cited a few people who said that they you thought they had consensus around it, but I don't remember them publicly saying anything about it.
  
**Greg** - It's such a mess, the consensus was so rough that we need to revisit that. I know on Twitter vitalik and and on the EIP on Twitter channels, Vitalik and I, you know, sort of agreed that the rough consensus in 82 was was bandz compromise, which lays it out that way. And the current EIP lays it out that way. But it's more detailed decisions we need to make on on what test set to bring it up on.
  
**Martin** - And I'd also like to kind of agree that we did talk about testnets, but I also I really think that's something we need consensus on and it's just a matter of standing up. If that's not those who wants to join can join those who don't. Don't.
  
**Hudson** - Oh, yeah. No, it's not I don't mean that we have to have consensus to spin up a test that we would for Ropstein, probably more so than just a random test that. Would you agree?
  
**James** - And something I have question I have for the groups we've talked earlier about how Rollston is at the point it's worth perhaps restarting. Is that still something that we think about or we still think is the case, or am I wrong that.
  
**Martin** - Yeah, before we go into that, yeah, I just want to answer Hudson's question. So the funny thing is, if we are to if we were to actually do a profile on Ropstein, is that I don't think it would cause any problems because I know first cinching would start with a Herbertson and would immediately see like what strange difficulties is this and it'll get rejected. So it's a lot easier than, for example, if we did the hard fork with an evm change, that's not immediately noticeable when you first think. So there's a difference there.
  
**Hudson** - Ok, cool, and then, James, you were asking everybody about rebooting Robstein or not rebooting Robstein but retiring Robstein, I guess you would say. Right?
  
**James** - I just I remember conversations that it might be time to add Robson is is. It's time to do a different one. But I want to make sure I remember that correctly or if that was actually a sentiment from the group. Like, separate the UAW stuff, just is that something that we're considering?
  
**Tim Beiko** - So one thing I'll say about Ropstein then is what's nice in the way is it has a larger state and I think for at least four fifty fifty nine is one thing we were considering maybe either for it, like even if it's not the real Robstein. But I think there's value in having a network with a fairly large state that we can try things on, but. Yeah, that's kind of the only the only point about it.
  
**Martin** - Yeah, I must admit, I don't pay attention to does anyone know how much does actually happen or.
  
**Hudson** - I see a good amount of daps testing on Ropstein, I have to give Ropstein test to people on a monthly basis.
  
**Vitalik** - I forget was Was ZK game on Ropstein or on Gerling?
  
**Hudson** - Ropstein, I believe. Yeah, actually, I'm positive it was Ropstein because I offered to give them some testnet eth. And they actually are miners on there, just FYI, I just found that interesting. Hmmm, that might be a better discussion for next time about retiring Ropstein, and that can be at the same time we're discussing a possible place for a pal implementation on a test net, regardless of which test net, if that's where consensus lies, which it sounds like there are some people and in favor of that, which is rather easy.
  
**Danny** - Which test net is reddit using?
  
**Hudson** - Oh, that's a good question. Do we know?
  
**Peter** - I think Ropstein. At least the original one, the original post started experimenting it was going to be I don't know if they switched since then.
  
**Hudson** - Yeah, I mean, it is a testnet so if we decide to take it down, people would just adjust.
  
**danny** - yeah, yeah, I think in terms of the reddit one, I think we should maybe get through that competition before we nuke whatever they're using.
  
**Peter** - But we don't want to do so, and regarding Ropstein, I don't think it's it's correct to say we want to nuke it in my opinion, but what we can do is start a new chain and just ask people to start using that. But we can't really stop anyone from using the old one. And I don't think it's nice to just delete support for the old one. So I think if there's an alternative one that clients and on people will switch fairly fast because it's just like the.
  
**Hudson** - That sounds good. Let me see real quick. I'm going to go ahead and lock the meeting because someone came in to try to spam it, OK? It's been locked. OK, so. Next up, so OK, basically just to finish this, so we have the notes, correct, and two weeks we're going to talk about the possibility of launching Prog POW on a test of some kind and and coordinate are in line with the compromise, Ben's compromise that we've talked about before. And with that, is there anything else? 
  
94.1.1 | Video | [13:24](https://youtu.be/q6bIeSu7r9o?t=804)
  
    Discuss the possibility of launching a Prog POW on a test net next week in line with the Ben's compromise
  
**Greg** - I'd like to hear from Axis before I have to run 
  
**Hudson** - oh, yeah, that's the next item I was meeting on the on the agenda item one. Sorry, I should've been more clear. Agenda item two is the Ewasm team's finding on EVM384. Axic, if you could just go over that real quick and see if anyone has comments.
  
# 2. Ewasm Team: Findings on "EVM384"
Video | [13:40](https://youtu.be/q6bIeSu7r9o?t=820)
  
  
94.3.1
    [EIP 2666 analysis results](https://github.com/ethereum/pm/issues/200#issuecomment-678115862)
  
**Alex (Axic)** - Yeah, so some of you may remember a few probably end of May is when we presented this idea initially with some some first findings and just a follow up to that, it is much more clear about what we have done and what could be possible with TVM trade 4. Now, the document is quite long and it starts with a lengthy history section. I think it has really nice, interesting tidbits of information. So I would suggest for anyone who has the time to actually read that part, but it also shows some of the motivation might be to consider doing this in the first place. And some of those motivations mean some. Iowa experiments which showed that it may be possible to actually implement some of these things if we have a speaker on top of the EVM successfully and then we delve into the the actual goal we are trying to achieve is to support some operations of the last 12 three eight one, which which is the curve by two and also wanted by a bunch of serology protocols. So what we are trying to achieve here is to to support and propose an alternative to the EIP 1962 and the 2537. Now, if you read this document, it might be confusing because we start with my family first. The main reason we have this assembly bit in here is that there's no implementation of BLS 12 on the EVM at all. So there's no way to benchmark and initially confirmed that this experiment would be useful. So what we did first is we took over the assembly implementation of this curve and more specifically, the pairing operation and the benchmark that is and it was an interpreter and compared it to native native speed. It was 100 times slower. And the next thing I mean, this is obviously not useful for anything. So next thing was to find benchmark and find the profile as this was an execution, find the bottlenecks themselves. After having identified those bottlenecks, we added host functions to Web assembly, which you could think about as precompiled. And actually just three of those functions here and Montgomery multiplication and then addition and subtraction, house functions. And with those in place, we were able to get to 2x slow down compared to native. And this was only used to give us an initial indication that this direction is useful. The rest of the proposal doesn't depend on the assembly at all. Don't be confused by that. And now even try it for we don't have a final proposal here, but we explain at length what the problems are and what potential solutions are there for introducing these three functions I mentioned. So, of course, with BLS 12, you need to have these operations on 384 candidates, one with numbers. And given the EVMs 256 bit, we cannot just use a stick item to represent these numbers in the computation we could use two stack items, we could put them into memory, etc.. So we describe all these different options and we choose one option to implement. And we describe all these different options, but what we ended up doing and we also have links to implementation in ETH 1 and solidity so it can be compiled. And now the next actually interesting part here is what we call the synthetic loop, is that we haven't actually implementing implemented a pairing operation, any of them using to see them wait for instructions. Rather, we have created an approximation to a two point pairing, but two pairings. And this is what we call the synthetic loop there in the appendix of the description, what have we arrived at the synthetic loop and the benchmark show that the synthetic loop is reasonably approximating the pairing, but it is a tiny bit slower. So we use that adjustment factor in the final comparison. So the next part then explains that the three different versions of of these events wait for instructions how the speed evolved across those three different functions. Those were the only optimizations we ever did. So the synthetic loop was implemented on the EVM and written in Yul, which is a language developed by the solidity team. And we haven't done really any optimizations on that implementation. We only use the default optimizer settings of the compiler and haven't fully spent any more time on it. We did, however, optimized these new instructions. We did two different optimizations and by those we were able to cut execution time by half. And the end result was that where we stand right now is compared to rust compared to native. We are at the slowdown and then the conclusion that you can read or you know what we think this means that we trying to summarize it a tiny bit. There is a lot of space remaining for optimisations, first of all, this Yul implementation of the synthetic loop is definitely not optimal. You will has an issue with optimizing access. So it does have a lot of overhead. Regarding that, there is one other language, more like an assembler for your EVM called Huff, which has been previously used successfully to try to really optimize code. And we think if a pairing operation or event doesn't preclude would be implemented using huff, we definitely would get a large speed-up. And then there is also other options to to improve to these specific instructions themselves. I have listed those. We have listed those in the conclusion. Regarding the next steps, The best would be to have three operations from EIP 2537, the pairing and the two multi exponentiation implemented using these instructions, because that would allow us to actually find the best design for this event, wait for instructions. And our hunch is that we would we should definitely be able to to be the WASM numbers, which is a 2x slowdown, but I think with optimisations we could even get closer to negative than what we have seen with with this was an experiment. And what that would mean is that there is a good potential that using these three instructions, we could actually support the entire feature set of the BLS bell curve and we wouldn't need those precompiles introducing each of those features separately. And last thing to note is that it would be possible to also support another curve, the BLS 12 377, but potentially other things which would require operations on 284 bit numbers. I think that's that's a summary. I'm not sure if there are any questions.
  
**Alex Vlasov** - Yeah, I'm curious, what do you think it will be possible to reach a performance which is like maybe 20 to 30 percent, just only 20, 30 percent slower, an easy one, because it's already an expensive operation and being four times more expensive is maybe just killing.
  
**Axic** - Yeah, I don't know whether you could reach 20 percent. I think you definitely could reach just twice as low, that definitely would be in reach. But I would say not too much effort. But I'm sure with enough effort put into it, you could you could get really close.
  
**Danny** - So you answer one of my questions, which was 384 seems like a pretty specific instruction set, and if there is anything else that would be worthwhile to use the more low level operations which said there are other curves and then is one of the primary reasons for investigating this, the reduction in complexity. Is that is that a driving factor here?
  
**Axic** - Yeah. And. Yes, as we have seen, it's been quite a long process to introduce a large set of recombines.
  
**Danny** - Right. And so this maybe also serves as a. Roadmap for how we might have a framework for how we might view introducing crypto parameters in the future, looking at more low level operation.
  
**Axic** - Yeah, exactly. We actually give an example that you could I mean, exactly what you said you could you could use this as a template for any future work. Another interesting tidbit is that with any pre compiled, we introduce whatever algorithm that we compile is implementing a what of optimizations that we compile. As for the curves, that is most likely looked down at the time of the introduction of the pre compiled. And maybe in many cases it's not possible to apply any any improvements unless there's a consensus to do so. If you only have these primitives or primitives like this, then there's there's no need to have consensus in applying any any further optimizations on the curves. It can be done on EVM.
  
**Alex Vlasov** - I would highly doubt that that's the case for at least simple arithmetic and Bering's, but maybe for other ones, like it would maybe affect the fact that if its draft changes or maybe maybe of that point into the curve, then yes, it would be easier to update just the solidity code or just low level assembly, but basically phoenix, which is largely used for pairings and multiplications and additions. If there were some end users and this is a recent update an algorithm and to [?], answers should always be consistent.
  
**Martin** - And so my five cents, I think this is totally in the right direction, because having these really large, really complex precompiles, which also has this slightly quirky, cool semantics where you can call them aesthetic calls, delegate calls, alt codes, and there can be errors of various types. I just think it was just the complexity. So we've been doing some for the last couple of weeks, maybe gaspers nethermind found two consensus issues regarding the BLS precompiling, not in actual math, but in the basic call semantics. Um. So I'm a little more positive towards adding this small primitives as the.
  
**Vitalik** - And and just, I guess, a matter of seeing just how efficient we can make the simpler primitives be, like if we can get close to any of the native efficiency, then we could definitely get away with just not having any more precompiles in the future.
  
**Hudson** - And then I think, Greg, you have something. 
  
**Greg** - Yeah, I was looking way back. We've got the A, B and C and three and four section. and here we've gone with, you know, just 384 bit numbers in memory as opposed to using two stack items, which would let you do, I guess, up to 512 bit. Arithmetic and the main issue there was just stack pressure and a separate option to talk about is the stack is just very small compared to the size of the caches on not current ups. So making a bigger stack could remove stack pressure is a design problem.
  
94.1.2 | Video | [28:13](https://youtu.be/q6bIeSu7r9o?t=1693)
  
    Move further discussion on precompile to ETH Magicians forum [here](https://ethereum-magicians.org/t/evm384-feedback-and-discussion/4533)
  
**Hudson** - Ok, I think if we can move this to the theory of magicians form, if you go on the agenda and click on the agenda item, you can see the magicians form that's linked. And I think it's also linked in the actual EVM three eighty four post, but it's also in the agenda under six comment. Do you have anything final to say, Axic.
  
**Axic** - Yeah. Yeah. Just to close this off. It would be really nice if whoever is interested in exploring this further and has experience with implementing BLS 12 or any other curve operations, it would be it would be really nice to work together; people who'd be interested in helping optimize the code and maybe come up with optimizations on the construction side. But we would be looking forward to someone who is capable of implementing the actual logic on the EVM itself.
  
**Greg** - This is really nice. So thanks for this, I've finished moving across the country in the middle of a pandemic so I can try to spare some more cycles on this. Thanks.
  
**Hudson** - I do want to say.. go ahead, James.
  
**James** - Does this how does this fit in with the subroutines EIP that you proposed earlier, Greg?
  
**Greg** - it's independent
  
**Hudson** - yeah, it's independent, my question was does this through EIP 2537 out the window for berlin, this would be in its place, right (others say yes)? This is something we should this is something we should probably decide on pretty soon, then like by next meeting at the latest, if not just offline and chat, because we would need to update a lot of different sources that are saying we're going with the twenty five, thirty seven and then also start work on implementing this if we're going to put this in the Berlin. Am I correct there or.
  
94.2.1 | Video | [30:11](https://youtu.be/q6bIeSu7r9o?t=1811)
  
    Decide, by next meeting, whether to go with Axic's and update the sources that say we're going with EIP 2537
  
**Alex Vlasov** - I think the biggest issue would be if performance, which is kind of acceptable for this kind of operations, will be reachable for use in this approach or not. Because four times (greater than native) is very expensive. I mean, verification, it would take one quarter of the block, I think at least.
  
**Axic** - It's more like three times, not four times.
  
**Alex Vlasov** - Well, I mean, it's still an order of.. like right now verification of plumptre on this completely different curve is half a million guess plus minus some optimisations with BLS, which is quicker. And with this penalty on top, it would be a factor of two just because it was Kebir and another factor of three. So it will be three million percent, which is kind of totally. I would say totally unacceptable for this kind of applications. And this wouldn't be a solution.
  
**Martin** - Right. So just to add to that, I don't think we should consider performance in those kinds of absolutes right now, we're at the point where state access is too cheap. We're going to have to rebalance it, which is going to mean that computation will. From where we are at now, we will favor computationally intensive over intensive operations. So...
  
**Alex Vlasov** - Yeah, I mean, there was this question earlier, like how much time was spent by some miner to actually evaluate also transactions the block and assemble it. And if it's done this way, we'll just like it will increase this time. In some edge cases, if is maybe and like you block this changed and a block is overfilled with one kind of transaction and not another. So it's still questionable. I, I would even say that any.. miner who wanted to risk his profit, he would just swap also the sequence of operations, which is basically being implemented with this set of op codes by some huge function, which will just read the memory and do it natively and then just give the same result. 
  
**Hudson** - Would this be a good time? Martin, would that what you just said, go into the italics idea that he posted earlier in the chat? Is that what you're talking about?
  
**Martin** - yeah, that was what I referred to.
  
**Hudson** - OK, in that case, let's just go into that topic because it's very related to the rest of this and the topic, if you could go over your idea and then we'll do YOLO after that.
  
# 3. Vitalik's Idea
Video | [33:38](https://youtu.be/q6bIeSu7r9o?t=2018)
  
**Vitalik** - Yeah. So basically the thing that I'm proposing is just to do that kind of fairly quick and dirty short term gas cost changes to increase the gas costs of op codes that touch storage. So this includes SVO, this includes the entire ETS family. This includes the entire call family, with an exception for pre-compiles and for contracts that have already been touched when accessing this transaction. The idea would be that the cost of those upgrades can be bumped up to some number that's needed between two thousand and three thousand. And the reason why I think this is valuable (and there's two reasons) one of them is it's a kind of pragmatic, short term, kind of short term security improvements to the chain. So there have been and especially with increased gas limits, there have been a lot of concerns around kind of dos attack transactions that basically try to make bloks take as long as possible to process by focusing entirely on storage accessing operations, which seems to be the most kind of underpriced thing in that regard. And so just that kind of heavily bumping up the gas cost of those operations would decrease that cost by a factor of something like three, which would be a kind of very useful corrective for what's what's happened since from both the recent gas limit increases and just kind of the passive increase that that's been happening in the future historically and will happen in the future because of the state size slowly going up. So that's the first motivation and the second motivation is that in the long term, we do want to have bounded witness sizes, including four fully Stateless clients. And this is something that's useful, for example, in an ETH 2 context and in the context of being able to have community sphere of verify, verified, logs that aree able to experience the multiple shards and so forth. And the Regenesis road map does give like does include a future for bounding gas costs in the context of partially stateless clients. But in addition to that, bounding witness sizes for nodes that are completely stateless are also becoming important. So basically this would end up serving both of those functions of short term scalability and or short term security improvement and medium term pushing the ecosystem toward more witness optimization would both be served by this. And it's a fairly simple change consensus wise.
  
**Hudson** - All right, other comments on this. 
  
**Alexey** - Yes, I have a suggestion here, so I have a kind of this is the generic kind of thought about all this. So we've tried to do this before. The bump up the remember, the latest EIP was 1884, right. When we bumped up the price of your operations. So the question is that since then the bogusly came up as well. So I think not probably as it used to be, eight million when the EIP was introduced. Now it's 12 million. So it's 50 percent increase and the bump was three times. So do you expect or does anybody expect that? Simply not. I think basically after this bump, we're simply going to have just a much larger gas block limit.
  
**Vitalik** - It's it's definitely not my own intention to push to push for much higher gas limits or where it will actually be even clearer, like I personally would oppose mining mining for trying to increase the gas limit to a number that's even higher than that than 12 and a half million. The goal of this is to kind of compensate for things that we've already had and at the same time recognize that even the eight hundred, eight hundred level and the seven hundred level that we chose six years before that, we're probably still a little bit too low.
  
**Danny** - Do you know the time and estimated time crossing the like, worst case, just like right now?
  
**Vitalik** - My understanding is that it's something like 30 seconds in my my proposed numbers would push it down to about 10.
  
**Alex Vlasov** - I don't know if someone has a statistics on how many calls on average, does one transaction make a I assume, taking into account a limited contract size and current approach to modularity with a lot of delegates calls, would it potentially impose a burden on a modern style of making smart contracts that will make them more expensive, especially something fancy, one like dex aggregators or just hexes themselves? So there is some statistics like this. 
  
**Vitalik** - Yeah, so. We actually do have a way of estimating this indirectly in the way that we do that is that we've we we've done numbers on estimating witnesses for the purpose of kind of one point X stuff. And so we've get we've gotten witnesses. So I think is somewhere around six hundred, six hundred kilobytes or so. And so from those numbers, we know that the number of these calls is going to be such that. I think as I as I recall, it would be somewhere, somewhere in the mind of 10 to 20 percent, 10 and 20 percent range in terms of how much more expensive average the average things would get. But then we could definitely estimate this more precisely.
  
**Alex Vlasov** - kind of related question. But it's more from a little perspective with the. Looking at the location on the desk would still it would have like highlights defined dnd start with it, but then you would get a huge batch of data potentially for free. Would it be reasonable to maybe increase the contract limit a little to kind of compensate that?
  
**Vitalik** - I mean, I'd definitely be happy to like I would personally definitely be OK with that and then well, the thing that we want to keep in mind also in the long run is that in the long run, we would probably wants to move toward a regime where contract contract code has either a much larger limit or no limit because we have code virtualization and we will be charging for a chunk. So and and in that context, like basically having your code be in one contract versus having your code being split among a bunch of a bunch of different addresses would be it would be almost equivalent potentially. But I would definitely see in terms a personal with a slight increase in the max contract size, especially if it helps alleviate the effects to developers.
  
**Hudson** - Ok, Barton, did you have something? I think you're muted, Martin, if you're talking.
  
**Martin** - Oh, yeah, I didn't know it was my time, so I just I mean, this proposed change, I'm all for it and it's technically very simple. And I guess the big problem is that this is something the community knows. It is going to break stuff up. 1884 broke some stuff. Most of it could be fixed. If we bump it from 800 to 2000, some things will be irrevocably broken. Yes, it's kind of like we have to just decide, yes, this is worth it for the future of Ethereum. And I think. You know, um I just want to get your thoughts on that. I think it's worth it, but still, 
  
**Vitalik** - In terms of the classes of things that would break like the mean, the biggest one is like twenty three hundred gas calls that are that do a storage look up, followed by a log, right. Do we know, like they also knew of a [?]?
  
***Martin** - I would say so, but one and also law at things which are linked to the security considerations for the it for 1884. Uh. Yeah, it's a little of storage fuck ups and then there's about twenty three hundred gas.
  
94.3.2 | [Context on 1884](https://github.com/holiman/eip-1884-security/)
  
**Vitalik** - Right, 2300 gas things can't cause state changes, so that would not end up causing coins to get lost.
  
**Martin** - No, right, but if you have a wallet which accepts ether.
  
**Hudson** - So in my opinion, what we would need is a write up on this, similar to the really excellent one that Martin did for1884, that would outline the reasoning and what would break as two of the primary things of the write up and then also an EIP would need to be written to, I guess, propose this in the first place. So Vitalik, did you want to do that.
  
**Vitalik** - Yeah, and I'm I'm definitely happy to talk to more than anyone else who wants to reach out and start coordinating that.
  
94.2.2 | Video | [44:13](https://youtu.be/q6bIeSu7r9o?t=2653)
  
    Vitalik to start coordinating a writeup on the impact of the gas limit increase (what will it break)
  
**Hudson** - Yeah, because I know it's going to get really sticky when we say things are going to break, because it was already a it was already a kind of thing to educate the public about whatever 1884 happened. So getting the getting all the information on document before actually telling everyone this might be a thing would probably be better. I say that as only 50 people watch this so live. So I'm guessing not many people are going to figure it out. I guess Tim has his tweets. But yeah, either way, let's get it on paper and go from there. Anybody else have any comments on that?
  
**James** - I think there was a proposal floating around for increasing the contract size limit. Does someone remember who or if that was a thing?
  
**Vitalik** - so, that definitely is a thing that's been floating around in the context of happening simultaneously with code merkelization. I'm not aware of it in other contexts, though.
  
**James** - Ok, I must be remembering the ETH1x stateless details during conversations then
  
**Vitalik** - Yeah, it's like the thing with commercialization, right, is that if we switch to zip code is more Margolyes, that if we charge for a chunk and if we load the witnesses by chunk, then there would be like code would basically functionally be another kind of storage. And there would be and basically no harms from a contract storage unit going all the way up to like a gigabyte if we were to potentially allow creating a contract over the course of many transactions. So, That's a thing.
  
**Alexey** - Yeah, and also the reason why, you know, if it would be harder to do it right now is because you would need to have a very weird pricing for the call for like for the call, for example, because you you would not be able to predict pretty much like how much the coal is going to cost. But if you do it in the context of witnesses, than the witnesses already will be charging enough for the for the for the depending on how much code you're actually using. And the same kind of goes into the the the proposal that has been discussed for raising the cost of the, um, the certain operations is, of course, if you look at the future that, you know, if we had the something like, say, Ethereum regenesis already, that wouldn't it wouldn't have been required. It's we only do it because we can't do the other things quick enough.
  
**James** - Thank you, that's really helpful. 
  
**Hudson** - OK, anybody else on that before we move on?
  
# 4. YOLO / YOLOv2 & Berlin state tests update
Video | [47:15](https://youtu.be/q6bIeSu7r9o?t=2835)
  
**Hudson** - Ok, from there, let's go to what was item three and now item four, YOLO  or and or YOLO  V to test net Anberlin state test update and just Berlin update in general. I'll pass this to James to do that one.
  
**James** - Thanks. Twhat is the status of everyone getting on the dole, if I remember correctly, that was a goal of last. Last call was for remaining clients to be able to sink so we can buzz.
  
**Martin** - I'm not sure about the case, was it?
  
**Hudson** - I'm not sure. I don't know if I remember that being the goal I remember we were going to go toward that.
  
**James** - I don't know if we said by next meeting or did we say where we're going to discuss it for the next meeting?
  
**Hudson** - That could have been it.
  
**Martin** - I think so. I requested the science. But YOLO will be too, or a burden for definitions, for status so they could be forced. I don't recall if we mentioned anything about actually running in your next race. I mean, we talk about it, but I'm sure we decided until 
  
**James** - we talked about it, we didn't decide about doing a new one. But I do remember, I think was it bazoo or someone else, maybe that maybe that was about the state test and not about, 
  
**Hudson** - yeah, I'm remembering it now, it was the state test for YOLO  for YOLO  Berlin. And to do that for the definitions. So they said, was there anything on that?
  
**Martin** - Yes. So the last couple of days, we throw this into the mix of planes being first. And I think so if I remember correctly, Mary was found two vulnerables. All of these guys want to mention it, and I think I don't think it was really specific, though. I mean, specific specifically, and we have done something for the better stuff and for subroutines. Yeah, another man gets mostly a little bit of parity, but parity also implemented the static, all the three components are cheaper. It's a bit problematic to the. And but is it's still finding bugs that's getting better, I guess, and. So I guess the question is, do we want another pre-burden testnet? And if so, what would be in it.
  
**Hudson** - That doesn't sound like a bad idea. Tim, go ahead.
  
**Tim** - I was just going to say it kind of seems like there's a VIP or not, but even three hours before that we were talking about considering there's all these gas cost changes with like the gas cost changes are very simple to implement. So would we want those in Berlin? And then if there's ever a proposal, does that mean we remove twenty five? Thirty seven? Yeah, it just seems to me like. There's maybe like some clarity about what we want to do before up. I mean, sure we can, but I'd like to understand, what do we want to get out of it if we're if we're doing it?
  
**James** - And I don't know from I'm still kind of up in the air about whether the EVM changes were having both or having one replace the other or have one be one further, I really.. we would need to investigate more, I think, before making a good decision, I just have been thinking back on the conversation itself, the similar to that, that. That that that change, I think we need to review its effect on Berlin or not. 
  
**Alexey** - Well, I would suggest this, I mean, I know what were trying to say, but they're just not they're just not saying it. I think so anyway. I would suggest to do this. So we have the YOLO with where two EIPs were basically included, which was the BLS and the subroutines. So first thing to do is to separate them. OK, now what I would say is that don't plug them together anymore. So no. Step one. Step two. Now you've got basically everything separated from each other. We decide which are the of the so then we go to other EIPs were just arriving one about the gas repressing and another one about the what is not appeared but the proposal which potentially could supersede wireless. OK, so sort them in the order of priorities, which one is the most priority one and so forth. And then it looks like and then look at the levels of readiness. So it looks to me like if we feel that the subroutines, for example, are kind of didn't have any issues so far, then I would suggest to repackage the Berlin with the subroutines plus the gas changes and then leave the other two for the further sort of analysis, because I think we need we need a bit of a more time two to do work on three eight four, even three eight four. So why don't we just do that.
  
**James** - And I think the other one to consider is the ex mod that changes that we've discussed a couple of times, I'm forgetting the number of the off the top of my head.
  
**Martin** - So are we actually seeing the changes? What changes are?
  
**Alexey** - You know, the thing the gist of the trilogy suggests that, you know, making things more expensive, I think because I said I should have see that out of all everything that we're discussing, this is probably the most urgent one. And if you're completely honest, right?
  
**Martin** - Yeah, I agree. I tried to ship it as this before and then us or..
  
**Alexey** - So, yeah, definitely the most urgent one, because it addresses the issues that are already could be reality. And then sort of just what did you say the other one was?
  
**James** - There was the the IP, the change, the gas price, yet for an imperative to anything everyone had.
  
**Alexey** - Has it been tested already? Is there any what is the I mean, we could sort of we could sort of try to include it, it depends on whether we want to run to try to split them up again or not. So it's just like it's a sort of this game of if you bundle them up too early, then you might need to it's like a, did you put the baggage in the airplane and then somebody doesn't arrive or something? I guess you have to kind of unload the baggage before the airplane, the airplane leaves in this kind of situation, like, are you sure? So if you don't mind doing that. So how many iterations of the test net that you want to do, if you don't mind doing it, let's just package up the ones that we think they are pretty much. Ready or urgent or whatever, just to go on this basis, because they shouldn't be this kind of guilt about it, because this is what I'm kind of sensing in this, like, oh, what about this one? So there shouldn't be like any guilt about like we leave this one behind them because the other thing which is more urgent just came up or something like that.
  
**James** - that certainly make sense to me, and I was listing it as that I think is in the list of ones that are ready enough to be considered.
  
**Alex Vlasov** - If I may add here, like, Axic's priorities are great, but for like me, from what I see from also the effort, which is four to five implementations of BLS, it looks kind of ready for me because there is no problem with arithmetics. And the hardest part was implementation. There was also no problem [?] for this part. So what's the problem with integration of these libraries? So I would consider this Radik. I don't believe that they didn't pay close attention to the spec house.
  
**Martin** - But I mean, it doesn't matter if it's in the math or it's an integration.
  
**Alex Vlasov** - Well, I mean, if it's in the maths, you would want someone outside to fix a server. But if it's internal in a client and the known code base, it's what was discussed earlier. What would happen if something happens with this consensus issue, then someone would have to fix it. And this would be someone who has  experience with writing the code like this. But as it happens, there is no problem with the hard part is there is a problem with the part which is closer to the people who contribute to the client code base every day and not make large packages and solve the problem 
  
**Martin** - because it's not your problem. 
  
**Alex Vlasov** - No, I mean, the first opposition for a pre-compile was just like one of the positions for pre-compile, which is which involves some cryptographic operations, was what happens if something happens with a consensus issue, like who would be responsible to fixing this problem? And well, I mean, I didn't have any opposition to take this responsibility and try to help if it's necessary. But I don't know the process. But I'm up for it, though. I say that this is the same rescan as integrating any other EP. Would it be similar or static call? And I say just not from the perspective it was a long time. Well, it's all kind of done in here, but people are like with Berlin in being more and more and more of a stone's throw more and more and more as a priority. But I just don't buy that op code for three hundred eighty four given its current state will average the performance, which would be close to negative, which was the whole reason to have the precompiles. in the first place to have it's in a reasonable price. In this case, people will most likely stick with the bell curve, which is kind of unsafe and is limited in many aspects, 
  
**Hudson** - how long would it take to figure out the performance metrics that you're requesting? I guess Axic can answer that one maybe.
  
**Alex Vlasov** - Oh. Yeah, I'm not a specialist in EVM and its internals, how you would be able to my results together, but from what I see here, it's not just a problem to get to foster arithmatics in, which is I would say most likely it can be done with kind of acceptable overhead. The problem is how your write brain function, which Axic has described and there is no benchmark for pairing because it's difficult to write? I don't know how difficult it is, but I would say it's insanely difficult to take into account the limited capabilities. So as the benchmark there isn't that it's just a number of operations. It doesn't take into account any petral flow and logic, difficulties which you would just incounter trying to glue it all together; so I would say its a huge effort, a great effort, but I woulnd't say it can be done in a reasonable time-frame: half a year at least; And that it gets close to the uh, well let's say it decreases cost of computations and lets see what happens after this and then will be completed after half a year, but well it's a great effor tbu unforutantely it won't achieve the goal.
  
**Hudson** - so Axic what would you say woudl be the implementation time, half a year?
  
**Axic** - I just want to reflect on the syntehtic benchmark, there actually is control flow in it. Of course it doens't 100% match the real implementation; but it's more than just crunching the numbers.
  
**Alex Vlasov** - Oh I don't say it's just doing the same input data for 6700 multiplcation, there are two problems here one is the problem of performance and basic operations; which I hope can be solved starting from  assembly for the maths itself, and maybe doing something clever with [?] a stack of memory management. But the second part, which I see is simple, is much more difficult is what you described trying to implement to actually implement all this pre compiled using one of the languages I see you have. And I would say this would be much larger problem. It's very non-standard and not many people who usually writes this kind of stuff work with it. I would be glad to help, but I just have all the doubts that it will ever be the performance, which is even two times slower since there is of native one.
  
**Axic** - So I'm actually quite optimistic on the speed, because I know that we we have done a really bad job at optimizing any of this, and we chose YUL as an implementation of language for implementation because it was the easiest to deal with. But it's just too high level to write this in an optimized or at least too high level today. And haff is haff has been used to for implementing XML on being one to eight with quite an amazing performance. And haff looks more like a mix between assembly and C++ templates. So I would say that is quite close to what people optimizing curve operations in C or go with assembly would do. So I don't think it would look so alien to to anyone who has done such optimization before. So I think it wouldn't take, you know, years to accomplish that. I cannot give, like, a hundred percent accurate idea how long this would take, but I think if there are at least two different teams working at two different aspects, then we can get.. the two different aspects would be One team or person implementing just repairing operation, for example, in haff, using these apps and other team, which likely could be the same team, is optimizing the OP code and EVM. I think this process shouldn't take longer than if they are the right people this shouldn't take any longer than one or two months and this should give us already a good hint where we can reach, you know, good performance. And, of course, you can spend infinite amount of time optimizing it. But I think just getting a first confirmation, if you have the right people, then it doesn't take that long. Implementing everything is on top of that. But just reaching the decision point, I don't think would take five, six months.
  
**Hudson** - Ok, I'll go ahead, Aleksi, just to finish it up
  
**Alexey** - so I just I just want to finish it up basically just know I'm not going to talk about technical details, but in general, I do understand the kind of frustration that it looks like there's a lot of work to be done. And so sort of keep hitting the wall on this stuff. And it is clearly that we are hitting the wall because. But it's not because there are basically like people on the other side who don't really want this to happen. But simply, I think it's because the we don't actually have so much this specific expertise in the in implementing teams yet. Maybe we will get that expertise. And that's why it takes such a long time to get everybody to sort of get comfortable with this because, you know, you don't really want to be running the code that you're you're not you're just you don't understand or you don't actually kind of sure that it works. So it does take time. but it gives us the good direction where if we want to do these things better and quicker, we do have to sort of bring this expertise into the teams. And hopefully, I mean, for example, one of the things that could come out of the proposed project is that somebody will have to reimplement again because, you know, we don't really have a lot of people who could actually implement the BLS three eight one. And I don't know how many people are actually comfortable with that stuff at all.
  
**James** - let's say that we we do is that Alexey is saying we move we get to the point where there is a decision, we have some kind of testing to make sense. And then two months from now we get to a decision point that makes sense. But after that point, do we have someone who can write BLS pre-compiles into that instruction set. do, they exist? 
  
**Alexey** - What I want to push back on is basically this sort of idea that we are kind of running the.. we basically are running the corporation here, is that we have to give like, you know, we have to say, OK, in two months time we should be done. We can't do that because we actually we don't know how much how long it's going to take. We are running on a very tiny margins in terms of like resources and everything. So it has to come into the account that, you know, things could take longer and longer and longer and like it is how it is basically.
  
**Martin** - just a stupid question, but if we were to do an EVM 384, wouldn't that mean that we show the large problem, all the complexities too, and we implement some rather rudimentary things in our layer, and then we don't actually have to care about whether someone implements Algorithm A, B, or C correctly, because it's similar to and it's not on our heads.
  
**Alex Vlasov** - What do you mean?
  
**Martin** - I'm saying it would probably be quicker, faster on the platform there to implement the rudimentary stuff, the small bits and pieces, and maybe it would take longer for labor, for someone to figure out how to efficiently.
  
**Alex Vlasov** - No, I mean, my doubt here is that this efficiency will never be reached, that it's just unreachable for this kind of architecture? I mean, this performance gap will still remain even with the effort which is put in there, which will at the end of the day result something's been. Factor of two, far from optimal, and you should understand that nineteen sixty two is not even the fastest one, is kind of the safest one from from zero implementations and full blown optimized versions exist and they have twice the performance, I think, in some cases. So it will be still comparing like writing BLS in native code without assembling and acceptable performance was not that much of an effort, but to kind of beat this performance and get close to it. From what I see and like from all my previous experience, I would say that for this purpose it would be necessary to implement all those operations, all this reality for bits, modular operations in assembly. Plus it would need to be icer, some key first excercises or some clever tricks to have all the memory proficient and maybe something like this, and then to have an efficient implementation in one of those languages which actually proposes. And from this perspective, this is enormously different amount of effort which is required to write and which will potentially result in never reaching the points of equal or even twice worst performance compared to average implementation, not even saying the best implementation, the fastest one.
  
94.2.3 | Video | [1:10:43](https://youtu.be/q6bIeSu7r9o?t=4243)
  
    revisit the discussion on EIP 384
  
**Hudson** - Ok, well, there's only one way to find out, which is to evaluate it over the next few weeks, it sounds like, because there is enough support for that, for what Axic proposed today, that I don't think we should just drop it off before more discussion. And there is the ETH magician's thread where people can collaborate and figure out what we're doing there. As for the rest of the Berlin stuff, there were a lot of ideas presented today and we do need to do a better job of... I don't know how to explain it like, we keep changing stuff a lot, which feels bad, but it's not bad in itself because we do need to update our expectations when things come up like the security concerns. But we might need to get on a better cadence of making these decisions. So what decisions do we want to make for next meeting? Or between now and next meeting?
  
**Martin** - did they actually have to spin up or to define a new YOLO with Vitalik's upcoming changes and subroutines?
  
**Hudson** - I think he did. For once, the EIP was written. Yeah, and that's a good idea.
  
**James** - I think we could add the modX to that as well. Unless people have reservations about that.
  
**Hudson** - Sounds good to me.
  
**Alex Vlasov** - The only question was for over the open ethereum team, which could only get to perform and collaborate in their code base. So we stopped from all the previous actions, I think.
  
**James** - It ruled out option.. there is an option A and option B, and it ruled out one of those, there still was a proposal for one that had been benchmarked on all the clients to an acceptable level. At least at least to the point where it could go on YOLO n my opinion. In general, I like Alexi's plan, I'll be transparent and I'm a little worried on the end of being able to do on chain verification of signatures. To switch gears, at this point, I'm concerned it would push it much farther, even though the evidence and all those things could happen in months, the actual implementation of the Beatles would happen months after that because someone has to figure out how to do the instructions and to optimize for it and all of those things. And that's barring that all things are working as we hope it would. So there still is value to having the onchain verification for the ETH2 deployment. And I'm just wondering out loud if the effort of finishing testing and doing the fuzzing would end up being less than waiting on. Three eighty four get waiting on three eighty four and then waiting on a decision for three eighty for implementation and then someone has to implement after.
  
**Alexey** - I said from the beginning that it wasn't a good idea to try to increase dependency anyway and just work on the assumption that it might not happen in time. And that's OK. So I don't know, like, what do we have to be stressing about not completing the details by the time that phase zero launches? Is anyone stressed about it still?
  
**Hudson** - I was, but I'm not anymore after your after you just said that (lol)
  
**James** - I don't see it as a stress, I, I see it as we are very close to having we are closer to having finished the EIP for BLS.
  
**Alexey** - Well, it was a nice to have, I think at this point. So it was whenever like but it's nice to have might not happen. Right.
  
**Alex Vlasov** - Yeah, so it's a point that everyone sees this as a kind of requirement from ETH 2.0, they don't have other options that maybe you see it's always like more and more application player to solutions it's nice in general, which also depend on this kind of operations and even more dependent on the performance of its operations. But it's just most likely out of attention of the core devs.
  
**James** - I don't want to focus on ETH 2 dependancy sort of thing, it's more of we are pretty far along to be able to have this be ship. There still is value of it shipping. So if we have to if we have to weigh moving it possibly six to nine months versus a few months of finishing testing.
  
**Alexey** - I mean, if somebody basically came up to me or to us and said definitely that this is the math, nobody has actually done that. Everybody was just saying, oh, yeah, that could be good. It could save lives. It could reduce some risk. But nobody actually said came and said this is a requirement. And therefore, I'm actually assuming that 
  
**Alex Vlasov** - I can say this is a requirement because it's part of the thing I do every day. I mean, I can deal with the different scenarios, whether it exists or not.
  
**Alexey** - the reason why it's not a requirement is because the initial.. like remember that that that day when Justin Drake said on the phone on reddit that phase zero will be shipped 2021. And the same day he changed his mind, saying it's going to be shipped in 2020. I mean, from that even from that, I could see that there is no requirement because now it has to be shipped in 2020. Regardless of that, I don't know.
  
**James** - whether it's a requirement for eth2 to there is still value. Is there value in the EIP in having BLS precompile outside of that
  
**Alexey** - Yes, there is a value.
  
**James** - so I want to focus on that. Value is close to being executed on regardless of if it's tied to two or not like forgetting, putting that aside completely and saying that there is value to be had from the BLS precompile being on. Being there for things like plonk and all of the and and implementations that want to be able to use it. I think that's what I was hearing Alex saying that for him it is a necessity not and he's not referencing anything with these two.
  
**Alex Vlasov** - Yeah, that's the correct interpretation, I mean, so so for me, I can deal with different various consequences when and how it's implemented, but it's just because I have resources and options and plans how to do that as a it's in general as as a core of what we do as a company. We try to open our tools and expertise a little. And I understand that there are people who would be willing to do something with this, but they wouldn't have any resources to do it some other ways which are possible workarounds. And I don't want to enforce like even while I can overcome potential problems, it's not like there are other applications. And not to say that BLS is like de facto standard, if and if there would be any cross chain interactions and new various type of signatures, and for example, Wheaton's compression with political commitments, which is kind of discussed in these court channel, it would need a curve which is secure and which has other capabilities, like having like being able to commit to much larger polynomial than the current BLS curve. And it would be a requirement in this case that it's all still kind of insecure and it need to be a possibility for people to use it and that people will actually find an application. I never proposed it out of the strict requirements that it be for ETH 2.0.
  
**Hudson** - Ok, let's take this to Discord because we only have nine minutes left. But I think this is important that we decide this relatively soon, what direction we're going, if possible. So, Axic, between now and next meeting, what can what can be brought up as far as better idea of performance metrics and stuff as that's something reasonable to bring up in the next two weeks?
  
**Axic** - maybe if the document and the results and the code gets more reviews, yeah, maybe we could have a better idea at the next meeting.
  
**Hudson** - Ok, and Thomas, did you have something to say?
  
**Tomasz** - We are discussing KERO a big decision whether we deliver Ethereum, which is slow because it has to be generic and its general computer we deliver today for the users of yttrium something faster. And I'm like totally understand both approaches. I mean, I understand why I would like to not introduce Bitcoin balls, because it will look very strange in five or 10 years when I look back why these companies complex were even added. But now it makes perfect sense because we just deliver for the users and improve the visibility of the EVM for the teams that are building on top of it. And we just ensuring the community actually gets delivered what they really need. And because they're on the bleeding edge, they need something. And because only fast things at the leading edge have any value when you go to the market and this is the question we are asking ourselves now, what do we deliver as a. 
  
**Hudson** - Good, good way to put it. Ok, well, we'll have to talk about it more offline, unfortunately, or we can have a whole another meeting dedicated to this decision at some point if we want to do that, if someone proposes that to happen. Next up, we have the raw benchmarks for EIP 2666. I think that was Alex, right.
  
# 5. Raw benchmark for EIP 2666
Video | [1:21:48](https://youtu.be/q6bIeSu7r9o?t=4908)
  
**Alex Vlasov** - Yeah, I mean, I got the results from Ultimata Clan and assembled them in the table, which is now in the PM issue, and I will simply post it to us and post a link to the core devs. But preliminary results are and I've used this as a kind of ideally should be placed in conjunction or after or at least partially together with twenty forty six if twenty forty six is introduced. And the call to be compiled since we used to forty or a hundred guests, depending on if that would be possible to put some optimizations in BLS or not. For example, as a result of this to be on the safe side, it would be necessary to adjust cost of additional multiplication. And all other compilers are on the safe side. So there is no internal problem with performance since there is no need for compensation for this seven hundred reduction of the seven hundred guests on the call. But as a next step, it is definitely possible to reduce pricing on hash functions, which are two of those separate compilers was shot and Reprogrammed. And on the code of itself, Ellson New Formulas represents the internal structure of function so much better. So they actually follow the maximum internal execution code logic and how it depends on the length of the input. So it's all captured in this EIP. I would most likely remove and could use separately as a proposal for different handling of gas being burned on air. It will be separate, but I think put in twenty four to six in Berlin is with simpler price would be an additional complication, would be a great step and later on we can we price the necessary compliance.
  
**Hudson** - And anyone have a quick comment. Ok, the next one up is the EIP IP meeting, we have come to consensus within the people who attend those meetings of new EIP statuses. Edson, if you want to go over that really quick, there's also a link to a hack md, that goes over what each of them mean. And we don't have to go through the entire thing, but just kind of what the goals are and point people out in the document, what we came to.
  
# 5. EIPIP | New EIP Statuses
Video | [1:24:20](https://youtu.be/q6bIeSu7r9o?t=5060)
  
**Edson** - Yeah, I can go over it quickly. Let me share my screen. So these are how the new statuses would look like. I don't think there's an image of the old ones that will changes are the removal of accepted. The trend is separating the hard fork coordination process from drafting the piece itself. So there would be drafted and then decision to go into Maine, that would be separate from the actual repeal. And there is an introduction of a review. This is so we can get more feedback from viewers before let's call. IT movement from draft review means the author is finished writing his portion of the draft for external feedback. And then the stagnant troop withdrawal, the replacements for accident, inactive or stagnant, is over some time has elapsed since the last change and it's automatically moved their. Or withdrawn as withdrawn is, it's intentionally removed and there's no intention of moving the forward. Then final means that the spec is frozen, the AP's frozen. These are the stats to be applicable to every single AP and the AP. 
  
**Hudson** - With the exception of living, living would only be for those VIPs that are that are specifically like Egypt one, right? 
  
**Edson** - Yeah. So living is Schäfer living document, which means that the documents meant to be updated and never meant to be final.
  
# 7. Cat Herders Survey Results
video | [1:27:19](https://youtu.be/q6bIeSu7r9o?t=5239)
  
**Hudson** - Any comments on this? OK, thanks for the overview, Edson. We will be looking to incorporate this and other changes into a PR that then we'll go through community review. Next up on the agenda, we have a theory cat herder survey results, but I feel like two minutes wouldn't give it justice to really walk through what we found and evaluate that based on the meetings we had in July. So would it be OK? I think Pooja is going to present this if we just presented it next meeting and just make it an earlier item.
  
**Pooja** - I'm good with that. 
  
# 8. Migration from the ACD Gitter to Eth R&D Discord
  
**Hudson** - And then finally, we have migrated from the Gitter to the Eth R&D discord. You can click on that link to get into the eth and discord. And we have an all core devs channel in there. We also have a section for ETH 1.0 that we can add subchannels to that that is just on request. If there's something that is like maybe even something like these IPS we're talking about today with the black signatures and stuff might need its own room. But if that comes up, we can discuss it within our core devs channel, under General, under the Ethar R&D discord. Any questions on that? There's also really cool channels about account abstraction, Regenesis 15 fifty nine and stuff like that already. So it's a it's a really neat place to hang out. All the cool kids are there. Let's get active [Hudson is my favourite]. The last thing is rreview previous decisions and action items. Looks like. Um. There isn't really that many, and I think we covered everything because Alex Vlasov, whatever the benchmarks. Uri Klarman was going to recheck prices and calculations for i.p twenty seven eighty. I don't know if Uri's here today or someone who can speak to that. And then reach out to the operatives chat options and present that next call. Yeah, we came up with going to the Discord. Um, that's all the actions required. And I think that's it for this meeting. Does anyone have anything else before we go? Ok, thanks, everybody. Our next meeting is September 4th. Twenty twenty at fourteen hundred UTC. Everybody have a great weekend. Cheers this weekend. Thanks.
  
## Attendees
- Vitalik
- Hudson
- Edson
- Pooja
- Daniel Ellison
- James Hancock
- Danny
- David Mechler
- Lightclient
- Martin Holst
- Axic
- Artem Vorotnikov
- Tim Beiko
- Alita Moore
- Peter Szilagyi
- Alexey Akhunov
- Tomasz Stanczak
- Pawel Bylica
- Alex Vlasov

## Next Meeting
September 4th 2020 @ 1400 UTC