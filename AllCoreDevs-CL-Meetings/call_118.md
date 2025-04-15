# Consensus Layer Call 118

### Meeting Date/Time: Thursday 2023/9/21 at 14:00 UTC
### Meeting Duration: 1 hour
### [GitHub Agenda](https://github.com/ethereum/pm/issues/861) 
### [Audio/Video of the meeting](https://youtu.be/7ob1JFbcwZo) 
### Moderator: Danny
### Notes: Alen (Santhosh)

## Summary <!-- omit in toc -->
Summary | Description
-|-
118.1  | **Devnet-9**: Devnet-9 will be the 2nd testnet featuring the full suite of code changes going into the Cancun/Deneb (Dencun) upgrade. Prior devnets were focused on testing Ethereum Improvement Proposal (EIP) 4844. Devnet-9 will also be the first testnet to feature the activation of EIP 7514 and 7516, two new EIPs that were added to the Cancun/Deneb upgrade during last week’s ACD call. Parithosh Jayanthi, a DevOps Engineer at Ethereum Foundation, said that his team would be ready to launch Devnet-9 next Wednesday, September 27.
118.2  | **Devnet-9**: Many Execution Layer (EL) and CL clients teams on the call, including Lodestar, EthereumJS, Lighthouse, and Geth, affirmed that they would be ready for this launch. Representatives from Besu and Nethermind said that they were in the process of conducting Hive tests on their Devnet-9 releases and could give an update on their readiness for the Devnet-9 launch early next week. Jayanthi agreed to check in with client teams early next week. He also highlighted that Devnet-9 could launch without all clients being ready. “We can still start the devnet as long as we have at least a couple of clients ready and we can add the rest post [launch],” said Jayanthi on the call.
118.3  | **Devnet-9**: Ryan highlighted that a few Dencun-related tests were broken and developers have since issued a hot fix to the “consensus-spec-tests” code repository to fix these tests. He also raised a potential change to an endpoint, “blockv3”, used for block production between the validator client and the beacon node. Enrico Del Fante from the Teku client team said that there was still discussion among developers about a previous change that would override this change to the blockv3 endpoint. Later in the call, Del Fante shared instances of configuration mismatches between the validator client and the beacon node and the way Teku resolves these issues. Del Fante agreed to post a new issue on the Beacon API GitHub repo to summarize this matter.
118.4  | **Devnet-9**: On the topic of Devnet-9, developers spent time discussing the deployment strategy for EIP 4788. As background, EIP 4788 will be deployed as a regular smart contract, meaning there must be a contract address that client implementations can reference to activate the code change. Developers agreed to test out the process for contract deployment through the launch of Devnet-9 by creating the address after the genesis of the testnet and before the activation of the upgrade. Mario Vega from the Ethereum Foundation testing team said that the contract address for EIP 4788 has not yet been finalized but once it is, client teams will need to update their releases to contain the address information.
118.5  | **Cancun/Deneb Timing**: Tim Beiko, chair of the ACDE calls, raised questions about the timeline for Dencun testing after Devnet-9. “I think it’s worth it, assuming the launch of Devnet-9 goes well, to think about how we want to approach [public] testnet deployment,” said Beiko, adding that if developers do not foresee launching Dencun on a public testnet before Devconnect, that is an Ethereum-focused developer conference in November 2023, then mainnet activation of Dencun most likely would not happen this year.
118.6  | **Cancun/Deneb Timing**: On ACDE #169, Beiko had recommended launching Dencun on the following testnets in the following order: Holesky, Goerli, and then, Sepolia. Holesky is a new testnet that Ethereum developers plan on launching next Thursday, September 28. Developers initially planned the launch of Holesky for September 15, the one-year anniversary of the Merge upgrade. However, due to network misconfigurations, the testnet launch failed.

## Intro
**Danny**
* Welcome all to CL call #118. I don't think I actually had left open from last time on this computer. And I suspect that I've screwed something up because of that.  you're streaming. You're trying to stream. Yeah. 

**Tim**
* And it said the stream was interrupted when I started streaming into it, so. Oh, I think there's no sound. 

