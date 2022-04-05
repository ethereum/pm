# All Core Devs Meeting 135 Notes
### Meeting Date/Time: Friday April 1, 14:00 UTC
### Meeting Duration: 1:42:20 hrs
### [GitHub Agenda](https://github.com/ethereum/pm/issues/500)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=1QU8r9-SJDc)
### Moderator: Tim Beiko
### Notes: Shubhangi Gokhale

## Decisions Made / Action items
| Decision Item | Description | 
| ------------- | ----------- | 
|135.1 | Coredevs will discuss issues related to storage of invalid blocks in the interops channel and maybe have something to discuss at next cl meeting.
|135.2 | Tim Beiko will research scheduling time between testnets and discuss it at next meeting.
|135.3 | Discuss Shanghai cfi at a higher level at the next ACD meeting.
|135.4 | Discuss issues related to increasing supply of Görli eth asyncronously and maybe discuss earlier at next ACD meeting.
|135.5 | Local devnet for testing may be available for coredevs by next ACD meeting. Related discussions will be continued in relevant discords.


## Merge Updates
### Kiln, Shadow fork updates

**Tim Beiko**
Okay, good morning everyone. Welcome to All Core Devs 135. I posted the agenda in the chat already. I think everything is working on the live stream. So a couple things today. A bunch of updates on the merge, so some updates, mostly on the shadow forking. I don't think there's much on kiln itself, and then Mikhail had some stuff about the latest flatted hash conversations we've been having, then on shanghai a couple things as well, so Alex had some updates on the withdrawal EIP, based on the call last time, and then there were two other EIPs, the S transient storage and the removal of self-destruct that were brought up in the comments, and then after all that, we have Afr here to talk about some of the issues we've seen on Görli, and some potential solutions to them. I guess to kick us off, Pari, do you want to maybe give like a high level recap of what happened with shadow forking, where we're at right now. I saw you kind of posted it in another discord this morning as well but just, yeah kind of bring everybody up to speed of course.

**Paritosh**
So since the last ACD, our testing efforts have been even focused on shadow forking. So what we mean by shadow forking is we take the config of a test net, in this case Görli, and then we just modify it to add a TTD and merge four blocks. So that means up until the TTD, we'd be following the canonical quality chain and post TTD, all the notes configured with the modified genesis json file would fork off into their shadow form, basically, but since we've set the merge fork block to be far in the future, we continue importing transactions, so the main idea is that we're able to test syncing, we're able to test actual load block production under load and so on. 

We had two attempts so far. The first attempt followed a mainnet distribution and we found issues in, I think every client, especially related to expectations of how quickly timeouts should happen, or how block production logic has to work, and so on. So we had a second shadow fork had happened day before yesterday, and that was a lot more stable. We didn't do mainnet distribution, for that one, we did a more equal client distribution. I think we've only found like one or two minor issues and they have patches being released. So we're attempting a third version again, with mainnet distribution. TTD is supposed to hit on Monday and information about the conflict has been shared on the testing channel in the RnD discord, and irrespective of how this one goes, we want to already try a mainnet shadow fork sometime next week, and the main idea is just to collect as much information as possible right now, so that we can make an informed decision about the merge sooner.

**Marius**
So one thing where we want to push for the mainnet shadow fork so quickly, is to collect data on how the clients behave on mainnet because we've seen on the Görli shadow fork that like syncing becomes an issue, like bigger blocks become an issue, stuff like this, so it would be really nice to see how clients work post merge on mainnet, so, one thing for example, was that we provisioned for the…yeah sorry I’m not at a great place…

So one thing we had for the first shadow fork is that we provisioned 8 gigabyte nodes and because of non-finalization these ran over, and geth ran out of memory and was killed, and then was killed repeatedly, and stuff like this is I think really important to see on mainnet state and on mainnet transactions.

**Paritosh**
Yep, and we don't really have an expectation on client teams to spin up their own nodes to test in. I’m spinning nodes on your behalf. More or less every client team knows whose ssh keys are on which machine, it would be great if you guys can have an eye on your nodes, test weird sync states, start syncing, switch ELs midway through sync weird things that people might do there.

**Mikhail**
Could people provide a bit of details behind those timeout issues? 

**Marius**
Yeah, so like there are multiple issues there. One was apparently no client has a pause between creating a new payload and retrieving the payload, so fork_choice_updated with payload attributes, and then get payload, so all and because geth right now builds blocks synchronously and fork_choice_updated, that's not an issue, but for nethermind which builds blocks asynchronously, every block is empty because they only have 100 milliseconds to build a block, and there was one issue, the other one was that clients didn't give us enough time to execute the blocks, so I think some clients did have a timeout of 500 milliseconds for new payload. A new payload can, like we can and we do execute blocks during new payload, and so yeah, we timed out and so some clients weren't able to sync…able to follow the chain.

**Mikhail**
What was it…http or websocket? Which communication protocol has been used?

**Marius**
I think http. I'm not sure, like right now only nimbus uses a websocket as far as I know, or maybe they also use http…

**Paritosh**
No, they're also using web sockets right now yeah and they're the only ones using websocket. Everyone else is http.

**Marius**
Yes and I’m not sure if we had the same issues for nimbus but for the other clients, it was.

**Mikhail**
Yeah. I would expect, like, if its http, I would expect like timeouts set to something some like to speak big number to one minute or whatever, even more than the seconds per slot rendering.

**Terence**
So I was gonna ask would there, should we provide some sort of recommendations for timeout duration, I guess just for a different method, there may be different recommendations, and I think it's fairly important that all client kind of uses the same timeout, so we don't see some sort of network asymmetry down the line.

**Danny**
Yeah, I mean timeouts are fundamentally dangerous, because if there's a timeout, I can construct a dos block that can sit right on the border of that timeout depending on the machine, then I can split the network. So you know on the order of something far beyond dos blocks, should be the timeout, if there has to be a timeout. But yeah, maybe there should be explicit recognition.

**Marek**
Do we discuss timeout for fork_choice_updated or for new payload to… because for fork_choice_updated, we should have relatively small timeout I think.

**Danny**
Why…because both of them have execution semantics baked in, so both of them can have the same…

**Marek**
Right…sorry…yeah…all right.

**Marius**
And then in fork_choice_updated, you might have to run re-orgs so…

**Mikhail**
Yeah I was just going to say the same so it could be like a rework that is processed synchronously like for if it's like two or three blocks and fork_choice_updated like what Marius said so it should be more the timeout should be should be enough to process like a few blocks so I would even expect that websocket is used. I don't think that websocket is, has some timeouts, like inside of a session.

