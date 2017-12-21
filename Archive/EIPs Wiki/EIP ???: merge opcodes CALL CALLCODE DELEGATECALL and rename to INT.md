cdetrio edited this page on Oct 3, 2016

New opcode: `INT`/interrupt.

Like `CALL` except takes a further parameter: `max_depth` - this limits the amount of further `CALL`s/`INT`s/`CREATE`s/`CALLCODE`s/`DELEGATECALL`s which can be done. Set to `0` and the interuptee cannot itself make an `INT` call.

Consider also including `const` param to remove the need for `STATIC_CALL` (see Vitalik's [EIP#116](https://github.com/ethereum/EIPs/issues/116)). Also, consider adding further params to remove the need for `DELEGATECALL` and `CALLCODE`. Eventually all could be preprocessed into `INT` and a later hard-fork would remove `CALL`/`CALLCODE`/`DELEGATECALL`.

### Rationale

Getting people thinking in terms of interrupts should make one of two things happen: if they're not familiar with interrupt-level programming, it'll be a gentle reminder that there be dragons here; the sensible ones will familiarise themselves with the concepts in low-level programming. If they are familiar with the concepts already, it'll be a reminder that semantics include the possibility of reentrancy and that they should code accordingly conservatively.

Middleware (solidity, web3.js) can go its own way obviously, but at least this sets the standard.

On that note, I'd like to see middleware adopt a five-way model here.

All assume `dest` is either `object.method` or `object` (for the fallback).

- `dest(params)`: Sets the const-flag, uses all gas. No state changes may happen as a result of this. **Reentrancy-safe**.
- `dest.send(value, params)`: Sends funds along with message, providing a bare minimum of gas. **No re-entrancy possible**.
- `dest.message(value, params)`: Sends funds with message. Sets `max_depth` to 0. **No re-entrancy possible**.
- `dest.post(value, params)`: Like send, except that further state transitions in the current execution are moved to precede it. It's non-trivial to get right, but basically, you'd buffer up all the operands (including the pointed-to memory if necessary) and leave the dispatch until the end of the message. Always "succeeds". **Reentrancy-safe**.
- `dest.post_or_throw(value, params)`: Same as `post`, except would throw if `CALL` fails. **Reentrancy-safe**.
- `dest.interrupt(value, params)`: DANGEROUS: defaults to using all gas, returns something, executes immediately. UNSAFE. Just like what happens currently.
