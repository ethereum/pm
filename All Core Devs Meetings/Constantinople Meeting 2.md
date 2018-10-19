# Ethereum Core Devs Meeting Constantinople Session 2
### Meeting Date/Time: Friday 19 October 2018 at 14:00 UTC
### Meeting Duration 1 hour
### [YouTube Live Stream Link](https://www.youtube.com/watch?v=5Q67tmkZ5So)
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/61)
### [Constantinople Progress](https://github.com/ethereum/pm/issues/53)

Video starts at [2:52](https://youtu.be/5Q67tmkZ5So?t=172).

# Agenda
1. Ropsten issues
2. When fork?

# What happened
* Afri summary
    * Noticed that hard fork was coming much earlier than expected, two days earlier, on Saturday, evening Berlin time
    * Client releases were very late, released less than one week before the fork
    * No one was mining the Constantinople chain
    * High hash rate on Byzantium chain
    * We tried to find miners willing to push hash power onto the Constantinople chain, took two hours to get the first block mined
    * Then we discovered first consensus issue between geth and parity
    * Harmony was for some reason using the wrong config
* Hudson
    * We had trouble monitoring the fork, knowing which was the canonical chain
    * No fork monitor, only basic ethstats page
* Lane: Can we work backwards and discuss what testing needs to happen before a mainnet hard fork?
* Hudson: Alexey had an idea to fire up many small testnets
* Martin: Yes, this is theoretically possible
    * Lots of small things went wrong
    * What went right is that we successfully found the consensus issue
    * We had limited visibility into the various forks, would've been good to have had more visibility
    * By now actual Const. changes well tested
    * Regarding transition of rules, while interesting, I think it's not that interesting to do it in real time
    * Observing the split network otoh is interesting, seeing how clients handle e.g. reorgs
    * Doesn't really have anything to do with Const. per se, it's just an interesting stress test that we should do, test client behavior under bad network conditions
    * On fuzzing, we're fuzzing on a less refined engine, which found bulk of consensus issues before Byz. hardfork
        * It's running 24/7, around 8 tests per second
* Hudson: So we think this is sufficient for testing infra. as a whole?
* M: Not necessarily, we also have manual tests, roll out on Ropsten, and fuzz tests
    * Would be great to also have more refined fuzz tests from libfuzzer
    * Great if we had more people to write manual tests
    * But at some point we have to say, are we satisfied or is there more we need to find?
* H: That's a good overview of where the tests stand
    * Something else that went wrong is that we weren't coordinating with the miners until the last second
    * Foundation has a miner running
    * Some miners in the ecosystem
    * We need to coordinate better to switch the hash power over before a testnet fork
    * Big problem is pinpointing the right person for this stuff
    * Which might default to me (Hudson)
    * But I could use help, esp. for things like the fork monitor
* Nick: Fork monitor is more or less unmaintained right now
    * It's open source
    * We should test this before another testnet hard fork
    * Are we rolling back Ropsten?
    * Lane: Alexey was pushing for this but I think he decided it's now too late and would rather spin up new testnets
* Lane: Have we had a release manager for forks in the past?
    * H: I never called myself this but I did act in that role
    * H: I hope someone will step up to do this
* H: Need to coordinate better with miners
    * Need to make sure time between client release and fork is sufficient
    * What's a good length of time for that?
* Martin: When we set the block number, is it set in stone? Can we signal it?
    * H: Could the signalling method inject a block number into the clients?
    * Before, a couple of weeks earlier, we release a client with a hard coded block number
    * One week later, if we decide to change the block, we need to rerelease
    * Const. functionality is there in all of the clients; we could add a commandline switch where you specify fork number, or override it
    * H: Can you hardcode a smart contract address and load it from there?
    * Yes, but there might be issue with light clients or fast sync clients that don't have the right state
* Johnny Rhea: Could we use IPFS? Point to latest content hash containing a block number
* Wei: Two ideas
    * 1
        * Put signalling into header data
        * Would work for all light clients that at least download all historical block headers
    * 2 Hardcode version number into the header
        * Requires changing header format
        * Then even if light client doesn't download all headers it would still work
* Jacek, Lane: Are we solving a real problem here or introducing unnecessary complexity?
* EG: Should we require a minimum interval between client release and fork?
* Nick: Which clients? Could I have my own client and delay the fork if it's not ready?
    * Lane/Hudson: We'd want to include clients that make up at least 10% of the network
    * Or multiple clients totaling to at least a certain threshold e.g. 50%
* Lane: Do we want a war room or canonical source of truth?
    * Project manager should manage this
    * Hudson put together a HackMD doc for Ropsten fork, that could be okay for now
    * As Martin said, all of the big things have been done
    * So what we need is more testing to make sure we're comfortable
* Afri: What's the status of Const. tests?
    * H: We need to write more manual tests
    * Fuzz testing is running 24 hrs a day, 9 tests/sec.
* Hudson: Let's talk about what needs to happen between now and a mainnet HF
    * Coordinate with miners
    * Add time between release and fork
    * Fix fork monitor
    * Define a better communication, "war room"
    * AllCoreDevs channel works for now, along with e.g. a hackmd file that's a source of truth for what's going on
    * Previously it was me or Afri handling a lot of the comms. to exchanges, miners, Infura, MyCrypto, etc.
* Lane: Is there a master list of these tasks?
    * H: It's in my head, and we have some Skype channels
    * I don't know which exchanges or miners are in these channels which is good so I'm not one on one reaching out to these people
    * So we have a way to reach out without it being too coordinated or centralized
* Lane: We could decentralize this further with a "chain of communication", bake in redundancies, etc.

# When fork?
* Afri: We used to have two weeks notice on the testnet, some minimal reliable stability, before a fork
    * Before we discuss _when_ to fork we should talk about this
    * I'm not comfortable talking about a HF date before the tests are ready
* Martin: On Dimitry and writing tests
    * AFAIK shift stuff is done
    * Working on SSTORE tests
    * There are EXTCODEHASH tests, not sure if they are up to date
    * Block rewards
    * Difficulty tests are finished
* Lane: I agree with Afri
    * Can we pick a "no earlier than" date?
    * H: This is currently end of November
    * H: How would people feel about pushing it back to January or February?
    * Need to factor in the difficulty bomb
* Martin: If we push back to Jan. or Feb. then I'd push for including ProgPoW, if everything works out
* Afri: Makes sense to some degree if we delay Const., but adding new features also increase testing, ProgPoW is quite involved
* Hudson: Where are the clients in implementation?
    * Afri: We have an open PR, spec. is not ready yet
    * Martin: Pawel, Andrei and I have been hashing it out quite a bit with the authors
        * They are updating the specs
        * Meanwhile three implementations in cpp, go, and rust are in agreement
        * Remaining parts for rust is not algo. but changes to integrate it into ethhash, which should be the smaller of the tasks
* Lane: I'll do some math offline to check how much leeway we have before the difficulty bomb
    * H: If we have leeway until e.g. Feb or Mar then maybe ProgPoW is a possibility
    * Jacek: Isn't leeway for extraordinary situations?
    * Lane: I agree, we want a feature freeze/test freeze some months before the difficulty bomb starts to bite
    * What's the counterfactual? What would have to happen for this hardfork to occur in November?
        * M: Dimitry says tests are complete, all client devs pass tests, no issues found
* Hudson: "Greg Colvin approach": Does anyone feel like, "over my dead body" we postpone this?
    * Pawel
        * I propose one month after clients are deployed, before mainnet hard fork
        * Many people say two weeks but I prefer one month
        * When releases are ready, confident clients are ready
        * Confident tests are all written
    * Afri: I agree, four weeks is minimum time we need between release and hard fork
        * Manual tests need to be ready within two weeks
        * Tests integrated into clients within two weeks
        * Totally collides with DevCon
        * I'd probably die in this process
    * Eric: We (Pantheon) are looking good as far as these features go
        * Expecting a lot of activity right after DevCon
        * November timeframe is tight for us too
* Dimitry: testing update
    * Added new SSTORE tests
    * Been working on EXTCODEHASH tests, not implemented
    * Few more SSTORE tests I want to merge
    * Chain transition tests, blockchain tests remain
    * Fuzz test, translating corpus file into state tests - remain
    * H: How long until this is done? (Manual stuff only)
    * I was hoping to finish before DevCon
    * I travel to Prague next Monday, I have a lot of time to focus on tests, plan to finish next week
    * We need to stress the network a bit more, try to trigger some more issues
* Afri
    * Let's not rush this
    * Martin: Good that we did testnet HF and found an issue
* Dimitry: Would like to see us do the HF on a testnet and run it for half a year
    * Maybe not this HF but the next one
    * We could apply EIPs one by one on the testnet
* Hudson: This would be for the next hardfork
    * Istanbul, or ProgPoW, which could be its own HF
    * Lane: If we get good at this process, it gets streamlined, then maybe it wouldn't be such a big deal to HF more often
* Hudson
    * Sounds like we don't want to do this by end Nov, thinking more end Jan.
    * Puts a lot less stress on client teams
    * (There is consensus, no objections)
    * Earliest we have it is January
    * AllCoreDevs on Nov. 9, one week after DevCon
    * So we can discuss this very quickly after DevCon
    * Anybody opposed?
    * (Nope)
* Johnny Rhea:
    * We hired a fulltime dev to start working on exthereum
    * Should have some updates soon
    * Named Mirko (not Merkle, oh well)

# Attendees
* Paweł Bylica (EF/aleth)
* Jason Carver (EF/Python)
* Dmitrii (Harmony)
* Dominator008
* Eleazar Galano (Infura)
* Hudson Jameson (EF)
* Nick Johnson (EF/ENS)
* Eric Kellstrand
* Lasso
* Lane Rettig (Ewasm)
* Johnny Rhea (ConsenSys)
* Danny Ryan (EF/research)
* Peter Salanki
* Adam Schmideg
* Afri Schoeden (Parity)
* Jacek Sieka (Status/Nimbus)
* Bob Summerwill
* Martin Holst Swende
* Wei Tang (Parity)
