# Consensus Layer Call 105

### Meeting Date/Time: Thursday 2023/2/23 at 14:00 UTC
### Meeting Duration: 45 minutes  
### [GitHub Agenda](https://github.com/ethereum/pm/issues/747) 
### [Audio/Video of the meeting](https://youtu.be/Xc6Ss-m_nlE) 
### Moderator: Alex Stokes
### Notes: Alen (Santhosh)

## Summary <!-- omit in toc -->
Summary | Description
-|-
105.1  |**Client releases:** Consensus spec release 1.3.0-rc5 is out.
105.2  |**Client releases:** Round-robin call-out for Capella (and Shanghai) readiness: all client teams on call will have a release out this week or early next week.
105.3  |**Client releases:** EF Blog post should be up Tuesday or Wednesday next week.
105.4  |**Client releases:** Pari, there will be one more mainnet shadow fork once all releases are out.
105.5  |**Client releases:** Bug bounty for Shanghai–Capella specific issues have been boosted to 2x. Up to $0.5m now: [bounty.ethereum.org](https://ethereum.org/en/bug-bounty/).
105.6  |**Client releases:** MEV-boost community call upcoming, mainly to discuss Capella readiness. March 30th at 16:00 UTC.
105.7  |**Deneb:** Discussion of [Add corresponding proofs to BlobsBundleV1](https://github.com/ethereum/execution-apis/pull/392): add proofs to the get-blobs engine API. EIP [6610](https://github.com/ethereum/EIPs/pull/6610) means that the execution layer now has the proofs, so it is easy to pass them to the consensus layer. Consensus layer doesn’t need to generate any proofs or commitments, just verify what it receives from the execution client.
105.8  |**Deneb:** KZG library startup times. Some can be slow to start and mean that every test can take 2 seconds. To be addressed in the KZG library. Not a problem in normal running, but a big problem for testing. [Dankrad] Transforming the setup data to Lagrange form is what takes most of the time. We could change the initialisation file to store in Lagrange form rather than compressed point form. This should reduce the startup time to milliseconds.
105.9  |**Deneb:** SSZ discussions remain ongoing. How much of the changes do we want to bring forward into Deneb? [Tim] Monday’s SSZ breakout call decided to wait until All Core Devs makes a decision on this - there are lots of factors to consider. Different client teams are in different places on this.
105.10 |**Research, spec, etc:** [Naming for the post-Deneb upgrade](https://ethereum-magicians.org/t/e-star-name-for-consensus-layer-upgrade-after-deneb/13248). “Electra” seems popular. Join the EthMagicians’ discussion to give input.

**Tim Beiko**
* We are live. 

## Capella [8.20](https://youtu.be/Xc6Ss-m_nlE?t=509)
**Alex Stokes**
* Great. Hey everyone. I'll be taking over for day today. This is consensus layer call 105. the agenda doesn't look too packed, which is good. let's see. There's one in the chats for people on the call. It's issue 747 on the PM repo. So let's see here. What have we got today? I think I'll go a little out of order here. and first let's talk about client releases. the first thing is that we have, consensus specs release, the latest one here is version one 1.3.0-rc5. 
* And I think the thing this does is we set the actual Capella for epoch that, we've agreed to for main net and there was some stuff for and we'll get that in a bit. yeah, do any of the client teams wanna go around and just, speak to their readiness? I think some people have releases. Maybe everyone has releases out now. 

**Terence**
* Prism will release early next week. That's the plan. 

**Alex Stokes**
* Great, Thank you. Should be done, in a few hours. 

**Marek**
* Certainly by tomorrow, Nethermind will be released today. 

**Marius**
* Geth has released yesterday or the day before, name Early next week.

**Sean**
* So we released for Lighthouse, but we're releasing, a hot fix for that release tomorrow I think. 

**Alex Stokes**
* Okay, great. So I think that was everyone on the call. I can't see the fullest, but yeah, so if people either have released or they will in the next couple days, it sounds like. So if you're listening, be aware, you know, follow the usual distribution channels and update your notes. 

**Tim Beiko**
* Yeah, we should have the blog post. We should have the blog post up, hopefully Tuesday-ish, Wednesday at the latest for people listening. 

**Alex Stokes**
* Okay, great. And that gives us a bit more than two weeks, something like that. So yeah, should be plenty of time. And, everyone keep an eye out for the blog post and yeah, nice work everyone. So that's it for, I mean, that might be a for Capella.
* Is there anything else anyone wants to discuss about Capella at the moment? then we'll move on to 4844 up stuff. 

**Pari**
* Just one thing, we started syncing some mainnet nodes and once all the releases are done, we'd have a main net shadow fog and I guess that would be the last, attempt of the transition publicly before we hit it on main net. 

**Alex Stokes**
* Okay, great. Thanks Perry. so one more mainnet shadow fork, with the final releases. That'll be nice just to, you know, give us one more go at things, not expecting any issues, but that'll be good to confirm. And yeah, any other Capella things while we're here? 

**Tim Beiko**
* Frederick, do you wanna mention the bug bounty? 

**Fredrik**
* Yeah, sure. sorry, can you hear me now? 

**Tim Beiko**
* Yes. 

**Alex Stokes**
* Yep, we can hear you. Okay. 

**Fredrik**
* Okay, cool. Yeah, sorry, I was muted. Yeah, so the bug bounty for Shanghai–Capella specific issues have been boosted to 2x. So there's a two x multiplier for any vulnerabilities that affects the, Capella code parts. so yeah, go ahead  looking for more vulnerabilities, as the max bound to pay out for Capella specific issues is now up to half million dollars. 

**Tim Beiko**
* Is there a tweet about this that we can share? 

**Fredrik**
* I'm still waiting for the, let's see, bounty, I don't think the banner has come live yet. No, it hasn't. So the, the banner will be updated on the bounty dotter.org, soon. And then I will make, a post about it on, or a tweet about it. 

**Alex Stokes**
* Okay, great. Yeah, that's exciting. And, anyone listening get to bug hunting. so Terrence, thank you for bringing up the MEV Boost community call. I'll just plug this while we're here. the main thing will be to discuss Capella readiness, for me, boost operators, relays, builders, you know, that, that whole cast and crew. the next call for this will be March 30th, at 1600 utc. So 4:00 PM And, yeah, maybe I'll just toss this link in here. * Let me grab that. and yeah, please attend if you can, especially if you're listening and you operate a relay builder, something like this. Okay, I think we can move on to dab now. there's not too much on the agenda. The one thing is, is PR and Add corresponding proofs to BlobsBundleV1 execution-apis#392, is Gajinder on the call? 

## Add corresponding proofs to BlobsBundleV1 execution-apis#392 [14.21](https://youtu.be/Xc6Ss-m_nlE?t=861)
**Gajinder**
* Yep. Hi. 

**Alex Stokes**
* Okay, do you wanna give us a little summary about this? So it looks like we want to at least it suggests adding proofs, to the Skip blobs engine api. 

**Gajinder**
* Right. So, we basically, bobs now decoupled, the network wrapper, for the blob transaction for EL has, will now also include blobs and there is a, PR for that, on EIP-6610. so now since the EL has the proofs, it can just, pass on the proofs to the CL using get blocks bundle. And, CL just needs to verify to batch verify whether that case is GS blobs and proofs, they all match. And basically then the block production can follow the normal part. 

**Alex Stokes**
* Okay. So this is just saying because we now have the proofs, you know, available with the EL, we can just pass 'em along to the engine API to the CL and do the verification there, at a high level. That sounds reasonable. has anyone had else had a chance to look at this PR. I haven't been able to look at depth yet. 
* Does anyone have a rough number? Does the compute proof take? I I guess this is mainly for optimization. Yeah, I mean it should be Something like 14 milliseconds or so, But if I'm looking at this correctly, this is work that would already need to be done, right? This is just kind of moving around where it happens. So it's not that we're adding extra latency or something like that. 

**Marius**
* No, the work doesn't need to be done because proofs already in the transactions, right? So producing, building a block now does not require computing any proofs, Right? 

**Gajinder**
* So proofs are already in the transaction. so EL just needs, needs to pass it along. And with respect to CL basically it's, it, it is sort of very keen thing that CL only needs to verify whatever it gets from, from EL and not really generate any proofs or commitments on its own. 

**Alex Stokes**
* Okay. Yeah. Again, makes sense at a high level. everyone please take a look and, yeah, taking your review to the PR Mario, set a questions and chat to discuss kzg library startup times. So I guess some of 'em might be slow. Marius, do you wanna say more? 

## kzg library startup times [17.34](https://youtu.be/Xc6Ss-m_nlE?t=1054)
**Marius**
* Yes. So something that, Mario discovered during, testing for 4844 is that now every test execution, on the 4844 branch takes a couple of seconds. And this is of the startup time of the, the evm binary, which has to initialize the, the kzg library. 
* And, I think he said that, it, this is going to be fixed by the kzg library that is used in kzg 4844 at the moment. but it's just something That, this is kzg I think it's kzg, I'm not sure. 

**Alex Stokes**
* Okay. 

**Marius**
* And, yeah, so, but this is something that, we should, really discuss. Like I, I know that in order to load the data, there have to be like in order to initialize the library, there has has to be a bunch of, a bunch of curve operations right? In order to un uncompress the points.
* And, yeah, I'm not sure how long that should take, but just I will want to remind the, the writers of the kzg libraries that we will have to pay this initialization costs for every test basically, and for everything. So it makes sense to optimize it even if it is in the normal note. It is only done once, but during tests it, it's done over and over again. 

**Dankrad**
* So I believe there are two things that happen actually on startup. One is, the uncompressing, but I think the long time that takes several seconds is because we currently transform to bash form on startup. and actually both of these could be changed in principle, like, we could store the whole setup in Lara form un compressed and then like it should literally just be reading it from this. 
* So, I think that could be changed. It could take milliseconds. 

**Marius**
* Yeah, that would be really good. 

**Alex Stokes**
* Okay. Yeah, that sounds good. we can talk to the kzg containers and anyone else working on those libraries, so look at that and yeah, if it improves startup times and then sounds like we'll get around that issue. So I think that's all we had on the agenda today for anything else on anyone's mind? 

**Ethan(Nimbus)**
* I mean the SSZ stuff is still kind of ongoing. question is if we wanna move some parts of it into the mainnet, like the, the withdrawals or this, signature scheme for the SSE transactions, Right? 

**Alex Stokes**
* So I believe there was a 4844 breakout on Monday. maybe someone here attended and could give a little summary. I believe this was discussed there at least briefly. 

**Tim Beiko**
* The short, I think, the decision we made is just to wait until all cord devs makes a decision. So we like, it seems like there's a lot of stuff to like, discuss around SSZ, and in the meantime we're just gonna keep this spec as is and if there are changes that happens, we'll we'll obviously retrofit for 4844 to support, to support that or, you know, before compatible with whatever, design we'd like to go forward with. But yeah, I, we didn't, we we didn't specifically, come up to a solution on that or anything. it's not clear what, 
* Yeah, I think that Makes, yeah, and, and it's not clear like how much time clients have had to like property dig into SSZ given like, we're shipping Chappelle right now. So yeah, it seems like there needs to be more conversation and, and kind of I guess diligence then on it by different client teams. 

**Alex Stokes**
* Yeah, I think that makes a lot of sense. I know it's a pretty big change, especially like the long tail of everything we could try to do in terms of converting these different accumulators and things, different serializations, and yeah, at that point it becomes like much bigger than just changing a few routes. but yeah, 
* I think that makes sense just to keep 4844 as it is now and yeah, definitely something we could change down the line if needed. And I suppose that's on the ACDE process to to resolve that. 

**Tim Beiko**
* Yeah, I think so. Yep. 

## Research, spec, etc [23.20](https://youtu.be/Xc6Ss-m_nlE?t=1400)

**Alex Stokes**
* Okay. Thanks for calling it out Etan. anything else for that anyone wants to discuss right now? I'll take that as a no. So the only other thing we really have on the agenda that's just sort of moving now into either different research questions, discussions, open discussions, one thing that was called out was the name for the upgrade after Deneb upgrade. 
* There's an Eth Magicians post here brainstorming Enames, anyone have a favorite here? They want to chime in. Let's see, looks like some leading ones are Electra, Abla, eif. We got an electro in the chat. Either way. More electros. Okay, everyone seems to like electro yeah, so I think, the Eth Magicians post is the place to chime in, if you wanna participate in that conversation. definitely also anyone listening to the community, take a look if you, if you wanna be part of the naming process and yeah, although I can just say here looking at the chat, there's a very broad support for Electra. yeah. And then we'll need some, you know, fusion name Tim calls out pro electra, which is pretty funny. yeah. Okay. I think that's probably, that didn't really didn't seem to be too much discussion. 

**Marius**
* If we don't have anything to Discuss. 

**Alex Stokes**
* Yeah, don't, I think it's pretty much open discussion now. 

**Marius**
* I would really like to drop the EL name. and I think the combined names are kind of horrible. I know that some people don't like this because of the possibility of a hard fork happening on one but not the other layer. but I think we can kind of burn the bridge, if we get there. so yeah, I would really like to drop the names, just because it makes everything so confusing and it also confuses the, it makes it not only confusing for us, but it also makes it confusing for the community because they now have to, they they see basically they see three names, right? 
* They see Shanghai, they see Capella and they see Shapella and they have to understand that all of these three names are the same thing. 

**ethDreamer**
* And Also I would say that dropping one only having a fourth on one side and just give it one name. 

**Marius**
* Could you repeat that? 

**Alex Stokes**
* You kind of dropped Off a, that didn't quite come through. 

**ethDreamer**
* Your concern was that people don't like this because we might have a fork on just one side, but you can still do that and just have one name. 

**Tim Beiko**
* Right now it's just the name looking at the, the name tells you whether it's one side or two side, but arguably that's small benefit. 

**Alex Stokes**
* Yeah, the way I see it is like having the greater resolution is good for, you know, people who are working on clients, things like this where it's like having that extra technical support resolution is really helpful. At least it can be.
* But yeah, I agree with what people are saying that like it is really confusing. sometimes I'll even get tongue-tied talking about them and like say something, you know, some weird other name trying to refer to, you know, one and a half at a time. So yeah, I mean I don't think it would be crazy to just move to one name If I may, is trying to, that Being said, oh yeah, go ahead. 

**Pooja Ranjan**
* I think this is a good opportunity for like Ethereum developers to kind of educate Ethereum community to learn all about Ethereum. Like tell there are people who thinks that it is Eth2 and I have read articles and like reputed news, websites saying that Ethereum has moved, it's a consensus to Eth2. So if we are having this two layer concept, we are trying to educate them in terms of suggesting that Ethereum works in on two layers and these are the changes the people interested in learning more about execution layer. They should follow the execution repository and learn more about that. 
* And definitely execution development team has their name. So I kind of support these two names. It's just that we need to start talking about it early on. Like we did it for Deneb. I don't think Deneb will have that kind of problem that Shanghai and Capella had, similarly. yeah, that, that's my thought yet. 

**Alex Stokes**
* Okay, thanks. yeah, I mean just, you know, to be respectful of everyone's time, I don't think we're gonna solve this right now on this call. maybe it warrants an Eth Magician post or something if you feel strongly and we can move to the conversation there. You know, I think we'd also probably want to bring this to All core dev and get that take. 

**Tim Beiko**
* It's so much more fun. It's less, better SEO as well, you know. How many hits do you get for Chappelle outside of Ethereum versus Prague? I like it. Yeah. Not a hill I will die on, but yeah,  if the concern is technical, like if the concern is actually like we should just tell the community one thing and they should only understand one name. 
* I'd much rather it's like a fun new name than like Prague. we can find some random stars nobody's heard about, but yeah, ideally two or three syllables. Potus. Yeah. yeah. 

**Alex Stokes**
* Anyways, So if I think, yeah, I think if you care about this, anyone listening, you should, someone should make any editions post and we can move the conversation there. Otherwise we'll just talk in circles about, by shedding names for the next hour. And that being said, anything else anyone has, I think otherwise we could just call an early call today. 
* I'll take the silence as no. So yeah, thanks everyone. and yeah, I think the main thing if you're listening is just to look out for the client release blog post something like two weeks from now. I think that was right and oh wait, was that one week? Yeah, sorry, more like one week from now. that's important to get right, so keep it, keep an eyes on the blog and yeah. Otherwise thanks to everyone and I'll talk to you all later. 

* Thanks for hosting. Thank you. Thanks. 


____

### Attendees
* Alex Stokes*
* Tim
* Trent
* Pooja
* Barnabas
* Terence
* Pari
* Ethdreamer
* Mikhail Kalini
* Mike Kim
* Zahary
* Pawan
* Chris Hager
* Gajinder
* Andrew
* Mario
* Shana
* Carlbeek
* Roberto
* Sammy
* Protolambda
* Saulius
* Marek
* James
* Dankrad
* Kevaundray
* Radek
* Fabio




