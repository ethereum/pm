# Consensus Layer Call 97

### Meeting Date/Time: Thursday 2022/11/3 at 14:00 UTC
### Meeting Duration: 1.5 hour  
### [GitHub Agenda](https://github.com/ethereum/pm/issues/630) 
### [Audio/Video of the meeting](https://youtu.be/GWkhFCvwOT4) 
### Moderator: Tim
### Notes: Alen (Santhosh)


## Intro [1.09](https://youtu.be/GWkhFCvwOT4?t=68)
**Tim**
* Okay. Good morning everyone. Welcome to Consensus Layer call #97. Danny's out this week. So, I'll be the one, facilitating this. 
* We have quite a few things on the agenda. I think this is our first call since, the post merge one. lots of stuff around withdrawals. then getting to this conversation around, the engine API and the block value that we sort of didn't have time for in Allcoredevs. and finally, there were a couple other topics. so the rebase of the F four four spec on Capella. the proposal for historical batches, some follow up of the gorde discussions and a way we can potentially fix that on the CL side. and then some updates from MEV Boost. and I think that should, cover it.
* Yes, I'm just covering for Danny being quote unquote out for a long time. I believe like client saw Danny, in person, so hopefully he's still around. okay, I guess, to kick us off, so there's two, there's two PRs on the withdrawal side, that we've been discussing. there was the one about moving withdrawals through a single queue by Danny. tons of discussions on that. And then POTS added or opened a new draft PR this week, which, removes the queue altogether and it seemed like there was some support on that. but then also a couple of pretty significant comments in the past, day or so. and Potus could not make it on the call. is there anyone who wants to just kind of share quickly the context and, and where things are at on that PR Test? 

**Terence**
* Test? Yep. Can can, can you hear Me? 

**Tim**
* Yes, we can. 

**Terence**
* Yeah, Yeah, Sorry. Yeah, so I guess Potaz can make it, I thought he could make it, but yeah, I guess I could give a high level summary on like portal approach sot ODR currently to process withdraw, there's three processing, there's two loops, one for full withdrawal and one for partial withdrawal. And this is not ideal for both like complexity and performance perspective, but one thing that's good about this is that full withdrawal is treated differently than partial withdrawal. 
* So therefore it has some variety. And some people really like this and this is also easier to test for this bad test perspective because now you have full and partial and because they're separate, right? And then they open a PR that's 3042 and this was born to withdraw into a single function single pipeline. Therefore, it is slightly simple to implement. And then, but this has a downside that the partial and full withdraw, they are treated equal. So this ship the fairness under certain circumstances and therefore full draw may take longer. And this is also like harder to write bad tests because everything's under one loop and client may have to, implement some, some cash around it. But those are client implementations. So, after seeing this Potuz actually came up with something else because he felt that, well, maybe we don't need the queue, right? So we don't need a queue, therefore this is actually much simpler from the spec and client limitation. And then you can remove constants such as like max withdrawals per eppo and then also max, max, withdrawal Q limit. 
* You also reduce pressure on like equal processing. So, and then also the look of for finding withdrawals in a block for the happy case of small and fast. Since, since the pro block limit is quite small, this also has the same, argument versus the one you approach such that the full and partial are treated equally, but that can be further, its tend or improved. For example, like you can use some ratio system that you can do variety over, over like full draw. there are some concerns such as that, well, like if the network has like inactivity over five days, well data get slash before processing partial withdrawal. But, and then with those concerns it could get more expensive. But generally, I guess from the comments I'm seeing from other, from other client teams, it doesn't seem too bad. So yeah, it seems to me like most of the teams have like a proof, on this PR and this seems like a way to go. So yeah, I'm curious if I miss anything, people feel free to chime in and please let us know, like how we can proceed further. 

**Tim**
* And I think there was I, Oh, sorry, Marius Yeah, go ahead. 

**Marius**
* So I have, I really have no idea about this, but one thing that I, had a question about when reading is with the withdrawal queue, the order of everything is under consensus, right? With this new approach, it's the order of the, of the like will every node deterministically come to the same order or can you like, I don't know, prioritize your own withdrawals over others or just say, I didn't have any withdrawals and I kind of like, sensor withdrawals or whatever. 

**Paul**
* It's fully deterministic. You can't censor. 

**Marius**
* Okay, perfect. 

**Tim**
* And yeah, like reading, or I guess skimming the PR and, and the discord in the past day, it seems like pretty much all client teams support this. but is there someone who opposes Potuz's proposal and thinks, Danny's like the 3042 would be a better way to go? Thanks Marius. 

**Micah**
* Someone Give a, someone give a, like, I don't know, one, one paragraph description of how withdrawal order is determined when there are more withdrawals that then can fit in a block. Those of us that aren't familiar, intimately familiar with this 

**Lion Dapplion**
* In the new approach or the current approach. 

**Micah**
* New approach

**Lion Dapplion**
* So you have, you have pointer that's persisted in the states and this would keep looking and the will process withdrawals up to the capacity of the blog, then it would stop and that would be persisted on the states and that continues on the next, on the next blog. 

**Micah**
* So, so is there still a withdraw queue? It's just in a different place then what you're describing sounds like a withdraw queue. 

**Lion Dapplion**
* So I would think in terms of, of a pointer that loops over the states and just stops when there is no more block space for withdrawals, Right? 

**Tim**
* And so the thing is you don't need to store the full queue, you just need to store the pointer. Is that correct? And this is why it's simpler. 

**Lion Dapplion**
* Yeah, so the way it was looking before is if at specific epoc, if there is, a large amount of withdrawals that would be cured by order of index from less to highest, and that would be the queue. as the epoch processes through the blogs here is just if we start, we start that index zero, if we can process say 120 indexes, word of withdrawals, then it will stop and then the next bucket will continue after the point that it has passed. 
* If index one becomes available, it will need to wait for this pointer to look over the set to be included. 

**Micah**
* So let's say a hundred people, let's say we have room for 10 withdrawals in a block and a hundred people all the same time decide just miraculously, they all simultaneously say, I wanna withdraw right now. So you have a hundred people that wanna withdraw, but only 10 can fit in the block. So presumably those a hundred people need to line up in some way or somehow be sorted, right? Are we still recording hundred people? Like, or the nine, only 10 of them get in just the first, come first serve another 90, try again on the next block and race each other. 

**Lion Dapplion**
* So it's that first conference serve by index provided that, that you are after the pointer. 

**Micah**
* So the, so all hundred people would register themselves as wanting to withdraw and that would still happen. Is that correct? 

**Tim**
* Well, it depends on your validator index. 

**Potuz**
* Can I probably here a little bit. so there might be a misconception. you do not request to withdraw, you request to exit a validator. I guess that's what you're, So all exited validator automatically will be available for withdraw. So what we're gonna do is you start today your pointer was pointing to validator numbers 100 and you're gonna check 100 is available to withdraw. Okay, good. 
* Then we put it in a block, we go to 101. Is this guy available to withdraw? No. Okay. So we go to 102 until we finish like getting the 16 ones  that we can put in a block and then we continue after in the next block with the next in index. So it doesn't matter when you actually are out for withdrawal, it just only matters what's your validator index. 

**Micah**
* And I'm guessing that we, the, clients don't need to actually loop through all 400,000 validators. There's some easy way to skip over. 

