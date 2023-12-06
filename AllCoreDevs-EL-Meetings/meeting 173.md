# Execution Layer Meeting #173
### Meeting Date/Time: Oct 26, 2023, 14:00-15:30 UTC
### Meeting Duration: 60 Mins
### [GitHub Agenda](https://github.com/ethereum/pm/issues/889)
### [Audio Video of the Meeting](https://www.youtube.com/watch?v=P_a3s6zNFEk) 
### Moderator: Tim Beiko
### Notes: Avishek Kumar

—------------------------------------------------------------------------
# Agenda
_____
## Dencun Updates
          
**Tim Beiko** [4:42](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=282s): And we are live. Welcome everyone to ACDE 173 and so bunch of Dencun discussion today so around Devenet 10. I think there's been some new analysis done as well on the CL block and blob receiving and processing times some updates on KZG and I think once we go through that. We can chat about what we want to do next for Dencun. And then finally Carl will give us an overview of the Roll Call series that's kicked off last week. 

## devnet #10 updates

And there's an EIP around empty accounts that Danno wanted to discuss but I guess to start We've launched Devnet #10. And Pari I saw the developers team put together a pretty comprehensive dock analyzing how things have gone so far. Do you want to take a few minutes to walk through that.

**Paritosh** [5:41](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=341s): Yeah maybe Barnabas can first set the stage and then I'll continue after with the analysis.

**Tim Beiko** [5:46](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=346s): Yeah, sounds good and I'll share this is the doc I've just shared in the chat. Is Barnabas here?

**Barnabas Busa** [5:55](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=355s): Yes I'm here yeah. I Can Begin I was just also looking for the doc. So basically we  launched with 330,000 Validators. So this is just slightly above the churn limit of four. So we started out with a churn limit of five and we wanted to test to make sure that the churn limit thing is working the way we want it to. And in Epoch 256 we have hit deneb. And at that point we had about 5,000 validators in the deposit queue and a few thousand in the exit queue. And a few EPOCH later I think in Epoch 260 we started to see that the churn has indeed went down from 5 to 4. So that's working and what else we had a couple of open issues that should be now closed. So we found a bug during Epoch 32 to 35 during a non-finality incident that I have caused by mistake. That prysm couldn't think back after the churn has started finalizing again. But this issue might have been solved already. I'm  not sure the issue has been closed by Prysm. And there was another issue by teku regarding some Mass deposits where the teku nodes were not voting on the correct deposit had also seem to be closed by now. And we have some upsending MEV related issues that maybe we can discuss a bit later.

**Tim Beiko** [7:41](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=461s): Awesome thanks. 

**Paritosh** [7:43](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=463s): Yeah, to continue on that we did the devnet #10 in sort of two phases. So the first phase was roughly 24 hours. So we had the Dencun Fork running we targeted a stable blob production. So roughly three we weren't spamming the network to any crazy number. We had arm machines as well this time around. And we basically just wanted to see how the network behaves if there's nothing chaotic going on. There was no blobber there was no bad block. It was just blobs as you would expect in a regular Network. You can see that as the baseline analysis and things look to be really good we do see some spikes here and there and put potential places for optimization. Most of the charts in the analysis are aggregated across clients but I've also linked all the dashboards. And there's often a filter on the top where you can choose your own client. So if client teams want to dig a bit deeper into how their particular client performs. And if they notice something that's more of a client specific issue. I would suggest hunting those grafana dashboards if you don't have access to them please reach out. and we'll create an account for you. The most important ones I think are the block and blob analysis, so that kind of correlates how many blobs exist in a block. and when things are being propagated. As a TLDR this was just a baseline towards the end you can see blob performance of a client pair. And just say every client is including blob so fundamentally we're good. What we tended was last evening we started the blobber as well as spamming blobs to a much higher degree also just a side point throughout the entire Baseline analysis we had TX fuz running that means there was transaction load. You can see very often 100 plus transactions in the network. So last evening we started the blobber so we're targeting more 9:53six blobs all the time. Of course that's impossible to always hit six blocks but we're trying as often as possible. You can see there are some outliers in CPU or RAM usage but in general things still look quite Good. We don't notice anything specifically different on our machines which is also a great sign. Network use did indeed go up and we're seeing extremely spiky Behavior which is also probably the point that Peter mentioned I think at the last ACDE or the call before where there's is really burst use of the network which we're yet to completely debug why but yeah once in a while you do see extreme bursts. As a result of the blobber we seem to have knocked out at least the prysm node, one prysm node potentially more. But Terence has already posted a message on interrupt saying they've identified the issue and they're patching it. Besides that there was a nimbus note that was also knocked offline but it seems to have healed before we got to it. So that's a good sign. We're seeing an increase in the depth of the reorgs which is not a great sign and we're yet to debug if that's a result of the blobber or if that's a result of something else. In general blobs on average are still being included at a great rate but the extremes have widened. I would recommend looking at the heat map for that analysis. And besides that, yeah, I think besides that we're still seeing stuff within tolerances. It's just the trend that we're seeing very often is that everything is happening as we're expecting. It's just our tolerances are limit are being reduced. And there is a note that the depth of the reorgs seem to be for some reason higher on teku nodes than the other ones. So maybe someone from the teku team can also look at into that. And just one last Point regarding MEV. We got the MEV workflow working completely. There are blobs being included. We only tested this with loadstar nodes. So the MEV analysis you would only see loadstar nodes for now. We're rolling out MEV on all other nodes but the fact that we're seeing blobs included indicates that MEV workflow probably works fine. Now and yeah I think there's some followup analysis from G11 Tech and from Enrico from the Teku team. So I'll also maybe ask if they want to say something about that.

