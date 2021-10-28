# All Core Devs Meeting 103 Notes <!-- omit in toc -->
### Meeting Date/Time: Friday 08 Jan 2020, 14:00 UTC <!-- omit in toc -->
### Meeting Duration: 1 hr <!-- omit in toc -->
### [Github Agenda](https://github.com/ethereum/pm/issues/232) <!-- omit in toc -->
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=ITVMTHzAcg0)
### Moderator: James Hancock and Hudson Jameson <!-- omit in toc -->
### Notes: Edson Ayllon <!-- omit in toc -->



---

# Contents <!-- omit in toc -->

- [Summary](#summary)
  - [Actions Needed](#actions-needed)
- [1. YOLOv3 & Berlin client updates](#1-yolov3--berlin-client-updates)
  - [Nethermind](#nethermind)
  - [Besu](#besu)
  - [Open Ethereum](#open-ethereum)
  - [Geth](#geth)
  - [EthereumJS](#ethereumjs)
  - [Other](#other)
  - [Actions](#actions)
- [2. Other EIPs or discussion items](#2-other-eips-or-discussion-items)
  - [EVM-384 Update](#evm-384-update)
  - [EIP-2937](#eip-2937)
  - [Hudson Stepping Down from ACD role](#hudson-stepping-down-from-acd-role)
  - [Actions](#actions-1)
- [Annex](#annex)
  - [Attendance](#attendance)
  - [Next Meeting Date/Time](#next-meeting-datetime)

---

# Summary 

## Actions Needed

Action Item | Action
-|-
**103.1** | This next week, reach out to clients to get done what they need for fuzz testing
**103.2** | Geth team finish final reviews to publish YOLOv3
**103.3** | Before next call, get YOLO up and running to focus on next steps, including fork block proposals.
**103.4** | Pooja and James to connect with client teams on a EVM-384 monthly call, in order to save time in the ACD call.
**103.5** | Async discussion for EIP-2937 on Ethereum Magicians.



---

# 1. YOLOv3 & Berlin client updates

Video | [5:42](https://youtu.be/ITVMTHzAcg0?t=342)
-|-

## Nethermind

Updated to 2929 implementation. Everything is green now.

2718, 2930. Implemented to the extent where it works to the basic operations, but fails for the sections unspecified. Just waiting for the final specification.

Built over the packages for the jmp library for the faster 3665. That's ready to change. Everything is ready.

YOLOv1 was implmented a long time ago.

## Besu

Everything is implemented. 

Still working on testing for 2930.

Cross-referencing data was provided by Geth. Still working on those.

## Open Ethereum

Everything should be ready. Finished implementation in December. Not expecing anything new, so everything done.

## Geth

2930/18 is remaining. After that is regular, surrounding stuff.

Did generate reference tests to share. Saw lightclient has been doing some updates, so we may have to change those again.

Should be up to spec now. Hadn't updated the signing hash, which has been fixed. Fixed cross-client hash to have the proper signature hashes.

## EthereumJS

Client is ready to join the testnets. Development done on a mono-repo. No release reflecting the changes. 

On mainnet it's processing blocks with decent performance. 

For YOLO testnet readiness, need to improve the connection reliability on the POA network, improve the hardfork integration, and do some other fixes.

All YOLOv2 EIPs are implemented. Are interested in joining. Should be ready by the end of this month.

## Other

Close to have the clients implement things. Would deploying YOLOv3 have value? Or deploying to main testnets create more value?

Launching a YOLO testnet isn't too much. And other testnets, there are parties who are relying on them being up.

The 2930 implementation will take at least a week to get merged. After that's merged, we can do a release for that testnet, with Geth.

If other clients are ready for YOLOv3, we can get it launched before Geth is ready.

Looking to have YOLO up by the next All Core Devs call.

The week after, James can do fork block date proposals.

## Actions

- **103.1**—This next week, reach out to clients to get done what they need for fuzz testing
- **103.2**—Geth team finish final reviews to publish YOLOv3
- **103.3**—Before next call, get YOLO up and running to focus on next steps, including fork block proposals.


# 2. Other EIPs or discussion items

Video | [19:48](https://youtu.be/ITVMTHzAcg0?t=1188)
-|-

## EVM-384 Update

A new update is being preferred, but nothing to present yet.

The difference of price can be up to 10 times more expensive. The gas spent on control flow is a few times more expensive than the precompile that does everything. The next update will try to address this.

This proposal might need reprising in multiple places in the EVM.

BLST is a C library, may be good to standardize it as a reference implementation, which may reduce risk of consensus divergance. However, there is safety concerns due to precompiles in general.

Better to address precompiles on a case by case basis, instead of formalizing a process for including them.

It's better to specify how much to fuzz given the specs of the device that's fuzzing. And then, once it's included, not make any more changes, even if improvements can be made.

Connect with James Prestovich, who has done work on BLS precompile with the Celo network.

BLS is something we should address sometime this year.

Currently, there is an unknown amout of precompiles that can and can't be added. Getting closer of what is and what isn't included with 384. It's not fair to ask for the 384 team to give a conclusion on this call.

Having a separate call to discuss 384 may be helpful, say on a monthly call.

## EIP-2937

Meant to be a companion to the account abstraction EIP. This is to create contracts that are guaranteed not to be self destructed. This allows abstracted accounts to have libraries. 

Generally the best solution is to get rid of self destruct complelely, but it would break several contracts. If someone wants to champion getting rid of self destruct, we would support it, but it's complex. 

Currently, self destruct is use to upgrade contracts, removing it would break those contracts.

## Hudson Stepping Down from ACD role

After Berlin, Hudson will be stepping down from Eth1.0 network calls. Hudson will not be leaving the Etherum ecosystem. Tim Beiko will be replacing Hudson with All Core Devs. It will be a multi month transition. 

## Actions

- **103.4**—Pooja and James to connect with client teams on a EVM-384 monthly call, in order to save time in the ACD call.
- **103.5**—Async discussion for EIP-2937 on Ethereum Magicians.

---

# Annex


## Attendance

- Adria Massanet
- Alex Vlasov
- Angela Lu
- Ansgar Deitrichs
- Artem Vorotnikov
- Danno Ferrin
- Guillaume
- Hudson Jameson
- James Hancock
- Lightclient
- Marcelo Ruiz de Olano
- Martin Hoist Swende
- Micah Zoltou
- Peter Szilagyi
- Piper Merriam
- Pooja Ranjan
- Rai Sur
- Sam Wilson
- SasaWebUp
- Tim Beiko
- Tomasz Stanczak
- Trent van Epps
- Tyler Goodman


## Next Meeting Date/Time

Friday January 22, 2021 14:00 UTC
