# Merge community Call #3 Notes 

### Meeting Date/Time: Friday 2022/02/11 at 14:00 UTC (9:00 ET)
### Meeting Duration:  1 hour  
### [GitHub Agenda](https://github.com/ethereum/pm/issues/465)  
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=65Pt6oS3kDM)  
### Moderator: Trenton Van Epps  
### Notes: Avishek Kumar
—----------------------------

## Summary 
- block times will go from ~13s to exactly 12s after Merge
- Rough Merge timeline is “launch Kiln” -> “merge existing testnets” -> “merge mainnet”
- Readiness checklist: https://github.com/ethereum/pm/blob/master/Merge/mainnet-readiness.md
- If you want to subscribe to RSS feed for EF post - https://groups.google.com/a/ethereum.org/g/announcements
- EF email - announcements+subscribe@ethereum.org

-----------------------------------------------
**Trenton Van Epps**: All right, welcome everybody to the third merge community call. There's been tons of progress over the past month and a half.

# post-Merge [Testnets](https://twitter.com/peter_szilagyi/status/1484548996169408512)

**Trenton Van Epps**: Moving towards new testnets fixing old ones and we're going to share a little bit about that and just generally talk about what validators users and the general community can expect when the merge actually happens. Let me grab the agenda again. There's a list of things that we've gone over in previous calls and I think there's a few new things on there but yeah does anybody have any topics that weren't added to the agenda
that they wanted to bring up.That they just want to bring up now and thenI can mark it down and we can get to it later.If not we can have time to jump into some stuff.

**Micah**: Have we already talked about randomness in the previous call? I don't remember.

**Tim Beiko**:  Yes but I can quickly cover it the difficulty thing basically

**Micah**: yeah if we've already talked about it that's fine. I just wanted to make sure, it gets one of these calls.

**Tim Beiko**: Okay yes.I do feel like now there's no way we can't cover it. I guess I know there's something. Yeah, maybe just to quickly recap application level changes that matter in the merge and then we can go into like what happened since the last call. Like Micah was saying there's only a couple things that really change in terms of  on-chain for applications. 

One of these things is that the difficulty value gets replaced with the random value from the Beacon chain. So if you are running an application that uses difficulty as a source of pseudo-randomness this will still work.It will just be a different random value that we get and one thing to note is that the random value is much bigger than the current difficult value. If I have the numbers right, I think the current random value, the current difficulty value is about 64 bytes and the difficulty is 256. So that's also a neat way, you can check at an app level if the merge has. Oh bits sorry so if  the value that's returned I buy this code is now 256 bits. It means you're in a pulse more post merged world on chain and that's one of the big changes. 

The other changes anything else that has to do with proof of work. So anything except the difficulties of things like the mix hash. The list of uncles and whatnot basically I will get zeroed out at the application layer. The random value is the only one that kind of gets added
replacing the current difficulty value. There are talks where I just saw yesterday. There was an eip published to start  specking out withdrawals from the beacon chains. It's quite possible that in the future the values that had to do with uncle blocks get used for something. I think they're state routes in the beacon chain or withdrawal routes.I am not sure quite what the term is but basically that we use use this displays in the block header to just pass information from beacon chain receipts and then the last kind of big thing that changes
From an application's perspective, block times go from 13 seconds on average with a lot of noise under work to 12 seconds exactly under proof of stake. And the one thing is If there's a proof of stake validator that's offline. They miss their spot so that means you know you get
the chance of a block every 12 seconds exactly does not guarantee a block shows up but if it does it will be kind of on a 12 second increment and right now we've only seen less than one percent of blocks not show up on the beacon changes. Because validators are offline or things that are the high level changes that you can expect in the merge.

## Kintsugi and its replacement

 There's a bunch of links that Trent has put in the college and that dive more into that and that's basically it. I think if we want to quickly  chat about stuff that happened since the last of these calls. So right before christmas, we launched the kintsugi testnet which is basically a new testnet that's running the post-merge version of ethereum. So it has both a beacon chain on it and an execution layer to execute some transactions. We did find a couple issues on the network mostly basically, we found a couple initial bugs. We fixed those but that led to the network not finalising for a while and then we found some more issues that only happened when the network was like in a deep state of non-finalization and we're in the process of fixing this some client teams already have and we have basically a new spec for a new test net that's called Kiln and we expect kiln to be the last test net that we launched before forking the existing testnets like Gordy and Robsten and what not. So I think one thing for applications that's  really worth doing  both on kintsugi that's live today and if not on
kintsugi absolutely on kiln when it goes live is making sure that like your entire tooling workflow and deployment. Workflow works it should understand  and we've tried with like a handful of applications already and things kind of work as expected but I think you should really see Kiln and if possible kintsugi has addressed rehearsal before the testnets fork, so if you can deploy kind of a staging version on that. There is an infer sign forever. There's an rpc endpoint you can just point to. You don't have to run your own node if that's not something you usually do for your application on the ethereum foundation blog. There's a blog post announcement about kintsugi that links up those things and there'll be another one for kiln. Well yeah I think it's really important to stress that this is kind of the time to find out that you know your contract deployment script doesn't work for whatever reason and or your UI is acting weird for whatever reason. These are the things we're hoping to find out with a special eye. I think it is towards tracing the applications we've deployed already. Don't really 
use extensive tracing so if you are an application that does and you're listening. If you want
to try deploying on kintsugi and kiln that would be great. If you find issues, if you can share that feedback that'll be super valuable and yeah the last thing I think that I have is the agenda, the idea of outsourcing to a web3 provider. Your execution client is probably not going to be possible after the merge, so right now it is possible if you run just the beacon
chain node to outsource. Your eth1 node to say infer our alchemy because you're only just getting kind of information from the deposit contract but after the merge. Basically if you're a
validator you need to produce blocks and you get paid to produce blocks including transaction fees which are immediately available to use and so because of that you actually need to run your own node on the execution layer. Yeah so that's something that people should be aware of in the future. There'll be some cryptographic incentives to or not incentives but like this incentives to rely on the third party I am not aware today of third parties that are going to propose. I am kind of outsourcing execution clients after the merge. But yeah I think as a violator basically you are kind of risking a ton of revenue by doing that.

**Trenton Van Epps**: Yeah so just to summarise if you are currently a validator on the Beacon chain and you're not running your own execution client and that means Gaff or
Nethermind or any one of those clients.  You're going to have to start running one before the merge happens.

**Tim Beiko**: And then the other thing.. 

**Trenton Van Epps**: You go ahead.

