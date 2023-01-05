# Ethereum Core Devs Meeting #149
### Meeting Date/Time: November 10, 2022, 14:00 UTC
### Meeting Duration: 1 hour 30 mins
### [GitHub Agenda](https://github.com/ethereum/pm/issues/652)
### [Video of the meeting](https://youtu.be/ZZx7d14vE10)
### Moderator: Tim Bieko
### Notes: Alen (Santhosh)

| Decision Item | Description                                                              | Video ref |
| ------------- | ------------------------------------------------------------------------ | ------------- |
| 149.1 | We will move 1153 to CFI to try it on the testnet with the help from the Uniswap and and Optimism folks. We're trying and improve the test coverage as well | [1:14:07](https://youtu.be/ZZx7d14vE10?t=4447) |


## Intro
**Tim**
* Good. Good morning y'all. Good morning. 
* Welcome everyone to All Core Dev #149. Hopefully YouTube is working. if not, this is being recorded and I can upload it after. But, yeah, a lot on the agenda today. I think high level, trying to figure out what Shanghai looks like is probably the main thing. and there's been some, bunch of work on the EOF side on the 4844 side. 
* So you can share some updates on that. And then there were a lot of other EIP that wanted to be considered for Shanghai. so I told all those people to show up today. so there's four main ones. Micah, you also had this agenda item about just talking about the fact that running an node is getting, more resource heavy and, that we should address that. so we, we can talk about that as well before, the, the Shanghai inclusion conversation so that, you know,  we have that context, assuming we get through all of this in less 90 minutes. Mikhail had a quick engine api, proposal that he wanted to discuss. and
* I think one thing that would be valuable is then talking about how we approach DevNet for Shanghai, if we have a good feeling  for what's likely going into the fork. and then there are a few other topics. So, mostly just, how we think about Sunsetting Robson and potentially testnet were generally, and some updates on execution specs and the tests, generated for the execution layer. I guess to get started, last Friday there was an EOF call. does anyone who was there want give a quick update on, sort of what was discussed and, and where things are at, with EOF right now? 

**Matt**
* Tim, you broke up a little bit there. I don't know if that was just, Oh, Sorry. 

**Tim**
* Yeah, I was just saying, does anyone, who is anyone here who was on the EOF F call, last Friday and, and wanna give a update on, on where things are at with that? 

**Danno Ferrin**
* Was I the only one there that's on this call? 

**Lightclient**
* I was there first hook ups, I was there as well. 

**Danno Ferrin**
* So a lot of it so circled around the debate of big EOF versus little EOF one of the big takeaways is we're gonna target the Ethereum JS test nets Shandong, and we're gonna try and target big EOF is our first and preferred approach to ship EOF. Shandong, is a test net. Tim wrote up a document showing that it's kind of on a parallel track. 
* It depends on everything in Shanghai may or may not includes deposits or not for the test net, but in essence, Shanghai is the most important what's driving the release, which is deposits and the other features, which would be, 4844, which is parallel to the EOF the big EOF changes, depend on Shanghai. And the premise being, if we can get things proved and shown working on Shandong and tested and all the clients implementing it, then we could move it into Shanghai if it's early enough. 
* And if it's not early enough, it moves out. So that way, we've decoupled development and validation of shipping it from whether it's part of Shanghai. So the discussion about deposits could be on a separate track. all we included in Big Shanghai was just relative jumps and function. We did not include, the, stack verification, because that's still kind of in beta, so those are the only two big things we added into EOF. but those do, change the nature of what the EOF container looks like. And because there was a desire to only do one major change in the next X number of years, we want everything, it's an EOF big from everyone on the call speaking for the people on the call. 
* So let's just do it in EOF big and ship it as soon as it's possible. 

**Lightclient**
* I dunno if I missed this part, but I thought stack validation was part of EOF big, like it's listed on the Epsilon EOF list. 

**Tim**
* So on the call, I think they said it was just not quite ready for implementation. 

**Danno Ferrin**
* And the thing about stack validation is if we do everything else, you can still write code that validates the stack and you can still get the benefits of linear compilation with a subset of stuff. the validation API would just reject stuff that didn't match that. So, that can be added later. And the real issue is it's not, particularly specified, in the specification way. It only has a reference implementation. So I think that's what's holding that one back. 

**Lightclient**
* I don't know. I mean, what do you mean it's not specified? There's the EIP I've mostly implemented the EIP at this point. 

**Danno Ferrin**
* The specification  says is, you know, check the stack high to each instruction for something that's, deterministic and repeatable. There would need to be an algorithm to find that this is what you do. And the algorithm that is in the reference implementation is actually not linear. It's like order and squared or something. And so there's better stuff. So it's not quite ready to ship would be the conclusion. 

**Lightclient**
* Okay. yeah, I don't know what the like timeline of making it ready to ship it, it felt like to me that this is something that we can like resolve relatively easily. Like all the other EOF EIPs have, like some small changes that need to be made just now that we're under this assumption of bigger EOF and those are things that are straightforward, whereas, you know, if we don't ship the stack validation, we do have to increment another EOF version since it would be possible to deploy contract code that stack overflows, whenever you do a call up. 

**Martin Holst Swende**
* Can I just make a question here, to dump it down a bit? so whether or not stack can overflow not from, I'm thinking from like pure EVM perspective, that's a pretty, negible check. Is it important from like other points of views such as, you know, verifiability and, and analysis? 

**Danno Ferrin**
* So if done rights stack validation can allow for Greg Colvin, linear compilation time to transp pilote it to something like machine code. 
* So if you have, if you can prove that, and that also provides a subset that then if you have stack validation tools like Solidity and you can only create, EOF it can only create EVM code that can be linearly done and it gets rid of a lot of compiler bomb attacks for people who are gonna try and jet it. it's, you know, Java has perfected some of this and brought it into their compiled process and they've got the same rules on their jvm.
* It's really, there's like a whole section on their spec about that. And that's I think one of the reasons I'm a Go ahead. 

**Martin Holst Swende**
* No, for any, for any compiler, they can always validate the stack, right? So what, and that's my argument is enforcing stack validation on contract deployment, which only makes a difference on run time or well, if you analyze live code on the blockchain, right? 

**Danno Ferrin**
* If you reject yeah, if you're gonna be rejecting, stuff that doesn't validate, 

**Martin Holst Swende**
* Sorry, are we going to reject stuff that doesn't validate or are we not gonna validate? From my perspective as like having go ahead, you know, building the EVM, I think the performance gain of knowing that this stack cannot be overflown is negligible. So therefore, I'm wondering is there some other aspect to this problem where this actually makes a difference? 

**Danno Ferrin**
* I kind of can concur why I don't think it has to be in, the Epsilon folk who were writing it. I think that was Powell. he, he kind of agreed that it wasn't quite done yet. As far as the EIP Yeah, there's a skeleton specification out there. There is reference implementation, but it's, you know,  he seemed to feel agree that it wasn't done and was happy with it slipping out. 

**Lightclient**
O* kay, That's fair. I think that it's just like, you know, one additional thing that a small amount of work could make, make it so that it's ready and we could avoid having, you know, this immediate thing that we might wanna make a version change to in the future, Right? 

**Danno Ferrin**
* The change is not proposed on the big EOF but that's not what we're focusing on right now. But if a finalized algorithm comes in that is linear and specified, you know, that's, that's what is needed to move it forward. And I think that's what he is working on, Right? 

**Tim**
* Like it's possible to add this to EOF Devnets that's basically, if it gets ready, before, before Shanghai, right? 

**Danno Ferrin**
* Yeah. Or whenever big ships, Right? 

