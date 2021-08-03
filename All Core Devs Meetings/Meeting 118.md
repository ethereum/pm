# All Core Devs Meeting 118
### Meeting Date/Time: July 23, 2021, 14:00 UTC
### Meeting Duration: 1 hour 30 min
### [Github Agenda](https://github.com/ethereum/pm/issues/354)
### [Video of the meeting](https://youtu.be/tjvviOLy0hw)
### Moderator: Tim
### Notes: Alen (Santhosh)

## Decisions Made / Action items
| Decision Item | Description | Video ref |
| ------------- | ----------- | --------- |
|118.1 | Tim to update the blog -  So just for this to be clear. If you are a validator on Gorli using Geth version is one that 1.10.6 if you're using Erigon, I'm not sure there's any of them but still 2021.0 7.04 - Alpha and if you're using Nethermind, the 1.10.79. All of these are linked in the post-mortem obviously and I'll make sure to have an update in the London announcement blog. Post on blog | [20.45](https://youtu.be/tjvviOLy0hw?t=1245)|
|118.2 | Setting up an end of life policy such as first release after Shanghai will remove the gas price field | [31.56](https://youtu.be/tjvviOLy0hw?t=1916) |
|118.3 | Micah proposed we speak to app developers about end of life for this gas price field on 1559 transactions and to see if any one has a  strong opinions and discussion about the timeline |[34.39](https://youtu.be/tjvviOLy0hw?t=2079) |
|118.4 | Tim on if we want to Target difficulty bomb only fork in December, maybe we don't call that Shanghai. And we call it some like to word name, like we did for Muir. Glacier his proposal, I think was Arctic Glacier or something like that. | [1.03.56](https://youtu.be/tjvviOLy0hw?t=3836) |
|118.5 | Tim to start an a thread on Eth magicians. Just to get kind of broader feedback on it and it is people have strong opinions. I think this kind of like the last time we could voice them on the Shanghai. |[1.12.01](https://youtu.be/tjvviOLy0hw?t=4321) |
|118.6 | Danny, the merge specific call has been discard, will happen through breakout on demand | [1.29.34](https://youtu.be/tjvviOLy0hw?t=5374) |
|118.7 | Tim, basically everyone aside from potentially Erigon really wanted to focus on the merge next that if we kind of got to a spot where we merge testnet. That might be a good spot to re-evaluate what we can put in Shanghai or whatever we call what happens in December. The kind of focus on the merge starting from here, get to a spot where we do have you know EIP implemented in all the clients and it's running on testnets and depending on how you know how much bandwidth we have there? We can possibly do some features for the December upgrade. But if we get there and realize that, you know, we just don't have the bandwidth, then it'll have to move further out.|[1.29.50](https://youtu.be/tjvviOLy0hw?t=5385) |


**Tim**
* And we are live. Welcome to awkward elves. Number 118, I posted the agenda in the chat already. Lots to cover today. I guess, the first thing is obviously, the Rob's didn't issue that happened. I think, on Wednesday, I have a Quick summary of it that I've I've shared a few times before, but at a high level, there was a transaction, which was sent from an account. I think, which would, the did not have enough funds to cover the max fee for its transaction, and because of how the assertions were done differently in death Aragon, and never mind versus Basu. It But a theorem that transaction which should have been invalid. Got the Mind into a block produced by Gareth and then it was accepted by Aragon and Nethermind rejected by basement opening theorem. And because guess was, the only mining client on Ropsten at the time and they were basically the only ones making the chain progressing. And so everybody else kind of got stuck on the the previous block Yeah, so and yeah it's you know, it was pretty quick to identify the fix. I think within one or two hours of somebody noting the issue, you know, there was a PR open and get with the fix and then pretty quickly after in Aragon and that Nethermind. And then yesterday those three teams put out of release with a fix for this, the one thing that did take a while that I noted, as it took about six hours for somebody to notice that Ropsten I was stopped,but I guess this was to notice that you would have had to be running. Basically an open Ethereum node or looking at ether scan, which seems to also be relying on, open a theorem. Yeah. So, I don't know, I guess just to start off. If anyone has any comments generally, or context? They want to add a around this.
* If not I'm I guess, Alex I had some comments in the Github agenda so if people want to scroll down I won't read the whole thing and but basically one thing he mentioned is the fact that to resolve this to repair the ruptured nodes miners have to run a full sink rather than like a fast sync and we should try to think about, you know, what would we do if something like this happened? On my net and especially at a spot where saying Gareth is the majority client, they're producing blocks, it obviously takes several hours to have a fixed out. Yeah. And I see Martin has his hand up.

**Martin**
* Yes. So this is not unprecedented we've been here before and when that happened the last time. I don't recall exactly which time but we have these long, long chains, And I think it was also a rotten and it was a pain in the ass to sink. Because when you get and I guess all the clients to the Past. Think and snap think we just select it with the heaviest one. And we just jump ahead to a state close to the head and thereby, yeah, we wind up on the wrong side of the fork because the that size 1 and what we did back then and guess is we added this command line plot. Called the white list, which is a comma-separated. Look number two, hash mappings to enforce. So you can basically start guest saying Adblock number something. I want to speak out, I want to have the hash something. And when guess then peers with someone else. Guess, we'll ask, what, what what has to do? You have for this number rather? Give me this number and it checks the hash, If it is what it expects and that means that you give will basically enter a mode where it only will speak printed on the same, on the desired change. Yeah, it's a clumsy. I mean, it's it's not ideal. It's pretty bad ux, but it's otherwise kind of hard to know. I mean, the the operator needs to step in Say, I don't actually want the highest difficulty chain. I want the other one and I don't really know how we can make the UX better, but this is this is kind of the best idea we had at the time so it is possible to handle this scenario. Yeah, if anyone has better ideas, I'm open to hear them and if not, I think it would be good if other clients also have something like this.

**Tim**
* So he's not here. But Alex, I said Aragon is working on a way to go back before any before Block in the past and kind of, I guess. 

**Martin**
* Yeah, sorry. So we do not set in Git and one thing we did consider previously was if we should add like the fourth book, minus 1. If there's like an own work, should we do an explicit flush of the state? So you can always go back that can be done, but it's kind of might be a bad idea. If the entire all the nodes on the entire network does an operation at the same time, even if it's a network brush but because it cannot macro effects with the entire network becomes slow. Although I don't really know how otherwise to do it. If you have a non-intentional for fork, I mean, is there you always flushing you basically run in Norco mode and you have every state always other than that, it's yeah, how how one would implement? But he says, other mode or do? I mean, you can do is set a big, it will write rewind to whatever state you have. It might have to go back. At 4000 blocks to the last time I flushed. It might have to go back up to like two hours of processing time but that's kind of yeah, that's where we're at. And I don't really see how we can improve it.

**Tim**
* Got it! Marius, you also have your hand up. 

**Marius**
* Yeah, I just wanted to say that it's not not 100% accurate but what Alexei said because I did set hurt the the before the for block with my note, that was snaps in so it's definitely possible if you have, I think when I, when I, when I heard about the fork, I set my I immediately set my node into archive mode to sink the chain. And so I had the states available before set at, so it's basically it's not, it's not really part of the the synchronization mode, but if you have the state available and it was I had the state available I quote, actually set her before that. 

**Martin**
* But then, it's basically, you can wind up in two things can happen. Either the fork, either. You were sinking were mainly, the fork has happened, and now you want to sink. You want to avoid landing on the wrong chain because your pivot block will be after the fork and you can use the whitest book for that. The other case is that you did sink. You let follow the wrong chain, which means you did sink. So you pivot Is earlier than the fourth book and then you pulled the wrong chain, you discover? Oh, I'm on the wrong chain, you update your Beth and now you can always do a set head back to the pivot block. Your, I mean, you're guaranteed to have the state for your pivot book and probably some other nice locations afterwards. But so both of those situations are resolvable with Geth.

**Tim**
* Would it be possible for either of you Marius, or, Martin to basically, add a comment by that in the in the post-mortem? So I'm going to I'm going to move the post-mortem from my hacking D over to the Eth-1 specs repo today but I think it would be valuable if we can just have like just Marius maybe explaining kind of what you did on your node because if in the future something else like this happens, then at least we'll have like a Some instructions about how to deal with it. 

**Martin**
* Yep. I can write on the agenda. 

**Tim**
* Did anyone else have thoughts comments about their Ropsten issue? I see we have Jeffrey. Oh no

**Jeffrey Quesnelle**
* I just wanted to chime in. I'm from the group that actually mind the block that had the problem and we were working with trying to figure out how to come back and fix it. And I would just say that the instructions there was just a lot of, we weren't sure, what should we do a debug set head? Why wasn't it working? So I think just kind of like a flowchart that would say what to do in the situation for geth miners would be extremely helpful but Then with what Beth already had in it, we were able to repair it and get the mining and get the chain going again. 

**Martin**
* Yeah. One thing I think is might be hard is knowing what is my Pivot block? And how far can I go back? And that is yeah it's not trivial and

**Jeffrey Quesnelle**
* Currently the experience is guests. Out of just either crashes or you get error messages, that don't tell you what. So just maybe just in case of emergency break this glass sort of post in the post-mortem to tell miners what to do. I think would be sufficient 

**Tim**
* Yes. Thanks for sharing Jeffrey. Anyone else have anything they wanted to add / their bring up?

**Marius**
* I think the focus not really, not really resolved yet. So, if you have any spare mining power to work on the real chain, then if you still have mining power on the old chain, if you ran a minor before the fork happened and you didn't hear about the fork yet, then please shut down your minor update your node and mine a new chain with with us.

**Tim**
* And it's worth noting. So for Ropsten, I believe, Gareth and Basu or the to clients and open Etherum are the three clients actually that can mine on it. Any other comments? 

**Marius**
* Yeah, we should also update the the sealers on all the other chains, two versions that have to fix. 

**Tim**
* Yes, that's right. A so for rinkeby I think the Geth team has all the Cedars there. Is that correct? 

**Martin**
* No, we don't have all the say there's something I can do.

**Tim**
* Okay, so I guess to any Cedars on rinkeby need to update 1.10.6, correct. Yes. Okay. And then for Gordy and there is like a wide set of validators across a wide set of clients. So just for this to be clear. If you are a validator on Gordy using Geth version is one that 1.10.6 if you're using Aragon, I'm not sure there's any of them but still 2021.0 7.04 - Alpha and if you're using nether mind, the 1.10.79. All of these are linked in the post-mortem obviously and I'll make sure to have an update in the London announcement blog. Post on blog , blog.etheorem.org later today which has updated versions listed there. Any other comments? 

**Tim**
* Okay, so, I guess, one thing that's been kind of implicit, but I just want to make sure there's no objections or thoughts about is the for clock, for London. So, all three releases from Geth, never mind and and Aragon, kept the current block for August 4th or 5th that were looking at right now. This everyone just still think this is the right approach. Obviously, you know, we found this on a testnet which is good and we've added That they catch this? Yeah, the people still feel comfortable or does anyone have a concern with going forward with the current block? Once twice. Okay. Okay, so then for anyone listening, I just to make it clear, you know, the four clock for my net, for London hasn't changed and the versions, Geth, Aragon, and Nethermind have so you can see them in the agenda for today and I'll make sure to update the London announcement blog post and share it out on social media and whatnot. Will a note about this just so it's clear. Cool.

## GasPrice for 1559 transactions [23.07](https://youtu.be/tjvviOLy0hw?t=1387)

**Tim**
* I'm so second thing on the agenda and this is my command. Yes, I am so on the last call, we discussed basically the gas prices field for 1559 transactions and to recap, the implementation is 1559 transactions. Contain a gas price field right now in order to maintain backward, compatibility with tooling and Because you can't actually know what the gas prices of the 1559 transaction before it, mines pre be in mind, the transactions. Gas price will will reflect the Maxi for gas. And after it's been mined, it will reflect the effective gas price, which is the amount that it actually paid based on the, the current block space for you. Micah has concerned. If I understand it correctly is, it's very bad to have an API, which can return Earn or field, basically, which can return a different value based on time and estate, and that'll lead to it being very hard to debug Micah. Did I get that roughly right? 

**Micah Zoltu**
* Yeah, I can interrupt you one. Sure. So yeah. So the what Tim said is basically the short summary and anytime you're debugging an issue and the behavior changes based on when you look at it, it's becomes a very very hard bug to debug. I suspect most users and app developers and Library authors and whatnot. Probably are not watching closely on these things and they will not realize that there's a change in behavior in the gas, price field. And so, this will be an implicit behavior change which if we accept should at least be something that doesn't result in like there's a really long tail of hard to debug problem. Almost, we're like my, a kind of work. Sometimes doesn't work other times, every time, a user reports, it, then when I go to check later, It works fine. I can every boost myself. Like that's what we're going to see if we go forward with this kind of behavior change to think my proposal is to just have as an alternative is to just have the max fee. We always returned as the gas price even after transactions mind because at least that way like you have consistent data being returned and if that breaks or something because of that they can easily figure it out and fix it unlike the current behavior which is the dapple still break. Just It will break sometimes and only for some users and only in some context. So yeah. So and then that and I would also like to believe you guys talked about deprecating this field. It'd be nice if we put an end-of-life date on it like maybe the first patch after Shanghai or something. I'm just so people have like a clear timeline and they know you know, is this something that I need to do? You deal with removing for my software soon or do I need to I put it off I think just saying is deprecated for a lot of people means out This is going to live forever because sadly and software. That's very common. So those two things, I'd like to get an actual end of life policy, whatever that is don't care. But I think there should be one and I think we shouldn't have this behavior where the return value changes based on time and context. 

**Martin**
* I disagree. 

**Tim**
* On which points on both, or just on the value changing? 

**Martin**
* Mmm. Well, we do have an evm opcode called gas price, right? Unless I'm mistaken. Okay. Sorry, say that again, you have one and evm opcode for gas price. Yes, but we don't don't know what that's going to return until after the transaction mines. Yes. But during when the transaction actually is included in the blocked, we do know they took the job and I think it's I don't see why we would not include that information for a transaction where we do know it. The effect of gas pricing used to gas price 

**Micah Zoltu**
* So the long term, I think the right place for that sort of information is in the receipt. Like so get transaction receipt returns values that are only available after mining. So includes the effect of gas price and status. 
For example, there's a couple other things that are not known until afterwards And that gives that makes it. So there's very clear behavior for app developers and so they know that. Hey, if I want some piece of information that is only available after mining, then I get that from the receipt. If I want information about the transaction itself, which is available before mining. So basically the stuff in the transaction and I get that from like getting transaction or whatever. I think long term, I think that's the right Behavior. Do we agree on on that, at least? 

**Martin**
* Yes.

**Micah Zoltu**
* All right. So then the question then is left. What do we do in the meantime? So we don't break people. I'm generally convinced that we shouldn't just return, nothing for that field because there are a lot of people that use gas, price or things and, you know, if we just didn't return it for 1559 transactions, those things tools would break. I feel like though, given the two options of return to different values depending on whether the transaction mined or not, I think that one's going to result in a lot more pain for app developers, just because the debugging problem. I guess the question is, do we want to do? We want a solution that is easy to debug, but more likely to fail or do we want a solution that fails less often? But when it does fail as much harder to the debug, I think. Maybe that's the trade-off here.

**Martin**
* Yeah and I think maybe us client developers are not the ones who have much at stake here. I mean, it's as Geth developer is like, we don't really care. We do this way or the other way, but it might be important for people like in Peoria or people who are actually using a evm. 

**Tim**
* So yeah, I guess two thoughts on that one, next Friday Trent and I were going to organize another infrastructure, call to get, basically these projects who are adding support to 1559 and London in general right now and, you know, answer their questions. And so that's definitely something we can bring you up there. And the second thing is basically every client has a version out for London. Now that has this kind of Changing Behavior implemented, right? Where it goes from. It goes from the max fee to the effective gas price. So I suspect, there are already some projects that have started doing this and it might be the worst of Both Worlds. If in some minor release, you know, Geth or Basu or whatnot changes the behavior because then it's like, you'll have you'll have some versions that have like, you'll have basically a Current behavior based on which non-consensus breaking change version of a client you're using. So I suspect if we really do want to make this change, it's almost like you need to It's like you need to tell people. Use this version for the hard fork in the way because otherwise, you'll be in a spot where there's just a lot of inconsistency. 

**Martin**
* But yeah, but related to this aren't there. Also other fields, which are added for transactions, which have been included in the block. 

**Micah Zoltu**
* Yes, like the transaction index and let somebody be what number number. Yeah. 

**Martin**
* I mean, all those three things that 

**Micah Zoltu**
* I would like to see all this I would love to see all this move to the receipt for the reasons I mentioned before like having the transaction return, like a static set of fields that are defined the transaction. And then the receipt return, all the things that you know, later that would be my preference. Long-term I don't I'm okay with like, a dragged out deprecation strategy for moving to that because I recognized it as not easy to just switch. Yeah, I mean, yeah, 

**Martin**
* It says it's a switch but the Whenever we do it by changes. Yes. We a lot of people get angry. Yeah, that's the problem. 

**Micah Zoltu**
* So if we do go forward with the switching context a little bit, okay? Is everybody? Okay? With setting and of Life? Clear end of life policy like a tentative dates, such as first release after Shanghai will remove this thing or whenever that is, that would make me at least a little more comfortable because it makes it more clear to people that have a real solution here, is to stop using this field and it is going away in a real-time like Just when you say a thing is deprecated, I've found that people usually continue to use it until there's an end-of-life policy in place because in software people deprecated things all the time and then they stick around for seven years.

**Martin**
* Sounds good to me. 

**Tim**
* And Michael, you're proposing basically waiting until the release after Shanghai. So that means that the gas price field would be supported basically up to the upgrade after Shanghai, right?

**Micah Zoltu**
* Without having to lose access to that field. However, if you want to run a client is compatible the next hard Fork, then you're going to have to fix your stuff. 

**Tim**
* Yes, exactly. What we're not asking people to fix their stuff before Shanghai basically, we're asking them to fix it, correct right after Shanghai? 

**Micah Zoltu**
* Yeah, sometime between Shanghai in the next hard Fork. If we chose, you know, patch after Shanghai, then that means that people need to fix their stuff sometime between Shanghai and the next hard Fork. So that gives them like 6 to 12 months. No, depending on hard for timelines. The strong opinion on, you know, time, I care more just that there is one.

**Tim**
* What I like about Shanghai is basically, we need to have a fork around December this year, right? So I like that, we can kind of put a date on it already because of the difficulty bomb. So I, you know, and it's also like far enough in the future that like clients are applications, don't need to deal with this today but it's, you know, not that far that the sticks around forever. So I would be fine for keeping this until basically, the difficulty bomb pushed back. and removing it in the release after 

**Micah Zoltu**
* Okay. So how about then for path forward? So we can move on to the meeting. We will tentatively say a chapter Shanghai is the end of life for this gas price field on 1559 transactions. It will still remain on Legacy transactions because it actually is part of the transaction there. People can discuss this in all Cordova's Channel and Discord with. You have additional thoughts after the call separately. Let's talk to the app developers and the call you've mentioned next week and see if anyone Strong opinions. If we're going to be deprecating this in the next six months I am more, okay? With just having this weird kind of behavior that we currently have. Just because I know it's going away and we can just tell people when they run into these bugs. Sorry. Anyway, we did our best to give you something that kind of was a stopgap, but you really shouldn't use this field.

**Tim**
* Yeah, I think that makes sense and on also bring up the timeline on the call next Friday with them to see if anybody has like a stronger reason why that would be too quick or something. Anything else on that? For me. Okay, I'm so next topic. Oh, Rai or go ahead? 

**Rai**
* Yeah, actually, if I want to move on, I just wanted to ask a question about a possible plugin Geth after midnight forks, I was just curious, what people's expectations are for the Dynamics around Miners. And the community, if there is a bug and get someone who's relatively new space wasn't around for what I heard was a bug, getting enshrined in ready at this point to understand. Yeah. What how people think this would go down? 

**Micah Zoltu**
* Poorly.

**Artem Vorotnikov**
* I think we should just recognize the current reality and make it so that if there is a consensus issue and gas is in the wrong, then everyone else corrects the way. So that it is the same way as Gap and we just added the yellow paper to account for The Quirk for specifically for gaff 

**Micah Zoltu**
* It would be great if I kind of agree with our time that I suspect, that is how it will go in reality. And it would be great if we could avoid that though. And just because it just means we now have this technical debt that we're going to struggle to get rid of for probably a long time to vent on the bug, some bugs, you know, you can pay it off the technical decnet next hard Fork, whatever. But I do worry about introducing technical debt because of a bug introduced and guess them socks.

**Artem Vorotnikov**
* I'm afraid it will be too painful for the main net especially since May net by the time, we recognize the bug, find the bug, the main net will basically to billions of dollars but that by the time and it will be inevitable that this back, we'll just be written into history, written to the annuals and recognized as a queer community room history and that's it.

**Martin Holst**
* That's it for the there is another I mean yeah there is also an added complexity. I mean even if we were to say that yeah our team's proposal that's what we're gonna do. They can also be that the bug is only in get the latest version and 40% on that were 50 or 60 but in older version the bug is not there. So It's not only the case that we may have. You know, Geth this off from the rest. We can have gets pissed off from Jeff and the rest is so we still might get very complex scenarios. 

**Artem Vorotnikov**
* And I think it should generally be go with the majority chain and that's it. 

**Martin Holst**
* Yeah, I would not commit to do that in right before. Knowing what the bug is because the if we decide to leave a bug there, it might have it might be able to, you know, To be used in ways that make it a denial service vectored might be able to without knowing what bug is. It's kind of hard to Right. 

**Danny**
* That the majority of Shane could have printed a hundred million ether and we probably will not follow that. 

**Martin Holst**
* Yeah, I mean we do have a Kate, we know that there is there was a bug in both got them party which was discovered After the fact and you know, that the ripened the touch delete which was not deleted because it was a pre-compile. And to say that when just the man with the yellow paper that we haven't actually managed to do that, we haven't fully been able to describe the scenarios where it where, you know, the this Behavior. How to describe this behavior, is it something special about ripened be? Is it something special about the weather? The rollback happens in the outer transaction or in an internal transaction? Or it's something magic with recompiles? It's it can be very difficult to. Yeah, retroactively So, I don't know. I I think it's difficult to I mean it's good luck with planets and discuss it but I don't, I don't really think we I cannot will commit to any particular strategy, right beforehand before knowing more facts about it? 

**Artem Vorotnikov**
* This discussion, it would be so much easier if we had think, like, Regenesis on the table where we could, you know, not not fix, go with him, not roll back, the main net, but instead have the square cake, enshrined and then have Regenesis. After some time, which would erase that Quark from the code of all implementations. Where we could fix fixed. Implementations. Remove the post complexity by just setting a new genesis block basically with the current state. 

**Lightclient**
* I think that's what we're looking into. Estate expert.

**Artem Vorotnikov**
* There are two parts to this proposal. One is just Regenesis, basically sitting the new genesis block. And the other one is expiring is shadowing the inactive State, the state x 3. It is a two parts of one big proposal basically 

**Micah Zoltu**
* On this vein of topic. Do we have any ideas or thoughts or plans or strategies for maybe trying to get more client diversity in miners or validators in the future? I'd or maybe Danny knows is do we expect more Klein diversity and validators for consensus that broomstick? 

**Danny**
* I think we have a bit more diversity right now and it is still trending in a positive direction, but it's hard to say. 

**Gary Schulte**
* It's probably to be determined yet, what the execution client distribution is going to be like, Training is only paired with the consensus client. 

**Tim**
* Yeah, and yeah, guys like us we want I do ideally. We would want to even I was just gonna say I suspect because of like switching costs, right? There's not like a magical thing that will happen where the client diversity resets after the merge. Just because if you're already using death or you're already using never mind and the goal of the merge is to minimize the amount of of I guess changes for application developers than you know. Yeah, you'll be in a spot where you don't really have to change your number.

**Micah Zoltu**
* Yes. But I think we actually do have a little better client, diversity and non-mining clients partly because not all clients can mine. And so like, another mine, for example, there are zero, my name, none of my clients,

**Gary Schulte**
* But there are non zero non-mining actual players in in the merger. Going to be somewhat. Different was not going to be a domination of just a handful of pools. 

**Tim**
* Yeah and William had a comment in the chat about MEV, right. Like that's another big factor in the client diversity so clients that are obviously optimized to capture our maybe there's just like a higher incentive to use them and especially so after the merge So first, I guess, any other thoughts comments on Rai Original question?

**Rai**
* Do you think there's like, is there some number n number of hours? That we think miners would roll back? Even if we did like if we if we did had have the worst case, where Geth doesn't disagree with older Geth clients and everyone goes one side. Or is it kind of like as soon as it happens? No matter how fast the pics goes out? What's good?

**Micah Zoltu**
* I think as Martin indicated earlier, it depends on the severity of the bug. Like if it was a bug that printed 10 million Ether, then I think we'd probably rolled back, no matter how long it took if it was something like, you know, it's annoying. It caused a desync, but things continued functioning properly and it's more likely that we'll just roll forward with it. 

**Tim**
* Yeah, and it's also, I guess one kind of factor. That's worth noting is just like the time that it takes people to move Eth, right? Like the amount of deposit confirmations on an exchange, for example, or, you know, the time that it takes to make like a uni swap trade is on the order of like minutes. And even for the most severe bug, you know, you're on the order of hours to find the bug in and put a release out. So, Or are you know, in those hours? Like our Tim said there's like billions of dollars in settlements that happen. So if anything kind of changes the history there, you're in a spot where you've changed stuff that you basically can't undo, right? Like you, you're basically double spending on exchanges and undoing your lot of undoing a lot of other activity, but that's happened on China. 

**Martin**
* Yeah, but I mean, there's always been Been the notion, right? If you run an exchange, you should run multiple clients and you should detect when they are not in sync and hold the deposits or withdrawals and take step to the back. Yeah, we've always been open with the serum that there can be forks and there will be consensus issues and there's the possibility of that. We don't have the reference client. 

**Artem Vorotnikov**
* To be honest, I think that even in the case of, you know, someone preaching a hundred a hundred million. If the Better Way Forward would be to just have something like that. Thou Hartford number two, then to roll back the chain. Because if we roll back by, even by hours, this would completely destroy Ethereum is reputation basically. As a reliable platform.

**Danny**
* Now, hurt for number 2, would necessarily be possible that I think that was possible because of the peculiarities of the capital being locked for some amount of time, whereas many versions of such a bug, would, you know, result in many transfers Center exchanges, you know, swap trades, all that kind of stuff. So, I really I mean, I don't think that we can come to a like, conclusion as to how we would. Receipt, I think we there are just so many options for the many types of bugs and many types of peculiarities that will emerge.

**Artem Vorotnikov**
* Yeah, just a bit point out. I mean, there's nothing that's very like, that's particularly special about along this chain, right? So it soon, as they kind of the rules that change follow diverge anyway. Then some exchanges might be on one chain and some extent might be on a different chain and it. Yeah, to me, to me, it seems like it was always kind of the obvious part of the social contract, on the Ethereum that if you end up on a chain, that does not follow the ethereum rules, you're just not The canonical you doing Jane and like, maybe potentially. If it's a super small difference to the cannot to the conical root and it doesn't matter. It could be that we end up just kind of accepting that as the canonical chain retroactively. But I don't think it makes sense at all, to kind of have any standardized expert expectation, wrong that behavior. 

**Martin**
* I want one more comment. Yeah, just so is instead of just generalizing? So let's say for example, this party better option, it's that had happened on London. I would talk to me, except if we just decided to change the rules and allow it because the only side effect would well, it turns action made it into a block, the transaction did fully cover, all its own expenses, it had the balance for the effect of gas. It just failed check, which is not really that important. And I would totally be a favor to just. Okay. We don't have to reactionary wine. Magnet for that. But yeah, Captain I wouldn't make it in general. 

**Tim**
* Yeah, that's a very good point.
* Rai feel like we've answered your question, or does anyone else have any comments or concerns about this? 

**Ansgar Dietrichs**
* Yeah. Maybe just thought I'd run it up. I wanted. Yeah, go on Insta. I'm sorry. I just wanted to Question is, would there be room for like, some sort of Oracle system to quickly kind of informs stakeholders that there's some sort of consensus issue? Like I mean, of course, ideally exchanges and everyone should run multiple different clients that quit their, I don't know, exactly makes any sense at all, but could there be some way to kind of like, very efficiently and People that now would be the time to be very careful. 

**Martin**
* And yeah I mean something like for come on, if you could subscribe to events from the fourth one, for example, or people built alternatives to the cork one, That's what it's there for you. 

**Micah Zoltu**
* Sounds like a great product idea and business opportunity for someone listening on the call. 

**Tim**
* Yes, and I suspect a lot of exchanges or other infrastructure is basically have something like for C'Mon. And that says, if you see a bad block, just pause everything, until the human investigates, 

**Danny**
* I would say some rather than a lot based off of my conversations,

**Martin**
* I'm fairly certain that in particular has fun. And if anyone wants to add the feature to the existing, for clone the Repository, I think has been moved to ethereum so it's like node monitor PRS are welcome. Otherwise we'll we can try to extend it ourselves. Might not be yeah, it might not get done next week but surely something we can look into 

**Tim**
* I know there's a core Dev apprenticeship program going on right now. Yeah, if you are a core dad Apprentice this seems like a pretty low hanging fruits, that provides a ton of value to the ecosystem, and if you're not sure how to get started, just asking the Discord and somebody will help you. Any other thoughts comments? Okay. Yeah. Thanks a lot for bringing this up, right? I think this is a pretty valuable conversation to have Okay, 

## Working on Shanghai and the merge in parallel [53.16](https://youtu.be/tjvviOLy0hw?t=3196)

**Tim** 
* So next up on the agenda that our big topic, so we talked a couple calls ago about potentially working on Shanghai and the merge in parallel. And on the last call, we briefly touched on it, but not too much. And I guess I was just looking at dates and it feels like a little high level. We basically need to decide either today or on the next call. If we And to do more in Shanghai than just a difficulty bomb, push back. The reason behind that is obviously if we just do a difficulty bomb push back, this is not something we need to deploy on test nets before main net, because they don't have a difficulty bomb. It's obviously kind of a one-line change. It's something that's easy to test and whatnot. So we don't need to like add complex new features and clients. So you know, we basically don't have to decide if we do it. And for how long probably until October or something, on the other hand, if we did want to include new eips, alongside this difficulty bomb pushback, which has to happen, sometime early, December, and then we basically need to have the finalists of the EIPs chosen, like in the next two weeks, so that we can then start implementing them. Testing them having an upgrade on test net than having an upgrade on maintenance. And it's also Worth noting. And you know if we do want to focus on the merge and client teams can't do everything and so it's not clear that you know it's not clear. What's the capacity to say do those things in parallel and how much that would push back the progress on the merge? I'm so I guess. Yeah. I'm and oh, so yeah. So there's a comment in the chat about saying are we certain that the merge this year is no longer an option? And we don't know. But regardless of that you know it's like if we work on something else and not the merge we probably push back, you know, the merge more. So yeah. I guess I'm curious with different trying teams. Think about all that the idea of like Shane Guy versus kind of Muir Glacier part 2 versus the merge. Yeah. 

**Artem Vorotnikov**
* I think we should do Shanghai. 

**Tim**
* And by Shanghai you mean like a feature Fork? 

**Artem Vorotnikov**
* Yes. If it you for it. I mean there is at least one EIP that I would like to see in that is the theorem object format for EVM but maybe we should also include something else. 

**Martin**
* Are you speaking for Aragon? I mean, the selection also. Feel that way, you know? 

**Artem Vorotnikov**
* Right now, I'm speaking for me personally but I would suspect that that would be his position too.

**Micah Zoltu**
* One thing to keep in mind with the Ethereum object format, is it keeps coming up as a potential long-term solution for some hard problems like State expiry. And so, it is part of you can consider it. I think part of long-term feature development, like it's a, it's an iterative step, but it's not just like a one-off like little thing. It's like enables. Some bigger things down the road. This is EIP number. I don't know, I thought might sorry, but if I follow 3670,

**Tim**
* Thomas, you had your hand up. 

**Tomasz Stanczak**
* Yeah. Sure. I think it will be great to keep pushing for the testnet for the merch in October. After some of the workshops and meetings, I know it would be a very short term but at the same time we expect that end of September, some big push, it happen from all client teams and then I believe that if testnet happens, then they'll be a period of time when many many infrastructure providers and users and apps will be experimenting with it. While the us, may we focus for a moment on the Shanghai fork and I would probably be happy to say to introduce some of the eips that were proposed. And I was looking today at this object format, to remember that many teams were suggesting. It was important, and I think the reasonable to take it into account 

**Tim**
* So basically just to make sure I understand you're saying you know we get merged testnets up as soon as possible you suspect, we might be able to do that before October. And it's like when October comes then we end the testnet up. Then you think we would have more bandwidth to work on, you know, kind of a feature Shanghai. 

**Tomasz Stanczak**
* I think that's maybe and of October test that is more likely and then if we if you manage to keep Shanghai reasonably slim and the like outside of coredev still be enough of the analysis of the EIPs, that one or two, make it the Shanghai and the other ones may be proposed for Cancun for next year. 

**Tim**
* Got it. Rai you any thoughts? 

**Rai**
* Sorry, I was distracted by something was the question.

**Tim**
* Any thoughts on basically Shanghai versus the merge versus Muir Glacier part 2? 

**Rai**
* For December. 

**Tim**
* Yes. Well, I mean not necessarily committing to, like having the emergent December but what're, you know our Focus right now should be on, you know, just focusing on the merge trying to potentially add features for Shanghai in parallel or yeah? Any other thoughts? 

**Rai**
* I'm leaning towards focusing on the merge. 

**Danny**
* Okay. I have a couple quick comments, one I think. Getting the other side of London, spending some time with the new merge EIP and accompanying. Other specs through September is going to give us by much better information. And I also we'll say that a number of researchers and developers certainly are stretched then and committing to a fork at the end of the year and committing to driving headfirst towards emerge. At the same time, seems like committing to a lot of work that we often kind of get into and then realize we have too much on our plates. So Yeah,

**Tim**
* So it seems like, I, I agree, we tend to over commit to stuff. And even, you know, I think London was an example where we tried to keep things small and it kind of grew. So I suspect, whatever. We commit to will end up being bigger than what we kind of agreed to upfront. It seems like everyone is kind of aligned on focusing on the merge. And there's some disagreement about, you know, when and how we might be able to focus on something else. So, perhaps it probably makes the most sense that, you know, obviously get London out the door, which will happen, which will happen in the next couple weeks, then, spend time going over kind of the merge requirements and whatnot. Then we can maybe make like a more informed decision after that and it's just worth noting that. Yeah, at some point it becomes kind of unfeasible to implement test deploy stuff on testnet, and deployed to maintainnet, but we don't necessarily have to make that call. 

**Danny**
* And a couple months ago, we discussed queuing up a feature fork in terms of wedding, proposals, and kind of figure out what that would look like. And I would say, regardless of wind Shanghai does land, it's probably good to. We can have that conversation in parallel to the merge without having to do an incredible amount of technical work on it. And so the overhead Avec planning for that is probably low, whereas, the overhead of actually releasing it on a certain time line because That's when you are a lot of the work comes. 

**Tim**
* Yeah, that makes sense. Micah you have your head up.

**Micah Zoltu**
* Just as a reminder Shanghai will happen this fall because we have two moves, the difficulty bomb, just question of whether it has interesting things in it besides that also, do client developers currently have an idea of How difficult the VM object format. Implementation is just like one of those things that's like relatively trivial easy, or I was just a big project. 

**Martin**
* Marius said, knowledge is going to say. So we talked about one of them which is 3670 and which is kind of smaller than me, but it also requires 35 Court. It would just be you fp1. I think well, I think it's non trivial to implement and I think it's non-trivial to going to make test case. For that. But I mean I'm I'm fully supportive of it and I think it's good and it's going in the right direction. But yeah, I would prefer to focus on the merge for the next. That's very, very was as I was looking for, just like, I got feeling on complexity, 

**Tim**
* And I guess, yeah, you have another point about like Shanghai will happen. You know, in December, oxic had a comment about that where like, you know, maybe for clarity, if we want to fold, you know, if we want to Target difficulty bomb only fork in December, maybe we don't call that Shanghai. And we call it some like to word name, like we did for Muir. Glacier his proposal, I think was Arctic Glacier or something like that. So that Be like an easier way to differentiate between them kind of saying that, you know, the merge is obviously kind of brilliant proof of steak over to the current evm chain. Maybe we have Shanghai, which is the set of features, and we have, you know, something else called, it Arctic Glacier, which is just a difficulty bomb pushback. And two of those things might happen at the same time, right? Like or I guess if we were in a spot where the merge happened in December, we just don't need this kind of Muir Glacier part 2, but if we are in a spot where in December Were we feel like, you know, we want to do both the difficulty bomb push back and add some feature. We can just have, you know, kind of merged. Those too hard for X but have Shanghai only referred to like actual functionality improvements so that it's clearer for EIP Champions. Like, you know, like we maybe don't know when Shanghai is, but we know that, you know, these set of changes will come together on on the network.I see, there's a plus one from Martin in the chat is not about having kind of the three different names, like merge Shanghai. 

**Martin**
* And oh, no, it was the common to, but just implementation, which is cool, really good.

**Gary Schulte**
* I think that's a good naming distinction to him. 

**Tim**
* Okay, so yeah, I guess that's anyone disagree with having the three names and worst case. If we do have Shanghai, which features at the same time, as this difficulty bomb hard work, we can just merge. Those two specs into one 

**Micah Zoltu**
* I do, but I've already expressed them many times before and so I don't need to reiterate them. 

**Tim**
* So just to be clear, you'd rather it to be called Shanghai. No matter what's in it. 

**Micah Zoltu**
* In the fall of 2021, we don't know what that's going to contain, but that's what we call the thing that happens and 2021. It's a very different strategy. That's my strong preference but

**Tim**
* Thomas, you have ambiguous comment in the chat as well, so which option do you prefer?

**Tomasz Stanczak**
* So one question, because it keeps saying the fall, isn't it not to happen in December? 

**Tim**
* Yes, which would be winter. It's alright, depends on your hair reading, I guess. Yeah, that sounds of the confirm is just a matter of geographical approach. 

**Tim**
* Okay. So Thomas you prefer calling, whatever happens in December Shanghai, right? 

**Tomasz Stanczak**
* Yeah, I think it also helps Community to understand that they can at least vote for things to be in there or not. And when it happens chronologically,

**Tim**
* Okay, I don't have a strong opinion, so if people prefer not to keep Shanghai, I guess. William, there's one opposition to keep in Shanghai. Referring to the Future Fork, but 

**Marius**
* Yeah, I would also oppose. I would also say that it's cooler to have the three different names and merge them if needed and to keep Shanghai as the feature fork regardless of whether it happens in December or q1 2022. 

**Martin**
* Yeah, I will post the opposition. I also lean towards having whatever, whatever is in the next fork and we don't know what's in it, but it's Shanghai. Makes it, I think it makes it easier. 

**Tim**
* Okay, I guess the seems pretty split do. It's like a weird way to phrase the questions, but do people kind of is it worth bringing this to say like the infrastructure called her and all core devs. And actually talking more with people who proposed eips than with core devs and kind of see what they prefer because I guess it feels like in a way, you know, we will kind of figure it out no matter what it is, and it's kind of our job to stay on top of this thing. But maybe kind of the perspective of People who are actually submitting stuff into these is you know, what makes it easier for them so this. 

**Micah Zoltu**
* Yeah. I think it also has an impact on just the broader Community people's people. Often talk about London, for example, long before London comes out and So, I think, I think they also are stakeholders that matter, like it shows up in news, article shows up in chat rooms, it shows up and Twitter tweets, like these names show up everywhere and they affect a lot of people. So yeah. 

**Tim**
* So with that being said, you think the time like Shanghai in the, in December, is it's just easier for people to keep track of 

**Micah Zoltu**
* That's my feeling but like if we wanted to solicit external opinions, I think that we should extend beyond just EIP authors and also trying to see if we can get feelings from the broader Community which I know is extremely hard. 

**Martin**
* So, the didn't we didn't kind of decide to use the dev com sites as the name for hard works just so we wouldn't have to be by shutting about names, so much in the future. I'm crazy. Why we should deviate from that on that? 

**Pooja | ECH**
* That was the first time when we decided that we will be following that Devcon names. And right after Istanbul, we did Muir Glacier because that was just the one Fork to push the difficulty Bob and I feel that it makes sense. If it is only for difficulty bomb, we should have something like that was proposed, like, our Arctic Glacier just to be in sync that. Okay, fine. It is just for difficulty bomb. And for all other feature folks that are very important for people to upgrade their nodes especially like with the latest of client it makes sense. I mean that's just my thought and it's not like very, very hard 

**Martin**
* And Yeah it's not a hill., whatever. 

**Marius**
* For me. It's also not the hill I want to on. Just my idea would be if like we start pushing for a feature fork called Shanghai and we then realize that it's like and we say Shanghai is going to happen in December and we then realized that We cannot really do the future for in December and then have to, I don't know, either kick the EIPs out of the out of Shanghai. I think then naming the the feature function high and moving, it would be better in my opinion than basically taking out all of the year. Piece that we said are going to be in Shanghai.

**Tim**
* Yeah, I I think the way around that is we just don't commit anything to Shanghai, you know, until we get there. It does feels like yeah, it's starting to get like bike shedding. I'm not sure is yeah I guess yeah I'll start a thread on Eth magicians. Just to get kind of broader feedback on it and it is people have strong opinions. I think this kind of like the last time we could voice them. Yeah. I don't think it makes a lot of sense to discuss. Much more to call.  Lightclient, you have your hand up. We can't hear you if you're speaking. oh, sorry about that if you want to come back with your comment, when Your mic works. We can we can have it later.
* Um, okay. So to change gears completely from bike shedding this week, Mikhail opened property IP for the merge. So, EIP 3675, and you wanted to take a couple minutes to just kind of present it and potentially get some some feedback, or at least Point people to it. Yeah. So Mikhail the floor is yours. 

## EIP-3675: Upgrade consensus to Proof-of-Stake #361 [1.13.19](https://youtu.be/tjvviOLy0hw?t=4399)

**Mikhail**
* Thanks Tim. Hey everyone. So yeah, they see EIP is the specification of the their Network consensus. Upgrade to the proof of steak, which is driven by the, we can change. In simple words is what we know is the merge. And this specification is the minimal viable mirror version of the merge that we have been discussing for like, several months already. Like this specification in its base is has like a number of proposals certain from various with Alex, proposals from the early and not that early days, going through the separation of concerns between the execution and consensus clients, and executable be can chain and click merge while rule, proposals, also the ideas from the high level design for the execution. I am, that has been presented by a few months ago and the Ryan isn't Stacks. The stack are also in the basis of this specification. So, that's the huge milestone for all the major Sheppard's on end for the Metro project and the result of the tunnel contributing of tones of efforts by different researchers and developers like modern for about two years. Yeah. Yeah, that's like the brick history overview so quick. Or speaking about this particular specification, I'd like to highlight a few things in which this specification is a bit of a bit unusual with respect to other EIPs. So first of all, this EIPs introduces, the new heart Fork mechanism that will be used for this API only I guess it making the reason. Predefined hardcore o'clock number instead of the block number and the terminal total difficulty will be used. And first block that reach this terminal. Double difficulty is considered as the terminal for block and any blocks that are Beyond this terminal, proof-of-work block, Must be a not protest by the notes that follow the protocol. So, yeah, for the rationale behind this particular mechanism. See the security consideration section of this document. Also, the these terminal total difficulty will be communicated by the consensus layer. So it's not like pretty find its communicated in there. Time. The other side is that, obviously, the other thing is that, obviously, we have, like, like the other side of the logic and specification, which is the consensus layer. 

* It's not specified, is just mentioned in several, like, throughout the document in several references, but it's not specified in this EIP. And the obstruction that is used for the consensus layer to be like presented in this back is the proof of stake events. You may find a section that describes this events. They are a bit tricky, so be careful with reading them. So that's that's how that's the to like things that I was going to mention also like this is This is one, this is one of the first, EIP relating to the merge. The other one at least is considered to introduce the deprecation of the difficulty of code in favor of depreciation, of the semantics of the of existence, semantics of difficulty, of code. In favor of this, op code to return the randomness accumulated by the, we betcon. So, So we haven't missed this change, it's just going in the Supreme deity. So yeah, that's kind of all I would like. Also to hand over it to Danny. Probably has more comments. 

**Danny**
* No, I mean, I think you hit the high points specifically. These events allow this specification to Black Box the functionality provided by the beacon chain. We see that Speck is handled entirely in these two aspects and from a practicality standpoint, the functionality will likely be handled from a client on that side. And those events. Although we don't really bring up like the fact that it will be a consensus API. Those events map to things that would be coming from that consensus API. That we've worked a bit with in the past, I don't know. Yeah, I think that this should read. I'm pretty cleanly if you're used to. Yeah, I peas and you're familiar with the inner workings of any fun client today. So, but we'd love any feedback and discussions. And, you know, this is a starting point will iterate from there. 

**Martin**
* I have a question. So obviously the block structure is not changed and we have the hard-coded can check the empty list and we're having a lot of zeros for the mixers for the stairs for the Gnomes, Etc. How come we're so afraid of modifying the header

**Danny**
* I mean, this is, this is a good discussion point that we can get into. We're not terribly afraid when you do, when we do modify those the modifications Ripple outward not just from the client, but into usually, their apis and libraries and things like that. So, it does probably have a more impact on the infrastructure providers and isn't as self-contained within consensus. So, I think that's definitely. One of the things I would want to contemplate before doing deeper changes, but they're on the table, we can certainly discuss them. 

* And I guess given 1559 and coordination around libraries and infrastructure providers people that have gone through that process, here would have a better handle on What such complexities might introduced and how much work it will be for the ecosystem. I think if we don't make some of those changes, it's a pretty nice user story and that would be I think that's my primary argument for not making them. 

**Tim**
* Yeah, I guess they counter to that is if we don't do it you're kind of stuck with these fields for, you know, potentially forever for as long as we leave them in there. 

**Danny**
* Yeah, I guess. Yeah.

**Tim**
* That's maybe a good question to have with some sort of merge infrastructure called like, is it better to have the smallest set of breaking changes? Or is it better to basically you know do stuff like changing the block format then because Anyways, people are updating their infrastructure and what not? 

**Mikhail**
* Changing the block format. If we do want to go this road, we will have to consider that. There are existing applications that potentially can use the block. The existing block format to validate is like receipt, route and transaction route. and even as like state  route by by taking the blog header, we refine it with people hash app code and Parson it according to the to the block structure that we have now and then using this data and how.  So like if we drop some fields at the end of the block header, it might not break these applications but the way we should consider this, right?

**Martin**
* You mean like it? Well, some Onsen validation of previous headers. It migt be worth looking into how much of those exist and how they're written. Right. 

**Danny**
* That's kind of like, well, not quite the same, but any sort of validation is against block against the hash, in the state route, are likely to be broken at some point. And hopefully there's not a ton of that on on chain. 

**Tim**
* Lukasz. 

**Lukasz**
* So we were discussing in the context of London, potential bugs issues, and like, Robux, and Etc. So, I'm not sure if there is anything we can anticipate with going to proof of steak, that we should might roll back to proof of work for example. But again, modifying more things like block headers, Etc, Make this even more complicated.

**Danny**
* Right answer. And I do think that the do some of the work to do over the next few months is better. I think the security considerations and different pads available or in a number of our heads, but we want to spend a lot of time writing that down, I'm working through contingencies and and that kind of stuff. As you can see further threat analysis at the bottom is DVD. 

**Tim**
* Any other I guess questions or comments on the EIPs. I thought it was a discussion about mining in the comments. 

**Martin**
* Yeah. Yeah well I just like to follow up on that last question. One more thing. So with a it with there is the concept of finalization, right? So if the majority eth1 client cruises and what me know, an invalid or incorrect State Route, and it gets accepted and eventually finalized the what? Because what's the timeline between that invalid States being included and it being finalized? And after that, would that be in any way possible to rollback finalized state, or do we say that? No. Further analyzed finalized. 

**Danny**
* So finality happens in the normal case in Tupac's which is about 12 and a half minutes and there's a couple of things there. So if a majority client or set of clients that represented a two-thirds majority, did have some invalid State transition that they agreed upon and they were able to hit those thresholds. They could finalize such a state, but you end up having a pretty substantial Polar thing as in proof of work.If I'm running a client that does not agree with that state transition. I'm just now going to be on a minority chain. That is being built, but is not necessarily being finalized. And at the end of the day, you can specify, you know, you can manually override and certain command line parameters for sure. Probably exists to be able to manually override such that even if something was finalized finalizes. You know, there's something social there but it's also like a practicality standpoint like that and less manual intervention is final and will remain within my chain, but in the event of error, you can always intervene going. 

**Martin**
* Yeah, I was just I think that's social element is going to be pretty large because I think the you know the essence of the word finalized, right. A lot of users to do. Care about the college's. They, you know, so it does final a - yeah, I see that, I see that and maybe we should consider a bit more. What that path is. I mean, it's from it's a yeah, okay. You know, it practically something. A hundred blocks deep and prove work is finalized as well but It doesn't carry the same term.

**Micah Zoltu**
* I think so, cause you can't have a shadow
* Fork that will cause clients to automatically switch bodies. 

**Danny**
* I agree. It's finalized from the way that people generally handle it and think about the state there, but it is subject to more attack vectors than a previous state finals chain would be

**Tim**
* I guess just because we're almost out of time. What's the best way to continue this conversation? I guess it's the there's a discussion to two field in the EIP. We obviously have their Discord for more like synchronous stuff. Anything else we Cal Danny that you think where you think people should kind of keep track of and leave their comments? 

**Danny**
* I would say those two. There's a merge channel in the Discord that we can specifically talk about. Obviously a lot of those my triple out into awkward elves at certain point. And the discussions to is fine Mikhail's, anything else just?

**Mikhail**
* Yeah, about the calls that are devoted for a specific topic. So if we will have something big to discuss, like, consensus API that involve both like becoin remain at quiet developers. 

* I think it makes sense to make it cold devoted for this kind of discussion, which will be just announced in advance. And yeah, and will happen on demand 

**Danny**
* And Mikhail. You're also implying that we are likely going to deprecate the merge specific call. That was regular and moved to discussions and awkward devs and that eth2 to specific call. And then if we need kind of a breakout room call on a specific topic, we will do that on Demand, right?

**Mikhail**
* Yeah, right. And yeah, we are tentatively book. This lot that previously used for the merge calls for this kind of breakout sessions.

**Tim**
* We only have three minutes and yeah, like client has pointed out a couple times in the chat. We kind of lot. Got lost in . Should any of the names earlier but didn't actually get like a super strong commitment on the actual next step in which we want to focus on. So it seemed to me like the most people I think. Basically everyone aside from potentially Aragon really wanted to focus on the merge next that if we kind of got to a spot where we merge testnet. That might be a good spot to re-evaluate what we can put in Shanghai or whatever. We call what happens in December. Does anyone disagree with that to basically, you know, kind of focus on the merge starting from here, get to a spot where we do have you no ill implemented in all the clients and it's running on test Nets and depending how you know how much bandwidth we have there? We can possibly do some features for the December upgrade. But if we get there and realize that, you know, we just don't have the bandwidth, then it'll have to move further out. Does that generally make sense to people, are there any strong objections? Okay, no objection. 
* So I guess. Yeah, at a high level. Let's do that, unfortunately. So there were two EIPs more that people wanted to present on this call 3670 and 3651 3670 was from oxic. And I know William. You kind of sat through this entire call and you're not, you know, kind of it necessary. Regular attendees of do you want to take like a minute or two to just quickly, present your EIP and point people to where? They can they can, they can interact. 

**William Morriss**
* I've shared my prepared statement on a ethereum magicians and posted the link in the chat. (https://ethereum-magicians.org/t/eip-3651-warm-coinbase/6640/5?u=wjmelements)

**Tim**
* Okay, thank you very much. Cool. And then there were. Yeah. So next week, I basically all core devs time. So exactly. One week from one this call started, we're going to have 1559 and London called for infrastructure providers. So if you are working on an application wallet or any other piece of infrastructure and are in the process of having 15 implementing London, support and have some questions, please come then and we can try to help you out as much as possible. Lastly others to peep in deep sessions happening. That are pretty relevant next week. Pooja, do you want to take 30 seconds and go over those two? 

**Pooja | ECH**
* Oh yeah. So to celebrate the Ethereum's, sixth anniversary. We are organizing to special people, anyone with EIP 3675. The upgrade consensus that we just talked about and that is scheduled on July 27th at 1400 UTC. They another one is going to be that, it's not a proposal specific, but a topic that people are looking to learn about that is blogcast limit with metallic beaut are in on July 30th at 1400 UTC. 
* We are also organizing one called for specific, a portal on upgrade that is scheduled on 2nd of August at 1400 UTC where we are. Inviting all the EIPs Earth is the climate change and the infrastructure implementers of those proposals of London. So please join it ethereumcatherders, thank you so much. 

**Tim**
* Any other final comments thoughts from anyone? Okay. Well, thank you very much and see you all in two weeks. Oh and upgrade your notes for London so and keep an eye out for the Ethereum Foundation blog post today or or Monday with the release versions. But yes London will be happening before the next Alcoredev F's. Thank you. Tim cool. Thank you. Thanks everyone. Thanks everyone. Bye. Thanks bot. Wow.

-------------------------------------------
## Attendees

* Tim
* Lukusz Rozmej
* YDXTY TS
* Lightclient
* William morriss
* Mikhail Kalinin
* Dusan Stanivukovic
* Gary Schulte 
* Trenton Van Epps
* Pooja | ECH
* MariusVanDer
* Ansgar Dietrichs
* Baptiste Marchand
* Martin Holst
* Jingwei
* Tomasz Stancxak
* Tyevlag
* Alex Stokes
* Crypto_Eren77
* Andrei Maiboroda
* Micah ZOltu
* Alenque
* Selvis
* Yanxi
* Charlie
* Kay
* Stag
* Thea
* Rai
* Danny
* Encryption wizard
* Artem Vorotnikov
---------------------------------------