**Tim Beiko**:  Oh! I was just going to say, yeah there are a bunch of like ad hoc guides to do that right now for kintsugi but one thing we are planning for kiln is to have a bit more detailed guide.  Hey I'm running your beacon node. How do I add an execution node or vice versa.  If you are running a node on the proof of work ethereum network. Today you're gonna need to run a beacon node post merge to get the head of the chain. So we're gonna try and just flesh that out a bit more and what do you actually need to do, how do you make sure that you've got it right and so on.

**Trenton Van Epps**: Yeah and the other thing you touched on which is a bullet point in the agenda as well which i'll go over again is that when I guess the bigger point is at the merge
withdrawals aren't enabled. That's going to be in the upgrade afterwards which we're probably going to call shanghai. But if you have either staked in the deposit contract. You won't be able to access that or exit from the beacon chain at the merge that happens later. But as Tim mentioned you will get transaction fees those will be immediately available and actually it was the call yesterday Paul from the lighthouse team was talking about how you know getting that process started about how to design the or standardising the flow of allowing validators to designate which address receives transaction fees from the execution
layer so something to be aware of again. ETH isn't unlocked but transaction fees will be so you won't be able to withdraw but you will have some sort of income. If you are validating or 
liquid income let's say  there's a question Marius do you want to just answer that in chat or
on voice if you're able.

**Marius**: Yeah so the current spec allows for the el to override. What does it gets from the consensus layer? so the consensus layer passes the coinbase address to the execution layer but the execution layer the spec allows for the execution layer to ignore that and change that. So what might happen in the future if the consensus layer does not provide an
address then it might just take the configured address of the execution list.

**Trenton Van Epps**: Right and for the recordings

**Mikhail**: It was being asked.

**Trenton Van Epps**: What do you think was being asked Mikhail?

**Mikhail**:  Whether or not it's possible to set up multiple executions. Clients that are backups of each other so that way if you need to upgrade os  that  your execution clients running on you can fail over to something else and I don't know if we have the tooling for that
built anywhere centralised.

**Trenton Van Epps**:um is the person who asked that question able to just clarify
which of those interpretations is correct either in the chat.Okay the second Micah's interpretation.

**Micah**: So I don't think we have someone correct me here Marius may know or Tim
or Trent. I don't think there is any tooling that is built by any of the core devs or anything for
automatic failover from one execution client to another. So the idea here is you have one beacon client and twitch shooting clients in that way if you want to turn one of those execution clients off. It'll fail over to another one so that way you can like upgrade the hardware or whatever underneath it and as far as Iknow that is not built

**Mikhail**: Yeah so  we haven't done something like this yet.

**Micah**: Wouldn't it just cost supposed to be  used like standard lot balancers if that
supports json rpc or some kind of this stuff

**Speaker 1**: Sorry what speaking  two being clients and one execution client is bad or two execution clients one being client is bad.

**Micah**: One of those puts you in a very bad situation. I don't know which one it is. Do you remember Marius?

**Marius**: Well  it doesn't really matter as long as you only have one validator sign in. 

**Speaker**: Yeah but if you have two beacon nodes  that send conflicting set heads then your execution plan gets confused.

**Marius**: Yes so you can run multiple  multiple execution clients off of the same consensus.

**Speaker**: Exactly

**Micah**: Yeah and the other way around is it more difficult and from a configuration standpoint. Does the user just need to connect to extrusion clients and point them both at
the same speaking client and that's it everything should just work or is there like that will they need to  do some sort of special setup


**Speaker**:  for the execution client no, the special setup has to be in the beacon client. In  the consensus layer client there you have to specify this your url for the execution client and this another url for failover

**Trenton Van Epps**: Let me jump in real quick, if people haven't realised that we're moving into sort of open discussion, so if anybody does have a question that isn't addressed in the agenda or isn't coming up naturally just raise your hand or put it in the chat otherwise we could talk all day about random things if you don't bring it up. Keep going Micah whoever was talking.

**Micah**: Pari could you  expand on that and voice if you're available on how a user might set that up.

**Pari**: Sure, usually most speaker nodes have a concept of a failover rpc and currently you can specify that in a flag.  So you have your main execution client and then you have your failover rpc client. For any reason if the main client is missing then the beaker node switches to the failover rpc. The same logic would apply in the future. So if you have two execution engines you should be able to target the main one during regular functioning and
the backup one later on as far as I know this is an untested feature for the execution client. It's a very stable running feature for just deposits like right now how it is in kintsugi  but with the execution engine I don't  think it's a really well tested feature yet. But it's something that will be tested by the time the merge happens.

**Micah**: While you're running in that node, if you've got a primary execution client and a failover execution client, will the beacon client or the consensus client keep the failover  execution client up to date? Will it be sending it said heads up?

**Pari**:  That's what I'm not sure about. So I am not sure of that. Right now but I think it should send it to both places because currently the beacon node queries both the failover as
well as the main one to know how many healthy nodes it's connected to at all times. So i'd
assume in the future it would just send a set head message to both. But you'd have to ask
cl dev about the exact behaviour.

**Trenton Van Epps**: Thanks guys, Remy your question for the recording, i'll just read it out.
How will validators choose the ethereum account for the transaction fees going into the transaction fees. They will gain from proposing a block. I think Paul mentioned that when you start up the node you will be prompted with your users will be prompted to enter an address and I don't think what he mentioned was that you won't be able to move past that without entering and Tim is unmuted and he's going to swoop in with some info.

**Tim Beiko**: Yeah so that's basically it you need to provide it to your node upon startup but
one thing to make clear is you get the transaction fees. Yeah you only get the transaction fees and not like any. I guess the fee for proposing the block itself. So the fee that you get for actually proposing the block accrues on the beacon chain but then the actual transaction fees accrue on the execution layer. Hopefully that makes sense but yes you just enter it at startup.

**Trenton Van Epps**: And in this case does startup mean like what would that look like for somebody? Who's already running a setup  when they install new software, when they update to the latest release.

**Micah**: It would be like a cli flag or environment variable flag or however you configure your client. Config file cli flag environment variable depends on each individual setup.

**Trenton Van Epps**:	 There's another question in the chat asking about downtime
in case of network degradation. I don't have a specific like percent  loss but the network is pretty forgiving when you're validating. You're not going to be, you won't be slashed for losing connection. Slashing is usually when you're doing something malicious like proposing an invalid block or something like that. But for simply disconnecting from the network.The leak is actually pretty small and anybody feel free with more specifics you can jump in.

