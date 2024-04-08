# Execution Layer Meeting 184 [March 28, 2024]
### Meeting Time: Mar 28, 2024, 14:00 UTC
### Meeting Duration: 1:33:02 Mins
#### Moderator: Tim Beiko
###  [GitHub Agenda](https://github.com/ethereum/pm/issues/982)
### [Audio Video of the Meeting](https://www.youtube.com/watch?v=cSQmbCVwGUk) 
### Meeting Notes: Metago

# Agenda

## Mainnet Missed Slots [1:30](https://www.youtube.com/live/cSQmbCVwGUk?feature=shared&t=90) 

**Tim**
Okay welcome everyone to ACDE number 184, we have a bunch of stuff to cover today. First we'll talk about what happened on mainnet over the past day or so, then there's a couple things we missed last call that were important so I bumped them up to the top of this agenda to make sure that we can cover them, so the state growth work by the Paradigm team and then there to retroactively apply the EIPs that we wanted to finalize, but have bumped for two or three calls now, and then just quick shout to the Dencun EIPs and what I suspect will take the bulk of the call, is talking about Pectra, so there's some updates on 2537 which is included around gas costs.

Mike had some updates about the questions we had around inclusion lists last time. Alex can you please stay muted? Thanks and then yeah we have a ton of EIPs that people wanted to discuss and provide updates for Pectra, we'll see how much time we have left when we get there but I think at the end we probably want to time-block a good 15, 20 minutes to actually hear from the different client teams around what are we including in the fork and trying to build for in our first devnets because we already have a couple things and I think having a finalized scope as at least a first set of devnets will be valuable. So yes to kick us off, mainnet missed slots.

So we saw a bunch of those yesterday Terrence before the call you mentioned it as well, so do you maybe want to share an overview of what you saw and we can go from there?

**Terrence**
Yeah definitely thanks for having me, so what happened yesterday was that well let's go back to how consensus work so block reference blobs but if today we see reference on the block but if the block never arrived in that case the block will never be imported so basically on that case the block is missed, considered to be missed by the client, so we have seen few of those before even last ACDC last Thursday, I mentioned it, on average we see 10 to 20 of those instances per day.

So we have been looking here and there and then we basically come to conclusion that we have seen those gossip from older client implementations, we have seen those gossip from older builders so we kind of suspect it was an ? issue. So anyway so let's has a question yeah so those blobs are never been seen so essentially yes they are never arrived at least from my nodes’ perspective, it could be dropped earlier already but from my node I've never seen those blobs.

Okay so let's go back to yesterday what happened was I guess there was heavier blob traffic I think at the highest point we see like 53 gr per buy so that's basically 10 times more blob rate then basically what we had two days ago so I think at the high point it was at 1/4 of the code data price just to give a reference on how much higher it was and because of those blobs are appearing more frequently and because of those then we are seeing more instance of that so at the high point we're seeing like 20 to 30 those type of blocks basically they never have blobs so we cannot import those so they kind of result in like two to three missed block for each and then it has becoming a lot more alarming, so we kind of send a few telegram message to basically the relayer to the Builder and then what happened at the end was that block Rod turn off their relayer and everything started working again so right?

Right now there's a strong evidence this is a blocks Rock BBN issue so because of the BBN they basically drop the blob somewhere along their network and so basically their relay has been shut up until they figure it out so we hope to see a postmortem from them soon at the end from the client there's this beacon API basically to prop get blocked and then we're also hardening that implementation to make sure that blob can still be propagated even the blog has been seen on the network.

So yesterday's blob wasn't so much about client couldn't handle that type of workflow because I basically that all the missed blob will costed by the block RW issue there's probably 99% of it so but then there is still that fundamental issue that okay what happens under yesterday's traffic. I suspect client yes may import block slowly before but that's something that I don't really have a strong evidence on, that's something that still remain to be seen but yeah that just an update.

**Tim**
Thanks I really appreciate the context there's a question in the chat from Pari mentioning whether we should re-evaluate how the circuit breaker works in this case, because I believe the current heuristic is five consecutive slots and obviously we didn't quite hit that yesterday.

So yeah anyone have thoughts on this?

**Terrence**
Yeah so I think even for the circuit breaker it wasn't close to hitting that I think maybe the circuit breaker is too loose but then again if you make the circuit breaker too loose then it kind of becomes able basically people can just trigger the circuit breaker to basically force the next slot validator to go to local building I think perhaps there I mean I know Alice Stone has been talking about implementing more relayer specific circuit breaker say that today if you see a missed block from a certain relayer and then there's some proof and then you basically disconnect with a relayer, but there's a lot of work to be done there.

**Danny**
Yeah I agree that if you go more fine grain than the circuit breakers are now they have to be specific, which there are probably there are certainly proofs and messages that can be passed around there are probably actually heuristics that could be calculated locally without passing around additional information, but those aren't going to catch on.

**Tim**
I guess this is maybe a naive question but why not make it Epoch based rather than consecutive, like we know in practice I understand why at the merge we wanted it consecutive, but I think now given what we know about the makeup of the validator set and you know the different builders, could we do something like find the 95th percentile amount of missed slots in an epoch and trigger it there?

**Danny**
It becomes such an attack vector if I turn off you I turn off that boost for everyone then you know I can keep my boost on and get way more profitable blocks so anything in that direction becomes very attackable and even the consecutive ones that we have right now like five consecutive that could be just outwardly bought by a malicious relay and turned off for everyone so I just I think that if we go any more fine-tuned, it just it probably has to be actor specific.

**Tim**
Got it my take anyone else have thoughts on this?

**Peter**
Do we agree that this is serious enough that something should have happened because as far as I can tell actual users of the network weren't significantly affected so are we happy to say that this is bad but it's not so bad that emergency shut off foul should be kicking in?

**Danny**
I kind of went in that direction honestly, barring independent actor shut offs

**Tim**
Potuz?

**Potuz**
Yeah besides my obvious comment about BBS I wanted to mention two different things about this incident. One of them is that most probably the fact that there's lack of client diversity within relays, have made this happen. Second is that Terrence has been talking about these blobs for over a week and no one paid attention to this and once it exploded, it only took a couple of phone calls to get to the right relays to actually look at their logs. This I think is unacceptable and yeah those are I guess my main two complaints about this that Terence has been talking about this and calling everyone and we even talked about this in ACD and relays didn't pay attention to the fact that they were losing those blocks if we could look at those logs or if those logs were made probably public, we could do that work.

