
## Ethereum all core devs meeting #147 
## Time and date: September 15, 2022, 14:00 UTC
## Duration: 1.5 hours 
## [Youtube recording](https://youtu.be/DdUt77_eWyc) 
## [Agenda](https://github.com/ethereum/pm/issues/616) 
## Note taker: darkfire-rain 
## Meeting administrator: Tim beiko

**Tim beiko:** * (8:05) Okay, we are live. Welcome everyone to this first post-merge. All Cordel's call acronyms one hundred and forty seven. I just shared the agenda in the chat here. I think we'll try and keep it relatively brief. Today. Basically cover the merge. Some discussion around starting to plan for Shanghai.I guess i'll start by saying congratulations. Everyone. I think the merge went extremely smoothly. By basically, all accounts. Yeah, it's been a while to see this happen on train. Finally, after so many shadow for it so many tests, and to have it go off relatively without any issues. Basically, So yeah, congrats on all the client themes, researchers, testing folks who worked on this for years to make it possible it was. It was really cool to finally see it live on the network.Yeah. And I guess you know the start. I'd love to hear from just different time teams about how you sides went. If there's any kind of minor issues you're chasing down or stuff like that. But you want it. I share it with folks here. Yeah, anyone want to share kind of their perspective on how it went and what they're They're monitoring. You're looking at now

**Marek Moraczyński:** (9:40) I can start  so we had many notes in our front. Generally all of them are working without any issues, no transition issues. Uh, what's more, just after we hit transition. I recently received some notes to confirm that our postman is working and look very good. Ah, so generally, so far. Other mind notes are very stable. Last March I didn't notice any critical reports from users. Yeah, that is all.

**Tim beiko:** (10:20) amazing. Um, Yeah,Anyone want to go next?

**Fabio Di Fabio:** (10:25) Yeah,I can talk for Basil. We had some ah issue just on the March block. Some users have to restart the nodes to start the sinking. The cows are still unknown. I was related to one side when I was using, but the rest of the engine and the consensus fix the problem mostly. Then there are some issues related to some visits at the station. From that we are investigating, and they also use our data reporting timeouts. Our notes are fine. They are missing, some at the station as well. So we are investigating this part, but they are in a S. And following the the that

**Tim beiko:** (11:46) awesome Thanks.Um, Someone from Aragon wants to go.

**Andrew Ashikhmin:** (11:50) Yeah, sure. So I think most everyone knows when fine through the knowledge. But now we are hearing reports that if you know that you try to restart after the marriage, then it occasionally becomes stock, or so it is. It looks like we need to improve our post now.  And there are also a couple of other smaller issues that appear to affect only not all the nose, but some notes. We are still investigating. What's going on.

**Tim beiko:** (12:34) Got it Thanks for the update. Um get.

**Berlin EF office:** (12:37) So for us. The merch was surprisingly boring. We Haven't noticed anything going wrong, and mark, and essentially one asked what metrics he is, or what is he looking at? Essentially he's the most interesting thing about essentially nothing. We are not aware of anything that has gone wrong. We'll Probably we do expect some people to have issues. So it's. It's a kind of a new world with different plan combinations. So I'm almost certain that some people will open issues, and i'll be tough directors, and there's a fairly high chance that some of them could be their gifts, so it's probably not a couple of weeks. It's like being addressed just to make sure that it works.

**Tim beiko:** (13:36) Got it. Um, yeah, that sounds. That sounds pretty pretty great overall for any of the Cl. Teams on the Call Water Sheriff. From their perspective. I see some prison votes take who I don't know if we have folks from other teams as well.

**Ben Edgington:** (14:05) If you want to fill some silence, taku no specific techy related issues. All seems very smooth. A lot of people seem to have paired tech you with bases. So we're seeing similar reports of occasional miss status stations and empty blocks from time to time. But it doesn't seem epidemic. It just seems to be a a handful of users, and it seems to be exclusively with with bases. So

**Tim beiko:** (14:35) So it um. Your cl team want to share anything. If not, I don't know if someone wants to, just maybe take a minute or two. Oh, Micah, you want to share something.

**Micah zoltu:** (14:53) Sure. I think I was the only person in the world who had a problem with the merge. Ah, I see bugs and look into it a little bit, and it turns out it's because I forgot to upgrade my execution line and install a, and it was because I had spent the entire time prepping, helping other people updated. I forgot to do my own.

**Tim beiko:** (12:18) I guess as long as you update your five things work does anyone want to take a minute or two to kind of talk about just the state of the chain. What we're seeing in terms of just participation rates, slot, block, inclusion, and slots and whatnot. I don't think I see Perry on the call who's usually are, or expert here, but anyone want to jump in?

**Berlin EF office:** (15:59) I'm here. Yeah. In general, we're not seeing an unexpected amount of this slots? We are seeing something like ninety, eight, ninety, nine percent at the stations so roughly ninety-eight, ninety-nine percentage of blocks out being reduced, which is big. Um, We also do relatively full of blogs, and I think I saw a couple of weeks of people down in about presented to fuller blocks in Pws and the Ip. One has had man, et cetera, were being paid. So I think we love it.

