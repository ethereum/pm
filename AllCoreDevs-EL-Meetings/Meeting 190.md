# Execution Layer Meeting #190
### Meeting Date/Time: June 20, 2024, 14:00-15:30 UTC
### Meeting Duration: 1.5 hour 
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1066)
### [Video of the meeting](https://youtu.be/8VGf-EE6zNE)
### Moderator: Tim Bieko
### Notes: Alen (Santhosh)

| Decision Item | Description                                                              | 
| ------------- | ------------------------------------------------------------------------ | 
| 190.1 | **Pectra Devnet 1**  Developers are aiming to launch the next dedicated testnet for the Pectra upgrade over the next week. The main specification changes between the prior testnet, Devnet 0, and the one upcoming are: The addition of EL triggered validator consolidations The replacement of EIP 3074 with EIP 7702
| 190.2 | **Pectra Devnet 1**  Besu: A first version of their implementation for Devnet 1 is ready. It has some tests missing and the team has questions about the specs regarding gas pricing operations.
| 190.3 | **Pectra Devnet 1**  Nethermind: They are working on reviewing their Devnet 1 implementation, merging various code changes and software branches, and writing test cases.
| 190.4 | **Pectra Devnet 1**  Erigon: They have a draft implementation of EIP 7702. They are reviewing the latest changes to EIP 7251, namely the addition of EL triggered validator consolidations
| 190.5 | **Pectra Devnet 1**  Reth: Their implementation for Devnet 1 should be finished before the next ACD call.
| 190.6 | **Pectra Devnet 1**  EthereumJS: The team is working on the implementation for EIP 7702. They expect to be ready for Devnet 1 in a week or so.
| 190.7 | **EIP 7702 Updates**  Even though developers are working on implementing EIP 7702 in Devnet 1, there is the possibility of the code change being revised in major ways to support new features, specifically the ability for users to revoke EIP 7702-enabled transaction authorizations.A pseudonymous Geth developer by the name of “Lightclient” has proposed new changes to the EIP that would support EIP 7702 revocations. He explained, “It's not as easy to see what types of authorizations you have in the air at any given moment, and it's difficult to know like what has been revoked and what's not been revoked. There are design patterns that avoid these types of scenarios but the reality is that maybe we won't know how wallets are going to use this and to have a more defensive mechanism an idea I think Vitalik mentioned on the last call, or maybe it was in a breakout room, [is] instead of having the authorizations be these temporary things that must be included with the transaction to set the code in the account, we can instead save the authorizations so that in the account you can actually look to see what code the account was delegated to at any given moment.”
| 190.8 | **EOF Updates**  Besu shared that his team will test EOF implementations after other Pectra code changes have been implemented. The readiness of EL client teams for EOF are tracked on GitHub. So far, two EL client teams, Besu and Reth, have implemented all EOF EIPs, while the others are still working on building out all the EOF EIPs. A representative from the Erigon team noted that additional test cases simulating Ethereum blocks containing EOF transactions would be useful. Mario Vega, who is part of the EF testing team, wrote in the chat that his team is working on releasing more tests for EOF and that he can share more on the next EOF breakout meeting. The EOF calls have switched from a weekly to a bi-weekly cadence, said independent Ethereum protocol developer Danno Ferrin, as EOF specifications are now finalized, and the focus of work for EOF is on testing and client implementations.
| 190.9 | **PeerDAS Updates**  Besu shared a quick update on implementation work for PeerDAS. He said that the next PeerDAS Devnet should be up and running in the next week or two. PeerDAS as discussed on the last ACDC call will be developed on top of finalized Dencun specifications as opposed to Pectra ones.
| 190.10 | **Announcements**  Beiko has proposed a new default template for EIP authors to structure their Ethereum Magicians posts. The new template is intended to facilitate “high quality reviews on EIPs.”Jayanthi highlighted the “eth-clients” GitHub page, which hosts several resources for Ethereum developers including the canonical configurations for Ethereum testnets and mainnet, among other resources. It is currently maintained by representatives from all the CL client teams. Jayanthi asked for representatives from EL client teams to volunteer and help maintain this GitHub page.

