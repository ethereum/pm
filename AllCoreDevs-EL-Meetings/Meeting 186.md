# Execution Layer Meeting #186
### Meeting Date/Time: Apr 25, 2024, 14:00-15:30 UTC
### Meeting Duration: 1hour 30 minutes
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1016)
### [Video of the meeting](https://youtu.be/iLnBFPH-1Gc)
### Moderator: Tim
### Notes: Alen (Santhosh)

| Decision Item | Description                                                              | 
| ------------- | ------------------------------------------------------------------------ | 
| 186.1 | **Pectra Devnet 0** Marek Moraczyński from the Nethermind team said that Nethermind has implemented all Pectra EIPs and is in the process of polishing them and writing tests for them. Justin Florentine from the Besu team said that Besu is in progress for Pectra EIP implementation and anticipate being ready with them all for the launch of Devnet 0.
| 186.2 | **Pectra Devnet 0** Andrew Ashikhmin from the Erigon team said that he was unsure if Erigon would be ready with the full suite of EIPs for Devnet 0, in part because some of the specifications for these EIPs are still in flux, and because the Erigon client is undergoing a transition to a new major version release, Erigon 3, that is taking up resources and time from the team
| 186.3 | **Pectra Devnet 0** Erigon 3 and Pectra EIPs will be finalized and built into the Erigon client together. “Lightclient” from the Geth team said that Geth is “days away” from being ready for Devnet 0. Gajinder Singh from the EthereumJS team said that Ethereum JS will also be “good to go” for Devnet 0. Developers have not yet set a date for the launch of the devnet but based on these client responses, developers will likely decide on a date over the next few weeks.
| 186.4 | **EIP 7685** Lightclient has merged EIP 7685, which creates a general-purpose framework for storing EL-triggered requests to the consensus layer (CL), and its impacts on EIP 6110 and 7002 into Pectra specifications. Beiko said that developers should include this EIP and its subsequent changes to other Pectra EIPs in their Devnet 0 releases.
| 186.5 | **EIP 3074** Ahmad Mazen Bitar proposed changing the behavior of EIP 3074 to allow DELEGATECALL before AUTHCALL to broaden the use cases for the EIP. Derek Chiang founder and CEO of a blockchain wallet operating system called ZeroDev proposed the creation of a “noncemanager” to facilitate global revocation of AUTH messages if needed, among other changes. Some developers on the call pushed back on changes to EIP 3074 that would greatly increase the complexity of its implementation.
| 186.6 | **Other Pectra Proposals** developers moved on to discuss what other code changes should be considered for inclusion in the Pectra upgrade. Geth developer Marius van der Wijden said that this should depend on whether EIPs with high complexity like EOF are going into the Pectra or not. “If we were to include EOF, then the fork is definitely full. If we’re not including EOF, maybe we could include something more,” said van der Wijden.
| 186.7 | **Other Pectra Proposals** Siri raised concerns about the inclusion of EIP 3074 in Pectra without a security audit. Beiko recommended tabling this discussion until specifications for EIP 3074 are finalized and there is a “reasonable concern” based on those specifications that could be addressed through an audit.
| 186.8 | **ACD/EIPs & L2/RIPs** developers discussed changes to Ethereum’s EIP process considering the new RIP process. Dietrichs noted that it has been six months since developers launched the meeting series for rollup coordination, RollCall, and the RIP process. There are outstanding questions about how these processes will and should impact the Ethereum EIP process down the road. An ongoing research question among L2s is whether long-term equivalence to the Ethereum Virtual Machine (EVM) is desirable for rollups or not, said Dietrichs. He also added that an open question is to what extent changes implemented on L2s will or won’t eventually impact protocol decisions on Layer 1 Ethereum.

**Tim Beiku**
# Intro
* Good morning everyone. Welcome to act number 186. bunch of things to talk about today. I think the most important thing is, making sure everyone is aligned on the Dev net zero specs. I believe they're now frozen, but there's been some l discussion on the CL call last week, and then a couple tweaks since the last call. So, yeah, just want to make sure we're all on the same page about the scope for dev net zero so teams can, continue working on that then, 3074.
* I think Nethermind had, some behavior that they wanted to clarify. And then there were a bunch of proposals for tweaks to the EIPs. So I think we should discuss those, probably in the context of like, future dev nets rather than, changing the dev net zero spec. and then after that, there's a bunch of other EIPs that people have wanted to, propose for Pectra. it might make sense to go over them, but also just to hear from client teams how we want to proceed, given we still have a lot of stuff to implement. so we might not want to, like, commit to even more stuff right now.
* And then if we have time to get to this, there were some questions in the agenda about how we want to think through the, L1, L2 governance separation and, how things like our EIP and EIPs should interact and whatnot. So, yeah, we can leave this for the end, but I guess just to kick it off, the teams want to give a quick update, with regards to where they are on Devnet zero. I know we have the implementation tracker, but yeah, any team has, any team want to share sort of where they're at now, any blockers that they have or. Yeah. Floor is yours. 

# Pectra EIPs [5:18](https://youtu.be/iLnBFPH-1Gc?t=318)
**Marek**
* So I can start on my side. I think we can say that we are almost ready for devnet, because we have all draft's implementation of all the EIPs. And we are right now polishing them, writing some tests. But of course, there are some things, that are easier to test on devnet. So there might be hiccups, but it's better to try, like, sooner than later. Nice. 

**Tim Beiku**
* And the other team. 

**Justin Florentine (Besu)**
* Yeah. Basically you can go, similar situation. We have everything in progress. 2537 is done. 6110 and 7002 are done pending, some revision to adopt the 7685, mechanism to wrap them up. so that's the same status as last week from the consensus layer. And, I think that's about it. Auth call are in progress. Sweet. So we are anticipating participating with all that stuff in dev net zero. 

**Tim Beiku**
* Very cool. anyone from Geth, any other team.

**Andrew**
* Well, for Aragon, we started, looking at most of the EIPs, but, and we implemented the BLS Pre-compiled one, but, I'm not sure, because that will be ready for Devnet zero, because, it's not it's far from being complete. The implementation. and also where in the middle of, a big change, we are switching internally to the Aragon three branch, which has been in the works for, well, for years now. yeah. So, we might, get, slowed down because of that, but it's a big, move for us. 

**Tim Beiku**
* Got it. And I guess your your expectation is that, Pectra will ship on Aragon three, basically. 

**Andrew**
* Yeah. 

**Tim Beiku**
* That's right. Got it. Sweet. anyone from Geth? 

**Lightclient**
* Yeah, we're in pretty good shape. We have 6110,7002 implemented using requests. 2537 is emerged. I'm not sure Mario's if the subgroup checks were merged yet, but we have those updated and 3074 is still in progress. But you know, in general, we're days away from being ready for a devnet zero. 

**Toni**
* Nice. 2135 is also ready. 

**Lightclient**
* Right? 2935 is also ready. 

**Tim Beiku**
* See, I don't know. Does anyone from Ethereum JS as well? 

**Gajinder**
* Yeah. I think, most of the things are ready. We just need to, integrate some 65, and we should be good to go. 

**Tim Beiku**
* Awesome. yeah, I guess. Yeah, maybe. Let's talk about, 7685, given that seems to be a common thing across, different teams. Matt. So I know you followed up with all of the teams over the past couple of weeks. Oh, Antonio, we can do the subgroup stuff after, if that's what your hand is for. but yeah, let's do let's do the message bus.  Do you have a feeling for like. yeah. Whether everyone is on board with this, is there any team that basically had concerns or issues? 

**Lightclient**
* It seemed like most people, most teams were on board. If anyone has complaints or questions, maybe we can surface those now. 

**Tim Beiku**
* Okay. So any objections to the generalized message bus? If not, Then I think this is something that makes sense to include as part of Devnet zero. Given it's a relatively small change and, sort of it's pretty fundamental to how we build a bunch of EIPs and we don't want to have like a version that doesn't use it. I know you had some PRS, 2611 2610 and 702 that based on this, I believe those have already been merged, right? 

**Lightclient**
* That's correct. 

