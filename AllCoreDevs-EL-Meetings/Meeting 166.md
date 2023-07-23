# Execution Layer Meeting #166
### Meeting Date/Time: July 20, 2023, 14:00-15:30 UTC
### Meeting Duration: 1 hour 30 minutes
### [GitHub Agenda](https://github.com/ethereum/pm/issues/834)
### [Video of the meeting](https://youtu.be/pTWm4EyStYg)
### Moderator: Tim Bieko
### Notes: Alen (Santhosh)

| Decision Item | Description                                                              | 
| ------------- | ------------------------------------------------------------------------ | 
| 166.1 |**Deneb/Cancun Testing Efforts** Parithosh Jayanthi mentioned developers ran into issues with tooling, specifically around the use of Blobscan, for Devnet #7. Blobscan is a blockchain explorer for viewing blob transactions. Though the tool was not able to capture data from the very beginning of Devnet #7, developers plan on using it for the genesis of Devnet #8. Devnet #8 unlike previous developer-focused test network for Dencun will feature testing for all Dencun-related EIPs. Full specifications for Devnet #8 can be found [here](https://notes.ethereum.org/@ethpandaops/dencun-devnet-8).
| 166.2 |**Devnet #8 -  Nethermind (EL)** The Nethermind (EL) team has merged all Dencun-related EIPs to a new release except EIP 4788.
| 166.3 |**Devnet #8 - Erigon (EL)** The Erigon (EL) team is working on merging several EIPs, with a focus on EIP 4788 and EIP 6780.
| 166.4 |**Devnet #8 -  Besu (EL)** The Besu (EL) team is also focusing on merging EIP 4788 and 6780. Other EL-focused EIPs are ready to be merged pending a few specification clarifications.
| 166.5 |**Devnet #8 -  The EthereumJS (EL)** The EthereumJS (EL) team is ready for Devnet #8 pending a specification clarification around new block payloads. 
| 166.6 |**Devnet #8 -  The Lighthouse (CL)** The Lighthouse (CL) team is in the process of doing final reviews on their release for Devnet #8.
| 166.7 |**Devnet #8 -  Teku** The Teku (CL) team is also ready for Devnet #8 and working on implementing a new publishing API for supporting optional broadcast validation.
| 166.8 |**ERC Repository Split)** On ACDE #164, developers discussed splitting ERC proposals from EIPs in a separate GitHub repository. As background, ERC are application-level standards for Ethereum such as ERC-20 and ERC-721, which dictate standards for the creation of fungible and non-fungible tokens, respectively. EIPs on the other hand have traditionally defined code changes to the core protocol of Ethereum. Danno Ferrin and Lightclient have co-authored an EIP to formally split out ERCs from EIPs to their own separate GitHub repository. According to Ferrin, the split is meant to nurture more tailored governance processes for both ERCs and EIPs.

# Intro
**Tim Beiko**
* Okay, welcome everyone to ACDE #166. so we have a lot of, basically PR updates, reviews, and then there was some, process stuff, around, the whole ERPC, conversation. And then, naming, just a shout about naming the next upgrade. I guess maybe to start, does anyone want to give an update on the state of Dencun, devnets and implementations? 

**Parithosh**
* Yeah, I can go, with that, we still have devnets. I've been up and running. we're updating the tooling a little bit, but, BLOB scan is supposed to work. Now the issue is that, it took so long to get it working on our infra that we've already started expiring. The old blobs, like the first couple of days of blobs have expired, so we can't index, the beginning few days and blob scan doesn't support, starting indexing at later stage.
* So we wanted to ask which clients already support, like an archive mode, and I think teku who already messaged with, with the flag that they use. so we're gonna be doing that, but we can't do anything about DevNet seven, so we're gonna have that for DevNet eight onwards. besides that, we did a tiny shadow fork of Sepolia this week.
* It doesn't really mean much because there's a very small subset of clients stuff, but it already brought out maybe one or two bugs in Genesis that, that we deal with and we're still getting the tooling up. So we'll do like a bigger analysis of how things are going, how lops perform there and stuff like that over the next couple of days. And I think in terms of the next devnet, the first step is getting Hive and getting all the client images in Hive. So only then would we start, planning that next. 

**Tim Beiko**
* Awesome. Thanks. do any of the client teams want to go into detail about, some of the issues or they might have seen on their ends or like progress that they've made? 

**Tim Beiko**
* If not, I believe we have the 4844 call, next Monday as well, so we can also spend time there and, yeah, dig into the details and, and next steps around DevNet eight. I'm, I'd be curious to hear also from teams. has anyone started implementation on the rest of, Dancun EIPs? so obviously 4844 is still the main one, but like what's the general status for, yeah, for other ones, Marek? 

**Marekm**
* Yeah, so from Undermind site, we implemented, all of EIPs and, only, we haven't merged yet for 4788, but it should be merged soon to the master. 

**Tim Beiko**
* Nice. Andrew? 

**Andrew**
* Yeah, so, sorry, II'm on holiday this week. so, but I'd like to say that we, we still are catching up on, 4844. So hopefully next week, maybe the week after, we'll be able to, finish, with 4844 and, pause the five test. we've implemented a couple of other, each, I think 1153 and, one other with mCopy was it, was that M copy? Yeah, I think, the, we have, the Beacon stay through in progress and, yeah, I don't think we've done this self destruct yet.
* Not yet, but my question would be, which, like, which EIPs do we want  in, the devnet8, like all of, can, so maybe a subset besides 4844

**Tim Beiko**
* I was just on vacation as well, so my memory might be a bit old here, but I believe we said we wanted all of them. but Perry maybe correct me if I'm wrong. 

**Parithosh**
* Yeah, we wanted all of them and enough, or posted a tiny, link with what all of them means, like which commit to target, etc

**Tim Beiko**
* Awesome. Thank you. 

**Andrew**
* Okay. 