**Danny**
In your case though it might actually be better to have the execution layer signal that it is still working via maybe a call to syncing, a return to syncing, rather than hitting the timeout, because then the consensus layer has no idea what's going on.

**Mikhail**
: And I think that since the communication channel was like a trustworthy relationship between cl and dl, I would expect that the match should be relatively high, so it's not like el is just kind of fine, it could be really in case of like attacks where every block is huge and it takes let's say 20 seconds to execute, I don't know it's just a random number, it would be useful to have enough time to process such big blocks, so the chain will be able to make progress in any case, otherwise if each of this block will be timed out we could have a blindness failure.

**Terence**
I think like um so coming from consensus perspective, from prism, what I can say is that most of the issues, or most of the edge cases we're seeing now, is always regarding time out. I think this is a very tricky area to tackle, just before we're checking time out, like the payload is invalid, but that's not true because the payload is not invalided, but it just means that we have to try again later, so we discovered a few edge cases there, and it may be important to basically, like I said, define some timeout values across all the methods so make sure everyone's on the same page.

**Marius**
Yeah. I think we should defend us async and not to them now one thing one thing that I like maybe I didn't hammer this point home hard enough because Pari just wrote me about it, basically the time that all the consensus layer clients currently wait, between when they ask us to construct a payload and when they fetch the payload from us, is too short, and so if we were to switch payload construction to async, which is something that we want to do in geth, every block would be empty, and so…

**Danny**
So essentially they're supposed to be making this call something like four seconds or more before because they know that they're going to be a proposer, and instead they're making it like very in rapid succession…

**Marius**
Yes. So they send us the payload attributes, we start creating the payload, and then they already send us the geth payload, and this is like 100 milliseconds apart, and in these 100 milliseconds we cannot create any blocks, and I think this is going to be, it's an issue.

**Danny**
Yeah, I mean the intention here is certainly to have on the order of like a third of a slot, if not more of lead time, and that's just, that's consensus layer should be doing that if they're trying to have anything profitable coming out of it…

**Marius**
Yes.

**Danny**
So if we can make a clearer recommendation…I mean it should be as soon as you have…as soon as you know the four choices of the prior slot, and you know you're the composer of the next slot.

**Marius**
I think I noticed it some time ago, and I reported it, and I think only tackle doing it in correct way.

**Danny**
Sorry, that was in the correct way or incorrect way?

**Marius**
Tackle is correct, sorry.

**Danny**
Got it. 

**Terence**
Chris had that fixed…we actually just began caching the payload id the slot higher when the hedge changes…I can give you a new image to try. Yeah.

**Micah**
Danny you said a third of a slot is the minimum. Why is that? Shouldn't you always know about one slot or more in advance?

**Danny**
Yeah, you should. I mean you get progressively more information during a slot about attestations so…

**Micah**
You gain confidence but you should know like, if your slot is coming up, like as soon as the previous slot shows up, I feel like you should be able to start building the block, like you don't, maybe that you're building on the wrong thing but you should be able to build something.

**Danny**
Agreed. So as soon as you see that block you should begin the process you might, during that slot, abort, and provide a different head with a different one. So say for example at slot in there's the proposer slot in actually makes two conflicting blocks and they're going to get slashed, but there's actually two conflicting blocks out there and maybe what I see is the head initially and I begin my build process on actually switches because of the weight of attestations throughout that slot you know so then there are these edge cases where you might switch but you're right as soon as you get the information, even if it's low confidence you should probably begin the build process, and only if you fork_choice_update, you could change the build process, if you, in these edge cases. 

**Micah**
Are any of those edge cases non-slashable? If it was a late block…

**Danny**
Yes. If f it was a deep enough fork well yeah a late block potentially or a deep enough fork where the shuffling is diverged, then I might all of a sudden resolve that I want to switch forks halfway through.

**Mikhail**
I have also another comment related to timeouts or a question. Is this possible to process multiple payloads at the time, on the old side, just curious how it's currently implemented in the clients. Yeah, like for example one payload takes quite a lot of time to be executed and then another new payload is coming. Will the first one be processed in parallel with the second one?

**Marius**
Yes, so that's no it like, it won't, because we have…

**Martin**
Sorry, were they both based on the same state?

**Mikhail**
Yeah, probably both on the same state like they're just sister blocks.

**Martin**
Theoretically we could do them in parallel. I don't know if we do. Marius probably knows that better.

**Marius**
No, because we have locks on the blockchain data structure, so we cannot, like it depends on what you mean with like execute them so we cannot like execute the transactions we can for example verify, like verify the block header and stuff like this and this is all done in parallel, but we cannot insert them into the blockchain in parallel

**Tukasz**
Similar, in nethermind, we run validations etc in parallel, that's fine but actual execution, not, because we have a concept of canonical state which is being modified.

**Mikhail**
And this is how it works today on the mainnet, right?

**Tukasz**
Yes.

**Mikhail**
Okay, thanks. I suggest we continue this conversation in discord. 

## LatestValidHash EL implementations ([context](https://discord.com/channels/595666850260713488/892088344438255616/957969488307953666), [summary](https://hackmd.io/GDc0maGsQeKfP8o2C7L52w)

**Tim**
Yeah, I think that makes sense. We can use the interop channel to do that, yeah, anything else on timeout? Okay, next up, Mikhail you had…basically there was a conversation on discord this week around the latest valid hash I shared the discord link in the agenda and you put together kind of a summary explaining your thoughts about it you want to maybe just take a minute or two and share your thoughts and you can share your screen also if you want with the document.

**Mikhail**
Let me share my screen, okay do you see it?

**Tim**
Yes