**Tim**
* And we are live. Welcome everyone, to ACDC  #190. Pretty light agenda for today. Yeah. So some Pectra Devnet, and 7702 discussions and then, two quick shout outs or three quick shout outs. and that should be it. yeah. So I guess most important, thing today's, Pectra and Devnet one guess. First off, maybe Barnabas or Perry. Do either of you want to give an update on, like, the spec and sort of infra side of Devnet one, and then we can chat with different teams, about their specific progress? 

# Pectra [3:09](https://youtu.be/8VGf-EE6zNE?t=189)
**Parithosh**
* Yeah, I'll talk about Pectra and then Barnabas can do EOF so, Pectra, I can share the link to the spec, but the decision last week was that we would basically do the same as Devnet zero, with the main change being, EIP sense and zero two. There's a thread in the interop chat where we're collecting status as well as which branches to use. I think some CL devs have already posted their branches, and EL have mainly indicated that it's a work in progress, so there's no there's nothing to really use right now. so that's the current status. We're just waiting on, ready branches to start with. 

**Tim**
* Thank you. And yeah. So, there was the there was the 7702 change and I think, yeah, we had a couple PRs, mostly in the execution API and a few on the engine API. Anything else on the specs for the Pectra Devnet one? And maybe. Yeah, before we do EOF and PDAs. I guess on the EL side, do any teams want to share specific updates about where they're at and yeah, how how the work in progress is going? If not, I will call on you. And Besu you. I see a lot of base people on the screen. 

**Daniel**
* I can give an update. so regarding 7702, we have like a first, version implemented. we had some questions regarding the gas pricing of the operation, but I think it makes more sense to discuss this offline. but yeah, we have, like, a first version that's some tests are missing, but otherwise, I think we are more or less good to go. 

**Tim**
* Got it. And 7702 was the last blocker like the last thing you needed. 

**Daniel**
* Yes. Because the other stuff should have, should be ready for Dev

**Tim**
* Awesome. Thank you. 

**Marek**
* So never mind. We have draft PR of all the changes needed for Pectra Definite one in branches. Now we need a little bit more time to review them. merge them together and write some, unit tests. Yeah, but that's it. 

**Tim**
* Got it 

**Racytech**
* I have a more of a question. Yes. If you don't. Yeah. So my question is the EOF testing I mean, Devnet 1 is going to be separate from the Devnet 1 Pectra right. Yes. That's okay. Got it. Thank you. 

**Barnabas**
* As in what the idea is that we're going to be having on top of Prague, so we would need to most likely have to rebase on Prague on top of Prague. That's what we agreed on yesterday. On the call 

**Tim**
* Yes. So we have Yeah. So, we have, eof aspect on top of Prague. And that feels like the right thing because there's no world in which we do eof before Prague. 

**Barnabas**
* The only issue that can be is that you will have a harder time debugging EOF bugs. If there's still some Prague bugs present. So. 

**Tim**
* Yeah, and I guess I don't know. It's even if that's true, it still feels like the right approach in a way, because like we want teams working on the core of Pectra. Yeah. And, you know, fixing those bugs. So I. Yeah, I it seems more reasonable than like basing it on top of the previous fork and then having to potentially like rebase it on Prague. Really late in the process and then also finding all those bugs. but this is. Yeah. I don't know if someone has a strong opinion against this okay. And we can yeah, we can go back to the EOF, devnet discussions a bit after, but I'd be curious to hear from other teams just on the the like. Pectra Devnet one. yeah How things are going. Andrew. 

**Andrew**
* Right. So, about Devnet one, we have a draft implementation of 7702, but, I haven't reviewed it yet, so it's, I'm not sure like how far it is from a, mergeable version. we haven't I don't think we have tackled the changes to the engine API, but I don't know. I haven't looked at them. Hopefully they are not that major. and I have a question about an update to 7251 because it seems that like the, increase the max effective balance because previously it was a purely CL change. Now it has an EL component. So we haven't implemented that yet. But I'd like to just double check. That means that for Devnet one, we effectively have 7251 on the EL side, right Yes. 

**Tim**
* That's correct. So is it the is the PR you're talking about, the one I just posted in the chat, the EL consolidations. Yeah. we agreed to include that in Devnet one. 