**Justin**
* Besu is, making progress on the stuff for eight. We have the beacon route, in progress. We already have the, updates to receipts to include data, gas use and data gas price. However, I just noticed that that PR has not been merged in yet. So, if we could get that finalized, that'd be great. yeah, so, pretty much same status. Oh, the, yeah, yeah, the Beacon route stuff is in place as well.

**Danno Ferrin**
* Also m copies in the stores in self-destruct is pending specification clarification, but otherwise ready to go in. 

**Tim Beiko**
* Awesome. 

**Gajinder**
* Only Ethereum Geth side we are sort of ready with the definite spec, just, small PR that is pending regarding to, fork choice update three. And also with respect to that, I mean, I opened the simplification pr, which I would like to talk about, regarding, again, the engine API method for new payloads. 

**Tim Beiko**
* Cool. Let's, yeah, let's cover that right after we finish, the client updates. I don't know if I think Geth on the EL side is the, everyone missing anyone from Geth, wanna give an update? Okay. and yeah, on the CL side, yeah, don't necessarily wanna put you on the spot, but if anyone has updates they wanna share, we can definitely, cover those as all. 

**Lighthouse**
* For Lighthouse, we've got the DevNet eight spec implemented. We're in the process of reviewing it right now. 

**Tim Beiko**
* Nice. 

**Gajinder**
* So the loadstar almost ready with DevNet eight spec, Nice And Prism side. 

**Erico**
* We are ready. The only thing that we are implementing now is the new publishing API for supporting the, broadcast validation option, but I guess it's not super important for running the devnet 8, but this is the only thing that we are working on. 

**Tim Beiko**
* Got it. anyone from Nimbus or Prism on the call? okay. anything else, on the DevNet implementation status, otherwise we can move to Gajinder PR. 

**Marekm**
* Just short clarification, should override builder flag, I guess should be added to DevNet a spec? 

**Danny**
* Yes, that's what we talked about on the consensus layer call last week. I can't remember if we talked about it on the execution layer call before. So it can easily be a no op, but it should be in the interface. 

**Tim Beiko**
* Cool. Mario, I thought you had your hand up for a second. 

**Mario Vega** 
* Yeah, this is small update. we have, test ready for obviously 4844 for devnet and 6780, which is already. M copy is ready also, but we're still working on 4788 entrance in storage, tests. but should be rain the following couple weeks. Nice. yeah. 

# Move parent_beacon_block_root in execution payload and update verification consensus-specs#3454 [13.45](https://youtu.be/pTWm4EyStYg?t=825)
**Tim Beiko**
* Okay. Gajinder, do you wanna talk about, the parent block route, engine API PR? 

**Gajinder**
* Yep. So basically in new payload what's happening is that the payload that is coming from Beacon, it now doesn't has, parent Beacon block route, but then there is a separate pattern that comes with the parent. We can block route. So EL basically then can, mandate to create the full, the full payload. But what, I'm trying to propose is a simplification, so that, you know, that, beacon blocks execution payload itself will have, should have, parent Beacon block route so that there is one-to-one correspondence between, the, data that is on the Beacon block as well as, the execution block that gets constructed out of it.
* So it, it is basically helpful in the scenarios, mostly in the scenarios of debugging. We are debugging something we want to construct, we want to run a block execution block, and we just want to extract data out of from the beacon block and so basically of course we can still marry parent, parent beacon block route from there, but I think it is quite handy and also quite clean that Parent Beacon block route exists as part of, the new payload, that we get.

**Danny**
* So there's a couple things here. Like you could either change the consensus data structure or just change the engine api. So which would require some more translation in like constructing the data structure when calling that method. we did, as I linked to in the consensus PR that you opened up, we did debate this before doing the release. it ultimately came to kind of an aesthetic sensibility. Do you do duplicate this field and thus have kind of this internal data structure self-contained or do you gather it from the outer commitment? we landed on don't do the duplication and some people thought, okay, well that's okay, but it's aesthetically nicer for it to be self-contained if it's actually a pain debugging. and the aesthetic principles have been elevated more practical principles.
* I think it's totally fine to cut another release with it. We're gonna have to add a few tests. There's an additional line of code in the validation to make sure these two things are the same thing. but ultimately I think it's fine if consensus devs or others wanted in there, we didn't have too much of a reason in either direction before the latest release. 

**Tim Beiko**
* And does anyone on the EL side have any thoughts on it? 

**Danny**
* Okay, so there's, I guess Assume seem because the longer we don't do it, yeah. Like if we have a dev net with this in there, then people are gonna create tooling for the workaround and then all of a sudden it's gonna be work to you know, it's like yeah, the longer we have it, the more people are just gonna figure out how to deal with it. 

**Tim Beiko**
* So I'd like to figure it out soon And I don't know, there's a couple CL teams on the call now, but not everyone, like can we, maybe I, is it too long to wait until next week to like have it fully agreed upon? 

**Danny**
* Yeah, I just, I wonder when DevNet-8 is, cuz doing it before DevNet-8 would be preferable to doing it after, right? 

**Tim Beiko**
* I guess, yeah. I'll get two questions, Perry maybe. Oh, okay. Let, let kind answer his own questions. So only, like do we expect to have DevNet-8 up before the CL call next week? I would be surprised if so I think I highly doubt that. 

**Parithosh**
* Yeah, I, yeah, I think realistically it would be the week after. 

**Tim Beiko**1
* Okay. So if we got pre-signal on this call and from the PR from everyone else before that call and essentially on the same day cut the updated release in one week time, would that be okay? Or do we wanna try to expedite the decision synchronously? 

**Tim Beiko**
* Yeah, I think let's, oh, go ahead Perry. 

**Sean Anderson**
* I was just gonna say, I think it'd be okay to like expedite it expedite the decision that async because it is sort of just an aesthetic change and it's just like requires like  a little bit of legwork, I guess. my 2 cents is, is nicer to conclude the Ginger's PR and like add the field and, makes it like a little bit easier. But I'm also, I haven't been implementing this, it's been marked, so he had a little bit more insight than me. 

