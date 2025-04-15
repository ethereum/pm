# Consensus Layer Meeting 125 [2024-1-11]
### Meeting Date/Time: Thursday 2024/1/11 at 14:00 UTC
### Meeting Duration: 40 Mins
#### Moderator: Danny
###  [GitHub Agenda](https://github.com/ethereum/pm/issues/936)

### [Audio Video of the Meeting](https://www.youtube.com/watch?v=YkHtTudq3Xo) 
### Meeting Notes: Meenakshi Singh


**Danny** [6:35](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=395s): All right we should be live welcome to All Core dev's Consensus Layer call 125. This is issue 936 in the PM repo. General Deneb discussion a bit of a discussion around a Fork Choice filtering change that's been brought up as to whether should go in or not. And then a couple of
other spec items. So we can go ahead and get started. Okay cool. So generally we have a testnet fork Goerli fork in Six Days. There is the blog post out which I believe has releases for all the expected clients which is exciting as we approach that. Do we have any discussion items in relation to that testnet in relation to existing Devnets, in relation to testing. 


### Deneb testnets/testing/etc

**Paritosh** [8:01](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=481s): Yeah maybe I can go first. We have a Goerli Shadow fork that was launched like an hour ago or so. It's based off the versions from the EOF blog post so it's kind of like a sanity check that everything would go as planned. And it did. The only note that seems offline is Teku Besu note but I'm 99% sure that's my fault. I think I used the wrong flag while starting it up and we'll look into getting on the right chain. And otherwise I think there's nothing to note there we've already started spamming blobs and blobs seem to be propagated fine. And yeah if you guys have something specific you want to test on there let us know. And then we'll carry it out for you.

**Danny** [8:50](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=530s): Great. Yeah any questions for Pari? Do the Explorer looking really good over here? Yeah cool anything else in relation to testing or the upcoming Goerli Fork? Okay keep moving forward let's see okay Phil added the fork Choice filtering change PR to discuss on whether this is being shipped in the upcoming Fork. Does any anybody Feel to have any context here to add? 


**Mikhail Kalinin** [10:04](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=604s): yeah I can speak on that. So what was previous decided is that we are rolling out this change within the Deneb and doing it in a Loosely coordinated fashion. So basically this change should be enabled in the mainnet releases lines mainnet releases including the Deneb for keep for the mainnet and from my perspective there are two ways to do that is one is that just merging the change before making the release. So it appears in this release only the other one is like enable  this logic conditionally based on the whether the for has set or not..  I believe the former is preferable by that's the context that what was started like a while ago. When we were speaking about how we want to roll out this change. And also one thing worth noting here is that probably some of confusion about this Change is coming from that the PR that proposes this change has been yet merged. But we decided to set the Deneb for the mainnet and merge the PR after that only.


**Danny** [11:43](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=703s): Sorry your last comment was in relation to which PR? 

**Mikhail Kalinin** [11:47](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=707s): The PR that proposes this Fork Choice change that is required for confirmation rule. It's not yet merged into this stack and some client devs were saying that they haven't started to implement it. Because of the PR was not mer but we decided not to merge the PR until the mainnet, epoch is set for Deneb. 


**Danny** [12:14](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=734s): Right. Thank you for the background here. I'm kind of leaning towards now that we're in the launch sequence that it's probably time to merge it. As a signal is there actually value in waiting for the Deneb. Epoch to be included because that ends up probably on a three-week Time Horizon. And I know that we decided to not do the conditional forking or the conditional logic here. One for Simplicity and two well Simplicity of spec as well as Simplicity of testing. And so we won't be doing kind of this conditional test. So I think that most clients are not going to do a conditional logic update. And so given that we're not conditioning this upon anything other than just getting it out and releases soon. So what do you think? Do you think we should wait until we have the neck or just go for it?

**Mikhail Kalinin** [13:27](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=807s):  I personally don't see any problems with merge PR right now. And it's actually preferable to me but maybe other people have opinions on that.So I merged it and yeah in the next release we'll get test factors incorporate in this change we already have them but they are attached in the comment to the PR which probably not that handy.

**Sean** [13:58](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=838s): I would support merging it as well. 

**Danny** [14:05](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=845s): Anybody against merging this week and having it available as a release very soon and to be the target. It'll be the assumed Target of any further Devnets and Mainnet. Great and if I remember correctly I kind of tagged it. I said this is the substantive change it's there are a number of I think minor helper changes just in terms of being able to reuse logic but it's really this one line or voting source. Epoch plus 2 is greater than equal to the current
Epoch. Okay anything else on this one we'll aim to do a release by Monday. Great yeah thanks for catching this glad. 

### Research, spec, etc
#### Derive OpenAPI type schema from pyspec beacon-APIs#402

**Danny** [15:42](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=942s): I didn't still through the cracks. Okay next up is from Dapplion deriving an open API type schema from the pyspec now that we do have the canonical Json mapping. Dapplion? 