**Andrew**
* Okay. So yeah we have to implement that as well. Got it. 

**Tim**
* Okay. Thank 

**Tim**
* You. Anyone from Geth or Ethereum JS

**Draganrakita**
* From our side. we started implementing 7702. It's only missing EIP and, it should be like finished like week or something like that. yes. Basically before the next ACDE. 

**Tim**
* Sounds good. 

**Parithosh**
* This also has the similar object we are working on, 7702. And maybe in a week or so we'll also be, ready with it. 

**Tim**
* Sweet. Anyone from Geth 

**Tim**
* Okay. no one from Geth. it seems, Okay So, clearly, yeah, there's still some work to do on the EL side here. We can check in on the next call. the one thing, I guess this is a bit out of scope. Oh, Marius is here. Just, no one else from speaking from Geth speaking. So. Okay, I 

**Marius**
* We still missing 7702. I think, and, yeah, we should implement this this week and be ready for the next one soonish. 

**Tim**
* Awesome. and I guess, okay, on the 7702 front, I think, yeah, we should leave the spec as is for Devnet one. But if we look in the future, for Devnet two, we still didn't quite find, like, a revocation mechanism we were super happy with. I guess. Yeah. Has anyone. Has anyone looked into this? Are there. yeah. Are there updates just on the spec side for 7702? 

**Lightclient**
* I've got an update that I wanted to share, but first I, I've been offline for the last couple weeks. I wanted to hear if there were any updates not related to this new revocation idea that that I opened a draft PR for yesterday. Maybe if Aragon has something that they found during the last couple of weeks looking into the revocation mechanisms 

**Andrew**
* It is Sudeep on the call. Yeah, yeah. yeah. 

**Sudeep**
* There was, a comment from Fangio in The Athenian Magicians which discussed about, account, based revocations and, yeah, I think that's the best solution that I can put forward right now. Well, so maybe Lightclient can, look at that later on. 

**Tim**
* What was the idea of the account based application? 

**Sudeep**
* It was basically, keeping track of the template addresses that you revoked in either a system contract or, the EOS storage itself. And when 77 transaction arrives, the, the execution layer will basically check if, yeah, if the template address is, already revoked. And if it is, then it's it fails. 

**Lightclient**
* Any. Yeah. I responded to this on Eth magicians and I as I said like this we we can implement this as an ERC. I really see no reason to implement this in the protocol. 

**Andrew**
* I think there was another idea with, Max nonce, but I'm not sure about, what's the current thinking about that 

**Lightclient**
* If it's the same mechanism with Max. Not so. We had previously approved in 3074. I think it works okay, but I didn't get the impression that most clients like the idea of having some way of bumping the nonce in, larger increments than just one. So that wasn't a super nice aspect of it. I don't know, maybe it's worth me just mentioning this other revocation idea that, yeah, please come up with. Because I do think it's a little bit similar to what Sudeep is asking for. The proposal by Franco on Eth magicians was basically trying to address the fact that it's not as easy to see what types of authorizations you have in the air at any given moment, and it's difficult to know, like what has been revoked and what's not been revoked. There's design patterns that avoid these types of scenarios, but the reality is that maybe we won't know how wallets are going to use this and, to have a more defensive mechanism and idea. I think Vitalik mentioned it on the last call, or maybe it was in a breakout room, but instead of having the authorizations be these temporary things that must be included with the transaction to set the code in the account, we could instead save the authorizations so that in the account, you can actually look to see what code the account is delegated to at any given moment. And this definitely changes how we think about 1702 and 3074. Because now, you know, we're not providing signatures every time. You know, once you've authorized the delegation, the delegation is there. And if you want to revoke the delegation, you could send another authorization to change the code to something else, even the zero address, maybe. So it is changing how we think about the authorizations in a lot of ways, but ultimately it feels very similar. It feels like it provides the same functionality while also avoiding these issues of having the outstanding offset users and wallets might not remember. And it feels like it resolves this discussion that has been ongoing for a long time about how to do revocation. Because the auth are no longer required every time you use the account, they are just a single use, authorizations. Now, once you delegate to an a address of code with an authorization, your nonce is bombed. That invalidates that authorization. That authorization is no longer valid. So that's kind of the idea. It feels pretty good to me in general so far. If anyone has concerns, we'd love to hear them. The one thing that has come up in my mind is it's starting to look like a protocol level proxy, and if we do that, we need to be very cognizant that this doesn't become a way which smart contract developers use for applications. So I could imagine if this was like a really cheap type of thing to do. It might be better for, say, Uniswap to deploy pool contracts using this like EOA proxy method. And I think that that is something to avoid. But in general, it doesn't feel like there's many other major concerns with this approach. 