## Deneb devnet-9
**Danny**
* Okay. Sound is back. Cool. Thank you, Tim. I had something wrong in my configuration. Clearly. Just a quick recap for those that are on the on the web.  yeah, the hardest part of the job. Um. At nine. We did have a spec release for the NAB on the consensus layer. There was a couple of tests that were broken.
* Those have been released as a hotfix to the consensus spec test repo but have not changed anything in the consensus specs repo with respect to release. Hopefully people have taken a look. I will now pass it off to those coordinating dev net nine. What's our intended timeline? Guess with comments from client teams on whether they're looking ready or not. 

**Parithos**
* Yeah, I think we'd ideally like devnet-9 have that at some point next week. But two things we want to wait for are first, a signal from the client teams as to how ready they are and then where the hype desks are because we like to get hype desks in before we do the maths. 

**Mario**
* I can start with the Hype test. They are ready and running right now for Devnet nine. So, yeah, they were updated last night. 

**Danny**
* Thanks, Maria.  any client teams that would not be ready for Devnet-9. Which Perry would that mean? A devnet release tomorrow or Monday? What would what would the requisite timeline be for that? 

**Parithos**
* We can just do it mid next week. So Wednesday. 

**Danny**
* But in terms of when you need client releases. 

**Parithos**
* We normally just do forks of branches. Sorry, we just use the branches from clients so we don't need releases for devnet. 

**Danny**
* Gotcha. Very cool is any consensus layer team not ready for such a timeline? Okay. And any execution layer teams that are here is anyone opposed to that timeline? Okay. Mario says get these blobs merged. Is that something likely the next couple of days? 

**Marius**
* Mhm. Yes. So I think we can be ready by next Wednesday. 

**Danny**
* Okay, cool. Perry  y'all can circle with the rest of the teams and make sure that we're in a good spot. 

**Justin**
* Justin So for EL, I'm actually literally just running those tests right now and we've running into some issues. So it depends on what the definition of next week is. I think. So put us down as ambivalent. 

**Marius**
* It's a week after this one. 

**Danny**
* What was that, Marius? 

**Marius**
* I said the week after this one. That's the definition of next week. So we are trolling. 

**Justin**
* Right? It's a. 

**Danny**
* Yeah. Thank you. yeah. So it is that intended Wednesday, but, Perry and Colin and circle back with you all and see how things are going at the start of the week. 

**Parithos**
* Yeah. And if not, we can still start the devnet as long as we have at least a couple of plans ready and then we can add the rest post effect. 

**Enrico**
* I just want to add something from Teku. So we are still working on Blocks V3 APIs, so we are ready if we don't consider potential interop between clients using this new endpoints for block production. It's not intended. We are ready because we have the churn, the new churn PR just ready to be merged. So next week will be fine. 

## block v3 beacon-api changes -- blocksv3: add consensus value beacon-APIs#358 [12.34](https://youtu.be/7ob1JFbcwZo?t=754)
**Danny**
* Let's go ahead and touch that. Paul brought up this. This is a PR 358 and the Beacon APIs repo. Looks like there's a change to the block V3, which is used for block production between the validator client and the beacon node.  this does seem like a. Pretty transparent or the network isn't going to really be aware of this unless we try to do mix and match things.
* So I would lean in favor of what Enrico just suggested, which is to not be concerned about the granularity of whether clients made this change or not. But I'm open to alternative opinions. Okay. Does anybody see this change as a blocker for moving forward on Devnet? Nine. 

**Enrico**
* Yeah, but to be clear, we are still working on the previous PR, which is not the consensus value but block V3. This has been already merged. So it's not talking about this additional change, but the V3 End point completely, right? 

**Danny**
* But we're good to move forward. Okay. I see some thumbs up. 

**Danny**
* Anything else on Devnet-9?

**Parithos**
* I had one tiny request to the beacon API stuff. We this got merged adding blob sidecar event. Sam and Andrew are looking to add like check that event in SA 2 and it would be nice if clients have support for this sooner rather than later so that we can also start testing tooling such that by the time we do the first testnet, we're not testing something that's alpha. 

**Danny**
* Got any comments regarding the readiness of this? Okay. Anything else on Devnet-9?

**Tim**
* Yeah. Do we want to? I guess there's a question in the chat. Do we want to do the contract deployment the same way we do on mainnet? Even if it's not with the perfect address, I think we have mined one suboptimal one and we're trying to look for a nicer one. 

