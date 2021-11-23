# Mocked start of Eth2 for interoperability testing

This document represents a set of standards to aid in the start of short-lived testnets _without_ an eth1 network as a source of initial deposits.

A network start consists of the following:

1. A `BeaconState`
2. Network configuration
3. Shared validator pubkey/privkeys
4. Validator distribution across nodes

## Beacon state

### Quick-start genesis

Quick-start is a simple method to create and run a common genesis `BeaconState` with from two parameters -- `genesis_time` and `validator_count`. These parameters can be specified either in a YAML file or as command-line params. This method is appealing in many testing scenarios because it is both simple and succinct. The main drawback of this method is that all validators are initialized with `MAX_EFFECTIVE_BALANCE` to start.

Sample genesis ssz states using this method can be found in [`test_quickstart_states/`](./test_quickstart_states/).

#### Generate deposits

A list of `validator_count` `deposits` is derived using the first `validator_count` pubkey/privkey pairs from a shared pubkey/privkey rainbow table of valid pubkey/privkeys generated in the [method below](#pubkeyprivkey-generation). `withdrawal_credentials` for each are set to `BLS_WITHDRAWAL_PREFIX + hash(deposit.data.pubkey)[1:]`. `amount` for each is set to `MAX_EFFECTIVE_BALANCE`. 

#### Create genesis state

Clients must create the genesis state by calling `initialize_beacon_state_from_eth1` with coordinated junk values for `eth1_block_hash = b'\x42'*32` and `eth1_timestamp = 2**40`, and with the list of `deposits` created in the [prior section](generate-deposits). The returned `BeaconState` must then be modified with `state.genesis_time = genesis_time`.

Clients must _not_ run `is_valid_genesis_state` as this state is already considered valid. Specifically, we do not check nor care about `MIN_GENESIS_TIME` in these coordinated starts.

### Start chain from specified state

In all interop testing scenarios, we must start from a specified `BeaconState`. This state might be a genesis state or some arbitrary state at any point in a chain's history. Specifically, when debugging testnets or testing very specific scenarios, a testnet might be started from a specified non-genesis state.

As with the state transition conformance tests, the `BeaconState` can be specified as either `.yaml` or `.ssz` format.

In most clients, it makes sense to just pipe the output of [quick-start genesis](quick-start-genesis) into this generic chain start method.


## Network configuration

A shared testnet must agree upon a common configuration of constants. The specs repo currently contains two [configuration presets](https://github.com/ethereum/eth2.0-specs/tree/master/configs) -- [`mainnet`](https://github.com/ethereum/eth2.0-specs/blob/master/configs/mainnet.yaml) and [`minimal`](https://github.com/ethereum/eth2.0-specs/blob/master/configs/minimal.yaml). `minimal` will serve as a primary configuration for most interop tests.

If there are components of this configuration that do not serve a specific need, we will add more configurations accordingly.


## Pubkey/privkey generation

For interop testing, we use a common set of public/private keypairs to populate validator records and new deposits. We use the following method to generate the shared keypairs.

There is a compute/storage tradeoff to be made here between calculating the required validators and reading them from a YAML file ([./keygen_10000_validators.yaml](./keygen_10000_validators.yaml)) and it is left up to implementors to choose which they prefer.

The following script is used to generated pubkey/privkeys for the first `N` validators. The `i`-th deposit/validator index uses the `validator_index_to_pubkey[i]` pubkey and associated privkey.

```python
CURVE_ORDER = 52435875175126190479447740508185965837690552500527637822603658699938581184513
validator_index_to_pubkey = {}
pubkey_to_privkey = {}
privkey_to_pubkey = {}
for index in range(N):
    privkey = int.from_bytes(
        sha256(int_to_bytes(n=index, length=32)),
        byteorder='little'
    ) % CURVE_ORDER
    pubkey = bls.privtopubkey(privkey)
    pubkey_to_privkey[pubkey] = privkey
    privkey_to_pubkey[privkey] = pubkey
    validator_index_to_pubkey[index] = pubkey
```

### Test vectors

[./keygen_test_vector.yaml](./keygen_test_vector.yaml) is a YAML file containing a list of the first 10 validators and their key pairs. The list index corresponds to the validator number. For the generation of more or fewer indices, see the script used to generate it at [./keygen.py](./keygen.py)


## Distribution of validators across nodes

Nodes should support running some subset of validators within a testnet configuration. For ease of distribution, validators should normally be split across nodes in contiguous ranges (eg validators 0-9 on node `A`, validators 10-15 on node `B`). 

To generally support this functionality, a node should accept a tuple of `validator_start_index` and `num_validators`. For example `(validator_start_index=5, num_validators=3` would provision a node to control validator indices `(5, 6, 7)`.

Nodes can also support specifying the entire list of indices, rather than the succint range form. This will allow for more novel distributions of validator indices at the cost of verbosity in specifying.
