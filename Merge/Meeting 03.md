# Merge Implementers' Call 3
### Meeting Date/Time: Thursday, April 29th, 2021 13:00 UTC
### Meeting Duration: 30 min
### [Agenda](https://github.com/ethereum/pm/issues/305)
### [Video of the meeting](https://youtu.be/KAm718N_bvA)
### Moderator: Mikhail Kalinin
### Notes: Shane Lightowler

# Intro

**Mikhail Kalinin**

* Welcome to the call, likely a short call today.

# Rayonism Updates

## Eth2 Clients

**Mikhail Kalinin**

* Teku updates first>>
* Teku is ready for first devnet.
* Tested with Nethermind, Besu, and Catalyst.
* Exciting!
* Havent yet tried interop with other cients.
* Have started work on Teku sharding implementation. Works in general but needs some sanity tests.

**Paul Hauner**

* Lighthouse updates>
* Have interop working with Nethermind and GETH.
* Still not calling the finalised endpoint, but can sort that pretty quickly.
* Ready for devnet!

**Terence**

* Prysmatic updates>
* Pretty much ready for the devnet, have spent the last few days debugging.
* Interop working with Catalyst. Trying others shortly.

**Dustin Brody**

* Nimbus updates>
* Testing with GETH/ Catalyst. Going well so far - interop has been solid.
* Ready for devnet!

## Eth1 Clients

**Lukasz Rozmej**

* Nethermind updates>
* No major issues.
* Releasing a hotfix today for an issue raised by Lighthouse re: contracts response. 
* Issue is response was not serialised correctly (response was saying value instead of success). Think its something to do with Docker. Not sure why it happened.

**Tomasz Stanczak**

* Could we not release the fix and Lighthouse workaround the response?

**Paul**

* Errors on that endpoint wouldn't stop us from progressing, so Lighthouse just logs an error saying we didnt find the field we expected in the response.
* The call works well in Nethermind.
* This doesnt stop anything from working it just creates an error log.

**Lukasz**

* The new release wont impact anything. If you just grab the laatest docker image it will be fine. We should still release it.

**Mikhail**

* Anyone from GETH on the call?
* I can give the update there... GETH works, I tried it :)

**Gary Schulte**

* Besu update>
* Besu / Teku local net is working. Ready to join the devnet.

**Danny**

* Different Eth2 clients have tried different Eth1 clients. Is the same true in reverse? Have we run any transient testnets with different consensus engines driving? Or will tomorrow be the first time?

**Protolambda**

* I've successfully paired Lighthouse and Teku. It works.
* Had some issues with Lighthouse / Nethermind which have been resolved. Am confident it will work.

**Mikhail**

* I've used Teku with Nethermind and Catalyst. They work well.

**Protolambda**

* At first we were looking at just launching with the minimal set of clients just to get something out.
* In the past few days its been a lot, as more clients have come online in the multi-client testnet. Theyve been coming faster than we can write deployment code for.

**Mikhail**

* This actually great, exciting! We'll see tomorrow.
* So we have three Eth1 clients and four Eth2 clients ready for the devnet tomorrow.

## Devnet Launch Details

