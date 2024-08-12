# Consensus Layer Call 139

### Meeting Date/Time: Thursday 2024/8/8 at 14:00 UTC
### Meeting Duration: 1 hour
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1116) 
### [Audio/Video of the meeting](https://youtu.be/o8p47gIt7Bs) 
### Moderator: Stokes
### Notes: Alen (Santhosh)

## Summary <!-- omit in toc -->
Summary | Description
-|-
139.1  |**Pectra Updates** Stokes said that EF Researcher Hsiao Wei Wang is preparing the next official release, alpha.4, for Pectra CL specifications. It adds a variety of fixes from the previous version and will be released by Wang shortly.On the topic of Pectra Devnet 2, EF Developer Operations Engineer Barnabas Busa said that the network is stable and has reached 85% network participation levels. There are a few bugs to work out in execution layer (EL) clients, primarily EthereumJS and Erigon. Most CL clients are stable on Devnet 2. However, Busa mentioned a minor issue in the Prysm client that needs further investigation. EF DevOps Engineer Parithosh Jayanthi added that investigation on an issue between Lighthouse, Teku, and Besu nodes is also needed by client teams.
139.2  |**Pectra Updates** improvements to communications about the launch of devnets. Prysm developer Kasey Kirkham wrote in the Zoom chat, “I didn’t realize when Devnet 2 was starting up.” To ensure that the launch of Devnet 3 is properly communicated across all client teams, developers agreed to create a weekly meeting series for testing updates about Pectra. Like the testing calls that had occurred in lead up to the Dencun upgrade, these meetings will be hosted on Mondays, though developers have yet to confirm the exact time. Jayanthi said that testing calls can be kept short, 15 to 30 minutes in length, and focus primarily on testing updates related to the various devnets related to Pectra, which include PeerDAS and EOF devnets.
139.3  |**Pectra Updates** On the topic of Pectra Devnet 3, developers reconfirmed that it would feature the exact same set up EIPs as Devnet 2. However, it will also feature the most updated EIP 7702 design and developers will earnestly test the interactions of this code change with the other core Pectra EIPs. Lodestar developer Gajinder Singh noted that on Devnet 2, developers found issues with EIP 7251, MaxEB. There was an issue with consolidating validator staked ETH deposit balances that has since been debugged but will need further testing on the next Pectra devnet.
139.4  |**Pectra Updates** As discussed on ACDE #193, there is a new Engine API specification that enables CL clients to fetch blobs from the EL blob transaction mempool. The method is called “getBlobsV1”. To avoid its misuse, Teku developer Enrico del Fante has proposed a few clarifications to CL specifications. Stokes recommended developers review these clarifications and aim to test the use of this method on Pectra Devnet 3.
139.5  |**Pectra Updates** developers discussed mplex deprecation. Mplex is a protocol used by CL clients that allows multiple data streams to be sent over a single communication link. Mplex has since been deprecated by its maintainers and CL client teams are aiming to transition over to a new data stream multiplexer like yamux. Lodestar developer Phil Ngo said that implementation and testing for yamux is complete for their client. However, they would prefer switching over to the new protocol rather than maintaining both for a period. He explained that supporting both mplex and yamux creates overhead for their client. Nimbus developer Etan Kissling said that his team is in the process of testing yamux. Developers agreed to follow up with the other CL client teams on this topic and revisit the discussion on how to transition away from mplex in a few months’ time.
139.6  |**Pectra Updates** On another topic related to Pectra, Kissling asked whether developers were ready to decide on the inclusion of EIP 7688. The code change introduces a forward-compatible data structure that smart contract developers can utilize even as Ethereum developers change the EL’s data serialization method from RLP to SSZ. The full SSZ transition will not happen in the Pectra upgrade. However, Kissling has proposed EIP 7688 to introduce a data structure that will ensure forward-compatibility of EL-related related data changes in Pectra EIPs.
139.7  |**Pectra Updates** Stokes was not enthusiastic about including EIP 7688 in Pectra, saying the upgrade was “already massive.” Jayanthi wrote in the Zoom chat that the earliest developers could feasibly add EIP 7688 to Pectra testing would be Devnet 5. Representatives from Lodestar, Prysm, Teku and Lighthouse teams were supportive of including EIP 7688 in the upgrade. Stokes and Beiko recommended that developers refrain from adding any new EIPs in Pectra until all existing Pectra EIPs are stabilized. Kissling agreed with this recommendation and sought clarity from the group on when to bring up this topic again. While there was no clear answer, developers seemed agreeable to considering EIP 7688 again shortly before the launch of Pectra Devnet 5.
139.8  |**PeerDAS Updates** Prysm client team shared an update on their PeerDAS implementation. This sparked a discussion on the necessity of the “blobsidecar” Engine API request. Stokes recommended discussing necessary changes to the Engine API due to PeerDAS on the next PeerDAS breakout call. Stokes highlighted that an EF Researcher has drafted formal specifications for removing the activity of sampling from PeerDAS to reduce upgrade complexity. On the latest PeerDAS breakout call, the proposal raised concerns that removing sampling may make it more difficult to add in through a later hard fork. Further, it remains unclear how the removal of sampling will impact the extent to which developers can safely increase the blob gas limit in Pectra. EIP 7742, a proposal to uncouple the blob gas limit across the EL and CL, was raised again on this week’s call. Stokes said that he would update the EIP and developers can discuss inclusion of it, along with topics related to changes in the blob gas limit in Pectra, on the next CL call.
139.9  |**Research Updates** The first was related to edge cases when validators are consolidating their staked ETH balances under EIP 7251. Kissling explained that validator balances may not update for an extended period during the consolidation period, and this may cause the protocol to incorrectly assign sync committee responsibilities to a validator. Stokes noted that these concerns are similar in nature to how the protocol processes validator exits. He recommended leaving the design for consolidations unchanged and instead leave a note in CL specifications that acknowledges the edge cases related to consolidations.
139.10  |**Research Updates** Ethereum’s networking layer, specifically the addition of a “quic ENR entry.” Quic stands for Quick UDP Internet Connection and it assists nodes in sending and receiving data. Stokes recommended creating a pull request (PR) on GitHub to further detail the exact changes for the quic ENR entry.
139.11  |**Research Updates** ProbeLab, a blockchain analytics firm, shared an update on the data they have been gathering weekly since the beginning of the year. In their latest report, they identified 8,335 nodes operating on Ethereum. 42% of these nodes are running on the Lighthouse client. 36% of nodes are operated by users out of the U.S. Roughly half of these nodes are run via a data center. Prysm developer “Potuz” asked why the number of Lighthouse nodes hosted through a data center is higher than the number of Lighthouse nodes that are self-hosted. Stokes hypothesized that the reason could be that the predominant users of Lighthouse are institutions and professional node operators.


