# EVMMAX Meeting 01

### Meeting Info
- Agenda: ethereum#1204
- Date & Time: Dec 05 , 12:00 UTC
- Recording: https://youtu.be/2ExBjJ0eySo

## Notes
### Summary (by @pdobacz)
- clients/implementations represented: Geth, EthJS, Besu, evmone, Cairo ZK-VM
- progress updates:
  - geth (EIP-6690 prototype+bls prototype using evmmax-bls12-381 tool)
  - evmone (low-level lib)
- Poseidon use case
  - no objections to select this as 1st priority use case to cover
    - point raised if the bottleneck for the use case isn't calldata cost rather than mod arith cost
  - what constants of Poseidon are we interested in?
    - depends on the field one's using.
  - use case of Poseidon Hash itself
    - merkle path verification, need 32 poseidon hashes for every update
    - the constants matrix is the same for all of them for a single application
    - constants change when you change the field
- choice of assembler - Huff-based like evmmax-bls12-381 vs Yul based
- how to format Montgomery constants - opaque or explicitly in Montgomery form?
  - needs measuring
- modular inversion - should this be an opcode?
  - complexity of such opcode would be large relative to current spec
  - needs measuring

### Summary (by Kev)
- Besu & EthJS: add modular arithmetic lib
- Chance: Spec out poseidon and add a poseidon impl
- Jared: Help chance integrate into geth codebase
- Investigate whether we need to precompute poseidon constants in montgomery form
- (low priority) Investigate whether opcode inversion is so costly such that it needs to be an opcode and also used in a way that makes batch inversion not viable

### Links shared in the meeting:
- https://eips.ethereum.org/EIPS/eip-6690
- https://ethereum-magicians.org/t/rip-7696-generic-double-scalar-multiplication-dsm-for-all-curves/19798
- https://github.com/chancehudson/moduli-comparison?tab=readme-ov-file#moduli-comparison