**Danny**
* I would prefer to see that. Yes, Lightclient. Are we ready to do that deployment method? We are. Okay, who's going to be in charge of that deployment method? And it also implies that we need enough lead time between Genisus and the fork to be able to fund the account, run the script. I mean, obviously that can happen extremely quickly, but we just need to be on it. 

**Parithos**
* Yeah, we can definitely add some lead time, like 20 epochs or something. So roughly two hours. If someone shows me what the deployment method is, we're happy to do it. But otherwise we're also happy to just pass on the Eth and someone else does it. Whatever works best. 

**Danny**
* Yeah. I mean, I think it'd be great if, Lightclint, Martin could work with the dev ops team to show them how to do it so that we can get it scripted and kind of integrated into the processes. Okay. And then there's a conversation going on in the chat around,  the updated KGZ values. Carl says, looking like we're aiming for Tuesday on those updated values.
* Is that something that we're attempting to get into this devnet or will we push it to a side test for now? Subsequent devnet or side test. 

**Parithos**
* Yes. 

**Carlbeek**
* As mentioned, I'm hoping to have that done by Tuesday, but no guarantees. The issue here being that after that, it needs to be compiled into the libraries. So that makes timing very tight for a Wednesday devnet. 

**Parithos**
* We've been putting out the alert that clients should allow it to specify as a runtime flag on almost every single devnet spec release. I think all the clients do have such a flag though. We've even been using it. Or is the worry that the flag is not respected, in which case we can just get rid of it? 

**Danny**
* I think the worry is that there's some final work to do, and it's unclear if that would happen before Wednesday with respect to getting this into the cryptographic libraries. Or are you saying, Perry, that the cryptographic libraries have flags? 

**Parithos**
* And I'm talking about the final client releases. Yeah. Cool. Then if it's ready in time, then we'll use it. But otherwise, I guess we stick to the old trusted setup for now. 

**Danny**
* The untrusted setup. Mario. 

**Mario**
* Yeah. So one small consideration that might be taking into account is that, we do need to update the tests for that. So if you guys want to use  the trusted setup for devnet-9, I think that would be fine. We just not need to consider that the hype tests and the actual devnet-9 trusted setup might differ. So yeah, there's going to be a difference but I don't think it's it should be impactful. 

**Martin**
* Hi. Sorry, I missed a little bit of the context of what we talked about previously, but we're talking about the 4788. 

**Danny**
* You sound very muffled. Martin Is there maybe an angle? 

**Martin**
* Is it possibly better now? 

**Danny**
* Yes. Thank you. 

**Martin**
* Okay. So I missed a bit of the context to the deployment of 4788, devnet-9, but the one thing that is important,  mean exactly what code gets deployed by DevOps in the genesis is doesn't really matter. They can decide what they want to deploy and all the clients will just use it. What is important is where they deploy it and all the clients needs to agree on what the address they're going to use for this system contract. 

**Danny**
* There was an intention to not deploy at Genesis and to instead deploy between the interim between Genesis and the Cancun Fork. 

**Martin**
* So sorry. I'm missing a bit, but we're talking about the testnet. Or I'm talking about a mainnet fork. 

**Danny**
* We're talking about the Testnet. I think there's just a at least I have the desire to see just us run through that manual process and kind of get scripts and things together rather than just shoving it into the Genesis State unless you believe otherwise. 

**Martin**
* No, that's fine. But. But the big problem then is not. And making the transaction and putting funds there and deploying it. That's not the big one. The big one is that we need to make sure that all the clients have the correct address anyway, regardless of how we put it there, because it takes it takes longer for everyone to make put the right address and make a release. So. Matt. 

**Danny**
* Yeah, agreed. 

**Martin**
* If you have figured out the the address, then put it somewhere publicly so all the client devs can just merge it. The correct address. 

**Lightclient**
* I'll do. 

**Andrew**
* I think it's in the the right address is in the exec spec tests version for like there was a release of that test suite recently with an updated address. 

**Martin**
* Very good. Then all the client devs should now know that they need to update this as soon as possible. 

**Danny**
* Cool. Should be good to go. Mario. 

**Mario**
* So the the. 

**Danny**
* I believe you cut out Mario. Yeah. Okay. You're back. Can you start over? 

**Mario**
* Yeah, of course. So the. The address in the latest release of the exe specs test is the the one that is on the latest commit in the EIP., but it's not the one that is being mined right now, so there might be a change. Got it. 