**Stokes**
* Okay, cool. I believe we are live. Let me grab the agenda. Let's see. There we go. Hi, everyone. Welcome to consensus. That is the first item on the agenda. Okay, cool.  there's the right link. So this is consensus layer Call 139. I put the agenda in the chat here.  it's PM issue 1116. and. 
* Yeah, looks like we have quite a number of things to get through today. So let's get started.  first up, Electra, and I think Shaowei is a few minutes behind.  but she wanted to call out that there's a PR for a new specs release Alpha4,  Let's see, that was the link that I put in the chat just above there. So yeah, generally just an FYI, there's a few things from the last release. Nothing to major.  but yeah, that should be really soon. So next up we can look at the devnets. 
* So we have Devnet2 now.  let's see maybe Barnabus, if you give us an overview of Devnet2, it looks like it's been going pretty well. 

**Barnabas**
* Yeah, sure.  so in the past few days, we've been working on trying to get the chain to finalize. Yesterday, we managed to get over 85% participation and,  voting correctly. Currently, we still have a few, execution client bugs, but I think most of the consensus layer clients are able to propose properly. We just did a quick non finality test, and we found a,  smaller issue. And when we try to come back, but,  I think they can give an update on that everything else is pretty okay. And all the issues have been reported for the appropriate client teams. 

**Stokes**
* Okay. Awesome. Are there particular like EIP that were causing issues or is it kind of just a mix of things? 

**Barnabas**
* Could you please repeat that? 

**Stokes**
* Yeah. You said there were some issues with the Devnet. I was just wondering if there were, like, was it a particular EIP or was it more just a mix of different things across the clients? 

**Barnabas**
* So Ethereum JS is just having a general hard time keeping up to the chain. And Aragon had some blog building issues that they're working on. I'm not sure if anyone from  Ethereum JS or Aragon are here to give us an update. 

**Gajinder**
* Yeah. basically, whenever the blocks will be full, it will start lagging. But yeah, apart from that,  as I inspected,  lighthouse Ethereum and it sort of,  was sent to the head, so I didn't inspect other nodes with,  Grandin. I think there is an issue of optimistic think because,  when Ethereum is trying to pull optimistic sink blocks, basically Grandin is forcing Ethereum JS to optimistic sink.  even when starting from Genesis, I think it jumps the blocks or some somehow forces it to optimistic sink. And when when Ethereum JS is pulling  the blocks from other EL clients,  using e-nodes.
* So it is throwing an error that it the block bodies they don't have request bytes, which is basically,  something the other clients might need to rectify, or they might have forgotten adding block bytes,  request bytes to the block body. So I guess this is something that your clients might need to fix. 

**Stokes**
* Radek. 

**Radek**
* Yeah.  just wanted to briefly,  say what happened,  on prism since we were mentioned. So it was just that,  we didn't we forgot to update,  validation on,  aggregates for Electra. It was it is related to the attestation EIP. So we were losing peers,  on the minimal configuration because Prism thought that the committee index is incorrect and the validator does not belong to the committee. And so it is done Downrated And we started losing them at Electra. So but the fix is already,  in a PR and it will be merged today. 

**Stokes**
* Cool. Pari

**Parithosh**
* So just to add this,  another issue that I've  posted in the lighthouse node thread on discord. So I tried a Kurtosis devnet with just lighthouse and Teku. And when I submitted a consolidation lighthouse seems to complain that there's a missing field of source pubkey from Besu and then it fails to propose. This fixes itself once another client is proposed a block so it feels like Besu or. Yeah, I think one of them is not communicating properly likely Besu.  yeah. 
* It would be great if someone could have a look at that one. Cool. And we we can also slowly talk about Devnet three because I also noticed Cassie's message. And I agree that we should probably coordinate a bit better on these calls as to when we do Devnet relaunches, because I think we have everything we kind of want from Devnet 2 the main thing is if 7702 feels ready, then we can start talking about Devnet three. 

**Stokes**
* Right. Yeah, that was my next question. So it sounds like there's some debugging on Devnet two.  generally we feel like the non finality experiment went well. It sounds like. Other than maybe some minor issues with prism.  but yeah. So assuming that all comes together then I think Devnet two I think will be about as much as we're going to get from there. Then with Devnet three. Yeah, I think 7702 was the main thing.  maybe just for my own knowledge.  is the spec there together? Is it ready or not yet? Does anyone know? 
* Okay. Yeah, we got Devnet three was two and then the 7702 last PR.  okay. I mean, I'll assume that basically means it's underway, so. Right. 
* So then okay, so it sounds like Devnet 2, we still have some things to do. Devnet 3 needs a little more time, but you know, hopefully that's sounding like in the next few weeks, even sooner would be better.  but yeah, next few weeks, then,  we'll be in a good place for Devnet3.  anything else on deep net two that we should discuss now? 

**Gajinder**
* Worry. Have you discussed the consolidation issue? 

**Parithosh**
* Not yet. Do you want to bring it up? 

**Gajinder**
* Yeah. So basically,  Pari did an experimentation,  on Devnet 2 regarding consolidation. So two times we tried to consolidate,  one validator into another. And,  what really happened was that instead of consolidating the balance,  so basically consolidation as such went through in the sense that one validator was sort of exited and other validators compound,  withdrawal credentials changed to compounding, but the balance was not consolidated.  What really happened was that the source validators balance was sort of withdrawn, and the reason for that was that there was a one off work for which  Mikhail raised a PR.  so in process, pending consolidations as well as in process deposits.
* So there there was a one off,  in the, in the epoch calculation that is used because if you use get current epoch of the state it will, it will not come to the, it will not it will be one less than,  the epoch transition for the epoch for which you are running.  So that sort of fixes comparing it to the next epoch sort of fixes the issue and the PR is merged. And I think in the next dev net,  we will try consolidations again where the behavior should be correct. 