[9:27](https://youtu.be/KAm718N_bvA?t=567) 

**Protolambda**

* Planning to launch devnet tomorrow.
* Initial configuration created yesterday, has been changed a bit (fork version on the eth2 side).
* Should be very similar to the configs people are used to, although this will be a mainnet config.
* Boot nodes will be set up after this call - we will deploy some of our own. Focus today will be on conncecting the nodes, getting them up and running.
* The devnet chain will start tomorrow at noon UTC.

**Mikhail**

* It would be good to jump on Discord voice after this call to cover details around the devnet launch. Would be good to have full coverage across the client teams on the call so we dont miss any interops.

**Protolambda**

* We will need/try to test all combinations of Eth1/2 clients.
* If you dont have validator keys already, please reach out to get your neumonics.
* We'll be talking on all the usual channels (incl Rayonism discord) leading up to launch. Ill send out a zoom link shortly before which we can all get on.

# Research Updates

[13:57](https://youtu.be/KAm718N_bvA?t=837)

## Fork Choice Rule Update

* Have updated the [fork choice rule section](https://hackmd.io/@n0ble/ethereum_consensus_upgrade_mainnet_perspective#External-fork-choice-rule) of the execution layer design doc.
* This removes the recommendation to use a new block as the signal for fork choice.
* Even if the execution payload is valid it doesnt mean that the whole beacon block is valid. Depending on the implementation of the consensus layer it could be the case that when the new block has been sent to the execution layer and its been valid. But state root mismatch happens on consensus side later.
* In this case the new head wont be issued for this particular block. This is why its been removed.
* The only trigger for the fork choice is the new head message.

**Vitalik Buterin**

* This is the trigger for changing the fork choice on the execution client side from being proof of work to be in transition mode?
* Oh its post transition?

**Mikhail**

* Right. You can use new block if its the lead. If its the child of the head of the chain you can switch to this block which, dependent on the implementation, might not work correctly.

**Vitalik**

* Is this because we want the execution client to not trust the consensus client for this?

**Danny Ryan**

* Say you ran execution and consensus validation in parallel, you might find some of the beacon block contents were invalid even though the execution payload was valid. Or any type of ordering issues on that.

**Vitalik**

* If the client implementation sendt the executiion block to the execution client before it did, at least one of the other checks, and if those remaining checks ended up not passing then that would be a problem.

**Danny**

* For example if you dont do this until the end, you wouldnt know.

**Vitalik**

* Whereas a new head message is something that would come to an execution client after the consensus client did the full validation cycle.

**Mikhail**

* Pay attention to the above if you have started to implement this  external fork choice stuff.

## Withdrawal Design Doc

[17:39](https://youtu.be/KAm718N_bvA?t=1059)

**Mikhail**

* The [withdrawl design doc](https://hackmd.io/@zilm/withdrawal-spec) has a PoC implementation for the withdrawal mechanism.
* This is what we'll probably use as a basis for the Rayonism spec. We did tentatively plan to test withdrawals if things went well.

**Dmitry Shmatko**

* I'm working on the withdrawals design doc. A spec could be made from it.
* Partial withdrawals are not supported. It only works with validator exit, which leads into full withdrawals. Will extend the spec with partial withdrawals in a few days.
* I was sceptical about partial withdrawals intiially, but I can now see they could be done without much trouble.
* The messages received should be infrequent.

**Danny**

* I was able to review the doc and have left comments. It looks good - seems simple and clean.
* Partial withdrawals should be unique and have a unique identifier so that the mapping isnt based on validator index.

**Mikhail**

* Everyone interested in withdrawls should check it out. 

**Danny**

* I should mention that we are going to turn on the core suite of tests for merge the spec thats in the repo. However the Rayonism merge spec has probably diverged from this on the beacon chain side. Let's talk about this in a few days. Primarily whether you can support the types. Most of the changes are minimal.

**Mikhail**

* What do you mean by diverging?

**Danny**

* Im not certain but... does the rayonism spec point to dev currently or is it pointing to a paticular commit on the beacon chain side?

**Mikhail**

* Its pointing to dev.

**Danny**

* Then cutting the test vectors would be useful.

**Mikhail**

* Let's get into spec discussion.

# Spec Discussion

[22:24](https://youtu.be/KAm718N_bvA?t=1344)

**Mikhail**

* I know there is work happening re: state and block sync implementation. Does anyone have any q's re: that work or any other spec/research work?
* No? Ok... everyone is clearly focussed on rayonism. Lets get back to this in a couple of weeks.
* Any questions re: beacon chain spec?

**Terence**

* Question re: merge spec, the sharding spec should be on top of the merge spec. We've done the execution payload... Im not sure how useful that is.

**Vitalik**

* Theoretically the changes that need to be done to the spec are pretty independant. You can work on the two specs in parallel. Theres not much value in implementing sharding before the merge, except for testing value.

**Danny**

* The current state of the spec is day zero stable. Everyone has current implementations of it.
* Its easier to have both the merge and sharding specs be based of that day zero spec. If changes to the merge happen we then need to update the sharding spec, and vice versa. We can independantly iterate.
* But once they stablise and theres a concrete order, merge will go to mainnet first, we would see sharding be rebased on the merge spec.
* * Once Altair implemntations exist...

**Proto**

* Sharding is already based on the merge spec in the eth2 specs repo.

**Terence**

* I dont see the execution payload header in the beacon state. Am I missing it?

**Proto**

* I think it just extends the ETH state...

**Terence**

* Got it.

# Open Discussion

[25:44](https://youtu.be/KAm718N_bvA?t=1544)

**Mikhail**

* Ok. Open discussion. Anything to discuss?

**Paul**

* Do we want to chat here about opening Rayonism nodes, or after in discord?

**Mikhail**

* Lets do it in discord after.
* Thanks to the implementers teams! Thanks for your hard work and very excitedto be here at this line - Rayonism.
* Thanks also to Proto for his coordination efforts.
* Let's wrap up here and carry on in Discord!

-------------------------------------------
## Speaking Attendees
- Mikhail Kalinin (Teku)
- Paul Hauner (Lighthouse)
- Terence (Prysmatic)
- Dustin Brody (Nimbus)
- Lukasz Rozmej (Nethermind)
- Tomasz Stanczak (Nethermind)
- Gary Schulte (Besu)
- Protolambda
- Vitalik Buterin
- Danny Ryan
- Dmitry Shmatko

---------------------------------------
## Next Meeting
May 14th, 2021 @ 13:00 UTC