**Tim Beiku**
* Okay. So then yeah, given that, like, effectively the spec already uses this, we can just add this EIP to the list. that's included in Pectra and part of Devnet zero. And continue with the PRs. continue with 6110 and 702, based on the latest PRS. Does that sound good to everyone? 
* No objections. and yeah, I missed rest in the updates before. I don't know if there's anyone from rest who wants to give a quick update. Okay. If not, we can move on. Antonio? You. Oh, Mario. Yeah. 

**Mario**
* Yeah, I just wanted to give a quick update on tests, if that's okay or. Yeah, yeah. so yeah, we have a very good set of tests for the Precompile and also for 6110. Those are basically done. I think 7002 tests will be done probably today if everything goes fine. remaining is the 2935. We don't have tests for that, but I think they will be done this or next week, probably. And when it when that is done, we will make a release with all the fixtures so the teams can consume them and also verify any bugs before devnet. 

**Tim Beiku**
* Nice. Thank you. And. Yeah. Antonio, you had your hand up, I believe about the BLS. Yep. 

**Antonio**
* Sure. Yeah, exactly. Thanks, Tim. Yeah. I just want to make people aware that basically, like the 2527 was has been stable like for years, but has been kind of, addition that is non-trivial in the last week. 
* So basically we now require subgroup checks for all the operations but add so in case people want to update their implementation, this is the right time to do it. And there is a bunch of, test vectors that has been added as well that cover all the corner cases, including this subgroup, checks that are mandatory. 
* Now, just this like announcement. I don't have anything else. 

**Tim Beiku**
* Thanks. Yeah. And I think we had your last commit in the spec for Devnet zero. But if you have a chance, can you just put the the PR, the commit in the chat so everybody can reference it? 

**Antonio**
* Sure. I'll do it right now. 

**Tim Beiku**
* Thank you very much. Okay there's some comments in the chat about when Devnet zero with different dates. . I don't know if like, it actually makes that much sense to set a date here. Like if the earliest is going to be, you know, sometime next week. 
* But I think we can probably coordinate this offline. as client implementations start to be ready, and maybe have like a bit more of a discussion on like having more clients join next week. 
* Yeah, I don't know. Does anyone see a strong need to, like, set a target date right now? * It seems like we can just keep working on the implementations and, launch it whenever it's ready. okay, I have one. Yes, in the chat. okay, let's do that then. and I think. 
* Yeah. also based on, like, Mario's, comments earlier, like, once we have, test vectors as well for more of the EIPs, then it's valuable for clients to actually, run through those, make sure that we're passing everything and not just launch a dev net where, we find bugs that the static tests could have caught. yeah. 
* Yeah. Anything else on Devnet zero? Oh, uh. Shall we? Yeah. Yeah. You want to talk about the bug? 

**Hsiao**
* Yeah. So just before this call, Dustin, he found the, test vector error, of the consolidation. So, we will fix it, and it. 
* I think the error is just in the test vectors, so we'll fix, cut a new release soon to address it. And also we will include the PR desk, new test on it, and also extra Electra test. Thank you. 

**Tim Beiku**
* So. Yeah. So, to be clear, the specs themselves should not change. It's really just the tests for all those things, right? 

**Hsiao**
* It's no substantive change to the electoral part. Got it. 

**Tim Beiku**
* Okay. Anything else on Devnet zero? can we get an El test release or at least field test before devnet? so Mario said they're planning your release for next week, but, targeting BLS 1107,0229, 35. 
* I think that's everything on the L side. Mario, will the Wilder release from next week basically target all the EIPs from Devnet zeros? Or is there. Oh, I guess maybe article is not included. 

**Mario**
* Yeah, maybe. Probably article is going to be. But the ones that we are trying to aim for the release are the ones that are like, absolutely necessary. For example, the 7002 and 6110, they have changes to the header. 
* Yeah. So, for the exception of 3074, as long as we don't call the opcode, the test will work. Yeah. 

**Tim Beiku**
* Okay. Okay, so we'll try to get test vectors for everything but auth call next week. And then we can add the test vectors for 3074 after. 

**Mario**
* Yeah. Yeah exactly. 

**Tim Beiku**
* Cool. Sweet. Anything else on Devnet zero? Okay so 3074 there was a comment by Nethermind, about clarifying some behaviour and then a bunch of requests for changes, from, different, developers. 
* So I think it makes sense to first address, the Nethermind concern, and then we can maybe go over, the other sort of proposals for it. who was it from? Nethermind. it's me. Yes, please. Yeah. so it's it's. 

**Justin**
* I think I have, miss, said it in the GitHub issue. It's basically delegate call before auth call, not the other way around. 
* Okay. so apologies for that. and so basically the idea was that currently auth call only works for the authorized invoker and the invoker cannot be some kind of a proxy contract that can, delegate the authorization to another implementation. 
* So, we were, I was thinking that, this will prevent, certain use cases, from emerging, and maybe we can we should look at it in a different perspective. There is some suggestions, to do it in another way. 
* So instead of allowing delegate auth call after delegate call, I think light client told me that, he's thinking about an approach where we, initialize the invoker contract inside the frame of the EOA, light client. If you if you if you care to elaborate. 

**Lightclient**
* I've sent this.  Around in a couple of places, but I guess the TLDR is one idea that I'm thinking about is to possibly change the behavior of auth call so that instead of just modifying the message sender. 
* So in the next frame you call like exactly the target that the EOA wanted to call, you actually call into some target code that was signed over in auth, similar to how the EOA. I think there's a lot of a lot more ability to reuse existing smart account code in this type of format, so it's something I want to look into. 
* I'm generally feel okay about allowing delegate call in 3074 in this format, or just allowing it in the currently specified format, but I'm not sure that there's going to be much change in 3074 for the next month or so as we're working on Devnet zero. 
* I would just like these conversations to continue happening and maybe have some sort of concrete proposal of change in one month's time. 

**Tim Beiku**
* Yeah. So there's a comment, by Ansgar saying, you know, this feels like a rather big change, I guess, talking about big changes to 74, it doesn't make sense to cover the other proposals and sort of see where we stand after that. Or do people have comments or thoughts? Okay. Have a plus one for the other proposals. So the other one, who was the first one that posted about this on the chat? so, Derek, I don't know if you're on the call. Derek chang that. Yeah. Yes. Do you want to talk to you? Talk through? Yeah. Your proposal. 

**Derek**
* Sure. Yeah. So. So the proposal was actually first proposed by, anchor from, dichotomy, you know, which I think you know, who I think is also here, you know, but but basically, like the idea is that, so, so basically, like, right now it seems that there are two different needs, when it comes to the nonce parts of the auth message. Right. So basically, like one group of people wants a, in vertical way to revoke nonce messages. So like in particular, I think they want to be able to revoke all the messages in a way that is independent of the invoker implementation.
* Right. You know, so so I think the concern here is that if the invoker is like buggy or malicious's, 
* There should still be a way for the user to revoke messages. and then there's like another group of people who have a lot of problem  with the, with the fact that. By including the nuns into the auth message. Every time you send a transaction from your EOA, you are revoking all outstanding auth metrics. Right. So the issue here is that so so so so for example, so, so for my, for my company, zero dev. so we are building a kind of abstraction based embedded wallet. Right. So some of the most popular use cases involve long standing authorizations, right.
* You know, so for example, session keys, the idea that you can attach a temporary key to your smart account and then, you know, basically like have other people send transactions for you. So if we were to implement that on top of 374, that would depend on  a long live auth message. 
* Right. And really like any other use cases such as like for example, like attaching a pass key to your to your smart accounts, that will also depend on that. Right. So the fact that like every time you send a message from your UA, you're killing all long live auth messages I think will be like a really, really big issue for this. I guess like smart account use cases. So the, the proposal that, you know, Ankur and I wanted to propose, is essentially, so I think, I think I would probably send a, put a link here, you know, but basically, I'll just put the link in the chat before I. Uh. Right here. Yeah. So basically this is the idea. And then you can see my reply to this message like right below this message. Right.
* So, so basically the the TLDR is that, we change the nonce parts of the, of the spec. sorry, like the, like the nonce part of the auth message to to two things, which is nonce manager edges and nonce manager nonce. So the nonce manager, the nonce manager can be any edges. So it can be a EOA or it can be a smart account. Right. so sorry, like a EOA or a smart contract. Right. So the most basic way to use this would be to set the nonce manager to your own UA, in which case you get the exact same behavior as today, right? In which, like if you send a transaction from your UA, you are you are revoking all messages. But this also gives you the ability to, essentially use another contract or, you know, you know, like another EOA or another contract as your nonce manager. 
* So, for example, I think like one very powerful way to do this is to use a counterfactually deployed contract as your nonce manager. So this counterfactually and deterministically deployed contract, will be essentially owned by your EOA. Right. So you don't. So you don't actually have to deploy this contract to have a nonce manager. So you can specify this contract address as your nonce manager. And then like when you actually need to revoke a message, you actually deploy this contract and you increment its nonce. Right. You know, you know, in order to revoke messages. But this means that first of all, you don't have to pay any cost to have to have a nonce manager.
* But then secondly, like it gives you the ability to both revoke auth messages out of protocol. so not not protocol, but just like independent independency of invokers but also it doesn't mess with the fact that you can, you know, just like use your EOA without accidentally revoking or outstanding auth messages. Yeah. So, basically this is a proposal to meet both needs once the need to have be able to revoke auth messages independently of invokers. And the second need that is the ability to use your ilas without accidentally like revoking all outstanding auth messages. Yeah, a that's a deal. Yeah. 