**Tim**
* Arik. 

**Arik**
* So, obviously just getting into this because it's a new suggestion, but, I voiced some concerns in the in the Mafia chat. I think that this actually doesn't provide the same capabilities as before. So I think it actually does limit the usage in a pretty meaningful way, which is instead of having a recommendation of generally using sort of like a single smart contract or even just to use something that 
* Looks like a four, three, three seven contract. Here we're basically saying you can only do one thing. You can only use one contract at any given time. You're committed to that contract. and that's a big change because both 3074 and 7702, all of the versions until now 
* Basically allowed you to have a design space of how you leverage this capability. and, that, like that, this, this, this is a new design space. It hasn't been resolved. What's the right way to use this? And this literally puts the limitation and says there's only one way, and it has to be a single account. That's
* Connected to a single account, forever. Not forever, because you can change to another single account. so I think it's a pretty big change. 

**Tim**
* Can you, can you go into maybe a bit more detail into like, what's a use case that would have been possible before? That's not anywhere. 

**Arik**
* Yeah. So, I thought about an example again, like it's a very preliminary example. And I think it's worth differentiating between use case and capability. There's definitely less capability here. Will over time understand what are the use cases. Right. Yes. But I think just a simple idea of a use case could be I might have an account that I have for very long term things like key backup. Right now, EOA has, like, the backup problem. what if I have some long term account that's very optimized for security? That helps me avoid, like, you know, not having access to a keys or handling will and inheritance and things like that. And on the other side, I would have, like more short term account, that is, for example, delegated access to a private key that is less permissioned in my account or batching or gasless operations or things like that that are more day to day. I could do that with the previous version. I cannot do this with this new version. I'm not saying it's a great idea. Maybe not. That's not correct. Yeah. 

**Tim**
* Why can't you do this? 

**Lightclient**
* That's just not correct. 

**Arik**
* Unless if I understood it correctly, once they have 17702 delegation active, I cannot do other 7702 at the same time that use different code. 

**Lightclient**
* You're, you're overindexing on a very specific design pattern that was coming about from 30, 74, from the last design of 7702. What you can do is you can delegate to a smart account that has a plugin system that allows you to add other plugins that do exactly what you're saying, but it's not. Functionality is retained. It's just in a different mechanism, a mechanism that's actually much more forward compatible with the future of having everyone using smart accounts. 

**Arik**
* I agree that there's other ways of implementing this, but it's a different thing. You're basically saying you can design a different it's a different thing, but the ultimate functionality is the same. 

**Lightclient**
* What you're saying is the functionality is different and it's not well, the functionality, the way that we get to the functionality is different, but the end result for the user is identical. 

**Arik**
* Not exactly, because if the user installs a malicious plugin for some reason, your plugin system is not perfect, then in this situation that malicious plugin will have access to much higher permission actions or like to a different 7702 message. 

**Lightclient**
* If you sign a delegation to a hot wallet that is insecure for some reason, even though you had an ultra super secure backup recovery mechanism, that hot wallet 7702 invoker thing that you signed to has root control of the account. Could steal all your funds, so it's not a reasonable argument. 

**Arik**
* I agree to that. But again, you're saying basically that that system that has two wallets is not a valid design by anybody ever? I'm not sure that's a statement,

