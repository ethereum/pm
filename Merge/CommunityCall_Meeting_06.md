# Merge Community Call #6 Notes

### Meeting Date/Time: Friday 2022/08/12 at 14:00 UTC (10:00 ET)

### Meeting Duration: 1 hour

### [GitHub Agenda](https://github.com/ethereum/pm/issues/580)

### [Audio/Video of the meeting](https://www.youtube.com/watch?v=AZq1acbjaz4)

### Moderator: Trenton Van Epps

### Notes: Avishek Kumar

---

## Summary 

-  Plan to have another merge community call in September 

—----------------------------

**Trent** [00:12](https://www.youtube.com/watch?v=AZq1acbjaz4&t=12s): welcome everybody to the sixth merged community call. We are very happy to have you here. We are going to go over general updates about where the merge is at any announcements related to mainnet timing if you haven't seen them and there will be time for questions as always and yeah we can get started. I am just going to do a quick survey through the members just to see what client devs or researchers are here. Tim do you want to kick it off with?

**Tim Bieko** [0:44](https://www.youtube.com/watch?v=AZq1acbjaz4&t=44s):  Yes I wanted to chill ladies and gentlemen here. Sorry yeah someone in the chat says they can't hear, but can somebody else confirm? that they okay remy already confirmed that the sound is good? Can somebody else confirm that they are here in the chat ? Okay perfect , okay thank you. 

**Trent** [1:06](https://www.youtube.com/watch?v=AZq1acbjaz4&t=66s): Yeah go ahead and I will just try to grab links for whatever you're talking about or if you have them handy and throw them in the chat. 

**Tim Beiko** [1:18](https://www.youtube.com/watch?v=AZq1acbjaz4&t=78s): Sure I guess the first thing we can cover is basically the last test update and  mainnet. Yeah, that's how we got there, so as people may have noticed Goerli which is the most used test network for applications and stakers moved to a private stake earlier this week. Good question by Trent was there a Goerli retro? Yes, Pari had a dock looking at the various um issues we hit the main one. Was that one of the client teams who run a lot of validators had an issue updating their nodes and that's been fixed then?  Since then there were a couple  issues with some of the client implementations but they did end up kind of reorging back and kind of being on the main chain. So given all of this client team still felt comfortable moving ahead with setting a date for maintenance and so yesterday on the consensus call we did that. We have now got an epoch for the bellatrix part of the upgrade. Let me see if I can pull up the number real quick. The epoch is scheduled for september 6th. I don't have the exact number. Maybe someone can find it and put it in a chat? So september 6 is when we expect belatrix to hit on the ethereum mainnet. 

Oh actually yeah Danny just posted his link in the chat. He put up a blog post today with all this info. So if you run a node validator or another type of node you wanna upgrade before september 6 both your EL and your CL client we expect to have a blog post with all of the proposed versions for these clients out around august 23rd. We do want to reconfirm that the ttd is right next week on the All Core Devs call but there is a very high chance that it's not gonna  change. But this is kind of the cause of the lag there. So next friday, next thursday we confirm the ttv on All Core Devs.  A couple days after that client teams put out a release on the 23rd expected blog post on. There'll be something on the ef blog but you can expect announcements across. You know the various clients themes, communication channels and what not if you can download these then you want to have upgraded before september 6th at 11:34 am UTC. 

At that point the beacon chain will upgrade to bellatrix which just gets it ready for the merge and then we have set at ttd. Ttd value starts by 5875 and  zero zeros towards the end. We expect this to hit around september 15th. Ttd is a function of the difficulty on the network which is a function of how much hash rate there is, so if there's a kind of increase in hash rate then we would hit it before september 15th. If there's a decrease we would hit it after  so this is why it's kind of hard to get an exact date and then Trent shared in the chat at ttd chat. Ttd tracker which updates kind of based on the latest hashrooms. 

Then the last thing I will say before I pause here is  between the original announcement like what you expect on august 23rd and ttd. It's expected that client teams will put out other upgrades of their release, so you know with either stabilisation improvements or just new features or stuff like that. So you probably want to keep an eye out and yeah follow whatever client you're using in those couple weeks because they might put out another release before ttd is actually hit. There might be basically almost a month between the time when we actually announce it in the timer and when it hits and then the actual last thing I will say is because ttd is very hard to estimate because it's a function of hash rates. We are in kind of the last innings of proof of work on ethereum. If we saw that the hash rate would drop dramatically and that instead of you know hitting ttd around september 15th, hashrate drops a ton and now we think it's going to be like october 15th and  kind of getting later and later . We could coordinate a ttd override. We did this on the robson network already. Ideally we don't just because it kind of forces people to either upgrade their nodes again or run a special command to do this. But if we see that you know bellatrix is activated and ttd is is not getting any closer because hash rate is dropping then we might make the call to do a ttd override and so again just please pay attention to either like blog.ethereum or your clients communication channels and this is where this stuff would be announced. But in fact yeah Danny's article has like a pretty concise summary of all of this.

**Trent**[6:54](https://www.youtube.com/watch?v=AZq1acbjaz4&t=414s): Great job Tim, yeah I think you have covered everything with all the updates.

**Tim Beiko**[6:58](https://www.youtube.com/watch?v=AZq1acbjaz4&t=418s): Yeah I think we could probably do just like questions for the rest because that seems like you know, so I mean like we have.

**Trent** [7:07](https://www.youtube.com/watch?v=AZq1acbjaz4&t=427s): If people didn't pick up on this, generally the summary of Tim's summary is if you haven't been paying attention before now is the time, the merge ttd has been chosen and this is likely what the number will be. It's not saying it won't change but this is the time if you're validating on the beacon chain. You want to be tuned in, you want to be aware of what's happening and making sure that you're running the right software ahead of the actual merge event, so for the next month or so you know don't disappear for a month make sure that you're following
 the client teams with the software that you're running. We would hate for somebody to miss it when the actual time comes. All right yeah and we can there are some client devs and researchers here who probably can answer questions. So if anybody does have questions generally.

**Tim Beiko** [8:16](https://www.youtube.com/watch?v=AZq1acbjaz4&t=496s): I think Pari is here. Pari, do you want to like to walk through the dock that we shared a bit more and kind of talk about like the implications.

**Trent** [8:28](https://www.youtube.com/watch?v=AZq1acbjaz4&t=502s): Yeah and generally just I will unmute you or find you first but generally what the  sort of class of issues that we hit over all of the test nets and generally what that means for mainnet. I think immediately Pari let me know if that didn't work.

**Parithosh Jayanthi** [8:45](https://www.youtube.com/watch?v=AZq1acbjaz4&t=525s): Yeah,  hey I think this should work now. I do have another doc that might help with that. Hang on, let me just find that. Just kind of goes through the class of issues that one might face during the march. yeah so we had the Goerli test net part. Yesterday and a decent bunch of the issues were just attributed to a client team not setting up the JWT authentication. So since so the merge is introducing this concept of an execution layer and a consensus layer so if you guys are used to running ethereum nodes what you've been running so far is now called the execution layer or eth1 node and you would have to add a consensus layer node that's the beacon chain node and in order for these two nodes to communicate with each other. We have introduced a new port that's the engine API port and by default that's port 8551 and that's an authenticated port. So you have to configure the same JWT secret on both sides. There's a bunch of guides online to guide you through how to set up these nodes as well as what the secrets mean and they're extremely good. I think we even have a couple linked. I will try and find the link  but that being said the client team had forgotten to configure the JWT token and once they did that the notes came back online.

The other issues were due to multiple terminal blocks and that essentially means the merge had two candidates and the nodes took some time to decide which of these candidates they're backing and we had some fail safes built in and the failsafe kicked in and once they kicked in. Essentially the chain was okay again but those were like the two big classes of problems. Yeah and besides that I would highly recommend that everyone on the call, look
through the checklist for the merge. It's again not not an exhaustive document but it covers most of the pitfalls. We have seen over the last couple of merges. Especially have a look at the common pitfalls like almost every big issue. We have noticed it has been because there was the wrong flag used or the port wasn't configured or the secret wasn't right or people just forgot to run one of the two pieces of software needed. So yeah just please have a
look at those and in general the logs will tell you nine out of ten times that something's wrong and I am happy to answer some questions, if someone has something

**Tim Beiko** [11:46](https://www.youtube.com/watch?v=AZq1acbjaz4&t=525s): I guess you have just more questions on which we can answer them. I guess you can ask them in the chat and we can answer them as a follow-up  and just worth noting Pari posted his checklist there and then there's a similar document on the launch pad as well that I have posted so if you are on a validator. Yeah just running through those.

**Trent** [12:09](https://www.youtube.com/watch?v=AZq1acbjaz4&t=729s): I think we should probably compile all of these links into a single spot just so it's easy.  Yes go ahead 

**Tim Beiko** [12:18](https://www.youtube.com/watch?v=AZq1acbjaz4&t=525s): Yeah we can do that yeah with the notes of this thanks. Okay Oleg has a question about ttd suppotage, so the only two ways you can affect ttd with proof of work. One is you stop mining and then ttd takes forever to be reached and this is the only impact that this has. Is it makes the merge happen at a later date than it otherwise would and so if this were to happen and you can think there's many reasons for people to stop mining now. Right? It doesn't have to be sabotage. You know people might choose to sell their gpus because they feel like their return on, like the rest of the mining life on ethereum, is not worth it. So it's not necessarily like malice that triggers this but if people stop mining ttd happens later than it. Otherwise  what we need to do is basically select a ttd value that is lower than the current one which we would then hit quicker kind of based on the new hash rates. So every single client has a flag or a configuration option that allows for this and clients can also put out new releases. New releases overwriting this. We have tested this procedure on Robson before. 

So I will link you to a blog post that kind of shows you what it looks like and kind of links every single client's command to upgrade to update this value. The other way that proof of work and ttd can kind of can kind of  get tricky is if there is so much mining power on the network that ttd ends up happening before the Bellatrix upgrade is activated and this was actually the case on Robson. We didn't have the case where there was not enough buying power. We had a case where there was too much. The reason for that is that mining on test nets is  basically not a profitable thing. So the hash rate is quite low and  so it's quite easy to raise it significantly so when we chose the ttd yesterday,  we basically choose a value which if you wanted to make it happen before Bellatrix I believe you would need the hashrate to have already spiked back to the all-time highest. We have seen on the ethereum network and to keep mining at that rate until we hit ttd and then the closer. We get to Bellatrix with every day that passes. You need to then not be at all time high but you need to have an even greater share of hash rate than that and because this is something we see on the network. If something like that were to happen you know we wake up tomorrow there's a massive supply of hashrate then we could do it override which pushes the ttd back to a higher value and then as soon as Bellatrix has happened. So it is scheduled for september 6. Then it really doesn't matter when the ttd is hit it becomes purely a sort of coordination exercise about like you know making sure everybody has the same ttd set But there's no kind of impact or attack on the merge based on that. So basically we think that yeah choosing a value where you know we have some pretty solid bounds in terms of how much the hashtag would have to increase to disrupt things. And then having like code and kind of a release procedure. That's well tested such as if this thing happened. We could counter it and so far. It's not looking like the hash rate is rising; basically the all-time high was something like 1100 pairs. Peter I am not sure what the unit is. Oh sorry 11 giga hashes oh sorry no anyways the 1100 something and then we are at about 900 now. So we have dropped since the all-time high by a fair amount. it hasn't risen since we have the ttd. We will keep monitoring it but then you know a week or two from now. You would have to have hash rates that goes past what the previous all-time high hash rate was and I think that becomes quite unrealistic and then maybe there's a follow-up question about what's the backup plan in the case of merge trails or some series of issues happen, so there's no way in which we can go back to appropriate work once to activate the merge sequence and the reason for that. First the code does not allow it but like the kind of design reason is once you move from proof of work to proof-of-stake and even once you signal that move. You can't  assume that if it doesn't work out on the other side. You can come back and the hashtag will still be there waiting for you and  mining right at the assumption. From a design standpoint is just  once we activate this you know we we assume that  there is no longer security on the proof of work side that could like backstop us and we need to ensure that like things work out on broomstick and obviously you know this is why we do so many test nets, so many shadow forks. If there was an issue that happened on emerge which we did you know which we
hadn't encountered so far. The solution would be fixing it on proof of stake on the main net as soon as possible. Not going back to the cover stage. Effectiveness  Remy I see you're posting about this in the chat. You want to ask that question?

**Trent** [18:10](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1090s): I will try to unmute him. Can't find the account. Oh maybe it's because I am a special character or something, yeah one second.

**Remy Roy** [18:24](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1104s): Hey Hey so effectiveness is known to be wildly changing on tests right? So I believe you were an illusion. You were mentioning that your effectiveness went down after the merge and I am guessing this is on Goerli. So it's common to see effectiveness changes on tests because  there's less resources being spent. There people don't have any real value or real money there. So it's not uncommon to see effectiveness go down but I posted the resources on effectiveness if you want to check it out in the chat supposedly by a testant. It'll enlighten you on how it's computed. I am not sure exactly how it's computed on the beacon chain of the website. I can't remember how it is but I believe it's with your attestation, if you're always correct in terms of the votes that you do on source target and head but on I mentioned on tests that it widely changes because people are not putting the same resources but on mainnet it should be quite stable. I don't know how it will look after the merge on mainnet but I assume it will eventually be quite stable.

**Trent** [19:57](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1197s): Thank you 

**Remy Roy** [20:00](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1200s): Hopefully that answered the question from the chat.

**Trent** [20:08](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1208s): Let me scroll up and try to find the next question. caleb asks are there plans to allow for a single cl multiple el configuration without a mixer, oh a multiplexer

**Tim Beiko** [20:25](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1225s): So today it's oh Danny you have the idea to take it. let's see can win right? 

**Trent** [20:36](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1236s): There are two Danny's.

**Tim Beiko** [20:38](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1238s): Lower case 

**Danny** [20:52](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1252s): API is unlikely to support that directly client teams may add support. But I think some sort of multiplexer sitting in the middle is a better generic solution. Gas I think cl client supported it you know if anyone does it'd probably be vary.

**Trent** [21:16](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1276s): Okay so short answer not without a multiplexer for now at least 

**Tim Beiko** [21:24](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1284s): Next one will this usage increase faster after the merger. Can I assume the same size increase before the merge summing up the usage is cl and el client. I know there was a thing here about like the blocks being stored on both layers and prysm. I knew I had looked into this. I don't know Terence can you give us a little list on the cl side  whether the storage increases because you now store the execution paid out as.

**Terence** [21:54](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1314s): Well, hi can you hear me? Okay so most clients have this feature. It's just not only in prysm, so I would highly recommend you guys to read the client documentation. So the future is basically instead of storing the full payload you store the header and then because there's no point in storing  payloads in two different locations and that's cl and el. Because el is storing the payload already so then the cl could just store the blinded version which is just a transaction root and if you need to retrieve the payload you can just get it from the el. So I would highly recommend you guys to read the documentation. I think for a prysm it's created behind the flag. It's not enabled by default and so the compromise of not using this feature is that I think this size will increase by what like 200 gigabyte per year,so if you're waiting to take the hit that's also fine as well so there's yeah so it's just a nice option here.

**Tim Beiko** [22:59](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1379s): okay so yeah short answer I guess is by default they would increase a bit because the execution payloads get stuttered on both sides but cl teams are working on or already have features to mitigate that to a large extent.

**Terence** [23:13](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1393s): Yeah exactly 

**Tim Beiko** [23:14](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1394s): Sweet thank you.

**Trent** [23:21](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1401s): Any other questions?

**Tim Beiko** [23:26](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1206s): Netermind plus lighthouse after the merge started to reorg. This is the angoria  I expect we did see. I don't know if there's anyone from Nethermind on the call here. If not I don't see anyone Nethermind if there is please let yourself known in the chat and will on youtube. If not there was definitely an issue that was found with Nethermine during the Goerli merge. It is mentioned as part of the dock that Pari shared earlier. Yeah I don't know that there's anyone on it who can have more details. Oh yeah exactly so in this doc there are some issues there. Yeah exactly this is literally what yeah yeah this is probably the issue from the doc where you have to restart and then it's back to normal. So the nethermine team is aware and they're working on this right now yeah and there's an hive test  that's also gonna be added to hit exactly this edge case if  I am not mistaken. Oh they already have a fix Harry says.

**Trent** [24:47](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1487s): Any other questions?

**Tim Beiko** [24:58](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1498s): If not I have a question for it's taker folks. Will there be another validator prep workshop before the mainnet merge? and if so where can people find this information?

**Remy Roy** [25:19](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1519s):  Yes, so there will be another workshop in about 30 minutes. So if you want to learn more about the details of that workshop let me try to find the link here. I will post the link in the chat so in 
In about 30 minutes, we'll have another workshop and people will be able to join us I believe.
We will have a summary giving us some updates about his guide for the merge and we'll do a bunch of different stuff in order to prepare for the merge and we'll answer everyone's question there. So if you have any technical questions with your own setup please join us and we will be happy to help you.

**Tim Beiko** [26:06](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1566s):  Amazing and is there a plan to have another one before mainnet or is this the last one? Obviously they're all recorded but Yeah just curious.

**Remy Roy** [26:13](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1573s):  Yeah I believe we have a plan to have another workshop  maybe next week or in two weeks. Let's see 

**Tim Beiko** [26:21](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1581s):  yeah okay and yeah Pooja  link that  in the comments there.

**Trent** [26:34](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1594s): Yeah it's. I am not seeing any other questions which I guess I didn't expect given this even closer to the merge but maybe everything's been answered. Oh here we go there's another one

**Tim Beiko** [26:45](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1605s): Yeah a good energy boost question. Is there anyone from flashbacks on the call? or who's like work done with mbv boost

**Trent** [26:58](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1618s): I think Terence has done some of the prison work for it.

**Tim Beiko** [27:03](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1623s): Oh yeah
there you go. Oh Terence you should be on youtube.

**Trent** [27:20](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1640s): Maybe he gave the mic back to Danny. 

**Tim Beiko** [27:28](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1648s): Okay let's wait for Terence.

**Terence** [27:51](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1671s):  So with
med boost it's little trickier because like every cl does this differently, so it's kind of hard to come to this cohesive point. How does it work and  how do you know who is working right? I think for us, we utilise the health endpoint of the mvp boost pretty heavily. So when something doesn't work you will see from the error log right away. So at startup we call mvp boost to check the health if there's some work and then you unlock the arrow and then before the blog proposing will also check the health status right but at the worst case we also
build a block in the background in parallel with the local as well. So it's in the event that the mev boost doesn't work or the relay is done. You will not be missing blood because you can still broadcast your personal block that's from the local ee. So I will say  just pay heavy attention to the log and just grab any error that you can find and that is related to a mev boost

**Trent** [29:07](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1747s):   Thank you Terence aks can you put your question in the chat first before we unmute you. Okay doesn't seem like we have any more questions coming in. Were there any topics or researchers? Client devs is there anything you want to say specifically to this audience of 80 wonderful people that we have here?

**Tim Beiko** [30:02](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1581s): I am actually curious so I like power bowery hopefully. I got your name right? Why do you think the gap should be bigger than seven to ten days given that as a solo node operator. You sort of have to be ready when Bellatrix hits anyway. So once paediatrics hits everything should be configured, so I am curious what's the thing you would like to have a wider gap for? What's the main reasoning? and we can either unmute you or or if you want to answer in the chat. But yeah I am just curious to understand better what's like the constraint there? and then while I think I have. Yeah if I have asked you to unmute if you can but yeah while we're waiting for that  Micah asks us to reiterate the ttd. Is it final ? So it's tentative basically if we should confirm it on all core dev as of next week but then even then if we see some crazy variations in the hash rate or what not we might change it once more. Yeah please keep an eye out but yeah. Okay and then aks has a question about miners turning off their nodes much before the ttd target. So yeah this is basically what we discussed earlier so what would be the first impact of this,  it would make ttd hit much later so that would kind of slow down the merge. There is a point at which you know a significant enough part of hash rate leaving ethereum kind of not as secure by however much hash rate. We have lost and so I think those are all cases like both in which we just consider making the lower and kind of pulling the merge forward based on the new. The new hash rate levels there are if0 we saw that the hash rate was going so low and you know being completely unstable or being attacked. There's another override method that we can use where we actually hard code basically a specific work block and agree on it as the final proof of the work block. This is really not ideal so you know doing that would kind of incur liveness failure on ethereum. So we don't want to get there. So you know if the hash rate goes lower the main solution is just to reduce the ttd and find a closer target.

**Trent** [32:58](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1978s):  Like I mentioned in the chat, the ttd isn't final so if for some reason there is a need to do an override just make sure that you're following tim or the ethereum blog as a place to get information about what the latest is over the next month.

**Tim Beiko** [33:17](https://www.youtube.com/watch?v=AZq1acbjaz4&t=1997s):
and okay there's a follow-up question about like if the ttd if the difficulty goes down so much can ethereum foundation fill in the gaps reminders and the short answer is no like the amount the hash rate that ethereum is massive even if the ef and all client teams wanted to. You know  there's no we don't have like this hardware so it's really the best tool that protocol developers have is just changing the ttd value rather than trying to affect the actual hash rates on the network. On testness we were able to do that because on testnets we basically you know for a couple hundred dollars. So maybe a couple thousand dollars could double the entire hash rate on the test net. This is  on the order of millions to tens of millions of dollars. So I am changing the ttd as much as possible. Oh good question by bub what happened is there's multiple miners that find a block passing ttd at the same time. So the way that the merge is designed is any block which passes ttd which is obviously a valid ethereum block and who is the first block. In its fork retreat to pass ttd is a valid candidate
terminal block, so it's very much possible that you know there's two of them or three of them like we see uncles on the ethereum network right now. So as long as they meet all those
criteria basically the validator who produces the block after is free to choose any one
of them and then it might reorg until this block is finalised and justin is saying in the chat this is sort of what happened in Goerli because basically yeah until we've finalised any proof of work block which exceeds ttd whose parents does not exceed ttd and otherwise follows all the protocol rules is a valid terminal block and this is and so it's possible to for a validator to select any one of them and it's possible for the next validator to select another one and this
is why we want to wait for the network to have finalised before we consider the merge to be complete. Yeah and ideally you know the network will converge quite quickly on one of them but we obviously want to finalise just to be sure.

Okay stable coin migrations, so short answer is at  the application level nothing changes nothing is required for applications to migrate to the merge. So if you have usbc now you'll have usdt after the merge and you know you don't need to move them or do anything with that. So you know there's no like applications where you should have to do an action in the case where there was a separate fork around the merge at the same time. So like a proof-of-work fork in parallel then everything on ethereum kind of gets mirrored on both side, so if you have say usdt balance in theory you have a usdt balance on both chains but then
because say usdt is backed by like actual dollars not on ethereum the tether like the issuer will have to recognize like this is the chain where these usdt's are actually redeemable for one dollar.  I believe so far tether and circle have both  recognized that this would be under proof of stake chain. But yes and Mike is saying this is the case every time there's a network upgrade .You know there's the opportunity for people on the network to not follow this upgrade and then what happens is like everything gets duplicated across both chains but anything that has like a reference to something off chain only kind of gets  honoured or like recognized on one of those two chains and for usdt specifically . I believe pretty much every stable coin. This is the proof of the stake chain and yeah Caleb has an important clarification. You know you shouldn't have to give out your private key sign any messages to migrate your coins. Please please be on the lookout for that . We've seen some really good phishing emails and just  fake emails about this. Recently so if somebody says you need to
move your coin or you need to like you know sign in somewhere to activate the merge or anything that it's  very likely a scam so please be on the on the on the lookout.

Okay so Remy has a question about basically the ttd estimate being from the hash rate at the current level with september 15th that's correct and so this is why we tell people that it is variable. So you know our goal wasn't to reach it exactly on the 15th. Our goal is mostly to reach it after Bellatrix happens and ideally not too far after the 15th, so you can think of like we want to be safe plus or minus a week on each side and this is roughly why the 15th was targeted because if you have Bellatrix on the sixth. You know you would have to have a massive increase in hash rate for it to happen before and if we get you know to the sixth and close to the 15 and we see we're still very far out that we would just do a ttd override based on the hash rate levels there or  the hash rate trends yeah but there is the goal isn't to like absolutely try and get it on the 15th. It's first and foremost to make sure it happens after Bellatrix and then ideally get it in one go roughly close to the 15th but if that's not going to happen. We can always do an override. Any other questions. I don't know where the pandas came from a couple months ago. I will try to find it. 

**Trent** [39:45](https://www.youtube.com/watch?v=AZq1acbjaz4&t=2385s):  Well but the verbal description is the execution and consensus layers are represented by a white player white bear and a black bear and the merge is done. Coming together that's where the panda comes from and people liked it so much it ended up in all the client software. Thanks Parry yeah yeah that's sweet. Yes I said white bear. It was technically a polar bear. There was a summary of Goerli francis. There was a summary of Goerli earlier, There's a doc if somebody can show that again if you're joining late. I am not sure what you mean by resource constraints. You mean in times of non-finality?

**Tim Beiko** [40:36](https://www.youtube.com/watch?v=AZq1acbjaz4&t=2436s): I think it's that some of the Basu nodes were running on a resource-constrained machine and that 
caused them to go offline. I don't know, is Justin correct? I am going to try and  on youtube yeah .

**Justin Florentine** [40:53](https://www.youtube.com/watch?v=AZq1acbjaz4&t=2453s): okay say again

**Tim Beiko** [40:54](https://www.youtube.com/watch?v=AZq1acbjaz4&t=2454s):  Was it basically that had some issues during the Goerli merge just because some of the nodes were running on. In short instances with two small resources.

**Justin Florentine** [41:05](https://www.youtube.com/watch?v=AZq1acbjaz4&t=2465s):   Not this time, that was a problem in prior shadow forks.

**Tim Beiko**[41:13](https://www.youtube.com/watch?v=AZq1acbjaz4&t=2473s):   Really okay I don't know. Maybe Pari do you know?

**Parithosh Jayanthi**[41:19](https://www.youtube.com/watch?v=AZq1acbjaz4&t=2479s): I also have to check. I am not sure which client it is anymore.

**Tim Beiko** [41:31](https://www.youtube.com/watch?v=AZq1acbjaz4&t=2491s): But yeah short answer is I think this happened on Goerli as well but then the situation is just you give them more resources and the clients were fine.

**Parithosh Jayanthi** [41:42](https://www.youtube.com/watch?v=AZq1acbjaz4&t=2502s): Also resource use tends to spike quite a bit during non-finality and at least on Goerli that period was just a couple of epochs after the merge and once we hit finality again resource use did does decrease quite a bit. So even with the previous notes I think I don't even think they had to upgrade but I think it sort of fixed itself once finality had been reached.

**Trent** [42:25](https://www.youtube.com/watch?v=AZq1acbjaz4&t=2565s): Any other questions?  Now's the time to get him in if you were waiting until a quiet moment and one last offer for any client, any client types or researchers who are on the call and you want to mention something that wasn't touched on before. Feel free to raise your hand if you'd like to talk about your client anything specific that people should be aware of. Any resources that you can offer to people things like that. Okay go ahead.

**Tim Beiko** [43:18](https://www.youtube.com/watch?v=AZq1acbjaz4&t=2598s):  I was just gonna say it's not because there's there's like been a couple questions about like estimating
the ttd and what not and maybe I will just  add a last amount of nuance there. The reason you know you could imagine a world where we just have Bellatrix happen and then we decide the ttd right and this is what we did on a couple of the testaments. The challenge with doing that is just that you have to get people to upgrade their notes twice and because this is already like a pretty complete complicated upgrade relative to other ones. We opted optimistically to like optimistically have people only need their nodes to be updated once and to kind of bake in a ttd estimate for that. Usually when we ask people to upgrade their nodes we think the order of about two weeks is reasonable, so we put out the software and put out an announcement then within two weeks usually we can get the community to upgrade their nodes. So if we kind of hit Bellatrix and we see it's gonna be way more than two weeks to hit ttd.  Then it probably makes sense to coordinate another ttd and have it lower and have people upgrade their notes again but this is  why there's so much uncertainty or yeah wide estimates around it. It's just because we need to predict. But yeah it's just we need to predict this value that's really far up in the future that has  a lot of unknowns that go into it. But if  we take kind of our best guess for it , if we see that this best guess is wildly off then we can correct it and the only downside is people need to re-upgrade their nodes or run an additional command and this is what we'd like to avoid in  the happy case. But  it's definitely not the end of the world to have to do it and we've done it. On Robsten and for users it's basically either downloading one new version of their clients or running one extra command on it while it's going live and then there's a question about issuance. So issuance is basically based on the total number of validators on the network so if there's more validators .The total issuance goes up but then the kind of rewards to the validators proportional to their stakes go down and that kind of targets a specific amount of validators. Yeah so it's confirmed that it is part of this spec but it's not confirmed in that we don't know how many new validators might want to validate after the merge and that impacts issuance and I think ultrasound.money. I believe has like a  nice little graph that you can tweak to see. Yeah based on how many validators and what not.

**Trent** [46:29](https://www.youtube.com/watch?v=AZq1acbjaz4&t=2789s): Oh nice. Yeah I didn't realise they had an adjustable graph. This is great. All right, it looks like we're actually out of questions now. Besides some ttd panda ideas but I don't know if we're gonna be able to include that Micah is sad for some reason. He would love to keep answering questions but I think we can probably wrap up here. I have done the last call three or four times now. Tim anything else?

**Tim Beiko** [47:19](https://www.youtube.com/watch?v=AZq1acbjaz4&t=2839s): No yeah thanks everyone for showing up. Well we'll oh we do you want to give the date for the next one because we've scheduled one more of these before the merge. If I am remembering correctly

**Trent** [47:30](https://www.youtube.com/watch?v=AZq1acbjaz4&t=2850s):  I think we were going to plan for it. let's see wednesday the 7th of september does that sound right.

**Tim Beiko** [47:41](https://www.youtube.com/watch?v=AZq1acbjaz4&t=2861s): 
Actually yeah there's oh yes so we said we wanted to do after bellatrix and before mainnet. Right so that there will be more steak events before bellatrix. We can encourage people to watch those  but then between Bellatrix and mainnet, we will do another one of these. 

**Trent** [48:04](https://www.youtube.com/watch?v=AZq1acbjaz4&t=2884s): So maybe that's the ninth thing

**Tim Beiko** [48:07](https://www.youtube.com/watch?v=AZq1acbjaz4&t=2887s): Yeah tentatively say september 9th at this time So four weeks from now exactly. Yeah that will be if you're interested in attending that. It'll be in the same spot as a pr in the the ethereum pm repo with an agenda and  in 10 minutes if you're a validator remember that there's an east stalker call workshop happening in 10 minutes and where Remy where's the best place for people to jump into that maybe you can share the link again or direct them a certain place. If you already left. I don't know where I would point you but the e-sticker discord probably is the best place.

**Tim Beiko** [48:58](https://www.youtube.com/watch?v=AZq1acbjaz4&t=2938s): Somebody just posted the youtube link again.

 **Trent** [49:01](https://www.youtube.com/watch?v=AZq1acbjaz4&t=2941s): Yeah oh perfect 

**Tim Beiko** [49:06](https://www.youtube.com/watch?v=AZq1acbjaz4&t=2946s): Yeah so take your youtube channel go ahead that's it. The youtube link there by ethstaker workshop.

**Trent** [49:13](https://www.youtube.com/watch?v=AZq1acbjaz4&t=2953s): One last question yeah i don't know if we can explain replay attacks but I am not gonna get into like how to financially profit from this  upgrade replay attack is when you send a transaction on one chain and it can be replayed on a chain that's similar but not exactly the same as the one that you sent the original transaction so aside from that yeah.

**Tim Beiko** [49:55](https://www.youtube.com/watch?v=AZq1acbjaz4&t=2995s): Okay yeah I think we got it.  Thanks everyone for showing up and yes you in about a month for the next one of these .

**Trent** [50:05](https://www.youtube.com/watch?v=AZq1acbjaz4&t=3005s): All right thank you again to the client devs and researchers who showed up and answered questions. I really appreciate you spending time on this so yeah we'll see everybody in a month or in the discord or elsewhere bye

----------------------------------------------------------------
## Attendance

* Trenton Van Epps  
* Thorsten Behrens
* Phil Ngo 
* Tim Beiko 
* Remy Roy
* Terence Tsao
* Marius VanDer Wijden
* Pooja Ranjan
* Parithosh
* Danny

## Next Meeting Date/Time : Sept 9 at 14:00 UTC (10:00 ET)

- 00:03:27	Wolf Prv BTC to ETH Maxi:	I can't hear anybody
- 00:03:48	Pooja Ranjan:	we can hear
- 00:03:48	Robin A. Nordnes:	sound is good
- 00:03:48	Wolf Prv BTC to ETH Maxi:	is anybody talking?
- 00:03:49	Pooja Ranjan:	well
- 00:03:50	Flibbr ETH Maxi:	Sound is good
- 00:03:51	Oleg Boiko:	Sound good
- 00:03:51	Theodore Degiuli:	sound is clear
- 00:03:53	Wolf Prv BTC to ETH Maxi:	ok its me t hanks
- 00:03:54	Philipp Schindler:	sound is good
- 00:03:56	Trent:	wolf it's on your end
- 00:03:59	Forrest:	I can hear
- 00:04:02	moon:	yes I can hear clearly
- 00:04:02	Wolf Prv BTC to ETH Maxi:	thanks
- 00:04:16	Flibbr ETH Maxi:	Wolf sucks get out of here
- 00:04:27	into_the_network:	hello
- 00:04:32	Flibbr ETH Maxi:	Lol jk
- 00:04:33	Trent:	was there a written goerli retro?
- 00:04:36	danny:	https://blog.ethereum.org/2022/08/12/finalized-no-36/
- 00:04:51	terence(prysmaticlabs):	https://notes.ethereum.org/@parithosh/goerli-merge
- 00:05:12	Trent:	thanks Terence!
- 00:05:20	Wolf Prv BTC to ETH Maxi:	thanks I got it now (audio)
- 00:05:55	@whalepool flibbr eth maxi:	Finally. Are you sure you are competent enough to upgrade your node? @wolf
- 00:06:15	@whalepool flibbr eth maxi:	Oh you don’t run a node you say @wolf lol
- 00:07:15	Trent:	https://bordel.wtf/
- 00:07:39	Trent:	this is the TTD tracker ^
- 00:08:30	@whalepool flibbr eth maxi:	Anyone wants to open a bitcoin LN channel with me?
- 00:08:52	Trent:	@whalepool please stay on topic
- 00:10:56	Chengzhi Li:	Questions: What were the problems encountered when merging the testnets? how likely it is for a successful mainnet merge?
- 00:11:38	Tim Beiko:	@Changzhi: https://notes.ethereum.org/@parithosh/goerli-merge
- 00:11:47	Sridaran Raguraman:	any issues post goerli/prater merge ??
- 00:11:59	Parithosh Jayanthi:	https://notes.ethereum.org/@launchpad/merge-configuration-checklist
- 00:12:09	Chengzhi Li:	@Tim: Thank you!
- 00:12:43	terence(prysmaticlabs):	@Sridaran. Goerli is fairly stable now
- 00:13:46	Tim Beiko:	step-by-step merge checklist similar to Pari’s doc linked above: https://launchpad.ethereum.org/en/merge-readiness
- 00:14:28	Oleg Boiko:	Greetings! Looks like TTD sabotage might sound too attractive for PoW supporters. Can you tell more about this override procedure? Is it some kind of software update?
- 00:15:09	Pooja Ranjan:	will add them in notes
- 00:15:18	terence(prysmaticlabs):	Prysm checklist: https://docs.prylabs.network/docs/prepare-for-merge
- 00:15:45	Chengzhi Li:	Question: What is the backup plan in case mainnet merge fails or some series issues happen? Go back to POW temporarily and wait for everything is fixed?
- 00:16:32	Tim Beiko:	https://blog.ethereum.org/2022/06/03/ropsten-merge-ttd/
- 00:17:07	luzian:	Question: Could you explain what exactly is the meaning of the  “Effectiveness" on beaconcha.in and why it went down since the merge? (The latter might be a personal problem of my valiator though, not sure about that)
- 00:19:32	Oleg Boiko:	Thanks Tim!
- 00:19:54	danny:	cross the rubicon
- 00:20:00	flibbr:	indeed
- 00:20:19	Caleb Lau:	Are there plans to allow for a single CL multiple EL configuration without a muxer in the future?
- 00:20:43	flibbr:	fix it in production
- 00:20:46	Rémy Roy:	Here is a good resource on "Effectiveness": https://www.attestant.io/posts/defining-attestation-effectiveness/ . On testnets it's common to see wild effectiveness variance.
- 00:21:00	Rémy Roy:	I'm muted
- 00:21:39	luzian:	Yep, on Goerli
- 00:22:10	BTH:	Will disk usage increase faster after the merge? Or can I assume about the same size/increase as before the merge (summing up usage of CL and EL client)?
- 00:22:56	luzian:	Got it, thanks! I'll read more about it on that link.
- 00:23:39	terence(prysmaticlabs):	Micro
- 00:23:44	terence(prysmaticlabs):	micdao
- 00:23:47	Tim Beiko:	amen
- 00:23:51	Micah Zoltu:	MicDAO
- 00:24:19	flibbr:	danny's mic is terrible just fwiw
- 00:24:28	Trent:	yes we told him
- 00:24:37	danny:	he knows
- 00:24:49	danny:	he sent the good mic to terence
- 00:25:01	Trent:	lolol one mic to pass around
- 00:25:27	flibbr:	Terence needs a 'pop' filter also on his mic, not nit picking
- 00:25:31	Tim Beiko:	lol
- 00:25:57	Trent:	any other questions, please submit them here!
- 00:26:12	eliekfouri.eth:	my Nethermind+lighthouses node , after Merge EL started to reorg block
- 00:26:59	Rémy Roy:	Some details about the Nethermind issue can be found on https://notes.ethereum.org/@parithosh/goerli-merge
- 00:27:06	eliekfouri.eth:	had to restart both El + CL , and back to normal
- 00:27:28	Parithosh Jayanthi:	they already have a fix 😄
- 00:27:42	eliekfouri.eth:	👍
- 00:28:32	flibbr:	thanks Remy
- 00:28:46	Pooja Ranjan:	https://www.youtube.com/watch?v=7Vn4xCDCXII
- 00:28:59	Pooja Ranjan:	Ethstaker workshop
- 00:29:16	Chengzhi Li:	Another workshop is great! thank you!
- 00:29:30	luzian:	Another question: is there any way to find out if my mev-boost config is working other than just to wait for me to be selected to propose a block?
- 00:29:39	Rémy Roy:	https://ethstaker.cc/ethstaker-validator-workshop/ for all the workshop details
- 00:29:46	flibbr:	yeah honestly really quiet considering this is announced merge right now
- 00:30:09	terence(prysmaticlabs):	One sec
- 00:30:35	Rémy Roy:	This is the workshop that is happening in about 30 minutes: https://ethstaker.cc/ethstaker-validator-workshop-3/
- 00:30:53	lightclient:	When should we stop running tipima?
- 00:31:41	Trent:	don't take the bait
- 00:31:53	Tim Beiko:	blocked and reported
- 00:32:21	luzian:	Great, thank you! I was just afraid of the possibility of missing the opportunity to propose beacuase of a potential mev-problem.
- 00:32:36	Tim Beiko:	I also pinged FB to ask them to clarify this in their docs :-)
- 00:32:43	eliekfouri.eth:	opinion: gap between Bellatrix and TTD should  be much wider than 7 to 10 days. As a solo node operator.
- 00:32:44	terence(prysmaticlabs):	All the clients will build a local blocks in parallel so missing blocks is highly likely unless they withhold
- 00:32:54	Micah Zoltu:	I think we should reiterate again that TTD isn't final yet!
- 00:32:56	Micah Zoltu:	It is tentative.
- 00:33:25	Micah Zoltu:	You don't need to configure before bellatrix unless you are a validator.
- 00:33:33	Trent:	yup agree micah - please everyone stay tuned incase there is an override
- 00:33:44	eliekfouri.eth:	"Ready for Merge" message logs on Lighthouse is very nice
- 00:33:57	AKS:	Hi, if miners turn off their nodes much before ttd target, will network security of pow eth chain be compromised ?
- 00:34:14	eliekfouri.eth:	and should me a similar message on EL logs too
- 00:34:22	Micah Zoltu:	Things will slow down, but the security profile is still largely the same.
- 00:35:21	Tom:	What roadblocks are in place to prevent a competing POW chain?
- 00:35:26	Trent:	none
- 00:35:47	Micah Zoltu:	None.  If people want Ethereum Classic v2 they can have that, though I recommend just using Ethereum Classic as it is great.
- 00:35:54	AKS:	Thank you. Any plans for eth foundation filling in the gap of missing miners
- 00:36:08	eliekfouri.eth:	I thought that" Ready for Merge" message just after Bellatrix upgrade
- 00:36:43	ßuß:	What happens if multiple miners find a block passing TTD at the same time? (sorry if this question has been asked before)
- 00:37:28	Justin Florentine:	thats kinda what happened with Goerli, re-orgs can still happen around them
- 00:38:26	AKS:	One last question on stablecoins, usdt, how the migration plan will look like , if i have usdt now, i will have usdt after merge as well, right?
- 00:38:33	flibbr:	^ this
- 00:39:26	Micah Zoltu:	The situation is the same as every other network upgrade.  The Merge isn't special in this regard.
- 00:39:42	Micah Zoltu:	*allegedly* backed by actual dollars.  😆
- 00:39:42	ßuß:	thanks for the response btw (regarding potential multiple terminal blocks)
- 00:39:52	Caleb Lau:	And you don't need to give out your private keys, sign any messages, etc, to migrate your coin over to PoS.
- 00:40:33	Damien:	Re ttd, does the estimate that 5875 would be reached around 9/15 depend on hashrate staying at current levels? shouldn't best guess be that hash rate will drop and 5875 would actually be reached later than 9/15, so if we actually want to reach ttd on 9/15 it would need to be set lower?
- 00:40:40	Trent:	excellent point caleb!
- 00:41:00	AKS:	Ahh good point, in time of chaos scammers hunt
- 00:41:03	AKS:	thank you thank you. You guys are great!
- 00:42:11	Damien:	Understood, thanks
- 00:42:23	luzian:	What's the deal with all the pandas? 🙂
- 00:42:44	eliekfouri.eth:	if Bellatrix deployed tomorrow there is no risk to TTD happens before it
- 00:42:47	Sridaran Raguraman:	🐼
- 00:42:49	Francis Corvino:	tldr of georli situation / resource constraints on clients?
- 00:42:49	Parithosh Jayanthi:	https://twitter.com/icebearhww/status/1431970802040127498
- 00:42:55	flibbr:	🐼
- 00:42:55	Justin Florentine:	polar bear + black bear
- 00:43:09	luzian:	🤣
- 00:43:36	Justin Florentine:	nft that tweet, historical artifact right there
- 00:43:39	Francis Corvino:	^tim - & thank you for doc
- 00:44:44	Tim Beiko:	eliekfouri.eth: that's correct. but we can't make bellatrix happen tomorrow because we need to have client releases out, give people time to upgrade, etc.
- 00:44:44	into_the_network:	so the best estimate is after 6th (Bellatrix) - 15 sept latest
- 00:44:50	Rémy Roy:	There are some details about Besu on the Goerli Merge issue notes: https://notes.ethereum.org/@parithosh/goerli-merge
- 00:45:00	Tim Beiko:	My range is roughly Sept 7-22 for TTD
- 00:45:13	Tim Beiko:	if we were going outside of that, on either side, I think we should consider an override
- 00:45:16	Francis Corvino:	thanks everyone
- 00:45:43	into_the_network:	thank you Mr Tim
- 00:46:00	Parithosh Jayanthi:	If your node has like <10% free disk space, probably a good idea to upgrade to a bigger disk right now 🙂
- 00:46:06	Parithosh Jayanthi:	there’s still plenty of time to resync
- 00:46:41	ßuß:	Considering the 5-7 bytes with low significance in the TTD value, is there a cool word or smth we could encode in there? (Similar to Bitcoin's genesis block message)
- 00:46:58	Rémy Roy:	If you have less than a 2 TB SSD, you might want to upgrade that disk early.
- 00:48:13	OC:	Is there any confirmed rate of issuance for validators based on the total staked ETH securing the network post-merge?
- 00:48:19	Justin Florentine:	or run clients that have intrinsic pruning, like Besu's bonsai mode.  SHILL MODE ACTIVATED
- 00:48:34	Trent:	very good Justin =)
- 00:49:03	Trent:	issuance is variable based on number of validators
- 00:49:09	Rémy Roy:	https://ultrasound.money/
- 00:49:23	Owen:	Thank you
- 00:49:31	ßuß:	As an example TTD of 58749999946366984675699 would have "pandas" encoded in the end while being 99.99% the same value 
- 00:49:43	Tim Beiko:	lol
- 00:49:46	Micah Zoltu:	😢
- 00:49:50	Tim Beiko:	having a lot of lagging 0s is easier to check
- 00:50:09	Micah Zoltu:	I'm sad that we missed the panda TTD.
- 00:50:27	Sileo:	🐼
- 00:50:38	ßuß:	58750030344637972046959 has "tornado" at the end
- 00:50:58	Micah Zoltu:	Perhaps TornadoPanda?
- 00:51:03	Rémy Roy:	Thanks everyone. Get ready for the merge.
- 00:51:08	Sridaran Raguraman:	🐼🐼🐼🐼🐼,      🔊🔊🦇🦇🦇🦇
- 00:51:08	Sridaran Raguraman:	🐼🐼🐼🐼🐼,      🔊🔊🦇🦇🦇🦇
- 00:51:08	Sridaran Raguraman:	🐼🐼🐼🐼🐼,      🔊🔊🦇🦇🦇🦇
- 00:51:08	Sridaran Raguraman:	🐼🐼🐼🐼🐼,      🔊🔊🦇🦇🦇🦇
- 00:51:08	Sridaran Raguraman:	🐼🐼🐼🐼🐼,      🔊🔊🦇🦇🦇🦇
- 00:51:11	into_the_network:	thank you so much
- 00:51:15	into_the_network:	we appreciate you guys
- 00:51:19	Basti:	Thanks, you guys do amazing work! So happy to see this historic event in real time..
- 00:51:45	BTH:	https://www.youtube.com/watch?v=7Vn4xCDCXII
- 00:51:46	Christina Kirsch:	🙏thank you
- 00:51:47	fatcrypto:	Hey, can someone explain replay attacks. Specifically if I wanted to liqudate my NFTs on ethPoW, to get ethPoW, to try and exchange it on a CEX, for ethPoS
- 00:51:48	ßuß:	"TornadoPanda" too long unfortunately, only 6-8 bytes would fit without significantly affecting TTD I think
- 00:51:57	Ridgerunners:	You guys are amazing. Thanks for all your hard work!
- 00:52:18	Sileo:	Thanks for everyone's work !
- 00:52:47	Sridaran Raguraman:	🐼
- 00:52:48	Synthex Moon:	Thanks a lot !
- 00:52:58	Pooja Ranjan:	Thanks everyone!
- 00:53:12	Troy Amyett:	Thanks!
- 00:53:14	Basti:	🐼


