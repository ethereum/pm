# EIP-1559 Implemnters Call 7 Notes

### Meeting Date/Time: Thursday, Dec 3rd, 16:00 UTC

### Meeting Duration: 90 minutes

### [GitHub Agenda](https://github.com/ethereum/pm/issues/226)

### [Audio/Video of the meeting](https://youtu.be/dopljpI59Rw)

### [All Meetings](https://github.com/ethereum/pm/tree/master/Fee%20Market%20Meetings)

### [Next Meeting](https://github.com/ethereum/pm/issues/229)

### Moderator: Tim Beiko

### Notes: Griffin Ichiba Hotchkiss

---

# Summary

Generally this call reviewed several pieces of research relating to proofing 1559, specifically an economic analysis written, simulations about how mixed legacy/1559 transactions would behave in the same pool, and testing the changes against a network with accounts and state comparable to mainnet. Generally the feeling is that there is enough robust analysis and research with this improvement to begin discussing the next steps in the process, i.e. how to move forward introducing to allcoredevs and Ethereum mainnet. Exciting!

### Agenda


* Economic Analysis of EIP-1559 (0:00 - 29:00)
* Legacy Transaction Simulations (29:00 - 53:00)
* Transaction Pool Management and Sorting (53:00 - 1:15:00)
* Large State Testnets (1:15:00 - 1:24:00)
* EIP-2718 transaction type for EIP-1559 (1:24:00 - 1:27:00)
  * **Action Item**: Wait until 1559 is included into the geth codebase before reformatting 1559 txs as 2718-compatible (which will go into Berlin)
* Mainnet readiness checklist review



# Call Transcript

00:01
Tim Beiko:
Welcome everybody to 1559 implementers call number seven. Re have a bunch of things on the agenda. I tried to list them in order to go through them, so maybe we can we can just jump in

First item: Tim Roughgarden who's joining us today has put together a pretty extensive economic analysis of 1559, he published it I think two days ago so hopefully people have had time to to digest it since then but maybe Tim if you want to take a few minutes to just give a kind of short summary of the analysis and then if people have questions or comments we can we can go over those.

Tim Roughgarden: Sure, I'm happy to and thanks to the invitation to join the call.

00:54
I don't want to go on too long because I want to be driven more by people's questions but maybe just sort of I'll just quickly say kind of the structure of the report so after describing, you know, just recounting how 1559 works of giving a you know, fully precise, fully detailed definition of exactly how it works the report talks about how to think about a market of Ethereum transactions, so you know, EVM computation is a scarce resource and ultimately you know users or creators of transactions or vying for that skills resource so ultimately that's the point of the transaction fee mechanism to figure out who gets access to that resource and what the price is and sort of the purpose of that discussion around a few in the market for Ethereum transactions is primarily to clarify you know, what in 1559 can be expected and cannot be expected to accomplish with respect to the the level of transaction fees because I know there's a lot of concern in the community about high transaction fees.

And the main point I wanted to make there is just that you know you know when sort of demand for EVM computation outstrips its supply you're gonna have high transaction fees really doesn't matter what mechanism you use. 1559 does help with things like absorbing a short-term demand spikes and so as a result you should see low or maximum transaction fees, you know in periods of hyper demand but again when you have much more of a demand than supply no matter what the mechanism is, you're going to see persistently high transaction fees, so then with that out of the way then I start to analyze 1559.

02:34
In two ways so the most technical part of the report sections five and six that's really analyzing the incentives of 1559 at the time scale of a single block, okay, so thinking about say miners who only care about the revenue that they get from that one block and are not thinking about making short-term sacrifices to reap rewards later on. similarly users who are just focused on getting a transaction in the current block and they're just trying to figure out how to bid. and so sections five and six outline several game-theoretic guarantees that you might want to mechanism to have.

So miners should be incentivized to do what you would like them to do, users should be incentivized to you know bid in some sort of obvious optimal way and then also you'd like robustness to off-chain agreements so that users and miners can't easily collude for example to sort of basically steal money from the from the protocol.

So those are sections five and six sort of listing those three properties. first price auctions the status quo has two of those three properties, but 1559 has has all of them or at least almost. In particular the sections include a mathematical definition of what sort of easy fee estimation might mean or what is sort of good ux might mean and first price auctions do not satisfy that property and the 1559 mechanism does satisfy that property except during periods where the base fee is much too low, okay, which would signify that there's been a very rapid increase in demand where the base fee hasn't had a chance to to catch up yet. So those are five and six they're the most sort of technical sections in the report.

Section seven, I discuss, you know, a tax or manipulation should be worried about the take place over longer timescales. and So for this you're usually thinking of about a cartel of miners. because anyone or at least mining pools because any one miner is probably mining blocks sufficiently and frequently that you know long-term strategies are not useful, but if you have a well-coordinated mining pool, or if you have a cartel of miners with a large amount of hash rate, all of a sudden you start sort of worrying about what they might do if they strategize over time for example, you know, could they manipulate the base feed downward to reduce the fee burn.

04:45
And from what I can tell it seemed like this was the one that's generated the most kind of discussion on you know, say Twitter. Thus far so maybe I'm just sort of say why what I think was that what I was trying to say with this section, so the first goal was just to sort of revisit first-price auctions the status quo and asked the same question. right so like what could miners and principle do by colluding over a long time scales and what do they actually seem to do and so there you identified collusive strategies that would in fact be in miners interest if implemented them and then we observed that miners do not seem to actually do sustained long-term collusion. and You know I'm not a position the conclusively say why that is I just sort of listed a whole bunch of reasons that I thought of and the people told me about here are the reason why we might not see this kind of sustained collusion with first-price auctions and then I go to on to observe that you know that whole list of reasons that apply to first-price auctions apply equally well to the 1559 mechanism. So there do seem to be impediments to collusion by miners now under first-price auctions and you know, and nothing about 1559 makes it easier for miners to collude.


06:01
now 1559 may make miners more motivated to collude because now they sort of have you know this this additional incentive of evading the fee burn so the point of this section is just to say that in some sense the cost of colluding I don't see any reason why that would go down with 1559, it's as difficult as before. However, it is true the benefit may go up to miners who are pulling off the collusion. And I try to be very careful and report of not predicting whether we'll see significant amount of collusion or not and the final section of section seven, caveats, exclusively discusses this point, you know, that the miners maybe more motivated to collude than they have been before and so in particular there are maybe types of collusion we have not seen in the first price auctions which we will see not because they're easier to pull off but just because you know, they're motivated, they're more motivated motivated to do it.

Section 8 is something I thought would a generate a little more discussion than it has thus far so I think as the first part of Section 8 is just to clarify that you can't really do sort of the fee burn without the base fee or vice versa with an exception and so this is section 8.3, this is one of the two alternative designs I discussed in the report so the first alternative design is so it's really crucial for the game theory the role that the fee burn plays what's really important is to withhold base fee revenues from the miner of the block which generates those base fee revenues. So it has to be withheld from the miner who mines the block the simplest way to do that is with a fee burn, of course, there's lots of other reasons why people like a fee burn as well but section 8.3 points out that the game theoretic properties are really just as good as long as you pay those basically revenues to somebody else for example and this is a proposal I've seen by Vitalik and possibly others, for example, you could instead pay the base to be revenues to miners of future blocks, okay, so for example next thousand blocks you can spread it out equally. and then there's No fee burn basically just each block now is kind of a bonus added to its block reward depending on the sort of base fee revenues from the previous say thousand blocks so that's one of the main alternatives suggested which actually not seen discussed so far and then the other one is a version of the 1559 mechanism where instead of the tips being user specified you hard code them into the mechanism and this has some problems like you would expect sort of off-chain tip markets to emerge, you know, I get no opinion on whether that's a real deal.

