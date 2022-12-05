# Consensus Layer Call 99

### Meeting Date/Time: Thursday 2022/12/1 at 14:00 UTC
### Meeting Duration: 1.5 hour  
### [GitHub Agenda](https://github.com/ethereum/pm/issues/667) 
### [Audio/Video of the meeting](https://youtu.be/KFc1sWYlVZ4) 
### Moderator: Danny Ryan
### Notes: Alen (Santhosh)

## Summary <!-- omit in toc -->
Summary | Description
-|-
99.1 |Capella: Recap of last week's All Core Devs call (of consensus stuff). Danny understands that we will keep withdrawals from EIP-4844 separate and slated for Capella. If they are implemented together, we will not combine the specifications, but rather stagger the upgrade. This was confirmed as the general consensus during the call.
99.2 |Testnets / progress updates: Operating two testnets (no EIP-4844): one post-merge and one pre-merge (to facilitate Prysm). Numerous participants... (For more information, see the recording.) Full withdrawals are working perfectly.
99.3 |Testnets / progress updates: Nimbus not yet participating, the consensus layer withdrawals implementation is in progress.
99.4 |Testnets / progress updates: The operation of changing BLS credentials is being tested with ethdo and a subset of the clients. Change message gossip has not yet been tested, but it is about to be.
99.5 |Testnets / progress updates: When Nethermind and Besu are ready, and Prysm can start from a post-merge genesis, plan to move to a longer-lasting single testnet. (That is, soon.)
99.6 |Bound withdrawals sweep: [Alex] Following feedback, the bound is set to a very low value. There are no objections to proceeding with this. More withdrawals test cases will be added to cover edge cases by the end of next week.
99.7 |KZG Ceremony: Public contribution period will be about 2 months.



## Intro [1.49](https://youtu.be/KFc1sWYlVZ4?t=109)
**Danny**
* We are live. Cool. Thank you everyone for joining since our call number 99. This is issue 667 in pm repo link shared in the chat. we will as usual hit Capella update, then merge, general open discussion around spec and research.
* First of all, I think there was a doozy of a call last week on the All core devs, execution layer call. I did want to recap what I think is maybe the most relevant conclusions for this group. obviously a lot of us have opinions about what's goes into the EVM, but let's keep it targeted on the Consensus layer and what we see as the next couple of upgrades coming. 
* My understanding is that we shall keep withdrawals independently specified and worked on in Capella and that 444 will remain its own specification and that I think importantly, even in the event that these things were say in some world ready at the same time, even though that's not the intention right now, that we still wouldn't combine the specifications and, and stagger the upgrade.but I think that crucially, you know, I think what was made clear by consensus layer teams is that, they believe that 4844 is not in nearly the same readiness as withdrawals, coupling them with significantly delay withdrawals.
* We will not couple them. We will work full steam ahead on Capella,in its current form, while parallel using the 4844 work still. is there any, is that correct? Is that the general understanding of the teams on this call? Does anybody not? 

**Arnetheduck**
* That's what we liked from Nibus. 

**Danny**
* Sorry, what was that? 

**Arnetheduck**
* That was, that's what we like from Nibus. Yeah. Okay. Makes sense. 

## Capella  [4.42](https://youtu.be/KFc1sWYlVZ4?t=282)
**Danny**
* Great. I will instead ask instead of affirmation, any dissent. Okay, cool. again, most of that was hash out on the previous call. If you're listening to this, you can go check All core dev. great. So let's move into our items for today, Capella. Does anybody have just a general progress update with respect to test nets and other coordination items? 

**Barnabas Busa**
* I think I would be responsible for that. So we are currently running two testnets. for withdrawal, does not include any 4844, implementation only, strictly withdrawal part. So currently how it looks like is we are able to do full withdrawal.we do the testing with, load star Lighthouse Teku and prism. Prism is not able to start from post merge just yet. they're working on it and that's why we have, currently two different Testnet. So one of the testnet is  the pre and the other one is the post merge. And the post merge has most merge like teku, Geth. Nethermind and the other one is, we just started that today, started over again and we started to, begin testing BLS to execution changes. 
* So that one currently runs, prism, lighthouse Teku and Geth. 
* And Nethermind because be still, doesn't have the Shanghai, by epoch implementation, we are awaiting for that. That should be done quite soon. Again. And as far as I know, Nibu and doesn't yet have any implementation for withdrawal that's why we able to, that's it

**Danny**
* What's the Nibu status? I mean you said from the Nibu team where we stand on on getting withdrawals, 

**Zahary**
* Were this a request regarding the consensus layer or the execution layer? On the consensus layer currently building out, the spec or we are pretty close to kind of running local simulations and the immediate next goal would be to joining this, the internal operator. 

**Danny**
* Great. And then on the,the BLS change operation, do we have tooling for testing that? What are we utilizing for that? 

**Barnabas Busa**
* We use it do and Prism is just testing it right now and, also Lu Star has something in draft and should be available I think within a week or two. So then we can also include low starting the testnet for that. 

**Danny**
* Great. I would recommend we so there's obviously getting into local men pool and block packing with those operations.Another is testing the gossip operation, so it might be valuable to insert them into a node that is not running validators and then if it's picked up by other nodes we know that the gossip is working well. Okay cool. anything on the Capella testnets Right time? 

**Barnabas Busa**
* This is the Capella or Anything else? Oh,anything else? not really. so this, this BLS execution, it's very fresh.Like we started maybe two hours ago. That's, that's why I didn't have that many to say about it yet. But, but the full withdrawal we tested a couple of weeks ago already and full withdrawal was work just fine when the visual addresses a zero X zero one. 

**Potuz**
* So BLS changes are being submitted and we tested that we can submit to the pool more than the allowed maximum in a block and the pool is accepting them and just sending them on the maximum per block. Other other nodes are taking this, we are not broadcasting them yet on the p2p on gozip. we'll test this right now. Okay, Cool.

**Barnabas Busa**
* So basically the future plans are, that we're going to migrate these two testnet into a single testnet and we would like to include all clients in that one and that's gonna be a bit longer lived one also. But for that, I would like to wait for Besu to implement their Shanghai based on epoc, and I would like to include Nimbus also. And we will do that once, prism is able to serve from a post, merge genesis, which is also should come very soon. 