**Mikhail**
Okay, cool. So yeah, we've been a bit touched this latest valid hash and apparently it has some complexity and supporting it so I’ve just put down some notes on that, some initial thoughts on how this could be implemented and when it's important, so tldr is here, we have two cases that should be considered during implementing this requirement: first one is important and to my opinion it's when the payload realization happens synchronously, so it's like when you submit the new payload and it's responded, it appears to be invalid. This is the easy case right so here latest valid hash is also the print hash and it might seem that this latest valid hash parameter is redundant in this case but if we take a look at fork_choice_updated, which has the same parameters in response, we can conclude that this would be important in the case if there is the optimization of short-range rewards done by some clients, for example, Aragon, that has been discussed previously on discord that this optimization like when you really fork and the new fork is like only two or three blocks it could be the case when like the first block is invalid in this fork and what you do is respond with invalid and in this case latest valid hash will point to the first block in this fork and this is important because we need, cl need to invalidate all the blocks that are starting from this first invalid block so that that's this is where it should be like implemented it should be straightforward because el client has all the information and it just sends it back to cl, so the other part is when el is syncing and it makes an invalid box somewhere in the middle of the chain that it has been syncing with and the el is syncing with this chain, because consistently a client said that this chain is canonical and fed all the required information to el to start syncing, so in this case implementation would be a bit trickier. There need to be a cache that will store the tip of the chain that the l nodes that the l observes the tip of invalid chain and this type of invalid change should be accompanied with the latest valid hash printer. So that's the kind of cache required here and this check is pretty simple, so every new payload if its parent hits this invalid tip hash, so it equals to invalid tip hash so in this case having this information el client just may respond correctly to this request.yeah we should not account for I think that we should not account for the case when the some payload is missed and el can't just build the chain like to understand that this payload p1 for example is linked to the invalid chain because for some reason cl didn't send the all required information to build this link and that's it so I think that this these two steps would be enough for implementing it in the asynchronous without validation casso yeah these are, this is the option. It's not that complicated but it's anyway complexity and the other question that is important, what would happen if we do not support latest valid hash or we know we do not support like sending this information to cl while el is syncing, so what may happen is just cl will not know that this chain that it follows, is invalid and will still keep following it, and pull from the network if it's available in any place of the network, probably in this case, a node is under eclipse attack and is being fed with invalid chain a nd el will just like assume that the l just see the invalid block and drops the entire chain and cl doesn't know about it anything and keeps sending new blocks from this invalid chain they all started syncing again and this going over and over, so in this case what will happen is just either cl will observe the valid chain and rework to it just because all other validators will have a switch to the valid chain and it can be seen from the attestation justifications and final finalization updates either this happens or a user will see that node is not progressing and we'll have to do a manual intervention. Okay, so two outcomes from this, lattice valid hash is really valuable thing for this first case and this must be implemented. This one is like optional I would say to my observation so but people may have other opinions on that.

**Marius**
I don't like should we only cache one invalid tip hash or should we cash all of the invalid tip hash?

**Mikhail**
 I would say that you should have probably invalid cache like for a few entries so and just catch them and drop the most latest one that were was added to this cache it's like yeah this case is only actually at one point in time there will be only one invalid chain that matters because el only syncs with the canonical chain and if canonical chain is invalid then it matters, otherwise, yeah so there is only one chain el is synced with. 

This is the assumption and this was also discussed previously so basically yeah probably there could be two chain a reward happens that might make sense to store in this cache two three five but probably not more.should like be on every chain that new payload is sent for, because yeah because in this while syncing what only matters is the canonical chain while this is synchronous payload validation, there is the response, is immediate and all the information is available to make a response according to the spec.

**Martin**
So two things, so I mean you know I wouldn't say that this will most likely happen during an ecliptic attack uh most likely the el has some data corruption in the database or in bad parameter or something. But I don't really get this first bullet point. So we're fed a new payload we should return the parent hash? How do we know that the parent has the most recent valid, what if we don't have a parent…

**Mikhail**
because if it's yeah right if it's synchronous yeah you're right yeah fair question because uh if you don't have a parent you would respond with syncing right so it's it falls to the second case not to the first one synchronous like validation happens only when you have all the information available and the current block is known and obviously it's valid in this case like the assumption is that this block is valid.

**Martin**
okay so it won't cannot have so if we're that new payload block 1000 and we say no this is invalid, and then you say okay here's the new block 1001. Should we just, okay, I’ll just have to go sync then.

**Mikhail**
Yes you will have to sync, if cl consists on sending a child of invalid payload so it must be something bad with cl because it got rid of a response that the parent is involved.

**Martin**
So Marius we will never restart the sync after we're synced right we haven't changed that.

**Danny**
I think he means more like reverse header sync like if you got a block and you want to find, not like genesis.

**Marius**
sync if we don't have a parent to some block then we will start syncing...

**Danny**
As in trying to fill in the gaps of the parents to find its roots in the chain you know about.

**Marius**
Yes.

**Danny**
Yes all right so Martin, in your example, if the consensus layer sends the next block in it forgot that you already said something was invalid so this does you know this could happen theoretically like if the consensus has a failure or the consensus layer turned off and then turned back on or something like that but we do need to handle the case where it does try to insert something that is…

**Marek**
only switch consensus databases.

**Danny**
Right.

**Marius**
or just a simple race condition.

**Andrew**
not only invalid uh so if the el returns syncing but then while syncing it discovers an invalid block but because the engine API is, it has already replied syncing on the engine api the consensus layer doesn't know yet that the block is invalid, it only got syncing for that block, then it starts building on that new chain, and sends new and new blocks to the el so, for every, for Aragon it's currently a problem that Mikhail has described we don't have this cache we have to implement it because you see the problem we reply to syncing and only after that we discovered that some blocks were invalid.

**Martin**
Yeah I think we did something similar, like we put them to some future queue and at some point we're going to execute that future queue and might notice that one of them was that...

**Mikhail**
So I’ve heard that nethermind's stores like a few the most recent invalid block hashes but this neither the invalid tip cash nor the latest valid hash it's like she's the invalid child of the latest valid block.

**Tukasz**
So yes for nethermind so we were thinking about it, and our potential fix for that is to keep invalid blocks in our block tree and just mark them as invalid to have like the whole thing and just when something is finalized, we can prune the invalids ones from the tree to like not keep garbage there.

**Mikhail**
Yeah and so you can just query the database right, so when you insert the new payload into the block tree, you may check this right, that the parent is valid.

**Tukasz**
Oh and yeah we could go to like the whole ancestors right, train right.

**Mikhail**
but uh yeah this sounds like an attack vector I mean if someone if this chain is pretty long and you should always hit, you should make like multiple database reads to just traverse this chain to find out the latest valid hash.

**Tukasz**
Yes that's a potential problem.

**Mikhail**
So, yeah.

**Marek**
so yes yeah but cache is not enough because if we restart our node it will be in let's state again so we can't just store it in memory cache I think…

**Danny**
You could recompute the cache essentially in that if you get some block deep into an invalid chain you recursively walk back and then you'll see oh this is invalid and then you can have the cache again.

**Mikhail**
Yeah

**Danny**
but storing it is fine too but it would be recomputed if the consensus player was continuing to pound information in that branch.

**Mikhail**
Yeah once again I do not think that it's super important it would be really nice to have this supported during syncing.Danny what do you think on it?

**Danny**
I think it's very difficult to construct realities where these full any number of um are like induced load on any number of large amounts of clients, so you know I want to kind of minimize complexity but also not leave this as a glaring hole, I don't know, that's not much of an answer, yeah, I need to think about it.

**Mikhail**
Yeah, we may just probably think more about it and discuss.