**Dapplion** [15:56](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=956s): Yeah hey  everyone so now that we have a canonical mapping from SSZ to JSON. We can drop a lot of builder plate on the beacon APIs. So I wrote a short python script that converts the pyspec into the types that are needed for the API plus we can also Define the extra types that are SSZ is as SSZ instead of the classic open API. So in my opinion it looks much cleaner it's wayless code for now it's not critically important but for future Forks it should alleviate a lot of Maintenance. And we can easily SSZ everything if we want to later which is an idea that has been floating around for a while and this would make it very easy. I'm bringing this up because it's a change on how the repo would work. So I would like to make sure that there is no one opposed in working with SSZ instead of open API. Or if we would lose some sort of exclusivity that someone finds important with this approach. So with the information that is available right now is anyone strongly opposed into dropping all that open API builder plate and just dealing with SSZ
Exclusively. Okay. Awesome. Then if you can please take a look at the issue it's a decent change it's a chunky PR. So I would work with involved maintainers to try to make the transition as smooth as possible making sure that nothing is broken. So that's all thanks.


**Danny** [18:12](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1092s): And this assumes a merge of 3506.

**Dapplion** [18:20](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1100s): Yes.

**Danny** [18:22](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1102s): Which I think we've discussed quite a bit. And just didn't click the
Button. 

**Dapplion**[18:28](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1108s): Yeah so now is a good time.

**Danny** [18:32](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1112s): Great 

**Arnetheduck** [18:42](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1122s): I think I might be the winner of the longest time open PR that actually gets merged competition. 

**Danny** [18:53](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1133s): There are some PRs open up from even older than this we can go look at them see be record.

**Arnetheduck** [19:03](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1143s): I'll just make up some shape. So they don't get merged.

### Modify long-lived attestation subnet calculation to allow pre-determined calculation #3545

**Danny** [19:14](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1154s): Great thanks Dapplion. Thanks Yasim. Okay and finally pop wanted to bring up PR 3545 which was
a proposal from age to modify the long lived standing attestation subnet to utilize. I believe prefix bits instead of the entire note ID. Pop or Age or anyone that wants to give some more context on this.

**Pop** [19:59](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1199s): Yeah. I think this PR is about using the Prefix instead of the suffix to determine the subnet that the node are supposed to subscribe to. I think it's good idea because clearly the entire node ID is used to determine the subnet. But that is a problem. Because when you want to find the node that I subscribe to the subnet you have to go to the discv5 and then and then do a random walk to 2 to 5 the node that are subscribed to the subnet but if you use only the prefix you can just use that prefix instead of the entire node ID. And it will be faster in the kademlia DHT. I think that is the Objective yeah.

**Danny** [20:59](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1259s): Does the current logic use the suffix or does it just use the entire node ID?


**Pop** [21:04](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1264s): It use a suffix like some some some bit of suffix but I think it make more sense to use only the Prefix. 

**Danny** [21:14](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1274s): I see so this doesn't change the grindability right because it would utilize the same amount of the prefix as the suffix apparently. Like if an attacker we're trying to grind node IDs to take over like a subnet this doesn't change that calculation does it?


**Pop** [21:37](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1297s): I think it doesn't change because you cannot prevent the attacker to generate a lot of node ID. It's doesn't matter you use the prefix or suffix that is what I think. Yeah.

**Danny** [21:52](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1312s): Okay.


**Arnetheduck** [21:54](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1314s): I think there is one downside actually which is that if you search that kademlia  by prefix you will not find the Subscribe all subnets nodes that subscribe to these subnets regardless. So you're kind of limiting your search to one whatever it is 6435 seconds of all nodes out there.

**Danny** [22:21](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1341s): But couldn't you do that search as well?

**Arnetheduck** [22:25](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1345s): You can but like you know if the reason we're doing the prefix is so that you don't search the whole Kademlia and everybody goes on to change. So that we don't do it then you could but you don't. 

**Danny** [22:41](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1361s): Sure I guess I see you can have like Fast lookups on the kind of honesty assumption here but you also if you're heuristic. It can also walk on whatever speed it wants to find the other type but I don't know, I mean there's two things there it's like one purposely populating but those peers still do exist. So they still will exist even if nobody's looking for them and provide additional utility. So I don't know I get the argument. I don't know how strong I'd claim the argument. 

**Arnetheduck** [23:22](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1402s): Neither do I? It's an observable change though.

**Dany** [23:26](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1406s): I mean it also is an observable change in that it's a breaking change and you would very likely have to condition this upon a fork or have some sort of transition period or something you can't just like put this out and slowly upgrade which is a downside. I guess, I don't have much fundamental opposition here. And I would presume most people don't but I think the conversation needs to happen in this PR is actually how the upgrade would look like. And given that we're coming up against the deneb if this needs to be upgraded at a fork boundary. I would presume that it wouldn't go into Deneb at this point.  But nonetheless I think we do need to have the conversation about how this upgrade could occur in that PR are we comfortable bringing that question to the PR and hashing it out there. Or do Is there further discussion for this Call?