**Tim beiko:** (16:36) Got it. And yeah, do we know? Can we attribute like this a one percent drop to anything. Um. And I know. Yeah, There was a little bit higher of a drop like when the merge happened. I think we just like we quickly hit like ninety-five fish. Um, yeah. Have we attributed this to something Your haven't had time to look into it. Yet.

**Berlin EF office:** (16:56) Um. Unfortunately, Haven't had time to look into that. Yeah, it's cool up in here. So one other thing regarding the merge, this whole chain, and they're all it kept producing. And right now the core one shows, I think, in twenty, five blocks, and we're produced, and these are so. These are produced by clients older than I guess, one little ten, twenty, one thing which are not configured for the merge. If if someone just uses to get a client which is properly configured, but it doesn't have the be come out. It would just thatline. But these are the things. They are older than that, and timestamp with the latest bug that I see on the horizon is two hours old, and but we discussed that a bit earlier, and Peter made the observation that right now for someone who runs old software and is mining the old of us, and we'll probably have very large difficulties propagating them across the network, because the most of the peers which have been able to to done the merge they will no longer propagate and announce the new gos. So it will be very yeah, a very chaotic chain. And but apparently at least to reach that, It's not. That's that's five or twenty, five blocks just to be it was twenty five that just interacting with initially, there were a lot more blocks being mine was propagated, and our explanation is that once the transition was happening and the blocks were still being propagated. But once we finalized the merge, then the internet would just stop propagating blocks from one rider to the other. So our expectation is that currently, if there are a couple of minors still mining on the old chain, they are most probably mining their own musical worlds, and these worlds will collide. Got it just for me. It's a big that's the i'm costing

**Micah zoltu:** (19:20) as the proof of work, gossip network, partitioned from the State custom network like they're no longer communicating.

**Berlin EF office:** I don't know. So the partitioning logic is based on the for copy, and that's not yet.

**Tim beiko:** (19:50) Yeah. And I guess uh, just to make sure there's nothing else on like the actual merge itself, we can finish that. But yeah, I think after that we can. We can discuss that. This is. And yeah, just before we go there was there anything else anyone saw on chain or with their client that they wanted to share. Okay, in that case, sure, if we want to cover quickly this fork, Id chain just for context  for folks listening uh, Usually when we have a network upgrade, the peer-to-peer network gets automatically disconnected from non-operated peers, and we use blocks to determine this But because the merge was triggered by a Tdd. And not a block height the kind of mechanism we usually use for This does not uh, does not work. Um! So we need to like retroactively have it, or after changes the fork, Id at a specific block. We've done this on a couple of the test that we have not done this on Gordy yet. I believe so. I think if we and we've obviously Haven't done it for main net. So I think if we wanted to to kind of set this, it would probably make sense to have it happen on boardy and maintenance roughly around the same time, so that people only have to download a single release, and both networks get upgraded. Um: yeah, I'm: curious what people think about this generally like. When should we do it. Yeah. But how long is it okay to have kind of the network? Not be partitioned by fork? I need.

**Berlin EF office:** (21:50) Okay, so maybe I don't. Oh, sorry, please. But did you repeat the question, 

**Tim beiko:** (22:00) How quickly do we need to do this right like? Do we want to like paying for a specific block height like today, and actually implement it? Or is this something that could wait, say after def Con? And it'll be all right

**Berlin EF office:** (22:30) so essentially that the reason the whole fork idiot is to this to clearly separate networks when most nodes do not upgrade. So it's actually mostly test that in the case of May, that we historically have always updated that for the merch I'm assuming almost everybody's already updated so from main that, or maybe that's perspective. There's no particular rush, because I mean for us it's super healthy. The only thing we're really unhelpful about is the whole blockchain, but that doesn't didn't play a priority. So  so I think it's completely fine to wait until whenever it's just it would be nice to finish the upgrade initial march completely and like, if there's no rush to,

**danny:** I would say, Is there not a like if that's the logic. Should we not just wait until the next hard fork on the main net? Because otherwise there's a chance that users fall off when there's nothing really that we, the Cleanup Doesn't, seem requisite. And so maybe the cleanup should actually just happen on the next forced coordination point, which is the next hard for it.

**Berlin EF office:** (23:45) So the weirdest thing is that this thing was already rolled out, and at least, so i'm not sure about the they made it. Even so. We kind of end up in a situation where our tests have a different behavior than maybe that some say,

**danny:** yes, sir. (24:05) Yeah. And I I guess if I was arguing to only do it in the next hard work, i'd say, actually still clean up the test nets. But if you think the divergent behavior there is not good, or maybe not even a good precedent. So I mean what?

**Berlin EF office:** (24:20) So it's four kinds of support. So it's completely fine to, so to say, do to works in the same block from a perspective, so you could just say that i'll be the next part, for I think that's Shanghai that will apply both the Shanghai update and also the merge next to it work. I so that works a bit wonky. But yeah, I mean it. It's fine.

**Micah zoltu:** I assumed we would just skip this fork. Id and just do the Shanghai.

**Berlin EF office:** We can't skip them. But, as Peter said, I mean, if we bundle them together, then effectively, it will be scary.

**Micah zoltu:** Yeah, okay,

**Tim beiko:** Because that yeah, the clients expect a a block for this right?

