# Stateless Implementers Call #25
## Info
Note: This file was copied from here: https://notes.ethereum.org/@rudolf/sic-notes#Call-25-September-23-2024

Date: September 23, 2024

Recording: https://youtu.be/pfORU9ngjzI

Agenda: https://github.com/ethereum/pm/issues/1159

## Notes

## 1. Team updates

ignaciohagopian and gballet for go_ethereum: just about ready for testnet relaunch. Most PRs merged. Also working on benchmarking. Some updates to the test fields, and fixed some tests around witness checks. Can also run the tests in stateless mode soon, where the witness acts as the prestate source of truth.

jasoriatanishq for nethermindeth: no major updates. Working with Ignacio on tests. Will try to run the tests in stateless mode this week 🔥

kt2am1990 and lu-pinto for HyperledgerBesu: last week, working on the flat DB based on stem key. Completed some benchmarking to see impact on SLOAD. Found the perf was quite bad. Working with Kev on some optimizations. Also working on integrating Constantine library into Besu, in order to compare perf. Made some good progress on getting the test fixtures to run. Will get back to finalziing gas costs after.

## 2. EIP-7702 in Verkle

We quickly went through a PR from Guillaume to update the stateless gas costs EIP in order to support changes coming in 7702. (Current plan is for 7702 to be included in Pectra, & 7702 containts a new type of tx: authorization_list. Info that is used to update some accounts)

TLDR is this updates the gas costs EIP so if you call these functions (EXTCODESIZE, EXTCODEHASH etc), then you also need to touch the CODEHASH_LEAF_KEY. Ping Guillaume with any comments/questions.

## 3. Partial Witness Charging

Ignacio walked through a few scenarios where a bit more granularity may be needed around gas costs in Verkle. See PR here.

Scenario 1: if you don’t have enough gas to pay for whatever witness charging you have to do, then you don’t actually need to include that in the witness. (e.g. if you do a jump and don’t have enough available to pay, then you wouldn’t include that cold chunk in the witness)

Scenario 2: there are several places in execution where you have to include more than one leaf in the witness. In these cases, Geth was previously always including both leaves. Even if you didn’t have enough gas, it was already added to the witness.

For both scenarios we want to allow for better granularity / partial witness charging.
TLDR: only add things to the witness if you have the available gas for it

## 4. Testnet-7 Check-in

Ending things with a quick check on testnet readiness. Pari said DevOps should have time to assist later this week. Recommended doing it locally first in case bugs are found, and then once it works locally switch to a public testnet 🥳