**Tim Beiko** [12:40](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=760s): Yeah amazing work Pari and Barnabas. And thanks so much for putting these docs together. It's really helpful to have it on one place. Yeah and Enrico Gajinder either of you want to chime in with your analysis. 

## CL block/blob receive time data

**Enrico** [13:00](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=780s): Yeah I can share what I gather two days ago and actually yesterday. And I updated also what the data from our from three nounce to this morning. So I can share maybe my screen. So I can give you. So I'm sharing here what the aggregated view of the data I gather. So I gather this data from only three teku nodes because I'm using debug logs that we produce specifically for blocks timing and blobs timing. So what we are seeing here is that we have this graph with the timing at which we first see something related to a particular block route that could be the block itself or one blob that we saw and on top of it. We have the computation time which is the amount of time that passes after we see the first block route to complete the whole set of blobs and block. And this is taking in account the validation so this is post gossip validation. So what is interesting here maybe this is the relationship between zero and the six. So as you can see we got a pretty Trend going up. And most importantly we have this percentile table that says. So the mean here is the graph represents the mean. So it's you see in the .5 percentile and matches accordingly but I'm also reporting some higher percentile and we can see that roughly at 09 we can and get around three to 200 millisecond or kind of each blob added to the block. So up to having pretty high a wide timing around 1 second compared to yeah maybe five millisecond in when blobs are. 

**Danny** [16:12](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=972s): So there's not a like this is generally in line with the data we saw with loadstar right. So not like a big surprise we just com seeing data.

**Enrico** [16:21](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=981s): Yeah it's just confirming that this trend is very similar what has been reported by loadstar. So removing the constant timing of the validation that maybe loadstar is not reporting but the trend is very similar yeah.

**Danny** [16:40](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1000s): And these absolute numbers are fine and safe and it's which attempt or which method you try to use to then extrapolate these numbers to mainnet where you may or may not have concern.

**Enrico** [16:55](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1015s): Yeah that's the real deal here. So we got this baseline that presents our testnet here. And then how we translate this to an hypothetical a mainnet Behavior this is where interpretation and ideas may vary. Definitely.

**Dankrad Feist** [17:18](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1038s): I don't think you can unless, like at the very least, I think you would need to send non-empty blocks on the testnet to get to understand what the actual Baseline is. Because I think you cannot get this comparison if you just compare to empty blocks like that's not what mainnet does. 

**Tim Beiko** [17:40](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1060s): And were these blocks empty or were was this taken from devnet #10 where we had the transaction fuzzer on.

**Enrico** [17:49](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1069s): Yeah this data is taken up to this morning so and is taken from deneb activation. So the first blocks that are empty is just because I think the blobs were blobs transaction were not yet produced and after a while blobs has been starting to to come in and you start getting these blobs also with different numbers. So and I don't know when these blocks were were starting being full and I can definitely filter out and starting gathering this data from a particular slot could be maybe interesting to remove the zero blobs zero blocks that are also empty.

**Dankrad Feist** [18:45](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1125s): Yeah because I think like that makes a big difference like like in real life blocks aren't propagated that fast because they are like more than a few kilobytes big. So this pushes just our baseline down arbitrarily.

**Enrico** [19:03](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1143s): I'll chat with Pari to set the a reasonable slot to start printing this graph and I can update you afterwards.

**Dankrad Feist** [19:18](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1158s): Right that would be interesting.

**Gajinder** [19:19](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1159s): As per Pari's input the blocks aren't empty so they should be full.

**Enrico** [19:26](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1166s): From the beginning? Then activation?