**Danny**
Yeah I mean the problem when you say anytime you make a claim that this can only become a problem when a node is syncing then the attack vector becomes, can I induce a lot of nodes to sync, and thus make this a problem, um you know the answer to that hopefully should be no, but like you know a bug if I can find a bug that can induce lots of nodes to sync, then I can maybe exploit you know an edge case in this that we didn't want to deal with…

**Micah**
Yeah the worst failures are always compounding failures where you have, you know one thing goes wrong and then something else powers on top, like those are the ones you gotta pray build again.

**Danny**
Marius, I mean they essentially they have these branches that because of the way fork_choice_updated can return an insert payload can return syncing syncing syncing they have these branches that once the execution layer does finish syncing you know they need to resolve these as invalid or not and if not they just have these branches that they just don't they can never really know if or valid or not if this cannot be resolved I mean the edge case is really I have I inserted a branch it has n blocks now you tell me the nth block is invalid what about the n minus one blocks before I don't know um and then I don't know what to do with them is the that's the problem. So its kind of...

**Marius**
oh I get it no thanks yep.

**Mikhail**
so um need to think more about edge cases for the syncing part of it, but for the when the parent block and state are known, and it can be and this information can be easily derived I think it's must to be implemented. Yeah I like I don't think it's just a must, yeah that's bad. Martin your hand is still up...

**Danny**
Sorry okay always yeah I mean just quick on this at this point we should find a solution that works I think very much I would prefer to not change the structure of this response and just figure out the most correct way and complexity minimizing way to utilize the value that is there.

**Mikhail**
Yeah and moreover we need this structure to be preserved for this first part, so it's it should be it must be in place, it will not change. Yeah, this question for how to implement the second part, it’s still kind of open.

**Danny**
Yeah and I mean additionally I think we need to figure out a way to induce and test these edge cases on in some sort of environment because it's hard to actually run into these naturally on some of these edge cases naturally on chain.

**Mikhail**
and this cache I don't think it should be persisted actually so it should it would be enough if el has restarted and this cache has gone yeah then the situation will likely repeat sent the el will be able to respond correctly.

**Marek**
after restart yeah?

**Mikhail**
yeah right yeah yeah yeah right so it will

**Marek**
we can't remove uh invite blocks from block 3, i'm not sure how f is working right now but we are uh on mainnet we are removing inviting blocks from block 3.

**Mikhail**
I think you can remove blocks from block 3 if you do this on mainnet currently, only information needed is basically these two values so in cache so you don't need to store invalid blocks for this purpose to serve this latest valid hash correctly, I don't think so.

**Marek**
Okay, I will think about it more. 

**Tim**
And I guess yeah we can use the interop channel to discuss this as well and hopefully have something I guess by like the consensus layer call next week, which we're happy with, anything else on this? Okay, oh Andrew, sorry go ahead yeah.

**Andrew**
Yeah, so I would like to say that in Aragon we probably most definitely will need to implement something like this because it's a problem and I would like to have tests in hive or somewhere for this kind of scenarios and also on how things with the merge are in Aragon, I would say, currently our implementation is alpha quality and before switching um public testnets, I would like Aragon to reach uh beta quality and um we need to fix the tests in hive implement this at kh case and quite a few things to finish, and also start preparing a release so I would say it will take us roughly a month to reach like to move from alpha to beta and, yeah from Aragon's, from my point of view, I would like quite a bit of time before switching public testnets to profile stake.

**Mikhail**
Right that was going to be the next thing I bring up just want to make sure there's nothing left on the latest valid hash but then I can kind of share my thoughts about that and how we're tracking. Okay uh yeah, so basically I guess you know everyone's aware the difficulty bomb is set to happen, it's probably gonna start being felt around June and kind of slowly ramp up from there, the rush and others somebody else has like a dune analytics dashboards and Vitalik has a script which estimates it, and basically roughly around like the end of July is when you start getting blocks which would exceed like 17 seconds, which seems pretty long and it's hard to, all these are estimates it's really hard to estimate how quickly the bomb goes off, once it actually starts having a bigger impact on the overall hash rates. It's probably even harder to estimate now because if the merge is the next upgrade, people might start selling their miners and so take all these you know they took like a grand assault, but basically I think if we want to avoid pushing back the bomb what you what you'd want is ideally not reach like 17 second block times, and people can you know disagree on the number feels like14,15 might not be too terrible, and a few calls ago, Vitalik had this idea where if anyways we are gonna put out a release with sort of a fake fork block, in order to like disconnect nodes who haven't upgraded from the merge, so just changing the fork id and we could do kind of a mini bomb push back, but that only buys us a couple of weeks, because it means that like we need to make sure that you know by the time the pushback happens on mainnet the bomb is still manageable. So all this to say if we want to like aim for that sweet spot of like we upgrade and run through the merge kind of before we hit like 17 or more second block times, working backward if you want to have, you know reasonable time for like a main net announcement, and then reasonable time for test nets, um we probably need to make oh I guess we need to make a call about like the test net fork blocks about a month from now, so like two not necessarily the next awkward devs but the one after, um I think if we're in the spot like late April we're like we're not ready to say you know the fork is gonna happen on test nets, in like a couple weeks, um then I think we probably want to consider like a longer bomb delay, um and how long is something we can you know we can discuss, but that's I think that's roughly where we're at right now where if we if like in a month basically four weeks from today we're comfortable saying we're gonna fork the test nets in another like three to four weeks um I think we're in a good spot to only need probably like a sort of mini bomb delay, which we can include with the merge release, if in a four weeks basically we're not confident about moving to test nets, then I think it makes sense to just delay the bomb a bit more independently, and then and then you know for that's when we're when we're confident and the client releases, and obviously you know stuff like shadow 14 mainnet next week, will give us a lot of data about you know how many more issues do we find, and yeah, I guess just general client readiness for to implement all the stuff we just we just discussed. yeah so that's roughly my point of view I’m curious if anybody else have thoughts on that.

**Danny**
All sounds like a reasonable approach to the timeline.

**Tim**
Marek, your hand is up?

**Marek**
I think it is good time to observe that but one comment from my site is that I think that we should run the test net, the public testnet for a longer time, the time the first test that should be, I don't know one month or something, not like a week after uh let's run the first test and a week after the first test that we are we are running second test, and that is my opinion.

**Mikhail**
Is that to see what happens?

**Marek**
Exactly, exactly.so for example for a... and observe it for I don't know months or something and then for the next test, that is my opinion.

**Micah**
that's one month after the TTD or is that one month from like when we launch the new clients?

**?**
After the merge?

**Marek**
Yeah, after the merge, yeah. After TTD, I think that is my personal opinion.