**Stokes**
* Right. Yeah. Nice. Fine on that one.  I don't know. I'll check with Charlie. I don't know if that will go into Alpha four, but that would then suggest it will go into an alpha five. And I think it makes a lot of sense for Devnet 3 to have that included.  So yeah, we'll be sure to get that taken care of. 
* So there's some chat here around devnet coordination, testing timing.  let's touch on this. So. Right. I mean, maybe a good place to start is just,  barnabas's comment here around a testing call.  I know we all have plenty of calls already.  Do we feel like a breakout for this sort of thing would be helpful? Or do we want to try to coordinate more async? 

**Parithosh**
* I think in the past the breakout had been helpful. We can also keep it really short. Instead of a one hour break off breakout, we can just keep it 15 minutes or half an hour if required. 

**Stokes**
* Right. And like, maybe we could just do them one off, like just for devnet launches rather than like a standing call. 

**Barnabas**
* I think standing call is better because we always every week we will have something different, especially when we have continuous devnet and we're going to have,  devnet we're going to have eof Devnet we're going to have better devnet. So there will be a bunch of,  topics to discuss. 

**Stokes**
* Yeah. Makes sense. Uh. Let's see. Should we just use the same time from the previous testing call? 

**Barnabas**
* That was Monday 4 PM, I think. 

**Stokes**
* Yeah, something like that. Okay. I mean, it sounds like it would be helpful, especially as we get closer to shipping factor. So I think that's probably a good idea. I'll just ask, why not use the first of these calls? I mean yeah, but so yeah, put as a suggestion like just using now basically. But it seems like even in addition to this, there's space for more fine grained discussion.  so I think it makes sense. Again, the call is optional, but it will be a dedicated time for people to talk about exactly this, and hopefully it will smooth the whole devnet process. Cool. Any other comments on Devnet 2 or Devnets?  

* Next up we have essentially some other things that will go into some devnet, but just around processing things. Any closing comments? Okay, so let's see if I have all my numbers. Right. I think the idea was for net three we would include  this change engine git blobs to v1. Let me grab a link.  so yeah, basically the idea here is like we could save on a lot of bandwidth with blob propagation. If a node has a way to essentially check their mempool first. And I think this makes a lot of sense. Right. Like presumably blobs are in the mempool and you kind of already have this propagation process just via the mempool. And yeah, this essentially provides a way to,  avoid needing to fetch data twice.  with regards to do you have a comment on this? 

**Lukasz**
* Yeah, I put the comment in the PR today, but the comment is that, EL as far as I know, at least, Nethermind. And I think we looked into ref implementation. Keep the data by transaction hashes, so,  not by blob version hashes. And the question is, does CL have this data and can request this by transaction hashes or at least add transaction hashes to the request? It would be very straightforward for us to implement it. 
* If it will request by blob version hashes. We either need to iterate through all transaction pool, or need to build a separate index to keep the data in this way which is adding a bit of complexity. So the question is does SQL have transaction hashes to that can request by it? 

**Stokes**
* Right.  let me go check. Yeah. So. But it says transactions are raw bytes, so there might be a way to recompute them.  I'd have to go check the PR to see what they proposed. But doing it by commitment is what makes the most sense. So I see the issue here. 

**Lukasz**
* So if not, it's like it's still doable. It's not like it's a deal breaker. It's just a difference between a bit more work and something really released or or worse, not a suboptimal performance, which still might be good enough.  but if the transaction hashes were available, it would be extremely straightforward for us to implement. 

**Stokes**
* Right. Do any CL clients care to comment? 

**Potuz**
* It's going to be hard to break that invariant that we don't need to interpret anything inside of the payload Particularly transactions are just raw bytes for us. So one way out of getting the EL to do this is for us to request the transaction hashes for a given payload, and then the EL given this back to us. But I think this probably is harder. I mean, doing this in two communications is probably harder than just asking the to keep this map. 

**Stokes**
* Yeah, that'd be my intuition as well. That essentially just having this index on the EL is the simplest way forward, even though it is a little bit more there. 

**Lukasz**
* Okay. Just wanted to you know ask if this is possible, and if not, that's fine too. 

**Stokes**
* Cool. Thanks. So okay. That was good. And related to this was a clarification to the P2P spec. I also dropped this PR in the chat here it's 3864 and generally this makes sense along with the other change.  yeah. Take a look. There's been some review and yeah, I think the next step would be to get both of these merged and then they can go into devnet 3. Let's see, I don't think Enrico is here, but yeah. Has anyone had a chance to look  anything they would like to discuss about these two PRS at the moment? 
* Okay, cool. So yeah, just be aware the intent would be to get these into Devnet 3. So take a look and we'll get them merged shortly. Let's see I lost the agenda. Here we go. Cool. 

# mplex deprecation: Deprecate mplex consensus-specs#3866 [21.26](https://youtu.be/o8p47gIt7Bs?t=1286)
**Stokes**
* So next up we had a request to discuss mplex.  so lighthouse's been working for quite some time on deprecating mplex generally.  I don't think. Well, I think there's a number of issues with it.  but. Yeah. So age was asking for essentially timelines in the past. We've generally agreed to go ahead with deprecation, but it's the sort of thing where clients need some alternative. The alternatives aren't quite baked. So yeah, he wanted to discuss general status there. As far as I've seen so far, Teku is saying that they essentially have progress on this alternative, but it's not quite ready.
* Any other clients have an update on mplex deprecation? Do you feel like you could? Are you ready already?  do you feel like you need more time or any thoughts on timeline? 

**Phil Ngo**
* So I can speak for Loadstar here. We have started testing yamaks on our side we noticed that we have a lot of,   performance gains with yamaks, but that's only with Yamaks on its own. And when we enable that with Mplex,  the combined overhead gives us issues. 
* So, you know, we're kind of ready to switch over to jam at any time, but we prefer to just, you know, switch off Mplex and go right to Imax. But we also don't want to cut off our other peers. So that's kind of our status at Lodestar. 

**Stokes**
* Gotcha. Yeah. I mean, that kind of implies then that we. Well, yeah, that one's tricky because it almost implies we just want to switch out our hard fork. If there's going to be issues like this for everyone. Around performance. 

