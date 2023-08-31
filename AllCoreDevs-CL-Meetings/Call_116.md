# Consensus Layer Call 116

### Meeting Date/Time: Thursday 2023/8/24 at 14:00 UTC
### Meeting Duration: 32:54
### [GitHub Agenda](https://github.com/ethereum/pm/issues/852) 
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=RysjOBGRDDg) 
### Moderator: Danny
### Notes: Metago

# Introduction

**Danny**
Okay, cool. Welcome to Consensus Layer call 116. This is issue 852 on the pm repo. I am remiss and put the agenda up last night before I went to bed and so it's a pretty light agenda, but if you have items that you were not able to add to the agenda decision, it did not exist, please jump in, drop a bunch chat or just chime in when we have time.

# Deneb

Okay uh so we'll take a look at Deneb and then one of our open items that's not currently Deneb related is I've never said this word out loud, Holesky, the testnet launch. So we have a couple things on that item and somebody can correct me if that was totally wrong.

## Devnet 8 updates [1:50]( https://www.youtube.com/live/RysjOBGRDDg?si=ZmGAqg2-cAwqrWQ3&t=110) 

Okay cool so there is some space for devnet updates. I believe there is a devnet out and there are things running, if anyone would like to give a current status update?

**Barnabus**
Yeah sure. So devnet 8 is running. We onboarded all the different clients and currently Aragon and Bezu don't have any validators. Every other client has a validator. They are doing very good. I just made some deposits for Bezu this afternoon and this should arrive soon to the chain. Bezu has been confirmed to be able to do block production on Kurtosis and I'm working on Aragon right now trying to figure out what is going on there. And the other Thea client that is not working right now is Prism. So hopefully we hear something from the Prism team on that one.

**Terence**
I can give a quick update. So we have a fix out there already. We're planning to merge it today. So yeah it should be hopefully working by the end of the day.

**Danny**
I'm always just kind of curious what sort of failures we're seeing in this state.

**Terence**
Yeah yeah definitely I can give an update. So the Prism issue is that we request block by root example that we are missing blob by basically a short range block. Day to day you get an authentication, you don't have a blob, you basically request a blob by root. But we forgot to request blobs by root after that. So essentially the processing of the block gets stuck.

**Danny**
I see. So we could potentially catch this upstreaming Kurtosis and if we do get some CL networking tests in Hive, can catch it there as well. 

**Terence**
Yeah 

**Danny**
Thanks any other questions or comments related to devnet8? Are we regularly sending blobs and doing anything other than just steady state?

**Pari**
At the moment there's some blobs but it's basically steady state.

**Danny**
Gotcha. 

**Barnabus**
Maybe Marius can begin hardcore fuzzing on it now, because we are pretty stable.

## [Dencun testing overview](https://notes.ethereum.org/@ethpandaops/dencun-testing-overview) [4:38]( https://www.youtube.com/live/RysjOBGRDDg?si=PvGHyUesa-JCOHOU&t=278) 

**Danny**
Cool. Next, I wanted to go over this thing testing overview that Pari and others put together. Some of this is pretty standard but some of this hopefully covers some of the components that we are new you know for example, exceptional blob networking cases. Pari, or are you the appropriate person to go over this document?

**Pari**
Yeah, I can go over it. So we've created this testing…

**Danny**
Can you share the screen?

**Pari**
Sure I can. Does it look okay?

**Danny**
Yeah. Thank you.

**Pari**
So we have this testing overview talk and the main aim of this is to create a list of different ways we're approaching testing and we want to know if we're missing something early on so that we can allocate resources to get that done asap. We do have a couple of needs at the current stage. None of them are urgent, so we will be getting to them over the next couple of weeks, but if someone's free and wants to take it up, please feel free. The testnet verifier for example would be used in kurtosis and a lot of other places essentially something that we can use to verify that the testnet is healthy. Sig test coordinators the same one we used for the merge tests it just needs an update and some loving care after about a year of not really using it.

And the other ones we do have some sort of testing in the pipeline, so please reach out if you're planning on working on them. But besides that, it's just an overview of different categories of testing. So we start with spec tests. Shall we, I think nothing is really new there for evm related testing. We're banking on Hive evm sizing execution specs and I think Mario and Mario's Etc would be kind of points of contact, with sync testing since we will be having a couple of new dependencies with the blobs, we wanted to make sure that we can sync test the basic scenarios so regular syncing after blockage blog expiry Windows checkpoint sync syncing when blobs are inside the window but missing, and Optimistic sync tests.

