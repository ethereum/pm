# Execution Layer Meeting 177

### Meeting Date/Time: Dec 21, 2023, 14:00-15:30 UTC
### Meeting Duration: 1:04:18
### [GitHub Agenda](https://github.com/ethereum/pm/issues/921)
### [Audio Video of the Meeting](https://www.youtube.com/watch?v=7amkZxKobX4)   
### Moderator: Tim Beiko
### Meeting Notes: Metago

## Agenda

### Dencun Updates

#### [Goerli Shadow Fork](https://notes.ethereum.org/@ethpandaops/dencun-gsf-1-analysis) [5:25](https://www.youtube.com/live/7amkZxKobX4?si=SYovWcHymu6ZSXNX&t=325) 

**Tim**
Sorry, I was muted on the stream. This should be fixed but just went over what was on the agenda. Okay, so to start Denon the Goerli shadow fork, Pari or Barnabas D, if you want to give an update?

**Pari**
Yeah I can go. So we had the Goerli shadow fork this week, the networks consisting roughly of 300 nodes split across New York, Frankfurt, Bangalore, and Sydney, we're running 100 validators per node, and then we initially synced the Goerli network and then forked it into our own shadow fork, started with Capella and dencun was at epoch 220. We didn't notice any issues with the shadow fork itself. Almost all the clients joined the shadow fork, we weren't able to sync Aragon in time, unfortunately, but we're going to shift to a snapshot approach next time, so that doesn't happen, but all the other clients joined the shadow fork successfully and they all forked into Dencun without any issue.

We were observing roughly 99 to 100% performance at a station as well as block production and then we started blob spamming so there's a link to the more detailed analysis that I've put up today. 

**Danny**
There was zero blob transactions before that point?

**Pari**
Exactly so for roughly a period of one hour, it was just Cancun and nothing else and then you can see the massive spike in the overall network use graph and that's exactly when the blob spamming began. So you're seeing no use, roughly 700 kbps, so that's bytes per second in the Cancun / capella paradigm and once blob spamming starts properly you're seeing it at roughly the 900 kbps paradigm, so we can assume that there's a roughly 200 kvps increase with healthy blob usage. 

One caveat I will note is that the network's extremely flat, there are 300 nodes and most of them have between 70 and 100 peers which means you're going to be peered with someone from almost every region so it's as perfect networking as you can possibly imagine. There's no clustering or anything that's happening but also not particularly sure how to simulate the clustering or what would be useful there. 

And then we went on to the blob analysis itself. So we have a few blob spamming tools that we use so we have Marius's TX F that's blobs and we have pk9 t0 G blob spammer. We were targeting at roughly the four blob range and if you look at the distribution, I think we've successfully hit like three, with six being the least and zero being the least as well, so I'd assume this is pretty much a scenario we'd also see on mainnet because the target is three.

So most of the time we would likely see three blobs per block. The next one is the average blob propagation time. Most of the time across 95% of the node, so this
includes the ones in Australia you they are receiving all the blobs in under two seconds if we don't include the P95 value and just take the average it's under 500 milliseconds and we have a couple more graphs as to the effect of more blobs effect on network latency with respect to blob propagation, as well as block propagation.

The caveat is that for block propagation the CL the way different CS emit their events is varied so some might emit the first time they see a block without verifying it. Others might emit it after they've verified all the blobs, so just keep that in mind when you're looking at that graph. 

At least yeah and in terms of block latency, we see an increase of roughly 300 milliseconds so the presence of blobs increases the latency by about 300 milliseconds. Attestations don't seem to be affected, they still happen at roughly the 4 second mark so we're able to achieve everything we need to, but every node is able to have all the data it needs by the 4 second mark.

Within the last roughly two days we haven't seen any reorgs on this network but I did post an alternate message on interop yesterday as to periodic spikes we see and the periodic spikes seem to be correlating with epoch transitions, so I think it's a known fact that epoch transitions are heavier, so we do see that the block or the slot at the epoch transition would take longer to propagate as opposed to the rest.

**Danny**
On the overall bandwidth consumption increase that we're seeing you said 700 to 900 if I remember correctly?

**Pari**
Yes.

**Danny**
Do you have any insight if that is from the consensus layer or the execution layer? Obviously you know we're  propagating blobs on the goset but we're also sending on the layer we're also sending in the meme pool. I presume you're not sending these just through like Builder networks, these are hitting the public H?