**Potuz**
* Yeah, I think.  It means that there's going to be some time to switch off. Not that it needs to be coordinated at a fork. 

**Phil Ngo**
* Yeah. This is just in our case specifically. It's just when we have both Mplex and yamaks enabled,  we, we get a lot of churn and are not a very good peer with,  with both of them enabled. So our preference is just whenever people are ready to just kind of go over the yamaks. 

**Adrian**
* Yeah, I'm not sure about the state of Nimbus. I know Prism's fine. So if Teku can support both at once, then it should be fine to swap over, I imagine. And unless we do it at a hard fork, there's always going to be old nodes that haven't updated, though. 

**Potuz**
* Can't load star. Just add a flag and you just pick one or the other one and then your loadstar nodes are going to be only paired with some subset of the network, at least until we deprecate the templates. 

**Stokes**
* I mean there is like if everyone switches to yamaks and then Loadstar is still on in Plex and they just kind of prune themselves off the network. 

**Phil Ngo**
* That could be an option. 

**Adrian**
* Does anyone know where Nimbus is with this? 

**Barnabas**
* We have it implemented. I'm not sure how well it is tested compared to Amplex, but,  if Dustin is on the call, I'm not sure.  I don't see him today, but,  I could ask him. 

**Adrian**
* Okay, awesome. It just means I just chase up Teku, and then. And then we're all good. 

**Stokes**
* Okay, great. So, yeah, follow up with Teku and then. Yeah, maybe in another month or two.  we can revisit this on CL call. Okay. Any closing? mplex discussion. Otherwise we will go to the EIP-7688 SSZ StableContainer inclusion in Pectra. 

# EIP-7688 SSZ StableContainer inclusion in Pectra [26.02](https://youtu.be/o8p47gIt7Bs?t=1562)
**Stokes**
* Okay.  right. So Ethan wanted to discuss,  inclusion of EIP 7688, which is the stable container EIP.  let's see. I don't know, Ethan, do you have any,  quick update you'd like to give around this?  before we move on to discussing inclusion. 

**Etan**
* Last time, it was mostly this,  devnet two instabilities that we wanted to resolve before discussing extending the scope. Which  makes sense.  now, from today, it seems that those issues have been fixed, and that their network two stable. So the remaining question now is if we could include the 7688 stable container without risking peer DOS getting out of hand?  at least in Nimbus, it's not the same people who work on those features. So from our side it would be fine.
* But I would like to also ask the others for opinion and that would be for Devnet 3 like that. The one in a couple of weeks. Not like something that needs to be rushed out on the implementation side.  Guillaume has started on zig as a C implementation.  I also saw that Casey asked something about testing in the chat, so I guess that he's in his continuing progress as well on the go implementation.  Ross is also still incomplete, as I know, but,  yeah, there's,  Devnet on the stability. Now, that box, if you scroll down to the left, there is a cortosis config. Yeah. that's essentially the update.
* And yeah, what I would like to ask about Devnet 3 inclusion of this feature. 

**Stokes**
* Right. And just to clarify, I wouldn't I mean it is it could go to some devnet. But I think the bigger question is do we put it to Pectra? 

**Etan**
* Exactly. Yeah. 

**Stokes**
* Right. And I mean, again, just to make the point again and again, Pectra is already massive.  but yeah. Do any clients here have a have a sense on this?  how are we thinking about it? 

**Kasey**
* I'll talk for real quick that,  I have  passing tests,  with our new code generator.  so there's a lot of steps for us to switch over to that new code generator. So,  whether it's able to land in a devnet in two weeks is a a little iffy just on the timeline.  but I think we're we're positive on inclusion overall.  yeah. 

**Stokes**
* Right. So again, this kind of gets away from us, like, I'll echo what Perry's saying in the chat. Like it would be devnet five or later,  before I think we'd even see this on a devnet. So the question is not so much like, oh, do we rush this feature? Like now? It's more just like, does this stack up along with everything else?  and again, I would strongly urge you to consider the size of Pectra. 

**Sean**
* Yeah. For lighthouse, we have a solid implementation of this,  and something I guess unique to the SSZ changes versus other changes. Is that, like, as we add the as we upgrade this in the spec, we'll get all the SSZ tests updated so we'll be able to like regression test a lot of stuff.  So it could be relatively well tested as far as like a,  a layout change.  yeah. I sounded like people from lighthouse generally supported it.

**Stokes**
* Right. But there's like, support now vs like in the next hard fork, you know, like there's like yes, I think we all agree that the features are beneficial, but then it's very much a question of like scheduling and then like the testing load across DevOps and the different testing teams, the testing that each of the client teams do individually and all of this stuff. 

**Sean**
* Yeah. So there's a timing component thing.  that's. Yeah, I think on some level that's who needs to use this feature. And how big of a deal is it for them to use this feature by Pectra or like a year plus later? So. Yeah. And I feel like I haven't really heard much feedback about that, but. 

**Adrian**
* Yeah. So I have been speaking to some people. I saw that Rockpool had a thread and that's been posted. I also spoke to Eigen Layer, and their opinion is that with some of these hard forks, we're actually changing core things in the protocol, so they have to update their proofs anyway. So stable containers isn't really a like a massive thing for them to have. They have to change the proofs anyway, essentially. 

**Stokes**
* Potuz. 

**Potuz**
* Yeah, I want to say two things, but one of them is what Adrian just said.  one is that there's been two arguments that I've seen, one from Sean from lighthouse about having a prescribed overhead to ports.  which is true, we have a finite amount of time that it's added to every fork in testing and getting it and shipping up. But on the other hand, there's this is offset by the exponential amount of time that testing grows with adding new features, because you need to test every single combination of them. And this is exponential.  
* So I would urge next time we already screwed up this port by adding indiscriminately many features that we shouldn't have had to keep this exponential growth in mind. As for this particular one I mean, again, I'm definitely biased in that I am pushing for a change like BPS, but any such change will change, will not be contemplated by stable containers. We will change all of the G indices, as soon as we move a payload outside.  and it's hard to believe that we're not going to be making changes in the protocol that are not going to be contemplated by stable containers.
* So I sincerely doubt of the impact on contracts for stable containers, I can certainly see that some contracts might be saved from changing. But I can also see how rocket pool Rocketpool might need to change their contracts anyways. 