**Tim**
I guess the counter argument I can see to that is we get like rapidly diminishing amounts of information, like if the fork actually works, that's like a lot of de-risking and then if you know it's still up for an hour after, that's great, and then if it's still up for like a week after, that's really good I yeah, I guess I maybe I’m wrong here I feel like that like from one week to one month we probably get less information than we do from like nothing to a week, but if that's wrong, yeah happy to understand why. Andrew?

**Andrew**
Well one valuable bit of information is after like a week after the merge, two weeks, couple weeks when you start to sync a new node from scratch what is the performance of this thing, that's something I would be curious to test.

**Tim**
Got it. Marius?

**Marius**
Yeah, like this is something we should already be testing right now on the shadow fork. I think we don't, like we shouldn't wait another month to start testing stuff, like syncing from scratch I tested that on geth yesterday already, and it kind of worked. It's painful of course because syncing a full test net from one of the big test nets probably from scratch is already painful but yeah so my opinion is that we should have two to three weeks for between the first between the first and the second test, maybe only a week after Sepolia, because I don't think that there's much activity on Sepolia, but for like a bigger testnet, we should have for the first bigger test that we should have like three weeks yeah three weeks I think is a good mark, and afterwards the other testnet should be in more rapid succession, maybe every week, maybe every two weeks, but in my opinion we shouldn't wait for every big test net for a month. That would just like delay things.

**Marek**
Yeah, just not to release all tests in one client's release that is, so not in one release, I set TTD for every test. That is my opinion.

**Marius**
Yeah, I like I don't think we can we can could even plan that that's that seems like something that would be very hard to plan because we have so varying GTDs on the testnets, tds on the testnets.

**Tim**
Will it maybe make sense so like we have basically Görli, Ropsten and Sepolia that are going through the merge. You mentioned you know Görli, Ropsten are probably the ones we want to see live or like we want to have like the longest data for, so like maybe there's something, where like you can start with Görli, and then two weeks after, you do Sepolia or  Görli, Ropsten whatever like whichever one of the big ones, and then you do Sepolia maybe like two weeks after, because you kind of expect that if you know you shouldn't like learn that many new things on Sepolia, assuming the previous one went well, and then two weeks after that, which is like four weeks from the original, you have the second big test net, and then if you do that then by the time we like choose mainnet blocks like once we've seen that second, you know test that be live for another couple weeks and we're confident that it's stable then you kind of choose the maintenance blocks and move there but maybe yeah maybe like using this testnet like the Sepolia test net which is like lower stakes in the middle, allows us to have like more time on under two other one which have more activity basically. Okay I guess yeah we can continue kind of the test net ordering conversation async as well but I guess people generally seem to agree we want like more than one week between each of the test net like we did for like London and probably more on the order of like two to four weeks and depending on the type of test that does that generally make sense?

**Marius**
Yes.

**Tim**
Okay cool and I’ll look at like what that would look like from a scheduled perspective and we can chat about it on the next call and yeah what yeah when we would need basically to make a call if we wanted to or I guess yeah when we would need to delay the bomb basically based on when we choose the test nets anything else on this?

**Tukasz**
I have a question especially to the geth guys but maybe also to other clients did you testing around pruning, how do you avoid, do you like track would finalize and allow pruning only the things that are finalized or how is it working for you?

**Marius**
like you mean pruning the chain away that is lower than finally?

**Tukasz**
For example, pruning the block tree or something like that.

**Martin**
No, we don't. Well we are the ancient, so currently at the point 30,000 block back in history, we only store the canonical chains and we move it over from our live database, and put it in a not a live database and when we do that we only store one of them for each type.

**Micah**
Do you have any plan on switching over to using finalize instead of 30,000 blocks or do you plan on sticking with 30000 blocks forever. 

**Martin**
I can't say really no no.

**Marius**
I think we committed ourselves to not doing that like again back in the summer because we think if something breaks and if we were to break the finalization then we should be able to, and we want to be ready for that, we hope that it's never going to happen, but if it's going to happen then we should at least support it.

**Danny**
Right, that's that length of time like if something goes wrong, we can fix it between this and that. 

**Micah**
And how long are 30,000 blocks? 

**Danny**
About two weeks. 

**Martin**
But it's not really, I mean the amount of the, we already have 15 million blocks in the old, I mean, it doesn't really matter if we have, if we move 20,000 more there or not, from a data perspective. The big game was moving out 50 million blocks from the live database, and moving in sharing up another 20,000 really.

**Danny**
And there might be other optimizations that are valuable there, you know, but they're I agree they're probably marginal compared to the big move, you know database versus memory and that kind of stuff has finality.

**Marius**
Also we only store so bad blocks are not stored in the block tree and we only store 10 of them, so for like investigation. 

**Danny**
10 for each bad chain depth or just 10 period? 

**Marius**
10 period.

**Micah**
And presumably you only have one bad block per chain right?

**Martin**
Yeah, presumably. I mean improve the work well I mean in our the way, we would only store a bad group of work block if the work is valid, we wouldn't just if someone sends us some random junk, we wouldn't have done, so if the work is correct and in a post proof mistake, well I’m not sure. I guess anything this el delivers.

**Danny**
Yeah well, that's been pre-validated validated with respect to the signature so similar, but the, you say you keep you keep the stuff not going an archive or not in the freezer whatever for 30 000 blocks that you can repair things that things go wrong, but if you're only storing the first block on an invalid chain, could in fact be a consensus split chain but how does that actually help you recover? 

**Martin**
Sorry, I didn't understand the question. 

**Danny**
Honestly we should probably move on, I’m sorry.

## [Shanghai Planning #450](https://github.com/ethereum/pm/issues/450)
### EIP-4895 updates, EIP-1153, EIP-4758

**Tim**
Okay, anything else on just the test nets generally or the merge? Okay, so next up, Shanghai first. We had Alex with some updates on EIP 4895 and then we had some other potential cfi EIPs so Alex you want to go ahead and share the list?

**Alex**
Yeah, let me just share my screen to get the EIP, let's see, oh wait I’m having some issues, okay there's, I don't think I’m gonna do that right now, that's okay, so I can just talk through it yeah I can share your document let me pull it up but go ahead and share my screen yeah I mean so basically we've talked through the process of withdrawals over you know a couple all core devs now just to remind everyone where we've gotten is that essentially you'll have withdrawals happening on the consensus layer if you actually just want to go to the rendered EIP that works as well, but either way so you have the consensus layer managing withdrawals they're dequeued in some way, piped into the execution layer. We decided to have these be represented in the execution layer as these new type of system level operations and essentially it just says here's an address and an amount and you should just credit the address. The questions that we had open last time are basically essentially syntax, like how do we want to, you know sort of structure the block, and the header and different things, and so yeah, thanks Tim, this is just what I want to show now if you scroll down just a little bit further, there's a block rlp here, where essentially all I did was say okay, this is going to be appended right after everything else, and this is like similarly in the header you have a root for all withdrawals that is again opened to the end so I think that was the main open question and I just wanted to get feedback on that point quick otherwise everything else should be about the same.

