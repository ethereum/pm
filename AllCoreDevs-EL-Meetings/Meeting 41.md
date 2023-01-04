# Ethereum Core Devs Meeting 41 Notes
### Meeting Date/Time: Fri, June 29, 2018 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/46)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=HpCMguxraBA)

# Agenda

* Testing
* Research Updates
* Client Updates
* Constantinople hard fork timing and what to include (continuing conversation from last call).
    a. EIP 145: Bitwise shifting instructions in EVM: pretty well-formed, but not 100% implemented or tested.
    b. EIP 210: Blockhash refactoring.
    c. EIP859: account abstraction.
    d. EIP 1052: EXTCODEHASH Opcode.
    e. EIP 1087: Net gas metering for SSTORE operations.
    f. EIP 1014: Skinny CREATE2.

# Notes

Video starts at [[4:47](https://youtu.be/HpCMguxraBA?t=4m47s)].

## Testing

* Dimitry is still working on RPC methods, still wants help with this
* Gave an update at ECDC
* Pushing for more clients to look at an issue on Github that outlines further required RPC methods, more clients to further standardize the testing

## Research updates

* Live from ECDC: watch [separate livestream link](https://www.youtube.com/watch?v=qAiPIE0sgqU).

## Client updates

* geth (Peter)
    * Been playing around with state pruning for the last few weeks
    * Still buggy and slow, hoping the next major geth release will have full state pruning
* Harmony (Dmitrii)
    * Regular work, hot fix
* ewasm (Casey)
    * Preparing to give talk tomorrow, will give the update there
* Mikhail (Harmony)
    * Prepared and published a roadmap for sharding research
    * Will share link later
* Nimbus (Jacek)
    * Published rough roadmap/timeline for sharding implementation, status.im/nimbus
    * Will publish to a slightly more public place soon-ish

## Gas cost reduction

* Vitalik published a proto-EIP for gas cost reduction
    * Only thing we need is more rigorous thinking and discussion about what to reduce gas costs to
    * Would like to see input from at least both geth and parity
    * Reducing costs depends on both of these clients having faster implementations that can handle that

## EIPs

* Nick Johnson on EIP-1087 Net Gas Metering
    * No changes since last meeting
    * Want to chat about whether remainder gas cost is reasonable
    * Currently subsequent storage writes cost same as storage read but could arguably be even cheaper than that
    * Let's continue conversation on EIP and FEM forum thread
* V: I don't think we need account abstraction for Constantinople but skinny CREATE will go forward

## Changing network IDs

* Alexey Akhunov's proposal
* Let's bring up next call when more people are on the call

## Attendees

* Hudson Jameson (EF)
* Nick Johnson (EF/ENS)
* Lane Rettig (ewasm)
* Vitalik Buterin (EF/research)
* Justin Drake (EF/research)
* Daniel Ellison (Consensys/LLL)
* Danny Ryan (EF/research)
* Casey Detrio (ewasm)
* Mikhail Kalanin (Harmony/EthereumJ)
* Dmitrii (EthereumJ)
* Péter Szilágyi (EF: geth)
* Martin Holst Swende (EF: geth/security)