**Pari**
Exactly, they're hitting the public meme pool so we're not able to get the metric per CL and EL, so what we've done is instead target the public interface so this is just each node has one EL and one CL and this is all the traffic that has come out and gone in from that public interface. There are some client specific metrics that we can track but the issue is that they're not necessarily standardized, so you might mean different things based on which client you talk to. 

**Danny**
One way to get transparency on the ratio there would be to spam blobs but only through, assuming you know we had nearly 100% Builder Network or something, only send them to builders through this and then you'd see only the increase from the consensus layer, because you wouldn't have any blobs in the public pool so that's true that might be interesting. Obviously that's work but could be interesting.

**Pari**
Yeah we can give that a shot. I'd propose we try that on Devnet 12 though, because the other point we wanted to make is that we'd like to turn off that Goerli Shadow fork today evening. So if there some last minute test we can do it but that's about it and I've added the blob bar a couple of hours ago, so it adds some latency of 1.5 seconds to random blobs and currently I don't see any effect of that. So I guess the analogy on mainnet is if you have a random dispersion of, I don't know, 10 nodes out of 300 that are really slow and propagating things, there's no network wide perceived impact.

**Danny**
They're not the originators of the message though.

**Pari**
In some cases they are, and sometimes they are… round dropping which node we submit the blobs to. Yeah I think that's all we had from the Goerli shadow fork. There was one thing that the r team wanted to look into with rate limiting. Cause we noticed these massive spikes once in a while, but I think they already have a PR ready for it. 

**Tim**
Yeah thank you, this is a really valuable analysis. Any other questions, comments?

**Pari**
One last point I wanted to make was we've listed a link to every graph that I've referenced. The analysis is based on all the clients together, but there's a filter on top so you can filter just for your EL or CL that you care about and look at per client behaviors. I think there's just too many clients to do individual analysis but it would be awesome if you guys can have a look. The metrics are persisted for the next couple of months, so there's no need to do it before the network is torn down, just adjust your time frame accordingly. 

**Danny**
This is awesome guys. Thanks! 

**Tim**
Any other questions comments on this? 

Okay, if not yeah I guess the next thing I was hoping to discuss was what to do in terms of next steps, a couple people reached out, oh sorry okay before we do that anyone opposed to tearing down the Goerli shadow fork by the end of today please voice your objection now.

**Gajinder**
Yeah we want to look into epoch transition thing and so basically we are debugging it and we might need some time for that. 

**Tim**
Okay so at least Lodestar…

**Barnabus**
Would you not be able to do that on 12 though?

**Gajinder**
On what?

**Barnabus**
Devnet 12.

**Gajinder**
So you are seeing the same behavior on Devnet 12 as well? 

**Pari**
I would be quite sure that it's present on Devnet 12 as well.

**Gajinder**
Okay we'll basically look over there as well and see if we can replicate it there then yeah we can get rid of the Goerli shadow fork. 

**Tim**
Okay, any other team who wants to look at something on the shadow fork? 

Okay so let's coordinate offline but at least check with lodestar before we shut it down. 

#### Next Steps [16:17](https://www.youtube.com/live/7amkZxKobX4?si=SYovWcHymu6ZSXNX&t=977) 

Okay so yeah next up, basically discussing next steps from here. So I know in the couple calls ago we talked about potentially forking Goerli, assuming the shadow fork went well and that client teams were ready to do that. I think I'm pretty sure we had Prism run through the shadow fork and then live on devnet 12 now.

So I'm curious to hear from teams, like, is anyone uncomfortable with moving to Goerli as a next step and if no one's uncomfortable, when would people want to see that fork happen? So yeah maybe first question, anyone not ready to move to Goerli sometime in January? Okay, promising, and so if we were to fork Goerli, just…

**Danny**
Do we have consensus layer teams represented? I'm on mobile so I'm kind of scanning through right now.

**Tim**
Let me see at the very least there's someone from Prism here?

**Danny**
That's what I was worried about.

**James**
Oh I'm here.

**Tim**
Oh oh cool okay so I I'll James just you know to make sure like from the prism side does like January for Goerli feel reasonable?

**James**
Based on what our team talked about, I think so. There's a couple of issues that we're still trying to work out but it looks promising.

**Tim**
Got it. So yeah, so if we want to fork this in January I think we probably want to have the client releases out something like 10 days before the fork actually happens. So based on that, if teams are ready to like put out a release as soon as they come back from the holidays then we could target something like mid-January and then if teams feel like they might need a couple weeks coming back from the holidays to like polish things up and put out a release for Goerli, then maybe it makes more sense to target end of January and the question is one, do people have a preference there, and two is it helpful to agree on like an epoch or at least a tentative epoch today so that when teams are starting to put out release, they can use that number? I guess if there's no objections or push back?

