# AllCoreDevs Meeting 126

### Meeting Date/Time: November 12, 2021, 14:00 UTC
### Duration: 90 minutes
### [Video Recording](https://youtu.be/Kk-kZXazi18)
### [Agenda](https://github.com/ethereum/pm/issues/407)
### Moderator: Tim Beiko
### Notes: George Hervey

## Decisions Made / Action items:
| Decision Item | Description | Video ref |
|---------------|-------------|-----------|
| 126.1 | Further review and async discussion regarding Kintsugi | [49:09](https://youtu.be/Kk-kZXazi18?t=2949) |
| 126.2 | Postpone EIP-4396 to Shanghai upgrade | [1:07:55](https://youtu.be/Kk-kZXazi18?t=4075) |
| 126.3 | Discuss EIP-4444 more in next ACD meeting | [1:32:04](https://youtu.be/Kk-kZXazi18?t=5524) |

## Intro:

Tim Beiko:
Hello everyone. Welcome to AllCoreDevs 126.

A couple things on the agenda today. As mentioned on the consensus layer call last time, we're going to spend some time talking about Kintsugi and the upgrades we have there. And then we have a couple EIPs and things about the merge to discuss, but first just wanted to mention Arrow Glacier.

## Arrow Glacier
*Summary: View transcript below.*

Tim Beiko:
So, the Arrow Glacier upgrade is happening on December 8th. All of the clients have a release ready. I'll just share my screen real quick. There's a blog on blog.ethereum.org with all these releases. Otherwise, in the execution specs repo, there's also a link to the spec with all of the client releases associated with it.

Yeah so you can find them here. There's only a single thing in Arrow Glacier so just difficulty on push back and nothing else going in. So that was the first one.

## Kintsugi 🍵 office hours
*Summary:*
- *Nethermind*
  - *Implemented EIPs and changes in execution engine API.*
  - *Ready to start testing with the consensus client.*
  - *More testing and changes on the way.*
- *Geth*
  - *Created a version with EIP 4399 enabled.*
  - *Need to decide to run on testnets enabled or disabled since it changes it block hash.*
  - *Mario created a tool to create and run test vectors in the execution layer (currently only runs with geth).*
- *Erigon*
  - *Started working on merge but nothing new for now*
  - *Still working on implementing EIP-3675*
- *Besu*
  - *Lot of progress lately but unable to provide much detail*
- *Other*
  - *In-depth discussion of fork identifiers, fork hash and syncing in merge. No decision made though. Further review and discussion will take place asynchronously.*

Tim Beiko:
Next up, Kintsugi. So I'm curious have any clients basically made progress on the specs? Any issues people want to bring up?

Marek Moraczynski:
I can give you an update. So, in Nethermind, we implemented EIPs changes in execution engine api. Of course, we have to do more tests. We have to recheck our sync process and we need to add message ordering. However, even without these changes, we are ready to start testing with consensus clients. What is more, we pass tests with merge mark and test vectors so yeah that is our update from Nethermind.

Nice! Anyone else?

MariusVanDerWijden:
Yeah so from Geth, I created a version with EIP-4399 enabled. We have to decide whether we want to run the first testnet or the testnet on monday with 4399 enabled or disabled because it changes the block hash. So I have one version with 4399 enabled, but I can also create another one without it. I created test vectors for... the test vectors are without 4399 but I can also create test vectors with 4399. And Mario created a really nice tool to run test vectors and to create easy test vectors for the execution layer. Currently, it only runs with geth but we hope to extend it to other clients soon. 

Danny:
Couple things there. The weekly devnet launches which we like to take any gear next week will be on thursday rather than on monday, so there's a little bit of time to coordinate between now and then. And I'd say, if possible, it would be best to just do it full feature unless we have a particular reason not to, but I guess we should circle back on pairing, put a proposal together so that on Monday/Tuesday, we can iron out the last details before Thursday.

Tim Beiko:
Yeah just to confirm, Nethermind, did you guys have 4399 implemented as well?

Marek Moraczynski:
Yes.

Tim Beiko:
Awesome. 

Danny:
Cool and I asked y'all to update if you have done m1 which is just getting implemented, basically implementation and testing together, mark it on the spreadsheet so that people can do a little bit of pairing at the end of next week. 

lightclient:
There is also something raised by Marek on the test vectors as a response for the update forks choice. If there's no execution payload, geth is returning 0x for payload ID. Is that the behavior we're expecting or one thing because the spec seems to imply the null value or not, doesn't exist on the object?

MariusVanDerWijden:
Well what, once again, what's the case when it should be?

lightclient:
If there's no execution of payload, there's no payload id and so I understood it should be known...

MariusVanDerWijden:
oh it's just an error in my code. I can fix it.

lightclient:
Okay.

Mikhail Kalinin:
I'm also wondering what should CL sound when the fork choice is updated when it literally creates the first initiate the build process for the first payload in the network. So what should be the fork choice state that passed on this call?

Danny:
Right. I mean semantically setting the head as a proof of work block might be you know as the fork block you're building on might be the correct thing.

Mikhail Kalinin:
Yes, so yeah that's what we currently need.

MariusVanDerWijden:
Okay because we need the consensus layer to send us the hash that they want to build on. 

Danny:
Yeah which makes sense. I mean if you had two viable competing terminal for fork blocks, the consensus layer needs to pick one and to build one and so that I think should be the way we do it.

Mikhail Kalinin:
Yeah, right. It sounds correct, but I just was wondering because this is something underspecified. It just means that with this call the choice rule will be switched to the proof of stake of choice rule as well.

Danny:
Right, which again, I think makes sense.

Mikhail Kalinin:
Yep agree.

Tim Beiko:
Cool. Anyone from Erigon or Besu have updates?

Andrew Ashikhmin:
Yes, so we have a team member Giulio who has started working on the merge in Erigon, but it's still very much at the beginning. But, I believe Giulio is on the call so he might give us an update if he likes.

giuliorebuffo:
Okay, regarding EIP-4399, I started looking at it yesterday, so I'm still trying to understand how we can implement into aragon, but yeah nothing new for now since the last call.

Tim Beiko:
That's cool. So yeah and you're still basically implementing the EIP-3675 as well i guess, the actual merge EIP?

giuliorebuffo:
Right.

Tim Beiko:
Great. Anyone from Besu? Is there… I don't think we have anyone from Besu on the call...

Fabio Di Fabio:
Yeah I can talk.

Tim Beiko:
Oh yes, sorry I'm trying to scan the grid. Awesome!

Fabio Di Fabio:
Yeah about this, Gary is mainly working on this and I can't add too much. Looking at the issue, there seems to be a lot of progress lately. So, Gary can for sure tell more, but he's not online at the moment.

Tim Beiko:
Okay, no worries. Was there anything else aside from the client updates and the issues we've touched on that people wanted to discuss about Kintsugi?

Danny:
Yeah, I have a quick point about the 3675 spec which was slightly different than amphora and I just want to highlight that. If you take a look at four choice rule in 3675, -- if you look at the first note in italicized -- that's the proof of stake a ps4 choice updated event must be respected even when the transition block of the four choice is not a terminal before block from the view of terminal total difficulty. They're essentially in the consensus layer, although the consensus layer and execution there will both be shipped with terminal total difficulty. But in the consensus layer, there is a potential manual override which can only accelerate the merge, so make a lower terminal total difficulty or set a hard-coded terminal block hash. And because of that, and to avoid complexity of having to do this override in two places and some of the errors that might occur there, it's only on consensus layer. So the consensus layer might have a view where terminal total difficulty might be earlier than what the EL has hard coded and so it the EL must listen to these four choice updated events even in the event that it seems a bit early compared to the terminal total difficulty. 

So, there's no need on the proof of the fork choice rule to validate TTD, but yeah I'll still use local TTD to turn off block gossip and block import for the P2P. And the second thing I linked is a deeper discussion of that design consideration. There was some testing and some different failures and different logic changes around the validation of TTD in EL so I just wanted to point out that the spec says slightly differently than what it did in Amphora.

Question? Okay if you have any questions around this logic change just ping me.

Tim Beiko:
Cool. Any other issues related to Kintsugi that someone wants to bring up?

Mikhail Kalinin:
I want to bring up a small issue. I just dropped it in the chat.

This is the issue to discuss the validation error format which will be used by EL to send the
validation error that happens during the execution of a block or validating the block header.
Initial thought was this is mostly like for ux purposes so the cl client will be able to just log some message if the payload is invalid and it can read from the logs without the need to go to the EL client log and match the payload hash and what has happened. It would be great to see more opinions before making the final decision on how it should be done for more EL client developers. So that's it.

Tim Beiko:
Okay, thanks for sharing. Anyone else?

Okay if not, I think Mikhail it's also worth it to go over your related point about the fork identifiers for the merge before we dive into the two eips we wanted to chat about.

Mikhail Kalinin:
Yeah cool. So we have to specify fork next and fork hash for the merge EIP-4675. And from what we have discussed during our print drop, these numbers and these derivatives should not be affected by the merge. So literally fork next just stay zero. And forkhash is the same as the previous fork. But when it's turned into the spec change, the question of how it should properly be implemented yet again, so I just wanted to just discuss this and make a final decision to make their respective change to the EIP. And my main question here, is if we have the fork hash, -- or let's just suppose the merge has happened and the fork hash hasn't been changed and suppose the proof of work network keeps progressing and considering the fact that the same process and the fork choice rule and everything else will be coming from the CL side to EL and also considering that block gossip will be disabled -- what can go wrong in the worst case if the fork hash of the nodes that run in the proof of stake network will be the same as of the nodes that are running in the proof of work network that keeps progressing?

So that's the main question if my god is that nothing bad can happen. These nodes may exchange with the transaction messages but i don't think it's a problem. We need to decide because we can't update fork hash easily like retroactively or like with how it’s currently specified in the EIP is that the fork hash is going to be updated when the real transition block number is known. But if it's done, it could like split the network for because nodes that are in sync and not yet known, this transition block number, their fork hash, will still be the old one but the nodes who has that has passed the transition will have a new fork hash and they just can't talk to each other. That's the problem.

Danny:
Right. I was just gonna say is this helps filter peers when things are well specified and known in advance and if we don't utilize this mechanism for this upgrade because it is hard to get right and can cause the splitting because of the dynamic nature of the fork block, if i understand correctly, it would only reduce our ability to filter our peers but if we have stable connections and peers we'd probably be in good shape anyway. Is maybe avoiding this mechanism here a potential path so that we don't have to worry about the issues?

Micah Zoltu:
Am I correct understanding that someone who just continues running proof of work and does not switch over to proof of stake, the only network that they're still gossiping on is the transaction network. Is that correct? Like they otherwise don't share any connections. Is that accurate?

Mikhail Kalinin:
Yeah but other methods will still work like blocks. There's no data that works. That stuff.

Danny:
Right. Those more direct requests other than gossip that's still very --

Micah Zoltu:
Well as soon as the first block comes in, you get like your execution layer, well node will say “Hey, I'm not expecting any more blocks. You're bad. I'm disconnecting you”? I guess the first block after the first finality is more accurate. Is that correct?

Danny:
Like somebody's gossiping proof of work blocks beyond.

Mikhail Kalinin:
Right, that's in the spec already.

Micah Zoltu:
Right so the network should split after the first finality. Is that correct? Like everybody should disconnect from each other basically and they'll stop trying to talk to each other and so we should get a nice clean partition at finality that first finality. Is that an accurate statement?

Mikhail Kalinin:
I'd say yes. That's a good point.

Micah Zoltu:
And so if that's true, the duration of this problem is for the time from the fork to first finality. I heard a groan from I think Martin. 

Martin Holst Swende:
It was from me, Martin. I think if all that happens is that one side disconnects the other, that's not the clean disconnect split. It just means that the disconnected partner will try again and succeed to connect and then eventually get kicked out again and it will continue that way.

If we want something clean I think we could integrate this with fork id somehow and I know there's been a discussion about that. Fork ID is usually based on numbers, and after the fork we do know the numbers so we retroactively could modify the fork id in hindsight but during runtime as in not like putting out the new client but the client dynamically modifying.

Mikhail Kalinin:
Yeah right, but according to the EIP --

Danny:
Mikhail, what if we do it at finality instead of once the transition block is known?

Mikhail Kalinin:
I'm worried that according to the spec, the node that has just started to sync with the network and will try to connect to those that have just passed the transition even if they reach the finality and whenever the fork hash has changed, it will be different. And according to the current spec, it should just not connect to this node because it doesn't know it's not... this is a known fork for fork hash or for the node for the local node that connects to the remote one and it just drops the connection.

That's my understanding of the spec. I mean obviously EIP that introduces fork identifiers.

Yeah if you said it retroactively and you're in run time so you can only do this when you know the exact number, right? But, if this number is not known for the local node because it's still syncing and hasn't reached this block, it will use different fork hash and it will need to connect to someone to pull the chain data and get some but it can't connect because the fork hash is different.

Martin Holst Swende:
Yes.

Danny:
So, is that strictly true though that you can't connect if your fork hash is different because the way the fork hash… I need to dig a little bit deeper into the EIP but I believe the way the fork hash is that if your peer doesn't know about a fork that you can still connect to a certain capacity and you wouldn't totally disconnect from them because they may be syncing?

Mikhail Kalinin:
You can recreate the if you can get the same forkhash using the fork next and the upcoming forkhashes then you can connect. If you can't do this, you should disconnect or you must disconnect according to the spec. This is my understanding. It's probably wrong but I've read it several times.

Alex Stokes:
No, I think it reads that way. I think the thinking is that this would have been a fork that happened in your past, and according to your past, it's not something that you respect so then you ignore it.

Micah Zoltu:
Is the expectation with fork ids that all of them are known at startup? Like so when you boot a client, you know all fork IDs that your clients should be able to sync with up to and including the latest.

Someone:
I think so.

Micah Zoltu:
And the issue here, if i understand correctly, is that because this fork doesn't have a known -- sorry, the fork ids are currently based on block number or hash?

Peter Sziilagyi:
Block number.

Micah Zoltu:
Okay so the issue here is normally for every other fork we know the exact block number like from genesis block. If you just start up a client brand new and you have genesis and a config file, you already know the block number for every future fork that up to the download client. And so therefore, you should be able to connect to anybody because you all agree on the fork numbers. The issue here is that we have a fork that we can't hardcode the block number in at least until the client releases after the fork happens and so we're in this weird situation where you don't actually know that from genesis. And therefore when you connect, you don't actually know what block number to say “hey, I'm expecting this for the fork id”. Is that all accurate?

Peter Szilagyi:
Actually, you can't even hard-code it after the fork because if you are good after the fork and for example, I restart my client and I say that okay I did a fork ten blocks ago, and everybody else will drop me from the network because they will see that i'm at block 20 million. I didn't work 1 million blocks ago but they are, again, similarly unlocked 20 million but they did not do a fork one million blocks ago. Essentially, they and I are on two separate forks based on the fork id rules.

Danny:
So we could create a synthetic fork block number where essentially it's like everyone should upgrade their el client to be proof-of-stake capable by this number and this is also the number that it would be using for fork hash and then ttd would be some time after that.

Micah Zoltu:
yeah that way we get the nice clean separation of networks which will basically be people who upgraded to proof of stake and people who didn't, or rather people who upgraded their execution clients to a proof-of-stake capable execution client and those who didn't. And once that block number which is a fork block with essentially no code changes in it. Once that's reached, the network should partition cleanly and then when we get into ttd we don't need to worry about fork IDing. Is that what you're trying to describe, Danny?

Danny:
Yes.

Mikhail Kalinin:
I have a question. This fork identifier, it's also used in discovery, right?

Peter Szilagyi:
Yes.

Mikhail Kalinin:
Okay, yeah we can pick like large block down path that will definitely happen after ttd as well. 

Micah Zoltu:
I think for Danny's idea, we'd want to target before ttd.

Martin Holst Swende:
yeah that was nice.

Tim Beiko:
And I do think there's maybe value in that because it kind of gets people downloading both clients. Like anyways there's going to be a change to the consensus layer before we hit ttd so we can tell people to also upgrade their execution layer clients at that time. And then they're going to have to upgrade their execution clients once more as we get closer, I guess.

Mikhail Kalinin:
And what's the purpose of setting it before ttd? Because if somebody really needs the proof of work network after the merge so it will also include this number as well?

Micah Zoltu:
No, so if you upgrade your execution clients to the client that has the code that says there's a new fork empty fork at this block, then we know that your execution client, assuming you didn't hack it or whatever, will turn itself off when ttd is reached. And so we're confident that you will at least not continue on a proof-of-work network. You will just stop at ttd worst case scenario.

Danny:
A bit funny here with my interest essentially if they intend to not do the fork then we will disconnect from them at this point.

Tim Beiko:
Yeah right, but that's not actually true though because they still have an incentive to mine all the way up to the very last block. They get paid so if they disconnect, then it basically says we're losing this amount of hash rate. And that might actually be a useful data point knowing like
x percent of the hash rate is not even going to bother mining close to the merge.

Micah Zoltu:
That is true, but it's like already there's kind of incentive for miners to leave early because sell your hardware off beforehand. This is just one more incentive like we're basically saying you have to do this last upgrade or if you want to stop a week early, you don't even have to bother
upgrading your infrastructure. Or it'd be nice if we can just say miners don't have to touch their infrastructure. Just keep running your old clients right up until the last minute. You don't need to do anything and that way we retain as much as possible so we don't have a precipitous drop in hashing power at the last minute.

Now I don't know how strong that incentive is. I don't know how difficult upgrading client software is for miners, and you know supposedly there's some mining pools that are going to be switching proof of stake. And so, they'll probably upgrade anyway so maybe it's not a big deal, but it is an incentive.

Tim Beiko:
So I think in practice assuming they want to keep making money. You know some of the miners as you said are mining pools. A lot of them will also use something like flash bots or whatnot. Then if they want to keep making money on mev as well, they need to upgrade. So it feels like if they're gonna drop, if for them the calc for them is like i want to drop before the merge. They're probably going to drop anyway. Martin?

Martin Holst Swende:
Yeah, so I understood one of the drawbacks of having a dynamic fork ID thing is that it makes difficult for nodes that are in the middle of syncing or are wanting to do a sync right around when it hits. But I didn't really understand, Peter, what you said about this being impossible or being the problems that you saw with it and in switching to another fork id.

Peter Szilagyi:
So the entire network simultaneously swaps in a new fork ID, that's fine. But if part of the network swaps in a new fork id and the other part does not, for example because it requires a new client or requires a restart, then what happens is that the clients who swapped in the new fork id will suddenly advertise a fork in the past that the other clients are not aware of, which means that chain-wise they aren't compatible with this command.

Martin Holst Swende:
Yes and that's exactly what we want to achieve.

Peter Szilagyi:
I thought that this particular suggestion was that we wait until POS arrives and then we just retrospectively say that “oh by the way yesterday's block was the POS block.”

Martin Holst Swende:
Yeah well, we reached the third total coming the terminal difficulty block and when we see it we switch fork id?

Peter Szilagyi:
If we do automatically an entire network does it, that is fine.

Martin Holst Swende:
That's the idea. Yeah.

MariusVanDerWijden:
But what if there are two blocks on the third terminal different? 

Danny:
Yeah I think probably safer to do it with a finality if you do it.

MariusVanDerWijden:
yeah the only way to do it is with finality.

Martin Holst Swende:
Okay yeah so the idea would be that the entire network that does continue on proof of stake does so at basically the same time?

Micah Zoltu:
We can't actually do anything at the same time though, right? Like one may see finality before someone else and then they see finality they advertise to someone else who has not yet seen finality and then that advertisement results in them saying “oh you guys we disagree on fork id. Disconnect each other.”

Peter Szilagyi:
There's no disconnection happening on for the updates so the forecast is only verified when you do an initial connection or in the eos figure out whether you want to connect or not. Current existing connections will not blow up because the forecast changes just if you want to establish a connection then that might be rejected.

Micah Zoltu:
So if you're in the middle of syncing and you’re let's say almost caught up. You're like a day behind or something or an hour behind/ahead, almost caught up with syncing and then you shut down for a reason, restart your computer or your power outage whatever, and you come back up. You won't be able to connect because you don't think that you're past the fork block and so you try to connect to people and they all say the fork block was back there, that block you downloaded. And you say “I'm past that block. That was not the fork block because you have not yet reached ttd.” Is that the issue?

MariusVanDerWijden:
But that cannot really happen because before that, for you to reach that point, you would have to have a consensus layer client already running. The consensus layer client would then feed you the current hash and you could sync up to that hash.

Mikhail Kalinin:
Okay. Once again, everybody has transitioned and switched their fork identifiers in
the network. I'm like the new guy and just starting my nodes. Let's say a half of an hour after the transition has happened, I'm trying to join. My execution layer tries to connect to everyone that has the new fork identifiers but I don't have it locally because I don't even know that i should change something in my EL client to be able to connect to each other and to the rest of the network. My question is, in this case, how would this client, that doesn't know about the fork id has updated, be able to sync with the network?

Peter Szilagyi:
In that case, there's actually a chance that… so yeah I know that in one direction, it is permitted so you will connect as long as you consider that you have enough data to download. I'm unsure what happens after. I think it will allow connections because from one side the peer that you join to, they will see that you’re advertising the next block will be forkhashed for you so they will say that okay homestead is at block 1 million something. You think that's the next fork. You're outdated. You are just wanting to sync. So the peer that you joined will allow you to join because they don't know that you're on some other fork. The only information they have is that you're at genesis and the next work is homestead. It matches up. You want to connect.

So from that perspective, the connection will be allowed. From the other perspective, what you will see is that the other person is actually on the fork id that you have you know nothing about. and that might actually cause you to disconnect because the other side will actually advertise Fork ID. If this hash checks something that you cannot compute because you're missing the thing. So, actually I think you will refuse to connect to anybody who's already on POS.
So in that case, possibly there would need to be an upgrade, a client release, with the hard code otherwise you will be able to join.

Mikhail Kalinin:
Yeah, that's my understanding, too. Also, I don't think that if we said this fork next before the actual transition. It would differ much from if it were just zero because if somebody wants to keep mining and continue the work network, they will just take this client release with this fork next and remove the ttd and other stuff and do other stuff that needs to keep supporting the proof of work network and just use this client and the same fork next will be there. So as if you're just zero. So I think it should be after the transition has happened if we want to split these two networks.

Peter Szilagyi:
Honestly, I think it doesn't really matter whether it's a little bit before the transition or a little bit after the transition. Generally the reason why we introduced fork ID was that, especially on the testnets, we have generally maybe 10% of the nodes upgraded to a new fork, 90 percent didn't, and then it was for the rest of the 90 percent, it took three months to upgrade. So during these three months, it was really annoying to find peers because you were constantly finding peers that were stuck on whatever old block or old chain and meaning that the way to somehow
separate the two networks. So obviously previously we did it very very precisely because we precisely knew, but I don't think it's necessarily essential for this fork ID to be extremely precise. If we can just hardcore the fork id to an approximate block where the POS would happen and essentially that block will be the one that will split clients that upgraded versus clients that did not operate. 

And this is not actually a protection mechanism against malicious people so if somebody is malicious and they want to download the code and they download geth source to their code modifier, or they try to convince other people to run malicious modified code we i mean we can't do anything they could as well take the fork id. The fork ID is kind of like to prevent naive non-operated users from causing too much annoyance. And from that perspective, I think it doesn't matter whether the fork id gets updated a thousand blocks or five thousand blocks before pos or five thousand bucks after pos. The idea is that it shouldn't cause havoc for three months straight after the pos switch. I mean yeah of course, it's definitely better the more precise it is, but I don't really see any particular downside if it is not that precise. If there are a couple days plus or minus, which in my view it should do the same.

Dankrad Feist:
Quick question. What speaks against just updating it well ahead? I don't know all the details on the peer-to-peer network but here's one reason why that could be good. Basically, people who forget to update their clients would then see a gradual degradation and thus get a very strong signal that they did something wrong and potentially be nudged into updating it in time. And so, you'd have fewer people who for some reason went right for the upgrade.

Danny:
Yeah, my primary argument against that is that if a contingent of miners want to run the chain beyond the proven stake upgrade and intend to do so, then they wouldn't upgrade their software to proof-of-stake software mode, and thus you might create a partition between those that want to upgrade a proof-of-stake and those that do not prior to the merge. And we might have delays in the merge because of dropping ttd I think.

Dankrad Feist:
Does the fork id change the consensus part at all though? Or is it only a networking thing?

Danny:
No, it's networking.

Dankrad Feist:
Right because like I mean do we actually know like... because miners might not actually just use the normal peer-to-peer network even. They might use specialist servers that guarantee them faster fusion of blocks and stuff like that. They might get their blocks from block builders, flashbots, whatever so I'm not sure if we need to worry too much if they ask to connect with them sync peer-to-peer network. Like it's very easy for them to be connected to two peer-to-peer networks.

Danny:
They certainly insert blocks into the geth network. I don’t know if we should assume that they don't use traditional means that would be locked out if they didn't.

Dankrad Feist:
I mean I'm personally much more worried about people being exposed because they forget to upgrade their nodes.

Micah Zoltu:
I’m also with Dankrad here. I think I have a weak preference that I'd rather find out sooner rather than later. There's a contingent of miners that plan on continuing to run proof of work...

Dankrad Feist:
I honestly don't think you will find that. I don't think you'll get that. 

Micah Zoltu:
Sure, we might not.

Dankrad Feist:
Like I mean as a miner, my incentive is to definitely stay connected to the p2p network that's going to switch, so I do that somehow even if that means running two nodes. So I don't think you get that signal that people will not distribute their blocks on our peer-to-peer network anymore.

Micah Zoltu:
Which would be great. I'm just saying if Danny's theory proves out, I'd rather know a month in advance instead of a day in advance of the fork. I'd rather not see the ttd drop off in the
last minute. I'd rather see the ttd drop off a month ahead so that way when we set the ttd, we can set it appropriate to the actual hash power that's going to stick around to the end. 

Danny:
And this isn't necessarily my theory. I mean the synthetic fork before was my idea and I kind of like it. That is the primary risk is that we accidentally fragment the miners off the network because they do not intend to upgrade to proof of stake. But I wouldn't say that's necessarily what I think is the outcome but I think that is the primary…

Dankrad Feist:
I mean if that is the risk that we see, then we can also easily add a command line flag that says “Yes, follow this new proof of stake fork id but do not switch to proof of stake. Like an override flag for that. And then miners can easily just do that and don't have to worry about modifying the clients and stuff for that.

Danny:
Which is another risk in another though. Make contentious work.

Dankrad Feist:
Do we really think we can stop that fork existing? I doubt it so I'm not worried about adding that. I just want it to never be the default option. The default option should always be if you just do the normal thing, upgrade your client. You should end up on proof of stake and you should never, on that path you should never, just end up on a proof of work fork and everything seems to be working and you didn't notice.

Tim Beiko:
So, it seems like we have a couple options on the table. There might be value in kind of thinking through them a bit more explicitly off the call. I don't know if we need to make a decision about this right now. I don't think we do.

Micah Zoltu:
Does anyone currently have strong opinions on this or is everybody kind of meh on all the proposed solutions? I know personally I'm meh on all the solutions. I have my preference for just a fake empty fork block ahead of time but I'm not going to die at all.

Danny:
That's my weak preference.

Peter Szilagyi:
Question. What do we want to always fall for? So essentially, what is the problem that we're trying to solve here? Because the fork id, originally the idea behind the fork id was that we
needed to separate the upgraded versus non-upgraded networks apart after the upgrade happened. Now if this is the goal, we actually have an interesting other thing that we can abuse for this purpose. Specifically that, as far as i understand it (correct me if i'm wrong), after POS mode the total difficulty of the chain conceptually remains constant. So blocks don't have a
difficulty anymore, right?

Micah Zoltu:
Yes.

Peter Szilagyi:
Okay, so in that case, if for existing nodes once pos happens and let's say finality also happens so that's fork plus 15 minutes or something like that, essentially after that point when i'm in fully eos mode whenever an eth handshake happens, both sides advertise their total difficulty with one another.

Now if somebody advertises a total difficulty that is higher than the total difficulty of my last block, the POS block from which point the whole thing is locked in, then I cannot disconnect it. So with this trick, essentially pos is aware clients can always disconnect non-upgraded clients if there's actually at least one more block mine on top of the ttd.

Mikhail Kalinin:
Yeah that's interesting, but as you have pointed out that this is more important to force as an indicator in the signal for a user that it just forgot to update. It's fine software. So I mean this fork id. After the client release so it's not gonna disconnect or… will it disconnect the nodes that has different fork next or just set to zero? Like my client is updated and somebody tries to connect to me and has the fork next set to zero but my client has the fork next step to the correct value. I think it's permitted, right?

Peter Szilagyi:
I think in that case, you will be the one. Your client will be the one disconnecting if once it goes past-- oh no wait actually if there's only the fork next it's different then clients don't disconnect because then it just means that one of them might not be up to date but as long as that work didn't happen, it's fine. But once that fork happens on the updated side then the fourth next will be zero at that side and just the forkhash will be different, and that will trigger it.

Mikhail Kalinin:
Right, so if we want this for this kind of purpose, then we should set it before transition before it connects to the full transition. And I think it's reasonable. If it's not, there is no security implications in that. Also, I think i know what to do with respect to the stack. 

So we can just have another constant that will say that the spec will say that fork next should be set to this constant and decide on the constant later on so what it will be. That's the right I guess approach in terms of the stack.

Micah Zoltu:
Regarding your suggestion a second ago, Peter. Do the clients already share their view of total difficulty during the hand connection handshake? Is that information we already have?

Peter Szilagyi:
Yes.

Micah Zoltu:
Okay so we already have the messaging and everything. This would just be adding a line to the client that says “disconnect if total difficulty reported is higher than the ttd that I think should exist”, right?

Peter Szilagyi:
Yes. The other thing is I'm not sure that probably will not help us for a client that is just joining and maybe that's the hard part that we actually want to solve. But I still kind of feel that if
we set a fourth block that is before pos, i mean we just have fork id ten thousand blocks or a week before ttd is supposed to happen, and we just have a couple loads on the network that just relay blocks between the two networks so you could just somehow have a node that… so essentially if i understand correctly the thing that we're afraid of is that if there's during or right before the fork, there's a set of miners which don't want to upgrade. We still want to pursue their blocks and I think we could do that by simply having some peers on the network that quote “connect to both networks and just replace the blocks across them.”

Micah Zoltu:
It sounds like a lot of engineering effort. 

Peter Szilagyi:
I'm not sure that it's somehow get away with it without-... I don't know.

Danny:
Run two nodes and use local rpcs to drop blocks between each other. But you wouldn't put it into the gossip from there anyway.

Peter Szilagyi:
No, I was just wondering if I can create a node that can, depending on who it connects with, just can advertise different fork ids. Essentially just lie about the fork id. And just fly itself onto both networks.

Micah Zoltu:
“What's your fork id? I don't know, what's your fork id?”

Peter Szilagyi:
Yeah that was perfect! The handshakes are transmitted concurrently, so it is perfectly fine to wait for the remote handshake before sending yours.

Mikhail Kalinin:
Peter, to your point, we can use hard code ttd to disconnect peers. So it will be
hard coded and everyone will know it even if nodes start to see.

Peter Szilagyi:
Yeah, but the problem is that you just know the ttd, the terminal difficulty, but you don't know
what the actual life total difficulty will be the final one. Because you know that it's going to
exceed ttd but you don't know by how much and that's the problem. 

Mikhail Kalinin:
Yeah I see what you mean.

Peter Szilagyi:
I think we shouldn't really hold up there. We can have another discussion about this.

lightclient:
Wouldn’t you have the weak subjectivity points and so you would know what the ttd was? or does that not kick in until later?

Danny:
And a fresh joiner could mean I reminded my node from a week ago and the transition happened two days ago so I still don't have information about what happened.

lightclient:
Okay.

Peter Szilagyi:
So I guess most of this complexity is just right during the transition right after the next few days or a few weeks because after that, it's kind of probable the whole thing is going to stabilize and most of these mechanisms will get thrown out.

Mikhail Kalinin:
Yeah. I prefer to have a full transition so that's a good indicator for a user too.Like a good fact. It's one of the factors that they should update nodes.

Peter Szilagyi:
Okay so then the simplest solution is to just hack in this “lying” node that can just join both
networks just to translate the blocks through. And then
just have that running for three days until the transition happens and then you can just lift up once POS happens. It's a bit of a dirty hack but it keeps the code clean. The production final code, that is the same place.

Tim Beiko:
So we've already kind of been discussing this for half an hour. Is it worth maybe continuing async and bringing this back up again on the next call. It's not something we need to implement for kintsugi. I don't know unless people have a strong opinion about something, but it does feel like there's a bunch of weak opinions and there might be value in just kind of thinking through them a bit more.

Peter Szilagyi:
Yeah I think especially here, we need a few people who would be willing to explore their own preference and then just see what it actually takes, how messy it gets and if it works or doesn't work. Because we have a few ideas with every need forkhashes.

Tim Beiko:
Yeah does anyone on the call want to volunteer to look into that in the next couple weeks?

Peter Szilagyi:
I can take a look at what it could take to make the malicious look. That's always fun.

Tim Beiko:
Sure, cool. And yeah I guess Mikhail, Danny and I can chat about the next steps for the other approaches and see how we can kind of flesh those out a bit more.

Micah Zoltu:
So I think from a technical side, the faux fork block should be absolutely trivial. Literally we just
introduce a fork that has zero code changes in it so every client has a mechanism for introducing forks. This is just another fork just like every other one. There just happens to be no code associated with it.

Tim Beiko:
Cool. Just to be mindful of time, unless anyone has any urgent comment about this, I think we should just move on because we have two more EIPs we wanted to discuss.

## Merge Updates
### Proposal to Include EIP-4396 to the Merge #406
*Summary:*
- *General uncertainty from Monday’s breakout session around how urgently this EIP needs to be implemented.*
- *Main concern of throughput loss after empty slots, plus a brief base fee spike. There are a couple possible solutions on the table including raising the gas limit, but may delay the merge.*
- *Pushed back to Shanghai.*

Tim Beiko:
Okay, so next up, Ansgar and Barnabe are here to give an update on EIP-4396, which is the one that proposed to change how EIP-1559 works in a post-merge context. Ansgar, Barnabe, do you want to give a quick update of what you've looked at over the past couple weeks?

Ansgar Dietrichs:
Yeah, I can start with a summary of the breakout session from last monday. So basically, splitting up the EIP into two parts, like the why might we need to do something and then what exactly to do kind of sides of things, I think the main result from Monday was that there's generally uncertainty around how urgently we need to do something. Is this something that can wait until Shanghai or is it something we should do at the point of the merge? There was also some talk on the mechanism side but then I spent some more time since then looking into the
mechanisms and I think that's really solid. So, the question is really more, “is there a need to do something,” basically.

Just to recap that briefly, there's one small concern in general about just that empty slots have a negative, like have a distorting, effect on the base fee, where there's this brief base fee spike usually after a missed slot, but the main concern is about the throughput loss. So every time after the merge there's a missed slot basically that the overall throughput of the network is just reduced by whatever like by the 15 million or whatever the target would be in an average block in that slot which just didn't happen. These kinds of through productions can be compensated in the medium term through gas limit adjustments. So if we see that say three percent of validators are offline permanently, we can just increase the gas limit by three percent and then on average it smoothes out.

There were concerns specifically about how well we will be able to adjust the gas limit after the merge. Of course, that's the role of the block builder so right now the miners and then after the merge, the validators. It's already not trivial to coordinate miners around changes every time there's some change. It takes a while and then of course after the merge, validators are even more decentralized so there's more people we'd have to reach out to before we get to 51% of people signaling a different gas limit.

One thing that could help actually is the centralization that's probably going to be introduced by the flashbots proposed merge architecture, which by the way I think should be a topic for for one of these AllCoreDevs as well because that might introduce some general centralization concerns, but in this case, it acts to our advantage because it means that you basically only have to reach out to flashbots to adjust the gas limit.

So basically that all helps for medium term adjustments but the issue remains for short-term adjustment and that's really basically the question really is. Like how important are these short-term adjustments? And do we have to do something about it in the merge? And so
again the facets there are like for one there's the concern around dos vulnerabilities and this is important this is kind of not what we used to talk about in the dos context like say slow blocks where basically transactions kind of like take very long to compute this is the different form, of course. This is kind of like identifying the real identities, the ip addresses behind this individual validator and then targeting them and bringing them offline right before they were producing the block. There's more incentive to do that if that results in a throughput loss to the network, so you
can actually attack the network through that whereas if the throughput is compensated for then of course you don't have much of an immediate incentive anymore so that could be mitigation against those attacks. and then also there are the other situations though. Say like a big staker goes offline for a couple hours for some maintenance a reason or something that just could be like a 10 throughput loss for a couple hours of network which is not great or in this in the scenario of like a client bug or a consensus issue or something that they could be they could basically say we have two forks and both have fifty percent of our debtors then at least until the gas limit starts moving, which again could take like a day or more. But the forks will only have half the throughput.

So that was made mainly in the necessity side. There's a lot also to report on the mechanism side but it's more detail-oriented. And so I probably first want to just stop here and get feedback like do we need to do something? and then if people generally think that we want to do something probably then we can talk a little bit about the mechanisms. What are people's thoughts? Is this something that is bad enough -- so these throughput losses and the dos incentives and everything -- is that bad enough to do something about it now? And that was just basically on Monday. Our conclusion was that it was hard to tell. Kind of on the fence. Mechanisms I'm really optimistic about, but yeah…

Danny:
Yeah, a few weeks ago, I was naively optimistic that we could shove this in here, test it quickly and there wasn't much complexity to deal with. I personally think that this would likely delay the merge on the order of a minimum of a month, if not two, just because of where we're at in the engineering cycle and attempting to have specs. Although I do think this is the good and arguably correct behavior. I do not think it's critical to have at the merge and that personally I think if we're sorting things merge sooner is better than getting this in, but I would be a strong advocate for putting it in Shanghai. There are obviously various concerns as you enumerated but I think between having the gas limit as a lever, even though a slow lever, we can mitigate most of those concerns there.

Tim Beiko:
Does anyone see an issue with potentially raising the gas limit to offset kind of the average throughput loss? And I think right now miss slots are like less than one percent if i recall correctly. We should expect them to be in that single digit percent range, so that solves kind of the general case issue. The issue where it doesn't solve is if a large subset of validators goes offline for a while then we have like a throughput reduction in the chain.

Micah Zoltu:
I'm against raising the gas limit for any reason just because I think the gas limit is already too high. So unrelated to this conversation, I'm not a fan of any increases.

Ansgar Dietrichs:
Wait but they are just vulnerability because i mean like at the end of the day because somebody's just a number right like what you're probably concerned about this is the general throughput per time and that will change.

Micah Zoltu:
State growth. Yeah so if I see an opportunity to lobby for reducing state growth, I will take it. And so if there's an active discussion for should we maintain the block throughput or should we decrease the block throughput, I will vote to decrease it, which is just what i'm saying here. Again though, I recognize this is not related. Just questions asked would anyone be against
it? And yes, I'm against it, but for a totally unrelated reason.

Ansgar Dietrichs:
Okay so you're not against the instrument. You're just against the...

Micah Zoltu:
Yeah I'm looking for opportunities to lower the gas limit and this is one.

Ansgar Dietrichs:
Yeah just just to point out. From a state growth point of view of course i don't think there
should be any concerns, well except for maybe that the gas limit increase could be sticky where once people come back online, maybe it's hard to bring it back down. But besides that there really shouldn't be any concerns because it just keeps the state growth rate constant because it only compensates for people offline.

On the peak kind of networking constraint side, of course that it does propose a bit of an added strain because well the average remains constant. Basically the peaks like instead of having one block every five seconds, maybe with a couple percent offline, we have like on average one block every 13 seconds, but it's ten percent bigger or something. So that's ten percent increased peak networking strain but it's important to point out that after proof of stake, we already reduced the peak network strength quite a bit because under proof of work, we had these stochastic block times. So you could have like two/three/four blocks within a couple of
seconds, and now we have like this minimum of 12 seconds in between blocks. So there's already a big reduction in peak strain, so this kind of small added increase again when we increase the gas limit should not be concerned under that.

Tim Beiko:
Right but it's worth noting that there's probably… assuming you go with this, you increase the gas limit to offset the average miss slots loss, you're still in a case where you might have an effective lower throughput if somebody goes offline in kind of an emergency fashion, right? And that's kind of the case we're not solving for. So if a large swath of validators go off offline for six hours, it’s probably not enough time to coordinate raising the gas limit. So what happens for
the little six hours is the network just has lower throughput. And that's basically the price we pay by not implementing your proposal, right? Is if there's a case where a large part of validators drop for a short enough amount of time that we can't actually coordinate to raise the gas limit that throughput is kind of lost forever.

Danny:
Correct.

Ansgar Dietrichs:
Correct.

Fabio Di Fabio:
So we're moving from a system where blocks come in on average every thirteen seconds because the same real blocks coming on average every 12 seconds so to some extent there was also a slight increase in capacity coming from that which maybe offsets the fact that some blocks might be missing.

Tim Beiko:
Right if less than eight percent of blocks are missing, it's still a net increase.

Ansgar Dietrichs:
Yeah. Maybe just because it sounds like right now we are really pointing in towards pushing this to shanghai which i'm personally absolutely okay with. Maybe just there's one last attempt though. I was just wondering, Danny, you were saying that you think by now we're already so late in the process that it's probably going to be unavailable. That this would delay the merge. And i was just curious to hear a little bit more about that because I'm just wondering. I definitely can see that for these more involved proposals, there was this extension section. But with the base mechanism to me, it really seems like five six lines of code change in the execution clients each. We of course plus a few other tests and everything so i'm just curious.

Danny:
I think the intention right now is to have a kintsugi testnet up in the first week of December to stand up through the holidays to begin to make decisions in January about very concrete and realistic timelines. I believe if you don't put an evm change into that test net and then are working on testnets in January with that change that you've very likely in practice delayed the merge because of our need to have thing on testnets even though there are a couple line changes. Correct me I'm wrong, but I just the discussion and analysis that I think we'd probably want to throw behind this thing is probably still not totally done is everyone comfortable with where we're at and so shoving it into kintsugi devnet in two weeks time doesn't seem likely to me.

Ansgar Dietrichs:
Okay, if that's the case, then I agree that pushing it is the better choice I would say.

Tim Beiko:
Yeah, does any client feel strongly that we should have this for the merge?
*silence*
Okay, I guess that's pretty clear then. I also personally feel this is something that would be really valuable to have in shanghai and there's a lot of interesting conversations to have also about the elasticity factor and whatnot that we might want to change for shanghai. But I think it makes sense to just not include this in the merge.

Ansgar Dietrichs:
One last briefing though just because it came up and it's not really related to it itself but it did come up in the discussion on monday. Because we talked a little bit about the elasticity and one of the extra concerns that Martin had last August was about like the slow block dos attacks on the network and how that could make it worse and even if we don't do this EIP now. Basically of course slow block attacks in general are still a thing and one thing that did come up on monday was the fact that the impact of these kind of dos attacks would be different after the merge than they are before the merge. And so it's just maybe something to keep in mind. To that, this could be something valuable to test on testnet. Basically just have a test net and just really crank up the gas limit all the way until the computation time of blocks kind of starts to go close to say six seconds or something so so we can see how our network would react under this kind of situation because if not implemented ideally in execution clients, the impact here could be worse in a proof of stake than it is in under proof of work. So just something that came up. It might be relevant even without the EIP.

Danny:
Why would it be worse on a proof of stake?

Ansgar Dietrichs:
Maybe we take this offline.

Tim Beiko:
Yeah just so we have time for uh
lightclients and George’s EIP.

Ansgar Dietrichs:
Right yeah so like just 15 seconds. Basically, just because the nature is different like proof of work you basically just create your block and then you start just trying to find a hash to mine on top of it. Whereas, in proof of stake they give us fixed time windows. There are more specific timing considerations, but like if you miss your window this, you can't just do it later or something. So yeah just in the difference of the nature and if you implement the exclusion plan correctly it shouldn't be an issue, but if they are like some non-ideal behaviors that can be worse. But yeah we should discuss all that offline.

Danny:
Right, okay. Both of them would result in many uncles uh but and maybe slightly different behavior but I'm not going to continue.

Tim Beiko:
Cool. Yeah let's continue this in the merge channel. 

### EIP-4444: Bound Historical Data in Execution Clients
*Summary:*
- *In general, we want to specify how clients can treat historical data which can beneficially prune hard disk space and remove old EVM versions in execution engines.*
- *Proposes a defined time threshold and specific networking logic.*
- *Expecting this to happen in 12 to 15 months. This is an early discussion.*
- *Overall goal for sustainability is to fix unbounded growth of the chain.*

Tim Beiko:
Last but not least, lightclient and George have an EIP, oh and Alex, have an EIP that bounds the historical data in execution clients. Do you guys want to share? Give some context? 

George Kadianakis:
Yep. Hello there. So I will do a small summary. I don't know if we have enough time to really exhaust everything but I'll do a small summary of the proposal as it is. So, the high level thing is that we want to specify how clients can treat historical data like old block states, receipts and that kind of stuff. The obvious benefits is that there are a variety of use cases that don't use those data so we can prune a lot of hard disk space with that and also execution engines don't need to keep the old evm versions around to parse those blocks so there are a bunch of benefits.

So that's the high level thing. And now in terms of specification, what EIP-4444 does is that it does two main things. One is it specifies the time threshold below which you can start pruning historical data if you want so as a client. And another important thing that it does, even maybe
a bit controversial, is that it specifies that clients must not serve all historical data over the p2p network and right now the proposal EIP-4444 is forcing clients to not serve such historical data because it does not want to make it optional and then have other clients rely on that optional feature and then like the quality degrade over time as more and more clients ditch this optional. These are the two things that the proposal does: define the time threshold and specify
the networking logic.

Also, this has implications in thinking so since historical data won't be checked till infinity, clients won't be able to do full things and this kind of things. And the proposal basically piggybacks on the weak subjectivity system so that clients can still sync basically to a safe checkpoint. But the way this should happen is out of scope for EIP-4444.

Finally the proposal also contains a bunch more discussion on various miscellaneous things. For example, various ways that such historical data can be retrieved, or how clients can sing from genesis, or how the ux should be. But it just basically touches on them, and then it leaves it for other EIPs or other topics, basically.

So that's it so far. We pushed the EIP to wherever eips get pushed. And we've gotten a bunch of feedback most of it is around the networking logic and whether we should force clients to not serve engine data so whether that should be a must clause or a should clause, and also about the dev p2p responses that our clients should give out when they ask for such data. So that's it for the eip4444 summary. Alex or lightclient, you can see more or we can go into the discussion.

lightclient:
I guess does anybody immediately have questions or comments?

Martin Holst Swende:
So this looks very much like something that Peter started thinking about in and percent that I talked about in I think Prague a couple of years ago. It didn't pan out eventually. I mean we
haven't implemented it, but I'm curious Peter what since you considered this a couple years ago, if you put your thoughts on it now in this context.

Peter Szilagyi:
I have a little bit in the current context. So way back, one of the biggest problems was that we kind of needed a way to distribute room chains because we kind of felt that there wasn’t… so currently in Ethereum 1.0 world, promise is that the chain is accessible and whether that's past headers blocks or even receipts are accessible and apps kind of rely on that and for us to just replace this guarantee with some other infrastructure we kind of needed something that is as reliable or almost as reliable as locally having the box available. I know that the best suggestion was that we could have some form of infrastructure run by major players and like consensus whatever a lot of people. We could have bigger companies running this infrastructure and they could just serve the past historical blocks.

It's a bit wonky because it's outside of the protocol. We never really were fans of it. And the reason why we kind of dropped it is because it just requires a lot of bureaucracy and a lot of politics to dream up such a system. The challenge here is not really the technical aspect. Rather it's the whole governance aspect of who is going to be part of it, why, and etc etc. And then essentially, we just had other things to do that's why we dropped it.

lightclient:
Do you think that with the reliance on weak subjectivity checkpoints for starting clients that the technical issues of not having those blocks available is alleviated?

Peter Szilagyi:
The problem is not synchronization. I mean we could have synchronized so we could have just released hardcoded fork blocks or start the hash that they didn't get and just say that well you're going to. So this whole week's objective could be because I can get a long time ago. The problem is that's rely on past state being available and Ethereum users are… Ether 1 promises to have that available, and that means everything is built on this assumption that you can always access the transactions in block 5 or the receipts on block 5. With this merge, I think that's an opportunity to go back on this promise so to say and just say that well for the long term, half of the network we're going to change these invariants a bit.

Danny:
Well and it does reduce the debate. Like you could argue releasing checkpoints and proof of work, they're like oh well that's not pure, whereas in proof of stake, you must have a recent piece of information to safely sync the network and so that the need to have all historic block
headers on the network to be able to find the channel head does become reduced because of the security model shift. That's not defined at the crux of the issue.

Tim Beiko:
Yeah just because we're basically at time, Andrew you have your hand up, so we can go over your thoughts and then wrap it up. I've shared the discussion link in the chat as well for async conversations.

Andrew Ashikhmin:
Right so I'd like to notice that Erigon at the moment doesn't have snapshot sync. We rely exclusively on sync from genesis so this change will break aragon. We'll have
to think of a workaround.

Also, on some general notice, it's better to do this change closer when we have a solution on state expiry. To my mind, it should be bound to state expiry other than or some infrastructure for state delivery or at least wait until all clients have their own system of reliable state delivery. I agree that there was a promise in Eth1.0 that all kinds of historical data is available and we cannot break this promise without having either proper infrastructure in place or some other mechanism or maybe look like either individual mechanism for each client or some agreed upon mechanism, but to my mind it's pretty much your...

lightclient:
Right. To be clear, we're looking at this happening in maybe 12 to 15 months, so this is very early in the cycle.

Peter Szilagyi:
So just to emphasize two things. One of them is that this wouldn't be implemented and brought out now. The only thing I can personally feel that is important to say is that come the merge, we should and must if we want to ever do this then we must at the merge explicitly state that the chain segments blocks older than X years will not be available as a photo. So photos don't guarantee this. Now whether we will implement this in one year, two years, five years or never, that's a different story. The idea is that we need to get people to stop relying on the subject expecting blocks to be forever available. And the reason just answer the other note that you said that you this whole thing should be rolled out together with state rent, the two things are a bit separate.

For one, the blocks currently outweigh the state fork one, fork three to one or something like that so they are significantly happier, but essentially what currently one proposal protocol improvement proposal are for witnesses and status clients or varying degrees data science but all these require some witnesses that need to be retained besides the blocks. And these witnesses are significant in size so they are maybe about one order of magnitude larger than the blocks themselves. So as long as there is no pruning on blocks, we cannot implement witnesses because it's just going to blow up the stuff we store on this to unimaginable proportions so essentially all the witness work depends on an aggressive learning strategy.

Tim Beiko:
Just because we're past time, there's a comment in the chat about maybe doing a breakout session next week. I'm not sure if there's urgency here given this is something we might want to do in the next year or two. If we can also just discuss it on the next AllCoreDevs and kind of pick up the conversation there. So does anyone have a strong preference for a session next week or is the next AllCoreDevs fine with people?

Peter Szilagyi:
I have one strong suggestion. Next for my goal is fine solving the technical aspect of this issue whatever is fine there's actually no rush, but i do think it is super urgent for us to decide what guarantees we want the chain to have after the merge and start prepping people accordingly.

Tim Beiko:
Right.

lightclient:
Sounds like we should discuss it on the next AllCoreDevs then.

Tim Beiko:
Yeah and i feel like the thing is this also kind of benefits from having a lot of different people involved in the conversation, and when we have these breakout rooms, we tend to only get a subset of people. So my hunch is we should probably wait until the next AllCoreDevs so that we have more people, but also center the conversation around the guarantees we want to provide and stop providing around the merge. And EIP-4444 is related to that but not the exact same thing. Does that make sense?

Peter Szilagyi:
Yes. Although I would again if you bring a lot of external people, I would emphasize that this session is not whether to prune fast stuff or not prune that stuff. The discussion should be centered around how we stop paying growth?

Tim Beiko:
How do we stop what? Sorry.

Peter Szilagyi:
The unbounded growth of the chain.

Tim Beiko:
Right yeah yeah.

Peter Szilagyi:
That is the goal and that essentially, if you want ethereum to stay alive for the next 10 years, that problem needs to be solved. And just saying that well we'll just keep the count down the road, that won't work. So, we need to stop. We need to start deleting stuff.

Tim Beiko:
Right.

Peter Szilagyi:
We can debate what we delete, but we cannot debate the need for the mission.

Tim Beiko:
Cool. That seems like a good place to end. We're already a couple minutes over time so appreciate people for staying over. Thanks everyone. And I will see you two weeks from now.

*-- End of Transcript --*

## Chat Highlights:

- 09:10:02 From Tim Beiko to Everyone:
	https://notes.ethereum.org/@djrtwo/kintsugi-milestones
- 09:14:58 From danny to Everyone:
	https://eips.ethereum.org/EIPS/eip-3675#fork-choice-rule
- 09:15:24 From danny to Everyone:
	https://github.com/ethereum/consensus-specs/issues/2643#issuecomment-953250363
- 09:17:23 From Mikhail Kalinin to Everyone:
	https://github.com/ethereum/execution-apis/issues/120
- 09:19:20 From Tim Beiko to Everyone:
	Fork ID context: https://ethereum-magicians.org/t/eip-3675-upgrade-consensus-to-proof-of-stake/6706/7
- 09:32:02 From Tim Beiko to Everyone:
	We could put this release out at the same time as the CL release with the TTD
- 09:32:18 From danny to Everyone:
	right. target around MERGE_FORK_EPOCH on CL
- 09:43:06 From lightclient to Everyone:
	If the remote FORK_HASH is a superset of the local past forks and can be completed with locally known future forks, connect.
  Local node is currently syncing. It might eventually diverge from the remote, but at this current point in time we don’t have enough information.
- 09:43:35 From Micah Zoltu to Everyone:
	If we are worried about miners dropping off due to disincentive of having to upgrade, we can mitigate that by having the faux fork block as long as possible *before* TTD, so they miss out on the maximum amount of mining income.
- 09:55:55 From Ansgar Dietrichs to Everyone:
	it would be desirable if, in case of a contentious fork, users who forgot to update their clients would not just by default end up on that continued pow chain
- 10:01:05 From Ansgar Dietrichs to Everyone:
	seems like we could come up with a reasonable upper bound for the difficulty of the transition block itself? and hard-code the disconnect threshold at td + that upper limit?
- 10:12:07 From Tomasz Stańczak to Everyone:
	https://ethresear.ch/t/mev-boost-merge-ready-flashbots-architecture/11177
- 10:29:09 From Tim Beiko to Everyone:
	Discussion URL for the EIP; https://ethereum-magicians.org/t/eip-4444-bound-historical-data-in-execution-clients/7450
- 10:30:53 From danny to Everyone:
	https://notes.ethereum.org/Mp5Iv4N0Qb-d6KZvNuBspg

## Attendees:
- Tim Beiko
- Danny
- Andrew Ashikhmin
- Ansgar Dietrichs
- Martin Holst Swende
- Barnabe
- Daniel Lehrner
- Fabio Di Fabio
- Fredrik
- George Kadianakis
- Giuliorebuffo
- Jose
- Karim T.
- Lightclient
- Marek Moraczynski
- MariusVanDerWijden
- Micah Zoltu
- Mikhail Kalinin
- Pooja R.
- Peter Szilagyi
- Trenton Van Epps
- Tomasz Stanczak
- Somu Bhargava
- Lukasz Rozmej
- Pawel Bylica
- Dankrad Feist
- Sam Wilson
- Alex Stokes
- Justin Florentine
- SasaWebUp