**Berlin EF office:** (25:00) Yes, I mean in theory, we could skip it just from a time. Configuration, perspective. It's weird that the merge we apply the merge, and then some part of it is just missing because we don't need it. It It just wonky. I guess we define the apply together which runs high, and then it's the same thing as a liquid.

**Tim beiko:** (25:30) Yeah, I think given There, there's always a risk like that, it was saying. It's like users, you know mess up when they're upgrading. Um! If there's no strong reason to do it before Shanghai, I personally would also rather have it just bundle like we like the double fork on the chain high block. Does anyone have like a strong objection to that?

**Berlin EF office:** (26:00) So one thing that we need to keep in mind is that cracks. We are talking about new chains here. One of them is a stake chain, and the other one is the left behind that blockchain. And in these cases basically nobody is running the old chain on a properties to not many people. However. Yeah, the chain that's not remained. You still have a Soviet table. If another author could change pops of them, this discussion might need to be reconsider,

**danny:** so that, assuming that they don't do this upgrade properly for themselves.

**Berlin EF office:** I'm almost certain that they will. Not so. but, anyway, so my Pr: I think it's completely fine to postpone doing this on just as long as the climate change doesn't change, like some weird change happens that we can always do.

**Tim beiko:** (27:00) Yeah, that seems reasonable to me. Anyone disagree strongly with that. Ok. And then related to the Merge. I think Chris, haggard from the flashpots team. Wanted to get a quick update on the Tv boost.

**Chris Hager:** (27:30) Yeah, Chris. Yep. Absolutely From our perspective we march. Well, we bet that the sixty-eight parts enabled thirty bits, and you are seeing no problem, and I just wanted to bring out the topic of adding a soc subscription to the speaker notes that allows builders to Twitter Record,

**Tim beiko:** (28:00) and this is to the beacon node. Correct?

**Chris Hager:** (28:15)Yes, this would be an efficient to the beacon notes, so to trigger lock work on whenever a new payload event is received, and that would land itself nicely that could include the builder attributes the we are currently using a the court here, and this is some. It's a hundred percent out like once it's not. It will be really beneficial, and there is more and more builders coming up. They would all profit from just having a subscription.

**Tim beiko:** (28:40) So I guess just because we don't have all the Cl folks on this call, and I suspect  no one has had the time to think through it. Maybe the best way to go about this is, if you can maybe put together like just a short like summary of what it would look like like an issue of poll request. And we can maybe discuss that on the C alcohol next week in more detail, and people will have time to review before them.

**Chris Hager:** Is that, Yeah, absolutely

**danny:** right on the flash box relay. We've seen how many, how many blocks come

**Chris Hager:** (29:30) on the flesh, what really is, and the it served one hundred and seventy six payloads, and there is five thousand registered proposals, which is about fifteen percent of all the proposals that are collect it or have connected at some point.

**Tim beiko:** (30:00) sweet um! Anything else related to the merge? Oh, And'sgar has a question about history. Duplication for execution, payload, and what the sales is. That is what you want to take like a minute. It just

**Ansgar Dietrichs:** (30:30) sure right. I'm here . I'm not i'm not sure if it's the best penny for it. I was just wondering because I was talking to some salespeople early in the morning. And then basically just I think my understanding is correct basically right now. Um, because the execution parallel is part of it. We can book. Of course it's it's being stored as part of the beacon chain industry by the Cl. And then, of course, the excuse passed on to the er, and also stop there as history. So right now, basically on on any machines are running both notes. Um, you basically just store the the excuse me, or twice, I think. Um ideally, of course, at some point we want to have some sort of duplication strategy, with only stored from the on on one of the two sides or something. So I was just wondering when I guess for me that's broadly like post-matched cleanup. And so now that we are post-mergers is wondering when when would be the best time to kind of talk about these things.

**Tim beiko:** Um, and I said, Terrence has his hands up.

**terence(prysmaticlabs):** (31:25) Yeah, so I can speak on on behalf of. We have a prison. We do not plan. We do not plan to do duplicate them. We have a plate flag to basically store the one diversion, and that is currently not be able by default. Just one more testing, I think, in our next release we we could enable by default by a todr is that we don't plan to on duplicate them.

**danny:** (31:56) But prism prism uses is kind of Ah, the the Eth Api to do so. It doesn't have support and like a more optimized way from, say, the the engine. Api: right?

**terence(prysmaticlabs):** That's right. Yeah. I believe my house as well. Yeah,

**danny:** I mean, you know, I think I think the conversation then becomes is the

**danny:** the the Pr. That you also put up quite a quite a while ago, you know, is that even maybe an optional endpoint on the engine? Api. Is that something that we want to move forward with? Or is the you take that sufficient? Or you know, I think I think that's that's the marching question. I do. I do should be elevated in support.

**Ben Edgington:** (32:52) Yeah, on Toku side. We have shelved this for now, because we really don't want to pollute the beacon chain side with Ah Rlp encoding, and all of that, What we would really like to see is an Api on the engine Api, which just deliver a payload in Ah Rlp. Then we can rebuild the, you know, with the transactions R. And being coded. Um, so that we can just rebuild the block from the blinding block. So we've done all the kind of database work on our side, and we can store blinded blocks, but we can't reconstruct the full block without a specific engine. Api. So that's that's where we are

