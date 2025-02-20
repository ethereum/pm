# Execution Layer Meeting #203
### Meeting Date/Time: Jan 16, 2025, 14:00-15:30 UTC
### Meeting Duration: 1hour 30 minutes
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1227)
### [Video of the meeting](https://youtu.be/uh1hZCE4k0w)
### Moderator: Tim
### Notes: Alen (Santhosh)

| Decision Item | Description                                                              | 
| ------------- | ------------------------------------------------------------------------ | 
| 203.1 | **Pectra Devnet 5 Launch** Developers launched Pectra Devnet 5 a half hour before the start of the call. EF Developer Operations Engineer Parithosh Jayanthi said he is seeing issues with gas estimation on the devnet and will collect logs on the issue to share on the Ethereum Research & Development Discord channel.
| 203.2 | **Pectra Specifications Updates** EIP 7623, increase calldata cost, to clarify gas refund handling. The update has already been merged on GitHub and included in Pectra Devnet 5 tests.The second update is related to the base fee fraction in EIP 7840, add blob schedule to execution client configuration files. There was no opposition to the update voiced on the call and developers agreed to merge the changes on GitHub before next Monday’s Pectra testing call on January 20.
| 203.3 | **Pectra Specifications Updates** The third update also related to blob base fees was regarding how to calculate excess gas during Pectra activation. As explained by EF Research Lead Alex Stokes, the calculation relies on information from the previous block header so if changes to blob capacity are activated at the fork boundary, meaning on the Pectra activation block, then the excess gas calculation will rely on information from the prior block constructed using old fork rules. Stokes said developers should clarify whether the blob capacity increase is activated at the fork boundary or one block after the fork boundary. “I don't think it really matters which thing we do, but we should all do the same thing,” said Stokes. Developers agreed to clarify EIP 7691, increase the number of blobs to reach a new target and max of 6 and 9 blobs per block respectively, so that the new excess gas calculations occur one block after the fork boundary and therefore use new fork rules only. This is the logic that is already being tested for in clients, said EF Testing Developer Mario Vega. Geth developer “Lightclient” said that he would update EIP 7691 by next Monday’s testing call with the clarification.
| 203.4 | **Pectra Specifications Updates** The fourth update is related to multiplication cost calculations in EIP 2537, precompile for BLS12-381 curve operations. Developers agreed to include clarifications that specify division in the EIP as integer division. Client teams passing Pectra Devnet 5 tests should already have this logic in their code, so the change is only required on the specifications side. EF EVM Developer Paweł Bylica said that he would make changes to the EIP on GitHub by Monday’s testing call.
| 203.5 | **Pectra Specifications Updates** Lastly, the fifth update is related to EIP 7702, add a new transaction type that permanently sets the code for an Externally Owned Account (EOA). COO of Otim Labs Julian Rachman proposed a behavior change to the EIP that would enable code introspection. As detailed in a document written by the Otim Labs team, code introspection “refers to a legacy contract’s ability to inspect its own bytecode or the bytecode of an external contract and change behavior based on that information.”
| 203.6 | **Pectra Specifications Updates** Code introspection is a behavior that developers working on EVM Object Format (EOF) are working to disable in a future Ethereum upgrade. However, as detailed in the document and on the call, enabling introspection for checking an EOA’s “delegate_address” would not hamper progress on EOF. The benefit to allowing introspection for checking delegation in an EIP 7702 type transaction is to support the safe use of relayers and other external accounts when enabling EIP 7702 type functionality such as gas sponsorship. Lightclient was in favor of including this update in Pectra specifications. “It feels like a very easy thing for us to update. We’re already determining if the thing is a 7702 delegating account and adding in the address to the designate we return is extremely simple,” said Lightclient. Beiko recommended giving call participants a few more days to review the changes before making a final decision on its inclusion. He recommended revisiting the topic on Monday’s testing call.
| 203.7 | **Pectra Specifications Updates** Beiko requested that Rachman’s team create a formal pull request on GitHub with all the proposed changes to EIP 7702 for developers to discuss on Monday. Regarding discussions about whether this update would require developers to launch a new Pectra devnet for testing purposes, Jayanthi said the change could be included in a public testnet shadow fork instead. All other specifications updates discussed on the call, Beiko added, also do not require a new Pectra devnet so developers can likely move forward with updating public testnets after further testing on Pectra Devnet 5.
| 203.8 | **Pectra System Contract Audit Updates** EF Protocol Security Researcher Fredrik Svantes said that all third-party audits of the system contracts in Pectra have been completed. There were no major findings and the audit reports will be uploaded on GitHub for client teams to review. Svantes also recommended dedicated time on the next ACDE call for the auditors to present their findings and answer any questions from client teams.
| 203.9 | **Pectra Testnet Scheduling** Beiko proposed a rough schedule for testnet upgrades moving forward. He proposed setting a block number for upgrading the Sepolia and Holesky testnets on the next two ACD calls and preparing client releases for them by February 3, 2025. He recommended aiming for a Sepolia fork sometime during the week of February 12 and a Holesky fork sometime during the week thereafter on February 19. Assuming no major bugs or issues, this would mean that the Pectra upgrade could go live on Ethereum mainnet three to five weeks after the Holesky fork in early to mid-March. There were no objections voiced on the call to Beiko’s proposal. Stokes voiced his support for coupling client releases for the Sepolia and Holesky tesnet upgrades.
| 203.10 | **Holesky Gas Limit** EF General Engineer Sophia Gold proposed setting the default gas limit in clients for the Holesky upgrade release to 36m and continuing to increase the default gas limit going forward on Holesky so that it is always higher than the gas limit on Ethereum. This would ensure that gas limit increases on mainnet can always be tested prior on Holesky. There were no objections to the proposal on the call. Representatives from the Teku, Besu, Prysm, and Nethermind team said their client releases for Holesky are already set to a default gas limit of 36m.
| 203.11 | **RPC Standardization Efforts** Geth developer Felix Lange expressed frustration at the lack of feedback from client teams on efforts to standardize Ethereum JSON-RPC specifications. Among several issues, one that Lange voiced on the call was a lack of clarity about the scope of RPC standardization efforts and what types of ecosystem stakeholders should be included in the discussion. Lange wrote a detailed explanation of his efforts to standardize the RPC and proposed next steps in a blog post. Beiko recommended further discussion about this on Discord and a dedicated breakout meeting on the topic. Besu developer Justin Florentine said that he would spearhead coordination for scheduling the breakout meeting.
| 203.11 | **Specifying Node Hardware & Bandwidth Requirements** EF Applied Researcher Kevaundray Wedderburn requested feedback on his document detailing the minimum node hardware and bandwidth requirements for Ethereum. Beiko asked whether these requirements should be drafted as an informational EIP for easier reference by developers and the broader Ethereum community. Prysm developer “Potuz” said that the node requirements for validating nodes and full nodes are different and so, the document should make this distinction clear. Beiko agreed with Potuz and recommended further discussion on the topic of node hardware and bandwidth requirements and next steps for formalizing Wedderburn’s document on Discord.
| 203.12 | **EIP Editors Workshops** There will be an EIP Editors Workshop organized by the Ethereum Cat Herders group on January 17, 2025 at 16:00 UTC. The meeting will provide an overview of the EIP editing process. All Ethereum community members interested in learning more about the EIP workflow and editing process are encouraged to join the meeting. A recording of the meeting will also be made available on YouTube afterward.