08:33
Problem or not but you would expect that to happen on the other hand it's definitely simpler to have hard-coded tips and it has some nicer game-theoretic properties. So you know, it's just explaining that we get into the weeds but so there are some nice nice aspects of that second alternative design that I call the tipless mechanism in the support. And the last section of section 8 is I talk about the base of the update rule and this again, I sort of seen people coming up very reasonable request that this should be analyzed from a control theoretic perspective.

09:05
I totally agree. I think that's just probably quite easy. Control theory problem if you can find an expert but in that case you know arguably the most sort of arbitrary feeling aspect of the 1559 proposal is the specific way that the base view evolves over time, so the functional form all the choices are sort of natural you can see why one would make them or why they're a natural guess but the functional form is sort of arbitrary, you know, one plus an adjustment factor, you know, there's two magic numbers in the rule so the one eighth which controls how rapidly the base fee can and increase or decrease and then also this is questioning of this a magic number of exactly how much bigger should the maximum block size be compared to the to the target block size. So in that section Section 8.6 I try to clarify all of the assumptions that are baked into the current update rule and you know what are the different what are some different dimensions that you know, they should be experimented with over time.

09:58
And maybe, you know, maybe hard that iterate on the updated rule until there's actual data from a real deployment just from the armchair it's hard to have a compelling case of why something else would be better than the current one but I just wanted to you know, a heads up that probably this will want to be revisited over time like the various other parameters that revisited.

10:19
With every network upgrade And then in the last section 9 I talked a little bit about the other benefits of 1559 so the report focuses just on sort of good UX easy fee estimation, but of course there's lots of other reasons people are excited about 1559, so I just talked about what those are in section 9.1 most notably the fee burn but also kind of preventing economic abstraction.

10:39
I'm having a reliable measure of kind of the current gas price that's hard to manipulate for use in smart contracts and then the final section discusses the escalator both kind of a standalone proposal and also how that might be integrated into 1559. So that's sort of the executive summary of everything discussed in the report and obviously people have specific questions about parts of it I'm very happy to address those.

11:08
Tim B:
Thank you. Yeah, that was great. I'm anyone on the call have any questions thoughts.

fred:
I have a question which isn't necessarily something explored in the reports, but I'm quite curious about your intuition with regards to it. The question is do you have any thoughts on what you think would happen with if you have two parallel markets running during transitionary periods because one of the suggestions has been to have both the first option accepting those kind of transactions with 1559 in parallel and I'm curious if I might have an intuition about maybe some emergence effects that might happen or I don't know if this curious about your thoughts in it.

Tim R:
Yeah, it's a good that's good question. So just to clarify so this sort of transition plan, you know, I've seen this a few different things discussed. My understanding is that plan A is you would have a period, you know, where legacy transactions we can be converted or sort of interpreted automatically in the 1559 format by taking the gas price and interpreting it as sort of both the fee cap and the tip. is that is that the is that the specific proposal that you are that you're talking about?

12:26
fred:
That one as well, but there's another level to this which is... the pun wasn't intended but but when you talk about layer 2 systems. because many layer 2 systems that we see think about also having a free market running on top of the base layers fee market. So there's the transitional periods where you do this translation but also dual markets when you have second layer markets running on top of it.

12:48
Tim R:
I see so you're saying interactions between this change at layer one for it, you know versus what happens upstream.

fred:
But also inside the layer one itself. I guess these are two separate problems those are the two that I see

Tim R:
okay yeah yeah. I agree they're really they're separate things.

13:03
I mean, you know I the discussion I've just seen around I feel like some some some good thought have has gone into and discussion has gone into how to manage the transition, you know by the by the by the 1559 team and I have not seen you know, In some ways I mean I'm not I'm not in the trenches with the implementations where I can't comment on that but you know from what I've seen the the plans seems very reasonable, you know to have a to have a ... so and one minute is nice about it potentially one would hope so first of all people don't have to you know, wallets don't have to change initially if you have these sort of support for legacy transactions and then you would hope that there were the economic pressure over time for everyone to switch over to 1559 format right because there's really a basically two parameters to play with the tip and the feed cap 1559.

13:59
And if you don't bother to pay attention to that you're kind of stuck with as much sort of more restrictive way of bidding where you just set the one gas price so that's that's one thing that I think is nice about that transaction. I mean, so first of all, I mean seems clear you don't just want sort of a an immediate sort of hard stop with lazy transactions aren't accepted and so this seems like a really nice way to have them around for a while but the same time, you know, there is an economic incentive for them to to hopefully go away over time.

The later one / layer two interaction -- I mean, I I'd probably have to know more details about. You know I assume that happens in like you know various ways for various layer twos and it's I needed more no details to talk about it at length you know I will say you know I mentioned this briefly that one of the side benefits of having this base fee is it should make it easier to sort of know what is like the typical gas price at any given moment namely the base fee unless you're in a period of rapidly increasing demand whereas if you just kind of looked at ether scan right now and sort of look at a block and you kind of like well if I wanted to associate a single gas price with this block, what would it be?

15:04
I mean, you could use the minimum the average the median etc is the statistics. You could use but you know this worries about you know, those could be manipulated if people knew what statistic you were using. Whereas the base fee is hard to manipulate and again outside of sort of sharply increasing demand, you know should give you a reliable measure of this sort of current gas price so my hope would be that would be quite useful additional functionality or really an improvement for interactions with layer two down the line.

15:34
Rick Dudley:
So I think --Hi Tim --  I think the easy way to think of the layer two thing is you have the layer two chain generates blocks at a higher frequency than the layer one chain and it's using within its own domain the exact same algorithm so it takes a bunch of transactions it generates blocks it then publishes those blocks on L1 in an L1 transaction and that's basically all there is to it..

16:05
Micah:
I suspect what fred might be referring to is before the first version of 1559 we had Two transaction pools at the same time so within a single block it have basically half the gas was dedicated to 1559 transactions and half the gas dedicated to legacy transactions and so I suspect the question might have been what kind of interactions do you expect to see there? If we did that instead.

16:33
Tim R:
Interesting so would there be perverse incentives to you know,

Micah:
yeah because I it gets definitely more complicated for users to decide, you know, which is better for you do you want to do 1559 transactions or gamble with the legacy transactions or...

Tim R:
Correct me if I'm wrong but my sense was that this idea was set aside in favor of this kind of default interpretation of legacy transactions in part because that problem goes away is that right

Micah:
yeah that, and a couple of other ones as well.

Tim R:
so you know, I mean, it's not something I thought about deeply but you know the latest transition plans that I've seen to be seen like pretty smart approach.

17:27
Ansgar Dietrichs:
Are there any drawbacks with this automatic conversion?

17:34
Barnabe:
So I'll have some comments on this transition but perhaps Micah can if I'm pronouncing your name correctly so Micah wrote a notebook on the transition period between 1559 and legacy transactions and maybe you can share it now.

Tim B:
Just before we do that are there like other areas of questions that people had about the report because I think yeah the legacy conversion and whatnot is a whole other can of worms and like yeah, I think we can cover it right after but I just wanted to give this basic people have other other questions either wanted to bring up about the economic analysis first.