**danny:** (33:30) So I would.  I would suggest we revisit y'all six Pr. Over this next week, and then decide on the consensus layer side. If this is, if that's meeting our needs or for me to modify it, now finded blocks, um, and then also loop and execution layer folks, you know, over the next couple of weeks to then decide if it's something that can be well supported over time, and maybe something that we can add as optional. I guess that's that's also probably a debate discussion point. But you, I think that we can have the consensus layer side of this conversation, probably over the next week, if you all are willing.

**Berlin EF office:** (34:40) Okay, um, if not the other kind of thing I had on the agenda is on the all part of the Channel in that art and vertical as we should set the so, the hass and the sentence of the number, and instead of G ttd

**Tim beiko:** um

**danny:** (35:15) it's, it's certainly safe to do so independently in your client, because you this cannot, will not be reverted. I guess. Then the question is, you elevated to specifications? And is that worthwhile? I don't have a firm at the moment.

**Berlin EF office:** (35:40) Um! So the one thing that I would avoid reincarnating is is that at least for for G. The fork Id is tied to work block numbers. So if I were to just now retrospectively add that then i'm all of a sudden, also affecting changes on the fork, Id So there. There are these considerations to make that there might be some political links between them.

**Tim beiko:** (36:20) so it's almost like the clients, could use the fork block internally to do things better. But we don't want to advertise that on the peer-to-peer network an actual fork block Because then, yeah, we're effectively doing this fork, Id change retroactively and losing peers

**Berlin EF office:** (36:47) if the engine Api has notions of the Dvd. If somebody wants to transition at like for a network you need to shut. Dtd: So it's uh. I think it would be a huge count for you to just redefine the merge. Yeah, I didn't want to. I'm not the proponent. I just wanted to raise it, because the art didn't mention it. I want to see what people thought about it. So my true sense is that we can definitely think about it. But I think it has more implications than immediately obvious

**danny:** (37:30) because they may be it can be complementarily added somewhere when ready to do a network upgrade on a merged network, but probably shouldn't subsume.

**Mikhail Kalinin:** (37:50) It probably makes sense to check that The remote pier that you are connected to has a certain blog hash with a certain height, just to prove that it's on the right chain. If the sink starts from scratch,  I don't know if it makes sense, but probably the

**Tim beiko:** (38:10) I guess. Given that this is, you know. First, a client thing is this something that's say, a cooler can prototype and

**Micah zoltu:** see if it can. All right. They would need to verify under the C out as well.

**danny:** (38:30) So that is one minor thing that did come up is the exchange  transition configuration. Some consensus layer clients turned that off, I believe at finality, and some did not. I think the spec was maybe didn't say to turn it off, but some thought there's no issue, and so I think one of the extremely minor issues seen with some users seeing errors around, not having that exchange configuration. So there's already a little bit of a hiccup.

**Micah zoltu:** (39:00) Can we just remove it like, Make that The way to go forward is all the sense to clients, and I shouldn't plan to move that exchange. Is that safe?

**danny:** yeah, They clarified. There were warnings. Um. So not errors. But yeah, um, I think it's probably reasonable to add a little note that it will be turned off. It finalized.

**Berlin EF office:** (39:25) So one thing that again at least uses that exchange is to detect if a consensus client is online, but it's not yet seen. So we've added a lot of different warnings to try to detect different misconfiguration on the different issues on the But if we don't see any messages from the customer's client, and we probably want the user that. It seems that their uh, the pdx changes. But we do not see consensus updates. Then. Uh, that would mean that the client is online, but it's not the exact same. So there are a few things that we can reduce from from these messages. Now, if we were to remove this, the Dvd. Exchange  and the beacon client is not yet synced, that essentially we would lose all communication. So the consensus Pride will have anything to tell us until it actually stinks up. So from our perspective it would be like it doesn't even exist. So this is again, it's a nice side effect that it's a hardly tracker between the two clients, so we could definitely remove it. But then it might be interesting to consider, adding some Api to somehow try to diagnose, or that if something's almost wrong or something's just  so, if something is correct. But on I think there wasn't really a reason to do it. It's it's more like we if for us it was to for knowing that we didn't know from the catalogs what's happening, whether some people were actually running the theand it was very annoying for us, because we always have to figure out. Okay. But okay, is it really good that this software is to be combined on being a state. And that's why we added over these warming, so that the user connections see that know that it seems operational, and the compliance seems not operational. But I think it was. It's just a user experience. Nice. It's not really needed for everything, and i'm assuming that's why it wasn't really ever added, because there was no need for it,

**Micah zoltu:** and that that I want you to describe sounds like a pretty strong need to me,  having the sense of client regularly. Say, Hey, i'm here, and this is my status like i'm doing this like i'm sync, or i'm sinking, or i'm initializing just having that information the execution client allows, actually declined to give better information to their users, which is valuable. 


**Berlin EF office:** I can't agree, so I think it would be nice to have some cross. I mean the consensus, but it can always query us because they haven't the Api, but the other way around them, so maybe it would be nice to expose some some synchronization. The synchronization states from the census prime back down the the execution by so we can have also backlogs. So i'm all for specing that now it's more meaningful.

**Mikhail Kalinin:** You mean synchronization like a scene process status, i'm. Propagated from Cl to Yale.