**Danny**
* Okay, thanks. Can we just get, does any other consensus layer team have feelings either strong or weak in either direction? and then I can knock on doors after the call to see if we get positive all around, we'll try to cut a release more like Tuesday to unblock this and keep going. but yeah, if anybody has a vocal opinion, please say so. No. 

**Tim Beiko**
* Okay. I guess there aren't, so yeah, let's try to, get some feedback on it async and, at the latest, yeah, finalize it on the CL call next week. 

**Danny**
Thanks. 

# Update EIP-6780: Add clarifications to EIP-6780 EIPs#7308 [20.31](https://youtu.be/pTWm4EyStYg?t=1231)
**Tim Beiko**
* Sweet. next up, Danno, you had, clarification, PR about the self-destruct EIP. Do you wanna get some context on that? 

**Danno Ferrin**
* Sure. So as, I was working through implementing it for Besu and integrating it with the execution spec tests, three corner cases that weren't really clear in the EIP were discovered and this EIP makes them explicit. These are currently reflected in the execution spec tests and in at least Besu when I think other clients that are following it. the first of the three items is to separate the notion of contract creation from account creation. Now this is a situation where you would send money to an address and I call those hollow addresses. You don't know whether it's externally owned or a contract. so that exists prior to the transaction. So you start the transaction, you do create to into what that address.
* Turns out that address is a create two address. and then you self-destruct in that case, I think the spec should, self-destruct that address because the contract code that's going in and the storage didn't exist prior to the transaction. so that would basically separate the notion of account creation from contract creation and what 6780 tracks would be contract creation when you actually call the create operation or if you actually started in a create transaction. So that's the first clarification that's reflected in tests right now. the second one is there's a corner case, where you can actually burn ether with self-destruct. If you self-destruct and you set yourself as a beneficiary.
* Currently that ether just completely disappears because by spec, the last step is to set the balance of the self-destruct contract to zero. so this would change so that you only destroy ether if you're destroying a contract in the same transaction. So if a contract existed prior to the transaction and you did the self-destruct and you point it to yourself, all of your balance would stay into in your accounts.
* So it wouldn't self-destruct it. now we can't get rid of it because it turns out optimism depends on this feature and they do depend on the in transaction create and destroy loop of a smart contract to, to burn the ether. And this is in their L2. So there are people out there using this feature. We can't just get rid of the burn feature. so that's not something that I don't think is good to do right now. The final step is to say that self-destruct always halts the current frame. I think that was an oversight in the first one. That was always the intent that if you do a self-destruct into what's gonna be like the new sweep mode, that the execution then halts at the end of that self-destruct. So that's just puts in line clarifies that the tests have always reflected that.
* So that's just worthy of clarification. So those are just three things that are, you could argue that those were the correct behaviors, but it's much easier just to put those into the spec and say, no, these are the correct behaviors and make it clear can optimism not just activate EIP.

**Tim Beiko**
* So I guess before we go into the optimism discussion, I just wanna clarify are the first and third bullets just you're clarifying, you're clarifying the current semantics and then the second bullet is one where we may want to change what the current EIP actually does. 

**Danno Ferrin**
* The way they're, they're all three of them I think are clarifying current semantics cuz the second one okay is really an emergent property, because the burn comes from the set to zero, only in the internal transaction. so I think that that, you know, if we were, that doesn't really represent a change. If we were to change it, I would say that it would fail for self-destruct self in a transaction if I were to change it and get rid of the burning. so I would say that all three of them are clarifications of semantics and those are the most likely interpretations. But you know, based on readings you could get different readings of it. the halt I think is absolutely needed as a clarification. Cause I think the best reading is that it does not halt. 

**Tim Beiko**
* Got it. okay, so there's some comments on like the, the burning. aside from that, does anyone, and  we can cover that after, but does anyone have any comments or contentions on the two other points? So the contract versus account creation and halting the call, does everyone agree that those two clarifications make sense? I guess if you disagree, now's your chance to raise that. Okay, so I guess on the, on the destroying one, yeah just for context, cuz this was posted in a previous, it wasn't posted on this EIP thread, but on the previous, self-destruct, EIP thread, so I believe that sending, like self-destructing and setting yourself as the beneficiary is how at least optimism and maybe other day or twos basically manage, withdrawals back to L1.
* So how they destroy kind of supply on L2 as they, they send it back to L1. and there's a bunch of comments in the chat about this. and it's not clear, you know, it's not clear whether this is like a major deal breaker for L2s or not. but yeah, this, and I guess, yeah, Mario has a comment saying if we renamed the upcode to send all, it's kind of weird if you send all to your own address that they would then destroy the Ether. that seems, yeah, unintuitive, yeah, no. Any thoughts on how we should approach this? 

**Danno Ferrin**
* So the op code wouldn't be send all when you're within a transaction, it's still is self-destructive. The transaction exists, so we can't go there yet. So if we get rid of this, the self-destruct for a contract created in the transaction, then it truly becomes self all send all, 

**Tim Beiko**
* Okay, does anyone not think we should make this change?  Or do people feel like they need to look into it more to better understand? 

**Danno Ferrin**
* So the change would to be never to burn. Are you proposing we change it so it never burns? 

**Tim Beiko**
* Okay, so the current implementation now would still burn it, right? 

**Danno Ferrin**
* Yes. The current implementation and tests. 

**Tim Beiko**
* Okay. 

**Danno Ferrin**
* Burning check for burning, okay, So table the burn for two weeks and let people think about it with the alternative being rewrite it so that it never burns. And if you self-destruct itself, in the same transaction, will it leave a hollow account or will it leave the data or will the fa the self-destruct fail? 

**Tim Beiko**
* Yeah. Mariel. 

