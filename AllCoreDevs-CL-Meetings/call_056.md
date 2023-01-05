# Ethereum 2.0 Implementers Call 56 Notes

### Meeting Date/Time: Thursday 2021/01/28 at 14:00 UTC

### Meeting Duration: 1.5 hours 

### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/200)

### [Audio/Video of the meeting](https://www.youtube.com/watch?v=_WK3k_k-4w8&feature=youtu.be)

### Moderator: Danny Ryan

### Notes: Avishek Kumar

  


---------------------------------------------------

  


**Danny Ryan**: Welcome everyone. Agenda is there and we will go ahead to be started. We will talk about client update, mid-year updates.

Here is the [document](https://notes.ethereum.org/@vbuterin/HF1_proposal), the top three things, we are generally to go. Couple of fork choice stuff, issues, that specs are being updated to resolve these issues right now. These issues must be resolved right now. But the 2nd of the issues I would like some engineering input on complexities of dealing with that fix in the context of the production [?](https://youtu.be/_WK3k_k-4w8?t=400) implementation. beyond that there are a couple of nice to have. we have been playing around and we are looking for the right kind of compromise to see if we can get the stuff cleared out and that would like to make a decision next to by two from now but in the meantime would release and release test documents and other things for the features that we had decided on.

Anyways , let’s do client updates and we can talk about anything in there that would like to and go from there. We do have a research Workshop, Hsiao-wei wang has been organizing, a mix of some presentations on educational stuff on merge and sharding and hopefully a lot of dynamic discussion engagement. This will likely be streamed, it will certainly be put on YouTube for public consumption at some point, so let's go ahead and do Client dates that start with Nimbus today.

  

# 1-client-updates

  

Is anyone from Nimbus ready to do an update if not I go to somebody else.

  

**Jacek Sieka**: Just wait a second. Mamy is having some connection issues.

  

**Danny**: Let’s do Prysm.

  

## Prysm

  

**Raul Jordan Prysmatic**: Hey guys, here update for the last few hours

* we are working finalizing the [EIP-3076 slashing interchange format](https://eips.ethereum.org/EIPS/eip-3076).

* We are complying with the lighthouse spec.

* We are working on Eth2 API implementations, just making progress in connection to the end points.

* Improving proposal efficiency on patching attestation and order and magnitude improvement and

* working on internal design documents and working on first network upgrade scoping as necessary work and planning.

* We are working revamping slasher from the ground up and improved and then totally revamped a local slashing protection.

* working on improving stability and codebase.

  

**Danny**: Curious on the slashing protection, what’s the fundamental approach there?

  

**Raul Jordan Prysmatic**: Yeah, we just used smarter database schema, previously we kept fairly naive approaches, kept a lot of spams in order to consume a lot of memory and it ended up being inefficient especially when we have thousands of validators on a single instance. Now even though we have thousands of validators on Beacon node, it will become reasonably. So with this level of database and a smarter schema and indexing, led us down the better path.

  

**Danny**: Cool. Thank you. Mamy did you get your mic sorted, let's do Nimbus last. Let’s do Lighthouses.

  

## Lighthouse

  

**Age**: hey everyone, Recently

* we have new release v1.1.0. has more sophisticated validator monitoring features, it was well received.

* On top of that, we will look into some more data analysis of attestation performances across all of our nodes.

* We found that late propagation of blocks is causing issues with attestations performance to degrade.

* We have been optimizing the cost of propagation for block propagation. And we have it flat to 3-15 millisecond, which is a significant improvement. Hopefully, it will improvise the attestation performance.

* The other thing which is degrading is we have been receiving blocks early to the slots, so we are adding caches to keep those blocks in the memory and process when they come.

* We are going to start Looking into the Eth1 and Eth2 merge API. Hopefully we should start getting implementation in the Lighthouse in the near future. Over a few weeks we should be getting the attestation performance to be as close to perfect as we can get.

  

**Danny**: Okay cool, Lodestar

  

## Lodestar

  

**Marin Petrunic**: so, we basically

* have a new sync implementation. It is supposed to be a lot faster.

* It does a lot of things in parallel and we are tracing it out.

* We are trying to keep a 2 week release cycle. So hopeful we will have a stable client,

* We are also running a validator on a testnet, generally some hiccup here and there but generally seems fine.

* Doing a lot of Light client prototyping, just implemented some spec.

* Doing some changes to the database to allow us to keep blocks from different forks.

  

**Danny**: Got it thank you and next Teku

  

## Teku

  

**Anton Nashatyrev**: Yeah hi so

* we had next release v21.1.1 here we have added support.

* Currently UPnP support is almost ready.

* We are working on refactoring to be able to support upcoming forks/upgrades, it’s the most challenging part now.

* We are enabling gossip scoring.

* Continuing improvement of sync and we are also updating to the latest Blst library.

  

**Danny**: Got it thank you and next Nimbus

  


## Nimbus

  

**Zahary**: I must have some partial update, some of these on top of my head probably, I miss something. Most important thing within this week is that

* we integrated batch verification of BLS signatures for better performance.

* We are also seeing more multithreading in this area.

* We are trying to get an upstation before verifying for signature verification.

* We also solved important issues which resulted in very long processing of blocks with deposits, which rendenderd the client unresponsive for a shorter period which sometimes resulted in misattestation.

* Also, solved the issue with Eth1 monitoring.

* We are also experimenting, did some peer management in lipp2p but this is a bit ongoing.

  

**Danny**: Got it. Thank you.

  

# 2. Upgrade 1

  

**Danny**: Okay moving on. So I expect this conversation probably to be ongoing over many weeks but that document was shared based on your team's review. Is there anything that you would like to discuss today? What we can do, so we can do a more async engagement, to move most of the structure of that document into more like a checklist format on to the Spec repo for async discussion.

  

**Vitalik**: I guess while we are here, do people have either more general or more specific thoughts of any kind of ideas or proposal of doing this kind of hardfork in roughly the time that we’ve been suggesting.

**Danny**: Broadly **timeline being this initial upgrade mid-year summer, focusing and then production testnets of one of the major upgrade sharding or merge by end of this year.**



**Jacek Sieka**: I think maybe the better question is like if you are going to do this hardfork, when do we start upgrading the testnet? What will be the timeline? how much do we need to test this before we’re comfortable releasing it on the mainnet?

  

**Danny**: Good question. I would prefer a minimum of one monthly time on my transitioning major testnet but to see testnets, local testnet and other testing, certainly a month prior to that.

  

**Vitalik**: Great, the reason why we are asking people to pushing on this is because we really want to get to the hard agreement on the content to hardfork ASAP. If we can get total consensus either on all of the features or all of them but one within 2 weeks, that would be amazing. One month of the mean time between the testnet and the mainnet definitely seems to be roughly standards for the time especially given that things on Eth 1 usually works, but then smaller testnets should probably just start happening as soon as developed in each client.

  

**Terence**: When do we need to come to a consensus on the bonus section, would you say that two weeks is a fine time frame?

  

**Vitalik**: Good question so part of the reason why I called this as a bonus section in that document because I know that those items are a bit deeper than the other items and so it might take longer or so if like in 2 weeks we get consensus on everything except for the bonus section, then that’s fine. If that happens what that means then the client team should just start development, building and even testing everything outside the bonus section and then add in the bonus section, at the end, basically do it last. So it is okay if final decision on the bonus section takes a bit longer than the other parts.

  

**Danny**: I’d say in terms of having concrete directions for those items. I would like to have in two weeks either we think this is a reasonable path on specs and would like input in review or we don't really have a reasonable path on specs and want to drop them. So at least in 2 weeks time if we’re not going to make any decisions, at least we would be in a position to evaluate.

  

**Vitalik**: For each individual item, either don’t do it or do option 1 or do it some other way. Basically, the more we can decide on, the better, but that's a possibility that thinks it would be some small detail that we decide which should be changed after it gets implemented a couple of times and we're just worried that it makes more sense and that’s unavoidable anyway.

One more just kind of quick warning on the bonus section by the way for those who have been following the document closely. I did come up with a new version of the empty epoch processing improvements that got literally turned into a PR over the last two days. So it takes a different approach, basically it amortizes offline penalties every 1/64 of epochs instead of every epoch and it does have its own trade-offs, so when you’re reading through things, just watch out for that.

Aside from the bonus, I don't think any of the other sections have really been significantly touched for quite a few weeks now.

  

**Danny**: Alright. Anything else you want to discuss over here?

  

**Vitalik**: On the HF1 topic, we’re expecting to make decisions in the next meetings. Hope we can all be prepared for the discussion in two weeks. Happy to answer any questions on the async channels.

  


**Danny**: Okay moving on, research Updates

  

# 3. Research updates

  

**Danny**: I believe it is **on February 2nd on Tuesday, we are having a research workshop** As I mentioned, Hsiao has been organizing that and should have been in touch with the team here.

  

.I don't think we have much to discuss here. Hsiao-wei wang do you have anything that you want to add here?

  

***Hsiao-wei wang**: Yeah so we will send the announcement to attendees by this week and we will share the youtube link later by monday I think.

  

**Danny**: great any more on research updates?

  

**Vitalik**: Dankrad has been doing the primary work and I have been helping a bit on an implementation of Verkle trees, that is probably more relevant to Eth1 developers than Eth 2 devs. Can’t think of anything from Eth 2 side.

  

**Danny**: If Verkle tree are eminently viable, would you Dankrad suggest migration to Verkle tree instead of binary merkle tree?

  

**Dankrad**: For storing state, it would be much more efficient from the witness size point of view to use a Verkle tree because it will use fewer levels. As Vitalik said it is mostly more relevant to Eth1 statelessness at the moment but the Kate commitments that we’re using is obviously relevant for Eth2. I will be giving an intro to Kate commitments on Tuesday.

  

**Danny**: Any particular resources, you’d want to share if people want to be caught up on the basics?

  

**Dankrad**: Yeah sure, I can do that.

  

**Vitalik**: Dankrad’s [blog post](https://dankradfeist.de/ethereum/2020/06/16/kate-polynomial-commitments.html) is recommended for kate commitment.

  

**Proto**: About Kate commitment, some people have shown interest in implementing those now, so it may be a good idea to start sharing findings with the implementers. I know Mamy from Nimbus is working on their implementation, Dankrad probably help to those interested. I know one of the outsider is looking into this. Anyone interested, please reach out to me on Discord.

  

**Danny**: Other research update.

  

**Mikhail**: Quick update from the merge side. we have started to work on the specs. There’s an initial draft and after some round of review it's going to be a pull request to the spec repo

  

**Danny**: Okay great, other research update.

  

**Leo BSC**: In BSC, we’re integrating the last updates on rumor on the crawler. We managed to solve the problem we were having previously. Now we get more accurate vision of the network. We’re moving forward in that aspect.

  

# 4. Networking

  

**Danny**: Thanks Leo, other updates. And networking items, does anybody has any comments, questions, thoughts, issues.

  

# 5. General spec discussion

  

**Jacek**: I could mention one thing, we’re figuring optimization in the spec and there are these functions that are executed for the block processing. We noticed in the spec test that if you run the test in a spec function is written, it works but then the given pre-states for the tests are actually invited. if you work with the pre-conditions that are established in the Order of Operations in process blocks. I'm just kind of curious if there's any appetite for fixing stuff for phase 0 or do we just leave it as is?

  

**Danny**: I mean if you want me to point me to a few of them and I can see if they are easy to fix, I will be happy to. You are talking about the disparity between get block proposers from state vs. getting the index from header?

  

**Jacek**: Exactly. As if the header wasn’t updated. I think the function hadn’t been run during the test generation.

  

**Danny**: I see because it's actually in the header sitting in the state rather than in the block header.

  

**Jacek**: Exactly. The test is valid but the state is like it could never happen in reality. SImilar issue to fuzzing.

  

**Danny**: is this because you want to have scripture validations in data or is this because there are certain optimization passage can't take because the way testing might have forced you to certain sources of data thing?

  

**Jacek**: It’s the later really, but also the statement on like how valid is the test but doesn’t have valid incoming stake? you could ask some question, perhaps.

  

**Danny**: Right I guess they were testing a function, you can make an argument that it doesn’t matter, but I see the value. As you find these, write them down, I'm happy to see if I can fix the test easily. there's a lot of different tests and types of tests in the way that they're kind of generated in some of them might be easier to fix than others.

  

**Jacek**: Yeah, because the optimization is kind of minor.

  

**Danny**: I am happy to clean them up but I don’t have a single fix for the entire test weed, I will have to look up.

  

**Jacek**: I’ll open up the first one that I found.

  

**Danny**: Yeah. Okay anything else today, spec or otherwise?

Great, we will have a long fun hangout on Tuesday, so will talk to you all then. And probably talk to you on the internet, otherwise. Take care, bye!

  

  

----------------

## Attendance

- Danny

- Leo BSC

- Vitalik

- Dankrad Feist

- Lightclient

- Mamy

- Marin Petrunic

- Ben Edginton

- Andrian Manning

- Terence

- Hsiao-wei wang

- Carl Beekhuizen

- Aditya Asgaonkar

- Alex Stokes

- Mikhail Kalinin

- Afri Schoe

- Zahary

- Lakshman Sankar

- Proto Lambda

- Anton Nashatyrev

- Raul Jordan Prysmatic

- Jacek Sieka

- Meredith Baxter

  
  

## Next Meeting Date/Time : Feb 11, 2021 at 1400 UTC

  


## Zoom Chat

  

- https://github.com/ethereum/eth2.0-pm/issues/200

- https://notes.ethereum.org/@vbuterin/HF1_proposal

- https://vitalik.ca/general/2021/01/26/snarks.html

- https://dankradfeist.de/ethereum/2020/06/16/kate-polynomial-commitments.html