## bound withdrawals sweep bound the maximum number of validators considered for withdrawals per sweep consensus-specs#3095 [9.53](https://youtu.be/KFc1sWYlVZ4?t=593)
**Danny**
* Great. Okay. Next up let's talk about issue or PR 3095. We did talk about this two weeks ago. I think I generally had agreement, on doing this bounded sweep. Alex, is there any update or any question with regard to this before we do a review and get it released? 

**Stokes**
* I don't think so. I've made the bound very small in response to some feedback and added some tests recently that was a little more involved than I was expecting. But yeah, it should be ready to go. Final review and then, yeah, the only thing is yeah, just agreeing that we all want this change. 

**Danny**
* Okay.I believe that was the general agreement two weeks ago and you sent on bounded sweep and it being on the lower end of okay. So I know we have a number of additional tests work in progress right now around some of the more edge cases on multiple balance updates for validators within a single block.so we're going to aim to get some of these new tests and this out by the end of next week for consumption. Good. Okay,Anything else regarding Capella? Okay, on 4844, there is a weekly call on Mondays. Is there anything that, needs to be percolated up to the larger group today? 

**Seananderson**
* So that line actually raised an interesting issue recently that I thought was worth bringing. it has to do with syncing where like syncing blobs. the general idea is that like we have  a lower bound of blobs like our men whatever request epoch for storing blobs, but like the actual lower bound seems like it would be the point of finalization.And if that's the case, then you have scenarios where the chain hasn't finalized within this sort of like prune depth we've defined. 
* Then when you're syncing from Genesis, you don't know where the point of finalization is until you get all the way to the head.So this would mean you'd have to sync like all the way to the head to find where you should have validated all the blobs and then go back and check that you actually got blobs and blocks from your peers in that space between like where the chains finalized and where the like prune and threshold we have is. 

**Danny**
* So why are you saying the that you should only need to get blobs? Are you saying that you only need to get blobs since finalized? 

**Seananderson**
* I'm saying like the minimum bound of where you need to get blobs seems like it's either the point of finalization or like this prune depth that we've defined. And when the point of finalizations like further in the past than this prune depth,there's some tough scenarios that make it seem like you'd have to sync to the head and then go back and double check you've got all these blobs correctly.Cause you don't really know what the point of finalization is apart from like what your peers tell you their like finalized epoch is, Right. 

**Danny**
* I don't see the interplay between finalization and the prune depth.If you have what is you think is a finalized chain, but you don't have the available blobs, you would consider it unavailable, right? 

**Seananderson**
* I think it's that your, peers could tell you an incorrect finalize epoch and while you're sinking to the head, you sort of have to trust this until you're able to determine for yourself whether it was finalized so they could give you an incorrect finalized epoch and then not give you blobs where you would've needed it.So then you'd have like blob blocks that are actually unfinalized with no you couldn't check that the data was available. 

**Danny**
* Yeah.So I claim that I don't see the interplay between finalization and data availability.Meaning even if you think if something is finalized, you should still be checking data availability so that a malicious majority can't pull you about vailable data. But I maybe I'm missing something here.Proto you had your hand. 

**Protolambda**
* So to clarify, we are talking about, periods of time, past the pruning period, so like more than 18 days ago. But if the chain is not finalizing for all the time, then there's a, where you might have, part of the chain that you don't have the data, but that is part of sorry. 

**Protolambda**
* Okay. So there's this part of the chain, in this case of non penality that we will not have to block data for anymore. So you cannot validate whether or not it should have been considered for family station,is that what you're saying? 

**Seananderson**
* Yeah, that's what I'm saying. 

**Arnetheduck**
* Just a quick question. Why aren't we tying the period, the removal of the block data to finalization instead? So data. Oh, like that. maybe they should. 

**Seananderson**
* So in the specs, it's actually specked out that you should have data until the finalized epoch as well.So it is there, but the case that I'm trying to get at is where like your peers are, I guess lying about what the finalized epoch is and you don't know that they're lying about that until you sync to the head.And so then at that point you would have to like go back and ask good peers to like double check these blocks that you, you thought you didn't have to check whether the data was available for and then like reprocess that. 

**Danny**
* Oh, cause the, so the network, the spec says do the maximum length, whether that be 18 or time since final. 

**Seananderson**
* Right.So like you should in your database.Yeah. 

**Arnetheduck**
* But in general,  we can never trust what the other clients are telling us. I mean, how is this unique, right? Like we always assume,

**Seananderson**
* Yeah. So the thing about this is like, you assume this, but you're able to verify this as you sync forward in sync usually.But in this case, it's like you'll be syncing forward as you're syncing forward.You have to like trust about the validation of the block that like, your peers aren't gonna give you blobs according to like their view of finalization, I guess. So the difference is that like you can still sync to the head and then at that point, you know what the actual finalized checkpoint should be and then you like can reprocess those blocks. 
* But the comple like I'm bringing this up I guess make more people aware that this scenario could introduce a lot of complexity because we don't have to like reprocess blocks during sync in other parts of like the consensus layer.Like we have to do it for optimistic sync for like consensus layer,execution layer sync. But this would be like unique to a consensus layer a strange edge case that potentially introduces a lot of complexity is most of my point. 

**Protolambda**
* I'd like to understand it better. So we have this, this for fork choice three, you sync one path of that from some peer the peer can claim whatever, you verify the data that you pull and then you verify all the state transition, you verify the finalization that happens during the state transition.And for the, at least the last 18 days worth of data you should have blobs downloaded. And if not, then you cannot persist that part of the chain.And then there's this edge case with non finality for more than 18 days. 
* And then there's another edge case with the I think I got this right.I'm not sure how to best describe this edge case where the block data period is shorter than the ization end and you want to download more blobs.In that case, I think we might not even want to download the blobs and change the spec.So where does the complexity where does get introduced? Assuming we can simplify the spec to say always verify the last 18 days and just verify the finalization like today without four before? 

**Seananderson**
* Yeah,I'm gonna have to think about that, but  I think generally it's like we'd have to introduce another form of like optimistic processing of blocks. But yeah I'll think about what you're proposing more goes. 