# Intro
**Tim**
* Awesome. Thank you. Welcome everyone to ACDC number 203. a bunch of things on the agenda today. lots of Petra spec stuff. and then discussions around the gas limit on Rpcs standardization. Node requirements and, EIP editing. To start, I believe Devnet5 has just gone live. Perry, do you want to give us a quick update on the devnet? 

**Parithosh**
* Yes. So, yeah, Devnet five, went live like, half an hour ago or something. you can find all the tooling links here. Electra activates at epoch four, and since then, we do see some, issues with gas estimation. I think on Aragon, but we'll Yeah, collect some logs and post it in there. I'll, share the link of what images I'm using, but essentially it's mostly just an updated version of what's been on the interop channel.
* And thank you to all the client teams for sprinting and merging stuff in so we can get this. 

**Tim**
* Thanks. And yeah, did Electra activate right before the call? Is that what you said? 

**Parithosh**
* Yeah. Like three minutes before the call. 

**Tim**
* Nice. great. Any team want to share anything else on the devnet? Okay. If not, then, we can discuss all of the potential spec changes finalizations for Pectra and see what, where we go from there. I'll go in order from the agenda. 

# Update EIP-7623: Clarify the gas refunds handling EIPs#9227 [5:47](https://youtu.be/uh1hZCE4k0w?t=347)
**Tim**
* But the first one there was a PR, from Paul on EIP 7623 about, the gas Refunds. I see it's been merged already, but was there anything that people wanted to discuss about this? I don't know if Powell was on the call. Yes. 

**Pawel**
* Yeah. I think this this issue has been solved to the point that tests were fixed and all of that. So the issue was, if I remember correctly, like the final tuning to the transaction, gas cost, when you need to apply this, this minimum gas cost that was computed before. I mean, it wasn't clear by the spec, that it's supposed to be done. This step should be done after refunds are applied or before the refunds are applied. And I think we agreed that it makes much more sense to apply this cap after the refund, but actually the tests and the reference implementation that the other way.
* So that has been corrected in EOF. And then in the execution spec tests and I think everyone is on the same page. So yeah consider that solved. 

**Tim**
* Thank you. Anything else on this issue. And I assume this PR was not included in Devnet 5. Is that correct? 

**Parithosh**
* Yeah. It hasn't been included yet. 

**Tim**
* Okay. 

**Parithosh**
* Got it. 

**Mario**
* Wait. It is. It's on the 1.2 release of this. So if they're passing the test, then it should be. 

**Tim**
* Yeah. 

**Parithosh**
* Okay, then. It has been. Yeah. 

# Update EIP-7840: Add BaseFeeUpdateFraction EIPs#9240 [7:42](https://youtu.be/uh1hZCE4k0w?t=462)
**Tim**
* Okay, great. Thanks for clarifying me. okay. Then the next one was about EIP 7840. Marek had a PR updating the base fee. See update fraction. Marek? Are you on the call? 

**Marek**
* Yes. Okay, so I can give quick context. So we introduce block parameters in the L configuration to specify the block target and the max block value per fork. However, in the meantime we introduce another EIP for block increase EIP 7691 which modified the block fraction constant in the fork. So this created an inconsistent situation where some block parameters were hardcoded while others were in the configuration. So it was a little bit messy. And this PR resolves that by moving the block fraction into the CL configuration alongside the other parameters. So target and max.
* And actually I think we have support for this PR from all EL client teams and testing team as well. Yeah. 

**Tim**
* Thank you. yeah. They seem like they support, on the PR directly. Anyone thinks we should not do this? Okay, if not, then I think we should go ahead and merge the PR. and once we're through the specs, discussions, we can decide whether, we think we need another devnet to test this or, and other changes, or if, we may want to move straight to test nets. but we should move forward with, the PR 7840 and I guess, somewhat relatedly. Sorry. We should clarify the PR a bit more before merging. and that there was a comment on it. yeah. Do you want to maybe expand on your comment, Jochem? 

**Jochem**
* Yes. Sorry. like, there was a comment also by Marek about the defaults, and I think we should, clarify that, but that was just a comment, which I got on discord. So we will check after ACDE. 

**Tim**
* Okay. So that's where we aim to have this merge before Monday's testing call, if that makes sense. 

**Jochem**
* Yeah, that will work. Yeah. 

# Blob base fee at fork boundary [10:36](https://youtu.be/uh1hZCE4k0w?t=636)
**Tim**
* Anything else on this PR? Okay. If not, next up, Alex brought up the, blob base fee at fork boundaries, I believe. there was a testing issue. yeah, that that that got triggered here. I don't know if. Alex, you want to want to give it a bit more context and suggest how we should update EIP 7691 to make this clearer. 

**Alex**
* Sure. Can you hear me? Okay. Yeah. So,  Yeah, this came from an issue during testing. And my understanding is that, essentially it's a question of like, when do we make the changes as we go to change the ball count? the reason this is sort of tricky is because the way the base V function update, like the, the function we use to update the base fee, the way it works is it uses the parent, parent header, I believe. And so then the question is like at the fork boundary, do you use the header which is like a bit weird because it's like new logic at the fork, but you're going back to the previous fork.
* Or do you just want to go ahead at the fork boundary with the new fork rules? and I think that was the issue. there was a clarification. The reason I brought this up is because there was a clarification to 7742 around the same behavior. And I think this is the analogous behavior for 7691, whichever the blob EIP is. yeah. So I just wanted to bring it up and check with clients what they would prefer. I don't think it really matters which thing we do, but we should all do the same thing. 

**Tim**
* Andrew. 

**Andrew**
* Oh, sorry. Yeah, someone can correct me if I'm wrong, but I think in Aragon, what we implemented is that when we used. When we calculate the excess gas, actually, for that, you feed the parent, block and you use the parameters, of the fork of the parent block. But then when for for other methods you you use the current block. So it's a bit tricky. Yeah. Because you might need for the same calculation you might have to use two blocks. But I believe it's actually it's consistent with EIP 4844. 

**Alex**
* Right. So at the fork block we'll use the parent header. Still, to calculate excess gas. 

**Andrew**
* Yeah. 

**Alex**
* But there is some consideration from one of their client team because I think it's just easier to write this way. and it really shouldn't matter either way. So do we just want to clarification? and again, it's probably 7691, I believe is the number. I'm happy to go clarify in the, in the EIP. 

**Andrew**
* I think it would be great to clarify it. Yeah. 

**Tim**
* Roman. 

