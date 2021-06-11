
# EIP-1559 Gas API Call (Breakout #10)

### Friday, June 4, 2021 at 14:00 UTC (10:00 ET)
### Meeting Duration: 60 minutes
### [GitHub Agenda](https://github.com/ethereum/pm/issues/328)
### [Audio/Video of the meeting](https://youtu.be/SpU6WACP2cM)
### Moderator: Tim Beiko
### Notes: Santhosh(Alen)

# Agenda
- Presentation by Gas API providers
- JSON RPC endpoint for gas price
  - Addition of eth_maxPriorityFeePerGas [ethereum/eth1.0-specs#201](https://github.com/ethereum/eth1.0-specs/pull/201)
  - Need to agree on return value
- JSON RPC endpoint for next block baseFeePerGas [ethereum/eth1.0-specs#207](https://github.com/ethereum/eth1.0-specs/issues/207)
- Open Discussion

⭐ [Cheatsheet: 1559 for Wallets and Users](https://hackmd.io/4YVYKxxvRZGDto7aq7rVkg?view)⭐

# Intro
**Speaker 01**
* Yes, we're recording, and thanks for joining us. This is a call to discuss the gas API and how 1559 affects it, and if we have time, we can go over any other questions or concerns that people here have. 
* So Trenton already shared the agenda in the chat here,  basically the main I think topic or yeah the main topic of discussion today is you know what do we do to return the priority fee in the json rpc api there was already some discussion about that on the issue and um before that though, I think Trenton put the presentation by gas api providers in the agenda.
* I'm not sure if there are any people here that have prototyped or looked at what a gas price oracle may look like after 1559, but if anyone wants to share that, it's typically a good idea to start by looking at something. Otherwise, we can get right into the api.

**Speaker 02**
* I see some etherscan folks here, but if anyone else wants to step in, go ahead. Whoever was just speaking, feel free to speak.

**Speaker 03**
* Yeah, I'm from the get team, and well,  I can talk about what we have as a guest fee record, if someone isn't familiar with it before or if it's already known to everyone.

**Speaker 01**
* I think it would be pretty bad, like it was at least valuable for me yesterday and the day before to understand it better, so yeah, I think walking through what you have now and how it's changing under fifteen pieces, and I know you and Peter posted some comments as well, but just to make sure we're all on the same page.

**Speaker 03**
* Okay, so I won't go into too much detail, but it's actually quite straightforward. For a long time, what we did for regular transactions was that we basically took the past I'm not sure how many blocks it took, because it depended on whether you were running a food or a light node. If you were running a full node, the gas price record took the last 20 blocks, which is a lot, but if you were running a light client, there could be two, and maybe now the latter will be better, but what it did was it took the few smallest guest priced transactions and basically found the not-so-good ones.
* But somewhat below that, so if we put them in descending order, there might be a 60th percentile or something along those lines, and we could just return it as a suggestion and yeah, so what we're currently planning, at least according to the most recent like kind of team consensus, is that we're going to keep this mechanism and use it for, I mean, we feed the effective miner reverse into it, so that's what it'll actually use, and this will be a suggestion for the private max priority fee and for the fee cap for the maximum fee per gas we suggest This proposal + twice the existing base cost, and yes, it's still a fair question how many blocks we should take, and it may depend on particular circumstances, so I also had this suggestion.
* I just posted this morning that maybe we could just iterate through the recent blocks and offer different priority fees depending on how urgent it is for you, and maybe this could be a nice signal for users to see if there's a congestion right now or not, and maybe this could be a nice signal for users to see if there's a congestion right now or not.
* I'll dig out the link, but it's in the 1959 free market left channel, so yeah, and so basically, we're going to use this to take the minimum or close to minimum tips of previous blocks and provide something below the median India, so that's what we're going to do.

**Speaker 01**
* Yes, thank you for sharing. So, to return to the topic at hand, I believe the biggest concern with the present get approach is that if there is a surge in demand, it will most likely be temporary And yeah, the 20 block is almost like remembering too much like looking at too much history, whereas under 1559 um you know things will probably happen much faster like if there's a spike it's likely to be something on the order of less than 10 blocks and um and if you're looking back at 20 you might have users overpay slightly.

**Speaker 03**
* I'm not so sure about that. If there is a spike, the surge is short-lived, so if you pick the most current block, so if you like fit yourself to the spike, you will spend a lot and get in sooner.
* And if you take a lengthier history, you will usually discover a tip that has worked in the past, and what will happen is that you will wait out like the spike and go in someplace towards the descending edge of the spike, so I'm not sure, interested yeah, that's correct, so it depends on what you want and how quickly you want to complete the purchase.

**Speaker 01**
* So basically, if I'm understanding correctly, the api would work pretty well if there is no spike at all, like if the blocks are pretty constant, but it would also work pretty well if there has been a spike in the last 20 blocks but it's kind of over and it would probably fail, and you know there is a spike happening right now And you know, yeah, that means you send your transaction and it just has to wait till the spike is cleared before it can be included again, is that roughly right?

**Speaker 03**
* Well, if we use a continuous setting, I mean content setting for how many blocks we look back, then yes, that's right, and thanks for attaching my proposal, so I guess that sort of handles this, but uh yeah, this is just like throwing up ideas right now, but alright, so that's what we have now.

**Speaker 01**
* Yeah, Micah, your hand is up.

**Micah**
* So I just want to reiterate my broken recordness, um most people here probably already know what I'm going to say but I'll say it again for the new audience i'm generally against any sort of priority fee estimation that isn't just what do we believe the miner's min value is the reason for this is because it's kind of self-reinforcing getting people into these auctions and bidding wars Although in most circumstances, it's probably unnecessary, and in the circumstances when it's still used, it can often harm the person as much as it benefits them.
* So, unless we're writing oracles specifically for like very advanced users like you know bot authors and stuff like that, which I don't think any of us are, I really think that for the premium we should just be saying hey, we know that miners will accept a premium of one, two, three, or whatever, and that's unlikely to change, and So this is what you need to set the premium to, and that's it, because I don't think we should be incentivizing or encouraging and helping people get into these gas auctions because they're just going to get themselves hurt, and things are going to go wrong, and it doesn't really improve anything in a significant way, and it's a lot of work and a lot of complexity, and then we have to disclose this in uis, and it's just a tremendous headache that I don't think will assist us in the long run.

**Speaker 03**
* Yeah, I kind of agree, but what so uh so this is why I'm saying that sometimes it makes sense to look further into the past and say, okay, this is the bare minimum that has ever worked and suggest that but I mean so you're talking about using a constant basically and ether price is changing so basically uh I don't know minor preferences the technology a lot of things can change so If these minor parameters change, how will users realize if we don't search for data like how many transactions are actually included

**Micah**
* Yeah so I think we do need it to be dynamic, but that dynamicism should be over really long time scales like we don't I don't yeah I want to be cautious here because there may be a little bit of incentive for miners to actually have dynamic base fee or sorry dynamic premium or priority pricing based on current mev rewards. This is really complex and difficult to do, but it is possible and theoretically rational as I want to be cautious with my words here, but at the same time, I think it's unlikely we'll see miners do this anytime soon because it's a lot of work and the games are pretty minor compared to other engineering tasks they could be doing, and so I think we can look kind of longitudinal.
* And, say you know the clients that are out there like guess that miners we think miners are using have just like a command line option for setting your minimum priority fee and we believe most miners are just setting a minimum to something and we have seen you know over the last ten thousand blocks ninety-five percent of the miners have been below two and so on.
* Have mined a block with a transaction below two, set your base fuel or say your priority fee to two, and I want to be careful not to get too into this not trying to be too dynamic not trying to adjust hyper fast to what we think miners might be changing because most of the time when that changes it's just due to a very short-term congestion spike that doesn't last and so I do think it should be dynamic we shouldn't just yeah i i agree with that.

**Speaker 03**
* Can i go next? Yes, go ahead, right so I believe the value should be dynamic as well, but the problem with looking at, say, past records of what people have been bidding is that we may be too slow to actually catch that the spikes are happening, in which case you're still recommending the minimum tip to users and at the end when the spike is over you're indicator will still be trailing these high values and may not be as useful, but we do have an objective source that we get for free from 1599 itself, such as we don't need to look at what users are doing, we can simply look at how full the blocks are or maybe like the two or three recent blocks and if we see that two or three blocks in the in sequence or even the previous block was full, Then we know we are in one of these spike regimes, and we don't need to wait for users to increase their tips because they may not do so on their own; they may rely on wallets to do so for them, and second, even if we wait for this with the parameters that have been set, looking back 20 blocks and looking at the percentile, it's not clear that you would catch immediately.
* that the spike is occurring and you can get it quickly enough by looking at the gas usage in the block itself so this is kind of what I was advocating for and I understand that it may be very different from the current paradigm and then there's a bit more implementation complexity but this is where I stand on the api.

**Speaker 04**
* Do you agree that we should respond rapidly to spikes with recommendations in the end?

**Speaker 03**
* Well, if you're going to react at all, so mika recommends not reacting at all and that's definitely a valuable position, but I do think that it might be possible for users to have at least some kind of indication that something is going on, so if you do want this indication, I think relying on the gas used by the previous block or the previous two or three blocks would be more accurate than relying on more subjective price points, such as what users are doing now.

**Speaker 04**
* Yeah well so this is why I propose that we like return a series of suggestions depending on how urgent it is and yeah so the users could decide whether they want to like find the fight fight for for priority or not and yeah it's also good to see whether there's actually had something happening right now but yeah always suggesting like to to to jump on the spikes I don't think it's a good idea to present it as an alternative that might be useful.

**Speaker 03**
* Right, I think returning a series of prices like options is fine, but I would still use the gas used as a metric to check that something is happening rather than user prices because then you have this kind of self-reinforcing behavior that I think mika is concerned about, and I am as well, so yeah

**Speaker 01**
*  Micah yeah so.

**Micah**
* Just to reinforce what Barnaby says, if we're going to do reactive gas pricing to congestion, we should definitely use the fullness of previous blocks to identify congestion. Similarly, if we're trying to figure out what the 95th percentile minimum is, if we decide to go with that, we should use that same block fullness to filter out um minimums like we're trying to figure out okay what the 95th percentile minimum is
* If we go with that, we should use the same block fullness to filter out minimums. For example, if we're trying to figure out what 95 percent of miners have set their minimum to, we should first filter out any blocks that were full or sorry any blocks that were full filter those out and don't count them at all um to get those numbers so that we're only seeing the minimum.
* The congestion times are not displayed separately. The key to remember in this debate over whether we should be reactive or not is that if everyone is reactive, it creates a pathological condition in which everyone ends up paying more, as if the reactiveness is valuable as an advantage over competitors and so on.
* If you have one user competing against another user, the one who reacts wins. If you are building an ecosystem, all of your users presumably are roughly equal, as you want to serve them all, in which case if you build in tooling for everyone competing using the same strategy, you just end up paying miners unnecessarily.
* So, if we do introduce these strategies at a very core layer, such as in Geth, we need to make sure that they're introduced in such a way that most people don't use them. I know it sounds strange to introduce a feature that we don't want people to use, but if we introduce them in such a way that everyone uses them, they become unusable, as they no longer serve a purpose.
* We desperately need to introduce this, and one way to do so is to have this concept of transaction priority, where the fast is saying yes, I want to be reactive, and the slow is saying no, I don't want to be reactive. One caveat with that, though, is that I'm concerned that compared to the base fee, if the base fee is 100 and the fast medium slow is like two one two three like everybody will always choose fast and now we're back in that same situation where everybody is choosing fast and it's no longer helping anybody because everybody's following the same strategy like in order for this to work we need people to be following different strategies and if everybody follows the same strategy the strategy stops working this is very common in game theory, therefore keep in mind that we need strategies to ensure that participants are not all using the same approach.

**Speaker 05**
* So one tangential question I have is that we're trying to solve the whole gas price suggestion problem before we actually see how the network behaves, and my personal two cents is that the current model that is being implemented is essentially just continuing the old algorithm, and I completely agree that this may be completely unsuitable.
* for certain tasks or scenarios, but it worked until now, so wouldn't it be prudent to wait until mainnet actually forks over and see how the base fluctuates and how tips fluctuate before we try to solve this problem? I'm afraid we're coming up with the wrong solution because we don't know what the problem is until the fork. Yeah, but the issue may be dependent on what we offer as a default choice, so yeah.

**Speaker 06**
* It's the I kind of agree with you but yeah we should also keep in mind that what we see in practice depends on what we offer as a default option now yeah yeah of course but essentially if we continue our current algorithm then at least we know how wrong it is whereas mica had a really nice example I think the base fee is a hundred and the tips are one two and three Then it doesn't really matter, and this is precisely the issue. We don't know how the tip will fluctuate in relation to the basic, which is why I think it's not easy to fix the problem; at least, it's not clear to me what the specific problem is or will be.

**Speaker 01**
* I stuck Greg because he had a comment, and I believe you placed your hand down.

**Greg**
* Yeah, for me it was just kind of coming back on mikko but he kind of answered it the big one for me um is that I personally believe like I would rather people pulling the nodes to figure out a gas price than a third-party api um and in that case like we're always going to have to be competitive to some degree so if you know you kind of have to go Back down to like there has to be some level of competitiveness there um obviously the issue is that we're going to run into the same problem we have now where everybody just competing for astronomically high prices is a problem um but in the case where like you know we have products that we use um if we don't we try using the node and we actually had to switch off of  geth and open a theorem just like we couldn't rely on the node for the gas price anymore and now we're using a third party which is not what I want to be doing right now so like I think we have to do some sort of competitiveness and like you said you just have to be careful but I kind of agree with peter in the sense that is there something simplistic we can do and just see how it ends up playing in the real world.

**Micah**
* So I think there's a simple thing we can do that has a good chance of working for launch and then we can re-evaluate once you have more data, and that is to encourage client devs to have hard-coded defaults for the priority min priority fee that miners use and a hard-coded default for the party fee that gets returned if you ask for a gas price recommendation and make sure those two are the same thing both of them can be overridden by command line parameters or whatever but the idea here is that by default if all miners just run stock guess and all users run stock guests then everything will just work like the min priority fee that miners accept is exactly the same as the priority fees that users use and everything gets through.
* With an exception for during congestion, at which point we get good data on how congestion happens and what happens there, and then a week or two later we can start making alternative recommendations, and then the next patch of geth can maybe include something more smart, but if we can get all the clients that kind of just agree that hey where's our miners, we'll do this by default is the min Our users will benefit from This is the minimum then I believe we have something that can work out of the gate and my guess is that most miners will run stock out of the gate and similarly watch and see before cranking up their numbers and so we can set that to one we said that's two let me say it to five you know we believe that you know one or two is probably the right number well you said it's five just because that will most likely be insignificant in comparison to the base charge at launch, and you know people won't mind five and it.
* Means that miners are less likely to manually alter that again, which requires all of the clients kind of deciding okay this is our launch number just to feel things out but I believe it's pretty straightforward and it gets us to a position where we have more data.

**Speaker 3**
* So, one counter-argument to that is that gas prices are currently fluctuating, I mean, I have no idea what it is currently lasts a few of days ago it was around 30 a week before that it was about 100. So you have a significant fluctuation with me, which means that the node must fluctuate in tandem with the gas price, otherwise your transaction will never be included.

**Micah**
* Oh, I understand. You're saying that the issue here is that the eth underscore gas pricing needs to function for legacy transactions, not uh.

**Speaker 3**
* No, I'm talking about internal both that one if you want to submit a transaction by get then your assumption is that the transaction will go through reasonably quickly now if cat will always tell you that the tip is to peek away and the base keys whatever then probably when others are paying 100 feet away for the tip I mean good luck with your two gigahertz.

**Speaker 1**
* yeah and I think so this is the failure mode of heart basically hard coding the base fee works only when there isn't a spike right so what you're saying there is like you won't you're guaranteed to not overpay when there isn't a spike but if there is a spike you'll be way underpriced and then you need some other way to estimate what the right base right the right price is.

**Micah**
* Yes, exactly, and the caveat there is that we expect spikes to be both rare and short-lived, so users who are just using the default will probably still get through like as long as you're setting like base feed times two or whatever like this common people talk about um you'll probably get through in almost all cases like it just might take you until at the end of the spike and the spiking will be over.

**Speaker 3**
* There are two cases where you won't get in, one is if there's a spike and the other is if there's a high mev transaction, which is why selling a constant is a bit more difficult. Barnabay has some graphs about this, but basically if a block has a really high mvv transaction, the opportunity cost of being uncold is quite high, so it's kind of unlikely to include anything.
* With this kind of hard-coded tip so if you get if you hard code a tip of two then it's I think it gets you something like 75 of the blocks with mev it still makes sense to include those transactions if you have a tip of and the top 25 probably just won't include transactions with low tip so that's the other case where you're just kind of selling it out I think right now last time I checked there's about 35-40 blocks that have mev so that means statistically if you're really unlucky you set your transaction the block has a ton of mvv in it but then you know the block after probably doesn't have a ton and and you get into that block but yeah it is a case where like and I don't think the current gas price oracle can.
* Really pick it up like it'll probably pick up what's the sort of average longer an average and and you know looking at it right now it would be like two ways would compensate for the uncle risk accounting for something like the 75th percentile of MEV but you're not going to be included in those blocks where there's like a 10 eth front-running opportunity.

**Micah**
* With the cap again, my caveat here is that we should do this as a launch item with intentions to adjust it in the future, hmm and the reason I think this is fine is because.

**Speaker 3**
* I believe you just broke we're going to have we missed we missed the reason you think this is fine.

**Micah**
* an you hear me now, or am I still 

**Speaker 3**
* you're good

**Micah**
* Okay, so the reason I think this is fine is because on launch day, I find it very unlikely that all the miners will all of a sudden have super advanced pricing gas min pricing strategies already coded into a patch for geth or whatever minor they're running um even without having any data on one five I just like remember miners are going through this exact same process as we are where they have no data they have no idea how things will work out in the wild they don't have the guest code to work on yet so they can't even start their patch until after we get our release candidates out and so like if we just plan on having this like this is our kind of launch thing to get more data and we know in a couple weeks we'll change it or in a month we'll change it I think that is safe, as I do not believe we need to be concerned about a huge number of miners employing hyper-advanced gas pricing tactics on launch day.

**Speaker 6**
* So, on launch day, on the day of the fork, most people, most clients who are sending transactions are probably going to continue sending legacy transactions until the market stabilizes or they'll gradually roll that out to something, and those folks are going to you know many of them still rely on the e gas price api, assuming that still exists At the very least, it is backwards compatible and continues to return the same implementation for legacy transactions, which means that the majority of the market will be sending legacy transactions with max fee set to max fee and max priority fees set to the same thing, which I believe means that the majority, unless we are committed to breaking eve gas price and doing rid of that api entirely we are the fact that like clients you know guest is going to be de facto making pricing recommendations regardless is that correct?

**Speaker 3**
* Yes, almost so it doesn't really matter what you have to eat gas price or not guest price uh 10 point because legacy transactions still only have one gas price fields which get interpreted as both the different I mean as both these so as long as you're sending a legacy transaction doesn't matter how you estimate the gas price it's still going to burn block.

**Speaker 6**
* so I think I sense a difference here hmm.

**Micah**
* I believe Peter is referring to people who send their transactions unsigned to geth and then guest fills them out, signs them, and submits them. I believe Yuga and others are referring to people who ask geth for the gas price and then fill out their own transaction in a script or an external service, sign it, and then give it to guest to submit to the chain.

**Speaker 3**
* I was talking about that the second thing so if you just ask a guest to sign the transaction we will never sign the legacy transaction so get will always default to 1559 transactions uh i'm so referring to the guest price on you when you sign when you sign it outside of get so to say you just ask for the guest price and create a legacy transaction yourself in that case I mean both the tip and fee will be the same, and I don't believe that was the primary issue, that everyone would be utilizing the old legacy transactions.

**Micah**
* so maybe I'm not clear on what you mean by the return value of each underscore gas price change with the fork.

**Speaker 3**
* only a single value, like a single number

**Micah**
* and that single amount will be a mixture of the base cost multiplied by two or whatever, plus some parity-free recommendation.

**Speaker 3**
* Prior to you, it will be a priority plus one.

**Micah**
* Okay, so it's going to be party feet.

**Speaker 3**
* So, effectively, the current behavior would be retained.

**Micah**
* People who want to sign a non-legacy transaction will most likely wish to utilize a new endpoint.

**Speaker 3**
* that gets a separate base fee and priority fee yes for that we didn't so there was a client made the uh the pr to the something specky whatever about the new rpc endpoint so we did introduce that so we do have the I don't know what it's called whatever is in vip it's called that endpoint to actually return just the tip and then uh okay we have a separate endpoint So, if you want to submit  1559 transactions, we have a separate endpoint to specifically give you a tip and we do not have an endpoint to specifically give you a fee cap because it's so if you don't specify you will just default to the tip plus to the base keys if you want more control you can specify it it's very reliable so the hard thing to do is estimate the tip so that's why we need to support an API for.

**Micah**
* Yeah, gotcha, that clears things out for me, thank you all right yuga, I'm sorry for interrupting, I was wrong.

**Speaker 6**
* No worries at all I mean I guess the only point i'm making is that it's clear that clients are going to make recommendations there's no way around that right because there are many many people who rely on these apis on the east gas price api specifically so we are de facto making a recommendation about how to price 1559 transactions because You know, legacy transactions can be interpreted as 1559 transactions, so I believe that ship has sailed, and the only question now is what kind of recommendation we make.

**Speaker 3**
* Well, you made a good point there that the problem here is that we don't just buy this switch forward to 1559; rather, we will have a mix and match for what's more, initially most of the transactions will continue to be legacy transactions, so people have expectations of how legacy transactions work, how they are priced, and how they compete with them, so I don't think we can really break that expectation then, if you have a network with 90 taxi transactions, you must design your 1559 transactions in such a way that they can compete with the legacy transactions, because if the legacy transactions are paying 10x the tip, no matter how nice an algorithm you devise for the 1559 transactions, they will not be included because they were always underpriced in comparison to the legacy transactions, so this is kind of where I was coming from, is that I don't think it's advisable to break the current workflow for legacy transactions because we have projects wallets and everything that kind of rely on it with all its quirks and ugliness and some optionality, so I don't think it's advisable to break that and if we don't want to break that, then our hands are kind of limited in how we can construct estimations for 1559, however this is a problem for which I do not have a solution.

**Speaker 1**
* So I guess one thing I'd be curious to hear people's thoughts on this greg you kind of mentioned earlier you know you see it as a bad thing to query like a third-party service to get more precise gas price estimates at the same time it kind of feels like a separation of concern issues like where you know guess gets like main functionality is not to be like a gas rights oracle right?
* It's to be a node and submit some you know reasonable estimate for the gas price and it does feel like 1559 has a much broader design space for like gas price oracle so I i'm curious like what what people feel like if geth has like this good enough kind of backwards compatible solution that's not optimal in all cases you know does it make sense to have folks like eat gas stations now and what not be the ones that kind of you know come out with fancier apis that do look at the block history that help with this use case like I assume I know more granular if if you want like use cases um I don't know if others have ideas on that rick I see your hand is up yeah.

**Rick**
* For me, geth is the best place to put an oracle because everything already kind of needs it and I mean itself needs it but it's like a point I can kind of trust if a person is trusting in fear they're going to continue trusting in fear it's strange that you know in order to do anything I trust infira and now some like a get gas price something something especially when All the data is sitting in memory in geth it has to for other purposes anyways um and that's kind of my hope is that I mean at some point I saw somebody else recommend it as well as even like a histogram or something of gas braces but it seems like there should be some way to like bubble up information in a call that they can be used by a more clever oracle even Even if geth doesn't want to be the final call, if they can bubble up enough information that's literally sitting there in memory, it doesn't have to hit the disc or anything in my mind, so that's kind of my take on it like in ethers when you connect to something you connect to something if you call get gas price it's not going to start then trusting some other service um for the gas price.

**Speaker 1**
* Got it. Santiago see your hand up.

**Santiago**
* Yeah, I agree with Rick that it would be fantastic if Geth could solve 95 percent of the cases, and we're mentioning that we still haven't figured out exactly how to solve the difficult cases, such as bot writers, traders, or people who need to get in during a spike, and I believe that would be the place where we would rely on gas now any gas station or more complex casper gas price oracles, but for the average user, I'd love it if you could share the entire answer cool peter is here hand it up again.

**Peter**
* Yeah, so an interesting question from the perspective of get is, um, given that 1559 will arrive, let's say we'll have two api inputs, one for collected transactions and one for 1559 transactions, our assumption up until this point has been that get is kind of work operates in this headless mode where an external app just does that to somebody's transaction.
* then gat needs to figure it out now from this perspective I don't think we can make it much smarter now I think it will show suggestion to maybe have an additional api endpoint maybe automatically additional part that may be able to provide some more information but the problem is that yes, we could be smarter and look at various metrics and try to give some options to the user but for such an api essentially, you need something in front of the guest that can actually show this to the user or make heads or tales of the recommendations or variations and then the user or something gets too big but I still think that if you just have a dumb program like a mining pool payout that just wants to pay regardless of how much it costs, then you'll still be in the dumb api which kind of just works and doesn't give me an option, but I'm OK with having an additional api endpoint that attempts to be a little smarter and offers some suggestions.

**Speaker 7**
* Yeah, that's how I imagined my suggestion yes, so that's why I think it's a good thing if the more flexible thing is like a generalization of the default thing and we should definitely leave the default uh default api and I also want it to work more or less the way it did before because yeah, it's better not to break things that already exist yeah.

**Speaker 8**
* Sir, can you confirm what Barnabé Monnot asked on the chat about what exactly this gas price api will return? Is it going to be the base fee plus an estimate of the maximum priority fee?

**Speaker 3**
*  so currently the gas price workflow within gas just looks at the past blocks and tries to see what was the minimum minimum I think for each block what was the minimum three tips actually paid to the miner and then based on that it will currently the crisis takes the 60th percentile so it essentially tries to take not if not the smallest tips within the blocks but the smallest tips within the blocks but the smallest tips within the blocks but the smallest tips within the blocks but the smallest tips

**Speaker 7**
* Yeah, but I think the best question was, "What will the old guess at gas pricing api recommend?"

**Speaker 3**
* So essentially I was saying that internally get calculates a recommendation for the tip and then for the old east gas price we simply add the current base fee for that to that tip and essentially that way the basically gets burned and the tip that the miner gets will be more or less what the miners were getting in the previous blocks so the miners should be happy with that.

**Speaker 7**
*  So, basically, the answer to the benefits question is yes, and thank you.

**Speaker 8**
* could you please provide a brief follow-up on that what is going to be excellent behavior if it detects a transaction on the mempool with a base fee that is less than the current block is it going to keep it on the member or is it going to drop it?

**Speaker 7**
* Currently, the implementation was actually encountered by Jordan, is that okay you can talk about it yeah just real quickly yeah so I don't want to go into details again but yes we do keep transactions in the manpod that are currently not includable if they have a high fee cap because then they will surely become includable really soon so so what we do is that  For the most of of the pools, we recalculate the actual binary reward based on the current base fee, the most recent base fee, and we prioritize transactions based on that, but there's a little space reserved for those transactions that would fare very poorly in this comparison but still have a high fi cap or max fee, so they're worth keeping because they'll be includable.
* I don't know how many blocks it will be in the following five, so sure, fine, thank you.

**Speaker 3**
* currently, the transaction pool maintains 4000 transactions, and with this update at 1559, we added another 1000 transactions whose purpose is to be those transactions that cannot currently be executed because the base fee overflows or underflows or whatever, but uh, they look good otherwise, but as a disclaimer, it is a new mechanism, so we're hoping it doesn't blunder.

**Speaker 8**
* And the reason I was asking is that there is an assumption that legacy users who send the old format transaction will always be grossly overpaying because their max fee equals their max priority, etc. However, if your api returns the base fee plus an estimate of the max priority fee, and if the max priority fee of this legacy user is really large over time, Base fee should try to compensate for this, and we will basically match the price levels that these legacy users are sending initially, which means that once that happens, the actual priority fee that these legacy users are sending should be pretty small, and should be close to the minimum that miners would accept, and so legacy users are actually a bit hampered by this because they are recommended prices that are close to basically which means that any small fluctuation of ones of the base fee means they are priced out it's not like the current mechanism where okay there's room they can still go in like the base fee is really binding so I don't think we need to be too concerned about these legacy users and I don't think we need to have necessarily this image that they will be really overpaying all the time.

**Speaker 9**
*  I'd like to ask a follow-up question to uh peter's comment about the memphis structure there um currently the mempool is divided into two parts of the uh cubed and the pending um did I understand correctly that there will now be a new component to the mempool that contains these uh high max fees but not um but the base fee is insufficient for the current block.

**Speaker 3**
* Yeah, so this is a different division, so cued and pending are per account things, and it's about the ordering of like sequential transactions, but there's like a big heap for all the or we had one big heap for all the remote transactions, and yeah, yeah so that's that that priority heap was for like eviction of underpriced very low price transactions and this is what has changed and this is now that works that yes if if it falls out of one queue that is based on current miner reward then it still has a chance to stay in the second queue that is based on most that is just based on vcap on max fee so yeah and this is a new queue.

**Speaker 9**
* Does this new queue consume additional queue, hmm type of slots?

**Speaker 3**
* like we have yes 4000 now for the pencil we did not want to break the existing situation so we raised the mempool's size slightly so now we have a 4000 sorted by current miner reward and an extra 1000 sorted by fee cap which is I think affordable and uh and it's also guaranteed that it will not work any worse than it did before at least if the code is not broken or something yeah

**Speaker 9**
* Thank you so much for the clarity.

**Speaker 3**
* slight clarification that I wanted to make or precision is that currently um this cue split isn't really a split isn't really introducing any new cues rather what it does is it just changes the eviction algorithm so previously when the queue was full i.e. depending on how many transactions were queued up for execution and another one arrived then that one actually needed to push Something out and then if there was something cheaper then it pushed that something cheaper out and with the new algorithm we have a combination that if I have 5 000 transactions because that's the new limit then if the new transaction pushes something out tip-wise from the 4000 then it gets included and if it cannot push something out tip-wise and it can try to push something out then it gets included.
* If it can't push something out tip-wise, it can try to push something out from the worst 1000 maximum cap-wise, so it's simply playing with the eviction rules, but otherwise the transaction remains exactly the same structurally.

**Speaker 1**
* Any other questions on the gas price article? There was another item on the agenda, so I just want to make sure we have 10 minutes, so it feels natural  transition.

**Micah**
* Yeah, I've seen a lot of people say they want to avoid centralized oracles, which I completely agree with. I think the thing to remember is that we need to drop our understanding of the old system and think about the new one. In the old system, in order to build an oracle, you basically need to monitor the pending pool and have access to large amounts of data. You don't need this high frequency data access, with the exception that you do need to know what the base fee is, so I believe the clients should return the base fee for the next block, and you do need to know what that minor estimate is, which is similar to a data problem, so I believe there's value in the clients returning data about that once we return those two pieces of data.
* Everything else should be calculatable with a small javascript library because you don't need more data than that like you used to and so I don't think we need to worry about  centralization of oracle's like we see with gas now and inferior or whatever because the oracle is simplified so much that it fits in a library as long as we have the data we need from the clients and so I would much r But once we have that data, like we can have every wallet use their own library they have their own little oracle they can tweak and tune it we can have standard ones that we share and so on and there won't be any centralization we don't need to worry about centralization as long as the data is available even if geth doesn't provide any gas price estimator.

**Speaker 3**
* Yeah, I agree that that is a nice approach just explosive data, but one thing I wanted to point out is that the basically is already exposed because it's part of the block headers, so you can always retrieve the basically of the current block uh I mean if you just retrieve the header you have to basically and you can see whether the block is full or not, so you can If you need to calculate the essentially for the next block, you could, but I doubt anyone wants to guess so near to the limit.

**Micah**
* I think some will like it if we could just have the end point that just because calculating the base suite for the next block is kind of complicated and you do need the full transaction list or at least the gas used for the block, um if you have the gas used for the block then end the base fee from the previous block it's already there yeah, that can also be live in the library, so yeah, all you need is the final block and the histogram of history things, I believe.

**Speaker 1**
* I tend to agree that over time, because the estimation was so complicated and now it's simpler, it probably makes sense that wallets can probably write some of it themselves, but I understand that this is a transition and you want things to go smoothly, So yeah, I think that's something we'll gradually see happen, and maybe one thing I can follow up on is how do we actually provide like this kind of basic implementation in javascript that helps you do a good estimation and shows people that it's not rocket science.
* We can do it quite easily because we only have five minutes left, but a few people have asked about having a json rpc endpoint for the next blocks base fee, and I just wanted to check how valuable and easy that is, both from the people here and from the people I know on the get team, because it's easy to calculate in some ways but it's also like you It is easy to calculate in some ways, but you do need to look at the spec from 1559, so it feels like it's something that the client could do fairly easily and that third-party libraries would have to fiddle with a lot to get working yeah, so here are our people's thoughts on like a base fee.

**Speaker 10**
* So, in order for us to build a pending block, we need the base cost for any block, which you can obtain by retrieving the bending block.

**Speaker 1**
* Okay, does that work for everyone here? So you get the block with the pending tag and obtain the basic pergas from there.

**Speaker 10**
* Okay, so that would already expose it; if that isn't enough, we can explore exposing another API, but I'm not sure if that is enough.

**Micah**
*  I would be happy to collaborate with Rickmoo to simply ensure that ethers.js has a calculated base fee from the pending block the latest blocks basically um I think it's simple enough that once javascript has it you can just copy that into whatever your language of choice is it shouldn't be too difficult it already exists in python.

**Rick**
* Yeah, what I've been doing in my current application of eip1559 is I just grab uh a get block negative one and take the black the the base view of that um my one concern is this get pending block is that new or is that something that is exactly like 1559 because part of ethers is right now detecting whether or not the network supports um eip 1559 by checking the previous block if there is a base fee on it so pending has been around for a while.

**Micah**
* Caveat that not all clients return the same result for pending, so for ethers, I recommend being cautious about utilizing that endpoint just because it isn't consistent across clients.

**Rick**
* I mean, I'm not sure what the other fields would be like, so yeah.

**Micah**
*  Yeah, neither could the clients, who all had different ideas, so.

**Speaker 3**
* Standing block has been a part of ethereum so actually since forever.

**Rick**
* However, you will be blocked by hash or block tag pending my number number, and you will be retrieving block minus one, thus. That's what I mean, if you pass in a negative number, ethers obtains the current and subtracts it for you using the most recent block number.

**Speaker 3**
* Yeah, if you get at least minus two in gambit, that's the pending block, but I'm not sure whether you'll be able to pass it, so if you just let me verify which end point you eat, that'll be OK.

**Micah**
* Block by number pass pending the word the string pending as the one parameter and you'll get it thank you i'll try that it's the same thing as passing the late the word latest in for that just in the same spot I think you might need a boolean as well for whether you want the receipts or the transactions I think you might need a boolean as well for whether you want the receipts or the transactions.

**Speaker 11**
* So the only disadvantage I see to using the pending block to collect the next basic fee is that you get a lot of superfluous data, but it works for our use case, so I'm fine with that.

**Speaker 12**
* So, if you don't understand it, the basic key is maybe five bytes and the header is 500, so yeah, from that perspective, you waste a lot of data, but the question is whether that's too much or not. It's a reasonable question, so I'm not saying we shouldn't add a gap; rather, I'm saying that we can do it now, so it could be worthwhile to watch how people use it before adding the endpoint that's actually required.

**Speaker 1**
* We have two minutes left for any other quick concerns that anyone might have.

**Speaker 13**
* I just had a quick quick comment or if I'm not sure what the plan is after this but I was struggling to follow along in some parts and so if someone could give me a summary of like the it sounded like they're going to be certain phases there is still a little bit of debate of exactly what the guest client will be providing and it also sounds like the gas station apis will be providing And it appears that the gas station apis will also provide some fancy extra fancy features potentially or not as a wallet we would still prefer to be able to get information easily and digestibly with like rich content from an api if that's possible from geth but without like we don't want to constantly be pooling on each of our clients for the last x number of blocks.
* So it'd be great if both were offered from an API standpoint as well as directly from the clients, but yeah, if you could outline what the phases are for rolling out that would be great definitely.

**Speaker 1**
* so right now or uh 

**Speaker 13**
* oh no, it doesn't have to be right now, it could just be in a summary after the meeting just to make sure that yeah we understand what's going on 

**Speaker 1**
* yes and I believe it's still kind of flowing but i'll try to get it yeah and i'll post it on the discord yup.

**Speaker 3**
* So before we close this video, I believe Michael mentioned that it would be beneficial for gas or ethereum clients in general to expose certain past historical I don't know histograms of who's been paying how much for which miner if we can so I think providing a gas oracle that works on these is kind of hard I mean forget because it's an api that we can't just change afterwards because We're shooting them a network if they rely on it, but if it's an api that just provides data that others can build on, that can remain stable, so if we just provide that api that returns a histogram of uh priority fees paid, at worst nobody will use it, but we don't need to change the api, it can't be wrong, so I think that might be a really good good idea.
* To expose this information, anyone can build a gas circle on top if they want something custom, and if something turns out to be nice and something tells us to be stable, we can also shift that within gap. The reason I'm saying this is that if we can figure out a reasonable data retrieval to expose from gas, I think it would be nice to add it, but that one requires an idea stacked out because ideally you want the same data from so micah if you have a recommendation on what data you would like to see I suppose george also had some instagram idea approach maybe you can manage your ideas and yep.

**Micah**
* To keep things short, I believe my recommendation is that, as I previously stated, guest returns only some data, some of which has already been returned, so I'm just going to try to be all inclusive here um the base fee of the latest block the base fee of the pending block the fullness of the latest block the fullness I guess that yeah so the defaults of the latest block base the charge for the pending block the fullness of the most recent block the fullness I guess that yeah so the defaults of the most recent block base field latest block base fee of the pending block and then a histogram of the minimum the lowest gas price accepted by over the last n blocks with full blocks filtered out I think that that full box filtered out I think is critical for getting the most useful data here and I think with that With that data, you should be able to build most of the types of oracles I've heard others propose with just a handful of lines of code in any language.

**Rick**
* A quick thought: in addition to the histogram of um gas prices, perhaps a histogram of whole blocks, if that makes sense, or at least so there's someone who knows how blocks work.

**Micah**
* I think it's definitely useful and interesting data, and I can imagine someone wanting to write an oracle that takes that into account, like oh, you've noticed that there's been a lot of volatility and block fullness lately, so we're going to change our strategy, and so yeah, let's add in a stretch goal of a histogram of block fullness over and blocks.

**Rick**
* Histogram may be the wrong word, but I don't know what else to call it right now.

**Speaker 3**
* Yeah, but we get the concept, so I think it'd be great if we could just write down a small list of what we'd like to see and then figure out how to expose the whole thing because gathering all that data and exposing it isn't particularly difficult, so it's just a matter of figuring out what the actual data we want to expose.

**Micah**
*  Tim, if you provide me a location to put stuff, I can start it and then let others modify it.

**Speaker 1**
* yeah okay sure i'll do that uh i'll send you something uh i'll post opposite the 1559 fee market channel and discord um if folks want to uh comment there uh yeah that would be really valuable so um yeah i'll i'll put together like a hackmd or something that anyone can edit um yeah um great yeah this was pretty helpful um and I suspect you know we'll probably have another one of these calls.
* In a few weeks, and once we actually have 1559 on a test net, it might also make things a little more concrete. In the meantime, if you want to play in a very experimental way, which I think is fine, we do have a devnet called calaveras that's up and running, and there's a spec for it in the github specs repo.
* If anyone wants to check it out, I'll just link to it here in the conversation. It's really basic, like rpc support and such, but it allows you to send transactions and, if you have your own tooling to kind of play with them, that could be useful.

**Micah**
* Just to mention it, if you download it, it also has the flag for joining this color as Tesla, so you can join it and play with the whole thing with an unstable build of get.

**Rick**
*  Had a brief question as well, is there like by call had someone else set up a rpc node we could just connect to and it didn't explore, will it be put to the new card calaveras the explorer is already there, but I'm not sure about the rpc node good.

**Speaker 1**
* Yeah the explorer is linked in the spec um and there's an each stats in the faucet as well uh okay last quick question what's the parameter to think death oh perfect yeah yeah and they answered in the chat yeah cool okay well yeah thanks everybody uh and yeah talk to you all or at least part of you in the coming weeks thanks everybody for joining we'll send out an email with the link to join we'll send out an email with the link to join we'll send out an email with a link to the recording and, if available, notes, or a summary document

-------------------------------------------
## Attendees
**Trenton Van Epps** 
**Pooja**   
**Micah Zoltu**  
**Tim Beiko**  
**Zsfelfoldi**  
**Juan Blanco**  
**Marius**  
**Alejo Salles**  
**Alex Chainsafe/web3js**  
**Barnabe Monnot**  
**Bartek Rutkowski**  
**Bruno Barbieri**  
**Caleb Lau** 
**Carl Fairclough**  
**Chris Meisl**  
**Dan Miller**  
**David P**  
**David Walsh**  
**Franco Victorio**  
**Frederik** 
**Gal Eldar**  
**Gred Markou**  
**Harith Kamarul**  
**Jake Haugen**  
**Jin Chung**  
**Jordan.eth (Frame)**  
**Juan Blanco**  
**Kevaundray Wedderburn**  
**Kevin Ghim**  
**Lightclient**  
**Maarten Zuidhoorn**  
**Matt marshall**  
**Nieldlr**  
**Polina Aladin**  
**Ricky Miller**  
**RicMoo (ether.js)**  
**Romavolosovskyi**  
**Samuel Dare**  
**Samuel Walker**  
**Santiago Palladino**  
**Yuga**  

---------------------------------------
## Zoom Chat:

10:00:22 From  Trenton Van Epps  to  Everyone: Agenda: https://github.com/ethereum/pm/issues/328  
10:00:48 From  Micah Zoltu  to  Everyone: Does anyone know if there is a way to make the web client show the tiled view for Zoom, rather than the "current speaker" view?  
10:01:15 From  Trenton Van Epps  to  Everyone: near the top  
10:01:25 From  Trenton Van Epps  to  Everyone: change view to gallery view  
10:02:11 From  Micah Zoltu  to  Everyone: I don't see such a thing in the web app.  
10:02:36 From  Trenton Van Epps  to  Everyone: oh not sure about the web app  
10:02:53 From  Richard Moore  to  Everyone: Can you re-share the link to notes?  
10:03:11 From  Tim Beiko  to  Everyone: https://github.com/ethereum/pm/issues/328  
10:03:59 From  lightclient  to  Everyone: unrelated, but i notice a small issue on etherscan -- the genesis block shows a 5 eth block reward to the coinbase 0x0 when actually no block reward is applied to the block  
10:06:39 From  Tim Beiko  to  Everyone: New Geth proposal: https://gist.github.com/zsfelfoldi/9ca596996f5a556c58dae3aa4f4d0049  
10:09:52 From  Bruno Barbieri  to  Everyone: The spike scenario is a bit problematic for time sensitive operations like swaps  
10:10:11 From  Tim Beiko  to  Everyone:@Bruno, but in those cases does the current gasPrice API work well?  
10:10:38 From  Tim Beiko  to  Everyone: Basically, how well do swaps work now if there is a sudden spike in demand for transactions?  
10:11:32 From  lightclient  to  Everyone: it feels like naively scaling maxFeePerGas by a constant factor is not the ideal solution, seems like there should be some mechanism to determine how quickly the basefee is moving + the direction it is moving  
10:11:56 From  Tim Beiko  to  Everyone: Do you think we need this in the client itself, @lightclient?  
10:12:11 From  Tim Beiko  to  Everyone: Agreed we need this, but it feels like something for EthGasStation or the like?  
10:12:27 From  Tim Beiko  to  Everyone: Ideally those estimations look at more than the price, but also the gas used  
10:12:47 From  lightclient  to  Everyone: i think it has to be available via clients if you want to allow all users to access this info without going through a centralized entitiy  
10:12:49 From  Bruno Barbieri  to  Everyone: @Tim Beiko - We currently fetch the gas price right before submitting tx, so we currently get the “fast” spike price  
10:13:41 From  Tim Beiko  to  Everyone: @Bruno if Geth updates over 20 blocks, as was just said, isn’t that value still underpriced if there’s a spike?  
10:17:53 From  Tim Beiko  to  Everyone: Greg, please go next  
10:18:01 From  RicMoo (ethers.js)  to  Everyone: What about returning a histogram? I saw someone recommend against that though, wasn’t sure why. I would also love it to be a `eth_getFeeData` call that returns extra stuff. In the future we can add more values to the dictionary, which means the caller can determine what the feeData includes. Such as % blocks full.  
10:18:03 From  Carl Fairclough  to  Everyone: If a large volume of users are transacting via wallet apps then we want to make sure that we’re not necessarily elevating fees  
10:18:24 From  Carl Fairclough  to  Everyone: unnecessarily*  
10:18:26 From  Frederik  to  Everyone:^  
10:19:40 From  Kevin Ghim  to  Everyone: The strategy could be based on different types of transactions such as swaps, onramp, send/receive. Depending on this, users might choose different speeds/priorities.  
10:20:35 From  Santiago Palladino  to  Everyone: Won  
10:21:34 From  Santiago Palladino  to  Everyone: Won't tips just keep matching the current gas price, if both wallets and gas price oracles wait to "see what happens" and keep sending pre-1559 txs?  
10:22:03 From  Barnabé Monnot  to  Everyone: It should still be somewhat of a default for users to keep the minimum miner fee, or increase their max fee. Ramping up the bid could be opt-in rather than opt-out. Either way the longer high bids trail in the histogram/return values of the API the worse the outbidding gets.  
10:24:05 From  Yuga Cohler  to  Everyone: The other thing to note is that most clients will probably not immediately start sending 1559 transactions. Many will continue sending legacy transactions for some period of time. That means the maxPriorityFees on these will be artificially inflated.  
10:25:34 From  Carl Fairclough  to  Everyone: I’d be happy with hardcoding provided that we’re VERY confident with the tip, and that it’s not a large overpayment. We would have to watch for spikes to revert to a auction pricing  
10:26:21 From  RicMoo (ethers.js)  to  Everyone: Does the new Block response include a `size` and `target`? So that users can estimate congestion?  
10:26:32 From  Micah Zoltu  to  Everyone: Yes.  
10:26:34 From  Barnabé Monnot  to  Everyone: To note, if the gas price level is 50 and everyone sends 5 Gwei priority fees, basefee should equilibrate at 45. There’s not really overpayment on the user side, rather more is given to miners than the minimum they’d accept. If users want to revert to FPA during spikes they’d have to bid above 5 however  
10:26:37 From  Micah Zoltu  to  Everyone: Well, sort of.  
10:26:48 From  Trenton Van Epps  to  Everyone: resources + info from the last few calls if anyone hasn't seen it: https://hackmd.io/4YVYKxxvRZGDto7aq7rVkg?view  
10:32:50 From  lightclient  to  Everyone: eth_maxPriorityFeePerGas  
10:36:37 From  Barnabé Monnot  to  Everyone: The eth_gasPrice API will be basefee + the geth estimation of the maxPriorityFee, is it correct?  
10:37:08 From  lightclient  to  Everyone: +1 to rick  
10:37:32 From  lightclient  to  Everyone: would hate that a critical peice of transacting with eth be centralized  
10:38:49 From  Juan Blanco  to  Everyone: +1  
10:38:51 From  David P  to  Everyone: +1  
10:40:30 From  Micah Zoltu  to  Everyone: *grumble* BRB, Zoom audio died on me.  
10:41:45 From  Micah Zoltu  to  Everyone: (back)  
10:42:47 From  Yuga Cohler  to  Everyone: So eth_gasPrice = current base fee + 60%ile maxPriorityFee of past blocks  
10:45:46 From  Tim Beiko  to  Everyone: Chris, please go next  
10:46:21 From  Yuga Cohler  to  Everyone: I essentially agree with Barnabé. Maybe the solution is to take a phased approach:  
10:47:16 From  lightclient  to  Everyone: here's the sketch + rationale for geth's tx pool changes: https://gist.github.com/zsfelfoldi/9607ad248707a925b701f49787904fd6  
10:47:34 From  lightclient  to  Everyone: @zsfelfoldi's work ^  
10:51:47 From  Chris Meisl  to  Everyone: @RicMoo Blocknative provides a histogram. Fair earning, its a centralized api ;)  
10:51:48 From  Tim Beiko  to  Everyone: @Peter do you have a follow up to that or is your hand still up from last time?  
10:53:09 From  Bruno Barbieri  to  Everyone: RE: Gas oracle vs Geth for estimations - Mobile devices can have limited resources and more likely to have network issues, so constantly polling the last N blocks to get an estimate it's not ideal from a mobile wallet perspective.  
10:53:31 From  Micah Zoltu  to  Everyone: Agreed, you only need the last block header.  :)  
10:55:07 From  RicMoo (ethers.js)  to  Everyone: You can call getBlock(“pending”)?  
10:57:01 From  Micah Zoltu  to  Everyone: `eth_getBlockByNumber('pending')`  
10:57:20 From  Juan Blanco  to  Everyone: ^^  
11:00:03 From  Micah Zoltu  to  Everyone: Summary from me (not everyone agrees): Don't use third party APIs, just use a 10 line function copied from Ethers to calculate base fee and priority fee from data returned from Geth.  :D  
11:00:38 From  RicMoo (ethers.js)  to  Everyone: (The method that will also be used internally to ethers ;))  
11:01:16 From  Juan Blanco  to  Everyone: Will you make that a gist part of the EIP  
11:01:31 From  Barnabé Monnot  to  Everyone: Could the API return recent block fullness then? Rather than past priority fees  
11:01:36 From  Barnabé Monnot  to  Everyone: Or both ;)  
11:04:17 From  Santiago Palladino  to  Everyone: Histogram of BaseFees may be more useful, and fullnes can be inferred from baseFees fluctuating up or down  
11:04:32 From  Barnabé Monnot  to  Everyone: True!  
11:04:53 From  RicMoo (ethers.js)  to  Everyone: Thanks everyone! :)  
11:05:23 From  Tim Beiko  to  Everyone: https://github.com/ethereum/eth1.0-specs/blob/master/network-upgrades/client-integration-testnets/calaveras.md  
11:06:13 From  Franco Victorio  to  Everyone: What is that param for syncing geth with calaveras? I didn't catch that  
11:06:23 From  Marius  to  Everyone: --calaveras  
11:06:24 From  Caleb Lau  to  Everyone: In geth it's --calaveras :)  
11:06:31 From  Franco Victorio  to  Everyone:Oh nice haha  

---------------------------------------