**Potuz**
* You will. So there's a very, nasty case, which is that no one wants to withdraw. So no one wants to take out all of their Eth. And also the whole network has been leaking for the last five days. So in this situation, then you're gonna go over the whole validator set and you're not gonna find a single withdrawal. 

**Mikhail Kalinin**
* I think if you're also leaking and there are just a few people that are willing to withdraw. It's also like a kind of nice case cause you might not meet them like scanning for say, a hundred thousand validators And that those nasty edge cases aren't so bad that the clients will fall over. 

**Micah**
* Like you can still handle that within 12 seconds, no problem. 

**Potuz**
* Yeah, we can handle those. So we are doing any ways a full validator set loop, in four choice on every block. And last time I timed it, it was five milliseconds. 

**Micah**
* Okay. There's been talk in the past about wanting to allow people to exit without withdrawing. Would this make that significantly harder? Should we decide to implement it in the future? 

**Potuz**
* So with All of our withdrawal methods will automatically withdraw you if you have a Eth one withdrawal address. 

**Micah**
* So yeah, I think that the idea with withdraw is that if you are, no, if you know you're going to have an, an outage for some amount of time, like let's say I'm going on vacation, I'm gonna turn my computer off for three weeks, I want to exit, but I don't want to go through the whole withdraw process because as soon as I get back I'm gonna rejoin right away. 
* The idea is to make it so users, again, this is just a proposal, this isn't final or anything, but the idea was is that someone might want to exit leaving their stake on the beacon chain and then when they return, they would reenter without having to go back to the execution layer and then back to the beacon chain. would this change make it so such a feature is harder to implement should we decide to implement Such a feature? 

**Potuz**
* It's not going to be harder or easier. there are research projects about putting validators to sleep and yeah, so nothing is set. okay, this proposal is not going to make it any higher, harder, or any easier. Most partly we're gonna have, if we want to implement that, we're gonna have to have a different figure instead of exited, but sort of sleeping validator. 

**Micah**
* Got it.

**Gajinder**
* Yeah, I think it should be easy to skip the validator to pushing in the withdrawal queue if you have that flag of sleeping, set for A particular validator. 

**Tim**
* So does anyone have an objection to Potuz's proposal? 

**Stoke**
* So this is not an objection on if someone has one, they should chime in, but there was like one kind of open question on the PR, which was if we want to bound how much you look per block or per slot, I know Potuz's do you have any thoughts about that? 
* Yeah, so, we, perhaps I'm not counting correctly, but it's, I think that most of us would not object that and some people really wanted this. So I think it's probably a good idea to add a bound. my only objection to the bound is that I think it should be very large because it should give us enough time so that holes in the validator registry given by validators that actually exited do not become so many that we're gonna be proposing blocks without all, without all withdrawals available. 
* So I think this constant, if we put it, which I'm not opposed to, it should be of the order of two to the 17, so say like a hundred thousand validators or something like this. And, but I think everyone agrees that this, there should be a bound to have a constant boundaries better than having this ever increasing number of that. We're gonna continue depositing. 

**Potuz**
* Yeah, I think that makes a lot of sense. So perhaps in like the next day or two, we can work on that and yeah, it sounds like there's pretty complete agreement on 3068. 

**Lion Dapplion**
* So I wanna add, I did a proposal on the PR that had bugs, but it should be fine with a bit more complex code to have both a no queue approach plus no wait for full withdrawals. So extend approach of to just have a double pointer and loop for full and partial independently. I'm not sure if that's support for that, but that would be like the best of what was, 

**Stokes**
* Does anyone feel strongly enough about prioritizing full withdrawals that we would add more state to the beacon state? 

**Lion Dapplion**
* So it would add four bites and it's not, it's not exactly prioritizing, it's just allowing them to be processed faster. 

**Potuz**
* So the problem with approach is that it makes the full loop on every block if there are no, So we do expect times people are not with fully withdrawing and are only partially withdrawing. And I mean this, this should be the common scenario and this proposal will make it so that we run the full loop on every single block. it's not something that part particularly bad, it's just that it's just more complex and it has this full loop on every single block. 

**Lion Dapplion**
* I mean, you don't really have to do that. So if you at, at every epoch do one loop and pre-compute the list of potential with that should be sufficient. I did that at demo implementation two days ago, and it's not complicated. And for the normal cases it should be extremely light and you can have discuss attached to the state. you can have either being forking or not. each one has different tradeoffs, but that easily prevents having the loop having to loop on every block. 

**Seananderson**
* I mean, my opinion is that it's probably worth prioritizing full withdrawals if it's like, not too much additional complexity just because otherwise in the normal case, I think if there aren't many full withdrawals, you'd be waiting like around two days or so because almost everyone on the network will have partial withdrawals pretty constantly. 

**Lion Dapplion**
* So I, hey, I think it's important to clarify that there is no prioritization here unless there is a mass slash event because the, the churn is really strict. So, unless there is a bump at the start for people that have exited before we activate Capella, partial withdrawals will take the best majority of withdrawal block space. So it's just a matter that the approach, having a, the partial pointer affecting the, with the full pointer, it will just, add an extra delay, but I don't really buy the prioritization argument. 

**Stokes**
* So then why would we make this change? I thought it was to prioritize full trials. 

**Lion Dapplion**
* So it's not really to prioritize, it's to not add, a delay, an artificial delay on them. 

**Stokes**
* Okay. Well I'll just echo what Micah was saying in the chat. Just like, even if it's just like only for bytes, it's like a whole new field and it's smart to test. And so like generally I think we need like very good reasoning to include stuff, in the beacon state, right? Cause like we'll have to maintain it forever and test it forever. So what I would suggest is we get 3068 in a good place and then, you know, you could open another PR to that once that's together. but yeah, personally I think we should just keep it as simple as possible. 

**Micah**
* Can we add the, the second pointer they're referring to, can we add it later just as easily as we can today? Or is there some significant advantage to adding upfront? 

**Lion Dapplion**
* No, that could be add later. And I agree. I would pouch for simplicity, it's just that we, we can avoid this UX penalty, so I think we should try to, but yeah, I agree. If it's complex, we I would be totally fine not doing that In my recommendation. 

**Micah**
* Then if this can be added later, just use days now, then my recommendation would be, do the simplest thing first and then have it live for at least one fork, see what the actual behavior on mainnet is like, and see if people are complaining, see what the delays actually are like once we clear out the historic with draw queue. And then if it does seem to be a very significant problem, we can add it in a future hardware by vote. 

**Tim**
* Does anyone oppose that? Cool. Okay, so I think we have consensus we're gonna keep working, on polishing Potuz's pr. So, that's 3068, and that sort of supersedes, 3042, which was kind of heavily discussed before. and I suspect in the next two weeks or so, we should be able to have something that's quite final and, and potentially merge into spec. yeah, so we can keep, keep making progress on the withdrawal front. Anything else on those two PRs? 

**Stokes**
* Just one thing to chime in here, and I think there's been a lot of discussion across both of them, but the one thing with this approach is just making sure there's not like, you know, undue extra load if there's reworks. So, you know, rather than going at the epoch, we're now basically moving the processing into a per block setting and that's fine, but you know, if there's like some crazy forking situation, does this like put more cash pressure or something like that, that we don't expect? 