**Berlin EF office:** I can imagine any and any sort of information in there, but that's the the one that media them, to my mind, is just like the sinking status initialization that that is so. The life cycle of access client right, is you? You're doing boot up. You're initializing You're setting things up. Start your services, Yada Yada Yada, and then you start sinking, and that's going to take a bit, and then you finally are synced, and you're following and just having at least those three seems like a good sort.

**Mikhail Kalinin:** Get it

**Berlin EF office:** (43:30) so the only we can debate what information will be useful and just the ideas that since the concern scribe is driving the whole thing, the Execution alliance, they only they don't have any option other than to wait for information to write. But if no information is arriving, we just don't know what we got. We don't print anything to the user whereas if some status updates were periodically shared, but at least we could decide whether everything is five or something wrong. I think that's useful,

**Tim beiko:** I guess. What's the best place to like spec this out. Continue this conversation. Figure

**Mikhail Kalinin:** appropriate, and n api execution. Api is yes, sorry, eh? Or A. Pr: Okay, Yeah. So I guess at the very least, we can open an issue there highlighting some of these concerns.

**Tim beiko:** Yeah, Then we we can add a Pr. Today.

**Berlin EF office:** (44:40) And I guess such a thing could be rolled out, even if you don't need to synchronize across five to roll it up. We could define this optional endpoint right by optional. I mean that eventually it would be part of the spectrum. Everybody should implement it, but it shouldn't get a problem if a client doesn't speak it yet. And then, if you just everybody can make someone, whatever they have time. And then it actually is.

**Tim beiko:** (45:10) Yeah. And I think this also kind of leads into the conversation around like versioning the engine Api, which was sort of happening in the chats. Yeah. So thinking about how we want to have optionals and potentially different just versions of the Api.

**Berlin EF office:** So with versions, I don't want to say I've opposed to versions, But I think we should really really consider if it's really necessary, because the moment it happens that clients need to seek multiple versions and then Ok, gas can speak virtual one to F three, and then we can speak first from two, four, and six, and you might end up in your scenarios where these rent some weird. So if we want to do versioning, I would say that maybe you should just use versions at a temporary of great path. But we should not really plan on supporting more than one in the long run

**Mikhail Kalinin:** when I was like thinking about version, and I was like thinking about something similar similar mechanism to what we have in the it's a protocol Ah! With like support, and the version that is supported by the the counterparty. So some exchange what version is supported by Cl and El, and whatever is the minimal version of the two, should be used for a communication. But you also should consider hard works. So and yeah, optional methods and methods that that are not related to directly to like consensus stuff. Um like these did application of payload bodies. They are like kind of not going to be affected by any hard work, and they can be deprecated as well, and some new methods can be introduced, and that's why I guess we need version in. Yeah. But I I think we should take this discussion from this call into an issue or a discord. It's like going to be a long one.

**Berlin EF office:** I just a very quick response to that. But I think the ease packages, versions is a perfect example of why, personally, is bad and specifically, there was a point in time and get spoke. At least four or five different versions of the Chronicle, and every single other clients wrote a different one. So we essentially the only way we could stop supporting all the clients is that we work on the Acd. Phones and the research this code. And we just announced that. Okay, you guys have one year to fix this one and a half years to about this, and we had to promote that, and we just enforce that. So we kind of use. That's a way to decrate the old protocols, and that was super bad from gas perspective, because all these old protocols had different data models, and that our database we couldn't operate our database because we had to serve some other client on some weird person. So that's why I was saying that if we want to use merchants to as a temporary operation, so that Ok, why, we are only not version, so you can also use version, one that's going to be fine, but I think we should really force people to pay after everybody upgraded to person to that proper. So one So Pt should be more like a transition rather than supporting in the long-term.

**Tim beiko:** Okay. So yeah, And we can continue this conversation on the engine. Api Repo. Any any closing comments on it? Okay. Anything else on the road? Okay, Um.

**Berlin EF office:** So ah, with the verge Ah, behind us. Basically We we kind of held off discussing Shanghai for the past couple of months too much, because we were all quite focused on the merge. Um.

**Tim beiko:** I think on the last see i'll call We We discussed that. The some teams feel like taking a well-deserved break right now might be the way to go um, and potentially have a best less awkwardives over the next month or so. The Cl folks have a great to already. Panic skip the call before and after Devcon. Obviously we'll skip the call during devcon itself. But that gives us at least, you know, three weeks, and potentially more like five. If we decided to also skip the next alcohol nerves, it would still be good to try and make some progress on, not necessarily like deciding exactly what goes into Shanghai. But the verity is understanding. What are the different things that are being considered? How we want to? First of all are those things like technically sound. Are there any issues with them? And then are there like higher level priorities that we want to focus on, and to perhaps try and have this happen a bit more, Async, that we usually do. So I've put together a proposal on the magicians for this at a high level. We could use these magicians as a way for Vips to signal, but they'd like to be considered for Shanghai. Most cips already have these magicians thread, because that's where discussion happens anyway. Um, And Basically, we can. We can kind of keep this list as a reference point for client developers and researchers to look at, and they give to the different proposals. And I think if if there's eits where we feel like, we need to have, like a deeper discussion or something like that we can organize ad hoc kind of breakout rooms with the people who are most interested in them. Um, and and kind of share those um, but kind of have a month or so where we're not necessarily having like awkward as call or cl calls, and and making it decisions about what goes in the forks. So people have a chance to just take a step back. Um rests, and also consider things from a bit of a a higher level. And Then there were a couple like other ideas around, like potentially just having like using the Discord Palace party lounge when we usually have awkwardives, and the sale calls for people to come and try about this stuff, and maybe having an extra discord channel as well. But I guess I just like at the high level. I'm. Curious how do people feel about just taking roughly a month and and not having these call schedules and and trying to do this a bit more asynch any thoughts There, I see Thanksgiving. You have your hands up.

