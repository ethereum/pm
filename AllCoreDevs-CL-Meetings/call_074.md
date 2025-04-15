# PoS Implementers’ Call #74 - 2021-10-21
### Meeting Date/Time: Thursday 2021/10/21 at 14:00 GMT
### Duration: ~0.5 hours
### Agenda: https://github.com/ethereum/eth2.0-pm/issues/239
### Recording: https://www.youtube.com/watch?v=5vGxLoTUqaQ
### Moderator: Danny Ryan
### Notes: George Hervey

## Table of Contents:
1. Altair
2. Client Updates
3. Merge discussion
4. Research updates
5. Spec discussion/Open Discussion/Closing Remarks
6. Chat highlights

*Highlights are curated and adapted from the [Quick Contemporaneous Notes](https://hackmd.io/@benjaminion/HyjI-xy8K#PoS-Implementers%E2%80%99-Call-74---2021-10-21) by Ben Edgington.*

## Meeting Discussion

Danny: Okay, I have created [an issue](https://github.com/ethereum/eth2.0-pm/issues/238) in the eth2.0-pm repo, which we did not rename in the great renaming because we plan on deprecating it. But, I haven't. And I made an issue named “deprecate this repo” so i've publicly committed to doing so by the middle of next month.

I just need to figure out where to put the old information and move into the other pm repo, announcement. But until then we're using an issue in the old repo. Issue #239, call 74. Let's begin.

## 1. Altair
*Highlights:*
- *If you run a node, you must upgrade now!*
- *[nodewatch.io](http://nodewatch.io/) indicates that 62% of nodes have upgraded. [See this doc for a breakdown](https://notes.ethereum.org/@djrtwo/altair-nodes-upgraded).*
- *Leo has compared the results from NodeWatch and their own crawler. Main differences seem to be down to networking/peering, leading to seeing different peers.*
- *Note that there is an EthStaker watch party for Altair.*


Danny: Altair is happening. I know that everyone in this call knows, but if you're listening, altair is happening. If you run a node validator or not a beacon node, you must upgrade unless you want to run the old chain. But otherwise, you must upgrade.

I did create... I scraped some data from nodewatch.io, which has when possible collecting the client version, and I summed the altair versions against the total and the dock i just shared with you shows that by node count -- by node count that nodewatch.io can find which i believe between the couple of crawlers you know there are some disparities so this is not canon but at least from what we can see from this tool -- 62% of nodes have upgraded. And then depending on the client type, it's a bit skewed. Looks like Prism's 58%, Lighthouse 73%, Teku 86%, Lodestar 100%. And Nimbus, for some reason that crawler is not getting the node the client version. Maybe it's being obfuscated, but I have not dug into that.

So I think we're in reasonably good shape. That doesn't map to the validator node weight but that has increased. A couple days ago, it was less than 50%. So, I'll be keeping my eye on that. 

Through the weekend if you have connections with node operators, if you run a staking community called east taker, if you have a twitter,... sound the alarm. It's time to upgrade.

I guess we wanted to get on this call and make sure everything's fine with respect to altair. Are there any issues or anything people would like to discuss as we move into next week? 

Leo (BSC): Alright, just one comment, danny.

Danny: Oh yes.

Leo (BSC): We launched an experiment with comparing the results of both crawlers, nodewatch and our crawler, in the same node running from the same moment. And we let it run both for 24 hours to see if we get the same results or not. And we observe quite a number of nodes that differ. So, we look at the source code of them and see if they were using another technique to categorize nodes but actually it's exactly the same that we do.

So our conclusion was that most likely there is a kind of networking difference on the way we peered with nodes. And so, we started looking into it. We looked into the IP addresses of those nodes that we recognized differently, and we noticed that there were a bunch of nodes that we saw that they don't see, and there's a bunch of nodes that they see that we don't see.
And that's basically the origin of the differences. And we looked at it and we also noticed that for the nodes that they see and we don't see, they have all also other fork digests. So it kind of looks like they are not only peering with mainnet nodes, but maybe other networks and so that may be that's show the difference.

Danny: So that would but that would show one direction of the difference, right? But there's the other direction of the difference where there's nodes you see and they don't, correct?

Leo (BSC): That's correct, and we noticed that there was a couple of uh small bugs in our case where when we peer afterwards for a second time with the same node that we already recognized in the past, but for some reason, the connection drops. Then we switch it as unknown but in a wrong way because we already knew the information of that peer before. So we corrected that, but
those nodes were like very -- I mean the numbers were very small -- so and they don't account for a significant part.

Danny: Okay, so that might be the culprit. So, we can take this offline, but I really appreciate you looking in. Hopefully, we can get some lockdown on the numbers in the next couple weeks. Thank you leo. Other altair related items as we move into next week?

I know that EthStaker is doing a watch party. Sometimes a number of folks do so if you want to
join the festivities you can take a look at that.

## 2. Client updates
*Highlights:*
- *Lighthouse - Working to get Merge interop branch merged into main/master/stable. Discussion in LH issue #2715 around payload construction. Michael Sproul is continuing to work on fingerprinting and diversity analysis of clients.*
- *Nimbus - Release 1.5.2 ready for Altair. Improvements on the REST API, increased default limits; improved throughput. Peer selection improvements.*
- *Prysm - Can now sync with the Merge testnet (Pithos). Checkpoint sync and Web3Signer support in progress. Improvements in code health, tech debt. Working on standardisation of validator key management.*
- *Teku - Option to use different ports for TCP and UDP. Updated to JDK 17 support. Not yet released support for API 2.1 and not merged support for liveness endpoint for doppelganger protection. Ready to support publishing system metrics to a remote service. Moving Merge code over to the master branch. Fixed a sync committee bug on the Pithos testnet.*
- *Lodestar - Interopped with everyone at the Merge event. Latest release is ready for Altair. Now compatible with forkmon. Improving memory and CPU performance. Better discv5 - faster discovery. Demoed light client at Liscon.*
- *Grandine - Altair is generally working OK after completing experiment around multiple runtimes. But mixed findings - will write them up. Now focusing on Merge interop.*


Danny: We can run through some client updates and start with Lighthouse.

Paul Hauner: Hello, thanks Danny. So we've been working to get the merge face-to-face branch merged into our main branch… kind of splitting off little PRs and bringing them in to just slowly get into master (branch) or what we call stable.

We've been engaging in some discussion around the roles of payload building for the beacon node and the validator client, so we've been doing that on issue #2715 on the lighthouse repo.

It seems that the current favored approach is just for the BN (Beacon Node) to drive most of the process. After the VC issues are kind of subscription-type-VC as the VC issues subscription-type-message. Yeah if you're interested in implementing that, then maybe checking out that issue is something worth doing.

Michael Sproul's been doing continued work on client fingerprinting and diversity analysis. And we're also wiring up some significant bandwidth usage improvements for the next release. Just been working on a couple of breakages in rusted p2p, but i think that we're pretty close to being done with that. That's about it from us.

Danny: Excellent, thank you. And Nimbus.

Mamy: Hi, so we released the nimbus 1.5.2. That was ready for Altair yesterday. Not urgent for 1.5.1 users but for the others we need to upgrade immediately.
Otherwise we had several improvements on the rest api. We increased the default limits so that you can make bigger requests. And also we improved throughput especially for people who make a lot of historical data. And also improvement on the networking side and peer selection side so that you can have less peers and with cycling faster into peers to disconnect phones that are less useful to us.

Danny: Thank you. And Prism.

Raul Jordan: Hey guys, Raul here. Yeah definitely missed all you guys at the face-to-face and that liscon. Nobody was able to attend from our team, but we're really looking forward to going to more events starting early next year. 

Prism can now sync with the testnet -- with the merge testnet. That's been a huge milestone for us and we're pretty much all ready for altair. We shifted work into other things. We're hunting for bugs in the merge testnet support, trying to improve the experience of running prism with geth and trying out other other execution clients as well.

Aside from that, we have been completing checkpoint sync and starting to integrate support for web3 signer, which is going to be important for multi-client, for client diversity. Code health is also top of mind so we've been working a lot on just improving the code health of a repository reducing technical debt when we have this downtime between altair and starting work on the merge.

Aside from that, we've been also thinking a lot about validator key management api standardization and thanks a lot to Dapplion (from Lodestar) for the design here. We're looking forward to supporting the standard in prism which will make it a lot easier to build kind of like multi-client web web interfaces installation interfaces. A lot of people rely on the prism web UI in critical capacity and especially for onboarding and importing their key stores and getting started. So, we foresee this as being a huge huge boost and usability for everyone. That's it for us. Thank you.

Danny: Thank you. Welcome to the testnet. And Teku.

Enrico Del Fante: So yeah, we did a couple of releases last week introducing options to specify different ports for udp and tcp for p2p, and we added the jdk 17 docker support and duplicated the jdk 514 and 15 because we are not getting new security updates anymore.

We also upgraded to blast 0.3.6. We actually then broke Windows release and forced us to actually roll back in the quick release after that. So what we've done also, not yet released, is implementing the api release 2.1 which includes the new header for specifying the consensus version. And what is not yet merged is support of the liveness and point for double ganger protection. And since we had some problem for this release in terms of windows support, we are working on better release management for detecting potential problems for windows release,
especially in general for native leap dependencies. And we are ready for supporting publishing system metrics to remote service and mostly working on moving merge data from merge code from merge interop branch to master which is a long process. 

And for the ptos testnet, we fixed the one bug related to this in committee participation rate and we rolled over a new teku version on the testnet and works good so far. That's it.

Danny: Got it. Thank you. And Lodestar.

Dapplion: Hey, everyone. Dapplion here. First of all, the emerging drop was a great success. Great vibes. We interop with everyone including javascript only execution and consensus which was very exciting.

Just a reminder, version 30.0.31 and any subsequent versions are ready for Altair so update.
We also fixed some issues and now we are compatible with Portman. Looks like we can interop everyone find there, too. We are still working on improving memory efficiency and cpu performance improvements both in Altair and in phase 0. Then also improve some tcp 5 integration. Now we can discover the weight vps faster. And yesterday we presented at Liscon the lifeline rest based demo that we have been working on, so super exciting going forward. Thank you so much.

Danny: Yeah, thank you. And Grandine.

Saulus Grigaitis: Hi. Saulus from the team. So finally we completed this experiment with multiple runtimes and we have Altair working. It looks like generally it works okay but there are a lot of interesting findings and some are not so great and some are better. I think I still need to write a bit bigger description about our experience with that and the next we’ll be focused on The Merge and interop. So that's all.

Danny: Great. Thank you. Yeah I'm curious to hear the one of the things and maybe you see over time is, just like that i'd be concerned about is, say an optimization that is worthwhile to back port and then you have to decide if you want to backboard to all run times.

Saulus Grigaitis: Oh yeah this is uh i would say the one of the reasons why we tried this we thought that well if all the hot fork is faster, then we should not touch it anymore. But it turns out that's not always the case. And yeah it felt like initially it's a great idea. But later we thought that well some optimizations and so on and and some similar things are a good back part. That's one thing. The other thing actually what we found really, really surprisingly hard is the transition process when you spin a new runtime and it needs a lot of context from the old runtime for your previous forum. And this is something that we underestimated really. So I think I'll just try to write a bit more about that.

## 3. Merge discussion
*Highlights*
- *Pithos continues to run, and teams are working on issues and stability. Transaction count on the network is low. Contact Proto or Pari for some testnet ETH to test transactions.*
- *Engine API: Aim to release a stable target for the Merge specs at the end of October. Most of the core is stable. Should be near mainnet-ready in November.*
- *The beacon chain upgrade just ahead of the Merge event could probably benefit from its own name. Eth1 and Eth2 upgrade namings should be independent.*


Danny: That'd be great. Thank you. Okay, moving on to the Merge discussion. Obviously we did not have this call two weeks ago because of the amphora interop and there's been plenty of write-ups about that.

Moving forward there were a number of, based off of discussions there, a number of alterations to the specs primarily in the simplification and a lot to do with the x engine api. I've been chipping away at that. And Mikhail just got back from vacation today so we will both be chipping away at that with a target to complete all of those changes by the end of October so that we can release a new stable target of specs.

Then, you can follow the changes in the active development branch on any of those three components: consensus layer, execution layer, and engine api. But that is not what pethos is targeting. And so it will also change a lot. It will continue to change over the next week.

But, moving out from there, we do plan on having kind of a new testnet target at the end of November based off of this stuff. Nothing's radically changing and most of the core functionality is stable, if not, some communication a bit simplified.

Other merge related items today?

Something that Paul brought up is naming. Right now we kind of call the whole thing the merge. But then we call the time at which the beacon chain upgrades its logic, but the merge hasn't happened, the merge fork. And then we kind of call the point at which the transition occurs the transition process. But it's also a bit confusing because the whole thing is called the merge you know, the merge fork, the merge transition process. And there was a suggestion to maybe
name the upgrade. It would also avoid the name collision with merging PRs which is kind of funny.

I don't know the proper path here on picking a name. It also collides with the naming process on the execution layer. There's a bunch of conversation in the merge general channel. I don't think we're- we're not going to come to a conclusion today but any thoughts to share that were not shared in the merge general channel on naming?


Mikhail Kalinin: We will have a new name for the merge fork on the beacon chain, right? Like it's the next name of the name of the next star or whatever language we use. 

Danny: Yeah so by default that's the path I think, so we could pick a B name. But then we have to think about what is the interaction between that and the upgrade on the execution layer. Does this
envelope the naming scheme over there? Or is this additive to that name over there?

Mikhail Kalinin: Yeah it's whereas it's more difficult. Like, what are the upgrades that involve consensus execution layers simultaneously will look like and how should they be set up, of course.

Danny: Yeah because we also very well might have upgrades that are just on one layer, you know? If just the EVM changes in the future. So, Beetlejuice Shanghai, Tim said no because Shanghai's been reserved for a different fork, but we could kind of keep the naming independently and have it additive as the sum total. Beetlejuice serenity thank you light client (haha). That's also not my intentional spelling. The intention of the spelling is after the name of the star, not the mad character.

Micah Zoltu: Well, that's boring.

Danny: I guess, but then Beetlejuice is also a long name. I'm only saying that because it's the only star name that has a “B” that I know off the top of my head. That's not the name.

Okay, maybe take this offline. Maybe we talk with the people on the other side of the aisle and see if we can come at least to a compromise on how these names are related. And then if we do pick a star name, we can pick some nice ones. And then either do an emoji vote or bring it to the call and see if anyone has some strong opinions.

Any other merge related items?

TL;DR being pithos is up. People are iterating and making things more stable. Specs to be done at the end of October. And then we'll have kind of a new meta spec that targets the stable versions of things moving into november, with the intention of these being near mainnet-ready specs and really only changing them if issues are uncovered between then and later.

Protolambda: About the pithos testnet, the transaction count is currently very, very low. Parithosh and me both have some ETH to disburse. I do believe that maybe one or two clients are not quite ready for our transactions at the merge interop event. It does certainly affect the state's roots in some ways, right? So it's just another way. Looks good on the surface. So far, it's been running well. I think we can handle it. So if anyone would like to have some test ETH for transactions then please just reach out and we'll start distributing some.

Danny: Cool, thank you brother. Okay, going once. Going twice. Anything else Merge-related for today?

## 4. Research Updates
*Highlights*
- *Need to consider future API changes that withdrawals might affect, so as to keep the API stable.*
- *Look out for future updates.*


Danny: Okay, any research updates that people like to share today?

Protolambda: Well there is just one fork more perhaps, the withdrawals. So I think that at least we should look at potential future api changes that the withdrawals may cost so that the engine api is port compatible so you know how it might change.

Danny: Right, and a lot of that centers around a push first pull on withdrawals into the execution layer, which I think there's a rich conversation to be had around that.

Protolambda: Right. For context for others, the funny thing is that deposits on rollups are the same as withdrawals in ethereum 2, where you move something from the consensus layer into the execution layer. We could try and unify these types of things. We don't have to. And then, there are nuances as well where it's not exactly the same, so maybe we shouldn't.

Danny: The primary id being there if we do make the functionality look pretty similar, then the engine api can be reused in a different context to drive rollups, which is nice.

Protolambda: The push model is basically a new transaction type on the execution layer and an addition to prepare payload methods to be able to introduce a transaction into a block that's suggested by the consensus layer instead of taken out of the memory pool.

Then the alternative is the pull model where the consensus layer keeps track of withdrawn from the validator. And then the execution layer allows you to mint ETH based on the commitment and based on another transaction, not a regular transaction to some special pre-compiled contracts that can process the withdrawal.

Danny: Right, where the formers probably if you can get it right -- maybe a more elegant design --, but at first look has a bunch of edge cases around, especially when those withdrawals are headed towards smart contracts which consume gas, and there's a question of who pays for the gas.

Protolambda: In developed contexts, you can think about this in two ways. You could have a deposit that doesn't trigger the EVM. It just increases the balance so that you don't have these edge classes. But then you also probably still want the other side as well so you end up with two types of transaction, or maybe some kind of flag within the transaction.

So, if you have some kind of fee payment for the minimal thing where it doesn't trigger EVM. It just increases the balance, or maybe not at all but just some limiting to this in the contents there. You can at least have this type of deposit or withdrawal transaction. But then if you want the contract interaction you get into a hairy situation with fee payments and with all your cases in the EVM.

Anyway, keep an eye out for future updates after the merge while they're designing this api.

Danny: Yeah, absolutely and I think once we get the merge spec stable at the end of the month, that's one of my priorities is to begin to specify and engage on the different designs on this.

Alright, any other research updates or points of discussion?

## 5. Spec Discussion/Open Discussion/Closing Remarks
*None.*

Danny: Great, any other items to discuss today? Open discussion, closing remarks, etc.

Great, well thank you for joining. If you're at Liscon, enjoy and we will talk to you all soon.
Upgrade in six days. It's exciting. Thanks everyone.

-- End of Transcript --

## Bonus: Chat highlights
**From danny to Everyone: 03:02 PM**
- https://github.com/ethereum/eth2.0-pm/issues/239
- https://notes.ethereum.org/@djrtwo/altair-nodes-upgraded

**From Arnetheduck to Everyone: 03:05 PM**
- nimbus does not include version in libp2p connection header

**From danny to Everyone: 03:08 PM**
- https://github.com/sigp/lighthouse/issues/2715

**From danny to Everyone: 03:09 PM**
- https://twitter.com/sproulM_/status/1451065804183662592

**From danny to Everyone: 03:17 PM**
- https://notes.ethereum.org/@djrtwo/ryF6iOY4Y


## Attendees
- Ansgar Dietrichs
- Arnetheduck
- Ben Edgington
- Danny Ryan
- Dapplion (Lodestar)
- Enrico Del Fante
- Hsiao-Wei Wang
- James He
- Leo (BSC)
- Lightclient
- Mamy
- Mehdi Zerouali
- Micah Zoltu
- Mikhail Kalinin
- Pari
- Patuz V
- Paul Hauner
- Pooja
- Protolambda
- Raul Jordan
- Saulius Grigaitis
- Tomasz Stańczak