**Potuz**
* So Yeah, so the way, the way I'm thinking of implementing this, I'm gonna do this today, I think it's zero optimization. It's just run the loop. whenever we update hack, and I think this is immediately reorg resistant because you're just gonna comput it again on a reor and there's essentially no load, because we're doing this and this loop, this full loop anyways on fork Choice, once we realized that we're doing this full loop anyway in fork Choice, then I didn't mind any of these implementations because all of them don't suffer much, of a performance issue. 
* That was my first concern, and that's why 3042, I think with Paul as well. But then it turned out that it, it's really not that bad to do that full loop. 

**Stokes**
* When you say full loop, you mean a full loop? The entire validator set. 

**Potuz**
* Yeah. So, and, and we're proposing to put, to add this bound, but even if we didn't have this bound, it would be fine to just compute it, to just compute it, on a reorg immediately. Again, there's no need to cash here. Anything we would need to cash if we add something like, Lion's proposal to have like the list of, fully withdrawal and this is, per epoch, but, if we don't need to cash anything, I think it's fine. Just for computing it, you only compute up to 16, 16 withdrawals per block and that's it, Right? 

**Gajinder**
* Also the point to note it, no, that is to notice that, the worst case scenario is when we do the full loop. Most of the times when most of the people who would have set their, their payout address, I think we will, we might just end up doing in 30 or 40 props at best. I mean at worst. So it won't really be a full loop anyway,

**Potuz**
* So The, yeah, so, so typically the loop is going to be only the next 16 validators except the few that might be exited. But the problem happens if the full network has done already a loop, so everyone did a partial withdrawal because with this proposal, with any proposal, all of your validators will be with 32 Eth and not much more. So if you spend like a week leaking, then all of the validators will be below 32Eth none of them will be withdrawal. 

**Stokes**
* And then in that situation, you're gonna do this loop on every block, And you're still saying, like, even in that situation from your benchmarks, it's not an issue. 

**Potuz**
* So either way, I, it's Not really an issue if we put this bound at a hundred, a 100 K, right? I think it's in the, it's in the microseconds per loop, Right? 

**Stokes**
* So yeah, I mean, I think we go with what Tim said, this is the direction, but also just everyone listening as you're implementing this, just think about this particular topic, on that topic. 

**Arnetheduck**
* One more question. I haven't really seen the proposal yet, but excuse making nervous. But, the effective balance, how much does that change? Because that's actually when the effective balance changes that actually a little bit more expensive, because then we have to, hash three root things, validators in particular, and that's, as everybody knows, one of the bigger pain points performance wise. 

**Potuz**
* But, so there are two kinds of withdrawals. One of them is already on exited validators, and the balance is going to become zero, and the other one is removing all of the excess from the effective balance. So the effective balance is not going to change. It's gonna continue being the max effective balance. 

**Arnetheduck**
* All right, great. Thanks. 

**Gajinder**
* I have, Yeah, I think also discussing to have, to have to, to leave a little bit of margin so that, you know, we don't really drop, the max the effective balance, even if, for example, there are few mis registrations. so I'm sure whether people feel strongly about it, 

**Potuz**
* But I think No, I it's not, that's not really the reason, right? You cannot miss your effective balance by just that missing  stations. 

**Speaker 01**
* Yeah, the histor takes care of that. You'd have to drop down to 31.75 balance before your effective balance drop to 31. So you've got 0.25 Eth margin.

**Lion Dapplion**
* So if I understand the comment is that whenever someone withdrawals after withdrawing, it will trigger a change from the process. Effective balance updates function. Is that intentional? 

**Potuz**
* No. Why, why would that happen?

**Lion Dapplion**
* So process effective balance updates, what it does is it eliminates state validators. And if the balance has deviated sufficiently from effectively balance, then that would be updated. And that's what's gonna happen when you withdraw. 

**Potuz**
* Why would that happen? Your validator never. So it changes your balance from all to zero. And that's gonna happen on all full withdrawals anyways. And on partial withdrawals is not going to change your effective balance because Yeah, sorry, I'm talking only about full. Okay. But then on full withdrawals, these validators are already exited, so there's no problem that, that the balance becomes zero. 

**Lion Dapplion**
* Right? But that's, that's when I extra hashing. But I guess that's fine. 

**Mikhail**
* Question, are you suggesting to have this limitation on the max number of scanned valid errors  in this spec? Like a a hundred thousand as you mentioned? 

**Potuz**
* Yeah. It's just a constant, right? So it's going to be some, some configuration constant, some preset, Yeah. Yeah, yeah. 

**Mikhail**
* Some preset. Its not in this, in the, PR yet, Right? 

**Potuz**
* It's not in the pr. I wanted to see if there was consensus. It seems that there is consensus, but someone raised now the issue of like the minimum scheme amount, and I'm not sure if Jim is here, but Jim has a good point. I think it's a valid point that if withdrawals are too cheap, then it becomes expensive to produce proofs for them because the withdrawal itself doesn't pay gas, doesn't pay the gas of the proof. 
* So that's the actual reason that Jim is proposing to have a minimum scheme amount. I am very skeptical in putting such a constant because, this depends on the price of Eth. So if, if we put a constant now, it might become a lot in a couple of years and then we need to change it. And that requires a hard for just to change a silly constant. 

**Stokes**
* Yeah. Again, I think from a simplicity perspective, I think we leave that bit out. And if you need to, you can batch your proofing right at the Yale. 

**Gajinder**
* I just want to bring to attention, that in consensus specs there is, a test case in which, the valid, the validator is withdrawing as well as it's present in the current sync committee. So I, in the consensus group, I have sort of mentioned the test and maybe those can be rectified. 

**Tim**
* Okay. Anything else on the withdrawal PR? 
* Micah, I don't know. You can't trigger, I guess if your balance is, you're gonna be automatically partially withdrawn every block if your balance is above 32Eth. So I don't know. 

**Micah**
* That's Oh, I missed that. 

**Tim**
* Yeah. I didn't realize this was fully automated. Okay. Yeah. So we are dossing the queue ourself in a way and Okay with that. 

## [RFC] Engine API: Add block value in response to engine_getPayload execution-apis#307 [31.43](https://youtu.be/GWkhFCvwOT4?t=1903)

**Tim**
* Yeah. Yes. okay. Sweet. the next thing is kind of related. Alex, you had, I don't know if it's your PR actually, but you yeah. Your PR about adding withdrawals as part of the engine api. yeah. Do you wanna give some quick context on that? 

**Stokes**
* Sure. Yeah. Okay. Yeah, so Tim just linked it in the chat. That's very helpful. So, there shouldn't be anything here other than, silence because I think this has been reviewed. it's just adding the extensions to the engine API to support withdrawals and yeah. Okay. It looks like they're just a comment by light clients, but otherwise, yeah, I will address that. 
* And then basically I just wanted to give everyone one more chance to say, you know, we should change this or we should hold on it, otherwise I'll go ahead and merge it. and this piece will be subtle. So does anyone have any additional feedback on this? 

**Gajinder**
* I have sort of used it, implemented it and interrupt with, and it works fine. So thumb up from my side. 