**Paritosh** [19:29](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1169s): No definitely not from the Deneb activation. I think it's a couple of hours after because first we want to validate that the 4.1.

**Gajinder** [19:40](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1180s):  So but I mean that still would be only very small data compared of empty blocks compared to the entire data set that you have used I think.

**Enrico** [19:52](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1192s): Yes it's just a couple of hours. Maybe those numbers will not move that much unless all the zero blobs block are always empty.

**Gajinder** [20:09](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1209s):  Yeah I think it would be nice to see what is the actual propagation of the full actual propagation slash latancy data of the full mainnet block. Because full block which is similar to a mainnet block because loadstar on my mainnet node. I saw that you know it takes around 3.5 seconds for 95 percentile of blocks to show up. So yeah we need to figure out and also on the mainnet there is an additional factor of MEV blocks whose proposals might be delayed anyway. Because of the communication between the Builder and the validator. And so yeah maybe even on the mainnet blocks. I might need to filter out for the blocks which might not be MEV based to do an actual analysis. But even if that is the case then our major concern will be to figure out how to resolve the MEV flow. So that we don't have an extra latency added over there. So all all the entire concern is that whatever is this the latency diff it shouldn't have an additive effect on the blocks. And if it does have a additive effect on the blocks for example loadstar would need to optimistically import the blog in the sense that we need to optimistically run validations even before all blobs show up. Which we don't do as of now but seems like Lighthouse does it. And it's definitely seems like a good strategy. So we might try to. 

**Dankrad Feist** [21:43](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1303s): Right we are not currently running the execution client when you haven't received all the blobs?

**Gajinder** [21:50](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1310s): Yeah loadstar is not doing that but seems like Lighthouse is doing sure whether other CL’s are doing it or not.

**Enrico** [21:57](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1317s): Yeah teku is doing that so when we see the block. We all already start doing the block import process or the state transition and also contacting the EL for doing the the new payload API while dealing with blob dealing with blobs side cars and also doing some partial KZG validation if we in the meantime we received subset of the blobs that we expect and we only do the final import while once once all the blobs have been received. So there is a level of parallelism in Teku up to three different streams while is the state transition EL importing and KZG from blobs.

**Gajinder** [22:54](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1374s): Yeah Loadstar will sort of need to improvise this flow and come to what you guys are doing. So that you know we don't see an additive effect. If there is an additive effect of Blob Latency on mainnet. 

**Dankrad Feist** [23:10](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1390s): I mean there will be an effect right because it just consumes more bandwidth. And there will be an effect because you now need to receive all these things. And if one is delayed it's just slower but yeah the question is how big that effect should be and I think that's just much more complicated to know.

**Danny** [23:29](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1409s): Right and extra try to extrapolate.

**Gajinder** [23:32](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1412s): Even in the current data we see an additive effect even when for example the bandwidth is perfect we should. If for example everything was parallel then as we all the numbers of blob is equal to zero and blob is equal to six they should basically align or maybe blob is equal to one and blob.

**Danny** [23:49](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1429s): No I don't agree with that because yeah depending on the message you're going to sit somewhere different in the relative mesh. So you might be one hop on message zero and you might be four hops to get message five because they're following different paths in the mesh. So like by virtue of that by having more messages you just you have a higher chance of being a longer hop distance on one of those messages than than other so. 

**Gajinder** [24:20](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1460s): But would the high translate into 2x delay which is what we are seeing well.

**Danny** [24:25](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1465s): It's not delay it's 2x to get the last message

**Enrico** [24:30](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1470s):  Yeah.

**Danny** [24:31](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1471s): Rather than to get

**Dankrad Feist** [24:42](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1482s): Yeah right and then also this is assuming infinite bandwidth which is also not true.

**Enrico** [24:55](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1495s): I mean the as you think that things are not going in parallel but taking my My Graph in mind since the first scene is also going up in time is actually a proof that things are actually sent in parallel because even even the first blocks or blobs that we receive if in case of six blobs. We are getting a delay there so it's definitely the bandwidth that is kind of split between blobs and blocks. So the first message that is completely sent to the pier is getting more time because bandwidth is use it more.

**Gajinder** [25:44](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1544s): Actually on devnet #10 the bandwidth is not an issue because 1 gbps symmetric upload download is there. And so what the analysis it might mean that actually things are not being started in parallel and also for example Pawan mentioned that lighthouse first transmit the block and then transmit the blobs. And I'm not sure whether it's also transmitting the blobs in parallel. So I think we all the CL
client should go and see whether there is parallelism in terms of the data transmission.