**Mario Vega**
* Yeah, I just wanted to clarify my comment. so on the test right now, if  I think it follows exactly what the, what Daniel proposes. So if it's in same transaction, it still destroys the Eth, but if it's in different transactions, the creation and the send all, it doesn't destroy the Eth and in my opinion, that's how, yeah, that's the semantics that sound more, yeah, in line with what the all core dev name describes. But, but yeah, I don't know what other people think I, Okay. 

**Tim Beiko**
* So clearly not a ton of of reactions, I think, yeah, it's worth looking into it a bit more. I've reached out, I sent your, PR to some folks on the optimism side. Danno, I think we should reach out to other layer twos as well. and maybe, I dunno, hopefully by like the CL call next week, we can at least have a good view on like, does this, is this like a deal breaker  for any of them? And, go from there. 

**Danno Ferrin**
* Okay. if we do a change, I'm gonna write this in chat. My recommendation is we would leave a hollow account with state and notes deleted if we delete in the same transaction. 

**Tim Beiko**
* Yep. 

**Danno Ferrin**
* Sounds Good. But other than that, my, you know, it is currently tested for how it's described, so Sounds good. 

# add eth_getBlockReceipts execution-apis#438 [29.39](https://youtu.be/pTWm4EyStYg?t=1779)
**Tim Beiko**
* Any other comments, thoughts on this? Okay. next up, had an execution,I think, Lightclient, you brought this up, for 438, get blocked receipt. 

**Lightclient**
* Hey, so there's three prs I wanted to talk really quickly about into the execution APIs. This first one here, adding this new method Eth block receipts. I understand some clients already have something kind of like this. It seems that there's been like generally positive feedback on discord and on this GitHub issue for the, for adding the method to the spec and supporting it. Basically, I'm just trying to ask if there's anybody who feels strongly against not going forward with this or weekly against not going forward with this 

**Tim Beiko**
* Last chance And there's some besu use support on the PR as well, so Yeah. Oh, Nethermind in favor as well. Okay, let's do it. 

# Remove mining namespace execution-apis#430 [30.54](https://youtu.be/pTWm4EyStYg?t=1854)
**Lightclient**
* Cool. So let's go ahead with that one. I'll, I'll arrange it up to this call. The next issue is 430 and that is a request to move the mining related Ether RPC. So right now you can check there are five still in the specification and these are ETH mining, ETH hatch rate, ETH git work, ETH submit work, and ETH submit hatch rate. They're not really used anymore for post merge related things. I'm curious if client teams feel okay with us removing this from the spec.
* This doesn't say that you have to remove it from your client immediately if you have networks that you still want to support, but generally it seems like something that we don't need to have in the like canonical Ethereum spec. 

**Tim Beiko**
* Okay. Yeah, remove, remove. Okay. Do it. 

# engine: default location for reading/writing jwt secrets execution-apis#297 [31.45](https://youtu.be/pTWm4EyStYg?t=1905)
**Lightclient**
* Excellent. Okay. okay. All right. The last one is 297 and the execution APIs repo. This one has been around for a while and we've been toying with some different ideas. Ultimately the goal is to improve the UX for running execution layer clients and consensus layer clients on the same machine. So today you have to kind of negotiate outside of the two clients as the user of the clients where you're going to save your JWT token, generate that JWT token, and then they kind of point them both into that direction.
* These PRs are sort of trying to figure out a way to improve that, where the user doesn't need to try and coordinate across both of the pieces of software like where this token is going to live.
* And this was the original proposal that I had come up with was just coming up with some sort of default location and some order of precedent for reading and potentially writing the JWT token there.
* I'll let you take a look and review like what the exact locations are, but we went down this path and ultimately I think be a proposal to have a fixed JWT token and only allow the fixed JWT token to be used if you are binding the engine API to your local host. We went down that path for a while and decided that ultimately we're kind of relying on some browser security properties of not being able to do a cross domain request to local host as like the kind of like securing property of that system.
* And it seemed a little bit brittle.
* So I've kind of like come back now to this default file path, method and trying to yeah, just reintergrate the interest in making this happen.So I'm curious like if client teams are interested in supporting this, if so, any comments maybe? Yeah, if you're not interested. Also important. 

**Lukasz Rozmej**
* I have a question. would there be any potential issues with accessing this path? because, and on different  so for example, on Windows, I'm not sure if you have by default access to roaming up data of not your, not for your actual application, right? That you're running and this would be like cross between EL and CL. So like question mark about the access paths and access rights to the paths. 

**Lightclient**
* Yeah, that's a, that's a good question. I'm not 100% sure on that for Windows. def I don't know if anyone knows off the top of their head if that's the case, would need to to look into that. Enrico. 

**Enrico**
* Yeah, we have been discussing this morning about this and we internally and I was the, was that for us was kind of weird that we have, spec that are prescribing things. So in detail it also related to operating system stuff and you end up having these issues like doing Windows, by default you get access to this directory or what if user gonna use Docker and you start having other level of complexity and then specing out these details. There I becomes a little bit, yeah. 

**Lightclient**
* Yeah, that's, that's fair. Originally when I proposed this, I used the must terminology as in this was like a hard requirement for clients, but we stepped that back to more of a may. Like clients may provide dysfunctionality and I do, I think it is useful if we decide to like move forward with something like this to have a sim you know, a relatively simple spec about like where can clients negotiate on this location? If it's too much effort to implement, then this is a choice for clients.
* But I think ultimately like this is a problem, like outside of the exact implementation of how to deal with this problem negotiated the JWT token is just a silly thing for users to have to do on a single machine and we should come up with a better way. I don't know if this is the end all way, this default path. I'm happy to like find another route, But Yeah. 

**Enrico**
* Yeah. Another, another consideration we were doing is that, maybe this kind of complexity will be gradually, kind simplified by the tooling that overall come up for home stakers to just help things set up. And this kind of detail will be kinda hidden by using these tools and might be that this kind of complexity were initially there, practically for when we were close to the merge, but then time passed by users, get used to this and a lot of tooling around this complexity will Yeah. 