**Stokes**
* Right. And yeah, I mean to add to this I would just probably echo what Tim saying in the chat here that essentially, you know, let's focus on getting the current feature set working. Well a devnet that's going to pursue from Genesis before really opening the scope discussion further. So can we agree to that? 

**Etan**
* From my point,  it makes sense. Yeah. Like to delay it until the rest is more stable.  with the caveat that we should,  have a time at least, where we definitely agree on, like, we we cannot indefinitely delay the decision. Right? 

**Stokes**
* What we should. I mean, it could be a thing where, you know, it might take, you know, a hard fork or two.  but that's like. Yeah, different. Different conversation. Yeah. 

**Etan**
* Like Inter says that we should,  have another should bring up, bring it up one more time before they even hit five because that's the earliest one where it could go in. Right? 

**Stokes**
* Sure. Yeah. And I mean, again, like. Yeah. That sounds good. Okay, cool. Anything else there? Otherwise, we'll move to PeerDAS. 

# PeerDAS [35:00](https://youtu.be/o8p47gIt7Bs?t=2100)
**Stokes**
* Okay. Thanks.  so PeerDAS.  first, I am curious if there are any development updates. Last time we touched on this, I think people were more in sort of engineering mode and just doing some more groundwork,  for the changes PeerDAS springs generally. There was also a bit of a complication with targeting,  Deneb vs Electra and then integrating the PeerDAS's work into Electra. Given Electra is still kind of a moving target. So yeah, I expect there hasn't been too much here.  but does anyone have anything they'd like to share? 

**Manu**
* I can quickly share the updates for Prism during the last two weeks.  yeah, we implemented the metadata tree.  so basically,  if you want to know what are the columns your peer,  custody,  you need to read,  custody subnet count in, in the record. But unfortunately, it's not record is always only available for your outbound peers. And so it's an issue.
* And so Ryan did a specification change where the subnet counts is also in the metadata which is called metadata tree. And so we implemented it.. We also work about some fix on data sampling and initial things.
* And we are right now working on the blob sidecar beacon API.  yeah. Basically for blobs before us is quite simple to to to reply to this API request because you just have to to read the blob in your database in your store. But with the data columns you have to convert the columns to blobs. And you may have to also to reconstruct all the data columns if you don't,  custody them all.  and also we work on the our data verification pipeline. This is for our updates during the last two weeks on prism. 

**Stokes**
* Cool. Thanks. 

**Gajinder**
* So unless you are of,  full node clustering, everything you want anyway, be able to reply to blob sidecar requests. So I think blob sidecar request should be deprecated anyway. 

**Manu**
* Yeah. Actually,  it's not really. Because,  so of course, if you are a super nerd, you are able  to respond to this request. But if you are not a super nerd, but if you custody at least the half of the columns, so you are able to reconstruct the all the other columns from the hearth. It is a principle of reconstruction.
* And then you can transform a codons to blobs. And I don't think we should deprecate it at all because,  a lot of application and  among other layer two really needs this API endpoints for an external application is I guess it's the only way this API endpoint is the only way to retrieve the blobs actually. 

**Gajinder**
* But if,  CL doesn't has any full blobs or does not has 50% of the columns, so it can't reconstruct any,  how will it sort of respond to the request? And then there is a question of always penalizing you if you are not,  properly responding. 

**Manu**
* So,  here are I'm talking about the the beacon API. So, there is no really a question of penalizing a peer because as a peer, you expose a number of your, as a peer, you expose,  yes,  columns. You should custody. And so here's the question  is not,  here? Yes. You should always custody the columns. You you you you advertise.
* But for your question, what about if a node is not able to and is not studying enough currents?  and in this case, what happens if,  this API, this beacon API call is done just,  as far as for for Prism.  what we do you can force the node to custody all the columns by enabling the flags.
* So flag by enabling the all subnets. Flag, you have a flag,  which is called yes something like  get all the subnets and if you enable the flag so you will have all the columns and  if a user use this beacon API call and is not able to get all the columns because the node doesn't have all the columns in the error we advertise the user that he should enable this flag on a beacon node start. 

**Gajinder**
* All right. So we can still deprecate the request response and points. Right? 

**Manu**
* I don't think we should, but because if we duplicate this blob sidecar endpoint, we will break a lot of application. 

**Gajinder**
* So I think the application cannot. 

**Stokes**
* Like the gossip RPC separate from the beacon API. 

**Manu**
* Here I'm talking about the beacon API. Yes, only the beacon API. 

**Gajinder**
* Yeah. So that that is fine. And I as Alex mentioned, I was talking more about the request response and. 

**Stokes**
* Right. So yeah,  I think you're correct. Gajinder that would make sense. It sounds like this is a topic for breakout.  separately. Also echoing what's in the chat. We definitely need some way to get blobs,  if a node has them. So the beacon API should stay, I guess. There is a question then like how does a node respond if they don't have all the blob data? 

**Manu**
* So basically all the columns and as I said either you can reconstruct. So in this case you reconstruct and then you, you respond to the API to the API call. And if you cannot reconstruct because you have not enough data in your store, because basically you don't consider enough data, you just return a further offer from just return an error. And in Prism we advertise the user like that. He could get all the data if if he enables the subscribe to alternate flag on the beacon node start. 

**Stokes**
* All right. Yeah, that makes sense.  is that in the beacon APIs or is it planned to be soon? 

**Manu**
* So the advertisement is just response when we respond with an error in the error message, we just,  add a please enable the subscribe to obsolete to all subnets,  flag. That's all we do. But maybe we should add this as a requirement in the, in the beacon API as well. Yeah. 

**Stokes**
* Yeah. No, that makes sense. Okay, cool. Yeah. Casey had a suggestion to use resource Unavailable here.  yeah, that makes sense. But. so next,  we had discussed last time about dropping sampling essentially to ship paired us more quickly.  it would cut a lot of complexity. And Francesco was kind enough to make a PR that would demo this. 
* So. Yeah, like zooming out a bit with PeerDAS in general, like, no, at least be another devnet, I would assume, if not several, before we even think about merging this into Pectra. And this is definitely an option here if we think it will simplify development of these devnets in parallel. Do drop sampling have clients had a chance to think about this more?  maybe even look at the PR? And do they have any any sense of which direction we should go in? 