**Tim**
Oh Martin, you're muted Martin if you're talking. 

**Martin**
Sorry um I got a phone call in the middle I didn't notice that was my parent yes I was wondering if we need a protocol update for this.

**Alex**
Like devp2p? Yeah right so we will want to update that as well 

**Martin**
Uh, yeah the ETH protocol update rather than p2p.

**Alex**
Yeah, right, yeah so I was going to make a pr essentially to that repo to reflect those changes, but also wanted to get sort of, you know, consensus on this first.

**Andrew**
So one small comment, I think just for precision the withdrawal shouldn't be an rlp, the withdrawal should be specified as a list, because then like the rlp should be applied at the end, like everything is a list, or like a byte array in rlp, and then you apply rlp at the end. That's it. It's a technical small comment.

**Alex**
I think that's how it was written or did you mean something else?

**Andrew**
I think you define withdrawals as an rlp of a list, but then kind of because rlp is a string representation, but we had a somewhat similar problem with type transactions, when you additionally wrap rlp as a byte array of things like that, so currently like for instance transactions in block bodies, transactions are defined as list, and then when you serialize block body as an rlp, then you serialize transactions as an rlp but if you define withdrawals already as rlp it means that they are a string instead of a list kind of you additionally wrap a list into as rlp byte array right I want to avoid this additional wrapping.

**Alex**
Sure, I see what you mean now and yeah I can update the EIP for that.

**Micah**
Martin, is your hadn still up? 

**Martin**
Sorry.

**Micah**
No worries. We already agreed last week that we're not going to use the ohmer sash we're going to add a new thing on the end is that correct?

**Alex**
Any other comments aside from the rlp issue? 

**Martin**
Okay, so what are the withdrawals they have an index now there's another amount what is the use?

**Danny**
Oh, it was initially put in there actually to disambiguate you know if you're following logs and to make it useful because theoretically with partial draws you could have a collision there, where you get the same withdrawal twice but this might actually have negligible value and we can consider removing it, especially with the push method. Very open...

**Alex**
I think it'll still be helpful for tracking it you know like if you're like a block explorer and want to track them right because you can still have two withdrawals are the same so it does differentiate them.

**Martin**
But isn't there a difference between the explicit index inside the withdrawal itself and the index in the list of withdrawals?

**Danny**
No. No. I mean if you were tracking all withdrawals ever then there would be a one-to-one mapping from the consensus layer in the execution layer but they
are dequeued from the consensus layer so they're not tracked in a list forever but if you were tracking them you can map them one to one with no problem.

**Martin**
No, I mean like couldn't the execution…

**Danny**
This is the index of all withdrawals not the index within a single block.

**Martin**
All right.

**Danny**
Which could potentially be valuable, it is not probably critical for it to be in there...

**Micah**
Seems useful to me if the cost isn't terribly high.

**Martin**
Yeah you should probably specify what type they are

**Micah**
There are integer or yeah it's like the under the system level operation colon withdrawal subsection of the specification and it has a one two three book list that has the types.

**Tim**
Okay anything else on the withdrawals.

**Danny**
Yeah light client there is…we can link to it here.

**Tim**
Okay, so next up we had Moody with an update on EIP 1153 and I know there was already like a lot of comments in the agenda about this. Moody do you kind of want to summarize kind of where things are at?

**Moody**
Yeah hey everyone it's Moody from Uniswap. Yeah, so right now I think my goal ideally for this call which might be a little bit lofty is just to get this EIP to cfi for Shanghai and that's not to say that like I want people to commit to like putting it into Shanghai, I just think we need to get it to a point where we can fund and do the work for potentially a future hard fork, and I think cfi will help a lot with that, and just in terms of like signaling that from client developers that like it is actually a good and useful change, and so from the last call when I talked about this EIP there were a few follow-ups which I can talk about if that sounds good to you guys.

**Tim**
 Yeah if you yeah I guess yeah if you can give us kind of the updates in the last time and then we can have the cfi discussion and whatnot, yeah. 
 
**Moody**
Yeah so last time there were a few follow-ups. First was like the impact that the EIP would have, the second was a concern about the linear memory expansion costs, which we've elaborated a bit on the EIP and the third was, is this like the best version of the feature, the best API for some kind of persistent memory across call contacts, and so just I’ll go I’ll start with the first one about impact so I mentioned the issues a bunch of developers from different teams that are all interested in seeing this feature implemented, we estimated in the thread, just for v2 you know swap v2 reentrancy a lock alone and just for the storage load operation being saved it's order of billions of gas just for unit swap v2, and then also in terms of like how much load there is on nodes it would, we estimate trillions of read operations from disk, and you can read some additional context of the thread. In addition like it allows us to do new smart contract designs with future versions of protocols we develop that weren't possible before, for example, this ability to like you know do a lock across multiple pools, and do things between all the pools without doing any erc20 transfers, and in some cases the gas savings are drastic, when you don't have to transfer erc20s or call into erc20s in case in certain cases and so there's a lot of context to that in the thread, including some gas estimates we did for different prototypes. So that's a little bit about the impact. The second one is the memory expansion cost so the amount of memory you can allocate is on issue but Martin brought up an issue about the journaling costs, which isn't really fully included or like not fully analyzing the EIP. I think a simple solution to the journaling cost is just limiting the number of keys that can be stored in the map per address, and I can update the EIP to do that. I think a thousand keys is just fine, 1024 keys um or double that or some order magnitude or order of a thousand keys is fine, and then there was a lot of conversation about like is this the best version of the feature. I think one alternative was making a persistent memory op code which is by address and works more similarly to memory I think we've had a lot of conversation, I've talked to like Charles from Viper, he was asking about a different API where a t store and t-load were by address, but still backed by a map in the client and so you could write to any 32 byte word any offset, but that one was a little bit obfuscating for the solidity developers and the compiler developers so I think like this t-store t-load interface is, I think it's probably the best version, just because the language support is the easiest to add, it's very similar to s4 and s load so it's like it's easy to think about, and there's also already sort of a concept of transient storage in the uvm which works through s store and s load, it's just not very well supported because of the refund cap and the fact that you have to use refunds and then it also has to load from storage so like there's already this concept in the evm that's supported with slo nestor so it kind of makes sense to implement it via t-store and t-load and then finally mappings and dynamic arrays are really heavily used in the use cases we have and they're not supported today with memory and solidity, so it would be extra work to get developers to start using it, and for it to be available in the language. And then yeah, there was one more comment about the fact that this is like sort of just like a gas optimization, doesn't revolutionize anything. I think it I think it opens up new smart contract patterns that will quickly become canonical, and so in my opinion it does have a bit more impact than is clear to see like via you know gas estimates or I think it has a lot of potential to like improve the developer UX for interacting with, you know, swap contracts, for example, but it's hard to express that without sharing too much. 

