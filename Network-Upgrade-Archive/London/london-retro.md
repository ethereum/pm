# London Testnet Retrospective 

## Ropsten Consensus Issue

### Overview

On July 21, 2021, the OpenEthereum team noticed their node had stopped progressing on Ropsten at block `10679538`. The issue, originally thought to be in OpenEthereum, was in how the go-ethereum implementation checked the balance of the transaction sender for 1559-style transactions. An invalid transaction, whose sender balance covered only the effective gas used by the transaction, but not the transaction's `maxFeePerGas` total was included in a block. Because Ropsten miners were exclusively running go-ethereum, this block was then accepted by other go-ethereum miners, despite being rejected by some other clients on the network. Specifically, OpenEthereum and Besu rejected the transaction/block, while Nethermind, go-ethereum, and Erigon (whose implementation was partially forked from the go-ethereum code) accepted them. The cause of the issue was found and fixed in the following releases:

* go-ethereum: [v1.10.6](https://github.com/ethereum/go-ethereum/releases/tag/v1.10.6), [fix PR](https://github.com/ethereum/go-ethereum/pull/23244/files); 
* Erigon: [v2021.07.04-alpha](https://github.com/ledgerwatch/erigon/releases/tag/v2021.07.04), [fix PR](https://github.com/ledgerwatch/erigon/pull/2415);
* Nethermind: [v1.10.79](https://github.com/NethermindEth/nethermind/releases/tag/1.10.79), [fix PR](https://github.com/NethermindEth/nethermind/pull/3238). 

### Problematic Block Information

* Network: Ropsten
* Number: 10679538
* Hash: 0x1252a34c4f2b061adc609e909d958c02e1ac39043e2e60c0ec47e565e3f625f1
* [OpenEthereum debug logs](https://gist.github.com/timbeiko/42dd5eee676aea6060dab04b6e0e9c34)
<details>
 <summary>eth_getBlock output (go-ethereum)</summary>

``` 
eth.getBlock("0x1252a34c4f2b061adc609e909d958c02e1ac39043e2e60c0ec47e565e3f625f1")
{
  baseFeePerGas: 11,
  difficulty: 1124214874,
  extraData: "0xd883010a05846765746888676f312e31352e36856c696e7578",
  gasLimit: 8000000,
  gasUsed: 1762587,
  hash: "0x1252a34c4f2b061adc609e909d958c02e1ac39043e2e60c0ec47e565e3f625f1",
  logsBloom: "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
  miner: "0xfbb61b8b98a59fbc4bd79c23212addbefaeb289f",
  mixHash: "0x178c542ebd5b730aa141b3e07fce663b81d7f5485011cca55b5cd55dc39b2550",
  nonce: "0x98728302c513a677",
  number: 10679538,
  parentHash: "0xe936ee0e5a915b9c163a7a1ff67269dd5f1ccb981f91b269a2130711e6a62598",
  receiptsRoot: "0x09a6eb2bf38000dd934b2cdc66f7f7923397ddd6d9cd1ac69379aaed73d00f1e",
  sha3Uncles: "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
  size: 5175,
stateRoot: "0xa942f7462d923a5e292627b64e1b20cc314bac31f7e72ecb02b65d954d12f758",
  timestamp: 1626863988,
  totalDifficulty: 34224959923696599,
  transactions: ["0x07ca8f5634d634e2eb67a9af6f9d510d73d3c2f0393f0e0490e7c0b4c18fdf0e", "0x9dbef6da5331b085d1dcc70eaa028376fd0452c49992e5ddccc132f4d42467cc", "0xdfa858a98cab341e540fc2da8abfd0b298df22a9ee9eff0c6e1edf4828ab9b84", "0x01bdfaba318f4c0b2878db0d413a20d3a2669ebbaa5c4e8f6901bdc9a01a99ec", "0xd9d2aa19f747b04863eb13a2698cd8a3c96b2463d2cf7eb60d7ca3ea8e2d45e3", "0xf5ee17e9bf8bc4fe3325860d91535d1eb98bc1d83f39fe998e0b6c4706c581c5"],
transactionsRoot: "0x6e6f39318ad2e60969e2422977deffd42dc34ac7bdbb6fb1934541c044f18774",
uncles: []
}
``` 

</details>

### Timeline of Events 

Note: all times listed are in [Pacific Time](https://www.timeanddate.com/worldclock/converter.html?iso=20210721T180000&p1=tz_pt)

July 21, 2021

* 3:39: Block 10679537 is [mined on Ropsten](https://ropsten.etherscan.io/block/10679537)
* 6:53: OpenEthereum developer posts in the #1559-dev channel of the Ethereum R&D discord that their node has stopped on block 10679538 on Ropsten. 
* 6:58: `@smixx` says their Ropsten node is at block 10680453. 
* 7:36: Besu confirms they are also rejecting block 10679538. 
* 7:51: Miner of block 10679538 is confirmed to be a go-ethereum node. 
* 7:55: Confirmation that go-ethereum miners are still progressing on the chain beyond block 10679538. 
* 7:56: Confirmation that Nethermind also accepted block 10679538. 
* 8:08: Possible root cause for the issue identified in go-ethereum.
* 8:43: [Pull request opened in go-ethereum](https://github.com/ethereum/go-ethereum/pull/23244/files) with candidate fix. 
* 8:46: [Pull request opened in Erigon](https://github.com/ledgerwatch/erigon/pull/2415) with candidate fix. 
* 9:01: Updated go-ethereum and Besu miners restarted on Ropsten (erroneous chain now up to block 10680803). 
* 9:43: EthereumJS confirmed to have the same issue as go-ethereum, Erigon and Nethermind. 
* 10:57 [Pull request opened in Nethermind](https://github.com/NethermindEth/nethermind/pull/3238) with candidate fix. 
* 19:22 Block [10680804](https://ropsten.etherscan.io/block/10680804) mined with fixed release.

July 22, 2021 

* 7:54: go-ethereum release with a fix for the issue, [v1.10.6](https://github.com/ethereum/go-ethereum/releases/tag/v1.10.6)
* ~8:00: Nethermind release with a fix for the issue [v1.10.79](https://github.com/NethermindEth/nethermind/releases/tag/1.10.79)
* ~9:00: Erigon release with a fix for the issue, [v2021.07.04-alpha](https://github.com/ledgerwatch/erigon/releases/tag/v2021.07.04)

### Suggested Corrective Actions

#### Increase Clarity of Assertions in Specification

[This commit](https://github.com/ethereum/EIPs/commit/ee7053ead7fb730a3f9178e7c7ad9e1b8cf3ee6c#diff-c7a67afc8ee3b0ff2a29ddb3cecd13fe0ce30f3c96def22f117456987f6a50a2) added new assertions to the validity of EIP-1559 transactions. Specifically, on line 217 it adds the following assertion:

```
assert sender.balance >= gasLimit * transaction.max_fee_per_gas
```

A few lines above (L207), though, `sender.balance` is modified to substract from it the transaction's amount (`sender.balance -= transaction.amount`). This led to confusion, as some client teams used the full `sender.balance` (i.e. pre-subtraction of `transaction.amount`) when checking the assertion defined on line 217, rather than the updated value. 

One suggested fix is to move this assertion closer to when the `sender.balance` value is updated, similarly to the other assertion on line 208. 

**Update: a fix for this was proposed in [this PR](https://github.com/ethereum/EIPs/pull/3681)**

#### Go-Ethereum Recovery

[Notes from @holiman](https://github.com/ethereum/pm/issues/354#issuecomment-885687324) about recovery from the bug in go-ethereum: 

##### Synced node followed wrong chain

You were running `geth`, and were in sync. At block `X`, the fork happened. Your node followed the erroneous higher-td chain, and at block `Z`, you stop the node and update to the patched version. 

Problem description; The node is still on the 'bad' chain.
Solution: Do a `debug.setHead{X-1)` to jump to before the fork. This internally will rewind the chain to _some_ state before `X`. It might not be `X-1`, since `geth` might not _have_ the full state for that block, but it will have the state somewhere. Usually, geth flushes the state to disk every ~10K blocks (or whatever corresponds to 1 hour processing), and/or during shutdown. If geth is running in `gcmode=archive`, then it flushes every block. 


##### Syncing in the presence of a wrong higher-td chain

You are syncing a `geth`-node,  and a fork has occurred at block `X`. Since the fork has already happened, and the erroneous chain has higher TD, you will most likely wind up on the 'wrong' side of the chain, with a pivot block `X+M`. If this happens, you _do not have_ any state for blocks `<X+M`, so you _cannot_ do `debug.setHead` to to resolve the situation. 

In this case, a resync is required. However, you need to prevent geth from winding up on the wrong side of the fork. This can be done with the `whitelist` command line parameter. 
```
$ geth -h | grep white
  --whitelist value                   Comma separated block number-to-hash mappings to enforce (<number>=<hash>)
```
So you'd do `geth --whitelist 123123=0x2342fafa9af9af9af9af9af9` 

The whitelist means that geth, when peering with another peer, will ask the peer "what's your block `123123`". If it gets a header back with a hash that doesn't match the whitelist, it will disconnect from that peer. So essentially, the node will isolate itself from peers on the wrong chain, and only connect to peers that will deliver blocks from the shorter (but correct) chain. 

### Upgrade summary
* Date and time (in UTC): Aug-05-2021 12:33:42 PM +UTC
* Block Number (Mainnet): 12965000
* Block Hash (Mainnet): 0x9b83c12c69edb74f6c8dd5d052765c1adf940e320bd1291696e6fa07829eee71
* Mined by: 0x7777788200b672a42421017f65ede4fc759564c8 

