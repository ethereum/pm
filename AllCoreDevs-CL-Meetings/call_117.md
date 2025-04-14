# Consensus Layer Meeting #117 <!-- omit in toc -->
### Meeting Date/Time: September 7, 2023  at 14:00 UTC <!-- omit in toc -->
### Meeting Duration: 1.5 Hours  <!-- omit in toc -->
### [GitHub Agenda](https://github.com/ethereum/pm/issues/854)  <!-- omit in toc -->
### [Audio Video of the Meeting](https://www.youtube.com/watch?v=zODMnGxQBG0 )  <!-- omit in toc --> 
### Moderator: Danny <!-- omit in toc -->
### Notes: Avishek Kumar <!-- omit in toc -->
-----------------------------

**Danny** [7:18](https://www.youtube.com/watch?v=zODMnGxQBG0&t=438s):  Okay, welcome to the Consensus Layer Call #117. This is issue #845 in the PM repo. Focus today, obviously but no today will be continued on deneb. We'll talk about testnets. I do want to bring up the testing plan that was brought up a couple weeks ago and make sure that we've put some eyes on it and that we know who's gonna be working on the the CL / P2P specific stuff. So that's kind of a high urgency concern problem for a lot of teams. Then we have promised to revisit the 4844 mainnet parametrization. So codex is here, they've been looking at some big mainnet blocks. So we can dig into that and then if there's any other inputs or thoughts on the 2436 parameterization  we can discuss. I have attempt to form consensus on mainnet parameters. I actually don't know what the temperature gauge is going to be here. So I don't know if that's something we can do today or something we can open the conversation for in the future. And then Ethan has a stable container proposal which is I think an update to EIP#7495 that we can take a look at. Let's get started! So now dencun devnets are there any progress or discussion points worth bringing up today on our public call.

## Devnets progress

**Barnabas Busa** [8:58](https://www.youtube.com/watch?v=zODMnGxQBG0&t=538s): Everything is perfect. We have 100% proposals and all the notes are up to the head. And I've just deposited some more validators for Aragon. So we're going to be able to check if Aragon is also able to make block of calls. And we have indeed all the clients.


**Danny** [9:22](https://www.youtube.com/watch?v=zODMnGxQBG0&t=562s): Very exciting.

**Marius** [9:26](https://www.youtube.com/watch?v=zODMnGxQBG0&t=566s): Wasn't there some clients that had some issues that kind of like fix themselves at some point?


**Barnabas Busa** [9:34](https://www.youtube.com/watch?v=zODMnGxQBG0&t=574s): Yeah! But everything has been fixed as of last night or this morning.


**Marius** [9:41](https://www.youtube.com/watch?v=zODMnGxQBG0&t=s): Like do you know like why they didn't want to sink in the first place. 


**Barnabas Busa** [9:51](https://www.youtube.com/watch?v=zODMnGxQBG0&t=591s): Is anyone from from prison here maybe?

**Terence** [9:56](https://www.youtube.com/watch?v=zODMnGxQBG0&t=596s): Yeah! I'm going to share some likes to learn. So why we did not see this issue before. So we found a bunch of issues with regard to saving the block size after the retention window. So it's funny I'm happy we're just to test this for more than 18 days. So basically the saving of the block size card gets really messed up in the index after the retention window. So the blocks are getting overwritten or deleted. So, that's why we're having trouble syncing so that's a crazy issue. The second issue is that we were using the wrong blob stop console removable from 426 but we did not update the parameter that's the blob subnet. So we're subscribing the four subnets this whole time. So we also fixed that. And then the last issue is that we were finally incorrectly hashing of the block’s that's inside the block size card field know. So we were hashing a block without the stay route before putting the stable in the block. So basically all our size card had to run blocked route inside.  So yeah created testing I'm glad we figured out most of those issues within 24 hours.

**Danny** [11:16](https://www.youtube.com/watch?v=zODMnGxQBG0&t=676s): Yes. Any other other updates or comments related to devnet 8. Are we transaction
spamming real quick and blogspam I assume so.

**Barnabas Busa** [11:36](https://www.youtube.com/watch?v=zODMnGxQBG0&t=696s): Yes fuzzing just spamming for now.

**Danny** [11:39](https://www.youtube.com/watch?v=zODMnGxQBG0&t=699s): Gotcha! Sorry Justin going.

**Justin** [11:41](https://www.youtube.com/watch?v=zODMnGxQBG0&t=701s): Yeah! Real quick we're investigating a potential issue with basically proposing empty blocks but only with lighthouse which is weird. So Lighthouse folks expect me or someone from my team to reach out thanks.

**Sean** [11:58](https://www.youtube.com/watch?v=zODMnGxQBG0&t=718s): So Michael's actually been looking into this on our team. And I think he's gotten to the bottom of it. We just haven't merged the fix for it yet we were doing like multiple fork Choice updated. It's like too quickly in a row on proposal and one of them had the incorrect parent beacon block route 

**Justin** [12:19](https://www.youtube.com/watch?v=zODMnGxQBG0&t=739s): Awesome thank you.

**Danny** [12:27](https://www.youtube.com/watch?v=zODMnGxQBG0&t=747s): Other Devnet 8 discussion plan. Okay I believe where we left it at the previous call was not having a timeline for devnet 9. I got murmurs that was changing now does anybody want to discuss devnet 9.

**Barnabas Busa** [13:00](https://www.youtube.com/watch?v=zODMnGxQBG0&t=780s): Yeah! We said I think on the Monday call that Devnet 9 should launch on Tuesday, next week what's the plan?

**Danny** [13:10](https://www.youtube.com/watch?v=zODMnGxQBG0&t=790s): Okay. Cool yeah! Any other things to share or discuss around that while we're here.

**Mario Vega** [13:20](https://www.youtube.com/watch?v=zODMnGxQBG0&t=800s): I would like some more time to update the hive tests for the execution clients. I'm not sure if we're going to manage to update everything for Tuesday. So Is everybody ready or are all clients ready for tuesday.

**Justin** [13:51](https://www.youtube.com/watch?v=zODMnGxQBG0&t=831s): Face is ready.

**Paritosh** [13:53](https://www.youtube.com/watch?v=zODMnGxQBG0&t=833s): I think the only change is how we're deploying the transactions right.

**Mario Vega** [14:01](https://www.youtube.com/watch?v=zODMnGxQBG0&t=841s): Yeah but we are also including more tests on the transient storage. We are simply more tests on the beacon route contract and I'm including more tests on the hive engine API engine API simulator so.

**Danny** [14:19](https://www.youtube.com/watch?v=zODMnGxQBG0&t=859s): With all additional coverage right.

**Mario Vega** [14:21](https://www.youtube.com/watch?v=zODMnGxQBG0&t=861s): Yeah its an additional coverage.Yeah but it would be nice to have it before the launch. 

**Barnabas Busa** [14:39](https://www.youtube.com/watch?v=zODMnGxQBG0&t=879s): I guess after this but we're gonna be quite busy. So if we don't do it on Tuesday I think we will have to push it at least another whole week.

**Paritosh** [14:50](https://www.youtube.com/watch?v=zODMnGxQBG0&t=890s): I think so fine considering the only change is really the transaction and if we want to be more chaotic on devnet 8 we can be next week.

**Mario Vega** [14:59](https://www.youtube.com/watch?v=zODMnGxQBG0&t=899s): Yeah I agree okay so it's only extra coverage from high upside. So if we find anything even after the devnet9 has launched we can just report it then. I don't think we are going to find anything that breaks devnet 8. So it's okay.

**Danny** [15:17](https://www.youtube.com/watch?v=zODMnGxQBG0&t=917s): Pari, were you saying the opposite and saying we could wait a week and just Spam 8 more.

**Paritosh** [15:22](https://www.youtube.com/watch?v=zODMnGxQBG0&t=922s): Yeah I think I'd prefer just waiting a week and then having everything that Hive can catch get caught by Hive and then just focus on causing more chaos on devent 8 next week considering that devnet 9 is pretty much just devnet 8 but with one change.

**barnabas Busa** [15:42](https://www.youtube.com/watch?v=zODMnGxQBG0&t=942s): And builders hopefully.

**Paritosh** [15:45](https://www.youtube.com/watch?v=zODMnGxQBG0&t=945s): Yeah but they haven't necessarily been working on local testnets yet so another week for Builders doesn't seem too bad either.

**Danny** [15:57](https://www.youtube.com/watch?v=zODMnGxQBG0&t=957s): That's the direction I would lean on lean in but I wasn't a part of the call on Monday that you know made a decision to keep it moving quick.
                                                       **Barnabas Busa** [16:11](https://www.youtube.com/watch?v=zODMnGxQBG0&t=971s): We still have one PR open 398 that have been checking on whether we could merge that is the transaction and receipts. Is there any holdback for this or can we just get it merged and you don't know it?

**Lightclient** [16:32](https://www.youtube.com/watch?v=zODMnGxQBG0&t=992s): I mean we didn't test for it.

**Tim Beiko** [16:38](https://www.youtube.com/watch?v=zODMnGxQBG0&t=998s): Hello there's a blocker to merging the PR?

**Lightclient** [16:44](https://www.youtube.com/watch?v=zODMnGxQBG0&t=1004s): Yeah!

**Danny** [16:57](https://www.youtube.com/watch?v=zODMnGxQBG0&t=1017s): This is in the ETH API not the engine API? 

**Lightclient** [17:01](https://www.youtube.com/watch?v=zODMnGxQBG0&t=1021s): Yes okay.

**Tim Beiko** [17:08](https://www.youtube.com/watch?v=zODMnGxQBG0&t=1028s): If the PF is listening this is an easy project with high immediate value.

**Danny** [17:19](https://www.youtube.com/watch?v=zODMnGxQBG0&t=1039s): Does anyone strongly opposed to devnet9 being at plus one week from Tuesday rather than Tuesday. We can hopefully merge this PR and get the hive test stuff we can do more Chaos on devnet 8 and something else in there but.

**Paritosh** [17:36](https://www.youtube.com/watch?v=zODMnGxQBG0&t=1056s): Just one more thing for devnet9 we'll be doing capella Genesis as far as I know
Barnabas has already tested and it was on our clients but just still wanted to mention that.

**Barnabas Busa**  [17:47](https://www.youtube.com/watch?v=zODMnGxQBG0&t=1067s): Yep I haven't tested direct just yet but I think you should do it because.

## CL P2P testing Review

**Danny** [17:57](https://www.youtube.com/watch?v=zODMnGxQBG0&t=1077s): Okay, Devnet 9 postponed plus one week from Tuesday. Sounds good. Cool anything else on devnets? Great! A couple weeks ago Pari and team shared this document just on testing overview there are some things in here related to CL testing. So probably things around Network partitions or long-running forks and resolving those in the context of being able to get blobs or not they're past a print depth. Delaying blobs delaying blocks and blobs like that kind of stuff I think a number and just maybe some sync tests in the context of blobs based on conversations with Consensus layer teams. You know those are some of the these like exceptional code paths related to the new P2P stuff around blobs are definitely some of the high priority concerns and items. But I just want to bring up the testing plan again and make this a couple weeks ago. We talked about this our our bases covered in terms of the tools and the people that are working on these things or do we need to make a more concerted effort in the next few weeks too tackle some of those items I just discussed.

**Paritosh** [19:41](https://www.youtube.com/watch?v=zODMnGxQBG0&t=1181s): Just give some updates on this one so sync testing it looks like the Nethermind team has been running some sync tests themselves I'll let them expand on that if someone from their nethermind is here, but you might have seen some results of that on the interrupt Channel. We still haven't gotten around to updating our own sync test Suite. So we're relying on the Nethermind team. For that chaos testing is still a work in progress we're hoping to get that done by the end of the month. We're kind of a bit held up because this protocol but soon and we're trying to get some things prepared before that and MEV related tests there was an issue with Mac boost not being able to handle Genesis and as far as I know since as of yesterday that's been fixed and they're actively getting ready to test on local devnets. And I still wanted to ask if CL side have had a chance to try it with mock MEV mode on curtosis because if that's working as well then devnet 9 we can already test the entire MEV workflow. But yeah besides that I will also we're having a call with Mario after this kind of if someone's interested feel free to join that one.

**Danny** [21:04](https://www.youtube.com/watch?v=zODMnGxQBG0&t=1264s): Great! And if anybody on Consensus Layer teams did have a chance to look at this testing plan since it was first introduced our our bases covered are there glaring omissions that we need to make sure to show up over the next handful of weeks.

**Sean** [21:34](https://www.youtube.com/watch?v=zODMnGxQBG0&t=1294s): Just like briefly looking at it now but do we want to deal with scenarios where the finalised checkpoint is further in the past than blob exploration and like how do we recover from that because that would require A 5.6 from like an unfinalized checkpoint I think.

**Danny** [21:56](https://www.youtube.com/watch?v=zODMnGxQBG0&t=1316s): Yes I guess there's two things there one is having a fork that goes beyond that depth. Well I guess there's a number of things you can have a fork that goes beyond the depth. And actually show that you can't you're not going to automatically resolve before because you can't do and Fork meaning partition because you could have done d a on the other Fork even if you weren't seeing it as your head and then there's the resolving from that from those problems. I think that it's probably worth throwing what we can at it. And these scenarios are pretty exceptional and worth testing do you think does like Lighthouse Etc, work from starting from a non-finalized checkpoint from a subjectivity or is that just not something that's been coded up before.

**Sean** [22:51](https://www.youtube.com/watch?v=zODMnGxQBG0&t=1371s): I think it does. It would be nice to test especially if it's like it would be a requirement to recover from a scenario like this so.

**Barnabas Busa** [23:06](https://www.youtube.com/watch?v=zODMnGxQBG0&t=1386s): Devnet 8 it's already 20 days old or 22 days also it should have some expired blobs. And it only has a single archive node that should have already update in there. So we should be able to do all these kind of tests under the date I think.

**Danny** [23:24](https://www.youtube.com/watch?v=zODMnGxQBG0&t=1404s): Yeah one of the things though is to make the network not finalized for the depth of the pruning period so on the order of weeks unless we change the parameterization of a Tesla.

**Paritosh** [23:38](https://www.youtube.com/watch?v=zODMnGxQBG0&t=1418s): Is there actually any objection to change that for devnet 9,  because we could do this test there and then keep the period as like 1D or something.

**Danny** [23:52](https://www.youtube.com/watch?v=zODMnGxQBG0&t=1432s): Yeah it's probably worthwhile having like a much shorter print depth because,
I think you can get a bit more chaos. It's certainly changes the load requirement because from a certain perspective because the amount of data that blobs that are going to be stored locally for each one becomes much much shorter. But I do think that if not devnet 9 some sort of lick side chaos net seems really valuable to put it on a pretty short term depth I think things are going to fall out.

**Barnabas Busa** [24:25](https://www.youtube.com/watch?v=zODMnGxQBG0&t=1465s): All right but do you mean the ejection balance should not be 16 or.

**Danny** [24:29](https://www.youtube.com/watch?v=zODMnGxQBG0&t=1469s): No the pruning period so it's like three weeks parameterized but you could make it half a day or a day and you can do a lot more chaotic things around that threshold if you do so does that make sense.

**Paritosh** [24:55](https://www.youtube.com/watch?v=zODMnGxQBG0&t=1495s): About once we're happy with some base level of stability you can just start like a line of distance with attack Nets called attack Nets leave Donuts alone so people can do that tooling and stable testing and then we can have all the chaotic testing on our attack net.

**Danny** [25:12](https://www.youtube.com/watch?v=zODMnGxQBG0&t=1512s): Yeah I think I agree especially in the context of like if we want devnet 9 to look and feel like the thing that we're going to launch it should probably look and feel like the thing that we're gonna watch. Okay cool there's a testing call on Mondays. I think it was pretty low attended on the consensus layer side. This past Monday I think it's every other Monday and I think as we are moving towards ironing out the final Kinks that's definitely worthwhile having some more attendance there. What is the pruning variable it's in the P2P spec on devet if I can pull it up main epics or blob sidecar requests. And I'll send the spec that it's for them.

**Barnabas Busa** [26:26](https://www.youtube.com/watch?v=zODMnGxQBG0&t=1586s): Right so that's 4096 a box at the default which is 18 days.

**Danny** [26:34](https://www.youtube.com/watch?v=zODMnGxQBG0&t=1594s): Yeah so you know 128 or 256 you know half a day or a day it probably gets weird if you make it really short but it might be worth playing with you okay. Okay alright cool anything else on testing conversation for today? Great thank you. So outside of the open it's even if it proves tough to make decisions today. It's time to reopen the conversation around the mainnet parameterization for the blob data gas limit. I think maybe that name was changed or something but blob gas limit essentially the gas line. So codex is going to kick it off they've been taking a look at Big mainnet Blocks and the information we can Csaba Kiraly of that Codex.

## Codex presentation on big mainnet blocks & Q&A

**Costa** [27:42](https://www.youtube.com/watch?v=zODMnGxQBG0&t=1662s): Thank you. Let me take a share. Okay yeah, so let me just quick background so  I'm sure from the Codex team we are not many working on the Central Storage but we are also working with an inbox team on only P2P. And we are working with ef with a gland on data available sampling and what we show here is kind of a side product of that work. So as part of the database sampling we were looking into gossip sub performance and especially to understand how it works now onto the network with Big Blocks and with small messages. We're going to show you that now and then we also had some nice findings on about big blocks now on the network. So let's just look into this how Big Blocks work now in the  mainnet. So that was the big block experiment my data Foundation I think you're all aware of this. So there was a capacity testing of the mainnet in which large transactions were submitted which then made it into large blocks which then could finalize. So here you see one example one of these blocks that was one megabyte in size and it was nicely finalized. So this would be a nice result for the experiments. Nice big blocks can be finalized but the experiment was about much more besides sending these big transactions which we came into Big Blocks. DF was also setting up the Sentry nodes. So I don't know how much you will this Sentry nodes are was set up in three locations. In each location each client was running basically depending on the time period a few of instances with running in these locations. And then metrics will collected well client implementation. So here you see the dashboard which was shared previously in which you see delays in seconds and some distributions of these and here see the below the design dotted time instances when blocks were big. And we wanted to get a bit more data out of this so we were looking into details. And this is what we got so if you look into latency data annd you look into the blocks and then you categorize blocks according to block size. Then you can basically plot how different block sizes are getting diffused in the network Now this is not one block one block diffuse in the network because for each block we have only a few measurements. But if we take a large number of blocks between 64 and 120 kilobytes for example. And we have measurements on all of these then from these we can plot a CDF. So what you see here there's an orange curve for example is a large number of of blocks detail is that size and latency measurements on these the latency means the latency compared to the to the spot start so when client implementation was saying I have received this block and what you see here is what we expect. So the bigger the block the bigger the delay. The point that you see here that highlighted is 64-128KB  block. 80% of blocks arrives before that time which is kind of two percent two seconds a little bit less than two seconds. So this is really nice we've seen since the diving we've seen the increasing delay. We wanted also to quantify this delay. But we were running into a few problems and the promise was that looking at different client implementations. We were looking seeing different numbers. So the figure that I was showing you was for please but then if we look into the different clients and here the client means the client receiving the block. So not the client which was originally putting the block on the network we don't know that this is the client which was receiving a block. And and we see these kind of differences. so as you can see there are differences and we already know that these differences are passage due to the semantics. So the meaning of the timestamp that we have as a latency is different in different clients. We need to know that there are some clients I think Disney is one of these which are exposing the timestamp when they receive the message on the gossip sub others are doing or the processing that they have to do and then they are exposing the timestamps. I don't know this is just a guess others might have low priority reporting set. So they might just have a timestamp which is very different so we don't know the other things behind but we have different spells for different clients. We were also looking into attestation latencies. I'm not showing that now the facilities that this has very small messages but we have lots of them. So we have much more data to plot some this is what you have seen with the Big Blocks and then looking into this we had also some nice things which is that.

**Leonardo** [33:33](https://www.youtube.com/watch?v=zODMnGxQBG0&t=2013s): Yes so looking into this at some point we started looking into the data sets that we have with the group Arnigo labs and we discovered that we observe also other Big Blocks in present in the network. And we noticed that these were out of the period where we were doing this experiment of injecting large transactions to make large blocks in purpose. And so we noticed that there were organic blocks that were really big in mainnet. And so we did a study on this so here we collected data over the last six months. So from March to till the end of August and we found that about we have over a hundred thousand blocks that are larger than 200 kilobytes knowing that the average block size in mainnet is about 100 kilobytes. So this is about 1.3 million slots. And so 109000 is about 8% of the blocks have these kind of big sizes. The biggest block was in this six months of period was sent about 15 days ago on August 22nd. You have the slot on the screen and the size is about 2.3 megabytes which is really really big. I mean, surprisingly,  at the beginning we didn't know that. We could have such big Big Blocks. Next slide we can see here just to give an idea of a distribution of the big blocks. This is all for blocks that are over 250 kilobytes. Here we don't see really well the Distribution on the right. So if we pass to the logarithmic scale we can have a little bit more more understanding of what we see on the side of large block. And so yeah what is interesting about these large blocks and the fact that they we can find them organically in the mainnet. Is that we can use them to compare anybody can basically use them to compare how block propagation happens for this kind of large block. So in this in this figure you see for example that between blocks of 250 kilobytes versus 2.5 megabytes. We know it takes about two more seconds more or less in average. And so this kind of studies I think help a lot as we move toward you know dank Chardon and very large blocks and again it would be nice to have some kind of homogeneity on how the different clients report this so that we see more clear distribution. And we can convert resource across clients and yeah just to finish. We have some resources here so if you have questions to answer.

**Costa** [36:28](https://www.youtube.com/watch?v=zODMnGxQBG0&t=2188s): Just wanted to add that on this Slide the the time axis the x-axis is Logitech scale so that's why you'd see a different shape from the previous one. So you have one second is the one thousand and then ten seconds to ten thousand and you see look at it thanks

**Danny** [36:44](https://www.youtube.com/watch?v=zODMnGxQBG0&t=2204s): So another question is this the compressed or uncompressed size because the size Channel ether scan I believe is uncompressed.

**Costa** [36:53](https://www.youtube.com/watch?v=zODMnGxQBG0&t=2213s): Yeah, we have discussed this is the uncompressed size. So now we are collecting the composite sizes and we will deploy it as a function of content size. Actually both both metal so complex size is metals and network uncompressed size Matters in the complexion and processing so it's also interesting too to see those differences.

**Danny** [37:12](https://www.youtube.com/watch?v=zODMnGxQBG0&t=2232s): Yep thanks.

**Costa** [37:16](https://www.youtube.com/watch?v=zODMnGxQBG0&t=2236s): Yeah we were sharing these links on the in the issue description so you can go and and check out these are Jupiter notebooks. So let me play with them.

**Danny** [37:32](https://www.youtube.com/watch?v=zODMnGxQBG0&t=2252s): Great this is awesome. Any other questions for the Codex guys. Obviously I think one thing that we need to contextualize here is these are sent as single payloads versus the method of serving blobs via them being broken up into the different subnets is going to have a different impact on how they're propagated. But still I think it's very valuable yeah so any questions.

**Costa** [38:13](https://www.youtube.com/watch?v=zODMnGxQBG0&t=2293s): Yeah I mean in the meantime just too little from my side the goal of this was party to look into the also into how small messages will propagate. And for that we were looking into it yet the station latencies. We didn't put it in the slides but that's somehow we defend the two. We should also have an understanding of how I'm making up things we really can in visual constructs.

**Leonardo** [38:39](https://www.youtube.com/watch?v=zODMnGxQBG0&t=2319s): There's a question about the description of the methodology used to collect the items data. I think is this is not describing in the notebook links that are in here in the slide. But we're writing right now post and Brad is going to be ready in a couple of days describing all the methodology.

**Costa** [38:57](https://www.youtube.com/watch?v=zODMnGxQBG0&t=2337s): Yeah in the first link Block size vs Latency says latency. You have at the beginning you have a link to the EF post about the present the notes and the setup. So that the times was part of the question and then you have a methodology to derive these results. Maybe it's important to say that behind such a distribution a curve heal you actually have a several random reliables. You have at some point the block was put in the network then the network was getting to all the nodes in which we are sampling in a few points. And then this is an aggregate of of many blocks of data collected from mailbox. So for the one specific block this curve would be steeper but when you are adding it up for for several blocks each one finding this pass then you will get.

**Danny** [39:53](https://www.youtube.com/watch?v=zODMnGxQBG0&t=2393s): Got it.

**Costa** [39:55](https://www.youtube.com/watch?v=zODMnGxQBG0&t=2395s): Yeah I think it's yeah from our point of view it would be really interesting to understand who is reporting how? and maybe agree on on unifying this or if just exposing them all timestamps so that we have better data.


**Danny** [40:12](https://www.youtube.com/watch?v=zODMnGxQBG0&t=2412s): Right around the the client disparities we're seeing here. 

**Costa** [40:16](https://www.youtube.com/watch?v=zODMnGxQBG0&t=2416s):
 Yeah around these differences which every child kind of huge differences. So but but we really know nothing some of the teams that the difference is. It's just we don't have the full picture of who's who's doing what in the reporting.

**Danny** [40:34](https://www.youtube.com/watch?v=zODMnGxQBG0&t=2434s):
Right or I guess since we're here our clients immediately aware of like the disparities here you know why maybe lodestar reports a much longer number like maybe it has to do with finishing up a database operation or something like that.

**Leon Dapplion** [40:59](https://www.youtube.com/watch?v=zODMnGxQBG0&t=2459s): Yeah we are aware we'll look into it.


**Costa** [41:05](https://www.youtube.com/watch?v=zODMnGxQBG0&t=2465s):
Yeah I'm just I'm not even sure the timestamp is coming from you or it's coming from the from the login go to the posting so that can be also I think. For example you are depositing another applied the key and then it's getting time stamped much later so it's just. This would be good to notice.


## #4844 mainnet parametrization

**Danny** [41:23](https://www.youtube.com/watch?v=zODMnGxQBG0&t=2483s):
Right. Okay thank you any other anything else for on these experiments. I think Dakota says would be happy to take questions asynchronously as well. Do we have other inputs other than these large block experiments to take into consideration. As we have the conversation about 4844 mainnet parameterization. You know our devnets work our devnets are also compared to probably mainnet topology. Is there any any comments about the devnets and N36 there? 

**Sean** [42:28](https://www.youtube.com/watch?v=zODMnGxQBG0&t=2548s):
So I guess it might be interesting on devnets if we had blocks with like that like took longer for the execution to happen. it's like we could test how different execution times impact our block processing times.

**Danny** [42:46](https://www.youtube.com/watch?v=zODMnGxQBG0&t=2566s): Because this is going to impact propagation probably not because propagation happens before that but it might impact like local import times which are relevant to attestations or what?

**Sean** [42:59](https://www.youtube.com/watch?v=zODMnGxQBG0&t=2579s): Yeah also block production which would be like the first input to Propagation.

**Danny** [43:06](https://www.youtube.com/watch?v=zODMnGxQBG0&t=2586s): Right yeah and I guess it kind of to Ethons question. If you're receiving 36 blocks at 3 seconds and you have really long processing. You might actually not attest to them correctly. So I see how it does compound. Yeah okay so there's not a lot of I think there's probably not a lot of inputs that we have beyond our observing. What we what we've just discussed and maybe there's also not a lot of more updated thoughts on it. So conversations a little late today. I then I guess what I'll say is we need to keep having this conversation over the next few weeks and because the lack of conversation here doesn't make me feel like we can try to make a decision. Yet am I reading the room right.


**Tim Beiko** [‘44:24](https://www.youtube.com/watch?v=zODMnGxQBG0&t=2664s): Yeah I could say that my feeling is just probably we haven't did already the tests that are needed because that needs to be created to actually exercise those bad and difficult stuff the current devents will be has been or well used for bug fixing so far this is my feeling. So I think they the actual test on these things should start now that clients are kind of more reliable. And we can actually fire stable test Nets and then start playing with these partitions and delays.

**Danny** [45:13](https://www.youtube.com/watch?v=zODMnGxQBG0&t=2713s): All right so chaos and load from here and help inform the conversation. Okay this is something maybe we won't bring it up next week but we bring it up in a couple weeks to at least make sure that we're getting the data that we want anything else on for  arameterization? Anything else on Deneb? Okay Etan you can take it away with the 7495 updates and looks like dapplion threw on something last minute to talk about after.


**Etan** [46:04](https://www.youtube.com/watch?v=zODMnGxQBG0&t=2764s): Yeah sure! So as part of this SSC transaction and receipts work that I mean I started this a long time ago. Maybe already half a year I think but the current approach. I tried to unify these unions and normalized approaches and I created a construct called a stable container like it's an SSC container. CLRS is very similar but it can have optional fields. And they get skipped during serialization but they still consume space in the miracle tree. So what this allows us to do is essentially to have something similar to a union where some objects have some of the optional field set and other objects have other field set. But the cool thing is as part of the Miracle tree the common fields that are used they always miracleize at the same location. So if you have a merkel-proof verifier for some of the fields that like just doesn't care about the rest. That verifier doesn't need to change all the time anymore. So I was wondering whether this table container could be used for other purposes as well. One idea is to for example attach it to the execution payload header. So that we don't have to worry about those bombs anymore where every time we add new fields and it reaches another Power of Two we break all the verifiers. Or like some other structures as well. and also in in the virkle specs there is currently an older version like this these optional fields are there to as part of the transition logic. I think there we could also use this stable container just because it's much more compact in serialization the optional Fields there they just don't consume any space. and like a zeroed field. Or I think the option allows it doesn't do space so yeah whatever. I mean question there is just I'm looking for reviews for EIP #7495.  And also maybe an estimate how complicated it would be to get it into the various SSC libraries. Yeah a channel in Discord if there are questions is the typed transactions Channel or just in the EIP there is also a discussion Link at the top. That's all for now.

**Danny** [49:00](https://www.youtube.com/watch?v=zODMnGxQBG0&t=2940s): Yeah any questions? All right take a look at it and follow up Ace information thanks a Etan. Dapplions?

**Dapplions** [49:21](https://www.youtube.com/watch?v=zODMnGxQBG0&t=2961s): Hey so I'm linking this PR that opened a while ago and I'm bringing it up now.Because it only makes sense if we want to do this for Dencun, which I know that is zero appetite on changing anything for Dencun at the moment. But I think the PR holds  submitted and I think at least Dunkard and some other people showed interest to do something like this. So at least I want to bring it to everyone's attention that this is something we could do. And it only makes sense if we do it for Dencun. So if we want to do it for the code we have to do it basically either now or very soon. So the background here is as you know the network is growing at a very rapid Rate. And if we don't do anything about it it will reach levels that could trigger some scenarios that we may may be problematic the way to address this on the long term is changing the rewards curve but doing this would require a level of research that we cannot afford for Dencun. So it will take at least for the next Fork, which would be being optimistic meet to meet 2024 maybe later.  Which at what point the network may be at a level that's again triggers this undesirable scenarios which is basically too much if stake and dangerous captured by LSD’s and also having State size to a level that clients cannot cope with it. None of these problems is truly catastrophic but it could be. so the idea of this PR is let's limit the churn. So that at least we buy some time. And whenever we come up with a definitive solution in a year or half a year or two years the network is still at the size that could be manageable. And specifically if we go for some solution since it's changing the rewards curve to encourage stakers to leave if we already  have such a big  but later said. I think it would be rather complicated to undo. So again just take a look at the proposal, think about it and if we want to do something about it we should do it now.

**Danny** [51:52](https://www.youtube.com/watch?v=zODMnGxQBG0&t=3112s): Thanks.

**Marius** [52:04](https://www.youtube.com/watch?v=zODMnGxQBG0&t=3124s): Can you quickly explain for laymen what this proposal is about? 

## Research, spec, etc

**Dapplion** [52:12](https://www.youtube.com/watch?v=zODMnGxQBG0&t=3132s): Yes, so this proposal has the intention to limit the growth of the validator set just by limiting the churn coefficient. So currently the growth is exponential with  normal validators, the amount of validators that we allow to enter the set is proportional to that to the number of active. So what this proposals specifically introduces is a Max so that the maximum number of validators that are allowed per Epoch remains constant and doesn't keep growing with the set size.

**Danny** [52:52](https://www.youtube.com/watch?v=zODMnGxQBG0&t=3172s): Just a note so churn question grows with the set size because essentially as a function of the set size to keep the same security parameters with respect to the subjectivity period you can change the set size only so much per unit time as a function of the set size. And so that's why it does grow with it obviously there are other considerations. How am I going to play these years. So it bounds it to be linear as a Band-Aid well people think more deeply about more Sustainable Solutions.

**Dapplion** [53:43](https://www.youtube.com/watch?v=zODMnGxQBG0&t=3223s): Yeah this book was always the minimum that we can do that could be considered somewhat Fair like any other solution that tries to mitigate the problem becomes either really political or security sensitive and would require more analysis. I think this is probably the only one that we could accept without a long time looking into it. I mean there are definitely some considerations that Danny raised about fairness for people that want to enter before and after this change. But I think it's not  incredibly significant compared to what could happen Downstream.

**Danny** [54:27](https://www.youtube.com/watch?v=zODMnGxQBG0&t=3267s): Yeah to be clear I don't think there's a like perfect Band-Aid. And so if there's an appetite for Band-Aid this seems in a reasonable Direction  but I'm not gonna throw my hat in the ring too much on if this should modifier spec at this point. Is there are there other comments today? 

**Barnabas Busa** [55:17](https://www.youtube.com/watch?v=zODMnGxQBG0&t=3317s): This is actually going to be considered for Dencun?

**Danny** [55:24](https://www.youtube.com/watch?v=zODMnGxQBG0&t=3324s): The answer is no one speaks up and says something that has to be has to go in but here we are talking about it.

**Dapplion** [55:40](https://www.youtube.com/watch?v=zODMnGxQBG0&t=3340s): Well in this course you have to ask the negative question right. Let's say is someone against adding this to Deneb?

**Sean** [56:02](https://www.youtube.com/watch?v=zODMnGxQBG0&t=3362s): I think I might be I'd have to think about a little bit more but my two cents generally is that like this is sort of a patch fix. And it is really small but it's small enough that like we could do it in its own Fork in something equivalent to like a difficulty bomb delay or something. I think it'd be better to put more effort into a better fix. And also like I don't know clients are continuing to improve how they handle larger validator set sizes stuff like that. Yes I don't think I'm in favor of it at this point. But.

**Danny** [57:10](https://www.youtube.com/watch?v=zODMnGxQBG0&t=3430s): Yeah, I mean this is one of those things that is you know happens late in the cycle urgent or potentially urgent things come up.  I think at this point given the state like the default is to do nothing and that I'd want a pretty loud we need to do this if we're going to derail that obviously if I'm mystery in the room then be loud and tell me otherwise. But I think we would need people to be speaking up you know and if that means review the proposal and sit on it a week and we talk about this you know asynchronously or even bring it up on the Execution Layer call. That's okay but I do think that we're at the default stable spec unless it's quite a verbal Consensus Layer to switch. Okay I do encourage you to look at and review this proposal there are High urgency problems in this domain. And it's going to be probably a big part of the Electoral conversation if nothing's done now. So let's continue the conversation and if this does Bubble Up as critical higher urgency after others have reviewed this. I thought more deeply about it this week speak up. Thank you Dapplion.

**Tim Beiko** [59:01](https://www.youtube.com/watch?v=zODMnGxQBG0&t=3541s): What is literally rewarding me I was just add one thing is that sometimes things happens non non-linearly so you got you arrive you reach some level of things. And things go bad very quickly. So it's something that they're definitely is let us thinking for a while and I'm personally not against this proposal but to what would you also have Holesky testnet ride about to be launched maybe this could be could give us more insights and prioritize it eventually in the future.

**Dapplion** [59:51](https://www.youtube.com/watch?v=zODMnGxQBG0&t=3591s): Right I want to mention if it's not clear maybe in the proposal there are two angles. so one is the state growth and what can that cost to clients and performance and the other one is the economics of it specifically if you don't believe that Lido having a hold of 50 of all the Ethan existence is healthy there is a train of thought that the only way to prevent that is by limiting overall if stake because of the one Winner Takes all Dynamics so just to consider.

**Tim Beiko** [1:00:24](https://www.youtube.com/watch?v=zODMnGxQBG0&t=3624s): Yeah I was thinking only on the technical side of it at the moment.

**Danny** [1:00:32](https://www.youtube.com/watch?v=zODMnGxQBG0&t=3632s): It's not actually I think abundantly clear to me that by just changing the total amount of ETH that it will be staked by a different limiting mechanisms. That would change light of dominance. Maybe tougher because you might have sticker short-term equilibriums. But it's not I don't know if that changes like the convergence there are the incentives there. I'm very concerned about.


Dapplion  [1:01:08](https://www.youtube.com/watch?v=zODMnGxQBG0&t=3668s): It prevents later from having basically having a higher market cap than ethereum in terms of liquidity.

**Sean** [1:01:23](https://www.youtube.com/watch?v=zODMnGxQBG0&t=3683s): This is just slime like the process of that happening. Though it doesn't actually change it from happening.


## Open Discussion/Closing Remarks

Danny  [1:01:32](https://www.youtube.com/watch?v=zODMnGxQBG0&t=3692s): I think the argument would be it slows what happens to them have a more sustainable solution  before the equilibriums are totally out of whack. nankara did say in the chat  he's in favor but and if we don't do it this probably becomes like a very high urgency thing right after before how complex is the chain. Yeah it's essentially a not quite a parameter change it's like a parameter addition and conditional on at the fork it being constant rather than a function but it's a couple lines. Okay is there anyone's suggestion on how to move forward do nothing let it marinate for a week make sure the spec is correct with tests. In case we do want to bring this up again next week like what's the path .

**Tim Beiko** [1:03:39](https://www.youtube.com/watch?v=zODMnGxQBG0&t=3819s): I'm not sure if this was discussed on AC DC before but on the execution side we typically try and not include something in the fork the first time it's brought on the call just so forks have you know a couple weeks to to review it. So yeah I don't know obviously the closer the farther we push this out the closer we are to like testNets and the morning cups specs finalized but I don't know if given the small size of this change nd like this sort of weak-ish consensus that there seems that to be around it it might make sense yeah delay another couple weeks before officially inconvenience.

**Dapplion** [1:04:29](https://www.youtube.com/watch?v=zODMnGxQBG0&t=3869s): So I want to point out that this is not the first time this is brought up this was brought up in call 113 on July 11th for the first time.

**Danny** [1:05:08](https://www.youtube.com/watch?v=zODMnGxQBG0&t=3908s): Is this something that we can put as a special agenda item on the Execution Layer call in one week and people can go back to their teams and talk about it and either come with like a strong yo or strong yes from various teams. So that we can push ourselves out of the murky equilibrium we sit in today and in the meantime we can review the spec and make sure that we're good on tests in the event that this switch to go in.

**Dapplion** [1:05:49](https://www.youtube.com/watch?v=zODMnGxQBG0&t=3949s): Or maybe here if dankrad wants to help on writing a piece to help get the arguments through and why this is important?

**Danny** [1:06:00](https://www.youtube.com/watch?v=zODMnGxQBG0&t=3960s): I will leave that to the Dankrad if he wants to. Okay if we're sitting in like the UN super uncertain Zone in a week then this isn't going to happen. So talk with your teams. Please try to form a consensus on whether this is you know verbally precisely where you'll stand  either as a team that'd be great or if you all have differing opinions to express those. But if you can express those you won't make time we can make a decision. Cool thank you Dapplion. Anything else for discussion today? Barnabas?

**Barnabas Busa** [1:07:05](https://www.youtube.com/watch?v=zODMnGxQBG0&t=4025s): Holeskey launches in one week as in eight days next week Friday is the launch day. So hopefully client teams can make a release before the launch day and everyone is ready to go.

**Danny** [1:07:22](https://www.youtube.com/watch?v=zODMnGxQBG0&t=4042s): Very exciting thank you.

**Paritosh** [1:07:25](https://www.youtube.com/watch?v=zODMnGxQBG0&t=4045s):  And if you're a Genesis validator and don't know about the coordination group then please reach out.

**Danny** [1:07:41](https://www.youtube.com/watch?v=zODMnGxQBG0&t=4061s): Okay anything else for today. Great thank you and big ask talk to your teams sit on this proposal come with strong opinions on the Execution Layer call in one week time. Thanks everyone. Talk to you all soon thanks bye.


# Attendees

* Pooja Ranjan
* Lion Dapplion
* Danny
* Justin Tragila
* Csaba Kiraly
* Mario Vega
* Barnabas Busa
* Leonardo Bautista
* Lightclient
* Phil NGO
* Costa
* Tim Beiko
* Dan
* Cayman
* Gajinder
* Anjana Ratnayake
* Dankrad Feist
* Mikhail
* Marius
* Terence
* Ben Edginton
* Roberto B
* Sean
* Paritosh
* Saulius Grigaitis

### Next Meeting Date/Time: September 21, 2023 at 14:UTC

