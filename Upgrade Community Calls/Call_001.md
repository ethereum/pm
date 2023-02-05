# Shanghai/Capella Community Call #1 
### Jan 20, 2023, 15:00-16:00 UTC
### Meeting Duration: 1 hour 
### [GitHub Agenda](https://github.com/ethereum/pm/issues/708)
### [Video of the meeting](https://www.youtube.com/live/uTWpSYn4MA8?feature=share)
### Moderator: Tim Bieko
### Notes: Alen (Santhosh)


**Tim**
* Good morning, afternoon, everyone, depending on where you are. first Shapelle community call. so I guess, these are helpful to just like, answer people's questions about the upgrade. we started doing them with the merge and, given the introduction of withdrawals, yeah, it makes sense to, do them as well so that validators and, and just node operators and infrastructure providers could come and, and ask questions. didn't have too much on the agenda today. I think,  if we have Danny and myself here, we could maybe both give a quick overview of like the entire upgrade so you get withdrawals, but there's a couple more things as well. 
* Then maybe go quickly over like the withdrawals faq, and, and just like show that it's there and what type of questions it answers. And, if folks here have questions, we can spend most of the, most of the call on that. but yeah, I guess to maybe to kick it off. so Shanghai, obviously, as I just said, the biggest, biggest thing, that's covering are withdrawals and we can, we can dive into those in, in quite some detail. after, there's also three other changes that will be included. So, Coinbase address, will be re-priced when you access it. so this is just a small gas cost change.Push zero is a new up code that's coming in. So, which as it, as the title says, pushes zero onto the stack. so you can get some gas cost savings by using that if you develop smart contracts. 
* And then, maybe the change that affects, smart contract developers, the most is, this limiting and, gas metering of init code. so previously, or I guess currently still on mainnet, init code is not, limited beyond I think the entire contract size. so this adds a specific cap for theit code and also adds, gas costs, for every, basically two gas for every 32 bite, of 32 bytes of init code, in a contract. So that will change kind of gas pricing, with regards to contracts. but yeah, outside of withdrawals, that's what there is on the EL. I don't know. Danny, do you want to quickly share on the CL Yeah. 

**Danny**
* So on, we'll do the non withdrawals. in the consensus layer there is what's called a double batch me Merkel accumulator. Essentially you take, blocks, block routes and state route, and you put them into lists. And then, every once in a while, once those lists get full, you hash you, you do a Merkel route of each of those lists, and then Merkel lies those.
*  And so you have a single route and you put that into a list, itself, the, these initial can be cleared, so they don't grow unbounded, whereas this like double batched list, does grow unbounded, but like on the order of 10 kilobytes a year. But this allows for like succinct, historic access forever. This exists, it's been, in the beacon state since phase zero, but because of the way the, state roots and the Merkel roots are kind of like hashed in the single list, if you wanna prove something about blocks, you have to have like a little state route. 
* You have to have this additional route to prove things about blocks, and if you wanna prove things about states, you have to have this additional route to prove things about blocks, about state. so because of that, some of the historic serving that we wanna do against states is not quite as clean as it needs to be. 
* Thus, that's being refactored and revamped a little bit such that we have two, we kind of like keep those two pieces of information, the historic summary  that batch of block roots and that batch of, state roots as independent instead of smashing 'em together into a single route. this was led by Sik and should help with succinct serving of historic stuff, cleaner serving of historic stuff, very technical. 
* It helps with, you know, state sync and other things like that, that probably as an end user you won't end up, really, really having much of an impact on you. I think that's the only change other than the withdrawals, which are obviously, one of the main reasons we're here. 

**Tim**
* Yeah. so do you want, I guess Alex is not here, but yeah, do you want to give maybe an overview of, I'm not sure if it's like the right, the right Point. 

**Danny**
* Yeah, I talked about like the validator process and how that we're kind of, that's being extended and then get into the technicals from there if people have questions. 

**Tim**
Yeah, let's do that. 