18:21
Tomasz:
So I have a question I think that's particularly well it's likely outside of the report but still very relevant so if we look only in the transaction market as something that exists by itself and the transaction values always external there's no other market to to relate to it's all fine but what if we have at this interest finance is market were miners can hedge the cost of of collusion like of the attack if they can actually benefit from the higher fee burning or the fees going down in particular, we actually work on the project were miners would be able to make financial transactions where they would benefit if the fees go higher or lower and if they can actually make big bets on these then they can cover the cost of the attempt. Did you consider this kind of correlated like a, A coexistence of two markets a decentralized finance market and the transaction fee market?

19:34
Tim R:
Yeah, it's not explicitly. I mean what you know, I find it quite interesting and in particular, I mean, I think where it ties into the report is the discussion around how to get miner buy-in into the proposal and you know, so you can argue, you know to what extent is it that necessary and then if you agree that it's necessary you can argue about how you might want to do it.

19:57
And so, you know, I think you know having some kind of, You know financial instruments so that you can argue that miners are going to win either way especially if it's something we're like they're in a particular particularly well positioned maybe to make smart bets on them, you know, you can imagine that sort of speeding up sort of adoption, you know, so lowering the you know, the the current sort of pushback that that I believe the community is seeing from miners.

20:30
Tomasz:
A great thank you.

20:35
Micah:
When you're analyzing the... Sorry which section I had a question and I just lost it someone else go!

Rick Dudley:
Yeah, I would just like to make a brief comment. I mean the the as the person who proposed the two-stage, you know, having two transaction types and two transaction pools the purpose of that was not game theoretic it was to force the removal of the dead code path of having one transaction type be interpreted two different ways.

21:16
fred:
There's also something else that maybe worth noting. I'll just press it over quickly which is you can see the layer two transaction fee market interacting a similar way to this first proposal of two transaction pools. because you can see it as part of the layer one gas being used and reserved for a separate transaction fee market.

21:40
So, I think the interactions in those might be comparable but not with this new transition period.

Rick:
Yeah, that's an interesting idea. I mean, that's a really interesting idea. I think that difference is is that the. well, I think there's two points and I'll be say the nicer one first the let's say you're using you know, the operator of the layer two whether that's a federation or an individual or whatever they ultimately have some discretion, right?

22:12
So they can they have within their protocol the ability to not participate in the next layer one block. So I so it is it is the segmentation but the, Two different pools are under different authorities. So that's a pretty big difference and then the sort of corollary to that is.

22:35
1559 doesn't stop the layer two operators from bribing miners, which is probably what they'd end up doing practically speaking.

22:58
Tim B:
There's one more question. I think you already kind of answered us Tim but Nick Johnson who's been one of the I guess friendliest critics of 1559 and really wanted to see a report he posted on Twitter yesterday. I'll share the actual tweet in the in the comments here and I'll try to just summarize his his question.

>https://twitter.com/nicksdjohnson/status/1334259190546632705

 Basically in section 7.4 or 7.5 you explain that miners could make these cartels but it hasn't happened before and he says, this is probably not a sound way to think about it.

23:33
And basically that the incentive structure is still the same under 1559 as it is now but it fails to consider the magnitude is very different today at Cartel benefits from the difference between monopoly monopoly pricing and market curing price but under 1559, it would benefit to the tune of the difference between the monopoly price and the cost price which is much larger.

23:59
Yeah so this I guess you mentioned earlier that the cost of collusion kind of stays the same but the benefit goes up I assumed that would be kind of the same answer here to Nick's concern

Tim R:
right so I started trying to be careful on this point in the report, maybe I mean, maybe there's a way I could have written it that I would have been clearer but I guess I would point to the very first sentences section 7.4 you just want to start classifying different types of collusion the very first sentence of the the section is, you know, I offer new prediction on whether there will be collusion under 1559 so okay if I don't wait so then what do I do?

24:33
I just say let's let's sort of make a Do an observational study of this status quo or first-price auctions, brainstorm possible reasons why we're not saying collusion and then assess to what it's you know, and then you know for each of these, you know, apparent impediments to collusion do any of those impediments break down because of something specific to 1559? And argue that no and in the top 10 take away is, you know, it's numbers five right so so so the the assertion is not the collusion is as unlikely under fifteen fifty nine.

25:09
First press options I didn't say that I'm very intentionally didn't say that I just said the impediments are as strong. I mean like problem is as difficult as far as I can tell for miners to collude under 1559 as it is now now. that doesn't again not saying that collusion is less likely for exactly the the reason the next mentions which is that they might see you either just because the economic reasons are more stake or they may feel betrayed, you know by the community and therefore sort of, you know, less altruistic and so that's that's covered in the section 7.6 I guess the caveat section and you know there again there's a sentence that says, you know the strong negative reaction.

25:56
I was referring to your your survey your question here by Tim this strong negative reaction make galvanize miners to sustain collusion to a group to a degree not yet seen on the status quo. So that's why I completely agree with Nick's point. I tried to make that explicit in the report perhaps it should have been positioned a little differently so it was more so it's sort of stood out more but I actually don't think there's any disagreement there.

26:21
Micah:
Cool, so let's. Get into the ocean. I was gonna ask what? She's and I can just talk about instead. I think the magnitude is off by a pretty large margin here, I believe because right now if miners were to 51 percent collude, they would make double the block reward plus wait plus transaction fees. With 1559 51 percent collude can still make double the block board and they get a little bit more transaction fees on top of that and while we have seen some big spikes in transaction fees periodically, the baseline is still way below the block reward and so.

27:03
It's like, you know, if you collude a 51 percent and you can make you know, a hundred million dollars or now with 1559 you include and make a hundred and one million dollars and it's like that I feel like that order magnitude is nowhere near enough to tip the scales just because like the games from colluding with.

27:24
For for colludin and manipulating 1559 transactions are just so small compared to colluding just with any type of transaction mining just by censoring 49% of miners you double your money, it's easy money right there, so if you have if you can collude you can make way more money to other things and so if that's where I feel like the real argument here should be is that the order of magnitude is just too small.

28:00
Tim R:
Okay yeah, sorry. I think you might well be right I guess I in the report I didn't want to presuppose how the base fee revenues would compare to the block reward. I just felt like

Micah:
that's fair enough and reasonable.

Tim R:
I thought any prediction I made on that point. I might just look quite foolish yeah a couple years from now sure and right so I guess number was the maybe that was the main thing.

28:25
I wanted to say, you know,

28:33
Tim B:
Any final questions for Tim?

28:40
Okay, yeah thanks a lot for for sharing all this this was pretty helpful and I'll make sure to think the report and the notes that we have for this call yeah and

Tim R:
and so we have to sign up but I mean sort of a general comment I mean, You know, this was not like some report I envisioned just like, you know issuing into the world and then you know never never never discussing with anybody so I'm gonna I'm really a report I made you know, the the point of it is to be helpful to be Ethereum community and so if there's just, you know, follow up questions or anything that would that would make it more helpful I'm obviously very receptive to that to that feedback and and future discussions, so.

29:22
Tim B:
And what's the best way baby for people who are watching the recording to reach out to you?

Tim R:
so email. Tim.Roughgarden at gmail. Great thank you very much, thanks everyone.

29:38
Tim B:
Michal, I hope I'm getting your name, right? Yeah, do you want to go into your report around the legacy transaction simulations?

Michał Komorowski:
Yeah, so um what I did so maybe to start with what was the goal of this report of this simulation? I wanted to ask the question how legacy transactions will be treated versus 1559 transactions by the network when 1559 is in use.