**Tim Beiku**
* Got it. Thanks. Ansgar, I believe you have a response to that. 

**Ansgar**
* Let's say. I mean, I think it's an interesting proposal, but the way I think about 3074 is our goal was really to basically. Be, because the nature of invokers is so unusual, because you can't just have arbitrary invokers, but every individual invoker has to be manually whitelisted by the wallet, which means we only end up with every wallet, will only end up supporting two, three, four and kind of community wide, big kind of standardized invokers. And because of that, we have much better trust guarantees about these invokers. And so it makes a lot of sense to try to delegate a lot of special purpose logic to the realm of the invoker. So, for example, in this case, you can get the exact same behavior by just making the kind of the in protocol nonce checks slightly more permissive.
* So you could for example, basically or at least very similar functionality, where basically you just in protocol instead of always enforcing the nonce restriction, you can basically make it optional. You can say if you sign over the zero nonce, basically it means now, now the nonce is non binding. And then we could basically instead of this having been an enshrined part of 3074, it could just be an ERC. So there's an ERC for if Invokers one they can opt into a nonce manager pattern. And then we could basically just on the social I enforce that hey, wallets should only whitelist invokers that follow this nonce manager pattern if we think it's a useful pattern.
* Right. And because again, like wallets will only there will be like 3 or 4 really, really popular kind of ecosystem wide invokers like like a batching invoker, like whatever. Right. So so we can just basically pick whatever community standard we like. 
* The big advantage of this is that instead of having to make a hasty choice now, which constrains functionality forever and is very, very basically opinionated about the choice, we delegate it to the ERC layer, where we basically then can take the proper time for the next one, two, three years, figure out what is the best patterns there, and then all come together around those features. So I personally be very, very strongly opposed to enshrining special purpose functionality like that directly into the opcode itself. 

**Derek**
* But just making sure I understand. So, like, like, are you proposing that we just remove nones altogether from the message? 

**Ansgar**
* Or you could. So yeah, to to press that out. So basically what you could do is you could say that you say if the nones is zero, basically it's not binding in the message. If it's not zero, it's binding. What that means is that by default the signer can choose right. What do they sign over. So your wallet could basically say, hey, I always make my auth messages revocable. I make them non-revocable. It could be a setting we can figure out should should this be in this setting explicit to the user. Is this insecure expose to the users. Do we want do we not want it. We could figure this out in proper time, right? We wouldn't have to make that decision now. And what that also means is that the invoker now could, on top of that, add restrictions. 
* So basically I could write an invoker that says, hey, my signatures always have to be revocable, right? Because it can it can impose some, some validity conditions on that nonce field. So that way basically we could just the protocol itself is unopinionated about it. And then it is up for the later on the community standardization process to figure out what rules we should enforce. 
* But we can end up in the exact same world with invokers that enforce the exact same rules. But we don't have to make that decision once forever in protocol and enshrined and hard to change in the future. But instead we make it on the ERC side. But we have much more flexibility. 

**Tim Beiku**
* And just to make sure I understand. So the changes that this would make the 3074 is effectively make that one field optional. 
* When you do an initial signature, and we hope that there's like a set of best practices that, emerge around just like either requiring that or disclosing it pretty clearly when, when it's not revocable. Is that is that correct? 

**Ansgar**
* Yes. And I would, by the way, propose the same thing for the chain ID as well. Make it optional. 

**Tim Beiku**
* Got it. Daniel. 

**Danno**
* So if we make the notes optional, we make internal authorizations possible. And that's where my big concern is, is unavoidable internal authorizations because we'll always have buggy code. We'll have supply chain errors. We'll have user error. I still want some mechanism such that, if there is an internal authorization, it can be revoked in setting the notes to zero. you know, if there's a way to create a permanent one, that's kind of the problem. That's what I'm looking for is some way to revoke these. And I agree with Ansgar in that, putting the parameters into a smart contract and the OP code is way too early. so. Yeah. So I don't like that proposal either. 

**Tim Beiku**
* Richard. 

**Richard**
* You just wanted to like to the part. Like what making optional means, right? Like, because it's interesting making a parameter optional, like, here we have like multiple parts in the horse call and there's a commit part where it becomes more optional if we move it there, and which I think more the IRC part, but also here, if we want to keep still on the outside, the same compatibility where we say we would want that the account nodes could be this global revoke, then we would also need a way to access the nodes the continents, which is currently not possible as an opcode. Right. Like so. Basically the question would be should we then push a nonce opcode?
* Which again increases the complexity. Or do we say? I think everything else is just another step that potentially then if we go the extreme argumentation route could be backed and not be called. 

**Tim Beiku**
* Yeah. Ansgar. 

**Ansgar**
* Yeah, just briefly on that point though, because if you still have the option, at least on personal loans, then you can always basically still accept access your own loans. And then for other contracts you could basically because you can just have arbitrary logic, right? You can basically just have yes, they cannot currently access their own loans, but you could just have any other repay protection mechanism. Instead, they can just manually write to storage and it has the same effect. 

**Tim Beiku**
* Okay. And there was a bunch more comments in the chat, but, including one by Mario saying, you know, should we have like, a specific breakout room to flesh this out? I. I sort of am leaning towards, though, like, it feels unlikely. That we like. Agree on the large design change of the EIP right now. and you know, there. I think there are some, like, there's a concern that like, you know, if we send this back to breakout rooms, we just keep iterating on it, forever and then end up not shipping something in this fork, which is not great. so. Yeah. The. Yeah. The people feel like, a breakout room potentially next week and then seeing if we want to make that recurring for a while, that would be valuable.
* I think. We probably want like some solution or final spec for this in the next like month or two. if we're going to actually ship it in Petra, assuming it's like a relatively simple change, and overall the ship is not like a huge one, but. Yeah. Does that make sense to people? Okay. No objections. I guess maybe if people want to coordinate in the chat here on the discord to find a time. yeah. I think, basically discussing the topic of revocation. We didn't even get into chain ID today, but, based on, ansgar's comments, you know, maybe we can use a common mechanism for for all of that. Yeah I. Yeah. Okay. So Matt will set up a breakout room where we can discuss this further.
* We'll keep, I guess, maybe back to the original concern. on the nevermind side. 
* Does it make sense to make that change? with regards to delegate call for Devnet zero, my sense is no, we should just keep this spec as is for Devnet zero. And then when we have, when we have, like a consensus on the updated spec, we can just move the whole thing. Does that seem reasonable to people? Okay. so, yes, Ahmad zero has 3074. but we would not change it from the current spec. And, yeah, there's a comment about, like, fully removing 3074 from Devnet zero. I would lean against it because it still seems like teams are in favor of doing it, and it's more a question of how rather than if.
* But yeah, if, a month from now we realize that there is no path forward and no one is happy about it, we can we can always remove it then. Okay. So Siri, I see you have your heads up. Is this about 3074? 