I would personally go first, so okay there's January 8 release around Prism. I was going to say I would personally go for either the 17th or the 25th, which are two dates where we get like a midweek accumulator boundary slot. Does anyone have a strong preference between the 17th versus 25th? Okay lots of people like 11 and 17 some people like 17, 25, so yeah.I think 17 is a decent compromise. So I from the row I had in the table on agenda this would be the epoch number so it would be Epoch number 231680 on the network, start slot is 741 3760, which happens at 6 a.m. UTC 6:32 a.m. UTC on the 17th, and then there's other local time zones that but yeah let's do that.

Obviously if we find a major issue or something crazy before then we can always cancel but this would mean that ideally we're putting out the blog post for the fork sometime during the week of the seventh, or sorry the week of the eighth, so that people have, you know, at the at least a week to update, so if client teams can target to have a release you know, at the latest on the 8th or the 9th of January, then we'll put up the blog post with all of those, and yeah that should give people time to update before the fork happens.

Any comments questions thoughts? 

**Marius**
Yeah what's the time stamp? 

**Tim**
I don't know if Adrian added it to his website so he does, let me just check this real quick. Goerli, the slot, I'll post the time, I'll verify it offline but I think this is the time stamp what I just posted in the chat. Yeah there's a comment by Asgar around, you know talking about a best case yeah timeline between different testnets. I think historically like yeah two weeks is the closest we've done, just it's like the pace at which client teams can put out a release and have the testnet fork depending on how confident we are. 

One thing we can also do is bundle, have a single client release for something like Sepolia and holesky if we assume that if Goerli goes really well and we assume holeskey is going to be trivial to fork once Sepolia forks. We can just have a client release and a single announcement telling people to update their nodes once and that might save us a week or something. Aside from that, assuming we actually have like a client release per testnet, it's hard to do less than two weeks per testnet and then between the last testnet and mainnet, we might want a bit more time for people to upgrade their nodes. Yeah.

Okay so yeah let's releases around the 8th or the 9th. We'll have the fork on the 17th and then from there we can also figure out next steps for the other testnets and if we want to bundle those releases. Anything else on Dencun as a whole, before we move on to other things?

**Barnabus**
Shouldn't we try to tentatively assign like plus two weeks from Goerli to the next testnet and then in case something goes wrong then possibly modify it instead of just waiting for Goerli to happen, and then discuss when we could for next one, because then we going to be losing another two weeks at least in just discussing potential future fork times?

**Tim**
I'm not against it, I don't know yeah how client teams feel about that. I would want to look at the numbers, not on the fly right now, on the call but like if people want to agree to rough dates now, we can definitely propose tentative like slots and then maybe what we could do as well is propose tentative slots that go in like a two week motion if people are okay with that.

And then reconfirm them on like the call two weeks from now so that yeah like teams won't have their releases out yet and then if they want to already include that in a release, it still gives them a couple days, but yeah, I guess would anyone be opposed to 31st…

**Danny**
And then 14th and continually reconfirm after each of those forks?

**Tim**
And I guess my question for between 31st and 14th is assuming we do first and holesky do we feel like we need two weeks between those two?

Given you know if Goerli and Sepolia have gone well holesky should be trivial so I could see the value…

**Danny**
31st and 7th? 

**Tim**
Yeah 31st and 7th. I definitely would not want to bake in a mainnet date yet like I want to sort of roll through that and at least get Goerli and Sepolia like smoothly upgraded but yeah does anyone think that like 31st and 7th is too aggressive or we should do something different?

Okay let's do that then so I'll look at some epoch and slot numbers right after this call but let's do Goerli on the 17th of January. Client teams have a release on the 8th or 9th that we can announce, then we'll do Sepolia around the 31st of January, and holeski around February 7th. Again assuming nothing goes wrong if at any point we see something we can always change those dates, but yeah, teams can start planning around that and the implication as well, being that we'd only have a single client release for the Sepolia and Holesky forks. So yeah, we'd want both of those coded in network and yeah.

Barnabus you have the question Did we agree to do sioa before holesky? I guess sepolia feels higher risk than Holesky so if we are combining the reduces it makes sense to do it before but I don't know if anyone has a counterargument to that right.

**Danny**
Define higher risk.

**Tim**
So there's just like stuff on it right there's like a bigger State there's more people using it whereas holesky is basically completely new, although hoski has like a larger validator set I guess. So 

**Barnabus**
it would be earlier to catch some network related bugs on holesky and then Sepolia, so that's why I would personally prefer Holesky before Sepolia.