**Tim**
* Yeah. Andrew, you've had your hand up quite a while. 

**Andrew Ashikhmin**
* yeah, we briefly touched it, on Friday, but I would like, to highlight that one important, task for the big EOF is, support and solidity. So that would both verify that, that the EOF makes sense and we can compile Solidity contracts into it and also ensure that there will be some real, contracts in production. Cause like, I would like to avoid having it on as a theoretical, thing that nobody uses. 
* And yeah, to my mind that's another thing, like not only implemented in all the EL clients, but have it like full good, good production level implementation and solidity. 

**Danno Ferrin**
* Yeah. But I concur it does have small EOF support, which is relatively simple. So the big EOF splitting into functions is not a, a small compiler change. 

**Lightclient**
* So I mean, if we're gonna hold EOF to the standard, I think we should think about holding other EIP to the standard. And I don't think that historically we have required a production level facility implementation for things. and I generally feel that, a commitment from the Solidity team that this is a good thing that they plant to implement it is usually, usually suffices. 

**Andrew Ashikhmin**
* The problem with that is that what kind of, reiterating merits is concern is that if we have some, like if we accept yours, that will be in the standard forever and then solidity commits to  support it. And theoretically then, it turns out that because of some crack of the EOF, as is they cannot fully support it and blah, blah, blah. So we'll have to have a new version of EOF, but the the intermediate version, stays there forever. 
* So that, that's to my mind, that's a very important change to the EVM. So we need to have sanity checks on it.
* One of the, so I see support not as something, not as an extra, but as a sanity, an essential sanity check. 

**Martin Holst Swende**
* Can I just, so I mean Alex Peri, isn't he both very involved in the EOF and very involved in Solidity. Yes, and I think, I don't know if he or Chris, one of them is, is like the head of the, that I think may be wrong here, which to my mind kind of speaks that yeah, the Solidity team are probably very well, you know, person aware in this proposal. 

**Tim**
* Yeah. And the, I believe Daniel is, yeah, 

**Andrew Ashikhmin**
* I would say, I would say that just awareness, well, at least that that's my position, that awareness is not good enough. like, a working compiled compiler, into EOF without dynamic jumps is like, to my mind at least, it's like  a requirement before releasing it to the mainnet. 

**Marius**
* I would kind of need it for testing anyway. So I would also really like to see,

**Tim**
* And I think, yeah, so I, posted this in the chat, but generally I think, the perspective was there, like, they supported like the first few EOF EIPs it didn't affect it much. the second ones obviously require more work, but they seem generally, yeah, supportive, although it's not clear, like it's easy for them  to support it. 
* So, we can definitely talk with them about it more. and, yeah, I don't know that any one of them is on the call right now, Respond to the comment. 

**Micah**
* My client made a bit of growth that we don't, hold other EVN changes. I think the difference here is that those other EVM changes are usually really small and everybody is quite confident that Solidity will have no problem implementing them.
* Whereas this change is quite substantial and there is non-trivial risk that Solidity will not be capable of implementing this reasonably. and so getting solidity this one first gives us that confidence that, oh no, there's no, there's no hidden gotchas or unknown unknowns anymore. 
* Like it can and has been implemented solidity, there's mitigates all that risk. 

**Lightclient**
* Honestly, I was referring to 1153 whenever I mentioned this. 

**Micah**
* Oh, which one's 1153? 

**Lightclient**
* This is transient storage. 

**Danno Ferrin**
* Oh, okay. How does this kill 1153? I'm missing that. 

**Lightclient**
* Well, if we're going to require Solidity to have the implementation done in a production manner, there's no in of 1153 in Solidity and it doesn't seem like there's intention of making an implementation the near future. 

**Moody**
* Well, they got it. I mean, I don't wanna speak for them, but they did say that if it's approved and goes in, they will implement it. 

**Lightclient**
* Right. But now we're saying that we're not going to approve things until it's implemented. 

**Danny**
* So I think there's a level of complexity that there's concern about on this other one. if there's a similar level of complexity of concern on 1153, then I would also maybe block on it, but I don't know if that's, the perception here. 

**Martin Holst Swende**
* Well, Chris did express, concerns about the complexity on 1153. Unfortunately, it's not on the call. 

**Moody**
* I mean there, it's also implemented inr, already, so it's a bit strange. Which one is index on 1153 is already in Viper T store and T load. 

**Danno Ferrin**
* It's much simpler than the container and getting rid of dynamic jumps. I mean, I, 

**Micah**
* To be clear, I don't, feel a need to, has to be solidity, but I do kind of agree that we should see some compiler implemented successfully. And so flow 1153 isn't funded by Viper. For me personally, that kind of meets the bar of this has been proven that there's not a bunch of unknown unknowns that we need to worry about anymore. 

**Tim**
* So I think, and you know, we, we don't have to make a final call about EOF or 1153 right now. I mostly just wanna make sure everyone sort of knows where things are at. it probably makes sense to move on given, how much time we spent all this already, but at a high level, client teams are working on implementations for, these four EIPs, that we listed earlier. 
* So, the two original ones, 3540, 3670, and then the addition of 4247, 425050. the other one for stack validation, we have some implementations, but it still needs some work. And then, so Solidity support is obviously an open question. Anything else anyone wanted to share on EOF? 

## EIP-4844 updates [20.31](https://youtu.be/ZZx7d14vE10?t=1231)

**Tim**
* Okay, I guess the next one, I'd like to get a quick update on, is just 4844. So I know there was a call, this week for that as well. So, yeah, does anyone here who was on the call wanna share a quick, update on where things are at? 

**Protolambda**
* I can give a short update and, others can chime in if I miss anything. So on Tuesday we had an 4844 implementer call. I believe the devnet v3 is on track, and we are targeting end of November. So after Thanksgiving, 
* I believe the last crypto APIs have been merged, but then there's some open discussion on whether or not to, share a precompatiable implementation as a whole, as a shared library to not have to do the decoding of the points on the client site or like in the EVF implementation rather than in the crypto library. And then I, believe Terence is tracking the open b2b, changes on the consensus layer. 
* There are some optimizations we can make there, specifically the branching part of the fork, where we can have many different beacon blocks. We have something called beacon block by route to fetch blocks on the existing beacon chain, and we may want an equivalent of that to fetch. And then there is some discussion of whether, or not to couple the, beacon block and block fetching with this by route method. And I believe those are all the, the big updates. 
* Also, the EIP was updated with, some parameter changes, which are still in the discussion. And then going into the testnet and with the further testing of mainnet performance of call data and so on, I think we get the data to decide on the parameters for, 4844,

**Danny**
* And specifically I think the block by route is a blocker, and rebase on Capella is a blocker, blobs by route I think generally has consensus, and I expect to be merged soon. although there might be a finer point around how deep you serve those requests. And then the Capella updates that are blocking the rebase being finished. We're gonna wrap up today. 

**Tim**
* Thanks. And I think also, like on the last call when we discussed this, we mentioned trying to like, iron out the final sort of design, PRs in the EIP. I believe these have all been merged, so like the fee market changes have all been merged. and there's was a PR also to change the output of the pre-compail. I'm not sure if it's been merge or not, but that might be the only outstanding PR on the EL side, that affects the actual spec. I don't know, is Ansgar here? I'm here. Yeah. Do you, did you just wanna get a quick update on just the, the PRs so the EIP itself? 