**Gajinder**
* Also, what we discussed and appeared as Breakout call was. Yes.  so for currently we will focus towards,  not doing sampling and the clients which are doing sampling, they can still do sampling, but they will not,  penalize the peers if the sampling fails and they will just log it. So it will be just for the information purposes.  And we will we decided that we will  think about inclusion of sampling at later devnets.
* Because the priority right now would be to get a functional devnet that has not happened till now in that sense that it has stayed up and has not fogged and,  and the new Nords could sing. So that manner we the priority is, was to get a stable devnet. 

**Stokes**
* Yeah. That makes sense.  right. And it seems like it's simple enough just to essentially ignore sampling. Like, I don't think there will be a ton of code thrash to make its decision now and then just enable it later. So that generally makes sense.  I'm not able to make the breakout calls, but,  yeah, I'm not sure if people have been talking about Devnet timing there. Does anyone know who's been able to make those calls? 

**Gajinder**
* I think yeah, Barnabas could update us. I think we want the next devnet to happen,  soon with,  without sampling and with the metadata PR changes.  but there is also another PR which sorts of separates out the custody groups then from subnets. 
* And I'm not sure whether we want to include that PR as well in the next devnet but I think we should because we should try to make sure that we do devnet as close as to the architecture that we intend to go live with. So maybe Barnabas can give us more information on this. 

**Barnabas**
* I think the general idea was to try to launch another Devnet as soon as possible with Alpha 4 spec. So whatever is going to make it into Alpha 4, that's what we were going to launch with. But I think we can discuss that in the next PeerDAS call. What exactly we want to include. 

**Stokes**
* Okay. And I think the two things were this metadata change, which I think is enough for already. The other thing would be this,  PR from Francesco. So that would probably take a little bit more time. So that sounds good.  get to either specs, release 4 or 5 with PeerDAS target, and then that will be the next subnet. And it will happen when it's ready. Okay, anything else on PeerDAS? Otherwise we will move to some more open research. Yes, Barnabus had this comment. Yeah. 

**Barnabas**
* I had one more question regarding the how can we uncouple the blob limit from here

**Stokes**
* So I had this PR to do this and yeah, I think there were some a few things that needed to be addressed which I haven't had time to do yet. Right. I mean, I think the way I kind of see this shaking up is this would come later, but was also. Yeah, I guess I'd want to see a little more progress on PeerDAS,  before feeling a lot of urgency here. I don't know if anyone else feels more strongly. 

**Barnabas**
* I feel like this would need to be included regardless whether pure does mix it in or not, because we going to need to have a way to update the number of blobs, whether we have PeerDAS or not. 

**Stokes**
* Right. And this PR, I think, just makes it simpler and easier to think about. We could still end Petra with no other changes, increase the blob count just in the way we did essentially for Deneb. So and that's kind of what I'm saying. Like this is nice to have.  but I don't feel a ton of urgency at the moment. 

**Dankrad**
* Right. But I mean, like, isn't the whole point that in case it doesn't make it later that we will be able to, like, upgrade it separately? 

**Stokes**
* Well, like ideally, but I'm just saying, like, worst case, we just have the constant set in both layers and we just update them regularly. Like this is not going that. 

**Dankrad**
* Well, in practice as well. Because like if we say, oh, this is ready two months after Pectra, it's very unlikely that there will be a whole other ultraschall at work for it. Whereas if we can do it as a CL only update here. 

**Stokes**
* Right. Okay. Well, in any case,  yeah, I will circle back to this and get it ready and. Yeah, hopefully by the next CL call,  we can be in a place to discuss in depth around inclusion. And, yeah, there's generally support in chat, so, uh. great. Anything else on PeerDAS.

# Consolidations and sync committees [50:55](https://youtu.be/o8p47gIt7Bs?t=3055)
**Stokes**
* Let's see. So next up we had a question from Ethan around the interaction between consolidations and the sync committee.  Ethan, would you like to give us an overview of the question? 

**Etan**
* Yeah.  from how I understand the consolidations, the way how it works is that it transfers the balance from one validator to another. But,  it could be that there are still like the source validator could still have open sync committee duties that last all the way into the next period, like up to two days in the worst case, like 27 hours plus one epoch less than 27 hours, I guess is the worst one.  
* I wonder if that is something that needs to be addressed. I think at the very least, it should be explicitly thought about,  whether such a consolidation should be delayed until the source validator no longer has active duties.  the duties themselves at this time are not smashable like this in committee duties. But yeah, I don't know, like, we we cannot just ignore the consolidation because it comes from the EL as well.
* So it is not like,  if it doesn't work, just retry it a day after,  because there is an EL transaction that needs to be made And when it succeeds, I guess the consolidation is expected to eventually go through. And I think exits have a similar issue, but,

**Stokes**
* Yeah, they do. 

**Etan**
* Yeah, but  for exits, at least, the balance is no longer in play. Maybe there are also, I don't know, like, oh yeah, and. 

**Stokes**
* It's still flushable. So yeah, I mean, I agree we should think about this. My gut would say just to leave it as is, like there is this similar quirk with exits where you can still be in the same committee even after you've exited. So for this, I would say to keep it the same, just because it's going to complicate things to like have like pending consolidations, like in the sense and yeah, do all the accounting.  I don't know if anyone else sees an immediate issue here with that approach.
* Like, yeah, I mean, so I guess to make it more concrete, like leave it as is and probably just have a note somewhere like, hey, by the way, this could happen just so implementors are aware. 

**Etan**
* Yeah, I think that that would make sense as well, just to have it explicit and not be an oversight because it's an interesting interaction. 

**Stokes**
* Yeah I agree. Nice find. Okay, cool. I can work on a PR just to call it out more explicitly, and that's probably a good place to continue the thread here. Let's see. So next up we had this PR to add quick to the inner. Let's see. So pop raised the point. I don't know if he's on the call. Yeah. Oh hey yes. 

**Pop**
* A quick entry into the ENR,   what I think,   I wish to, to to to to to have,  quick  as an optional transport protocol like. Yeah.  currently we,  currently  we try to use  yeah. But but if, if you support quick, I think it's better to use quick instead. Yeah. So,  this is just about adding the ENR so that the ENR empty so that you know that, okay, this node is,  this node support quick. Yeah. 