**Micah**: Yeah it's .000018 or something that per block you failed to attest from. Correctly the time it really ramps up. Is if lots of people disappear at the same time, so if there's like a major network partition like across the internet or an actual attack or you have a large section of validators that all try to collude and drop at the same time that's when the leak will start to ramp up much faster and so for most of the time you know if your computer just shuts down your local power whatever it's not a big deal. If your whole country goes offline
your country consists of you know 50 of validators know that's going to cause all those people to leak much faster. So it really depends on the specific scenario but for the normal case what transcends exactly right.  You're probably not even going to notice.

**Speaker**: That's one of the reasons why it's important to not correlate yourself by using the same software and hardware. If you're validating in the same cloud providers because if any of those things fail for a large majority of the network, you're going to leak a lot faster than if you're using you know less than majority used software and hardware microsoft's clients. 


**Mikhail**: Definitely there's just one more thing that is important: all validators come with the database. It's called the slashing protection database if for any reason you need to migrate and follow all the procedures for migration but in principle the slashing protection database makes sure that the validator doesn't sign anything that it could get slashed for. So you don't have to worry if you're offline for a bit the validator wouldn't automatically get slashed

**Micah**: Oh yeah just a clarification on terminology uh slashing usually means, you're actually being actively penalised. This is different from leaking so there's leaking and they're slashing so leaking is just like if you go offline you don't show up to a test you're not going to get penalised you just  leaked a little bit of money if that makes sense? 

**Speaker**: Can I be even more pedantic about the terminology here please. So you are penalised for being offline. You receive penalties. They're about the same as the rewards you would otherwise receive so if you're offline for a day then you're back online for a day you end up even. There is a leak this is happens when the whole network is not finalising
and that you receive more severe penalties for being offline. So we call that the leak specifically and then slashing slashing is punishment. You're not punished for being offline,
you're punished for breaking rules and that's very severe. You're basically ejected from the network and you lose some of your stake. It's very hard to get slashed. You have to screw something up in your setup to get slashed. You're not gonna get slashed in the normal course of events.

**Speaker 1**: I a'm sorry so to clarify so initially someone mentioned that if there is a larger
number of validators that go offline. Simultaneously that causes something called a leak and that should  aggravate the penalty that offline validators will face. How is that?

**Speaker**: yeah, it's complicated and i've written about it and i'll drop a url in the chat but it's
never happened on the beacon chain so far we have never had a leak on the beacon chain in the  13 14 months it's been running. It should be an extremely rare condition if you are online 80% of the time or more during a leak then you end up even if you don't earn any reward but you don't get any penalty. So uh even then but if you're offline more than 80 more
than 20 of the time during a leak then you can be quite heavily penalised but it's still not slashing. Slashing is something else.

**Speaker 1**:  Thank you so much just one more clarification on that does the validator have to always re-authenticate itself with its originating ip address or so i'm imagining some water for load balanced infrastructure where you've got failover band links where if one goes down you use the other does that really matter and would it be not too hard for this thing to be able to. You know publish itself from a different ip address.

**Micah**: Yeah ip address is more or less irrelevant in the gossip network. So yeah you can come back you may if you start if you lose your database and you lose your ethereum node record then you might have. It might be slightly slower to find new peers but we're talking minutes we're not talking hours for that so basically yeah no problem at all.

**Speaker**: I am gonna throw out something wrong here in hopes that someone corrects me. I
believe if you want to be very careful with failover validator clients because if you remember correctly if you have two validator clients running on two different machines and they're both trying to validate that is one of the conditions where you can get slashed. Is that accurate?

**Micah**: Yeah, that's a classic way to get slashed. I think every single instance, We've seen so far of slashing has been due to people having funky fail-over mechanisms and not minding them carefully. Yeah basically having two validators running in different places at the same time.

**Speaker**: Yeah so in general the advice that i've heard given out is you're far better off. Just running one validator and eating the downtime then you are trying to set up a failure node unless you are really careful and so either spend you know months of engineering time to set up failover that is very careful to never go wrong or just accept that you'll have some down time because the downtime is much less punishment than  double sign in.

**Trenton Van Epps**: Yeah I think this is one of the things. One of the misunderstandings about validating and I am not quite sure where this comes from. Maybe it's we just need to be more explicit in documentation or how things are communicated but a lot of people often have the misconception that you know any sort of downtime is an immediate penalty or it's as severe as slashing or yeah even using the term slashing which is kind of a catch-all term for penalties when in reality. They mean different things and have very different outcomes. So it's very common but I think for anybody on the call just understand that  having your validator down for a little bit is actually very minor in the grand scheme of things. Obviously you don't want to get your stuff back online as soon as possible but if you're running a setup you're not going to lose lose a major portion anything else related to slashing or penalties or
inactivity.

**Tim Beiko**: I have a question for Ben. some essays going on in the chat here. yeah. Is there if you're offline when your validator is due to propose a block that affects your penalty somehow or does it not matter.

**Ben**: only to the extent you don't get the block reward or any transaction fees associated with that.  So yeah indeed that would be unlucky to be offline when you're a block proposal but there's no penalty for not proposing a block. You just miss out on the block reward and the transaction fees.

**Tim Beiko**: Got it, thanks.

**Trenton Van Epps**: That would be like salt on the wound if you got extra penalties for missing your slot because you're all fun and just generally I should have mentioned this at the beginning but if somebody can respond verbally. I know everybody is maybe not able to but if you can ask or respond to a question verbally it helps because this is being recorded and then it'll be transcribed but the chat is a little more ephemeral.But yeah I appreciate everybody who's asking questions and answering them in the chat as well. I am trying to skim through and catch up on any new questions.

**speaker 1**: Someone asked if the network will be down at the time of the merge and the answer is no. It will be just like any other worker in the past.

**Trenton Van Epps**: Yep yeah and this is kind of related to a bigger topic that concerns users. In reality users applications, They're not going to notice any difference leading up to at the point of the merge and directly after you know this is updating some sort of app in the background. Once you open the app it kind of just works. You're not going to really notice anything; the services will continue just the same. You won't have to like more broadly you're not going to have to transfer your ether to a new chain. You won't have to or if you're a developer your contracts aren't going to have to be migrated. You know what we're trying to do is make this as seamless as possible and you won't really have to do any sort of transition or migration everything should be the same.