I wanted to ask what the question whether it may be the network will give preferential treatment to one type of transactions or other types, so I created the simulation that is based on the library EVM 1559 that's prepared by Barnabe, sorry if I also produce your name wrong.

30:41
I introduced some changes but I use it this library heavily. In my simulation I distinguish let's say three types of transactions, so or maybe three types of users. So we have the gas users that for some reasons don't use a 1559 and when this kind of users submit transactions and these transactions have gas premium or tip said to the same value as maxfee. Then we have 1559 users that utilize 1559. I decided to distinguish let's say naive users which always sets a gas premium to the same value one way so here this kind of users who do not analyze transaction pool to figure out what is the optimal the best value of gaspremium. and and we also have something I call 'clever' 1559 users that look at the transaction pool and try to figure out the gas premium they should use in order to be included in the block as soon as it is possible.

I forgot to say that legacy users also try to analyze transactions all in order to figure out the best gas price. And in each iteration of the  simulation, I generate the same number of transact of legacy transactions and transactions from naive users and transactions from this clever users and what what is important?

32:39
When we look. Not at the pairs but at the tree of transactions from each of these three kinds of users, they have the same value. I mean a business value a business value the user associates associated with given transaction. Why? Because I want to compare let's say apples with apples.

33:06
If I have in the and I think that if I have the transaction a poll one legacy transaction one regular transaction, one naive transactions with the same business value. Then I can I can compare compared them in the reasonable way. And after the conclusions and, Let's say the most important.

33:36
Okay, so firstly if you look I calculate a lot of statistics and metrics. So, I will only tell about the the basic ones but if we look at this statistics, we can distinguish phase one and phase two. By the phase one I mean situation when a base be very very quickly very dynamically grows and phase two when this base fee reaches stability stabilization.

34:06
So in this first, Phase all these statistics I calculate like average gas price per block, average waiting time, and and many different, they change very very dynamically and this is even quite difficult to to reason about this phase. Nonetheless this phase is quite quite sure quite short and then we have this as second phase when it is much easier to reason about the behavior of the network.

34:39
So according to my simulation and I think it is good information when the base reaches reaches stabilization transactions from all all these three types of users will be included in the in the blocks. So we don't have the situation but for example only legacy transactions are in blocks or only 1559 transactions are in the block.

However in this first stage when the basefee grows quickly here situation is is different because in this stage I observe that mainly or almost only this clever 1559 transactions are included in blocks.

35:41
It also means that almost only this 'clever'. 1559 users will take advantage from the lower values of the basefee. When it comes to the gas price here, let's say comparisons are are not super surprising. The naive 1559 users will pay the list why because they do not try to be clever they they simply always pay the same the same gas premium, whereas clever 1559 users or Legacy users who looks into transaction poll to who wants to pay.

36:26
More to be included in the blocks, they pay as slightly slightly slightly more but if we compare legacy users and 1559 the users, they more or less pay the same. Hmm what else? I implemented very simple transactions pool, so  I simply assume that I can have some maximum number of transactions in the transaction pool and when there's more more transactions, I simply removed from the transaction pool the worst. And what I mean by by the worst I order I sort transactions based on the gas premium they offer to the to the miner.

37:11
So and what is important? I observe evictions from the transaction pool almost only in this initial initial phase then when the basefee reaches stabilization there are no evictions and transaction transaction pool is not full. At all. Hmm. What else? One one more thing but is another concussion let's say that is quite let's say not around nothing surprising.

37:52
I also calculated average waiting time of the transaction in the transaction pool. So of course this naive 1559 transactions which always pay the same gas premium needs to wait more than legacy or clever clever 1559 transactions to be included in the block, however I spotted one interesting thing though.

38:23
I cannot explain that now what why it happened. Sometimes I observed that legacy transactions wait longer and sometimes I observed that this clever 1559 transactions waits longer in the transaction pool. I need to analyze it memory to explain what happened.

38:49
Okay, so I think that those were the most those were the bullet points the most important conclusions I noticed. If you have questions feel free to ask.

Barnabe:
Hey and I yeah, I really enjoyed the notebook we said if he was a really great use of the library actually and at the have been gotten like to play around a bit with it since we start over the week. So with Fred we've been looking at how to that's really look at oracles that give a like first price auction legacy users information about the current price that they should pay.

39:40
One piece of code but Fred added would be saved but users who are using selective we are after the transition we have 1559 users legacy users and legacy users are deciding their fees based on the oracles, which is also kind of what you are doing in your in your notebook and so when when you have these oracles like the presence of a base fee even though it's simply sit for the legacy users, it has a sort of stabilizing effect on the oracle, so let's say I have 50% of my users who are legacy and 50% of my users who are 1559, you can think of it as some of the users know the correct price (1559 users) and so since we know the correct price and that's the price we are putting in transactions, they actually tilting the oracles to our giving that price for the legacy users.

40:38
So I think of it as almost like a first price auction is with boiling pot of water and the 1559 new cells are just throwing cold water like lowering the temperature so allowing the legacy users to to almost like have a better let's say estimation of the current price and the market although it's a complete it's very implicit like it's not direct but it goes through the oracle and that makes plain also why by the end, when base fees stabilizing, you find that let's say legacy users in 1559 users are included in the block in almost equal proportion as we are when they join the market so yeah, I

think we we had in mind was that since legacy transaction users would be overpaying we would tend to maybe have some sort of priority but that's no longer true, let's say when basefee start to stabilize because when that happens, we are records will start to sort of align themselves with the basefee and provide to the legacy users being actual basefee.

41:49
So you should kind of expect this convergence. I don't know if it makes sense and if it's maybe something that you you noted as well.

Michal:
Yeah, I feel that my simulation there's not only confirm what you just said, maybe because one comment. What you said is that is totally true but if we only if we assume that this legacy legacy users will not overpay  too much because at least in my sim simulation yeah the gas users ask Oracle for the for the price but this Oracle returns the minimal the optimal the minimal price, however, if we have some legacy users who really want to pay a much more to be included in to be included in blocks then then probably even if basefee a stabilizes we'll see more legacy users in blocks.

43:00
Barnabe:
Yeah actually it's true but it I don't think it's true to the magnitude that we expect so for instance some most of your records are based on some kind of percentile of the past transactions, so you look at the that's in 95 percent top paying transaction and and you set the so like metamask when it gives you the "fast" price it's it's kind of like these very high percentile, but if you have like basically which is kind of stable and most of the transactions even some of the legacy users who are using the slow or medium who might be actually targeting the exact base fee it might.

43:35
Start even let's say tilt the fast oracle, so the one that would make you over pay towards the base fee itself again. because it's sort of a distribution thing where because the fee variance is reduced in the block thanks to the basefee you also have this effect that propagates to the to your oracle itself unless your record is some sort of fixed let's say I make you over pay by five gwei but I think most of oracles are based on this idea of looking at the distribution of transactions and setting the price at least.

44:12
Michal:
Okay, so maybe one more one more thing because it seems to me that's when we see this stabilizing stabilization effect only if we have a big enough number of 1559 users users using the network so here, of course, it's only a guessing the question is how it will look a in practice if we have let's say 89% of legacy the users and only 10% of 1559 users.

44:48
I think that it wouldn't look so nice when we had 50% of legacy users and 50% of 1559 users.

Rick Dudley:
Sorry I'd just like to comment on that yeah. I think that's an extremely good point and I think to me, I mean, I really appreciate all this research and I think it's really interesting fascinating work.