**Danny**
* So, as you know, validators can deposit and become activated. There's an activation queue. Normally it's pretty empty, sometimes it can be long. Similarly, today already you can exit and then if you, if you initiate and exit, you go through, the exit queue, you're not done validating, you still get roles and duties until you're on the other side of that queue. Normally it might take on the order of like four epoch, it could back up on the order of months if like half the validator set was trying to leave once. 
* So you can exit today and then your validator is no longer active. but your phone's kind of sitting limbo. So what this upgrade primarily does is completes the circle and brings, allows for, both kind of the principle 32 E balance and the validators rewards to go back into the execution layer back into the kind of normal user layer, normal Ethereum accounts, out of the beacon chain. And there's two primary methods. You know, I talked about how you can exit. 
* So obviously once you exit, you probably want your, your ETH back. So all of your balance, 32 eth plus any awards or 32 eth minus any penalties, once you get out of the exit queue. 
* And once you go through the men validator withdrawal ability delay, which is 256 epox, which is 27 hours. So exit queue plus 27 hours, now you are withdraw. and on some sweep, you know, there's a certain number of validators 16 per block that can, go back into the execution layer. it's a round robin sweep. your funds will eventually be picked up and put into the execution layer. There is another method, of withdrawal called partial withdrawal. 
* And this is if you are active and have balances in excess of 32 eth, so you have some rewards on that account, the rewards in excess of 32 eth, in that same round robin process, will be sweeped and swept and put into the execution layer. That's the mechanism at its core. There's one big caveat and that is there are two types of withdrawal credentials. If you set up a validator, you know, you have an active key and a withdrawal credential. at Genesis, the only available withdrawal credential was called the 0x00 BLS withdrawal credential. 
* So you have a BLS key essentially that controls the ownership of the funds, not the active, not the active key. if you have such a key, you don't have a, essentially you haven't not elected a destination in the execution layer for your withdrawals to go to. So, if you have a 0x00 key, initially you will not be a part of partial withdrawals. And if you exited and you were with withdrawable fully out of that queue and passed that 27 hour window, your funds would just kind of sit there. 
* So there's a new message type called BLS credential change, BBLs Change Operation, something like that. BLSQ change operation. I apologize for not having that on the top tip of my tongue, but there's a new operation, that tools like the staking and CLI and Eth do allow you to essentially convert your BLS withdrawal credential into a execution layer withdrawal credential. So it goes from 0x00 version to 0x001, and essentially it's a one time operation in which you sign a message with that BLS key, to say what I want the ownership of these funds to be on the execution layer. So it's essentially taking a BLS key and,  electing permanently your execution layer address, your normal Ethereum address that funds will go into. 
* So once you do that, if you're active, you'll now be a part of that partial withdrawal suite. So any balances in excess of 32 eth, we'll go in there. So, you know, if you have a couple ETH that you've earned over the past couple of years, you don't have to exit to get those funds. You just have to do the change operation if you ha don't already have that type of key. And again, at that point, if you exit and become withdrawal, your, all of your funds will go into that execution layer address. 
* Similarly, if you're already exited or if you do the operation in the other order, you exit and you wait for a while and then you do your BLS change at that point, you'll be part of this week. So that's probably one of the very important things I understand here is that your validator will essentially continue to operate as it is today if you have a BLS credential until you, elect to sign that message. 
* And so a very important thing is kind of the UX and safety around signing. 
* You know, you can use that staking CLI tool, although you have to use an upgraded version, that you may be used to deposit. There's also a great tool called that a number of, security auditors are taking a look at right now as well, that we've been using and testing and, and it has an ICU X to do so. and then the, the step from there is to go to your client of choice that you run, you know, your node software, and there will be some sort of interface, some sort of, tutorial, some sort of guide on how to take that message, load it into that machine so that it gets broadcast the network and, picked up into a beacon block. 

**Tim**
* Question, There's a question from Trent in the chats. Are there any good tutorials, that people can follow to do this? 

**Danny**
* Great question. I was looking at the new, staking faq, which we can take a look at in a minute. which does link to, I believe it links to how to do it in and then it is cataloging the docs from the various clients on how to then take that message and put it into a client.
* I believe we might be at like three or five or four or five clients that do have this documented, and that's a very high priority for them to get over like the next week. the staking CLI last I checked yesterday, there is a work in progress PR to add this functionality. and  I would suspect that's also done probably next week. So at least taking CLI tutorial guides will also be updated as that's completed. 

**Tim**
* Okay. two more questions. So one from YouTube, and the these, by the way, don't all have to be for Danny. If you're on the call and you have the answer, please feel free to jump in. but yeah, from YouTube I recently came across EIP 4 36 consensus layer withdrawal protection. Can somebody please explain this a little bit more? 