**Tim Beiko**: One thing to note though I guess for say exchanges or like any application that also deals with offline or off-chain funds and whatnot. I  think that's probably the way you've already wanted to think about the merges. We have this terminal total difficulty which triggers it on the proof of work side so that means once we reach that point no block basically. There can only be one set of like children blocked that exceed this terminal total
difficulty but there can still be multiple ones so different competing forks at that block then one of those will be chosen basically by the the proposer from on the beacon chain for the next block and two epochs after that  first kind of post proof of work block will be finalised and that's kind of the stage where you know that everything is is kind of done. I think Marius had a comment about that with finalising the rpc that's probably a good segue but  when you see the first when you see the first block having been finalised on the beacon chain after. The last book for work one is kind of when you know that the transition has happened successfully and that this first block is not going to reorg and say you're in exchange you can kind of accept a deposit or like reopen deposits or whatever. Yeah Marius do you want to take a minute or two to talk about how this is exposed at the rpc layer.

**Marius**: Yes sure,  so  we have a lot of calls that  you can either specify a block number
or a block hash or you can specify one of three different keywords. Latest pending or earliest
and what that gives you is for example the pending block is the block that hasn't been mined yet. So we try to apply some of the transactions that we have in the transaction pool on top of the current block to predict which transactions might make it into the next block. This is called the pending block and you can query your note for that in order to see for example
if your transaction gets properly executed or not or like the receipt of a transaction. If it would be executed and we also have the current block which is you can specify latest for that you get the current block that is the best block that the node has seen at the moment. We also have to state for and what we will add in the future or I  think I already edited but the idea is you can also specify final finalise now in these calls and these types of calls and this will give you the last finalised block. So basically finalisation in  these two works or in post-merge works that 164 blocks have been executed on top of a block of 64 slots. No it's two times 64
slots have been passed then block gets marked as finalised. So it's not the new block. The news block but it's some block a bit further from time ago but you can always be sure that this block will not change except for vary. No it will it will not change so that's a difference in
how the new world works. You can be sure that stuff doesn't change. So we make sure to expose this behaviour to the user for example for exchanges to say okay. Once a transaction has been included in a finalised block or the the block that had a certain transaction was finalised, then we will accept the payment or whatever and so yeah that's basically every call that you could specify pending or latest tool will now also accept final last that's it.

**Micah**: If you're subscribed to blocks in some way. Will there be any indication or if you ask for a block. Is there any indication in the response whether that was a finalised block or not? No getting blocked by dash get so.

**Marius**: And also like lots of this is not really specified right now but we implemented it already. Just to make sure that users can use this.

**Micah**: And a a minor contentious point in addition slash correction to that so finalised means that it will not the no execution client will automatically reorg no executive client or consider the claim will automatically be ordered past a finalised block and so the only way to reorder past final items block would be with some sort of user activated hard fork and so
this is good

**Speaker**: Yeah you need two thirds of the validators to finalise the competing chain and that implies that a third of the validators on the network. Would be slashed,  so you know the cost
is like the same order of magnitude as a large scale 51 attack on ethereum.

**Tim Beiko**: So it's possible in the same circumstances that a deep 51 percent attack on ethereum is.

**Speaker**: Yeah and the key here is that in order for a reorg unlike with the bitcoin or proof work ethereum today, approved work networks. They can automatically reorg you know back if someone does launch 51 attack an automatic bureau can occur and the clients will reorder back however many blocks it can be up to infinite or up to genesis. I guess the cave here is with proof of stake. We do have the ability to launch a user-activated hard fork which can reorg past the finalisation point and this would be in a very extreme scenario where validators have been shown to be actively attacking the network and we want to make sure they get punished for it. So unlike proof-of-work, we can in proof of stake, we actually can punish validators after the fact so if we see some evidence of malfeasance by validators by a large chunk of validators that the protocol could not identify. We can go back and slash them later now. This would be you know talked about, this would not be something that just happens automatically. Again unlike proof of work. None of this would be automatic this
would be a very manual intervention where we tell users hey please upgrade your clients that does this roll back. It'd be a major thing so don't think that  finalise. Really is it does mean finalised in basically all scenarios unless the network is actively under attack by validators in some way which is unlikely to happen.

**Trenton Van Epps**: All right, unless there are any other comments on this. There were some other questions any final comments. Okay backup a way in the chat somebody was asking about nodes. Requirements I think Marius responded. Can you just summarise what you put into the chat for the video or the recording.

**Marius**: Yes sure so if the requirements don't change too much. If you're currently running both. The execution layer and the consensus layer node then you should be good. If you're currently only running the consensus layer node and rely on inferior or some other type of service for execution layer data then that's not possible anymore. So you need to run your  own node which will increase your hardware requirements. There might be things coming up  that will alleviate some of the costs but in general it's if you're currently running both notes. Then you should be good. There are sometimes where nodes start to struggle in times of 
non-finalization so if the network breaks down then nodes will use a lot more disk space than they use during normal operation. But  first of all that shouldn't happen on mainnet and second of all the teams are already thinking about how to reduce the disk space during times of non-finalization and yeah that's basically.

**Trenton Van Epps**: Great yeah and then another person asked whether they could run
for example a validator client or beacon client. Then the heavier execution client on something more substantial and yes that's possible. Tim, do you want to summarise the question about block rewards again. Just so we have it in a couple different places. Maybe my explanation earlier wasn't good enough.

**Tim Beiko**: So the block  rewards basically there is no block reward on the execution layer post merge. Right? The rewards that exist on the beacon change on the beacon chain
go and change so you get today already rewards for proposing a block on the beacon chain. You get rewards for testing other blocks on the beacon chain so that stays the same and then transaction fees on the execution layer stay the same. So you know every transaction on ethereum pays a fee, part of that fee is burnt the rest of the fee goes to the block producer and so after the merge validators who are block producers get the sub of those two things. They get their current rewards on the beacon chain to the same extent that they've already had. There's no like increase or anything that it's still based on the total number of validators that whole thing but they also get the transaction fees from the execution layer sent to any ethereum address that they want. So this means that they don't they're not subject to being locked. A validator does not need to to withdraw or to have a partial withdrawal to have access to those funds. They're immediately available. 

**Trenton Van Epps**: This is  okay,  awesome, perfect. Yeah thank you um thumbs up.
Let's see what else we got here. Oh the one thing we haven't touched on yet. What happens to test networks or testnets after the merge? I think Tim probably has the clearest picture of this. Do you want to summarise forever any developers on the call?