**Tim**
* I don't think I don't think that's the that's the argument though. The argument is can we find something that we're comfortable shipping the L1 that introduces a lot of value to users?and has, you know, minimal kind of side effects in terms of the design restrictions. so obviously there's like a trade off where like the most permissive thing you could ever do will have the most security risks. And like, I think we've heard from many client developers that they're uncomfortable if, you know, say there's just no revocation or, optional revocation doesn't get used a lot. so it's not about like, can you enable every possible use case, but like, can we find some set of use cases that are valuable for users, that we think leave the protocol, you know, secure or at least that the trade off we're making in terms of the risks we 
add, you know, are, like sound. and yeah, it is it is very possible that like, at least at first version can't accommodate every possible use case. But it's like, is that still a net improvement on today. and I will highlight, you know, like Marius has this comment, saying we can always ship nothing, but like, we should sort of see this as the status quo in a way where people have been asking for something like, you know, 3074 or similar for like many, many years. And the status quo for the past five, six years is we've shipped nothing because we haven't found anything that's, you know satisfies the sort of constraints around security and like, expressive expressibility. So, yeah, just want to say like, that's the angle through which I would look at, like I wouldn't compare against like the perfect alternative, but against we ship nothing. and is this something that gets us, you know, closer to shipping, something that's valuable to a large set of users? 

**Arik**
* So I think just my point of view on this is I think the current version is better than the new suggested version. Not definitely. Not saying we shouldn't ship anything, definitely should have revocation in the protocol. We were proponents for that from when it was introduced but I think the new version is just not an improvement on the previous one. I think the previous, the existing version actually, that the one that has been merged in the last one, we think it's just better. 

**Tim**
* But I think the concern there is just not better. 

**Lightclient**
* Like, you should come up with a something that's possible in the old version. That's not possible in the new version, because the new version actually provides a more value in the two points I mentioned about resolving the outstanding offs that we don't know about, because it's recorded on chain and resolves the revocation debate that we haven't resolved. Still, those aren't fixed in the current version of 7702 or in 3074. So the older version is not an acceptable solution yet, and this one is something that is potentially acceptable. I think everything that's possible in the old seven, 7702 and 374 is possible in the new 7702 I want to be very clear about that. 

**Tim**
* I see Frangio has his hand up. 

**Frangio**
* Yeah. So I was just looking at this proposal. I haven't seen it before. can you comment, Matt, on on how this interacts with cross-chain replayability? It sounds like because the nonce is incremented unless you broadcast and actually publish the auth to to all the chains you want, at the same time you would have to regenerate the auth later. if you want to submit it to a new chain. Is that right? 

**Lightclient**
* The auth should allow for being, you know, having valueable chain ID. If you use chain ID zero, it should be replayable on other chains. If you do not and you use a specific chain ID, then it's only valid on that chain 

**Frangio**
* But by being tied to the nonce, it seems to be tied to one chain anyway. I might I might get that correctly. 

**Lightclient**
* If you have a new account with non-zero everywhere, then there's no problem. But yeah, if you have already utilized your account and other chains and the nonce is different then you would have to individually sign messages, right? 

**Frangio**
* So I feel like this is one place where it diverges from the current spec. And you have some patterns that are definitely not doable. In particular, maybe when you combine using as AA and EOA at the same time, which, a lot of people have raised, and I don't think there's like a clear understanding whether that's a clear consensus on  whether we think that's what's going to happen. 

**Eric**
* Yeah, just as, as a thought. Why not have the, the new version where that's how we handle long term withstanding, delegation, but still at the same time allow 7702 calls that have a signature in them, execute the code they sign. So do you still have the way to do, like, the ad hoc quick thing that like the specific delegation in a separate process without changing your long term delegation, but then you have the long term delegation active. Maybe that's a solution that gives us both options 

**Tim**
* I guess the one immediate thing I can see is just you're effectively creating two features that do pretty much the same thing. Richard has a question around, like, how this impacts the ops codes and whether it was, yeah, whether it makes things more complex I don't know, like do you have thoughts on that? 

**Lightclient**
* Yeah, it's definitely more complex. All opcodes that interact with the account, with the accounts code in some way would need to be modified. We're basically creating a new we're creating a kind of a pointer in the protocol to say, if I loaded some code and it was of this pointer type, then actually you need to follow the pointer to load to continue loading the code. And this is going to be more complicated. We're making things more complicated as we go. But I think it's not too, too horrible. And we need to resolve the questions around revocation and around, perpetually valid authorizations. And this feels like a good path to doing so. 

