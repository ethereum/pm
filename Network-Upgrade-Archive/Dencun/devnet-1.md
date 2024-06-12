# Proto-Danksharding (EIP-4844) Devnet v1 User Guide

**note**: this file was copied from [here](https://hackmd.io/@inphi/SJMXL1P6c) for reference.

- Proto-Danksharding (EIP-4844) Devnet v1 User Guide
    - [Peering](https://github.com/poojaranjan/pm/new/master/Archive/Dencun#peering)
    - [Getting Devnet ETH](https://github.com/poojaranjan/pm/new/master/Archive/Dencun#getting-devnet-eth)
    - [Uploading Blobs](https://github.com/poojaranjan/pm/new/master/Archive/Dencun#uploading-blobs)
    - [Downloading Blobs](https://github.com/poojaranjan/pm/new/master/Archive/Dencun#downloading-blobs)
    - [Endpoints](https://github.com/poojaranjan/pm/new/master/Archive/Dencun#endpoints)
    - [Troubleshooting/assistance](https://github.com/poojaranjan/pm/new/master/Archive/Dencun#troubleshootingassistance)
      - [When I try to run Prysm on MacOS, I get this error "Caught SIGILL in blst_cgo_init…](https://github.com/poojaranjan/pm/new/master/Archive/Dencun#when-i-try-to-run-prysm-on-macos-i-get-this-error-caught-sigill-in-blst_cgo_init)
    

## Peering

To join the network, you'll need to build and install the following geth and prysm forks:
* geth - https://github.com/mdehoog/go-ethereum/tree/eip4844-devnet-1
* prysm - https://github.com/Inphi/prysm/tree/inphi/clean-slate

Both geth and prysm contain preset configuration for the Proto-Danksharding network. Similar to the way geth/prysm can be configured for testnets using `--goerli` or `--ropsten`, you can configure both using `--eip4844`.

```
echo '[Node.P2P]
StaticNodes = ["enode://37737cd323817af681773df6784ea3ca90b1cef899a432032a48368a41100327637031be27a6a34034788215014a7237e0d35ec97b70dded4d2333b1e6a07c0d@34.171.161.213:30303","enode://5d9beaf6ead0d2a33dcb48c6204cf2588f1dad47615d6729a3774f2733ac28cf79d74d8e6862f0b021acf746619d5257e225f7397cc1c5d9f3fa16f2b4f764b3@34.123.216.69:30303","enode://8190e9afea4c5e53611c8372fc68e6ab4ece205f23538af14853d0155eb4e8ac4f2e1035b354aaaec20cf0c7aeb0d5ff44bde92dd0b9b44b3d679459f08ee3e9@34.170.213.201:30303","enode://d20da051537a909f6d55316d55b51b5cd23fdcec166cd68a48f54d93ca382adf19220546020f95e7ff6b3eafbf8f0506469184d34a7dbbf82f31b22e523c48ee@34.68.253.231:30303","enode://17d98d030c9d2d8b2966b0556bec0856d3f9962801c9571f9f44ddac46ab899b845066481f1a83769360788a7c212cc41c66b73c105c02eb30c7e8dfbbae94d0@34.133.211.115:30303",]' >  /tmp/geth_static_nodes.toml


geth\
    --eip4844\
    --config /tmp/geth_static_nodes.toml
    --http\
    --http.port=8545\
    --http.api "engine,eth"\
    --authrpc.port 8551
    
curl 'https://raw.githubusercontent.com/Inphi/eip4844-testnet/master/genesis.ssz' > ./genesis.ssz

beacon-chain\
    --eip4844\
    --genesis-state ./genesis.ssz\
    --subscribe-all-subnets\
    --min-sync-peers=1\
    --verbosity=debug\
    --http-web3provider=$GETH_RPC_URL
```

TOOD: Preset beacon genesis
The genesis files are available [here](https://github.com/Inphi/eip4844-testnet).

## Getting Devnet ETH
You can request devnet ETH on the deployed Multifaucet: https://eip4844-faucet.vercel.app/

## Uploading Blobs
Blobs can be uploaded by sending blob transactions to geth. [blob-utils](https://github.com/Inphi/blob-utils) is a handy script that makes it easy to send blob transactions:
```
blob-utils tx\
    -rpc-url <your_geth_rpc_url>\
    -blob-file <blob_file>\
    -to <to_address>\
    -value <value>\
    -private-key <account_private_key>
```

## Downloading Blobs
Blobs can be retrieved from the beacon chain network. [blob-utils](https://github.com/Inphi/blob-utils) lets you do this easily:
```
blob-utils download\
    --beacon-p2p-addr <beacon_node_p2p_address>\
    --slot <beacon block slot>
```

## Endpoints
If you don't have a node handy, feel free to use the following addresses to access the devnet.

Execution RPC:
- https://eip-4844.optimism.io

Beacon nodes:
- `/ip4/34.123.216.69/tcp/13000/p2p/16Uiu2HAm1u3vdfHLVnHRJtHDxSMYhHgrRVhKxBXLbQ99b4deM8Yq`
- `/ip4/34.171.161.213/tcp/13000/p2p/16Uiu2HAm3fx3hL8EEzu4rvW2y74FFcgq3nFoU5Dau1JdpS2JHF9W`
- `/ip4/34.123.184.76/tcp/13000/p2p/16Uiu2HAm2XQfneEyWEuAnFWsJKTEi4V1KV1P5mHPCbUS9mYAApK2`

## Troubleshooting/assistance

If you have issues running the devnet, please reach out in the `#sharded-data` channel of the [Eth R&D discord](https://discord.gg/wNT8ghMbkw). 

### When I try to run Prysm on MacOS, I get this error "Caught SIGILL in blst_cgo_init...

This error occurs on Prysm start up (on MacOS 12), and causes the program to exit:

```
Caught SIGILL in blst_cgo_init, consult <blst>/bindinds/go/README.md. 
exit status 132
```

Workaround is to run Prysm with environment variables `CGO_CFLAGS="-O -D__BLST_PORTABLE__"` and `CGO_CFLAGS_ALLOW="-O -D__BLST_PORTABLE__"`:

```
CGO_CFLAGS="-O -D__BLST_PORTABLE__" CGO_CFLAGS_ALLOW="-O -D__BLST_PORTABLE__"\
    go run ./cmd/beacon-chain\
    --eip4844\
    --genesis-state ./genesis.ssz\
    --subscribe-all-subnets\
    --min-sync-peers=1\
    --verbosity=debug\
    --http-web3provider=http://localhost:8551
```