**Roman**
* Yeah. Clarification is great. again. What is what is the outcome? It's unclear. So for the first block do we use for the Prague four block? Do we use concrete parameters or Prague parameters? So how I see it for when you actually calculate the excess gas, you use, Cancun parameters. for, for, for in that calculate excess gas. But for the rest of the things, you use factor parameters. so that that does not make much sense to me because, in, in most AP language, I read it said, like, once the fork is activated. Use the the New Prague parameters and.
* Well, the way I understand it is the fork block is the fork activation. So we should use Prague parameters. But. Right, right. But for, for access block I guess the parent is used. Right. So. And the parents still belongs to the previous fork. I mean for, for I don't know the another example would be uh validating the gas limit increase or decrease for that. The parent block is used as well, you know. But these are like these are pure functions. I don't know, I don't want to bike shed too much because like I think this is insignificant. I just want us to agree on something. 

**Tim**
* And I don't know. Mario, do you want to give context from the testing perspective? 

**Mario**
* Yeah, basically, just to echo Ramon, I think I think it, it it feels to me that if we use Kankan parameters on the first block of Prague, it doesn't quite make sense. It feels like a one off logic deviation to me. And also for for testing. We should like we never pass like, whether when we're filling a block in the test, we never pass. Whether this block is the fork is at the fork boundary, we always just pass Prague and that's it. So for this to work, we would have to pass. Okay. This block is a boundary because else would have to know, that it needs to use the parameters, which doesn't make sense. So yeah, basically just I agree with Roman.
* It just just favor the, the using the, the Prague parameters at the, at the first Prague block. 

**Tim**
* And this is what the testing behavior does today Day already? 

**Mario**
* Exactly. Yes. 

**Tim**
* I would then default to just clarifying the words in the IP to match the behavior that we have in testing. If that's okay for everyone. 

**Alex**
* It works for me. 

**Tim**
* Great. So if we can, yeah, try to get this done as well before, the the Monday testing call. that would be ideal. 

**Alex**
* Yeah. I should be able to make a PR to the EIP today. 

**Tim**
* Anything else on this? 

**Alex**
* Well, I was saying it will make the logic more complicated. 

**Tim**
* Oh, and Robert is saying that death already does this. yeah. I assume some clients may have to change, regardless of what we do. It should not be a major change. Assuming that's correct, I think we should, uh. Yeah. Should just move forward with this. 

**Alex**
* Yeah. In the interest of speed light client. Okay. He says he's okay with either way. 

**Tim**
* Okay, great. So let's copy the behavior from the tests to the IP. Get this merged in the next couple days, and then, yeah. If get or others need to update their code, they can do that. and if you want to post maybe. Oh yeah, you did post already the PR, the execution spec tests. Nice. okay. Anything else on this one? And moving on. okay. The other, spec change, was one for the BLS precompile that there were updates, to, the multiplication cost to G2. I'm not sure if the author of this PR is on the call right now. 

**Pawel**
* I can I can talk about it. 

**Tim**
* Okay. 

**Pawel**
* Yeah. so, like, quick background is that, like, original BLS, AP spec, put some, like, careful attention to the, constants that are there. And there is explicitly a sentence confirming that. So the, the gas constant were picked in a way that they are divisible by 1000. And in the end, some formulas that are later used in the AP. How to How to calculate the the end gas costs for multi scalar multiplication. it's in this formula there's division but it doesn't really matter what kind of division it is. By kind I mean usually we use integer division. But it's mathematically also the same in this case. However, over time we changed the gas cost constants and we didn't notice this detail. And in the end now it matters.
* And also the order of computation in some formulas matters. So at least I can argue that the spec is kind of inconsistent with itself. and the easiest fix to the spec is this what has been proposed by Radek, which just corrects the constant. So it follows the previous assumptions. This is, however, not the easiest fix for the implementation because we need to update the tests and I actually prefer to fix the spec rather than fixing implementations. I mean, yeah, I prefer to fix a spec and update the tests, but I think there were some other opinions about it. And I also commented about this other options in the in the pull request, but that's more or less the story about it. 

**Tim**
* Thanks. 

**Marc**
* Sorry. So as I understand. So if everyone agrees to divide in the same place or use the same formula using integer division, then that's the only change we would have to make. 

**Pawel**
* Yeah. I mean that's, that's it's one of the fixes. I just for me it's like the the the least preferable one. because like this is why we noticed the issue is that we actually implemented it differently. And that's why we actually spotted the bug. It wasn't that by reviewing the API, it was just by implementation difference. secondly, there are some like annoying small things that are coming up from this because, at least on like some analysis level, you will still have fractional gas costs. like for example, if you compute the the cost of precompile for some number of points and then you will compute what is actually the cost per per single point, you will get fractional values. So if you do any analysis outside of pure uh implementation you will need to need to handle this fractional cost somehow. 

**Tim**
* What do. 

**Pawel**
* You. 

**Tim**
* Mean? An analysis. Is this like benchmarking? 

**Pawel**
* Well. Like plotting. Or like doing? Yeah, it's it's something outside of the consensus. Right. So it's it's not like a huge deal. so I agree that's like the, like the lowest effort fix is to agree that the formula, like most of the clients implemented is the way to go. But it's definitely not my preference. But if this is definitely the preference of all others, I think I'd be fine with that. 

**Marek**
* What is your preference to update this gas costs? 

**Pawel**
* Yeah, that's that's the easiest. But we can also update the formula. But in some other way. So the three options we in my opinion we can select from update the gas cost as in the request. Then this is like minimal spec update. The secondly we define the division. We mean is is just integer division. But the order of we can modify the formula that it suits the current implementations more or less. Or we can modify it in a way that it's actually also needs to test updates and implementation update. And we need to fix some like wording in some other parts of the spec. So I can see three options. yeah. But one of them gives you no work on the client and tests and like more work on the spec. 

**Tim**
* And, I don't have like, an intuitive sense for this, but, like, what's the difference to like an average user, if the gas costs for this multiplication goes up 500 gas like, is this something that's called once,ten, 100 times, in like transaction? 

**Pawel**
* I think the diff the difference is, is mostly, I think, aesthetical to my understanding because we already lowered that by more than two times. 

**Tim**
* Okay. 

**Pawel**
* So it was now it's in the range of 23,000. 

**Tim**
* Right. So it's like yeah. 

**Pawel**
* So it's I don't know how many percentage it is, but it's like one digit one. But we lowered that from around four 40,000 to my if I remember correctly. So I think it's it's not a big deal. But if someone really Cares about that to be, uh. Precisely. Yeah. so so I think the changes are there in the, like, rounding and we just pick the, the different rounding factor. 

**Tim**
* And then alternatively, when we say like we would like require like require specifying that everybody uses integer division, like what's the where would we specify this. basically like how how do we enforce this? My fear with that approach is we all agree on this call to do this, and we do this with the fork. But it's like not clear to me where and how we can have test conditions For the the way in which this gets calculated. 