**Justin**
I think higher risk is also more informative too right. There's more people using this sepolia we might want to consider learning from it earlier

**Tim**
But yeah I guess it is a good point if there are more validators on Holesky and the main thing we're concerned around is like networking and blob propagation I think it's fine to do holesky first if people want to risk that.

**Danny**
Yeah I could make pretty compelling arguments either way.

**Tim**
I guess does anyone aside from Barnabas have a strong preference on ordering? The argument for Sepolia first is just there's more usage, there's a bigger state but there are less validator nodes. Yeah 

**Danny**
So usage is also important for actual users testing things yeah so like if that gives L2s an extra week uh to test where they're actually currently testing their environments then that's a good argument for me. 

**Tim**
Yeah I don't know if any L2 people are on the call. I don't think so but Carl, yeah?

**Carl**
I think that would be helpful. Most of the testing's been done in private so far and I think it also just act as a signal that hey this is really happening in the short term and might help have more robust deployments get ready sooner around mainnet launch cuz I think that might not necessarily be the case for some of the L2s right now.So just better in my opinion.

**Tim**
Okay so I guess that would bias me towards sepolia first. I don't know how much is on sepolia already but I've definitely heard l2s wanting to move stuff to sepolia if they haven't already so yeah giving them an extra week to do that seems reasonable. Yeah okay so I think I I'd push towards sticking with Sepolia first.

Barnabas are you okay with that?

**Barnabus**
Yeah sure.

**Tim**
Okay so we have the schedule then Goerli so 

**Danny**
Just to state it out loud, like we picked the oldest testnet because if it works who cares we picked the second oldest testnet because that will help users more than the newest testnet in terms of timing, and then the newest testnet. I just say it out loud it doesn't have to be a general rule but like that is reasonable logic, and maybe we will reuse it.

**Tim**
Yeah and I guess the argument to have done holesky first is if we cared less about user behavior like on chain behavior, and wanted to optimize more for validator behavior because there's just more validators on holesky. 

**Barnabus**
It's not just really about the validators but it's the number of nodes on the network right? and holesky only has like 100 nodes or something like that and POI has a significantly more so BL

**Pari**
I think Holesky kind of like in the order of magnitude of the shadow fork we just did, at least based on some crawling, it's like 5 / 600 so it's not that 

**Danny**
And what do you think Sepolia is?

**Pari**
Couple of 100 like 200 at max. 

**Danny**
We could beef it up if we felt like it right before obviously that doesn't beef up the validator nodes but you'd still get deeper like block propagation paths. I don't know I probably wouldn't advocate for that but it is a possibility. 

**Tim**
I mean both of these are also like in order of magnitude under mainnet right ?so it's not like definitely it's not it's 75% of mainnet and Sepholia is like 10% They're both…

**Pari**
Yeah yeah I think the most we're going to learn is from Goerli because the validator set is small enough, there are a lot of esoteric setups and so on. Holesky just has a very large validator set size which means by default most people are just running really beefy machines with a lot of validator keys on one host.

**Danny**
Got it. 

**Tim**
Okay yeah so I think let's stick with the Goerli Sepholia holesky ordering. If we see something going wrong on Goerli, we can always readjust that and you know if we think that the next test being on Holeski is better, we can just swap them around but for now assuming things go well let's just follow that order.

I'll come up with some slot numbers after the call and then clients should have the first release for Goerli and then the second release after Goerli, for the two other test nodes that makes sense everyone? 

Cool. Anything else on Dencun? 

### [Precompile Address Ranges]( https://github.com/ethereum/pm/issues/921#issuecomment-1864735001) [34:05](https://www.youtube.com/live/7amkZxKobX4?si=NiLh3rIOBXAYupcJ&t=2045) 

Okay if not, next up, Ansgar, you wanted to talk about pre-compile address ranges and yeah how L2 pre compiles may affect this.

**Ansgar**
Yeah I mean Carl has his hand up. 

**Tim**
I'm not sure I think Carl's hand is just up from the last comment. 

**Carl**
Okay so yeah so basically but fun enough that's also K me so just recap we have recently started this EIP process rollup Improvement proposal process to standardize evm and evm related changes across layer two chains, of course purely opt-in so it's not a governance call or anything, it's really just a standardization forum, and now as we're starting to get the first kind of proposals through this process.