**Ansgar Dietrichs:** Yeah, I just if you want to say, I think in general that makes sense. I just think it's important if we want to have this a bit more like a relax time where basically people don't feel like they they miss out on decision making. I think it's important that we actually also kind of structure it that way, So that basically Um, if we I at basically I would be worried if we go too much into actual kind of decision-making territory asynchronously basically, like including high level priorities, like what? What what kind of kind of workshop. Can I be? All these kind of things, I think, are better left for then once we return to to synchronous communication, one um, and also like Ip discussions. If it's basically people have to be afraid that if they miss out on those, and then they come back, and all the decisions or and the apps are already made. I think that it basically negates the purpose. So I think kind of if we just leave it to posing all the earpiece that are on the table, maybe going into them a little bit, taking them on soundness and whatnot, but like if it's just me, try and refrain from from kind of like talking too much about relative priorities, and what should and should not go into Shanghai. I think that would otherwise. I think it kind of lose the point.

**Tim beiko:** That's that's worse than ours. Well, I think what? And to be carry out what I meant for like having calls and lots of spiky ids is some of them do have like technical things to dig through, and you know I'll I'll take an example. We've been doing a lot of work for it for four recently. It's not about like. Does this go into Shanghai or not, but it's more. You know there are things with the eip that still need to be specified or whatnot, and that's that's more like the being goal is to give up.

Greg Colvin: I don't. I just strongly suggest that people go and start reviewing eips. A lot of a lot of them have been sitting there for a while, so people could have forgotten about them, and asynchronously people can get looking at the eips on the magicians and start actively reviewing them. I think most of them are at the review stage are very late drafts, and that's something we can do asynchronously and really help on the decisions.

**Tim beiko:** Yeah, I think I think that's that's reasonable. I shared the link in the chat about the eips that have already signaled this. There will be more, because, first of all, we hadn't really agreed to this yet, and i'll also make sure to reach out to anyone who'd like previously signaled for Shanghai to make sure they're like where this is what you were doing, so you could expect this list to grow in the next week or two, I guess. Does anyone like strongly disagree with this approach? Not, I guess, in terms of just like logistics, and I think we agreed to keep the consensus there. Call next week, because first we have stuff to talk about, but also in case you know we see some merge stuff coming up, you know, in the first week of an option. It'll be good to have this this place to discuss things. Um. I would suggest that we kind of remove the Al Qaeda's on the twenty ninth, unless obviously, if there's a major issue on on May that you know some sort of emergency level thing. You can always bring it back that we like default to remove it. Um. So that we that would mean we basically get a month to basing. So we would have um. This this call on the twenty second of September. Uh then no call on the twenty-nine. They'll call on the sixth. Defcon is a week after that. No call on the week after the death con, which is usually a bit slow, anyways, and then we would resume our cordabs. Um! Two weeks after that. does that sound reasonable to people? Okay, I will go with it. There's no objections. And then I think the last kind of bit was, Mika you've advocated for like a Shanghai planning channel on discord. I think the pro there is. Obviously, we can maybe move the conversation a bit forward. In the meantime, the con that I can see, and why i'm a bit hesitant to do it is again, if if we're like forcing client team to monitor, and that if they're not looking at this channel, they kind of miss like, you know, a big decision about Shanghai that might go against like the purpose of things. Um, we obviously have operatives we can use to discuss this stuff already. Um. But yeah, i'm curious. If client teams feel strongly, even like channel like this would be quite beneficial, or actually potentially like harmful or distracting, just because they then need to monitor it and make sure like, yeah, they haven't missed something there.

**Micah zoltu:** So I think it having this channel. I would like it, even if we do take a break like once the break's over, I think, having the channels there, it's valuable. Not necessarily just, for during this break, like, I would like to. Yeah, Okay, I personally, okay, yeah, would support it much more strongly if we only turn it on after the break. Basically so that we like for the next four weeks client devs don't feel like they have to monitor that constantly, and like otherwise, they missed like this scope and shape of Shanghai changing. But then, when we actually get talking about that, I I think it's reasonable to have such a channel. Yeah,

**Tim beiko:** I mean. And anyways, we can reconfirm that in a few weeks, but, like anyone else, have a suggestion or a strong opinion on this. Yeah. So I posted a link to the each magician spread on the agenda for today, and and my guys are coming to the chat that we could just shut down all of this, for if we want to force vacation, I don't think it's like necessarily forcing vacations, but I think it's more like we can have. People spend time on. You know what they want, and if that includes vacation. That's great, and also feel like if they're not following as closely for two weeks they're not missing like. Oh, this major Eip got included in Shanghai, and