45:13
As a practical matter if collectively the community can do something to ensure that 1559 gets adopted by someone like say Metamask then we a lot of this simulation we don't really have to worry about these corner cases right we just know that the majority of people will use 1559.

45:36
Tim B:
Well I think I was just gonna add I think we had a bunch of discussions about this in the past as well, but like we can start with this, you know neutral approach of like reaching out the folks there is already I think a lot of support for 1559 in the community so you know step one is like you reach out the folks like metamask like, you know coinbase or whatnot ask them to support this and then instead do is like if that doesn't work in the next hard fork, do you want to add like a carrot or a stick right which regards to gas prices or?

46:11
Whatnot, but I think it's yeah it's it's hard to predict in advance what the adoption rate will be and therefore to come up with like a good a good plan for like how do you get the people who you would have wanted to adopt it that are not adopting it to actually do so.

46:31
Ansgar:
And so I do think that they are safe stabilizing incentives in the sense that the less stable the base fee behaves just because few people have adopted 1559 so far the more incentive there is to actually adopt like move to 1559 transactions as an individual user just because like again with legacy you may tend to overpay or just general it's it's less controlable. and so basically like the the few people are using 1559 the more like attractive is for individuals to move over to the profit from the like increased stability locally and so I would assume that it very quickly kind of would converge to a situation where enough people moved over that the overall situation becomes relatively stable at least on the most .

Tim B:
That's a really good point and I think what's interesting is a lot of the projects we spoke to as part of the outreach that were managing transactions on the behalf of the users really care about giving their users the best price in the best UX so if there is kind of an incentive to do so I suspect we'll see, you know, a lot of projects wanting to differentiate by adding that yeah.

Barnabe:
Another consequence with this inside that we are records converge is that the more 1559 users you have the easier it is for legacy users to keep using legacy transactions. The less they would over pay because the oracles would kind of tend to become so... bouncing on what Rick said if you get the 80% users by having metamask switch to 1559, then this long tail of users who are not switching it's actually not that bad for them they get somewhat correct rate still you have like, of course, it's kind of a gradient.

48:19
Between if everybody is using first price auction versus everybody is using 1559, but yeah most users are 1559 years old when I guess from a legacy user of perspective, you might not be able to think that much either.

Tim B:
And that's not like the end of the world right like the the direction we're going to over going in at the protocol right now is like if we have support for these 2930 transaction these 1559 transactions the legacy transactions.

48:47
I suspect will have to carry a bunch of different transaction types for a while, so I don't think so. I'm I think there's maybe a more meta discussion about like how do we deal with this long tail of like older transaction versions that's kind of out of scope for p1559 and if we have some reasonable, you know intuitions that there are good incentives for a large portion of the network to adopt it.

49:13
I think that's probably sufficient given yeah that we still have to maintain some types of legacy transactions anyways due to other reasons.

Ansgar:
That actually leads me to a question I was having earlier so in case that the transition like the initial the transition to 1559 goes smoothly and the experience a lot of adoption early on and a lot of people earlier basically talked about transition periods that would imply that there's like some end of the period where then the presumably you would completely phase out legacy transactions and you've basically just saying that that that might not be like a necessary at least like immediately or something. I was wondering if they even is there any like important reason why you would ever want to phase  out legacy transactions instead of just continuously converting them forever?

because I mean, they're always edge cases maybe someone is yeah, it's a hardware wallet where they really don't have a way of generation types, or something.

Tim B:
The short answer is client code complexity and and the way I guess the scenario under which it would be very helpful is if you have clients that don't want this thing for just from Genesis for a reason. So you know, some people have talked about like regenesis things like that, but maybe a more possible or concrete thing is like assume there's the Eth1/Eth2 merger... right maybe people want to write clients to be like an eth one engine for Eth2 but not sync everything since if one's genesis just like start processing stuff at the merge block them if you got to a point there, we're say, I don't know legacy transactions are not supported anymore, they just don't have to implement that and it makes the client much easier to do that so.

50:57
I think that's the main argument in favor but when you talk with teams like geth or you know, other trying teams that need to support clients from Genesis, it doesn't really make a big difference that you know say to us on base we deprecate 1559 transactions or not because we still need to validate all the blocks where there were like legacy transactions, so that means we need to keep that code in the client as well. I think yeah, the biggest benefit is you could build a client from the spot where you don't process those transactions anymore.

Rick:
Yeah, I mean, so. At the time my thinking was that there would just be a potentially a lot of complex dynamics by keeping this old by having two transaction types that are possible and is I just thought it was really difficult to reason about I was having a very difficult time figuring out which one you know, what would happen and so it's better to just like close that that door both from like an engineering perspective but as as Tim points out that kind of doesn't work because you have to replay from Genesis but then also to sort of close that door in terms of like, you know, the economic exploitation.

52:15
Micah:
One could also a client that has so for each time there's a fork block the consensus rules change one can imagine a client architecture where you have a separate engine for each. Fork and so it'd be nice if your new engines don't have to speak but you don't touch them it's like, you know your version one you don't touch it you maybe get security updates but that's it. Whereas you don't want it to your v1 code sitting in your v7 code code base which may be completely isolated again depend on your architecture.

52:49
Tim B:
I suspected practice they'll give it the current clients that existed he was working out them nothing like that will happen before Eth1/Eth2 merge yeah. I happy to be proven wrong but yeah my hunch is this is the only kind of point at which it makes sense to change the architecture so much to to get there.

53:13
This is a bit of a tangent, though. Yeah people have any other questions about the legacy transaction simulations?

53:26
If not yeah Ansgar. I think you had some updates you want to share about the transaction for management, which we spent a bunch of time talking on talking about on the last call.

Ansgar:
Sure yeah and so so this is just for context I haven't been following so I've been following the one the 1559 efforts like loosely but by not I haven't like joined most of the previous implementers call and everything so so I'm I might not be fully up to speed but I'm basically like I talked to Tim and the Quilt team and we talked like a I think two weeks ago something and mentioned this kind of that there were some open implementation questions around mempool handling and so we kind of decided to look into that a little bit and so I basically wrote up some of my thoughts around specifically the sort because I think.

54:14
Most of the mempool related questions like how to handle what 1559 transactions differently from exiting transactions really boil down to to to sorting. And so some my like basically initial conclusions and again those this could be off. I'm not I would definitely not yet an expert I think but it appears to me that there's really basically two different types of sorting that usually happens in mempools the first one is just for miners that's like basically of on the high end of transactions.

54:44
basically choosing if you're having an efficient way of finding the currently highest paying transactions and of course highest paying meaning like at those that that basically at the highest effective tip. And in currently, of course, you just use bigger the gas price for that. And so currently for example in in in geth the way that's implemented is with like a max heap where you basically have like a partially sorted list but by maximum gas price and you just traverse that to find the highest paying transactions.

55:14
And that doesn't quite work for 1559 because unfortunately, like, of course, I had this little diagrams or Whatever of course I would observation I think this is an old one that with 1559 the relative order of transaction can can change from the base fee changes because of this these two parameters so sometimes so basically like if for low base fees usually transactions under static period where they basically pay their maximum tip that they they're willing to pay but then at some point they reach this this kind of inflection point where the base fee becomes so high that they that it's that eating into the tip, they are still willing to pay so and so for different transactions that point is at different locations and so when it can be that that that was, Willing to pay to have to pay to pay a higher tip that that now goes down and now basically all of a sudden this is willing to pay less than another transaction.