We're starting to just kind of run into several kind of questions and one of those specifically referred to pre-compiles. So you might have already I think we already discussed on all core devs as well. The potential future R1 curve precompile 66 p256 R1 and that now has an EIP number and is scheduled to go live on several rollups basically as soon as possible, they all just waiting for it to be finalized in this process and so the last remaining question we have is now for pre-compile that starts out as initially a layer two targeting evm change should that basically take the next sequential pre-compile number that we have open on mainnet, or should that go into a separate range?

And so the one kind of nuance that makes this not a trivial question because I think initially a lot of people had the intuition that kind of a separate range for L2s might be better but the problem of course is that a lot of evm changes that will start on layer twos first will at some point later and potentially come to mainnet.

Especially in the future we would expect that most dips actually start on layer 2s because they just ship things faster and then later on potentially come down and so of course we wouldn't want to have them be on a separate address on mainnet from layer 2, so then that would mean that if we give layer 2's their own pre-compile ranges that would mean that now on one, we would at some point also start shipping from that new range which is a bit weird. 

So alternatively of course we could just keep one continuous range and then that would mean that at some point in the future on mainnet, once we ship future pre-compiles, we might start to have gaps where there's just no pre-compiles for a few addresses because they are only on layer twos and then some that we shipped on layer one, so that's kind of the trade-off here and given that again like a few L really want to ship this R1 pre-compiled soon, basically the hope was that we could kind of just make at least like a decision maybe one off decision.

Ideally of course the most atic decision here, how we how we want to treat this, and the one ones maybe because hog also asked on the call scheduling and GitHub issue there will be some sort of registry as well like a meta EIP with a list of all the pre-compiles and the different layer tools that they shipped to.

We haven't created that yet but we are in the process of also setting that up and then the question is if we decide to have one continuous range on layer one and layer twos and is that enough to basically just have this kind of list of pre-compiles in the 
EIP repo or would C then also prefer to have some sort of meta EIP in the EIPs repo as well that kind of clearly lists which pre-compile addresses are basically blocked. 

So yeah those are basically two questions that I would have for people.

**Tim**
Thank you. Danny? 

**Danny**
Given we don't know like how much I'm pro adding a range for L2s and if there is significant adoption of an EIP before L1 adopts it to use disjoint sequencing and use what was selected from that range for L1, because it's very unclear at this point what's going to happen with RIPs in terms of like you know is there to be one EIP for the R1 curve, yes probably but you could imagine maybe there's two because there's splintering in terms of like what one L2 wants to do in relation to another L2 you know then we also have to think of what is that EIP being adopted on l2s what is an L2, you know what makes it in that range. There's all sorts of these like questions which could make that space quite utilized, could make that space quite fragmented. 

Obviously I know that's the goal is to avoid a lot of those things but as we don't know how that's going to happen I would be I don't think it makes much sense to like give it the mainnet allocation range at this time, and to instead like pick from it if we want to use it. 

Obviously like having disjoint ranges is also kind of annoying so I understand the argument the other way but I think this gives us just better optionality as we kind of watch the L2, the rip process full unfold. 

**Marius**
I think we will be having disjoint ranges anyway because like the no matter how we do it in the end there will be EIPs that are or RIPs that are finalized that will not make it to mainnet and so there will be unassigned pre-compiled addresses. I would also prefer the RIP process to have their own disjointed range, like it doesn't really need to be disjointed but we could say something like okay from like I don't know like address 256 upwards is the L2 range, and the address zero or one upward is the until 2 to 256 is the is the L1 range.

**Danny**
and Marius if for example they selected one from the range on the above 256 and then say it was the R1 curve and then L1 was going to ship that same exact functionality would we then utilize their number is that what you're suggesting?

**Marius**
That's the other question. I'm not like I'm not 100% sold on just using what they propose, I think there needs to be a debate about that and it kind of feels like an SK is just like proposing this as it's given that we adopt the same address, but I don't think so…

**Tim**
What's the rationale for that? not what…

**Marius**
Well that's what I'm saying, like there's a debate to be had around this and I of course like it would be preferable for users for smart contract devs to have the same address but…
**Danny**
It's really a matter of how this manifests in compilers and things most of the time right?

**Tim**
Right yeah and I guess my question is like what is there an advantage to having the same functionality at two different addresses? It feels like it might only just create additional risks or confusion, so I'm trying to understand what's the argument for having like the R1 curve at address A on an L2 but address B on an L1. 

**Danny**
Encumbering L1 to L2, for example if the R1 if all the L2s we're going to modify the deployed EIP and functionality at have that address then they might modify extend Etc and there's now L1 is using something different than L2, you know these things can move independently so I would, that that's my main argument.

