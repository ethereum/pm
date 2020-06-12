# Ethereum Core Developer Meeting 87 Notes
### Meeting Date/Time: Friday 15 May 2020 at 14:00 UTC
### Meeting Duration: 1 hour 30 minutes
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/169)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=bGgzALuyY3w)
### Moderator: Hudson Jameson
### Notes: Brent Allsop, Jim Bennett

## Summary

## EIP Status

EIP | Status
---|---
EIP-2315, EIP-2537 | `Accepted` Targetting Berlin
EIP-2046, EIP-2565 | Proposed for Berlin
EIP-2464 | `Last Call`

For more up to date EIP status see the [EFI tracker](https://github.com/ethereum/EIPs/pull/2378).


## Decisions Made:

Decision Item | Description
--|--
**87.1**   | Both EIP 2315 (Simple Subroutines for the EVM) and EIP 2537 (BLS12-381 curve operations) have been accepted into Berlin.
**87.2**   | Ephemeral Berlin testnet name YOLO (you only live once) to test these Berlin EIPs
**87.2.1** | 2315, 2537, 2565
**87.3**   | 2046 is pending results from open ethereum benchmarking.
**87.4**   | Simple Subroutines for the EVM (2315) has some outstanding specification issues which will be resolved by Tuesday to make the specification final.  Greg (Colvin) and Martin (Holst Swende) are getting involoved in that.  James Hancock can also be contacted.
**87.5**   | BLS 12-381 curve operations (2537) is going to have the pre compiles listed by Alex Vlasof (Champion) by early next week to make that final.


## Actions Required:
Action Item | Description
---|---
**87.1** | Decision required on looking at the contract code for Simple Subroutines.
**86.2** | Completed last week.  James to reach out to Alexi for merkalization in Simple Subroutines.
**86.3** | Ongoing.  ProgPoW compromise proposal to be decided on (testnet then pocket).
**87.4** | Update EIP bot with Withdrawn
**87.5** | Move EIP-2583 to Withdrawn
**87.6** | James Hanckock to review EFI EIP and accept existing pull requests.
**87.7** | Alex (axic) to review Berlin EIP and accept existing pull requests.


---

## AGENDA

**Hudson Jameson**
Hi, everyone. I didn't start the stream correctly. This is Ethereum Core Developer Meeting 87.

### Agenda #1: [Berlin EIPs](https://docs.google.com/spreadsheets/d/1BomvS0hjc88eTfx1b8Ufa6KYS3vMEb2c8TQ5HJWx2lc/edit?ts=5ebe9851&pli=1#gid=0)

And we are going to Agenda Item Number One, which is the Berlin EIPs.

That is going to be a [clickable link in the agenda](https://docs.google.com/spreadsheets/d/1BomvS0hjc88eTfx1b8Ufa6KYS3vMEb2c8TQ5HJWx2lc/edit?ts=5ebe9851&pli=1#gid=0) that opens up a spreadsheet that Pooja from the Ethereum Cat Herders created and is working with the Ethereum Cat Herders and James Hancock to continue to be updated. I'm gonna have James take over, and he's looking to share his screen in a second, or I'll share my screen if he can't figure it out, to go through the different clients and the status of each EIP. James, you want me to share my screen?

**James Hancock**
Yes, it's giving me something I have to do - permissions for something now which I didn't expect.

**Hudson Jameson**
All right, [we are here](https://youtu.be/bGgzALuyY3w?t=70) and everyone can see everything, it looks like.

**James Hancock**
[jump]... waiting for Berlin. I decided to withdraw the difficulty bomb, because I'd rather focus on making sure that Berlin gets out in time for the Eth2.0 stuff, so that can just go into the next one. And I don't know the status exactly of 2046, but I am assuming that that will not be ready in time, and that's fine, because we can do one in a few months after Berlin for the EIPs that are ready for it. Doesn't make sense to wait for anything, at least EPS that are almost ready.

So yeah, EIP 2315 - simple subroutines. If I could get just status updates from each client, we'll just go through the ones for Berlin, which is EIP 2315 and EIP 2537.

And starting with Geth:

**Peter Szilagyi**
As far as I know, the spec isn't even completely final yet.

**Martin Holst Swende**
Yeah, I would like to add that the spec is currently, up until today -  I think Greg made a change today - but the spec up until today is implemented in a PR. It passes the test. It says in the comments there that it is more or less done. Having said that, we do anticipate that the spec may change.

**James Hancock**
Okay. Open Ethereum?

**Artem Vorotnikov**
So basically we have merged 2315 into master branch today as it was one month ago. So if the spec was changed today, then the current code in Open Ethereum master does not reflect it. So I guess we need to have some investigation here.

**Martin Holst Swende**
Question: Did you guys check out the tests that were made as a PR to the test repo from the Besu team?

**Artem Vorotnikov**
Not sure. We'll take a look.

**Martin Holst Swende**
Yeah, please do, and just give a thumbs up if you if you pass them or not.

**James Hancock**
Okay. Besu?

**Tim Beiko**
For Besu, we're in the same boat. We've merged or have a PR ready to merge the spec as it is, but we're kind of blocked on basically the spec getting finalized. Like Martin said, we wrote some acceptance tests that reflect the spec as it was when we wrote the test, but the biggest blocker for us is just getting a final agreement on the EIP.

**Greg Colvin**
Yeah, the intent is to settle that Monday. And so I should be able to get a final spec on Monday or Tuesday.

**Martin Holst Swende**
Right. And so a few of us are going to have a call. But naturally, anyone who has a particular opinion about this way or that way or whatever, you're welcome to join. Just ping us.

**James Hancock**
Where can people do that?

**Martin Holst Swende**
Well, I don't know. I guess the [AllCoreDev channel](https://gitter.im/ethereum/AllCoreDevs).

**Greg Colvin**
Hudson or somebody could volunteer to get it organized. Random pings may not converge on a consensus.

**James Hancock**
I can do that. I can talk with you, Martin, later about times that if anyone wants to join, just have them ping me.

**Greg Colvin**
Okay. We're spread across a lot of time zones.

**James Hancock**
That's pretty normal.

Nethermind? Someone here from Nethermind today?

I understand we'll talk more about the state of 2315 later, but I just wanted to go through this initially to get everybody on the same page at where things are.

EIP 2537, the BLS curve operations, starting with Geth:

**Peter Szilagyi**
So there is an open PR on our repo. The PR was kind of updated with the final-ish note from the author yesterday. It's 16,000 lines of code. So I think that kind of sums up the status.

**James Hancock**
Yeah. I talked to Alex earlier about getting more testing and things ready, but he wanted... So open PR, it's just a giant block of code that we still need to make sure works.

**Peter Szilagyi**
Yeah.

**James Hancock**
Open Ethereum?

**Artem Vorotnikov**
So there was a big update on this front from us. So we actually have two PRs open for this now, using different implementations, one from Alex Vlasov from Matter Labs, and the other one by Wei which uses the Milagro Library, which are the bindings developed by Lighthouse, basically. So we have two open PRs, and we would like to test both of them, but we will have them ready in any case.

**James Hancock**
Cool. So I'll put that as PR here.

Besu?

**Tim Beiko**
So same thing, we have a PR. The only blocker is having the final addresses for the precompiles, and then it'll be ready to merge.

**James Hancock**
Okay, and Nethermind isn't here.

I already went through not withdrawing the 2515 for Berlin. And then if someone here has an update on 2046, we could go to it, but otherwise I'd like to move on.

**Artem Vorotnikov**
Actually, it has been implemented in Open Ethereum approximately a month ago, I think.

**James Hancock**
All right. So, as a PR or merged?

**Artem Vorotnikov**
Merged. In master.

**James Hancock**
And that's all that. I think I will turn it back.

Oh, do you want to talk about 2315 first, Greg, or do we want to talk about timing for things?

**Tim Beiko**
So, wait, just for 2046, did we decide we're not doing that in Berlin? Should clients start implementing it? It's been kind of unclear these past couple of calls with the status with it is. I'm just curious to see what everyone else is thinking about this.

**Alex(axic)**
I have a comment on that. I think three or four calls ago, when we last discussed it in depth, and Alex also explained his benchmarks and findings, we left these final comments on the PM issue. And the suggestion was that the repricing of the TPN precompiles should be part of 2046. And because those are necessary because they were underpriced. And the repricings for the other precompiles should be separate EIPs because those are not necessary for security. Those are just a benefit to the users. But none of these changes were applied to any of the EIPs. And I remember also Alex said that he may be proposing a lower number, potentially zero, as a cost for static call. So I don't think anything has changed or moved on this direction.

**Alex Vlasov**
Yeah, just because it wasn't final, whether it goes into Berlin or is delayed. Most likely it should be split in two. I think it should be easy to adjust price of one of the precompiles, which is the only one affected by reducing static call to precompile price. Unfortunately, I didn't do an EIP for this. So maybe, I don't know who is the author of 2046, but maybe it can just be extended. It also requires us to increase the price of one of the existing precompiles to cover this cost.

From a technical perspective, it only requires us to increase the price of PN additional precompile to reduce the cost of static call without any additional security issues.

**James Hancock**
Have we done the test? My understanding was we had comprehensive benchmarks or something that was needed before all of this was accepted.

**Alex (axic)**
Somebody - was it you, Martin? You wanted to also replicate the results on Go Ethereum.

**Martin Holst Swende**
Yeah. And I told all the client implementers that you guys may want to test your nodes, your clients. But in particular, I care about Go Ethereum and want to benchmark that.

**James Hancock**
Is anyone particularly motivated to do all the work, maybe to get it in before Berlin?  I don't want to say it can't make it or won't make it, but without someone driving it really hard, I don't see that exactly happening.

**Alex Vlasov**
Well, at the moment I can only tell that eventually I will also try to do it on Geth, but Go is not a language which I know well, in particular. My [unclear](https://youtu.be/bGgzALuyY3w?t=784) will be with other clients. But eventually it should be a larger work, which includes repricing of other precompiles, which are currently hugely overpriced.

**Hudson Jameson**
And we want to keep in mind the EIP-centric process where we're trying to work around which EIPs are done...

[cut out]

**James Hancock**
That is a good call. Martin, go ahead. I feel like you have thoughts, so bring it on.

**Martin Holst Swende**
So my gut reaction is that there is no chance that Geth will be ready with the BLS curve operations for mainnet launch in July.

**James Hancock**
In July - any part of July?

**Martin Holst Swende**
Yes.

**James Hancock**
Okay.

**Martin Holst Swende**
I don't know, Peter, what do you think?

**Peter Szilagyi**
I don't know. I can't really say. So the thing is, we have this gigantic PR. We can definitely review the cool parts. Those probably are okay-ish, and we can fix anything that's not okay-ish. So that should be trivial enough to work.

As for the crypto part, I personally cannot review that. I cannot meaningfully - either the crypto itself, the math itself, or the assembly itself. So from my perspective, the only thing we can do is fuzz it to death. But I don't know what timeline is realistic for something like that.

**Martin Holst Swende**
Yeah. So we are trying to pursue that angle, there is a BLS12-381 fuzzing infrastructure by [unclear - Greta Brankin?](https://youtu.be/bGgzALuyY3w?t=913) that we're hoping we can use to fuzz it against some of the libraries and also against - there are two implementations in Go, so we can fuzz those two against each other. But I can't really say we're going to be done with that in time for a mainnet launch in July. I'm not saying it's impossible, but my gut feeling is that you shouldn't hope too much for that.

**Hudson Jameson**
If we would, if we could get the type of cryptographic experts you would need who are also familiar with Go, would that be something where they could come in and do the type of reviews necessary to make us feel a little more secure about the implementation? Would that be something that would be acceptable?

**Peter Szilagyi**
So at the end of the day, the thing is that we ourselves cannot meaningfully vouch for the code. So we can ask other people to help out, but at the end of the day, we're still trusting somebody that the code is valid.

**Hudson Jameson**
Yeah.

**Peter Szilagyi**
So what I personally could do is try to check the math if there is some hard reference stuff to compare it with, but that's most of it. So I mean, I can check that the code kind of executes some formulas. But whether those formulas are correct or not, that's completely beyond me. And I cannot do anything meaningful with them.

**Hudson Jameson**
Because my thought was as this is an EIP that is wanted by a few different teams across the ecosystem, namely the Ethereum 2.0 team, if they were to bring in someone who can get familiar with the implementation code base for this EIP, and just double check that it's integrated into Geth properly, that could be something that I would help arrange and find the right people for, so you all wouldn't have to waste time [unclear] that out.

**Peter Szilagyi**
So integrating Geth properly, that's the easy part. We can do that. The problem is with the crypto and the assembly. That's the thing that we cannot do.

**Hudson Jameson**
Okay, well, if you're open to it, we can talk about it afterwards in a Geth channel and make sure that I understand all the requirements of what the person would need, and then I can see who would be able to help, if anyone. It's worth a try, I'm thinking.

**Alex Vlasov**
I think they should also comment on the assembly part. [Unclear](https://youtu.be/bGgzALuyY3w?t=1101) exists there for kind of just to limit optimizations on modern 64 bit CPUs. It's not strictly a requirement, and you should talk to the owner what will be the penalty, and it seems a penalty will not be that large, You can just answer with anyway alternative code, which is in pure Go and which just implements also some stuff for systems which are not 64 bit x 86. So maybe he will be able to just not kind of turn on the feature to use assembly. Or at least allow end users to turn it on if they really, really want it. But I think the owner should be able to help on it - the person who did the PR.

**James Hancock**
is it something we could move forward with making a testnet date and then just say things with testing and fuzz testing need to be really, really ironed out before we're comfortable with the mainnet date?

**Peter Szilagyi**
I am comfortable with looking at a testnet.

**Martin Holst Swende**
Yeah, I mean, we could naturally just merge the thing and have it so you can enable it via some configuration, and we could spin up testnets. But I noticed historically that people get upset when testnets break. I don't know why.

**James Hancock**
So do we make a BLS - do we just spin up -  Maybe the shadow forking routes and kind of thing that you talked about previously, Peter? Is that something we could do?

**Peter Szilagyi**
Yeah, the problem is that kind of works if you are screwing around with existing opcodes. But in this case, we are deploying 8 new precompiles, or other money with precompiles. So I mean, we can fork Ropsten, but as long as nobody's using them, it doesn't matter much. So you kind of have to convince people
using them.

**Martin Holst Swende**
In this case, it will really be the case where you want to fork Ropsten is where you change some opcodes that are commonly used. If you just want to test the BLS stuff, there's no point in forking Ropsten. You can just spin up a brand new testnet if you just want to fit us. And that's easier. So

**Hudson Jameson**
I'm okay breaking Ropsten. That's a personal opinion. Oh, because you can spin up a new one is what you just said.

**Martin Holst Swende**
Yeah, it's easier to do the test on a brand new testnet.

**Time Beiko**
And I'm sure there also we could get the Eth2.0 teams to help with some of the, I guess you could call it "manual testing," but just setting up deposit contracts and the proxy for it and having that on the new testnet. It seems like you don't need to have that high of a volume of transaction. We just need to make sure this application for which this EIP was built works, right?

[Crosstalk]

**Martin Holst Swende**
I don't think this would really give - the coverage we would get from it is the amount of effort that people on the internet or research are willing to spend on playing with it. Which probably is not that much, actually. A good thing that it would bring is that it would force all the clients to put out versions where this feature is activatable, which means that it can also be fuzzed to the [unclear](https://youtu.be/bGgzALuyY3w?t=1334) So I guess that's, that's a primary upside as I see it.

**James Hancock**
So if we did a new testnet and had BLS on it, and then maybe did a bug bounty for breaking it, would that perhaps help?

**Martin Holst Swende**
Yeah, that might be an idea.

**Hudson Jameson**
Yeah, I think we should go ahead with a testnet that just does the BLS curve. Is that something the Geth team wants to take on coordinating? I don't know who's the most expert at running setting up testnets, etc.

**Peter Szilagyi**
I just wanted to say that I don't really see it. So if you want to set up a testnet, then set up a testnet for everything that's supposed to be in Berlin. Just picking out the single EIP will make things a lot more horrible because then clients will all of a sudden need to support a weird testnet with half-baked EIPs in it.

**Tim Beiko**
Oh, I agree. I think we should have 2315 as well.

**Alex(axic)**
So who will try to break the BLS code?

**Hudson Jameson**
Eth2.0 team and...

**James Hancock**
... and Alex Vlasov.

**Alex Vlasov**
Well, I posted a link with a small repo which anyone can clone. They just start fuzzing with two comments. What I need to do there is actually I was basing the codes - I use a fuzzer which can run Rust simultaneously. So I made bindings to Go code. And I based those bindings on the old repo which is not the one which is integrated into the gas right now. So I need to make this adjustment somehow. And then you can literally test Karen PR into gas against code which is used by Besu and  from the PR, which I sent to Open Ethereum.

And it's most likely much more efficient than trying to sponsor a network where it will be limited to how many may be while equal seven, or how many million gas for 15 seconds, and each call to precompile, which costs at least half a million for [unclear](https://youtu.be/bGgzALuyY3w?t=1479). So I don't think it is a proper way to try to break the BLS precompile on a testnet. It's much easier to break it just by writing a fuzzer tester. It would be good if there would be some external machine available, so we just start it there and leave it running. But maybe I will just spin up a server. On a laptop, I found one problem, which is actually already fixed, and only happens because my bindings are on outdated version. So far, I didn't find any as a problem.

**Alex(axic)**
Someone also mentioned that the Eth2.0 team will try to break it. Are you referring to the deposit proxy?

**Hudson Jameson**
Deposit proxy and I felt like they had one other piece, but I could be wrong. I'm not as in tune with it.

**Alex(axic)**
I think the the deposit proxy hasn't been touched for a while, and it was only an experiment by Alex Stokes, I believe, but nobody is actually allocated to make this piece of code.

**Hudson Jameson**
The last time I heard about it, I thought Alex was in the process of writing it a month ago, but that could be completely wrong.

**Alex Vlasov**
As far as I know, it is in a form which is usable and only misses constants to what addresses are available for some precompiles. Otherwise, it's final draft, I think.

**Hudson Jameson**
Yeah, so what  decisions I think we're starting to come to here are if we do a testnet, it should be a testnet that covers all EIPs going into Berlin, and if we were to do a testnet, we would need to pull in resources - it would be ideal to pull in resources beyond fuzz testing, so that people can play around with it either from "let's break it" perspective or from a usability perspective, I suppose.

I think the good next step would be to set a date for a new testnet that would have all the EIPs for Berlin in them, and then between now and then, me and James and others can get together the right people to help on the verification of the cryptographic aspects of the implementation and also talk to the Eth2.0 team and maybe other teams about what they would use this for. I know that there's more than just the Eth2.0 team that needs this curve and this EIP.

**Alex(axic)**
So just a bit of feedback on the Eth2.0 side.

The deposit contract which doesn't do any BLS verification has been audited. And that is what's used in all the testnets. And that is, I believe, what they plan to launch with, and and the debt auditing process took all the time. Now if you introduce this proxy, which does the verification on top, you would want to verify it as well, audit it as well. Otherwise, why should anybody trust it more than the audited underlying contract?

**Alex Vlasov**
The [unclear/crosstalk](https://youtu.be/bGgzALuyY3w?t=1694) of a proxy contract is it actually prevents the user from making a mistake they should never have made in the first place. So it's additional protection, it cannot make things worse.

**Alex(axic)**
Well, if there's a bug in the proxy, then you can lose all the money you're sending to it. Well, you would lose it anyway if it wasn't there. If there is a bug in a proxy contract, which allows you to pass the invalid public key, it cannot make things worse. If there was a mistake, and it wasn't caught, t's not a good outcome.

[crosstalk]

You can just verify. You can just verify that the public key is well formed.

**Alex Vlasov**
So it's not a proxy.

**Hudson Jameson**
Yeah, they call it a proxy, but it's not a proxy.

**Alex(axic)**
A proxy is written as a proxy. It's not a pure function. It's a payable function.

**Hudson Jameson**
Oh. I was under the impression it was just a verification function. But, yeah, if it's called a proxy, that makes sense. Okay. Yeah.

**James Hancock**
I think they did that because, so, as far as errors, so on the [unclear- slice?] I don't know how to say the testnet, but the Eth2.0 testnet, there, ProtoLamba found something like 150 or more keys that were submitted that were malformed, which shouldn't be possible but happened.

**Hudson Jameson**
Yeah, and then on Topaz it was like over 400 or something, or, no, I forgot the number, but Topaz had a lot of them, too. So they have incentive to get this quickly audited, and quickly - well, not that audits should be quick, but y'all know what I mean, basically get this in order.

**Alex(axic)**
I've been submitting patches to the proxy. And I don't think it has been touched for at least a month. I do like the idea quite a bit, and I'm definitely interested in personally participating in that. But I just don't really see that there's any priority for writing and auditing this contract and launching it. And we are trying to push the BLS beacon parts because the Eth2.0 team depends on it. I think it would be really good to see the priorities right, because I don't think there's any chance that the Eth2.0 launch would go with the proxy.

**Tim Beiko**
How long would the timeline be to get an audit on the proxy? Because it seems like  with Eth2.0, the beacon chain probably won't be launching this summer anyway, so is a couple months sufficient? Because if we deployed this BLS curve to mainnet, say, I don't know what it's call it August or whatever, then if they write a proxy contract over the next month or two, get it audited, is it realistic that by the end of the summer or early September, you would have that contract audited? And if that's a realistic timeline, I think it's probably still aligned with the Eth2.0 launch.

**Alex(axic)**
I think it's obviously a chicken and an egg problem. I mean, why would anybody audit deposit proxy if it depends on an unfixed, underlying precompile? So maybe this idea of a testnet for BLS might be a good idea for for that reason. But yeah, I don't have a clear answer. And I don't think anybody on this call has any idea of the Eth2.0 timelines. So I'm not sure we can answer this question.

**James Hancock**
My previous talks with the Eth2.0 teams was that the pieces that changed from the audit would be pretty easy to go back over, if necessary, so that there wouldn't be a lot of necessary effort to go back in. I was talking with Alex Stokes and some others. And if it's a chicken and egg problem, then let's just make the chicken or the egg, I'd say, and do the testnet, and then have them react accordingly, instead of this stalemate of who's going to do what first. That'd be my recommendation.

**Alex(axic)**
Sorry, I also wanted to, before we get into this rabbit hole of the proxy, I wanted to ask, maybe I missed it previously, if there's any other use cases - I mean, there's definitely a lot of use cases for the new curve. But are there any other imminent projects trying to utilize the curve?

**Alex Vlasov**
Well, eventually, I would really, really want to [unclear](https://youtu.be/bGgzALuyY3w?t=2004) as soon as it's available. Well, not as soon as it's available, but as soon as we can conduct a trusted setup for it. But otherwise, it's a really good upgrade which allows you to do much more stuff withe the SNARKs in the sense that you can [unclear](https://youtu.be/bGgzALuyY3w?t=2028), especially with new proof systems which give you a slashing overhead factor. Every SNARK should eventually be migratable there.

**Hudson Jameson**
Oh, so every SNARK that's currently deployed would be upgradeable and therefore benefit from the gas reduction?

**Alex Vlasov**
Almost. Like it's - what's the right way to say it? I mean, it obviously depends on the SNARK [unclear] and fuzzer, but if the purpose of the SNARK itself is some form of duplication and compression, in principle, BLS12-381 allows you to fit more into a single SNARK versus proofs. So effectively, you pay a constant price for verification, but you pay this constant price for a much larger amount of items that will be compressed.

**Hudson Jameson**
Okay. I think I get that. So, Alex, I don't know if we have the exact team names who would use it besides what Alex Vlasov mentioned, but the way I see this whole thing is,I think if we produce the testnet, we can take the gamble on the Eth2.0 team utilizing it, just because it's becoming more apparent that it's very valuable for them because of people messing up this - I forgot how to say it, but basically mess messing up the signing, was that the signing key or what's the thing that's generated that gets messed up?

**Alex Vlasov**
Well, you have to deposit to a public key which is in another form on Eth2.0. And right now you just declare it, and you don't perform any explicit verification on chain if the form is correct.

**Hudson Jameson**
Got it. Okay.

**Alex Vlasov**
If you declare it as point not on the curve or something else, you will just deposit, but to something which looks like a public key push down to a private key.

**Hudson Jameson**
Okay, I think this is a good opportunity to one: build a testnet, number two: get more cooperation between the Eth2.0 and Eth1.0 teams to use whatever experts they have in cryptography to validate some of the stuff that we have on our end. Can we go forward deciding on making a testnet that involves all of the Berlin EIPs and then from there having the Eth2.0 team use that as well as other people just trying out the testnet? I guess I don't see a downside, but I was wanting to know if I'm missing anything.

**Martin Holst Swende**
So there's one kind of downside that I see. I'm okay with that downside, but the downside is, if people think, "Oh, the testnet has been up now for a month, so there's been no problem, so let's just do mainnet." And I don't want to give that impression. I mean, we can spin up another testnet anytime, no problem, but it's not a signal about mainnet readiness. I just want to get that said.

**Hudson Jameson**
Yeah, that's a narrative problem. So all we need to do is not call this a testnet but call it an alpha testnet.

**Peter Szilagyi**
[cuts out - lots of background noise and echo in the following:]
I guess what we could do is get all the clients to merge in all the PRs for Berlin, even though they know they might be unstable...
And I guess the purpose would be to just...BLS... to hit it as hard as they can. And then if nothing breaks for a couple weeks, the maybe it makes sense to try to fork Ropsten. It just would be nice to have some pre-testing done on something that people don't depend on.

Otherwise I can use Puppeth to deploy infrastructure fairly quickly. And that's a starting point where people can just screw with it.

**Hudson Jameson**
Okay. I think that'd be great if you could get that together. And I can work with James on communicating with the Eth2.0 team and even maybe getting a bounty out. I'd have to work on that from a different angle. But I can I can take that on.

**Tim Beiko**
I think this all makes sense. It still doesn't solve that both these EIPs have things that are missing or clients that merge them. So Greg, you mentioned that early next week, we should expect some resolution on 2315. And then, for 2537, there was still the question of figuring out what addresses the precompiles are at. And I know that or I don't know, actually, there's a lot of people on the call, but if a champion for 2537 is on the call, it would be great to get that finalized so we can actually merge this into clients and then deploy it on a testnet.

**Alex(axic)**
Did we move on from the BLS? I had just one last comment on it, or question,rather.

**Hudson Jameson**
Oh, we're still talking about that pretty much. We just asked if the champion could work on getting the precompile addresses together. But if you had another comment, that's fine.

**Alex(axic)**
It's just that one of the precompiles relies on the IETF draft. And I think a new version of the draft came out last week or so, or this week. And I don't know if it changes anything for the EIP, but this was an outstanding question that one of the people in the past depends on an in-draft IETF specification.

**Alex Vlasov**
Well, I can answer this one immediately. The latest version is version number seven, and it was merged, I think, a little more than a week ago, but it was already based on version seven at some point. It just simplified the part which actually wasn't even in precompile. So the deaft itself didn't affect - well, it kind of affected the precompile, but in a very small manner. It just depends on how you define and sign all the field elements. And it actually simplifies the code. So it was already implemented on top of the draft, which was known to come up more than a month ago. So it doesn't affect any current code. It was already modified to support the latest draft and Eth2.0 also was intending to move to this one.

**Alex(axic)**
Yeah, that is the other question. It's unclear when this IETF specification is going to be finalized, and it is also unclear if Eth2.0 is going to lock in a version.

**Hudson Jameson**
They said the other week they're locking in seven, I think. Seven or eight. I forgot which one.

**Alex(axic)**
So then is the precompile going to be locked to version seven just to support Eth2.0? Or, you know, t's like an open question.

**Alex Vlasov**
Well, so far I don't know on any plan to make a new draft which would affect the part which is implemented in the precompile, actually only two precompiles out a set of nine, which are parts of this EIP will only be affected by any changes in the future, and everything else that is not affected by changes in draft.

I cannot guarantee that there will be no changes. But if right now, we accept that it's version seven, those two precompiles will stay at version seven. And if maybe in the future later on, it will require an extension or change, the answer should be two other precompiles, or maybe at this point, we will already move past it.

**Alex(axic)**
Yeah, I really hope we can avoid another Keccak-256 where it's this [unclear-shattery?] situation.

**Alex Vlasov**
Yeah. Well, this was more about the change in the standard which felt like a downgrade in security. So this is why it wasn't widely accepted by the community, I would say.

**Hudson Jameson**
So FileCoin, Ethereum Foundation, and I believe StarkWare are all coordinating on which IETF draft of the curve that they're going to be implementing. Again, I think that's seven. I'll check on that. But if your concern is everyone being on the same page, Axic, then I think that we will get information from the Eth2.0 team once we start talking to them about if this is messed up or not, because they'll be looking at it.

**Alex Vlasov**
At least so far, I don't know of any draft of the next round. So far, we cannot progress any further.

**Hudson Jameson**
Yeah. They have to pick one at some point.

**Alex Vlasov**
Yeah. And regarding the precompile addresses, I don't know who should sign them. I mean, I can write the numbers, which is just the next precompile starting from the largest available right now, but I don't know whose responsibility is to actually make them solid. I can put them in the draft. It's not a problem.

**Peter Szilagyi**
I mean, I don't think it matters. So pick whatever makes sense.

**Alex Vlasov**
Okay.

**Hudson Jameson**
Okay, so decisions being made. I'm talking to the Eth2.0 team with James and a few other people. We're coordinating them looking over the different code bases, particularly the Geth code base for the cryptography behind it. We are starting the alpha, the first Ethereum Alpha testnet that will not necessarily be a predecessor to a mainnet, but rather be its own independent testnet. And that's going to be called Alpha Testnet YOLO. And according to the comments and chat, at least, if anyone has any disagreement...

**James Hancock**
We should call it an ephemeral testnet.

**Hudson Jameson**
Ah, okay. Yeah.

**Rai(ratan.sur@consensys.net)**
How about "ethereal testnet?"

**Hudson Jameson**
That's just gonna make people think it's an Ethereum testnet, because that just sounds so similar.

**James Hancock**
Ephemeral Testnet Berlin Yolo.

**Hudson Jameson**
Ephemeral Testnet Berlin Yolo. Okay.

So we're doing that. Let's move on, unless anyone had any final, final things.

**Peter Szilagyi**
Not a final thing, but a question about testnets. I'm not sure which clients are going to serve Berlin on mainnet. But is every client supporting the click thing or should I make it a proof of work?

**Hudson Jameson**
So if you don't support click, speak up.

**James Hancock**
Or if you want proof of work.

**Hudson Jameson**
We don't know about Nethermind. That's the only thing.

**Peter Szilagyi**
Görli definitely supports click.

**Hudson Jameson**
Oh, Görli is click, isn't it? Everyone supports click, then, yes. Ethereum JS may not, but I don't think they've had a representative on the call for a while.

Okay, sounds good. All right, let's move on.

**Peter Szilagyi**
We've had issues when there's some big miner and then there's some asymmetry and then all hell breaks loose. So, yeah, we've got to run something a bit more stable.

**Hudson Jameson**
That's a good idea.

### Agenda #2 [Eligible for Inclusion (EFI) EIP Review](https://youtu.be/bGgzALuyY3w?t=2836)

Okay, we're skipping EFI so we can go to some of the EIPs that people want to bring up for the first time. I think that's a good idea, at least. What do you think, James? We've kind of gone over some of these before.

**James Hancock**
Yep. Perfect.

Okay.

### Agenda #3 [Berlin Timing](https://youtu.be/bGgzALuyY3w?t=2852)

Oh, Berlin timing. So we're almost off of Berlin. But now we've crossed out the mainnet date. The proposed testnet date, I think we could have  the Alpha Testnet YOLO sooner, right? We don't really need to schedule that because it's not on a block number and it's just going to happen when it happens. Yeah, that sounds fine.

**Peter Szilagyi**
Yeah, the only thing we kind of need to figure out is what's going to go -  So. I guess the BLS, we need the pre compile numbers. But that should be fairly done. And the only thing we need to figure out what happens with the subroutine jumping so that everybody -

**Martin Holst Swende**
let's assume that we'll figure something out early next week and have it implemented by the end of next week. Something like that.

**Hudson Jameson**
Yeah. So it would be 2315 simple subroutines and 2537 BLS 12-381 curve. Those would be the two additional EIPs that would be involved in this ephemeral testnet.

**Martin Holst Swende**
Yeah, if we're making any changes, we just restart the testnet.

**Hudson Jameson**
Okay. So, timing, then - James, do want to go over that, or is that something we shouldn't even bring up today now that we've had a lot of this new information?

**Hudson Jameson**
I don't think we need to go more into the testing. It would be nice to get up the testnet by the first week of June, so then social coordination can start happening around that time. That would be nice.

**Hudson Jameson**
Great. Okay.

### Agenda #4 [EIP-2565: Repricing of the EIP-198 ModExp precompile](https://youtu.be/bGgzALuyY3w?t=2969)

Next up, I just put this agenda item number four back in from the last meeting. I don't know if anyone's here to speak on it. It's 2565 repricing of the EIP-198 ModExp precompile.

**kelly**
Hey, Hudson. Yeah, I'm here. Let me share my screen real quick.

Great, so hopefully everyone can can see my screen. This should be a fairly quick update just looking for some directional guidance here on which direction to take with this EIP.

So just as a quick refresher, EIP 2565 is to reprice the ModExp precompile. Came in about a month ago after doing quite a bit of benchmarking on GO Ethereum. We found out that GO Ethereum was about 10 x overpriced. And so we recommended changing a simple parameter from 20 to 200 to more accurately price that precompile.

At that time, Martin had recalled that during the original pricing that Parity was quite a bit slower. So we went off and benchmarked Parity, and sure enough, it was about two to five times slower, therefore making the sort of 10 x gas production not able to be done with Parity because it would make the the gas price too low.

So what we went off and did last week was go and look at alternative libraries for Parity or Open Ethereum to use. We found some Rust bindings to - first we looked at just simple version bumps of the Parity precompile, because it was quite a bit out of date, at the suggestion of Alex Vlasov. Unfortunately, these didn't get us near the performance of Geth. We were still sitting about two to four x slower than Geth.

So we went and looked at Rust GMP. We were able to benchmark this, and if Parity or Open Ethereum uses this, they'll actually be faster than Geth. So this was based off some feedback from Peter two weeks ago. He said, "hey, it seems kind of weird that Rust is slower than GO. And sure enough, if they use this precompile or this library they will actually be faster.

So there are two paths forward with this EIP. The first option is to continue with a simple parameter change for both Geth as well as Open Ethereum where we change this parameter from 20 to 200, and Open Ethereum goes in and implements this GMP library instead of what they have today. And that will keep everything above 20 or 25 million gas per second, which is sort of the standard that we're seeing for precompiles.

So this is option one. I did send some information into the Open Ethereum Discord. Their only reservation that they said that they had was that Rust GMP may not compile on Windows on Visual Studio. This was some feedback from Artem.

I went to look at ether nodes. Right now, there are 20 Parity nodes running on Windows that are synced to the mainnet. So I'm not sure how big of a concern this is.

Our recommendation would be that Open Ethereum adopts this library, and we go with the simple parameter change. If that's not possible, we can go with a more complicated pricing formula change for both Geth and Open Ethereum and then just make a minor version bump to the Open Ethereum library. We won't get quite as much savings, and it is maybe a little bit more complicated of a pricing change that makes the pricing formula more accurate to the complexity, but this is another option to move forward.

And so I really just wanted to have a discussion. I'd like to move this EIP towards Eligible For Inclusion, and we just need some direction on which of these two options to go with here.

**Artem Vorotnikov**
So I'm just going to spin up the Windows machine, Windows VPS next week and get some testing for the GU toolchain in case the GMP does not compile under the Visual Studio tool chain. So we'll see how it works. So potentially, we are open to using the GU toolchain but we need to do some testing.

**kelly**
Fantastic. That's great feedback. So, should that be successful, it sounds like the path forward with this is to swap out that library and then make the simple parameter change in the pricing formula in both Geth and Open Ethereum where we change this G quad parameter from 20 to 200.

**Artem Vorotnikov**
I suggest that we make a final decision during the next call, because I cannot commit us to anything without testing first.

**kelly**
Okay, so just to be clear, you know, is the case that if we are able to compile this Rust GMP library with the the new toolchain on Windows that this is the appropriate path forward for Open Ethereum?

**Artem Vorotnikov**
Well, if it works well, then why not?

**Peter Szilagyi**
Two weeks might be a bit late. So, perhaps, if it's fine, we could try to investigate this next week and just decide on AllCoreDev calls that if the library works out, then that's having been concluded as to the number of up to 200 and run with it.

**Martin Holst Swende**
I mean, alternatively, we could lower the number on the testnet. And then if Open Ethereum says no, it doesn't really work for us, then screw it, we're not going to deploy it on mainnet.

**Peter Szilagyi**
Yeah, but that kind of also means that - so if we create a configuration where some EIP is enabled -

So, essentially, in Geth, when you say that, okay, next hard fork is Berlin, then the hard fork, you just specify one block number and it implicitly collects the EIPs that you enable. So if we want to throw out one EIP from Berlin, that means we need to modify the code so that Geth will not run on the testnet anymore because the Berlin hard fork version - and I don't want to add [crosstalk] versions in Geth.  

**Martin Holst Swende**
I mean, these are ephemeral testnets.

**Peter Szilagyi**
Yeah, I'm fine with that.

**James Hancock**
So are you suggesting adding this to the list of the Berlin ones?

**Martin Holst Swende**
Well, I don't really care about how we do it, but what I would have felt was a good idea was maybe to actually, if we're going to spin up a testnet in the next whatever week, we could just lower this threshold. Because that means it's easier to do actual benchmarks for external people like me if I know that Open Ethereum client is configured with the lower gas price. And if it doesn't work, we just drop it from Berlin and don't have it on mainnet. If we keep redefining Berlin, then it's gonna be messy. But that's only a problem if the testnet's going to be persistent. That's where I'm at.

**kelly**
Yeah, it seems reasonable to me if we can change this from 20 to 200 for these alpha testnets, then we'll have changed that, and then for Geth, there are no changes at that point. And then for Open Ethereum, it'd be looking at if they can switch the library out before mainnet.

**Peter Szilagyi**
Can we make this decision on Monday or on Tuesday? I expect that we will have some results by then.

**kelly**
Sure.

**Hudson Jameson**
That sounds reasonable.

**Peter Szilagyi**
I just wanted to make sure that we don't wait two weeks to get your final decision on this.

**James Hancock**
We can add that to the things. So, getting the addresses, Greg finishing on Monday, maybe if by Tuesday, we could have all of these pieces wrapped up. We can set that as a goal.

**Hudson Jameson**
I think that's good. Everyone kind of knows what they're supposed to do for the most part. And there's kind of a,for lack of better word, champion for each thing, because Greg's figuring out his thing. Kelly will check back in Monday or Tuesday on the results of Artem's benchmarks and the address for the BLS. And then that one is Alex Vlasov.

**James Hancock**
So I'll reach out to you guys. And by Tuesday of next week, let's wrap that up.

**kelly**
Okay, great. Thanks, James. Yeah, so it sounds like the plan is we'll make this change from 20 to 200 on this EIP, and I'll work directly with Artem on the toolchain stuff, and we'll get an answer to you on Monday. James, thanks for the feedback.

**Hudson Jameson**
All right. Thanks, Kelly.

### Agenda #5 [EIP-2481: Adding request IDs to ETH protocol request and response objects](https://youtu.be/bGgzALuyY3w?t=3574)

All right. The next item on the agenda is [EIP-2481: Adding request IDs to the ETH protocol request and response objects.](https://github.com/ethereum/EIPs/pull/2481)


I believe that is -

**Christoph Burgdorf**
It's me, Christoph. I'm on the call.

**Hudson Jameson**
Oh, awesome. Hey, Christoph. Go ahead.

**Christoph Burgdorf**
Okay. So this EIP 2481 is about a change in the Eth networking protocol, moving it from EIP 65 to EIP 66. And it's about adding request IDs to all the request response pairs that we have. We've talked about that outside of this meeting at the last DevCon with some of the client teams implementers. And it's basically what the LES protocol also already has.

So the objective is that we can make the networking slightly more efficient if we don't have to loop through all the incoming responses and try to match them to the requests based on their contents, which sometimes means for things like Geth node data, you have to Keccak over the content to match it to the requested hashers. And instead, with the request IDs, early on, you can just say, oh, okay, this is not the response that I'm looking for, so I don't further look into this. So, yeah, that's basically what it is about. And the EIP keeps it quite simple.

So, for instance, it doesn't dictate that response IDs need to be sequential. So client teams are free to implement this - like you can say, across different request types, I might share the same request IDs, because the request responses are already separated by the type anyway. The EIP doesn't define - it keeps it flexible that response IDs can also include and can also be duplicates. So the IDs can be duplicates, which means you can totally ignore the thing and put a constant, like, put it to zero, which basically means, Okay, I just do what we do right now,"  we treat it as if there are no request IDs.

So this is to basically keep it simple from the implementation side. But for the clients that care about making making this a little bit more efficient, they can implement it properly. And, yeah, we talked we talked about this at the last DevCon with some of the Geth team, and I think Peter also signaled that they support us with Geth. And that's basically it from us so far.

**Artem Vorotnikov**
I've taken a look at the proposal. It seems quite easy to implement in Open Ethereum. The only thing is that we haven't merged EIP 65 yet, but after we do EIP 65, which should be in May or June, this one should be fairly quick to implement and merge.

**Hudson Jameson**
Do we have other opinions or comments?

**Peter Szilagyi**
Yeah, just wanted to say that the proposal would make quite a few things a lot simpler. For example, Geth, whenever there's a need to pierce connect on the Eth protocol, Geth does a few challenges just to make sure that the other side's on the correct chain to make sure that the other side is synchronized if we are not yet synchronized in these kinds of challenges, and apart from that we also retrieve some data concurrently. And generally, it's a bit ugly to match up because essentially there are times when we just shoot off three requests to do a node, and then the three requests eventually, the replies can't come in. And for once, it's really annoying to mix and match the replies to requests. The other one is that often the replies are empty, in which case, you really just have to guess what the reply might be for.

So all of these scenarios would be really elegantly solved by the request IDs. The only only problem that maybe one that mostly affects us and Open Ethereum is that we cannot really drop support for the old protocols. So for us, every protocol is just additional complexity, because as long as somebody is running the old one, we can't just nuke it. But still, I think the proposal itself is a step in a very good direction.

**Artem Vorotnikov**
But we will be able to drop 63, 64 and 65 eventually. So it will be simpler in the end.

**Peter Szilagyi**
Yeah, eventually, but for now, there are still peers running 63.

**Piper Merriam**
In theory, we could end-of-life 63 and just set a date for it at some point here.

**Peter Szilagyi**
Well, I guess the next hard fork is implicitly end-of-life for it. Because you need to update your client to be on the next hard fork. So whatever is the lowest common denominator will be the last supported version, and we can drop everything below it.

**Piper Merriam**
We can look at EIPing that just to be nice and clear and give everybody lots of leeway to know that we're going to stop supporting.

Not to sidetrack things. Back to the discussion.

**Peter Szilagyi**
I don't think we need that much bureaucracy around it.

**Hudson Jameson**
Okay. If anyone wants to make an EIP out of that, feel free, but I don't have an opinion on the matter. Anybody else have comments on 2481?

And, real quick, Piper and Trinity team, I apologize that I don't always bring up Trinity when I'm talking about mainnet clients. What's the status of syncing to Eth1 mainnet and you all want me to have you all be more included in some of the stuff when I bring in Nethermind, Besu, Open Ethereum, and Geth?

**Christoph Burgdorf**
So the current status is that we have, we have so we have dropped [unclear-Fastnet?] awhile ago because it was just not working for us and not a viable option. But since we started implementing [unclear], this is actually looking quite good for us, so we've been able to follow the mainnet chain, and we're still in the process of implementing the parts that deal with backfilling the state, backfilling blocks. So it to sum it up, we plan to go in [unclear] within, I would say, maybe two or three months. I don't want to make our commitment here, but that's just my general feeling.

So yeah, we certainly also like to be included. I actually noticed that we were missing on the spreadsheet earlier for Berlin support. So yeah, we haven't started to implement any Berlin EIPs, but we definitely will. And we try hard to soon be a client that we will actually promote for people to try out as a mainnet client.

**Hudson Jameson**
Okay, great. That absolutely answers my question, and we will definitely include you on the sheet. And if I just forget in future meetings, just point it out, like, "Hey, we're over here." And I'll bring it up. Thanks so much.

**James Hancock**
They're already included.

**Hudson Jameson**
Oh, perfect.

### Agenda #6 [evm384: an alternative route to precompiles for supporting BLS12-381 on EVM (@axic/Ewasm)](https://youtu.be/bGgzALuyY3w?t=4125)

Next up, we have evm384: an alternative route to precompiles for supporting BLS12-381 on the EVM (@axic/Ewasm)

**Alex(axic)**
Yeah, I will try to be quick. So I may have come off that I don't really want BLS12 support earlier on the call, but I just really want BLS12 support to be done well. And I felt like that maybe some questions are still really, really outstanding for the precompiles.

So regarding BLS12 in the Wasm team, we also have been working on benchmarking BLS12 in Wasm itself, because obviously, the reason of Eth2 using it, as well as recursive SNARKs, at least some projects want to use it for recursive SNARKs.

And to that end, first of all, I shared a document on the Gitter channel, which has some of these these details. At the very end of it, there's a chart with some numbers, and these are numbers on benchmarking BLS12 implementation appearing on Wasm.

So we have a native implementation in Rust, and we are using Wasm SNARKs BLS12 implementation for the Wasm part. And the native code is running around five milliseconds. The Wasm SNARK implementation in Wasm on the Wasm interpreter is running around 500 milliseconds. And this Wasm code doesn't use any house functions or anything. It was just purely Wasm. And then we started to use big number or big integer host functions for the Wasm code, which would be similar how EVM has 256 bit operations. But in this case in Wasm, we had 384-bit integer operations as host functions, which means those are not implemented inside Wasm. Rather, the engine provides it, and it's implemented natively. And with those optimizations, we were able to get down to close to 15 milliseconds. And we think there's still more opportunity to optimize that code and make it faster. So that means we're roughly three times slower than native in Wasm.

And then we also were thinking whether we can replicate these findings on the EVM. And that's what EVM 384 is. So we had a couple of different options to do this. And basically, we are introducing three new opcodes. None of this is final or ready for any EIP or anything like that. These are still just experimentations.

We have implemented what I have listed here is option one, which means that we have three opcodes and modular addition modular subtraction on 384-bit numbers and Montgomery multiplication on 348-bit numbers. And these three opcodes in EVM operate on memory only.

And we have implemented a synthetic benchmark written in Yul so it compiles to EVM. And the reason for the synthetic benchmark is that, obviously, so we have spent probably two weeks on this project so far, and we cannot really implement a complete BLS pairing on EVM in two weeks. So we decided to only take a small building block used by the pairing operation, and the synthetic benchmark tries to approximate the complexity of the pairing operation using this small building block. And we have built this synthetic benchmark and using Wasm SNARK, and we have implemented the counterpart in EVM.

So in EVM, the actual implementation is in EVM 1, and the bytecode is written using Yul. And what we have found is that our approximation isn't fully closely approximating the pairing operation yet, but it is within like 20% to the pairing operation, and what we have found is that we get pretty good results on the EVM. I don't have the final numbers yet, and we need to optimize quite a bit on the EVM part. But the initial results showed that t seems to be possible to get somewhat close to the Wasm performance with the host functions.

So what this would mean in the end is it may be potentially possible to support BLS12 with more primitive additions to the EVM and not to precompiles.

This may have been quite a bit of information and the document is more comprehensive. But if anybody has any questions now?

**Alex Vlasov**
Well, what would be the final number compared to, not even compared to Wasm, maybe in abstract milliseconds per pairing? Because it's very difficult to compile multipliers. And Wasm SNARK is not the fastest one and  definitely not as fast as one which goes into precompile. It's also really quite expensive to use.

**Alex(axic)**
So which number are you looking for?

**Alex Vlasov**
I mean, you said that a Wasm SNARK or something, which is actually not the fastest library in the West, is five milliseconds per pairing. In this case, you should also specify what is the number of pairs, actually. I think the fastest libraries do two-point parents in something like two milliseconds. And you get a performance which is three times slower than this with EVM, or the same performance, like expected performance, not the full pairing, but expected performance.

**Alex(axic)**
Are you asking whether we expect performance to match the native?

**Alex Vlasov**
No, no, no, no. Let's say that Wasm SNARK made in the spring of 2 pairs with five milliseconds of writing time. What would be the expected performance if you would add these EVM functions? This part that wasn't clear. Would it be like the same one as Wasm SNARK, or would it be like a factor of three or five higher?

**Alex(axic)**
I don't have the final numbers to share on that, because we are benchmarking on a different machine, so it's not comparable, but we definitely aim to get very close to the Wasm. And I expect that we can, I hope we can get to maybe 50% slower than the Wasm version.

**Alex Vlasov**
Well, if you say 50% slower, it will be already five times slower than the native code, and it already gets quite expensive. It will be 10 millisecond roughly of execution time on EVM, which is, I think 33 million or something like this, if I do the math correctly.

**Alex(axic)**
Yeah, so in terms of gas, we don't have I mean, the current BLS precompile EIP doesn't have any proposed gas values. Well, at least last I checked, which was a month ago, maybe it does now. But we hope to not exceed maybe twice the cost of what's there in terms of gas. But yeah, obviously, we don't have the final numbers on any of these things yet.

**Hudson Jameson**
I was gonna timebox this real quick, if you could just have a final thoughts.

**Alex Vlasov**
[crosstalk]...which you compare the gas is already not the fastest one. And it's already much slower since the one which was proposed, which is a native code, which is integrated right now, and for which there are numbers...

[crosstalk]

**Alex(axic)**
...the native code, we are using your code. And are you saying that Wasm SNARK isn't the fastest? I believe it is the fastest on most of the Wasm interpreter cases we have ever used it with.

**Alex Vlasov**
Oh, yeah, yeah. I mean, even the native code itself is already quite expensive for not like everyday use, but it's already quite expensive. Taking into account modern SNARKs, which are much trickier to check, and making it a factor of five, at the end of the day, is kind of prohibitively expensive.

**Martin Holst Swende**
So I have a question for Axic. It's a quick one. I'm wondering about the complexity. So, to recap, you have three opcodes to replace a number of precompiles. And I'm wondering, these three opcodes, how difficult are those opcodes and how large you know how many lines of code is it to implement those small Lego bits? Do you have any rough numbers on that?

**Alex(axic)**
Yeah, we have a bunch of different implementations of those opcodes in terms of C. And I believe it's like roughly 100, 150 lines of code for the three opcodes in C.

**Martin Holst Swende**
That's not much.

**Hudson Jameson**
Okay, we're out of time here. So I did want to go real quick. And before we go

79:33
quickly, say what decisions have been made today and any action items so that the note taker can note that on the meeting notes, and we can reference that in the video at the end of people look back on this. So first of all, we are making what we're calling an ephemeral test net named YOLO. A femoral Berlin test that named yellow which is going to include the following IP

80:00
AIP 2315 and AIP 2537. For sure, we are potentially going to include AIP was at 2046.

80:12
Pending results from an open theory and benchmarking that will finish by Tuesday most likely.

80:20
The simple subroutines for the VM has some outstanding specification issues that will be solved also by Tuesday is the expected date. Greg and Martin are getting involved on that. And you can contact James Hancock, if you want to get involved in that discussion. And the BLS 1231 curve with AIP 2537 is going to

80:44
have

80:46
the pre compiles listed by Alex last off who's the champion of that tip? by early next week, in order to make that specification also final

80:58
What am I missing?

**Tim Beiko**
81:02
The other tip for the test net the one I think Martin said we should just do is not 2046 but it's 2565 right? It's the mod x freakin PA. Ah, thank you. So it's not 2046 it's 20 was it? 22 52565? Yep, yep, yep. Okay, thank you. So yeah, note taker Please take note on that. The decisions made last time is that Berlin will be dependent on the BLS the IP sub routines may or may not make it. We now know that sub routines will be making it

81:36
and then the actions needed.

81:39
Decision required on looking at the contract code for simple sub routines. That's 86.1. If you're looking at the notes for meeting 86 86.2 is James to reach out to Alexi for medicalization and simple sub routines. That happened that happened. Okay. 86.3 prog pal compromise proposal to be decided on and then in parentheses, it says

82:00
Test net than pocket. That was Greg's request to have about a month of discussion within the community about prog pal going into a hard fork and or and or it being put on a test net and then pocketed when we need it as a compromise. So that discussion is ongoing that's nothing's been decided today on that that's just me going over the action item that was decided on last time.

82:28
Update AIP bought with withdrawn and move Ei p 2583. To withdrawn are the other two action items. Is there any disagreement on the decisions made or action items I've listed

82:43
2515 the difficulty bomb was withdrawn from Berlin. Yes, 2515 has been withdrawn from Berlin. That is a current

82:53
decision made that should be noted. The tip statuses on last week's notes are now in the repository.

83:00
Everyone can check those out if you want. I didn't want to go through all of them.

83:04
But some of them are EFI. Some of them are accepted, etc.

83:08
That's just, yeah. One quick note about that. I know James, I think you're the author for the meta, you know, JJ, the author for the VIP EFI list. And Alex, you're the author for the meta AIP. And I think there's a bunch of pending prs against both like from Pooja I know, I have either a PR modification on poojas pr, but it would be good if we could merge both the EFI and the burden, meta EAP, so that they're up to date, because that's kind of where the community goes to

83:43
look at this stuff.

83:46
Okay, who is needing to look that over just an editor, or was there a particular person? Oh, no, I think it needs to be the author. So I think for me, me for the BFA and Alex, for the Berlin Yeah, he wants to do something different.

84:00
Accept. Okay.

84:02
Got it.

84:04
Okay, any other comments, final stuff?

84:08
A comment about the networking eat to 481. And that one still needs to be watched

84:18
as a draft, and I guess we decided to do it or, um, no. What do you do? We can merge it as a draft, regardless of any decisions made, it can be in draft status as long as it is well formed. So I think there's some outstanding comments, or did they? Oh, actually, it's approved. Okay, I'll merge it right now.

84:42
Good. We want to have any fire. Talk about that next time.

84:46
Let's talk about that next time. There's not a reason to have EFI on that today.

84:51
Okay, next call is may 29th at 1400 UTC. Thanks everyone so much for coming. And we will see you then. Cheers. Thanks. Thanks for that summer.

85:00
Right That was

85:01
sure cheers

85:06
bye


# Attendees

* Angela
* Brent Allsop
* Hudson Jameson
* Jim Bennett
* Pooja Ranjan
* Tim Beiko


# Date for Next Meeting: 26 May 2020, at 1400 UTC.