**Siri**
* Yes. the suggestion was that we would discuss the additional stakeholders, who, did not get a chance to voice their concerns about 3074 in general. And perhaps consensus was formed prematurely before pulling in, sufficient, community members. So I think there are some people on the call that have concerns about 3074 being kind of bad in principle. and something that would, slow us down, on the path to full account abstraction, you know, that  it's, essentially a kludge, that it doesn't give us things like, key rotation. I mean, we would need to. 

**Tim Beiku**
* Look, I think we we have basically discussed this for, like, the past four months on this call on and off. And I know there's a ton of ETH magician's thread. I know there's other proposals. I know there's like some, effectively, like tech debt that we get out of this if we move to a like full, say, 4337 world. My sense is that despite all of that, client teams still seem pretty in favor, and it does seem like the most, I don't know, the proposal with the most consensus in the short term that we could actually, you know, improve the state of EOAS, in the next fork. So I guess unless there's, like, something new, that came up and, like.  Yeah, I would. 

**Siri**
* Client teams shouldn't be the only ones that make this decision. This is something that affects everybody. And, you know, we should hear from other stakeholders. Unless we want to say that basically we're handing over governance, the client teams, which I don't feel is a decision we ever made explicitly. It's quite unsafe in my opinion. So if we don't want to veer into the realm of making contentious hard forks with everything that entails, I think it would be better, to try to get a feel for what other stakeholders, how how they view this proposal. 

**Tim Beiku**
* I mean, I think this proposal was first brought by like, not like I mean, Non-client team developers requested this for this fork. And again, we had a bunch of conversations about this. It's fair that like some people disagree. And look, I agree that we should, you know, we should get broader input in that. But, Yeah,  I'm not. I'm not convinced that there's that much value in, like, rehashing the whole debate again. But. Yeah. Martin is this. 

**Siri**
* I don't think it's about rehashing the arguments. I mean, some of the arguments may be some people have not heard. It's just filling out whether we do have consensus because, you know, this is, again, something that affects everyone. And there's a trade off here to be made between improving things on a short term basis, with, something that does have potential UX improvements but also has potential US drawbacks, depending on how you implement it. Also in other levels of the stack, like wallets, whether you're whitelisting or you want, you're not whitelisting. So I think I feel like it's important for us to at least and for the client teams to at least understand how other parts, of the ecosystem are viewing this.
* And if it's true that, you know, there is actually consensus, then, you know, that's one thing. But if it's just something that's, you know, convenient and easy to implement, but maybe it gets us stuck on a local maxima and delays us in getting UX improvements that are more sustainable long term and, you know, improve the UX for everybody. Maybe that's a trade off that we want to discuss. Because, you know, ultimately this is a value judgment on what you want to prioritize. so I feel like we should at least hear other people out. 

**Tim Beiku**
* Yeah. Martin, please. Yeah. 

**Martin**
* Yeah. So I think well, I have probably been one of the voices who have been critical, critical about or at least raised some concerns about 3074. Still, I do think, progress is important, and I really don't want to, stop this progress and essentially kind of, yeah, kind of try to heckle or reverse that decision. I think I would say we should go forward with, 3074, but I still wanted to bring the perspective that it brings. yeah. My contract developers in a, in a yeah. Well, challenging perspective or position because clearly we want long term account abstraction with things that key rotation. And the question has always been is there a path to upgrade us to do that or is a manual transition necessary.
* And with 3074, kind of the answer lies in between. it is partially by doing this migration of EOAS, but not fully so kind of for smart contract teams, it's just 3074 without commitment to 503, put them in a, in a hard place. And I heard that from obviously I talked to safe, but also to the other, smart contract teams. because well, now it's not clear. should we try to convince users to give up their EUAS and move to, a smart contract, or is there actually a path to to stay on this EUAS and fully upgrade it? So I would say, or my wish would be that there is a commitment to one of those two paths.
* So essentially saying either yes, we say we want to upgrade, EUAS and there will be whether it can be directly included in this, fork or in a future one, but at least there's a commitment to, yeah, let's say 503. 
* Well, that would be great. Or if or also if there's a commitment. Okay. This will not happen. But then that would also, be an answer and then, you know, okay, well, then you can use 3074 at least to make it very efficient to batch or to to do a large transaction and move all your funds over to a smart contract. I mean, that's also something to work with. But this uncertainty is, is quite challenging. 

**Tim Beiku**
* Thanks. Yeah. And I think that's that's very fair. Like, yeah. Like whether 3074 has a path towards full smart contract wallets. yeah. Is an important question to, to, yeah, to determine, and I will say, yeah, like we did consider, you know, 5086 early on this year and had a bunch of conversations about that. So, yeah, there is a tension between like rehashing all those conversations versus, yeah, moving forward with something, that actually improves UX today. Ansgar. 

**Ansgar**
* Yeah. I just wanted to largely, Echo and agree with what Martin, just said. I think some of the kind of the concerns here from the side is more on the process side. Like, we obviously debated this for quite a long time, and I think a lot of the concerns came only after the decision was finally made, which, of course, is not how that should be. At the same time, I understand that the governance process is not even though it's open. It's not always super legible for people who don't as part of their full time work. Pay attention to it so actively. So I feel like it's important that we kind of find this some sort of compromise here.
* And I think actually, because we've had precedent, right, of changes that are kind of preliminarily accepted in Tupac and then relatively close to the fork, we make a final go, no go, no go poll and potentially pull it back out, which is always not that hard to do. So I personally would propose that we basically spend the time between now and when we would have to make a final decision. The default would be that it is assumed that 3074 is in, because we did accept it after all, but that basically now there is a responsibility for us to really spend the time sketch out a concrete plan that includes like a proper kind of long term transition path, including like,
* I don't think it makes sense to consider gaps like 5503 for, for for spectra. But I think, for example, committing to to shipping it as soon as possible afterwards or something or, some, some general upgrade path.
* So basically on that side and then also separately just basically having a very kind of reliable path for compatibility, even in the meantime between 3074 in place.
* And I think basically we should, we should only we should, we should make have the understanding that 3074 will  be pulled out unless we make enough progress there, that by the time we make that decision, everyone is happy about the path forward. And I feel like that, that that seems like a reasonable compromise to me. 

**Tim Beiku**
* Marginal to everyone, I think I agree. yeah. Vitalik. 

**Vitalik**
* Just like one side point in terms of this, idea of, agreeing on a path forward, beyond spectra, one other side of this. 
* That's, worth keeping in mind is basically, signaling ahead of time what kind of guarantees and invariants are going to exist versus, are not going to exist. And so there's possibly value in doing some kind of, signaling similar to how we deprecated self destruct. But like for example, deprecating the idea that, if an address has no code, then then it's not non-transferable or like similar kinds of things that are used by, like for either soulbound token people or other kinds of applications, like, I feel like there's like some small number of, applications that, rely on certain invariants that exist today that are definitely not going to exist in a smart contract world. And this is one other of those, like 2 or 3 hard fork things. That's, also worth thinking about pretty far ahead of time. 

**Tim Beiku**
* Yeah, I think that's that's actually a really good point. Like especially something like, you know, if we did 503 and for whatever reason, we can't include it in this fork. and that changes, you know, effectively the invariant on a smart contract on an EOA. We can then, yeah, have just like an informational EIP in this fork saying like, as of Osaka, you know, you can't assume that an EOA stays an EOA. And this is also good just in terms of like if. Yeah, giving people time to deal with this behavior. 
* So if, for example, we decide in like 2 or 3 months that we want to do 503, and then we ship that 2 or 3 months after that, it feels like a really quick timeline to change, you know, something that's been a pretty strong invariant for like, yeah, over five years, almost ten years at this point. 
* So I guess. Clearly we're not going to come up with a final spec now. like client said he would organize a breakout room on this. where should people go to? Just like. basically help schedule the time for this breakout. 

**Lightclient**
* It's all posted on all core dev discord. Cool. 