**Pawan** [26:22](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1582s): Yeah this is something that we are exploring that I'm exploring on Lighthouse if it's doable on P2P. I'm not the P2P experts I've been looking into the code and seeing if just calling publish on blocks and blobs in multiple threads would that gain like would that result in a concurrent publish over lip P2P as well. So I'm checking that out and like I'll should probably have results sometime by tomorrow but it might take time because I'm not the P2P expert.

**Enrico** [26:56](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1616s): If it was if it was completely sequenced from all client I would not expect the first scene to move. For me the first scene should be completely constant.

**Gajinder** [27:08](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1628s): Correct first be Constant because there is no bandwidth issue involved and for as far as loadstar is concerned there is some serialization that is happening till the point of all the block and blob data being converted into bytes and handed over to the network layer. So there is a serialization factor for example which loadstar like engines can't do away with because we have only one main thread running. 

**Enrico** [27:32](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1652s): So you mean before even start sending anything you you you serialize everything and then you start. So this is adding something that is function of the number of things that you have to send even if you send.

**Gajinder** [27:44](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1664s): Yeah so that is because of the underlying node concurrency model in which basically Asing task start after the current whatever it can execute in serial and then basically you know the hand.

**Enrico** [27:59](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1679s): That's clear so I think every client should double check the parallel level of parallelism in Gossip sending out.

**Tim Beiko** [28:31](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1711s): Yeah I don't know that there's a specific like that we have enough data here to come to a conclusion. But what the people feel is the right Next Step. So there's some comments in the chat about potentially running this on more nodes. Potentially comparing it to large call data blocks. And it might be worth also like running this on a testnet and seeing in an environment where there are transactions in blocks by default and there's like a larger distribution of nodes. yeah I don't know how the people feel without next steps here. 

**Gajinder** [29:21](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1761s): I think we will definitely need to test it on a real test net and then only you know make some conclusions about it because having it in a data center will not get us near to the real deployment conditions that might exist for mainnet. 

**Paritosh** [29:38](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1778s): Definitely agree with that one also the setup we use typically doesn't have web 3 signer. It doesn't have stuff like vouch we don't use any custom things. We're just basically running native clients and that's typically not how mainnet is
Run.  

**Potuz** [30:03](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1803s): So one worry about like going to testnets. I mean certainly this has to be tested and and there's a danger that we might need to go to bundling blobs with blocks. But one thing that worries me is that we have only so many testnets to fork and we are seeing very very serious bugs still on clients. Prysm has had terrible bugs and every client has forked one way or another on their own Fork. So I would want to wait a little bit before we test before testnets until the clients are a little more stable.

**Tim Beiko** [30:38](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1838s): Got it yeah and so I guess yeah. So we basically have three testnets right. Like we have goerli which is deprecated and this will be the last Fork we have on it then we have sepolia and holeskey. So yeah we want to make sure for sure that by the last one things that are going live or effectively what's going to go on mainnet. But yeah how do people feel about stability in general at this point. Terence?

**Terence** [31:09](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1869s): Besides the ability there are still things that like we haven't tested such as the MEV Builder and the relay and Client   and that is arguably probably the biggest and most important part because like 90% of the mainnet client uses MEV boost. So I think we probably will need to spend some more time testing it. I know we started on loadstar but yeah be spend some more time testing it before moving to Testnet. 

**Paritosh** [31:39](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1899s): I think the only counter point I have to that one is at least in all the previous Fox we we only tested the circuit breaker before we agreed on Mainnet. And we still have like a couple of weeks to test out MEV workflows even before goerli. For example if we were to agree on it.

**Tim Beiko** [32:08](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1928s): Yeah I'm curious how do other clients feel about this.

**Sean** [32:19](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1939s): I'd be interested in seeing liking on a bigger testnet and yes we'll continue to use devnet #9 until we get another testnet up and running. Because there's still things I think we can figure out and if we can like for example optimize our upload a bit. We could see if Enrico's numbers change on devnet 10. So yeah.

**Tim Beiko** [32:50](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1970s): So when you say sorry you said see another testnet but do you mean you want to move to something like Goerli or you want to see another devnet like devnet 10 or devnet
11.

**Sean** [33:02](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1982s): Yeah I was thinking Goeli okay honestly and we would continue to use devnet #10 until that was running.

**Tim Beiko** [33:09](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1989s): Got it.

**Barnabas Busa** [33:11](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=1991s): We were actually thinking about shutting down devnet #10 by Monday. So maybe we can have like devnet 11 with smaller number of validators just for running it for a longer period of time but not really for stress testing because running these 100 nodes is pretty expensive. 