**Tim Beiko**: Yeah I don't think, we're 100% set on it yet but what seems to happen for sure is some testnets will be deprecated. What seems likeliest um and again this could change is that Rinkaby does not transition to the merge so Rinkaby seems the testnets to make it if your application runs on Rinkaby only. I would strongly suggest starting to look at other tests that's basically now Broxton seems likely to transition through the merge. But then be shut
down sometime after. I am not sure how quickly but I think if you're on Robson. You also probably want to look at alternatives. Gordy seems very likely to just transition and stick around long term. So, if you're on gordy, you're probably good and then finally  there's a new
a proof-of-work test net that was launched.A couple months ago called sepolia and the goal is likely to transition sepolia over run the merge on it and then maintain it instead of Robsten. Just because it's a bit of a newer test net and it's less heavy. So tl dr Gordy and Sapolia are looking like the best candidates post-merge. One thing also is there's testnets basically have two values. One of the values is  a staging environment for applications. The other value is a staging environment for client devs and the things you want to test  for client devs are slightly different. We'd like to test our client software in cases where the network is  not finalising for example and things aren't going well and that's obviously not great for applications. You probably just want to test on something like a copy of mainnet, so there's plans to make one of the post-merge test nets more geared towards  client testing where we regularly turn off some validators. Because it is not to finalise make sure that the client  software can handle that. Then there's another one that'll probably be a bit more stable and where you know you can expect kind of similar situations the main net. We haven't really made that call yet but it's probably gonna be you know Gordy and Septolia are likely to be one of each. Yeah so that's something we'll have better information on in the next couple weeks but if you are on Rinkaby. I definitely suggest looking at the coin out of the testnets. The other one sorry coven is the one where I really don't have a view. It's a bit unclear what the situation is there. I know in the past they've lagged updating it until after may after mainnet has updated. I think there were some plans updated for the merge but it's not fully clear to me yet. So I think yeah if you are just on coven you probably want to reach out to the
maintainers if it's to to understand a bit better with the with the premise though

**Trenton Van Epps**: Yeah somebody asked me about that the other day and I  had no idea what's going on with Covan.  Cool excellent summary. Any questions about testnets and which ones are going to stick around which ones are probably going to be deprecated if not I think those are all the things I noted from the discussion. Somebody asked about incentivizing solo staking. I think we touched on that earlier about their anti-correlation penalties and if you abstract that or de-abstract  that would mean if you're staking on the same cloud provider you know if the majority of the network is all on aws and aws went down that there would be a pretty big  slashing event or no there would be a inactivity leak
and that's one way solo staking is incentivized. There are other maybe not incentives but initiatives from people like superfiz and the east staker community to onboard more people and then Remy has also done some work with guides and in helping people understand the best practises for running your own validator guide so there's a ton of community work that's
gone into solo staking and that's probably going to continue. I don't see it stopping anytime soon because that's definitely a really great way to learn about the network and participate on your own terms with your own hardware. If anybody else has other comments on solo staking feel free to jump in.

**Micah**: Please run a minority client.

**Trenton Van Epps**: Yeah everyone of course.What is a minority? I haven't decided Micah 

**Micah**:  Not Geth and not prism so for your execution client do something that's not guess and for your consensus client do something that's not prison. You pretty much can't go wrong as long as you don't choose those two.

**Trenton Van Epps**: And this is yeah just to be clear for anybody anybody who's a validator currently or is looking to get into it soon. Prism and Geth are great clients.You
know they've been around for years. They have great people working on them. This is nothing against those teams but client diversity is really important and it's not something
where we want to. It's only an issue once it's a problem you know it's not something where it's causing a problem now but it'll be an issue. Once there's a failure to finalise or a bug in one of the majority clients. So we want to take care of the  problem now rather than down the road when there's actually a bigger problem. Anything else in the chat. Yeah somebody asked about timing and Marius rightfully answered it'll happen when it happens. Basically, yeah there's a checklist. I don't have the link on me now but maybe if somebody has. Tim's gonna get it but yeah it is hard to predict when everything happens and I know everyone in crypto is used to things taking longer than they seem that  they shouldn't take. That's kind of the way it goes . But one thing we want to be really clear on is that any upgrades are secure. You know there's no bugs and it's not going to introduce issues if it goes live. We're not testing in  production. So security and safety for the chain stability. These things are all way more important than hitting a certain deadline so the broader answer is you know the merge 
will happen when it happens. When all the client teams are comfortable when there's been enough testing. We've gone through the transition enough times and everybody is confident that  this is gonna  go through well and it's not gonna cause other issues. Oh! right there's the link.  Yeah the things in this readiness checklist aren't you know it's not like they all have equal weight so take that with a grain of salt but it's a pretty it's a good way to get an overview of the things that are being worked on with a bunch of great links to the work. What's left so if you're interested in timing this is probably your best bet for understanding when the merge is actually going to take place go ahead Tim.

**Tim Beiko**: Well yeah so one thing i'll post this in the agenda as well but Frederick at the
ef has helped set up a google group that people can subscribe to get blog posts announcements about the merge. So we will post everything on blog.ethereum.org and I think there's already an rss feed. So if you're on rss you can use that but if you just want to get a simple kind of digest of the upgrade news related to the merge. Let me share the link in the chat here.We'll make sure there won't be more than the blog post but you'll get an email
saying hey there's a new blog post. Yeah so you can just join here if you're not using  google
or gmail you can just send an email to this email that I posted at announcements plus subscribe by ethereum.org it'll reply back and ask you to subscribe. It did go on my spam the first time so please check that  but generally it should work for any email provider. If you just wanna yeah if you just want a heads up when these upgrades are published.

**Trenton Van Epps**: Someone again asked about whether infura can be used after the merge. No you should start getting used to running your own execution client. Leading up to the merge

**Marius**:  Can I just clarify that trend if you're stalking then the encouragement is to run your own execution client infuria is undecided about whether they'll provide that but that's the buy if you're stalking run your own client. If you are running a dap and you're providing a service and you just hook into the normal eth1 apis. You don't you can just carry on using
infuria or alchemy or whoever you use as you always have done.  You don't need to get involved with this side at all. If you want to run your own node, if you're currently running your own eth1 infrastructure for your dap, you will also need to run an eth2 client, a consensus client alongside that so you've basically got three scenarios there and we should distinguish them carefully.

**Trenton Van Epps**:  Yep. Yeah that's my mistake, I thought he was asking about validating, yeah just for applications or apis. You can still use infura or any web3 provider.

**Micah**:  I am assuming we've got confirmation from inferior that they are planning on
starting to run a validator client or because those clients are on their back end.  They are going to.