**Tim**
* I guess. Okay, Ansgar. Oh sorry. Let's do Richard. And. 

**Daniel**
* Yes. I just wanted to follow up. 

**Richard**
* I was not on the same question. I wanted to have a another comment in general. But yeah, there is a comment on this topic of complexity. First I would first enter this. But if not for me, it was the general First of all, I do like the new proposal, but I'm biased here primarily because for me this proposal is closer towards also as Matt said, that that on the way towards this upgradability real path. But in general, I'm fine with two versions, but I like this proposal. The downside of this proposal is for me, the is what was mentioned earlier in the chat that you cannot basically just deprecate it again. Right. Like because they're potentially the the current version of 7702 is very, very nice since it has no on chain impact, can just deprecate it a lot easier, at least in general. I still think for me, the worst outcome would be to have both at the same time, the current version and the proposed version, because this feels like we're going into a scope creep, which and then we have to have why we have the advantages of both. We also get the worst of both. So I'm not sure if this is really the preferred outcome. And I would rather say either we say, hey we you know, revocation is how it is and we don't go, with expensive schemes or complex schemes where you can bump nonsense than it is how it currently is. It's optional and people can opt out, which is the current version. And I think there are quite some advocates for this also happy with that. Or we say we go with the other one where you say, hey, okay, we limited where you can get the certain functionality only if you bake it into the account that you delegate to, but then you have a strong replay protection because they can always only basically have upgradable accounts and protocol for us. but I think having both feels very dangerous. also when it comes to specifying it, and here generally, I agree with Matt that I think the new proposal solves a lot of questions with maybe some drawbacks, but it solves this biggest question right now around this revocability which or like this. Yeah. And if that is the biggest question, and if I think also here, it would be interesting to hear also the Aragon team, I know it's short term, so maybe not in the scope, but what they think about this because they were the most vocal ones around the revocation at least. So they're probably not the only ones 

**Andrew**
* And yeah, I need to look more into it. But on the surface of it, the new proposal looks good. 

**Tim**
* So I guess. Yeah. 

**Andrew**
* And I agree that we should like, we, we shouldn't like make 7702 super, super generic and have like different, various different flavors. all available at at once. That will be horrible. 

**Tim**
* So I guess, yeah, it does feel like people need time to review this, you know, more thoroughly. And to be sure, the PR has only been out for 17 hours right now. So, it's not like people have had a ton of time to do it. do we feel like it's worth scheduling a separate breakout on this, or do we want to just review it async and, discuss it on the next on the next all core dev EV? yeah. It would be nice if by the next call we, we had something that, people were generally happy with and that, we could use, you know, whatever new version, whatever, it's this one or a tweak of it as part of Devnet two or something like that. that 

**Daniel**
* Yeah. Just to clarify, it's something I mean, it comes a bit what you said right now about Devnet two for devnet one. Would we then implement the current version? Yes, because I mean but the the proposals are quite different. So we might, implement something that afterwards we have to throw away after a few. I mean, not everything, but part of it, of the code we have to throw away after a few weeks because, 7702 is changing again. So I don't know how much sense it makes. If we are very sure that we will change it to continue working on the on the current spec, 

**Tim**
* I guess my understanding from like what teams previously shared is it's like probably less than a than a week of work to finish 7702 for most El teams. If that's the case, it feels like that's still the quickest path forward. but the other, like the other approach, is we just removed seven, 7702 from the next devnet altogether. I don't the one thing I would want to avoid is blocking the launch of 7702 based on, like this draft PR yeah. So I yeah, I know that, yeah. Last time it felt like there was still some value in having the old spec in a PR, even though we knew it would change. but I don't know if  we thought it would change less than it's currently changing, but I yeah, I don't yeah. 

**Daniel**
* At least my impression the last time was that there were discussions around the non handling and the revocation, but nothing else, which seemed rather small. Yeah, but the current spec, is a completely different approach to how we, how we do the current abstraction in this case. So I guess v very different. 

**Tim**
* The teams feel like it is generally if we feel like it's I think the the alternatives is we just do the devnet without 7702 the people feel like that's a better path forward 

