# Devcon SEA History Expiry and Portal Network session

**Summary:** Discussion of urgent need for history expiry, and how Portal network supports it, focusing on execution clients plans and needs going forward.

**Facilitator:** [Jason Carver](https://github.com/carver/)

**Note Taker:** [Nick Gheorghita](https://github.com/njgheorghita) 

**Pre-Reads:** 

- https://github.com/ethereum/portal-network-specs/blob/master/README.md
    - Our main entry point for the specifications that make up the Portal Network.
- https://github.com/ethereum/portal-network-specs/blob/master/history/history-network.md
    - The specific specification for the history network which is the component of Portal that is most relevant for 4444s
- https://eips.ethereum.org/EIPS/eip-4444

Deeper dives into how Portal works

- https://ethportal.net/
    - The main Portal website.
- https://github.com/ethereum/portal-network-specs/blob/master/portal-wire-protocol.md
    - The "Portal Wire Protocol" is the generic P2P framework that all of Portal is built upon. This is a good read for those planning to implement a Portal client or to do any kind of deep integration with a portal client.
- https://ethportal.net/concepts/execution-clients
    - Explanation of what a Portal based execution client looks like
- https://github.com/ethereum/portal-network-specs/tree/master/jsonrpc
    - The Portal network specific JSON-RPC API


## Agenda 


- Current Context: 2TB storage not sufficient, soon
- Discuss simplest solutions:
    - Do nothing
    - Drop a fixed-length hunk of history
- What are the challenges of dropping history?
- What are some solutions?
- Among the solutions: Portal
    - Conceptual review
    - Current status
- Status updates from clients on dropping history, and solutions
    - Do you want to drop history in your client.  Why so/not?
    - If so:
        - what will your client do for JSON-RPC requests for evicted history?
        - what will your client do for "syncing" the chain history?
    - For those expecting to use Portal, what is your integration plan?
        - Write your own client?
        - Integrate an existing client?
        - Run existing client in separate process?
- Portal integration support
- Next Steps
    - When are we planning to drop history?
        - Who is leading this effort
        - Who are the contact points on each team
        - How are we coordinating progress
        - Do we need a coordinated network upgrade
    - What needs to happen between now and go-live?
    - When does work need to start?
    - Should we do an interop or otherwise in-person event?

*The default structure for breakout session is a **10-15m opening presentation by the facilitator, followed by a ~60m open session**, and ~15m to wrap up and move to the next session.*

## Notes & Action Items 

**Session Notes**

# Round 1 (11/10)

tl;dr:
Execution clients all agree that history expiry needs to happen. Some want an implemented, decentralized solution before setting a hard date, some want to set a hard date before agreeing upon a solution (otherwise it will not get prioritized).

- HD usage is crossing 2tb threshold for running an execution client in 6months
- History expiry now feels urgent... how do we deal with it expediently?

Session goal:
Define a date when clients will no longer be **REQUIRED** to respond to devp2p / jsonrpc requests for block bodies / receipts before the merge.

What is expiry?
- Not serving old block bodies, & receipts over devp2p network
	- headers are special, so start with dropping bodies & receipts
	- 4444s defines the threshold as dropping everything before the past year, but it doesn't define what a client must do when old data is requested. so let's figure it out
	- clients of course can choose to still store this data if they want
	
What would stop us from dropping pre-merge today?
	- reth: only has full sync, needs to access this data over devp2p
	- latencies concerned with retrieving data that you don't have locally
		- to fulfill rpc calls for old data (and also getBlock / getTransactionReceipts)
		- filtering logs
	- block replay with old state
	- concerns about permanent loss of the data...
		- it's safe to treat permanent loss as a non-real threat.
	- consensus clients require access to deposit contract data / logs ( but there's already a solution for this on consensus sides which most clients already support)
	- how do clients maintain network health / aka client's health in participating if not all of them implement it the same way - we want heterogeneous solutions to avoid this

Does ERA1 already solve this?
	- can help with full sync
	- era1 format allows random access lookup within a file
	- helps with permanent loss... we can definitely preserve the history somewhere with this solution
	- it's not great with latency.. over rpc. but is this really an important use case? aka how many users are really requesting this data over rpc?
	- how do we distribute era1 files?
		- we don't define this and leave it up to clients to choose what's best for them
		- torrents / centralized servers

Why choose the merge as the border where we start with dropping old history?
	- premerge era1 file is 450gbs so that's our immediate savings 
		- even though it's an easy point to talk about... the real distinction here is between current & old data... so the border is arbitrary
		- counter: there is a difference in data format over fork borders
		- post-merge we can use consensus accumulators to verify era files... so maybe the merge makes sense as a border
	- there is a large variance in size of era files (~8200 blocks) based on height... 0 - a few kbs, merge - a few gbs

*STRAW POLL #1*

Question:
~ can we allow clients not to be required to respond with pre-merge bodies / receipts? ~
- not defining a solution, just that clients can drop data, aka just that clients **CAN** refuse rpc requests & devp2p for this data
- most people agree
- peter disagrees
	- where do we store the data & how do you access this fast? distribution is the problem.
	- what if the server gets overloaded? everyone syncs at same time
	- objects to era as the solution, but not to dropping pre-merge data
- consensus side uses centralized servers a lot, so is it a valid concern? why do we care about it so much on execution
- reth doesn't want to be the only one who doesn't drop data
	- means they can only rely on other reth nodes for sync, and this will be very slow

comment: we can't require the solution to be perfect, aka hold solving the problem hostage with an imperfect solution... we need to find a minimum compromise by defining the problem and agreeing to a drop date.

peter: i'm willing to sacrifice reth.

Portal Network
- a decentralized / p2p solution for serving this data
- can we slowly transition to the future by using portal without any "drastic" protocol changes? aka prove that clients can use portal to serve uses without drastic changes
- aka .. it shouldn't be allowed to not serve these requests. they must use a solution in the meantime and battle-test them.

Do we need set a hard date?
- Yes: otherwise it won't be prioritized and it will never get done
- No: we can use market incentives. if a client implements this, allowing users to free disk, then they will become more popular
- ok but honestly, do stakers really care about a tb or 2? Is the growth of ethereum truly threatening to kill stakers ability to run a node...
- Reth isn't trying to block people. They are on board with the goal of history expiry. But if forced to implement a solution in 6 months, they would probably do era1 torrent/centralized server
- Geth: they have era1 implemented. they have a lot of internal mechanisms that assume history is available.. so it's not so simple just to yank it out.. but they expect history needs to be dropped anyway, it's on their roadmap, but they don't feel ready in 6months

comment:  it's not about the date, it's about a p2p solution... if clients don't have a p2p solution, they shouldn't be dropping the history. era1 is not a sufficient solution to enable dropping old history, we need a decentralized solution

Portal Network
- collection of distinct, p2p networks, consuming / serving this data (among other types)
- chain history network is the relevant network for this convo
- API (chain history)
	- block hash -> header
	- block hash -> body (txs, uncles, withdrawals)
	- block hash -> receipts
	- block number -> header
- who's running these nodes?
	- well execution clients eventually...
	- users for the wallet use case
- it is running today. live. with active monitoring & 100% reliability for pre-merge data
- portal network goals:
	- we want to see how far we can get without syncing the chain ever
	- build a full execution client that is not dependent on devp2p
	- wallet provider

New Portal API requests?
- block lookups by range not by a single block-hash
	- not today, but the portal network is very flexible and this can be easily implemented
- Portal network shouldn't be thought of as a vendor of data to serve execution clients, it needs to be implemented and the teams need to collaborate together to evolve the protocol & message types to support the various needs
- the initial portal implementation is a minor lift, but adding new types to the network is very easy. once implemented, the protocol can adapt to serve various needs down the road
	- interaction with the client teams is important to understand these needs

FINAL VOTE
- Are client teams willing to commit to dropping pre-merge, receipts & bodies, in 6 months? Also allowing peers to not respond to requests for that data?

GETH - OK but afraid, bc of the implications. what are we breaking?
NETHERMIND - YES
BESU - YES
RETH - ?s - it will slow down their sync
ERIGON - Not present
JS - YES
NETHERMIND - 

![](https://storage.googleapis.com/ethereum-hackmd/upload_6e0202645af9cf28eb51179af21751e6.jpeg)

# ROUND 2 (11/11)

# ROUND 2

tl;dr: AGREEMENT HAS BEEN REACHED!

**DROP PRE-MERGE BODIES & RECEIPTS by MAY 1**
- all clients on devp2p network can drop this from their db, and are not expected to respond to requests for this data
- you are not required to / but you are allowed to, aka clients can change nothing and still serve historical data
- keep on storing headers, it's not a large footprint

Client teams likely solutions...
- geth leaning towards portal / with fallback
- reth leaning towards s3 & 7801
- erigon: 7801 & torrents
- besu: short term 7801 long term portal
- nethermind: portal & 7801
- nimbus: portal 
- js: portal

How will clients retrieve this data?
- it's up to each client team, they can choose their own path forward
- portal is the leading p2p solution, but it's not necessary for clients to adopt
- torrents / static era files are the other approach

Can we make this proposal/agreement better?
- Q: Should we just jump to 4444s (aka a rolling window for dropping history) & not do pre-merge boundary? 
- A: this level of agreement is not going to happen today

What is our north star here? Where do we eventually want to end up?
- rolling window for dropping history at the head of the chain
	- or should we just define a new range of data to drop every year, rather than implementing the rolling window, which does involve a significant engineering effort
- does this include dropping headers?
	- portal will serve these regardless
	- with portal, its not efficient to sync the chain, so it's probably better to leave headers in devp2p
- portal has plans to support full sync over network

CONCERNS...
- pre-merge cutoff has a very secure recovery mechanism... and we don't yet have the same level of security for recovery with the rolling window

Standardizing / hardening post-merge data recovery...
Client teams - in the next 6 months - as they implement dropping pre-merge, need to focus on addressing this concern
- prove era files - their availability, how many sources are there
- portal monitoring
- erigon torrents
- 7801
- post merge era files don't have receipts, which is a problem

Are cls ok with dropping rolling history ( because of deposit contract logs )? (probably)

The rolling window should be...
33k epochs
~ 1 million blocks
- so that els & cls can share a database

Would it be better to use existing big data storage formats over era?
- era has some custom benefits for proving that is actually a benefit, and it's already implemented and used

Era format details
-  era1 is pre-merge
- era is nimbus' format for exporting history
- era format is really for importing/exporting data and not to be used as data storage format

Solveable problems that we need to solve
- adding new data
- evenly distributing the data
- sharding the data
- random access of the data
- proveability of the data

Solutions include: 
- 7801 
- torrents 
- portal

Teams are free and encouraged to work on implementing whatever solutions they think are the most promising.

7801 has been updated
- dictates what data clients can serve in past and future
- devp2p is maybe not the best networking layer for this problem. Retrieving data might be tough, if you don't have a peer with the target data, so you might not be able to find a peer with the data when you need it.

Lookup by block range is important - really important. portal team is currently working on support for this.

Sync might actually become better w/ portal because of the networking layer allows for better parallelization / maintaining a large pool of peers. goodbye devp2p?


**Action Items**

- Follow-up session, tomorrow
