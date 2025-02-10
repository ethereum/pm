# Consensus Layer Call 148

### Meeting Date/Time: Thursday 2025/1/9 at 14:00 UTC
### Meeting Duration: 1 hour
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1218) 
### [Audio/Video of the meeting](https://youtu.be/4LbNL_hp2Ho) 
### Moderator: Stokes
### Notes: Alen (Santhosh)

## Summary <!-- omit in toc -->
Summary | Description
-|-
148.1  |**Pectra Devnet 5 Open Questions** EF Developer Operations Engineer Parithosh Jayanthi flagged one open issue in CL specifications that needs resolving by developers for Pectra Devnet 5 launch. In addition, Jayanthi noted that hive tests for both EL and CL clients have been updated and most clients are doing well against these tests.Stokes noted that there is another open issue impacting EL clients related to the system contract in EIP 2935, serve historical block hashes from state. Stokes said that he would follow up with Geth developer “Lightclient” on the status of this issue after the call.
148.2  |**Pectra Devnet 5 Timing** On the topic of Pectra Devnet 5 timing, Stokes recommended touching base on the status of implementations with EL client teams on the next ACDE call before finalizing a date for Pectra Devnet 5 launch. EF Protocol Support Lead Tim Beiko recommended touching base on the Monday testing call, earlier before the next ACDE, and ideally try to launch Devnet 5 sometime next week. Stokes agreed the earlier the better so long as EL client teams are also ready for launch.
148.3  |**Pectra Devnet 5 Timing** If Devnet 5 launches in the next week or two, Stokes said that optimistically speaking, developers could start upgrading Ethereum’s public testnets, Sepolia and Holesky, in February and aim for a mainnet activation sometime in March. Jayanthi and Lightclient both commented that coordination for a Devnet 6 launch is likely needed before or during public testnet upgrades.
148.4  |**Pectra Devnet 5 Timing** Beiko asked what everyone’s thoughts were on upgrade ordering and whether the Ephemery testnet, a new Ethereum public testnet that resets once every month, should be upgraded alongside Sepolia and Holesky. Stokes and EF Security Researcher Justin Traglia said Sepolia should be upgraded before Holesky. Beiko said that client releases for Sepolia and Ephemery could be bundled together so that they are upgraded concurrently. Stokes said that bundling client releases for Sepolia and Holesky would also help speed up the timeline for mainnet activation.
148.5  |**Pectra Devnet 5 Timing** bundling client releases is only effective if there are no issues found in code during public testnet upgrades. Assuming two weeks of time between the Sepolia and Holesky testnet upgrades, any updates made to client software in light of the Sepolia upgrade will require developers to release updated software for the Holesky upgrade.Developers did not reach a decision about the next steps for Pectra testing such as when to launch Devnet 6, either before or during Pectra activation on Sepolia, or how to plan client releases for the Sepolia, Holesky, and Ephemery testnets. There was some discussion in the Zoom chat about kick starting a bug bounty program for Pectra after the Sepolia upgrade, but this was not confirmed on the call.
148.6  |**ENR Field Updates** A developer by the name of “Pop” has proposed three new fields to Ethereum Node Records (ENR) specifications. ENR specs define information for node connectivity. As stated in the documentation for ENR on GitHub, “A node record usually contains the network endpoints of a node, i.e. the node's IP addresses and ports. It also holds information about the node's purpose on the network so others can decide whether to connect to the node.
148.7  |**ENR Field Updates** Pop explained the three new fields enable nodes to establish outbound and inbound connections on both IPv4 and IPv6 addresses. Stokes asked developers to review the proposal on GitHub. Pop said that the changes are backwards compatible so they can be merged and finalized independently from Pectra.
148.8  |**Validator Hardware Requirements** “Kev” has created a document defining the minimum hardware requirements for Ethereum validators. As stated in the document, these efforts have several benefits. “A clear hardware specification is crucial for ensuring meaningful benchmark comparisons across different implementations, enabling informed decision-making about protocol upgrades and their hardware implications, [and] providing clear guidance for node operators with respects to the future,” Stokes asked developers to review the document and provide feedback on it to Kev.
148.9  |**G-star Upgrade Name** the CL’s seventh upgrade, the upgrade after Fulu. Based on an Ethereum Magicians post, the G-star name with the highest number of votes was “Gloas”. The accompanying EL fork is expected to be activated at the same time as Gloas is already named Amsterdam. Stokes mentioned that one of the reasons for going with Gloas was that the portmanteau for the combined EL and CL upgrades could then be “Glamsterdam”.