**Tim**
Got it thanks. There's a comment by Alex I get two comments in the chat one by Alex saying you know we should wait for the Postmortum that before making any decisions on a solution that's reasonable and then there's also a comment by Ansgar around the way 1559 works right now makes this worse because 1559 is block fee or is block based rather than slot or time based so it sort of doesn't know about the missed slots, so this is also something that we've considered in the past but that we should potentially consider in the future is you know if we switch 1559 to time based, then it can take missed slots into account a bit better.

Okay and some comments that we should have probably had a more formal written warning about this somewhere.

Where's the best place to just follow this conversation? I know Alex it seems like you were working on relay specific circuit breakers you know if people want to follow this better where should they go?

**Alex**
Yeah the MEV Boost Community call would be one option I think many of us here will push blo raut and others for postmortem which will share in the usual channels. Yeah.

**Tim**
Okay anything else on this? Ansgar? 

**Ansgar**
As well but I was just curious why the default behavior is not for Builders to release blobs once they see their block signed on the peer to-peer because at that point Alex said unbounding concerns but at that point basically the content of the block is already leaked so even if you have worries that you might be too late anyway with releasing the blobs at that point for the blob to be accepted at least you have a shot whereas the contents of the blobs themselves are not the sensitive part, so I'm curious why that's not default kind of fallback Behavior.

**Stokes**
The builders could do this especially if they've seen the block signed but I'm not sure clients are written a way that support this out of the box.

**Danny**
The contents of the blobs also could be sensitive 

**Stokes**
that's an assumption they could have but if the block signed then the exchanges happened so it's fine after that.

**Danny**
Oh yeah no I know but from an unbundling perspective.

**Tim**
Sure okay yeah because we are kind of packed agenda wise I think we can probably leave it at that, have the conversation on a MEV Boost Community call and then if people who attend that can just share any sort of postmortem or things that come out of it with the rest of all core devs that would be great I the time based 1559 at the same time but okay let's move on,

## [State Growth Research](https://www.paradigm.xyz/2024/03/how-to-raise-the-gas-limit-1) [15:33](https://www.youtube.com/live/cSQmbCVwGUk?feature=shared&t=933)

Next up, we had the R's team has been looking into State growth and put out a really good article going into the details we've wanted to cover this for one or two calls but didn't have the time so I wanted to make sure we got to it today.

I don't know georgos or storm either of you yep storm is on the call storm feel free to take the stage or screen.

**Storm**
Hi there let me share the screen and store worth train okay is my screen visible slides?

**Tim**
Yes.

**Storm**
Great so hi everyone I'm storm I'm a data scientist and data engineer at Paradigm and so I work a lot with the ref team and something that we think about all the time is how do we use data to navigate different design trade-offs, so whether we're trying to decide the optimal value for some parameter or we're trying to decide between different architectures, data often plays a huge role in those decisions.

So today I want to share some data relevant to Ethereum scaling road map and specifically on state growth and history growth and we think this data could be pretty helpful for figuring out if or how Ethereum should scale beyond its current level. So Ethereum is a really complex system has many different bottlenecks on how much it can scale. This is a rough sketch of how we've been thinking about the problem so starting at the top we have the gas limit that's the ultimate governor of things like block size and Ops per block. Downstream of those things we have our familiar bottlenecks like history growth and state growth and each of these bottlenecks has its own relationship to the nodes hardware constraints.

So each box here is a pretty deep rabbit hole and today I'm just going to touch on a subset of it so starting with State growth a couple weeks ago georgeos and I put out this research blog post walking through some State growth data so today I'll touch on those results and then after that I'll go through some of the results for our next blog post, which is on growth.

So this right here is a view of how all state on Ethereum is currently being used the total State size is around 245 GB on dis for bre at least and the size of each rectangle here represents the portion of those bytes occupied by different contracts or contract categories. So for example ER c20s are the biggest category and they take up around 67 of the 245 GB and this isn't too big of a surprise but the biggest contributors to state are tokens. erc20s and ERC 721s this is because every user balance of every token typically requires its own storage slot and there's a lot you can learn about Ethereum just by staring at this graph if you want to play around with it, this is an interactive visualization in the blog post and you can sort of just click around and find your favorite protocols in there but to keep it brief I'm just going to move through these charts pretty quickly, if you'd like more detail feel free to reach out to me or georgos.

So that was a chart of the state distribution this is a chart of the state growth over time and showing the relative contributions from each contract category so here every vertical bar represents one month since Ethereum's Genesis and the y axis is the number of gigabytes that the state grew during that month so you can see that state growth peaked around 6 Gigabytes a month at the end of 2022 and now it's currently around 2.5 gigabytes a month which is actually the lowest it's been since 2021 you can see that the main reason that state growth is down is the decline of nft usage shown in blue here.

And state growth from erc20 has actually been increasing every year for the past few years and that's shown in green so if we take the integral of State growth we can see the total State size over time starting at Zero from Genesis and going all the way up to the 245 GB that were at today and state hasn't been growing exactly linearly but it's kind of more linear than you might expect even going back four or five years so from this we can make a rough projection of how big the state might get in the future and there's a lot of assumptions you have to make in order to do this, but under a very simple model we find that existing consumer hardware can sustain current rates of state growth for a very long time probably decades, and note that I'm only talking about storage capacity and memory capacity here, this isn't saying anything about the reads or the rights to State under this framing I'm considering reads and rights to be part of State access, rather than State growth. This is also not saying anything about what would happen if the gas limit were to change. So State growth we often think about as a pretty big bottleneck on Ethereum scaling but from these numbers I'm actually not super worried about state growth in the short term or the medium term, however the thing that makes me very uncomfortable is history growth and I think history growth is kind of a silent killer that hasn't gotten as much attention but even after 4844 I think it's going to be a major problem and so maybe my hottest take of the day is that EIP 4444 history expiry should be given very high priority for inclusion in the next hard fork and maybe even sooner than that if it's possible, and we should also be looking at other EIPs that reduce history growth like 7623 pretty closely.

So diving into some data this is a graph of Ethereum's history growth rate over time and like the last graph the y axis here is showing the number of gigabytes that history grows during each month for each contract category. So a few things pop out here, one is that the history growth rate is much larger than the state growth rate by almost an order of magnitude. Another is that the main driver of history growth is bridges which here includes l2s and rollups and then finally until the last month or two history growth the history growth rate has been rapidly accelerating for many years now, and note that since this is the rate of growth, if the rate of growth is increasing then the total amount of history can increase very rapidly.

So if we take the same graph and normalize it to 100% we can see the relative contribution from each contract category. Something pretty interesting here is that there's been kind of four distinct epochs of how Ethereum has been used over the years. So in the beginning, first couple years very little is happening on chain almost nothing relatively speaking and of what is happening it's pretty hard to identify a lot of these early contracts it's kind of like archaeology, but then around 2018, 2019, we see the rise of ERC 20s. Around 2021 2022 we see dex's and D5 become the dominant use case, and then in 2023 bridges become the largest use case.

