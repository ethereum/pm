# Ethereum Core Devs Meeting #150 Notes
### Meeting Date/Time: 2022-Nov.-24- 14:00 UTC
### Meeting Duration: 01:47:28
### Audio/Video of the Meeting: [Recording](https://www.youtube.com/watch?v=HX_Zr_gVeOE)
### Moderator: Tim Beiko



# **Summary:**
- We discussed the state of testnets and what to do with them going forward. Only specific decision is agreeing to fully shut down Ropsten by EOY. Broader testnet proposal to be discussed here: https://ethereum-magicians.org/t/proposal-predictable-ethereum-testnet-lifecycle/11575 
- We went over the EIPs we've been discussing for a while now and discussed which should be moved to CFI... and what CFI means! No strong consensus on the latter, "definition" is here (https://github.com/ethereum/execution-specs/tree/master/network-upgrades#definitions). With 4844 and EOF (all 5 EIPs) being on devnets already, they've been moved to CFI. For 4758, people wanted to see a better elaboration of the ways to deal with contract breakage before moving it to CFI. 2537 was also moved to CFI... but it's been CFI'd since Berlin. 
- After that, we discussed what should be the scope of Shanghai and when it should happen. Hardest part to summarize given the diverging views, but there is strong (unanimous?) consensus that withdrawals should happen ASAP, and if we add anything alongside them in the fork, the delays to Shanghai should be minimal. Teams felt like a March fork with withdrawals should be possible. 
- On next week's CL call, client's devs will discuss more how CL teams feel 4844 might affect withdrawal timelines 
- On the next ACD (which will be the last one of 2022!), we'd like to get a final list of EIPs we can include alongside withdrawals. 
- A withdrawal devnet is live! The status of withdrawals will be covered in more depth on the next call.


Moderator: 