# Intro
**Stokes**
* Cool. Welcome back everyone. I hope you had nice holidays and we will get started now with this Consensus Layer Meeting  148. The agenda here is in the chat. It's issue 1218 on the PM repo. And yeah I think the main thing today is to discuss W5 with Pectra. there's like a few things to touch on there and then a few other things after that. So let's go ahead and get started. So first up. Yeah. Devnet 5. we had gotten, I think, the specs mostly together before the holidays. people have been working on them since then, so thank you for that. And yeah, just to close out the specs.
* I wanted to ask if there are any open questions I don't know, Harry. I see you're here. Are there any devnet things to touch on before we dive into the specifics? 

**Parithosh**
* Yeah. So there's just this one open PR I've listed it in the chat, but otherwise I think there's nothing. there's nothing on the devnet side of things. we have a specific hive instance, and I guess, updates. Since the last ACDE, there have been execution spec test release as well as consensus test releases. So those both are pinned in the spec sheet, and we have a hive instance now that runs the execution spec tests. And most clients are doing quite well. I think Nethermind also just commented earlier today that they've already updated and addressed some of the failures, so the next run of hive should pick that up. besides this, we're also doing the execution spec test inside Acerta, and I think 
* Phillips found a few things that he's just clarifying with the testing team and will bring it up. probably soon. In chat All right. 

**Stokes**
* Great right. So, yeah, this was one open thing that Perry linked here, 4077. I think we got a little carried away with our versioning. And so this PR basically just rolls back a V2 endpoint to a V1 with the blob sidecars sort of RPC set of 
* Endpoints. Pretty straightforward change. Looks like a number of people have already approved it. Anyone here opposed to this change I don't think there's much to oppose Otherwise, we can go ahead and merge this in after the call and get that into Devnet five. Let's see Okay. I think that was it on the CL side of things with net five specs. I looked at the spec tracker that we have. There was one more specific thing. Just because it was open, I figured we could talk about it now. it's this PR. Let's see. This is 9144 to the EIP repo and update to 2935 system contract. Does anyone have any more context here? Maybe, Lightclient.
* This is your PR It looks like there are a number of changes, but I assume these are good to go 

**Guillaume**
* From what I understand, this has already been released on Devnet five. like, optimistically released on Devnet five. But, yeah, the update, like the PR itself needs to needs some work, but it should be it should be merged at some point 

**Stokes**
* Okay, great can we merge in the next few days just so everything's ready for Devnet five? 

**Guillaume**
* Well, you have to ask, Matt, but apart from that, yeah. 

**Stokes**
* Okay. I can follow up with him So cool. And then in terms of specs, was there anything else anyone had or wanted to discuss If not, then we'll move to Paris. Question here. Where are the CLS on dev workflows? So yeah, this also kind of gives this up to the next point, which is implementation, sort of progress. And yeah. Would anyone like to give any updates there. So one where our clients with Devnet 5 and then two specifically with the builder specs and implementation of MeV support 
* Our clients are mostly ready with devnet five. 

**Sean**
* So for lighthouse we're mostly ready with devnet five. We've got like a couple small things to fix, but lighthouse is like working with itself on testnets. and the builder spec is a work in progress for us, though 

**Terence**
* I think prism has been passing that net five kurtosis, but it's on a different branch. That's not ideal. We want to run on the latest basically the main branch. And then yeah like I said we have a PR that is out already that once it's merged you can run latest develop. Besides that we have a pending builder PR that will start putting more focus on that will review and merge in the next, hopefully in the next few days. So besides that, we want to be ready for the builder path as well 

**Enrico**
* The tech side, we we are devnet ready on master. we don't have yet support for SSO builder. flow. But the builder flow should be fine as well. But we will double check on that. So good to go 

**nflaig**
* So for Lodestar, we are also good to go. I think the only thing we need to do is now revert the v2, regressed endpoints, I guess, because we would start querying those after Electra so and also we support the builder flow and SSZ as well 

**Saulius**
* Let's see. And for Grandinetti, the update is that likely everything is ready except the SSZ builder flow. So we are quite similar to the other teams 

**Stokes**
* Okay 

**Stokes**
* And then let's see, I think Nimbus 

**Stokes**
* I'm not sure if anyone's here, but in any case,  Yeah. Good to hear that. There's been good progress on devnet five. I will call out this other comment Justin put in the chat. beta zero specs released today, so keep an eye out for that But yeah, it sounds like things are moving along pretty well So if there's anything else to add there. yeah. I think the next item 