**Pawel**
* No, I think it's it's relatively easy. We we definitely can do that clearly in the specification. And the test already covered it somehow. But we can make sure that this is. Yeah. Because the test court caught our our like difference in implementation. 

**Tim**
* I see. 

**Pawel**
* So tests are there already. And we can actually make sure that there's maybe specific tests that but uh seems yeah. If you run just like different examples of different multi-scale, multi-scale modification cases with different number of points, this is already covered. 

**Tim**
* I see. And would any if we, if we did this if we enforce using integer division would any client team have to change anything aside from obviously even one. But like with any like main net kind team have to change everything. Or are they all passing those tests? 

**Pawel**
* If you already pass net five tests, I think you're fine. If you didn't try it then you can find the same issue. 

**Tim**
* Yeah. In this case, if we can specify it in the spec clearly and we already have test cases for it, I would lean toward just enforcing integer division. it feels a bit uglier than changing the gas pass, but also, yeah. if we already have this and. Yeah. I'm not that keen to delay the fork. over. Just, Yeah. Having another entire iteration cycle just over this. But anyone object to this? Okay, so let's have a couple thumbs up in the chat. let's verify the spec to do this. Paul, is this something you can do in the next couple of days? 

**Pawel**
* I can do it. 

**Tim**
* Oh. 

**Pawel**
* Yeah. Do it, do that. Yes. 

**Tim**
* Thank you. Yeah. Thank you. So, yeah, if Epsilon can, can clarify the spec, ideally by Monday's call as well. it shouldn't require anything on the client's end, but at least we will have clarity. anything else on this topic? Perfect. Thank you very much. last, potential spec change for Pectra today. a bit of a bigger one. so there's, hackmd that was created to make a case to allow for delegation introspection. Julian, do you want to give context on the proposal? 

# Spec change [29:31](https://youtu.be/uh1hZCE4k0w?t=1771)
**Julian**
* Yeah. GM everybody. so yeah, if, uh. Oh, yeah. Great. Thanks for dropping it, Tim. so a little bit of background, I think over the past couple of weeks, we've kind of talked about this idea of like, code introspection and Xcode opcodes. you know, having sparked new discussion in terms of, like the way that we build things on some 702, it kind of sparked this for us as well because, you know, after, you know, building with and then without, you know, prefix plus delegate address, kind of realize it's actually a great, a great feature that, is very useful. Wouldn't change the behavior of you of contracts, but I realized it was a big sticking point. So we decided to take the time to break down. Like, what does that even mean? Just by saying it affects it may or may not be affected by EOF.
* Is it aligned by EOF? and kind of like breaking it all down. in this doc. So I would say, you know, the first maybe 70% is, is a lot of background. And then towards the end is an actual analysis on why we believe actually, you know, allowing Xcode opcodes to act on the full EIP 7702 delegation designator for delegated Eoas instead of just the prefix is like the best way forward. And, you know, we hope that this final upgrade is update is like kind of the very last thing that we would want to add to 7702. you know, leading into Petra, you know, Dave is, you know, one of the main authors and the the protocol engineer behind this deep dive. So he's more than happy to add any additional comments, but I hope this is, a good background. 
* In terms of, like, what we wanted to get across and hope to get done today. 

**Tim**
* Thank you. yeah, it's Dave on as well. Any additional comments? 

**Dave**
* I'm here. I think that that hits it all pretty much. I would just say that, there's some discussion, on discord about like, oh, should this make us reconsider EIP 7702 mutability or EOF, code introspection behavior. And we don't, like, recommend either of either of those things. We'd say that basically just this change for Xcode. Behavior for 7702 it simply like would improve, like safety for relayer schemes. It doesn't, like, completely, you know, warrant the need to change like mutability for 7702. Or definitely, definitely not. code introspection behavior.

**Tim**
* Thanks, Daniel. 

**Danno**
* Features for iOS, when something's added, it can't be removed. So probably where we're going to start with, with the iOS and introspection is the delegates is it's not going to be there because there's no code introspection in iOS. but because it's a thing that can be fixed by adding an opcode or making a new opcode, perhaps a code delegate. it's not like we're stuck there. So just the plan going forward on this for, you know, initially for us, my my prediction is we won't have introspection of the delegate in iOS code because it can be undone easier than adding it in and removing it later when we figure out we don't need it. We're really committed to trying.
* If you listen to the calls, there's a lot of places we're trying to get rid of code introspection, including, how we're calculating hashes for iOS create. So we're really committed to make no code introspection be the default. 

**Dave**
* I think we're completely aligned with that, vision. Like in the doc, it lines up or outlines how, we think that the removal of code introspection is a good thing. and that we, you know, hope that iOS can include some notion of delegation introspection in the future, but that it's not necessarily, it needs to be included in the first version. also that yeah, kind of differentiating between code introspection and delegation introspection. like imagine interactions between EOF contracts that have no external code introspection, but can only just check the delegation designator for eoas then it would act, you know, simply like an implementation identifier, which I think would be beneficial for EOF contracts, while like nowhere in that interaction would there be real code introspection.
* So I think, I mean, it'd be something to consider down the line, like you said. and yeah, I'm not, you know, intimately like, aware of the details. for, you know, if that would make certain assumptions about code inspection, behavior breakdown. but I think we think that simple delegation introspection is like a far less, complex like way to reason about interaction than full on code introspection. 

**Tim**
* I guess one question I would have is, yeah. To what extent? This is a big change. in in clients, theorem JS seems to be like a pretty small change. yeah. Does any other team feel strongly, in terms of either the work that this that this represents or just the general. yeah. Value of the feature. Okay, I guess no strong opinions. my sense is people probably have not had the time to, like, fully review this. I don't know how accurate this is. I just read the doc the first time this morning. yeah. So I don't know, I on one hand, I would like us to make a decision today about what to do, because if we are going to change this, we should do it as soon as possible. to not delay, either like, another devnet or potentially moving to testnet. yeah. On the other hand, I think we should make sure people properly review this.
* Yeah. And I know maybe, like, a question for Dave is like, how problematic would it be to not have this change included? 

**Julian**
* I, I'm not sure if they wanted to answer that. I was going to say, uh oh, go for it, Dave. I see you unmuted. 

**Dave**
* Yeah. So we outlined in the doc basically a a front running attack that can be carried out against Relayers, in like, relayer schemes that the EIP Intends to like service. and so we were just pointing out that like to make interaction with delegated eoas safer for relayers. this change would this would be beneficial for that? While it wouldn't change any behavior for EOF contracts and it also wouldn't change like safety for interactions with delegate delegated eoas such as like self sponsorship, where you where the submitter of the transaction can trust themselves. so this is really just about like safety for relayers with 7702. 

**Tim**
* Got it. Um. And yeah, Justin from BCU says he's unclear and would like to talk to some of the wallet devs. my. Yeah, my sense is if we're not, if people need to review this more before making a decision, perhaps we can finalize this on Monday's testing call. unless people really want to move forward with this today. But I think maybe getting 2 or 3 days to review this, over the weekend and tomorrow would help us make a big decision. 