**Lightclient**
* Abstract a way that this stuff, I dunno, I mean even just for myself, I would love to not have to deal with this and I don't think, I think users aren't really getting better at running clients, they just stop running clients. So I don't know. I think that we can, we can do a lot better about making it easier for people to be running our software. 
* Okay. Generally seems pretty mixed. That's the takeaway. 

**Ahmad Bitar**
* I think just having a default value for, the location of the def the, the file is, is fine as long as we are not enforcing the user to always locate the file at that place then. And if the user does not specify another path for where it is, I think having a default value is a good option. I don't see why anyone would object to having a default value or, or how it would affect the user experience in a negative way to having an, a default value. Even with the tooling that already exists with the existing complexity, since they already specify that location of the GWT file, they do not have to deal with any regressions caused by this change. 

**Lightclient**
* Right. I think the point Enrico was making, and correct me if I'm wrong, was just there's more effort on the client side to deal with these different default locations and it adds some complexity like it does. 

**Enrico**
* Yeah. I mean, at the end you, you may start, having more, more interaction with, end users that assume that is gonna work, but then for their system that don't work, so they start, yeah, there is more, much more support around this, this, this thing. And then you fall back to say, okay, please explicitly pass this, this information that the JWT path explicitly there to fix it. So, but I agree at the end that's a default value. seems like, seems like, cannot worth, cannot be, cannot make things worse actually. 

**Lightclient**
* Okay. I, it sounds like we don't really have enough forum to prove this this time. I would really like if more client teams could weigh in on the issue and we could try and iterate a little bit on it and get it to something that people are generally happy with. 

**Tim Beiko**
* Yeah, Barnabas had a nice comment as well saying that with whole Sky, it's gonna force each client team to run multiple set of nodes so people will experience the pain personally a bit more. 

**Lightclient**
* So that might be, I think the client team's already run nodes Knock enough. Yeah, you heard it A knock in every household. Yeah. 10 nuts in every household. 

**Tim Beiko**
* Yes. Yeah. but yeah. Okay. Let's, and people can continue, discussing like the specifics on the, on the issue, but I agree it seems like, we might wanna get a bit more inputs before moving forward with this. 

**Lightclient**
* Yeah, sounds good. I'll merge the first two PRs. Thanks a lot for the feedback on this one as well. Cheers. 

#  https://eips.ethereum.org/EIPS/eip-7329 [41.00](https://youtu.be/pTWm4EyStYg?t=2460)
**Tim Beiko**
* Okay. next up, so there's two, related, I guess, proposals. So, EIP 7329, which is the EIP ERC of repo split. We've discussed this, on the call, I believe two calls ago. And then it kept discussing it on EIPIP and then, so, Danno and Light lient put this together and I think, Greg Covin, I'm not sure if he's on the call, but had a proposal to EIP-1, that addresses some of the issues, around the process, but maybe, yeah, Lightclient, like client Dano, do you want, to give some context on this? 

**Danno Ferrin**
* The context is to affect what we decided a month ago. and this EIP just formalizes it in a way that is acceptable to EIP editors. It outlines the alternatives considered and the objections, but I don't consider my opinion changing on it, that we want this full separation, we want full governance split. and that's what we had agreed on what the All core devs wanted a month ago. So that's formalizing this process. 

**Tim Beiko**
* Cool. Does anyone else have comments, thoughts on this? 

**Danno Ferrin**
* Do any core devs disagree? Do any core devs want us to stick with one unified EIP repo? 

**Tim Beiko**
* Okay, so this seems pretty clear. I don't believe Greg. Oh, you are here. Okay, great. Perfect. So yeah, do you wanna talk about your PR and yeah, your,

**Greg (Gcolvin)**
* Well, not all of us are on board with it, as it is it, I can't really review the big PR cuz it touches 924 files. So some of us feel this is major surgery that we wanna consider. my EIP it'll probably get split. Some of it are, I hope uncontroversial changes about things that people have complained about that, that don't require the split, which is things like our link policy way too tight and people don't like fighting with that and other issues of that sort. the bigger thing it tries to do is to clarify, what parts of the responsibility and workflow belong to the developers and what parts are editorial.
* I think they've gotten mixed up. And so we start wanting to split the editorial repos instead of saying some of what we want to split shouldn't be there in the first place. so I think a lot of the trouble is just that we're trying to track, track the EIP status in the Editorial processes. The editors don't care about whether it's CL or not, or CFI if it's considered for inclusion, if it's going on the test nets, that's entirely development workflow. so my EIP just tries to separate that to create, essentially two side repos where all of the ERC editing gets moved into one repo. All of the EIP editing gets moved into the other, but the current repo stays the same cuz that is the working repo where the editors do their main work, and actually publish.
* It's horribly cluttered cuz people check in the draft and then all of the editing on the draft is going on in that repo and for ERCs, that's a huge amount of churn. 

**Tim Beiko**
* Does this, Does this imply that there would be a single repo where like all the drafts get merged into, so there's like a ERC pre-draft repo and EIP pre-draft repo and then they go both get merged into this common repo? Or does, is it more that this common repo hosts things like EIP one or whatever, like high level process stuff, but then there's an EIP repo and an ERCs repo and that's where all the activity, for each side happens? 

**Greg (Gcolvin)**
* It could, it could work like this. a draft gets checked in to the existing repo. The bot says we have a new draft here. I'm going to put a PR, maybe automatic merge, but at least a PR over on say the core repo, the Eth the core directory in the EIP repo, the softer one side. So now there's a draft there and further editing happens over there. as the working group iterates on that draft, at some point that draft could go to CFI. and when its status changes to CFI, the bot can then, put a PR back on the main repo and say, Hey, this one's gotten the CFI, so we'll make a note of it. So the main repo only contains the major changes in status and those major changes are defined by the working group.
* In this case, the core developers say what their status is, they don't have to tell the editors, we don't care. and so this I think splits off the work in the ways that the work is actually done and let's the editors manage their repo in the way that's best for us to do our own work and publish final documents, which is our real job is to get to a final document that actually describes the protocol. and  to support working in between, but not to get in the way. You know, we're just in the way right now and I don't think the split gets us out of the way. It just doubles the problems. 