**Danny**
* I only have a cursory understanding of this. I would, you know, if somebody else does, please jump in cuz I cannot do justice. I'll at least give the background. Yeah. there's certainly some fear that, some people might have their keys compromised, whether they, you know, expose them in the clear somewhere or some sort of mishandling in key operation, in the past couple of years. 
* And so there's the worry because you have to do this change operation. there's a worry that, you know, there's a race between you and an adversary, somebody who hacked your keys, and if the adversary gets their message on first, then you have, you know, they essentially get to finalize the stealing of your funds that maybe they've been trying to for a while. 
* I believe that this EIP is a standard to do some sort of, you know, identity verification with large operators to, to essentially put your key into their pool, early rather than hoping, you know, and, and racing against time said, I do not, you know, this is an attempted kind of social solution to try to give the correct owners of funds rather than the hacker, the ability to change their, their key. but I do not know how the details of, of how they intend for this to work. 

**Tim**
* Yeah. And Pooja, shared in the chats, there's a PEEP and EIP 4735 that's happening, in two weeks Feb 01, and it should be live, a week after that with the recording. and so for the people who don't know PEEP EIP are like hour plus long deep dives into the specific EIP  with the authors. 
* So, yeah, keep an eye out on the Ethereum Cat Herders, for that one it comes out. Christine, you had a question about public dashboards tracking the withdrawal credential updates, for the withdrawal credential sweeps. there was, answer in the chat. Barnabas, do you wanna maybe give some, some details there? 

**Barnabas**
* Sure. so the current, stage is that we are working together with the beacon chain and the box block scout, and they both are going to be able to provide a nice visual interface where we can see which validator has withdrawn or which has not. And also, we can change, there will be a way to see how long it's going to take till the next sweep. This could come into your validator. 
* So it is upcoming and, we do have a working beacon chain right now for the running Devnet. So it's the, the latest it's running on it. That's where all the development is happening right now. 

**Tim**
* Awesome. couple more questions from YouTube. so I'll get through them in order. Is it accurate to say that the withdrawal message expires after two hard forks? 

**Danny**
* This is that, change the spec validator the other day that Marius didn't understand - It's very complex. I'm just poking funny at you, Marius. the answer is no. This was a, a change to the spec recently, to essentially sign the message in a very generic way, with the Genesis fork version. So that is valid for all forks. 
* This is  as opposed to how, like say attestations and even exited exits are signed where they're very fork specific and they kind of degrade across fork bound boundaries. so the good thing here is once you, once you have a tool, it will work period. 

**Ben Edgington**
* Ben, So, so Danny, I, that's covers the credential change message. I think we agree to use the Genesis four version, but the withdrawal message remains signed with the fork version, right? So that expires The exit. 

**Danny**
* Yeah, and I, I know the terminology is kind of clear. Sorry, the exit Unclear. Yes, you're correct, Yeah, but no, but, but you're right, the message I was talking about wasn't a withdrawal message as well. So there are exits and there are key changes. 
* If you're exited and you have your, on your key change, you will be withdrawn. So, so yes, Ben, the, the exit, which is actually maybe a more akin to withdrawal message, does degrade over those two epochs, and I don't suspect that's something that is changed, although it's been discussed, it won't be for this fork. it's something that's kind of been discussed lately here and there. 

**Tim**
* Okay. okay, another question about the, the two cues, and this is something that's like comes up, I get a DM about this probably every day. so can you please cover what order the withdrawal queue and sweeps are processed? So I think basically the, I think the interaction of the exit queue and the withdrawal sweep, we probably need like some sort of animation for this, but Danny, do you wanna Yeah, Right. Yeah, expand on That. 

**Danny**
* So there's an activation queue, you are active, then you submit a voluntary exit and then you enter into the exit queue. The exit queue is, you are still active while you're in the exit queue, you still have duties you can still make, you can still, gain and lose rewards based off of your attestations and proposed performance.
*  On the other side of the exit queue, you are no longer active, but you are not yet withdrawable. There is the men validator withdrawal ability delay. It's 256 epochs, that's about 27 hours. So you're out of the exit queue, you are exited, you then have a 27 hour delay and now you are with Drawable At that point. 
* You are part of the, you can be part of the withdrawal sweep, which is round robin, so you know, if the last, if you're a validator 32 and on the last block it left off at 31, then you're the next one in the week if you're validator 32. And the, last block it left off was at 64, you're almost at the end of this week is gonna go all the way to the end and then back at the beginning. So exit Queue with all ability delay, then round robins sweep clear as day, right? Yeah. 