**Richard**
* On this one. Personally, as more on the wallet side for us, it's super helpful to even with the current version, not with updated version to play around with it and get a feeling for it. While we can obviously try to set up local test nets, but if it's nowhere implemented then we it will be also harder to get up to the local test nets, right? Like so. This is where possible. And I mean, I know the autumn team doing an awesome job. They're pushing stuff for this, even for 3070 for having something like this would be super helpful. And they're having, it as part of the Devnet would make this a lot easier 

**Tim**
* I don't know any other El teams feel like we should either keep it in or or take it out If there's no other strong objections, I think I would just default to leaving it in because, um. Yeah, there is value in having it 
* And like, there's also some risk of issues when we take stuff out of dev nets, as we've seen time and time again. So I yeah, I would keep the devnet spec as is. and obviously when we test Devnet one, like, it's probably not the most valuable use of our time to test all the different parts of 7702 but like, yeah, it doesn't seem like it's going to delay us a ton. so okay, so let's keep it as it is. we can I'll post after this call in the discord to schedule another, 7702 breakout before the next ACD. I'll look at all the dates that don't have, 14 UTC call, in them already. But, yeah, let's try and have another, another 7702 breakout by the next ACDC. And hopefully by then we have a final spec that we're, that we're happy with. anything else on the topic? Okay. Thanks everyone. yeah, I think this is this is good progress. this was kind of a long detour, but, we we were going to talk about EOF and peer deep nets. But before we go there, anything else on? Just Pectra devnet one stuff. aside from EOF and peer days, do we have a rough target date? so it seems like there's at least a couple EL teams that should be ready within the next week. So it would be kind of neat if even if it's not all the all the teams, if we could get Devnet one stood up with the subset of clients before ACDC. that'd be really cool. My sense is we can get at least a couple, a couple ELs and on the CL side it seems like things are ready as well. So let's try a partial Devnet one set up by, ACDC Yeah, see see how we do on that front. Anything else on Pectra that, Devnet one. Okay. EOF Barnabas, you started talking about the EOF devnet about half an hour ago. do you want to give us a status update there? 

# EOF [39.42](https://youtu.be/8VGf-EE6zNE?t=2382)

**Barnabas**
* Yes, we had a up call yesterday, and, we have agreed that we're going to be testing EOF after Pectra. So after Prague, which means that each line team will have to rebase their EOF code over their Prague code. And we have the Ethereum package already updated with EOF. So client teams should be able to test on that already. 

**Tim**
* Also fix any team updates on EOF. 

**Marek**
* Yeah, I know that Nethermind implementation is kind of ready, but we are still failing some tests so it's not ready. We are working on it. Uh. 

**Racytech**
* At Erigone, we are passing all the validation tests. and it would be. It's just a suggestion. It would be nice to have a actual blocks so we can execute them and test it as well. yeah. Thanks. 

**Tim**
* So, what do you say? Actual blocks. You mean just like some blocks creating EOF contracts and, like, calling various opcodes and stuff like that? 

**Racytech**
* It would be nice to actually test the behavior of the software if we had an actual blocks with the transactions in them. I mean, EOF transactions with them. Yep. Oh yeah. One more thing is that we are not fully ready yet, since some instructions are not implemented yet, but, validation tests, I mean, validations steps are already done. I mean, so far the latest execution spec tests are passing. Yep. Thanks. 

**Tim**
* And then there's an upgrade. an update from reth in the chat saying they're passing state and validation tests. That is, work has begun integrating EOF into foundry. anyone from the beige or get side. 

**Danno**
* I pasted the readiness matrix into chat that shows the, implementation  status Besu has them all implemented. I'll let get speak for them. But the radius matrix, we should. When you have your updates, please update this spec file. 

**Tim**
* Yeah. Any Geth updates? 

**Marius**
* Sure. We are passing all except for one tests from the, stack validation. And, I'm currently trying to make the status work. but they are based on Prague, so I need to revise first. to get everything to Prague. and make the make the make the actual functionality work. 

**Tim**
* Got it. Thanks. So I guess next steps. obviously getting the rebase is done. finishing, these implementations. And if someone has the bandwidth, maybe adding some, full block tests. yeah. Does that seem reasonable? No objection. anything else on EOF? People wanted to discuss 