**Tim**
* Okay, sweet. So, yeah, we can go ahead and merge that. next up, there was this issue about, adding the block value in the engine api. We wanted to discuss this on our Allcore devs, ran out of time. And the idea is that this would help, validators compare the value of their local block to something they get, from an external builder. there was a bunch of back and forth on the PR about how exactly we should, compute this value and what's the right comparison to have. I don't know. I think Terrance, you were the one to bring it up on all core devs. do you wanna give a quick update on, on where we're at, with this? 

**Terrance**
* Yeah, so I just wanna say this PR will be really helpful. It's like the baseline for censorship, like resistance for like just defense again, censorship. For example, we can have a Aly flag. They basically implement a ratio and can compare, say like, okay, if the bid from the builder is half less than my local block value, in any case, I will select my local block essentially. 
* So I think this definitely opens a lot more avenue to this type of defense. So I'm basically, I really wanna see this happen. In terms of progress, I honestly cannot say much I have been following as well, it seems to me. Yeah, it seems to me maybe Lucas from Nethermind or Yeah, or someone else comment on that. 

**Lukasz**
* So in terms of progress, so I think it's fairly easy to implement in any client. the thing is just, focusing on the spec, what do we want to implement? because, I seen that in Geth it was, I think prototyped as only the fees, was returned while, for example, in the old flash spec, it was the delta between the balance of a receipient before and after block while the, the proposal here was about the, just the balance after block. So we just need to figure out which one we want to do, and that's it. So from my opinion, the balance after block is the easiest. but yeah, but it depends on the use case. What do you want to compare, right? 

**Stokes**
* So I think we want the diff right, not like the complete balance. Cause then you can just directly compare that to bids from remote builders. 

**Tim**
* Mikhail, you hand up. 

**Mikhail**
* Just a quick comment on that. I feel like, yeah, I feel like we should have something simple here and it definitely should be compliant with how the bid is computed, by builder. if we'll have any fancy logic of compute this, bid, and then we will incorporate this logic into EL and then this logic, after sometimes is changed on the builder's side. For whatever reason, we'll have to change this, on the EL side as well. And this is what just, you know, what I would try to prevent from happening, design in this particular thing. So we just need, I think that balance, absolute balance is fine. the deep is also fine, but, yeah, something else probably, be more, like more just adding more complexity without any, gain. 

**Gajinder**
* So I would like to add, points of opinion on this. I think it should be diff because that is the perfect, target, that builder may converge to. And most of the times builder will also match that if, for example, if, there is, there is no, self-initiated withdrawals or there is no payment into the builder, proper builder, account. So most of the times it'll match.
* And, and for the engine api, it should always be the perfect fees that that is being paid to the pre recipient. So maybe over the time builder can find a way to converse to this, but 99% of the time it'll anyway match. 

**Tim**
* Chris, you wanna give the perspective from the flash bot side here? 

**Chris**
* Yeah. There has been lively discussion about the block scoring and better to, sport as the diff or as the value the payment transaction, which seems to more accurately reflect the additional value provided to the proposal because otherwise transactions to and from the proposal fee recipient will inflate or deflate this value without any doing from the block builders. I guess any way implemented in Geth or in the engineer APIs, fine. But there's another discussion going on about in the builder specs, what should be the bit value? Should this also include, mainful transactions to the proposal fee recipient? And there is some back and forth on this. 
* I post the link again here and it's also a question about what is the easiest to, as a, if we would include a payment proof as part of the bids in the build specs, which type of proof would be easy to validate inside MEV boost? So MEV Boost could filter out bids that are not conforming or, but that the proofs are not valid, if that makes sense. So I think in general, it, there's no clear consensus which way to go, but it's an important discussion that we would like to see moving forward. 

**Tim**
* Got it. anyone else have comments or thoughts on this? 

**Lukasz**
* So, my comment here is that I'm not sure if we are talking on the same level because we are, I think this discussion is about, consensus clients and its configuration being able to pick, local build block, even if it's slightly worse, for example, but it needs to be able to compare how worse is it than the one from the MEV boost, and just pick up because someone is fine, not, not receiving small amount of additional fees in terms of, providing uncensored blocks, right? that's I think is the, yeah. Final value. And you're talking about payment transactions, things like that. We don't have this concept here at this level. 

**Chris**
* Well, but it compares to the bid value that the builder network provides as part of the bid. So there is like this same relation here because you're going to compare it to this blocks core that is not yet divided. So I agree it's not the core question, but it's, related and just want to bring up the connection. 

**Marius**
* So one property that I kind of like about, about doing the diff is that it kind of improves, like it encourages transactions or like transactions to the builder or to the validator in that case, increase the likelihood of the block. So if I have a transaction that pays 20 Eth to me, then this will increase the diff and I will be more likely to put this transaction into my block. The problem is the other way around, because, gas will always include local transactions first. all of my transactions that decrease my, the amount of money I have will negatively, impact my score kind of unfairly because that it's transactions and it's not really that I'm losing money because of this, because of the block that I sent. 

**Micah**
* Right. And if, if any of you boost decides to use, block scoring, then it would be using the same strategy as the EL and therefore they'd be directly comparable If it, any of you boost decides to go with or the relays or whatever, whoever doing the block scoring, if they decide to instead go with payment transaction, then the situation you described comes into play. So Mikhail, I think the, the problem here, if I understand correctly, is that if the relays are submitting bids in the form of payment transaction and the EL is submitting bids or the equivalent of a bid in the form of, fee recipient balance change, then the two aren't actually comparable because the reasons that Marius just mentioned. And so either we need to accept they're not, we're comparing two things that aren't, shouldn't be compared, they're basically different units and we just kind of accept that and in some cases we're gonna get it wrong. Or we do the same thing as the relays are doing in terms of what they've been bid submission is, or the relays submit a bid and they also submit the thing BL is doing. So there's basically two versions of the bid. 

**Mikhail**
* My understanding that we just try to, evaluate the value of the block of the local block and compare it to the value of the produced block. 

**Micah**
* That's, so we don't know the value, We don't know the value of the block coming from the relay. We only know the bid that was, We know the claim. 

**Mikhail**
* We know the claim, right, Right. 

**Micah**
* But the claim is a different unit. The claim is what is the payment, Let me rephrase that slightly. The claim being made is either going to be, we claim this, the balance of the free reci increased by this much, or the might be we claim that the, fee recipient received a last transaction the block that paid them this much. And those are two different things. And the relays and the maybe Boost and all that haven't decided which one they're gonna go with yet. And so if they go with the latter one, then the claim they're making is not comparable to the balance change of the in the block. 

**Mikhail**
* I agree with that, but I don't think it should be comparable. I mean, like the algorithms, like the ways of evaluating these two, these two let's call it this way anyway, is different. But yeah, I think that it's okay. I mean it's, if claims that A pays, propos this amount of Eth and luckily, build block is estimated with a higher amount of Eth pay two propos, then yeah, that, that's it. We just need to set the right algorithm for estimate and the local, value, that we can get for proposal. 

**Micah**
* Right. So the, the problem is, as Maria has indicated, there will be situations where the locally built block will underestimate because the user is sending a transaction from the fee recipient address, and so therefore they're balance decreased over the course of the block. 

**Mikhail**
* Ah, yeah, I see what I mean. Yeah,

**Micah**
* That's, and That's fine as long as the bid, that's fine, as long as the bid from MEV Boost is of the same form because they're comparable. And so if both of them include that knowledge transfer and there is an edge case because gas will include local transactions, whereas the builder won't. but you know, for the normal cases, I don't think that's an issue. 