**Carl**
Okay so to be clear on that in rip process we'll enforce that if you do want to do that once we agree that something is finalized you need to deploy a new RIP and you'll have to use a different address because that's horrendous ux on the L2 side as well.

**Danny**
That's kind of debatable in my opinion as to well you know when you're adding new functionality whether you know if it's an extension of functionality or just a minor breaking change of functionality then you do change things you know, like self-destruct, we changed for good reason and so things that are calling a previous place still get a different functionality so like that's certainly a precedent for changing functionality at an address space.

**Carl**
I mean I think if that's a concern then we should deploy RIPS as EIPs to the same address as the RIP and then like the mainnet thing just follows the whatever said in the EIP but I don't know, it just seems silly to like potentially lose out on all these synergies just because there's a potential for change in the future like we're just default into a worst case scenario unnecessarily.

**Danny**
Yeah I disagree just because the practicalities of how I've seen things upgrade in the past, but obviously like it's optimal from a certain perspective not to change things once they've been deployed. 

**Ahmad**
Yeah, one concern about this is that if the addresses are not the same, then there will be like different versions of compilers and like compiler developers will have to deal with like different versions of the compiler for each network.

**Tim**
But they would have to do that anyways because on L1 even with a separate address range on L1 that address is nothing and on L2 it might be a precompile right? So they're going to need ideally two versions but not n versions so…

**Danny**
There is certainly like network specific like metadata depending on compile target as well.

**Tim**
Ansgar, I don't know if you're hand again.

**Angsgar**
Yeah, I just wanted to briefly say because I didn't want to make it sound like by the way that I assumed that was a given. Of course that was just kind of an opinion. I wasn't aware that there might be kind of opinions against ever kind of deploying two precompiles at the same address. I think it's fine we can discuss this and if this is something that basically we don't feel comfortable at least committing to yet, which it sounds like we're not then I think that would mean that we also already have an answer for my other question around the pre compile ranges because then we should definitely not use the same range right? Because if we of course use the same range then we're kind of committed to shipping at the same address, so then I would say kind of as a takeway from today, we should just give L2 pre compiles their own separate range.

Maybe question, are people generally okay with 256 that seems like a very sane default and basically ZX whatever 256 and upwards I mean. Of course not ZX, whatever the heck that is, and then we can basically discuss this once we move closer to actually shipping one of those precompiles to layer one which I could imagine might be the R1 pre-compile relatively soon but then we don't have to make that decision today. 

**Tim**
Yeah that seems reasonable where we can always choose to take 0 x256 if we want to go that route or 0x10 if we prefer. Yeah does anyone disagree with the 0x 256 range?

If not yeah and I guess we should probably put this in like some informational EIP or RIP or at least somewhere other than the transcript of this call. Yeah, the highlight that we reserve 0x, I guess we would reserve 256 onward for L2s, like maybe we want to bound that range, at least for now to some, I don't know if it's like 100 or a 1000 precompiles.

**Marius**
We already have a bound and that is zero like basically we have 0 to 1024 is the bound of the pre-compiles.

**Tim**
Okay 

**Danny**
So we're saying that then we just flip the upper bit and call it half the range rather than starting at 256. 

**Tim**
I feel like we'll probably have more than a one to one ratio though?

**Marius**
So you're proposing 512 right?

**Danny**
Yeah it's essentially like the bit flip signals, which you're on that would be that feels natural to me, if there's compelling arguments about like the ratio of the amount that we'll see. 

**Tim**
Yeah I feel like 3 to one feels more reasonable like if you look in the history of Ethereum we've shipped 10 precompiles in like seven years, some of the EIPs you know have a bunch of pre- compiles they want to add but feels unlikely we hit 256 but I can see L2s.

**Danny**
Yeah I mean yeah there's a lot more degrees of freedom. One who's doing innovation and what, so it's a compelling argument.

**Guillaume**
Could it be possible to have a range that's actually starting from zero x f like all the way at the end of the space and having a decreasing so that you can extend it as much as you want. It will never clash?

**Marius**
Well you cannot extend it as much as you want…

**Danny**
…but you don't have to decide where they're going to meet.

**Guillaume**
Yeah exactly, you don't have to worry where the wrench starts because you know where it starts at the well not FFF all the way, because it's been reserved for other chains but FFF e for example and just have it decrease and decrease and decrease.

**Tim**
Are there some like weird gas cost arguments to that? I don't think so, but the fact that it's zero that 

**Marius**
There definitely are…yeah so I think yeah if you're loading…

**Tim**
Sorry go ahead.

**Marius**
Yeah if you call into a pre-compile that is or like if you're loading the address of pre-compile you can just add a two, push two instead of push 32.

