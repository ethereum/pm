# Ethereum Core Devs Meeting 37 Notes
### Meeting Date/Time: Fri, April 20, 2018 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/37)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=vKumx5CIA-k)

# Agenda

1. Testing
    * string test_addTransaction(string _jsonTransaction) (continuing conversation from last call)
3. EIP 908: Reward for clients and full nodes validating transactions + @MicahZoltu proposal (time did not permit on last call)
Ben Edgington's proposal that all EIPs ought to contain a PR against the yellow paper before being merged or accepted (continuing conversation from last call)
1. EIP 960: Cap total ether supply at ~120 million (continuing conversation from last call)
1. EIP 969: Modifications to ethash to invalidate existing dedicated hardware implementations (continuing conversation from last call)
1. EIP 999: Restore Contract Code at 0x863DF6BFa4469f3ead0bE8f9F2AAE51c91A907b4
1. Research Updates
1. Constantinople hard fork timing and what to include (continuing conversation from last call) - Afri: meta-EIP for Constantinople? Hivetests already has tests enabled, Parity failing, cf. paritytech/parity#8427.
1. Client updates
1. Timing of next call (EdCon)

# Notes

Video starts at [[6:11](https://youtu.be/vKumx5CIA-k?t=6m11s)].

## Testing update from Dimitry [[7:07](https://youtu.be/vKumx5CIA-k?t=7m7s)]
* _(Audio issue here, notes will be filled in when backup recording becomes available)_
* RPC methods for state test are almost complete and implemented in cpp-ethereum
* Posted link in chat, follow GH issue and see discussions
    * https://github.com/ethereum/retesteth
    * https://github.com/ethereum/retesteth/issues/5
* New RPC method for transaction, I removed the method from the protocol, implemented tx signing on client side, so no need to implement new methods (`test_addTransaction`)
* Client required to have sign raw tx method but every client already has this
* Using send raw tx instead

## EIP 908: Reward for clients and full nodes validating transactions [[13:39](https://youtu.be/vKumx5CIA-k?t=13m39s)]
* https://github.com/ethereum/EIPs/pull/908
* https://ethresear.ch/t/incentivizing-full-state-nodes/1640
* Nick Johnson: unwarranted complication to the protocol
* Vitalik: should be done at second layer
    * Summary: When a client signs a tx it attaches a user agent to a signature which can then be used to some amount of ETH to the author of that client, would be sent to that author (EF, Parity, Etc.) when 
* Vlad: could be done with a forwarding contract
* Nick: or with tx signature improvements
* Alex: Many proposals try to make clients usage message signing in attempts to transfer tokens, wallet contract could do this and get tokens in return, I agree it's more a second layer thing
* But let's wait for one of the proposers to defend the idea

## Ben Edgington's proposal that all EIPs ought to contain a PR against the yellow paper before being merged or accepted [[17:04](https://youtu.be/vKumx5CIA-k?t=17m4s)]
* No formal EIP for this yet, nothing written yet, just wanted to test the water
* If people are interested I'll write it as a PR to EIP-1
* Few months ago I raised questions about maintenance of yellow paper, Gavin relicensed yellow paper, Yoichi maintaining it
* Discussed different formats for Ethereum spec, K-EVM vs. yellow paper
* Whatever format we agree for formal spec must be maintained
* I suggest that maintenance should be done as part of EIP process
* Where relevant a core EIP before accepted should contain a PR or diff against the spec, diff subject to peer review process same as EIP text
* Link to PR could form part of header/preamble of EIP
* This would make it easier to maintain the spec (yello paper)
* But would also bring rigor to the EIP process, help identify edge cases and ambiguities
* Vlad: only for changes that affect the protocol right?
* Ben: yes, EIP's defined as "core" would fall under this scope
* Proposed as requirement for acceptance not for merging the draft - not everyone capable or interested in writing a yellow paper PR
* So an EIP may be merged as draft then someone can work with author to write up in right format for yellow paper
* Changes to yellow paper included as a PR within the EIP
* Vlad: this would slow down dev process for any core change if we have to do the spec first
* Danny: not if it's part of full acceptance or final state, vs. getting merged as drafts
* Piper: account abstraction EIP, only exposed complexity at implementation time - if someone would have done this at spec time - could be an argument for or against this
* Nick: would be good to detect these issues before people begin implementing things
* Peter: this would be nice but how many people here can actually open a PR against the yellow paper? We don't want the quality of the yellow paper to suffer
    * Yellow paper has a certain, math-heavy style
    * If I add my EIP mod to this I'm sure it wouldn't be in the same style
* Nick: I object to this because I think we need a better spec for Ethereum before we propose a process for changing it
* Ben: Maybe as a prelude to this we should revisit K-EVM or other spec question
* Nick: Currently the spec reflects only the _current state_ of Ethereum, whereas I think ideally a client would include all information necessary to build and sync a client from genesis
* Let's continue this conversation either as a PR on EIP-1 or else on the [Fellowship of Ethereum Magicians forum](https://ethereum-magicians.org/)
* Vlad: Yellow paper already has its own update process involving Yoichi and others, let's not have dev process blocked on their process, would affect them also so get feedback from people working on yellow paper now

## EIP 960: Cap total ether supply at ~120 million [[25:11](https://youtu.be/vKumx5CIA-k?t=25m11s)]
* https://github.com/ethereum/EIPs/issues/960
* On last call decided to wait for community feedback and then discuss further on this call
* Vlad: Is this an implementation to a repo or just a norm re: rewards in protocol?
* Danny: Discussed as an actual implementation, having rest of issuance live in 0x0 address and live there
* Vlad wrote an article [Against Vitalik’s fixed supply EIP](https://medium.com/@Vlad_Zamfir/against-vitaliks-fixed-supply-eip-eip-960-18e182a7e5bd) arguing against this idea
    * Vlad: public debate is too early to warrant implementation, unclear about norms
* Vitalik: I agree, it's too early to know community consensus
* Danny: We have a lot of more important development tasks, if this were to happen it would be after that
* Vlad: And if there isn't strong consensus it might not be highest priority/might not be worth imeplementing
    * Or do devs implement regardless of whether or not there's community consensus?
* Danny: Is there a historical precedent for that?
* Vlad: The Dao is a good example of implementing something contentious when there's only some indication of support
* Martin: Implementing something that might not fly is probably not a good use of time
* Alex: Let's schedule to discuss this again along with discussing date for Casper hardfork
* Vitalik: We could do that. But there's also the other question, if it is to be implemented, when is the right time? Before/same time as Hybrid Casper? Full casper? After it's been running for six months? Lots of options there.
* Danny: Let's table this one until someone wants to champion it

## EIP 969: Modifications to ethash to invalidate existing dedicated hardware implementations [[31:51](https://youtu.be/vKumx5CIA-k?t=31m51s)]
* http://eips.ethereum.org/EIPS/eip-969
* Picking up from last call, wanted to wait to see how community feels about it, if clearly of interest we'll bring up in the next call
* [Hudson's summary](https://www.reddit.com/r/ethereum/comments/8bkkv1/asic_resistant_hard_fork_discussion_overview/) of both sides of this debate
* Piper: I acted as a facilitator for this, left this for the author of 969 to champion this if they want to
* Vitalik: Let's wait for more data, if people want to keep digging for that data, great but at this point we know too little to be discussing this in concrete terms
* Vlad: You mean, how exactly does the ASIC work, what sort of spec would definitely make it obsolete, etc.? Not, do people support it or not?
* Vitalik: Yes, the technical stuff
* Vlad: A lot more people saying it's important it happen than people arguing that it shouldn't happen
    * One arguing against is Phil Daian: [Anti-ASIC Forks Considered Harmful](https://pdaian.com/blog/anti-asic-forks-considered-harmful/)
* Vitalik: three categories of people here
    * 1. Pro
    * 2. Pro if zero cost, anti given real world costs
    * 3. Anti even given zero cost
* Vlad: and the "my GPU mining farm isn't profitable" people?
* Vitalik: they probably go in pro-fork or moderately anti-fork category
* Alex: If you want to move forward with ASIC protection, if it's something we have enough data on, I would put it together with first PoS fork because there might be some concerns from GPU miners, if we also provide them with ASIC resistance it might be a good compromise
* Martin: How complex would it be to make a small change to ethash? How much development are we talking about?
* Nick: As part of an existing fork, relatively low, avoids overhead of setting up a hard fork
* Vlad: We don't really know what these ASICs are, if they're generalized hardware much harder than if they're very specialized
* Danny: If modifying a parameter is cheap and has some probabilistic value to communiyt, might be worth it
* Vlad: Might be worth it just to measure the drop in difficulty
* Danny: hard to isolate change if bundled in with Casper reward changes, not ideal experimental design
* Nick: Suggest rolling into next hard fork regardless if overhead is low, current proposal of changing some FNV constants
* Vlad: Even if a small change, we still need to think about whether there's community support -- for this one it feels like yes but it's anecdotal
* Nick: Few people strong no against this who object to the very idea, more people like myself question whether we have cost-benefit in our favor
* Vlad: Shall we table for now pending more information?
* Lane: Sounds like it should not be its own hard fork but we could roll into the next hard fork
* Nick: Yes, no evidence/urgency to create a hard fork just for this
* Danny: Could bundle with Casper because it's like a compromise with the miners as described before
* Vlad: Agree it doesn't deserve its own hard fork, but I'm not convinced which one it should be in, if any
* No one is opposed to rolling this into another planned hard fork
* Piper: It would be good to have someone own this to move it forward, I'll reach out to the EIP author and see if they're willing to be the lead on getting it defined for a subsequent hardfork, so let's bring it up again when this person is up for this responsibility
* Vlad: So rescheduled for next meeting where we have a champion

## EIP 999: Restore Contract Code at 0x863DF6BFa4469f3ead0bE8f9F2AAE51c91A907b4 [[43:26](https://youtu.be/vKumx5CIA-k?t=43m26s)]
* http://eips.ethereum.org/EIPS/eip-999
* Afri: summary
    * Written to replace self-destructed parity wallet library destroyed last year in November
    * Asking how to proceed and whether there's any feedback
* Martin: Should we discuss technical content of EIP or governance process?
* Afri: Not sure if we are capable of going into the governance process here, but if there are reason to improve or reject this proposal straightaway I would love to hear it now, if no objections to reject it in the context of EIP-1 that would be nice too, seeking general feedback from client developers
* Vitalik: Technically-speaking the prtoposal seems low risk and good way to achieve objective
    * It's more a matter of social than technical tradeoffs
    * Should be the domain of community debate and discussion not this call
    * Only if community strongly in favor should we discuss on this call
* Vlad: Broader question I have is whether or not acceptance as an EIP should be blocked on community question
    * Implementation and deployment makes more sense to try to avoid a contentious hard fork if possible
    * If unclear whether community will come to a steady state/no consensus then maybe we should have an implementation and a potentially contentious hard fork
    * But if discussion ongoing/process questions coming up, no clear deadline, then we should wait for a consensus
* Alex: From social side, it's clear the issue is contentious, and will generate a contentious hard fork
    * The Dao had a clearer consensus on the fork side but we still had a contentious hard fork that's still live today
    * So it's unavoidable that this would create a split
* Piper: Let's not map this to the Dao, which was a security issue for the network
* Vitalik: It was not a security issue for the Ethereum network
    * The only concievable issue for the network is if an obviously bad actor had access to the 4M ETH, then they could use this to try to run 51% attacks, transaction spam, etc.
    * If our systems can't find some way to handle a bad actor with 4M ETH then we need to find a way to make our protocol better anyway
* Piper: We did something to handle it, taking the 4M ETH from their possession
* Vlad: Lots of reasons for that, fact that some staker would have a lot of coins was just one piece of the debate
* Vitalik: I don't recall that argument being dominant
* Vlad: We all agree that ideally the implementation would follow community consensus and there'd be alignment, everything released would be adopted
    * But what happens when there's a lack of consensus
    * In the Dao we had somewhat of an answer, there's a flag you can set to have one outcome or the other
    * That way both sides of the debate get served by developers
    * Later developers can decide where the users are and which fork they want to serve
    * Don't think we should have the devs leading the decision, ideally there's a community led decision
    * But what if the community doesn't reach a decision?
* Alex: But the result would be a split, two sustaining communities when something contentious happens
    * In [Avoid Evil Twins: every ethereum app pays the price of a chain split](https://medium.com/@avsa/avoid-evil-twins-every-ethereum-app-pays-the-price-of-a-chain-split-e04c2a560ba8) I argue there's a huge cost to this
    * We can't ignore it
    * So we should try to avoid getting there
* Vlad: I'm not sure every contentious hard fork would lead to a self-sustaining community for both sides, this takes a lot of work
    * Probably for a few blocks
    * But not sure for how many
* Danny: especially on the order of years many communities will falter but in the short term they may last a while
* Martin: What do exchanges do? Which one is canonical ethereum?
* Peter: AFAIK the reason Ethereum classic survived is that poloniex decided to list it after three days after it seemed to die
    * From exchange perspective it always makes sense to list it as it's in their financial interest to do so
* Vlad: But they do need to list one of them as ETH in a way that doesn't upset their clients
* Martin: And if one dies out before that happens how do they pick one?
* Vlad: Two main parts
    * Is trademark controller going to sue them?
    * What do their customers think?
* Alex: Doesn't matter which one becomes canonical, once there are two of them, there's incentive for both to be listed, traded, etc.
    * This is a bad thing for the community as a whole
    * All dapps need to decide which one to serve, dragged into political mess
    * Some have a legal mess if not protected themselves appropriately
    * We know there will be a split, it doesn't matter which one wins
* Vlad: Other side of that is that there's a cost associated with never having a contentious split
    * Having a norm that we should avoid contentious forks
* Alex: We should try to avoid a fork if we can find other solutions
    * Also don't think we should shut Parity and Web3 Foundation out of this, there's good argument to helping them
    * If not they have more incentive to split
    * We should keep exploring other ways to bring everyone to the table
    * Proposing multiple attempts at recovery, that should be applauded
* Vlad: Are you saying we should either come to consensus to do a recovery or not?
* Alex: No
* Vlad: If we don't come to consensus, or come to consensus not to recover, then there's still a contentious question about having a split
* Alex: It's a governance question, maybe not a good use of this call
    * It goes into a larger governance question
    * Your question on what sort of public goods we can fund by not reducing issuance
    * If we focus discussion on whether there's a governance way to use funds to help victims of bugs, etc., that's my more general thing
* Vlad: Suggestion is just wait for governance debate to continue?
* Alex: Put that in governance pile and keep doing governance until we find a way to fund public goods like Parity recovery - could be considered a public good
    * Not going to happen on this call
* Vlad: So you're against EIP-999 but want to use some other source of issuance?
* Alex: Yes, We should explore other sources of funds without having to recover this multi-sig
* Vlad: Do you really want implementation ASAP as a hard fork?
* Afri: I have more questions than answers, I am just following EIP-1 and trying to figure out where this proposal stands
    * Yes, I'd like to see implementations
* Vlad: The idea of waiting for more discussion - do you have hope for the public debate?
* Afri: So far it's been quite constructive, however it puts me under stress, next step not for four weeks
    * I'm open for counter-proposals
    * We saw several of these already in December, which changed EVM semantics around contracts, that was rejected
    * [EIP-156](https://github.com/ethereum/EIPs/issues/156) or recovery process in [EIP-867](http://eips.ethereum.org/EIPS/eip-867)
    * For me this is the most logical step to take, just to implement 999
    * Don't see benefit of waiting another four weeks to conclude this
* Vlad: Concern is that this is a contentious hardfork and will lead to a lot of headaches
    * Hope is that as we get more clarity it will become less contentious, but this is uncertain
    * Other option is to embrace the contentious hard fork
    * Hope people figure out which side they want to be on and could pick a side by implementation
* Jutta: But putting it into implementation state doesn't automatically lead to a hard fork

Left off at [[1:01:50](https://youtu.be/vKumx5CIA-k?t=1h1m50s)].

## Client/team updates [[]()]
* geth (Peter)
* Parity (Afri)
    * MyCrypto integration with mobile signer
* cpp-ethereum (Pawel)
* Harmony (mkalanin)
* ewasm (Lane)
* Turbo geth (Alexey Akhunov, [posted in agenda](https://github.com/ethereum/pm/issues/37#issuecomment-383053302))
    * still working on reorg functionality, more detailed report will be delivered at Edcon
* Pegasys (Ben)
* Trinity (Piper)
* Nimbus (Jacek Sieka)
    * a new Ethereum client called Nimbus (https://github.com/status-im/nimbus) from Status.im team that will hopefully see the light of day in a few months
    * we recently completed the basic P2P and crypto parts and connected successfully to a couple of testnet nodes - any malformed, weird or suspicious activity might be us
* Drops of Diamond (James Ray)

## Attendees
- Vitalik Buterin (EF: Research)
- Paweł Bylica (EF: cpp-ethereum/ewasm)
- Jason Carver (EF: python)
- Ben Edgington (ConsenSys/PegaSys)
- Makoto Inoue
- Nick Johnson (EF: geth)
- Mikhail Kalanin (Harmony/EthereumJ)
- Lefteris Karapetsas (Brainbot)
- Dimitry Khokhlov (EF: cpp-ethereum, testing)
- Dmitrii (EthereumJ)
- Piper Merriam (EF: Python/py-evm/Harmony)
- James Ray (Drops of diamond/sharding)
- Christian Reitwiessener (EF: cpp-ethereum/Solidity)
- Lane Rettig (ewasm)
- Danny Ryan (EF: Research)
- Thibaut Sardan (Parity)
- Afri Schoedon (Parity)
- Jacek Sieka (Status/Nimbus)
- Jutta Steiner (Parity)
- Martin Holst Swende (EF: geth/security)
- Péter Szilágyi (EF: geth)
- Alex Van de Sande (EF: Mist/Ethereum Wallet)
- Jared Wasinger (EF: ewasm)
- Vlad Zamfir (EF: Research)
