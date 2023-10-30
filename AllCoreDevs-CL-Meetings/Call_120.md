# Consensus Layer Call #120 Notes 
### Meeting Date/Time: Thursday 2023/10/19 at 14:00 UTC
### Meeting Duration: 1.5 Hrs
### [GitHub Agenda](https://github.com/ethereum/pm/issues/892 )
### [Audio Video of the Meeting](https://www.youtube.com/watch?v=KD07crJXN9U)
### Moderator: Danny
### Notes: Avishek Kumar 

--------------------------------------------------------------------------------------------------------

## Agenda

# 1. Deneb

## v1.4.0-beta.3

**Danny** [07:12](https://www.youtube.com/watch?v=KD07crJXN9U&t=432s): Hello! Welcome to Consensus Layer call 120. This is issue #892 in the PM Repo. I guess kind of as some of the last calls dominantly, just kind of checking in on Deneb, various things, testing, Devnet Analysis. If there are other discussion points, let me know when we get to the open discussion. Okay, so first of all I believe most of the Consensus Layer call devs probably saw that their v1.4.0-beta.3 is out. In that is the mainnet k configuration, which is already baked into KZG, so I don't think it's much of a change for you to be able to use it, as well as an additional gossip condition that Enrico found. Essentially, we weren't properly bounding the blob index. It allows us to prevent spam of totally invalid messages from being passed around. Big shout out to Enrico on that. I think other than that there are some additional tests, maybe a whisk update, but should be generally pretty good. And I believe that that configuration is to be used in Devnet 10. Does Devnet 10 exist? Let's transition, or any questions on the consensus specs release? All right, cool. 

## Devnet Updates

Let's jump into Devnet updates. First of all, does Devnet 10 exist? What's the status on that?

**Barnabas Busa** [08:59](https://www.youtube.com/watch?v=KD07crJXN9U&t=539s): So, we are waiting on client releases and some PRs to be merged, and we're hoping to launch tomorrow. Currently, the only image that we know that might work on Devnet 10 is prysm. No other EL / CL team has reported that they have a working image. Or a branch, yeah, we don't need a full release, just a branch that we can use, that we can build. The new KZG setup?

**Potuz** [09:32](https://www.youtube.com/watch?v=KD07crJXN9U&t=572s): Are we supposed to use the new KZG setup for this DevNet? 

**Barnabas Busa** [09:38](https://www.youtube.com/watch?v=KD07crJXN9U&t=578s): Yes.

**Potuz** [09:40](https://www.youtube.com/watch?v=KD07crJXN9U&t=580s): We, so, Golang clients cannot, unless we coordinate among Go KZG that it's not, hasn't included these changes, get and prysm.

**Danny** [09:56](https://www.youtube.com/watch?v=KD07crJXN9U&t=596s): Okay, so it's not an outer kind of configuration that has to be baked into Go KZG?

**Potuz** [10:03](https://www.youtube.com/watch?v=KD07crJXN9U&t=603s):  It's a problem with the way that we have dependencies. Get depends on Go KZG and prysm depends on Gas. So the way this needs to be updated is Go KZG needs to first make the changes, then Get needs to point to a master branch in Go KZG, then prysm needs to point to that, and then Go KZG needs to make a release, Get needs to point to that release, and then prysm report needs to report to that. Yeah, we probably need to solve this. This is not maintainable. Any change in Go KZG is a pain.

**Danny** [10:38](https://www.youtube.com/watch?v=KD07crJXN9U&t=638s):  Yeah, so I mean, one of the major intentions of Devnet 10 is to use that setup. So I guess we're blocked. We could move forward and add Geth and Prism, but yeah.
 
**Andrew** [10:57](https://www.youtube.com/watch?v=KD07crJXN9U&t=657s): For Erigon, we're also waiting on Go KZG release with the trusted setup. 

**Danny** [11:07](https://www.youtube.com/watch?v=KD07crJXN9U&t=667s): Got it!

**Gajinder** [11:08](https://www.youtube.com/watch?v=KD07crJXN9U&t=668s): On the Lota side and Ethereum JS side, I will release deneb bindings by tomorrow and try to integrate it. But I think even without all this, we have the flag to run with a custom trusted setup, right?

**Paritosh** [11:26](https://www.youtube.com/watch?v=KD07crJXN9U&t=686s): Yes, so there's two blockers right now for Devnet 10. The first one is the trusted setup and the second one is the issues we saw on Devnet 9 yesterday. We can of course go ahead with Devnet 10 without acknowledging any of those issues that would just basically be Devnet 9 but bigger. Or we could wait until we fix both of them and then start Devnet 10 at the cost of time.

# Testing Updates

**Danny** [12:02](https://www.youtube.com/watch?v=KD07crJXN9U&t=722s): These are the issues that Mario found in testing and then escalated to tests in the testnet environment, right?
 
**Paritosh** [12:12](https://www.youtube.com/watch?v=KD07crJXN9U&t=732s): Yeah, exactly.

 **Danny** [12:15](https://www.youtube.com/watch?v=KD07crJXN9U&t=735s): Ok, so these, we know they would be hit if we do send a certain series of bad and good blobs in relation to each other, right? A certain series of bad and good blobs in relation to each other, right?
 
**Paritosh** [12:29](https://www.youtube.com/watch?v=KD07crJXN9U&t=749s): Yeah, exactly. 

**Danny** [12:34](https://www.youtube.com/watch?v=KD07crJXN9U&t=754s): Mario, do you want to give us a quick on that, please?

 **Mario Vega** [12:38](https://www.youtube.com/watch?v=KD07crJXN9U&t=758s): Yeah, of course. So basically we are using the new tool that we are using on Hive.  So this thing is like a proxy that sits in between the beacon node and the validator client. We set it up yesterday on a Devnet on a single client combination. So every time that this client combination was proposed. What it did was basically just receive the unsigned block and blobs from the beacon node. And then it signed the block and the blobs, but it also created an extra seemingly valid blob. So the only difference between this blob and the correct blob is that the KZG was correct, the signature was correct, everything seemed correct, but it was broadcasted to a different peer. So basically one peer had the correct blob with the correct KZG signature and it can attest to the correct block. And the other one received this other incorrect blob. So what happened was when the block was eventually broadcasted, the clients received the block and the ones that received the incorrect blob, they were ignoring the correct blob. So at the end of the day, one side of the recipients that didn't prune the incorrect blob from their database, they will unable to follow the chain. This tool was configured this way and it kept doing this every time there was a proposal from them. So this was what we were seeing yesterday on the Devnet. And we have a Hive test for this, it's reproducible. So the clients can, if they want, just run this as many times as they want. The Hive test is very simple. It does the same thing every single slot over the course of an epoch. If there are too many missed slots, the test will fail. So they can immediately know if they have fixed or not the issue.
 
**Danny** [14:46](https://www.youtube.com/watch?v=KD07crJXN9U&t=886s): This is really exciting that this is in hive now. Enrico?

**Enrico** [14:53](https://www.youtube.com/watch?v=KD07crJXN9U&t=893s): Just to clarify, you said that some clients have these blobs into have these blobs into database, but I guess this is incorrect. Should be that might be more of like, cache, right? So this is a thing that we discussed recently. So you kind of poison the client cache and the client is not able to recover because it's not even trying to look up by root another time. Is this correct? Mario?

**David** [15:25](https://www.youtube.com/watch?v=KD07crJXN9U&t=925s): Yeah. I'm sorry. My understanding was different. 

**Mario** [15:29](https://www.youtube.com/watch?v=KD07crJXN9U&t=929s): I guess that is correct. This cache is not database.

**Danny** [15:35](https://www.youtube.com/watch?v=KD07crJXN9U&t=934s): It's persisted somewhere that prevents it from wanting to do the work again. Potuz?

**Potuz** [15:43](https://www.youtube.com/watch?v=KD07crJXN9U&t=943s): I just want to mention that this abstraction is better presented somewhere because in Prism it is actually currently database. We're not using a cash. 

**Danny** [15:53](https://www.youtube.com/watch?v=KD07crJXN9U&t=953s): I mean from the perspective of the test and where it gets both are coherent and makes sense.

**Enrico** [16:06](https://www.youtube.com/watch?v=KD07crJXN9U&t=966s): I think Tegu is not affected by this. We fixed this recently and basically we delete everything. And if the next block builds on top of the one that some of the network nodes seen as complete and good. We do then look up by route to everything. So we're going to redownload block and Blobs again, and we should be able to follow the chain with a bit of blob. 

**Danny** [16:49](https://www.youtube.com/watch?v=KD07crJXN9U&t=1009s): That makes sense. So you kind of protect yourself from doing way too much work in the single slot, but then use additional signal to catch up. Okay. Mario, so now that we have this additional ability to test both on the testnet and inside of Hive, do you have an updated list of what you intend to get there such that maybe some of the Devs here could take a look at it and add or modify in any case? 

**Mario Vega** [17:22](https://www.youtube.com/watch?v=KD07crJXN9U&t=1042s): Yeah, of course. I have a list of the test cases that we are doing in Hive, which is basically related to the possibilities of the Blobber. There's a list of actions that the Blobber can do and we can configure them in Hive. And this is basically the same thing that we are running on the Devnet. I can share the list. It's very simple. There are not that many slot actions at the moment, but we can increase that. If there are comments from the Devs that the stuff that you guys want to test, we can also include them. I will share the list.

**Danny** [18:00](https://www.youtube.com/watch?v=KD07crJXN9U&t=1080s): Cool again, this is awesome to get some basic networking testing in hive. Enrico, is your hand up?

**Enrico** [18:15](https://www.youtube.com/watch?v=KD07crJXN9U&t=1095s): Just want to also to mention what we discussed during a nice conversation with Mario which is related to this latest thing that Mario was talking about. So is it another condition in which a proposer actually, so the proposer if the block doesn't contain is not full of Blobs. So there is still a room of one or two blobs there. So he could play with these two additional slot kind of creating a Blob that is invalid and still related to the block and slot with an index that doesn't match any commitment in the block. So technically the data is available because all the data that is required by the block is available. But there has been seen by the node something additional that is incorrect because porteco is incorrect just because we saw a Blob with an index that doesn't match to any commitment in the block. So what we do, and we do it on propose, but I'm not sure if it is at the end is a flow in the client. So we actually don't import the block. 

**Dankrad Feist** [19:51](https://www.youtube.com/watch?v=KD07crJXN9U&t=s): Yeah, this is not necessary. I think the block would not be available in that case because it hasn't been committed in the block. 

**Danny** [20:03](https://www.youtube.com/watch?v=KD07crJXN9U&t=1203s): But the block has everything it needs. So you have to import the block otherwise that's going to cause.

**Dankrad Feist** [20:09](https://www.youtube.com/watch?v=KD07crJXN9U&t=1209s): Yeah, I agree. But I would just want to respond to the concern that they get free data availability. They don't. Because there's nothing provable on chain that data. 

**Danny** [20:22](https://www.youtube.com/watch?v=KD07crJXN9U&t=1222s): Correct but it can be passed around p2p. 

**Dankrad Feist** [20:27](https://www.youtube.com/watch?v=KD07crJXN9U&t=1227s): So they get like the proposer can like basically put some extra load on P2P that is true but they don't get any benefit from this and they get a slight down they get a slight downside which is that their block is slightly less likely to confirm because they like increase. They often risk because it has competition with the other blobs so I don't see any reason why any proposer would do this.

**Danny** [21:00](https://www.youtube.com/watch?v=KD07crJXN9U&t=1260s): I know Enrico is trying to make a claim that there's free data availability. I think he's trying to make a claim they can induce load on the P2P and if we're doing different import strategies on this it can cause the network split. And it's really important that we don't do different strategies on this. And it's really important that we import even if you see invalid  extraneous blobs because somebody could easily not have seen those and do the import.

**Dankrad Feist** [21:23](https://www.youtube.com/watch?v=KD07crJXN9U&t=1283s): Right what you could do is not attest to such blocks that would be okay. But you should not like on a Node level you should not exclude them from the fork Choice otherwise you risk a split. 

**Enrico** [21:35](https://www.youtube.com/watch?v=KD07crJXN9U&t=1295s): Well I'm not saying that I'm not importing that anytime in the future. I'm just saying that I'm not importing that in that moment. So I'm going to import I'm going to test on the previous head but if the next block again Builds on top of it. Then we just look up by root the data that we need. And we actually not even realize that we an extra blob floating around because we are not even requesting for it. I probably not.

**Dankrad Feist** [22:07](https://www.youtube.com/watch?v=KD07crJXN9U&t=1327s): But we would at that point verify that all the blocks that are blocks that are referred are available. Yeah I mean that seems okay but maybe too much complication.

**Danny** [22:18](https://www.youtube.com/watch?v=KD07crJXN9U&t=1338s): Yeah a mixed strategy here is at least going to like cause some clients to be more profitable than others in relation to such an error flash attack because some are gonna like. It depends on kind of if you sit on the majority or not in terms of the attestation on whether it's going to come in or not like so it this is probably something that should at least have a note in the spec. 

**Enrico** [22:46](https://www.youtube.com/watch?v=KD07crJXN9U&t=1366s): But I think like there is also well assuming that there might be something malicious attached to this behavior maybe there is no advantage to do that but if that was next proposal we're going to reorder the block. That's the thing. 

**Danny** [23:12](https://www.youtube.com/watch?v=KD07crJXN9U&t=1392s): So if depends on the attestation. If it has enough attestation you can't.

**Dankrad Feist** [23:18](https://www.youtube.com/watch?v=KD07crJXN9U&t=1398s): I would be much more careful with these things about reodering a block because you are interfering in the fork choice Rule and we don't want to normalize that. So anything like that. I feel like should actually be an agreement that we all have like. I have a similar feeling about the other like reorg Glade blocks thing that it was a bit too hasty to just say it's okay. If some clients do that like it seems to me like something that affects the fork choice is something that we really need to have a quite a strong agreement on that. We're okay with that because otherwise anyone else will also think they can also interfere with the Fork choice in such ways and that's just not okay.

**Danny** [24:07](https://www.youtube.com/watch?v=KD07crJXN9U&t=1447s): But to Enrico to your point this is much more dangerous for the the local client than even this other Fork choice rorg for late blocks because you make yourself blind to the block and unaware of you know even the probability in relation to what you assume is going to happen in relation to the attestations you've seen by doing. So it and seems strictly worse than just having it in your view.

**Enrico** [24:40](https://www.youtube.com/watch?v=KD07crJXN9U&t=1480s): Yeah and moreover as we already know that probably we are the minority because we are probably the only one that does this. So if we know in advance these. So could that much there must be.

**Danny** [24:59](https://www.youtube.com/watch?v=KD07crJXN9U&t=1499s): Right I do think that a note about invalid blobs side cars in beyond the you know index the highest index of the commitment in the block should not invalidate the block. I think just an explicit note about that is probably pretty important such that anyone reading the spec doesn't accidentally put themselves in a forkable spot. Again you know barring knowing Network distributions like not doing the import and then building upon what is prior and not having a view of attestations. You know seems strictly just more dangerous than doing the import and knowing the knowledge should.

**Dankrad Feist** [26:02](https://www.youtube.com/watch?v=KD07crJXN9U&t=1562s): I also think this is much less important than like say like the late block reorg at least like there is a gain that the proposer gets from this. Which we kind of don't like which is why we do want to like we do kind of like punish punishing them in some way here there is no gate there is a potential like slight load increase by a maximum of factor of 2. Which we kind of say is like at least as a temporary load is okay anyway. Because that's just the Maxum of blobs. And so like the attack Vector seems very limited like basically oh yeah like node band with requirements will go up not even by a factor of 2 and yeah you don't really get any gains from that. So like I would say do nothing is the best. 

**Danny** [26:56](https://www.youtube.com/watch?v=KD07crJXN9U&t=1616s): I think, I generally agree, I do think that I mean anything in the play around additional blobs. And these are just primarily like a vector for potential Network splits like sending invalid ones and valid ones. At the same time sending ones in excess and potentially like having people consider their block differently like these are all these all hinder your ability to get a block in but become strategies for views Enrico.

**Enrico** [27:30](https://www.youtube.com/watch?v=KD07crJXN9U&t=1650s): And just another side comment if this becomes something that we consider important should we consider to introduce Slashable events. Next work at this point. 

**Dankrad Feist** [27:46](https://www.youtube.com/watch?v=KD07crJXN9U&t=1666s): That would be the correct way if we actually concerned about it but it seems very excessive to me in terms of the extra risk it adds for the gain it provides here.

**Danny** [27:59](https://www.youtube.com/watch?v=KD07crJXN9U&t=1679s): The potential slash event becomes more valuable probably for sending conflicting blob commitments than sending these extraneous blobs sorry conflicting sending blob, an a valid and an invalid one for index zero double sign. Right now you just kind of you have to you just have these like gossip conditions that try to do anti-dos. We don't really have like a crypto economic reaction to it because the consensus doesn't know anything about these side cars. I think it's certainly worth having the conversation.

**Dankrad Feist** [28:35](https://www.youtube.com/watch?v=KD07crJXN9U&t=1715s): If we can get both of these into one slashing condition then it would be preferable yes.

**Danny** [28:40](https://www.youtube.com/watch?v=KD07crJXN9U&t=1720s): Well and if we were prioritizing the other.

**Dankrad Feist** [28:44](https://www.youtube.com/watch?v=KD07crJXN9U&t=1724s): I think slashing conditions are realistically very high cost though in terms of like how deep the changes are. We have to touch the validators which we haven't really for a long time and like what risks they add how that changes the cost benefit analysis for stakers. And so on like it's a but I mean it's not it's not out of the question.

**Enrico** [29:10](https://www.youtube.com/watch?v=KD07crJXN9U&t=1750s): I think the Slashable condition have to be two because there are Slashable condition comparing two blobs one blob with another blobs conflicting. And one is comparing a blob that is inconsistent with the corresponding block. So comparison between block and blobs and comparison between blobs. 

**Danny** [29:34](https://www.youtube.com/watch?v=KD07crJXN9U&t=1774s): You could potentially both could potentially reduce to being inconsistent with the current block yeah but that's a bit different.

**Enrico** [29:45](https://www.youtube.com/watch?v=KD07crJXN9U&t=1785s): Right. 

**Dankrad Feist** [29:48](https://www.youtube.com/watch?v=KD07crJXN9U&t=1788s): So then basically the cost of sending conflicting position commitments is not sending a block which is like yeah a big opportunity cost.

**Danny** [29:57](https://www.youtube.com/watch?v=KD07crJXN9U&t=1797s): Yeah like the double signing is also much easier to like make sure you're not doing in the context of a validator client whereas like making sure your signing is correct in relation to something is much more difficult and likely for ER. 

**Dankrad Feist** [30:14](https://www.youtube.com/watch?v=KD07crJXN9U&t=1814s): Oh right I was thinking of going for the other one I was thinking of only having it with respect to them correct us with respect to the block.

**Danny** [30:24](https://www.youtube.com/watch?v=KD07crJXN9U&t=1824s): Yeah but that's intuitively much more difficult thing for the small validator client to get correct. I think that it's you know there's some read on here on like slashing was not and some some desire to do so and not it's certainly worthwhile exploration but I don't think it's something we need to continue on the conversation today. Certainly when we had these conversations in Austria and after around blob de coupling. We did make the decision around using essentially our P2P, anti-dos and peer scoring conditions to handle this. Obviously if we've gotten more information around some of the issues and concerns. Here we could escalate it to potentially do crypto economic condition. But well you do get the block eventually.

**Potuz** [31:34](https://www.youtube.com/watch?v=KD07crJXN9U&t=1894s): Yeah I'm just talking about this thing of the peer scoring we cannot downcore the peer that is giving us these bad blobs. Because we haven't had got the block to check this. So this is the real problem here that we have someone that is actively malicious. And we cannot penalize it because when we find out that he was malicious we already lost who this guy was.

**Enrico** [31:54](https://www.youtube.com/watch?v=KD07crJXN9U&t=1914s): Well you could also track the peer that's sending you but you could say you could receive things from two different peers. So even if you track who is the sender of a given message then you end up in the same situation yeah.

**Danny** [32:17](https://www.youtube.com/watch?v=KD07crJXN9U&t=1937s): Agree right okay. So in two relations like the peer scoring in a lot of scenarios is not possible but the anti-dos conditions combined with the fact that it's not incentive compatible to get your block in is kind of what we're relying on here. You know, if you send a bunch of these messages. It's very likely you just increase the likelihood of orating your block at the potential gain of view splits and compounding things in relation to view spits for for gain. So like that's kind of the tradeoff space here without adding a slashing condition. I can make an issue around this and toss it in the Electra tracker and it's something that we could potentially talk about. As we move into that conversation are people comfortable with that or is it something. We need to continue to hammer on right now Mario?

**Mario Vega** [33:30](https://www.youtube.com/watch?v=KD07crJXN9U&t=2010s): Yeah so Potuz, you mention that you want this documented where do you want for us to document this What's the best place to document this for you?

**Potuz** [33:41](https://www.youtube.com/watch?v=KD07crJXN9U&t=2021s): Oh any place is fine. I think we're all in Discord whatever you you put the few lines just to make sure that I understood the problem correctly but it seems to me that tech one prism are acting exactly the same way. and that also seems to me to be the incorrect way. 

**Enrico** [33:57](https://www.youtube.com/watch?v=KD07crJXN9U&t=2037s): Yeah I think we can discuss on the issue that Danny is about to open. So we can maybe Define the thing.

**Danny** [34:06](https://www.youtube.com/watch?v=KD07crJXN9U&t=2046s): Yeah so I'm going to make an issue around the potential tradeoffs around you know the Dos conditions here and slashings for a future conversation I will make a PR about a node about not invalidating blocks if you see valid invalid side cars in excess of the index in the block in that PR. We can talk about if we want more explicit guidance than that cool and I'll share both on Discord so people are aware. Once I pop them in there okay let me take a quick note about getting both of these in Okay. Cool, Dankrad, it might be worth at least putting your thoughts in the chat in relation to Potuz recent question okay um so we do have devnet 9 currently we're moving merging towards devnet 10 with some of these known blockers. And Gajinder you had some sort of analysis in relation to and devent 9 on Twitter the other day I didn't realize. And so you put a comment up this morning. Would you mind going through that and giving us some context?

## @g11tech blob/ Latency analysis

**Gajinder** [35:51](https://www.youtube.com/watch?v=KD07crJXN9U&t=2151s): Yep so I basically last weekend.

**Danny** [35:56](https://www.youtube.com/watch?v=KD07crJXN9U&t=2156s): Do you want to share your screen I guess once you get to that point or share a link okay.

**Gajinder** [36:48](https://www.youtube.com/watch?v=KD07crJXN9U&t=2208s): Okay so over the weekend when blobs were being spammed in the devet 9. So I collected some data around gots arrivals of full Block Plus blobs. So basically blocks having one blob two blob three blob four blob five blocks having one blob two blob three blob four blob five six blobs. And so these timings are pre validation done on them. And what I did was basically then plotted a histogram and as well as the percentile scores. And basically this graph shows that how drastically blob, where the blob where there are six blobs in the block how drastically basically those arrival times are quite late. So if we look at this metrix which is the percentile scores of how / when the blob and blocks are fully available. And so even though these numbers look small because there is no it takes no time to produce a block on Devnet 9. Because these are the only transactions that were being bundled over there. So we can see that you know blob where blob is equal to six it takes it introduces quite a large amount of latency. And we can also assume that all these nodes are in the same data center. So that latency is still not facted in. And basically this leads to my
Projection.

 **Dankrad Feist** [38:44](https://www.youtube.com/watch?v=KD07crJXN9U&t=2324s): What protection.

**Gajinder** [38:47](https://www.youtube.com/watch?v=KD07crJXN9U&t=2327s): So I wait a second I not able to move this bar. 

**Dankrad Feist** [38:55](https://www.youtube.com/watch?v=KD07crJXN9U&t=2335s): So this is important times this is when the blog is actually recognized is there any significant Delay, as having the seeing them on the network.

**Gajinder** [39:09](https://www.youtube.com/watch?v=KD07crJXN9U&t=2349s): Yeah, so one second I'll just take you over the projections. So these are the Blob projections that you know what I did was I took a lodestar node for the mainnet. And basically calculated its percentile scores for various arrivals of the block. And the column that you see for blob is equal to zero those are the actual percentage scores that might not saw
for using load star. And then I added the depths of the latency that I got there from with respect to the Baseline blobs is equal to zero. To give an naive projection. So if I add the extra latency that has been introduced and if I look at this 95 percentile score. 

**Dankrad Feist** [40:04](https://www.youtube.com/watch?v=KD07crJXN9U&t=2404s): What do you add it to? What do you add your latency to?

**Gajinder** [40:08](https://www.youtube.com/watch?v=KD07crJXN9U&t=2408s): I add my latency to the current latency of blocks that I see on my node.

**Dankrad Feist** [40:17](https://www.youtube.com/watch?v=KD07crJXN9U&t=2417s): That doesn't seem like the correct thing to do though because like there are things happening concurrently here. Like these blobs are not it's not like once you're node it has done everything that it does now now they propagate the
Blobs. 

**Gajinder** [40:31](https://www.youtube.com/watch?v=KD07crJXN9U&t=2431s): Right. So what I have done is that these scores are with respect to the actual blobs latency that is observed on devnet 9. So blobs is equal to Zero is basically when you see a blob with no blobs. And if there is a significant diff between blobs is equal to Z and blobs is equal to 6 that means that increasing the number of blobs is adding to the latency.

**Enrico** [41:09](https://www.youtube.com/watch?v=KD07crJXN9U&t=2469s): And this is pure Network latency this is not considering any validation block import right. 

**Gajinder** [41:17](https://www.youtube.com/watch?v=KD07crJXN9U&t=2477s): Correct.

**Dankrad Feist** [41:18](https://www.youtube.com/watch?v=KD07crJXN9U&t=2478s): Wait how so that's what confused me that's what I just ask if this after this measures when you actually import like when your client actually says everything is is done now I have the block or is it when you saw them on the network.

**Gajinder** [41:38](https://www.youtube.com/watch?v=KD07crJXN9U&t=2498s): As soon as my node saw this and this is pre processing right. So that's what I did basically I add did latency to the actual latency that my node is seeing and did a naive projection.

**Dankrad Feist** [41:57](https://www.youtube.com/watch?v=KD07crJXN9U&t=2517s): I do not understand why the blobs are arriving after the block then because we're propagating everything in parallel.

**Gajinder** [42:06](https://www.youtube.com/watch?v=KD07crJXN9U&t=2526s): So blocks can arrive at or it's can arrive before or at any anywhere between or after. I mean it's not really following a particular order. But what I'm saying is that so blobs is equal to
Zero is the Baseline that I matching with the latency that I'm sitting I'm seeing on the mainnet today and whatever is the diff for example blobs equal to 6 minus blobs equal to 0 so whatever is a diff I added the diff. So basically I added the extra latency introduced in my projections I mean it's a name way to do it but that's what I did.

**Dankrad Feist**  [42:46](https://www.youtube.com/watch?v=KD07crJXN9U&t=2566s): Okay I would like to because something like I already commented in the threat these are more than the mainnet latencies we saw from actually just adding extra data to the
Blob. So it feels like something can't be right about this granted.

**Danny** [43:06](https://www.youtube.com/watch?v=KD07crJXN9U&t=2586s): These are 95 and 98%.

**Dankrad Feist** [43:10](https://www.youtube.com/watch?v=KD07crJXN9U&t=2590s): Right I know. I agree.

**Gajinder** [43:21](https://www.youtube.com/watch?v=KD07crJXN9U&t=2601s): Yeah so I mean some other client I can't claim that this analysis is comprehensive because obviously it has not been done over multiple nodes and multiple Network conditions. But yeah some other client team can sort of Reverify it and check all the steps, it would be nice. 

**Danny** [43:43](https://www.youtube.com/watch?v=KD07crJXN9U&t=2623s): It would be definitely be valuable to get such data from another client latency I mean we did see with our mainnet experiments with you're using these kind of events some wide disparities across clients. But yeah I also do I'm not 100% sure that like these tails are much different than what we saw on Mainnet because we do have you know tails in excess of you know the 4 seconds but in by and large in most cases seeing them pre four seconds.

**Dankrad Feist** [44:14](https://www.youtube.com/watch?v=KD07crJXN9U&t=2654s): We didn't see Last drop adapations though, which like if we saw this Beyond 4 seconds we would have seen like not at below 1 mega blobs right. So it doesn't feel like this data can be correct it's my feeling. I mean I'm happy to recheck what exactly I felt with on like what we get had there. We still I think we can still find the dashboards but like I feel like the way also the way of computing this is overly pessimistic because it seems like it makes the assumption that blobs are not propagated in parallel anyway.

**Gajinder** [45:05](https://www.youtube.com/watch?v=KD07crJXN9U&t=2705s):  I mean it's not really making that assumption because what it's doing is that it's actually comparing the data that the node is seeing on blobs is equal to six and comparing it.

**Dankrad Feist** [45:18](https://www.youtube.com/watch?v=KD07crJXN9U&t=2718s): So, what is the Baseline latency on this test net for blobs that are with zero blobs. With zero blobs what's the Baseline latency because you said you normalized it to 0 seconds.

**Gajinder** [45:30](https://www.youtube.com/watch?v=KD07crJXN9U&t=2730s): Yeah, so Baseline is present in the data itself and I think one second. So you get 95% within half a second and then you get 98 percentile with 65 seconds.

**Dankrad Feist** [45:51](https://www.youtube.com/watch?v=KD07crJXN9U&t=2751s):  Right which is much slower than mainnet which you kind of have to take into account because like this time is still available on Mainnet to propagate blobs like if like, I don't know, two seconds or three I don't know what the exact number is on Mainnet then like during this time blobs can still propagate assuming mainnet is not saturated with like in
Bandwidth.

**Dankrad Feist** [46:18](https://www.youtube.com/watch?v=KD07crJXN9U&t=2778s):  If you see what I mean the analysis that I have done on some of the main net blobs for example lodestar missed on. So I have done these kind of analysis and I see that you know generally the proposal is published after 2 second because by one and a half second you get block from either execution or from  the me itself and then basically you sign it. And then you propagate it. So by the time you end up propagating it's already more than two plus seconds and that is lots are not also shows that that is the latency that the lodestar node is seeing on the mainnet blobs. So I mean whatever so right now in this particular devnet 9. We can assume that all that time is squished to zero is squished to whatever blobs is equal to zero. So whatever is the additional latency will definitely add up when the blobs will also surface on Mainnet. 

**Dankrad Feist**  [47:25](https://www.youtube.com/watch?v=KD07crJXN9U&t=2845s): I think, I strongly disagree with that statement you cannot just add this when we're like explicitly doing things in parallel. It's not like because that what you're saying is basically oh like currently blocks take 3 seconds to propagate and now we're adding the blobs. And that's another like one second or something when in reality all of them start at time zero and yes the blocks takes longer and maybe the blocks take longer but they're still in parallel so you still can't add these things.

**Potuz**  [48:01](https://www.youtube.com/watch?v=KD07crJXN9U&t=2881s):Are you sure they start at second zero, Dankrad? Because most blocks come from the Builder and I don't know how the Builder path is going to be on disseminated blobs there's a big latency now in actually negotiating the with the builder so if the Builder actually is going to be starting to send the blobs
later then I think your point is no longer valid.

**Dankrad Feist** [48:21](https://www.youtube.com/watch?v=KD07crJXN9U&t=2901s): That I agree with and we can also like it might be possible that are playing latency games already like I mean well we very likely know that some people are but these are economically in incentivized so these people will if they see that now they're they're missing blocks because they're sending blocks late they will just have to like decrease their latency if it's that.

**Danny**  [48:46](https://www.youtube.com/watch?v=KD07crJXN9U&t=2926s): And to be fair the difference.

**Dankrad Feist** [48:47](https://www.youtube.com/watch?v=KD07crJXN9U&t=2927s): Technical negotiation process then I agree with you but it doesn't feel to me like that takes two seconds that seems very unlike.

**Danny**  [48:55](https://www.youtube.com/watch?v=KD07crJXN9U&t=2935s): And it might be some fixed latency added from there but that's not the same as the latency added from the parallelization of the the network dissemination.

**Gajinder**  [49:06](https://www.youtube.com/watch?v=KD07crJXN9U&t=2946s): Yeah so towards that argument where we are saying that you know the blobs should alive parallel but that is not something that we are seeing in devet 9. Because there is a huge disparity in latency between blobs is equal to zero blobs. And blobs is equal to six blobs. So maybe we need to look at the clients. Or you know we need to look at the implementations where the blobs are not being transmitted in parallel or they are being transmitted one by one. I think so it would be yes definitely nice whether a second client can sort of confirm my observations. And it would be nice if all the blocks if there is a very little discrepancy between blobs is equal to Zero and blobs is equal to six column in devnet 9 itself then I can sort of agree with you that things will happen in parallel. And it will not really add to a different latency number over there.

**Danny**  [50:04](https://www.youtube.com/watch?v=KD07crJXN9U&t=3004s):I also I don't think Dankrad's point is that there won't be additional latency for full Gathering of information. If you have you know three verses six. But that it shouldn't necessarily be like a a strict like lineary relationship.

**Dankrad Feist** [50:20](https://www.youtube.com/watch?v=KD07crJXN9U&t=3020s): Yeah just adding it just seems overly pessimistic that's what I say.

**Gajinder** [50:27](https://www.youtube.com/watch?v=KD07crJXN9U&t=3027s): Right it might but we should basically do an experiment and sort of figure this out I think at least that this experiment  warrants at at most at least this much.

**Danny** [50:40](https://www.youtube.com/watch?v=KD07crJXN9U&t=3040s): I agree especially getting another client to gather similar data and for those that are gathering it to think about you know if the current presentation and extrapolations make Sense. Or if we want to modify some of that Enrico.

**Enrico** [50:56](https://www.youtube.com/watch?v=KD07crJXN9U&t=3056s): Yeah currently teco is not able to show the arrival time of the of the gossip message the actual one so we are adding a little bit of latency there but we are working on Gathering the exact arrival of the message down from the P2P layer I don't know if there some other there are some other clients that are currently better showing this arrival times. 

**Danny** [51:29](https://www.youtube.com/watch?v=KD07crJXN9U&t=3089s): And poan said he's going to try to gather some data on Lighthouse by tomorrow which is great are we still spamming blobs though in the same way on devnet 9. Or do we need to turn that back on for this data analysis data gathering?

**Barnabas Busa**  [51:45](https://www.youtube.com/watch?v=KD07crJXN9U&t=3105s): I don't think we have blobber running. Right now we turned it off because prism had the.

**Paritosh** [51:53](https://www.youtube.com/watch?v=KD07crJXN9U&t=3113s): No that that's not blob but we have Mario's transaction flops by running all right.

**Dankrad Feist** [52:00](https://www.youtube.com/watch?v=KD07crJXN9U&t=3120s): Is is prism still bored on.

**Danny** [52:03](https://www.youtube.com/watch?v=KD07crJXN9U&t=3123s): Yes okay so probably be good to get prism back into the fold so that.

**Paritosh** [52:09](https://www.youtube.com/watch?v=KD07crJXN9U&t=3129s): I just updated prism get once so I'll have look.

**Potuz**  [52:12](https://www.youtube.com/watch?v=KD07crJXN9U&t=3132s): If you run that PR it should be it should be fine.

**Paritosh** [52:15](https://www.youtube.com/watch?v=KD07crJXN9U&t=3135s): Yeah I just run it on prysm get one I'm validating if it's fine and if it is then out the rest of them.

**Terence** [52:22](https://www.youtube.com/watch?v=KD07crJXN9U&t=3142s): You also need to resync the DB.

**Potuz** [52:26](https://www.youtube.com/watch?v=KD07crJXN9U&t=3146s): I don't think so because we never imported those blocks so it's going to remove the blobs from the DB.

**Terence** [52:35](https://www.youtube.com/watch?v=KD07crJXN9U&t=3155s): Oh that's right unless, yeah, but we need to do that for initial syncing. Right!

**Potuz**  [52:47](https://www.youtube.com/watch?v=KD07crJXN9U&t=3167s): Yeah that's probably right I mean.

**Paritosh**  [52:53](https://www.youtube.com/watch?v=KD07crJXN9U&t=3173s): You can set into prism, get one and have a look at let's do it. 

**Terence** [52:57](https://www.youtube.com/watch?v=KD07crJXN9U&t=3177s): That sounds good I will look into this.

**Enrico** [53:02](https://www.youtube.com/watch?v=KD07crJXN9U&t=3182s): Another thing that we can still gather some data from teco maybe are not super accurate but could be worth to have so when you run per this session if we can enable those famous logs maybe we can you can ping me. And so I can grab all these logs and already have some tool Lings and scripts that crash crunch this data. And put it in a spreadsheet so we can do some analysis on our side as well.

**Paritosh** [53:37](https://www.youtube.com/watch?v=KD07crJXN9U&t=3217s): Yeah sure I can run that. But in the meantime do have a look at the grafana dashboard here if it's something we can modify in the dashboard directly. Because we're listening to the event stream and we're adding how long block side cars are taken to propagate and how long the blob associated with the block has taken to propagate as seen by each of these nodes.

**Danny** [54:21](https://www.youtube.com/watch?v=KD07crJXN9U&t=3261s): Okay any amount of additional data and additional perspective on how to parse this data would be super valuable I would recommend in the event that we do collect a bit more data to pop this on the ACBE call for at least a quick look next week. If we do have additional data to look at because obviously safety of propagation of data in a relatively small environment is very important. Any other comments on blob data load in relation to Devnets or testnets or mainnet before we move on today. Great I think you goes in there see so generally the big things to further talk about if anyone has anything or anything in relation to devnet, anything in relation to testing, anything in relation to Deneb for today. 

**Paritosh**  [55:42](https://www.youtube.com/watch?v=KD07crJXN9U&t=3342s): Just wanted to clarify the conditions for devet 10 right now. Do we just wait for the trusted setup file and as soon as everyone's updated that we roll out Devnet 10 or do we want to wait for further changes on collecting data on Devnet 9 or figuring out a slashing condition or whatever it is.

# 2.Research, spec, etc

**Danny** [56:02](https://www.youtube.com/watch?v=KD07crJXN9U&t=3362s): No so definitely on Slashing additions we're that is not part of the deneb conversation currently as for the clarification around invalid blobs and excess of the index in Blob that will be like a probably small conversation in the specs repo that might modify a little bit of behavior in some of these extraneous scenarios. But I don't think we need to wait on that I would want to see a fixed prism which it seems like we're on the border of having that. So I would put the main blockers on getting the the setup in place everywhere and making sure Prism Works over the next like hour. 

**Paritosh** [56:51](https://www.youtube.com/watch?v=KD07crJXN9U&t=3411s): Sounds good.

**Barnabas Busa** [56:54](https://www.youtube.com/watch?v=KD07crJXN9U&t=3414s): In order to have a launch 
orrow for Devnet 10. We would need to have working branches for most clients though is that something that we could get done. Probably by end of today. So we can start testing tomorrow. 

**Sean** [57:17](https://www.youtube.com/watch?v=KD07crJXN9U&t=3437s): Yeah for Lighthouse we can do that.

**Potuz** [57:23](https://www.youtube.com/watch?v=KD07crJXN9U&t=3443s): It looks that for prism is to be very easy lightclient already posted a branch With the Changes needed and our changes are very small.

# 3. Open Discussion/Closing Remarks

**Danny** [57:36](https://www.youtube.com/watch?v=KD07crJXN9U&t=3456s): Okay can anyone not meet that.

**Barnabas Busa** [57:45](https://www.youtube.com/watch?v=KD07crJXN9U&t=3465s): That could all the client teams please leave a comment in interrupt regarding which branches we should use. Or which latest images we should use then we can start working on it tomorrow morning and possibly make a launch around noon or 1 p.m Central European Time.

**Andrew** [58:10](https://www.youtube.com/watch?v=KD07crJXN9U&t=3490s): Sorry a question about trusted setup because I mean we could have a an Erigon version without like without waiting for a go KZG release but I would prefer go KZG released so that we can switch to a released version of go KZG for The Trusted
Setup.

**Potuz** [58:38](https://www.youtube.com/watch?v=KD07crJXN9U&t=3518s): I don't think go KZG can release. I don't know if kCG is here but he was explaining that if go KZG releases then it would break Gap until Gap actually points to the new changes.

**Andrew** [58:58](https://www.youtube.com/watch?v=KD07crJXN9U&t=3538s): So there is some kind of weird like infinite dependency between go KZG and gass.

**Potuz** [59:06](https://www.youtube.com/watch?v=KD07crJXN9U&t=3546s): So the problem is that golang is going to think that there no that they're breaking changes and it's going to pull if you update go kcg then with a release then if you download Gass it's golang is going to pull the new changes from go kcg and those are actually breaking changes. This is also internal breaks prysm.

**Barnabas Busa** [59:36](https://www.youtube.com/watch?v=KD07crJXN9U&t=3576s):  We had the other trusted set up how did that work? We had a previously working trusty setup that was not the real data and that did not break anything so how did?

**Potuz** [59:50](https://www.youtube.com/watch?v=KD07crJXN9U&t=3590s): Yeah but the thing is the thing is that now these changes are actually breaking changes but golang since they're both pre version one golang will not recognize them as breaking changes. And it will automatically update for a new release. So anyone that downloads the Gas repo and tries to build is going to build a broken client. Gas there's a channel I'll link a discussion in the RNG and with an explanation from kevf.

**Andrews** [1:00:25](https://www.youtube.com/watch?v=KD07crJXN9U&t=3625s): It sounds strange to me because in go you typically like you can fix a specific version of your dependencies in go mode right so that that's I don't quite understand why you can't do that with prism or.

**Potuz**  [1:00:40](https://www.youtube.com/watch?v=KD07crJXN9U&t=3640s): Yes you can but that's the thing that then we need to coordinate the three clients to actually have these changes.

**Andrews** [1:00:49](https://www.youtube.com/watch?v=KD07crJXN9U&t=3649s): But does go kcg depend on gass or prism still okay.

**Potuz** [1:00:58](https://www.youtube.com/watch?v=KD07crJXN9U&t=3658s): No it's the other way.

**Danny** [1:01:19](https://www.youtube.com/watch?v=KD07crJXN9U&t=3679s): Okay can we take any additional particulars around this dependency issue? Outside of the call.

**Andrews** [1:01:31](https://www.youtube.com/watch?v=KD07crJXN9U&t=3691s): Yeah sure okay.

**Danny** [1:01:41](https://www.youtube.com/watch?v=KD07crJXN9U&t=3701s): Anything else on deneb today. All right. Any other discussion points on anything today. Get those images and branches to Barnabas developers team and we'll keep moving thanks everyone talk to you soon.

---------------------------------------------------------------------------------------------------------------------------------------
# Attendees
* Danny
* Andrew Ashikhmin
* Barnabas Busa
* Carl Beekhuizen
* Daniel Lehrner
* Dankrad Feist
* Echo
* Enrico Dell fante
* Guillaume
* Haiao-Wei Wang
* Joshua Rudolf
* Justin Florentine
* Mario Vega
* Mikhail Kalinin
* Paritosh
* Potuz
* Saulius Grigaitis
* Stefan Bratanov
* Stokes
* Terrence
* Tim beiko 
* Pooja Ranjan

### Next Meeting Date/Time: November 02, 2023 at 1400 UTC.