**Tim Beiku**
* Yeah, I think I think it makes sense to have it there. And I think, yeah, we'll definitely open a GitHub issue as soon as we have like a rough time. and I think for anyone who thinks who has like a different perspective or, you know, concerns about 1374, it makes sense to bring them up there. 
* Yeah. So anything else on that EIP? Okay. Thanks everyone. I appreciate people coming and sharing their thoughts on this. and again, yeah, for Devnet zero, let's just leave it as is. And, hopefully in the next month or month and a half, we can have sort of a V2 of the EIP that we can then, change all at once. next up, there were a bunch of proposals that people also wanted to get included in spectra. I've listed a few on the agenda, but, two more that, weren't posted in the agenda. But I know we've been discussing your obviously eof. And then Eaton had a bunch of SSD related EIPs, that he he posted in the Ether Magicians thread.
* I guess given that we have already like 6 or 7 EIPs in spectra that client teams, have not implemented those, do there's any like, client team feel comfortable including more stuff yet? If not, how do people think we should proceed with regards to, like, signaling what we might include in this fork? Do we think there's any chance we can include anything more? Yeah. How do people feel about that? 


**Martin**
* Kind of depends on what we're, what we're going to include. 
* Like for definite zero. We're like, we're definitely not including anything more. Yeah. for spectra, if if we were to include EOF, then the focus. So it's definitely full if we were not to include us. Maybe we could include something more, but even then I would be kind of against it. 

**Tim Beiku**
* Got it. Any other. 

**Siri**
* Well, not not speaking as, one of the execution client teams, but, there are there are still some potentially unresolved, security concerns in regards to the EIP 3074, and it is possible that they will be resolved, on the devnet one way or another. But it's possible that the ones that we've kind of, flagged as potential issues are not the only ones. And it's been three years since the last audits and quite a few things have changed. so there is potential interactions, that we may not have fully taken into account and seems to be a little bit safer if we do more work just to validate that this is going to be, you know, safely interacting with everything else. And yeah. 

**Tim Beiku**
* I think they're probably the best, the best approach is one, getting to a spec that people think is reasonable. Once we have that, I think we can consider whether or not we want to have an audit. 
* I don't want like, an audit to be like a reason. We just use the delay making a decision if people actually understand the risks and are comfortable with them. Not that like we should never do them, but, historically, there's probably like a 5050 hit rate as to whether these are actually, you know, quite valuable and provide us new information on something or, just something we do to effectively, like get more confirmation on like, or at worst delay kind of the process.
* So I definitely wouldn't want to commit to like imposing this extra requirement on this EIP until we have one a final spec and two, like a reasonable concern to think that there's something about this spec that's like unique in that they requires like an audit, whereas like by default, the IPS don't get a full audit before they go in. 
* And I guess yeah. Back to like the just the broader inclusion point. So there was a comment in the chat on 7212, which is like a relatively small change. and it feels like there are a bunch of relatively small chains that are being proposed. 
* So, you know, 503 is one, 7623 to call data repricing is one, you know, are there changes that teams would like to CFI to sort of signal a short list for stuff that's being considered for spectra, do you? Do people want to just, leave the scope as is, move forward on the, implementations and then, you know, revisit this in a few weeks? 

**Justin**
so a personal, opinion is to include, 721, or, a similar widely supported elliptic curve, to actually improve account abstraction for the users. if we like, instead of, trying to, say that EOA will stop account abstraction from proving we should actually try to improve account abstraction so people actually try to move to that. And 7212 does exactly that. It improves, how account abstraction could deal with, they use the user's keys and allow things like, passkeys and, fingerprint, authentication and our fingerprint signing, etc.. biometric signing. a lot of other possibly key holding, devices like YubiKey, etc.. So these things I believe that including something like that will actually do improve, account abstraction and a meaningful way.  

**Tim Beiku**
* I know Besu was like in favor of 7212, but yeah. Any other thoughts from client teams on this? 

**Andrew**
Eragon is also in favor. 

**Lightclient**
* So I think the. Yeah. I think one question that we had was, is, R1 the right curve to be adding as a Precompile, I am under the understanding that there are there is another curve that is starting to gain adoption and that people are migrating towards. I feel like if we're going to add a precompile, it would be better to add the precompile that people are moving towards it right now rather than the precompile that's on the way down. But this is something that is like a bit outside of my expertise, so I'm not sure if anyone. 

**Vitalik**
* Up at Rising Curve do you have in mind? 

**Lightclient**
* I have heard that people are looking at moving towards E22519 as an alternative, but I don't really know, like what the status of that is in hardware. 

**Vitalik**
* And. Yeah, I don't either. Like, I definitely know that E22.51.9 is a super popular and just cryptographic applications in general, just because it's, a very fast curve and it has, addition equations that don't have any sub conditions, which makes it like simple words and, side channel safer. But, yeah. Hardware support. it depends. maybe we again, this this gets into a bigger rabbit hole of, like, just how general might it make sense to make an elliptic curve? Uh precompile. But, might be worth taking offline. 

**Tim Beiku**
* Ansgar, is this on the same topic? 

**Ansgar**
* Yeah. Just wanted to very briefly mention and just to flag for people that they're aware. So 7012 happens to be the only the first and so far only EIP that has been shipped to layer two. So there's quite a few layer two's already that have this life in production, which of course does not, you know, have to force our hand at all on many decisions, but at least it's something we should we should take into account. So, keeping keeping in sync with features that are shipped on layer two, I think should at least be a small reason to what's doing it? 

**Tim Beiku**
* Yeah, I guess based on all this I would lean towards just making 7212 CFI. So we have it as like part of our short list, not committing to implement it, you know, in the fork yet and definitely not in dev net zero. Yeah. Anyone against that. Okay. And I guess. Yeah. Are there any other. Of the proposed EIPs that client teams would like to sort of CFI so that we can. you know, consider it for the next step once we're a bit farther on on these implementations. 

**Marius**
* Yeah, I also like 7623. 

**Tim Beiku**
* This is the call data. 

**Marius**
* Yeah, it. It's not like it's super easy implementation, but also it makes kind of intuitive sense for me to cap the amount of call data, that can be put in a block and the block size. Right now the maximum block size is 7.4MB. Right? uncompressed. because we snappy compress it, all the time, it's way less something like 2 or 3MB. but if we are, when we're moving to, what's the pair dos and putting more blobs on the chain? It's just a nice insurance to, have a tighter cap on the maximum size of blob that we need to send. 

**Tim Beiku**
* Okay. Anyone else in favor of CFI 7663. Are strongly opposed. Oh. All right. 

**Marek**
* I think if we ever want to raise this limit, this cap might be required, for example, because clients have, ten megabytes limit. Or we have to change this limit. and the cap will makes, make things better here. so, yeah, I think it is good EIP. 

**Tim Beiku**
* Okay. Any other thoughts on 7663? Yeah, I guess it would probably make sense to CFI this one as well. I know we've been talking about it for like several calls and people were generally supportive, but again, it's like a question of bandwidth and yeah. Richard has a question about this around data. whether data around how this would increase average gas costs. Tony had a ton of data on this. I don't know if he's on the I think he's on the call, but what's like, yeah, what's the best place for people to sort of see all your analyses? 

**Toni**
* Yeah. So I put a lot of, posts on if research. I think there are three so far. And in the one that is directly about the EIP, there is also, this GitHub page linked where you can input, addresses or functions and check if they would be affected by the increase or not. 

**Tim Beiku**
* Nice. yeah. If you can post this in the chat here for easy reference, that'd be great. 

**Toni**
* Yeah, I will directly look it up and post it. 

**Tim Beiku**
* And then Ansgar a question in the chat around. Like if we have broad support for it, why not include it immediately, I think. Given, like all the stuff we still have to implement. I'm cautious of like adding more things in like an ad hoc way where if over the next like three calls, we just add a little thing or a little thing every call we end up in a spot where like, okay, we can't actually commit to like a bigger thing to add to Pectra because we just added a bunch of small things.
* So I feel like it's better to sort of just identify the things we'd want to add after Devnet zero actually gets Devnet zero done.
*  See, you know how things are for something like EOFs see how things are for 3074. and then decide like, okay, do we want to add like two small EIP, one big EIP and have that conversation when we actually have more context? Does that make sense? Okay. aside, from these two, 7127, 6623. Anything else client teams feel strongly about? 