**Sean** [33:34](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2014s):Okay yeah that works as long as we have something because we're still like digging into logs and like understanding how this works.

**Barnabas Busa** [33:48](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2028s): Yeah we can definitely launch something maybe even bigger than devnet #9 for devnet #11. And then we could have that until the point that we would fork early.

**Sean** [34:01](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2041s): Okay that sounds good.

**Tim Beiko** [34:10](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2050s): Any other client teams have thoughts on what they like to do for testing. I guess yeah so if all for all the like eight other teams the people feel I guess like they agree that they need
more time before running to like a first testnet or are people more comfortable and potentially ready to move forward with Goerli sooner. Yeah I think I'll just call on the team I don't know guest. How do you all feel about yeah just overall
readiness ? 

**Lightclient** [35:31](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2131s): I mean I think I've set this for a little while like we are in a pretty good place a lot of things are also on Master now. And yeah I mean on the EL side this is not really where I think the big decisions are being made so I don't really feel like it's my place to say. Let's go forward but yes from gut I think we're okay.

**Marek** [35:56](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2156s): More or less the same situation on nethermind side I think we are quite comfortable but I think it's not on execution side.

**Andrew** [36:13](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2173s): Yeah for Erigon it's the same we are comfortable with going with the fork on Goerli but we can wait as well if there is need to wait more.

**Justin** [36:28](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2188s): Okay yeah same at Besu we're comfortable with it not in a rush to move forward.

**Tim Beiko** [36:36](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2196s): Got it okay so and I think okay. So clearly on the CL then looking at the MEV Pipeline and and a bunch of other smaller like client specific issues are the two things so yeah maybe it makes sense to decide the next steps on this CL call next week. And I guess until then if we are launching a new devnets then the main thing we should be doing is making sure that all the clients are all the clients are set up with the MEV pipeline. Is there anything else that we want to make sure we do on the next devnet. I see a lot of Thumbs Up and comments around Shadowforks as well. Yeah so if it either if I don't know if devops forks yeah want to give an update on Shadowforks.

**Paritosh** [37:45](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2265s): Yeah we can do Shadowforks that's absolutely no problem for ourside.  We just need to discuss which network it would be. Yeah goerli just has a big state so that would be the most expensive and I guess either holesky or sepolia would be the cheapest.

**Potuz** [38:09](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2289s): Yeah so for shadowforks I wonder if there already rollups that are actually testing on 4844. I mean as soon as we have a deployment of actual clients that that are sending blob transactions at a more or less realistic Pace like a natural roll up batch posting. Then it would be nice to have those testnets. 

**Paritosh** [38:36](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2316s): I mean once we do I think at least optimism is using goerli if I'm not wrong. So I guess if we do a goerli Shadowforks, then we can also ask them if they can point some load at us. 

**Tim Beiko** [38:54](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2334s): Okay and there's a comment in the chat saying there's an OP stack rollup briefly that briefly ran on devnet #9. So we could likely get that either on devnet 11 or on a shadowfork. Yeah whatever the simplest there. Okay so yeah devnet 11. So basically getting the MVE pipeline set up with all the clients getting a rollup implementation running and then obviously every client sort of fixing the the issues they have with their own implementations. Is there anything else we want to see out of devet 11 before moving to Goerli.

**Gajinder** [39:52](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2392s): Loadstar so I'll add importing the block and running validations even before all the blobs show up so that is might to do. 

**Tim Beiko** [40:01](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2401s): Got it okay and is it realistic to get this done in like the next week or so such that like either we such that like by by next CL call on Thursday. We have a like understanding of how all
those things went.

**Paritosh** [40:34](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2434s): Yes so we can plan for just sort of summarizing on the schedule we'd want to get rid of Dvenet 9 because it's using the old KZG setup. And I guess at this point all the tooling has moved on and everyone's using different Forks so we'd like to turn that off  devnet #10 can stay up as long as you you guys decide. I think we were default into shutting it off on Monday. After we collect all the data that we need we'll start devnet 11 which would just be a longer running small scale Devnet. So if anyone wants to actually test out tooling Etc they can expect it to last for a while. And we can do a goeirli Shadowfork we plan for that early next week. So that by CL call we'll have some more data. Does that sound okay?

**Tim Beiko** [41:28](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2488s): Yeah does anyone disagree with that?

**Paritosh** [41:38](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2498s): And is there any sort of request on the sides of the goerli Shadowfork yeah and we'd probably want to keep the this yeah it depends we're going to have to see how long we're still going to keep accepting goerli traffic because in the past I think we had like roughly 3 days worth where we stayed peered to the canonical chain before it no longer Mattered. But yeah I guess we can just do a midsize network. It would teach us more about the processing time but I doubt it will teach us much about the networking. And the alternative is doing something at the scale of Devnet #10 just as a shadowfork.

