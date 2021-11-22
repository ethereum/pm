# Ethereum 2.0 Implementers Call 19 Notes

### Meeting Date/Time: Thursday June 13, 2019 at 14:00 GMT
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/45)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=izspfej05lE)

----------

## Suggestions

**Suggestion 19.1**: Replace SHA256 with xxHash during fuzzing

**Suggestion 19.2**: Data visualization of testnet.

**Suggestion 19.3**: Add interop to agenda in September.

**Suggestion 19.4**: Add to spec - the ability to dump.

**Suggestion 19.5**: Criteria to decide production ready should be written down.

**Suggestion 19.6**: Standardize client implementation by writing specs.




**Danny**: Welcome everyone.
We released [v0.7.0](https://github.com/ethereum/eth2.0-specs/releases/tag/v0.7.0) the other day. It is an iterative semi-major release prior to the end-of-June phase 0 spec freeze. End of June is going to be subsequent minor fixes and is one what probably most people are targeting.
# 1. Testing Updates
**Danny**: Our test have become even more inefficient, in the Python, mainly due to the Tree hashing. We are exploring some caching to speed that up. Right now it's not a major blocker. Mainly just makes generating the tests take longer.

There has been work going on Fuzzing of the Go-specification (ZRNT) and getting some machinery in place to Fuzz the Python spec implementation.

**Protolamba**: There are these two efforts.
1. Trying to find new bugs and everything thats been missing in the current spec. Looking into input bugs. New kind of input has to be checked. To add more condition to the spec.
2. Coverage checking helps identify untested parts specs to complement with new tests before the freeze.

**Danny**: Fuzzing efforts right now isolates the implementation of this spec that go in Python but we have to expand it to clients. Any other testing update ?

**Justin Drake**:  One thing which might be worth highlighting that we do try to replace SHA256 with xxHash. **xxHash is a non cryptographic hash function**, so we can't use it in production but its **much faster than SHA256** for testing.  What is found with Serenity is that **runs the fuzzing about three times faster** so it might be worth having some sort of a flag in the client implementation to switch over to xxHash so that we could do just 3 times more fuzzing.

**Danny**: Agreed.

**Suggestion 19.1**: Replace SHA256 with xxHash during fuzzing

# 2. Client Updates
## Prysmatic

**Terence**:
* Aligned block and epoch process in 0.7
* Re-implement caching
* Benchmark for state transition with profiler and tracer and done optimization of block and epoch process.
* Working on test better alignment and make sure SSZ is up to date.

## Parity

**WeiTang**:
* 0.7 patch implemented yesterday and pass all the test vectors
* decided to deliver no caching until the spec is frozen. Don't want to redo any work.
* For next, Shashper, we are looking into network implementation. In short term, we want to reintroduce substrate network library and get that to network and communication layer for our clients and lend some testnets.

## Artemis

**Johnny**:
* We did a lot of profiling in optimizing on state transition stuff. When we first merged in v0.5.1, we noticed none of our optimization, caching worked anymore. So we profile that by reimplementing the cashing.
* We're starting on the next version of the spec.
* The good news is also our **short-lived testnets can run pretty much indefinitely**.
* We’ve  broken out a validator client implementation. Fall in line with other clients by making them discrete from the Beacon chain.
* Joseph wrote an article about [Ethereum 2.0 Deposit Merkle Tree Implementation Guide](https://medium.com/@josephdelong/ethereum-2-0-deposit-merkle-tree-13ec8404ca4f?postPublishedType=initial).
* also working with Harmony and Raul (protocol labs) on [minimal JVM implementation of libp2p](https://github.com/raulk/jvm-libp2p-minimal/)
* Released a bunch of bounties funded by Joe Lubin for super simple Network implementation so that we can test the consensus layer in multi-client  testnet.

## Trinity

**Hsiao-wei Wang**:
* Working on state transition to version 0.7
* Testnet implementation before the end  ? is finalised.
* working on Eth1 deposit contract, going to use it to check deposit contract log on Eth1 chain.
* Working on Discovery version 5.

**Danny**: Are you planning on using the Eth1 implementation in Trinity as monitoring or are you just writing in web3 to connect to whatever node?

**Ithaca**: Currently I'm using web3

## Lodestar

**Cayman**:
* In a branch, we are passing the v0.6 spec test except for BLS verification. We're still working through that. It's kind of odd because we're passing the BLS spec tests like the ones for BLS  specifically.  It has to do it like which private keys are being used.
* Also in the past few weeks we integrate GossipSub and implemented the RPC protocol as it exists in the spec right now. So, now have networking layer.
* Also toying around with pulling up pieces of our code and rewriting them in assembly script which is a language that  looks like typescript  but it compiles to WASM.
* We're starting with  lmd ghost just to try something out and get used to the tooling.
* Our next steps - we're working towards like an end-to-end short-lived testnets.
* We also need to finish our syncing modules, so that we can sync between the network and the chain.

## Nimbus

**Mamy**:
* Regarding the specs, 2 PRs pending for v0.7 compatibility.
* We've backward sync integrity, so requesting blocks up to a point is available.
* On Networking side, we've libp2p daemon integration in Nimbus. Currently working on releasing libp2p based testnets.
* On libp2p library on pure Nim, we have an issue on mobile because the mobile phone application makes it sleep and it kills the connection.
* On the Eth1 front, we now have an API to watch the contract, the goal is to use Nimbus for that.
* Regarding Eth1 security, we are starting fuzzing on the Discovery and fixing bugs for Eth1 implementation.
* Open question to all the clients - we would like to have data visualization of testnet. Add interop to agenda in September. Some kind of minimal RPC standout to request to clients - block we're on, how many things we've processed. So, that we can have some kind of nice display of what is going on multi client testnet.

**Danny**: Agreed.

**Anton**: Feel free to take a look on the [ETH2.0 metrics](https://github.com/ethereum/eth2.0-metrics/) work and get inspired.

**Jonny**: Why make it a RPC and just not dump it to a log file?

**Mamy**: You have two ways for metrics:
* Push- to a database or a log file and retrieve
* Pull- it requests your state, you just reply.

**Jonny**: The problem with pull is that you have to be in sync. You have to know every slot,  I better ask.

**Danny**: Big data consumers like Amberdata, they want both.

**Jonny**: Let's add that to spec - the ability to dump?

**Danny**: Make sense.

**Preston**: About the document that translate, this week I'm putting together the API design. It's still a pull method but supports data providers like Amber data or Etherscan or anybody who wants to build some sort of read access, consume data remotely without having access to the file system,  so it supports that use case.

**Paul**: Ther're two different things here.
What Mamy was talking about is metrics. Like developing useful metrics to tracking - how your system is performing (Anton is working).
What Preston is talking about is more like an API to the uses of the application. These are completely different things.

**Mikerah**: We can also have this **extra stuff optional for client developers**.

**Danny**: I agree.

**Suggestion 19.2** : Data visualization of testnet.
**Suggestion 19.3** :Add data visualization to interop agenda in September.
**Suggestion 19.4**: Add to spec - the ability to dump.

## Harmony

**Anton**:
* we have completed wire implementation and regular sync.
* up-to-date with 0.6.3 and passing all compatibility tests
* currently working on adoption of latest configuration
* started working on validator to see the interface
* started working on minimal libp2p JVM implementation.

## Lighthouse

**Paul**:
* up-to-date with spec 0.6.3 and passing all tests
* Running a testnet and looking into graphs about what we're doing. Its very easy with Prometheus and Grafana to get dashboard.
* progressing on Discv5
* have been fuzzing on own fuzzing tool
* Kirk has been working on Vitalik's optimized BLS signature schemes
* stress-testing on testnet with 1s block time and trying to see if we can break it, finding bug and fixing it.

**Danny**: How much forking are you seeing in testnet with 1s block time ?

**Paul**: Not a whole lot because we didn't add network latency into it yet. We are trying to see, if we can sync under really heavy load. There is a cool tool PUMBA which adds latency for dock setup, we are going to apply that for setups.

**Mikareh**: Fuzzing tool, is that specifically for Lighthouse or you are going to generalize it so other client team can also use it?

**Paul**: The one that we use now is Lighthouse specific. We would consider making it. The reason we haven't made it generic is because we already have a generic fuzzer so we didn't think it was useful. This one we are trying to keep it server side. If there is one that everyone is using, will definitely be helping with t hat one too.

**Adrian**: This is a Rust specific one . We're targeting very specific function inside our Networking spec in Lighthouse specifically, can't imagine we target other function in other clients.

## Geth

**Protolambada**:
* relatively quite.
* trying to figure out what to do with recent specs
* about fuzz, generalized testing efforts is currently spec focused

# 3. Research Updates
**Danny**: Whats going on in Phase2 front?

**Vitalik**: The main update from on my side is [SSZ](https://github.com/ethereum/eth2.0-specs/issues/1160) stuff. Finally managed to get the SSZ partials implemented in Python.  Realization I got from that is it's just way more complex at present that its used to be. The bulk of the complexity comes from Merkle proof paths in the dynamically size of objects like a list instead of a fixed length.  If you remove that property so that there is an exact and stable one to one correspondence between paths.  If some particular object would always have the exact same sequence of moving Merkle tree to get to it that would probably remove the bulk of the complexities from the SSZ partial implementation. I had some discussion with other people and the proposal that we seem to be converging on is basically requiring list to have a max length so that you can always have them in the same position.
It can be thought identical to Vyper like in Vyper you can have a fixed length list that has end value or you could have a dynamic link list. But with dynamic length list you have to specify what the maximum length is. The idea would be the serialization would not change at all except maybe at some point later in the future we might want to add another SSZ serialization Vyper list. For SSZ hashing length of a Merkle Branch would be length of a fixed value.
Example: If  your list has a maximum length of 20. Then it get rounded up to 32.  The length of Merkle branch would always be 5. Regardless of what we put the actual length of the list. It doesn't change depending the current / dynamic size of the list.

**Danny**: This is simplification on tree hashing side and not a major change on serialization.

**Vitalik**: The only thing in this requires us that we'd have to run through the block and state data structure for every dynamic list and stick a maximum on it. For the block data structure in phase 0 there is no problem because we already have a natural maximum which is the constant for the maximum numbers of each objects in a block.
The one thing in the state that is currently dynamic is the validator set. For the validator set we just need to have something reasonably high.

**Danny**: The historic root is also unbounded currently.  

**Vitalik**: I've been thinking about **how abstracted fee market would work?** How block producers will collect fees in the context that different execution environment existing.  **The main design here is to simplify the experience for the block producers and make them get fair amount of revenue**. I came up with this idea where there are some standards for how execution environment pay fees. They would issue receipt in standardized format. The  execution environment will collect the fees from the transaction centre, the  execution environment will issue a receipt, the  execution environment would have an account at the standard execution center called fee market where block producers will publish the receipt and collect the fees there.

Instead of using receipts, you would use synchronous calls, this would involve transaction being able to call other base layer transactions inside of themselves.

Another thing I realized we need to start taking seriously L2 moving forward is Light clients and Light clients server markets.  Basically because everyone will be a Light client in almost every shard and there is going to be heavy reliance on this node that have data saves in that particular shards and provide Merkle branches in exchange of payment through a payment channel. If you have that architecture then Light client servers just could be the relayer and this transaction package could just be relayer. The category of node that specializes in maintaining the stage for a particular shards is something that probably we would want to think about more. I know some of Geth developers like Zolt spend some time thinking about it.

**Danny**: He is working on channels to fund light servers on Eth1.

**Ben**: Quick update from PegaSys research. The Handle paper of [BLS signature aggregation at a large scale](https://arxiv.org/abs/1906.05132) is publish now.

**Justin**: Going back to Phase2, one of the things we look at is what is the work to be done to [Eth1 execution engine](https://ethresear.ch/t/work-to-natively-integrate-eth1-into-eth2/5573).
There seems to be rough consensys that we wouldn't want to launch Phase2, without any execution engine, just the basic logic, the very thin layer. Instead we would want to go with a more controlled launch where we have either Eth1 as execution engine or a new execution engine which has all the goodies that is in, may be called as Eth2 execution engine or both at the same time.

**Danny**: Agreed.

**Justin**: In addition to the consensys layer, I think it would be significant external infrastructure that needs to be built out and tested, like the fee market. We might also want to test Statelessness and things like that.
Another update about **Eth2 Genesis**, phase0.
One of the things merged recently  is the  removal of the Eth2 Genesis log from the deposit contract. We replaced it in the favor of a custom function subjectively runtime size as they were, which is  both more secure because it allows us to better capture what we wants to have as a trigger for the Eth2 Genesis and also more flexible.
There are few requirements for Genesis:
* Sufficient Eth at stake (2mil ETH)
* Sufficient production level clients (ideally 3 but could launch with 2 )

If we’re to bake in a trigger in the deposit contract, when we’re ready to launch; this gives flexibility to update the Genesis trigger.

I guess **from a timing perspective, we're on track for the phase zero spec freeze on June 30th**. That might be a good opportunity at the end of this month to think about new realistic targets.

Two good things to think about is
**1. when we want to launch the deposit contract?**
    * The idea is to launch the deposit contract ahead the target Genesis to allow time validators to make deposits.
    * Do a deposit contract ceremony at Devcon. One of the reasons of having this public  ceremony is so that we can all agree on the exact address of the deposit contracts and avoid scam deposit contracts.
**2. Targate date for Genesis?**
We still have quite a bit of time before the end of 2019. I think looking at the target Genesis dates towards the end of 2019 could be realistic. One thing that could work well is the 3rd of January 2020, the 11th anniversary of Bitcoin genesis.

Assuming, we do the deposit contract ceremony at Devcon, it will provide us enough time to accumulate 2 mil ETH and will allow 7 months from today to reach at least 2 clients to production status.

**Justin**: Criteria for production ready clients - well I guess at the very least that we have a long-running Cross client testnet which has gone through  security audit, has gone through fuzzing, part of which may have gone through form of verification and potentially has not suffer major issues for  half the amount of time.

**Vitalik**: Same as we have in Eth1. Long running for some period of time with no bugs and the security auditing on all the clients.

**Suggestion 19.5**: Criteria to decide production ready should be written down in some post.

**Danny**: Agreed.
I think that  launching the deposit contract we should at least have some target for going to production. Because otherwise we're asking people to put their money in for an indefinite amount of time.  People may not actually show up and we don’t get the participation levels that we expect.

**Joseph**: I have a question about the deposit contract. so I am assuming the changes you're talking about now are replacing the log with function for Eth2 genesis?

**Danny**:  yes so essentially instead of listening for that log,  you're running a function locally and get a new deposit on whether it's time to start

**Joseph**: OK it's a call rather than a log it's going to be a system that would not going require gas for execution.

**Danny**: No, I am receiving logs locally and I've local logic on whether to start the genesis. We are going to be more dynamic to make decisions. Hopefully simpler and flexible.

**Justin**: I mean that was the initial [trigger](https://github.com/ethereum/eth2.0-specs/blob/dev/specs/core/0_beacon-chain.md#genesis-trigger) where we realize that people could make just one Eth deposits the minimum and make a bunch of these and then trigger the Genesis. Someone send 32 Eth at the same address  repeatedly and then they triggered the Genesis. The shared source of truth argument is a little bit of an illusion and the reason is that we need an alternative backup mechanism without presets for source of truth. If we don't reach that , we don’t reach the target.

**Joseph**: That makes sense but I do a wonder why then we would calculate the sparse Merkle tree in the contract because essentially that the sparse Merkle trees are useless if we’re not ever meeting to  any Genesis root value.

**Justin**: It’s still valuable. The sparse merkle tree for the deposit basically allows for the  accounting of the deposits and making sure that it is properly reflected on Eth2.

**Danny**: Most people will be handling a tree locally. So its a helper, gives you more flexibility. Say, if you started running this for a year from now as a validator, you might use that mechanism and  actually have a sparse view of the deposits locally.

**Joseph**: I think it would be great if we could get deposit root public.

**Justin**: I just checked its public.

**Matt**: There are some more update on research. There are good conversation about, what a token is going to look like on execution environment of Eth2 at scaling Ethereum. And still thinking about different ideas there but I went to share an idea, I can get some feedback is about removing the need for like two transaction flows for ERC20. Discussion in [Eth magician forum](https://ethereum-magicians.org/t/brainstorming-the-token-standard-in-eth2/3135).

More about it is  the idea of sending a transaction to any kind of contract.  Since it's already signed by you or by your contract wallets,  you're essentially giving  permission to send a token. It's just that right now there's  not an ability of  saying that you want to also send some ERC 20 token or something other than Ether in one transaction. It  has to be split into like notifying the token contract and so if we can extend it to wear message.value is some token contract address and some amount of tokens. Then we can add some EE function or opcode essentially that like as a delegate call to the Token contract assuming it supports like some generic interface that supports transfers. So the message I sent her through delegate call will still be the message. Send her to the Target contract with the user one. Then I can verify that, that user was sent over to that contract.

**Danny** : Help me understand, that this is functionality that could be defined in the contract and not the protocol wide?

**Matt**: Yeah, the message I value that's going to be kind of like an EE concept. Since it's not going to live at the protocol layer and so if we can just extend that in the context to be an address and a value.

# 4. Network
**[fjl](https://github.com/ethereum/eth2.0-pm/issues/45#issuecomment-501699492 )**: Sorry, I cannot join this time. discv5 updates:

* Go implementation is progressing. Still missing integration for the topic stuff, but basic DHT works.
* Implementation in Trinity (python) and Lighthouse (rust) is ongoing. * Rust version is pretty far along.
* Minor spec changes TBD.
* We are negotiating an external protocol audit.

**Mike**: From last call we get some feedback on from production readiness to implementation and test environment. We're taking action on  a lot of things that came up. For JVM LibP2P, I think Jonny covered it. Web3 Lab which is also looking to get involved too. so we may get more Firepower on the implementation. But, even without that it seems to be progressing pretty well. On the production readiness of JS LibP2P, we followed up with Chainsafe folks, who have worked on JS libP2P and know what its flaws and warts work. We are looking at making a grant to fix up things, mostly documentation issues so we now have a full-time writer on working on specifications for LibP2P.  I know that's been a weak spot. Everyone who tries to implement it how can I implement this without a proper specification. We’ve a full time writer and will continue it indefinitely.
There was some benchmarking at the scaling Ethereum event in Toronto . We are working with White block to try to iterate on those tests. Its good initial work we’ve done.

**Danny**: There is telegram channel where you can ask questions with Mike to be better directed. Any questions?

**Jacek**: Yeah I have one. I was thinking about the transports and there has been lose plan to move on to maybe TLS. Any thoughts on that or progress updates?

**Mike**: Yeah, it is the intention to move on to TLS. The status of TLS varies with implementation. Whether it is complete or not various implementation. We've working TLS1.3 implementation in go-LibP2P implementation.  I do not believe we have one in JS and other languages, but the point is not all of them have it. So, we are going to be falling back.

**Jacek**: Two aspects to that question :
1. Is it finalized how LibP2P over TLS should look like from spec perspective or functionality perspective? For clients, do they have something to implement?
2. Are there any concerns that would prevent TLS from becoming the de facto transport for where  LibP2P runs implementations have caught up?


**Mike**: On your last question, I am not TLS expert but talking to our expert Martin, there's no reason why we would not eventually go 100% TLS once implementation are caught up. We have no theoretical reason not to do that.

**Jacek**: From a client perspective, on spec, have you decided on what you want?

**Mike**: I think we're happy with Go implementation and want to turn that into a spec. I can follow up with Martin, who is TLS expert and implemented that. Overall we're satisfied.
There are a few issues with Rust TLS which Rust main library does not support self designed certificates which we would like to use in some cases. There are some open questions. SO, NO, we are not fully certain but we're extremely close.

I think, it's not our intention to re-implement TLS on in every language. We're mostly relying on language standard libraries - Go or node1 for JS

**Zak**: What's the technical reason behind implementing TLS or requiring it at all?

**Mike**: We want o support something that is industry standard and that TLS is the standard. SECIO is something that we wrote, and security audit of it will be done. But for a lot of use cases we think, it may be safe to support TLS1.3. We couldn't use it in past because, prior to version 1.3 TLS required you to have a notion of a server or a client. You had to designate one side as a server and other side as a client, it doesn't make sense in peer to peer. 1.3 finally gives us a  way to not make that  distinction.

**Zak**: If payloads are inherently cryptographically secured from the application layer, whats the point in providing additional encryption on the wire?

**Mike**:  Good point. It's not mandatory and you can use on unencrypted transport. So if you're doing the encryption at the application layer then you could use unencrypted transport.

**Zak**: In which use case would I require or want an encrypted wire in terms of Eth2?

**Mike**: I think this question is out of my expertise so I don't have a good answer for it. I think maybe we could follow up with Raul next week.

**Jacek**: One reason we of then want  to use this because some Networks do packet filtering
And anything which they  don't recognize like HTTP and HTTPS traffics, so those might be the reasons.

**Adrian**: The RPC protocol and the Gossip sub don’t have any encryption built in. Adding encryption at the network layer prevents. There is no encryption at the application layer at the moment.

**Zak**: Why not just use wire guard - VPN tunnel between two separate points?

**Danny**: I think it make sense to have the capability to support encryption in the way. We don’t encrypt at the application there nor should we necessarily look into encrypting at the application there, so having this an option is a good one.

**Zak**: Updates -
* We wrapped up our initial P2P gossip subtests.  We had a call with Mike and Raul, a couple days ago. So we're currently in the process of like designing an actual test phase this them, I am drafting something this week. I will post it on GitHub and would like any feedback from the community in designing these tests and ensuring that the topology is correct, based on the consensus of the community.
* We are re-writing the client to remove the daemon our test client. We started working on a discovery v5 implementation and C++. SO we can perform similar tests and analysis on discovery v5; we are doing that concurrently.

**Danny**: Each of you team seams to have at least one networking guys. When Zak does post the next plans for tests, I’d love if you all could take a look before the test implemented.  

**Zak**: Another thing that we need to discuss to move towards multi clients, the way keystores are implemented. If we can standardize how keys are stored might be helpful for interoperability and using easy testing that all the client implements the same kind of function. SO, we don't. have individual logic for each specific clients. Like in Prysm, they use the Keystore from gas but we can use it like a flat JSON file. If we can standardize across clients how that process occurs then it will be much easier for testing in future like interop efforts.

**Jacek**: Key storage is very platform specific. A lot of platform offers keystore that are supported by hardware.

**Zak**: I don't think that it's like super important how we do it . At this stage what is important is that we agree and standardize some implementation. However,  it doesn't need to be necessarily for production purposes but at least for these initial R&D and like testing phases that would be a lot easier.

**Jacek**: I think import export should serve that.

**Zak**: Whatever that is, we should just define. We should just specify that like write a spec; this is how we should do it. We will implement that in all the clients just that we need to agree on what it is going to look like.

**Danny**: Agreed.

**Suggestion 19.6**: Standardize keystore import/export for client implementations


# 5. Spec discussion

**Danny**: I did want to survey how people are thinking about and searching for attestation slashing.  Cem and I were talking about that and I know that some of you have dug into it. If someone wants lay of the land as they see it, might help.

**Ithaca**: From clients perspective, that just add complexities. There is no real obligation from a protocol point of view to perform slashing. Its almost outsourced like a third party.
Difficulties lies in the fact that we can't really write conformance test.

**Paul**: Part of me thinking about moving into a separate process but not sure if it going to chew up the capacity to maintain consensus but that's actually just more complexity in the long run.

**Danny**: Generally our view consider narrow every time we have finality. But in doing so , if we receive an attestation for something that's outside of our block tree or may be for something in the past. We may or may not have the requisite data and see if the attestation is valid or see who is even the part of that attestation. We don't necessarily have the state to go and verify that decision. Under that consideration, even if it is slashable, we might just discard. That probably is fine in general because we finalized things.

**Paul**: If we want to try and incentivize clients to implement slashing, one way to do it might be when we release these testnets is to make bunch of open source tools that allow people to very easily create malicious blocks. Add the ability for people to cause chaos. If your clients doesn't support it then we fall of line but that's the way we incentivize people, it's really not protocol level.

**Danny**: We do want to have testnets in which say 50 % validators go offline and we go through an activity leak and during those times when your block tree becomes relatively large wrt your latest finalized and those are the times that you would be more concerned about people going back to two epochs and signing something new and attempting to mess with things. So, we should definetly create this scenarios.

**Jacek**: I would be interested in hearing thoughts on slashing protection, client stashing data that they don't accidentally cause a slashable condition for their validator. How much extra data do we have to store because we voted for a branch that later became unviable ? SO that clients don't create the slashable condition accidentally because they have forgotten about it.

**Danny**: The requisite data held can be very narrow. This is not optimal and in terms of the optionality given. If you remember your latest attstation, you just not vote on something that is from the past at all. I will add more to the validator guide him what you think is the minimal that you think.

**Paul**: As long as you never vote in future, there is always a case where you can choose to just skip a couple of duties and then you're safe again. But if you choose to vote in the future, you've to wait until you say.

**Dany**: The only case in which that is not true if your node sometime forgets the latest justified and points to a previous justified and wants to a new fork. Then you could end up doing us around.
Slashing is hard that is something that we literally cannot launch without. Whether it is baked into clients or we have some sort of other processes running, we as a group need to solve this problem.


# 6. Open Discussion/Closing Remarks

**Joseph**: Organizing Interop - We got contract sign and place called Muskoka. It will fit 25-35 people. Its **September 6-13**. I will send out RSVPs as soon as it is confirmed. It will be **restricted to implementers and researchers**.

**Hsaio**: Reminder: Devcon application is open.


## Attendees


* Adrian Manning (Lighthouse/Sigma Prime)
* Alex Stokes (Lighthouse/Sigma Prime)
* Alex B.
* Antoine Toulme (ConsenSys)
* Anton N.
* Ben Edgington (PegaSys)
* Carl Beekhuizen (EF/Research)
* Cayman
* Daniel
* Danny Ryan (EF/Research)
* Ithaca: Hsiao-Wei Wang (EF/Research)
* Jacek Sieka (Status/Nimbus)
* Jannik Luhn (Brainbot/Research)
* Jonny Rhea (Pegasys)
* Joseph Delong (PegaSys)
* Justin Drake
* Leo (BSC)
* Luke Anderson (Lighthouse/Sigma Prime)
* Mamy Ratsimbazafy (Nimbus/Status)
* Matt Garnett
* Mike Goelzer (libp2p)
* Mikerah (ChainSafe)
* Nicholas (Hsiu)
* Paul Hauner (Lighthouse/Sigma Prime)
* Pooja Ranjan (Ethereum Cat Herders)
* Preston (Prysmatic)
* Protolambda (EF)
* Steven Schroeder (PegaSys)
* Shay
* Terence Tsao (Prymatic)
* Tomasz S.
* Wei Tang (Parity)
* Vitalik Buterin (EF/Research)
* Zak Cole (Whiteblock)