**Tim**
So how about we do 512 and then if we ever exceed the 512 on the L2s we can
give the sort of second 256 range back to the L2s which will be kind of ugly but  something we can deal with five years from now?

Does anyone disagree with that? 

**Carl**
I mean we could also just add another 1024 on top of it, if we ever needed to and give that to EL, as well right? 

Which give us that 3 to1 ratio, whatever it doesn't matter? 

**Tim**
Yeah but I think yeah 512 probably gives us room for like several years and we can revisit this or other people can revisit this in 5 10 years and think we made a really bad decision.

**Danny**
Or we can revisit ourselves and think we made a bad decision.

**Tim**
Yeah okay so let's do that and then yeah I think an informational EIP probably makes sense because we want L1 to be aware of this, and then we can have RIPs that like reference the range or something. I think if it's just an RIP if it's just an rip then someone just looking at like L1 stuff might not know that we have reserved this range, so yeah I would add an EIP for this.

**Carl**
Okay we can get…

**Tim**
Sorry go ahead.

**Carl**
No, I just want to say just to point it out though because we have had the similar conversation in the past that people would are generally uncomfortable actually having layer 2 specific information in an EIP so they would literally just say that basically the upper half of that range is blocked for mainnet and then to actually see which of these addresses correspond to which layer two precompiles, you would have to go to the EIP repo.

It sounds like a good…?

**Tim**
Yep yeah exactly but knowing that on L1 we shouldn't deploy anything in that range I think is, yeah is what we wanted in the EIP. Yeah.

### Next ACD & Testing call times [52:52]( https://www.youtube.com/live/7amkZxKobX4?si=ywSukQwpveQHFqJH&t=3172) 

Sweet. Anything else on this? Okay, next up, real quick, we discussed this a bit last week on ACDC, but in the next couple weeks with regards to the all core devs, we said we're going to skip a formal all core devs next week, potentially have a testing call at 14 UTC on Thursday, if people want to show up and organize something. The week after that, January 4th, given we're going to want client releases shortly after,it feels like we should have an all core devs call but I just want to check, does anyone feel strongly that we should not? 

Okay, so we'll keep the call. I will be out but a lightclient will be running the call, so he'll see you all there in two weeks and then last thing on the agenda, we have this thread for the devprague and Electra EIP proposals. I went over it a couple days ago to compile sort of everything that's been proposed so far. 

## [Prague/Electra Proposals](https://ethereum-magicians.org/t/prague-electra-network-upgrade-meta-thread/16809?u=timbeiko) [54:00]( https://www.youtube.com/live/7amkZxKobX4?si=ywSukQwpveQHFqJH&t=3240) 

There's been two more proposals in the last day so 7547 and 7212 but aside from that we have a decent list already there I was curious to hear if anyone has thoughts about the overall set of proposals anything they'd want to bring up now to discuss or bring to people's attention…

I think at the very least people should be reviewing this over the next couple weeks and as we move towards the testnets for dencun, we should start triaging to all of this sort of individually, but yeah any initial thoughts comments questions from any of the teams?

**Guillaume**
Yeah just to question are we still targeting a very short fork for Prague? 

**Tim**
I don't think we've agreed to anything yet, so yeah, Ansgar?

**Ansgar**
Yeah I basically had a comment on that. I just wanted to say because we are also actively working on EIP, one or several EIPs regarding adjustments to the kind of staking reward mechanism. I think related to similar how in dencun, we ship basically this the throttling of the of the cues just to make sure that we kind of never go out of bounds in terms of how many validators we have on Ethereum and so while those are not quite finalized yet, I think in general it would be nice from that point of view if we did have enough of a fine grain forking schedule that we don't have to, worst case, wait for 9 plus months on to change, once that becomes urgent with potential kind of developments in the total amount of staked eth and whatnot.

So in principle there would be a preference towards having more of like a smallish fork that we can still ship by the end of  next year at least. Instead of one that like really bundles everything that might be delayed until, I don't know, mid 2025 and then we basically are not very reactive, in case we need to make small adjustments.

**Danny**
One additional thing to note is a number of the consensus layer proposals are not and do not have to be cross layer, so there is an ability to make an independent decision here on a lot of those EIPs, if the execution layer is going to be digging deep into a big feature.

**Tim**
And I think on the EL side, the big fork is basically, do we choose to do Verkle now and then prioritize it and you know we might include other EIPs alongside Verkle but effectively, you know we only ship the fork when Verkle is ready, and just generally any large feature has taken us over a year to ship, whether it's the merge obviously, whether it's 4844 that we're working on now, so I think if we do go down the road, Verkle at least, on the EL side, we shouldn't assume it's going to go live in like less than a year right? 

