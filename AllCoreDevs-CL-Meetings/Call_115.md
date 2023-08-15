# Consensus Layer Call 115

### Meeting Date/Time: Thursday 2023/8/10 at 14:00 UTC
### Meeting Duration: 30 minutes
### [GitHub Agenda](https://github.com/ethereum/pm/issues/844) 
### [Audio/Video of the meeting](https://youtu.be/LJt4cu3eG2g) 
### Moderator: Terence
### Notes: Alen (Santhosh)

## Summary <!-- omit in toc -->
Summary | Description
-|-
115.1  | **Devnet 8:** Developers agreed to launch the next official test network for the Deneb/Cancun (Dencun) upgrade, Devnet 8, early next week. Parithosh Jayanthi, a DevOps Engineer at the Ethereum Foundation, mentioned that his team is working on updating local testing tools for client teams based on the issues discovered in client configurations on Devnet 7. Jayanthi encouraged client teams to review their configurations to ensure there are no inconsistencies for the launch of Devnet 8, the first dedicated test network that will feature the activation of all relevant Ethereum Improvement Proposals (EIPs) finalized for the Dencun upgrade. Representatives from Prysm (CL), Lighthouse (CL), and Nethermind (EL) said they were ready for the launch of Devnet 8. Andrew Ashikhmin representing the Erigon (EL) client team said that they were working on fixing certain Hive tests and was not certain they would be ready for Devnet 8.
115.2  | **EIP 4788:** On ACDE call #167, developers agreed to update EIP 4788 from a stateful precompile to a regular smart contract. As background, EIP 4788 exposes the roots of Beacon Chain blocks inside the Ethereum Virtual Machine (EVM) on the EL so that decentralized applications (dapps) can easily access this data without having to trust an oracle or off-chain data provider. Last week, Martin Holst Swende, lead security engineer and Geth (EL) developer at the Ethereum Foundation, pointed out that converting EIP 4788 into a regular contract coded in Solidity and priced natively through the EVM would decrease the complexity of the EIP and reduce the risk of it causing a chain split
115.3  | **EIP 4788:**  On ACDC #115, developers reaffirmed the decision to rewrite EIP 4788 as a regular contract. Chair of the ACDE calls Tim Beiko said that a new pull request (PR) has been created for the EIP on GitHub by “lightclient,” a pseudonymous Geth (EL) developer, that contains the necessary changes. Beiko also highlighted that there is still uncertainty around how to best deploy the contract. “[The question is] whether we just deploy it like a regular transaction for the fork or if we couple it with the fork so that during the fork activation, we also do a contract deployment,” said Beiko. Furthermore, Beiko said the Ethereum Foundation is starting to reach out to third-party auditing services to formally review lightclient’s PR and recommended that client teams also look at the proposed code. Tsao affirmed that changes to EIP 4788 and its deployment strategy will be revisited as a topic for discussion on next week’s ACDE call.
115.4  | **Fork Choice Filtering:** As discussed on ACDC #114, a few changes to the CL fork choice specification are required to implement the confirmation rule. The confirmation rule is a new algorithm that Ethereum CL teams have been working on for the past several months that would be used by node operators to easily and quickly determine whether a block is guaranteed not to be reorged, that is removed from the canonical chain. Rather than requiring all client teams to implement the fork choice filtering logic for the confirmation rule at a strict epoch boundary, such as the activation of the Dencun hard fork, developers expressed a preference to implement the changes through a soft fork a few weeks prior to Dencun. Ben Edington representing the Teku (CL) client team was in favor of this strategy to reduce implementation complexity. Developers agreed to move forward with merging the PR for implementing changes to the fork choice filtering logic through a soft fork before Dencun once the epoch number for Dencun activation is confirmed.
115.5  | **Client Behavior Standardization:** Developers also discussed a PR to merge new clarifications to CL client behavior when aggregating validator attestations. Validator attestations are votes on the canonical head of the blockchain that the Ethereum network aggregates and uses to finalize new blocks. A developer named Pop Chunhapanya pointed out that certain clients such as Prysm only aggregates validator attestations in the first 6.5 seconds of a slot, rather than the full 8 seconds, while other clients such as Lighthouse aggregate attestations on a rolling basis for the entire duration of the slot. Chunhapanya’s PR recommends updating CL client specifications to specify that all Ethereum CL clients should include live attestations for the full slot duration. Tsao was in favor of this PR but recommended that the keyword for this change should not be “must” but rather “should,” as CL clients face inevitable delays in sending attestations that may force them to miss certain attestations sent in the duration of a slot.
115.6  | **Holesky Testnet:** Jayanthi gave an update on big test network experiments for the launch of the Holesky testnet. As background, Holesky is a new public testnet that Ethereum developers and client teams plan on launching in September to replace the Goerli testnet. Holesky is envisioned to be Ethereum’s largest public testnet, hosting more active validators than Ethereum mainnet. For the past few weeks, developers have been experimenting with the validator set size. At 2.1mn active validators, Jayanthi said that the testnet was not able to finalize. “There were too many validator duties [and] some blocks coming in late leading to not enough attestations being propagated throughout the network. So even though you were seeing something like 80% [block] proposals, we were only seeing between 40% to 45% of attestations on the network,” said Jayanthi.