56:06
And so so the read order can switch and so you can't have like a static and sorted data structure anymore and however, like. I think specifically for for the for the question of mining it seems to me that you can become kind of finding somewhat more clever but not all that much more complex way of going about it.

56:27
So, so there are the main observation that I had was basically that within this kind of what I'm called calling static state where like you're you are able to pay your full tip right and transactions that are all currently willing to pay their full tip those those continue to have a static order because while they are in this static range, of course, that's a static amount.

56:45
So that's a that's a that the ordering stays constant and then within the declining phase where your tip is being eaten into by the base fee, transactions within that also because it's like a linear one-to-one relationship like the one more gwei in the basefee is one less gwei in your tip, and so that also basically means that they're all shift in the same speed and so so they never intersect so transactions in that state also never kind of switch order.

57:09
And so it's really just about transactions where they're basically switch between those two to two states. And so I think what you can do is basically just have can have like a ones partially sorted heap for for the static notations one for the for the dynamic transactions, they have few questions over there that I haven't really that don't I don't think I've quite the answer yet so basically what you'd have to do every time you block comes in the chain space for you to kind of process the ones that that that now passed their inflection point there and you know switch between the two states and it's not quite clear you could if effectively remove them from because you you don't actually want to to do a lot of removal from this heap, so there are few intricacies but I think generally directionally this is like a really solvable problem.

And then and the interestingly though like the other sorting problem in mempool is on the other side right not the high paying transactions, and that's only for a miner problem, but Like for eviction right? and then there you need you you want to find the the the basically bottom tier transactions to to get rid of.

and this is like seems to me to be a little bit more complicated because another legacy transactions you again just use the gas price but what you kind of optimizing for is you want to get rid of the transactions that have the lowest chance of being included right because those are the ones you you you want to drop. and previously with the like static order and everything that is a very simple decision to make you just look at the gas price now with 1559 again with like the the the dynamic order they can shift over time it's not clear anymore right just because the transaction right now would be willing to would have like a lower effective tip then another one doesn't mean that it has like a lower chance of inclusion because maybe as soon as the best base fee goes a little bit higher than the transaction is all of the sudden is willing to pay more or something so so you kind of have to have it like as implicit assumptions about basically behaviors so basically what you the the metric you would want to use is like the like the the average tip that that you expect like.

59:12
Expected expected value of of the effective tip that of the transaction over like all over like a probability distribution of future base fees, and of course, you don't want to do it all the complicated so questions just can you find like a simple heuristic that that that does something of that sort that is good enough?

59:34
I mean, for eviction you don't really care if it's like a intellectually completely perfect solution, it really just has to be practically enough but has to be practical enough. I'm not like a lot of different paradigms so so slowly changing base fee high like quickly. Quickly increasing what quickly falling highly and volatile low volatility all these different paradigms so basically the goal just this fine find it heuristic that is like really robust and all these paradigms but then also you can implement with some efficient data structure where you don't like not you what you don't want to do is basically every single time of new block comes in you don't want to go through your whole mempool recalculate this effect this is expected value for every single transaction and completely restart your mempool that is too much.

1:00:16
I think at least that is too much housekeeping effort after every single block and so basically finding some. Heuristic that you can you can find some order that you only have to update every single block or something I don't know I I have like I don't really have good like concrete ideas around that yet I think it's it seems like that should also be kind of solvable though, but it's it's a little bit more complex issue so so that these are basically like my my thoughts on sorting so this may be one more special case of like transactional replacement, but I think transaction replacement really is not all that complex because they are you really only wanted to be predictable by the user because transactional placement where you just replace a transaction or pending transaction because it's you want.

1:00:57
To bump it basically I think you can just have very simple rules that protect you against DOS and issues but also kind of keep this this the structure something but but yeah basically so so I don't know maybe I'm sure if it was clear something and then again, I might have been missing things or just previous write-ups or whatever on that topic but that's my rough outline so like high-end for miners low and for eviction for all notes and high-end you want an explicit solution low end just some heuristic that's good enough that's kind of where I'm at right now.

1:01:30
Rick:
I like that analysis thanks a lot. I just I do have one question which maybe I also not being an every meeting missed something but when you're talking about evicting transactions, isn't there a velocity like isn't there a maximum rate of change of the base fee such that you could say like it would be a week before this transaction could be included or a day or there's some longer bound where you know that the velocity of base fee changes.

1:02:05
Would certainly exclude a transaction from a reasonable amount of time.

Micah:
Yes there there is I personally advocate for using strategy like that the caveat yeah we have to remember though is that in a time of rapidly increasing base fee it is possible to see the transaction pool filled entirely with transactions that meet that criteria so even if you say that evict any transaction that cannot be included in the next block it is still possible to have a transaction pool that is entirely filled with transactions that meet that criteria and you still need to evict.

1:02:45
So you still need a secondary eviction strategy in that case to deal with that situation, at least.

Ansgar:
Yeah so it would agree that basically like a simple yes no rule always runs into these edge cases where you can construct a situation where it's basically very close, but just you're still just below whatever base fee they need or something and so some some just some some some relative metric we have like one value per transaction they can assign and then just compare and and and they and and pick those with with the lowest value.

1:03:17
I think I think that is preferable but I do think that it illustrates how while there is like again, there's some uncertainty when The transaction order can flip they're still a lot of structure in that like it can only flip to limited extent because the base fee can only change at a certain rate and all of these things so I think you still have you can still come up with sorting that is mostly stable but the kind of when the basefee starts to change it it only changes a little bit and so you you can you basically only have to to do a little bit of kind of updating or of your sorting there. but yeah, the goal really should just be to be able to to to identify the the transactions no matter like how close they are to being includable or how how far away.

1:04:02
Micah:
So another thing that like client brought up. Last week early before is that if we can get. If we change the the miner bride. Or tip or whatever wanted to call it this week to be static not dynamic that I'm willing to pay this much base fee up to this much-based fee and I'm willing to pay this much to the miner and those two are separate values and so you totally pay as the sum of the base fee plus the miner.

1:04:34
That greatly simplifies the transaction sorting problem, but it introduces a new problem that it greatly increase the complexity of upgrading legacy transactions to this new transaction type. So if when people are thinking about this problem, if you can solve that problem the upgrade how do we upgrade legacy transactions when the tip or the miner bribe or gas premium whatever you call it is static then this whole problem of transaction sorting goes away and we're back to basically legacy style very simple sort.

1:05:08
Ansgar:
I do have to say though um because Tim and I we talked about that um quite a bit after that and the impression that I got and of course if it could throw the correct me there but the impression that I got there that is not indeed actually correct because it turns out you still you because like for with this decisions you still want to do this kind of fix like the the chance of inclusion or something and just because now it's a cliff so basically you have a hard drop off that still kind of gives you the property that there's like a non-static order, but it is because because there can be transaction that is like more easy in order that it's basically higher paying for a long time and then it just instead of gradually dropping off it just immediately drops drops off to like a inclusion chance of zero basically but but it still has this this property that you cannot enter into intersections between the the kind of the relative value of two transactions and so it's not in fact that it now all of a sudden basically it's a static order again.

1:06:08
You still have the property that that is the order or it's dynamic and flips. And so you kind of have to do this expected value of things. So, I personally don't actually think that this is, That that this is basically gets rid of the problem.

Rai:
Micah you were saying that the problem of promoting the legacy transaction types under that suggestion that you had is because there's now just this static fee that does it there's no basically item that depends on a per gas basis, right?