**Marius**: Yeah already dude. 

**Trenton Van Epps**:  We're down to the last few minutes.  It's been a lot of great discussion  and I appreciate everybody who joined and asked questions or if you're a developer. You took time to come and answer the questions. Is there anything we missed or
should quickly summarise. This is your chance to speak up. Great, we've covered everything.

**Marius**: So the thing that we've been talking about in the chat regard to unsafe head and
safe head so when by the time the merge goes live the expectation is that when you ask for the latest block, you will get what's called the safe head and the safe head is about 12 seconds behind real time ish 12 16 seconds something like that. So just be aware you can ask for an unsafe head but unsafe head is very likely to get reworked, so be prepared if you ask for unsafe head. I don't think json rpc's are available yet but eventually before the  merger should be you have to run safehead that'll give you the absolute latest and greatest . So if you're like someone doing mev or something where you absolutely need to know exactly the latest things going on. You can get that just by being aware that is likely to get reorg, high probability if you ask for the safe head or latest what you're used to getting now going to get blocks a little later than you do currently. So they're going to be delayed by 12-16 seconds or so. But on the plus side it is very unlikely that those will get rewarded. They only rearrange very bizarre scenarios in almost all cases. It's probably going to stick around to finalisation, so just be aware that things are going to get a little slower. If you continue if you just do nothing and just continue this latest and if you  want to be on the bleeding edge. You are today in terms of timing then you'll have to switch over to  unsafe head and be aware that the rework chances are kind of high with that.

**Trenton Van Epps**: Great, yeah  somebody asked where this will be recorded or where  the recording will be hosted and it will be on the ethereum cat herders youtube where the other calls have been uploaded and I think we've been producing notes for all of them. So if you'd rather read this then listen to it. It'll be available on one of the repos that we'll link to as a final final note. If anybody on the call was looking and looking to get into validating on their own or just curious about proof of stake. Generally they want to learn more about participating in consensus. I cannot recommend Super Phiz and the eatstaker community more than I can't recommend them enough you should definitely check them out. They've done great work like I mentioned earlier. You know, creating tutorials helping people understand what's required of them and yeah definitely get involved with that community. They're amazing.

**Super Phiz**: Yeah thanks I do my audio even work. I've spent the past hour fighting with my audio. So yeah it's great to be here. I can't wait to go and catch up but yeah so eastecker tries to be a welcoming first and knowledgeable second community and that's a really weird
thing for a lot of technical people but  we really just want to welcome people and help them feel comfortable getting into staking. We don't have all the answers but we will welcome you and help you figure things out as you go. So yeah we'll be glad to have anyone.

**Trenton Van Epps**: Yep and as Marius mentioned we are more than happy to have anybody help us test the merge and that just means you know joining the testnet breaking
things where they can be broken and then telling Marius how you broke it so if you're interested in helping with that , join the ethereum r d discord. If you need a link to that just dm me on  twitter and I will send you an invite link. I don't have it on hand right now but yeah 
Thank you again everybody for coming.

**Marius**: Also also uh if you're a depth developer deploy your dap on the test net to see if the dap works like the smart contract shouldn't be a problem there but also check out if your back end works. If  we make some changes to how the header works and stuff like this so
it would  advise any project to deploy their code and also test it with their back end on the new testnets.

**Trenton Van Epps**: Yes, test the merge, deploy your applications and we're gonna make it. we're all gonna make it. All right I think we can wrap there one minute over thank you again everybody. We'll see you somewhere online
thank you

 ----------------------------------------------------------------
## Attendance

* Trenton Van Epps  
* Mikhail Kalinin
* Micah Zoltu  
* Tim Beiko 
* Ben Edgington 
* Super Phiz
* Marius VanDer Wijden
* Pari
* Pooja Ranjan

## Next Meeting Date/Time : TBD


## Zoom Chat 

- 08:59:31 From  Trenton Van Epps  to  Everyone:
	https://github.com/ethereum/pm/issues/465

- 09:03:41 From  Trenton Van Epps  to  Everyone:
	https://github.com/ethereum/pm/issues/465

- 09:06:43 From  Trenton Van Epps  to  Everyone:
	https://twitter.com/ralexstokes/status/1491950188944056320

- 09:09:56 From  Micah Zoltu  to  Everyone:
	Is there a Kintsugi/Kiln faucet?

- 09:10:12 From  Marius Van Der Wijden (M)  to  Everyone:
	for

- 09:10:19 From  Marius Van Der Wijden (M)  to  Everyone:
	kintsugi yes

- 09:10:19 From  Micah Zoltu  to  Everyone:
	Testnet ETH.

- 09:10:29 From  Micah Zoltu  to  Everyone:
	Link?

- 09:10:38 From  Marius Van Der Wijden (M)  to  Everyone:
	sorry, fat fingers

- 09:10:51 From  pari  to  Everyone:
	All links can be found here: https://kintsugi.themerge.dev/

- 09:13:58 From  JHM  to  Everyone:
	Will there be possible fallback for execution layer?  This is super helpful when updating the OS etc

- 09:14:13 From  Marius Van Der Wijden (M)  to  Everyone:
	yes thats possible

- 09:15:44 From  JHM  to  Everyone:
	The second

- 09:16:13 From  apuya  to  Everyone:
	Hey

- 09:17:02 From  pari  to  Everyone:
	2 beacon 1 exec is bad

- 09:18:09 From  pari  to  Everyone:
	CL clients usually have a `failover-rpc` flag

- 09:18:13 From  pari  to  Everyone:
	You’d need to specify it there

- 09:18:28 From  Micah Zoltu  to  Everyone:
	👍
- 09:19:21 From  Samast Khanna  to  Everyone:
	gm 😬

- 09:19:49 From  Rémy Roy  to  Everyone:
	How will validators choose the Ethereum account for their transaction fees to go into, the transaction fees they will gain from proposing a block?

- 09:21:16 From  pari  to  Everyone:
	If someone has the ability and the time, please help build this: https://github.com/karalabe/minority

- 09:21:40 From  Samast Khanna  to  Everyone:
	I know this is probably available in some documentation somewhere if I search for it, but since I'm here I'll shoot:

	how would slashing work for a validator intermittent network uplink degradation? or just intermittent unplanned downtime in general?

- 09:22:08 From  Fredrik  to  Everyone:
	re: using backup EL's; on for example lighthouse you set the flag--eth1-endpoints http://localhost:8545,https://mainnet.infura.io/...,xxxx and it will use the first one, if that goes down it will use the second down, etc.