So this is a good illustration of how things have become more and more complex over time. So one of the big questions you might be thinking is how do blobs affect history growth and if rollups are the biggest contributor to history growth, will 4844 dramatically reduce history growth? So this is the same chart as before except now we're zooming in so that each vertical bar represents one day instead of one month and you can see that after Dencun, history growth from bridges has fallen by about 50% and overall history growth has fallen by about one third.

So history growth is still quite large but it's also a pretty rapidly evolving situation, everyone saw all the craziness that happened yesterday with blobs so it's something to keep an eye on before we get a sense of how The Blob Dynamics will play out in the long term. So I'll wrap it up with a comparison of State growth and history growth and how they compete for node resources. So as I mentioned before, history growth is a much larger storage burden than State and the problem is not just that history is big, it's also growing really quickly even after Dencun. So within just a couple the storage burden for a full node is on track to surpass 2 terabytes and this is mostly due to history growth.

But there's a direct fix for this which is EIP 4444 history expiry. So this current graph shows where we're going right now and then here I'm adding in projections of how 4444 affects the storage burden so the main difference with 4444 is that nodes would only store a Year's worth of History, so at steady state the history storage burden transforms from the red line into the pink line and then the total storage burden changes from the black line into the Gray Line and you can see that this makes a massive difference to the storage burden and makes things more sustainable for the next few years and beyond this we should also look pretty closely at EIP 7623 to reduce the history growth rate and Tony has done a lot of good analysis on this and you should check it out if you haven't seen it. 

So this research is still a work in progress, we're still in the middle of analyzing other scaling bottlenecks and trying to tie it all together with the gas limit, we also want to analyze the of l2s with the same methodology and see how they might be different to mainnet. So that's all I have for today, again one of the main goals here is to leverage data to help improve the design of Ethereum and the node clients, so if there's any variation or followup to this data that you think would be helpful please reach out we'd be interested in possibly collaborating we're going to publish a few more blog posts on this topic and we're also open sourcing everything that I showed today so thanks for your attention and thanks to all the people on this call that have already given us a lot of useful feedback.

**Tim**
Thanks, thank you excellent work and yeah thanks for sharing the sneak peeks on the history side as well, we had a question from Andrew who has his hand up. 

**Andrew**
Yeah, thank you storm for the great presentation and I know that you haven't gone into the state access yet but I'd just like to comment that one problem that I see with the state size is not only the storage requirements but also that the bigger the state the slower the access to it because it all boils down to something like a B+ tree and the complexity there is logarithmic right so you will like if you have a huge State then each access will be slower. Yeah, that's the only thing I'd like to note. 


**Storm**
Yeah, completely agree we're still figuring out the best way to sort of measure and benchmark that but it's definitely something we're thinking about.

**Tim**
Thanks any other questions comments? Okay, Oh Lucasz? 

**Lucasz**
Yeah so one comment from me. I totally agree with the conclusions that EIP 4444 and the call data cost increase should be prioritized and thank you for a great analysis. 

**Tim**
Thanks, great. Ahmad?

**Ahmad**
Yeah, one idea here that pops to mind that there was a lot of discussion behind dropping serving these historical blocks from P2P network or not and there was some people that are not big fans of having some nodes being able to serve these historical blocks there are rival nodes in some other not being able to serve them but as a temperory solution to each something that….a good archival storage 4444s, maybe having something like this is a good transitionary stage. 

**Tim**
So what would be the transition stage exactly?

**Ahmad**
So given that clients can drop blocks that are earlier than certain points, let's say merge or deposit contract or something like that, if we agree on a certain point that all clients can drop before, some clients can drop these blocks and some other nodes could opt into keeping them for whatever reason, and they can also opt in to keep serving them on the P2P network if they want to. 

But this will make the P2P Network some nodes have all the blocks and some nodes will be able to serve part of the blocks and there's an EIP that I proposed earlier that will solve also this issue, of finding the peers that will be able to serve you the blocks that you need.

**Tim**
Right. I think yeah that definitely seems reasonable as like a path to full removal. I think if we were to do that I would almost call that like deprecated you know like kind of like we did with self-destruct where we in the fork before we flagged that you know it was going to go away so you could have something similar here where you say you know as of this point serving say pre merge block data is optional and you know some clients might choose to do it but you should assume it's deprecated and then you know as of a fork after that or whatever then it becomes gone by default but there seems to be some push back about this in the chat and Danny you have your hand up.

**Danny**
Yeah, I just want this Point's brought up many times without doing that and having an alternative distribution method that new freshly clients syncing can utilize, like I don't know torrent, portal, whatever there's just a concern that the quality of service to sync a new node could significantly degrade during that transitionary period. I think if one or two of these distribution methods are well specified and have high quality service then you could have a decreation period but without that then you're just putting the kind of the syncing of new nodes in a very tough place during that period.

**Tim**
Okay and Ahmad, did you have another comment? 

**Ahmad**
Yeah, I would just like answer Danny and some of the comments so like my idea here is not to keep this forever that we can have this only as a transitionary period till like we have a solidified archival solution. Another thing is that the rate that nodes will start dropping historical data is not as high as we think it will be. Existing nodes will not suddenly after the fork decide, okay I want to prune all of this history away right now, and data will become unavailable in a single day. I think most of the nodes will opt into keeping the current configuration, keeping the history, until they actually need to start pruning because their drive for example does not fit any more data. 

**Danny**
I might agree with some of those assumptions. I just doing that transitionary period and having an unknown time horizon I think is potentially dangerous if there if it's stepwise and there the assumptions are stated and the time frame is known then I think it could make sense.

**lightclient**
I kind of feel like we have a path forward and it seems a little weird to me to try and take a different path as an intermediary step when we kind of know what we want the long-term future to look like. It's just a matter of rolling out supporting era, figuring the last things that need to be figured out about how this supports the era format, post merge and then rolling those types of things out 

**Tim**
Right. Then given we have the error format for pre merge block I think last time we discussed this the rough plan was to try and set up some out of network retrieval scheme whether it's Torrance or portal or something like that and then have clients start using that sometime this year and then start serving like pre-merge blocks start serving pre-merge blocks on that Network this year and potentially stop serving them sometime next year on the peer-to-peer Network. I guess yeah sorry go ahead.

**lightclient**
I just say that's that's kind of how I think that we should proceed.

**Tim**
What's the best way for people to follow this like is it in the Discord?

**lightclient**
 The Discord Channel History expiry.

**Ahmad**
Is it called State expiry or history expiry?