1:06:54
Micah:
It just doesn't fit with the model we have for upgrades. So for upgrades the model we have right now, of course is we just say the legacy transaction gas price is both the fee cap and the miner bribe. Both values the same thing and everything kind of just works out magically. If they are seperate so they're additive onto each other so they the thing you pay is now basically plus miner arrive we can no longer just set the fee cap and the miner bribe to the legacy transactions gas price that doesn't work out forgotten, but.

1:07:42
Ansgar:
I would also idea that it the one other major problem that that solution has and is basically that you have this just like the the behavior again of like basically your transaction is willing to pay a certain tip and then as soon as what under like the dynamic approach basically usually you would have this this inflection point and then you the tip you're willing to pay slowly be great but you can still be included in the block whereas under the new proposal basically you could at that point you could just not long no longer be included and so from you like from a UX point of view. I think it is also a little bit problematic that now you could have transactions that are like like price-wise perfectly able to get included but they can't because of this this rule so. So sorry, so I'm personally a little bit skeptical of this approach.

But it is like a very interesting like it alternative approach to think about because I think I think if I remember correctly that was exceed the one that kind of when when lightclient and I were talking about it is it's that was the one that kind of led us to realize that and basically within these different stages I used to have the the the static order so so let me like a very interesting kind of thought experiment but it I don't personally like it as an actual design.

1:09:24
Tim B:
And so just so I understand it seems like the next step here on the eviction side is finding is there a good enough heuristic that we could use which might have some failure modes, but that should should work most of the times that right.

Ansgar:
Yeah that that's how I would at least see it.

1:09:44
Micah:
I think the most important thing is that we do not have a failure mode that results in a DOS factor against for the addiction strategy pretty much anything else is almost anything else is optional that being said there are like if you are the worst case eviction strategy as you're evicting from the the most likely transactions to be included right it's like the pathological failure mode.

1:10:09
If you imagine that then that can become a DOS vector because now clients are constantly dropping transactions that then they'd have to get fetch again as soon as they get included in the next block and so we do have to be careful about that but that's really the core is don't allow big DOS attacks.

1:10:28
Rai:
Is any of those get easier to solve I remember hearing forgive me because it's my first 1559 call but I remember hearing rumblings about potentially enforcing at the protocol level that blocks are filled first of EIP 1559 transactions does that solve any of this because you only have to relatively order them like only order 1559 transactions among themselves and then legacy among themselves.

1:10:57

Ansgar:
I'm not sure the the problem is that even within 1559 transactions if you don't don't like have any of these of these legacy converted transactions in there. I think within that block you still have similar issues, at least maybe it's easier when like most of the tip is some some wouldn't like a similar range or something but I think so like of course for the legacy side of things it would make things easier because then you have the same properties again, but I down and I don't see at least why that would solve the the issue on the 1559 side, maybe we'll make it all easier I'm not sure.

1:11:43
Rai:
So what if you add also the static miner fee instead of the per gas miner fee and now can you determine basically sort those the 1559 pool.

1:11:57
Micah:
You're saying have two transaction pools one that is legacy transactions that are that once they're included in a block they look like1559 transactions, but the second pool is actual 1559 transactions. But they have the static gas premium?

1:12:21
Rai:
I was suggesting that we have the 1559 transactions with you know, the fixed the fixed tip and then you we just have legacy transactions as they always were in a different transaction pool, except they can only be included in a block after 1559 transaction.

1:12:46
So they can only fill up empty space basically yeah and so there and so they're like, you can affect them, however you want if there's or you can have a gall them if there's only 15 59 transactions. And then the 1559s transactions as they are now also would have this sorting problem.

1:13:03
I think because of the per gas

Micah:
so I don't know we can have you have the elastic. I don't know if we can have them be 11, that's second pool be elastic because we don't know if we should. (Micah breaks up)

Rick:
Yeah, I think you was an effect just expands the block one block late and I think um expanding the, I think having the 1559 take up all of the block and then have the original transaction type take up the remainder and then if that was full, expand the block that I think is a really weird game where it makes sense to like do all sorts of weird stuffing and price manipulation because now you can control the size of the block in this kind of counterintuitive way it I don't know that that all of all those games are worth the algorithm benefit that you're aiming for.

Rai:
Okay cool yeah. I just remember hearing this is a suggestion but I never heard kind of the counter argument to why it wouldn't work but that makes sense.

1:14:44
Tim B:
I'm yeah, just because we're running low on time and we still have a couple other things to cover is there anything else regarding this that people really wanted to bring about?

1:14:58
Okay, if not I think yeah the last big thing we had is Abdel with some progress on generating testnets with a large state. Abdel you want to take a few minutes to kind of share that?

Abdel:
Yes sure so we want to see how the network would work with the high block elasticity like can network handle twice the block size as now and to that the first approach was to kind of fork mainnet, but we don't really like this approach because it implies to do some tricky things in the code of the ethereum clients and we don't want to merge that code because we don't want to introduce new attack vectors.

So we wanted to explore another approach which is to have basically to not touch at all ethereum clients and to have another standalone service that interacts with the clients and to see how could quickly we could generate a state comparable to main net. So we implemented the proof of concept for this service, so I will show you.

1:16:17
So, can you see my screen? Yeah. Yes, okay. So basically, we have a standalone service that will interact with the Ethereum client using the RPC endpoint and we have a few rest API so basically API to understand because it is all long-running processes so we need a way to on the client side see if the test is completed and the duration of the time of the task etc.

1:16:46
And then basically, we only require to have two deployed smart contracts. So one to create accounts and one to fill the storage basically.

So the first version we were to create account we were only doing basic transfers so without using a smart contract but it's required to handle a large TPS and this is more efficient to to create a bunch of accounts per transaction.

1:17:23
So this is why we create the account directly in the smart contract. And also, you can monitor the number of accounts created. And also yeah, we have the other contract that is always possible to fill the state storage. And yeah, basically, I will show you a quick demo. So first I start 1 ethereum client with very low difficulty.

1:17:53
To quickly produce blocks. Ok, and then I start my standalone service that has the RPC endpoint of my Ethereum client. And we have web application. So, Yeah basically it connects to the Ethereum client and retrieves some configuration parameter. So for the moment, I don't have anything deployed because I just deployed the network from scratch.

1:18:26
So the first thing will be to deploy the two contracts required.

1:18:35
Okay the second one. And now if I go to the configuration, I can see the addresses of the deployed contract and some parameters directly queried from the smart contract, so I have not created anything from the moment. So we start let's say by created 10,000 accounts. And 15,000 entries in this smart contract.

1:19:04
Okay, so tasks are pending. Let's wait a few seconds. Okay, account creation is done. And the state storage is done as well. And if I care again, like smart contract I can see that 10,000 accounts have been created and 15,000 entries have been created in the smart contract and I also have the address the last created address.

1:19:35
And to show you some results. So basically, we tried several iterations, we started from 10K accounts and 10K entries in the smart contract and between each iteration we multiplied by 10 and we have measured the time we needed to build the states. And so the last iteration was 100 million.

1:20:01
So this is something comparable to main net. And it took basically four days to to build this large state. So the the two processes have been done sequentially. The next step will be to try that in parallel. And obviously, we did some test with the single node network. And if the approache seems reasonable for you guys one next step will be to set up a new in 1559 testnet and to kind of build a large state comparable to main net and I think so we'll have to deploy multiple clients on each type (besu, nethermind, geth) and I think we should try to run this service on or clients directly or as an building the state and then think with the other clients that will be more efficient to make sure we all deploy our clients to the infrastructure and then we start to generate the state and with hopefully within four days also we could be able to have something comparable to main net and then we could start to play with the high block elasticity because we did some tests with the high block elasticity on the current testnet, but, The state is very small so we don't see the impact on the large state and we started to measure the evolution of the block production time versus the number of accounts.

