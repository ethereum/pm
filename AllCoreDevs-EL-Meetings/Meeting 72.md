# Ethereum Core Devs Meeting 72 Notes
### Meeting Date/Time: Friday 4 October 2019, 14:00 UTC
### Meeting Duration: ~ 45 mins
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/129)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=rPD2EpDDI-0)
### Moderator: Tim Beiko
### Notes: Pooja Ranjan

----
	
# Summary
	
## DECISIONS
	

**DECISIONS 72.1**: Ice Age EIP will not be included in Istanbul. It seems like there's no major reason to do it now. Based on James calculations, it should give us well enough time to plan for another fork and not delay Istanbul.

**DECISIONS 72.2**: Bring your objections to AllCoreDevs in 2 weeks if anyone have anything opposing to Geth team defining Eth 64 as Fork ID thing and rolling it out. Ref [EIP 2124](https://eips.ethereum.org/EIPS/eip-2124)




## ACTION ITEMS

**ACTION 72.1**: Cat Herders to reach out to the Gorli team to make sure that there are clear communication about node upgrade for Istanbul.


**ACTION 71.1**: David Palm will talk to Wei Tang to see if 2200 should be self-contained. 
 


	
-----

**Tim**: Welcome to core developers meeting 72.

# 1. Ropsten Istanbul fork re-cap

**Tim**: First item is Ropsten fork recap, if anyone wanted to give just a quick update about what happened there?

**Peter**: Essentially, Ropsten fork came 2 days earlier than expected. It was a surprise, but it turn that somebody is mining Ropsten with about 1.5 Giga Hashes. Some of these pushing was really hard. It came a little early that scared us because it looked like the fork failed. Then it turn out that the fork did succeed. The problem was this miner who was pushing with 1.6 Giga Hashes Ropsten, is actually pushing the non forked chain. So we have a huge miner on non Istanbul currently.
For past couple of days we've spent trying to figure out what happening in Ropsten because the network currently is really unhealthy. It boils out to the fact that most people did not upgrade yet, so most of the nodes are non-Istanbul nodes. Since there are really heavy non-Istanbul chain, it makes upgraded nodes minority; thats quite annoying to upgrade currently.
It did surface a few issues. Currently, what's happening are non upgraded Istanbul nodes are eclipsing the upgraded one. 

For **Geth** specifically we do have a flag. If you run with that, it will filter out the non upgraded chain and it should be ready to go. I am not sure for Parity.  But long story short it's a bit of an issue and **we have a few proposals about how we can avoid this scenario in the future** but for Ropsten it's already too late to the retrospective to add those fixes. For Ropsten, we need to ride the way until the Istanbul chain gets heavier than the other one or enough people update. Until that, its firefighting mode. You can run Geth with this distinct flag.  Other client , I am sure they can give you some help to get on the correct chain. 

**Martin**: I want to add a bit to that. So, the last time we worked on Ropsten,  it caused some problems. This time no one from dev community actually reached out. On the previous occasion,I thought it was a really really good tests on how to handle chains but had bad feeling from the dapp developers. This time around, it doesn't appear someone actively complaining from an infrastructure perspective I think, it's super interesting to see this - how clients behave when they are for longer side chains within the block. As Peter said, we've a couple of proposals. One of them has some new issues, features that we're going to implement them to make Geth handle the scenarios better. I think its really valuable and worthwhile to actually do this as a force. It brings a lot of stuff out for attention.

**Peter**: Just adding one liner thing, that even though Ropsten fork currently was a bit of a shit show **there are really no worries** that a similar thing might happen **for mainnet**.  Since we don't expect mainnet to be all of a sudden pushed by a 10x miner on a non forking chain. 


**Tim**: Thanks for the recap, Martin and Peter. Does anyone want to add comment about this?

Okay, just to be to be explicit about this, even though there were some issues on Ropsten,  all the other testnets were still going forward as is. There's no specific action were taken aside from the changes and the proposal you want to implement but those don't change the other testnets, is that correct?

**Peter**: Yes. Currently, there are two more testnets that I am familiar with - Rinkeby and Gorli. Both these testnets are proof of authority testnets. **In Proof of Authority testnets, only majority chain can progress. So, either you have non upgraded chain or you have an updated Istanbul chain progressing, but you cannot have two concurrent one.** So, from this perspective, **Gorli and Rinkeby are completly immune to the issue** that happened to Ropsten. 

**Tim**: Got it. At the very least, we can message clearly to people, to validators that they really should upgrade.
This is as action item for the Cat Herders to follow up and make sure that there are clear communication about that. There was one [blog post](https://medium.com/ethereum-cat-herders/istanbul-testnets-are-coming-53973bcea7df) already written about the testnets on the Cat Herders blog, we'll make sure to get that spread widely. Anything else?

**Peter**: About contacting validators, Gorli team probably has a list of people they need to think. As for Rinkeby, the foundation is running three validators. And we've four more validations running by Oracle, Augur, Akasha and not sure who the fourth one is now. We can definetly reach out to them. We are also regularly monitoring the status updates on the Rinkeby stats page. So, Rinkeby is probably safe. As for Gorli, that's up for the Gorli team to reach out to make sure. 

**Tim**: Great. Let's keep this as an action item for the Cat Herders to reach out to the Gorli team. Anything else on the testnet upgrades?



# 2. [Reminder: "Ethereum Roadmap 2020: A Community Discussion" @ Devcon5](https://docs.google.com/document/d/1pD9RxQcgI4hBoOWGWlVwg4JqNS19_YIUnr3HsftHtE8/edit)

**Tim**: Second point on the agenda was just still a quick shout-out to do for Ethereum roadmap session at Devcon. So this will be on the first day of Devcon. Basically all of the afternoon will be split into a session to discuss Eth 1 roadmap, then Eth 1 to Eth 2 roadmap and then Eth 2 roadmap and then I think there's some time at the end of the afternoon as well for working groups form or want to discuss specific ideas. If that's something that you're interested in, it would be great to have a lot of people from the core dev side as well as the broader community side to discuss these things. Anyone has comments, thoughts about this?




# 3. Ice Age

**Tim**: Okay so next point on the agenda was Ice Age. I think Hudson had a comment about whether we should plan to delay the difficulty bomb in Istanbul or in the following fork called Berlin. In more general way to know, do we have any idea when the difficulty bomb will start being activated again and when we have to diffuse it?

**James**: I have some, should be verified, back in a hand map that I've done. As last year T. Jay Rush and I did really investigated the difficulty bomb and hackathon and then worked with Vitalik and Lane  to make a script. So there is a [script](https://ethresear.ch/t/bump-bump-boom-the-story-of-how-the-time-bomb-will-affect-you/4367) somewhere floating around that predicts it, alright. It predicted it fairly well. From my memory, it took about 12, I'm just checking back historically it took about 12 months for it to start showing up last, at 14 months when it started showing up last time. And given that we're about half the hash power, it should take longer for it to show up and it did last time. The absolute hash power actually showed, has it show up earlier or later relative to those numbers. So given that it's in the April May June July range that we might see something.

**Martin**: Oh I thought it's sooner, because the previous postponement said that if I recall correctly, the next time would be like this coming winter. So, you are saying, it's not until Spring then? 

**James**: When the fork was implemented on March 1st, the last time, when at least the block time went down. As I said, I need to go back and figure that out. I'll figure out how far we pushed it back? I think we pushed it back even farther than we did last time, as well.

**Danno**: We went from 3 million blocks to 5 million blocks, I think.  Byzantium was 3 million, Constantinople was 5 millions.  Really push it back  2 more million blocks, which is roughly a year. 

**James**: Okay, so then yeah it would be still in the March but it should show up slower because the hash rate is so much less than it was last time

**Danno**: That was gonna show up earlier with less hash rate.

**James**: From my research before because it adds the hashrate before, the block hashrate before and the current one, then actually the large the magnitude, more of an effect it would have. So it showed up earlier and more aggressive last time because it hash rate was so high, compared to the time before. So this time, is the hash rate less so it will show up later and less aggressively.

**Martin** :I pasted the [link](https://eips.ethereum.org/EIPS/eip-649) to the [EIP]( https://eips.ethereum.org/EIPS/eip-1234). It says in the rationale what they calculated back then , they that it would hit 30 second block time by the end of 2018. Sorry, that's not the latest one. 

**Danno**: But I think the takeaway whether it's a month, one way or the other. This is something we need address probably in the first quarter.

**Martin**: yeah 

**Peter**: I just after that, I think Hudson's question was where we want to address this in Istanbul or not? Unless it is extremely urgent to do something, I would really be against doing it in Istanbul because we already defined What Istanbul is and Ropsten is already forked. So if we start to redefine what Istanbul is then the Ropsten fork is invalid unless we do another Petersburg #2 too. To do a double fork on mainnet and hotfix fork on Ropsten. So unless there is actually a reason to push the delay soon, I wouldn't.  And also we were talking that it would be really nice to do Istanbul - II in a couple months, named Berlin, but is a tentative name for it and it's supposed to have it. The idea was that it's not a hard for that's open to adding everything rather a very focused hardfork for adding cryptography and we can always say that ot gets the cryptography plus the delay and done. Or alternatively we can try to go down mark and  suggested pathway of preparing the EIPs and forking when something is ready. Either way, I wouldn't do it in Istanbul. 


**Tim**: Yeah **it seems like there's no major reason to do it if James calculations are remotely correct, it should give us well enough time to plan for another fork and not delay Istanbul**, does anyone disagree with that?

**Peter**: Well, I guess is if the Ice Age cannot to be even felt currently, not even a bit then, I don't think we should be in a too much of a rush.

**James**: The delay of the last fork also, I think would affect our initial target of around Christmas or whatever because it ended up going out two months later, almost. So the year would still be March to year mark.


# 4. Testing updates

**Tim**: Okay. So, the next agenda item was testing updates. I saw there was a comment about the consensus tests and it tagged both Martin and Danno. I don't know if either of you have an update?

**Danno**: All the tests except for the 220 test that Martin and I put together and merged into reference tests now. There is one concern about particular random state test 94. Clients just need to be aware, it's going to consume about a trillion gas when you run it. SO, to run in parallel, it's gonna consume too much memory and issues like that. **Reference tests for everything but the 220 are committed**.  

**Tim**: Great, any other comment on testing?

**Martin**: I can add **small update about fuzzing**. It's been keeping fuzzing stuff millions and millions of times and I found nothing so far. 

**Tim**: Okay thanks, Martin, Danno.
I see we also have Lewis on the caller who joined I don't know if you wanted to bring up anything specific?

**Louis**: Not really. 

**Tim**: Okay, so next item on the agenda is reviewing action item so before we do that does anyone else have anything they would like to discuss or bring up?

**Martin**: Would now be a good time about **Fork ID**?

**Peter**: Oh yeah! It's just a panic proposal. Although the idea would be to get some feedback on it.
Long story short, one of the issues with Ropsten, the reason it is having a hard time doing anything is because network wise the forked network, before the pool of forked nodes and the pool of non forked nodes have no idea whether peer is forked or not. The only thing, currently they can do is try to advertise each other's for chains to blocks to each other and they download it from each other and then they realize that okay, something deep something deep down is not compatible or some block is invalid. The problem is that if we don't do anything to somehow separate peers from each other at the more lower level, at the networking level; then it just puts a really nasty strain  on the whole block processing, block validation everything. Way back we had a proposal, we did it with Felix about a half a year ago. 
So, when two peers do a handshake with each other currently, they exchange the genesis block. I mean the hash of the genesis block. The idea was that this way we can have multiple. The problem is that this one cannot detect if two peers share the same genesis block but then forked away from each other. Kind of like Ethereum and Ethereum Classic or Ropsten or Istanbul etc.   The idea was that instead of exchanging the hash of the genesis block, we should exchange something else that contains both the Genesis hash but also all the old forks somehow mashed together. Ane we figured, which Felix came up with this idea of Fork ID, which is just to check some of the genesis hash along with all the fork block numbers and the proposal. We had an EIP, it's already accepted and versioning.


My proposal would be to publish a new version of the Eth protocol so essentially bump the Eth protocol to Eth 64 and the only change would be to replace this Genesis hash in the handshake to this fork ID and what it would allow us to do is when  two peers connect then even if they have the same Genesis block they will immediately know  whether they are compatible or incompatible with each other fork wise. If this would have been implemented on Ropsten currently then the two networks, the ones who didn't fork into the Istanbul and the one who forked into the Istanbul, they would have separated really cleanly at the networking level and then all of this messy synchronization log processing problems would have been solved.

I think it's really an elegant solution. If anyone wants to take a look, please take a look. I linked the [EIP 2124](https://eips.ethereum.org/EIPS/eip-2124). The  proposal is just replacing a single field in a handshake. The question is - does anyone have any objection publishing an Eth 64 version well, since Eth name space is the officially theorem protocol. We just don't want the Geth to publish the version unilaterally and say that this is the verion 64. But we would really like to do so and it's really a more or less trivial change. That's why we're kind of optimist that **the effort to implement it is really tiny and the benefits will be huge, specially for testnets**. Of course even if we do implement it that would definitely keep speaking the old protocol side by side. So, it's not that we want to roll out something incompatible rather, it would be just an updated version. 

So, action item does anyone have anything opposing to us defining Eth 64 as this Fork ID thing and rolling it out?

**Danno**: In Eth magician there is a [thread](https://ethereum-magicians.org/t/forming-a-ring-eth-v64-wire-protocol-ring/2857)
so any position there was a lot of other ideas for sort of things that are going to Eth 64. Stuff relating to like - archive versus partial nodes, doing things like not sending out the log bloom on the transaction message produced burden on the wire protocol. Should we consider if there is  anything that's easy to put in and it's quick as well or do you really committed to just having this being a one feature change Eth 64 and moving all those suggestions to a neat 65?

**Peter**: The problem with the suggestions in general is that there are lots of suggestions and I don't know in which impact state those suggestions are in? Example, we also have an idea for new synchronization protocol which would be really nice to have but it's not yet fully spec out. So I don't mind adding anything else that is fully spec out and fully agreed upon. The reason I was suggesting to go with this single change because we have test cases, we have everything and it's something that is easy to roll out and it's something that's needed.  I'm really open to adding other stuff but I don't want to start a whole research thread and the one year delay just because, we don't know what else to add or how to add them. So, anything that's ready, we can add but stuff that's not ready, I would postpone to Eth 65.

**Danno**: Right, I think a deadline on that would help a lot. Ready by now, we ship in 65 sometime in next year.

**Martin**: I don't really agree. I mean it's not like coordinating hard forks where everyone has stopped it simultaneously. As long as there are no conflicts, that the Geth team defines 64 this way and then someone else defines it differently, then there is a problem. But other than that as long as we coordinate, okay 64 is this thing, and 65 is this next thing. I don't really see a problem with doing many releases or any versions simultaneously.

**Peter**: One advantage of doing 64 just as a tiny thing and a 65 as the next tiny thing is that it's a lot easier for a client to implement and make sure that it works and then in come the next thing and make sure it works versus if we create an Eth 65 or Eth 64 that contains a ton of features and it's just really hard to make sure it's implemented correctly that clients agree on it etc etc.

**Danno**: That make sense.

**Peter**: With the same theory,  I would also say that if we can make smaller releases to the protocol, smaller version bombs then that is probably a bit healthier. I'm a bit partial because I do see some urgency in networking aspects whereas the rest of the things are kind of niceties or optimizations that definitely should go in. For example transaction propagation is another thing which should be solved but it's not an immediate urgency. Whereas this whole network thing stresses the network every time we do a fork.

**Danno**: Yeah, it would be nice if we could possibly ship it before the main Istanbul.

**Martin**: I mean, we can ship it on Monday. 

**Peter**: This one will probably won't have any effect on Istanbul. If we add this extra field in the  in to the handshake and then peers can decide that they are on the different chain that also implicitly  means that people who did not upgrade they also need to be able to speak this new protocol. SO, essentially, if  you don't bother upgrading then you won't have this update which allows you to do this fancy handshake.

Essentially, what I am saying is that this won't fix Ropsten and this won't fix Gorli and Rinkeby. On mainnet, if people update and the mainnet fork won't happen, for I don't 1-2 months then it might help  a bit. But realistically it's probably help for the next Hartfork. 

**James**: So, a change like this does need to be paired with a hard fork or it doesn't need to be?

**Martin**: Does not. We retain backward compatibility on Eth 63. But if any one wants to speak Eth 64, then we change the fork ID. 

**Peter**: Currently, the problem with Ropsten are with nodes that didn't upgrade. If nodes don't upgrade then they won't have this Eth 64 either to solve the problem. 
That's why I am saying that it is a solution for a future Hartfork. I mean it will help a future hardfork when everybody in the network will actually be running Eth 64 already. 

**Danno**: I don't know if I want to say yes to it, 
but I like it and probably bring it up next week.

**Tim**: Is it worth also just posting on the All Core Dev Gitter?

**Peter**: We posted it a couple of days ago.

**Martin**: Yeah it's been posted to the PM and it's been a public for half a year and  accepted.

**Danno**: I think what's needed is probably the post and say **we're  going to shipping 64, just this change. Bring your objections to call for core devs in 2 weeks.**

**James**: Maybe if we treat it like the EIP fork eccentric process that if there are things that are currently ready to be added in, then they can be talking about the things that need to get ready to be added in should be a different conversation.

**Peter**: Yeah

**Tim**: I guess share this proposal in AllCoreDev and Eth magician and see if there's any comments in the next two weeks. Otherwise we can accept it in the next core dev call officially. Does that make sense? 

Anything else anyone wanted to bring up?

# 5. Review previous decisions made and action items
* [Call 71](https://github.com/ethereum/pm/blob/1d012e2942234d6c035a95f8cd68b7f450b97de8/AllCoreDevs-Meetings/Meeting%2071.md)

**Tim**: I would be going over the action items.

**ACTION 71.1**: David Palm will talk to Wei Tang to see if 2200 should be self-contained. I don't know if anyone has any update there ?
It will be considered as continuing action item.

**ACTION 70.2**: Ethereum Cat Herders to create a communication that describes all changes and highlights the concerns around EIP-1884 and provide it back to the All Core Devs for review before it is put out to the community. This document will be released when every client has completed the Istanbul updates and has a block number.

That was done. Adding  [link](https://medium.com/ethereum-cat-herders/istanbul-testnets-are-coming-53973bcea7df) in chat in case anyone hasn't seen it yet. 
# 6. Client Updates 

**Tim**:  I don't know if there's any client or testing or research updates that people want to share?

## Geth
**Peter**: I do have one update. It's completely independent of Istanbul. We did Geth v1.9.6 release a couple of days ago. Among them quite a few fixes, we actually tweaked Level DB a bit. If you do fast sync, this tweak reduces your disk i/o by half. If you do full sync, it reduces by a factor of ten. It reduces disk I/O by entire order of magnitude. We are happy about this.  so if anyone wants to watch the benchmark it and see how how Geth performs, we are really curious to see the numbers out in the wild.

**Tim**: That's impressive.  Any other updates?
Okay, then I guess that's it.

**Pooja**: Next Core dev call?

**Tim**: Two weeks from now, same time.  
Thanks everybody.
a) Geth
Geth release 196
b) Parity Ethereum
c) Aleth/eth
d) Trinity/PyEVM
e) EthereumJS
f) EthereumJ/Harmony
g) Besu
h) Turbo Geth
i) Nimbus
m) Nethermind



# Date for Next Meeting: Friday 18 October 2019, 14:00 UTC

 
	
	
# Attendees

* Daniel Ellison
* Danno Ferrin
* James Hancock
* Louis Guthmann
* Martin Holst Swende
* Péter Szilágyi
* Pooja Ranjan
* Tim Beiko



## Links discussed in call:
* https://eips.ethereum.org/EIPS/eip-649
* https://eips.ethereum.org/EIPS/eip-1234
* https://ethresear.ch/t/bump-bump-boom-the-story-of-how-the-time-bomb-will-affect-you/4367
* https://ethereum-magicians.org/t/forming-a-ring-eth-v64-wire-protocol-ring/2857
* [EIP 2124](https://eips.ethereum.org/EIPS/eip-2124)
* https://medium.com/ethereum-cat-herders/istanbul-testnets-are-coming-53973bcea7df