**Arnetheduck** [24:46](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1486s): I'll make a comment on the PR but like what I just said doesn't isn't the blocker for the PR. It comes after right like having nodes already do this that doesn't change anything. It's the change in behavior in Kademlia lookups in clients that  is potentially weird.

**Danny** [25:07](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1507s): Yeah but I do think that independently like how you actually upgrade this in a live network has to be discussed in this PR.


**Pop** [25:16](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1516s): Yes I think yeah I agree.

**Danny** [25:21](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1521s): Okay Pop can you either pose that question or pose an upgrade path in there. We can further discussion there.

**Pop** [25:29](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1529s): Sure.

### Open Discussion/Closing Remarks


**Danny** [25:31](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1531s): Okay thank you. Okay that is everything that is on the current agenda. I know there's beginning to be discussions as to what we do next. Personally would probably get us a little bit further into the fork before we hash out all individual proposals but if people would like to open up for discussion broadly about the framing of the fork kind of if there's a big thing what the priorities kind of feel like by all means we can have we can begin this conversation. I'm also okay with you know having a bit more of a structured conversation next time.  I didn't  give you much to bite into there but I can come in two weeks if no one's opposed and give a bit more to bite into to begin the conversation. Anyone opposed to beginning this conversation in the next on the next call.


**Stokes** [27:13](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1633s): Not oppose but I have a question where is there a place we could in the meantime you know discuss async things for the CL.

**Danny** [27:23](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1643s): There is an open issue on the consensus specs repo where we have been Gathering a list of EIPs which right after this call. I can kind of go through and make sure that it is reasonably up to date. I think there's one more comment since I last looked right. So EIP 7549 okay so it is this issue 3449. So I either cataloging the information here there also is a magician thread that is open that does have some dialogue. Ansgar? 

**Ansgar** [28:09](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1689s): Yeah I didn't want to kind of get too much into the discussion already. I just wanted to flag that this year we might be in a somewhat unusual situation especially on the on the CL side in terms of kind of for what features going forward where there is this work on the data availability sampling side. That it very much has the nature of of a feature that usually would be part would be an EIP or something but just because of the way we structured for does not actually require a hard fork or an attached EIP and I think with that comes the risk of it maybe not having quite the same visibility where like maybe we start collecting APIs for the next Fork. And then we basically say now we have so many things to do. So we can't focus too much on data availability sampling anymore where that's kind of backwards. Because that would kind of because to me data available , something really is kind of the highest priority thing to do. So just wanted to flag already going conversations that yeah just because it's not an EIP we don't. 

**Danny** [29:09](https://www.youtube.com/watch?v=YkHtTudq3Xo&t=1749s): I'm not certain why it wouldn't be an EIP. We had this conversation a bit the other day on some of us that have been working on the peer D spec. And I think it should manifest  as an EIP it did. It is newly in an open PR on the consensus specs repo as of some amount of hours ago and I think the intent is to couple it with any EIP even it's kind of work in progress status.  Sean, did you want to go over some of that or at least signal that it exists. Okay well there's the draft and the intention is to while we're getting the draft open to also get an EIP open in relation to it. As noted in the chat if you did modify the data gas limit it is a hard Fork consensus change. If you don't you could imagine a pure networking change it does beg the question as to why you're doing it? I guess you could make an argument for upgrading to the modified networking before updating the gas limit. But I imagine we would be having those conversations in sequence but yeah the intention would be to make this an EIP regardless of how the upgrade path Is and we should have an EIP number for it for discussion by the two we count From here. Yes so that issue on the spec repo where we have cataloged things that people do want to bring up for discussion if you do have additional EIPs please get them there soon.Conversation can obviously occur dynamically in the Discord or more async in that magician's thread if they're technical items to touch on maybe put it in the consensus specs. But we don't have like a 100% perfect division on where to have these Conversations. All right yeah check out that PDS spec draft especially if you're on the networking side of things on your client relatively simple relatively straightforward. Any other discussion points for today? Let's go with Devnet zero after didn't that hard fork. Okay cool appreciate it thank you. Please get your thoughts organized around how you and your team are thinking about proceeding from here in terms of priorities. And upgrades and we will pick up the conversation in two weeks. Thanks everyone. Bye.

## Attendees

* Danny
* KaydenML
* Kolby Moroz Liebl
* Barnabas Busa
* Frank Chal
* Lightclient
* Nishant
* Maintainer.eth
* Stokes
* Paritosh
* MauriusVan DerWijden
* Spencer-tb
* Ben Edignton
* Mikail Kalinin
* Trent
* Terence
* Mario Vega
* Toni Wahrstaetter
* Ansgar Dietrichs 
* Joshua Rudolff
* Pk910
* Gajinder
* Gary
* Enrico
* Carl Beekhuizen
* Saulius Grigaitis
* Justin Traglia
* David
* Pop
* Lusakz
* Arnetheduck
* Tim Beiko
* James He
* Lion Dapplion
* Scorbajjo
* Phil NGO