**Tim**
* Someone says we should call it limbo when you're exited waiting  to be withdrawn. 

**Ben Edgington**
* Yeah, it's not, it's not very long limbo. Right? I mean, even if every, even if every validate has 0 0 1 credentials, which they don't, at the moment only about, 40% due,  it's will still take I think four days to complete a whole sweep through the entire validator set. 
* Yeah. So once you are exited, you've got a maximum of four days and probably much less, to wait until your funds appear right, A maximum of five days because of the men validator withdrawal ability delay, which is 27 hours. That that only applies if you've only just deposited. Right. once you've been running for 127 hours, that that no longer applies. If I remember correctly. 

**Danny**
* You might be correct. I need, I need to double check. I'm Very wrong. 

**Ben Edgington**
* Yeah, it's just for some people, becoming active and then becoming inactive straight away. yeah, but once you've been running 27 hours, yeah, You, you're good. 

**Danny**
* I think you're right. 

**Ben Edgington**
* I'm gonna, I, I wrote about it somewhere. You can, you can, you can take a look. 

**Tim**
* Okay. one for the EL side as the, oh, you, I think you're wrong. That was quick. 

**Danny**
* Yeah. the withdrawal epoch is set as the validator dot exit epoch plus men validator withdrawal ability delay. So I believe that, you there is the, the delay there. 

**Ben Edgington**
* I see it corrected. 

**Tim**
* Okay. Next one, Lightclient clients, because you dare to answer in the chat, so we're gonna get a full answer out of you. the question is, is, can you provide information, that explains the new block format and, how to detect withdrawals on the EL? so, yeah, like Lightclient, you maybe wanna just give a quick overview of how the ELs block, how the EL blocks change with withdrawals and maybe also like, this idea that like withdrawals are processed as like an operation and not a, a transaction itself. 

**Lightclient**
* Sure. Yeah. So, you know, the EL block header changes to include a commitment to all of the withdrawals that go into the block, and that commitment is very similar to some of the other things we're committing to, like the transactions in the block and the seats in the block. 
* So that's just adds the block header and then the actual block body that is sent over the peer to care network is extended to include the withdrawal objects. This just lets us get them from our peers when we're syncing so that we can store them and and send them over the JSON RPC if someone requests information about them. But they generally originate from the CLs over the engine api. They are just added to the, the calls that seed the EL with a new, new block information. 
* So it just extend to also support that withdrawal format. The withdrawals are slightly different than transactions because they are operations and they are, not really validated much of the EL layer. They're mainly just given to us by the CL. We verify that, you know, the withdrawals route matches the same thing in the execution payload, but we don't check any of the, conditions about if the validator is properly withdrawn or if the index of the withdrawal is correct. And so we just processed those withdrawals exactly as the CL gives them to us after we process all the transactions in in the block. 

**Tim**
* Okay. thanks. We'll see if there's follow up questions about that. next question was, there was like a couple questions on like testnets and like the order and timelines. I think like the higher level answer is like, we haven't made a decision yet. so I'll take all of this with a grain of salt, but generally, what, client teams were, we're thinking about is, we're, we've launched a bunch of, dev nets and, and are, are still launching some, to testings. I think when things are a bit more stable probably in the next week or so, we plan to launch a longer lived new testnet to allow people to, test withdrawals and, and other Shanghai Capella stuff on it. 
* Kind of like we did for the merge, we had, kintsugi and, and Kiln. and then I think a couple weeks after that, assuming we don't find any issues that things work as,  we expect them to, we would move to forking the, the different, existing testnets of Gordi and sepolia. we don't quite have a decision around like which one we would fork first. sepolia is generally easier to fork because the validator set is, is closed. so anyone can sort of, or sorry, not anyone can be a validator on sepia and it's easier to coordinate that fork. that said, Gordy is like a better test for main net, because, home taker can also, stick on Gordy and see how things go there. 
* So which of those two comes first? I think we'll, we'll need to, to decide, but we'll have them happen usually within a couple weeks of each other. And then assuming those go smoothly, there's no issues, then we'll schedule main net, for a couple weeks, after that. 
* So I don't know how that lines up in terms of, of of dates, but I think in terms of just like the steps we need to take, yeah, that's, that's basically it. launching a new kind of long quote unquote lift, definitely DevNet, that, that people can try forking sepolia and Gordy TBD on the order. And then once all of that is stable, then we'd, we'd move to 14 mainnet. another YouTube question was, is there a way to access or retrieve the complete withdrawal Q State including your position in the queue for a full withdrawal on the Ethereum blockchain? Yes, I, one more. 