**Danno**
* EOFs going to move to the implementer calls going to move to biweekly. We'll have a meeting next week and then we'll move two weeks off of ACD. we went to weekly when we had a lot of, spec updates, but now the spec updates has gone to basically none. Now, it's mostly a testing and implementation call. So we can do a lot of that async. 

**Tim**
* Awesome. Yeah, that's a good sign. sweet. Anything else on EOF? And then, yeah, I know we might not have everyone, to discuss this here, but, any updates on the devnet? Or implementation, I guess. I doubt we're at that yet. 

**Barnabas**
* Not one will be based on Alpha three as well. So each, client team suggested that that would be the easiest to do. So the inner change would need to be applied. I'm not sure if any CL people are here, but, the idea would be to be up and running also within the next week or two, maybe just, definite one. Awesome. 

**Tim**
* Any other comments? Thoughts on the peer work? Okay. Anything else on Pectra at all? Nice. Well, okay. Great. Then it seems like things are moving along. just three quick updates then. first off, we discussed in the past a couple of times wanting to have a formal place for, people to leave, like, high quality reviews on EIPs. After some back and forth. it seems like something that's hard to standardize. You know, some EIPs will get audits, some EIPs will get a really good comment on the PR, some EIPs will get a great comment on eath magicians. And so some an idea that, we came up with to address this and track it is that when the EIPs have their discussion threads and Eth magicians, we can basically make it the job of the EIP author to keep track of all these reviews alongside with, you know, updates to their EIPs and, and potentially open issues or questions that still need to be resolved. so I posted this draft in the chat, but the idea is that when you open an Eth magicians thread, you know, for an EIP, you would get this as like a default template to fill out. we obviously can't force people to use it, but it's kind of a nudge towards doing that. and because client teams are the ones who end up reviewing these EIPs and making decisions for them, if anyone has feedback on, like, stuff that should be in this template or stuff that should be framed differently, either we can discuss this quickly here. If someone has something they want to share, but otherwise I would just, uh. Yeah, move the conversation to eath magicians. but yeah, that should hopefully give us, like, an easy way to keep track of, like, these are, you know, if, like, solidity leaves some significant comments on an EIP and they don't want to show up every two weeks to say them over and over, then it should be basically tracked in the first post if the ETH magicians thread on the EIP. yeah any thoughts? Comments? If not, okay. Next announcement. Perry, the ETH clients repo. 

**Parithosh**
* Yeah. So to introduce the organization to EL devs there's this, GitHub org, it's called Git clients. And it contains the, at least from the CL view, the canonical configs for sepolia as well as mainnet. It also contains all the checkpoint sync endpoints. And potentially I think Jasek was mentioning a potential in the future. Also sources to get error files and stuff like that. the idea is that there's at least one admin from each client team, so it's a joint resource that's maintained by every single client team, and we can use that however we see fit. right now there's just admins from CL teams, and almost every CL team is represented there. So we wanted to start adding the teams in there as well so that we yeah, we round out all the client team, admins there. So there's a thread on on all core devs. I can just share the link to the thread. if someone from Eth team mentions, who they want me to add, and I can just validate that and go ahead and add them. Thanks. 

**Tim**
* Thanks. okay. Yeah. Any questions? Comments Okay. and, like, client has an unrelated question, but we have some time. So what's the latest on dropping Pre-merge history for Pectra? Any updates there We. I don't think we've discussed it here. Last call if anyone has updates. So no updates on that. and then. Okay, last thing I asked in the discord if people wanted to have an ACD, on July 4th, everybody wanted to, no one said they would be celebrating and missing this. I'll be out, but, Alex Stokes will be there running the next ACD. so we'll have it at the same time two weeks from now. Anything else that we want to discuss before we wrap up? Okay. If not, well thanks everyone. I'll post a recap on the R&D discord and, yeah, talk to you all soon 

**Tim**
* Fine. Thank you all.


-------------------------------------
### Attendees
* Tim Beiko
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

-------------------------------------
Next meeting on July 4, 2024, 14:00-15:30 UTC