**Tim Beiko** [42:35](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2555s): Okay I yeah I think that makes sense Barnabas has a chat comment about can we choose a Goerli date now and he was asking for November 9th.

**Barnabas Busa** [42:53](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2573s): Next week we can postpone it if it's really rushed.

**Tim Beiko** [42:56](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2576s): Yeah and I guess that yeah to give context so I think generally what we try to do with testnet Forks is have the
blog post out at least a week before the fork happens. So the blog post means all the clients have a release that's like people can go and download that's fairly well packaged.So like if we want to for Goerli on the 9th it means basically mid next week. We would need the client releases out with all the clients. Does that feel realistic to people. And we basically by the time it by the time the CL call happens next week. We would be a week away from the fork. So it would be kind of the latest absolute latest we could postpone.

**Andrew** [44:01](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2641s): It's fine for Erigon.

**Tim Beiko** [44:07](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2647s): How about on the CL side because that seemed to be where there was most concerns about timelines.

**Potuz** [44:22](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2662s): I'm speaking for myself but I would say that prysm is not ready to fork.

**Tim Beiko** [44:28](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2668s): Got it yeah and I guess the alternative basically if we do the same thing a week from now it's like instead of the 9th then you're talking about something like the 15th or whatever on goerli at the earliest give or take yeah.

**Potuz** [44:49](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2689s): So again speaking for myself not representative of the Tim. But I see very large and deep changes still being pushed in the branch. We are storing blobs on DB directly there's no gash for blobs. We are moving that to file storage these things are like deep changes these are not just on liners I don't see how this is going to change in a week or so. 

**Tim Beiko** [45:14](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2714s): Got it and what do you have a feeling for like the order like the time for just larger changes to stay like be done and the overall code base for prysm to stabilize.

**Potuz** [45:31](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2731s): I do expect this to be of the order of weeks, certainly not months but one or two weeks.

**Tim Beiko** [45:37](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2737s): Yeah got it any other teams have thoughts concerns about this. Okay and yeah there's a comment so saying that we probably shouldn't Fork if devconnect is going on. So this means it's unlikely if we don't do like the 9th which seems pretty early for teams then it means we probably have the fork happen like in the week or so after devconnect at the earliest. And so that means basically devconnect is having Goerli around somewhere between I don't know around November 22nd. I don't know if that shorts to be. And then okay so Ansgar has a question if we Fork after devconnect do we have a shot of shipping this by the end of the year I mean historically. I think the closest we forked testnets apart has been like two weeks or so like Devconnect if we Fork after devconnect that's November 22nd two weeks after that is November 6 two week after that is December 20th so we can probably get all three testnets done before Christmas but it seems unlikely you can also shove mainnet into that especially if we want to see especially. If we want to see things on testnets for you know more than a week. I think if you really wanted to like push everything in 2023 and you're forking the first testnet after Devconnect you'd have to have something like a week between each different testnets which probably means that the same client releases are for different testnets. So that seems hard given it doesn't give you the opportunity to like fix any issues that you do see on testnets between one and the next. And yeah there's a lot of chat going on. I don't know if anyone else wants to chime in on the call directly. Okay I guess yeah, let's see how things involve in the next week and talk about it on the CL call next week but I think clearly we won't be forking Goerli on November 9th. And then yeah if we're also not going to be forking the week after that because of devconnect then it means we will be doing it towards the end of November at the earliest. And that also will give more time for client code bases to stabilize. So, any other comments concerns thoughts around Denon testing and Fork schedule. 


## KZG Ceremony verification

Okay if not Carl you had an update on the KZG ceremony.

**Carl Beekhuizen** [49:45](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=2985s): Yep so as you all know we're now using the final output from the KZG ceremony which is great. But a very important component as that is for everyone to verify the contributions. So if you participated in the past and you know you participated but your output's not in the final ceremony then something clearly went wrong. And we have ways of proving that but this is not something we seeing but it's important to check those. So there are two easy ways for you to do this one is the same website that most people use to contribute http://ceremony.ethereum.org. You should just be able to go there you can paste in your credentials use to contribute. And that should allow you to verify the ceremony and claim a pop. Then there's a second alternative method which is a rust script for doing the same verification. It performs slightly more in-depth checks and is a little bit easier to obviously order that the code that you see is being run. So if you really want to go in depth I'd recommend doing that. So please everyone verify the ceremony.