**Ansgar Dietrichs**
* Sure. So at least, last evening, I haven't had it. I, so I haven't had look at, but I, I don't, the precompailer was not in merge, but it's, it's, it's ready too merge, right now, because of a small issue with the EIPs repository every, PR to the EIPs, not only needs, author approval, but also, an EIPs editor to estimate it . so it's a little bit slower, but basically there are, three, PRs at least that, that I was involved with. One is just a small, change to, so that the, the pre compile, the point evaluation precompile, it used to only take basically return, like just basically it just used to revert,  if it was invalid or not revert, if it was valid, but not return any values. and now it was, it's supposed to return the, degree of the, polynomial and also the modules, of the field. so that's change one that's, that's ready and just needs to be merged. then there's a second change just to, decrease the, throughput, of, 4444, 
* I think basically everyone agreed that if we, at least as long as we we're still optimistically targeting, Shanghai 4844,we would want, to start, with lower throughputs just so we don't have to to worry about, node load and network load. so that's still pending. And then there's a third one, which is, basically, a bit more open for discussion on whether or not we would want to introduce a minimum price for blocks, lower than the, higher than the theoretical minimum of basically one, one way per per podcast. that ones unclear whether or not people end up wanting to even do that, but that will also just be one constant change in the, So that's, EIp that's the three spec PRs that basically i, I have a view on. 

## Increasing Operational Cost of Running an Ethereum Node [26.20](https://youtu.be/ZZx7d14vE10?t=1579)
**Tim**
* Thanks. any other questions? Comments on 4844? Okay, I think, yeah, so the next thing I think it probably makes sense to, to cover is, Micah, you had, commenting the agenda addressing sort of the increasing the operational costs of running a node. do you wanna take a few minutes and maybe walk through what you see as the issue and, Yeah, sure. 

**Micah**
* So the, to preface, I'll give a short little spiel to set the stage. My, my hope here is that we can walk out of this with, a more consistent vision on kind of what we're, what we're trying to build. I, I feel like it's, it's kind of, fracturing a little bit. And so, I don't, I do have a personal opinion on what want, but I would rather see us be consistent on what we all want rather than any particular stance. So I think right now, if we round the nearest inte, about 0% of users run their own node. And when I say users here, I mean people who are using Ethereum to do something that might be by and selling NFTs or trading tokens or whatever. 
* This means that about a hundred percent of users are using centralized services like infire and El Camin and whatnot. The many of those pop those centralized services are actively censoring right now, like today. they censor people from a number of countries that really could use cryptocurrency, and they also censor, a number of tools that are really good for privacy and stuff like that. And so we, we have a, this kinda censorship problem, and it's been slowly growing over time. And, during that time as it's kind of slowly kind of built up, we've been focusing a lot of our effort on scaling. And at the moment there, there's lots of, lots of blockchains out there. 
* They focus on scaling bsv swan, you know, they focus on scaling and they prioritize that over censorship resistant, meaning people being able to actually run a node. And so I feel like 4844 is, is kinda another step in that direction that we've been on where we're prioritizing scaling at the cost of censorship resistance in the case of 4844. 
* This comes in the form of 4044 is, is going to increase the storage cost requirements of running a node and the network cost requirements in a, if this, EIP to change it, 5 8 63, or sorry, it this pr to change the throughput. that helps a little bit, but it is still strictly an increase. So 4844 is going to decrease the number of people who are capable of running their own Ethereum node from 0% to a smaller 0%. we do have some stuff, stuff on the back burner that's been working on very slowly, which is virtual tree statelessness, history expiry, state expiry. these things have been worked on for quite a while. but we keep prioritizing other things over them, unfortunately. And so they're taking a very long time to actually come to fruition and make it onto Ethereum. And during that time, you know, the, the size of the state continues to grow, the throughput continues to grow. 
* Gas prices or gas block gas limits have been increased a couple of times, I think over the past few years. Right. and we just keep, you know, keep kicking this cam down the road. And I think that at some point we need to stop and ask ourselves, do we want a high scalability blockchain or do we want. 
* Blockchain that people can actually run themselves. And if we choose that we want the censorship resistant blockchain that people can run, then I think we need to take steps to say, you know, anything that makes that situation worse, we should wait on until we have solved the problem of making some people gonna actually run their own node, whether that's like clients or, pipes portal network or state X free or history X free or statelessness or virtual trees or whatever that looks like. there's lots of options here, but I think that if we continue to not make the choice to prioritize those things, we're going to continue to make the choice to prioritize scalability. And that scalability comes at a cost. And we're paying the cost every time we do it. And it's a little bit at a time each time, right? So a little, this 4844, it's going to decrease or increase operational costs a little bit. It's gonna decrease the number of people who can run their own node a little bit. 
* And it's the same as almost everything before, you know, increasing the block gas limit, it increases at operational costs a little bit, and these little bits just add up over time. So what I'd like to see, see us decide is, you know, do we want to kind of make the assertion that yes, we understand that we're sacrificing censorship resistance for scalability, and that's an intentional choice we're making and we do plan on fixing it, but not today? Or is, do we want to focus on censor resistance today and sacrifice scalability and make that trade? so yeah, like, like I said, I, I have a personal preference. I'm for sure everybody here knows what it is, which is like your primarily about sensory persistence, but I'd at least like to see us kind of agree that we care more about scalability today than we do about that. A little bit of extra, sensibility that comes with 4844 and similar. Thanks. So that's my speak. 
* I'd love to spend some time talking about it, but I know we've got limited time, so I'll let Tim take it from here. 

**Tim**
* Thanks. Yeah, no, I think that was, yeah, I appreciate all the other concepts, all the contexts there. yeah, let's just use the hands to go through the comments on this. so Andrew, you were first. 

**Andrew**
* Yeah, from my perspective, we can do both.  we can try to, like to my mind, scalability is important and, we can reach, better network participation with, light clients version two or three. Whatnot, but I would like to, to to comment that, we, to we, to my mind, we can achieve both if we concentrate on, fundamental like fundamental improvements. so I would, for instance, in Aragon, we, we are still working on snapshot think sync, and then it'll allow us, to support things like, history expiry of like, to be precise, more precise, but our, capacity is limited. So I would rather avoid, tweaking guest schedule or trying to optimize guest schedule things like, 1153, which, thinks that don't contribute either to scalability or censorship resistance because, they bog us down and we are not able to concentrate on making fundamental engineering improvements. 

**Tim**
* Thanks. Ansgar

**Ansgar**
* Yeah, I just wanted to say that, I generally appreciate kinda my sentiment.  I think in our general course makes sense kind of being pragmatic and in compromising. I think we have a good long term, roadmap where at the end state will be one where it'll be very, cheap and easy to run, your own local nodes. And that is absolutely important. LikeI would hundred percent agree on that. Like in the long run, the concentration would not be acceptable. but I do think that it's sensible to, to be willing to compromise to some extent, in the short run or pragmatic reasons. And I think we are decent at this. I think, for example, with the current gas limit, there's a lot of headroom that we could have right now of increasing this, and we, we are not, I think and that's the right choice. and then also with something like point 4844, it is explicitly designed to have constant cost for not operator. So there's no growth, which is the main problem with all the other, load. 
* So  I think that makes a lot of sense. I would agree that say for 4844 a lot of people want this to be dependent on a fully decentralized, history provider system being live. before we would move forward with this, I think this is a big mistake. I think we could, we can literally, like, once it's implemented, and I mean as we just heard, of course, clients would need some time, but, but I think once it's implemented, I think we should just move forward with it, because it would be the, the biggest gain for remote operators. But again, basically my point is I think Ethereum's cause of being a bit in the short run, but having a very strong vision for the, for the long, long run, Makes sense. 

**Tim**
* Thanks Ansgar. Dan? 