**Barnabas Busa**
* The Beacon Chain Explorer will keep track of it. So you will see when, it's going to be your Okay. 

**Tim**
* Beyond the Explorer. Yeah, the node doesn't track it by default. 

**Barnabas Busa**
* Yeah. But the BLS pool is public, so the BLS pool, every node is So as soon as you publish your own, BLS changes and it's going to be the same kind of way as  swept in the same fashion as the partial visual. 

**Tim**
* Okay. sweet. next one was, someone said there's a translation subtitle function in Zoom that we haven't activated. I did not know that this was a thing. but yes, I can look into it for the next call. for sure. if you wanna send me like a link about that, I can try to see if we can, we can activate it. 
* Okay. no other questions in this chat. there was one more on YouTube. can you please elaborate a bit more on the change from 0xo to 0x1, since 40% already have 0x1 one set, would it take, would it take four days to change everybody else, to the credentials to, to cycle through the credentialed updates? 

**Danny**
* Yeah, I believe there are 16 of these operations that can be included on each, each beacon block. So each non induced slot, which generally, you know, that's 99% of slots. so yes, it'd be 60% of 4.3 days, would be how long it's gonna take. So, a few days. And that's, you know, we don't know how many people are gonna be doing this immediately at the fork, or doing it over the course of, you know, a few weeks, a few months. So, you know, we shall see. 

**Tim**
* Okay. different, withdrawal question. so, basically they're still interested in allowing exits using only withdrawals credentials. there was discussions about this on forums and GitHub over the past year, and this is something that would be, helpful or critical for, liquids staking providers, where you can initiate exits from the execution layer. Anyone have an update on that? 

**Danny**
* I know there are a couple proposals in progress to do 0x01, you know, withdraw credential triggered exits. and so we could have smart contract triggered exits, which would, help make a number of these like different pooled operations, more trustless. my gut is that there's an appetite for these, but there's not a full proposal nor, you know, a governance kind of discussion around that yet. 

## Withdrawals FAQ [31.26](https://youtu.be/uTWpSYn4MA8?t=1886)

**Tim**
* Got it. Okay. And I think that's pretty much all the questions, at least I see right now. so maybe before we have sort of client chilling, it's sort of going over this specifically. We have this new withdrawal faq, that, the DevOps teams and some other folks, at the EF put together. I won't read over everything, but it does cover like pretty much everything we've discussed so far as well as much more technical details. so the, URLs note side.org at launchpad slash withdrawals faq, it's linked in the agenda for this. I think this is probably the main thing, like for people who, want to understand the process in more detail without, reading the actual spec line for line. I think this, this gives  a good overview. We'll keep updating this in the coming weeks. I think, if there are questions that people would like to see here but that aren't there, you can either post them in our Discord. I mean, if you tweet them at me, I'll make sure that they get added here. But, the goal is that over it a couple next couple weeks and, and months, we have this as like the comprehensive, FAQ for withdrawals. 
* Yeah, let me check the YouTube Actually, I can't check the YouTube chat anymore. I'm sharing this, but any questions about the FAQ itself? Oh, okay. Oh, there's one more question on YouTube. Is it accurate to state that slash validators leave the queue before those who request voluntary exit The exit queue? 

**Danny**
* No. If you're slash you're put into the exit queue, but you can no longer receive rewards, even if you continue to try to do your job, and will lose money while being in the exit queue. so no, the exit cannot be subverted by slashing. 

**Tim**
* Got it. 

**Danny**
* And then the, once you become withdrawable, which if you're slashed, I believe there's a much larger delay put on you because there's kind of like this trying to see all the amount of people that were slashed in the same time period. But once you are withdrawable, any remaining funds are put into the normal round robin sweep, so it will take guaranteed longer to get your money out if you slash yourself than if you do a normal exit. Yes. 