**Micah zoltu:** it it feels to me like we could. There would be value in having a place to do to talk about these things so that way. Once we do start shing I plane efficiently. We've already work through some of the conversations that are likely to occur. There would be, i'm, totally on board with no decision making power happening during this time. I still think that the value in those of us who don't take vacations, being able to go,

**Tim beiko:** I think it's things I think I would use a party down for that, so I think we can have like an unofficial meeting. Ah Weekly at Fourteen Atc in the party lounge on this board, and there very much. Our people who want to work on this stuff twenty hours a day, seven days, a week, fifty weeks, fifty, two weeks a year. So I think, Yeah, that's fine as well. I think we can yeah have like a a soft chicken like a soft age of that to use a party lounge when we would usually have the court apps or Cl calls no objections. I think it is. Yes, um, And then the last thing I had somewhat related is at thefcon we're putting together another session similar to what we did in Osaka. Um. It kind of has a conversation about the theorem roadmap to kind of answer questions from the community. To have people who like want to talk about specific Corey. I keys have a chance to organize um. So if you're a kind of and planning to attend devcon, it would be neat if at least folks from like most teams, could send people for a couple hours to this. I think the community really appreciates. When we have these in-person sessions it helps clarify a lot of the scenes we do here. Yeah. So I I posted again the the link to that in in the chat. Um, We don't have a specific time, but I think the default schedule will be going out in the next week or two. So once that's out i'll, i'll share it there. Um if you could expect to last a couple of hours and be quite similar to what happened in Osaka. Was there anything else anyone wanted to shout about.

**Berlin EF office:** Oh, yeah, This request, if we are a natural one we are going to discuss in Shanghai and essentially going forward. Is that because I think you've been filing a lot of complexity in the whole system with this with the merge, and it would be nice to also just pause a moment and try to figure out what thing this merge allows us to now remove from the from the clients. And one specific thing just to give an example is that essentially after the merge everything. That's. most clients still implement this plotable and sense a system where you can have two before you have a priority. And now I have to go. State, However, if you have to take this one step forward and create a group of authority like behavior, So the engine Api that are centralized official air clients to get without their entire logical consensus model, which would be a lot of road thrown out the window. So, for example. This is a a case where it would require working up it. Then creating a tiny spec for running the authority, we can change what to say, but it has changed. It would allow you to move in a lot of code from the exhibition clients, so I think it would be nice to. In the shortish. There are future to grant folks and these kinds of things to where we can. Ah not only keep filing new stuff on top, rather also practical existing stuff out there are not. The

**Micah zoltu:** is that something that someone could do like as a hackathon-type project where they basically spin up something that looks like it, says the client, from the point of view of the execution layer, and it's but it's just a group of authority

**Berlin EF office:** like you said that I'm saving it if you think I think Yes, so I think it's. Probably you need to think about it a bit, and my assumption would be that it would need to be somewhat similar to click just operating on the engine Api level. But if somebody, when you think through it, i'm. More or less confident that it can be done in a very short amount of time.

**Tim beiko:** Uh, proto. So you have your hand up.

**Protolambda:** Yes, so this is exactly how you think about layer two as well, using the engine Api to not have to modify Gf or other excretion layer clients as much, and rather to create the block production and the consensus outside of the modes. If so, money is around there in. If Berlin, then i'm definitely done to help port our for clique to such external software. So

**Berlin EF office:** super,

**Tim beiko:** i'm anything else. Okay? Well, I guess we can wrap up. Yeah again. Congrats everyone on the merge. Amazing work. It went down. I think, more smoothly than even people here expected. Yeah, it's it's It's been great, and i'll see some of you at Devcon, and otherwise. See everyone here on the all cordes on October the twenty seventh