**Stokes**
* Yeah. Just to boost what Chris had in the chat, this conversation has been had in other places and yeah, this is like a known sort of, con to this plan, but the general, I think like solution here is just say yeah, like validators, like how often would you have a validator sort of have a transaction that would decrease their balance when they're also proposing a block? And I think it's pretty rare. 

**Lightclient**
* This is only a problem if we're trying to figure out the balance or the amount receives if you're building locally. 

**Stokes**
* Well, in any case, I mean, I can gossip the transaction that like sends 20, But if, Yeah, but if I'm, if I'm building, Sorry, go ahead. 

**Marius**
* I think that the, it's actually really important use case, if I'm being censored, and I have a validator I can build locally and get my transaction in. 

**Stokes**
* So how would you know that? Cause then you could just say, ignore MEV Boost entirely and just use the local pathways and like force it through. Yes. 

**Tim** 
* Is there a case maybe with like staking pools or whatnot, like mining pools would, prioritize their transactions and payouts and whatnot at the top of the block. So could you imagine something like, there's a large validator who like when they propose a block they like to include their transaction first or whatever. And so well, it's a balanced if it comes Oh right. It's a balanced if if it comes from that same account.
* But they could if, I guess if this was a, Yeah, they could just use another account or something and sidestep that. 

**Mikhail** 
* Actually if we rethink on the balance, so the balance for me is like you have the, this balance before the blocker has been executed and first address and you just has another one after the block has been executed and you, you do the, just the subtraction and calculate and delete. the other way is to pay with all the, fees, right, that has been charged to the peer recipient address. And I think that, if we will not account, for, if we use the former approach, we'll not account for coin based payments and direct transfers to the peer recipient address, which is probably fine because this type of payments are usually used by searchers, right. And probably builders to pay, to the, to the peer recipient, not, not something that you can grab from your local number, which means that probably the sum of, fees received  is a better approach. 

**Lightclient**
* Yeah, I'm, I'm not sure what this debate for the balance of diff that the local EL layer is about. Like it's already trusted, so we don't need to have any kind of proof against things. Like for me, the reason to do the diff is that you can prove it against the state easily. 

**Micah**
* And so you can compare against the MEV boost block. So you can decide, whether you should include your locally built block or the MEV boost one, one can imagine UHV boost, But you can do this with sum of fees. what do you mean? 

**Lightclient**
* I'm saying you can calculate the total sum of like the tips of the transactions regardless of how many transactions you sent from your account and then that's the value of the block to you. So Let me catch that. 

**Micah**
* Go ahead, whoever. Also stop. 

**Stokes**
* I was just asking, does some of fees include Coinbase based payments? 

**Micah**
* Presumably? No, there wouldn't be Coinbase payments in your own block that you bill locally most likely. 

**Stokes**
* Why not? 

**Micah**
* Because your local EL isn't doing, me extraction and so there's, I mean someone could send you a Coinbase payment, but no one does. It's one of those things like why would someone just be giving the block builder free money Because you're extracting long tail me. 

**Lightclient**
* And so this is like That you're running a different builder, like I'm talking about like the stock client mechanism and there's nothing precluding clients from adding support for tracing all the transactions of block and adding this to the total sum. If they see a Coinbase payment, there's just no reason to like subtract from that value. Like something sent from the Coinbase. 

**Micah**
* Yes, I see your argument. it's not unreasonable and it gives a, a high estimate. So if we say, if we're suing stock EL that doesn't do any sort of extraction, just does, you know, fair ordering for some value affair, then the fees that it gets from transactions is basically all it's gonna get in the standard case. And that will, I think, generally be an optimistic estimate and potentially higher than any boost, especially if MEV boost is doing, block before and after diff and so, that gives a little bit of nudge towards using the EL build block, which is nice. 

**Lightclient**
* I just don't, I don't get why you are comparing these as if they're like different mechanisms. They're both outputting like the value of a block to the validator. 

**Micah**
* Oh. So again, the goal here is to compare, like I built a, my EL built a block MEV Boost is giving me a bid. That means something. If those two things are counting different numbers, like if, if MEV Boost is saying the balance after versus the balance before and in that block there was a transfer, away from my account, then MEV Boost will score the block low. So it's gonna say, Hey, you made one Eth. Whereas my local EL is gonna say, Oh, you made 1.2 Eth because I didn't subtract that out, I only the fees.
* And so the local EL will have a slight advantage there and therefore you will choose local EL block instead of the MEV boost block, even though the MEV boost block may have actually given you More money. 

**Lightclient**
* I mean sure. But I think if we were to use a state diff then we have to have an in variance for people using a boost that they can't be sending transactions from their fee recipient during that block. 

**Micah**
* Yeah, and I think your ways is reasonable for the ESL side since we don't need to prove anything. 

**Tim**
* So like beyond discussing just these approaches, like what's the best way to like prototype it and get this actually tested? Where, where should like the conversation happen and and how do we get like a prototype of it? 

**Marius**
* So we Prism already has a prototype I think. 

**Tim**
* Okay. So Geth PR prototype doing what actually 

**Marius**
* I'm computing the fees, the just the normal canvas fees and returning them to Prism and Prism is, 

**Terence**
* Yeah, I am getting the fee from Marius's branch and comparing it and just pick the highest one to go. Sorry. And if the local one's higher, we just keep MEV Boost. 

**Tim**
* Got it. 

**Lightclient**
* I think we need to like push the conversation forward on the engine api PR. 

**Tim**
* Yeah. Okay. And, but, and to be clear, there's no PR yet. Right now all there is is an issue like this RFC, 

**Lightclient**
* Oh no, sorry, me, there's ad engine. Yeah. oh no, this Is all boxes. Versioning get payload to support locally built block value. 

**Tim**
* Okay. I can't find it right now, but I can post a link.  Okay. So yeah, let's move the conversation there. okay, awesome. Thank you. And yeah, I don't know. 

**Lightclient**
* Yeah, I mean what kind of timeline are people interested in for making something like this happen. 

**Marius**
* As soon as possible? 

**Tim**
* Double asap, Triple aap. 

**Lightclient**
* Okay. I mean, yeah. So it would be great by next meeting to merge the PR. Yep. So if people could review it, yeah. And the next meeting we can talk about cutting a new release for the engine API and figuring out how to roll it out. 

**Tim**
* Cool. 

**Micah**
* We still don't have versioning solved for engine API yet, right? 

**Lightclient**
* No, we do. 

**Mikhail**
* We have solved it. Just need to stack it out and Yeah,  we can have a PR so it will be, if, the new methods and the structures following currently is specified versioning that we currently have a small, piece of version in STACK and the engine api. So they will be forward compatible with the whole design. It's very simple. I mean they design like introducing new methods and how this will be handled by clients. 
* And yeah, with respect to this peer recipient pay payments, we agreed on submitting a PR and taking the conversation of what the value, what the computation of this value will be to some other place, Right. Or we agreed on that. It will be some of your recipient, payments in the block, like not payments, just transaction tips. 

**Stokes**
* I think we just set it on tips. I wanna make sure that this is not gameable, but yeah, that's the simplest thing it sounds like for now. 