**Tim**
* Barnabas, Do you want, do you wanna answer? Do you wanna repeat the question? 

**Barnabas**
* Yeah, Yeah. The execute six months long. Okay, go on. Yeah, if the queue is six months long, then you get slashed, then you will leak it till the exit queue clears. So that Correct is not a good time to get slashed. 

**Danny**
* Correct. And that's one of the primary reasons it is that way because if the execute was really long and maybe people hadn't been slashed recently, you could try to like subvert the system and kind of get around the queue, through that mechanism. So it's certainly supposed to be not incentive compatible to take that path. 

**Tim**
* Okay. sorry, reading the chat here. okay. Anyone have an update on MEV Boost? Basically, and yeah, I guess none of them are on. Oh yeah, please. 

**Marius**
* I think from what I've heard, MEV Boost will be able to, like will support the folk and they are working on, like supporting withdrawals and, and will hopefully be ready fork date. So yeah, tthey're working on it, but unfortunately they are not part of this call. And also yes, there's a disconnect between the Discord devs and the Flash Bots team. Yeah. 
* Yeah. And we can, which is like the maintain, like one of the maintainers of  MeV Boost. Yeah. 

**Tim**
* We can try to get some me v Boost maintainers, at the next one of these and, and go over it in more detail for sure. Yep. 

**Christine Kim**
* Do you guys think that, like is there any like Eth devs focusing on MEV or is it really just kind of like the focus of Flash Bots? I'm wondering if there's kind of like people dedicated to MEV on the Eth core dev side, aside from like research stuff like PBS, but more like actual implementation stuff, like is that a priority in your guys' mind? 

**Tim**
* Oh, there definitely are people. So I mean, you know, first I think the, one of the biggest example like Thomas, like the CEO and founder of Nethermind, is also part of Flash Bots, and has been for like, several years now. So I think, there's, and there's other developers, you know, I think Light client I believe might still be a maintainer of MEV Boost if he, if not, he was definitely wanting to pass. 

**Danny**
* So like, yeah, Alex's Justin Trag is, yeah, so there's a number of, there's a number of maintainers that are not flash butts on MEV Boosts, you know, rig, the Robust Incentives group spends quite a bit of time not just thinking about pbs, but thinking about, issues that emerge from MEV. I think in terms of like the development right now, primarily MEV is handled through that m e Boost mechanism, and so I think, there are touchpoints from the core developers on that. but because any sort of like native L1 one mitigations are not what's happening in the next couple forks as far as I can see, you know, it's not a ton of depth focus on it right now. 

**Marek**
* In Nethermind, for example, we, not only have client developers, but also MEV Boost maintainers like Sarah Lu for example. So we are working close with Flash Bots team. 

**Tim**
* Yeah. And yeah, definitely we can cover just in more details on, on the next call. Yeah. Any other questions? 

**Christine Kim**
* This also isn't a withdrawals question, but I'd be curious to know kind of, updates around like client development. it sounded to me like the ELF stuff was, sort of maybe not the EF stuff, but like the harmonization, I think between EL, CL block headers was like partially to support like clients and wondering if like there's other blockers for like, client development, like what's the status on that? Can any of the Eth devs like update on that on like a summary of like client development and, some of the protocol level changes that need to happen to make, to like, I don't know, help that initiative? 

**Tim**
* Marius? 

**Marius** 
* Sure. So, gas used to have a working light client for a really long time, which was not enabled by default, but which was, kind of supported. The problem was that  it wasn't compatible with a merge. And, so there has been a, big initiative to make the Geth light client compatible with a merge. one issue with the, with the Geth light client is kind of that you, you have to trust the light server. 
* So, the, , like, there are people that run light servers and the light clients connect to those and you like, it's not a trusted relationship, between light server and light client. And, this is something that, we can only really get with, with worker, because otherwise it's kind of too much computation to, actually verify everything. but yeah, with the new,  we have Beacon chain light clients and we have, now also  a geth light client. And the idea is that, can run the Beacon chain light client with the guest light client and, everything should work fine. We, have a working demo, but it will take, I think some more weeks, maybe months to, to get it in a state where it's actually, usable by, by the, by the community. 