**Dankrad**
* Yeah, so my first comment is like, I wonder in some ways if this is the right forum to discuss this because this seems about like the strategic direction of Ethereum. So I feel like, the right place to take this is the community and not a call of like the engineers. but since Micah have brought it up, I do want to comment on it. And I think like my first most important comment is I think like, the current, the, the resource consumption is not currently the main reason why people don't run ethe nodes. It's UX of all kinds. it is of course the state, itself that you have to download that, but due to your UX problem, but like this, I think 484 4 is so mar marginal in terms of like  for node operation at the moment. 
* I mean, it will be very different when, when we, once we have full statelessness that I just don't see it as relevant. I don't, I don't think it changes much for people who run nodes and most people don't run nodes because it's so much more convenient to use one of the centralist services. and not because they can't run, run a raspberry pie. And the, like, the other argument here is like, so what is decentralization, right? There's both like running and node, yes, but there's also using Ethereum and right now, like the cost of using Ethereum is typically much, much higher than the cost of running a node. and that excludes much more users than the cost of running a node, which mainly is the UX problem as I mentioned. So like, I find, I find it weird and I think like Micah is like in a very, like, I mean, I think already the e community, if you see it on a global scale is is on quite, a strong position towards decentralization. 
* Like very, very few other chains if you look at them are like, care as strongly about decentralization as we do, which I do care. Like, I mean, I'm working on many projects to make this better. but, but the, the arguments like that Micah just brought are like in the absolute extreme direction even within that community. And so like, I feel like, like we have to be a bit more programtic, here and prioritize people actually being able to use Ethereum.

**Tim**
* Thanks. And, yeah, Martin was saying in the chat basically the same thing with regards to the UX being the blocker rather than necessarily hardware requirements. yeah, you have to jump. So I just wanted to share that. 

**Lucas**
* Lucas, I have a question because, my knowledgeable two is limited, but would 4 8 4 4 actually increase internship resistance? Because not, you don't, you not only would have to censor like native Ethereum transactions, but also those blobs, which might be kind of hard to censor because they, they are, they don't have like a, a fixed, structure. That's the question. I don't know the answer. 

**Micah**
* I think it just, it moves the opportunity for censorship to the L2 itself. So if an F and L two is strongly anti censorship, enter anti censorship and they implement whatever's necessary to make that actually happen, then I, I suspect that the blobs, like you say, kind of makes it opaque instead of transparent. And so when someone, you know, adds just an L2, it's blob to the chain, it's much harder to notice that L2 is maybe doing something that is sanctioned or working with someone from a country that's not allowed to use Ethereum or whatever. Yeah, exactly. And now when we are having multiple Ls, we increase the censorship resistant because you would have to cens around all of them, right? To be actual censoring. Yes. And this is, I would say that as I'll, I'll leave my comments till the end. 

**Tim**
* So if anyone else wants to say something Then is your hand still up from the Oh no, sorry. Anyone else have any thoughts they wanna share on this before mic close mic please. 

**Micah**
* So there's a couple of responses to a couple of those, the comments that were made there. so engineering is a finite resource. While we can theoretically work on multiple things in parallel, and we, we do, engineering resources that are put to other stuff is engineering sources that aren't being put towards censorship resistance stuff. And that includes things like UI UX, like someone, someone could be building another nethermind actually is to be fair, working on their packager thing that packages, beacon and execution layers together. but you know, for every engineer they have implementing 4484, that's an engineer that's not doing something like that, whatever that that other thing is. and so I think that we, we need to consider that this isn't just like 4484 specifically, this is anything that is not addressing the problem is taking away those resources that could be addressing the problem. the other thing that I wanted to comment on was that I'm not, this is minor. I, I'm not super convinced that the costs of prohibitive, I think for certain use cases, like if you're living in a third country, you're probably not gonna use Ethereum to buy your coffee. but maybe you could with the payment channel. but you might be okay to receive your, salary every, every two weeks, via the crypto via Ethereum. And the fees are not so high that I think that's prohibitive, especially if it's just east. and then the last thing for the L two situation, I generally agree that 4844, has potential to kind of, you know, help L2s along and L2 are c sensor re persist. That helps there become cen persistence. The problem is, is we currently have no L2. if you define L2 as something that actually gets a security from Ethereum and is not sensible, currently every single L2 that is live except for one which has no zero users is centralized in some way. Like it's got, admin keys or back doors or whatever. And so I'm, I'm hesitant to lean on the, oh, we make L2 better and then all of a sudden our censorship problems go away because currently no one is built actually building or has, no one has actually built and launched, I should say, and actually censorship resistant L2 and you know, it's, this has been like this for what, a year or two now, and they keep saying they're going to and no one does. And so it's concerning to me to rely on that as a solution to this problem. 

**Tim**
* Thanks. I think, you know, one thing that's like probably quite doable is, you know, the, everything that was mentioned around like the UX of running the node, like sure it does also require engineers to build this stuff, but it feels like it's probably more paralyzable because we don't necessarily need core kind devs to do this type of work. so that's, you know, probably something that's like worth exploring more, like are there different dev teams or contributors that can help with this specific problem that are sort of adjacent to client teams and, and not basically, you know, we're not as resource constraint, constraint on them. anything else on this topic? Okay. next kind of big thing is, there were a couple more EIP that people wanted to discuss with regards to Shanghai. there's four that kind of got, mentioned. so high level, we had this self-destruct 1153, the transient storage, the BLS pre, and then EIP 2294. I'm sorry, I don't have the the title off the top of my head. but you can just go through them quickly in order. so is Jared here? I know Jared was looking into the self-destruct EIP. 
* I don't think he's on the call. Does anyone have an update on the self destruct EIP? 

**Andrew**
* I'd like to make a suggestion about the self-destruct eip. maybe we can, list it as, CFI for Shanghai because we are considering it. And to my mind, a good thing would be to have a block post on, on Ethereum about that, about self destruct that, we are seriously considering it and if any, and that, that that developers who rely on this, functionality, should screw basically start screaming and, highlighting their use cases and then, then we can think about mitigations because if that there was  one pin contract, but if that, that one is dead, if nobody screams, then maybe it's not a big deal if maybe we might, disable certain contracts. But if they're dead anyway, then why not? 

**Micah**
* So, so there currently is one, at least one person who is screaming like they're doing exactly what you want. We,announced that we wanted to do this and they were screaming saying, this is going to break my thing. 

**Andrew**
* Okay. Can you, is there a blog post or something? yeah, I got actually check what's the, the details of the smart contract and if there are potential, Oh, okay, I see the link. Okay. 

**Micah**
* Yep. Okay. One option is if, if this is the only person that screams, and this is, and we do some research, we find that's the only one. I mean, there is the option of just irregular state change to fix that one, as a potential workaround. And I think, I think we asked them and they said they would be fine with that. I might be mixing up my a though, 

**Marius**
* I'm not fine with having an irregular state change To fix. Sure. 

**Guillaume**
* No, but if I understand correctly, that person is also, I don't think we need a state change for this. He just, like he's creating, contracts and then self-destructing them in the same transaction. We don't need to actually change the state. That's, we just need to make sure that when self-destruct is being called during the, during a contract creation, then it still works as it used to basically. 
* So there, there are, there are paths around doing something as ready as a stage change

**Micah**
* Are, are you sure this is the guy that, or the person who I thought they were, they self obstruct was in a different transaction from Z Create? 

**Guillaume**
* Yeah, I didn't check. I know, I know of a guy who's called Rob, he's working for some, I forgot the name of the thing. yeah, I'm on mobile right now, so I can't check the, the link sent. That's fine. 

**Micah**
* And this person's name is Rob something else, so it feels likely it's the same one we're talking about. Maybe I'm just missing saying what his contract's doing. 

