# Ethereum Core Devs Meeting 48 Notes
### Meeting Date/Time: Fri, October 12, 2018 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/59)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=lz5CcpnQ1_s)

# Agenda

1. Testing
2. Client Updates
3. Research Updates
4. [Constantinople](https://github.com/ethereum/pm/issues/53)
5. ProgPoW

Call starts at [[5:33](https://youtu.be/lz5CcpnQ1_s?t=333)]

# Testing update
* Martin update
    * Tests not yet stabilized, still activity in generating the tests
    * Earlier today we found a consensus issue in the cpp-ethereum engine, this has been fixed, waiting for tests to be regenerated
    * Can't speak to coverage of tests
* Dimitry update
    * Getting reports of failing tests from different developers, we are fixing these issues, tests already regenerated and merged
    * Hope we find all consensus issues during this test period
    * But extcodehash tests and some around storage, blockchain transition tests still in dev
    * Difficulty formula tests merged in past week, see `basictests/difficulty-constantinople-json`
* Martin: Fuzz testing framework running for a couple of weeks, has run millions of tests, some false positives, found one consensus issue but it cannot be triggered on mainnet since it's due to behavior of non-existing precompiles
* Hudson: Have you been getting help with testing or do you still need help?
    * D: No help developing tests in JSON format, Jared helped a bit

# Client updates
* Parity (Afri)
    * Did Constantinople releases today: 2.0.7, 2.1.2
    * Prepared for Ropsten, Kovan HF
* Geth (Peter)
    * We did a release Monday or Tuesday which enabled all EIPs for Ropsten HF
* Trinity (Piper)
    * Working on sync performance, getting sync time down to a reasonable level
    * Have made a lot of progress but still a lot left to do
* EthereumJ (Dmitrii)
    * Published release just now, Constantinople on Ropsten
    * Not passing all tests, I hope no consensus issues
* Aleth (Pawel)
    * Released v1.4, stable for some time
    * Mostly an effort to have stable releases from time to time
    * Not fully Constantinople-compatible
    * But master branch is and we have one node running cpp on Ropsten
    * Switched to parity's network monitor, so it should be on the list
    * This is the only node that will participate in the Ropsten HF
* Nimbus (Jacek)
    * Continuing to work on sync and getting general state tests to pass, making steady progress
    * ETH2 beacon chain, work being done on test format, if you're interested, check beaconchain project on ethereum, there are open issues
    * Looking into platforms, making sure we can compile on ARM and others
* Pantheon (Meredith)
    * Implemented all Constantinople EIPs
* TurboGeth (not present)
* EthereumJS (not present, left comment)
    * Making good progress, have substantial parts of all EIPs implemented
    * Merging SSTORE implementation
    * Confident we can do Constantinople ready release of VM within 1-2 weeks
* Mana (Andrew)
    * Updated all EIPs, working on syncing Ropsten, began last week, at around block 300k
    * Mainnet, we are at 1.7M
* Nethermind (not present)
* Exthereum (not present)
* Ewasm
    * Lane
        * Lots of work on benchmarking, will report results at some point
        * Testnet running and mostly stable, will launch publicly at DevCon
        * Working on documentation
    * Pawel
        * Close to release EVMC v6, need to update go bindings
        * Don't want to modify more for next month
* Hudson: Every client is totally Constantinople-compatible
    * Except: Trinity, ethereumJS, exthereum
    * All major clients have updated CREATE2 specs

# Research updates
* Danny update
    * Justin working on VDF feasibility study, effort to create strong, unbiasable randomness
    * Filecoin has agreed to split the cost of the next chunk of the feasibility study which involves circuit design, they are interested in it for the same reason
    * Within next couple months we'll hopefully have an idea if this is going to work for the random beacon
    * Randao serves our purposes for most uses, will likely move fwd with this and can add VDF as hardening in future
    * Been cleaning up, expanding ETH 2.0 spec, lots of development going on
    * You guys all have lots of valuable insights to add to this process
    * There is an ETH2.0 specs repo, eth2.0-pm, please take a look, don't hesitate to reach out to me to talk about what's going on and where you can get involved

# Constantinople, Ropsten HF
* [Progress tracker](https://github.com/ethereum/pm/issues/53)
* Hudson
    * Ropsten HF will happen around Sunday or Monday
    * We'll have folks online
    * If anything bad happens we'll get together
    * Mainnet HF will happen after DevCon
    * In about two weeks, first folks will be arriving in Prague for DevCon, should we skip the next meeting?
    * (No complaints, consensus achieved, we'll do the next meeting in four weeks)
* Martin
    * Everything is implemented in all clients
    * If we find no consensus errors in testing or on the testnet, when should we aim to do the HF?
* Afri: mid-November might be a bit rushed
    * Maybe end of November?
* Piper: second end of November
* Hudson: How much time do we need after setting the block number, before the fork?
    * About a month
    * When should we decide the block number?
* Piper: Can announce it outside of this call, confirm on 11/9 call
* Afri: Should we have a quick call in ~one week, just evaluate the fork on Ropsten, see if it's going well, announce a preliminary block number
    * If something goes wrong, we can put it on hold until January
* Martin: How do we avoid the fiasco of the last HF?
* Peter: We discussed at the last DevCon, whether we need a bailout mechanism for the HF
* Piper: Let's take this offline and see if we can settle on something before the meeting next Friday
* Hudson: Having a smart contract that the clients can ping to see if the fork is still on - is this the idea?
* Dimitry: Clone existing mainnet, where every client repeats existing mainnet tx as if already running on Constantinople
* Martin: We could do it but no one would be using many of the changes, bomb delay not noticable, etc., would be useful to see gas changes
* Afri: Check out https://ropsten-stats.parity.io/, WS secret same as ethstats

# ProgPoW
* Martin: Andrei, Pawel and I have been in touch w ProgPoW folks
    * Have ironed out some kinks
    * Some problems with the EIP
* Pawel: Some big gaps in EIP spec
    * Practically impossible to implement it based on the EIP itself
    * Had to reach out for source code mostly done by ProgPoW team
    * Final version found somewhere in one of the implementations, we discussed the differences
    * C++/Go implementation on the same page
    * EIP is in bad shape
    * There are some very small improvements we can make
    * Most important part is we have two reference implementations but no proper spec
    * I don't like this situation as I don't want people to have to read the C or Go code to figure out how to implement it
    * The team did some work on improving EIP and answering questions but not so much in public
    * We are in touch with them, we can ask them questions directly and usually get some answers
    * This helped me finish implementation that produced same results - just yesterday
* Martin
    * Some changes need to be made, the original idea is that it has internal epoch of 50 blocks
    * When translated into ethereum it uses the same epoch as ethash which is 30k blocks, which leads to some problems
    * Needs an update of protocols between the miners, the getwork function
    * Other than that, the general idea is to launch a testnet for it ASAP
* Hudson: So we want the EIP updated to include more detail
    * Have we communicated this to them?
    * Pawel: Yes. As of today they still plan to update the EIP with what we discussed privately, to fill the gaps.

* Hudson
    * Skipping next call
    * Constantinople special call in a week
    * Won't shift overall meeting schedule

# Attendees
* Meredith Baxter (ConsenSys/PegaSys/Pantheon)
* Paweł Bylica (EF/aleth)
* Jason Carver (EF/python/trinity)
* Dmitry (Harmony)
* Daniel Ellison (Consensys/LLL)
* Matthew English
* Andrew Gross (Mana)
* Fredrik Harrysson (Parity)
* Hudson Jameson (EF)
* Mikhail Kalanin (EthereumJ)
* Eric Kellstrand
* Dimitry Khokhlov (EF/testing)
* Piper Merriam (EF/python/trinity)
* Lane Rettig (Ewasm)
* Danny Ryan (EF/research)
* Afri Schoeden (Parity)
* Jacek Sieka (Status/Nimbus)
* Martin Holst Swende (EF/geth/security)
* Péter Szilágyi (EF/geth)