**Danny**
* Right. So, Nimbus think are very active in, specifying and developing on Beacon Chain Light clients portal network, is in a very kind of like alpha state as at the end of last year for serving, historic execution layer blocks, but doing integrations that help with, trustless getting, the data needed for beacon chain light clients is, is a high priority for them this year. Additionally, good smart contract beacon chain light clients are very high value item. you could kind of use the sync committee construction pretty easily, although there are a couple of teams that want to do a much higher security construction, and are attempting to  either the entire beacon chain or at least the entire FFG core kind of consensus part of the signatures. so I'm actually expecting some pretty like good, like client smart contracts this year as well. in terms of the harmonization effort, that's an important effort to kind of reduce this. the case in which I've, I've lightly synced the beacon chain.

* I need to insert a block header into my, execution layer. it would be much cheaper and kind of easier to do that with the harmonization, although it's not impossible to do so. and it's still in like a, a trustless manner today. You just kinda have to download more data. so that's an important, I think, iteration, but it does not block like clients from coming online. 

**Tim**
* Okay. any other questions? If not, we have a couple of client teams here. do y'all wanna take a couple minutes to talk about what you've been working on for Shanghai Capella, why people should use your client? Anything special? They should be aware if they're already using their client? yeah, Marek. 

**Marek**
* Yeah, I, can start. So you can try, Nethermind. If you want to have a very quick synchronization mainnet only a few hours. if you want to support, execution client diversity because we are still minority client, you can use health check plugin, which is making staking even easier and help with you with monitoring the note. you can write your, custom plugin. we will, we have, good performance if JSON, with JSON RPC Yeah. And Generali, I will send you a couple of links. 

**Tim**
* Cool. Any other team? 

**Ben**

* Good. We're in good shape. Shanghai, already I believe that we are doing most of the heavy lifting on the latest DevNet, correct me if I'm wrong, but I think Teku is running 75% of the validators, and, looking strong. couple of recent things. we've finally got doppelganger detection implemented, so that will be coming out in a release very soon. bring us in line with the other consensus clients and coincidentally with Nimbus who works, on exactly the same feature completely independently. we are forgetting historical consensus blocks. So we have a new minimal node, which means that, once blocks get, outside the, minimum mandatory retention period, then you, you no longer store them in the database. 
* So that keeps your, consensus client database down to, I dunno, be something like 30 or 40 gigabytes. so very low footprint, on, on that is optional. you can store the history back to Genesis if you wish to do so. yep. So that, that's, that's Teku. 

**Tim**
* Awesome. Any other team here? Okay. Marius, do you want a few moments for Geth? 

**Marius**
* I don't know, I think it's, it's very important to have plant diversity. but it's also Geth is a pretty good client and we are in a really good spot, with regard to withdrawals and yeah, so run our client if you want a really good client, but also consider running maybe some of the lesser known clients. Thank you. 

**Tim**
* Thank you. okay, I think that's pretty much everyone. and oh, actually one final thing before we, close out Pooja, do you wanna talk about the, the node operator survey? 

**Pooja**
* Yes. Thank you Tim, for that. So as we know that client diversity is one of the important focus of Ethereum blockchain, we would like to have a diverse network share on the blockchain. even Marius has just mentioned Geth is doing great, but we would like to have other clients considered for running Ethereum node. So if you are running Ethereum node, whether it is on execution level or on the consent level, please consider responding to this client diversity survey. 
* This is a way of collecting your thoughts and we will share this with the Ethereum client team. So if you have anything to say positive about the client, do mention it. If you think that there is a blocker, in the present client that you would like to be fixed, so you can adopt that and run your Ethereum node, please do mention. So yeah, it would be great to hear from you. Thank you for taking our time to consider this survey. 

**Tim**
* Thank you. anything else before we wrap up? Okay, well, yeah, thanks everybody for coming on and, yeah, we'll probably have another one of these as we get, we get closer to, upgrading test notes and, and whatnot. yeah, see you all soon. Bye bye. 

-----------------------


### Attendees
* Tim Beiko
* Danny Ryan
* Pooja Ranjan
* Marius
* Koichi
* Ray Shi 
* Rony
* Lyutskan
* Cody
* Langers
* Marek
* Barnabas
* Roberto B
* Dainel
* Trent
* Daniel Celeda
* Abdel
* Sungjun won
* Gabriel
* Alexey