**Guillaume**
* Well, if that's not the same person, then we have two people screaming. But, yeah. Okay. thanks for pointing that out. 

**Tim**
* So does any, I guess does anyone disagree with the idea of like announcing to the community that this is something we're considering in having some sort of like outreach, you know, both telling them to like post on each magicians, but then also, you know, maybe having some calls or whatever where we can discuss this and like understand what, what breaks and and whatnot. does anyone think like, we should not do that? if not, so I, Ansgar had some comments in the chat about like, moving this to CFI is probably premature. and we might want to like wait until we have a final spec to do that. so I think, you know, what I would probably recommend is, yeah, quote unquote being louder.  
* I don't know if like an EF blog post is the right way, but definitely like at the very least we can reach out to like a bunch of projects. 
* Matt says he was looking at the list of, all the contracts that sort of could be affected by this. we can then reach out, you know, to those contract creators  if we can find them. so I think it is, you know, it is possible to do more on the outreach side that we've done. yeah. Oh, sorry, 
* Yeah, Jared said that, but yeah, I guess, yeah, is there some objection to just doing that and, then potentially updating the EIP with, you know, with with changes, and I don't know if this means we can do it for Shanghai or not, but at the very least we can signal that we are gonna be deprecating, self-destruct, and, and try to accommodate, yeah, accommodate as many of the like edge cases as we can. Okay. no objection. So I, I'll take some time to, to look into that and like, yeah, follow up I find with, with Jared as well to, to try and reach out to all of the, the contracts that are, that are affected. 

## Proposal to include EIP-1153 in Shanghai #438

**Tim**
* Okay, next up is 1153. so we have, I believe a couple of the people who've been championing on championing it on the call, Moody, or, Sarah, do either of you wanna give a quick update about where things are at with 1153 and, and, yeah, we can go from there. 

**Moody**
* I think Mark time away from optimism is, 

**Tynes**
* Hey here. Cool. So, real quick, what is 11? What is EIP 1153? It adds two new op codes in this concept of transient storage. So there's t store and T load, and basically what transient storage is, is it's very similar to storage, but it is in memory. the two op codes work exactly the same way as S store and S load, except they, they write into this transient storage in memory. And this, the storage only lasts for the duration of a transaction. You know, it persists between call frames, which is different than regular memory, and it's name spaced by accounts just like storage. And both of these OP codes cost 100 gas. So let's talk about the benefits that it provides. 
* So, one common use case would be using it for re locks, and let's look at like the data for Unop v2 if UNI V2 is using transient storage for its reentry lock. So today on main net between one to 2% of all the gas used is the V2 router. And this, the re lock has been triggered 26.7 million times in the last year. And with, you know, 2100 gas per load, and we assume that there's an eth price of 1100 and a gas price of 50 gray that would, you know, switching to transient storage in, instead of using regular storage, it'd save users 3 million usd per or $3 million per year. And not only would it save users money, but it would also just save, you know, disk lookups like the hardware itself. 
* We can also think about, you know, if we designed some sort of dex aggregator or AMM from scratch that uses transient storage, a lot of the accounting itself can be moved internally instead of having to do the accounting externally in contracts updating their storage. So for example, we can look at, in Unsa v3, trades that are, that contain more than one swap. So they're kind of like multi hop, token trades. in the last year there's been 2.1 million transactions, with an average of 2.26 swaps per transactions or per transaction. So what this basically means is, we can remove calls in S stores, from these intermediate, you know, tokens and we can do all that accounting kind of like internally. And if we kind of naively look at unap B3 using kind of this sort of style, we could have saved users like, you know, 1.15 million, dollars in the last year. 
* And that's just looking at unswap b3, like if you kind of really think, from first principles and design a d aggregator or an using this style, you know, we think that we could make it extremely cheap to kind of do like these multi hop, token trades. another thing is that the storage refund accounting is pretty complex and requires developers to do weird hacks in kind of setting values to from, being set to unset. And it kind of is this like leaky abstraction. So we think that, you know, if we can convince people to start using transient storage instead we can start cleaning up the tech debt and moving away from the kind of these like hacks that developers have to do to save gas. And another interesting benefit is, and, and there wasn't consensus on this in Bogota, but I do believe that if self-destruct is banned, then when trying to paralyze execution, you only need to rely on the storage slots being touched. 
* So if people start moving to a world where they use more transient storage instead of storage, especially for ency locks, then I do believe that we will be able to paralyze more execution. And we understand that adding additional features to EVM will, result in like all of the ecosystem needing to upgrade their tooling. for example, like there's like a lot of formal verification stuff out there that will need to be upgraded and kind of take this new feature into account. but it's like not that different from storage. So, it shouldn't be like, it shouldn't break all the existing tooling in like a really crazy way. and just note that EOF will also require the tool to be upgraded. And kind of as a final note, 1153 has already been implemented in Besu, Nethermind, and Ethereum Geth, and there's a comprehensive integration test suite in the Ethereum test repo and all of them pass it. 

**Tim**
* Thanks, Mark. Mark, sorry. okay, Andrew, you've had your hand up for a while. 

**Andrew**
* Yeah, I think in general it's a good Eth but I see it as an example of a, Geth gas at tweaking. So, which might be okay, but we need to weigh costs versus benefits. If it's something trivial like  coin base, sure that's a no brain, it's a couple of lines of code and it's easy, but here we have to prioritize it against fundamental improvements, like Eth 4844 force. And, because fundamentally if we manage to decrease gas costs significantly, like, I dunno, by to two times or what not, that's a much bigger win than optimizing it  by 2% my two 10. And also it'll say like, if we spend time on, things like 1153, then the more time we spend on things like that, the last time we, we spent on refactoring out, like cleaning up, refactoring out code base, making performance optimizations and so on. 

**Tim**
* Thanks. Dankrad.

**Dankrad**
* Yeah, I mean like, I don't know much about this particular EIP, but like the argument of like, oh, it makes re-enterence blocks easier. Just makes me wonder, is there a point that you get 80% of the value using something much simpler, like simply one flag you can set for the, on a contract that's transient? Like, do you actually need to build a full scale storage system or is this complete 

**Moody**
* I would say that re logs are just an easy example. and if you, if you look at like uni swap, protocol design, you can do a lot of things to like say token transfers. If you take advantage of transient storage. for example, when you do a multi hop swap, that means like swapping across multiple pairs. you're not actually changing the overall token balance of the intermediate tokens in the unit swap. So you can completely get rid of those, those S stores and those calls to that, to those intermediate tokens. if you take advantage of this transient storage, which is really just transient balance changes. So, I think there's a lot of like, like real protocol innovation that can come from this, which will just open up a lot more block space on L one. And, and I don't think it's just like a, you know, like a, I don't see it as just a 2% increase  in the block gas limit. 
* It's that that also like scales to L twos, l twos benefit from that additional block space. So it's anything that helps oh one, just is multiplied by however much L twos can can scale L one. 

**Tim**
* Thanks. Daniel. 

**Daniel***
* Yeah, I just wanted to add something from, from Besu side. So 1153 is one of the very, very few EIP that has been implemented by external developers for us. And this is really something that, that, that does not happen a lot. And I would like the, the other clients maybe also  to reconsider that they really did the hard work and that, and not only just implemented the prototype for, but also for minority clients. And I would like to use 1153, like as a role model to say that people look, if you want your e included soon, maybe do the same, maybe go to the minority clients as well, implement the prototype yourself. And like this, maybe we really, in the mid and long term, we really could gain because we get more external developers and like this, we could really also get in more features by hardwork, simply by having more developer power on it. 