- 09:22:30 From  Tim Beiko  to  Everyone:
	@Ben, perhaps you can answer the slashing question?

- 09:23:35 From  Klas  to  Everyone:
	1. Do existing validators only need to update the execution client and beacon client or is there something else? 2. Will the hardware requirements stay the same (mostly about disk size growth at same pace as now)?

- 09:23:41 From  Marius Van Der Wijden (M)  to  Everyone:
	@Fredrik but that might change since the eth1 endpoint isn't read only anymore (you can't use infura for it anymore)

- 09:24:08 From  Ben Edgington  to  Everyone:
	There's no slashing for downtime. You will get mild penalties that are the same as the rewards that you are missing. So 1 day's downtime loses you as much as 1 day's rewards. Of course you also miss out on transaction fees.

- 09:24:14 From  Fredrik  to  Everyone:
	perhaps it's worth mentioning that technically you don't get slashed by being offline, you suffer offline penalties

- 09:24:19 From  Marius Van Der Wijden (M)  to  Everyone:
	1) both

- 09:25:26 From  Marius Van Der Wijden (M)  to  Everyone:
	2) They will increase a tiny bit from what you currently need to run both el and cl nodes

- 09:25:34 From  Fredrik  to  Everyone:
	@Marius indeed

- 09:25:50 From  lightclient  to  Everyone:
	so the leak only scales up when more than 1/3 is offline?

- 09:25:55 From  lightclient  to  Everyone:
	my misunderstanding

- 09:26:24 From  Pooja Ranjan  to  Everyone:
	https://github.com/ethereum/annotated-spec/blob/master/altair/beacon-chain.md

- 09:27:38 From  Marius Van Der Wijden (M)  to  Everyone:
	Especially in time of non-finalization the hardware requirements go up (e.g. additional 7gb per day of beacon state)

- 09:28:15 From  Ben Edgington  to  Everyone:
	My write-up on rewards/penalties/slashing https://upgrading-ethereum.info/altair/part2/incentives

- 09:28:24 From  Jemshit  to  Everyone:
	noob here, will network be down at the time of merge and transition to PoS? What happens if things do not go as expected?

- 09:29:10 From  Rémy Roy  to  Everyone:
	Even people that were *careful*, failed it. Avoid failovers.

- 09:29:14 From  Fredrik  to  Everyone:
	My numbers may be a bit incorrect, but under normal circumstances Validator that are online > 50% of the time will see their stake increase over time. With this assumption, if the rewards were set at 8% for a year, you would normally lose at most 2.56 ETH from being offline the entire year, or ~0.007013699 ETH per day offline.

	With that said, if you are using a majority client or a majority service provider such as AWS and there is an issue causing downtime for you and everybody else using the same service or software, an inactivity leak will commence. As an example, we can say that 1/3 of all Validators are offline, so blocks would not finalize. Due to blocks not finalizing, the rate of the penalty for the offline Nodes is increased and you will end up losing 60% of your deposit after only 18 days (19.2 ETH per Validator), or roughly 1 ETH per day. The reason for this is that the network will try to repair itself to be able to continue making decisions as a protocol by removing offline Validators once they

- 09:29:42 From  Fredrik  to  Everyone:
	drop below 16 ETH, and the Consensus Layer can then reach finality with the Validators that are online.

- 09:30:13 From  Marius Van Der Wijden (M)  to  Everyone:
	The network will not be down during the merge

- 09:32:06 From  Christian Gebhardt  to  Everyone:
	When merge? :)

- 09:32:10 From  pari  to  Everyone:
	Logs will just nicely show “PoW ended. Entering PoS stage” and life continues on 🙂

- 09:32:26 From  JHM  to  Everyone:
	1. Do existing validators only need to update the execution client and beacon client or is there something else? 2. Will the hardware requirements stay the same (mostly about disk size growth at same pace as now)?

- 09:32:42 From  Cem  to  Everyone:
	How do you incentivize solo staking?

- 09:32:51 From  Marius Van Der Wijden (M)  to  Everyone:
	Should we talk about "Finalized"  in RPC?

- 09:33:51 From  Cem  to  Everyone:
	And how do you motivate people to not use Infura for the execution (sorry joined just right now)

- 09:34:25 From  Marius Van Der Wijden (M)  to  Everyone:
	You can not use infura post merge anymore (at least without big changes to infura)

- 09:35:07 From  Tim Beiko  to  Everyone:
	Infura, and I don’t think any other web3 provider, doesn’t provide blocks today and I haven’t heard of any of them that plan to

- 09:35:10 From  Trenton Van Epps  to  Everyone:
	does anyone have any writeups related to not being able to outsource the execution layer? realizing we don't have a link in the agenda

- 09:35:41 From  Tim Beiko  to  Everyone:
	As a validator, if you do that, you risk the web3 validator sending you a wrong block leading to loss of funds

- 09:36:00 From  Cem  to  Everyone:
	So, I need geth running on the same machine as my validator clients?

- 09:36:14 From  Trenton Van Epps  to  Everyone:
	any execution client

- 09:36:18 From  Micah Zoltu  to  Everyone:
	Doesn't have to be the same machine.

- 09:36:30 From  Micah Zoltu  to  Everyone:
	And doesn't have to be Geth (can be Nethermind, Besu, Erigon).

- 09:37:23 From  Rémy Roy  to  Everyone:
	Geth is currently producing the majority of the blocks for Ethereum. How dangerous is this going into the merge? What efforts are being deployed to diversity execution clients?

- 09:37:25 From  Cem  to  Everyone:
	Thanks. Ok, just not a provider. So I could use a raspberry pi for exec client and another one for the consensus clients

- 09:37:34 From  Tim Beiko  to  Everyone:
	@Cem yes

- 09:37:39 From  Micah Zoltu  to  Everyone:
	@Remy Pleading.

- 09:38:10 From  PX101  to  Everyone:
	Sorry Tim, you confused me a bit with the rewards...
	Block Reward -> Consensus Layer (Locked)
	Transaction Fees -> Execution Layer (Liquid)

	Is that correct?

- 09:38:49 From  Tim Beiko  to  Everyone:
	Re: finalized blocks, the table at the bottom of this post shows the various options: https://blog.ethereum.org/2021/11/29/how-the-merge-impacts-app-layer/

- 09:38:56 From  Tim Beiko  to  Everyone:
	@PX101, yes

- 09:39:03 From  PX101  to  Everyone:
	Thank you

- 09:41:27 From  lightclient  to  Everyone:
	did ppl talk about safe head?