**Stokes**
* Right. So, yeah, in general, I think this is something we want eventually. I think at the moment only lighthouse supports. Quick, please correct me if I'm wrong. And Prism. for example, okay, nice.  right. So yeah, I guess this is the thing where it's optional in the sense, like you can add it if you want.  right. So then I guess Pop's point was just,  I guess merging into PR just to make it more formal.  anyone feel we should not do that? 

**Manu**
* Yeah, just just to to reply to Barnabas,  who said,  lighthouse already had quick in the owner. That's right.  but yes, it's not in the specification. And that's why I wrote the specification, just to be sure that every new clients,  which want to add this quick support, use the same,  ENR entry. Actually,  let us use this exact quick node record entry, and I just copy copied what lighthouse used to do. 

**Stokes**
* Yeah. Makes sense. And. Yeah, I mean, I think there's a question of the actual identifier. I think what we have, the ENR works. Came in as a question. Do we need a separate entry for the V4 and V6 quick ports. 

**Adrian**
* Yeah we have quicks. We have quick six. but I was just looking at the specs. Like in the specs, we only have UDP and TCP, but I think there's TCP and UDP six. So maybe there's a separate PR for IPv6 support. But lighthouse uses Quic and quick six for the fields. 

**Stokes**
* Is that in this PRD you know the quick six. 

**Adrian**
* No it's not it's not in this PR but we probably need to also add TCP and UDP six if we're going to do IPv6 support. 

**Pop**
* But there is only  there is only an IPv6 field in the ENR right. So why do we need like TCP six and six like because you just look at the IPv6 entry. 

**Adrian**
* Yeah, but if you have dual stack where you have IPv4 and IPv6, you can have different ports for different sockets. So then there's there's ambiguity there. 

**Pop**
* Got it. 

**Stokes**
* Do we feel like we want to add the V6 identifiers. 

**Pop**
* I think we should do it in a new PR. Yeah. 

**Manu**
* I can add it in in this this pull request. It's okay. Why do we need to to do it in a new pull request? 

**Stokes**
* One argument is it'd be simpler just to merge in the quick thing. I think we've been working on this for a little while, and then otherwise, yeah, it might just add latency if there's back and forth on the V6 part. Okay. I think it also works in the same PR. So yeah, I think whoever is writing this can decide. 

**Manu**
* It's okay for me to add a quick fix as well in this in this pull request. I am the author. 

# ProbeLab update [59:37](https://youtu.be/o8p47gIt7Bs?t=3577)
**Stokes**
* Thank you. And okay, last on the agenda, we had,  a request from ProbeLab update. They'd like to share some of the work they've been doing around dusk, V5 and some network analysis. Let's see, is someone. Let's see. Yep. Yeah. Hey. 

**Guillaume Michel**
* Hi. This is guy from problem. So yeah I'd like to present what we've been working on with respect to monitoring the consensus layer network.  especially the v5 DHT.  we've also done some work on the gossip part, but Mikhail will be presenting this work probably during the next call or the one after. So what we've been doing is we've been running a crawler that's basically getting a snapshot of the V5 DHT and every 30 minutes.
* So just enumerating all the peers and trying to connect to them. So try to open a TCP connection, but also sending so DC five a peer UDP request, um to learn about the full routing table of every single peers. And this way we can just enumerate the whole network, get the PNR, get all the information. We put everything in a big database and thanks to the HTTP connection, we can also get some extra information from the identify protocol such as the supported protocols and the multi addresses.
* So all the multi addresses that are supported um and so on. And from all of these data that we gather we can do some statistics. Then on cloud providers on where the nodes are located on the protocol that are supported.  and so on. So let me quickly share my screen. And also send the link here. All right. So that's the the product that we have.  in the end we build weekly report So we create one report for for every week. And um we show a lot of data. So I will not stop on every single plot there.
* But for instance we show the client diversity.  just one thing. To be clear, that's counting the number of beacon nodes and not the number of validators. 
* So you might be seeing different numbers from different sources. And we're showing the number of nodes, not the number of validators.  so we can see the distribution over time. We can also see the version distribution, um for the user agent. So can be helpful to see how your,  client is getting adopted.  and so using this plot, you can see, for instance, here, the last version of lighthouse has like an adoption rate among the lighthouse nodes of 29%. And by the end of the week, okay, didn't grow much.
* But see, if we take,  another one here for Lodestar, we can see that the latest version,  has quite some adoption during the last week.  and. Yeah, then so we have other numbers and something where. So, so we don't need to address it now, but we have some numbers that we would like to flag.
* And then,  we can take the discussion offline.  is for instance, he here we see the supported protocols for all of the nodes. We can see that, for instance, 99.9% support the mesh sub 1.1 protocol, which is kind of required.
* And then we can see the breakdown for  each of the user agent. And with all of the supported protocol. And we can see, for instance, for TCU, that TCU is only advertising these protocols at least through identify. So I'm not sure whether the other protocols are also supported but just not advertised.  or if they're missing. So yeah.  and then maybe one last plot.
* So, yeah, some things we can also do is,  checking here so we can see the in the distribution per country that here there's a small drop from the number of nodes that are hosted in the US and an increase in the nodes that are hosted elsewhere.
* And if we look so I think yeah, it was  again taking notes. So, so it means that they have been changed from a US location to elsewhere. And when looking at the cloud providers,  because we know it's taking nodes, we can see that they've been taken from a data center in the US and that they are now hosted elsewhere, not inside the data center,  outside of the US, in another country. So that's how we can use, for instance,  the stats we're doing.
* And yet the last thing that I wanted to touch upon is on the number of stale record.  the way the disk V5 DHT works is,  each node is going to keep connection to other nodes, so they're going to keep their honors. And then upon request, they're going to share it to each other. And it turns out that around a quarter of the records they hold are pointing to peers that,  aren't responsive. So to peers that may be dead or offline and that's not healthy in the network.
* So it means that we didn't do any analysis on which clients,  are,  pruning the records or if it's all of them, but it's generally not really healthy because when you use these with everyone to discover new periods, you don't want to learn about some peers that are not there anymore. And so that's a bit concerning, but it's not like a major red flag.  so yeah, if you have questions. So we'd love to have feedback. And so we plan on adding,  a plot on quick showing.
* So which clients support quick and and so on.  in the future. And if there's anything any other plot that you would want to see or if there's something useful,  you wanted to add,  feel free to reach out. 
* Yeah. Or if you think something is wrong, it's possible. So we've discovered recently that,  for instance, we weren't able to,  to actually count the number of lighthouse nodes that were at,  supporting quick.  so we retracted the plot. But so it's also possible that, for instance, for the take node, we miss something. And. Yeah. So I think that's it. I'm gonna write in the chat the email that you can reach us at. And if you have any question. 