**Tim Beiko** [50:54](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=3054s): Thank you. Oh and as a heads up you need to be on desktop to do this a bunch of people have ask this question. So yeah thanks Carl. oh and I guess yeah you had another so we were going to talk about next steps for dencun after but I think that's that's pretty clear. We sort of went over that but you had another item Carl you want to give an overview about the RollCall. 

## RollCall overview

**Carl Beekhuizen** [51:25](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=3085s): Yes sure so RollCall is something that myself Ansgar and Y have been working on. The idea is it's a neutral platform for coordination between a bunch of the rollups and L2s. So there's a process that much like we have EIP’s and ERC's. The new addition here would be RIPs which is basically changes specific to Layer 2s. And this ideally allows them to have a little bit more standardization between them. There are many things that they've implemented which are slightly incompatible with one another. So hopefully we can bring everyone on the same page. And possibly even make some slight changes to the EVM if they if people particularly want but at least try to do it in a standardized way that everyone can see and work on. And then the second thing is the idea is to have it be an API between well like metaphorical API between L1 and L2. So obviously there's lots of things happening in the L2s where it's people bring up points that they're interested in but it's not obvious that whether this is just like one particular team that's interested in something or whether this is something that' be helpful for the whole ecosystem. So  helping L1 and all our governance processes to see have a bit more insight into what the needs are from the L2 side of things. And then also from the reverse side of things is to help L2 see when things are needed from them. So great example of that is what we talk about testing on devnets by posting data blob data so I'll go back and I'll bring this back to them the mini L2s. And see if we can get some of them some more of them to test. So the idea is just to help these processes become slightly easier to participate in everyone here is of course welcome that's not supposed to be exclusionary or whatever just help separate concerns so if you want to participate jump there's a RollCall call which happens monthly. And you should be able to see that coming up in the PM's channel the PM's repo much like ACDE and ACDC and also there's the Layer 2 channel in the Ethereum Discord has been renamed to RollCall for participation if anyone wants.

**Tim Beiko** [53:59](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=3239s): Thank you any questions. oh yeah please.

**Andrew** [54:05](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=3245s): Sorry I didn't want to jump in but I just want to mention we also have an in-person event doing Devconnect. So if you're in town and you have some free time on that's the
Wednesday. I'll put the the link (https://ethereum-magiacians.org/t/rollcall-1-in-person-at-devconnect-istanbul/16220/1) in the chat and there might be some topics you can have a look in if there's some topics that you think you might be interested in. Maybe joining the conversation yeah reach out to us and that would be great to have some L one people involved as well.

## EIP-7523

**Tim Beiko** [54:41](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=3281s): Awesome yeah thanks a lot. Okay the last thing we had today Danno wanted to bring up EIP-7523 which is is about prohibiting empty accounts on post-merge networks. I don't know Danno or Peter if either of you are on the call to give some context.

**Danno Ferrin** [55:08](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=3308s): I'm on the call I don't know if Peter is. So I'll quick summary of this EIP so the scope really is mostly going toward some of the test data in the reference tests and formalizing some some behaviors for clients that meet the standards but what EIP 7523 says is that if you're either the mainnet chain after the merge hash or if you are on a chain that has the Genesis post Spurious dragon and has no empty Accounts at Genesis then if you follow the rules of the specification then empty accounts will never be persisted between blocks. So based on that clients can make assumptions that they'll never see empty blocks. And the whole swath of corner case that interrupt as to what he you what he do with an empty block. If you do a revert when you touch an empty not empty block empty account if you do a
revert when you touch an empty account if you touch an empty account you delete it from the state that whole bit of logic that was put in after the Shanghai attack no longer applies. And this it does have impact on some some client design if you're writing some some State systems. And EVM that can behave more efficiently if they don't have to care about empty accounts and they can run quicker if this you know this EIP is presumed. So I guess the temperature check here is what do people think about clients having modes where they're only working post Spurious dragon with no empty accounts. And if that's favorable what would be the  how they would feel about updating all the reference test cases that are post for Dragon to not have empty accounts and not test for empty accounts but only to test in the Legacy test cases so those are the two questions I want to get before I push this any further elsewhere to make sure that this is something that the rest of allore devs is cool with not everyone at once.

**Dankrad Feist** [57:18](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=3438s): I think I didn't get the full context but are you aware that with verkle trees at least at the moment there will be a difference between things like positions in the state that have never been written to versus position in the state that have just been overwritten with zeros. I just want to make sure this is not creating a conflict with that.