1:21:39
So it does have a significant impact actually so it will be interesting to see how it will work with a large block elasticity. And yeah, that's pretty much it.

1:21:57
Rick:
That's really impressive. I just have a quick question after you've generated that spent the four days to compute that state let's see it. I'm sorry it doesn't seem to say the size.

1:22:23
237 gigs. But does it make sense to create a backup of that for the respective clients so you can run more tests or do you just want to destroy it?

Abdel:
My plan was to destroy it and regenerate something from scratch using the tool. Because the time needed is quite generally reasonable.

1:22:45
I guess we're less than a week is. I don't know.

Tim B:
And these didn't use 1559 transactions No right Yeah exactly So we should probably have wow. Yeah. Yeah. Yeah, I think we just did it with yeah Legacy, but we should probably have I agree with you Rick that like once we do it with 1559 style transactions we should keep that and not have everybody else need to run a four-day process every time.

Abdel:
It does not really matter. I mean to fill the network we do need to use 1559 transactions because most of the work is done in the smart contract anyway, so that won't affect the results.

1:23:22
Tim B:
Yeah, oh I get yeah. What we want is we want the net. Work once we have the large state we want to whatever network to be able. Yeah. So it is Yeah. Okay, we could use that. Yeah, put that in like a set of clients that support 1559 and then run the transaction generator pool, right?

1:23:42
Yeah, okay. So I guess in that case, we probably should not delete it now.

Abdel:
Okay, okay. So yeah, first I wanted to see if the approach makes sense for you and then we can see the next steps.

1:24:01
Tomasz:
So this is this to check if the, Clients can handle the the low to the level of the main net right?

Abdel:
Yeah, yeah, so with the yeah this week twice the block size of the main net. Yeah.

Tomasz:
So you to generate like 100 million accounts because main net is 100 million accounts and accounts.

1:24:29
Tim B:
Yeah. And then there's also a smart contract, which has a hundred million stores slots. Yeah with 20 bytes per slots. Yeah.

1:24:43
Tim B:
I'm we're almost out of time. I know Rai you had you wanted to bring up 2718, do you think you can do that then like one minute or two?

Rai:
Yeah, I think if someone has arguments against it then we won't and it'll go somewhere else but I'm hoping that it will just push through quickly.

1:25:01
So essentially since the writings on the wall 2718 is gonna be in Berlin and the whole point is to introduce transaction types is everyone good with having EIP 1559 transactions be a 2718 transaction and we can just. You know temporarily pick a value of like 15 for it and then pick a what's it called like an incremental value on the fact you about to go into a hard fork.

1:25:34
Tim B:
How much hot like does it slow down people right now to add 2718 support or or not because we're already doing as part of Berlin, right?

Rai:
Yeah, I was gonna say that I think all the clients have it now and so it would actually just simplify the encoding decoding code paths to just have that be a type.

1:26:00
Abdel:
Ramil can you say yes if you have merged the master branch because I think the I'm not sure the emerge the master branch

Ramil:
Yeah so actually we almost completed so we just need a couple of more hours today we are going to create pull requests on the original geth repo

Abdel:
and would you be confident to use 2718 type transaction envelope for 1559 transaction, have you. Looked at it or.

Ramil:
No not yet so we are based on top of master so that transaction type request is not merged yet right?

Tim B:
okay, so maybe it makes sense yet to wait until it's part of the geth code base like it's actually merged into geth I don't know what the status is and and then set a transaction type and I assume we can kind of figure out async what we want the transaction number to be.

1:27:00
Yeah because I guess I wouldn't want to slow down the stuff on like the large state test net if like it'll take a while to get it merged in geth and get and and then be yeah, then we need to update the 1559 implementation of Gath and whatnot does that make sense?

Rai:
sure make sense once geth goes in then we can switch it to 2718, yeah

Tim B:
and I guess we're we're kind of out of time but the final thing I wanted to see is like when does it make sense to have a follow up call it feels like we have a lot of like parallel threads?

1:27:35
So should we have like, you know breakout rooms for any of them does it make sense to just have maybe a call in two weeks instead of a month so that we can follow up async and and kind of share updates in two weeks what if you feel will be like the most productive?

1:27:51
Tomasz:
I think I think generally we should actually start planning the road to roads to test nets and to release like so we should actually transition to the stage when we plan how to how to move it to main net instead of just analyzing it anymore, it's like overwhelming proof lots of different research cases that show that it's very solid.

1:28:16
I'm not probably like this this few slightly risky points that were mentioned in yeah in the recent report but apart from that it would be great to start. Planning how to go to main that all the way I still have the roadmap what's the first target date that we have for the release and how we get there when the clients join what are the acceptance points like ours from our perspective from all the clients when we say okay, we are ready and that will be great.

1:28:48
Tim:
Yeah, I agree with you it seems to me like from a research side it's pretty de-risked the only two outstanding issues seem to be figuring out this transaction pool sorting which is not the you know, it's not rocket science, it just has to be done... and then maybe looking at the update rule but that's also pretty minor I think with regards to all core devs wailing until like Berlin is out or at least, you know, kind of finalized probably makes sense before bringing it up there.

1:29:17
So, maybe I can definitely work on putting together a roadmap over the next two weeks. Maybe it just makes sense. Yeah, the follow-up then to see how the work on the testnets is progressing and if we have a solution for the for the transaction pool stuff and then how do we want to bring it to all core devs basically after the holidays?

1:29:39
Tomasz:
Yeah generally thing that we we should totally decouple it from the Berlin conversation will be much much better working group because I still make this bet that is like 10% chance that this will happen before Berlin.

Ansgar:
One last maybe a little aspect that I wanted to mention is I think it might also make sense to start talking a little bit about like general timeline for for like Ethereum mainnet because I think like starting maybe a year from now or something there'll be like a lot of these big changes with like the merge and maybe statelessness and so on and yeah get like some feeling right because I would really hope that one of my might might be able to just go in maybe like summer / autumn or something so so that then we can stay clear of all of those because otherwise it might be a little over.

1:30:30
A year additionally just because why oh yeah higher probably things

Tim B:
I agree that was always my goal is to get 1559 ship before stateless because otherwise having the two kind of come in at the same time is is is pretty bad, um, yeah,

Ansgar:
but then now also with the accelerated merge timeline that might also Yeah, yeah.

1:30:46
Tim B:
I agree. So, I guess yes sorry we're already a bit over time. This are people fine having another call in two weeks and doing stuff async until then and using that call maybe to do a bit more of the planning. At least I can share of first driving the planning of like what I think makes sense to bring to all core devs and and we can also follow up on the various kind of transaction pool and and other issues.

1:31:14
Okay. I'll think I'll take this as a yes. Thanks a lot everybody this this was great. I'll try to upload it to YouTube later today. Thanks bye. Thank you. Thank you everyone so.


### Attendees

- Tim Beiko
- Tim Roughgarden
- Michał Komorowski
- Abdulhamid Bakhta
- Baranbe Monnot
- Micah Zoltu
- Ramil Amerzyanov
- Rai Sur
- Rick Dudley
- Tomasz

### Next Meeting

TBD