**lightclient**
History expiry and execution R&D.

**Tim**
Okay. I think we could probably continue the conversation around history expiry there. Any other final questions on just the overall presentation before we move on?

## Retroactive EIPs [7610](https://ethereum-magicians.org/t/eip-7610-revert-creation-in-case-of-non-empty-storage/18452) [7523](https://eips.ethereum.org/EIPS/eip-7523) [37:00](https://www.youtube.com/live/cSQmbCVwGUk?feature=shared&t=2220) 

Okay well yeah thanks again storm and George for putting this together, this is really good okay hopefully we can get through these next couple things quickly so these two retroactive EIPs, first one was 7610 we discussed this a few calls ago, and there were some questions around whether this would be compatible with Verkle or not. I don't know if anyone's looked into that or what the current status on this one is.

**Gary**
Yeah I think it is compatible with Verkle because we have this consideration that if we switch to Verkle, is there any easy way we can determine if the account has empty storage or not, so in order to solve it so according to the current repo spec because there is no notion of storage route anymore so it might be a problem, but in order to solve it, we can choose to discard the useless storage during the Verkle transation, specifically if an account has zero nonce and zero runtime code then the storage can be discarded and it is totally fine as because run time code is zero so this storage are not accessible and we have 28 accounts in total eligible for it on the ex mainnet so by doing this like if we can, no account will be eligible for tracking this special scenario that the destination of the deployment has nonce storage and yeah and also after the transactions the EIP can be disabled automatically, because in Verkle the storage route returned is always empty, so this additional condition is basically useless and the client team can choose to remove it or it's also fine to keep it, so yeah, I don't think it's a blocker for Verkle.

**Tim**
Guillaume?

**Guillaume**
Yeah, so basically everything that Gary said is correct I mean it does, that the EIP effectively auto disables itself with Verkle. I remember a couple weeks ago someone was asking how would 5806 affect this and I remember discussing it with Hadrian. I think he's here but our conclusion although I don't remember the details so I hope he's here but our conclusion was that it would not happen because you can't really create accounts, you don't have storage, you cannot write storage when doing delicate transactions, so I think that we are completely okay to move, but I see that Hadrian has his hand up so I will give him the floor. 

**Hadrian**
Just confirming what Guillaume just saying is that if 5260 was to…any point…phrasing of the EIP states that you cannot use any op-code that sets storage…nonce…in the context anyway, so that’s EIP would not be used to set state under any OA so it doesn’t conflict with…Verkle assumptions nor with this EIP.

**Tim**
Got it. Thanks. Peter?

**Peter**
Yes, so a lot of these issues come from there being a bunch of like slightly annoying edge cases of accounts that couldn’t exist because they are very old. In particular, a lot of these problems have gone away because anything created after spear Dragon was deployed, the nonce got bumped to one if it was contract created and I think what I am hearing, there is a reasonable case for taking the opportunity of the Verkle transition to remove the…cases by lumping the nonce of the account that have storage and deleting storage for contracts with no codes and no nodes

**Gary**
Yeah, so I would choose to remove the storage because they are useless and very safe to delete.

**Peter**
I think its also worth pointing out that like this edge case only exists in the case of a ludicrously implausible intentional attack on Ethereum so we should be designing our semantics here based on what’s easy for clients to implement as reasonable rather than like what makes the most sense for people doing it intentionally because someone's probably attacking Ethereum if this ever happens. So for example if we delete the storage during the Verkle transition, it's possible that someone has the ability to deploy code at that address, because they found a hash collision and what happens will depend on whether they do that deployment before or after the Verkle transition. Normally I would be against any such behavior but given that I don't think this is likely to happen at all, and yeah I don't think it's a thing we should be worried about, we should just be like what's the easiest least complex thing we can do that results in all clients having the same behavior.

**Tim**
So one thing to clarify is, is the Verkle complexity effectively would be part of the Verkle EIPs or is this something we need to consider in the case of 7610. My understanding is this is something we would include as part of Verkle to deal with this like to sort of deal with the consequences of this but just is that correct? 

**Gary**
I think it can be applied right now and whenever we switch to Verkle we need to think about how to

**Tim**
Okay I guess in this case does it seems like all this like potential concerns have been addressed and like even though we might need to figure out the right you know the right interaction with the Verkle transition there should be a way to do it and it's just a matter of how rather than if, does anyone like oppose just retroactively applying this EIPP from Genesis? Okay no objections.