**Tim**
* Thanks. Yeah. I guess Moody or Mark, do you wanna maybe just take a minute to talk about like yeah, all the implementations. I know you briefly mentioned it at, at the start, but like what's the state of the implementation across the different clients? and Sarah just shared also the, the PR to Ethereum slash tests. 

**Tynes**
* Yeah, totally. So I believe that, Geth has an open PR right now, between Besu and NetherMind. I believe one of them is merged and one of them is still open. the Ethereum js PR has been merged for a while now. I do think one thing that we could do to kind of, show that all the implementations are correct on top of having them pass the integration tests, which they already passed the integration tests, is running basically like a, a multi-client test net. that's something that we haven't done, but that is what seems like the next logical step to do and kind of proving out that this works. we're also working on a fun little ctf, that uses transient storage in a really interesting way that we plan on launching very soon on a test net. just to kind of get something out there and show like what's possible with using these new op codes. And we're hoping that, you know, the community can have some fun, you know, playing around with this and, you know, solving this like, on chain puzzle. 

**Tim**
* Thanks. then Craig again, I'm not sure if your hand was still up from last time. if so, then Lucas? 

**Lukasz**
* Yeah, just a quick here on the, my point of view from this PR. So I will, I managed, we managed the PR but before that I managed to have a very detailed, review and actually there was some back and forth to like improve,  some things based on I think performance and our general, I'm not sure if it was like any, cuz it was some time ago if there was any like, issues with it or just like, maybe just some smaller improvements I would have to check. And I was also suggesting implementing, some tests at some point, which were done, but I haven't validated them. So I would say the main effort here would be validating if the, if this test should, of course, apart from each, each client validating their own implementation, validating that this test should, is good in terms of its coverage that it covers every case. 
* And yeah, running proof proving this with a testnet would also be helpful. Like with external testnet, that would be, another thing that would, is the burden. 
* And so the question is, more in rather than like the throughput capacity problem of engineers is more if we generally want that to be included in EVM and, potentially how well tested it is, rather than, which in my opinion is a good candidate for like, some future improvement that, instead of like, if you, if you really want something included and there is a consensus that we want to include this at some point, instead of, like pushing everything on the core devs, if you can like, actually provide value here by doing part of the work yourself and only leaving the validation to the core devs, that might be something good and something that actually helps the community. Right. And yeah, that's, that's it for me. 

**Tim**
* Thanks. and Marius, you had a different opinion about, this, the chat, so please. 

**Marius**
* No, actually, I have a kind of the same opinion. what I just really want to make sure is that no one, actually believes that like only because someone showed up and did the work that this change is going to go in. I think it's very important to validate every change on, on whether this is actually a good change, not whether  it is ready. I think this change is actually a good change. 
* I am not sure if, it will increase testing and it will make, if we want to schedule it in Shanghai, it will make Shanghai, even harder to test. especially because we have like a lot of other EVM changes, right now considered for inclusion. And, all of these EVM changes kind of interact with each other. 
* And so we need to, we need to test, the, the interaction and we need to test that everything is working. just from the feeling I have is, I would say this is, it's not important, not as important as other changes and it's, not worth, the increased testing effort and maybe the delay of Shanghai for, but I'm still on the fence so I can also be convinced otherwise I guess. 

**Tim**
* Yeah, I, you know, I'd be curious to hear just from client teams, like it seems like the rough feeling is, you know, people think this is generally useful, it's unclear, you know, yeah. The relative benefit of this versus, something else. but yeah. Does, I guess, does anyone feel like we should basically give this precedence over something like EOF which is probably the other big change that for the EVM that's been considered for Shanghai, because I can imagine, you know, if we didn't do EOF in Shanghai, we could probably do this and vice versa. so I dunno. Yeah, I'm curious to hear from client teams if that's the right way to think about it then if there's like a strong preference either way. 

**Lukasz**
* I don't have a preference or anything, but this is, this is a lot smaller than than EOF as a, as a whole of EIPs. This is, And right. 

**Tim**
* Yeah. So yes, I, I agree with that. And I guess, yeah, do, you think, so say we did have EOF in, is your view that like, we probably don't have space for something like this, is that correct? 

**Lukasz**
* So I dunno what the, from Nethermind perspective implementation is finished. So in terms of space for that, there's no problem. in terms of testing, I haven't validated the test cases. So if someone from core development, would do that, that would give us more visibility, how much, more is needed, there's definitely, value in running a test net with it. so, but yeah, that's, it's my opinion. So it's hard to say how much effort that would be from the testing point, right? Because if the test case are already robust, then there's little work. 

**Tim**
* Got it. Any other team have a opinion on this? yeah, Danielle? 

**Daniel**
* Yeah, I think from, from pesticide also, mainly the testing effort that we need to put up. As I said, there is already a PR I think we need to do some, some small changes to it, but more or less is ready. But it would mainly from our side be that the traditional testing effort, nothing more. 

**Tim**
* I'm curious. Yeah, Nethermind. Sorry, not Nethermind. Aragon, Andrew, I know you were saying like this is probably less of a priority and  I don't know if there is an implementation in Aragon already. So is this something where like you, it would slow argon down significantly or can you take also from Geth what's been implemented there? 

**Andrew**
* I think we can, benefit from Geth implementation because our EVM implementation is still quite, similar. yeah, I mean if I kind of also on the fence, I would rather not do it, but if the majority wants to do it, then we of course implement it as well. Or let's say I would rather not do it in Shanghai. 

**Matt Nelson**
* Right. And I guess, yeah, maybe this is like, I dunno, it's hard to pre-commit the stuff in the next fork because we, things change a lot. But like, is this something that we should basically try and get alongside the devnet we're building for Shanghai and see if we're happy with the testing and all of that, or you know, should we, should we basically soft degree, to do it in the next fork, assuming we can, we can test it and, and you know, the implementations are, Yeah, I mean, so to this is Matt from basically to echo what Daniel was saying, I mean as far as the minority clients are concerned, it's straightforward. 
* I would love to see it included in the test networks or at least in some specific multi-client tests like we're standing up for withdrawals. so if the tests, yeah, if there's agreement that the tests are robust enough, that we're just shared, I don't see an with at least attempting, right. if it does add complexity in, in light of some of the other changes to the EVM, or unforeseen things, with these kind of test nets, it could be useful to push. but again, it just depends. 

**Tim**
* Okay. And so I guess, you know, Sarah Moody and Mark, you've been like doing all of work on this in the past few months, obviously. if we were to say like, you know, let's try and add this to Shong, and you know, see how multi client testnet work  and you know, if we need to increase testing coverage, is that work that you can sort of own such that it's not like the core client teams who have to do the bulk of it? 

**Moody**
* Yeah, definitely. Yeah, absolutely. 

**Tim**
* Yeah, I, so I guess, I dunno, based on this, my feeling would be like, we should probably make it CFI added to Shong and like see how the testing goes and assuming it's a minimal effort on the part of Pine teams and we're happy with testing we, we included as part of Shanghai. if for whatever reason, you know, we find the testing is is too complicated or that when, you know, interacting with EOF or whatever, there's some weird issue and, and we'd rather do EOF, we can always like remove it, but it seems like if, I dunno if, if like the unit swap and and optimism teams are, are willing to help and like champion this, it's not really a ton of additional work for, for client teams. And yeah, it doesn't, it seems like everyone sort of wants, this is just a question of do we have the resources to do it? So does anyone disagree with that? 
* So making it CFI trying to, to get it in in shong and sort of reconsidering based on how, how well that goes. 

**Pawel**
* I have like small issue of this, because I will not be like from EVM one, I will not be able to have combined tests, having this because that's the way where the transit storage is placed is like kind of outside of the AVM API have, so I wouldn't be able to participate in any like, testing that has both features enabled. 