[1:03](https://youtu.be/HX_Zr_gVeOE?t=84)
**Tim Beiko:**
* Welcome, everyone to All core devs 150. A lot to cover today on the call. The high level really only a couple of main buckets. So we've been wanting to talk about test nets and their status for a while, and it always keeps getting bumped out. So I think it probably makes sense to just take like 5 min at the start to to just discuss this real quick. Then main thing to cover is Shanghai, and and how we're organizing that and I suspect that'll take us probably the entire call. If we, if we do have some time at the end, there is still some engine Api stuff, as well as some execution specs and testing discussion to cover and its worth noting there's only 2 All Core Devs left this year. So there's today in December 8th. The other one is like 2 days before Christmas, so we'll skip that one and and resume in January. And so this is the second to last All Core Devs we'll be doing this year. And yeah, Happy Thanksgiving to anyone in the Us. I guess. Okay, to start with the test net bit.  Do you want to give some context here?

# 1. Ropsten sunset date (and testnet sunsetting generally)
[2:54](https://youtu.be/HX_Zr_gVeOE?t=174)
**Afri:**
* Yes, sure. Thank you very much. So a lot of people will be probably be aware that we have issues with Goerli test net it. And we have been trying to address this through different Apparatus But long story short, it's actually most stakeholders they start recovery Goerli test net and get over it and maybe just deprecated it and get a new test nett. The problem is, that there's a lot of migration currently happening in the community towards Goerli test net and putting out an announcement. saying Goerli test net could be blown. For a lot of bigger applications, or even L2 move there faster. So I kind of sat down and brought out the proposal. So to to address these problems. I think we need to 2 things. We need to be more transparent here because we got to communications. Well, for when we going to launch new tests nets. And when are we going to duplicate old ones and to to even make it more predictable? So, on the other hand, I worked out the schedule. so predictably lunch a new test net every other year and limit public test nets life time to like 4 years, and fork when necessary and one year long term support so that the teams have time to migrate to public test nets. I was told by the community that application developers have infinite runtime on test nets, so they never want to migrate, because it's a lot of work for them. And I explain some the incentives for, like free public tests nets are just not given in 5 years is actually a long time. So to totally migrating it takes around 6 months for them between planning and execution. So yeah, a long story short, I propose that we also move Goerli into a duplication status starting next year, and it looks like another year to run and then launch a New Test net towards Q. 3 next year. Looking at the latest numbers because Goerli is already 4 years old. It was for almost one year schedule. Goerli could hit end of life early next year and Sepolia test net would hit end of life around 2026. I know that the more client think that test nets are  more like free, and they can be just discarded anytime. I just want to create the awareness of for application teams. I want to know if there's strong resistance to accept a more predictable schedule here. I don't know if anyone saw the proposal, I wrote a lot of text around future test nets 

**Tim Beiko:** 
* thank you. Anyone have thoughts on this. They want to share right now. Does that eths magician's thread that I free link as well in the agenda. We can have like a longer discussion there. But Anything people want to share about the test nets? Oh, there you go. 

**Mario Havel:**
* hey? I just wanted to mention a project on ephemeral test net, We are testing and working on it the past 2 weeks and the goal there is to create a network which automatically erasers back to Genesis every given period so it would serve as a short-term testing environment for of validators, or even application devs. Without like growing state, without supply issues. So Just to let you know I will share here a link for a repo with more resources, and if anybody is interested and you help or have any questions, feel free to reach out. 

**Tim Beiko:** 
* Cool anyone else. yeah. And, Mario, if you could post that link in the Eth. magician stream, I think that'd be great. So it doesn't get lost in the zoom call one last thing so we have discussed previously shutting down Robson at the end of the year. It seems like it's already in a pretty bad state. Adrian mentioned. There's about like 30% or so of validators online. so it's not really useful. Does anyone have like an objection to just turning everything off during the holidays? So to say, you know, we shut it down around Christmas and so at least you know, client teams can know that they can just shut everything down. We'd put out a blog post just to tell people you know again, I don't think it's. It's quite useful for for anyone in the screen State. But yeah, at least we can have like a here. I she or shut down. So anyone opposed to that. Okay, and Afri. And whatever announcement we make, i'll make sure to link your proposal. And so people know that this is kind of the place to go for a longer form discussion about just the the general future of test nets

Afri: Thank you.

# 2. Shanghai Planning
[9:01](https://youtu.be/HX_Zr_gVeOE?t=539)
**Tim Beiko:** 
* Okay, nice. so next big thing is Shanghai planning and like in in the last call 2 weeks ago we sort of left off in the middle of trying to figure out what was going to be CFIed or not and we basically run out of time there. I think that's probably the first thing you make sense to just discuss. then I spent some time in the past 2 weeks, talking with different client teams. about like the relative priorities, and and how they felt about different things. I was thinking I would summarize it all before this call. But obviously the the opinions were pretty varied, so I think it's it's worth it for people to like. Take the time to to kind of share their views, and and so we can make it the the proper nuance there. and then we have all these EIPS that we've been discussing that there's been up updates to. But I was looking right before this call basically at like what do we actually mean by CFI, and how we've used it in the past. and generally the idea is that this is something conceptually that we'd want to do that we would be comfortable putting in dev nets, even if it doesn't mean deploying it to maintenance specifically. Based on the the conversations we've had, and the work that's been happening. it feels like a lot of the EOF stuff that was not already CFIed. effectively. We're acting as though it is. I'd say it's probably scimitar for 4844 and then the self-destruct and EOS EIP i'm less, sure. And I think the the reason why it be important to get this clarified is I think it's like an important signal to the community to say, hey, these are like the things that are like seriously being considered and then the expectation I think of the community will be something like a subset of this would be what makes it into Shanghai ideally. In the next 2 weeks we can figure out what the right subset is, and we can use a big part of this call to do that. But I think first coming up with like a clean CFI list means we can just share that announce it. And and Also, you know, people who are not in this call can can kind of share their thoughts in the next couple of weeks. So I guess maybe just to start like and and take these one by one at a high level. Does anyone feel like the other EOS EIP  that we've been working on I forget the exact number, but  2400, 4750, 5450 They're already sort of effectively past what our bar would be forCFI So does anyone like a post move between them the CFI and this is not a commitment to move them to Shanghai but so you know we're working on this. It's on dev nuts, and it might be part of Shanghai. Mike, and then Andrew.

**Micah Zoltu:**
* just for clarity on the CFI my correct understanding that you're saying CFI means the core devs all agree. This would be a good upgrade for ethereum, but it doesn't make any sort of commitments. is that accurate?

**Tim Beiko:** 
* correct. I think the commitment that makes is, basically we're going to try to prototype this on a dev net.  which is effectively what we've been doing. But yes, it doesn't.

**Micah Zoltu:**
* So something that everybody agrees is a good idea, but it may be 1 or 2 forks out is CFIed. That would be a reasonable state of things. Is that correct?

**Tim Beiko:** 
* Correct? we also don't want the subset to be like meaningless right. like it's  not like every single potential thing that we considered. But I think things that we're seriously considering and we're writing test and putting it on on dev nets.  Andrew.

**Andrew Ashikhmin:**
* well, I think. because we pretty much agreed that we are going for the big UIF It's unrealistic and counter productive to do it in and Shanghai it's also like there is no immediate pressure to do it, especially without solidity suport there is no urgency. so my strong preference is to move it all UIF to cancone and move all the the UIF to CFI. And also I think that better production quality Sulitity support a must for UIF

**Tim Beiko:** 
* I know there's other teams who feel stronger about having this in Shanghai. So Does anyone just want to voice that opinion?

**lightclient:**
* I feel like if UIF doesn't go in Shanghai it's increasingly unlikely It goes into another fork. I think we have big upgrades that we want to do in, like many of the next forks, and it's always going to be this debate of you know this is the important thing we want to make the fork small. We want that thing to go in because it's important for the roadmap whatever, and I think that with withdrawals and EOF. This is like a perfect time to have, like a relatively small fork and do EOF so if we move it to Cancun like, I just really think it's going to get bumped out of Cancun to.

**Tim Beiko:** 
* Okay, I think I know my view on like, even if we were to move it to Cancun. I think we should still CFI it, and we can make the decision basically on the next call of, you know. moving you to the next fork. But I think the signal like clearly. If the if if the argument is like, you know, we should maybe do this and Cancun and not Shanghai that would push me towards having it CFIed, so that it's clearly labeled that way. Marius

**MariusVanDerWijden:**
* Hmm. Just to kind of rebut that's argument. I think if if something is so low priority that it shouldn't go like that, it won't go into the next, for because we have something else then why should we to it now?  Like if only because, like now we have a bit more room in the fork

**lightclient:**
* I just think the people who are loudest on these types of calls don't prioritize changes to the EVM. And I don't think that's like an accurate representation of everyone in the community. And so I think that for that reason, like things will get bumped, and that's not necessarily. You know, total representation of what people desire for the EVM.

**Tim Beiko:** 
* Dankrad 

**Dankrad Feist:**
* I am very worried about trying to prioritize it for Shanghai. That's like an argument let's make it a small fork like as I think I've said before, I think it's crazy to like raise a little version for a minimal version of EOF one that isn't actually very useful like I mean, I think, like reserving an extra version, and the EVM should be considered a huge step, and should be only like, should be done when really important changes that actually makes sense provide significantly better security better analysis, better scaling, 

**lightclient:**
* right? And that's why we've made the the this EOF upgrade now, like the bigger suite of EOF Eps because of that critique. And now I think, like this version of EOF is. you know, hits those points.

**Tim Beiko:** 
* The 2 kind of counter arguments EOF still kind of leaning towards CFI, and because right now we do have 2 of the 5 EOF  EIP CfI. So I think, and We can discuss like the the status of things after. But I think to not take up all of the time moving the 3 other ones Given that if we do, EOF it's very much leading towards being those 5 EIPs that seems more coherent than having like 2 out of 5 of them CFIed in the rest Not yeah, Andrew.

**Andrew Ashikhmin:**
* well, I think they should be CfI but it's not a good idea to cfi them for Shanghai, because and we can code the Cfi, for Cancun we have a a great commitment that we are working on it. We do think it's a good idea. It just well, at least my opinion it's it's a big change, and I would hate to rush it and end up with some unused, or like semi-broken version that we will have to support forever. But I think there is enough time.

**Tim Beiko:** 
* We don't have like Cancun given. We don't even have this scope for Shanghai. I think I would link to make it. Cfi All of the Cfi thing will be like for Shanghai. But there's this expectation that not everything makes it into Shanghai, and then you know some of what doesn't make it would likely make it into Cancun. So I think it's just probably easier for people to understand? If it's all in one place.

**Andrew Ashikhmin:**
* Why not create a Cancun and move it all out there, because 

**Tim Beiko:** 
* i'm not clear that there?

**Andrew Ashikhmin:**
* clear separation of all EIF goes in one place and gets CIFed for Cancun, we can mark it as like starting with enabled that the Cancun block in the EVM. Or Geth, So there is more clarity. 

**Tim Beiko:**
* So I think that's maybe like the second step of the process. It's not clear to me that like that's the general consensus, whereas, like We probably want to do this at some point. Feels like, Obviously some people disagree with that, but it feels like there's definitely more consensus there and then, when we do it I think it's just like a separate conversation. But I just try to get the first part of it settled, and Then we can discuss when we do it, and relative to everything else, it's been considered. Alex.

**Alex Beregszaszi:**
* Yeah, I would like you to reflect this. Notion that it's not useful for solidity. and/or it may be broken. if it's fresh. I just would like to ask you what would be the the way for solidity to the signal that they would be interested in this change? Because on the discord but seemingly that wasn't like a strong enough signal. So What would be a convincing argument from solidity. for this group.

**Tim Beiko:** 
* Andrew.

**Andrew Ashikhmin:**
* well, my position, that working solidity compiler into EOF without dynamic jumps, is a convincing argument, and that's pretty much, in my view, a prerequisite. not a commitment, but a working compiler.

**Micah Zoltu:**
* would it be correct to say that you would like to see solidity implement first, then the EVM, implement it rather than the other way around.

**Andrew Ashikhmin:**
* Well, both can be done in parallel

**Tim Beiko:** 
* solidity would implement it. Obviously you need supporting the EVM, but before it's deployed the main net, I think, is it. Andrew saying

**Andrew Ashikhmin:**
* Yeah

**Tim Beiko:** 
* Thomas

**Tomasz Stańczak:**
* That's my suggestion as well like all the changes, the solidity side and the Evm side should be prepared and tested together on test nets. And people should say that, yeah, there are observable improvements. And there is an indication from Solidity users, and so the compiler teams that the changes that are implemented in solidity and testable on test nets that are ready to go. And then we all have everything to say. Yeah, They delivered what was needed. So the team didn't discover anything that's that actually was against their assumptions.

**Tim Beiko:** 
* Got it? Okay, let's do, Alex. And then I think we can move on to another one and discuss EOF specifically, and which fork it should be in later. But yeah, Alex.

**Alex Beregszaszi:**
* Yeah. So solidity is a working on an implementation, and it is related to this year. So which means basically before Christmas. But at the same time, you know, the the core developers have of solidity have said that this wouldn't break anything. This should workand now we are basically doubting the the understanding of both the compiler and the EVm.  And also, you know. just generally when stuff isn't, there's 0 agreement about whether something is useful or not. from this group. That is. that is a signal for you know, people like solidity not to do anything with it, because also their time is is very limited. and the USA. Has been pushed back for 2 years at this point. and that's why Solidity Hasn't implemented it. Because. you know, they also have the lack of people, and they had to prioritize that at things.

**Tomasz Stańczak:**
* Okay. So 

**Alex Beregszaszi:**
* all this last time, last time everything was implemented already in the clients, and it's in the like, the changes for the for the EVM. And then it was not used. So the example is working the other direction that the the functions.  So I mean the previous example. The sub routine solidity objected it from the beginning. Maybe they just weren't loud enough. you know. I mean justice. Now.

**Tim Beiko:** 
* Okay, just to make sure we can move forward. I don't think I've heard anyone say this should not be CFIed, and we can  it. Yeah and we can discuss like the specifics of EOF later. But I does anyone disagree with moving to 3 other EIPs which we've already started prototyping in our in both nets to CFIed along with the other ones. It's not a commitment for Shanghai specifically. Last chance. Okay. so let's do that. Let's move at those 3, the CFI 

##  EIP-4844
[25:03](https://youtu.be/HX_Zr_gVeOE?t=1501)
**Tim Beiko:** 
* The next one that's in a similar spot where we've started prototyping it on Dev net already. there's a bunch of client teams that are working on. It is 4844, and I think this is also very much one where you know some people really want to see it in Shanghai. Some people. I don't but leaving like, which fork aside, and whether it makes sense to couple it with withdrawals. does anyone disagree that like this should be Cified. Okay, this one was much easier. so let's move forward forward to Cfi, and we can discuss it in more detail a a after I think. Okay, I'll push back on your comment. There is, I think this is like a perception that if you attend all of these calls and have, like a very good context of like all this stuff that's being considered. Then maybe it's obvious with like Cfi or not. But in the past couple of weeks, like a bunch of people outside of these calls have mentioned to me. It's it's not so like having this signal to like people who don't attend these calls that these are the main things being considered and debated.  It's almost more useful for them than for us. And this is Why, I think it's worth insisting on having like the clear distinction.

**lightclient:**
* fHow do they act upon it? I'm just curious like now that 4844 is Cfi like, how does that change the operation of people outside of this group? So I think it's not in Shanghai yet to right it's like, yeah, we consider is the core dev call that. We think this is an important upgrade for ethereum.

**Tim Beiko:** 
* Yeah. But I and I think this: the Cfi just reflects that. Basically and it's like a way for people to know that this is the case and have like somewhere that it's written down. But that's the Yeah. I don't know that it affects their actions, but it affects their perception of the process.

**arnetheduck:**
* I would say one thing which is basically that moving to Cfi does put a strain on the client developers and the resources that we have to allocate to things. So regardless if it goes into Shanghai or any other, fork this is going to like saying that something goes into, CFI will divert resources in that direction, and it will delay anything else. That is CFI really that's maybe the best way to put it.

**Tim Beiko:** 
* I think that's true, but I think. and then it's all. It's already the case for 4844 and EOF right like there's already resources from teams. that are that are allocated to both those things. but I didn't think I think that's fair. Yeah, definitely like time teams feel like more pressure to like work on it once. It's CFIed, but okay. So there's 2 more. We discussed last call that I think are like, maybe slightly less obvious about what we should do.

**Jesse Pollak:**
* I just want to jump in and share my perspective on the Cfi from the coinbase lens, I'll just share the kind of anecdote that, even though coinbase has been working for the last 6 months on 4844. i'd say in inside of what is now like a 5,000 person company or 4,000 person company. There's very little understanding of what ethereum's overall kind of like roadmap priorities are, and where coinbase has opportunities to contribute, make a difference in both the kind of ability for for us to execute quickly and safely, and to to kind of like figure out what should happen when. And so I think the thing about Cfi, and like the way that that Tim is presenting it that I like, is it? It is just like a checkpoint basically where it's like, hey? These are the things that ethereum is saying. are like ready to be executed against and like over the next year or next one and 2 years will happen, and, like. coinbase, come and figure out how you can contribute to that, I think, without some formal recognition and process. that just becomes really hard, and instead becomes about like people like me who sit on this call, taking it back to like people like Brian Armstrong our CEO, who have like 15 min to understand this kind of thing and that kind of like. you know word of mouth is less effective than being able to say. Hey, here's the list of things that, like everyone, is aligned on being important over the next year, like, how do you want to help make these things happen?

**terence:**
* I just want to also add on top to that from our end Prison we've been actually working on it for the last 6 months, and the thank you like Optimism, and Conebase for the support as well. Well. I think we should be a little bit more cautious, because I, from our point of view, I don't think we should deal with draw, I think we draw should be the number one per it. As a Core Dev. We should get withdraw out as soon as possible, and the also a safe as possible. So I wouldn't like Say today, if you have 100% resources working on withdraw, I wouldn't shift those resources from working on 4844, and having to delay withdraw of 4844

**Tim Beiko:** 
* Okay and thanks for thanks for sharing. And I think you know, One part of this is like a lot of this stuff probably should have been, CFI  and like before, as we were starting to work on it, and it's like now, just making sure that the status tracks what we're actually doing. and that provides legibility to people outside this call, We can discuss the specific definition of it offline. I will probably take the whole rest of the call. If we were to do that here. I think, at a high level. The things that, like we're already working on have resources already allocated. are being built on dev nets. It seems reasonable to move them to the state this should have been, and then we can debate how they should all come together in a fork. So the 2 more that we did discuss, and you know, might make sense to CIF were the self destruct removal. EIP this one's a bit different. I'm not aware that anyone's been working on it directly, but I think a lot of people want to see it happen, and you know, think it's important. So yeah, that's what I'd be curious to hear from clients. If we think it should be CFIed. Jesse, if you're still not for that. ok No. Rob

**Rob Montgomery:**
* Yeah. Hello. So I My name is Rob. I am a ethereum dev, and I have built something called Revest protocol which uses the self-destruct pattern in its in its contracts. What we do is we do a very unusual system. I came here today to tell you all about it, because the proposed change would unfortunately brick our contracts and result in hundreds of thousands to millions of dollars, being permanently locked. What we do is, and we did this actually to Ironically enough. we did this to help with state growth and increased security. the idea being that we a contract. Well, actually, to begin with. When a user makes a deposit, we use a individual, Id to predict where the create to contract will live with that salt. What the ideas that salt. And then we send their funds to that non-existent contract that we will deploy in the future when they're ready to withdraw. We use that same Id. And this is an NFT idea, actually so kind of fun. But we use that same. Id to say, okay, this we're going to deploy the contract. Now we're going to withdraw. However much funds the user wants to withdraw. There is a situation where the user does not withdraw all the funds. So this is that's that's the edge case that causes the problem. So the user. Withdraws the funds, and then at the end of that transaction to prevent state growth. and you know, keep the transaction cheap. We call Self-destruct That results in the the contract, and they're being destroyed, and they're never having been a record of it at the end of the transaction. So it never exists between blocks or between transactions the problem with 4758, and it's impact on us is that create 2. It's designed to revert if a contract exists at a given address. and in the course of this.  If the user were to, you know, withdraw partially in one transaction, they would no longer be able to access any of the funds that are sitting in the contract now, because the system still thinks the contract doesn't exist, it will try to deploy a contract at that address again.  but because 4758 has deactivated self-destruct. Now we can no longer actually have ability to retrieve those ones. So I guess I just wanted to come here and suggest that the implementation of 4758. Take that into account, and perhaps have some sort of an edge case check. I make sure that if the contract is deploying the same transaction that it can, in fact, be removed in that same transaction. Allowing that edge case would solve all of my problems. That would mean that this wasn't a problem for me and for several other people I know who are using the same pattern.

**Tim Beiko:** 
* Thank you for sharing yeah, and that's definitely something that we need to consider I think Vitalik you have you hand up first

**Vitalik:**
* Yeah. So one thing I wanted to mention on a self-destruct in particular is that I think one good argument for pushing it into CFI early is because that historically we have been bad at convincing the yeah community. That's some change that that might break compatibility and make it is actually going to happen in people. And actually, we need to take it seriously right. So thinking back to some of our previous examples, particularly with increasing some gas costs and so this is some extent its one of the best signals that we have that’s actually selected to happen, and not just I. You know not just a couple of people in a quarter randomly thinking about it, and so that would reduce the chance of more applications that depend on the self-destruct feature being that created in the future. And then, as we said before Cfi, does not need one Fork It could be in 2 forks for now. And these kinds of things should that absolutely have met with long periods between the decision and implementation. And just because there's so many applications. And of course, you know, obviously there's like issues on the other side right? Which are that we want to consider a change that will reduce that overdose. That's say, impact to a couple of important applications. And if the same transaction edge case does it, then that's absolutely worth it. Obviously that does kind of affect the whole CfI and What is the meeting of CFI But just wanted to keep in mind that you have the broader picture of that to the extent that we are going to do stuff that breaks backwards compatibility in the future. so just examples of things that we'll break backwards, and a compatibility in the future. Vertical trees are a big one that'll break every application that relies on manual introspection, and like in EVM verification, or in stark verification of state merkel branches for those kinds of things in the future we should some ability to signal that Yes, this is actually happening in a way that's like much ahead of actual execution, because that's going to be needed for developers and just generally better think about the yeah issue of how to handle these kinds of things, so that we're both actually able to make changes that have long term benefits that are worth it. But also do them in a way that does minimize their costs, and that leaves a room open to make changes that minimize costs. Further, if options for doing that appear.

**Tim Beiko:** 
* Thanks. Ansgar, I think, yeah, you had your end up and had some comments about this, the chat as well.

A**nsgar Dietrichs:**
* Right? Yeah, I just wanted to briefly say, I, I think I generally agree with Vitalik in that I think it would be really useful to have some like advanced signal of commitment to making changes. just for the outside. But I do think that the like Cfi, as we currently have it is just not quite the right form it, because like to me at least the meaning of CFI really is that in the EIP in its current form is is at least already considered for main net And I just don't think like the if for example, right now I will be very strongly opposed to bringing the the EIP to main it without at least having fully evaluated the same transaction and the edge cases. So the EIP is not ready yet, and I really i'd be very hesitant to basically break with the meeting of CfI purely for the signaling purpose of it. especially because I mean we we see kind of Rob coming on this call here already, like people do start to be aware of, kind of self destruct. And in general. So I think, yeah, I really think we should stick with what CFI supposed to mean and only move a piece to Cfi that are basically final.

**Tim Beiko:** 
* right? And I think basically, for you, the bits that would make it worthwhile to move. This is, if we have this like edge case, you know at least proposes an option in the EIP, and we've had the EIP in the past that proposed, you know, different edge cases or different ways of solving stuff. So at least having some spec for how we deal with like the this. Andrew.

** Andrew Ashikhmin:**
* yeah, I Basically, agree with Ansgar, I think. if we update this to include Self destruct within the same transaction. then and afterwards we can move it to Cfi, but not beforehand.

**Tim Beiko:** 
* Dankrad

**Dankrad Feist:**
* Yeah, I mean, I wanted to respond to Ansgar, because clearly like now we have the situation that since we have already very strongly considered the active addicts Self destruct, someone has deployed new contracts that make use of it so clearly. They Haven't noticed that like this really should not be used anymore. So like I'm. Yeah.  I don't quite understand, like what what you are suggest, and how to solve this, you

**Tim Beiko:** 
* Well, there was some proposals about, you know, If the if the self destruct happens within the scope of a transaction, or something like that you could. You can still keep self destruct. and we discussed a lot of these. 

**Dankrad Feist:**
* Yeah, yeah, sure. But I mean this contract specifically, was deployed at a time where it was already very clear that we're going to deactivate it. 

**Tim Beiko:** 
* this was like it just wasn't said to Cfi, but I think like

**Dankrad Feist:**
* there there was like a clear momentum to what said already. And now we're adding like a special case, I mean, like let's just consider. This is this is like a huge thing. This is like technical depth that we are adding to the EVM to support this one very special like this one case with one contract forever.

**Tim Beiko:** 
* Well, it's. I don't know there's more to be clear like I, and I think we are still looking into like how many there are. But it's not a case where there's a single contract effect there's like a pattern, and there's at least a handful of like contracts with significant views that that are affected. yeah. Andrew.

**Andrew Ashikhmin:**
* Well, my my position on technical is that there are different kinds of technical debt. So backwards compatibility is very important. So okay, but if by technical that we mean that there are some my extra 10 lines of code and a like some extra 10, 10 lines in this back. Then, to my mind, it's not a big deal, so you're right. It. You test it you pretty much never change it. It doesn't affect like your performance strategically.

**Dankrad Feist:**
* Highly doubt it will be 10 lines of code. 

**Andrew Ashikhmin:**
* We need to investigate. But if it's a reasonably small piece of call that mitigates a number of real contracts. So then, to my mind, it's worth introducing. This small.

**Dankrad Feist:**
* This is going to have to change the way you're right, states because it means that we don't support. the whole point of self-destruct the activates. Abstract is that we don't want to support, and deleting contracts from State. Now this means that in order for these temporary contracts, you will have to add a way of writing that not writing that state during the transaction by keeping in some cash somewhere. I guess this will be much more complicated than people imagine. 

**Andrew Ashikhmin:**
* We already have such data structure in an Agon and Gith, and probably in the other EOF as well.  we already do it. It's like no technical debt on that side.

**Tim Beiko:** 
* Okay, and Ansgar. See your hand this up again, and then you can. Yeah.

**Ansgar Dietrichs:**
* right. I just wanted to briefly clarify that from my point of view I didn't want to say that I would want this change in the EIP before making it CFI just think that basically exploring this question, I mean, I think, then, what specifically illustrates? Why, this is a complicated question. It's not so. Not just like, okay, yeah, sure. We could do it. It's like a this. Seems like maybe desirable, but it could also introduce meaningful extra capacity. So this is just like a small business side research question within the EIP. That's just not explored yet, and I think that means it's premature for Cfi: that's all.

**Tim Beiko:** 
* yeah, I i'd be curious if you're from other time teams as well, I think. yeah, basically is this: the general feeling that to make this Cfi people would want to see at least some like explored or fleshed out proposal for how to deal with these edge cases? Or is this something Because it's going to impact people and we want to figure out how it's going to impact them and and and have people show up. I we should kind of make Cfi now, so that people have like a strong signal that is happening, and we can, even if that leads to like massive changes to the the spec, because we we need to accommodate some edge cases.

**Micah Zoltu:**
* Fortunately, I think the answer to your question requires us to all agree on the definition of Cfi, which it sounds like. Yeah, unfortunately.

**Tim Beiko:** 
* So I guess. you know, using the the ones you posted in the chat it The second one was like, you know, climb Ups would like to see this in the next handful of hard forks.  That seems reasonable. liam.

**Liam Horne:**
* come back to me after we finish this.

**Tim Beiko:** 
* Okay, I guess. Does anyone oppose like moving it to see if I like? I mean, I guess Ansgar does.

**Andrew Ashikhmin:**
* Yeah, I oppose as well. Okay.

**Tim Beiko:** 
* Okay, so, I think there the next step for this would be to actually flesh out what those edge cases and solutions are, and we can have that conversation at a time. Lucas

**Łukasz Rozmej:**
* so i'm not opposing going into Cfi if we can have a Cfi with a big asteroids that this final it's not spec is not the final eyes because of its cases.

**Tim Beiko:** 
* Okay.

**Łukasz Rozmej:**
* and in terms of the edge case itself. I think we should where it's possible, and the cost isn't enormous, and it seems in this case it isn't enormous to keep as much backwards compatible as we can. Yes, it is something that complicates things a bit, unfortunately, that's live for supporting a low level system. That's a lot of higher level systems are built upon. and I don't think we should break it. We are supporting as much as we can of existing stuff makes us seem more reliable in the long term.

**Tim Beiko:** 
* liam. You had your hand up, and then Andrew.

**Liam Horne:**
* Yeah, i'm mostly what I wanted to. I wanted to understand just kind of where we landed with 4844. if I can go into more detail about what i'm thinking there. But it's just the right time to jump in?

**Tim Beiko:** 
* Okay. So I think before it 4844 We've CFIed it people want it at some point in the next couple of forks. If it's Shanghai or not, is still to be decided. And I think you know it probably makes sense to move, to like what our time teams perspective on what Shanghai should be. The only specific EIP we haven't touched on is the DLS one. So I don't know. I guess. Yeah, maybe lets do DLS quickly. Then we can discussion. Shanghai, so we're we're kind of done with the Cfi stuff. But does anyone have a strong opinion in your direction about whether we should CfI DLS and and you know, consider it for either Shanghai or the fork after. 

**Lightclient:**
* I we should.

**Tim Beiko:** 
* Okay, Does anyone disagree with that? Yeah, we deals with DLS was CfI for burden?? so I yeah, Does anyone disagree? It should also be Cfi. Okay.  I will take this as a No. so just to recap. You know these are all the things that are centered in the next forks. you've added the rest of the EOF EIPs, and we've and also added, 4844 and DLS self destruct. I think we want to see just some better thinking around the edge. Cases. yes, rest of your life. That includes a 5450.  okay. So now, obviously, you know we have all these things we could be doing, which one of them we should do When is the biggest this the biggest discussion. I asked all the EL teams what they thought about this in the past 2 weeks, and the answers are like pretty different. So I think it maybe makes sense for just the different  to take a couple of minutes, and then do some CO folks here as well lets Just take a couple of minutes kind of talk through what? What would be your preferred kind of outcome for Shanghai specifically, and how that, you know, relates to everything else. yeah, we can. We can go from there. and, Matt, I know you've been sort of in the chats dying to have this conversation. So you want to start. And yeah, we can go from there.

**lightclient:**
* yeah. I mean, I for a while have felt that it's best to try and keep Shanghai small, you know.  Historically, client teams have preferred smaller forks to like very large forks and I think that if we go into this saying like we'll do withdrawals and 4844 and EOF that something will end up breaking later on, and something will get lost, and we'll spend a lot of like development, cycles and energy, trying to do all of the things, and then we come out with less of the things and more energy expended. So I'm like a proponent for focus, it being very focused on a small fork, and then trying to like somewhat quickly after, have, you know, another small fork rather than putting all the eggs into a single basket. so my preference is withdrawals and EOF for Shanghai. Try and do that sometime in March and you know, and then the other Cfi eps or sorry, not the CfI. Eps, but the things that we're CFI prior to this call and then doing like a Cancun fork with 4844, sometime, you know. Q. 3.

**Tim Beiko:** 
* Good. Thanks. Anyone from another. My team.

**Andrew Ashikhmin:**
* yeah. I think our preference is also to do us small Shanghai release with just withdrawals and the 3 small Eps. But if we want to make it bigger. I would, I guess, go for either 4844 or 2537, so pick one of those not make it too big.

**Tim Beiko:** 
* Okay. anyone from Basu?? or Nethermine

**Marek Moraczyński:**
* Yeah, I think I we are agree with Andrew. So withdraws should be a top priority, and we should decide what we want to target what we want to try to deliver. If we don’t have a huge delay because of this thing, we can do it later. But a generally a withdrawals plus trying to deliver EOF or Eip, or 4844

**Tim Beiko:** 
* And do you have a preference between those 2 in that environment, or

**Marek Moraczyński:**
* I think. Oh, team agree that we are slightly prefer for a 4844

**Tim Beiko:** 
* Charlotte.

**Justin Florentine:**
* yeah, so we're pretty much on the same pages, I think what like client outlined definitely withdrawals. I think we're more comfortable with all of EOF going in and then deferring 4844 to can Cancun

**Tim Beiko:** 
* Got it. So just to recap on the EL side. Obviously everyone wants withdrawals that come as soon as possible, and then the handful of small the EIPs that that we considered before and then, you know, there's probably room for something else whether that's something is 4844, EOF is unclear and yeah, I there was a bunch of comments from like a CL devs in the chat as well. Does anyone want to share their view there?

**terence:**
* Yeah, I guess I can go first. I think, like we draw remains the height. Paris remains the highest priority, I think, as as a court. There we have a responsibility to get withdrawal as fast as possible, and then also as secure as possible and I personally would not want to see withdraw being delayed by like anything else and that's just my perspective. And then, after we draw definitely 4844, just because I don't think it CO had to worry about EOF like, luckily. Oh, yeah, I think 4844 is a good target after withdraw.

**Tim Beiko:** 
* And when you say after that would be a separate upgrade right?

**terence:**
* Or yes, assuming there's delay. Yeah.

**Tim Beiko:** 
* okay, right. Okay. So if for it for for the delay withdrawals. Then we would just okay. Anyone else on the CL side?

**Ben Edgington:**
* Yeah.

**Paul Hauner:**
* I don’t have consensus from the entire team. But my personal consensus is align with Terence

**Ben Edgington:**
* I agree with Terrence and and Paul the I think there are. There are many unknowns, about 4844. We Haven't tested it in the network environment. and there is extra load on the consensus clients that we have not quantified yet. So there are. There are uncertainties around that committing to have it in. Shanghai introduces uncertainty about timing on that, and we will inevitably delay things. We love to be optimistic, but, I think it will will potentially delay by several months withdrawals, favor a small withdrawals fork on the consensus side, and then separate that. Decouple it from 4844. That that's personal view, not speaking for techy team specifically.

**Tim Beiko:** 
* Thanks.

**arnetheduck:**
* Yeah. I can agree with Ben and everybody else has in saying, which is that. we want to ship withdrawals our test nets, for withdrawals are coming now, and there's some things coming up. 4844 inevitably will delay Shanghai if we put it in there. So I would prefer to see a smaller Shanghai, and then faster, Cancun. Let's put it this way so that we can ship 4844 in a timely way as well.

**Tim Beiko:** 
* Thanks. Anyone else on this. CL side, Andrew. And then I know. Liam, you had your hand up earlier and Poto. You had a bunch of comments in the chat, so I think it probably makes sense for the 2 of you to to go after that. Andrew.

**Andrew Ashikhmin:**
* well, it just a an open question. So what do people mostly yell the the clients think about. Then if 4844 is going to delay. Shanghai. Then should we include either 1153 or BLS the compiles 2537, like what's is the sentiment like a pick one of those. Are the useful and do we want them in Shanghai?

**MariusVanDerWijden:**
* I think they're useful, but I think they would also delay So from my perspective.

**Marek Moraczyński:**
* Yeah, I agree with Marius. You know just what Like just what Mat, said you have Withdrawals in Shanghai, and 1153, and 4844 in the one after that, and I hope that by then we can stop calling it. Cancun and only used fork names

**Tim Beiko:** 
* Ansgar 

**Ansgar Dietrichs:**
* right. yeah. I just wanted to to say that I think it would be important to talk generally. Talk about time lines here kind of just to contextualize this discussion, but because I think a absolutely minimal fork could make sense. I personally, I would like to just hear some clarification around. it seems like some people will be like. For example, it sound like you would not be an extra constraint, at all, where some other clients made it sound like basically withdrawals plus one big change. Would delay it personally I think, if we do a kind of minimal withdrawal, for it should really be a fork that we can deliver on whatever that absolutely passes time in this we can like, I don't know. February focus something. 

**Tim Beiko:** 
* given everybody wants withdrawals to happen asap you know there's some conversation in the chat about like what's the quickest we can fork. I think, realistically for my net. That's probably March. You know, like it's basically end of November. Now, you know. Assume you get all of the implementations done before Christmas. That means you're testing stuff in January. You're forking test nuts in February, and you're like forking main net in March. you know it's hard to imagine things going quicker than that unless there was some sort of emergency. so maybe using that as like a, you know an anchor of like, you know what we can do. yeah. Assuming we wanted to fork and have withdrawals go live in in in March. you know what's what's possible to to include alongside that and that doesn't delay withdrawals significantly. yeah, I don't know if anyone has like a strong opinion there of. I guess you know. Geth is shared like for them. It would be withdrawals this EOF and it's unclear if other people feel that way about the EOF and I know earlier in the chat. Proto was saying that, you know, if we. if that's the line for 4844 you might be able to do it. So Yeah. anyone have thoughts on this Proto

**protolambda:**
* So based on the Cfi discussion. I like the meeting of Cfi. I think, like us cor devs after this call we're not doing our job very well. We should be singing and discussing the EIP in detail on these calls based on the merits of the EIPs, and to like, explain the impact a lot of tasks on if they're them as a protocol. and we should be listening more to senior. Also, outside of this call to set the roadmap rather done prioritizing EIPS purity on what we think is the right thing to do. and so with EIP 4844 Specifically. we are making this this big, impactful change to etherium. Must this data credibility layer? And I think this is super under values. delaying this with basically main roll ups today. Keep hijacking. Call data for something that was never used Never designed for and at the current rate. This means ethereum just grows linearly, and we'll keep growing linearly. These resources are mis allocated, and users are over paying a lot for layer 2 and by changing this long term layer, one can have less trust it' be less stress on the disk space and the consumption of layer on the exclusion to our clients and by basically creating the 0 some game between for it for 4844 and the EOF and EIPs we, basically we ruined the roadmap of ethereum But I, not listening enough to outsiders out of this call. and by setting priorities based on development rather than based on the pressures on the Ethereum network.

**Tim Beiko:** 
* Ansgar

**Ansgar Dietrichs:**
* right. I just wanted to say that I  agree with Proto that it seems to me that kind of from a how important and urgent is this point of view for it for 4844 It's the only urgent upgrade like withdrawals. We want to protest because we've been promising it for a long time. That makes sense, but it's not in itself urgent EOF. Again. We have been wanting to do a EVM. Upgrades for a long time, and I think it's a very sensible upgrade, but in itself it's not urgent 4844 is urgent, so I don't think that necessarily in itself means we should, if we we should not do a withdrawals only Shanghai for. But I do think that would depend on how much we believe this would delay for it for 4844 If basically we say having a separate fork means 4844 come arrives 3 months later, then I would very strongly be in favor of having one combined bigger fork. If people are confident that just separating it out into 2 separate forks has no or minimal overhead. i'd be fine with it, separating it out. But again, it would be very strongly dependent on the impact on 4844 not just the readiness of the EIPS

**Tim Beiko:** 
* I think. it's worth noting in a chat. There were a couple of comments about withdrawals actually being like quite urgent and critical, and you know, beyond getting people their stake. back. There's a lot of concerns about, you know, centralization and people not being able to move their stake around and and you know. so giving people the opportunity to withdraw It's not only about the Ether liquidity it's about like allowing people to then stake with providers, you know, either stake themselves or stake with providers that they think are better. because there's been a lot of changes to the staking landscape since the we can change went live. Jesse. Oh, just see if you're talking. We can't hear you still can't hear you.

**Jesse Pollak:**
* Hello!

**Tim Beiko:** 
* Oh, yes, No, we can. Yes, we can.

**Jesse Pollak:**
* just having you with the coinbase perspective. the the first thing is that withdrawals are the P. 0 number one priority for us. just like you know, other client teams here. It seems like, you know, everyone is aligned from my perspective that pushing forward withdrawals to to get out as safely and and quickly as possible is the most important thing we can be doing. Second I think, from a other. Cfi ,EIP., 4844 is the highest priority for us. we as I mentioned, Devcon are actively working to bring our customers on chain currently. We can't bring them on to Eth. L1 because it's too expensive. It Currently we can't even bring them on to Eth L2,, because it's too expensive, and we see 4484 as a key unlock, for actually enabling us to be able to bring our customers on chain and kind of continue investing in the ethereum ecosystem. And so that's a really important priority for us. and then I guess the third, the third thing that I'd say, and this is not a priority, input, but more just a process input, which is, I feel like there are kind of 2 cogent paths that we can take at this point. One is we say, like withdrawals are the most important thing, and we should do nothing that blocks that. and that means we're not going to take on additional scope and we're going to just push as quickly as possible to get withdrawals and then ship everything you know else that we want to do in the next hard fork I think the second path is, we say, withdrawals are the most important thing, and we believe that we have capacity to do X number of other things. and then we have a priority conversation about what those X number of other things are. I think if we get into the situation where we say the like. A third path, which I think is being proposed, which is like withdrawals, are the most important thing. and we think we can just slot something else in and we need to decide, based on, like the people who are kind of driving which respective things. Which of those is like the right thing from a size perspective to not impact withdrawals. It's going to just get subjective messy. and I don't think we do a good outcome, both from a process, perspective and from a kind of timing perspective. And so i'd encourage us to try and like which of those 2 paths we're going to take first, and then have the downstream conversation which which feels like it will lead to the best outcome.

**Tim Beiko:** 
* Liam. And then Guillaume

**Liam Horne:**
* I yeah, I fully agree with what I just said. I just want to

**Tim Beiko:** 
* you're breaking up Liam.

**Liam Horne:**
* Is it? Okay, now.

**Tim Beiko:** 
* a bit better. Yeah, try.

**Liam Horne:**
* Okay, it's breaking up. It's it's picking up. I'll try really fast from the Optimism. Perspective. 4844 is like clearly our priority, because we see it as an unlock for basically Ethereum, specifically being like establishing it as like the the the sole place you'd want to be going. If you're going to be building any new sort of sovereign blockchain environment, we from just purely having operating out. There's a main that constantly see projects that come to us, saying they they would be on Optimism, or more generally an Ethereum roll up if it were the case that 4844 or more generally, if Ethereum was just affordable to them for their use. Case and instead they don't, and they moved to other ecosystems or other worlds that Don't offer the Ethereum security, or any of the ecosystem benefits so it's, i'm saying the obvious here. but 4844 is not just like a win for roll ups. It's a win for Ethereum, because all these projects and these users that are going to other ecosystems will have a we have no reason to. because the Ethereums ecosystem will offer the exact same price at the in security that we're already familiar with. And so you know, i'm saying the obvious, but this it, you know. I think it matters quite a lot.

**Tim Beiko:** 
* Yeah, hey, sir. Thanks for sharing that Guillaume. You had your hand up.

**Guillaume:**
* Yup, yeah. So I was actually going to give some push back on what Jesse has said. yeah, we have those we have. Those projects different people are different, are interested in everything and  in different things, and they're pushing for their own. for what they think is is correct. I mean, we've been hearing different views. So some people believe withdrawals are more important some people really 4844 is more  important. I have to say both of them are important. In my view. The question is, I don't get the impression that either of those efforts are ready and I don't get like I ready to ship, and I also don't get the impression that's the there's a lot of conflicts between the 2, so we could perfectly have 2 forks like very close to each other, like clearly not the same week, but 1 or 2 months apart. And I mean, I would say sorry for the strong wording, but I don't care what the internal conversation that Coinbase is they are free to allocate the resources, how they see fit. But we're not going to. I mean, I don't think we should make a decision before we have any clarity on what the projects are going to be delivered at at what time. We just need to focus on delivering things. There's a lot of important things to be delivered in Ethereum. We need to work on that, and whenever it's ready it will ship. I think that's the that's the wisest approach.

**Tim Beiko:** 
* Right? I think on that, though there is like a there's like a path dependency thing here. So, for example, you know. if we say we're good, you know, if we say that 4844 is the next thing we're going to ship. Obviously, time teams put more resources on it than it happens quicker. If we say EOF is the next thing we're going to ship. The same thing happens there, and and you know there's not an infinite amount of of resources in in client teams. I think Another thing like just from the chat. you know, there was a lot of conversations around, you know, if we forked in March with like withdrawals, and maybe you know, some some minimal stuff.  Could we then have another fork with, say, 4844 it like around May or June And is that something that's like possible. so I don't know i'd be curious to hear like just from the client teams like. you know. Again, everyone seems to agree that withdrawals is the main priority, and you know we want to ship this as soon as possible, which, realistically is, probably around around March. you know, if we go down that path is it realistic to include for 4844 in that timeline, and if not, what's like a realistic timeline for 4844 to ship. Is it like we could ship it a month after? because it works all happening in internal, anyway, or is it? You know we're going to need 3 months or or 6 months. yeah. And, Lucas, I see you have your hands up.

**Łukasz Rozmej:**
* So I want to remind something that Peter should like you said, I think, like 2 or 3 All core Devs in the past. that realistically, we are not able to deliver hard forks very fast. So, having a timeline of 1, 2, or even 3 months between hard for is probably not realistic and this is because just coordinating all the definite upgrades, giving time for people to test, etc., etc., is a huge effort and if we if we treat 4844 same, a similar high priority as withdrawals, I would say, just bundle them in one big fork. this might delay it by a month for something or 2, but it's it will be generally a lot of faster to production than doing 2 forks and never mind, is able to do that in terms of capacity.

**Tim Beiko:** 
* Nice, Any other teams has a perspective on that.

**lightclient:**
* I feel like we showed after the Berlin hard fork with a very quick London hard for that. We are capable of shipping forks quickly, if the need arises, it's not the most fun. but it's very possible. So I don't think that we should make the assumption that we can only do one Fork.

**Tim Beiko:** 
* Yeah. And yeah, Berlin. And in London i'm looking now, we're less than 4 months apart. So Burden shipped April 15th, and London shipped August 5th, which is like just under 4 months. Yep. Marius

**MariusVanDerWijden:**
* Yeah. And I think the we we've improved quite a bit since then, especially in the testing department. And So 1 thing that I they want to point out. is that between Berlin and London we like we kind of had to create new features. If the code is ready by February, then shipping the the new fork is just testing it, and well and testing is done by by February. Then it's just enabling it on the on  test nets, and then publishing the final thing. And that's exactly 2 months, one month for going through the different test nets, and one month in a dissipation of the of the final hard fork. So we can. If the code is ready, we can push it in 2 months. If the code is not ready, we then there's no discussion. because then we will delay the withdrawals for for for it for 4844. So if if you can reasonably promise me that for it for 4844 is completely ready and tested in in basically January. then I think we can. we could schedule it with a together with withdrawals. But I  don't think anyone is willing to make that commitment. and so we will would delay with over there. and it's a at least for the Geth team. It's a different story with. We have EOF ready, and it will be ready and tested by January. and so it's. It's a it's kind of a different story for us. It might be different for other client teams, but that's for them, to say

**Tim Beiko:** 
* thanks Ansgar. And then, if any other one client teams wants to share, I think it'd be good. A lot of people are like typing this in the chat. I think it would just be good if some other time contact. I want to share their thoughts on the call, because most people will be listening and not reading the chat that's very visible on the Youtube stream. but yeah. Ansgar

**Ansgar Dietrichs:**
* So I just wanted to say that I would at least say that if we go with a minimum Shanghai, then I think the feature set there should be just be withdrawals plus things we want to include, but that we should be very ready to say in a month or so, if it becomes obvious that these features are not quite ready, and they would start delaying the for the to kick them back out. I think basically like a withdrawals, plus ideally, this and this kind of for make sense; but if we make it like a if it was, it depends with them too strictly. Now and then we have to delay the entire for it. I think that will be a failure.

**Tim Beiko:** 
* thanks, Daniel and Paul.

**Daniel Celeda:**
* Oh, so great, so quick one from me, instead of like having strong opinion on what should go first, and how, I will just give you that a short information how we?? What is the status in for the way in their minds. So we are working in parallel on 4844, and in withdrawals. And so from my perspective it's not that we drive us our. you know and but I agree with that. we could, you know, work that would be the best approach to work in parallel on both of them ship according to it, depending on on what is the status of both. But I understand that it could be a problem for Green in some of the teams. But could maybe we could actually ask, what is the status between between the teams of of these EIPS we just looking what should we shape? But we don't actually understand what it.

**Tim Beiko:** 
* Yeah, I think that's a good point. let's do, Paul, Daniel, and then we can end with just client team sharing what the status is, and also when they would need to make a call about coupling or not coupling in order to not delay. with withdraws. So okay, Sorry just came on. But like Paul, Daniel saw this, and then if we can just get yeah, the the teams to share the status of that. Paul, please.

**Paul Hauner:**
* Sure, I just had a single sentiment to the previous speaker that we're working on withdrawals, and 4844 in parallel, I think, doing a rapid fire for is something that we're definitely open to considering. might even in some ways help us, because it kind of on blocks. The 2 teams from each other, because withdraws is on. Clearly a few steps ahead of the phone for a 4844


**Tim Beiko:** 
* got it, Danno

**Danno Ferrin:**
* so as far as withdrawals, and and EOF and 4844. The efforts for the engineers are fairly segregated between EOF the other consensus layer impacting things. So from a basic perspective, we where you have, Lance is completely disconnected from the consensus layer work As far as my understanding of CL priorities. Withdrawals are much further along than 4844 work but I should let them speak to what they want to do, for together are separate.

**Tim Beiko:** 
* thanks. Saulius 

**Saulius Grigaitis | Grandine:**
* Yeah, so we're just thinking, you know, like before, 4844 is clearly not ready at the moment, and why we can just made this decision for a bit, and the I see what is the progress in the coming weeks, or a month on this? 4844, because there are already some something like 6 teams working on that And the there, I know if in a few weeks it becomes clear that, like most of all, the problems are sold then. maybe it makes sense to strongly consider it to include in the next hard fork, because at least from our experiences. it's much easier to to implement something that is already implemented by other teams and confirmment on the testimony. Comparing to you know, building a new feature where which is not, you know, tested and completed. So I think we have it, at least for my point of view. It looks like the decision. 4844 problems to be delayed a bit until they are much more clear. What is their actual status and the you know just to wait a bit until we share more results from the next test nets

**Tim Beiko:** 
* Yeah, I think that's probably like the the best place to end. is just from the different client teams that you know. If, like within, say, like 1 min can share. you know roughly where they're at with the different implementations, but also most importantly like, when do they need a decision about what gets coupled together right like because It seems like. So far the discussion is is kind of saying that you know these things are pretty modular. specifically 4844 and EOF and withdrawals, and they can all kind of progress in parallel. But obviously at some point we're going to need to like bundle them together. assuming we didn't want to delay withdrawals, and we wanted those that happen, you know, around around March of next year, when the client teams need to know which path we're taking right like, and kind of commit to something rather than just pursue different things in parallel. yeah, I don't know if any of your client teams want to. I share this.

**Marek:**
* Yeah, I think it will be good to resolve discussion as soon as possible about EOF. If versus EIP 4844 because if you, if we really want to do something in March besides withdrawals, we need to know it's like right now. I mean very, very soon. Right? Yeah, yeah, of course.

**Tim Beiko:** 
* liam. And then, if any other time teams want to

**Liam Horne:**
* on the thing I'll just really quickly shout out, is there are a regular 4844 developer calls. One is curious or was be willing to kind of join those calls. That's the right place to discuss the status of testing. These are been happening regularly for a while now, and we go pretty in-depth. So if anyone is curious, they don't feel like a sufficient amount of information whether their questions are being answered. That's the place to discuss them and there's like a regular cadence of these things. so i'd recommend anyone join.

**Tim Beiko:** 
* Yeah, thanks. I posted the information on the chat there. I don't know if Mario is on to talk about testing but if not the I curs from other client teams. if yeah, when when a decision needs to be made about coupling if we want to ship something around March. Potuz

**Potuz:**
* so I can just report some on what's the status on withdrawals. We are pretty much in scheduled, and we can have full test nets by January and i'm pretty happy to fork with rawls in for Goerli if a decision is made to include 4844 it doesn't matter when you tell us in, because it's clearly going to delay withdrawals. Anyways.

**Tim Beiko:** 
* Got it. I did. Your team have perspective there.

**arnetheduck:**
* Yeah, from members similar as Prison.

**Tim Beiko:** 
* Okay.

**Ben Edgington:**
* mit Ctl: and yeah, take you. Same, I if we wanted to do a march upgrade, I think we'd need to know the contents nailed down by the next call in 2 weeks, I'd suggest.

**Tim Beiko:** 
* Paul.

**Paul Hauner:**
* Yep. I agree with the previous speakers

**Tim Beiko:** 
* okay. So there's kind of a trade off there where earlier. Where is the saying like, you know, you want to have the code already, and that minimizes the time to to ship this thing once we decide to do it. Obviously it's unrealistic to have all the client implementations for either EOF or 4844 done in the next 2 weeks. But is it more valuable to like. Make that decision sooner, and you know. kind of decide which path we're going on the next call? Or is it more valuable? at least on the EL side to wait a bit more, and you know potentially to the first call of next year to make that call because we see? yeah, we sort of see more data about what these are. One chat comment about deciding sooner rather than later.

**MariusVanDerWijden:**
* So I think for guess it. doesn't matter too much, because we have we have EOF mostly done 4844 is also being worked on by Coinbase and Optimism. So Geth will probably be like the first one to have, like the finished versions of every everything. so I think it makes more sense, for so we don't. We don't really need to know prioritization because it's almost done.I think it makes more sense for smaller client teams that have, like resource constraints to speak up and say that, like they need to prioritize right, they need to prioritize one over the other, and I think it's important for for them to say how much time they would need to come like if we decide not to go with the Uf. And to go with 4844 only. Then they need to like one. probably like shift priorities quite a bit. And so I think client teams and smaller client teams and testing. should comment on that when they need to have this the decision.

**terence:**
* Yeah, same with Kristen, we will continue supporting 4844. We'll continue working on, but you will just be a separate branch, so we will not be merging any employees for our staff into our men develop branch unless it's confirmed. So for us, confirming like sooner or later, it doesn't really matter.

**Tim Beiko:** 
* Got it? Thanks. I guess, liam, and we just have your hands up. We can wrap up with I, you guys, because we're already at time. And yeah, so please be

**Liam Horne:**
* Oh. Sorry 

**Potuz:**
* i'm just quoting what I've what I wrote in chat I think there's been consensus, and I unless i'm mistaken everyone here agreed that we do not want to delay withdrawals, and no one claims that we can actually ship the 4844 as early as we're thinking, we can claim we can ship withdrawals, so I think, on the CL. Side every decision is already made. We are not shipping 4844 in February, as we're thinking February March, as we're thinking, we withdrawals, and then the remaining the EIPs do not affect us so. I think this is a No, no problem for CLs and the decisions are already been made. Yeah.

**Tim Beiko:** 
* okay, I think that's like probably a good place to wrap up like, I think. then, the question for the cl kind of moves to like. you know schedule and and past these, for example. Obviously there's the Cl call next week where death can be discussed. so I think it makes sense for sale to to have that conversation there, I think. would probably make sense on the el side of the next 2 weeks is they get like a strong view from client teams around, like which EIPs well, you know what if we want to do a fast withdrawals? You know what's the best set of vips that works for them there And I think, you know. trying to to narrow down that scope and and finalize it on the next call would be really valuable, so that we kind of head off to the holidays. And we know. yeah, we we know what's what's being included alongside withdrawals. So yeah, let's continue the 4844 kind of scheduling and you know sequencing conversation on the sale call next week, and if el teams want to. look at the other ips that are being worked on and and consider what could be included without delaying withdrawals. we can consider that on the next call anything else ? people want to share before we wrap up Oh, and we we didn't get to the Engine. Api stuff apologies again. we yeah. We discussed this a bit on the CL call last time. But, Mikhail, maybe is there a 1 min, you want to.

**MariusVanDerWijden:**
* but can we? I would like to give a like a 30 s update on the withdrawal test net. We started a we started a dev net with Geth, Nevermind a Prism Lighthouse, LordStar and Teku. Yeah, sorry, Teku. And all of the clients are still following the chain. I think maybe Lighthouse had some some  issues. But yeah, so we we're on track, and it's going pretty well. So i'm very bullish  on withdrawals.

**Tim Beiko:** 
* Thank you. Thank you. Okay. So yeah, and I think next call. cause yeah, we did get sorry to sidetrack by basically everything else on on this call, I think. Next call we should start with an update on where withdrawals are at that'll help kind of ground everything, and then we can also quickly discuss this engine Api issue, so that we don't skip it for a third at the time. Yeah. okay, Barnabas. And then we have to close because we're already over

**Barnabas Busa:**
* in willing to weeks, and I would like to be able to test for every clients withdrawal, and for that I would like the client to reach out to me because i'm organizing now for the visual test net And if you have any problems or any questions, just let me know and find you on discord. Number one of us

**Tim Beiko:** 
* cool. Thank you. Anything else. Okay? Well, thanks. Everyone. and talk to you all next week on the next call. 

## Date and Time for the Next meeting: 2022-Dec.-8-14:00 UTC

## Attendees:
* Alex Beregsz
* Potuz
* Jesse Pollak
* Lightclient
* Saulius Grigaitis | Grandine
* MariusVanDerWijden
* Marek Moraczyński
* Pooja Ranjan
* Barnabas Busa
* Mario Havel
* Crypdough.eth
* Ben Edgington
* Danno Ferrin
* Carlbeek
* Terence
* Paul Hauner
* Mikhail Kalinin
* Andrew Ashikhmin
* Marcin Sobcz
* Pari
* Holger Drewes 
* Roberto B
* Protolambda
* Ashraf
* Trent
* Mario Vega
* Stokes
* Kamil Chodola
* Dankrad Feist
* Karim T
* Alexey
* Guillaume
* Francesco
* Sara Reynoldsaa
* Pawel Bylica
* Ruben
* Arnetheduck
* Oleg Jakushin
* Vitalik
* Ansgar Dietrichs
* Łukasz Rozmej

## Links Discussed in the call:
https://github.com/ethereum/pm/issues/662
https://ethereum-magicians.org/t/proposal-predictable-ethereum-testnet-lifecycle/11575
https://github.com/taxmeifyoucan/ephemeral-testnet
https://github.com/ethereum/execution-specs/tree/master/network-upgrades#definitions
https://github.com/ethereum/execution-specs/tree/master/network-upgrades#process
https://medium.com/ethereum-cat-herders/shedding-light-on-the-ethereum-network-upgrade-process-4c6186ed442c
https://github.com/ethereum/execution-specs/tree/master/network-upgrades#definitions
https://github.com/ethereum/pm/issues/450#issuecomment-1323758031
https://github.com/ethereum/pm/issues/450#issuecomment-1323758031a