We still need to figure out how we do it with the sync target. We might need to wait until we have it on a public testnet before we can get this up and running and of course Hive also already has a lot of sync related tests built in. Kiosk tests are something we have been doing in the past with antithesis I think Tyler's kind of been the main point of contact a lot of you might have interact with on the topic, but Barnabas and I have also been looking at chaos mesh along with kurtosis, so the idea is that you can cause a lot of network level instability resource level time related faults, and you should be seeing something on this topic over the next month.

I think we still have really alpha ideas on this but it seems to have some legs and should be able to help us with testing and public testnests, so we have devnet shadow forks and begin metrics Gaza that would help us with some optimization related topics. We have MEV related tests so kurtosis now supports two modes. First mode is mock MEV and that would use Mario's mock builder that has an implementation of the builder API. 

So if you are a client team who wants to have a target where you know the API has been implemented you can use it with MEV type mock and knock out a lot of local bugs that might be happening or versioning issues and ideally once the relay side of things are up and running, you can switch this MEV type to full and that would spin up relays, builders, the relay API endpoint, and everything so this is literally the MEV workflow that you would see in mainnet Ethereum and there you should be able to test the entire integration end to end.

I would see that more as making sure that all the different entities work together and we don't see any surprises when once we hit the fork ? in it. The other thing that the mock MEV target supports is invalid payloads, so you can configure when an invalid payload happens, and this is really useful for checking circuit breaker conditions, so that if something does go wrong, we need to make sure that nothing happens to Ethereum clients.

And yeah a couple of more tests, we have were regression tests. I think historically we've tended to Hive for regression tests, but if they're more complicated ones, kurtosis also supports a golang SDK now. So you can orchestrate a more complicated test scenario with kurtosis, still really alpha and we're working out some PRS here but actually something to know about.

And then anything related to bad blocks, bad blobs we have TX fast that Marius is working on, and should be relatively up to date as well as some internal fuzzing tools by the security team and we've listed down a couple of blob specific tests. This is largely based on this really nice PR from I think Peta where he talks a lot about the blob strategies of the goethereum client, and we kind of took everything that he claimed as an issue from there, and made it as a topic we need to test in the future. 

It would be great if client themes can also kind of coordinate and tell us more things that we should be adding here, we're still not necessarily sure which tool these tests would end up on, but it is something we would need to look at. If there's something on this document that you would still like to see please reach out, if there's information you want to add there please reach out, and yeah we just wanted to kind of use this as a way to, so that everyone has an idea on what sort of testing is being thought of, and if we're missing something that we can catch on the double.

**Danny**
Awesome. So on these blog specific tests, definitely talking with a number of consensus client teams, like the exceptional networking scenarios I think are top of mind, and so things like staggered sending, you know I got blobs I didn't get blocks until later, I got blocks I didn't get blobs till later, you know I got this message not that message and I guess network partitions or other types of like reorgs where I'm going to have to backfill. I think that's like top of mind for concern you know seeing devnet 8 run relatively stably is great, and then but I think it's these like exceptional pads that people are pretty worried about so if you are a condensed layer team and you have been thinking about some of the P2P exceptional cases that you're worried about, I think this list is top of mind to review please.

And yeah Mario's like the bad blob generator from like the transaction gossip standpoint I think is important and also insertion into blocks that we have some failed blocks but I think there's also some tooling and things we want to think about like on just the CL gossip component of these you know sending one without the other sending things in like very asynchronous staggered ways. 

**Pari**
Yeah in case someone already has like malicious client ideas that we could use please let us know. I know there's a couple that we've thought of I'm just not sure if it's a perfect tool for the job. 

**Danny**
Any other questions or comments here? Should people leave comments in the doc or should they reach out to you directly if they have things that they want to they have questions about?

**Pari**
I think to minimize chaos we've set the permissions so that anyone I can actually just change the permission such that anyone can comment maybe that's easiest. Okay if it's something sensitive then please feel free to reach out to me or potentially anyone from the testing team or security team and I'm sure we'll be coordinating on pretty much everything.

**Danny**
…? is that an addition or a concern?

**Potuz**
I don't know so they were asking for malicious clients those two would be the first ones I would implement.

**Danny**
Yeah cool. Okay anything else related to testing? Cancun? Great, anything else related? Yeah go on.