**Tim**
* So this would be just for EVM one? 

**Pawel**
* Yes. 

**Tim**
* I don't have a good feeling for 

**Moody**
* Could I ask, is that like, an implementation thing we can help with? 

**Pawel**
* I don't think so because like it's like on the client side to have that, so I kind of need to redesign the API that's that kind of plugins the EVM And, But it's like minor issue in the sense like if one doesn't like participate in the testnet, but if, like, yeah, it'll be really annoying for me if the status like kind of have all the features suddenly enabled. I don't know how to like figure out the, like the current testing with this, but So we Can try to figure out later like just, 

**Tim**
* I guess, yeah, and I, I don't know, it feels like we've never really blocked something on that and also just, yeah, it like, especially cuz a commitment is just to move this to the test nets and I don't, I would probably still lean towards doing it unless I don't know someone else have like a strong objection to that. Okay. So yeah,  I say yeah, let's, let's move 1153 to CFI try it on the test net with the help from the UN op and and optimism folks. and,  you know, trying and improve the test coverage as well. yes, CFI, and, yeah, we, and then yeah, we can see in the next couple weeks how the devnets go and, you know, if there's any issues that that come up from there. and I think it's, it's sort of again, reemphasizing like ideally this should take kind of minimal bandwidth from client teams and, if this is like a way we can get external contributors to bring your whole change in,  that's a really valuable thing. So we should, yeah, should try and get that done. Anything else on 1153? 

**Tynes**
* Nothing else to add from our end, but yeah, thanks for, you know, making space for us. 

**Tim**
* Of course. Yeah. and I,  assume you're all in the R&D discord, but we can use the channel there to chat about this stuff and, and the DevNet. sweet. 

## Proposal to add EIP-2537 (BLS Precompile) to Shanghai #343 [1.15.18](https://youtu.be/ZZx7d14vE10?t=4518)

**Tim**
* Next one on the list was, we've talked about this many times in the past, BLS pre, 25, 37. there's like many different people championing this. maybe Alex, I see, yeah, I you're on the call. Do you wanna give a quick update of Are at Me, Alex? 

**Stokes**
* Yes, theres, yeah, everyone. So yeah, I think many of you have seen this EIP in the past. Essentially it's adding BLS arithmetic to the EVM. there's like many, reasons we'd want to do this. you know, we could have like more secure snarks, we could start verifying any messages from the consensus layer, which unlocks a ton of use cases around stick pools. lots of good stuff like this. So, yeah, I think historically there were some concerns around implementations, but I think those have pretty much all been resolved. Like if there's any like, concerns around stability of the underlying code, you know, this stuff has been used on the layer for many, you know, quite a while now. so yeah, so I think, the question now is just like, do we wanna push for this in Shanghai? 

**Danny**
* I think an important, so chains that use bls, we could have like client support in main net, I think in a very important second order effect is that EVM change would likely adopt these changes and thus the beacon chain could then be like client tid in there. It's kind of a weird reason to do it. Cause you know, the fact that it's on main net would then make it on other EVM chains, which makes main net interfacing with other UBM chains potentially safer, is the argument. But there's a lot of other essential use cases and reasons here, other than the fact that, you know, at this point this is just a native Ethereum crypto curve that we can't natively use inside the, I guess, yeah. 

**Tim**
* I'm curious from client teams, does anyone feel like this is something we should be prioritizing in Shanghai? like obviously there's value here. We've been talking about it since the burden hard fork. yeah. Does anyone think this is when we should be prioritizing given I guess the other things in Shanghai that we could be doings? 

**Marius**
* So I actually think this is, more important than some of the other things in Shanghai. I would like, I think this is, it enables a good amount of new use cases and I would say it's more important than things like EUF or 1153. but that's just my personal opinion. I'm, from the kind of the testing perspective, there's a way harder to test than, some of the other changes because it involves the, I think eight or nine pre compiles. and, we have seen in the issues with cryptographic, libraries, we've seen in the past us, issues. so all of these analysis, us analysis are like very old at this point, so we need to rerun them and, yeah, so I'm, I kind of think it's, it's very, it's good. but I think it will, like if we do this, then we will definitely delay Shanghai. yeah. Got it. That's my general feeling. 

**Tim**
* Jared

**Jared**
* Hey. I just wanted to, chime in, and say that I had, drafted an EIP 5843 for, expanded, modular arithmetic in the EVM. and it's not really a competitor  or, to the  2537, but, just, chiming into, maybe ask for, to, to just say that maybe we should consider something like this to, potentially implement some of the cheaper operations that would be covered in 2537, just as a food for thought. and this is, this EIP is something I've been working on for quite a bit and has, been around the idea's been around, it was previously, called EVM 3 84, about two years ago. so yeah, just, saying I've been working on that on and off. And, just to add that in there, to ask people to consider that, that as a, route to maybe also get some of this functionality in the chain with little added overhead versus some of the peak balls. 

**Tim**
* Marius is your hand up for another comment? Yes. 

**Marius**
* Yeah. Quick question. which of the operations could be solved with? So right now, like the BLS EIP has, as I said, like nine, different, pre-compiled. And if we could get that down to maybe only the pairing pre-compiled and solve everything else with the, the stuff, I'd be really happy. 

**Jared**
* Yeah. so Yeah, so  I was actually looking at, I think my, 5843 to answer the question, from Alex in the chat. a draft of an EIP and I'll, I can link, more resources about it. But, I guess in short, my understanding is that, the elliptic cur, so, scaler, multiplication in addition, so G one ad G two AD G and the G one G two mole, would be fairly competitive. And I started to put together DOC about that, that I have not finished yet, but, I can, I can try and release that fairly soon. I know, so there was an implementation of the pairing, back in when with the EVM 3D four spec. but my understanding is that it's like significantly, like on the order of three to four times slower than blast, but I don't have a a pairing implementation in the current spec. but I can, yeah, I can, put out some more information about this pretty soon. 

**Tim**
* So, I feel, yeah, we had a similar conversation when we were doing Berlin and then BLS ended up not making it in because of potentially doing 384. is that, I'm curious to hear from client teams, like the people think that's still worth sort of waiting for, or at least, you know, and we can discuss this again in the next two weeks. We don't need to make a decision now. but yeah, I'm curious how strongly client feel about either way of, BLS. 

**Guilaume**
* Yeah. I would say we're, I mean the guest team, I think I speak for the guest team when I say we're not a big fan of adding more pre compiles, simply because curves change and if you have nine pre compiles that you have to keep maintaining forever, that might be a bit of a, I mean, it's not great. So I think it's worth at least digging, you know, into suite four and see if we can, if we can, make it work in a reasonable timeframe. I understand BLS is here to stay, but you never know, like, you know, the research keeps happening that you get more, newer ideas, better ideas.  I think taking two, two extra weeks to to consider it would not be wasted time.

**Tim**
* Antonio. Yeah. 

**Antonio**
* Just quickly my opinion about what, Gim said.  I agree that the crew change. The ones like we are using this exact same curve in the contents layer, so it's kind of, if it changes, we have a, I mean, if, if something in research happens that make BLS 12 3 1 obsolete, we have a problem in any case, right? To, so for the moment, we don't know. We think BLS 1221 is the state of art group, but so was BN in the past and things changed pretty quickly. But again, keep in mind that this group we used in the consensus later by all the clients at the moment, Right? 

**Tim**
* So I guess, yeah, just we we're running against time, I think given that it probably makes sense. So yeah, spend just two weeks looking at the potential M 384 up code also, you know, progressing on, on all of the other Shanghai stuff. And then, yeah, we can discuss this, I think on, on the next call. Does that make sense? Any final comments on, on BLS? Okay. 