**terence**
* Wait, so the spec says that you cannot import a block unless there's a blob, right? So for forwarding case that if you don't have a blob, then you just cannot import it. Are you talking about potentially moving that into more like a optimistic model? 

**Protolambda**
* No.So you should require the blob for data that is less than 18 days old but then there is some doubts better not to change that based on finality especially in the case of like long non finality. 

**Danny**
* Okay. So there is a PR open with I believe this explained on 3141 on the consensus spec.I need to take a look at this to have a more intelligent conversation about it. do you think that we can make progress here today or that we should move to this PR Let discuss in the PR? 

**Protolambda**
* Yeah, I agree. 

**Arnetheduck**
* I would just ask the question, is there any problem time, removal of blob to the finality instead of I guess wall clock? 

**Danny**
* Do you mean even in the event where you're finalizing in two epoch removal blobs? 

**Arnetheduck**
* Yeah, I mean you're finalizing into epox so you keep data for, you know, 20x possible. 

**Danny**
* Yeah, so I mean, one argument would be that a malicious majority can fool you if you're offline for an epoch and you come back online. there are certainly debates as to what the pro depth should be. 

**Speaker**
* It also removes our guarantee of, constrained state growth. Theoretically. 

**Arnetheduck**
* No it doesn't because the chain can only go on for, what is it a month before it dies. 

**Micah**
* There's no, No finality of on for leak for a month. Well, this is a total leak for a month, but then the new site can continue leaking. So from a theoretical standpoint, this is unbounded. Like you can just have, you know, 75% leak out and then the remain 25% then fail their Achieve finale and they start leaking out, then the remain 25% fail their achieve finale Lee leak out. And you repeat this forever, theoretically, I recognize this is very low odds.but,no because finally everybody looks up but you know, Some that's true. 

**Arnetheduck**
* I guess we do, we do round to one at some point right,and is that like some of the validators stay in there, those that didn't leak out and I guess reasonably those cause finality at the point where, the leaky ones are finally exited? 

**Micah**
* Yes, that would be a reasonable expectation of what should happen, but it's not theoretically guaranteed. Again, my migraine year is just like as an edge case. we are currently asserting with very strongly that there is a very finite amount of states that can be contained by these blobs.This would change that to a, you know, more of a, economic guarantee rather than a hard guarantee, which is probably still fine, but I think we should just recognize that 

**Arnetheduck**
* It's a fair point and it's that kind of risks that I was curious about. 

## KZG ceremony update [25.30](https://youtu.be/KFc1sWYlVZ4?t=1530)
**Danny**
* Okay. I'm going to read this and move my comments to 3141. If you are interested in digging into this, please do the same.Okay.Trent I just saw you added, KZG ceremony update.Can you give us that while we're here? 

**Trent**
* Yeah, real quick related to 4444 most of you are probably aware that it requires a trusted setup. but for anybody listening to the call live or the recording or reading the notes later on, just a quick update. We're finishing up the, the second audit with Sigma Prime.that'll be done probably this week. We'll respond to their changes.And then shortly after hopefully in the next few weeks or at least, at the start of the new year, we'll be moving into the public contribution period.So, if you, any teams or individuals, communities want to participate, please start sharing this. 
* We're, we're starting to ramp up some, education awareness stuff.We'll be doing Twitter spaces.So if you have a specific community that you want us to come talk to, Carl and myself will make ourselves available. we're more than happy to do that. yeah, this is, as you probably know, trusted setups are, we want them to use credible as possible, and that means getting as many people to participate.So that's where we're, we're gonna aim for this to be the largest, summoning ceremony,in the crypto space at least.probably, let's say eight to 10,000 contributions is what we're aiming for. So yeah, if you have any communities, that you think might be interested, please reach out. We're, we'd love to come talk to you. and if you are, someone with,let's say an academic a amateur or professional interest in cryptography, we're also running a grants round to get other people to write implementations.And that'll be happening after the public contribution period,but we want to get people aware of it and please reach out if you're interested in writing your own implementation.from what I understand, it's relatively straightforward, not too crazy, maybe a day or two of work. so we'd love to have as many implementations as possible contributing to this again to make sure this is as credible and legitimate a ceremony as possible.Okay.that's all I have. 

**Jesse Pollak**
* Thanks Trent. Do you know how long the public contribution period's gonna be open? 

**Trent**
* We're aiming for at least two months or right about there. 

**Jesse Pollak**
* Got it. So like early to mid-January to like mid Feb, mid-March or something like that? 

**Trent**
* Yeah, roughly. we'll,  definitely have like a tighter, a better idea of what the, the bounds are as we get closer. 

**Jesse Pollak**
* Great. Cool. And just a quick update from my side,cuz I'm here. coin I've been talking internally at Coinbase, we're all aligned on the kind of like social content side. So that will happen for sure. And then I'm working on the call to actions in the product. I think that's gonna happen as well. 

**Trent**
* Oh, awesome. Thank you. 

**Carlbeek**
* One, extra thing to add here is that like, if you do have any questions or doubts or whatever about this, like please don't hesitate to ask. like, this is a weird and fun thing  to be doing, so like, let's make sure everyone understands it and is comfortable. Like, don't hesitate to, to reach out if you have any concerns about all of us or Thanks. 

**Danny**
* Thank you. any other 4484 discussion points For today? Great. 

## 3. Research, spec, etc
## (networking) attnets revamp Consensus-layer Call 99 #667  [29.22](https://youtu.be/KFc1sWYlVZ4?t=1762)

**Danny**
* We have a number of Research items across a few different domains. Age you had a couple. The first was the ATS revamp.can you give us a quick on that? 

**Age Manning**
* Yeah. so I just wanted to rise a few things that we're, planning on, I guess releasing or adding into Lighthouse that can affect everybody else. so that nets revamp thing, so this is where we get a beacon node.so I guess if we just do lighthouse a specific beacon node subscribes to one or many subnets rather than it being tied to the validate account.so this is entirely backwards compatible. We can kind of just release this kind of thing tomorrow,but the overall effect on the network is that the density of the subnets of the ation subnets is going to be reduced depending on how many Beacon nodes, you know, beacon nodes to subnets we have have.So yeah, I wanna just gauge other people's thoughts on doing this before going into any questions. 

**Danny**
* Any of the simulation analysis that was that completed? I know you were working on it. 

