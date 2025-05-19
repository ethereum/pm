# Ethereum 2.0 Implementers Call 1 Notes
### Meeting Date/Time: Thu, Aug 16, 2018 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/2)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=8F9NPGIv9vI)

# Agenda
1. Client Updates
2. Research Updates
3. Wire Protocol
4. Message Serialization
5. Bootstrapping initial validator set
6. Sharding meetup pre-devcon
7. Shuffling algorithm
8. Testing
9. Last remarks



# Client Updates
* EF beacon_chain (Danny)
    * finished v2.1 spec
    * Editing spec as bugs arose
    * Hsiao-Wei conducting review
    * Still need to implement forkchoice
* Prysm (Terence)
    * Deprecated sharding manager contract
    * Beacon node GRPC service along with GRPC Client -- communicating effectively
    * proposer package interacts with chain via RPC to determine if/when proposer/attester
    * beacon node simulates block and cycle transition
    * aligning codebase to v2.1 spec
    * New Prysmatic [Discord server](https://discord.gg/KSA7rPr)
    * Fork choice coming up
* Lighthouse (Paul)
    * [sandbox](https://github.com/sigp/shuffling_sandbox) to mess around with shuffling algorithm (speed/output)
    * building out ancillary components (database/data layer)
* Harmony (Mikhail)
    * Working through proposer logic
    * following spec and focussing on simplicity
* Pegasys (Ben)
    * Team building
    * Olivier been at VDF workshop
    * two new hires
    * Research been focussing on new version of casper. beginning to work on
      new version over next two weeks (Nicolas)
* Nimbus (Mamy)
    * message serialization
        * schema to simple serialize and assessing implementation in nim
    * [BLS implementation](https://github.com/status-im/nim-milagro-crypto/blob/master/src/scheme1.nim) with milagro
        * [Post with tips and pitfalls when implementing BLS](https://ethresear.ch/t/pragmatic-signature-aggregation-with-bls/2105/29)
    * eth1.0 progress -- syncing pow early blocks
* eWASM (Lane)
    * No sharding progress currently
    * tooling and deployment in rust and assembly script
    * work on execution layer for sharding coming up
* Lodestar (Mikerah)
    * Implementing state transition functions
    * looking into a pure JS BLS implementation
    * Beginning to implement gossip sub in JS
    * Doing some independent RNG research

# Research Updates
* Sharding p2p poc (Kevin)
    * nodes can join, leave, broadcast messages, and sync with other nodes
    * docker image available
    * working on open tracing
    * package management issues with p2p. reported and fixed!
    * added documentation to README
    * refactoring and restructuring for modularity
* Network simulations (Jannik)
    * Goal: compare different gossip and discovery protocols
    * Simulation setup
        * Using [OMNet](https://www.omnetpp.org/)
        * all simulations on single machine so not entirely realistic but still
          useful
        * can handle simulations up to 100k nodes
    * epi-sub (proposed successor to gossip sub)
        * implemented in simulation
        * number of hops is very large for propogation (20-40 hops for 5k-20k nodes)
        * too large. Should not use in current state
        * Danny: why taking so many hops?
        * Jannik: protocol trades efficiency for propogation time. Takes a lot
          of hops but takes very few messages
    * gossip sub
        * beginning to model the same metrics
* WhiteBlock (Zak)
    * Have framework that emulates network behavior/activity.
        * functionally replicates behavior instead of simulation
        * opened [issue in POC repo](https://github.com/ethresearch/sharding-p2p-poc/issues/43) to present capabilities and testing methodology.
        * Please provide feedback on what types of tests would be most useful
    * This week
        * Got POC running, fixed a couple of issues
        * Got POC running on OSX
    * Examples of what whiteblock can test
        * ability for validators to subscribe to topics in certain period of time
        * simulate number of nodes, latency between nodes, what is maximum
          amount of latency that node can tolerate performance degrades
        * security implications of latency in network
        * adding/removing nodes
        * introducing high volume of nodes at once
        * observe partition tolerance
        * stress tests
    * Jannik: We should test various implementations in same network. Is that possible?
    * Zak: Yes, definitely
    * Will be useful when we have actual clients to run too instead of POC
* v2.1 main changes in last couple of weeks (Vitalik)
    * fairly small modifications
* RNG/VDF (Danny)
    * waiting on detailed hardware analysis to better understand VDFs in the
      RNG design
    * report hopefully in 3-4 weeks

# Wire Protocol
* Paul
    * pushing packets around and considering wire protocol
    * easiest might be copy eth1.0, but want to start discussing
* Preston
    * Prysmatic currently just using protocol buffers for time being when just
      one client and early in development
    * defined specific messages for each topic for gossip/flood sub
* Danny: are there issues with the eth1.0 wire protocol for our purposes?
* Mikhail: Do not currently see any issues with eth1.0 wire protocol
* Paul: will need some changes like removing difficulty from protocl
* Vitalik
    * need to consider denial of service resistance
    * pow does this fairly easy
    * not as trivial in pos
    * dos: sending malformed blocks formatted in such a way that wastes target's time
    * slightly worried because of big BLS signatures
* Danny
    * dfinity using ZK proofs to prove part of validator set without revealing which validator
    * allows for privilege communication between validators
    * does this sort of solution resist DOS
* Alexey
    * if proof can be replicated, defeats purpose
* Vitalik
    * idea is to weave proof into set of messages you are making
    * scheme: make a proof with a merkle root. When make a message, reveal a
      root for up to N messages
    * alternative: prove that this other public key is related to an unknown
      validator public key so this new public key can be used for messages
* Jacek: would it be enough to do this per connection at p2p layer?
* Vitalik: Probably
* Danny: Probably worth examining a bit deeper

* Paul: will start poking through prysmatic stuff and documenting research to
  continue conversation

# Message Serialization
* Paul
    * planning on running comparisons between the formats -- time/size/etc
    * liking the schemes that dont require any decoding/encoding between
      network messages and database layer
    * in favor of simple serialize (SSZ) for consensus layer stuff
* Vitalik
    * I made two protocols both named SSZ. Which do you mean?
* Paul: the ethresearch one


# Bootstrapping initial validator set
* Danny
    * What method should we use to get our initial validator set in the beacon
      chain
    * a bit of chicken and egg problem. validators in beacon chain are supposed
      to validate incoming registrations from new validators, but no validators
      will exist to do the validation at the beginning
* Terence
    * currently in Prysm, just initial a bunch of validators upon chain
      creation
    * looking into config file for this
* Danny: So in practice, that's some sort of initial inshrined validator set
* Alexey: Another approach is to use testnet to seed genesis block
* Vitalik
    * Ethereum created genesis block with a public python script anyone could
      run to scan the bitcoin blockchain to assess who participated in the sale
      and assign them eth
    * This approach is totally fine
* Danny
    * Idea would be to have registration contract in which validators can burn ETH and set their params (pubkey, withdrawal addr, etc), contract broadcasts this data via receipts, have open for some amount of time, then run script
    * would have start and end date for initial registration (or rather block height)
    * This is a tentatively reasonable approach
    * in terms of development, just consider the genesis to have an initial
      validator set

# Sharding meetup pre-devcon
* Danny: Status has some space for hack-a-thon. might be space there
* Jacek
    * best date would be Friday 26th
    * How much time we need?
* Danny
    * I lean toward a day and not do multiple days
* Lane
    * what is the purpose of this meetup? will help decide time
* Danny
    * Long form version of this call.
    * catch everyone up, meet everyone, facilitate collaboration on the finer
      details
    * updates, research Q/A, and some specific issues
* Jacek
    * Eth magicians meeting up around then too
    * Knowledge sharing would be useful. presentations on people's research
      would be good

# Shuffling algorithm
* Paul
    * Module bias and extra iteration in shuffling algorithm -- [issue 57](https://github.com/ethereum/beacon_chain/issues/57)
    * made a [sandbox](https://github.com/sigp/shuffling_sandbox) to play with shuffling algorithms
* Vitalik
    * doesn't alg already do filtering for modulo bias?
* Paul
    * yes, but filters out on entire list size, not on remaining amount
* Vitalik
    * looks like a type/bug
* Paul
    * also randmax needs to be dropped into loop
    * changes based on remaining
* Vitalik
    * you're right
    * updated code in v2.1 spec
* Paul
    * made a reference implementation in the sandbox that is a bit slower but
      separates out the different parts for understanding
    * shuffling sandbox outputs shuffled array given a seed, can use the sample
      outputs for testing in different clients

# Testing
* Vitalik
    * have we talked about unified testing yet?
* Danny: not really yet
* Vitalik
    * There's that [proposed testing lang](https://notes.ethereum.org/6ozACHyKR9i86vfkt086Ow#) spec I made a few days ago
    * way to write tests quickly and have various clients validate them
    * review the doc and let's assess if that approach makes sense
* Danny
    * it's a testing lang that allows us to specify the creation of blocks, the
      attestation of blocks, and assess the forkchoice and the other components
      of the chain

# Last remarks
* Mikhail: can use a pow block hash at some pre decided upon height in the
  future as the seed of the shuffling in the initial validator set
* Carl: Can just use RANDAO commitments from initial validator set
* Danny: yes, could use XOR of those commitments. Both approaches seem reasonable. RANDAO is very likely but RNG is still a little up in the air

# Links shared during meeting
* [New Prysmatic Discord server](https://discord.gg/KSA7rPr)
* [ethresearch post](https://ethresear.ch/t/pragmatic-signature-aggregation-with-bls/2105/29) with tips and pitfalls when implementing BLS
* [BLS implementation in nim](https://github.com/status-im/nim-milagro-crypto/blob/master/src/scheme1.nim) using milagro
* [OMNet](https://www.omnetpp.org/)
* [whiteblock methodology issue in POC repo](https://github.com/ethresearch/sharding-p2p-poc/issues/43)
* [shuffing algorithm issue](https://github.com/ethereum/beacon_chain/issues/57) on github
* [shuffling sandbox](https://github.com/sigp/shuffling_sandbox)
* [proposed beacon chain testing lang](https://notes.ethereum.org/6ozACHyKR9i86vfkt086Ow#)


# Attendees
* Lang Rettig (EF/eWASM)
* Danny Ryan (EF/Research)
* Mikhail Kalinin (Harmony)
* Mikerah (Lodestar/ChainSafeSystems)
* Chih Cheng Liang (EF/Research)
* Kevin Chia (EF/Research)
* Hsiao-Wei Wang (EF/Research)
* Jannik Luhn (Brainbot/Research)
* Zak (WhiteBlock)
* Paul Hauner (Lighthouse/Sigma Prime)
* Preston Van Loon (Prysmatic)
* Terence (Prysmatic)
* Mamy Ratsimbazafy (Status)
* Alexey Akhunov (turbo-geth)
* Carl Beekhuizen (Decentralized staking pools)
* Ben Edgington (Pegasys)
* Vitalik Buterin (EF/Research)
* Jacek Sieka (Status)
* Nicolas Liochon (Pegasys)
* Nicholas Lin (EF/Research)
* Jarrad Hope (Status)
* Boris Petrov (Status)