**Danno Ferrin**
* So basic, I think the split does get the editors out of the way because it gives all core devs final jurisdiction Yeah. Over the items it wants to do. And this process set up with this working group and the second editor group, I don't think gives us final jurisdiction. It still provides the ways for editors to be in the way. And if one person to stand up and say, I veto this or to keep a spectrum from going to final because we have some little knit wrong with particular formatting or process of one particular thing. The big advantage I see of this split is it gives the all cord dev side of the house final and total jurisdiction over how they do their processes and what they publish. And that is what I want more than anything else is final jurisdiction in this meeting. 

**Greg (Gcolvin)**
* That's what I'm trying to do. Or a working, a working group should and already does have at least one editor, in the working group. And I would say that that editor should have right permissions and if the working group wants to push it to final, the other editors back off and just say, you say it's final, you wanna merge  it's your PR do it. 

**Danno Ferrin**
* But that's not the experience we've had in the past. Of course, there was a networking PR where reset this is final and an editor that was not in the working group from outside the working group came and said, no, you have to go through the process of a two week because the other editor still could go in. It's, we've seen these happen in the past, right? So stop. I don't want it possible for someone outside of all core devs to come in and say, you have to do that. So unless those editors are given complete and total jurisdiction, I don't see how this solves this without it actually being a full formal, total split. A working group is just, you know, moving the deck chairs around. 

**Greg (Gcolvin)**
* I've very clearly I want to get rid of those stages. There shouldn't be a last call for core EIPs. There shouldn't. but I don't wanna, I don't, I wanna rehash this discussion. We have the EIPs on the table. We have discussion threads both on the magicians and discord. So that's where to take this up. I'm just saying this is controversial. You can force to merge if you want, but you'll be forcing it through controversy on the editor's side and if you force it through against controversy on the editor's side, you will do damage. And I don't think the split is necessary to achieve the goals that you want to achieve, but I don't, I don't wanna spend this morning of arguments here. 

**Tim Beiko**
* Yeah. I mean there's a way where like we could eventually get to that even with a repo split. So I think clearly, you know, the strong support for the repo split, we just, you know, have no objections again. and it probably makes sense to go forward with that first. And then if we find that there's some, you know, core set of like overhead, you know, like the obvious number, the obvious, the obvious thing is just like numbering. But if there's like more than that, that like makes sense to live in a common repo, maybe after we sort of create this sort of EIP me or EIP editors repo or something like that. 

**Greg (Gcolvin)**
* But I please, Please let the editors try to come to a consensus. We aren't there yet. We don't have a consensus on this. 

**Tim Beiko**
* Sure. But that means, you know, you personally could block this decision for like another year if, if you wanted to. 

**Greg (Gcolvin)**
* No, I Look Victor strongly opposed, but has said he will not block. I'm strongly opposed. I'm blocking. I've said that I will remove the block, if we finish this whole discussion and have a reasonably coherent plan that doesn't risk splitting the editorial organization into two organizations. And that if I cannot remove my block, I'll simply remove myself as an editor and, and allow the, the other editors to do what they want to do. but I, this is, I yeah, This is the nature of the consensus here. We probably can't get unanimity, but I'd sure like to be closer than one editor strongly, four, two editors strongly against and others in the middle. it, you know, let's take a little time. We've got solid proposals on the table to discuss. We're not going in circles. 

**Tim Beiko**
* But I just think your, your block is kind of, there's like some fundamental thing here where if the reason to split out the ERCs and EIP process is like each side has more control over how they do things, then of course the editorial is gonna be split out because, you know, the editorial in the long run is probably gonna be quite different and maybe a single person can choose to like sit on both. And I believe at least some of the current EIP editors wanna do that. But we are, but it's, it's gonna be two different processes. So I just like, fundamentally it seems hard if we actually want like, the benefits of splitting the repo, which is we can tailor both sides of the process to like the users of the process and the main stakeholders, then from an editorial perspective, you're gonna have to change things as well because, otherwise we'd all be happy with the current process.
* Like the fact that we feel there's some constraints as part of the ERC process that, make it harder to, do EIP work is kind of the root of it. 

**Greg (Gcolvin)**
* Yes, I want to fix that. I don't believe that the current split proposal is the right way to split things. 

**Tim Beiko**
* Right. 

**Greg (Gcolvin)**
* But, and I guess they're Edit look, I'm sorry, editing. We're editing technical English, it's all the same. It's technical English. It has the same spelling, the same grammar. The only form we're imposing is we really want to see an abstract, we really want to see a securities, considerations and we really wanna see, references. and we're handing over to the core devs, what references are allowed, what sections in between the abstract and the security are allowed. And I would propose that yes, if the core dev say it's final publish it, the editors will back off and say it's your EIP you're telling us to publish it despite our misgivings. We will publish it, you know, to give the core devs plenty of control, but not say we need two editorial organizations to manage stuff is not editorial. I don't see, I keep bringing up the EIP, the internet engineering task force.
* They've been managing all of the EIP and more protocols for what, 50 years now? Maybe 60. they have one editorial organization with one head editor. They've never felt the need for multiple editorial organizations to manage all the different processes. They simply give a lot of power to each working group to manage their processes and keep the editorial work, minimal. I think that's a good model for us. I don't think making up another model that's this complicated, I just don't think it's the way to go. But I think we can meet the actual problems and fix those. and I'd lack a chance to do so. 

**Tim Beiko**
* Right. But again, I think the set of all core devs and like everyone on this call sort of has already moved past this. So I don't think blocking the split is the right approach when you know, at least what Else can I do? 

**Greg (Gcolvin)**
* I totally disagree and if this split goes through, I will need to leave cuz the organization's values will have diverged from my values and I believe the values of those who set up the organization circuit 2017 Then. 