**Tim**
Right thanks a lot for the update I know Mark, Martin and you had like a long kind of back and forth on the agenda comments and Andrew also I brought up earlier like the idea that something like say deactivating self-destruct could be higher priority than this for shanghai, so I guess just to kind of take a step back here like with in shanghai we already have a handful of small EIPs. I don't have the full list, we already have this withdrawal EIP and oh EOF was the other big one so we have EOF this withdrawal EIP that's cfi a couple of other small changes like the warm Coinbase the push zero op code and whatnot and I think on the previous calls we discussed a bunch of potential solutions to lower the cost for layer twos and none of those are officially cfi yet, but there's like some progress on them, so I guess yeah I’d just be curious to hear from clients in general like, do you think we can add anything more scfi for shanghai now would you want to wait until we're a bit farther in the implementation to decide that are there things that you think we should potentially like earmark now yeah I’m just curious how people generally think about that and Andrew you have your hand up?

**Andrew**
Yeah, I concur with Martin. I think Shanghai is already big enough and if 1153 is also big, I personally or the I have checked with the Aragon’s team members and our how we see it the priorities the following so if 4758 deactivate self-destruct is a great candidate for Shanghai inclusion because it's a simplification and it also paves the way for the Ryoko tree so our preference would be to include 4758 into Shanghai. As to 1153, I would say we can see fight for Cancun and also I think because Shanghai is already big. I would cf 4844 shot blob transactions for Cancun as well.

**Tim**
Got it. Thanks. Micah you have your hands up.

**Micah**
I just wanted to comment that I’m ambivalent on Shanghai or not Shanghai, but I do think there's significant value in core devs giving signals as to whether this is something that we are likely to include in some near future hard fork. You know I think we all agree this is kind of a neat useful thing, but is this something where we can say yes you know moody, go tell the swap team and other app developers that you should spend money and time you know developing this further and working with solidity team and working with client devs to implement this, or should we tell them, you know we're probably not gonna get around this anytime soon, I wouldn't recommend spending money and time on further developments for now.

**Trenton**
I just want to say that Moody’s question, I think what he started with was whether this could be moved to cfi, not necessarily whether it should be included in Shanghai. I think that's ideally what he'd like and the unionswap team is interested in it but I think he's just talking about cfi and I don't know if it's right to say you know, this should only be like the what Andrew just brought up like, this should be removed from shanghai, which it already isn't being included in favor of removing self-destruct. I don't know if that's the right way to think about this.

**Andrew**
Right I guess the one thing I’m just cautious about is we haven't implemented like anything that's in the cfi list yet, so like if we had already like three quarters of it implemented, I think it would be like a different conversation where it's easier to say like okay let's try to potentially add this as well and then if its working as expected, and there's no issues with it, then we can move forward but the fact that it's like there's already like six and yeah at least six things that like are not implemented I yeah I I’m just a bit cautious that like we get you know to after the merge and we have a list of then 10 things we need to implement and we're basically back in the same spot yeah.

**Moody**
So sorry I should give an update on the status like in terms of the development work we've done we've actually implemented it's incomplete we've implemented it in the Ethereum jsvm and it's been merged, and that's how we've been doing the testing is against you know hard hat with that Ethereum jsvm and yeah I agree there's a ton of testing yeah and we've written some of the evm by code tests but like of course we have to write right okay yeah so yeah sorry.

**Andrew**
I guess I was more responding to accident but like yeah they're it's good that like it's obviously implemented in one client and that it works and I think that's like really valuable, but it's there is a difference between that and like it's being implemented across like the four clients, and you know we've tested it and it works and we've had like a devnet running at it like yeah.

**Moody**
And but we don't have a good word to discern between those two things.

**Tim**
I guess I’m curious if does any client team like feel strongly that this should be made cfi for shanghai now? Yeah, it's probably a good place to start. Okay.

**Moody**
Can I ask, what about like for Cancun it sounded like one-person signal support but cfi in general I think just means that we can spend the time and resources to basically build on top of it as well as like do the work ourselves for writing those tests and implementing clients?

**Martin**
So I think that a lot of clients I’m not just going to think that I mean are going to agree that it is a useful feature, and it's very nice to have and if they ask is like would we be open to at some point in the future you know including this, I mean I would say yes, but if you're if like cfi is some kind of stamp that this is now slated for inclusion, and maybe not in shanghai but definitely Cancun or whatever comes next, and then I will be hesitant to like say so right now, but on the other end I mean yeah sure, maybe, sometime, I don't know exactly what they ask you.

**Tim**
Yeah I think the challenge is we you know like Shanghai realistically you know is going to be at the earliest end of this year probably you know sometime early next year it's all depends on there's a bunch of things but like so if you're talking about Cancun you're talking about the fork after that it's like you're talking at the earliest more than a year from now like you know say next summer like 2023 and the challenge is the priorities might change between them right so it's like I think even if we had like strong consensus on this call that like EIP 1153 is like the most kind of important thing to do after shanghai, it's kind of hard to make a commitment that that'll still be true in a year yeah and I guess we can yeah collect science we can time box this in like maybe two more minutes?

**Moody**
So I’m not I’m not sure I understand what like cfi means, like just based on the naming, it sounds like it's like consider for inclusion not necessarily inclusion.

**Tim**
So in practice yeah and in the past what we've done is like we've tried to implement all the cfi EIPs and if there were like issues that came up during like the multiple client implementations, we would you know remove them as we've had happen would say like the bls EIP where we implemented it we still weren't confident with it but there was like this implication of like if we implement it then it's all good the default path would be for it to go to mainnet. 

**Martin**
So yeah I kind of see cfi as some kind of almost promise from the client corridors that if you do the work with us and you help us with the tests and everything, then we will put in the work from our side to get the stuff merged and to, you know that there's this we have approved it, and now if everything goes well we're gonna do the work together to actually get it out there. 

