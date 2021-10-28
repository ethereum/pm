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
* Jutta: But putting it into implementation state doesn't automatically lead to a hard fork, not saying we're going to turn this on in our next release
* Nick: If this leads to a split, then any benefits far outweighed by costs to ecosystem as a whole, and this seems like a reasonable probability at the moment
* Vlad: But implementing it without releasing it doesn't mean we'll have a contentious hard fork
* Peter: If we do implementations in all the clients, it means we are willing to fork
* Vlad: Willing to make the option available, so maybe that's a per-implementation question for now, the purpose of this call is to determine if it's consensus critical
* Vitalik: Don't want to speed implementation unless it has a very high e.g. > 75% chance of being implemented, otherwise we're wasting development time
    * More conclusive community discussion is the only way I could see something like this getting to that point
* Martin: Development effort is pretty low
* Vitalik: We also have testing and "contentiousness handling" so I'd say this is nontrivial
* Peter: When we did the DAO hard fork there was a ton of extra networking code and mumbo-jumbo needed to make sure both forks could survive, if we hadn't done this, ETH classic wouldn't exist
    * So if we really want to give the community a choice, it's not so non-trivial
    * So may be better to wait for community consensus
* Nick: It's a bit easier now that we have chain IDs with replay protection but yes still more work than non-contentious hard fork
* Peter: But we don't have ETH protocol separation at the networking level, so without extra header rules clients will always try to synchronize to the heaviest chain which could be on the wrong side of the fork, we need to figure out how to split the chains
* Vlad: Imagine we never get social consensus on this, do we table it indefinitely?
* Peter: If no consensus then we'd have two Ethereums, do we want that?
* Vlad: If this were about Casper then yes, but basically the answer is always no, but who is to judge?
* Peter: You could have a Casper and a non-Casper Ethereum but the networks are different with different guarantees. In this case the networks are otherwise identical.
* Vlad: If we're never going to reach this consensus then I feel a contentious fork is preferable to tabling indefinitely
* Alex: What if e.g. geth doesn't implement this, would parity still implement and deploy this and make it available?
* Jutta: We haven't decided yet. While there is still a lot of contentious discussion, I'm not convinced it's as contentious as it sometimes seems in social media.
    * This point is important
    * Often conclusions are drawn based on social media but this is not all that matters
