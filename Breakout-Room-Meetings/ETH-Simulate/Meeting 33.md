# Eth_Simulate Meeting Meeting 33

Note: This file is copied from [here]([[./Meeting%2063.md](https://hackmd.io/QmTl38cVRteyG24a27VB8Q)](https://hackmd.io/QmTl38cVRteyG24a27VB8Q))

### Meeting Info

- Agenda: ethereum#
- Date & Time: January 06, 2025, 12:00 UTC
- Recording: [here](https://youtu.be/OpybdKZ4Ft8?si=dCBReLxqE5n85C_j)
## Notes
### Summary 
# Ideas for eth_simulateV2  

List of suggested ideas for the possible next version of `eth_simulate`:  

## Contract Creation Events  
Emit an event when a contract is created. Currently, it is impossible to see if a transaction creates a contract, except when the transaction creates only one contract using the standard method.  

## Multi Gas Calculation  
Currently, if you override `ecrecover`, it consumes more gas than it should. We could make it consume the correct amount as `ecrecover` normally would, but then adjust it to account for the correct gas amounts against the global gas limit of the call.  

## Stack Traces  
When execution fails, all you get is the error being thrown. It would be highly useful to have access to a full stack trace.  

## Full Tracing  
Enable full tracing support for all transactions.  

## Phantom Blocks  
Currently, you cannot create blocks far in the future. Phantom blocks would allow for the creation of future blocks while padding the missing blocks with a "phantom blocks" concept.  

## Witness Creation  
Enable witness generation for `eth_simulate` results to allow receivers to verify the correctness of the results.  

## Dynamic Timestamp and Block Number Increment  
Currently, to create future blocks and timestamps that depend on the head, you must query the head and then quickly make an `eth_simulate` call with the correct values. It would be useful to allow timestamps and block numbers to be defined dynamically, such as:  
- `timestamp: latest + 10`  
- `block number: latest + 10`  
This would eliminate the need to query the latest block manually and avoid race conditions due to block number changes.  

## Gas Simulations  
For each transaction:  

```json
{
  "gasLimit": number | null | "estimate"
}
```
or
```
{ gasLimit: number | null, estimatePlease: true }
   (what to do what both are defined?)

include the transaction with the estimated gas limit to block

## Remove `size` from return value
```