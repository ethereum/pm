# Mocked Eth1Data votes for interop testing

Most initial interop tests will not have an associated eth1 chain to come to consensus upon via the `Eth1Data` vote mechanism. This is a quick standard on how clients should stub this vote. The goal here is to check that `eth1data` updates but to _not_ update it in such a way that new deposits must be processed.

We may come up with a more clever mechanism that can actually handles deposits in the future, but for now we just operate in such a way that disables deposits.

## Stub standard

The following stub standard allows the eth1data mechanism to update. This should be used by validators whenever they are supposed to retrieve data from the eth1 chain.

This has validators agreeing upon a stubbed `deposit_root` and `block_hash` but always keeps `deposit_count` at `state.eth1_deposit_index` so that the consensus does not force deposits even as eth1data is updated. 

```python
def get_eth1data_stub(state: BeaconState, current_epoch: Epoch) -> Eth1Data:
    epochs_per_period = SLOTS_PER_ETH1_VOTING_PERIOD // SLOTS_PER_EPOCH
    voting_period = current_epoch // epochs_per_period
    deposit_root = hash(int_to_bytes(voting_period, length=32))
    return Eth1Data(
        deposit_root=deposit_root,
        deposit_count=state.eth1_deposit_index,
        block_hash=hash(deposit_root),
    )