**Age Manning**
* Yeah, so the simulation, so we've got like some simulation stuff,but it's not really for the attestation subnet. So I guess fundamentally the question I wanna ask the other client teams is how they're managing,how they're managing peers, in terms of like collecting the ones that are on subnets that you need.Because if we make this change, and if you have just like a one to one mapping,one beacon node to one subnet,then if you have,let's say 60 pair and you kind of collect them so that they're uniformly distributed across the subnets, you, you still should at least have one on every subnet. I'm not sure if other client teams are doing this kind of, this kind of logic. 
* If we, if we, could also say one beacon node should subscribe to, six subnets and you'd have roughly the same density as you have on mainnet at the moment. And you shouldn't see, you shouldn't see a drop. You might actually see better improvements because, because every beacon node that you connect to will be, will be to a subnet rather than having these small groups of big nodes that, you probably can't connect it cuz everyone else is trying to connect to them.So just trying to gauge other people's thoughts on whether it's a backwards compatible release that can kind of happen slowly in one client that's not gonna destroy the entire network in one hit potentially.  
* Is there any thoughts on this by any of the other client teams?Is it gonna do we think it's gonna drastically affect, other people's implementations? 

**Nishant Das**
* Is it possible to test this out on Goerli first before mainnet? 

**Age Manning**
* Yeah, of course. It'll, like, we do it on, for sure, we do it on testnets to begin with. but it's mainly about, no distribution, which is very different between the testnets and mainnet. 

**Danny**
* Yeah. So like on on Testnet, given our assumptions on node count, we might have to make the minimum 10 or something, whereas on mainnet, the target would be, the minimum would hopefully be one, Right? 

**Age Manning**
* Yeah, exactly. Yeah, exactly. Yeah. 

**Danny**
* So it would be  semi artificial test. It'll show that the functionality works, but it won't show necessarily that the distributions work for me. 

**Pari**
* I mean Yeah,The most interesting thing about this proposal to me was that it also changed the way we did sync committee submit because currently getting on the sync committee, match is actually problematic. I mean, at least from what we've seen that the sync committee meshes are, are sparsely populated and difficult to get into. Now, if this means that a lot of lighthouse nodes suddenly will be less interested in forming meshes, then, then obviously it's going to have two effects.One is that,lighthouse will use less bandwidth, than the other clients. and then I'm hoping that we will not end up in a situation like the same committees where like we get reports from people, we look into it and then they couldn't get onto the mesh. I don't really know what a good model for releasing that is but Right. 

**Danny**
* I wouldn't, even though we can do this in a backwards compatible way, I don't think we should do it unless we're confident that the entire network can do so. and that this is like the new specified honest behavior. the goal here would be to make sure all nodes are helping contribute while also you know having so having a better distribution and also potentially reducing bandwidth for the average node as well.So I'm, although I've proposed it, I don't know the best way to a hundred percent validate it before we move forward. 

**Age Manning**
* Sure.I can post some statistics, which doesn't entirely help us all that much. One of the other, I guess, important metrics that's a little bit difficult to find is, you've got these bunch of nodes that are subscribed to a lot, which is the, the ones that are gonna be reduced. So the ones that are subscribed to 64 subnet, essentially we, we've reduced those down to one and, and that's where the damage would mainly be. But the, the interesting metric that you kind of wanna see is how many peers can connect to those nodes at the moment? Because if they, if they, for example, if they don't accept 50 peers and they all their peers slots are full and, and new notes can't connect to 'em anyway, they're, they're not as valuable as what we think they're, 
* I can try and get some more information and That but there's also there's a couple things here. 

**Danny**
* One, you can't, like, you can just lie. So nodes can just lie about ad right now. so this, by making it just a function of your peer ID or some sort of external, piece of data about yourself, you can now make it whether somebody's like doing their job or not, which is good. And it also it scales with the network. So the meshes you know, naturally kind of become reinforced as there's more nos in the network rather than right now if you had a hundred times more nodes than than validators then you have even more trouble finding kind of like the sparse validator nodes. so like to reiterate like there's a number of reasons even in future constructions that we don't wanna just be relying more heavily on these nodes that are disconnected to everything. 

**Age Manning**
* Yeah. Another semi safe way of doing this, if you just wanna go on like kind of raw subnet density numbers is if we said one way connects to six or seven subnets, then the density should be the same, but you should have a greater connectivity, so it should be a strict improvement in principle. 

**Danny**
* Yeah, I get worried. Yeah. Yeah, just that would be a drastic for a home validator with one validator. 

**Age Manning**
* That's Probably a drastic. That's the Downside. 

**Danny**
* So I think that I would only be comfortable moving to this if we can convince ourselves that only order of one or two is is safe. 

**Age Manning**
* Okay. I'll personally issue and try and just post the current statistics and we can make a decision on the issue. I can move on to the next one unless there's anything else on that. 

**Arnetheduck**
* Two more small things. One is that I do think that clients should strive to follow the spec, so I'd love to see this added to the spec and then we start releasing it to mainnet, otherwise, we're on a slippery slope, blah, blah, blah. 

**Danny**
* Yeah, I agree. That's what I meant, but we should be agreeing to this even if it's backwards compatible rather than just shipping this. 

**Arnetheduck**
* Yeah. The other thing was, I think something we talked about at devcon, which is that the guarantee, I mean, it's still based on honesty even after this change. Like, and I think what we discussed at devcon was basically that, you can signal that you're, you know, part of the subnet and, and then you can just not join the mesh even though you subscribe to the topic. So like, if you want to be dishonest there, there is still a loophole. the verifiability is, let's say nice, but I wouldn't take it as foolproof. Like it's not proof. You still need to verify that they're actually transmitting messages and stuff like this, and that that goes into difficult territory. 

**Danny**
* It's difficult, but not impossible territory, at least in a heuristic zone, right? Like if I think you're on a mesh and you never gimme anything from being on that mesh, then I can downs score you and move on. 

**Arnetheduck**
* No, but I can say that my mesh is full, I can prune you and, and that's I can't tell anything about, Which is another reason to move on. 

**Danny**
* But yeah, I mean, the worst, the main thing you can do is if somebody's lying to you about this is to not connect them and if they're also simultaneously just pruning you from the mesh, that's also a reason to not prioritize them and not connect to them. So, Yeah. 

