# PeerDAS Breakout Room #12
Note: This file is copied from [here](https://docs.google.com/document/d/1Ng2IrCe28kTt1BnIsjtMlKHq2MHgaja24LhFXSvqfJQ/edit#heading=h.tubwqb51zcjq)

## Meeting info
Date: 2024.11.26
Agenda: https://github.com/ethereum/pm/issues/1193
YouTube video: https://youtu.be/vVACJNHA3tY

## Notes

### Client updates
**Prysm**
- Merging change from feature branch to dev branch
- Will building on the top of Electra

**Teku**
- Will finish rebasing at the end of this week

**Lighthouse**
- No substantial updates on Peerdas since we are focusing on Pectra.
- Not started the rebasing but should be simple.
- Refactoring syncing

**Grandine**
- Building on dev branch.

### Devnet updates

Launch devnet based on pectra

Finalize devnet5 spec by the end of the week

Launch devnet5 next week or the week after that

Hopefully activate PeerDAS as Fulu

### Spec discussions

Last call for the decouple subnet PR https://github.com/ethereum/consensus-specs/pull/3832 

**Manu**: not against the change but has concerns with the fact we don’t have a finalized devnet yet
- Other teams: fine with both

**ACTION: merge it**

Discuss about the validator custody PR https://github.com/ethereum/consensus-specs/pull/3871

**Question**: does it help syncing? Manu: all nodes become supernodes with Devnet config.
- **Francesco**: yeah, like, it might actually make things harder on, on devnets and less flexible. 
- Francesco: we need to think about, if we want to add such feature, how to apply it at Devnets?

**ACTION: not merge it for now**

### Open discussions

Should we specify the timing for starting reconstruction?

EIP-7742

Latest proposal to be discussed on Thurday ACD: https://github.com/ethereum/EIPs/pull/9047

## Zoom chat links

https://docs.google.com/document/d/1Ng2IrCe28kTt1BnIsjtMlKHq2MHgaja24LhFXSvqfJQ/edit?tab=t.0

https://github.com/ethereum/consensus-specs/pull/3832

https://github.com/ethereum/consensus-specs/pull/3871

https://github.com/ethereum/consensus-specs/pull/3871