**Danny**
Quick question on devnet 9 in relation to 4788, would it actually change anything now that the kind of spec on deploy is set? I guess because on devnets we might still deploy in this kind of like genesis configuration, although I suppose we could create the genesis have a significant delay before dencun and actually do the like manual deploy method, so maybe that's worthwhile doing in devnet9?

Is that the only difference in the specification at that point?

**Pari**
I think so I don't think there's anything else that's changed since the last event.

**Danny**
Okay so I guess it could give us peace of mind that like this synthetic transaction or address method works, but we would also see that certainly on the next couple of testnet.

**Pari**
Then yeah so we wanted to kind of decouple that a tiny bit and kind of push everyone who thinks they're ready with the builder flow to start using kurtosis today or maybe tomorrow, because I know there's an open PR to the mock builder but the idea is that by the time devnet 9 or devnet 8 with the builder workflow is ready, it should be a nothing burger, like we should have tested everything locally already.

**Danny**
Yeah it's almost like devnet 9 if it even exists, pretty much is should is probably short-lived, it's probably like testing the fork testing, all the load testing, it looking like mainnet, whereas like devnet 8 we really should be we're pretty much at spec other than the deploy method and can test everything here.

**Pari**
This is one of the kind of open question so the past folks we always had one long living test net that we kind of publicized for people who are working on Integrations, examples Kiln, do we need one this time around or since we would have Holesky soon or Goerli, you should be just fork it. 

**Danny**
I do think we need a place that we are telling validators to test their setup, and it could be an A1 of those I think we just need to like make that clear like at some point we're at production, what we think is production setups, and say if you do want to test your setup, this is the place. 

**Pari**
There's just one other point I want to add. We still don't have a final decision on 24 or 36 and at least my talk on the topic is that we should experiment with 36 on Goerli. If it goes badly then no big deal but if we try 36 on Holesky and it goes badly then we kind of have a lot of coordination for nothing. 

**Danny**
Barnabas, all the CLEIPs are in. 

**Barnabus**
Yeah but we haven't written it down I guess. I will add it to this.

**Danny**
Because yeah okay if you're pointing to the CL spec release that encompasses that but being explicit is probably better.

**Barnabus**
Yes sure.

**Danny**
Yeah, what's the reboot cycle on ephemery weekly yeah I mean that honestly is probably the appropriate place to point people to, but we just need to integrate
once we have specs finalized, integrate builds over there.

Yeah I agree Tim. Why don't we work on like a straw man proposal and that we can debate on the next call and kind of have an agreement by then?

Cool anything else related to devnets testing testnets that we want to chat about today? 

**Barnabus**
I think there's another topic about Holesky that could go through. Yeah let me just real quick. 

**Danny**
Anything else on Deneb, Dencun? 

**Sean**
Small proposed change for the builder's effects, this is just to change the constant used in defining the blinded blobs bundle struct, so instead of using the max blobs per block constant which is like the three sorry I think it's six right now, and it's sort of the networking limit for blobs, the consensus layer limit, use the constant that's actually used in the body of a beacon block, and the reason is this struct is actually signed over.

So in creating the signing route the value of this constant actually like will change the signature if it changes. So using the max blob commitments per block constant makes it so across a hard fork, like signatures are the same we don't have to worry about this. That'll be the reason to do it but if you take a look at the link which I post in the chat, it's very small change yeah.

**Danny**
Yeah that seems to make sense. Does anybody have any opposition or want to review and throw a comment up in there? Essentially we have a value to keep the tree the same shape for the consensus, so we might as well use it here. Okay cool yeah take a look Stokes and seems like we can probably merge this pretty quickly. 
Thanks Sean, other Deneb related items before we talk about Holesky? 

# [Holesky Discussion]( https://github.com/ethereum/pm/issues/852#issuecomment-1691582782) [23:55]( https://www.youtube.com/live/RysjOBGRDDg?si=-wzMs4l7pI6p4d-v&t=1435) 

Okay Barnabus?

**Banabus**
So there's a couple of topics regarding Holensky. We initially thought that we should be having Shapella on epoch 10 just so it's convenient for us and if anything goes bad but there was an argument to make to change that to 256. There's an open PR about this. I'm just curious what the different CL teams think about it. 

**Danny**
What was the opposition of 10?

**Barnabus**
That is not power of 8196 slots.

**Danny**
I see so if we were testing error files and things it would not have the same kind of conformance that we've sought on mainnet.