**Arnetheduck**
* Yeah. 

**Danny**
* And like, And if they're doing everybody, they're going to be disconnected from most people. 

**Arnetheduck**
* Yeah. That's fair. Let's do, Yeah. 

**Danny**
Okay. Well, a you have another one? 

**Age Manning**
* Yeah,so there's another kind of two ones,I won't take up too much, time for everyone.But one of the other issues in terms of like connecting to all these peers that, that we need for the, for the subnet is that there's a lot on the network that are behind Nats at the moment. there was a drive, in Disney five to, to build like an automatic, nat hole punching thing, which we're close to having kind of a, a version working. but that involves specking out, some extra fields in the enr.so anyway, there's, there's some work towards this and if the other client teams are kind of interested in doing this kind of it'll translate over to TCP at some point after a bit of specking.But, essentially re specking some ENR fields modifying discovery five and, adding like a, a tcp automatic hole punching is something that, we're kind of working on and would be handy if we get some other client teams for interrupt. 
* I'll post something about that. People can reach out if there's anything interesting about that. 

**Arnetheduck**
* Yeah. I saw that loop P2P themselves are specing out, what's it called? Auto nets  Is this somehow related or integrable? 

**Age Manning**
* Yeah. So my understanding with AutoNet 2.0 you it's a entirely lip P2P thing, so it's entirely over tcp and you have, you organize a relay and via that relay you organize the whole punch on tcp. so there was a Yeah, so there was a spec Yeah.For portal in particular that wanted to do, some, that whole punching, which is semi specked in Disp five. Fundamentally what happens is that you, you do a similar thing using relays, that the whole punching usually works better over udp. And once you have that you essentially have a connection with a node over EDP. And I think quite easily we can use discovery v5 to then, essentially organize a, a whole punching through tcp so we don't have to have the, the relay that you would need, with auto and p2p. Like we can, we can skip a step Because We have discovery. Okay. Yeah. 

**Nishant Das**
* Is, is there a link to the spec for this? 

**Age Manning***
* Yeah,I'll post it. So there's, there's some stuff that  we're semi making up and some stuff that's in the SB five spec. So if you go, if you go to the SB five spec in prs, I think, there's, there's a proposal there that's not entirely stable at the moment. 

**Nishant Das**
* Okay. Sounds good. 

**Age Manning**
* Yeah. so the last thing is, ipv6 support.They've been, people kind of hustling us for quite a while, which we have mostly figured out, but the first step to kind of onboarding ipv6 nodes is, is having ipv6 compatible boot nodes. so we were considering just enabling, the lighthouse boot nodes to having IPV six, which gives an onboarding for some nodes to then use IPV six if they want to. We won't have ipv6 and they would in lighthouse, but just having the boot nodes, capable of doing it allows us to upgrade at some point in the future. I'm wondering if there's any thoughts about that, whether we should do that, should not do that. It'll be dual stack, so it's entirely back compatible, which means that it has an ipv 6 and ipv6 IP address. 

**Nishant Das**
* It just means that in ther you then have the option, So all clients would've to update their booth known in, sorry. 

**Age Manning**
* No,Other clients need to do anything, but if we do the lighthouse ones, it just means there would, of all the boot nodes we have two of them, can advertise an IPV6, and so other IPV6 nodes can kind of, advertise off them and, and, and can contribute to the dht. It's just an entry point. 

**Nishant Das**
* Yeah. But, like, lighthouse booth node are like hard coded to different clients, right. So, each client would've to update their lighthouse boot node to have the IPV6 in house them. Right. 

**Age Manning**
* Yeah, so, so we would, we would update the ENR in each of the clients, so that it's, they're hardcoded into the client, but it's, I don't think that's entirely necessary because when you initially connect it, when it does the handshake via Ping, it realizes that the sequence numbers outta date and it downloads the new one, it automatically. 

**Nishant Das**
* Okay. Right. Yeah. 

**Age Manning**
* So, as long as you have the, node ID essentially and the keys to connect to it'll update it automatically, even if it's not hard coded. But, but we should hard code it. 

**Nishant Das**
* Right. Sounds good to me. 

**Danny**
* So this doesn't require any sort of spec change. does it require anything from other clients or are you asking them to also add ipv 6 to their boot notes? 

**Age Manning**
* No, so it doesn't do anything. yeah, so no one else needs to do anything. The reason I'm bringing this up is in a previous conversation I've had with everybody, there was concern of having, a network split. If, there's ipv six only nodes, then the IPV six only nodes can only kind of talk amongst themselves. Essentially, by enabling ipv six in a boot nodes, you now semi enable the possibility for people to try and run these kinds of setups. In Lighthouse, we're only gonna allow dual stack to begin with to not segregate the network, but it opens up the possibility that, IPV six only nodes that start joining can, can kind of partition if anyone's attempting to run that kind of thing. So,that's kind of why I'm raising it. I don't think that there's a downside other than that it's just, forwards compatibility, and if we update the nodes now, then we can upgrade later. 

**Micah Zoltu**
* If you launch a dual stack version of a client and the operator runs it behind a NAT that doesn't have some sort of auto hole punching, won't they naturally fall into ipv 6? Only because in most cases, because of the abundance of ipv 6 addresses, lots of get an IP via six dress, but they're natted behind IPV 4, and so they may only have public access via ipv 6. So is there a risk that they might accidentally partition even if you do dual stack? 

**Age Manning**
* Yes, So I think that's right in that case. And so then those nodes probably won't find any peers or they might Yeah, they might start petitioning themselves. Yeah. If there's, bunch of them doing it,

**Micah Zoltu**
* They, they'd find all the I P V 6 peers and they wouldn't be able to communicate with anybody. The ipv 4, not due to maliciousness, just due to their network was set up such that their added with IPV 4 and they didn't punch a hole.Right. 

**Age Manning**
* Correct. Yeah. 

**Micah Zoltu**
* So at the moment, Yeah, they would end up accidentally being Ipv 6 only nodes, even though is there anything we can do, I guess what I'm asking, is there anything we can do to try to make that not happen by accident? Like if someone wants to do ipv six, they have to kind of really go outta their way to do it. They can't accidentally fall into ipv 6 only. 