**Seananderson**
* Wait, so I thought it was more that in the execution api, like you're getting a value with your execution payload or whatever. And since this is coming from a trusted node, we don't really care about like how it's derived. It's like you can, someone implementing the execution API can do it however they want, but it's trusted, so it doesn't matter. We don't have to prove it. 

**Stokes**
* Definitely There's still value in all green to do the same thing. 

**Micah**
* I think the important part of the, I think the most important part of the agreement is that the CL the cls all assert that we will compare the thing, the number the EL sends us against the number we get from MEV Boost. And then if someone wants to run an EL that, you know, fudges their numbers up or down or whatever that's that's on them, like they can, or someone wants to build an EL that fudges numbers up or down, that's fine. I think as long as we have standardization on what comparison is being made. 

**Lukasz**
* So, are the, CLs wanting to also do some kind of wiggle room because it's prob probable that, MEV block will be better. But if for example, it's like 5% better or 10% better or whatever, maybe the user could set it still would go to the local one, for example. So if someone is okay with losing like 5% of the, of the,Of the rewards, to, just supply, censorship resistant, for example. But if he gets like 200%, tip in this block, maybe he still wants to take MEV. Right. 

**Stokes**
* Yeah, I think that makes a lot of sense. I also think that's like a different conversation, different pr, so this is like the foundation, and then from there we can say, Okay, separately, someone is gonna have to make that comparison. And then you can also, like you're saying, add in that, you know, the wiggle room. 

**Gajinder**
* Also, there is a corresponding PR on the builder specs. I mean if anyone wants to chime in there as well, 

**Tim**
* Can someone post the PR to the builder specs in the, in the chat? okay. Second. Okay. Just we have a couple more things to cover. Anything else on this? Okay. thanks everyone. And yeah, we can follow up on the next call and, and see where implementations are at. okay. 

## Rebase EIP-4844 on Capella consensus-specs#3052 [59.35](https://youtu.be/GWkhFCvwOT4?t=3575)

**Tim**
* The next big, PR is this rebate, 4844 on, Capella. basically, there's, there's work happening on, on 4844 and I think we have pretty strong consensus that like withdrawals are the first thing that's gonna be prioritized on the CL side. We'd like to get, 4844 implementations done so that we can potentially ship them, if not the getter very close to one another. and the, the sort of way we've discussed doing it is having 4844, rebate on top of Capella so that, you know, you could imagine activating them one epoch apart or something, on the consensus there. and yeah,
* I know there was a lot of discussion on this PR and how we want, to approach it, but, yeah, and, and Shawe had some updates on, basically making, a lot of the withdrawal stuff, no ops, I don't know if this still applies given the change in withdrawal spec. so yeah, curious, what people think we should, be doing with this one. 

**Terence**
* I was pretty happy that we were able to come into some sort of decision on not having the queue in the vision state. So I think like it's fairly easy to move forward now, so now we know there's not going to be a queue in the beacon state, but within the block you still have those like, Bos to, to, Eth one, signature changes the, address changes. And those can be stuff out with like MEV or Zeros. So yeah, I don't see anything that's blocking this PR right now, so yeah, I'm happy to approve it or anyone else wanna approve it as well. 

**Seananderson**
* So from Lighthouse, like we were pushing for this, but since other teams didn't really like the building on top of the unstable changes in withdrawals, we're working like on our side to make withdrawals completely disable. So, our positions now just like whatever can support other teams more easily. And I guess generally it sounded like actually merging this into the consensus spec repo might not be great in terms of like, just the general structural repo and like testing infrastructure, so it's not a point. 

**Potuz**
* Yeah. Also the Beacon State structure is gonna change, so I, I'd suggest to hold on on that PR a couple of days, at least until we get our, the PR with the actual Beacon, new Beacon State and all the structures that you will need on the consensus side. 

**Tim**
* Okay. And then in terms of implementing and continuing to work on 4844, people can just step out the withdrawals, as they were previously doing it, or what would be the Yeah, what would be the best path there? 

**Terence**
* I don't have a strong preference on this. I mean, I think for us, we can follow other clients if other clients have strong opinion on this. 

**Seananderson**
* Yeah, I think for us also, like whatever would better support clients that might be further behind in development. 

**Tim**
* So, any other client team have opinion here? 

**Potuz**
* So perhaps I, I missed the, the question, but I think, so if I understand correctly, there are two things to test is one is for 4844, and the other one is withdrawals. And it seems that withdrawals, the execution layer is already ready to test, as in at least that's what I'm getting from Marius. so  my guess is that we can try to, give them clients now with the actual structures for withdrawals so that we can start testing right now the execution side Yes. As soon as possible within a Week, so yes, Yes. In just a couple of days. 

**Tim**
* Yes. So that's, yeah, that's definitely something. And I think that the, the other challenge on the 4844 side is I believe the Prism implementation was built with like 4844 after the merge. So like after Bellatrix rather than Capella and, others are starting to implement it and would rather have 4444 after Capella. And so making them interrupt together is a challenge just because of that. 

**Potuz**
* My suggestion there is that we actually ship today or tomorrow or as soon as possible, the actual structures on our clients, just the structures because they then they can be stopped out. I'm gonna have this in prison today. 

**terence**
* Yeah. So basically we can do, basically we can do with Capella or without Capella. I mean, yeah, basically we have two options and I think we can go with that, whatever other teams prefer. 

**Tim**
* Yeah, I think if it helps us with the testing for withdrawals to just get the, like, get all the structures implemented in clients and move that forward and then we can step them out when we're doing the 4844 stuff, that seems like the best approach. does anyone disagree with that? Yeah. And obviously, we need to get, at a high level all the, for all the withdrawal stuff done before, so let's, yeah, let's have teams focus on that and then, the 4844 people can yeah, just work with those trucks and, and stuff them help. Cool. Anything else on this PR.

## Historical batches consensus-specs#2649 [1:06:05](https://youtu.be/GWkhFCvwOT4?t=3965)
**Tim**
* Okay. I believe, you had one proposed, the historical batches PR. do you wanna give a quick, overview of that? Here's a link. 

**Arnetheduck**
* Yeah, sure. so this is really just a small cleanup of one of the fields in the state. right now for those that I haven't seen that PR it's basically that in the state we have this historical roots field. it's basically a miracle route of all the blocks and all the state route of all the history that led up to that particular state. What the PR does is that it splits it up into two, lists, historical route, or rather that you can get, route for the block route separately from that of the state. And what that enables is that whenever you have 8,000 blocks, like the data of them, you can verify that these 8,000 blocks belong to that state without having to recompute the state route. which is nice for archival purposes. Like you just grab a checkpoint state and you can immediately verify all block data against roots that are present in that state. 
* The PR itself, it's gone through a couple of iterations. it's kind of simple right now, I think is like 10 lines or something. in the beginning we thought we'd like kind of backfill some of the information, but we've come to the conclusion that the information that is to be backfilled, it can be shipped as a content, because it can be verified against other state data. And the other simplification that PR has gone through is that the new field that it adds, now ends up at the end of the state so that we don't change the header of the beacon state so that if you're reading like the first 10 fields of the Beacon state across different forks, that'll continue to work. the PR itself, we kind of, it came, the idea came kind of late in the BIS cycle, so we decided to postpone it. I think, now would be a good time to just throw it in. Curious what questions. 

