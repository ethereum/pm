Gav Wood edited this page on Nov 30, 2015

NOTE: In this EIP all uses of the term _contract_ are replaced by either _class_ (in the case of a prototype contract) or _object_ (in the case of an instance of a contract).

# Overview

In following the "do one job and do it well" mentality, EVM should be restricted to a strict minimum of externalities. This facilitates simplicity in the definition and implementation, makes testing easier and modestly reduces opcode-decoding overhead.

To this end, this EIP proposes removing all externally-interfacing opcodes save `CALL`. All other externalities are notionally replaced by objects (some built-in, some not necessarily) which may later be upgraded or augmented. Messages may be sent to these objects in order to cause particular behaviour or retrieve information.

## Current Externalities

- `CREATE`: Replaced by the Creation object;
- `LOG0`, `LOG1`, `LOG2`, `LOG3`, `LOG4`: Replaced by the Logging object;
- `BLOCKHASH`, `COINBASE`, `TIMESTAMP`, `NUMBER`, `DIFFICULTY`, `GASLIMIT`: Replaced by the Environment object;
- `BALANCE`: Replaced by the Ether object;
- `EXTCODESIZE`, `EXTCODECOPY`: Replaced by the Lookup and Unhash objects.
- `DELEGATECALL` may be retained assuming it is agreed to become part of the EVM prior.

## Implementation

A naive method would simply to implement all needed classes as built-ins. This works but has few benefits over the current system above functional-isolation (much like our existing precompiled contracts).

Another option may be to add a "super-user" privilege system, e.g. retaining the address 0x000..000 as a special "validator-information-origin" address. This allowing validators to use the existing transaction processing system to interface with otherwise normal objects. This has the advantage of increased clarity, easier portability and upgradability. This approach may work well for, e.g. the Environment, Ether and Logger objects. The Creation, Lookup and Unhash objects almost-certainly need an custom implementation in the client.