- 09:41:33 From  Micah Zoltu  to  Everyone:
	Not yet.

- 09:41:43 From  lightclient  to  Everyone:
	:o

- 09:42:13 From  Micah Zoltu  to  Everyone:
	IIRC:
	latest == safe head
	unsafe head (new)
	finalized (new)

- 09:42:26 From  lightclient  to  Everyone:
	flip unsafe and safe

- 09:42:29 From  Micah Zoltu  to  Everyone:
	Er, maybe we did in a previous call.

- 09:42:32 From  lightclient  to  Everyone:
	safe is new

- 09:42:40 From  Micah Zoltu  to  Everyone:
	Hmm, pretty sure safe head == latest.

- 09:42:43 From  Hamid  to  Everyone:
	As my understanding crypto exchange just need to update their node during the merge

- 09:42:44 From  lightclient  to  Everyone:
	no

- 09:42:58 From  Mikhail Kalinin  to  Everyone:
	safe head is intended to be an alias for latest

- 09:43:11 From  Micah Zoltu  to  Everyone:
	We argued in a consensus or ACD call about this IIRC, safe head == latest is far superior to unsafe head == latest.

- 09:43:21 From  Fredrik  to  Everyone:
	Rémy: there are a few different efforts to increase diversity. Some of the things I'm aware of is for example the launchpad that new validators go through which provide information about running the different EL-clients.

	some long term efforts is the client incentive program ( https://blog.ethereum.org/2021/12/13/client-incentive-program/ ), and these clients are also now being onboarded to the EF's bug bounty program.

- 09:43:28 From  lightclient  to  Everyone:
	safe basically means “i’ve seen enough attestations that i’m reasonably confident this won’t be reorged”

- 09:43:42 From  Micah Zoltu  to  Everyone:
	Yeah.

- 09:43:52 From  lightclient  to  Everyone:
	so i suppose it is prob the right replacement to latest

- 09:43:58 From  Micah Zoltu  to  Everyone:
	Estimated to be about 4 seconds after unsafe head in most cases.

- 09:44:24 From  Micah Zoltu  to  Everyone:
	Or maybe it is 8 seconds... 🤔

- 09:45:01 From  Trenton Van Epps  to  Everyone:
	if any other community members / validators have questions, please ask away!

- 09:45:06 From  Fredrik  to  Everyone:
	Rémy: oh and I forgot to mention https://github.com/karalabe/minority

- 09:45:39 From  Trenton Van Epps  to  Everyone:
	https://twitter.com/peter_szilagyi/status/1484548996169408512

- 09:45:48 From  Trenton Van Epps  to  Everyone:
	testnets possibility ^^

- 09:46:33 From  Mikhail Kalinin  to  Everyone:
	@Micah it takes unsafe a slot to become safe in general case. If e.g. attestations are received only via blocks and attestation gossip is disabled to save bandwidth

- 09:46:48 From  Micah Zoltu  to  Everyone:
	So about 12 seconds behind?

- 09:47:21 From  Marius Van Der Wijden (M)  to  Everyone:
	Safe head -> latest will break soo many mev searchers :D

- 09:47:24 From  Mikhail Kalinin  to  Everyone:
	yes, 12 seconds is for sure. it also includes a time require to propagate a block in the next slot

- 09:47:47 From  Mikhail Kalinin  to  Everyone:
	is to be sure*

- 09:48:01 From  fuscheman  to  Everyone:
	Sorry guys, I just got in. Have already mentioned anything about the timing of migration? if it is still scheduled for q2 of this year or if it has been delayed a bit?

- 09:49:10 From  Marius Van Der Wijden (M)  to  Everyone:
	doesn't make sense to commit on a schedule atm, but no major issues have been found

- 09:51:38 From  Tim Beiko  to  Everyone:
	Yes, the rough “schedule” is “launch Kiln” -> “merge existing testnets” -> “merge mainnet”, and we want to make sure at each step that everything works as expected.

- 09:52:49 From  Tim Beiko  to  Everyone:
	Readiness checklist: https://github.com/ethereum/pm/blob/master/Merge/mainnet-readiness.md

- 09:53:28 From  fuscheman  to  Everyone:
	thanks guys!

- 09:54:00 From  Samast Khanna  to  Everyone:
	thanks!

- 09:54:05 From  Micah Zoltu  to  Everyone:
	@Marius is "safe head" and "unsafe head" a valid BlockTag for JSON-RPC?

- 09:54:11 From  Tim Beiko  to  Everyone:
	https://groups.google.com/a/ethereum.org/g/announcements

- 09:54:17 From  Tim Beiko  to  Everyone:
	announcements+subscribe@ethereum.org

- 09:54:25 From  Marius Van Der Wijden (M)  to  Everyone:
	no

- 09:54:35 From  Jemshit  to  Everyone:
	will everybody who depend on infura have to run their own node after PoS?

- 09:54:38 From  Micah Zoltu  to  Everyone:
	Is that planned, just waiting on a spec?  Or was there some reason that didn't make it in?

- 09:54:46 From  Tim Beiko  to  Everyone:
	@Jemshit yes

- 09:55:51 From  Jemshit  to  Everyone:
	For Api, dapp

- 09:56:23 From  Guang-Yi  to  Everyone:
	Thank you guys!!

- 09:56:30 From  Marius Van Der Wijden (M)  to  Everyone:
	Afaik "latest" should provide the "safe head" (according to spec). Right now we return the unsafe head on latest :D

- 09:56:39 From  Micah Zoltu  to  Everyone:
	/tableflip

- 09:57:06 From  alexiskef  to  Everyone:
	Huge THANK YOU to all you guys!

- 09:57:51 From  Klas  to  Everyone:
	Thanks all! Where will recording be? I missed last 5 min

- 09:58:01 From  Trenton Van Epps  to  Everyone:
	cat herders youtube

- 09:59:05 From  apuya  to  Everyone:
	POAP?!

- 09:59:23 From  Marius Van Der Wijden (M)  to  Everyone:
	Join TestingTheMerge! to help us test the merge ;)

- 09:59:41 From  Trenton Van Epps  to  Everyone:
	no POAP, sorry

- 10:00:07 From  apuya  to  Everyone:
	Oh, Thanks

- 10:00:35 From  PX101  to  Everyone:
	Very informative call. Thanks for taking the time.

- 10:01:24 From  fuscheman  to  Everyone:
	thankss

- 10:01:26 From  Christian Gebhardt  to  Everyone:
	Thanks!


