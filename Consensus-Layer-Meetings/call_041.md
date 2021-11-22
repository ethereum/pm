# Ethereum 2.0 Implementers Call 41 Notes

### Meeting Date/Time: Thursday June 11, 2020 at 14:00 UTC
### Meeting Duration:  1 hr
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/158)
### [Audio/Video of the meeting](https://youtu.be/WmU3k2v4UA8)
### Moderator: Danny Ryan
### Notes: Pooja Ranjan

-----------------------------

# Contents

- [1. Testing and Release Updates](#1-testing-and-release-updates)   
- [2. Testnets](#2-testnets)   
    - [2.1 Validator key hygiene](#21-validator-key-hygiene)
    - [2.2 Wallet vs. keystore discussion](#22-wallet-vs-keystore-discussion)
- [3. Client Updates](#3-client-updates)   
   - [3.1 Teku](#31-teku)  
   - [3.2 Nimbus](#32-nimbus)   
   - [3.3 Lodestar](#33-lodestar)   
   - [3.4 Lighthouse](#34-lighthouse)   
   - [3.5 Prysm](#35-prysm)   
   - [3.6 Nethermind](#36-nethermind)   
   - [3.7 Trinity](#37-trinity)  
- [4. API WG update](#4-api-wg-update)
- [5. Research Updates](#5-research-updates)   
   - [5.1 Verkle trees](#51-verkle-trees)   
- [6. Networking](#6-networking)   
- [7. Spec Discussion](#7-spec-discussion)   
- [8. Open Discussion/Closing Remarks](#8-open-discussionclosing-remarks)   
   

-----------------------------

# 1. Testing and Release Updates

Video | [01:40](https://youtu.be/WmU3k2v4UA8?t=100)
-|-

**Danny**: There are a couple of non-substantive but clarifying and potentially optimizing PR in the Fork choice, that are up right now. I expect them to go to development soon, and will make a note to the team. Probably release will be in next week or so. 

Lighthouse has integrated Alex's fork choice tests. We are still looking at and figuring how to officially release them.

Other testing updates?

**Proto**: 

### Testnet

For testnet, I've worked on [validator tooling](https://github.com/protolambda/eth2-val-tools) for  wallets for stress testing. Testnet tooling involved, so be warned for bugs. 

Lighthouse assumes strong point to use key store specifically. It will bring some change to Serenity. Worked on [E2DB](https://github.com/protolambda/e2db/). Lighthouse has API exposed to fork choice information and blocks. This tool can be helpful in analytics. 

**Danny**: Other testing update?

**Mehdi**: 
### Beacon Fuzz Update
- Good progress on fuzzing
- Prysm now supports native Go builds. Thanks, Prysm!
- It allowed us to progress significantly in integrating Prysm into Beaconfuzz framework. 
- Found 2 bugs. 
- Also, found panic in Lighthouse ENR crate, fixed immediately. 
- Also integrating Lodestar 
- identified 4 bugs. 
- Helping with BLS fuzzing for Eth1/Geth. 
- Working towards dockerizing Eth2fuzz, so that community can help find bugs.
- Analyzed OSS fuzz requirements
- Confident to get fuzzers running on Google infrastructure very soon.

**Danny**: Does Google provide infrastructure?

**Mehdi**: Yes for open source projects that are highly used. We want to coordinate and submit one request for all clients. The docker we have is very much in line with the requirement. 

**Danny**: Cool, thank you!
Any other thing on testing front?

# 2. Testnets

Video | [7:10](https://youtu.be/WmU3k2v4UA8?t=430)
-|-

**Danny**: Moving on to testnet updates. When is Onyx testnet?

The update is Prysmatic will be launching Onyx and we will be talking about where the clients are wrt to multiclient testnet. 

**Afri**: (in the zoom chat) In Brief: 
* Schlesi is history. I purged the last validator and bootnode.
* Witti is fairly stable, 100k slots, liveliness almost perfect, 75-90% validator participation. Not aware of any major issues.
* Altona might happen in the next one and a half weeks, only one client ready for the 0.12 spec yet. we might be able to launch with 4 clients this time, I'm confident Nimbus will be able to provide a genesis validator too. that said, going forward, I'll invite the client teams for genesis, so they have a chance to run their own nodes upon launch. if Altona works out we might be able to prepare for an official, public multi-client testnet.

### 2.1 Validator key hygiene
I threw up an item here, *validator key hygiene* there's a lot here and maybe we'll end up having some discussion out. We need to start training users today wrt to our testnet. eg. Not storing withdrawal credentials on the same machine used for staking, thinking about air gapped machine, thinking about some of the trade offs. There are also other component of this conversation including keystores, how to tie your keys altogether.

The first is PSA - to start shifting the docs in favor of securities even on the testnets. Does anyone wants to get into Keystore discussion?

**Mamy**: Related to that, for audit proposal, we asked auditors to give us some guidelines on secret management. I think it's relevant and ask about Dos and Don'ts.

**Danny**: Yes absolutely, we are also talking to another security firm to do a top down look at for validating for hobbyists which would include things like DOS mitigation, managing reports etc.

**Raul**: From Prysm, we've been thinking about this and currently working on accounts free design, dealing with their keys. Planning on basic commands vs power user commands. We will focus to make sure what do the user do with the withdrawal credential, where to put them. Feedbacks comes down to 
- how can I move my accounts from one computer to another?
- where are my keys?
- how do I safely move them around?
We feel like there are a lot of friction there and would be helpful if we all can think about it together.

**Danny**: Absolutely!

### 2.2 Wallet vs. keystore discussion

Video | [10:55](https://youtu.be/WmU3k2v4UA8?t=655)
-|-

**Proto**: This discussion started when I was diving further into how to deploy 1000s of validators of different clients.
Lighthouse is keystore-centric. It makes deployment easier if you just procure the key. Secrets are managed separately and well. All the clients can look into further securities. I know Teku is doing similar things. Carl has been working on a new standards. 

*(It's worth listening the conversation.)*

**Danny**: Carl you have any follow up on the new standards and changes coming in?

**Carl**: I've few points that I would like to update EIP-2333 from the BLS standards. There's a [PR](https://github.com/CarlBeek/EIPs/commit/690ddcc12c06f471acb4c06c1d6897d09338e489). The challenge here is the EIP has already made to multiple versions. 
Then there is EIP-2334 which specifies the path where the keys exists. A lot of this comes with this discussion that a path needs to be specified for Keys need to be included. The withdrawl key is the pair key of each signer key. Secret shared keys is a path that needs to be followed anyway, so it make sense to talk about the path if we're going to be using secret shared keys.  By definition you don't know where they exist.
**Staking services** - you can still use the services till the point you have the withdrawal keys and the staking services can be separately derived signing keys and then your withdrawl keys are going to be yours anyway. 
The wallets will share two different mnemonics that I agree gets very confusing and increases the possibilities of loosing keys.
The other option we have that the hardware wallets be able to export keystores which would be my personal preference. Because then we agree that keystores are the standards and we keep our keys in the hardware wallets.

**Danny**: Do any hardware wallets provide that?

**Carl**: Yes, we do not want to keep the secret inside. 

**Danny**: That's a design goal. 

**Carl**: I am little concern because, I am not sure of the power they have to compute the hash rate required to produce the keystore. I don't know but they maybe there like the Keycard kestore or the keycard wallet wouldn't. 

**Danny**: Help me understand, in the argument, clients not knowing and caring about wallets and instead just caring about the keystores, that provides maximum flexibilities and how you remanage your keys. The more you have wallet standards 
1. opiniated on how people generate the keys
2. likely if you use this key generation where withdrawl generation and the signing keys are generated from the same wallet, we now have tied the withdrawal credential close to the signing keys. This way we want clients to only think about the key storage?

**Carl**: Yes, that's the basic ideas this also add a lot of flexibilities. Furthermore, I don't necessarily I really don't want to client to really hold on to withdrawl keys, that's a secret.

**Mehdi**: I think we definitely agree here from Lighthouse if you decrypt the wallet you can almost access all the possible keys from that wallet. It's probably not something we want. 

**Proto**: Just to repeat, compatibility is also there. eg, for many clients managing keys at there ends. If they all are after unloaded system, it's not going to work.

**Danny**: There's a handful of things here.
1. Evolving EIP standards and discussions
2. How to use key and key stores in clients?

I think theres a lot here to discuss, we probably need to take discussion to threads, potentially get on a call and hack through this and there are a lot of other things to cover that. 

Carl, can you make sure to share any links where conversation is happening. Is there any other place where you would want to have people have their eyes on.

**Carl**: For now, not really. One of the point that I would like to bring up is what client need to start up the validator? As if do clients need access to deposit data or withdrawl keys or just getting the keystore is enough? In theory, keystore should be sufficient. But I know some people have preferences for having more information on that. 

**Danny**: Meaning, if I handle my deposit in a totally other place, how do I actually onboard into a client?

**Carl**: Yeah.

**Danny**: Sure.

**Proto**: I think client also need to approach where they keep directory for preferred validator, at least the keystore and option of the other deposit. They generate when they need them. SO you can search with the keystore or you can go through the deposit process with the client and keep the data up to date. Teku is doing it slightly different in structure. We should try and discuss  it here.

**Danny**: Does the keystore management within the context and the key manager of the context of a client wants a standard, a doc for guidance, an EIP on where this information should be standardized?

**Carl**: Considering other things in an EIP, we can have an EIP.

**Proto**: Maybe we should first go for interest of parties and see what they think before we start an EIP?

**Carl**: Absolutely.

**Jacek**: I am interested in seeing that what is the minimal operating perspective would be. Like absolute minimum support needed so that we can clearly divide the things that are necessary and the things that clients might add on that, like this division.

**Danny**: I'd agree. Someone can give you a key and you can run that validator likely in the form of an encrypted keystore. 

**Proto**: and secret management, the very basic management. 

**Danny**: Secret management in the sense of how I decrypt keystores?

**Proto**: Yes.

**Carl**: One of the small topics on the description of Keystore asset management is-  is anyone opposed to using allowing Unicode passwords for encrypting and decrypting assuming the use is normalized?

**Jacek**: There are multiple ways to encode.

**Carl**: That’s why I am suggesting normalized for. 

**Jacek**: But even those, if you think into a context, they’ll get heavy.

**Carl**:  I am thinking more from international standardization stand point of Unicode characters.

**Danny**: Do password systems commonly allow Unicode characters ?

**Carl**: Many of them don’t to avoid this problem, but the arguments for normalized should get you around this.

**Danny**: If I log into a standard website these days, would they let me use unicode?

**Carl**: They give you an option.

**Danny**: Not that it is a standard?

**Vitalik**: Yeah, it used to be like there. As far as I can tell, Chinese people normally just have passwords that are numbers and letters.

**Dankrad**: That’s true,  but I think for like other languages it would not be uncommon to allow things like passwords. I feel like the only reasonable way to allow that is to have unicode support. 

**Carl**: So, if I have to generate mnemonics pointer to what/ not to use that would be with the EIPs and in passwords you can use unicode characters, so it’s sort of an extension of that. We can take this discussion to the other channel, the working channel.

**Danny**: Cool!
I was thinking maybe tomorrow but I thought maybe we want to gather ourselves a little bit more , let’s plan on next week. I’ll  organize something in the next day and try to get a good time for everyone.  Maybe this time on Thursday but maybe a little bit earlier. It’s important giving people hygiene standards.

# 3. Client Updates

Video | [27:23](https://youtu.be/WmU3k2v4UA8?t=1643)
-|-

## 3.1 Teku

**Ben**:
* v 0.12 update is going well.
* BLS is done 
* Gossip sub 1.1 is done, fork choice, state transition and validator changes are done. 
* Just finishing off the remaining networking changes.
* We’ve had a big focus on our memory footprint and 
* we’ve managed to reduce the remarkable memory use for hot states, and 
* we’ve just merged a big rework / refactor that limits the number of states stored in memory and regenerates them as needed.
* Other than that, mainly fixing bugs, check the repos if you’re interested
* reducing the noise in our logs, and improving usability.

**Danny**: I guess the memory reduction is conceptualized by the JAVA garbage collection. It essentially explains the memory as much as you get it. 

**Ben**: We’re talking a lot about how much you can trust the information shared on the Eth2stats. For example that  report so kind of whole usage of the Java process for that's not reflective of what  was actually being used on what job will get out of the way if somebody else makes a memory. So it looks bad but it's not in reality that bad.

**Danny**: I got you. 
 I haven't run some of the various clients so if it does seem like most clients are still slowly leaking or slowly growing over the time. Cool, thank you!

## 3.2 Nimbus

**Mamy**: In the past two weeks, we have had a few exciting changes.
* We made block and attestation processing 250X faster by caching hash tree root. It’s not full remerklable , we took an easy path to get to a stable state and get up to speed.
* Validator client progress - PR for spec 0.12.x plus BLS.
* you can toggle  compile time between Nimbus 0.11 and Nimbus 0.12. Default is 0.11 to make Witti connect faster. 
* EIP 2333 is in PR. 
* Audit will start in 10 days, and will announce details soon. 
* On site - we updated Grafana monitoring. 
* On Witti - exciting news for mobile users. you can start Nimbus on your phone, it can sleep overnight and resync! 
* Updated guides for installing Nimbus, in particular on phones. 
*  No Go required any longer.
*  A few platform specific bugs exist, e.g. Windows 32-bit (I hope no one uses it), ARM64, which are under investigation.
* A lot of bug fixes. 

**Danny**: Great, thanks!
Does Nimbus sync Witti?

**Mamy**: When I was mentioning about the sleeping and wakeup resyncing, it was with Witti.  But there is an issue, we have an issue with the forkchoice right now. There is a proposed fork choice that is living in the PR and somehow when we switch to it, we don’t finalize any more. The fork choice that we’re using right now is guaranteed split if there is a tie-break because we are using a smaller hash as a tiebreaker while everyone else is using a bigger hash, but it didn't happen yet.

**Danny**: Tie break is generally unlikely but ..Okay cool!

## 3.3 Lodestar

**Cayman**: 
* we're probably two-thirds of the way through the 0.12 update updated.
* Fork choice updated, 
* the bigger thing that still left is Gossip sub 1.1is still in progress, working with the libP2P team
* we've been working on tooling to help us with testnets for our purposes. As far as syncing with the testnet goes, we currently, our initial sync is stable but we have a bug where we're not switching over to gossip and so we're working through that right now, and
* we're going to be working on a validator CLI, we've been holding off because of this wallet versus keystore kind of situation. So I'm sure once we get for consensus on that will try to follow kind of a standard path towards that.

**Danny**:  Great, Thanks!

## 3.4 Lighthouse

**Mehdi**: 
* We’ve been implementing 0.12.1 on a dedicated branch
* passing a lot of tests but too much changes to add
* Michale has been doing some state transition logic and update all BLS library with the latest standard changes.
* Paul’s been writing fork choices
* two interesting issues with the spec
* memory usage available to Eth2 stats
* We are now natively supporting Raspberry Pi thanks to an external contributor. Updated our docs for making it easier for people to build on the raspberry pi.
* Massive CPU usage on Schelesi has been resolved issue.
* Trail of Bits has completed the first round of peer review. Waiting on few more comments before we can see the report. Nothing critical so far, they’d be performing a second review on networking and stack and the changes introduced since the first review.
* In the process of selecting an independent firm for second independent review that should most likely take place close to mainnet. 

**Danny**: Great, thank you! Is the CPU fix that on Witti?

**Mehdi**: Merged to master, a few days ago.

**Age**: Not merged in the master yet. Merged Disc V5 in the master. 

## 3.5 Prysm

**Terence**: 
* We’re live to spec v0.12.1. 
* Topaz is shutdown, launched Onyx. 
* 4000 deposits away from the genesis, it maybe Saturday afternoon Pacific time. 
* Doing some sanity testing on mobility on Onyx multi-client experiments.
*  So far we’ve tried Teku 
* we verified that they does the Eth1 deposit the same way Prysm does, will try Lighthouse next.
* If any client is ready for 04, feel free to ping us, we will be happy to launch it.
* We now offer a  native Go support, start developing your favorite test editor.
* We’ve full support of Nethermind and other Eth1 node implementations on Prysm. 
* Added a few more debugging related RPC endpoints. 
* In the background, we’re working on revamping the validator key management. We’re researching the EIPs, getting feedbacks from users on components.
* Bunch of minor bug fixes, improvements and optimizations. 

## 3.6 Nethermind

**Tomasz**: 
* Working on Eth2/Eth1 integration, 
* deposit workflow. 
* Will be updating to 0.12.1 spec. 
* started looking at updates to the API. 
* Have a full time person on testing. Will add capability to run tests automatically.

## 3.7 Trinity

**Alex**: 
* Spec updates to 0.11.3. 
* Work on optimizations to be able to run mainnet config. 
* Working on efficient forkchoice: looking at protoarray.
While I have everyone here, I also want to announce that we’re working on a proxy contract for the main deposit contract basically to verify BLS signatures. If anyone wants to help with that or review the contract, just reach out to me, link in the [chat](https://github.com/ralexstokes/deposit-contract-verifying-proxy).
**Danny**: Is this deployed to the Yolo testnet?
**Alex**: It’s not deployed yet, but it’s something that I was looking. 

**Danny**: Cool!

# 4. API WG update
Video | [43:42](https://youtu.be/WmU3k2v4UA8?t=2622)
-|-

**mpetrunic** (Update from [Agenda](https://github.com/ethereum/eth2.0-pm/issues/158#issuecomment-641305001))

As for WG APIs report:

* merged: /node namespace endpoints
* open PRs: /beacon/state and /beacon/pool endpoints
* in progress: /beacon/blocks
* missing: /configendpoints (a bit tricky, it's hard to keep params up to date), update /validator endpoints

It would be really helpful if teams could take a look at PRs and comment if they see some stuff missing or hard to implement.

**Danny**: Keep an eye out for things that are difficult to implement and things that people need to be able to do and it would be difficult for them to do. 

In terms of timeliness and completeness we generally have the roadmap for space v1 and that most of it. Likely by the end of next week would be in this repo and at that point, we can go back and forth if there are any continued issues.

As for the remaining discussion points that Ben pointed out, I am not quite sure what other points would currently be debated but if there is anything contentious then we will drop the API. Discord (as a note) for discussion.
 
# 5. Research Updates

Video | [47:45](https://youtu.be/WmU3k2v4UA8?t=)
-|-

### 5.1 Verkle trees

**Vitalik**: Yes, myself and Dankrad with the help of some academics and just some other people have been looking at Verkle Tree, which is basically an alternative to Merkle Tree for state storage.  are the propI wrote an Eth Research page to specify what the problem is a couple of weeks ago. And  the problem is basically that you want something that has all the properties of a Merkle tree. It's a commitment to a whole bunch of objects that you can make proofs for any objects. if a small piece of the data gets changed that you don't have to recompute over everything to make proofs to the new commitments or the new state root, and so forth, except adding the requirement for witnesses to be compact. So the Merkle tree’s witnesses are going to be (right now it is somewhat crazy ) but it will be about 700 bytes per object, which is a bit too much for comfort. 

So the main alternative so far has been the Kate commitments. Let’s say you have 48 bytes of proofs for an unlimited number of elements. Except, it is kind of fatal that if the data changes then you have to do a huge recomputation over the data in order to be able to continue making proofs. So trying to figure out how to kind of move past that and the more recent kind of direction that at least I've been going is Verkle Tree, which is basically a kind of Merkle Tree Style construction made out of Kate commitment.  So basically Verkle Tree might be something like you know somewhere between between 256 and 16000, we haven't decided yet. If you have a proof like this you will basically just having the same way you would any other proof except because the tree has a much larger width and because that Kate proofs are single object the other proof size would be it basically it something like 96 bytes per element looking likely. Still evaluating this but it's also a potential candidate to replace even binary Merkle trees.

**Danny**: Is split up the state space and two subsets and make it categorized and then Merkelize them?

**Vitalik**: Right, You could do multiple layer of subsets. I’d probably favor three layers. the width of each commitment would be 2048 and then you would have t3 layers 2048 *3 you basically have space for a 8 billion elements.

**Danny**: Got it.

**Aditya**: There’s a small bug fix from when process blocks were refactor. Thanks to Alex V. for catching this and I just made a pull request for that fix just want one I can check it out in the [chat](https://github.com/ethereum/eth2.0-specs/pull/1886).

**Danny**: This is a forkchoice?

**Aditya**: Yes,

**Danny**: Is this this is effect normal or is it an exceptional case?

**Aditya**: It prevents certain target checkpoints to be added to the store basically the ones which I haven't been pulled up so when you get on your getting blocks every slots and you could just cause an epoch.  It prevents those targets from being added to the store

**Danny**: Got it. Thanks!  Any other research update? Okay!

# 6. Networking

Video | [52:35](https://youtu.be/WmU3k2v4UA8?t=3155)
-|-

**Danny**: Age managed to get connected to Disc V5 to multiaddrs. Was there any substance of changes  that need to be made both to the protocol and the implementation.

**Age**: The spec supported it but the implementation specific, I guess. We had some issues with a CPU usage in our so we pretty much refacted everything, right,  we kind of rebuilt it from ground up, so it can support it. I think you can only support in-line peer id. I'm not sure, it is implementation specific.

**Danny**: Perfect! I think the UX around passing the others here for direct connections to the nodes , direct connections are valuable so if you want some insight on how to do it, chat  on Discord. Any other networking items?

# 7. Spec Discussion

Video | [54:00](https://youtu.be/WmU3k2v4UA8?t=3240)
-|-

No discussion

# 8. Open Discussion/Closing Remarks

Video | [54:22](https://youtu.be/WmU3k2v4UA8?t=3265)
-|-

No discussion.

**Danny**: We have an API Key Management discussion on the calendar and otherwise testnet thing. Thanks everyone!

------

# Annex

## Zoom Chat 

* From protolambda to Everyone: 03:11 PM
E2DB I mentioned earlier: https://github.com/protolambda/e2db/ testnet validator keystore tooling, trying to work around all keystore incompatibility issues: https://github.com/protolambda/eth2-val-tools
* From Carl Beekhuizen to Everyone: 03:17 PM https://github.com/CarlBeek/EIPs/commit/690ddcc12c06f471acb4c06c1d6897d09338e489
https://github.com/ethereum/EIPs/pull/2670
* From Alex Stokes to Everyone: 03:46 PM
https://github.com/ralexstokes/deposit-contract-verifying-proxy
* From Aditya Asgaonkar to Everyone: 03:50 PM
https://github.com/ethereum/eth2.0-specs/pull/1886

## Attendees

* Aditya Asgaonkar
* Afr Schoe
* Age Manning
* Alex Stokes
* Ben Edgington
* Carl Beekhuizen
* Cayman
* Danny Ryan
* Dankrad
* Grant Wuerker
* Guillaume
* Hsiao-Wei Wang
* Jacek Sieka
* Jonathan Rhea
* Joseph Delong
* Lakshiman Sankar
* Mamy
* Matt Garnett
* Mehdi |Sigma Prime
* Pooja Ranjan
* Protolambda
* Raul Jordan
* Terence (prysmatic)
* Tomasz S.
* Vitalik

## Next Meeting Date/Time

Thursday, June 25, 2020.