**Lightclient**
* I mean, I think I'm pro this decision, and my only hesitation has been the interplay between this and EOF. But if people don't feel like this is creating some kind of precedent for how we'll deal with things in EOF, then, you know, I don't really see a specific issue with this. If they need to add a new opcode, the, you know, is delegated opcode, something along these lines. You know, that's not a that's not a big problem for this change. And it will come with EOF. 

**Tim**
* Thanks, Daniel. 

**Danno**
* So the opcode um I'm wait and see on that to see if the market develops and if we need it, it can be added later. So I would think the initial EOF position would be to keep our existing code introspection. And if the market shows that we need this, the path to fix it is to add the opcode. So we have a way out. And I'm I'm kind of wait and see to see if we really need this. But again, this is another thing. If we put it in shorten now, we could never add it into legacy. So it's kind of a sticky wicket to be in. but you know, as far as whichever way you go, EOF has a way out. it might not ship in Tsusaka. It might ship in Amsterdam. You get the full solution, but that'll give us time to see how the market reacts to this and if there's a need for delegation introspection. 

**Lightclient**
* Yeah, okay. Yeah. I mean, I'm supportive of it. I don't really see something that's like, Franjo said this was sort of a toss up between the two behaviors when we were making this decision. And the reason that we went with the two byte specifier is because it was more similar to how things behaved with respect to EOF. And now we're in a kind of a weird situation where only the external code reading operations are getting this, uh f01, prefix where the code copy code sighs are actually getting the executing the executing code, the code that was delegated to. So I find this the difference in behavior between these opcodes? Weird. So this could be an opportunity to just like unify all of that together in a better way. 

**Tim**
* And I guess there was yeah, one comment in the chat by Justin about, wanting to talk to some wallet devs. there's some responses that this has been talked about in the forums. so. Yeah, I don't know. Do people prefer to move forward with this now in order to have sort of a final spec, or do we want to wait a couple of days and make a decision on Monday? And if we do make the decision on Monday, like are there specific people we'd like to bring in on the testing call or reach out to? in the in the upcoming days? 

**Justin**
* Don't we already need a devnet six for the GMO stuff? 

**Tim**
* Potentially, yes. 

**Justin**
* I think that's enough time for me to, you know, talk to the people that I'd like to talk to. 

**Marek**
* For what we need devnet six. 

**Tim**
* So we have two small changes. We agreed to the changes. actually, like the GMO, the GMO, we would not need the net because the, this is the current behavior that clients do. 
* But then, yeah, we have already these two pretty minor changes around, like the base fee update fraction and the blob base at the the fork boundary. I don't know if we want to set up an entire new dev net just to test these two relatively minor fixes. assuming we did, then, yes, we should include the 7702 To change. and then if I don't know if this seven, seven, oh two changes the thing that, you know, goes from it requiring not requiring to require to requiring a note, uh. 

**Marek**
* Just small comment about block based fraction. I don't think it will require, the definite because, we can just update, email clients with the new configuration and that's it. I think we can coordinate it without definite. Okay. 

**Tim**
* Okay. So this 7702 change then would be the one I, I don't know, would we actually want an entire new dev set for this or would we be comfortable. you know, having obviously static tests and then potentially going straight to test nets with this change that has not been deployed on the dev net. 

**Parithosh**
* So that I planned a shadow fork. work anyway. likely and potentially mean net as well. so if we want, we could just avoid a net life cycle and just integrate the change with the shadow fork. That would still give us, let's say, a week ish, basically until, enough time for everyone to pass five tests, before we spin up the shadow fork. And then ideally, we've made this decision by then and we either include it in the shadow fork or not. 

**Tim**
* Okay. Okay. So I think what I would do in this case then is push this decision. Oh like I said we can put this in dev net five meaning like we'd update the client versions and. 

**Lightclient**
* I mean, I don't know how far along people are. I think, you know, we're kind of at the, at the bleeding edge of dev net five, I suppose. And it feels like a very easy thing for us to update. I mean, we are already determining if the thing is A77 702 delegating account and, you know, adding in the address to the designated that we return is, you know, it's extremely simple. 

**Tim**
* Okay. So clearly regardless of whether we put it in Devnet five or if, if we just as in the shadow fork, there's a path to testing this without requiring an entire new devnet iteration cycle just for it. my proposal would then be to give people a couple of days to review this and make a final call on Monday's testing call. and if there's anyone we need to speak to or we want feedback from, either try to do this, today or tomorrow or have them come on the testing call. does that seem reasonable? And then. Yes, actually the other point is having a PR to the IP. If we could get this today, I think that would help. yeah, that would help us reason about the change. but yes, we should not launch an entire new devnet cycle just for this. and then if it is, if we do move forward with it, then it should be a pretty simple change. We can implement it after Monday. 

**Parithosh**
* In case someone can't make the testing call and has objections slash support, then please at least leave a message on it Eth R&D it out at the testing call. Ideally, we'd want support from every year. 

**Tim**
* And yeah, one last comment I'll hide from the chat is that we had this behavior in 1702 before and we are now bringing it back. So, yes, it's, something that clients have implemented in the past. Anything else on this proposal? Oh, sorry. Okay. There's other comments in the chat now saying it was a different behavior that was implemented before. so. Okay. So then I, I will close by saying this emphasizes the need for a clear PR proposing the changes. If we can get this today, review it, on Friday and then, discuss this on Monday's calls. That would be ideal. And I believe this was the last, spec change proposal for, Petra. So, summarize, we have the seven, six, two three change that was merged already. Then these two changes around, the blobs. So one around the base fee updates. one around the fork boundary for 2537.
* We agreed we're not going to make the gas cost change. We're just going to clarify the IP with regards to what, division method to use and then make this final decision about 7702 on Monday's call, once we have a prep to properly review anything else on the specs? If not, yeah. Wanted to also highlight the audits we've done for the system contracts in Petra. I believe Frederick is on the call. I can give a quick update on this. 

# Audit updates [49:30](https://youtu.be/uh1hZCE4k0w?t=2970)
**Fredrik**
* Yeah. So in September, as some of you might know, we did a request for proposal for, basically bytecode audit of the system contracts in Petra. We had quite a lot of Proposals. I don't recall the exact number, but, maybe 15, something like that. and, basically we moved forward with a handful of these entities. the these have now been completed by these, firms. So, we now have, all the reports, available for them. So in the call, in two weeks from now, I would propose that we invite them to, to present the the findings that they have had, in, in their audits, basically. 

**Tim**
* Thanks. And I guess, just to be clear, all of the changes and suggestions from the audits have already been implemented in their contracts. Correct? 

**Fredrik**
* Yeah. Yeah, yeah. And we did like this. We can talk more about this, I guess, in the follow up call. But we we did this type of rolling audit where we had the first one do it. Then we implemented a lot of the proposals. Then we had a second one to do it, and basically rolled the audits like that to be able to cover as much as possible. but yeah, they've been implemented and there were no major findings. Um. 