**Parithosh**
* I think on the CL side, they're mostly good because they're passing kurtosis tests as well as CL spectres. would be great to hear from the ELs if they're around, because I think most of the hive failures still need to be addressed as well as like lion's point, about the 7702 transaction pool. If we want to have that in Devnet five or not. But both of those are clearly EL topics 

**Stokes**
* Right any EL want to speak to that I suppose we want to have the 7702 transaction pool sorted before main net. So that kind of implies it's time to do it now Okay 
* Possibly no ells on the call who want to speak up So in that case, we could check in on next ACD and get a better sense of timelines. Unless someone wants to do something else but it seems like that's kind of where we're at Oh, yeah. There's a testing call on Monday So. Yeah, I mean, yeah, we'll we'll keep checking. I think every touch point we have Yeah, by act would be great okay. There's some stuff in the chat here Okay. I mean, yeah, sounds like everyone's busy and trying to get this as soon as possible, so hopefully in the next week or two, we can have done F5 
* Then from there, I do think it's helpful to talk about timing for test nets for spectra. And then minute. sort of just like a sketch of one possibility here is, you know, if we have net five, let me just pull up the calendar, you know, the next week or two that kind of tease us up to start doing test nets in February if we have no issues and can move quickly. I think it's possible to do it in February. Then from there, that kind of teases up for minute in March Anyone feel good or bad about that timeline Can I ask about that? That sucks. I mean, I would say we do net six if we need it, so that kind of depends if we see net five, having issues So optimistically, there are no issues and we can kind of move forward like I said. Otherwise.
* Yeah. We'll have to squeeze in net six somewhere. No comments. So I assume everyone's okay with that, at least in theory Okay Anything else to discuss around better coordination around dev nets, test nets and then to net 
* Ten has a good question here. What do we think about test net ordering. Would someone prefer sepolia versus the other sequence People are different. I would suggest doing sepolia just because it's less chaotic. And then halusky. Yeah, there's another comment here, Justin, saying the same thing One thing is, if we do sepolia, that's kind of like a stable app facing test. Net and I think some people have been asking about testing things like 7702 as soon as they can. So that would be nice there's a question about ephemera here. Part of the official deploy schedule yeah. I'm not as close to operating ephemera as anyone here. Closer to that. Who can speak to that 

**PK910**
* Yeah, we can think about, doing it, too. But we eth client stable releases for that first. That include all the extra changes 

**Stokes**
* Gotcha should we, like, block the test nets on ephemera? Do we think or. It's not that important 

**Tim**
* I think if we have the Sepolia releases, we can probably use those for ephemera for people to start testing. And then, it depends as well. If we want to do a single client release for Sepolia and Hoskey, but if we don't, then we can use the Sepolia release for ephemera, even if we want to wait to see how that goes before we do hoskey and then update it if there's anything wrong 

**Stokes**
* Yeah, that works for me Which, by the way, I do think that's a good point. Like if we can cut releases for help and support at the same time, that will help us pipeline quite a bit and move faster So something to keep on everyone's radar Okay. Anything else here There's a question about higher validator counts on the dev nets 
* Yeah. Per suggestion of devnet six with higher validators 

**Parithosh**
* Yeah. I think I can just bump the validator count for Devnet five and for six we can discuss having something with a lot more validators and potentially just doing it as a shadow fork or something. So there's also some state to play with 

**Stokes**
* Yeah. Would you want to do that before sapolio or you'd be okay doing them at the same time 

**Parithosh**
* I think same time is probably okay as well But I just focus for now on dev net five being out the door, and if that's done then everything else can happen in parallel. 

# consensus-specs#3874 [18:37](https://youtu.be/4LbNL_hp2Ho?t=1117)
**Stokes**
* Yeah, for sure Okay. Any other questions If not we can move to the next item here. There was a last call for adding IPv6 support into the inner. Let me grab the PR here So, yep, there it is in the chat. 3874. And yeah, there's been a lot of discussion on this over the last couple of months, and I think it's pretty much ready to go yeah. Anyone here want to add anything? Pop, you are here and had the comments. Any more context? 

**Pop**
* Yeah. This is about adding three new fields to the inner, we add we are adding TCP and UDP. The purpose of adding this field is to, to to allow like the, the node to, to have a different port for IPv6 than the port for IPv4. Because if you don't have this field, we, we, we can have only like single port that that is used both by IPv4 and IPv6. But yeah That's it 

