Péter Szilágyi edited this page on Sep 2, 2016

# Notes for Core Dev Meeting 9/2/16

## Notes from prevous meeting
https://pad.riseup.net/p/poPmdTm3ACas

### EIPS
* BIGINT_ADD, BIGINT_MUL off the table for now - to be implemented as solidity library first
* BIGINT_MODEXP
	* Need to figure out gas prices
* ECADD & ECMUL
	* https://github.com/ethereum/EIPs/issues/102
	* waiting for pairing OPs 
* SEND ALL GAS: negative two's complement sounds nice, needs a bit more investigation
* Gas costs for return memory: Proposal B looks like it will reach consensus, still need voices from ethcore and ?
* Transaction spam: block limits and/or other mechanisms in the scope of Serenity (to ponder on), mainly to avoid junk circulating the network long term.


### Mist Swappable backends

Attempt on adding swappable backends that are downloaded on demand. Requires:

* Better documentation of IPC/RPC calls Mist makes that are required for integration
* JSON config file containing information on download links on latest versions of clients
* interfaces repo: github.com/ethereum/interfaces
	* Things that should go into it
		* JSON-rpc spec
		* ABI
		* Wire Protocol?