**Danny**
* All right. I think we're on the same page on this. Any other devnet-9 related items. Okay. Any other Deneb or Cancun related items? 

**Tim**
* Okay. Not that we need to make a decision about this now, but think, It's worth it. Assuming that Devnet-9 goes well to think about how we want to approach testnet deployment.  and I guess there's a few considerations there. The first is obviously a holesky. The launch didn't go quite smoothly, so we probably don't want to use that as a first testnet. And then second, whether we want to,  whether we want to have a first test net before dev connect or not.
* Because given dev connect is in, you know, mid-November, this means that we probably want to have that testnet early November at the latest. And if we want to have the releases out, that's around like mid October or maybe late October,  which is, you know, probably a month or less from now.  so yeah, I'm curious if anyone has thoughts about that, like how realistic that is. And, and I guess also it's worth noting, I think the implication if we don't do a testnet before dev connect.
* It's probably unlikely we can do mainnet before the like Christmas holidays.  because after Dev connect there's us Thanksgiving and then there's basically three, maybe four weeks before like, Christmas holidays and people being gone. So that's probably not the best time to fork mainnet.  Yeah. So just wanted to put that out there. 

**Danny**
* Curious on your first point in relation to Holskey.  is it, is it unlikely that we would be able to use Holskey in a few weeks? 

**Tim**
* I'm not sure. Maybe someone from who's more involved there? Yeah. 

**Parithos**
* I think it. So the whole Gensis is scheduled now for next week, so the 28th. So it will be usable in times for dev in time for dev connect, but it still make the case for Holskey not being the first fork, but rather potentially the second or third, mainly because we have Gorley as a perfectly functioning test net that is deprecated, which means we can try out the three six blob option on Gorley and if it goes badly, it's a deprecated test net anyway. If it goes badly on Holskey, then we have to figure out how to save it. 

**Tim**
* Yeah, I would also and also like if there's something that goes wrong with the whole deployment the second time, I think it's good to have like a bit of buffer where we can. You know, if we go for Gorley, we don't have any other variable to control. We could also choose to do Sepolia first.
* Sepolia has a smaller validator set, so it might be a bit more easy to coordinate the upgrade. But yeah, either Sepolia or Gorley at least are stable and we can just think about deploying the fork rather than the stability of the network. 

**Danny**
* Yeah, the Gorley first argument, given the deprecation, it seems like a sound argument to me. 

**Enrico**
* Yeah. Think we can get more insight from 363 six blobs if we do that one first. Otherwise so small that you might not get enough information. 

**Tim**
* Yeah. And we agreed as well. A couple calls ago to not like, if 36 is bad just leave it as is on one test net and you know, shift the value for other testnets. And so in that case, yeah, I'd also lean towards Gorley being the one that's like not up to mainnet spec if there's a change to be made. Yeah. Yep. 

**Enrico**
* Yeah, considering that is. Doomed to be deprecated. We'll go away with 36.

**Danny**
* Yeah. So Tim's second point was with respect to timelines and whether a first testnet is in the cards to be forked prior to Dev Connect, call it, you know, first week of November or so.  is there a reaction to that type of timeline intended one way. Or the other? 

**Sean**
* On the lighthouse side. I think we can make that timeline.  I'm keen to start testing on, like, bigger test nets because it is like the, networking component would be like, the most, like at this point, an unknown that could require more work. So I think it'd be good to get more information about that more quickly.
* And then just on our development side, we're in the process of getting the network merged into our, unstable branch, and I think that's probably the blocker for us in terms of getting it into one of the bigger devnets. But we should definitely have it in by by dev connect so. 

**Danny**
* Marius says. Any other reactions to the timeline? 

**MArek**
* I think Nethermind might is okay with this timeline. 

**Danny**
* Perry, Are we intending to do some main shadow forks as we move into the testnet progression? Because that also, depending on how many how we scale up nodes and stuff could give us some interesting data. 

**Parithos**
* Yeah, we can plan for that. I think the main issue is that our the nodes we rent for mainnet Shadow fox tend to be quite well provisioned, which means like the blobs won't really stress them. I'm loosely in favour of having smaller nodes, but a larger network like more physical nodes in the network.
* So that we can test more peer to peer related timing issues etc, that might teach us more. But if there's more appetite for mainnet Shadow fork can do that first, whichever is preferred. 