**Tim**
* Yeah. Do you have any other time? Do you have comments or thoughts about this? Okay. I guess people can comment on the PR directly if there's anything. yeah, and once there's a bit more feedback we can probably make a decision on it. thanks. I guess next up, there's been a lot of discussion recently around Goerli's supply issue, so it's really hard to get Goerli Ether, and people are literally paying for it, which is not great. there was a community called earlier this week, Afri ran, to go over these. So Afri, do you wanna maybe take a minute to talk about the different kind of things that came up there and what are the proposals that like we can maybe do on the CL side to help with this? 

**Afri**
* Yeah, sure. Thank you. I mean, test nets, Goerli specifically has been an issue for a while now, specifically with a total supply, just not satisfying the needs both for stakers that want to test stake setups, but also application developers. And with the amount of, test net we deprecated to year earlier prior to merge, there are a lot of, applications and layer twos migrating too Goerli, which does not make it easier. was a supply issue currently. So we had a community call two days ago, and we discussed, various things and there's always two sites, was discuss discussions. The one side is, client teams that really don't want to put so much effort in, testing infrastructure or testnet specifically. And on the other hand, there are application teams that, ideally just want to have one functioning testnet for literally forever. And, our challenge now is to find a middle ground here and one thing because the easiest way for us would be to just duplicate, Goerli and start something new. But the issue is that so many teams are currently migrating to Goerli and we kind of miss the shots to communicate is properly what the state of Goerli is and what the future for testnet that looks like.
*  Some one middle ground would be to find an intermediate situ, solution to inflate the supply. 
* And there was this discussion if the, the sprawls with Capella offer us opportunity to maybe have something in the consensus layer specifications that would allow us to tweak some kind of factor, that would allow us to inflate a early supply. and I submit a pull request  specification is consensus layer specification, that proposes ara boost factor that would be basically a multiplier for the  amount. that was always one on all testaments, but it could be tweaked for testing or testnet purpose. And, the discussion is now how trivial would the lead to implement this? I mean, it would be trivial, but what are the implications? What are the downsides? is inflating the supply generally good idea if, if anyone can do it. And yeah, if anyone has any comment on that, I would appreciate it. 

**Tim**
* And maybe one extra piece of context of like why this is CL thing is, on the EL side, there's not really the ability to change network parameters after this the, the genesis is set. whereas the CLs use a bunch of constants that, yeah, the CLs use a bunch of constants that, can be like extended. And so this is just a easy, it seems like a low impact, from a code perspective way to add a constant that's set to one for main net and then just something else for other networks so that when people withdraw, that's a way to increase the Goerli supply. and the biggest risk is obviously that you can then have like a sort of infinite loop of growing the supply. So, you know, you can launch a validator, withdraw, multiply your Goerli Eth and then, do that over and over and over. so there's a point at which you would exceed like, what clients can handle. And I believe load Star has a relatively low value, which is something like 70 million times, the, the current supply. So like it's, there's still some room to grow, but yeah, people can just withdraw, increase their Eth, over and over. So that's the risk.
*  Yeah, that said, if we could get this changed then it would help with all the supply issues on Goerli, which is great. And if we can set the constant to something that's relatively low that we don't expect to be hit too quickly, I think it's, it's probably quite valuable. And also I think Perry, someone who mentioned this, we've had proof of work testnet in the past, Proof of work testnets have a lot of like phlo flaws in their design and people have generally not broken them. so there's a hope that like users will be somewhat altruistic here and won't destroy Goerli with this attack. and I believe most of the Goerli validators are controlled by client teams, the EF anyways, so like, yeah, a large part of this stake would probably not be malicious. 

**Micah**
* Doesn't it only take one person to execute this tech? 

**Tim**
* Yeah, so some, yeah, so somebody can like slowly, you know, start from 32 Eth ouble it, and then eventually become the core a divided error set, which could give us a also Having mostly altruistic validators, that doesn't really help us at all. Well, it helps can Just, it helps slow down the rate at which this attack would happen. Right. 

**Lightclient**
* I feel like before We even like debate the actual mechanism, we should determine if CL teams are even willing to accept a testnet specific parameter or fork change, right? 

**Tim**
* So the accepted test, not specific deposit contract, but yes. 

**Paul Hauner**
* So for Lighthouse, I'm not fully opposed to doing something weird to help roll out. One concern that I have is that we really pay in terms of client's performance for every validator index that's created. And if we create a scenario where one person or a few people are incentivized just to spawn validators, then exit them to make a lot of Goerli, which I think people will just do, then we're gonna blow out the size of the validator registry and we're gonna make it really hard to process the change. that'd be my concern with this approach. 

**Tim**
* Got it. 

**Arnetheduck**
* Well, growing it to the double of the current validators at wouldn't be bad actually because once we enable withdrawals, we need to be ready for that, right? 

**Paul Hauner**
* It would be an interesting test, but if we want to have Goerli, as a place where people can test things, it might like if they, if they wanna be able to have a stable operating environment, it might not be a good idea. I mean it'd certainly be interesting for us, but I'm not sure, but the intention of it. 

**Lightclient**
* Okay. So I guess then the next question is, is it the right decision to try and improve the distribution of Goerli youth? Because we do have this test at Selia that we kind of are wanting developers to move to and that should be like the preferred place and if we resolve the supply issue for Goerli, I think that Sepolia there's not as much point for it cuz the developers aren't gonna move. 

**Arnetheduck**
* I mean I think there are two core issues there actually. One is that, well there is a dual use use, case of Goerli. One is to test out your validators, and that requires 32 Eth, which is a whole lot, right? And then there's applications that just want to, you know, I dunno, uniswap, whatever. And they don't require as much e or somebody wanting to test their uniswap transactions or whatever. could something be done to keep the two apart? 

**Lightclient**
* Yeah, I think that there is work on creating a like stake testing specific test net because it doesn't make as much sense to have those things two things together.  so that the staker aspect is being resolved. So I think we're like really thinking about these people who are like trying to test on a testnet. So like run integration tests across many applications. And so the question is like, do we want to resolve this for Goerli? Like what is the future of Goerli? And to me, I was thinking like the right thing was to kind of let Goerli die over a longer period of time and then push the developers to Sepolia. 

**Potuz**
* There's also a way of, keeping Goerli working for Stakers, and having the full testing environment if you just have a contract that is founded, and I think each taker is already deploying these things where you just send very little Goerli and then the contract deposits for you. so you send a deposit that it's exactly the same experience, it's just that you send a less amount and then the contract access a proxy and deposits for you. So it keeps Goerli working for people that want to stay. And I agree with Lightcliens that if if we fix Goerli then we're not going to see developers moving to Sepolia. 

**Afri**
* I want to make two comments before we move on with this discussion there. This boost factor is just one of, different, a couple of, measurements we want to take. the, there is also, Mario working on the status test net. So we are trying to, have a different solution for people for specifically want to test, staking setups. So this is like an entirely different discussion and we don't need necessarily right now. And also I have been working on, something I call a test net release schedule that is kind of predictable. So when, which testnet should be the primary testnet is also a different discussion For now.
*  I would like to focus like on feedback on  how to fix Goerli or if we should fix Goerli at all or move on to another test that would be really appreciated if we can, can discuss if something like is like factor on, on on the clients would be feasible