**Vitalik**
* Were we going to talk about the SSZ O? 

**Tim Beiku**
* I don't know if Ethan is on the call. he posted an update that it magicians. I'm not sure if he could make the call to talk about them. I don't see him, but there's 100 people here, so maybe I missed him. 

**Marius**
* This is. See on the execution layer, right? 

**Tim Beiku**
* Yes. So let me. I'll post the like, his comment in the chat here. Yeah. Vitalik, did you have thoughts on them? 

**Vitalik**
* Let me read through the comments and come back in a minute or two. Cool. 

**Tim Beiku**
* And yeah, worst case, we can always discuss this on the next call. Any other, Any other EIPs people feel strongly about. 

**Marius**
* I feel strongly about not including Zach on the execution. In fact, I think for that, we would need to, write or audit new libraries. for the SEC formats, we would think about, the hashing overhead and stuff, and, that would, that would really make it, make it hard to ship paper, I think. the SEC ification of the execution layer should happen in a, in a future fork. 

**Toni**
* Yeah. Just to add to this. So I've been evaluating SSD. Libraries after we discussed that in Taipei. And I'm talking about the Golang SSD libraries. And there's one I still need to look at. But none of them is really workable with at the moment. Which is why, if I'm correct, we decided to drop the topic for the previous fork. 

**Tim Beiku**
* Got it. Anything else is SSZ. 

**Vitalik**
* Yeah, I just looked at that quickly. And is there an EIP yet for CFI and receipts? It's like, I know there's a bunch of a bunch of work for transactions, right? But, uh. 

**Lightclient**
* I'm pretty sure there is. 

**Vitalik**
* Yeah, I think it's. 

**Lightclient**
* Very close to the transaction EIP. 

**Vitalik**
* Yeah. Right. Yeah. Because receipts I think are also super high value. And, one of the reasons why is basically because receipts are the one place where you, where currently we can have these, like indivisible, potentially like many megabyte hashes take place. And, that actually causes a whole bunch of, like, pain and extra security auditing, overhead for, you know, for roll ups, which, admittedly, can be solved by, but, by a layer two.
*  But, like, there is basically a lot of, receipt hashing applications that are needlessly for X to inefficient at the moment.
* That could be improved a lot. So I think there's, Like there's significant value beyond the inherent goodness of cleanups to think about it. 

**Tim Beiku**
* One other thing I think is worth getting an update on is EOF. So I asked, I know there's a meta EIP that's in progress. I think we still need to get it merged. But, yeah, I know there's been a lot of work on that in the past couple of weeks. there's been some work done until, like, looking at the interactions with Verkal. I don't know if someone from the EOF camp wants to give a quick update there so people can get up to speed. 

**Danno**
* Yeah, I'll take it. so, yeah, we've got, we're starting to write, execution spec tests. We have specific, facilities added in there to test the EOF. Besu EVM one and Geth have reported they've finished their implementations. Geth is making really good progress. and we're the difficult parts of the parts we expect the validation, has a lot of corner cases that covers the test. The tests cover very well. and the operations themselves really aren't terribly difficult. Once you get well compared to the validation.
* But it's achievable within, you know, a single handful of, you know, months at for a single engineer so that's report from it.
* I know that. guillerm from Verkal has been speaking with, Daniel from solidity. When it comes to cutting features from EOF. My big question is, we can't cut so much that Solidity and Viper won't support it in their compilers. That, for me, is the point where it becomes viable and non-viable. So, games working with Daniel to see what that that point really is. because they're the ones most interested in reducing the scope and reducing the risk in EOF.
* I'm comfortable with where it's at now, but I accept that other people aren't comfortable with it.
* And, I think that's the right approach to figure out what the customers really want out of it and what the real minimum standards are. So  that's, a brief update of EOF. 

**Tim Beiku**
* Thank you. Anyone else? Want to share thoughts or updates. Okay. Oh, actually. Sorry. Yeah. Yeah. 

**Guillaume**
* I just want to give some more details. yeah. So it's true. I've been, talking about the topic with, with Daniel to try to reduce the scope a little bit. it turns out that, yeah, it's going to be hard to cut the scope, or at least the pushback that has been given  by Ansgar especially, is that, yes, we could reduce the scope. but then that means the second version of EOF would have to be fairly small or fairly. yeah. Hard to justify by itself. And therefore, the fear at least.
* I mean, Ansgar can give the argument himself, I guess.
* But, that would mean that. Yeah, if we have a reduced copy EOF! That means that's the only thing we deliver for, for the last, for the next five years. And, that pretty much kills the whole point.
* So, yeah, we're still trying to find a sweet spot, but it's not going to be very easy to to not ship all of it in one go. 

**Tim Beiku**
* Got it. Yeah. 

**Charles C**
* Anyway, to. 

**Tim Beiku**
* Please go ahead. 

**Charles C**
* Sorry to jump in, but is there any way to ship, like, Because the problem is, like, we're trying to, like, upgrade the train while it's running, right? Is there any way to, like, ship experimental versions of EOF that can be iterated on that run in like a sidecar? 

**Tim Beiku**
* We discussed something like this, like on L2's a few years ago. And this was before, like, the rip process was a thing. I think the concerns from then were, one there's probably some of the like EOF work that we want L1 client teams and testing teams and security teams to actually, you know, thoroughly review. and so like, yeah, there's like a significant part that it makes sense for L1 to own.
* Two is basically L2 shipping and deprecate your version of EOF leaves them with like the DEP forever. And you know, that's not something they were super keen on. and then three is like, if we have, you know, something like dev nets or whatnot, then it's it's kind of hard to get enough support from like tooling and languages and whatnot. So like, sure, you know, we could launch like an EOF v1.5 devnet, but like World Solidity and Viper and all that support it. That seems unlikely. 

**Charles C**
* What if it's like neither? What if it's like an L2? That you know the well, some set of responsible parties set up that is kind of like a devnet in that it's supposed to be torn down at some time, but it's also not maintained. 

**Tim Beiku**
* So the risk is like if. Yeah, either there's either the chain has no value or it has value. If it has no value, the incentive for tooling to support it feels very low. Maybe that's changed. Like maybe there's more tooling providers today, but if there's value, it's like, yeah, people's eath can get stuck. Yeah. 

**Charles C**
* Why couldn't it have value. 

**Tim Beiku**
* Right. So yeah. So if you have value on it and then you have a deprecated version of EOF and or like a conflicting version of EOF and stuff like that. like you end up in this case where you have actual funds that are stuck potentially in something. and I don't think anyone just wanted to take on that, like, complexity. 

**Charles C**
* I mean, if the I think the the issue that I've seen repeatedly in discussions about EOF is that, well it's like not perfect, which I actually agree. And if the goal, if the bar is that we need some system that is perfect or at least like very long term, like the nature of these things is that sometimes you don't actually know until they're in production. so. And. I don't know if the bar the this must be perfect before you ship it bar is very realistic. 

**Tim Beiku**
* Got it. yeah. Let's do. 

**Guillaume**
* Yeah. So just, to to give some, like, share more information from my talk with Daniel and try to answer some of those concerns. basically the compilers, what they want to, you know, there's an EOF version that's not the, like, sorry, compilers support EOF, but they support the former version. And, in order to keep maintaining this, to be able to produce test nets and, try to do some testing.
* And by the way, this is a problem we have for Verkal two, because we would like to understand how Verkal and EOF interact. But there's no way to to test this at this time. I think like what the compilers want is to have EOF schedule. So, yeah, I think we should schedule it for sure.
* I don't think it will come to anybody as a surprise that I think we should schedule for Amsterdam, but, in any case, compilers, if you want EOF to make progress on the tooling so that you can actually test it, you need to schedule it.
* That has been made very clear by, by compiler people. 

**Charles C**
* Yeah, I'm pretty aware of what compilers want. So I think that, yeah, if we can have some kind of middle ground, it might be very helpful for everybody who's working on it. 

**Tim Beiku**
* Yeah I know. Yeah. Ansgar and Vitalik have like a thread in the chat about potentially a simplified version. Yeah. Either of you want to give some context on that? 