**Tim**
* Thanks. Yeah. I think, that seems reasonable to have a discussion about it and answer any questions in the next call. I think if we can have sort of the actual reports, ideally a week or so in advance so that people can review them and raise any questions ahead of time, that would be great. yeah. We can do a deeper dive on the next act. 

**Fredrik**
* Yeah, exactly. Yeah, we'll we'll add them to a repository. I can, make sure that they are Distributed that way. And, yeah, I will, post where to find the the audit docs. 

**Tim**
* See any questions? Comments on the audits? Okay. yeah. Thanks, Fredrik. Next up. yes. I wanted to follow up again on, um. Sorry to think about testnet releases and, scheduling. so we have Devnet five up right now. I expect we'll need to do a bit of work on this. and we have some, like, final spec changes to consider. I guess my first question would be, you know, how our clients generally feeling about moving to Testnets. Do people feel like we want to start getting this done In, say, you know, the next couple of weeks, are there things that, teams feel they need a bit longer to work on or to finalize? and I guess related to this, do we want to potentially fork both test nets using the same client releases, or do people prefer to have two different client releases and potentially a longer break between the two test nets? yeah. How are people feeling about, moving this test nets?
* And if there's no strong opinions, maybe my starting proposal would be something like we should set test net fork blocks on the next HDP in two weeks.
* Expect, Expect client releases in the week after that, so the week of February 3rd and potentially have a first testnet fork on the week of, February 12th. Depending on how we do releases, we could have the second testnet fork either the week after or two weeks after, which would be week of the 17th, the week of the 24th of February. is that a schedule people feel is reasonable? Um. Okay, so no objections. So I guess what if there are no objections, what I would do is yeah, I think on the next, either next week on the consensus layer call, or at the latest on the week after that, we should, yeah, start looking at at updates, Perry has questions about whether teams have started merging changes to their release branches. **Tim**
* Seems like Basu has. Oh yeah. Getting a bunch of thumbs up. Uh. Basu. Tiku. Never mind.  Breath. Okay, great. So it seems like things are generally moving forward. Well, so what I can do is I'll propose, I'll propose some potential dates and for blocks, on next week's AC, DC, and, we can take it from there, but we'll roughly target something like, the,  Sorry, the last week, or. Sorry, the, the early February, basically for the first test networking, which would give client teams like two weeks or so to get a ready result. and it seems like there's no objections to this. Fit. and then related to this, Sophia wanted to bring up, something around setting the gas limits. as we, as we put these releases out for testnets. Sophia, do you want to give some context on the gas limit? 

# Holesky gas limit [56:04](https://youtu.be/uh1hZCE4k0w?t=3364)
**Sophia**
* Yeah. so for context, we're all aware that recently there was a push by validators to increase the gas limit to 60 million. in response to which some here found what is essentially an edge case, preventing us from doing that immediately. I don't think this will be a one time thing. We would like to more or less continually increase the gas limit over the next several hard forks. and there are currently, several threads of work that people are people are doing to enable this. but that also means that we'll need to know what increases are safe. well, ahead of time and foresee, problems with them. and, so I'd like to suggest that the way to do this would be to have always have a higher gas limit than mean that, and unless there are any objections to this. and then I would ask, client teams, now to set the default limit on Holeski to 36 million, and then when it forks to Pectra, go to 60 million and we can proceed from there. 

**Tim**
* Any objections to this? Okay. yeah. So we don't quite have a way to, like, spec this, but I think as people start to, work on their test net releases. We, um. Yeah, we should make sure that, we include these changes. Oh. And, uh. Okay, there's a comment saying base two already has this. thank you as well. So. Great. prism as well. So. Yeah. So the test net prism. Never mind. So great. So test net releases can go with 36. And then when we have a main net release we can bump the defaults for the test nets to 60 million as well. Um. And then there's a question by POTUS in the chat about the test net forking schedule around whether we have enough validators in host key to actually make it happen before main net is the risk here that key doesn't finalize or something for long enough for mainnet, Perry says. We have enough validators under our control. Okay. We should be good for housekeeping. Okay.
* Anything else on, net schedules or gas limits? Okay, great. okay, next up on the call, different topic. Felix had a proposal around RPC standardization. I don't know if he's on the call. I think so, Felix. You wanna give context on this? 

**Felix**
* Yeah. I'm here. Can you hear me? 

**Tim**
* Yes. 

# RPC Standardization [59:14](https://youtu.be/uh1hZCE4k0w?t=3554)
**Felix**
* Okay. So, yeah, I posted this document a couple a days ago. Just to clarify. so, what? I posted the document mostly so that people who aren't super familiar with this whole thing can can read a bit more. But ultimately what I want to discuss on here isn't so much the document, but some specific things that we should probably do now to move to move this process a bit forward. so first of all, this kind of started because I asked, Perry for, to include the RPC compatibility test as part of the hype run for the Devnet. And, the reason why this is because we have this cycle for this fork cycle, we were actually pretty quick with adding the, RPC compatibility test, for Prague. So there are some Prague tests already in there, and we are adding more right now. And so, it's actually very interesting. basically, we can use these tests to check if the clients implemented the more optional parts of the fork correctly, like, for example, if they have support for the new seven. 702 delegations in each call and things like that.
* And this is something we've never done before, but, unfortunately, this testing doesn't really work because, yeah, the clients still have issues, just, you know, with the basic test set up. And, so this is why kind of I started this effort. So I feel like, you know, I've been working on RPC standardization for a long time, and, yeah, it's just very frustrating because there's very little feedback from the client implementers. And I never really know if like, these, they find these tests actually useful or, yeah, if there's any interest to move the spec forward. **Felix**
* And then there are some open questions in general, just like, how are we going to be handling updates to the spec and what should be the scope of the spec and all of these things and so on. The specific question, that I wanted to ask is just more generally do. can we get some more support on. Trying to pass these tests and, should we have like a dedicated breakout call related to these things? Like, maybe that could be a good start here. 

**Justin**
* Yeah. Hey, this is, Justin from Bay view. We're very interested in improving the RPC specifications as well as potentially, you know, a lot of the things that were discussed in discord I found very productive. And we have a lot of interest in this. So, if the first steps in doing that is to make the, the testing, a little bit more of a gate to moving forward, I think we're all for that. 

**Marek**
* So we never mind are also interested and we are actually checking those tests. I know that we are not passing all of them, but sometimes there are like weird issues, between, for example, GAF and never mind. And actually, I think we just need to discuss it more together. 