## [GöeIP-001: Set Balance of 0x552fCB6425a1eD22696c967E741C3bC49c52c338 to Ninety-two Quintillion Ether goerli/testnet#97](https://github.com/goerli/testnet/issues/97)
**Tim**
Yeah I’m sorry to cut this short just to leave some time for the Görli conversation. I do think like Marius commented like we probably don't have the consensus to move to cfi today, and I think maybe one thing we should discuss on the next call, is just like generally when do we want to start, like do we want to maybe hold off in accepting new stuff for cfi until we're a bit farther ahead with shanghai implementations, and we have a better view, but I think we can probably discuss just like shanghai cfi at a higher level on the next call, and if there is no time to discuss that on the next call then it probably means by default we're not ready to add new stuff, because we're still dealing with the stuff that's happening right now, but yeah just to make sure we can cover the Görli thing. Afri, do you want to give a quick rundown? 

**Afr**
Yes, thank you very much I know 90 minute calls are draining so I will keep it short there is this kind of issue with some speculation on Görli testnet and I kind of feel responsibility to encounter these speculations, and I personally believe that the Görli testnet is still having a lot of significance initially with ETH2 or consensus layer testing now was merged testing protocols depending on Görli and I believe as opposed to like older testnets such as rinkeby and ropsten that might be duplicated soon Görli should be around for another couple of years at least, after the merge, and I would love to drastically inflate the available supply of Görli tesla tokens to first of all avoid further speculation on any non-zero value of early testnet tokens but also to provide um application developers, but also consensus layer testing engineers with necessary resources to conduct testing. I used to have a huge stock of Görli. This is coming to an end soon and I know the timing is not very fortunate right now because we are going all in merge this year but I would like to propose to inflate the Görli testnet supply. I have written an initial proposal I called it a Görli EIP 1, because I don't think testnet specific stuff necessarily needs to go through the EIP process, or to bind so much more resources so I proposed to pre-fund an externally owned account with 92 quintillion ether on the Görli testnet to keep it short. Martin said that we should not do this. I think Peter commented somewhere that we should not do a network specific or tesla specific force, eventually Martin proposed that we instead of forever hard coding one key I hold that we could just have a more generic approach by pre-funding all active validator balances by a certain amount so I created Görli EIP 2. it's linked in the agenda under the first comment and again if anyone wants to take a look, I just want to have general notion from the coordinates from the oil collapse if this is something feasible and we should consider it and I would really appreciate if we could do something like this on the Görli test net and no we should not so it was has been proposed to do something with block reward, but I believe we should keep it really simple, because if we modify the click block reward then we will play around with consensus engine and this would might this might drain too much resources from core developers that is not really necessary, so it should be like a one-off thing I believe.

**Tim**
So just yeah because we're very close to time and I think that does anyone have like an objection to generally addressing this like and you know whether we do it through like a one balance increase, or all validator increase like just at a high level, is anybody opposed to just the idea of like increasing the supply to make sure that the test nets value the testnet coin's value kind of stays basically zero?

**Micah**
All right. I don't think we should do it for that reason, but the other reason I do think is very reasonable, like giving money to people that need Görli to test things issues...

**Tim**
So to be clear I think the amounts though that like afri proposed are like so high that it basically drops to the value of zero

**Micah**
Yeah if that's a side effect I have no care, I just don't like if the only reason was to stop people from trading Görli eth for eth, I would not be in support of this at all. You definitely need a better reason than that. 

**Afr**
That is the the main reason today.

**Marius**
So Micah the issue with increasing the block reward is that we don't have any block reward on Görli, so the proposer block the miner is always set to zero and we don't have the private key for the zero address unfortunately. 

**Tim**
So one thing okay so I guess the other thing we might be able to get rapid consensus on is basically, is this something we want to do before the merger after, I suspect doing it before the merge would like delay things, but I’m just curious from client teams like how it, you know assuming we go ahead with some version of this proposal, the simplest from like a client developer perspective, in terms of timing, how the people feel about this.

**Martin**
So the consensus approval authority that the coordination of the network itself is pretty easy, it's like four or five nodes that need to be updated, but then you have the other infrastructure and the cl test that rely on Görli, and all those, I mean getting the testnet itself to upgrade with the procedures, that's pretty easy, but getting all the other infrastructure and cl into integrations upgrade as well might be a bit more tricky and would be the thing that causes a bit of delay as well, and operational issues maybe.

**Tim**
So okay, clearly there's some comments in the chats with like different thoughts what's the best way to continue this conversation async over the next two weeks Afr and then we can cover this a bit earlier on the next call.

**Afr**
I personally would appreciate if people could spend some time on the Görli testnet repository to just leave a comment. I personally believe that this is something, because it's only addressing a testnet, that it can be totally solved asynchronously. Also there is this idea of, so I turned ideas just to wrap this up are creating a new testnet and obviously was the downside of losing all the existing infrastructure, there might be a compromise in between these ideas is to have a regenesis. So basically reset Görli genesis. This is also something that could be interesting by retaining the name the infrastructure but having a new genesis, basically starting from scratch. This is also something we can discuss and I will invite everyone to the early test repository to discuss these ideas and eventually come to the conclusion. 

**Tim**
Cool thank you and yeah apologies that we didn't have a ton of time to dive into this last up light client if you want to give a less than one minute update on 4844, and this is also something we can queue up for a longer discussion on the next call if needed.

**Lightclient**
Sure, yeah, just a really quick update we're continuing to work towards getting some sort of stable devnet running. We have George working on a tool to submit data blobs that actually commits to the blobs with the kcg commitment. Vitalik wrote a really nice faq for the EIP, which I linked above but I’ll link again here, and then proto is going to start working again on the integrations next week so, you know I think by next ACD it's pretty likely we'll have some sort of local sort of devnet available for people interested in using and then maybe after ACD after that we'll have more of a like longer running devnet available I think we're gonna onboard some more people onto this over the next couple weeks as well, so we'll just keep posting updates in ACD, and in the other relevant discord channels. 

**Tim**
Cool. Thank you very much um anyone else have any quick things before we wrap up? Okay uh thanks everybody I appreciate everyone sticking around a couple extra minutes at the end.

People bid farewell. Meeting ends. 

## Attendees (29) 

Tim Beiko (host)
Trenton Van Epps
Afr Schoe
Alex B. 
Alex Stokes
Pari
Tukasz Rozmej
Andrew Ashikhmin
Ben Edgington
Daniel Lerhner
Danny
Micah Zoltu
Marius VanDerWijden
Pooja Ranjan
Marek Moraczynski
Rai
Greg Colvin
Lightclient
Justin Florentine
Danno Ferrin
Marcin Sobczak
Mikhail Kalinin
Karim T.
Martin Holst Swende
Fabio de Fabio
Pawel Bylica
Sam Wilson
Jamie Lokier
Dankrad Feist