**Ansgar**
* Yeah, I think the idea was just to say that there's two different types of small EOF we could ship. There's a small EOF that would basically be incompatible with the big EOF, and so it would require us to then ship a separate version of us later on if we wanted to. All the features of EOF, and that has the downside that then forever and ever. Now layer one has to support basically raw contracts, USB one and USB two.
* And because all of them exist. Whereas if we can basically slim down the scope of us by just removing features that can be later on added to the existing version without breaking things and that like for example, right, you could initially just not ship a specific opcode. And then we later on add the opcode that usually does not require a new version bump.
* And that makes much more sense because then we can ship small EOF now and still by later on adding the remaining features, we would not need a new version.
* So that that variant of small if I had actually I think is promising. 

**Marius**
* But is it so easy to add a new opcode to us? Because you need to kind of You need to make sure that. 

**Vitalik**
* You just add a new opcode the same way we add new opcodes today, right? 

**Tim Beiku**
* An EOF also has validation. 

**Danno**
* Yeah, because we have validation. We have greater security that space is there and unused. We won't run into nasty side effects, like when we're trying to add relative jumps, into the legacy code that, by the way, you could put jump test in a in a push to zero in every in a push 32 and things suddenly change. 

**Charles C**
* You do need a, like, version bump. Because otherwise it won't pass. Validation. 

**Danno**
* It'll pass multiple levels of validation. You don't have to encode the version in the byte stream, but you would have different versions of validation. 

**Tim Beiku**
* Oh, yeah. 

**Marius**
* At least for us, complexity wise. What would Basically mean. Because it would have to write a new validation. That basically copied most of the validation, algorithm at that. At that. 

**Tim Beiku**
* Right. But there's a difference. 

**Marius**
* I know it can be. 

**Tim Beiku**
* Oh, sorry. You sort of broke up. Yeah. 

**Marius**
* It's not a it's not a version bump, but. It's it wouldn't be a version bump that would make the complexity. It would be similar complexity, at least in our implementation. 

**Tim Beiku**
* Got it. Ansgar. 

**Ansgar**
* Yeah. I feel like you were also starting to say this, but I just want to point out that there is still a difference in the complexity, because it might be the same complexity to for like implementing and adding the these extra features later on. But in terms of long term support, right. If you think ten years from now in one world, the client needs to support three different types of bytecode that could it could encounter in the EVM and in the other version, it only needs to support two different types of bytecodes.
*  And because the kind of the validation and deployment rules you only have to do if you replay the old history. And I think there are all these ideas already that science in the future might not be just out of the box support replaying the entire history. And you might need to have like older versions of the clients for that and everything. It basically means in one world you can slim down the rules and forget about these old rules and the other version. You have to support them forever. So I do think it still makes a big difference. 

**Tim Beiku**
* But, I guess. Yeah, this also feels like something we're obviously not going to fully specify on this call. there are bi weekly, if not weekly EOF calls. So I think it probably makes sense to continue the conversation there. And then, again, as we get ready to consider stuff, the ad, the picture beyond what's already there. yeah. Hopefully we can make some progress on all those issues for EOF. but yeah. Any final comments? Questions? Concerns about EOF? 

**Charles C**
* Going back to this, sidecar thing that I'm that I'm hung up on. I don't know,  I think that L2 might be interested in doing it if, there were there was a guarantee that under certain conditions, it would be merged into mainnet, because I think the issue is like nobody wants to be left holding the bag, right. Main net doesn't want to implement it and then have to like change it later. L2 doesn't want to implement it and then like just have it be, turned into a, you know. Abandoned or whatever.
*  So if there were some way and maybe this is going to be important, like in the future because of what what is it called like L1 ossification.
* So I think if there's some way to like kind of increasingly escalate the stakes involved with it, instead of it being like all of a sudden all or nothing, maybe that's another way to do it. 

**Tim Beiku**
* Yeah we can. That is the last thing we had on the agenda. So let's do the comments by Epsilon. And then we can move over to that general, topic around like L1 and L2, governance and feature deployment. but yeah. Ipsilon. 

**Ipsilon**
* Yeah. Maybe this wasn't made clear. And in today's update,. But on yesterday's EOF call, we did, mostly agreed to simplify the creation question. And so there were in the chat, there were some discussions, about EOF create and TX create and EOF create is for creating new contracts within an existing contract. So like factory contracts and TX creates the, the external transaction creation process. The TX create is the the more complicated one. And we agreed to go with like a legacy approach which we don't think is the the final ideal case. but the design we have is actually forward compatible.
* It doesn't require a new transaction type. It doesn't require a lot of complexity. It is rather simple, but it's forward compatible with the introducing TX create and a specific transaction type in the future. and I think this was the most contentious, item in terms of complexity. And it seems we have removed this. so I think we would be curious to learn maybe on on the next EOF call, which is every Wednesday. we would be curious to learn what other, blocking complexity exists. 

**Tim Beiku**
* So, yeah. can someone post the agenda to the next, EOF call in the chat here or on the discord so people can know, where to go for those. I'm. 
* Okay, last topic on the agenda. So, this. Yeah, we've covered this a bunch of times, sort of, indirectly today. but, L1 versus L2 processes, I guess, you know, the the question is around, how should we think about Ethereum l1's roadmap, given that, you know, we want rollups to play a larger and larger role? you know, can rollups actually ship stuff before? What's like the process we can use for something like that? and it might make sense for, Carl and or Ansgar to start by sharing their thoughts on that, given they've been running the roll calls for the past couple months. and, yeah, we can we can take it from there. 

**Ansgar**
* Yeah, I can. I don't know how to. I mean, I can briefly say something. So, basically we've had the kind of the roll call as like a kind of an experimental, forum a while now, for half a year with over half a year already and, and the kind of accompanying EIP process. 
* And so the way to think about it really is to I think there are basically three different dimensions here. There's the research side, there's the governance side, and then the client implementation side. 
* And so so on the research side, I think we basically we still have an open question of long term. Do we want to stick with EVM equivalence or not. There have been like a lot of kind of arguments on both sides of this front, but a lot of it hinges on this question.
* So basically there are all these ideas like in the future we could have an  ZK, EVM on mainnet, and then you could have basically enshrined rollups that that natively are verified and everything. 
* All of this only works if you have fully equivalent layer twos that follow the exact same rules as layer one. In that scenario, we don't really have to talk about this topic much. Then we maybe should just talk about how can we have layer truths be more present on all core dev so that we can maybe govern the EVM together more and more and more kind of, effectively. But if of course, we we decide that it's fine that if layer twos over time depart from from mainnet, EVM and more and more, then the questions that becomes, how can we basically enable them to to do that more?
* And they are specifically that's it's again, it's like governance and the client side. 
* And so basically on the governance side, I think it's more the question about, layer twos in the past have been very reluctant to ship features where they basically have the worry that main net might either never ship them, which is still kind of fine, or ship them in a slightly different and incompatible way. I think this is usually where they what they're the most afraid of, right? 
* Because then that kind of bifurcates the ecosystem a lot. And I feel like for that we really, over time, need to just make a decision on on layer one, to what extent we are willing to take this into into account in our decision making. 
* Of course, layer two is often make decisions before layer one makes them. So to what extent are we willing to basically be bound by layer two decisions? 
* And the nice thing is that with the R1 Precompile, we have a first candidate where we can just very practically debate all of this. So if, say, next call, we want to talk about whether to include the R1 Precompile or not. We have a lot of these practical questions to answer. Letters have already shipped it.
* We have given them a separate. If you remember this from a couple months ago, we've given them a separate precompile range. So now they are tooth have shipped our one Precompile added layer two specific address, but we want to take over that address. Do you want to not take over that address? 
* Would we even want to maybe say modify the opcode, the precompile behavior, or are we willing to say no, it's finalized in layer two. We're also going to take it as is and basically ship the same version. 
* So I think basically just exercise going through this exercise of figuring out to what extent we are willing to basically be somewhat bound by layer two governance. 
* On the layer one side, I think it would be very helpful for guiding guiding layer twos. And then the third one is that that's also a really interesting one so far, even though there has been some interest where they choose to basically start diverging more, the main worry they have is that a lot of their tools, of course, also run on layer one clients out of the box, but as their as clients for their for their own chains as well.
* And the client developers here is also CL client developers mostly have focused EL on the L1 feature set. And so the question is how can we start enabling, chains that don't quite follow, layer one, the layer one feature set, and just basically have to still still use these same clients more so. 
* So I think in the past there's been quite a bit of debate, like some clients are more open to also like say supporting layer two specific features out of the box. So for example, implementing and supporting EIPs, I know, for example, from Geth that there's a bit more skepticism and hesitation about supporting features that are not actually intended for main net. And if that's not the right path.
* We could also like talk about more standards for extensibility of clients. But basically we need to find a path forward where actually practically in software and client software these features can be supported. 
* Otherwise it's just a non-starter. So basically I think so far our lessons from six months of roll call. These are the three topics. Research. Do you want to diverge from EVM equivalence governance. How does layer one interact with the decisions where to make on EVM changes? 
* And then the client side, if they choose, want to actually ship features beyond layer one? How does that actually then end up in code? And I don't know Carl, do you have anything. Is that does it match your your impression? 