**Stokes**
* Cool. Thanks yeah. Otherwise I think, this PR is pretty much ready to go. So yeah, I mean, I guess you'd like to merge this soon 

**Pop**
* Yeah. If there is no objection, I think we can merge like this soon Okay. 

**Stokes**
* So. Yeah. Everyone listening, take another look. If this is relevant to you. And, yeah, it looks pretty straightforward. I don't believe we need to get this on texture or anything. So it's here and you can go when it's ready. so. Yeah, please take a look when you have some time 

**Pop**
* It's actually backward compatible, so we don't have to ship it like on any hard fork. We can just ship it, like, as soon as possible because it's backward compatible All right. 

**Stokes**
* Cool Okay, so I think that's all we had for Petra today. anything else? Any final comments? Otherwise, we can move on to the rest of the agenda Okay, so next up, then we have items under perdas, you know, scaling the blobs. And there wasn't anything in particular. I just wanted to ask if there are any updates. I know that there's been some work on subnets, kind of in parallel with Petra. People have been pretty heads down on Petra over the last, say, a couple of weeks, so there might not be anything to report, but I figured I would ask I think there was a breakout earlier this week, but I couldn't make it Let me double check. Yeah, it looks like there was one. I don't know if there's anything to share from that breakout 
* Okay. I think people have really been focusing on Petra, which is good, but yeah, expect a lot more pure dos once we get Petra to main net 
* So next up then there is a reminder here to review this document on hardware requirements let's see, is Kev on the call? He put this here I don't see him 
* So, yeah, I can share a little bit. there's this document here, and basically it's just trying to define, like, a minimum set of hardware requirements. This is really helpful for all kinds of things, both like communicating to people who want to interact with Etheresay, as a validator. also, when designing the protocol and thinking about different parameters of different designs, what, you know, makes sense and what would not be okay. So this documents here, number of people working on it over the past say month or two. yeah. Super cool to see everyone. Please take a look. And I think the concrete ask is if you have any, feedback on this document, to send that to Kev Otherwise. yeah. I think that's all we need to say for now on that And then otherwise, there was just one last thing here on the agenda for the name of the G star.
* So we have a poll here on East Magician. So let me grab the link that's there. And there are a number of names from AB Coachup. I'm actually not sure how you say his handle, but in any case, number of names here. And then there was a poll. if you look at the poll, the leading result right now is Globus, which I also like. I think it's pretty cool. So Yeah. Oh, wait. Kev is back. Yeah. Let's jump back there then. Kev, do you have anything to add Yeah, I guess just chime in if you do, but otherwise. Yeah. So, we have Amsterdam. The G star Globus is the leading candidate, and. Yeah, don't really want to open up a huge bike sharing convo, but unless someone is super strongly opposed, let's move ahead with Globus for the name And then we have a great portmanteau here. Amsterdam Okay, sounds like people are indifferent or they like gloss.
* So let's go with that 
* And I believe that was it on the agenda for the day. super short and sweet call anything anyone else would like to discuss? Otherwise, we'll go ahead and wrap up early today Okay. If not, let's go ahead and resolve these few open questions for the Devnet five specs, implementations. Yeah. Keep, you know, polishing the things you have. And, yeah, we'll get to them at five, as soon as we can 
* And with that, I think we'll go ahead and close. So thanks, everyone, and I'll see you around

  

---- 


### Attendees
* Stokes
* Tim
* Arnetheduck
* Marek
* Lance
* Micah
* Paul Hauner
* Ben Edgington
* Loin Dapplion
* Terence
* Enrico Del Fante
* Pooja Ranjan
* Hsiao-Wei Wang
* Saulius Grigaitis 
* Roberto B
* Olegjakushkin
* Chris Hager
* Stokes
* Dankrad Feist
* Caspar Schwarz
* Seananderson
* Andrew
* Crypdough.eth
* Zahary
* Matt Nelson
* George Avsetsin
* James HE
* Marius
* Ansgar Dietrichs
* Lightclient
* Stefan Bratanov
* Afri 
* Ahmad Bitar
* Lightclient
* Nishant
* Gabi
* Pari
* Jimmy Chen
* Gajinder
* Ruben
* Mikhail
* Zahary
* Daniel Lehrner
* Andrew
* Daniel Lehrner
* Fredrik
* Kasey Kirkham
* Protolambda
* Cayman Nava
* Stefan Bratanov
* Ziad Ghali
* Barnabas Busa
* Potuz
* Trent
* Jesse Pollak