**Danno Ferrin** [57:48](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=3468s): So if you're following the EVM specs right now in producing it accounts would only get over with zeros if selfdestruct happened. And since we're deprecating that and possibly removing it you know. I guess there was one question about doing it within the transaction writing it out. And I think we settled on it wouldn't get persisted to dis if it was a transient storage option. If it never actually hit the disc so that is one corner case but just the general premise is that you would never write an empty account in normal operation. If things are operating correctly aside from self construct in the band mode.

**Dankrad Feist** [58:34](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=3514s): Okay I'm not I'm not still not sure. I understand fully what your change means I just wanted to make sure that the new state fracture with local Tri would be taken into account.

**Danno Ferrin** [58:44](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=3524s): Right it shouldn't impact it I mean zero zeros on States will still be written. I mean that changes nothing about writing a state it only has to do with at the end of execution. If you find you have an empty account or if you start with an empty account how you would handle it differently than if you end with an empty account. So as long as there's no empty accounts in the system then following the rules of EVM ensures that aside from self-construct you won't be writing empty accounts to dis. And as far as pulling it off a dis I think that's fairly you know maybe we need to drill into this with this the verkle account. But I don't see how you know it would affect anything different because the real issue comes in there's one corner case where if you read an account that's empty. You do a transaction that touches it which would then Mark it for deletion from the system. and then you revert that block and then the the touch is undone and the deletion never happens. That's the real Corner case . That this is getting rid of. So you know that I think that is you know separate from what's writing to this it's almost entirely within the EVMs to make the assumptions. And the real impact here is I want to go into the test code. And there's a few test that still put empty accounts into post merge test cases and get those updated. 

**Tim Beiko** [1:00:05](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=3605s): So I guess on one hand it's worth taking some time to just silently check the verkle and self-destruct compatibility issues but assuming we did this when, what, how, do we reflect this in like the chain activation history. So we have eips now that like we've retroactively activated since Genesis this wouldn't work in this case because of spurious dragon. So would we say this EIP was like activated as part of like the Paris Fork retroactively in a way or something like that? 

**Danno Ferrin** [1:00:41](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=3641s): So it's written into the specification there's two cases that matches the second is any chain which has no empty accounts in his posterous work. And the first one is the mainnet chain whose merge block has the hash which is the merge hash so it's written into the spec that the effect of this activates it the merge right now.

**Tim Beiko** [1:01:00](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=3660s): Okay so yeah we can figure out how to represent that and the reason why I ask about this is like somebody who's writing your client from scratch you know do we want this to show up as part of the merge EIP’s. So that they can know when they they've get to that point like. Okay I can assume there's no longer empty accounts or is there a better spot for it to show up but.

**Danno Ferrin** [1:01:28](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=3688s): Right and I think that's exactly the question that we need to have yeah what is the appetite for writing accounts that can't do the full history of ethereum that only start at the merge or only start with a certain point with a certain set of data from a fork. Do we need to keep all historical ways to generate blocks in future clients or even current clients and that's a separate Pandora box to open that. I don't think we have nearly enough time to talk about.

**Tim Beiko** [1:01:53](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=3713s): So I guess where's the best way for people to discuss it should we just use the eth magicians thread of of this EIP. 

**Danno Ferrin** [1:01:59](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=3719s): There is an ETH magicians thread. Yes I think that's the best place to drop your issues.

**Tim Beiko** [1:02:04](https://www.youtube.com/watch?v=P_a3s6zNFEk&t=3724s):  Okay any other comments questions concerns about this. Okay yeah thanks a lot Danno. So people can use this Eth magician thread. That was the last thing we had on the actual agenda is there anything else anyone wanted to discuss before we wrap Up. Okay well if not we can close out here. Thanks everyone for coming on. And I'll see pretty much all of you on the testing call next Monday. Yeah, talk to you soon.

# Attendees

* Carl Beekhuizen
* Tim Beiko
* Guillaume
* Paritosh
* Joey Santoro
* Roman Krasiuk
* Jochem
* Ben Edgington
* Marek
* Mikhail Kalinin
* Gary Schulte
* Karim T.
* Barnabas Busa
* Danno Ferrin
* Majntainer.Eth
* Pooja Ranjan
* Justin Florentine
* Terence
* Fabio Di Fabio
* Justin Traglia
* Mehdi Aouadi
* la Donna Higgins
* Damian
* Peter Garamvolgyl
* Stefan Bratanov
* Ameziane Hamlat
* Piotr
* Light client
* Enrico Del Fante
* Stokes
* Sean
* Josh
* Marcin Sobczak
* Phil Ngo
* Mario Vega
* Andrew Ashikhmin
* Ansgar Dietrichs
* Gajinder

### Next meeting [ 2nd November, 14:00-15:30 UTC]