**Age Manning**
* I'd have to think about that. There's a bunch of changes in this NAT stuff that I'm talking about where we the local knows identify what kind of nats they're behind, whether it, in which if we had that functionality, potentially we can, we can do some stuff, but I'd probably have, I don't have an answer right now. Okay. I'd have to think about whether we can do that, but in principle, yeah, adding this support and allows that, that kind of setup to petition themselves rather, at the moment, they would just not connect to anything On a similar note. 

**Micah Zoltu**
* And related to the previous point about not whole bunching, can we, a note that is I dual stack, can they use the  IPV 6 to establish that poll for I for their own IPV 4? 

**Age Manning**
* Yes, I think so. In principle, I think That be, Yeah I don't see why not. It depends on the relay. If the relay in between supports ipv 6, in, in discovery. Yeah. So I think it's possible. Yeah. 

**Arnetheduck**
* Out of curiosity or using a single socket or two sockets, like a single deal stack or, it's

**Age Manning**
* I think it comes out as two sockets in the Russ.  The Russ Library uses a single socket, but you, you have like essentially allow map to dress, which gives you a second socket. 

**Arnetheduck**
* All right. Yeah, we're looking to get IPV six in there at some point as well. 

**Age Manning**
* Okay. yeah, I think like semi enabling it is, one step closer I guess or at least just doing the, doing the boot nodes early so that they're in the dht but not having functionality. Otherwise, I'll make some noise on an issue that people  can post, just giving a heads up. Cool. That's it for me.Thanks guys. 

## (Beacon API) checkpoint sync api status Checkpoint Sync API beacon-APIs#226 (comment) 50.24 https://youtu.be/KFc1sWYlVZ4?t=3024

**Danny**
* Thank you. Okay. We have an old Beacon API on Checkpoint sync APIs. I think you raised this right? 

**Mikhail Kalinin**
* Yeah. so Checkpoint sync, API that has been Yeah. Opened a while ago as Danny said. so yeah, just want to give an update on it. And, yeah, just before we move on, the, with the update and the current state of the, with the checkpoint sync, just wanna give a quick reminder on what was this PR about? so this PR basically proposed to endpoints.the first one was, for state providers.The second one for was for trust providers. the goal of state providers, endpoint was to make it, convenient for, actual state providers to,  provide the state. basically it allowed to provide any finalized state, that the state provider wants, which is within the weak subject period. the other endpoint allowed to, allows to use the, whatever the trust knows that, whatever knows that you trust, and, the trust is a subjective thing, but, it allows you to verify the state that have been, that you have been with and obtained from the, actual state providers. So that's the, the overview of the proposal. And, yeah, since that, has been opened, there was the checkpoints tool developed, and, yeah, basically the tool provides, a convenient way for, state providers to supply the state comes with like those protection, it comes with it can talk to a multiple upstream, beacon nodes and decide on whether the state is finalized, whether they agree on the, finalized state and then expose it. Also, it comes with the cashing, so it basically suits very well the first goal of, this proposal. And, also it provides data, than the state, only because some of, CL clients can't srap with the state only. Yeah, it's the problem that, or talking to, to the checkpoints and proposal. But anyway, the checkpoints do also solve this problem as well. and for the second part, for the trust part for the verification part, the checkpoint still also yeah, provides this functionality. My main concern about that is that, in this case, checkpoint still become the single point of failure if everyone will use this for providing the trust for allowing to verify the state that has been given  to start with. and we have another PR that has been merged, recently, which equips every, response in the Beacon api.That's response with, some chain data with finalized flag. So basically, the reason endpoint, a simple endpoint that can be used for state verification and, yeah, probably the other way, without creating a single, point of failure would be to for those who wants to be a trust provider to, make their own, custom configuration and those protection and what and utilize this finalized flag.that's the other way of doing this. yeah, and basically,the intention is to my intention is to deprecate this proposal,unless there are some,I know some other opinions on that and that's why I'm bringing it here.Just announce that it's about a bit deprecated and if you're interested in it cause of whatever reason, just yeah.post the comment in the issue or say it here on the call.Okay. 

**Mikhail Kalinin**
* Yeah, I think it makes sense to keep it, the issue, keep the PR open for I dunno until the end of this week and just close this somebody appears. 

## (Beacon API) Attestation and sync committee aggregation selection Attestation and Sync Committee aggregation selection beacon-APIs#224 55.47 https://youtu.be/KFc1sWYlVZ4?t=3347
**Danny**
* Got it. Okay.another speaking. Beacon API's known for a while. this, let's see. Can you give us is the person who posted this here? 

**oisinkyne**
* Yeah, I think so. It's me, Danny. 

**Danny**
* Oh, okay. Sorry. 

**oisinkyne**
* How are things guys? So, the, poll request that I'm looking for, kind of review and feedback and acceptance on relates to, distributed validators and the aggregation duty.I'd say a lot of people on this call are familiar with the idea of distributed validator technology. It's making a, you know, one logical 32 weeker validator run across multiple machines with you know, threshold BLS keys and multisig like signing.And the, this pr addresses specifically the aggregation duty right now, the aggregation duty is decided by you signing the slot, which is called a slot signature, and then hashing it and, and doing like a modulars check. And the problem is with a distributed validator, every individual validated at a different BLS private key. So they all have different salt signatures and then all try and aggregate at the different time,the proposal or the kind of tweak we're working on. We've been, you know discussing this a few people for a good few months now shout out Danny, Ben, Terrence, and some of the others. But basically as it's refined now is it's one extra API call that, the consensus layer doesn't have to implement.It'll be implemented at the middleware layer, and it would be opt in to be used by validator clients if they turn on a feature flag. And it basically means when you're trying to decide if you're supposed to aggregate, you just send your partial slot signature to the consensus layer, and then it returns you a full slot signature, which you then hash and modulars check in and continue on the flow as normal. So, yeah, ask is have a look, have to answer the questions now, but, if we can get it, accepted, then we can kind of talk with the client teams about getting it implemented in a branch, kind of behind a feature flag and stuff. Excellent. 

**Danny**
* Okay. So the decision was to return whatever may be a full slot signature, and the validator client still does the local computation rather than just the middleware or the beacon node doing the computation on the full slot signature and returning true or false or aless of indices, right? 