**Tim Beiko**
* Well, I think there's a, this is, I think if you care about the consistency of the editorial process, you know, waiting to see how the split goes, even if you disagree with it, and then potentially trying to find ways to like, make things more coherent at the editorial level. If there's, if there's room for that, like I think, you know, that could be an approach. But I, given we've discussed this for, you know, first many years but also many months recently, and there seems to be like extremely strong support from all core development and, and and research side across both the execution and consensus layer. I think we should continue to work on the split.  I feel like, you know, we asked like 10 minutes ago if anyone had objections and there doesn't seem to be so, I thought my objections, I mean, sorry, from the client teams, Noam. Yeah. 

**Greg (Gcolvin)**
* Yeah. 

**Tim Beiko**
* So, but I think look, if, and if you disagree with this at like a fundamental level and don't feel like you can engage with the process afterwards, 

**Greg (Gcolvin)**
* There's no going back to what we had from the split. 

**Tim Beiko**
* Well, you could always add, I think I disagree. I think if, if there is actually like a set of common things that like need to happen across both repos, and like, yeah, numbering is one example, but if there's like more of those types of things, then you just add an EIP meta repo or EIP ERCs repo or whatever EIP coordination. Like I, but my view is like from the client teams, from the research teams and like everyone I've spoken to who's like deeply involved in proposing changes on the, the protocol side, the split is what they'd like to go forward to. and and I think respecting that and you know, potentially trying to find ways to make things better, afterwards is like an approach where you can probably get some of your changes as well.
* Like, and  I haven't like fully reviewed your your your PRs but like just skimming through it.
* I suspect a lot of the things you propose, there are things we would want on the EIP side of things, but you know, the difference is like which repo does this end up being written in? And I think the strong preference from all the client teams is they want a separate repo that's focused on core EIPs and, and this can be part of that. Yes. 

**Greg (Gcolvin)**
* Yeah. I'm proposing a separate repo, but I'm not proposing creating that either the ERC or an EIP repo don't create that by essentially cloning the existing EIP repo and trying to clone the existing process. Right. 

**Tim Beiko**
* It's sure. So then you're saying you've got like a blocking objection on basically an implementation detail where most of the client teams effectively disagree with you. 

**Greg (Gcolvin)**
* And Right, but it's the editorial team that has to live in these repos. 

**Tim Beiko**
* But but again, like part of the argument is like why we want this split is client teams do not live in these repos right now because they feel like they're not set up for them. Yes. And the thing we want to get out of it is, is that yeah,

**Greg (Gcolvin)**
* Yes, I'm proposing that there be an EIP repo separate from Yeah, separate from the editorial repo that there be Yeah, there be a developer's repo for the purpose of managing EIP. But I would like it to start new and empty and then going forward we start working in it, it's much, much easier. Requires no surgery to speak of. and if we really like that more stuff can be migrated into it as we want to. So I think it amounts, it amounts to a good piece of the split to work with. But, but not trying, my hugest objection is no, I don't wanna split the editorial processes and I don't think that things like link rules and spelling and grammar need to evolve and different directions.
* I just think the editors need to back off to editing and let the core groups, take care of, of developing and specifying what they develop. You know? 

**Tim Beiko**
* Danno, I saw you had your hand up. 

**Danno Ferrin**
* Yeah. so a lot of these things in the EIP one pain relief,  they're not mutually exclusive. We can still do every single one of them. Yes. And the one commentary I wanna say is that a lot of these ideas have been discussed but never seriously considered until the moment the split was mentioned. and so there's a bit of the  window shift and it's that having to threaten to leave and to split things to get work done is not healthy. So if we had final jurisdiction on this, we wouldn't need to, work, we wouldn't, we would know and control our final destiny. And even that little bit of asking the editors to back off, there's still the final step. We don't have full autonomy in the process. And that is what is essential in this split. 

**Greg (Gcolvin)**
* That's what I'm offering, I guess. 

**Tim Beiko**
* I guess, does anyone else, have thoughts on this or, 

**Greg (Gcolvin)**
* I'm offering that the core devs have the power to merge final EIP no matter what the other editors think. 

**Parithosh**
* There shouldn't be an editor group to think about it. We should be our final owner of it. 

**Greg (Gcolvin)**
* Okay. That's okay with me too, but I don't, I don't see the objection to letting the editors, check the spelling and grammar and, and the check that all of the links are actually live links. 

**Tim Beiko**
* But the, Yeah, the thing is, the split does not stop this. Right. The split makes this happen in two different repos. And I think, again, this is like the preference that's been stated many times. So it's, I don't know. I feel like there's a pretty strong like, preference from the client developer group of how this should be done technically to accommodate their workflows, which in practice doesn't really change, you know, how, like what, what modifications we can make to the process. so yeah, I don't know, based on like this and the other conversations,
* I would be like,  I think we should probably move forward with the split, consider your suggestions as part of the, like new or I don't know, like separated core EIP focus repo. and, and I think like, yeah, if that's a way to get more clients to engage with the process, then that's, that's great.
* And if there are things we can do after that to help the editorial side, we should, we should obviously do those. but I think holding up the entire kind of transition that people are like pretty strongly in favor because of some objections, because of like some objections to the form on your end seems, yeah. That, that seems wrong. 

**Greg (Gcolvin)**
* This repo modifies 924 files. I can't review it. 

**Tim Beiko**
* Sure. Well, I mean, I, I know I think like client did the PR, but I assume most of those are just like links and naming changes, right? 

**Greg (Gcolvin)**
* I don't know. I can't review it. GitHub can't show me a table of contents anyway. There's an editor's meeting next week. We, we can take this up as editors next week. 

**Tim Beiko**
* Yeah, but I, okay. 

**Greg (Gcolvin)**
* And I'm sorry, blocking is part of the consensus process and deciding that, deciding that my block is solid, but I'm not gonna change my mind. 

**Tim Beiko**
* Sure. But that, does it mean everyone else has to stop moving forward because of your block, right? 