# Intro
**Terence**
* All right. Hey guys. yeah. So today I will be covering Consensus Layer Meeting meeting 115, copy and pasting the agenda here. 

# Deneb -- devnet-8 and testing updates [0.42](https://youtu.be/LJt4cu3eG2g?t=42)
**Terence**
* Let's see. Okay, so first on the list is, devnet-8, status. So as far as we know, devnet-7 seven is, has been tore up, so devnet-8 is the next one. So, from the last meeting, even on Mondays, the devnet testing code, it sounds like it was blocked by 4788, but, but then we made the decision to not fully be blocked by 4788.
* So I guess in terms of like client status, like, when are we comfortable with, with devnet-8, start date? yeah, does anyone wanna take an update here? 

**Parithosh**
* So maybe we can just start from, testing perspective. yeah, so I've posted a link for Hive. I think most of the, can we mute Matt somehow? Yeah. so from, from the Hive perspective, I dunno if Mario's here, he isn't. So, okay, I can just cover it for now. There were a couple of config issues. Those have all been fixed now, and you can see that most of the tests are indeed passing.
* So Barnabas and I are now just working on getting, on updating our local testing tools and we will just post a link on how different client teams can just make sure that there's no, inconsistencies. And in the meantime, if the client teams themselves are feeling confident, then we're happy to start planning it and launch it early next week. 

**Terence**
* Sounds good. does any client team, have an objection with the timeline? So that is early next week. Alright, sounds good. Sounds like that's easy. we'll do devnet-8 early next week. And, burnout base, just ask our client somewhat ready. I guess I can speak from Prism. Yep, we are ready. But yeah, I guess the question is, is any client that's not ready for early next week, 

**Andrew Ashikhmin**
* With there Argon, we're still, working on, fixing the Hive test, so we might be ready, but it's still, it's not certain. 

**Terence**
* Okay. Thanks for the update. 

**Barnabas Busa**
* Do we have an image that we could use already for Ergon? 

**Andrew Ashikhmin**
* No, not yet. We, but it, it'll be our, in our dev in our default branch. but it's like, no, it's still, it's not working yet, but next week it might be. But yeah, just I don't know for sure. We we'll make, we'll make an effort, certainly. 

**Terence**
* Okay, sounds good. are there anything else we wanna cover for devnet-8 a before we move on? Okay, I got a thumbs up. 

# 4788 code deploy method synthetic-tx vs fork placing the code. not a devnet blocker, but reaching further consensus would be valuable on the CL call. Attempting a harder deadline by ACDE on following week [4.07](https://youtu.be/LJt4cu3eG2g?t=247)
**Terence**
* Okay, so the next topic is four seven aa. So from my understanding, this is, there's a debate going on between regular contract versus system contract, and the discussion is mostly on the EL side. So the CL side is fairly simple and easy to reason. So, I guess, the decision by which way to go will be made in the next ACDE call. So it doesn't make sense to make the decision here. but is there anything that people want to say to push towards further consensus?
* Okay. Tim say that already decided for the smart contract? Yeah,  I guess, I'm just scrolling through the agenda that like, sounds like we don't want to make a decision here because most of the EL are not, I guess some of the ER are not here, so it, it seems like it's better to make a decision in the next ACDE call.

**Tim**
* Yeah. Can you hear me? 

**Terence**
* Yeah. 

**Tim**
* Okay. Yeah. So we did decide to use a smart contract rather than recompile. and Lifeline has a PR for that. The thing we still need input from the EL team for, and that it would be good to decide by the next ACDE is how we deploy that contract. whether we just deploy it with like a regular transaction before the fork, or if we couple it with the fork so that during the fork activation we also do a contract deployment. that seems to be the biggest question.
* And then as for the actual contract code, lightclient, PR has, has a first pass at it, if people wanna review that, and, you know, potentially suggest improvements  or optimizations, we're also starting to reach out the auditors to formally review the pipe code, to make sure that it's, yeah, it's, it's, Sounds good. 

**Terence**
* Thanks for the update Tim. And Matt, anything else you just wanna cover here or from anyone else? Awesome. It looks like the hype change already as well. There is a hive issue. 818 Thank you Mario. 