* Piper: There seems to be a pretty vocal "no" consensus on the FEM forum, even after removing unknown people, that's one metric
* Vlad: It's hard to measure the community in its entirety
* Danny: This has only been published for five days, it's too soon to start implementation
* Vitalik: I agree that the social consensus does not depend on the implementation details, the idea has been debated for months
* Lane: There was a [Coinvote poll](https://www.etherchain.org/coinvote/poll/35) about this
* Alex: It has swung back and forth several times
* Vitalik: It's at 350,000 ETH, but also uses signing rather than transactions which makes it harder for contracts to vote, and many people with hardware wallets may not be able to sign easily, so makes the poll difficult to participate in
    * I don't believe that something that passes a Coinvote should be considered as community consensus by itself, it's one factor
* Alex: There's a big power law distribution (some votes backed by enormous numbers of ETH)
* Peter: Parity team probably controls a lot of ETH and therefore may have large sway in this vote, so I don't consider this a fair vote
* Alex: But someone developing Ethereum for a long time should maybe have more sway, and we don't have any fair way to measure
* Peter: Depending whether you joined in August 2014 or April 2015 that's two zeroes in your ETH holdings, both people on the team for a while, but a coin vote assumes a guy who joined a few months earlier has all the weight
* Vlad: Agree the polls aren't fair, but at least non-technical people can also vote, if we had opinions of all the coin holders -- but it's not everyone
* Nick: Ideally a voting system will tell you whether there will be a split and what value/use would accrue to each side of the split
* Vlad: If we know this will never be settled with social consensus, then what? Is a contentious hard fork worth it?
* Nick: If it's contentious then I don't think it's worth the cost, but if people do, then they can push forward
* Vlad: This is a deep governance question, this is something we need to think about here
* Lane: Let's continue discussion in FEM forum and in the EIP

## EIP 908: Reward for clients and full nodes validating transactions [[1:21:24](https://youtu.be/vKumx5CIA-k?t=1h21m24s)]
* Bringing this topic up again since it's James's proposal and he just joined the call
* James: advantage of having this in protocol is it would avoid tragegy of the commons, misalignment of incentive for providing a resource i.e. maintaining whole state/verifying transactions
* Vitalik: I thought funding would go to author of user agent, what does this have to do with state storage?
* James: There are two proposed way to do this, Micah made a [proposal in Ethresear.ch](https://ethresear.ch/t/incentivizing-full-state-nodes/1640) to incentivize full nodes, he didn't go into much detail yet
    * How to do this is open for debate
    * I think it's important to incentivize different resource providers for the protocol
* Vitalik: What's the concrete proposal that incentivizes state storage?
    * Cf. https://ethresear.ch/t/incentivizing-full-state-nodes/1640
    * This is just one proposed solution
* Danny: This one should be more formalized before further discussion

## Research updates [[1:26:44](https://youtu.be/vKumx5CIA-k?t=1h26m44s)]
* Danny's update on [EIP-1011: Hybrid Casper FFG](http://eips.ethereum.org/EIPS/eip-1011)
    * Just published this morning, ready for review and discussion
    * Spec generally ready for clients to implement
    * There might be minor tweaks, I'll make this clear on the appropriate channels
    * Not locking in bytecode until we've finished formal verification
    * Ready to go into full swing client implementation
    * Gathering in https://gitter.im/ethereum/casper to coordinate client development and testnet
* Dmitrii: Michael from our team made update which runs private Casper network, so you can test it with Harmony, will add Python Casper client later when it's available
* Danny: I'll keep doing updates here as implementation and formal verification are nearing completion, so I'll signal when it's time to start talking about fork block numbers, etc.
    * Let's leave EIP up for discussion a bit longer before we start writing tests for this

## Hard fork timing [[1:30:02](https://youtu.be/vKumx5CIA-k?t=1h30m2s)]
* Is there a meta EIP for Constantinople?
    * Yes: [EIP-1013: Hardfork Meta: Constantinople](http://eips.ethereum.org/EIPS/eip-1013)
* Question about Parity failing tests on Hivetests has been sorted
* This hardfork meta currently contains:
    * [EIP-145: Bitwise shifting instructions in EVM](http://eips.ethereum.org/EIPS/eip-145)
    * [EIP-210: Blockhash refactoring](http://eips.ethereum.org/EIPS/eip-210)
* 145 is implemented in cpp and geth, 210 implemented in cpp but not in geth, neither in Parity yet
* 210 not marked as "accepted" yet
    * Vitalik: I'm in favor of this being released if we do a hard fork before Hybrid Casper so we can have a dry run of code manipulation
    * What remains between where we are now and implementation?
    * I'm okay with this being a finalized EIP
    * We wanted this to have more testing, not sure if anyone has written more test suites yet, that could be done in parallel with finalization
    * The only thing I expect that testing could reveal is an issue in the serpent code
    * It's assembly-style serpent, could be written in LLL or vyper assembly instead
* Vitalik: Could consider CREATE2, part of account abstraction where you can create a contract at an address where address dependent upon a salt and init code of contract
    * Pre-init addresses with a particular piece of code
    * Useful for state channels, lets you make counterfactual transactions going to counterfactual addresses, with certainty you'll be able to instantitate it later
    * Being sure about the code at that address
    * And having multiple objects in the queue, of which you could instantiate any one you want to
    * Martin: it's based on init code, how can you be sure of the contents?
    * Vitalik: Don't mean sure of in the strict sense, but if you trust the init code and you've seen it then you'll know the contract will have code produced by a particular piece of init code
    * Peter: When you create a contract you have a context with blocks and sender, the init code could react to the context
    * Vitalik: Important that address has to be hash of init code not of final contract code since at instantiation time we don't know the contract code
        * Includes sender, salt, and init code
    * Two-step create thing is an abstraction for account abstraction
    * This is more limited but will make it easier to do state channels and other stuff
* There is no EIP for this yet, let's create one and discuss for the next hard fork

## Client/team updates [[1:40:29](https://youtu.be/vKumx5CIA-k?t=1h40m29s)]
* geth (Peter)
    * At beginning of the week we released geth 1.8.4, 40% speed increase on mainnet
    * Reduced block processing time from 200ms to 100ms on mainnet
    * We merged in Martin's work with the standalone signer, not ready for production use but we want to get it to a place where other clients can depend on it
    * Want to have a standalone signer that can handle all the nasty stuff with hardware wallets
    * Maybe of interest to new client developers that don't want to roll their own
* Parity (Afri)
    * MyCrypto integration with mobile signer
* cpp-ethereum (Pawel)
    * No updates
* Harmony (Dmitrii)
    * Changing DB and cache settings, found that we can get improvements of 5x on block time, when we finish we expect we'll see something close to parity
    * Big memory leaks
    * We'll have a release in a few weeks and fix these memory issues
* ewasm (Jared)
    * Spent last two weeks moving from Travis to Circle-CI, fighting the CI a lot and fixing things
* Turbo geth (Alexey Akhunov, [posted in agenda](https://github.com/ethereum/pm/issues/37#issuecomment-383053302))
    * still working on reorg functionality, more detailed report will be delivered at Edcon
* Pegasys (Ben)
    * Processing all frontier blocks
    * P2P discovery working well
    * Pluggable key-value storage
    * Would like some advice from seasoned developers, come to us or we may come to you with questions
* Trinity (Piper)
    * Mainnet full sync is very close
    * Spent last 1.5-2 weeks chasing performance optimiziations to get block processing times down
    * We're always a few weeks away from an initial release, we still are a few weeks away
* Nimbus (Jacek Sieka)
    * a new Ethereum client called Nimbus (https://github.com/status-im/nimbus) from Status.im team that will hopefully see the light of day in a few months
    * we recently completed the basic P2P and crypto parts and connected successfully to a couple of testnet nodes - any malformed, weird or suspicious activity might be us
    * Status wants to bring Ethereum to the masses
    * Focusing on resource-restricted devices e.g. mobile phones, we optimize for these
    * Finished crypto and P2P parts
    * Now working on various RLPs
    * Expect a lot of breakage on the testnets
    * Once we reach 1.0 our focus will be on light client technologies, since we cannot sync full chain most of the time
    * We're keen on research in this area such as sharding, stateless clients
    * Aiming for full web3 stack with whisper and swarm as well
    * Our licensing is permissive on purpose to help with adoption
    * Hope to be more active in EIP process and community in future
    * We very much welcome reviews and ideas in these early stages
* Drops of Diamond (James Ray)
    * Sharding implementation in Rust
    * Started a month or two ago
    * Put together a basic CLI with notary functionality based on now-retired phase I sharding spec
    * Updated to match latest spec with minimal sharding protocol
    * Working on:
        * block serialization/deserialization
        * Sharding P2P networks
        * Storing data on each shard
    * See list of issues on Github, team of three at the moment, unlicensed at the moment
    * If folks want to learn rust and contribute, they're welcome to do so

## Timing of next call [[1:52:49](https://youtu.be/vKumx5CIA-k?t=1h52m49s)]
* EdCon happening in two weeks so next call will be in four weeks, May 18
* See https://github.com/ethereum/pm/issues/40

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