00:05:38	stokes:	gm
00:05:43	Abdelhamid Bakhta:	gm
00:05:51	lightclient:	good merge
00:05:58	Tomasz Stańczak:	good merge
00:06:00	stokes:	good merge
00:06:02	Tim Beiko:	gm
00:06:07	lightclient:	grand merge
00:06:22	Tomasz Stańczak:	let's merge sth more
00:06:27	Tim Beiko:	ther grand merge
00:06:30	Tim Beiko:	The Grand Merge
00:06:31	Tomasz Stańczak:	le grand merge
00:06:51	Abdelhamid Bakhta:	4844
00:07:08	lightclient:	oooooooooooooof
00:07:16	Micah Zoltu:	4444
00:07:23	Marius:	progpow next?
00:07:28	stokes:	no
00:07:31	Tim Beiko:	no
00:07:33	Tim Beiko:	veto
00:07:40	Marius:	sad
00:07:44	Tim Beiko:	sfyl
00:08:00	Pooja Ranjan:	Micah with Panda dp!
00:10:23	Micah Zoltu:	🐼
00:10:55	Micah Zoltu:	Everyone was asking for a more up-to-date profile photo of me, so I complied.
00:11:23	Tim Beiko:	https://github.com/ethereum/pm/issues/616
00:12:26	Ansgar Dietrichs:	what if we merge with ETC next
00:12:27	Ansgar Dietrichs:	bring home the lost child
00:12:45	stokes:	ETC as a rollup
00:12:57	Micah Zoltu:	If we rollback the DAO hardfork.
00:13:22	Ansgar Dietrichs:	let's just give every user the average of their two balances
00:18:14	Daniel Celeda:	:)
00:18:21	danny:	is this comedy???
00:18:25	danny:	loll
00:18:29	Micah Zoltu:	Reality is a comedy.
00:18:43	danny:	indeed
00:19:35	danny:	do we suspect the 4% drop during the merge to be related to besu?
00:20:50	Fabio Di Fabio:	idk, some Besus needed a restart, but I can't quantify the share
00:21:37	danny:	might be an interesting leak of besu usage by validators but unclear
00:23:44	Micah Zoltu:	Do the ETHPoW people have bootstrapping nodes?
00:25:29	danny:	it clearly doesn't seem imminently requisite
00:26:26	Ansgar Dietrichs:	could we just not do it at all?
00:27:20	mrabino1:	now that we are at a PoS consensus... when do we plan to reduce the time  (block followi) for new validators ... especially if we are finalizing…. thx..
00:28:32	Micah Zoltu:	I like cleaning up wonky.
00:29:35	danny:	otherwise, I'd say do after devcon and before Nov 18
00:31:28	Chris Hager:	https://github.com/flashbots/prysm/blob/develop-boost/beacon-chain/blockchain/execution_engine.go#L296-L301
00:32:15	Micah Zoltu:	I thought CL call was cancelled?
00:32:26	Chris Hager:	sry ^^
00:32:31	Tim Beiko:	Not next week, one after
00:32:58	Chris Hager:	https://boost-relay.flashbots.net/
00:33:11	Ansgar Dietrichs:	I was separately wondering about execution payload history deduplication (not storing a copy with the CL and EL each) - would that also be a better fit for next week's call?
00:34:53	Micah Zoltu:	Does fixing withdraw merkle tree generation count as "post merge cleanup" as well?  😬
00:35:07	stokes:	you mean deposits?
00:35:13	Micah Zoltu:	Sorry, yes.
00:35:26	Mikhail Kalinin:	i'd say it does
00:36:13	Mikhail Kalinin:	we should figure out how to version and update Engine API as well, this is required for any further hardfork  or Engine API upgrade
00:37:02	Tim Beiko:	Does someone have a link to that PR?
00:37:03	Mikhail Kalinin:	The PR https://github.com/ethereum/execution-apis/pull/218
00:37:12	Tim Beiko:	Thank you!
00:38:28	Pooja Ranjan:	Now that the merge has finalized, can we please agree to replace TTD with transition block number everywhere?
it's simpler and TTD imo doesn't make much sense outside PoW
00:38:38	Pooja Ranjan:	^ Artem
00:38:45	Tim Beiko:	Thanks!
00:42:04	MariusVanDerWijden:	*warning
00:42:08	MariusVanDerWijden:	*warnings 
00:43:07	danny:	ah, interesting
00:43:33	Mikhail Kalinin:	though, currently EL clients may be modified in a way that they don't even start syncing before receiving FCU from CL client
00:44:07	Mikhail Kalinin:	In this case checking terminal block hash isn't necessery
00:47:22	Micah Zoltu:	Engine API
00:48:26	moody:	why does the EL need to query the CL for this stuff? can't it just print to logs just to report nothing coming from CL?
00:49:21	Micah Zoltu:	The EL can't differentiate between "no CL connected" and "CL is connected and doing stuff but not telling the EL about it".
00:49:48	danny:	I have to run early. sorry! awesome work everyone. talk soon
00:49:52	Micah Zoltu:	Which means the EL just looks like it is frozen, because all it can do is wait, and users think that their EL doing nothing means the EL is broken (CL likely has logs happening).
00:49:56	moody:	if the EL logs say in the logs it hasn't seen anything, that's a good signal to user to look at CL logs
00:50:27	moody:	i don't think EL should try to diagnose the reason the CL is not giving it updates
00:50:41	Ahmad Bitar:	I believe if there are breaking changes in engine API, they should be introduced in new methods. and if EL does not reply to the newer method, the CL can fall back to the older version
00:54:01	Tim Beiko:	https://ethereum-magicians.org/t/shanghai-core-eip-consideration/10777
00:55:26	Ansgar Dietrichs:	+1 for the party lounge, always a great place
00:55:29	stokes:	+1
00:57:39	Tim Beiko:	This is the list of current candidates btw: https://ethereum-magicians.org/tag/shanghai-candidate
00:58:36	Micah Zoltu:	I don't like vacations, but I have already lost that debate I think.
01:01:36	Micah Zoltu:	We could just shutdown all of Discord if we want to force vacations.
01:03:41	Tim Beiko:	https://ethereum-magicians.org/t/ethereum-magicians-protocol-roadmap-gathering-devcon-vi/10866
01:03:42	Micah Zoltu:	I think I'm the only one who objects to a vacation so I won't object anymore.  😆
01:04:01	MariusVanDerWijden:	Thanks micah
01:05:14	Ansgar Dietrichs:	I think no one objects to you not taking a vacation, Micah - I am sure all the client teams are already looking forward to returning to a big pile of prepared Micah comments on potential Shanghai EIPs in a month! :-)
01:05:28	Micah Zoltu:	All of history!  (see 4444)
01:08:30	Abdelhamid Bakhta:	🎉