# Research, spec, etc when/how to release fork-choice filtering change Include FC filtering change #3431 into Deneb consensus-specs#3466 [6.39](https://youtu.be/LJt4cu3eG2g?t=399) 
**Terence**
* Okay, so next on the topic is the, for choice filter change for confirmation rule that is, PR or issue 3431. So the T L D R is that there is a new four choice filtering change is two, it's a simple two liner. It's a refactor, it has new tests. So there is some debate on whether, to support changing fork choice object at, at the specific boundary as a part of their devnet release.
* So we can group them as close as possible versus do not enforce that.
* So may help or anyone have any input on for this PR or issue. 

**Mihkail Kalinin**
* From the comments that are in this issue, I can, there is a slight preference and not to implement, the strict, forking logic here and just make it, make this change into the devnet release of the clients. 

**Terence**
* Right, and even with the release, we can assume most clients release will be grouped together within like two to three weeks each, so Yeah. 

**Mihkail Kalinin**
* And the question is there any concerns with this way of making this change? 

**Terence**
* I was talking to  and seems like Prism may have this change implemented already, so there's something to double check within Prism. But yeah, any other CL team have any concerns or input? 

**Sean**
* I'll just say from Lighthouse, supporting the change at the EPOCH boundary is something  we would be able to do. if people do have preference for that as far as whether we should, I personally would have to dig into the, like, change itself more to understand if there's any risk in not doing it at an epoch 

**Ben Edgington**
* For, Teku, I think I already shared that we would, have a slight preference for not forking out a specific epoch, but releasing a version, prior to the, Deneb upgrade that supports  the new fork choice. just because it, it's a tiny reduction in complexity to do so. and just makes testing and all of that,  more straightforward, having a sense for the risks that that would open up.
* There would be a very short window of time where potentially clients have  there are multiple versions of the fork choice out there. the circumstances in which that could cause trouble seem to me very remote, but I dunno if anyone has a better sense for that, than, than I do. 

**Mihkail Kalinin**
* Yeah, I think that the probability that something happens on the mainnet that will, cause a split, between the clients that have this upgrade and between those that don't have this upgrade, it's really low. so it's more in edge case, very much even more edgy, on the mainnet. so, yeah, if there is the, preference of the client teams, so not to activate this on epoch boundary, then this is probably the way to go. 

**Terence**
* So sounds like, there's no strong objection that we can move forward. And is there like a PR that to merge based on this? Is that 3431 and there's also test that go with it? So would you say the next setup plan is essentially to approve and, merge, this PR 3431? 

**Mihkail Kalinin**
* There is the comment from Loin, which is, sounds reasonable to me that we should merge this. yeah, when the mainnet network EPOCH for is that we like merge this PR and and create the structures for it. 

**Terence**
* Okay. So sometimes we are blocked by the Devnet hard fork epoch and anyway, but we do have rough consensus here that the, this is what we prefer. Okay. Sounds good.

# clarifying aggregation behaviour Include timely attestations and aggregates consensus-specs#3472 [12.01](https://youtu.be/LJt4cu3eG2g?t=721)
* And next topic is, 3472, We want to clarify aggregation behavior. It looks like currently clients do things slightly different, like for example, Load star aggregate attestation as attestation comes versus Prism, it aggregates at 6.5 seconds. So, the motivation of this issue and the spec is so that client could be more consistent. is pop here, do you wanna give like a high level intro for the PR? 

**Pop**
* Yes. the motivation is that I noticed that, the esthetic session that arrive only before 6.5 seconds, so, for the session that arrive between 6.5 and 8 second, you'll be not included  in the prism So, and, and, and that is why we are, and, and this PR is, is to,  specifically that the high-end should include all the sation that are like before eight second and yeah, but in my opinion, the high end should not like change, like the high end should not work too much on implementation to be consistent because like I don't think it's worth, spending time,  but I think it's at least, a good idea to to be specific in in the specification. Yeah. 

**Terence**
* Yeah, I tend to agree and I read through the issue, it sounds to me there is just, couple points on like what language should you should use, just like 20 validated spec doesn't really use like must and should, right? And it sounds like it will be nice to start using those keywords more often. And then at the end it sounds like we're agreeing that like must and must meaning that you must aggregate at a second and then you must send, it's kind of impossible because there's always delay. So sometimes it's between like shoot versus shoot versus something like that. 

**Pop**
* Yeah, that that makes sense. 