**Potuz**
* Yeah. The question that I asked in the chat, I found it strange that lighthouse is the only one with this curves reverted where there's more data center nodes than the non data center. 

**Guillaume Michel**
* I hear you, man. 

**Potuz**
* Yeah. So why is this? I mean, is there any. It's striking. 

**Guillaume Michel**
* Yeah. So so we don't really know why. So we basically our methodology here is to gather the EIP addresses and then check whether the EIP addresses are associated with any known data center or cloud providers. And then we classify it this way, whether it's data center or not. Data center. So I guess it depends on the striking. 

**Potuz**
* I can't even think of an explanation because also this is according to your numbers. This is the client that you have most data points. 

**Guillaume Michel**
* Yeah that's right. But so it means that overall around half of the of the clients are running from a data center and half of them not from the data center. 

**Potuz**
* Yeah, I know, so this the total numbers is not something that strikes me. But it does strike me that if you look at Nimbus then essentially every node is on a non data center.  And it's a huge difference. Prism is also higher. Not that much higher but it's higher for the non data center ones. And lighthouse is the only one that has that is connected in data center.
* So that's why I'm surprised. 

**Guillaume Michel**
* Yeah. I mean, I guess the question would be to ask to the operators of the actual nodes. Or I mean, unless you know them and you're sure that most of the nodes are running from outside the data center, and then we can always double check. So the sources that we have to map IP addresses to data centers. And then I see a question some other. 

**Stokes**
* Questions in the chat. 

**Guillaume Michel**
* Yeah, I see a question from Adrian. What classifies as unreachable in the DHT?  so we consider a node as unreachable if we cannot open a P2P connection, nor,  send the UDP disk v5.  yeah. Packet connection. So in this case we consider a node as unreachable. If we cannot do either of these. 

**Adrian**
* If you can do one of them is it reachable. 

**Guillaume Michel**
* So the condition if we can reach out the node on P2P, it is reachable. And if we cannot but we get but we can reach the node on UDP and then the error that we get from the TCP connection. So there is an active error not a timeout. And the error is everything but PID mismatch. We count it as online. So yeah essentially a UDP connection is enough to be considered as online. 

**Adrian**
* Okay thanks. 

**Guillaume Michel**
* And then is this filter by main net? Yes. So it's main net for all of the plots but the stale records one. So we can see. So that's the one filter by main net. And this one is global for all of these five. And for all of the other plots it's filtered just for a minute. 

**Stokes**
* Yeah. Generally,  super nice work. The charts look really nice. I like the, the version thing because we have this question with hard forks, like we tell everyone to update, but then don't necessarily know if people have updated in time. So I could see this being useful for that. Just watching the data update, you know, week by week or maybe even day by day. 

**Guillaume Michel**
* Also concerning hard fork,  we wrote the blog post here, so showing exactly the same data where we can see so nodes leaving the. So the Capella network and then joining the NAB and some of the nodes that are still remaining in Capella after the Hardfork and so on. So yeah, if you want to have a read just check it in the chat. 

**Stokes**
* And yeah, if there's any feedback, is this email the right place?

**Guillaume Michel**
* Cool. Thanks a lot. 

**Stokes**
* Yeah, thanks. Okay. We have a few minutes remaining.  any other closing comments? Otherwise, we can wrap up a little bit early today. Are you done? 

**Etan**
* I have one more thing for the requests. Like the the validator operation request. And there is this disconnect still between the EL, which has this requests list that contains all of the deposits, withdrawals and consolidation requests. And on the CL where we have these three separate lists in the execution payload.
* So I wonder whether we should put those separate lists into a sub-container just so that we have like when we later extend it with additional request types that they still conceptually are grouped together.  I have linked it in the chat as well. 

**Stokes**
* Yeah, thanks. Yeah, I think both these came up on a past call and yeah, I'm not sure people have had time to review. 

**Etan**
* The last call was for the engine API.  this one is something similar for,  the CL data structure. 

**Potuz**
* Last call. We discussed them both. And it's important on the CL data structure itself. 

**Etan**
* Okay. 

**Stokes**
* Right. So I mean. 

**Potuz**
* My take on this last time we were we were supposed to open that issue. We opened it. And the idea was that we were going to discuss it there. My feeling about this is that,  well, Misha doesn't like this, but everyone else seems to like it.
* But there isn't enough feedback in that issue, so at least we should have at least someone from each CL client signaling something in that issue so that we can actually go ahead or not. 

**Stokes**
* Okay, so can CL all teams take a look.  I'll try to follow up independently with everyone before the next CL call, and we can make some progress then. 

**Potuz**
* So there's something to note. This change is a very simple change, perhaps in our code base, but it's pain in well, to write the spec PR I'm definitely not writing that spec PR and it's really going to be painful to write that spec PR and changing all the Python tests. So it should be done quickly if we're going to move, if we're going to move to such a thing. 

**Stokes**
* Got it. Okay, well, I'll take a look at these and I will try to follow up independently with the client teams. And yeah, let's just try to make some progress here. I don't think there's anything, anything new to add otherwise.  unless you see something else Etan or Potuz.
* Okay. Yeah. Thanks for bringing this up. Well, let's not drop the thread there. And otherwise. Yeah. Anything else?  let me double check the agenda. People like to add comments as we go.
* Okay, yeah, I think we've covered everything. And yeah, unless there's anything else. Going once, going twice. Going three times. Okay.  then I think we'll go ahead and wrap up. Thanks, everyone. See you next time. 

**Potuz**
* Bye, everyone. 

**Adrian**
* Thanks. 



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

  
### Next meeting Thursday 2024/8/22 at 14:00 UTC