And I mean, you know we can hope and like work hard and whatnot for that but like if there's something that actually urgently needs to go live before that ,bundling with verkle unlikely to have it go live in like less than a year.

**Danny**
And yeah, on my read, there is demand to get some of these things out on the consensus layer in 2024 and so we can just keep that in mind as we're making the decision on that side.

**Tim**
 Yeah.

**Guillaume**
Just to be clear, nothing should go at the same time as Verkle. It's such a complex thing that there's too much risk. I mean if it's activating yeah, even if it's activating some pre- compiles I would prefer seeing a like smallish fork that takes three months to release I know it's never been done but if it's just for a precompile, it might be doable.

I would rather have that than anything happening at the same time as Verkle because yeah once again the complexity is bonkers. 

**Tim**
I guess yeah on that you're really selling it. Yeah on that then, I think again with like the three month thing it's hard to like realistically commit to that and I think the reason is there's never just one pre-compile if we wanna ship. If we want to have a fork, there's a bunch of stuff that's going to want to be included and there's like high fixed cost to shipping your fork, so we should probably bundle a bunch of things together.

By the time we're bundling you know three to five EIPs, it's basically more like a six to nine month thing so I think it's fine to do that but we should not tell ourselves like oh we're going to like choose the things and like fork in April, after we've chosen in January, because it's only one thing. T

That said I think what we did do this time around is we sort of pre-committed 4844 to the fork after, while we were working on the withdrawals fork. So if we wanted to ship a bunch of smaller things on the EL side, whether coupled or not with the CL, and then you know slowly start working on Verkle in parallel and sort of pre-commit the next fork to that, that is something we can do as well, and this way we can get all the smaller things out earlier, but also sort of reserve the next fork for Verkle in advance and potentially have parts of the teams working on it in parallel. 

And I guess maybe like this is probably the main thing that would be good to like agree on in the first couple weeks of next year regardless of like what the small EIPs are.

I think you know on this thread everybody can get a feel for like the type of stuff that's being proposed, but do client teams want to do, at least on the EL side, something before Verkle or not, and then if we agree to that, you know early in January, we can then figure out okay, what are the things we want to do before Verkle and this will give us, this will give us a good idea of like yeah, how long this fork is going to take and maybe on Verkle specifically like gam was just saying it's a pretty huge change.

I know there's been the Verkle’s implementers calls and there's the website now and Josh has been doing the summaries on Twitter, but do people feel like it would be valuable to maybe dedicate part of like the ACDE call to go deep in Verkle and have people sort of understand exactly where things are at, and potentially ask some questions.

Yeah would it be worth having a call like that early next year, so that we can zoom in to the details? 

**Marius**
Good idea, okay. 

**Tim**
So yeah, let's maybe do that. I don't want to like schedule an exact date. We can, maybe play it a bit by ear, but I think if teams want to start looking at everything around Verkle, start looking at all the other smaller EIPs and get a feeling for, do we want to do those EIPs before Verkle and if so, do we have preference on which ones we can discuss that in January, and then find a time, even if it's not like a full all core devs, maybe have like half of an all core devs focused on just going deep into Verkle, so that we sort of know what we're getting into, or at least what the current state of things is.

Any other questions comments? Okay, anything else anyone wanted to discuss before we wrap up? 

Okay, if not we can leave it at that. Thanks everyone. Yeah let's get Goerli out for Dencun and hope everybody has happy holidays.

## Attendees

* Frank Chai
* Danny
* Ahmad Bitar
* Peter Garamvolgyi
* Danno Ferrin
* Pooja Ranjan
* Trent
* Mario Vega
* Carl Beekhuizen
* Karim T
* lightclient
* Barnabus Busa
* Mikhail Khalinin
* Justin Florentine  (Besu)
* Matt Nelson
* Guillaume
* Hsiao Wei Wang
* Ignacio
* Scorbajio
* Alexey
* Gary Schulte
* iPhone
* Ben Edgington
* Ulas Erdogan
* Marius Van Der  Wijden
* Tomasc Stanczak
* pk910
* Ansgar Dietrichs
* Paritosh
* NC
* Joshua Rudolf
* Marek
* SasaWebUp
* Mark (ethdreamer)
* Ayman (Nethermind)
* Ignacio
* Tomasz Stanczak
* James He
* dan (danceratops)
* Yona
* eric
* Fabio Di Fabio
* Ashraf
* Plotr