[44:37](https://www.youtube.com/live/cSQmbCVwGUk?feature=shared&t=2679) 
And then we had another similar EIP, so sorry what's the number, 7523 this is Peter's EIP which basically cleared some empty accounts that were missed in the Spurious dragon hard Fork did this before the merge and so the EIP makes the assumption that there are no empty accounts on any post merge Network or network which applies this or sorry or which applies Spurious dragon at Genesis and I believe we've had two people verify that Peter's script was correct yeah Peter do you want to add more context?  

**Peter**
Yes, so this is the EIP that says there are no empty accounts after the merge and that we no longer defines behavior in the presence of empty accounts. Everyone operating in a post-merged context should proceed on the assumption that empty accounts simply can't exist. This allows deleting of a large number of test cases, removing special case code, and avoiding edge cases that can never occur. It's useful for everyone.

Yes, at this point me and Marius and have both manually checked that there are no empty accounts in the current head or at any point after the merge. I think we can proceed with this. You could always do more checking, but I've not seen any demand for more checking. People generally think me and Marius are reasonable and diligent people who checked thoroughly. Does anyone object at this point?

**Lukasz**
Yeah, there is a question of is that true for other chains that are evm compatible right because if we define this as a evm thing and they are incompatible with that if they have any edge cases that occurred then that might be a problem for them.  

**Peter**
Yes, this is a good point. The thing to bear in mind is that to have an empty account, your chain must be extremely old. Creating empty accounts was abolished at the end of 2017 and effectively every EVM compatible chain is more recent. Any rollup is way more recent. I checked carefully and I'm confident the chains that can have empty accounts are: Ethereum (where they've been manually cleaned), robston (now deprecated), Ethereum classic (I manually cleaned all the empty accounts, though I haven't checked my work there), and some extremely old Ethereum classic test nets. My position is, given we cleaned things off ETC, I don't think we should block stuff on Ethereum because it might break something on an old ETC testnet. I'm confident every other context applies. 

**Tim**
There is a question about chains without adopted EIP 158.

**Peter**
As for chains without EIP 158, I'd have to look into that. My opinion is if you have EIP 158 at launch, you probably didn't have any empty accounts. I'll make a note to look into this but someone would have to tell me what these chains are. Yeah, someone mentions maybe Gnosis. 

**Tim**
Yeah, someone mentions maybe Gnosis. My sense is we've talked about this for over a year. If someone wants to notify Gnosis they can also run the same script we've run, on their chain and clear stuff. I think we should move forward with it and consider it…

**Peter**
…retroactively applied from the merge. 

**Tim**
Yeah, and I guess on this point I've been thinking so I think this is like our fourth retroactively applied EIP if I'm not mistaken and they're not really documented anywhere so I think I'll probably put together a meta EIP that tries to list those so that when we do make these changes that you know people should consider and have been like decided after a specific hard fork, they're at least documented somewhere so I'll put together a draft with the two EIPS we discussed today and then all the ones we've did in the past and I'll shout it out on all core devs in the next week or so.

Anything else on the retroactive EIPs? 

## [BLS Gas Cost;Update EIP-4844: Update blob base fee to base fee per blob gas EIPs#8316](https://github.com/ethereum/EIPs/pull/8316) [51:12](https://www.youtube.com/live/cSQmbCVwGUk?feature=shared&t=3072) 

Okay, so we have about 40 minutes left. There's two quick updates that we have to do that we quickly should cover on Pectra included or considered stuff and then a bunch of updates on potential EIPs. For everyone else who has updates on like the long list of stuff consider that you'll have probably one or two minutes to give an update on the most relevant new things and then we'll keep the end of the call to sort of discuss what should go in and how we scope the first devnets but first Marius you did some analysis on the BLS gas costs? Is he here?

**Guillaume**
Okay he might be on holiday actually. 

**Tim**
Okay so if he is not here anyone else have comments on the BLS gas cost otherwise I just posted the link we can continue the discussion async if there’s no comments or questions.

**Dan**
I think…

**Tim**
Yeah go ahead.

**Dan**
Yeah I was just going to say that we are going to do some benchmarking for the libraries that we'll be using in ref, which are going to be different than the ones that Marius posted in The Benchmark so yeah we'll post these in the Discord when we have them.

**Tim**
Got it thanks, Alex you're going to say something? 

**Alex**
Yeah oh first off just plus one to benchmark another libraries that'd be really helpful yeah so Marius did some benchmarking with his software stack. I think the document's pretty self-descriptive, there's kind of an open question around subgroup checks which is like this cryptography detail of the pairings and yeah just the update there is that work's underway and yeah it's moving along. 

**Tim**
Got it, any other questions or comments on that?

**Danny**
And the sub group check was the really expensive part and by work on to decide if it must be in there?

**Alex**
Right, so the way the EIP is written right now, there's subgroup checks that are essentially required for the pairing precompile they are effectively suggested or recommended for the others but they are very expensive so I know Antonio is looking at benchmarking them for these other expensive calls and then it kind of becomes a question of do we want to mandate them meaning higher cost for users or can we skip them and then you know it'd be cheaper to use but then you'd have to be more careful as a user to not you know shoot yourself in the foot so to speak. There might be a new version of these subgroup checks that are the best of both worlds where they're cheap enough and then also secure so yeah that work's ongoing.

**Tim**
Thanks.

**Dan**
Yeah one comment on subgroup checks, given that there's multiple libraries that implement these operations, we would have to, I mean the benchmarks for each of them will guide this I agree, but like if there's a newer faster one it's only implemented in one library then I'm not sure we can recommend decreasing the cost, for example but I guess that should be obvious. 

**Alex**
Yeah I mean the idea would be that every implementation would use the new thing. 

**Dan**
Yeah yeah 

**Danny**
I mean if they're off an order of magnitude that's obviously a place to look into.

**Tim**
Okay so we can keep discussing this async, and last question maybe we can just answer in the chat but someone's asking if there's any links or information they can to understand why we need the subgroup checks, so yeah someone has… seems like Dan has so thanks. 

## [Prague / EL Electra Proposals(updated list](https://ethereum-magicians.org/t/prague-electra-network-upgrade-meta-thread/16809?) [55:50](https://www.youtube.com/live/cSQmbCVwGUk?feature=shared&t=3350)

Next up so we have CFI the inclusion list CIP on the last CL call I believe and there were some concerns there that were raised around how it would interact with account abstraction and I believe Mike has an update on those concerns. 

**Mike**
Yeah hey Tim hey everyone thanks. I'll try and be pretty brief here I have one diagram to share to kind of help visualize this and I'll start by saying also Potusz has this doc, I'll paste it in the chat that also covers this issue really well so for more context I'd point the interested reader there. 

Hopefully you can see my screen so I'll just give a really high level view of this issue and then talk through these three options at the end which are three things that I think we can do to resolve it. So the context here is that we're the slot n plus proposer and we're deciding you know where to where to build our block as the or which block to use as the parent and this is our current view so we saw the slot n block and we saw, we basically like the proposal for 7547 is that the inclusion list is composed of two different like objects the first object is the summary, the second is the list of transactions. The point for doing like a summary instead of the full transaction list and committing to just the summary is to solve this free da problem which we talk about here I'll send this link to just so everyone has it.

Right so we saw the slot n block and we saw the slot n summary but we didn't actually see the slot n transaction list that corresponded to the summary and the way that could happen is if we saw the slot n plus 1 block which included the slot n summary and we confirmed that the slot n plus one transactions so this is kind of like part of the inclusion list mechanism is we ensure that the summary is included in the block and that the summary entries are satisfied but remember we didn't see the actual slot n transaction list that corresponded to the slot n summary. So now we're kind of here and it's my time to propose a block, it's slot n plus two and my fork choice says that slot n is actually the head of the chain so now I'm building on slot n for whatever reason let's just say slot n plus one didn't get enough attestations for me to consider it the head and in order for my block that I proposed to be valid, I need to include the slot n summary in my slot n plus two block, and I need to satisfy the entries in the slot n summary, but I can't be guaranteed that I have access to all the slot n transactions that were in the slot n inclusion list because I didn't see this object on the network.

So this is the kind of weird situation where if we don't resolve this then the slot n plus 2 proposer can't actually produce a valid block that is the child of slot n they would have to build on slot n plus one so yeah I guess there's a few issues here. 

One thing we can do and I guess so this is kind of we haven't even touched the issues around 3074 yet and so I'll talk about the three options and then I'll describe where 3074 fits in here. Right so one option is to reorg this slot n block to say okay we didn't see a transaction list for the slot n summary so we're going to reorg that block, that doesn't seem great. We could not accept the slot n block as a potential head of the chain in the fork choice view which is how we treat 4844 blocks so 4844 blocks we don't accept them into the fork choice view unless we've seen the blobs and then the third option is to reconstruct the slot n transaction list from this slot n plus 1 block, and this is actually where the 3074 issues come in, so the reason 3074 causes an issue is because without 3074 we know that the slot n summary transactions are either in the slot n block itself or they're in the slot n plus 1 block. 

With 3074 instead of the transaction from an account being included there's a chance that that account had balance drained by an external account and so in that case the satisfaction of the summary entry, I apologize this is complicated but yeah whatever I'm getting close don't worry, that account could have been drained by a different account and so in that case reconstructing the slot n transaction inclusion list is not possible from just the slot n transactions and the slot n block so this is the kind of issue. 

Yeah those are the three options and yeah I guess there's one thing that can make 3074 work with reconstruction which is if we can check not only that a transaction from the account has been included but if we can pull out the 3074 transaction that invalidated the transaction that was originally in the inclusion list then that works too and yeah so basically I think there is a way we can do reconstruction with 3074, but as Marius pointed out this becomes a slightly more complicated proposition.

So yeah I guess the last thing I want to say is that you know this does feel like it kind of creates some complications around the inclusion list design, but I do think there's three options that actually do work and I also don't think that there's going to be like a silver bullet to fix this, because this is like fundamentally an issue about how transaction inclusion works and how inclusion lists are designed, so like I don't think waiting yeah I don't think like we're going to find a better design that doesn't have these same issues that it has to resolve and we can make it work with 3074 specifically, which is a nice compromise the enshrine 4337 things become a little more complicated, but yeah since we don't know we're going to go for in shrin 4337 I think those realities can be worked out in a future scenario.

So yeah I think we can still do 7547 in Electra for those realities and because we do have three options to consider I think it'll probably be the type of thing where it's worth writing up a short doc explaining the details here but yeah that's kind of where I see the 3074 plus 7457 relationship.

So yeah sorry that was a little longer than I expected wanted to quickly shout out the people in the channel who've been working on this gender Matt Marius pan Terren Ansgar Daniel and Sean lots of attention on this in the past few days so hopefully we can get it resolved quickly. Happy to take questions online or off.

**Tim**
Lets take one question from Danny and then move one.

**Danny**
On the diagram if we have just to help my understanding say the slot n plus one block does not exist, I'm the slot n plus 2 proposer I see everything that I see except for that n plus 1 so I can't do reconstruction right so I don't even really can I even build on n at that point? 

**Mike**
Right at this point you wouldn't consider slot n valid, this block valid because it's the leaf chain so it's like it's the leaf block so it's a candidate for the head of the chain but it doesn't have a full summary accompanying with it so part of So part of, if it's a leaf block, it has to have a valid I/O. If it's not a leaf block, then you can maybe do this reconstruction thing.

**Danny**
But it's like, why does this case matter, right? 

**Mike**
This case matters because there is a situation where this block was the head and then it got reorg. So it's only mattering in the reorg case, so it's a bit of an edge. 

**Danny**
I'm just, I'm like, in the event that n plus two didn't see interesting because 

**Potusz**
without notable 

**Danny**
What was that Potusz? 

**Potusz**
Sorry. You can make an attack in which you build a block that is not reorgable. 

**Mike**
If slot n plus 1 gets built and is not reorderable, then that's a problem. 

**Potusz**
So, you send the IL to everyone, you send the I to no one, but you collude with the next slot Builder and then you guarantee that the next slot can just come and it's never going to be reorged. 

**Tim**
I'm sorry, but we are pressed on time. Thanks Mike for sharing the update. We can then discuss this in another breakout room. I'll move us to the big list. 

Candidate EIP specific updates](EIPs [5920](https://eips.ethereum.org/EIPS/eip-5920) [7609](https://eips.ethereum.org/EIPS/eip-7609) [2935](https://eips.ethereum.org/EIPS/eip-2935) [7545](https://eips.ethereum.org/EIPS/eip-7545) [EOP](https://github.com/ipsilon/eof/blob/main/spec/implementation_matrix.md)
[7212](https://eips.ethereum.org/EIPS/eip-7212)
[3074](https://eips.ethereum.org/EIPS/eip-3074) [7664](https://github.com/ethereum/EIPs/pull/8357) [6493](https://eips.ethereum.org/EIPS/eip-6493) [Issuance Curve Adjustment Proposal](https://ethereum-magicians.org/t/electra-issuance-curve-adjustment-proposal/18825) [1:05:30](https://www.youtube.com/live/cSQmbCVwGUk?feature=shared&t=3930) 

Try to keep it to about one minute, and I think all the EIPs here, except one, have been presented before. Assume that everyone on the call has context and try to focus on what is new and or special about each EIP and why it's relevant. Charles, you had two of them that we didn't get to last call, so 5920 pay opcode and then 7609 decreasing the cost of t-load and t-store. 

**Charles**
Hi, I'm Charles. I work on Viper. I want to present two UX-related EIPs. The first is pay. I brought it up on a few calls before, but basically, it allows you to send ether without transferring execution context. People have pointed out that you can use self-destruct for this, but we are trying to deprecate self-destruct, so I don't think we should depend on the particular semantics of how self-destruct works right now. 

I think it's a super important EIP because right now, in order to send ether, you need to transfer calling context, and this has resulted in a lot of bugs before. For instance, one of the reasons that the whole call gas schedule is so complicated right now is because of these artifacts from when send had a 2300 gas limit hardcoded or something, and if we had had pay, that just would have never happened from the beginning. 

So it prevents a whole class of re and other kinds of bugs related to calling context. In previous calls, the main, as far as I know, agreed that it should get into the EVM, but the main objection is that the testing complexity is somewhat high. That's the summary. 

Then for EIP 7609, this is a proposal to make the pricing of trans and storage cheaper and slightly more complicated. Excuse me, the second.

**Tim**
I guess any questions or comments on pay? 

**Sam**
Yeah, so on pay, that got some special attention a couple of weeks ago from the testing team and the eels team. We used it as our prototype EIP for testing the EIP process, and we actually have a bunch of tests and stuff written for it already, so we can help a lot with that. 

**Tim**
Got it.

**Charles**
If that resolves the testing objection, then I would really like it to be considered for CFI. Then, yeah, just, cly,

**Tim**
We can do the CFI discussion and inclusion at the end for everything. 

**Charles**
Just, oh, okay. Then the other one is transit storage pricing. I think that honestly transit storage was mispriced to begin with. Basically, it should be cheaper than warm storage for a lot of reasons. It doesn't interact with the database ever, it doesn't interact with refunds, basically, the rules around it, around the implementation are much simpler. There's some other weird things like in the current gas schedule, you can allocate a lot more transient storage than you can allocate warm storage slots, so this EIP fixes that. 

One thing I changed is that I added a little more analysis around how much you can allocate. So, there's one parameter coefficient in the EIP, which is currently set to one, and basically, the amount you can allocate grows sublinearly with respect to the gas limit in a single transaction. It grows roughly the square root of the gas limit, and it makes it cheaper in most use cases that you want and it adds better bounds for how much transient storage you can allocate. That's the quick rundown. I'm happy to answer any questions. 

**Tim**
Okay, if there are no questions, then let's move on. Thanks Charles for the updates. Next up, Guillaume, you had two related EIPs or at least Verkle adjacent EIPs. One about historical Block hashes in the state and then the Verkle proof pre-compile. Do you want to give some quick context on those? 

**Guillaume**
Yeah, I have a very quick presentation. I don't know if you guys can see the slides, but it's going to be very short. We had this EIP by toas and Vitalik about storing the state in the contract, turns out, so this EIP was stalled, but we discovered while running the Verkle test net that actually stateless clients need a way to be passed the block hashes to be able to execute the block hash instruction. So, we created a revival PR against that EIP. 

So, we're effectively completely hijacking this EIP. The short summary for this EIP or of the changes at least is that we changed the way the fork gets activated. It used to be number-based, but since then, we had the merge, so now we do time-based transition. We no longer store the entire history, we just store a ring buffer of 256 blocks, and there was this weird activation period where the fork would have happened but you could not use the block hash instruction using the contract just yet. So, we got rid of that, we made it simpler. 

We just say at the fork transition, we will simply copy the last one 156 blocks and that will be it. And why do we want it in Prague? Yes, it's required for Verkle, but we can sort of include some Verkle EIP this way, signal that it's happening and it's also useful even before Verkle. So, there was this proposal for by Peter around the time we were in Istanbul last year where, what I call light client diversity. 

So, instead of striving to get every fourth person to install a different client, we just make sure that whatever is the majority client just also works as a light client to a minority client to make sure there's no catastrophic supermajority bug. So, that's pretty much it. Why we want that now? Because it could be used even before Verkle and then due to the complexity of the Verkle change, it's also nice to be able to do some stuff that is light before the actual fork. And while I'm at it, I'm going to talk about 7545. 

The main reason is for like the main, the rational or the purpose of this EIP is to abstract the way smart contracts verify proof because we're going to switch from MPT to a new pre format. So, that means all the proof the proof format will change. I realize this is the informal version of my slide, so I'm sorry if it's a bit cryptic. The idea is we want to be able to handle the transition. We don't want every smart contract to have to guess when it's performing the transition. Just receiving a blob that is a proof of some state on one L1 or L2 allows, for example, L2 contracts to not have to worry about which proof format they have to handle. You can release one contract at any time before the fork without having to rush at the last minute to release the contract that can handle the new proof system right at the time of the fork.

Once again, why in Prague? Because we want to signal that Prague is the last fork before Verkle. So if we want people, especially L2s, bridges, and whoever needs to handle proofs, to be ready for Verkle and not have to rush, it would have to be released in Prague. People have the time to update their contract and make sure it's Verkle ready. That's pretty much it. 

**Tim**
Thanks. Vitalik, you have your hand up.

**Vitalik**
First, I wanted to suggest making the size of the buffer 8192 instead of 256. The reason for this is that, in practice, a lot of applications end up not using the 256 block hash precompile that has existed since launch. The window it provides is pretty tiny, less than an hour. Generally, we've had outages longer than an hour, and one week is generally accepted as safe for rollups. If we can increase the length to that higher number, applications would actually be able to guarantee that if something happens on chain, a user will be able to submit a proof of it before the time runs out.

**Tim**
There is some support for this in the chat. Because we're a bit pressed on time, we can move on. Generally, it seems there's support to match the params from 4788, which has 8192. Any questions on the pre-compile EIP? Otherwise, we'll move on.

Next up on the list, Danno, you wanted to give a quick update on EOF.

**Danno**
Sure. As far as the status of EOF, we're at the point where the specs are locked down, and we're writing reference tests and implementation. Bas is almost completely done, along with EVM one. There are just some issues with TX create they're going through some of what the final transactions might look like. The status of the others is RM, which reuses, is starting implementation. 

I know there are old implementations for Geth and Nethermind from the big EOF days back in Shanghai. They're probably not fully blank on that, but they do need to bring it up to date. That's mostly the status of EOF; people are implementing it, and we're getting reference tests written. 

**Tim**
Awesome. Any questions on EOF? Yeah, thanks for sharing the Matrix. There's a comment by R that they need to update that table. 

**Draganrakita**
It's a few weeks old, and I need to update on the progress with him. 

**Tim**
Awesome. Let's keep moving. Matt, you had two from your end, EIP 7212 and 3074.

**Matt**
Yes, that sounds good. Thanks, everyone. I'll be super brief. With 7212, it seems that with the RIPs and the kind of adoption on L2s, it would make sense to include this pre-compile on L1 as well. Just so we don't break any compatibility and we can make sure that wallet development stays the same across the two layers. That's kind of the same thing with 3074. 

Moving from... I spoke to some of the Marmoset team and did some due diligence on the consensus side as the Besu team on 3074 and 717212. Hopefully, moving to include those and show the support of those from this team to those. So, you know, I don't think we need to dive into the specifics of 3074 right now. But motioning for support from Besu. Yeah, that's it. I'll be very brief. Yeah, there's some support comments for 7212 in the chat from Geth and Reth. Anything else on otherwise on the 3074 point?

Prolo had the new EIP addressing what he believes is a new edge case. So, there's a draft for it, EIP 7664. Prolo, do you want to give some context on this?

**Prolo**
For sure, thank you for the time. This EIP is brand new; I drafted it yesterday. It's called EIP 7664. What this EIP does is enhancing the utility of access lists such that contracts can require a user to statically define a certain input to the contract. This is functionality we're losing with 3074, where previously you were able to enforce that the transaction input data matches the contract call data. 

So, by using access lists, we can allow contracts to require these inputs to be declared in a transaction without coupling it tightly to the account model or the call stack or anything like that. Also, this just generally, besides that decoration of inputs, fills the original motivation of the Berlin EIP 2930. The original motivation described that we can use this for statelessness or for these static analysis type purposes. This implements exactly that and doesn't add additional resources but fills this gap that 3074 leaves. 

**Tim**
Thanks. Any questions, comments? Yuav? You are muted.

**Yuov**
Hi, yeah. So, one question regarding you. Can you hear me? 

**Tim**
Yes, we can now. 

**Yuov**
Regarding the latest addition to 3074 with a supporting value, that's something that I, until yesterday, thought was safe enough. But yesterday's problem with blobs made me realize that there may be a problem. So, I wanted to bring it up, see if anyone has any comments. So, with blobs, we have an eviction protection policy where we don't allow a type two transaction to replace by fee a type three blob. But if we allow a 3074 to drain accounts to move Eth from accounts, how can we fix the policy for blobs so that we don't get a lot of blob evictions as a denial of service attack? 

**Tim**
Does anyone have an answer to that or thoughts?

**lightclient**
Why is it different than the current situation? Because you could today have a number of blob transactions sitting in TX pools and then work with a builder to build a block with a number of transactions from those accounts that are 21,000 gas transfers just sweeping the account balances out. Then all of those blobs become invalid. It's a bit more expensive today, but I think the fundamental attack still exists. 

Yeah, that's what I initially thought. But then I realized that the current eviction policy doesn't let you replace by fee on a blob. So, a blob is more expensive to propagate, but once it's been propagated, you cannot propagate another transaction from the same... 

**lightclient**
Can you definitely replace? You definitely can replace, but it's much higher. I forget the exact number. I think you have to maybe double the base fee of the blob. I think it was 2x, but you still are paying roughly the same amount because I don't think you have to 2x the priority fee for execution. I might be wrong, but you're only 2x-ing the blob base fee. So, as long as the base fee stays below, you're paying the same amount. 

**Yuov**
So, you're saying there there's no concern where invalidating a large number of blobs doesn't become significantly cheaper with a single transaction with multiple off calls?

**lightclient**
I think it becomes about three times cheaper because it's about 7,000 gas to go through the off-call process to sweep the account, maybe a bit more. So, you're saying 7,000 per account to sweep versus 21,000. 

**Yuov**
Yeah, except that with doing it with an EA transaction without 3074, you do need to pay much more for this 21k because you need to replace. The protocol knows that you are actually replacing a blob where here, the transaction doesn't have to pay any higher fee because it doesn't come from the same EA anymore. 

**lightclient**
The protocol, this is only a transaction pool characteristic. The protocol doesn't care if you receive a block. It's not going to enforce that the block that's coming in, that transaction, is paying enough to…

**Tim**
Okay, I think sorry guys, I'm talking about a private builder. We're, I think, we're gonna need to take this offline because we only have three minutes left. Yeah, but thanks for bringing up the concern Yuov. We can definitely keep discussing it. 

Okay, so there's two more quick ones to go over. One was, so I guess, Prolo, sorry, on your access key op code, the general feeling seems to be that people think it's interesting but need to review it a bit more. You wanted to also bring up the SSZ EIP?

**Prolo**
Right, I'd like to give some Layer Two perspective on the SSZ. So, this EIP has been discussed. Yeah, it's just that I think it's kind of underestimated where 3074 and the inclusion of this EIP, these things rely on transaction typing a lot. But then, there's a lot more to say for SSZ outside of this. You know, the new set of EIPs, specifically for transactions today, they're just very difficult to prove and to prove attributes of. 

This also applies to receipts. So, like, this proofing, this is a big deal for Layer Two, both for scale and for security. For scale, if you think about charting, like, we can sample data all we like. We cannot sample the EVM execution the same way. We're not there yet. So, what this means is that all these rollups, they're registering their data through the EVM and basically duplicating the registration of this blob data or, and then pulling information from Layer One is all going through the EVM. 

Well, this all could just be like a non EVM-operation. This could just verify through the commitments we already have in the Ethereum chain. So, the state today is basically we're forcing a certain bottleneck through the EVM, and we're duplicating data, and we are making it very difficult to prove the attributes that exist in the chain today, in the history. Now, we can fix this by just improving the merklization, improving the representation of this data in the history. And then, for security specifically, Layer Twos end up implementing all kinds of workarounds to verify the data today. These workarounds are generally less safe, less sane, really just a lot more complicated than they need to be. And so, this SSE fixes this by improving the layout of the data, improving the merklization of the data for all the types. And I think this is really important for the future of Layer Two, to be able to scale and to securely verify Layer One data. Thanks.

**Tim**
Thank you. We'll take one comment and then try to wrap up because I know we're already at time. Guillaume?

**Guillaume**
Yeah, just to add to that, sorry. SSZ merklization uses SHA-256 instead of KAK or KACK. I never know how to pronounce it, and this is also better for ZK. 

**Tim**
Thanks. Okay, we're already at time. I think I was hoping we could have like a bunch of time for client teams to share their preferences today, but we already have stuff included in the fork. Do people want to make a case for anything else being included as we work on the first Devnets? I think we can take one minute for that. 

Reading the chat 3074 seems to be the only one that's been repeatedly mentioned. There's been a couple mentioned of other things. Yeah, the people have a strong preference on making this decision now for some of the things. Do we prefer to push this back two weeks and give people more time to digest everything that happened today? Any strong preference? 

**Matt**
Maybe better to get some opinions now so we can start working on any prototypes we want for the dev nets.

**Tim**
Okay, I think yeah, based on the chat, I think it's probably better to wait two weeks to start. I mean, I don't think client teams have implemented everything that's already included so far. So, we can definitely start with that and then block off all of the next ACDC or ACDE, sorry, to discuss any additions. 

And I think yeah, in the next two weeks we should dive deeper into all the stuff that's been brought up today and aim to make a decision then. And I think anything, the implication is like I think anything that's like not fully figured out or specified two weeks from now is probably not going to make it into this fork if we want to move forward. 

Does that make sense to people? Okay, thanks everyone. I appreciate you all getting through all of this today. This was a big one. 

Yeah, so again, please review everything we've discussed, and we'll block off the first part, at least, of the next call for discussions around what's going in the next fork. Yeah, thanks everyone.

Attendees

* Tim
* Danny
* Terrence
* lightclient
* stokes
* Storm Slivkoff
* Pooja Ranjan
* Alexey
* Tomasz Stanczak
* jochem-brouwer
* Zoom user
* Mikhail Kalinin
* Carl Beekhuizen
* Andrei
* Peter Davies
* Guillaume
* Tori
* Etan (Nimbus) 
* Roman
* Marcin Sobczak
* Andrew Ashikhmin
* Saulius Grigaitis
* Roman
* Marek
* Danno Ferrin
* gakonst
* Justin
* Swanny
* Ben Edgington
* Anna
* Marcello Ardizzone
* Justin Florentine
* Ignacio
* protolambda
* Lokasz Rozmej
* Matt Nelson
* draganrakita
* Andrei Maiboroda
* Dan Cline
* Ansgar Dietrichs
* Mehdi Aouadi
* Hadrien Croubois
* gakonst
* Echo
* La Donna Higgins
* Ahman Bitar
* Hsiao-Wei Wang
* Vitalik