**Lightclient**
* So is does anyone feel super strongly to keeping Goerli alive for the longer term for developers or is everybody on board with trying to make Sepolia the default place for application developers? 

**Tim**
* So it depends what you mean by like long term, right? Like I think it's unrealistic to think about shutting Goerli down in say the next six months. Like I think we've shut Robston and Rinka be down and some people are already are like in the middle of like migrating the Goerli. I don't think there's as much infrastructure support for Sepolia yet as there is for Goerli. So like, you know, sure we can push people off of it. I think that is still like a, you know, call it six or so months, probably more like six to 12, process. And it's like what do we do in the meantime? and it might not be, it might be fine to just say like, look, even if it takes a year and it becomes weird for a year, that's okay and we move people to Sepolia, and we can invest our time and efforts in building something like a staker specific testnet which shuts down gradually or, frequently. 
* But yeah, I don't think we can like say we're gonna just turn off Goerli in three months or something. 

**Pari**
* There was another, idea that kind of came up in chat now. we could in the next fork of Goerli, change the effective balance and the ejection balance as well so that when partial withdrawals and withdrawals are enabled, we kind of free up locked Goerli eth in the deposit contract. It wouldn't solve the problem, but it would at least free up existing locked Goerli eth and a lot of the freed up amount would still be under the control of client team slash ef. So we can solve the allocation problem in a separate manner, probably with hopefully better process or whatever the solution there is. 

**Olegjakushkin**
* Sorry guys, but what if we'll have this schedule of network disabling, What would happen to users that want to check what can happen to their staff? I kind of tease and stuff like that after, for example, the period that archive nodes keep their data. So how can users be able to test long term effects of their contracts and their stuff if we will have like schedule of killing networks every say half of a year, a year? What's an example of a long term thing you think that like How data can survive after it is migrated from like, I had something made recently then I waited for a period of time that is longer than our like period of fresh node. 
* The period when data is like captain archive node, how can I check that that data is still alive, still accessible from the node that are currently in the network? So such kinds of tests, 

**Tim**
* Is that something the network should guarantee? 

**Marius**
* It's something that you want to test and I think it's it's actually valid. There should be some longer running test case, test that,

**Pari**
* Well the longer running testnet could still be supported, Right? 

**Marius**
* Yes, exactly. The way I see it, this this like ephemeral kind of ephemeral testnet is more for testing for giving stakers a way to test. And Why just, just the flow. 

**Tim**
* Why do we think Sepolia won't end up in the same state as Goerli? You know, fast forward two years from now, we have the ability To min as much Eth as We need. Oh, because of the, because of the, the token gate Withdrawal contract. Okay. 

**Pari**
* Yeah, we kinda deployed a couple of tricks when, when deploying the beacon chain we have Genesis validators with a couple million e Genesis balances and we can withdraw them or partial withdraw them or whatever, and we have the token gate deposit contract with another couple trillion Eth

**Tim**
* Okay. And we can, we can mint e in that to, because we, we also had like, you know, the genesis whales for Goerli and clearly that's not sufficient long term, but like if we have the ability to mint additional Eth through the token contract, I think that's probably like the big differentiator. Yeah, Paul for your suggestion, we had proposed that the EL devs and they were against it. So if CL devs want to do that, that works, I guess it's worth Be the most straightforward. 
* So if it, but even if you do want to move to Sepolia, like in the, the, the medium term, is it worth specing out this effective balance change because that seems like something where we're not actually adding a new constant to this spec? you know, like with the withdrawal boost factor, we don't run into this potential like infinite loop of supply issue and like given that most of the Goerli e on the validator side is most of the trader validators were run by client teams and the Eth, if we have a lower effective balance and it allows all those teams to get a ton of, of Goerli Eth I think it it's reasonable to like have them distributed the faucets and whatnot and it might just buy us some time. 
* so is anyone strongly opposed to that or is it worth at least putting together respect for it and, and seeing what it, what it would look like? 

**Lightclient**
* I think I'm generally opposed of modifying Goerli 

**Tim**
* Just because we want move people to seia. Is that the main reason? 

**Lightclient**
* Yeah, I think if we modify currently then it makes it pretty unlikely that we'll ever move to Sepolia. 

**Tim**
* Okay. Anyone else strongly opposed to this or. So let's use that, to continue this. I literally had that channel muted for some reason. let's use that to continue this conversation. yeah. And okay, we're, we're already sort of at time. I know Chris you wanted to give a quick MEV boost update. Do you wanna take a minute or two to do that? And I know you shared a link in the chat as well. 

**Chris**
* Yeah, sure. just running through it, there is an upcoming release of me Boost one four O, which is a bunch of minor improvements, but the notable improvement is the ability to set a minimum bit value so any proposal can define whatever value they want as a minimum bid value. And below that, no bid will be sent to the CL client. That's, they're only notable. There is a bunch of minor improvements like clogging multiple reflex and you can see the details in the Github issue. 
* So I really did API updates as we discussed before, the profits switching in the beacon node and the block scoring standards and payment proofs that are somewhat related. Ongoing research about inclusion lists inside and or outside MEV boost, improving performance with SSC payloads. 
* There is conversations in both the builder specs and the Beacon APIs. Previously there was also the discussion about SSC subscription to trigger block production that's, stagnant at the moment. And a few stats about the relays. There are eight relays currently producing blocks. We've put a table in there with the number of payloads in the last 94 hours for each one. And I put together a table of multiple builders that submit blocks so the flash puts relay that are landing on chain. So you can get a bit of a feeling of what's going on in deep builder ecosystem at the moment. 
* Yeah, that was the very short version. Any questions? Right? 

**Tim**
* Okay. Yeah. Thanks Chris. Anything else, as we wrap up? 

**Stokes**
* Okay, Thank you. I'll just call one more thing just to call out the document. I put in the chat about withdrawals progress. it'd be very good if we could get to a testnet by the end of the year and I'm generally trying to keep track of everything. Let's see. I'm trying to find it, but here we go. Oh, I can't copy it. That's annoying. There we go. This one, what I just based it in the chat. Just everyone, take a look. 

**Tim**
* Cool. Thanks everyone. and yeah, next one of these Danny should be back,
* Thank You. Thank you. 



---

### Attendees

### Attendees
* Tim
* Arnetheduck
* Marek
* Lance
* Micah
* Paul Hauner
* Ben Edgington
* Loin Dapplion
* Terence
* Enrico Del Fante
* Pooja Ranjan
* Hsiao-Wei Wang
* Saulius Grigaitis 
* Roberto B
* Olegjakushkin
* Chris Hager
* Stokes
* Dankrad Feist
* Caspar Schwarz
* Seananderson
* Andrew
* Crypdough.eth
* Zahary
* Matt Nelson
* George Avsetsin
* James HE
* Marius
* Ansgar Dietrichs
* Lightclient
* Stefan Bratanov
* Afri 
* Ahmad Bitar
* Lightclient
* Nishant
* Gabi
* Pari
* Jimmy Chen
* Gajinder
* Ruben
* Mikhail
* Zahary
* Daniel Lehrner
* Andrew
* Daniel Lehrner
* Fredrik
* Kasey Kirkham
* Protolambda
* Cayman Nava
* Stefan Bratanov
* Ziad Ghali