**Barnabus**
Right.

**Danny**
I'm not sure if Yasuke's here but I'm sure you would very much appreciate that and anyone else that might be testing error file distribution. And given it's like kind of a one-time one-day cost, and it seems to make sense to me. 

**Barnabus**
Is there any opposition of doing 256? Because then I will get it merged asap.

**Danny**
Okay yeah sounds good. 

**Barnabus**
Next the next topic would be ejection balance. So we did some calculation and we derived that we should have ejection balance of 28 instead of 16. So this would lead to a nine-day ejection period in case of non-finality. 

Any oppositions against using 28 instead of the 16? 

**Danny**
Okay none from me.

**Barnabus**
And the last one is regarding genesis state. Currently the uncompressed genesis state is 198 megabytes and we are aware that this is probably not something that client teams want to include in their binaries, and there's some different ways to get this genesis state. One would be just an S3 bucket and have a URL pointing to that S3 bucket, and each client would just fetch that transit state on startup. Or from checkpoint sync, but we would need to have an agreement regarding whether we would want to offer this genesis state in a compressed or an uncompressed format. 

So the benefit of having it in a compressed format is I think it reduces the genesis size to about half of the current size, maybe a bit more than half, but it would require more compute from every client to decompress it. 

**Zahary**
I personally tested some formats such as Snappy and zsdd and indeed they took the sizing out and my own suggestion would be to use Snappy, because every client already needs to have a snap implementation anyway. 

**Danny**
I'm sorry was Barnabas, were you suggesting using a different compression algorithm? 

**Barnabus**
I'm just curious whether we want to support a compress or an uncompressed genesis state for checkpoint C.

**Danny**
Yeah a person notes that this is just a one-time thing as you get your client up and running and so the compute probably isn't a worry and it's probably easier to, well I mean I feel like the implication is the compute's not a worry and it's really easy to reduce the download, especially because as ? Snappy
is already embedded. But maybe you're implying otherwise.

**Barnabus**
Okay I don't know that that's fine. Just then you should make sure that every client is expecting an uncompressed or a sorry a compressed genesis ssz file.

**?**
Yeah I don't think Teku is currently supporting that, but if there is consensus and everyone and all the clients are already supporting them, we could start thinking about that. Another option would be what about exposing the genesis state in HTTP gzip stream so the compression will be on the on the HTTP side instead of on the file. Makes sense?

**Pari**
 Yeah I think the idea is just that we wanted to use as much as we can, purely because genesis is in like three weeks. 

**Danny**
Potuz notes that the spec tests are snappy compressed states so there's some path that Teku is using there. 

**?**
Okay so on the SD file format, it's not just a zip version of this. Okay we can double check that.

**Barnabus**
Okay so the general consensus was that it can be compressed?

**Danny**
Yep.

**Barnabus**
Yep.

**Danny**
Zahary, okay are you implying that there's a there might be some tooling and configuration mismatches that the server needs to be aware of?

**Zahary**
No no what I'm saying is that they're not so kind of already available tools that you can use on the command line and say the devops scripts, but there are some, just I'm mentioned this, because it may be not obvious.

**Potuz**
Yeah I second that. I try to look for a command line tools to use snappy directly and I couldn't find anything. Yeah I had to write my own.

**Zahary**
I did find some and yield them successfully but still something to be aware.

**Pari**
Thanks for that. Could you maybe post some links of how you guys came through the problem because then we can upstream it to zcla, which is typically what we're using to inspect the SSZ files. 

**Danny**
Okay anything else on this one? 

**Barnabus**
That's it. Thank you very much. 
**Danny**
Okay that is the end of the agenda. As I noted, I put it on the internet up pretty late so are there any other discussion points for today? Okay excellent. Thank you all for joining. We will talk on ACDE next week. Good luck with all the testnets. 

Everyone says goodbye. 

# Attendees
* Danny
* Nishant
* Ahmad Bitar
* Terence
* David
* Sean
* Marius Van Der Wijden
* mrabino1
* Ben Edington
* Barnabus Busa
* lightclient
* Gajinder
* D (computer)
* Justin Traglia
* Justin Florentine (Besu)
* James He
* Tom
* Spencer
* Paritosh
* Enrico Del Fante (tbenr)
* Fredrik
* pk910
* Joshua Rudolf
* Phil Ngo
* Mikhail Kalinin
* Mario Vega
* Echo 
* Anna Thieser
* Pooja Ranjan