**Carl**
* Yeah, I think that's a pretty good summary of where we are. 

**Tim Beiku**
* Thanks. Yeah. That was that was great. Peter. 

**Peter**
* So one thing I wanted to react to was, basically, how we should, approach one layer to ship certain features and one whether we should pick those features up or not. I think there's there's a I wouldn't necessarily call it a dangerous precedent, but there's an interesting, thing there that, if we commit to layer two is introducing something and then we'll just pick whatever they introduced, I think we kind of run the risk of layer two is just yoloing into certain things which they want, and then they can just point to it. 
* Basically, the one of the dangers is that we kind of, that feature that they ship might be appropriate for them, but might be not completely appropriate in general for everybody.
* And then the question is, well, since some big important layer to ship it, are we going to basically have everybody use something that's not really appropriate for them just because I don't know, optimism rolled with it first the other problem that I see is what happened, for example, with Pre-compiled. Well, what happens if you have two layer twos which use the same address for different pre compiles? 
* I mean, how do you solve that. Because then you cannot actually follow the what layer twos are doing. And and thirdly I think it it kind of I'm not entirely sure we want to end up in a place where basic layer twos get to dictate that while we shipped it, it works, so you have to roll with it. So I think it's a because of these things, I think it's I would be kind of cautious against, going down the path of saying that. Well layer two X shipped it, so we should ship it. 

**Tim Beiku**
* Yeah, and I don't think anyone proposed that specifically, but I agree this is this would be like a huge, huge risk. 

**Carl**
* It's a huge risk, but I also don't think it's anything anyone's trying to do. The I don't think the layer two is are trying to ship some weird feature that no one's going to want or whatever, and there's no proposal that whatever ships and layer two has to be shipped on layer one. 
* I don't think that's that's a realistic concern yet. and I think we'd have to address if we ever got there. I don't think this is a way of layer two is like co-opting and like, trying to take over layer one governance. 
* I think this is just layer two is trying to have some of their own sensible standards for, for for this happening. 
* And then to your second point about shipping Pre-compiled at the same address, that's like one of the things we want to help prevent with RFPs and roll call is like. Like how? How do we prevent these? These these kinds of things from happening? Because that would that would suck for everyone involved. And so it's like part of what RFPs are trying to achieve. 

**Peter**
* So, I definitely agree that I don't think there's a danger of, layer two is necessarily wanting to co-opt layer one governance or do anything super mean or, and obviously, if they were to deploy something, wonky, then obviously there would be no, not even a guarantee they layer one wouldn't follow them. 
* I think the dangers are the I think the things that I see as potential problems are more in the nuances, in the details. One as a layer, two the the idea, the reason why people like layer two is because they are too scared to experiment. They can really go very fast and they can. I wouldn't say break things, but the guarantees are a bit different.
* But this kind of also means that layer two will probably. But once they have a solution for their problem, they're going to roll with it. They will not wait for 100 people to agree, whether that solution is the perfect or not for everybody. 
* They will just go with the perfect solution for their specific problem. And I think that's the that's the nastier corner case where, for example, you have optimism who ships a solution for some quirky problem which isn't perfectly optimal for everybody else. 
* But then, okay, what do you do? Do you? So that's that's the issue. And I think layer two will be actually incentivized to just roll whatever they want with the nuances they want and then just say that, well, we can't really change it. So you just have to roll with it. 


**Marius**
* I think my biggest concern is. What what happens if if roll ups just die and walk away and we have we have to keep maintaining the feature because they once needed it, but now they see the completely vanished or they have changed  their stack to use some different proving mechanism or whatever. And. There's a lot of precedent for this where like people.
*  Came and proposed features and pre-compiled for exactly their use case, and then their use case didn't really work out, or they completely died, or they moved on to to the next thing and we are stuck maintaining and the BN curves stuff.
* So, like to be and so, yeah, I wouldn't like to be in a situation in this situation again. 

**Tim Beiku**
* Thanks.  we're already a bit past time, so let's do Pooja and Ansgar and then wrap up. 

**Pooja**
* So thank you. Tim. I know this is not the best place to discuss the process part, but I'm thankful to Ansgar that he brought up the, significant element, which is, governance here. I'm really interested to understand a little bit more about it. Maybe in short of time. We may not be able to do it here right now, but it would be very, interesting to learn about. How do we want to see it? I want to congratulate proposal 7212 to to be to be, considered for inclusion being CFI.
* But it is our RIP and we are like when we talk about upgrade, we talk about EIP. So there are some, some details which we may want to iron out.
* I'll be happy to hear the venue where we can perhaps discuss it with the roll up teams. Generally for EIP, we discuss it in EIPIP meeting. but is it something that we should be joining our RIP calls? Yeah. 

**Tim Beiku**
* Yeah, I don't know that we have a great answer right now beyond, like a ACDE and RIP calls. Yeah. But yeah, I guess we can discuss this async more. Ansgar. 

**Ansgar**
* Yeah. I just want to briefly respond to what Peter said. And I just want to say because because I think the impression has always been that Verzuz can just experiment and go more wild. I think in practice, what we've seen is that most of them decided to not do this, or even or at least maybe started doing this, and then over time have mostly stopped.
* So now they're really following mostly layer one specs. And, and I think at least given that, you know, like the rollup centric roadmap was something where we kind of all decided this is the best way for the Ethereum ecosystem to go. I think we at least owe Layer two's clear communication about clear guidance and communication about like the best path forward here. Like, I don't think we necessarily have to be willing to say constrain our own decision set or anything. 
* It's more about clearly saying, hey, if you want to, over time, deviate from their one features. These are the ways in which you can do it. These are the ways that you won't be able to do it. And for example, maybe it means you'll have to completely fork away and you have to run to write your own client, maintain your own client. You have to maintain your own, basically. now, now virtual machine and everything. 
* I just feel like in the past this has not been very relevant because layer twos have been mostly focused on just getting the basic rollup stuff ready, like the fault proofs, and basically like just learning how to walk. But now that Layer twos are mature, they are starting to be more ambitious beyond the constraints of layer one in terms of throughput, in terms of additional features. 
* So these these topics, these questions become more urgent. And I do think basically we owe them, some guidance. So I don't have any specific proposals or anything. I just think we it's important that we have these conversations and that we figure out a path forward.
* And just saying they can just keep experimenting is not the right approach, because right now they're basically not able to experiment because they don't see a way to do it. So I think at least giving like making it clear from our side what, what the scope would be or what, the design space would be for them to operate in, I think is very important. 

**Tim Beiku**
* Thank you. Okay, I think we can wrap up here. yeah, there's a lot of threads to follow up on async. but yeah, already a bit over time. Any final comments or things people thinks we should address? 
* Thanks, everyone. yeah, I'll post the recap about all this on the R&D discord. And, there's already a poll up for the time for the account abstraction 374 Breakout Room. yeah. Talk to you all soon.



-------------------------------------
### Attendees
* Tim
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

## Next Meeting
May 9, 2024, 14:00-15:30 UTC