**Terence** 
* Does any client teams have any inputs for this PR? Yeah, If there's no input, I think we can, it sounds to me, yeah, there is some sort of agreement here, so we can just take you to the PR and I don't think Potus is here. POTUS is the one that's being, voicing. But yeah, it sounds to me if today we can use the shoot keyword, not the must keyword, we should be able to merge this PR, but yeah, thank you pop for opening the PR. This is great. 


# FC proposer boost equivocation fix to "last call" Apply proposer boost to first block in case of equivocation consensus-specs#3352 [15.20](https://youtu.be/LJt4cu3eG2g?t=920)
**Terence** 
* Cool. So the next one is, four choice proposal boosts in incorporation. So this one modified the on unblock, so it, so it awards the proposal boost to the first block rather than the last block. So this was one part of the postmortem for the RPC unbundling attack that was described in Michael's post. And then such that proposal boost is only set once per slot and then from the PR it seems like this is safe to draw gradually. So that's nice. And yeah, does any client team have any input on this? 3352 and I believe I've seen a few approval already, so seems like there's no strong disagreement there, but yeah. Does anyone have any voice or input on this one?
* Yeah, if there's no input, I think, we can merge this by end of this week, shall we? I think, yeah, I think that's what we're looking for. Yep. 

**Terence**
Alright. going through the agenda again. Looks like we covered everything. Yeah. Oh, Perry wants to talk about, 2 million elevator tests. Yeah. Perry, go for it. 

# >2M validator tests and the plan forward for Holesky [16.31](https://youtu.be/LJt4cu3eG2g?t=991)
**Parithosh**
* Yeah. Hey, so the last weeks, last week, week and a half, we've been running these, big validator testnet. we've had I think three big, three relatively, yeah, relatively big attempts. The first two, one that's successful, beacon Chain test two was the one we had last week. there's, there's a detailed analysis posted over here, the, I can send you guys a link to the logs as well as some profiles that we've taken from last week as well.
* But essentially at the 2.1 million mark we weren't able to finalize. the theory at the moment is that, there were too many validated duties slash some blocks coming in late leading to, not enough attestations being propagated throughout the network. So even though we were seeing something like 80% proposals, we were only seeing between 40 and 45% of attestations on the network. So we dropped down the, overall validator set size to 1.4 million now, and we also dropped the number of keys per node to 3,300. And we had the test, the test and genesis earlier today.
* And this testnet Genesis looks successful. We're seeing relatively healthy  rates of participation, so hovering around the range of, 80 to 90%, proposals and similarly 80 to 83, 84% attestations. So hopefully this testnet is a bit more useful for client teams in order to run profiles on. we leave it up until tomorrow morning, so it would be great if, if you guys can have a look, if you can collect whatever profiles you need to and so on. And we officially be making the proposal to have a 1.4 million validator set, public testnet for ky and if there's any reason we shouldn't be doing that and we shouldn't be creating the Jan estate with that size, then we'd love to hear about it now or over the next week of course. 

**Terence**
* Great, thanks Perry. anyone have any, updates or, feedback questions for Perry? I guess I have a question whether like, is 2 million still the goal that we're working in the background or are we like satisfied with 1.4 million right now? 

**Parithosh**
* At the moment I think I would just go with 1.4 million. I think 2 million would recover, would require a decent bit of work from a lot of clients. And we're not necessarily sure if you wanna have that in a public test network coordinating, it'll be a lot harder. 

**Terence**
* Got it. Makes sense. 

**Parithosh**
* Also, we'll have enough ether in the 1.4 million, Genesis states to grow it to 2 million eventually. So we just buy more time into it eventually if we need to. 

**Terence**
* Yep, that makes sense. And then you would mentioned that the, so the, so the proposal is about 90% rate at attest station's, about 80 to 83%. so the clients that's missing the dissertations, do they also know that? 

**Parithosh**
* Yeah, I don't think anyone's any single client is missing all the attestations. I think it's more of, every client isn't able to do a hundred percent of the attestation station. 

**Terence**
* I see. Cool. That's great. Yeah, I would encourage people to take a look. And this is happening on the Discord interrupt channel, right? 

**Parithosh**
* Yeah, that's right. And everyone who's used to it has access. The IP addresses are in the same places as you always find them. 

**Terence**
* Great. Yeah. Thank you Perry for the update. Very useful. And thank you partner Barna B just posted the, Graf as well. That's also very useful. Thank you guys. anyone have any, inputs for the Testnet or the testing status? Cool. So that is it from the agendas perspective. Does anyone have like, any open discussion, closing remarks? Great. This may be the shortest Thank you for making my job very easy. Yeah, we'll talk in two weeks. Bye. Thanks nce. Thank you guys. Bye. Bye. 

____

### Attendees
* Terence
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

### Next meeting
Thursday 2023/8/24 at 14:00 UTC