**Danny**
* Yeah mean mainnet shadow forks but in the direction of slightly lower resource and more nodes or other types of tests that are have more nodes I think is going to push us in the direction. That's interesting. 

**Parithos**
* Yep. Once we have net nine up and running, we can look to start doing that kind of tests. I would guess that's what we would spend most of October on. 

**Danny**
* Any other comments or reactions to timelines or anything Tim brought up? 

## Research, spec, etc coordination on new params -- Replace INTERVALS_PER_SLOT time setting with ATTESTATION_DUE_MS style presets consensus-specs#3510 [32.04](https://youtu.be/7ob1JFbcwZo?t=1924)

**Danny**
* Dencun Related items. Okay.  let's see. Enrico put up a link to a issue or PR about some discussion in relation to adjusting the attestation timing window. Enrico, can you give us some context here? 

**Enrico**
* Yeah, it was more focused on not this specific new attributes that he's been discussing. Actively discussing the PR is more on the configuration changes that we recently had. let's say starting from the networking configuration that at some point they become configuration. This triggers some interoperability issues, especially sometimes with Lighthouse,  with Lighthouse, sorry.
* And this was because at some point the validator client that used beacon node so remote validator clients lost the configuration from the beacon node. And if you don't have upgraded your beacon node with the new value, that will not start because the new version expect this attribute these parameters to be there and.
* So what we did recently, very recently, at least on the teku side, on the side, we  try to start from a known configuration and known preset and then apply the attributes, the parameters coming from the beacon node, end point.
* Which means that if the beacon node is still on old configuration, the VC side still get all the parameters that expect. So it should fix everything that happened in the past. But no, if other clients, what are the logic on the other clients when they start getting configuration from the beacon node? So think on the Teku side, we should in a better position to try to avoid those configuration changes and breaking changes. 

**Danny**
* Okay, so we're saying if the VC is out of sync with configuration changes the beacon node, we can sometimes have failures. 

**Marius**
* Yeah. 

**Danny**
* So there might be a better practice to pull down configuration values from the beacon node instead of strictly only respecting what's local to the VC? Or am I missing something? 

**Enrico**
* Yeah. So previously we were applying only the preset and then all the configuration from the beacon node. So this opens the door of having a beacon node, not providing everything that you expect and force the operator to have to upgrade the beacon node first and then the validator client first after.
* And then if you are also have a mix of VC from one client and from another client, you have to make sure that the other client has updated the configuration first.
* It's so it happened recently. So teko who now applies also the configuration from the VC perspective so ignoring well yeah getting getting the the updated information that validator client has locally so even if the beacon node is slightly older it can still get all the configuration. 

**Danny**
* I see.  do. Clients have reactions to this strategy that teko using? 

**Sean**
* I'd have to look into what Lighthouse does in this scenario, but I thought we just like loaded configuration and both the validator and the beacon and we would just log if they don't match in the the like based on the request.  but I don't remember what we do if there's a mismatch. 

**Enrico**
* Yeah. No, we weren't, were we? Do some warning when we can ignore something that is not mandatory. But now we actually default to. To unknown value and then override if Beacon provides the information. Seems like a nice strategy. So it could if all the clients applies this and there is no drawbacks. It could be reduced the interoperability issues when new config arrives. 

**Danny**
* Right.  So you're taking the strategy of beacon node config trumps the config in the event that that doesn't break anything. 
* Enrico is there. Maybe we should elevate this to a maybe an issue in the Beacon API's for further discussion rather than embedded in this specs issue. 

**Enrico**
* Yeah, could be. Could be a nice. Place where we could start discussion there. Yeah. Yeah. 

**Danny**
* Would you mind quick? Just writing up a quick version of this there. 

**Enrico**
* Okay. 

**Danny**
* Any other perspective or comments on this? Otherwise, we're going to take it into the Beacon API's repo. 
* Are there any other items that weren't on the agenda that people like to discuss today? 
* Quick and easy. That usually means that the hard work is not on the call. It's happening in the plants. Cool. So let's keep things moving forward for Devnet-9 next week and otherwise talk to you all soon. Take care, everyone. Thank you!


____

### Attendees
* Danny
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

____

### Next meeting on Thursday 2023/10/5 at 14:00 UTC

