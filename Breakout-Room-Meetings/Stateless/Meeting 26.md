# Stateless Implementers Call #26
## Info
Note: This file was copied from here: https://notes.ethereum.org/@rudolf/sic-notes#Call-26-October-21-2024

Date: October 21, 2024

Recording: https://youtu.be/MJA1e95cfww

Agenda: https://github.com/ethereum/pm/issues/1186

## Notes

## 1. Team updates

ignaciohagopian and gballet for go_ethereum: added around 30 new tests in the execution test spec repo, mostly covering edge cases regarding out of gas execution transactions. (This is relevant for Verkle because if you run out of gas, you might generate a partial witness). Guilluame has been working on speeding up witness generation, as well as the rebase on top of Cancun to get updated metrics.

jasoriatanishq for nethermindeth: testing and debugging latest hive tests. Also have been progressing on the Nethermind implementation of the transition.

lu-pinto and kt2am1990 for HyperledgerBesu: Working on gas costs. Currently 2 tests are failing (regarding self-destruct). Also all of the BLOCKHASH tests are failing because the logic for pulling out the BLOCKHASH from the system contract is not yet implemented, but that’s up next. Have also completed some optimizations on the rust-verkle crypto library. And now have a working version of the flatDB based on stem. Next step here is to generate the preimage to be able to run this flatDB with mainnet blocks and compare performance. Lastly, continuing to work on integrating the Constantine crypto library into Besu.

## 2. Circle STARKs seminar

Matan joined to share some info on an upcoming SNARK-focused seminar he will be leading, which will be open for anyone currently working on stateless. The seminar will be focused on bridging the gaps for upcoming items on the Verge roadmap, in particular exploring the topics of SNARKing Verkle, Circle STARKs, and STARKed binary hash trees (as a potential alternative to Verkle). No prerequisites or math background required for the course. Idea is accessible to lay audience. The seminar will likely be weekly and run for TBD number of weeks.
Apply to join here!

## 3. Verkle Metrics

Guillaume shared an updated document which provides a helpful overview of latest Verkle metrics. This is data collected by replaying ~200k historical blocks (around the time of the Shanghai fork). While they don’t provide a perfect predicition for how things will look in the future, it does help give a solid approximation of what to expect.



## 4. Spec Updates

Last up on this week’s call, a few quick points related to gas cost spec:

CREATE gas cost: currently 32,000. But for Verkle, we’ve considered reducing this.
Decision: keep as-is for now.
How much to charge when doing account creation (e.g. when doing a call and the address does not exist yet). And similar question for SELFDESTRUCT
Decision: open a convo with research team for further discussion