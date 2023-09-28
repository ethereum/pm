# Execution Layer Meeting #169
### Meeting Date/Time: August 31, 2023, 14:00-15:30 UTC
### Meeting Duration: 1hour 30 minutes
### [GitHub Agenda](https://github.com/ethereum/pm/issues/850)
### [Video of the meeting](https://youtu.be/GkSjuiqqkKU)
### Moderator: Tim Bieko
### Notes: Alen (Santhosh)

| Decision Item | Description                                                              | 
| ------------- | ------------------------------------------------------------------------ | 
| 169.1 | **Dencun** Devnet #8 launched two weeks ago on August 16. Barnabas Busa, a DevOps Engineer for the Ethereum Foundation, said that the developer-focused testnet for the Dencun upgrade is looking healthy. Busa mentioned that nodes operating the Nethermind (EL) client software appeared to be having some issues. Lukasz Rozmej, a developer for the Nethermind client, explained the nature of the issue was due to misconfigurations in their implementation for the blob transaction pool.
| 169.2 | **Dencun** Regarding EIP 4788, developers briefly reconfirmed the new deployment strategy for the code change. The contract to expose Beacon Chain data on the EL will be deployed like a regular smart contract, which requires someone to fund the contract address and do so before upgrade activation. The next testnet for Dencun, Devnet #9, will feature this workflow and ensure developers are comfortable with the process.
| 169.3 | **Devnet #9** One more devnet with Dencun specifications frozen. Stress-test the network and assuming developers are happy with it, move on to public testnets. Otherwise, launch Devnet #10.
| 169.4 | **Holesky** Fork the newly launched Holeksy testnet and deploy the Dencun upgrade on it.
| 169.5 | **Goerli** Then deploy Dencun on Goerli. As the second last testnet launch before mainnet, the specifications for the upgrade by this point should be final and provide enough time for users and applications to test their software before mainnet upgrade activation. Dencun will likely be the last fork on Goerli before Goerli is deprecated and replaced with Holesky.
| 169.6 | **Sepolia** Finally, deploy Dencun on Sepolia for good measure.
| 169.7 | **Verkle Trie:** Next, developers discussed Vitalik Buterin’s [proposal](https://notes.ethereum.org/@vbuterin/verkle_and_state_expiry_proposal) to combine the Verkle Trie and State Expiry roadmaps to reduce the complexity of Verkle Trie implementation and expedite the benefits of State Expiry on Ethereum. As background, the Verkle Trie or Verkle Trees are data structures that allow a user to easily verify a large amount of data by relying on a single cryptographic proof. They are not unlike the Merkle Patricia Trie (MPT) which is the data structure used to store Ethereum state. However, Verkle Trees are comparatively more efficient to prove than MPT, which is why developers have been working on transitioning MPT to Verkle.
| 169.8 | **SSZ Serialization** Etan Kissling, a developer for the Nimbus (CL) client, gave an update on his efforts to upgrade Ethereum’s data structures to an SSZ serialization format. For more background on this issue, read prior Ethereum developer call notes here. Kissling highlighted a new approach to updating Ethereum’s data serialization using a SSZ “PartialContainer” based format


## Intro
**Tim**
* Okay. We probably have enough people to at least get this started. Yeah. There's someone from Geth. Is anyone from Nethermind here? Oh, Vitalik. Have you joined another Nethermind? 

**Tim**
* Let's get this started. welcome, everyone to 169. so some Dencun stuff today. Getting some updates on Devnet 8 and then we can continue the conversation around the testnet ordering. And then Andrew wanted to bring up the Verkal try and state expiry strategy so we can spend some time discussing that. And those are basically the two big things. After that.
*  I think Ethan just had some updates SSZ on wanted to share. and that's pretty much it. I guess to kick it off, do we have a Barnabas, do you want to give an update on Devnet eight? 

## Dencun Updates: devnet-8 [1.15](https://youtu.be/GkSjuiqqkKU?t=75)
**Barnabas Busa**
* So dedicated has onboarded all the different clients and everything looks very healthy and we have a few of the pairs that are not really working. Yes, we had a smaller issue with Nethermind. Hopefully someone from the Nethermind team is here to let us know what has happened.
* I'm not quite sure, to be honest, but we see quite some drop. And then they released a new version and after rolled it out, everything went back up again. And so we have a few pairs, as mentioned, mainly Aragon and EthereJS that are struggling with a few of the keys. They have now beacon chain Explorer, also onboarded. And we have a light beacon chain explorer also. I will share the link in a second. 

**Tim**
* Sweet. Thank you. Does someone from Nethermind want to give some context on the issue that was fixed? 

**Nethermind team**
* So I'm not entirely sure because I wasn't involved. But as far as I know, the experimental transaction pool stuff was merged and was causing problems and was like that was merged. And so yeah, so that's basically it. So the transaction pool part that we have separate for, for it, for, for transactions was causing problems. It's not yet ready. 

**Tim**
* Got it. So so was the fix just to revert that change rather than having a full working transaction pool? 

**Nethermind team**
* Yes, I think so. So I think Martin will handle that since. 

**Tim**
* Got it. Thank you. any of the other clients want to share?  Yeah. Context on any issues or fixes they've made this week. Okay.  And I guess before we go into the testnets themselves, it seems like we probably still want to get more testing done on Devnet-8 and.
* What does it feel reasonable to try and get to try and get all of the pairs working on Devnet 8 And then once we have that move to Devnet 9, do the last changes with the four seven, eight eight spec and hope all the pairs sort of work, work on that pretty smoothly. 

**Barnabas Busa**
* I personally think that's reasonable. And I'm just curious if we had an agreement on how to deploy the contract. 

**Tim**
* So we. Yeah We decided we're just going to use a normal transaction. and if I remember correctly, the reason was it was, it was pretty split between that and the custom deployment logic, but we figured a normal transaction was easier to implement and just start with that. And then if for whatever reason there's like issues with using the normal transaction, you can always add the logic around the enforce deployment. yeah.  

**Barnabas Busa**
* Assert there be any test for this. 

**Tim**
* Good. Good question. Don't know, Mario.  What do you mean by. 

**Danny**
* So there is going to be like a particular address that needs to be sent from it's like a synthetic transaction and that it's reverse engineered from a particular, actually don't know exactly how it works. I'm not going to explain it, but there will be a particular address that needs to be funded to do the deployment and they'll need to be a gap, a big enough gap between Genesis and the fork on that test net such that we can do that.
* I think we normally have such a gap, but it's just going to be something that we manually need to make sure is done, in that interim and not to just for this test net, don't just deploy it to a particular memory location at Genesis. We want to do the actual transaction. The spec it's mentioned how to do so in the actual spec. 4788 That's why it has a particular address. 

**Barnabas Busa**
* And  the client teams can? Quite quickly. 

**Danny**
* Just one person has to do this. 

**Tim**
* Okay. Right. This is not in the client. 

**Danny**
* One person. Maybe Matt or others should, you know, write a script or just do it themselves. If it's not script not worth to be scripted and it's just a couple manual steps. 

**Barnabas Busa**
* But I assume for stuff like Devnet, we would need to have this then deployed on the. And the actual epoch of Dencun. 

**Danny**
* No. And deployed before. So that's why I said there needs to be an adequate stretch between Genesis and Dencun because the manual transaction has to make it on chain. 

**Tim**
* Mario?

**Mario**
* Yes, sir. So I guess we can just ask. The expected address in the Testnet Genesis, Genesis and also the tests just to match what the address is currently in the EIP. And yeah, instead of sending the transaction and that's the reason I asked the if we were doing a normal transaction under this section because we did with this transaction, we have a deterministic address everywhere and it's just easier.
* But yeah, for the tests, I assume we're going to update the address to the final address we are seeing in the EIP for development, if that's okay with Barnabas and. Yeah, we can do that ASAP if you if you guys want. 

**Danny**
* And so we should certainly go on. Sorry. 

**Tim**
* I was just going to say. Yeah, as long as it doesn't affect any. So I guess as soon as you change it in Hive, you know, those tests will start breaking for clients. and obviously we shouldn't retroactively change this on devnet 8, but yeah, going to devnet 9, we should make sure that yeah. Hive reflects this address. 

**Mario**
* Yeah, I will just send the message and when we get sufficient. go ahead. From every client will just update them. Have this. 

**Danny**
* Mario, can you make sure that there are five tests where this contract is not deployed in time to that address? Just that's something that almost certainly won't happen, but it's something that can happen in this technique. So I just want to make sure that we do test the kind of like no OP at that address. It should just work, but we should have to. 

**Mario**
* Yeah, absolutely. 

**Tim**
* And so there was a question by Barnabas in the chat asking if client teams are ready for Dev net-9 and guess based on the comments by Nethermind, should like do we want to figure out the full blob transaction pool on dev net-8 and potentially test that on dev net eight before we deploy Devnet 9? Or would we want to move to dev net 9 sooner rather than later so that we can have the final 4788 spec and then maybe do a bit more non-consensus changes on that dev net. Jochem? 

**Jochme**
* I sorry. I just want to ask like about 4788 for devnet nine. Do we also want to add the Beacon contact as a warm address or not? 

**Danny**
* You say the address? 

**Jochme**
* A warm address. So like it is sort of a. But do we want to add to this warm or not? I'm not sure if this is the right place to ask this question, but do we want this or not? Because I know this question has been raised before on the R&D. 

**Tim**
* So this is the deposit contract where we should always treat it as a warm address. 

**Jochme**
* No, So the beacon block route. So the new. The new contract. 

**Danny**
* Matt says, I think we decided no. 

**Jochme**
* Yeah. So. Okay, then. That's fine then. Yeah. 

**Tim**
* Okay. And guess so. Back to the Devnet 9. Oh shit. I was muted for everyone on the stream. sorry about that. Everyone watching the YouTube. I can try and swap with the zoom recording here today.  Back to that Devnet 9. so do we want to get it live as soon as possible? Or do client teams want to make sure that things are working? that we have like the, the blob transaction pool on dev net eight that we may spam dev net eight, send some bad blocks on it and all of that.
* Yeah. How do people feel about moving to the next one versus doing more testing here? 

**Danny**
* Assuming there's no spec change other than this, the way this contract is deployed, I'd rather be very confident going into Devnet nine rather than like saying, okay, well, we hope these things are going to work. And so in that case, I'd rather iron out the things that we know are issues. Otherwise, if we have a high chance of issues in Devnet, then we certainly will have a devnet tend and I'm not saying we shouldn't have a devnet 10, we should have the amount of devnet that makes sense. But I think at this point we can attempt to have Devnet nine be like really solid. 

**Tim**
* Yeah, I would also lean towards that, unless people think there's like some reason to test the 4788  change much, much sooner.  

**FLCL**
* It looks like the current debate. Well, clients have several quite critical issues. Like we have differing opinions about how to calculate block hashes, which is quite a basic stuff, right? And we are observing payloads, new payloads with some kind of wrong data. Up here, so maybe we could at least make it more stable and fix all of that because the network had multiple forks, as far as I know.
*  Now it seems more stable, but this issue is still exist, and I think it will cause, a lot of troubles if we do another network. Maybe we could spend more time on stabilization. 

**Danny**
* I also just want to echo, like I believe and I think most of you on this call believe that like the deploy method for 4788 is like almost a no ops for clients. And so I don't think we need to rush to test that spec change. Like it really doesn't manifest as a change to them. It's obviously something we have to test, but stability and reduction of additional overhead and dev net, it seems to be the preferable. 

**Tim**
* Okay. So yeah, that seems pretty widely agreed upon. So, let's move forward that way and obviously we'll check in on both the CL next week and then this call in two weeks, about devnet testing. And we can use that to inform when we launch Devnet 9. And guess so the next thing. 

## Testnet ordering [15.54](https://youtu.be/GkSjuiqqkKU?t=954)
**Tim**
* So, you know, once we're once we're kind of feeling confident with the Nets, whether that's after the net mine or, you know, potentially if we need more. After that, we started discussing the ordering of test nets on last week's call and think it would be good to start to align on the order just because we're going to want to announce the launch of goerli, the deprecation of Gordie and all of that.
* So even though we don't need to like talk or decide on dates or anything now, yeah, I'd like to just get a feeling from like what do people think is the right order for them. My proposal was starting with hockey because it's basically new. No one will be using it and I ass they'll be like a pretty controlled set of operator at Genesis. So it's not a huge group to coordinate, to upgrade the test net then I would probably do Gorlie if this is the last fork we're going to do on the network.
* I guess the risks of breaking it are slightly lower in a way. And it's also good because most of the applications and especially the l2's run their test nets on Gordie so it gives them a tiny bit more time to test and would finish with Sepolia just as a final sort of dry run before main net. and by then we'd obviously expect to no longer have any any sort of issues. 
* Yeah. Does that generally make sense to people as a as an ordering? Do people have preferences or different preferences than that? 

**Tim**
* Okay. Yeah. No objections. So if that's good, we'll probably have a blog post announcing that post  went live once it's actually been launched. And, you know, it's. It's relatively stable in that same blog post will also mention that this is the last blog for goerli. And finally as well there's been some folks working on ephemera which is a dev net that keeps or sorry, a test net that keeps restarting at Genesis for, for stakers to test their setup. So we'll start mentioning that as well.
* But it's still, it's still semi in development, so we're not going to use it as like a one of the main test nets or anything, but we'll at least let people know that they can test validators on it and have like a quicker iteration cycle. 

**Danny**
* Is the cycle one.Week or two weeks. Or less. Always. 

**Tim**
* I always forget. I think it's on the website. Let me check. 

**Tim**
* I can't rememeber it super quick. I don't know. Is Mario on? 

**Tim**
* See. And then Barnabas, you had a guess, just changing the time on Hoskey for, basically removing Cancun until we figure out the time. Is that right? 

**Barnabas Busa**
* Yeah, that's correct. So apparently  would have an issue overwriting the content if it's already set once. 

**Barnabas Busa**
* So this is something that maybe some clients will have to change, but the pier is still open. I would just want all the year to. You know, approve it before I merge it in because it can potentially. For some issues, especially for urban users. 

**Tim**
* Sweet. And anything else on test nets or dancon. 

**Barnabas Busa**
* One more thing that I also think that should be the first one going into the Dencun. And we should really stress test the three and six blobs that we have set up. So it's going to be a very good test to see if you can handle it. And after that, we could adjust if needed, Dencun to 2 to 4 or if it's deemed reasonable, then I think we can leave it as is because at 1.5 million validators, if that can handle it, then it should be good for the minute to. 

**Danny**
* The heads up. Adjusting down would be a hard core. And so I'd rather if we did deploy through six, I'd rather just leave it as is or reboot the net and having like a, you know, a hidden hard fork for that testimony. 

**Barnabas Busa**
* I'm not saying that we should like hard fork. I'm saying that we could probably adjust it down for Goerli or sapolio. 

**Tim**
* Right. But would that mean. I know on the send you can probably set all of this in the presets on this CL. I don't know if on the EL this would mean we have to maintain two versions of the code paths based on the network. So I don't know how easy it is for the CL to support different block counts by different on different networks. 

**Tim**
* Yes. I ass it's easy on the. I don't know if it's easy on the. On the yell. 

**Danny**
* It seems like a configuration parameter, but sometimes things go. 

**Danny**
* Unexpected? Yeah. 

**Barnabas Busa**
* It's a reason we wouldn't want to fork. Also down to two for. 

**Danny**
* That would certainly be exceptional. Codepath. At that point, because you need conditional logic to change the configuration dynamically. And so I would definitely not advocate for. Even if it's not the parameterization we go with. I think you either keep hulsea at a higher or you get rid of hulsea and start over. 

**Tim**
* Think, Justin, you're going to say something about the side. 

**Justin Florentine**
* I think Danny's got me covered. I was just saying that for Besu, at least, it's more of a protocol schedule concern than a configuration concern for us. So it would be work, but it would be and it would be nontrivial work, but it wouldn't be hard. 

**Tim**
* Okay, So. But it would be better to keep hölszky at three six no matter what. Even if we make all the other deaf or all the other test nets and make net two four. Right. Then rather than having a special fork just on hölszky that goes from 3624

**Justin Florentine**
* It would be easier. I wouldn't say it's better, but yeah. 

**Danny**
* So just a heads up. We do have the schedule to talk about next week. Again, the main net parameters and some new information presented about big blocks on main net. And just to reopen the conversation, as you know, it's a default in our conversation, but we've all agreed to talk about it again, so we can obviously talk about it more here. But we before even deciding if he's going to go to four, three six, we should decide if we're going to.
* If we want mainnet to be such before we go to this. So next week is good too. Sorry I was wearing my hat. When I wear my hat, you can't hear me. It is not a tinfoil hat. 

**Tim**
* Yeah, it's better without the hat. Cool. Okay, So I think I got the gist of that. we're going to talk about it more on this CL next week. And there's some interesting data based on seeing larger blocks on main net right now. 

**Danny**
* Yeah. Please join, because it's their consensus call. You know, I think we've. We're easily talking about this for 20 minutes, if not a bit more with some more data to discuss. 

**Tim**
* Anything else on Dencun or the forks or the testnets? 


## Verkle Trie + State Expiry Strategy [24.51](https://youtu.be/GkSjuiqqkKU?t=1491)
**Tim**
* Okay. Next up, Andrew, you wanted to bring up the whole strategy around Verkal and state expiry. you maybe want to take a minute to chat about, what questions you wanted to get into, and then we have, I believe Guilla, Josh, on the call have been working on Verkal and then Vitalik, I think is also here. so yeah, we can probably hear from them. Yep. 

**Andrew Ashikhmin**
* All right. So, and I'm sorry, my connection is unstable, so I might break, but. Briefly speaking like to my mind, state expiry makes. 
* Sense because, well, for obvious reasons that with bigger state you the sync time goes up. But also like even disregarding the sync time with each access, the biggest state generally, like roughly speaking is like the cost is logarithmic and also like, like there are just so many dust accounts, things that are irrelevant. So just suboptimal to keep, never to never clean the state. So yeah, and I'm a big fan of both velko and static expiry and Vitalic's proposal makes a nice plan how to achieve both.
*  As far as I can tell, the only thing like the only problem is that like an address expansion, it's not like that was designed  to help with the state expiry, which might be technically challenging to have this address expansion. But to my mind that's a separate discussion. If we decide to have state expiry, then we need to to like maybe rethink whether we need, whether we achieve that with address expansion or somehow else. But I would rather have both velko and state expiry. 

**Tim**
* Got it. Thanks, Guillaume. 

**Guillaume**
* Sorry. Can you guys hear me? Yeah, I mean, I agree. The question that I'd like to understand, or at least the point I'd like to understand if. If you're making or. Yeah, I'd like to understand the point you're making. Sorry. Are you saying like, we should have, you know, Verkal or stateless end state expiry at the same time? Because, you know, the current upgrade path does not preclude getting state expiry later. Right. so my understanding is that you want both at the same time.
* And I have an issue with this because state expiry has been effectively abandoned as a research topic for the last two years. that would push, waiting for it would push Verkal back for at least a year if not more. And we have some kind of ticking clock in the meantime, which is the the state is growing and that means the more we wait, the more the conversion will take time. So I understand that if we switch to that scheme that Vitalik proposed and I think is very has a lot of things going for it, namely that you don't really need to do the conversion live.
* So it would be it would be actually not such a big problem, like it would not be such a ticking bomb. But the the way I see it is there's been efforts to to get it implemented. There's been several in in 2019, if I remember correctly, and also in 2020, they've both been abandoned. So, yeah, I don't see like at the current state of research which like I said is abandoned, I it's more like we're writing a blank check and we hope that there will be state expiry implemented in the future. yeah. 
* This way, if it turns out this is abandoned a third time, we find ourselves with having to perform the overlay transition. Except it's done a year later. So the amount of data that needs to be translated is even higher. so yeah, basically the question is not whether or in my opinion, it's not whether we should choose between statelessness and state expiry, but if we should do them at the same time. My favorite answer is no. But if you think differently, I'd like to to understand why. 

**Tim**
* And you dropped it. Came back while you were talking. Are you back? Andrew. 

**Andrew Ashikhmin** 
* Yeah, sorry I'm back. But, yeah, I didn't. I missed the last part. So is there a question? What's the question? 

**Tim**
* Yeah, guess the question is trying to understand if you are you arguing for state expiry to happen eventually or for it to be coupled with, with the transition to verkal tree inside the same Hardfork All right. 

**Andrew Ashikhmin** 
* No, but, but, my wanted to to happen eventually, but it affects Verkal because if, if we decide that it happens eventually then we can follow Vitalik proposal and not bother with translating parts of the Merkle. Patricia try with with every block. That's kind of that's how it affects the code. It actually simplifies. So. 
* It simplifies our transition to work together. Oh, yeah. Sorry. So if we do it eventually, we just need to do piecemeal translation and just. Just we don't like. If that happens eventually, then we can. We can introduce the. 

**Tim**
* Yeah. Think I understood the gist of what you tried to say, but you're breaking up quite a lot.

**Dankrad Feist**
* Yeah, sure. So, I think it's,  It's definitely still open that we will do state expiry and eventually, but I think we should also. So there is also basically the option that statelessness goes goes well, like we achieve all the goals with the local and very few nodes in the end opt to have the state because we find a good way of providing the state through other means, for example, like secured node with like clients proofs as well as, I don't know, like something like Portal Network and and in that world it seems like state expiry would become at the very least much less urgent and would be like a potentially long term future thing.
*  And then that world, carrying around the old Merkle Patricia tree would make work in many ways significantly worse and more complicated. And that is why eventually we opted like that. This is. Pretty and elegant, and that would be best to just do the full circle. And even in the state expiry world, that's still better because there's no old empty that's still carried around. so I think we should stay with this current roadmap, which is simply to like have a full transition to Verkal that makes no asstion about future state expiry, which is still possible. and the question to do state expiry eventually, which is still quite a difficult problem, especially because it's coupled with address space extension. yeah. So we make no prejudgment about that, whether it happens or not. 

**Tim**
* Got it. Vitalik. 

**Vitalik**
* Yeah. Guess you thought I would just give a bit of a background as to, like, why some of, like, we first thought about doing verkal and state expiry at the same time and then why we, you know, like, ended up switching and like some and some of the various nuances around all of those issues. so at the beginning, right, the, you know, we thought about verkal trees and verkal trees are important because they allow us to have witnesses that have bounded size, which makes stateless clients possible. It actually also reduces worst case bounds for VMs by quite a bit because like if you have a 400 megabyte witness, that would also be a forged megabytes of hash. so it's something that we probably have to do anyway.
* But the challenge with verkal tree verkal trees is one, the transition process and the transition and then two is that like they don't solve the full problem because there's still a few nodes that have to have the entire state, right? So with the transition process, the issue is basically that like converting a 50 plus gigabyte Merkle Patricia tree into a 50 plus gigabyte verkal tree in a live network is just friggin complicated. Like this is something that the research team like literally agonized on for more than a full year. Like remember like last year at Dev Connect, it was basically the topic at the research event.
* And you know, like it's basically as much effort as the entire rest of the verkal road roadmap put together, probably like just the process of how to do a live transition, like it's literally comparable to the merge in, in terms of complexity in some ways, right? And so it's pretty like it ends up breaking a lot of asstions like either you have to do some really complicated thing where nodes stick two states at the same at state routes at the same time, or you have to bring in trust asstions or nodes that are fast sinking during the transition process will have to have custom code to download two trees and so on and so forth. 
* And so with state expiry like the natural attractiveness of this. Right is basically that that whole complexity goes away because you basically say, well, the epochs zero or I guess the era zero tree. So it's that epoch to be somebody else. Now the error zero tree is a merkle Patricia tree. Then we start era one new state goes into era one and then after one year you state goes into era two. And actually we don't have to keep the birds around forever because what we could do is once we're in Era two, then we can actually go and just do an offline computation and just in place, swap the route of Era zero for with a Verkal route.
* And that actually ends up being significantly easier than than doing a live transition. Right? But basically, yeah, because just the form factor of state expiry does make it significantly easier to like do these two at the same time rather And like it basically removes the the transition complexity and it does of course add all of these other transition complexities involving base extension. And I think the problem of address space extension itself might might even be like complicated enough to be to have by itself been decisive in terms of putting things off, in terms of the research agenda. Right? Because like just to like give an idea of this problem, basically, Yeah.
* Right now we have 20 bit addresses. But then if we're going to have these new eras that the whole point is that objects that are created during these new eras would be in spaces that cannot collide with the existing 20 byte address space. Because if you see one of those objects in the state, then like you know that it's actually new and you'd end, you know, that you don't need to like scan proofs for like an absence of some other edit record in the past. 
* Right. And so, but the problem is that pretty much all existing contracts make huge asstions all over the place about addresses being exactly 20 bytes long and that doing that would work like getting around that would just require an unprecedentedly insane ecosystem level wide amounts of work. And like if we have the capability to do that amount of work, then personally I would like there's like five other things that are higher priority. Yeah. In, in service of the good that they could do for the Ethereum cosystem, right. Like, like getting everyone to switch over to. Like abstraction getting old adapts to support ERC 1271 and 6900.
*  Getting everyone to use to be standards compliant so non metamask wallets would stop breaking just like this. You know incredibly long list of stuff that, you know, that requires that same level of ecosystem level wide coordination and moving from 20 byte addresses to 32 byte addresses is like literally that level of a task. And crazier, right? Like even erc 20 contracts would have to be redeployed, right? Like there's huge amounts of code that for optimization purposes, assume that an address is 20 bytes and try to pack something together with an address within a one storage slot. So it's.
*  Now, there is one other possibility that's kind of less well known that I suggested, which is address space contraction. And there the idea basically is that we ban one over two to the 32 of the address space from being used right now. And then we start using that in order to make error, in order to create address spaces for new errors. And if we do that, then that actually completely solves the problem, but that it has this like one really important big sacrifice to it, which is that counterfactual addresses that are multi-user stop being secure. 
* So there's this fairly small but somewhat difficult to understand subset of applications that are kind of small right now, but might become significant in the future that stop working. And but like it's the sort of like security weirdness that I think, you know, rightfully sort of like perk security people's ears up in terms of just like bad things that could happen, right? Like we like security practitioners and devs and cryptography. People just don't have experience dealing with hashes that are preimage resistant but not collision resistant, which is effectively what we get if we use address space contraction because the hash part of the address would only be about about 15 bytes.
* So that's basically all in service of address space contraction for links. I wrote about this on ether research and they give you just like search on ether research and like maybe address space contraction or something, it might be in there, right? But basically it's like there's these two proposals and the think things kind of got stuck because they're both of like one of them is just very hard. And the other of them is very is kind of imperfect in a different way, though one thing that's worth noting is that we probably can't keep kicking the can down the road on this forever because as of today, the security that we have on address collisions is to the 80 and we are over the next, you know, a couple of decades got to get into the regime where like doing two to the 80 compute power to create an address escalation is going to be start to become open to more and more people.
* I mean, technically it's doable already, right? Like in its history, the Bitcoin network has done something like think two to the 93 work or something like that. 
* So right now though, yep, that's the one. But, but so it is something that we have to address anyway. But it's like a very thorny problem and like extension and contraction. Both have, both have their issues. And the one of the other kind of things with Merkle tree is, is that if we do the like a Merkle tree transition and we bite the bullet and we like actually do the complexity of implementing just a pure Merkle tree transition as a transition, then I think the the downsides of delaying state expiry by literally another decade go down by quite a bit. Right. And the reason why they go down is because even though it's true that the state size is going to keep blowing up and at some point people are probably going to complain and ask to increase the gas limit.
* At some point, the gas limit is going to go up to like 40 or 50 million or something. And as the state size will grow up faster and the state will be a couple of terabytes, but the portion of nodes that would actually have to have the state is going to be much smaller. And even validators like the nodes participating in proof of stake would be able to be stateless. With the combination of Merkle trees and the builder proposer proposer builder separation, including both ensure enshrined and the the current boost based stuff plus a couple of like fairly small bit modifications that are totally manageable. You'd have to do a little bit of extra work to make inclusion less work because you'd have to make.
* Transactions carry proofs with them through the mempool. But like, that's totally doable, right? But like, the point is that with that infrastructure, the ner of nodes storing the state goes down by quite a lot. 
* And like the amount of people who suffer, if the size of the state literally blows up to four terabytes is going to be much lower. And so if Merkle trees exist and the urgency of solving the state problem just decreases quite a lot compared to the urgency of all of the various other stuff that the enthusiasts have down the pipeline. Plus the urgency on the developer side to kind of just be cautious and continue to improve client quality and and make the existing chain work more efficiently and all of those things. So I think just kind of sarizing all of those different considerations put together like it does feel like a bit of a binary decision in that either you do state expiry quite like basically with the with the Verkal transition, or if that doesn't happen, then like it's okay to just wait a decade and do state or at least five years and do a state transition kind of fairly or do state expiry like fairly far down the far down the pipeline after that, like it's the middle path, like doing state expiry somewhere like one year or two years after the Merkle tree is dead probably is, is unfortunately a bit of a worst of both worlds, right?
* So I think that's roughly the, the consideration. And I think it just depends. I mean, like how much we are concerned by the. you know, like issues involving a growing state. another thing, actually. Feel like I might have sort of misspoken a bit, right? Like when we talk about things like complexity of state sinking, like doing state expiry also will require a changing a lot of that code, right? Like it's not like doing the state transition or it's not like doing a Verkal state expiry transition at the same time is easier than doing just a Verkal transition, right? 
* I think it's maybe like it's definitely much less hard than doing the two transition separately, but it's still like more work than doing one of those transitions, right? So we're not going to like save time by going, I think realistically by going straight into state expiry. So the question is just how much ah, do we value feeling like we have the the state problem completely solved versus being okay with this kind of kind of equilibriwhere we, you know, rely a bit on proposer builder separation and the portal network and some ner, some smaller ner of state holding nodes and all of those kinds of things. Does doing together mean we don't need, no, you still need address space extension or contraction. If you, if you do state expiry and Verkal trace together. If you do if you want to do state expiry, you need to fix the solve the address space problem at that time regardless of what format you do it in, Right?
* So if we want to do a state expiry now, then basically we have to just like bite the bullet on one of the two address Space solutions and commit to biting that bullet like basically literally now so that developers can start preparing for it. 

**Tim**
* Got it. And so guess I'm trying to understand. You said the middle ground is the worst.  I'm trying to understand why. Why would doing them together actually be like, what is the like? So guess we wouldn't need we wouldn't need the live transition by doing them together, which simplifies it. Right? From what I understand of the of the the work that's been done on verkal trees so far, it seems like we're actually doing okay with regards to like designing your life transition and like improving on that. So we don't know how far along we are, but, you know, definitely more than zero mean. 

**Vitalik**
* Yeah, right. But like we're doing okay. But just as a fraction of complexity of the entire Verbling project, it's surprisingly high. Right, right. 

**Tim**
* Yeah, . But it's like, guess we've already sort of accepted the bite that bullet and go down that path versus address Space extension is basically in the same spot. It was like two years ago.  Right. 

**Vitalik**
* That's fair. Yeah. I just want make sure. 

**Tim**
* Yeah, that's actually the case. Yeah. 

**Vitalik**
* Yeah. Guess one of the variables there that I don't know is like what percent of the cost is sunk. Like are we talking about 80% of the work being done or are we talking about like 45%, somewhere in between, something even lower? 

**Tim**
* Yeah. Guilla, do you want to maybe walk us through? I know we covered this a couple a couple calls ago, but do you want to maybe sort of rehash where we're at with Verkal and specifically the transition? 

**Guillaume**
* Sure. Yeah. Well, I mean, okay, the problem is always that there's exactly what just happened when some design people agree on the design and then people just start paying attention and come up with a new design. but, my, I mean, the way I see it, which is really just. Yeah, I'm speaking for myself here. we have like the, the implementation of Verkal tree in 2 clients, two and counting. There's a Ethereum js also that has made some progress, and I don't exactly know where Besu is exactly these days, but  they also started working on it, regarding the transition.
* So  we at some point there was, there was an agreement on the overlay method. This has been implemented. This has been tested. We have numbers. It looks like it's at least a workable solution. We are still discussing Pre-image distribution. And there's some there's been some back and forth about some details of the of the transition. Like should we keep, should we keep the frozen or should we keep writing to it? I mean, this, this is a discussion for another time. but Is it completely done? No, this is definitely more than 50% done.
*  This is, I would say 90% done. Of course, there's the question of, like I said, pre-image distribution. so I think at this point it's, yeah, there's got to be a good reason to , to change the transition method. but yeah, like you said, last 10% is 19%, 90% of the work, obviously. And that's quite true. Although, yeah, I think we're closer than that. but yeah, I mean, okay, like I said, some people will disagree for sure. I think we have a pretty clear path and now it's just about know implementing the last few details and, and getting people to try it out. 

**Tim**
* Got it. Thank you. And I assume just to be. Clear as well. I'm not aware of anyone who's worked on like address space extension or compression like significantly in the past year or two. But does anyone know of some? Yeah. 

**Vitalik**
* I mean, one thing I think I want to stress is that it might be worth revisiting in the just for kind of future compatibility reasons in the context of ELF there may well be decisions that we can make with ELF while ELF is not yet released that might make it significantly easier for us to do address space things in the future. 

**Tim**
* Andrew. 

**Andrew**
* Yeah. Just wanted to note that we don't have any to make any decision now. But I think  like I don't agree with Guilla's argnt that the workflow trace is mostly done. So like. Like how I heard it. Then we should ship it. But we should ship what? What strategically makes sense, right? So we need to think about like what we do strategically about state expiry and based on that we like that might shape how we ship Verkal and that's all right. 

**Tim**
* That's right. And yeah, I think that that makes sense, like trying to and I guess it's maybe just sharing the like, mental journey that the, the Verkal people have have been through and like how, how Verkal. Yeah. Fits in those parts of the roadmap and obviously like the if the explicit asstion is like we just put state expiry on hold for a long time because we rely on basically on the builders to provide the state and whatnot.  

**Tim**
* Maybe it's just worth making that a bit more explicit.  And, sorry, Josh, let me just read your question. Right? Yeah. So how much extra value do we get by shipping state expiry at the same time rather than only getting Verkal ASAP?  Yeah. I don't know if anyone has thoughts on that. And I guess maybe one last question for Guilla, Democrat and folks, what's the best place for people to just chat about stateless and Verkal on like a more regular basis? There's there's a Verkal tri migration channel on discord. Is that the main spot that people should follow? 

**Vitalik**
* I think there are state expiry and address space extension channels somewhere in there too, right? 

**Tim**
* There's a space expiry channel that's a state expiry. It's pretty dead and yeah, there is. Do we still have the address? Space extension channel we write? Oh, yeah, we do. Okay. Okay. So those three. Yeah. Address space extension hasn't been used in over a year.  

**Vitalik**
* But yeah, I mean, I do think that there is value in just like putting a team to think about the address space issue because like it has a lot of future optionality value. And as I mentioned, like even if we never do state expiry, the, the whole like 80 bit address collision complexity thing is like a bit of a long term ticking time bomb that's worth starting to figure out and figure out how to diffuse. 

**Tim**
* Yes. If you're listening and you want to take this on, please reach out. And yeah, we can probably help set up a grant and put you in touch with the folks who looked at this in the past. And Andrew. You still have. Oh, yeah. 

**Guillanume**
* Sorry. I just wanted to finish answering your question. There's also a Verkal implementers call where we discussed this kind of stuff. The next one is next Tuesday, I think. so, yeah, that's, that's usually a topic we, we talk about the transition. 

**Tim**
* That's it. Andrew, did you want to add anything else? Anything else on this? Okay.  Yeah. Think this was good to bring up and get everyone a bit more context around where things are at.  Next up, Ethan, you wanted to share some updates on SSZ? 

# SSZ EIPs update [56.45](https://youtu.be/GkSjuiqqkKU?t=3407)

**Ethan (Nimbus)**
* SSZ has been standing still for a while, but could finally find some time to update it. from last time when we discussed it. We essentially had two different approaches one based on SSZ unions where each transaction type, so to say, has its own branch in the object and a normalized one where each transaction gets converted to a unified representation. so now what I did is essentially combine those two approaches into something called a partial container. So how this works is that essentially it behaves like the union when it comes to serialization. It is very close to it, a little bit different in the header, but the rest is exactly the same. But it also ensures that when there are common fields in the transactions, which there are a lot, for example, the amount is present in every transaction type so far. or like the destination, those common fields, they now Verkal is always at the same location in the tree with this new approach.
* So there can be holes now in this partial container. So if one transaction type doesn't use a certain field in the Merkle tree, it simply becomes a zero. And this ensures that we essentially get all the benefits of the union without requiring any, clients that verify Merkle proofs to update each time there is a new transaction type like they can just continue to keep the same verifier forever unless they start caring about the new fields. so yeah, that's the latest approach there. I have also extended the specifications for networking so with the previous approach, the transaction was only something that gets created as part of the execution payload. But with this latest specification you can also directly sign transactions and put them in the mempool and everywhere.
*
* **Tim**
* Because of this flexible container it is possible with. To test, mix and match your own fields. I have somewhere with a police car. Not it's not. It's not for me. It's somewhere else. so I have made sure that there is like, a little function that checks the invariants so that no new combinations are possible. So, for example, if you include a blob, then you also have to include the destination and you have to include the priority fee. So no new transaction types. but everything that's possible right now, with the exception of the Replayable legacy transaction is now also possible with transaction exact same feature set. yeah. So just want to raise some awareness there to check out the EIPS. I have put them in the PM issue on GitHub and would appreciate reviews. And also if there are any question as to typed transactions, channel on Discord is the one for questions. 

**Tim**
* Thanks.  Yeah. Anyone have any questions or comments? Want to bring up now? Okay. Well, yeah, thanks, Ethan, for the update. and then I think that was basically it. was there anything else anyone wanted to cover? If not, I'll just give a quick shout to Els. So the ELs team officially put out a blog post announcing the python spec for the eel this week. So the specs went live for a while, but I think now it's call it production ready. There's also a PR from Guilla about about the self-destruct removal that he opened and that you can contrast with the original. So that shows kind of a nice, yeah, a nice side by side implementation in both eels and in irregular.
* So if people want to use the right ships, you can and you can even link to it in your and the bot won't. the bot won't stop you. and similarly, so the yellow paper came up a bunch on Twitter in the past few weeks. People were linking to it. so, so I figured it was worth a quick update. But just as a heads up, the yellow paper hasn't been updated since Berlin. So if you look at it today, you basically see the Berlin spec. so, if someone wanted to update it and add support for London and Paris and all the the difficulty bomb forks in the meantime, there's the option of a grant for that. and we've linked this in the yellow paper repo and also are pointing people towards eels there as the up to date spec for main net. I don't know. Guru Did you want to add anything more around ELs? 

**Guruprasad Kamath**
* Oh, no, not much. You covered most of it. So, like, some new apps are welcome. Also, like some feedback on, like, how easy or smooth the process is. And yeah, we'd like to continue to work on like, solving any issues that people might encounter. So feedback very much appreciated. 

**Tim**
* Anything else before we wrap up? Okay, Well. 
* Thanks, everyone, and talk to you all. yeah. When? Whatever the next call is.


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

## Next Meeting
Sept 14, 2023, 14:00-15:30 UTC