**Greg (Gcolvin)**
* No, they don't. 

**Tim Beiko**
* Yeah. 

**Greg (Gcolvin)**
* And I think The editors are free to move on without me, but that's true. But I, this is, this is how important it is to me, and it's a hill I'm willing to die on. I'm sorry. 

**Tim Beiko**
* Yeah, I I appreciate that. I don't, yeah, I don't know. 

**Greg (Gcolvin)**
* I, if there's,  I'm trying so hard to give everybody what, what they really need here, and this is on the basis of, at least 30 years of experience in standards groups, and how they go right and wrong. So I, this isn't coming outta nowhere. Yeah. 

**Greg (Gcolvin)**
* Yeah. I, I don't know if anyone feels like this makes them reconsider whether we should split. This is probably the time to speak up. 

**Tim Beiko**
* Otherwise, I think I prefer Okay. The editors can take it up next week. 

**Tim Beiko**
* No, But yeah, I'm mostly curious to hear about client teams because Yeah. Yeah. but yeah, last call, I guess the voice objections And yeah. So I guess in terms of next step, then yes, you know, you can obviously discuss it in the editor meeting and discuss the specifics. even just also around like reviewing the PR and the script and whatnot. But I think from like the client team's perspective, it seems pretty clear that we wanna move forward with this. and I think it's helpful to also have, EIP, what is it, 7329 that like lays out the specifics.
* So I'd  I encourage client teams to review that. as well as, as as your PR Greg, so that, you know, there's probably a lot of these suggestions that we would want to pull in, to the, to the post let repo,

**Danny**
* 7329 Is in the last call until the end of the month, so please comment. Cool. 

# https://ethereum-magicians.org/t/name-needed-for-combined-el-cl-prague-electra-upgrade/15122 [1:07:22](https://youtu.be/pTWm4EyStYg?t=4032)
**Tim Beiko**
* Okay. Last, thing I believe we had on the agenda, just a quick shout. There's an eth magician's thread about finding your name for the next upgrade. So Prague and, Electra, the two, the two, options proposed first are Petra and Elektra. And then, Ben in the comments says he wants to die on the Prague Elektra Hill. I don't know if we wanna discuss this now or just leave it on Eth magicians. yeah, any thoughts on this? Okay. so, okay, let's use, let's use, Eth magicians, anything else, that anyone wanted to bring up? Cool. 

**Barnabas Busa**
* Did I bring up, yeah, 33 block, version three endpoint for Beacon api? 

**Tim Beiko**
* Yes, please. 

**Barnabas Busa**
* Is this something we want to include in, DevNet eight? 

**Tim Beiko**
* Any any comments from time teams? Have people had time to review it? Okay. If there's no comments here, I think we should do, I, oh, and then everyone has PR I was gonna say, so for the blocks version three, I think we should try and do like for the, other PR we mentioned, get some, consensus async in the next week and make a go or no go decision, on the CL call. Alexa, I is, I believe your PR is like similar. 

**Alexey**
* Yeah, and just small, about, your codes and general cleanup for, looks. and, well if we can consider it for inclusion, tool or measure would be cool. 

**Tim Beiko**
* Does anyone have thoughts on this? PR okay. It, I think what we should do as well. So, let's discuss the async. We will, I'll make sure to add them to the agenda for the 4844 next week as well. So, we, you know, people have, in a couple days to look at them before then. yeah. And we can make a call at the latest, on the ACDC call next week about whether we include them devnet 8. Anything else? Okay. Well thanks everyone. talk to you all soon. Thank You. 

**Andrew**
* Bye. See all.
  
**Andrew**
Bye. Bye. 

-------------------------------------
### Attendees
* Tim Beiko
* Danny Ryan
* Pooja Ranjan
* Mikhail Kalinin
* Marius
* Wesley
* Barnabas
* Saulius
* Danno
* Lightclient
* Pari
* Ethan
* Mario
* Tomasz
* Oleg 
* Kasey
* Marek
* Crypdough
* Fabio Di
* Terence
* Andrew
* Roman
* Marcin 
* Pop
* Guilaume
* Protolambda
* Carlbeek
* Mike
* Gajinder
* Stefan
* Hsiao-Wei
* Josh
* Phil Ngo
* Alexey
* Holger Drewes
* Dankrad
* Guillaume
* Proto
* Holder Drewes
* Stokes
* Peter Szilagyi
* Sean
* Micah Zoltu
* Jiri Peinlich
* Marius Van Der Wijden
* Potuz
* Evan Van Ness
* Moody
* Tynes
* Alex Beregszaszi
* Marek Moraczyński
* Justin Florentine
* Ben Edgington
* Lion Dapplion
* Mrabino1
* Barnabas Busa
* Łukasz Rozmej
* Péter Szilágyi
* Danno Ferrin
* Andrew Ashikhmin
* Hdrewes
* Crypdough.eth
* Ameziane Hamlat
* Liam Horne
* Georgios Konstantopoulos
* Mehdi Aouadi
* Bob Summerwill
* Jesse Pollak
* Stefan Bratanov
* Sara Reynolds
* Caspar Schwarz-Schilling
* Ahmad Bitar
* Marcin Sobczak
* Kasey Kirkham
* Sean Anderson
* Saulius Grigaitis
* Ruben
* George Kadianakis
* Dankrad Feist
* Andrei Maiboroda
* Gcolvin
* Ansgar Dietrichs
* Jared Wasinger
* Diego López León
* Daniel Celeda
* Trent
* Mario Vega
* Kamil Chodoła
* Ziogaschr
* Kevaundray
* Antonio Sanso
* Oleg Jakushkin
* Leo
* Nishant Das
* Pote
* Sam
* Tomasz K. Stanczak
* Matt Nelson
* Gary Schulte
* Rory Arredondo

-------------------------------------
### Next meeting [August 3rd, 2023, 14:00-15:30 UTC](https://github.com/ethereum/pm/issues/836)