**Felix**
* Yeah. Yeah. So there is a, there is a json-rpc channel in the discord, where we generally discuss it. I brought up some of the things before, so mostly the like there are two classes of issues so that some clients do not pass the test because they cannot load the test chain, or because they have some other issue with it that prevents them from even running the test. This is currently the case for Aragorn and Bisu, and Aragorn has been broken on these tests, like at least in The Runner that we use for more than a year. So I have actually no idea what the status of of Aragorn and related. I just gave up trying to make it work. the, other issue is that once the tests are actually running, we see that there are some minor details in all kinds of places. And I've tried to elaborate a bit on the document, like kind of the specific kinds of things that happen on there. And we do have to come to an agreement.
* And generally I think we do have to come to an agreement of like what's in scope, for example, specifically for the core devs to decide on even because ultimately what the RPC interface is implemented by so many people in so many different contexts that it feels weird to just only have this be like a core dev thing where we like, we make these decisions. However, there's a subset of the API that which it's the subset that's currently in the specification, that thing I do think the Ethereum core devs have some authority over. And we need to figure out like is this it or do we want, do we want to expand this set of, of of functionality or how should we handle these, these kinds of things. **Felix**
* And it's more like a process question. I don't I just want to know, like where is the forum where we can come up with the decision? acid was used as a forum in the past, but it's just kind of weird. And so yeah, I just I just don't really know. 

**Tim**
* One question I would have for you, what are the other people you think or projects we need to include in these discussions? Like, is it like, you know, infrastructure providers basically, or like l2's that, it's more about the users of this than like the forks of the client on, say, L2's? 

**Felix**
* I mean, yeah, so it's the L2, it's the wallets. The wallets also provide this API. It's the infrastructure providers, basically everyone kind of. 

**Tim**
* Okay. Got it. 

**Felix**
* Is somehow involved with this. And I mean we cannot define everything for everyone. I mean, even now, it's not even clear if the wallets should be included in this process or like if they should have their own process, this, which they don't. It's just this is a very organic thing, like the RPC is one of these things that is just like inherently very organic thing, because it just grew out of everyone trying to kind of support the same thing. And with the standardization, we are sort of like post-facto trying to figure out like what can even be standardized. So that's like this. That is why it's so messy is because there wasn't really a spec for the longest time, and now we're basically retroactively trying to create one and trying to align everyone as best we can. But I mean, a lot of these actors will just not be. Won't even be looking at the spec. 

**Tim**
* Got it. Roman, you've had your hand up for a while. 

**Andrew**
* Yeah. So very much in favor of this effort. my only request would be if, standard in this case would be considered the minimal subset of functionality that every client should provide, but the clients are free to. Extend their method, their responses with any fields they want. And uh. So basically changing the, assertion equality test to be more relaxed. Regarding additional fields. 

**Felix**
* Yeah, this is this is this now goes a bit into the detail. I also don't really know how much time we honestly have on here. So I so I don't want to go too much into the whole detail, but this is actually kind of a good point. So the thing is that at the moment we have the situation that all of the clients have various extensions to the spec, and I've tried to highlight it a little bit in the document. One way out of the situation would be to just freeze the extensions at their current state, make all of these a part of the spec as they are right now. And then basically we would be in agreement on the current state. And then in the future we would have to come up with some other process where the clients can add extensions if they want to.
* I think the current method is not super sustainable with like everyone, just sort of like adding the extensions when they feel like it, because it means we will never reach this point where the standard stuff is supported. Like we can never fully agree on the API in the current state.
* And that's why, yeah, I kind of put in this request.
* That would be good if actually this is something we always kind of wanted, is like that client would somehow push back a bit against users who want to put in these extensions and just literally say that, like, okay, there are certain extensions you can make, but when it comes to certain other extensions, it requires a much more extensive governance process. And yeah, basically. I don't know. I know you. You don't necessarily agree with this, but you know, from the perspective of standardization, it really hurts things when basically it's all like a moving target. 

**Tim**
* Okay. I think there's a yeah, rough consensus in the chat that we should have a breakout on this. and maybe start with a call with just client teams and then potentially have a follow up call where we kind of open it up to more people. and Justin says he's happy to herd the cats on this and try to find the time. So let's maybe have a poll in the JSON RPC to find the best time and try to set up a call in the next week or two to go into more details. Justin, are you okay running with this? 

**Justin**
* You got it. 

**Tim**
* Thank you. Anything else? anything else to discuss on this before we wrap up? Okay. Yeah. So thanks a lot for, the write up and bringing this up. and we'll follow up in the Json-rpc channel. Next up, Kev had a comment around, finalizing requirements, around, hardware limits and potentially opening up the discussion about bandwidth cap. You want to share a bit more here? 

# Hardware & bandwidth requirements [1:09:50](https://youtu.be/uh1hZCE4k0w?t=4190)
**Kevaundray**
* Yeah. Can you hear me? Hello? Yeah. So, yeah, we've been collecting, feedback on the hardware requirements stock for a while now, and, it seems like we can start calling for some sort of finalization on there. and I just wanted to alert everybody just in case people haven't looked at it. people have, like, strong opinions that they want to still, put across, feel free to, like, put it in the discord or on the hackmd MD document so that we can see, ideally we start finalisation on the next ACD so if you have time to look at it between then and now, if you haven't already, that'll be great. should we make it. Yeah. The question on making it into an informational EIP, I would ask the EIP maintainers. but yeah. Tim, do you want to. 

**Tim**
* Yeah. So I think the one advantage of something like this is then it's easy to reference and people are aware of it, and it's kind of part of the set of things we reference. The one downside maybe is that, once we have an EIP final, we don't like to update it. So, you know, to the extent that we expect these hardware requirements to change, it means we would probably just have another informational EIP, say in three years. You know, we revisit this and things have changed. then we would just create some new EIP that says it supersedes the previous one. but yeah, I do think having it live somewhere a bit more permanent than like a document or a research blog post, would be would be good. yeah. Nico. 

**Nicolas**
* Yeah. We could keep the IP under the living status and having, like, an informational one that is living. 

**Tim**
* Yeah, that's true. We can do that as well. But, um. 

**Nicolas**
* So we don't have to open. 

**Tim**
* Yeah, yeah. 

**Kevaundray**
* Yeah. I have no strong opinions on sort of where it lives or so. Yeah. We can probably discuss that offline if like the EIP maintainers don't have any strong preference towards. 

**Tim**
* Yeah I think we can we can do this. And that's kind of a good way to move this towards like a more finalized state. and you know, at some point we point. You can literally have it in Last Call as an IP. And then you mentioned bandwidth as well. So with the idea here to also have like a similar dock for bandwidth requirements and kind of go through a similar process. 

**Kevaundray**
* Yeah. So there is a dock for bandwidth. I kind of wanted to push towards the TLDR of it to see where the dissenting opinions are first. just because it's a bit more controversial. possibly we could just put that the bandwidth requirements inside of the same IP. if it's not too controversial and we can sort of finalize it before the along with the hardware requirements. but I have no strong opinions on whether we have 1 or 2 either. 

**Tim**
* What are the controversial, do you have the link to, the bandwidth one? What do you feel are the controversial, bits? 

