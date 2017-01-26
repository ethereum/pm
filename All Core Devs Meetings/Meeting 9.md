# All Core Devs: Meeting 9
## Time: 1/25/2017 14:00PM UTC
##[Audio of Meeting](https://youtu.be/ex51Gb3SVqo)

### Agenda:
  0. Should we set up a persistent meeting time? The first and third Friday of every month at 14:00 UTC maybe? Given enough notice, we can push these meetings back or forward a week due to major events that multiple core devs will be attending (such as Edcon Feb. 14th).
  1. Come to final agreement on [EIP 5/8](https://github.com/ethereum/EIPs/issues/8) [Facilitator: Christian]
  2. [EIP 196: Precompiles for elliptic curve point addition, elliptic curve scalar multiplication and pairing by @chriseth](https://github.com/ethereum/EIPs/issues/196). [Facilitator: Christian]
  3. Metropolis, upcoming ice age, and potential Metropolis EIPs. [Facilitator: Vitalik]
    - Abstraction
      - [EIP 86](https://github.com/ethereum/EIPs/issues/86) by @vbuterin
    - Putting block hashes and state roots into the state
      - [EIP 96](https://github.com/ethereum/EIPs/issues/96) by @vbuterin
    - Remove medstate from receipts
      - [EIP 98](https://github.com/ethereum/EIPs/issues/98) by @vbuterin
    - Uncle mining incentive fix
      - [EIP 100](https://github.com/ethereum/EIPs/issues/100) by @vbuterin
    - Bigint arithmetic
      - [EIP 101](https://github.com/ethereum/EIPs/issues/101) by @vbuterin
    - Cheap throw
      - [EIP 140](https://github.com/ethereum/EIPs/issues/140) by @nmushegian
    - Putting block hashes and state roots into the state
      - [EIP 166](https://github.com/ethereum/EIPs/issues/166) by @vbuterin
  4. [EIP 176: New general state tests](https://github.com/ethereum/EIPs/issues/176). [Facilitator: Martin S.]
  5. [EIP 116: STATIC_CALL](https://github.com/ethereum/EIPs/issues/140) [Facilitator: Christian]
  6. [EIP 141: EVM opcode: designated invalid instruction](https://github.com/ethereum/EIPs/issues/141). [Facilitator: Christian]
  7. [EIP 1 Update: New Changes to EIP Process](https://github.com/ethereum/EIPs/pull/183) by @Souptacular. [Facilitator: Hudson]

# Notes
## 1. Come to final agreement on EIP 5/8.
**Summary**:
This EIP has been discussed in previous meetings and received general consensus. Tentative consensus for acceptance pending official word from Parity.

## 2. EIP 196: Precompiles for elliptic curve point addition, elliptic curve scalar multiplication and pairing

Christian: I propose adding pre-compiles to enable zk-SNARKS on Ethereum. Although the research team tried to keep the precompiles flexible and have the ability to enable other curves, generally there are no generic ways to do that. I propose to implement precompiles for elliptic curve for ZCash. In particular, elliptic curve point addition, elliptic curve scalar multiplication, and a pairing function precompiles. Pairing function is complicated that takes 2 points on 2 different elliptic curves and maps them onto a finite field. We could run into representative problems. There is not a unique way to run into elements of these sets. Instead of implementing the pairing function, we can implement a pairing checker which will return true/false depending on if the result is the identity or not in the target group. This will greatly reduce complexity. Todo: Decide on an encoding for points for these 2 elliptic curves and assign gas costs.
Vitalik: If we want to make the sum of the precompiles slighty more generic, we can make the addition and multiplication support any curves that have have any b param. So the b param will be 0, but the b can be anything. This is also is nice because it also covers the curve we use already for ECC recover. It might even be 0 complexity.
Christian: So you're saying you can make the elliptic curve operations more generic, but not the pairings?
Vitalik: I'll need to check. One thing worth adding is that you can view the implementation in Rust.
Chrisitan: There are implementations in Rust and C++.
Christian: Go team, what do you think?
Jeff: We have a Go implementation for ECC recover. Only C++ dependency that we have are the recovery functions, but other than that we would need to implement the precompile ourselves. We can use a reference from another language and get help from others. We aren't too keen on C++ dependencies because it breaks cross-compellability.
Christian: Makes sense.
Vitalik: We can use Python as reference implementation for those who don't have an implementation if we'd like.
Jan: We can put wrappers around it (for Ruby) so we are good.
Paritiy team: We are good.
Java team: Just had a release so only recently diving in, but it should work.

**Conclusion**:
There is general consensus around this, but the details need to be fleshed out in an EIP that Christian is working on. Should be discussed next meeting.

## 3. Metropolis, upcoming ice age, and potential Metropolis EIPs.
### EIP 86: Abstraction
#### 2 Components
      1. If you send a TX whose signature is 0 it is assumed to be sent from the 0 address.
      2. Rule change for how to generate address for contracts. One people seem most happy with is creating a new CREATE OPCODE for the new rules and find a way to safely deprecate the old one.
      
Vitalik: We have discussed this several times in previous meetings. Basically allows a new transaction type that has a sender of 0 and has 2 features that modifies the scheme used to determine the address of a contract. Move away from sender and nonce to sender and code. I recall people generally finding the idea acceptable. Potential issue brought up before: What if ther is an exsisting contract that calls CREATE in such a way that it tries to create a contract with such a code many times. We don't want to break existing things unless we have to. Potential solutions are 1. Have a very compliocated scheme that detects for that and jumps to  a different address, 2. (Simpler) Create a new CREATE OPCODE. I recall the opinion being towards option 2 because it would be cleaner.
Question from chat: Instead of an opcode can we have a precompile for creation?
Vitalik: That is worth considering and am happy to take that discussion offline. If you have a CREATE precompile without having a CREATE OPCODE, you have a precompile that theoretically not be implemented in VM code and adds complexity. Best argument of having just an OPCODE for the time being.

### EIP 96: Putting block hashes and state roots into the state
This is part of the abstraction portion of Metropolis and is generally agreed upon.

### EIP 98: Remove medstate from receipts
Removes intermediate state roots. Will interfere with light client according to Jeff. Pros and cons are going to be discussed offline with Jeff and others. Feel free to join.

### EIP 100: Uncle mining incentive fix
In response to bug report by Sergio Lermer that points out an incentive flaw that encourages large mining pools to mine uncles. Solution: Instead of targeting a fixed time between block # increments, we would target a fixed time between blocks including uncles + a simple formula change (1 line code change).

### EIP 101: Bigint arithmetic
Vitalik: The reason is that we can support various bigint crypto, like RSA. If we are doing this I think modular exponentiation is enough, so we don't need to bother with multiplication and addition. Reasoning is that of the 3, exponentiation is the one that needs optimizations. Add and mult can already be done cheaply.

### EIP 140: Cheap throw
Jeff: Seems dangerous. Reversing state happens at no cost.
Vitalik: You would lose the gas you spent, but would get the rest as a refund.
Christian: Don't we already have the stipulation that we have to implement it at no cost because you can have a throw after running out of gas?
All: Yeah.
Chrstian: A danger with this is that we can currently do a sloppy gas counting when we hit OOG. We can look at this offline.

**Summary**:
General support for this. Caveat: If we run into a time crunch with homestead, we can push this to Serenity

### Metropolis timing and roadmap discussion
Hudson: I remember previously discussing phases for either metropolis or serenity or both rather than one big set of changes.
Vitalik: The time I proposed breaking up Metro into Pt 1. and Pt 2. is when we were fixing the DoS issues and wanted to potentially add a few EIPs to the hard fork. At this point 1 step for metro is sufficient.

Approximate ice age start according to Vitalik:
  - Around March 25th (3 months) - Block time is 15.2 sec.
  - Around July 25th (6 months) - Block time is 29.7 sec.

Hudson: [In Metropolis folder of ethereum/pm repo](https://github.com/ethereum/pm/issues/4) we can store any formal metro stuff. We created an issue here () to start keeping up with metro updates.
Hudson: Between now and next core dev meeting we will try to assign rough time limits to implement/test the EIPS. Using that data we can make a list of MVP EIPs for metro and then add others if we have time.
Vitalik: Once we get informal consensus on EIPs, go ahead and start implementing ASAP.

## 4. EIP 176: New general state tests
Support for this, let's move forward. Jeff has some suggestions and will comment on the EIP. Next core dev meeting we will bring this up again and decide to accept it or not.

## 5. EIP 116: STATIC_CALL
New opcodes similar to CALL but with restrictions.
- no state modifications (static call)
- no state reads either (pure call)
  (Vitalik: prefer CALLBALACKBOX)
- other kinds of restrictions?  need to explore possible combinations

Alternative to an additional opcode(s), consolidate *CALL into [INTERRUPT](https://github.com/ethereum/EIPs/wiki/EIP-%3F%3F%3F:-merge-opcodes-CALL-CALLCODE-DELEGATECALL-and-rename-to-INT), taking flags as arguments to change behavior.However, behavior changing flags make static analysis more difficult.

More discussion on the issue: https://github.com/ethereum/EIPs/issues/116
Will be on agenda in next core dev call.

## 6. EIP 141: EVM opcode: designated invalid instruction
Solidity would like to have different 'throw' behaviors.  One for 'throw' the other for overflow etc. Asking group for consensus on these changes and designate 0xfe or 0xef. 

Consensus reached to designate 0xfe and keep it invalid.

## 7. EIP 1 Update: New EIP processes

- Template: Similar to current.
- Process:
  - First open an issue (can be one line or full PR-style), discuss freely
  - Then make a PR for formal submission of draft EIP.

Should be implemented in the upcoming weeks.

Full details at https://github.com/ethereum/EIPs/pull/183.

## Attendance

Alex Beregszaszi (Solidity), Arkadiy Paronyan (Parity), Alex Van de Sande (Mist/Ethereum Wallet), Anton Nashatyrev (ethereumJ), Casey Detrio (Volunteer), Christian Reitwiessner (cpp-ethereum), Dimitry Khokhlov (cpp-ethereum), Greg Colvin (EVM), Hudson Jameson (Ethereum Foundation), Jan Xie (ruby-ethereum & pyethereum), Jeffrey Wilcke (geth), Kumavis (MetaMask), Roman Mandeleil (ethereumJ), Martin Becze (Research/EthereumJS), Martin Holst Swende (security), Nick Johnson (geth/SWARM), Vitalik Buterin (Research & pyethereum), Yoichi Hirai (EVM)