**oisinkyne**
* Correct. The reason we return it is because, at second age you have to make an aggregate and proof and in that aggregate you have to actually put the proof, which is the like the fully assembled slot signature.So that's why we're sending it back instead of just sending back through. 

**Danny**
* Got it. And if you're implementing this on the, would you implement, so would Beacon Nodes actually implement this and just like have it essentially a noop where you're just returning the value that was given, so the validator client doesn't really care if it's connected to middleware or beacon node, or would you not expect Beacon nodes to implement this? 

**oisinkyne**
* I don't really mind. I think in the polar request, I'm suggesting we don't implement it for simplicity. and I was suggesting that a consensus client either return 5 01 not implemented to like explicitly say, no, we're not doing this. Or potentially like a 400 to say, Hey, you're potentially sending like a, this endpoints interview for a distributed validator and you're hitting it off of a consensus client, you probably want a 400 to see what's going wrong here. so, so yeah, 
* I it could be implemented and be no op, but I was thinking either kind of a, a 5 0 1 or 400 depending on if we want to kind of tell the user that something is up. 

**Danny**
* Got it. And in the event that this is not added to the, something like this is not added to the valid api, then that's going to make DVT teams probably be forking validator clients, which is not What we want. 

**oisinkyne**
* Yeah, that's, that's really the thing. The other option is that distributed validators don't implement aggregations and they don't get penalized themselves, but like network effectiveness would gradually decline if, if these make up like a larger percentage of the network. So yeah, you'd prefer to be, you know, additive to clients rather than be kind of pushed into making a kinda a custom validator. 

**Danny**
* Got it. there has been a bit of conversation we see on this issue, even through October. what do you see as the blockers here? Is it primarily, generally thumbs up across these teams or are they sticking issues on sticking points on some of the time? 

**oisinkyne**
* Happy to ask them, but I think we're mostly aligned. I think the, the main change between the last of stuff was this was suggested as  a V2 endpoint for the subscriptions one, and it was gonna be just like returning true and then we said, actually let's just bring it onto its own endpoint of standalone rather than have one endpoint kind of do two things. And normally when we move to a v2, that implies a deprecation of v1, which isn't the case here. So the, I think the main changes have been addressed, but, you know, good for client teams to cast a final line bot over it and see that it's kinda all good and they're happy with the, the proposed changes. 

**Danny**
* Got it. so if your team has not taking a look at this, I do request you do. So maybe by the end of next week, and if this issue is not resolved by the next call, then we will attempt to resolve it live. Sounds good. 

## (engine api) engine api spec improvement proposal Consensus-layer Call 99 #667 (comment) 1:02:05 https://youtu.be/KFc1sWYlVZ4?t=3725 
**Danny**
* Okay. And Mikhail on engine API spec improvement proposal. 

**Mikhail**
* Yeah. so there are two main questions for making this, proposal. I took this back. yeah, so the first one is the, engine gate capabilities method. do we need the this method at all? so the, the default and lazy, in terms of like, probably not lazy but less complex in terms of specing out and engineering is the, optimistic strategy suggested via it can be already implemented. So we have everything for this. So it's basically, if, CL knows that they're gonna be an update on the EL side and it starts to support the, for example, new payload with two method and, yeah, it starts to send the new payload with the method to the, EL, if EL doesn't support this method, it returns in the correspond error and then CL falls back to, to the previous version. 
* So that's basically the, optimistic strategy, try and fall back on error

**Danny**
* Some scenarios fall back wouldn't even be an option. Right. It'd just be kind of a critical failure depending on the functionality between the two versions, Right? 

**Mikhail**
* You mean that at some point the V2 will be a must, right? Is that what you mean? 

**Danny**
* Right. You could imagine certain structure of the data is just critical for the v2 Or the v2 Yeah, right. 

**Mikhail**
* Compared to Yeah, that's correct. Yeah, that, that that's correct. But, there is like a rough consensus that, that we should try our best to, to make the version, the next version backs what's compatible with the current one. So it's, somehow, yeah, it, it should support and probably in most of the cases we can do it. 

**Micah Zoltu**
* When you say current version, when you say current version backwards compatible, the previous one, you explicitly mean only one version back, so we would not support backwards compatible with two versions back. 

**Mikhail**
* Basically that was the agreement. I don't think we should, if there is no need for this, I don't think we should, support the versions that are like pretty old older than two, two versions from, from the current one.  I actually doesn't, I actually don't see any, any reason for doing it, so, Okay. 

**Micah Zoltu**
* I just wanna make sure we avoid getting into the situation that like the execution layer teams are in where, their gossip protocol is very frustrating because you have to support every previous version and it would be nice. 

**Mikhail**
* Yeah, that's the main point of  not supporting because this is similar to supporting all hard fors, that have ever happened, like in terms of engineering burden. Okay. So, getting back to,  the engine api to get capabilities method. Geth capabilities basically returns the all methods that currently supported by, by the EL. And what CL can does, can do with this method is just, you know, call in this method in the background with the same, some time out, say like five minutes or whatever  number of minutes a reasonable, and once it sees that the new method is added and CL just switch, switch  to the new one and uses this new one, once it's available. So that, that's the one of the ways to, to utilize this method. So the main question is like to see all CL clinets, will they use it, is it useful for, for them?  if not, so we'll probably, we'll likely to use the, this optimistic strategy as it does not introduce any, additional complexity. So see CL client please go to your, code basis and check out the engine API clients, and try to, in order to understand whether it's whether gate capabilities matter will would be beneficial or not.
*  So any questions or comments to this for it, as Danny said that probably sometimes we'll have to prepare the, payload for EL, that will not be able to, and we will not be able to make it backwards compatible this thing where it's considering. So I'll take look at this potential. And the other part is the, the basically decomposition the way that we want to decompose the, spec documents. obviously we do not want to have one specification document for every methods Ava speced out. It's just like, not just inconvenient. So there are two approach to the breakdown. One is the, breakdown and by fork. So whenever new fork is added, we have a new document that's back out, the new methods that are related to this fork was proposed originally. The other way to do this is to break down  by functionality. So if method works, a group of methods working with payload goes to one document, the other group of method that works with as goes to the other one, was proposed by like client, I just did like a couple of examples. You can take a look at them and, yeah, both have downsides and upsides, so probably functional is  more convenient for developers. Just take a look, add those two. 