## Proposal to add EIP-2294 to Shanghai  #645 [1.26.23](https://youtu.be/ZZx7d14vE10?t=5183)

**Tim**
* Last EIP, that someone, wanted to bring in was e i P 2294. and, Zainan Victor be is your handle, hopefully I pronounce that right, yeah, you wanna take a minute to talk about it? 

**Zainan Victor**
* Hey team. thanks everyone. so, can you hear me by the way? 
* Yeah. So just wanna quickly shift the light. This is, EIP 2294, proposes, abound on the, chain ID. I discovered this is because I was trying to implement something and realized that Chan ID was not very, specifically, formalized in 1155. And when I dig into the history, there is a bunch of it, and one this seems to be a, a proposal for, for, for years. I like to know the context why it was not prioritized, and it seems a simple implementation, but can have a lot of benefit now. what adds to the urgency is that if we are envision a, shouting multi, like chain, world chain ID will, explode. 
* And I wouldn't be surprised if people started to do things like cash, something with chain id. 
* So adding a bounding, as currently proposed by the previous, EIP author, was using what's founding it under 200, under 64 bits. So you can imagine if some people start doing cash is definitely going to break it. so want to ask people's thoughts about whether we should prioritize this or, I personally feel strongly about that we need to prioritize making at least a decision. and then whether it is, 64 bits or 254 bits is up to debate. Yeah, thanks. I'm done speaking. 

**Marius**
* I think it's, we, we don't really need to prioritize it. It's not a breaking consensus change. we can have a soft fork for it. And from my point of view, like I don't see anyone being against this. If there's anyone against it, then they should speak up. But, otherwise we can just say, let's do it. 

**Tim**
* What do you mean by let's do it, 

**Marius**
* Let's implement it in the clients and just ship it whenever, like there's, As a software as long Fork consensus? Yes. 

**Tim**
* Okay. So, okay, so then given we're gonna be implementing a lot of stuff that needs consensus in the next few months, my suggestion would be, we just talk about this in like three to six months when the Shanghai work is pretty much done. 

**Micah**
* Does this actually need to be talked about? other than just like, just people saying yes, like this is very similar, I believe, to the non limiting where currently this is effectively already in place. We just need to make it official. We need everybody to say Yes, I agree, and then we're done. I think. 

**Marius**
* Yeah, exactly. That's what I wanted to say's. No one disagreeing. 

**Zainan Victor**
* I see people asking why this 256 bits is because the word but also the bound of 64 is that if it might not break the consensus layer, but it can break the application layer quite a lot because of how, the non  and the signatures were calculated. And yeah, just like in case people did agree without deeply thinking about it, I personally want to ate it, but hope that is a stronger consensus of 

**Andrew**
* Yes, I would include it into, Shanghai though it's not, necessarily a protocol breaking change just to track all the changes. So we can kind of loosely couple if, it with, Shanghai for trackability. 

**Tim**
* But I guess the question is should we do this now? Is it trivial? If it's trivial to do, then maybe, but in the chat we're sort of discussing the fact that there's way too many things considered for Shanghai now. So is is like putting that additional load on teams to do it? 

**Micah**
* Yeah, we don't think In this call to do it. That's, that's it. There's no additional load on teams. Like no one else has to do anything for Shanghai. We just say that officially this is the rule as of Shanghai, But I mean, it's effectively been the rule for all the time. Like we, we could, we could assert today that this was the case since the beginning of Ethereum. it was very similar to the nonissue. We literally just need people to agree that yes, this is, this is the thing. no work needs to be done, no code needs to be written. 
* There are some, probably some places we could improve some code, but that's just tech debt that clients can pay down whatever they want. 

**Tim**
* Okay. Does anyone disagree with that? 

**Danno**
* So just because no one's used, over 64 bits, we can't use it ever again. I mean, I see no value in limiting this and I see, don't see how it impacts main net. 

**Tim**
* Okay, then, okay, given that we're at time, I think if there's like any amount of contention we should just talk about it offline and, and try to like, we can even make a decision offline once we're all on the same page, but yeah, we're already sort of at time. 

**Tim**
* And I'm guessing the only decision we need to make is 2 56 or 64. 

**Tim**
* Yeah. Yeah. And once we've made that, then we can, yeah, we, we, we can just kind of signal it, but yeah, let's not have this conversation here. yeah, and that sounds good. If you wanna follow up with Dan, that's, probably the way to go. okay. 
* I think, yeah, so we're not gonna have time to cover everything in the agenda. I think one thing that's probably worth covering, we discussed 4844 in the call before the like CFI conversations. and Lightclient was saying, Well, given you know, what we're doing with the EOF EIPs, we should probably make them cfi 42100 and 4750. does any, I guess, does anyone disagree with, And actually before that, the other part of the conversation from the chat is that it's probably unrealistic that we can do EOF 1153, BLS 4844 and withdrawals on an, so we probably need to like prioritize for a subset of that that we can spend most of the next call. 
* So discussing that. but yeah, generally do people wanna move either of these two EOF EIPs, or for 4844, the CFI, the people strongly disagree with any of that, and if we can't get quick agreement, we can discuss this on, on the next call. 

**Lightclient**
* I'm not sure 44844 is in a place to be CFI yet. 

**Tim**
* Yeah. Okay. if anything is like a bit contentious, we, yeah, let's not make, let's not move it to CFI today then, but I think we should move the EOFs ones to cfi. 

**Andrew**
* Yeah, I agree. I think because we all the consensus is that in favor of the big EOF, so they should either all be in CFI or none of them should be in CFI. 

**Tim**
* Okay. Does anyone, So, and and to be clear though, there's the two I think we should move to CFI are 4200 and 4250. does anyone disagree with that? 

**Protolambda**
* I disagree. I see arguments to take all the EIP and enforce a decision where we only do one or two of them, but then I also see arguments that, okay, these are ready for CFI, so. And as a result, I think the other EIP is do not get sufficient discussion and might never reach CFI just because of these first decisions to wish.

**Tim**
* Anyone have stronger opinion on this. 

**Gcolvin**
* I think it's been clear for a long time that the stacked validation's essential. So if we're not clear on that, I think we need to take it up at the, the next EOF breakout. 

**Tim**
* Yeah. Okay. So I think, yeah, I think I would rather have this discussion next time with like more time on the call. I think it's, you know, we are working on 4200 and 4750, so I don't think them being CFI today changes how much, like progress is gonna happen in the next two weeks on them. and, and yeah, I guess like just for client teams and other folks to think about in the next two weeks, 
* I think probably the main thing we should try and figure out in the other call is like given the testing and implement STA implementation statuses of all the things we discussed today, you know, what is the subsets that we think is highest priority  to consider for Shanghai? yeah. And we can sort of spend more time discussing sort of these, these five or so things that we, we touched on today. and yeah. And then there were a bunch of links. 
* So, apologies we didn't get to them, but Mikhail had an engine api, spec improvement proposal. So if people can review that also before the next call, that would be great. I think for DevNet we don't really need to change anything in the next two weeks. and one thing also that's probably worth it for client teams to look at is the new test framework that, Mario put together. So this is linked in the agenda. and finally on the other call, we should discuss, a sunset date for Robston. So it's already been deprecated, but yeah, when we want to actually shut it down. but that can wait two weeks. Cool. Thanks everyone, and Ill see you all in two weeks. 
* Thank you. 

---------------------------------------

### Attendees
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

---------------------------------------

## Next Meeting
[November 24, 2022, 14:00 UTC](https://github.com/ethereum/pm/issues/662)

