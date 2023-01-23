# Execution Layer Meeting #153
### Meeting Date/Time: January 19, 2023, 14:00-15:30 UTC
### Meeting Duration: 1 hour 
### [GitHub Agenda](https://github.com/ethereum/pm/issues/704)
### [Video of the meeting](https://youtu.be/hVeMHoUUZ30)
### Moderator: Tim Bieko
### Notes: Alen (Santhosh)


| Decision Item | Description                                                              | 
| ------------- | ------------------------------------------------------------------------ | 
| 153.1 | **Testing & devnets:** Barnabas, last week we deprecated DevNet2 and launched DevNet2. DevNet3 is currently active, and we have a landing page for it. I made a post in the chat. Everything appears to be very stable. I've now included all CL and EL teams, |
| 153.2 | **Cancun CFI:** We believe that when it comes to determining the overall scope of the fork and which EIPs the community wants, which one should be prioritised, those are all conversations that end up being a bit more all core dev on this call and where, different groups, want to express their preferences and are unsure how to engage with the process. As a result, we will begin using the Ethereum Magicians thread to learn about community preferences.|
| 153.3 | **Announcements** We have the first Shanghai Capella community call tomorrow at 15 UTC - e'll basically give a quick overview of the fork. tell people, yeah, tell people what's, what's in it, how it works, and then answer their questions.|
| 153.4 | **Announcements** The Ethereum Cat Herders team has created a survey called the [Ethereum Client Diversity Survey](https://docs.google.com/forms/d/e/1FAIpQLSdxWpN_kcZj4I_43vME2MOKHq3yD5_OFv8Lj-RO14537r1GLA/viewform). So, obviously, in the last year, we've expended a lot of effort on the CL side to improve client diversity following the merger. It's also critical that we improve on the EL side of things. So we'll reach out to node runners and operators to better understand which types they use, why they use them, and what we can do to improve diversity there. |

## Intro

[4.42](https://youtu.be/hVeMHoUUZ30?t=262)

**Tim Beiko**
* Okay, we should be live. good morning everyone. This is All Core Dev execution layer #153. Couple things to cover today. So first, obviously updates, for Shanghai. So testing dev nets. then there were some, updates on, the withdrawal route and, and, how, the withdrawals would be represented in terms of units, on the EL. 
* I'm pretty sure we got all of those details, agreed upon, but just wanna make sure we go over them. Then. there was this, interesting EIP around, announcing a deprecation for self-destruct, that's sort of covering. and then a couple more things. So last call, or two calls ago, we made the, no last call, sorry. We made a decision to remove, EOF from Shanghai itself. 
* It wasn't unclear if we wanted to make it cfid for, for Cancun already. some client teams had had signaled that yes, but we, we couldn't get everyone,  to agree. then I had a proposal for how we should actually go about organizing, the next upgrade and then a couple announcements and that will be it. but I guess to kick us off, I see Perry Barnabas, you're both on the call. Do either of you want to give an update on, Shanghai Dev Nets and where we're at there? 

## Shanghai Updates [5.54](https://youtu.be/hVeMHoUUZ30?t=354)

**Barnabas Busa**
* Yeah, sure. I'm not sure if you can hear me well. Yep,so last week we have, deprecated DevNet2 and launched DevNet2. DevNet3 is currently running, and, we have a starting page for it. I posted in the chat. Everything seems really stable. I've now, included all, CL and EL teams and everyone is able to use the gray instead of conversion, so that's very good. 
* Nice. another quick update. I would like to begin DevNet four next week, sometime midweek and, for, we would need all client teams, all CL client teams to have the BLS pools, implemented and working, so that each client team could actually post BLS update before Capella to their local pool and hopefully, gossip bit once Capella hits. 
* Nice. That would be this. And it would also be a larger test with about 500 or 600,000 validator. So we can actually test, diverse case scenario with 310 or 330,000 validators, key change before Capella. 

**Tim Beiko**
* Nice. 

**Danny**
* And on Devnet three, are we also sending exits as well to get those referrals coming through? Yes. 

**Barnabas Busa**
* Yep. Cool. it just takes a long time. I just fiGweired two exits, this morning, but, I'm using the main net, steps are the main net. the things on it and the main net setting are quite slow. 

**Danny**
* Okay. Gotcha. And in terms of like doing any of that manual testing, sometimes it's good to send exits and let them get fully exited and withdraw before doing a BLS change. cause that does a slightly different code path. 

**Barnabas Busa**
* Oh yeah. That, that  we done in previous devnet. Sorry. 

**Danny**
* All right, cool. Thank you. 

**Pari**
* Nice, thank you.And just from My, sorry. Yeah, so just to follow up with Barnabas updates, also had a shadow for earlier today. we used the same config, same, sorry, the same client versions and the same spec versions as we had on DevNet three. all client pairs were perfectly fine. the only one that I wasn't able to get working yet was, Argon, but purely cuz it didn't sync in time and we wanted to make sure we have an update for the call. 
* But I will try out Argon later on and give an update on that. We also tried the BLS changes there and I did trigger withdrawal both look good. We've also set up nodes to do a main not shadow fork. And the plan is to have made that shadow for on Monday. And yeah, we're gonna reuse the same config as we have this week. 
* So yeah, that's, I think the updates on the shadow fork site. And we,  I posted a message yesterday about, on the interop channel about delaying the public test net until after the shadow fork done so that we can focus on, bugs during the interop time and not focus on user support as mentioned by Paul. 

**Tim Beiko**
* Great. And just to, just to clarify, the shadow fork, today was on Gordy, right? 

**Pari**
* It was on Sepolia, yeah, Actually. 

## CL-EL withdrawals harmonization: using units of Gwei execution-apis#354 [10.20](https://youtu.be/hVeMHoUUZ30?t=620)

**Tim Beiko**
* Okay. Oh, interesting. Yeah. Nice. Any other testing or, development updates from the client teams? Okay. then I guess we already sort of touched on this app and when we briefly covered it, on this, on the CL call I believe. But, we made a change, in both, the execution APIs and on the withdrawal EIP to use Gwei as the unit of account for, withdrawals, to match the CL. 
* Alex had two PR to this. so PR 354 on the engine api 6325 on the EIP. it seems like our client teams have implemented this already. I don't know. Alex, do you maybe want to, is there anything to add beyond this? 

**Stokes**
* I don't know if there is, is a pretty simple change just to use units of Gwei and Yeah, I think all the clients, well, I know all of the clients have implemented the code and yeah, it sounds like it's even on, Testnet already. So I think we're pretty good here. There is, one other PR for like the, the deeper change to have withdrawal to be sort of full fsc. 
* But yeah, that's something people can look at, but I think should be a feature conversation. 

**Tim Beiko**
* Okay. And just to clarify, where did we land with the actual route? So we're using Gwei on the EL right now, but we're still encoding it with RLP or are we encoding just the withdrawal route with SSZ to match the CL route? 

**Stokes**
* Yeah, still using our ELP. So it's, we just changed the units of the amount. 

**Tim Beiko**
* Okay. got it. And my, my read was we don't want to do more than that because, of Shanghai being pretty much done. 

**Micah Zoltu**
* That doesn't align at all with what I remember from this CL call last week. I thought we were going to get some specs out so we had something more concrete to talk about today and then we're gonna make a change today. Cause there was a lot of disagreement last week, Right. 

**lightclient**
* Some specs for the way to way change, which they did do Specs for that and specs for,

**Danny**
* Yeah, it was to do specs for both.The conversation was heavily leaning towards gray, only my interpretation, but to at least like voice, based on the complexity of the SSC specs and people thinking about it a week. Yeah. I, my read is to not do it, but I'm, given, you know, the conversation of last week, but I am very open to hearing other people then input at this point. 

**Tim Beiko**
* Yeah, and Alex actually had a draft PR for this as well. I'm not sure how final it is. I just posted it in the chat. so I guess, does anyone on like the EL side feel strongly we should go that route and, and make the change to SSE? 

**Tukasz Rozmej**
* I have a question. Are we talking only about changing the route or anything else too? 

**Tim Beiko**
* I only the route I believe,Yes. 

**Tukasz Rozmej**
* Okay. So we in Nethermind were experimenting with generating the route and I think Mark had success today with actually, being able to, generate the route from our, SSE library correctly. 

**Marek Moraczynski**
* Yeah. So, we get the same results like Ethereumjs and some, consensus reference test. So we are a bit more confident about our library now than we were, week before. But still, if we want to change something, I would change only withdrawals through and do not douch, transaction route received through. yeah. 

**Tim Beiko**
* Yeah, I think everyone was pretty much on the same page. Should not change anything beyond the withdrawals route if we were to change anything. and even that, I think there was some concerns to make the change kind of this late in the process. but on the other hand, if we don't, okay. 
* Most people, sorry Micah. yeah, on the other hand,if we don't use SSE right now, then we're gonna have to change it, in the future. but realistically everything else is also gonna change. Yeah. 

**Gajinder**
* So Basically ethereumjs sorry, speaking for ethereumjs, we, are ready to move to SSE route for withdraw. 

**Tim Beiko**
* So I guess, yeah, there's comments in the chat about like not changing anything unless this is like a safety issue. I would also lean towards like making as few changes as possible now unless someone like really, really wants to make this change. and otherwise we can move to SSZ more things in future upgrades. 

**Micah Zoltu**
* So I don't think Mars is here, but I do feel last week, I believe, and he may have changed his mind since then, I might have misinterpreted. his position was if we change to Gwei, we should also do the SSZ route. We should not do just the Gwei change. And he seemed to feel pretty strongly that we do both or neither. 

**lightclient**
* I asked him about this and he said that because the majority of other clients felt that they didn't, did not want to do SSZ, but they still wanted toque that he was okay with it. Hopefully I'm not putting words in his mouth, but this is what he sent to me when I asked him. 

**Micah Zoltu**
* That's why I merged the PR to execution APIs So I will once again, stage my pointless objection that I really think that we, it feels like this change. We are not thinking about the long term health of Ethereum. We're thinking about how do we, you know, do what the public wants today. 
* And I feel like as All core devs, our job is to think about the long-term health of Ethereum and not to capitulate to equals, you know, logging and demands for I need withdrawals this week. I think that doing the right thing means not adding technical debt that we know is gonna be technical debt in like six months. 
* And if Cancun we switch to SSZ routes, that means we've got literally one fort where we have to deal with wherever the fact that we had withdrawal roots as rlp and that's gonna live with us till the end of time. And the cost of fixing that is, you know, maybe delay withdrawals by a week or two. 
* And that feels like a very obvious win to me. If the thing we care about is the long term health of Ethereum we care about just, you know, giving investors what they want, then sure give them withdrawals right now. But I really don't think that's what we should be optimizing for. 

**Danny**
* And I agree with the sentiment, but I also, I'm not confident that we know what we want the design to be in Cancun. I think that we generally think we should be moving the transactions route to SSZ, but we have not done the diligence there. So I don't even know, I could not confidently say that that's actually what we're gonna do because there is an alternative. 
* The alternative is that we hoist the ROP route into the consensus layer to handle, the like client use case that we want here. And without doing the transactions do diligence. I can't say for sure that's what we're gonna end up landing on cuz there's a lot of things, there's potentially applications that will break on chain. 
* There's lots of pooling that we might break. and, and so because we can't do that, I don't, I feel like landing one way or the other on withdrawals is, you know, assuming that we want these things to be unified and in a similar operate in a similar manner, I'm not confident that we're gonna land on, one of the other in camps. 

**Andrew Ashikhmin**
* I think, kind of slightly implied, inclined to fixing or like switching to SSZ to  in Cancun, I think, currently, withdrawal route is not terribly exposed. it's, would, it's much more like the, the amount unit is much more exposed to tools and withdrawal withdrawals through. So  even if, for some historical blocks, it uses a different algorithm.
* I don't think it's  too, too bad a thing. It's some kind of minor technical issue to my mind. 

**Micah Zoltu**
* So, to comment on, Danny's comment, I thought, and maybe I'm misremembering or maybe I'm projecting, I thought there was agreement a while back that we were going to, like everybody on the EL team kind of agreed that SSZ EL blocks eventually. And it was just a question of when, did I misinterpret that? Is that, or did that change? 

**Danny**
* That could certainly have been stated. but I,two weeks ago when thinking about, you know, the pressure to change the transactions or, now it definitely allied the fact that, there are changes there that will have impact on users that we have not done the the diligence to understand yet. 
* And so even if that is like the agreement, there's still not done the, we've still not done the process of like, Hey, what is this break? and really made sure that it's done if it's,certainly to be done in a proper way. In appropriate way. So yeah, I, can't speak to exactly, I think there's a general sentiment that that's the direction we wanna move in because it's a better commitment. but changing things those costs, as you know.

**Tomasz Stanczak**
* So I feel that there was a sentiment towards SSZ, but they go towards the SSZ much larger change than simply, the one that we are discussing now. So while if you're talking Mike about the introduction of technical debt, I think that our review of RLP versus SSZ will be so significant when we look at it to clean it. 
* And the process of thinking was so significant that, this technical debt that you're referring here to will be simply a small thing comparing to the amount of changes. So on the uncertainty now in the delay, like delay itself for the sake of better long-term network would be very convincing. But this particular change, the SSZ RP, I think would be a larger process of thinking of designing. And I would like the designers to rush now thinking of how to solve the SSZ RP in this particular place. 
* Like the researchers or all of us, would prefer us to look at it holistically, and give ourselves a proper time starting with this conversation in the process of preparation for Cancun. 

**Micah Zoltu**
* For, both, this is for both Thomas and and Danny.  that those deposition you Gweiys both hold is assuming we only we only do SSC application of the withdrawal route in Shanghai, not transactions or receipts, is that correct? 

**Danny**
* Correct. But my point being is, the doing of the withdrawals route is premised upon kind of that being the common solution to handling these couple of routes. and we don't know precisely how we will handle the other route, even though we have an intention on how we will handle the other route. so doing them together seems appropriate to me. 

**Micah Zoltu**
* I guess I assumed that the consensus teams had already kind of thought about this a lot and solved it and the EL would would follow, but maybe that's from the sound of it, maybe that's not the case and we want to rethink just how we're Doing. 

**Danny**
* It's less about, yeah, it's less about selling to me, it's more about, you know, one, how do you handle the transition two, you know, the technical things that rely upon this transactions group. and you know, when we disable something like self-destruct, we spend some time fiGweiring out what's gonna break and try to make a, some sort of cost analysis on moving forward with it. And we have not done that on the transactions route. 

**Micah Zoltu**
* Yeah. So I agree with all that. I agree that the transaction route requires, significant thought. Same with the receipt route, because they already exist. They're, they have the past. I think the thing that I'm confused on with your, your argument,I think I'm just missing something is withdrawals route isn't out there, so there's no backwards credibility in EL yet. And so if we just do what the CL does, like, are you worried that, that if we did what the CL does today in, in EL and we got that out in Shanghai, are you worried that we later want to change how withdrawal route are encoded in the EL and the CL? 

**Danny**
* I'm worried that we then have two different ways that doesn't, that doesn't fix kind of one of the core problems that we're talking about here, which is how light clients insert execution, payload headers into the execution layer. and so then although we do kind of patch the withdrawals route, if we never change the transaction route, then we'd also have to, hoist the transactions RP route into the slayer. 
* And so now we have kind of like a very mismatch solution on doing that. Like it doesn't necessarily get us, you know, the first step on the like common solution. and so I'm hesitant to say it's like the appropriate path at this point. 

**Micah Zoltu**
* So your hypothesis is that there is a potential future where we do RLP in BCL instead of SSC in the EL and that's a, so Yes, and there's, you can either compute it in the CL or the engine API could return that value. 

**Danny**
* But either way then you have kind of like the mismatch handling of roots, which is not the end of the world. but then you have also SSZ in the execution layer and RLP in the execution layer depending on which route you're looking at. And I don't know, so I kind of think fix this in one swoop in a unified design and handle the damage at that point. 

**Micah Zoltu**
* So I think your arGweiment, I think is compelling if, we start with the assumption that there's not consensus that we're moving the EL to SSZ. And it sounds like that's where you're coming from is that you're not super sure the EL is going to move to SSZ. 

**Danny**
* Yes. I do not understand what will break when we do sure when actions migration. So I couldn't throw my hat in the ring one way or the other until I understand that. 

**Micah Zoltu**
* Right. I think I was coming from the assumption that, we had already agreed to do SSZ in the EL, but if that is not the case, then I do find your arGweiment compelling. 

**Tim Beiko**
* Okay. And there's a bunch of support in the chat for like moving things all at the same time to SSZ. and you know, earlier we were saying we'd rather not make these changes to Shanghai unless they're, they're like quite critical. so I think it makes sense to just move forward, with RRPL for now keeping the Gwei as a unit and we can discuss SSZ, all the things, for Shanghai or sorry for Cancun coordinator. 
* Cause I know like years ago when we discussed this, there were talks about putting SSZ on the peer to peer A first because, this way you still have the previous versions running in parallel. There's less of a risk than switching all the consensus stuff. so I think it's worth having that conversation. 
* But, yeah, for a later fork and going forward with RRP for first Shanghai, does anyone strongly disagree with that? and Lightclient has a, has a comment we should make sure application developers understand this though. I'll show our community call tomorrow 15 UTC where we can start, talking about this stuff with, the broader community, yeah, Andrew, 

**Andrew Ashikhmin**
* But is withdrawal through to exposed, like especially the ROP withdrawal through to exposed to at all to dev developers. 

**lightclient**
* It's in the block hash. 

**Andrew Ashikhmin**
* Yeah, but I mean still they, they contact us, they, the withdrawal route itself

**lightclient**
* They can create a proof to the withdrawals route, which I'm guessing that's they'll want to do so that they can verify certain withdrawal systems are working. 

**Danny**
* Yeah, I would suspect that is the case. you know, for example, one of some of the liquid staking derivatives might use that route to fiGweire out distribution of payouts or something like that. but they'll also be warned heavily that things might change.I think most people will generally understand that hader commitments are gonna likely change, but yeah, 

**Micah Zoltu**
* Correct me if I'm wrong, but the withdrawal route has to be exposed because if it's not, then no one can validate a block. 

**Danny**
* Like it's part of the block cutter and it needs to be known in Order to Yeah, I think is also, is it exposed within the EVM is the question too, which Oh, Is exposed to meeting EVM. Sorry. Yeah. Yeah. Cool. It has to be by virtue of the black hash being in there, so. Right. 

**Tim Beiko**
* Okay. And Etan said, in the chat, he's gonna volunteer on to draft a full, SSZ EIP for Cancun. yeah. Cool. okay. Next up on the agenda. oh, and I guess, yeah, just to close this out property. So last call we had discussed, Etan actually is PR about, had adding the hexary trie roots for lists in ExecutionPayloadHeader. Paneled headers is obviously, not gonna happen because we're using Gwei as a unit. so I just posted out on the agenda. but yeah, just.People are on the same page there. 

## EIP-6049: Deprecate SELFDESTRUCT [29.06](https://youtu.be/hVeMHoUUZ30?t=1746)

**Tim Beiko**
* Okay. Next up, self-destruct. So, we've discussed on this call many time for many years, deactivating, self-destruct, through many different ways. we still haven't landed on an actual technical solution that everyone is happy with. but somebody, wrote an EIP to basically announce that we would deprecate self-destruct. so the EIP it's, 6049. put it in the chat here. 
* It doesn't make any code changes, so it doesn't require clients to, to write any change in behavior. but it's more like a deprecation announcement. and so I was curious whether people thought we should include this in Shanghai. 
* So basically, you know, saying that as of Shanghai self-destruct is deprecated, again, the on Hanshan code would not change, but you could imagine, this being a way to like alert the ecosystem of it and, you know, programming languages can start to give, you know, deprecation warnings when this happens. things like ethers scan or infer our alchemy, you can start, also warning users that like, hey, you know, the self destruct, is is now deprecated and, and and will be going away or, or at the very east changing in behavior sometime soon. so yeah, curious what people think of this. I saw Guillaume and Vank both raised their hands, so, Guillaume you wanna go first? Oh, still. Oh, I think, can you hear me? 

**Guillaume**
* Yeah, we can now. okay, cool. yeah, I don't quite, I mean, yes, there's already, an EIP 4758 that is, actually doing the modification. What I don't understand about this EIP  is, is, why would that be part of Shanghai? if there's no code change, oh, so we just announcement. 

**Tim Beiko**
* Yes, that's correct. But people pay attention. A lot of people only pay attention to the hard fork blog post and then stop paying attention until there's an under one of them. 
* And if. we, if we include, so for example, say we include like, 4758, a lot of people will be like, wow, this is the first time I ever hear that self-destruct is going away. And, you know, they'll be very mad about it. So this is kind of a way to let people know that. And, and, and the, the EIP itself doesn't say it'll go away necessarily, but that it might also have like  a significant, behavior change. yeah.

**Guillaume**
* Okay. Yeah. if is just about a blog post announcement, I, okay, fine. Yeah. You're saying people can, will only watch if there's a hard fork announcement. 

**Tim Beiko**
* Yeah. And then, and I do think that it makes it easier for, you know, like, say, gets to yeah, log a warning when it happens for solidity, for viper to log a warning when you compile a contract with self-destruct, right? It's like, something that all these, these tools and, and developers can like point to say, you know, we're referring to this and this is why we're giving you like this deprecation warning. Yeah. 

**Dankrad Feist**
* Yeah, so I strongly agree with, like, yeah, finalizing that EIP and marking it as final or whatever that is the process. I, same thing as Gwei, I don't think it needs to be included any particular hard forks. So ultimately I think like what you're saying is just that we want to  include it in the hard fork blog post, which I think is, probably a good idea as well. 
* But I don't think like it's really, it's associated with any hard fork, nice. And yeah, what I want to say, like some, some people like criticize the EIP because they were like, oh, but they are alternatives that don't deactivate it at all. 
* But yeah, I think like the in any case, the change of behavior is significant enough that one, it doesn't make sense for anyone to use self destruct now. And probably it also won't make sense to start using it after others. It's basically, it's just a way to like somehow do something for legacy applications. So I still think like with any, any option that's on the table, it makes sense to, first market as applicated. 

**Tim Beiko**
* Thank you. Thomas. 

**Tomasz Stanczak**
* Hi. And strong support of the EIP creative way of making sure that we have a clear indication for our tool builders to deprecate to Warren. I think it's been discussed and generally agreed on that either change or removal of self disconstruct would happen, and showing it in a, in an official way, might improve the way we communicate such drastic changes for the future. in the past, I think that communication was, one thing that the users are complaining about, that the EIPs were promoted, but when the change was happening, creating this two stage process, seems to be a good improvement. 

**Tim Beiko**
* Okay. Does anyone disagree with this? And there was, yeah, there was one argument against it. Dan you sort of hit on it. I don't know if it was in the all core dev channel directly, but people saying basically there might be, yeah, there was a, another proposal like EIP 6190 that's a vertical compatible self-destruct that might not require any significant changes to it or, yeah,I don't know if anyone has a strong opinion about, 

**Dankrad Feist**
* Well, that's actually not true. I mean, it's still a huge change to self track that it would not the contract storage database, we just hope somehow that all the contracts, that currently use self construct in some ways aren't affected by that, but it has actually made a change in behavior anyway. 

**Tim Beiko**
* Okay. Then I think, yeah, then I think I'm convinced, cuz the EIP 6049 doesn't say it's necessarily gonna go away, but that there'll be potentially future behavior changes. So I think that's, that's still included, so, okay. 

**Micah Zoltu**
* Worst case scenario. We can just reenable it Later. 

**Tim Beiko**
* Yeah, right. It's better to deprecate it and deprecates than to like, yeah, yeah. Tell people too late. okay. 
* I can add, so I guess the two places the, like I would edit is like the Shanghai spec, with the other EIP that are listed. So as people kind of click through those, they'll see this. and then, obviously any announcement we make of, of the upgrade. yeah. Any other thoughts, comments on this? 


## EOF updates [37.00](https://youtu.be/hVeMHoUUZ30?t=2220)
**Tim Beiko**
* Okay. so that was it for Shanghai. okay. There was another thing, we sort of discussed last call and, and didn't quite, get the resolution on. so we agreed to move EOF out of, Shanghai. and then I put up a PR to, to remove it from the spec. and, Andrew from Aragon, was asking you if we should move it to CFI for Cancun. 
* Ethereum JS felt the same and, and I believe Besu as well on the chat. but I couldn't quite get like a plus one from everyone. So does anyone object if we make the EOF EIPs that were previously included in Shanghai? CFI for Cancun doesn't mean we have to do them, but it just kind of adds them to the list. yeah. Okay. 
* So I'll take this as no objections. I'll do this PR right after this call. and then, okay. 

## Cancun CFI [37.12](https://youtu.be/hVeMHoUUZ30?t=2232)
**Tim Beiko**
* Talking about Cancun, I put up a thread on Eth Magicians about this, a few days ago. But basically I think, when we were doing Shanghai, when we were doing the planning process for Shanghai, there was a lot of people who, who shared a bunch of feedback about how we should consider different, stakeholder groups in the community, what's like the right role for all core devs, what type of conversations and decisions should happen here? 
* And, basically, you know, how do, how do we make this all work? I think one thing that that sort of comes up, a lot is, the, the decision around like relative prioritization of EIPs and like higher level planning. So, we do a pretty good job on the call of like discussing individual EIPs and like their pros and cons and their, their technical details.
* But I think when it comes time to like figuring out what's the overall scope of the fork and which that look like, you know, between two EIPs that the community wants, which one should be, should be prioritized, those are all conversations that like end up being a bit more all core dev on this call and where, different groups, want to express their preferences and, and are not too sure how to engage with the process. 
* I think one thing I would like to try out to, to kind of address this is that as we plan these upgrades, we also open a thread on Eth magicians, to kind of discuss what, what the upgrades priorities and scope should look like. and then we can, we can obviously, because it threads on Eth Magician, anyone is, is welcome to to contribute to it and we can kind of discuss what comes out of that thread on this call as we're planning the upgrade. * But, and, and this is kind of a way to avoid every single project, having to send a representative here and, you know, having, having like the, the, the short time on this call kind of taken up by a bunch of people who come and, and, and share like their, their one preference for, for a fork. we discussed.
* I think Micah, you actually had proposed this a long time ago as like a Discord channel that would like a temporary Discord channel that would appear when like we're planning your fork about that. 
* And I think Eth magicians is like a bit better of a platform for this in that like it's a bit of a slower pace and people can put like more thoughtful, updates there. it's also like a nicer record of like how the decision or like what inputs kind of came into the decision. yeah, so I guess I, how do people know where to go? 
* I guess we would mention it on this call can link it on the agenda. yeah, basically the same way that people know where to go to propose an EIP p for a hard fork.
* I think we can, we can link it at a bunch of places is my, my short answer there. yeah, I guess any thoughts, comments, about this? 
* Okay. If there's no opposition, I think what I would do is I would try it for Cancun. again, I can open this like today as we're starting to, to kind of discuss it, so people can, can start chiming in there. and yeah, we, we can see how it goes and, and whether we want to keep doing it, for future forks. That's pretty much all we had on the agenda except a couple announcements. 
* Was there anything else anyone wanted to chat about that we didn't cover? Oh, Mike, I don't know if you came off mute or not. Okay. Doesn't seem like it. okay then, two quick announcement. 

## Announcements: Shanghai/Capella Community Call #1 #708 [41.17](https://youtu.be/hVeMHoUUZ30?t=2477)
**Tim Beiko**
* First, we have the first Shanghai Capella community call tomorrow at 15 utc. so people listening to this, and then if folks from some client teams want to show up, we'll basically give a quick overview of the fork. tell people, yeah, tell people what's, what's in it, how it works, and then answer their questions. yeah, so, people always enjoy when there's client teams who can answer their very specific client questions. 
* Yeah, so we'll have that second, Pooja and the Ethereum Cat Herders team have put together a survey, survey around, Ethereum Client Diversity Survey. so obviously in the past year we've spent a lot of efforts, on the CL side trying to improve client diversity there, post merge. It's also quite important that we improve, the EL side of things. so we're gonna reach out to node runners and, and operators to better understand kind of which kind they use, why they use them and, and what are things we can do to improve diversity there. and lastly, the K C G ceremony is happening. Trent, do you wanna give a quick update on that? 

**Trent**
* Sure, yeah, it's been mentioned a few times on previous calls. it's a prerequisite for proto Dan charting. I won't go too deep into what it actually is, but just if you're interested in learning more, go to ceremony.ethereum.org. It's, yeah, prerequisite for Dan Charting and Pro Dan Charting and everyone is encouraged to participate. It's open for the next two months.
* We have a grant round available if you want to dig in a little bit deeper, write your own implementation. So, encourage everybody to go check that out and contribute cuz it's an important building block for, future Ethereum infrastructure. Thanks. 

**Tim Beiko**
* Thank you. 

**Micah Zoltu**
* If, if the queue stays full for the entire two months, is there a plan to extend it? 

**Trent**
* So it's definitely been saturated these first few days. It's dropped a little bit, which is a good it's sign. eventually we will have to end the ceremony and choose a final output. basically this first two month period is open contribution, so anybody can just roll up, sit in the lobby as long as they'd like. 
* But we will at some point switch to special contribution, which is bespoke implementations, special ENT generation, things like that. And then we plan to revert to another open contribution period for basically as long as we can until, relatively close to Cancun or, or whatever network upgrade for it 4844 scheduled for. 
* But at a certain point, yes, even if the queue is full, even if it gets saturated even more than it is now, we will have to, end the ceremony at a certain point and that may happen when there are still people in the queue. So if you're worried about this, I'd recommend tracking it, trying to get in at, early, as early as possible and getting that out of the way if you're, if you wanna make sure you have the most trustless contribution and that you actually are included. 

**Tim Beiko**
* Sweet. And I guess one more small thing, we mentioned this on discord, but just as a heads up, there's no CL call next week and we'll have an EL call two weeks from now. yeah, anything else before we close? Okay, well thank you very much everyone, and talk to you all in two weeks. 
* Thank you. Take care. Bye. Thank you. Bye. Thank you. Bye bye. 

-----------------------


### Attendees
* Tim Beiko
* Danny Ryan
* Pooja Ranjan
* Micah Zoltu
* Jiri Peinlich
* Marius Van Der Wijden
* Potuz
* Evan Van Ness
* Moody
* Tynes
* Lightclient
* Alex Beregszaszi
* Marek Moraczyński
* Justin Florentine
* Alexey
* Ben Edgington
* Terence
* Lion Dapplion
* Mrabino1
* Barnabas Busa
* Łukasz Rozmej
* Péter Szilágyi
* Danno Ferrin
* Andrew Ashikhmin
* Hdrewes
* Crypdough.eth
* Pari
* Ameziane Hamlat
* Liam Horne
* Georgios Konstantopoulos
* Mehdi Aouadi
* Mikhail Kalinin
* Carlbeek
* Bob Summerwill
* Jesse Pollak
* Stefan Bratanov
* Sara Reynolds
* Phil Ngo
* Caspar Schwarz-Schilling
* Ahmad Bitar
* Marcin Sobczak
* Kasey Kirkham
* Sean Anderson
* Saulius Grigaitis
* Stokes
* Ruben
* George Kadianakis
* Dankrad Feist
* Andrei Maiboroda
* Protolambda
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
* Vitalik
* Tomasz K. Stanczak
* Matt Nelson
* Josh
* Gary Schulte
* Rory Arredondo

-------------------------------------

## Next Meeting
February 2, 2023, 14:00 UTC

 