**Danny**
* I'm a bit bias towards forks because it's the beast that I know, but I'm sure both end up working fine. 

**Micah Zoltu**
* In my experience with documentation, you should always pick the one that the person actually writing the documentation wants to do because it is really hard to find people to write documentation, so bend over backwards to make things easier for them. 

**Mikhail**
* What's good about functional thing is that you will have like, say new we one than we two and with three in one place, and you can incrementally, define the cation of we two based on top of we one. So that's probably, and it's easier to read and easier to reason about when you have everything in in, in, in the same screen. Yeah, that's the main, upside that I can see in this approach. 

**Danny**
* Yeah, I get it. I think my bias comes from the writer's side, you know, what am I what I want this new thing to look like? And assuming the writer probably knows what the old thing looks like, but I'm, I, that's just my opinion. I will cast into the wind. I'm pretty happy either way. Thank, this is really good stuff. 

**Mikhail**
* Yeah, thanks. And also in this functional breakdown, I try to, you know, to add the proposal also has this table ofs where they described, and the statuses of those methods, whether the method is deprecated or final or a draft. so instead of this,  I just try to, you know, write a status of each methods, alongside to the specification of this method. So it's probably easier,  to maintain and easier  to work with, to not create more entities that you, you should, you know, spend your attention on. Thanks everyone. Okay. 

**Danny**
* That's, So does look like we're honing in on this. I know that you did wanna present it to All core dev. Is that kind of the, the final blocker in, getting this ironed out? So sorry, then can you repeat, So  I know that you did wanna present this on All core dev as well. is that the final blocker in getting this  ironed out or what are the substantial bloggers at this point? 

**Mikhail**
* Oh, yeah,  I don't think it's a blocker actually. So, I would like to see all devs to chime in on the, get capabilities and basically we can debate on the, break the data composition, the way of the composition like, in a chat or whatever. and yeah, if get caps is, gonna be beneficial, so we'll have it and then we will need to ask EL client devs whether they like really, want to implement this as well. 

**Danny**
* Got it. 

**Mikhail**
* Yeah, we, we do care about EL  as well, so yeah, it probably makes sense, you know, to just give a quick, quick quick announcement on ACD but I'm sure that, I dunno, yeah, that's up to Got it. Probably quick announcement will be Useful. 

**Danny**
* So if you have strong opinions on caps, but it's chime and asap, But I would not say that, not now since this on Data blocker. Okay. Any other items for today? 

**Micah Zoltu**
* That'd a small quick one real quick. client diversity org has two data sources for consensus clients and they're wildly different. Do we know which one's correct or which one's closer direct or which one's most likely to correct? 

**Danny**
* Is this, This is the Lighthouse, so no one is a, one is a crawler and one is a crypto, one is a a block proposal attempt to figure out who's proposing blocks. One's gonna map to the stake weight, one's gonna map to node. I do, I'm looking at this crawler data and it looks very wrong, based off of my understanding and other crawler data. So one they're different, two, one of them looks wrong. 

**Micah Zoltu**
* And do you know which one is the one that looks wrong? One that says Lighthouse Is, sorry. 

**Danny**
* So block print is the one that tries to analyze validator stake distribution. The MEGALAB one is a crawler which would give us the node distribution and I'm pretty sure that is wrong and I think our understanding is block print is pretty good. There's gonna be some error, but Okay, that was it. 

**Micah Zoltu**
* Thanks. 

**Danny**
* Yeah, I'm not certain if there's a crawler that's in good shape. there is node watch, which is presumably necessary crawler as well, but I don't think that's been updated or maintained in a while. So, but gives a different view. Okay. Yeah. Anything else for today? 

**Arnetheduck**
* I can just make a quick announcement about Nibus. So we'll be pushing out a release I think today hopefully, big change in it. We're finally publishing a separate validator client, like we've had one in testing for like forever, but this is the release where it makes the official cut. So, we'll keep the integrated validator mode around. we welcome everybody that wants to run a separate validated client to join the Nibus family as well. 

**Danny**
* Nice. Yeah, I think the, machine separation is pretty valuable for a number of users. Cool. Anything else? 

**Saulius**
* Just, a question for members as well. So working on separating the data client for and the, so the built-in, data client is gonna to use, the API to run, or did you internally, did, did you keep the internal access  to the beacon mode? 

**Arnetheduck**
* This question for, so from a purely technical architecture point of view, the internal one uses, like a private version of the API obviously doesn't go through json or any of that stuff. And it also uses a couple of shortcuts which makes it more efficient, like, a lot of efficiency in Nibus and initially was based  on these assumptions and like gradually what we've been doing is, making sure that without losing efficiency we can expose the same kind of data to the validator client. 
* So internally there are a couple of assumptions that one can make when running the validator client inside the beacon mode, which makes it both a little bit safer. Like there are errors that simply cannot happen. so from that point of view, the internal validator client code remains more simple and, and, and we're going to keep offering it. but that said like the external validator client uses the same implementations, shall we say, it's just that there's a couple of extra failure modes that result from the fact that there's a socket in between. And from the fact that there are some like tiny pieces of information that are not exposed via that a validator client running inside the beacon can, can make use of. 

**Saulius**
* Okay, so just summarize. So you'll try to keep the internal well client more or less is that position of being internal in the client the right, Yeah. 

**Arnetheduck**
* And I mean it's still a great mode to run if you're just running a few validators because you only have one process, well now you have two or three, 

**Saulius**
* But I believe other clients are not following this approach and the more going with this public API approach is it Right. I think also offers internal their clients. 

**Danny**
* Perry wanted know, is the internal gonna have long term support on Nibu? 

**Arnetheduck**
* Yeah. It's taking around like there's no reason to remove it. What we've done is generalize the internal one to external one. And I mean it's also possible to mix and match numbers with, you know, Teku or Lighthouse, validator clients because they all use their the same rest api. 

**Danny**
* Got it. Okay. Anything else for today? 
* Thank you everyone. Oh, and we will meet two weeks from today and then we will, take off right around New Year for this call. So, talk to you all in two weeks. Thank you. Bye-bye bye. Thanks everyone. Thanks. Bye. 