**Kevaundray**
* Yeah. So I can, I need to modify it a bit more, but I put it inside of the GitHub issue. Essentially, I want to start a discussion on going for a 25 download 25 upload. Given we have fossil and you're using MeV boost and 50 download 50 upload. Given we have fossil but you want to self build. 

**Potuz**
* I think I was one of the one dissenting on this document. I think Ethereum today doesn't have a way of differentiating nodes from proposal, proposal and validating nodes from just full nodes. And, and I think this, this documents were based mostly for validators that have hardware that is overdetermined in general. I think unless we have a way of differentiating the duties of validating nodes and non-validated notes. We should really aim to have hardware requirements for full nodes that are typically required to have less hardware and less bandwidth than validating nodes. 

**Kevaundray**
* Right. Yes, I think I replied in the GitHub discord with that. Since you're a full node, you're not as latency sensitive, so you can have less requirements than validating node, or in particular someone who's trying to do a local block building and a testing. And I think what I said was that we should ideally have a document for full nodes as well, even if most of the stuff are sort of the same right now, like storage would still be the same, for example. your hands are still up. Did you want to say something? 

**Potuz**
* Oh, I apologize. No, that was my only comment that I think it's just hard to differentiate. As I say, storage is the same, but most of the things, everything is the same except CPU time and upload link when you're proposing. Everything else is essentially the same, right? 

**Kevaundray**
* Right. I think it'd be good if when we make protocol upgrades, we sort of have this distinction, which is what I think two documents would, sort of make very explicit, if we make a protocol upgrade that pushes up full nodes, it should become quite obvious, hopefully. 

**Potuz**
* That if you're if the document that says for validating nodes, you need to have, this bandwidth or this storage, then you cannot have a document that says for full nodes you can have less storage. So since the bottleneck for storage is the full node, I think we should focus on the full nodes first, establish that number that is the smallest number. And then then we can talk about validators that are anyways going to be over determined. So I think it's it's we should have started with the full nodes before the validating nodes because the full nodes require less. 

**Kevaundray**
* Right. I mean, I don't think it matters because we can say if you're a full node and you want to keep up with the chain just as a validating node, then you'll need to have the minimum requirements just like a validator. But if you sort of want to be one slot behind, for example, then you can have less than, let's say 25mbps, the storage. I do agree the storage would still be the same over both. but yeah, I don't think it matters which one we started with. 

**Potuz**
* I don't disagree with anything you're saying. It's just that the optics of this is you're going to present an IP, which is for requirements for validators. No one would disagree because validators I mean, all of these requirements for validators are reasonable. But the problem is that then later those requirements that are reasonable for validators might not be reasonable for full nodes. And there's no way back from that, because once you require something for validators, for storage, for example, then full nodes will require the same. So I think it's more reasonable to start with full nodes that require less. And then you can require more for validators. And then becoming a no op. 

**Tim**
* So what I would propose here is we have a single document for hardware bandwidth. That's an informational EIP. And then you have two columns. One that's for validators, one that's for full nodes or two sections or whatever. Um I agree these requirements should be different. And, you know, they might evolve differently over time. And I think even if you zoom way out into the future, you know, we have these ideas around a tester proposal or separations or whatever. So you could imagine having a third column. It's like full node, the tester node, proposer node, whatever. so I would move towards having like a canonical reference document. and then yeah, try to just have different categories, as part of that. And our starting ones are bandwidth hardware, full node, validator node. Does that make sense? 

**Kevaundray**
* Yeah, that makes sense. I would say it's probably easier to have, well, maybe I need to think about it, but it seems easier to have separate documents, but then have one IP that sort of merges them together. 

**Tim**
* Oh, sure. Yeah, yeah. Like, we can we can do the discussion like independently. But I think like once we have some consensus on these things, they should all come together in like a single IP, if that's okay. 

**Kevaundray**
* Yeah, that makes sense. I guess, does anyone have a dissenting opinion on the bandwidth recommendations? I guess the the rationale behind it is that once we have fossil, local block building is not as important for censorship resistance. so if you do want to go down the local block building route, you will need to have sort of sufficient bandwidth for it.  Right. That's true. Fossil doesn't currently include blobs. 

**Tim**
* Is there a I forget if we created a channel to discuss this in the R&D discord or where? If not, where were we discussing this? 

**Kevaundray**
* Most. We had a, I think a general ACDE channel initially. 

**Tim**
* Okay. Got it. Does it make sense to also have a separate channel to discuss this? Because I expect we'll come back to the topic, over time. 

**Kevaundray**
* Yeah, I think it'll be useful. yeah, just a bit surprised. No one has any dissenting. 

**Tim**
* Yeah, yeah. 

**Tim**
* The doc in the channel, dissenters will come out. So. Okay, perfect. So let's do this. I'll create the channel after the call, and then, Kev, you can, draft the docs based on. Yeah. Okay, cool. Your current specs. And, we can take it from there. 

**Kevaundray**
* All right. Thanks. 

**Tim**
* Anything else on the node requirements? Okay. If not, we have, one last quick announcement, around EIP, editing. I believe it's an EIP editor workshop tomorrow. Sam, do you want to give context on it? Sure. 

# EIP Editors' Workshop ethcatherders/EIPIP#372 [1:21:13](https://youtu.be/uh1hZCE4k0w?t=4873)

**Sam**
* How's my audio? Good. Okay, good. I never know with zoom. yeah. So we're doing an EIP editing, like workshop tomorrow. It's for anybody who's interested in becoming an IP editor or an EIP reviewer. one comes with governance responsibilities, and the other one doesn't. just pulling up the time here, but my computer seems to have died a little bit. yeah. So that'll be tomorrow at 1600 UTC. we're going to go through how an EIP like goes through the workflow. We're going to talk about the types and categories of EIPs.
* And then I'm going to do a few live EIP editing so people can ask questions and just kind of see how that works. and then we'll have some questions if anybody wants to ask anything. So yeah, come on out tomorrow for pm UTC. looking forward to seeing you all there. 

**Tim**
* Thank you. and yeah, I'll add this is something where, current IP editors have a lot on their plates. It would be amazing if we could eventually move to a world where, like, this is spread out much more evenly. my dream is something like every client team ends up with an IP editor. and others obviously can participate as well. But going from a spot where we only have like 2 or 3 people actively doing this to where we have 5 to 10. I think would help improve one of the just basic Thick operations of the IP process and then to, you know, give us more bandwidth to potentially, evolve it in a way that's, more useful to everyone. so if you've been curious about IP or intimidated by them, please join tomorrow's workshop.
* I think, yeah, it'll be a good starting point to bring in more people. And there was a comment in the chat about whether it will be recorded. Yes it will.
* Any other questions? Comments? Okay. anything else people wanted to bring up before we wrap up today? Okay. If not, then yes, there are a couple PRS to be open and reviewed before Monday's call. I'll put a summary in the discord, but please, keep an eye out for those and I will see everyone next week. Thanks, everybody. 

**Fredrik**
* Thank you. 


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
Jan 30, 2025, 14:00-15:30 UTC







