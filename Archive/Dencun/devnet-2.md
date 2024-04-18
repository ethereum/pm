# Proto-Danksharding (EIP-4844) Devnet **v2** User Guide
**note**: this file was copied from [here](https://hackmd.io/@inphi/SJKLtgJXs) for reference.

- Proto-Danksharding (EIP-4844) Devnet v2 User Guide
    - [What's Changed?](https://github.com/poojaranjan/pm/new/master/Archive/Dencun#whats-changed)
    - [Peering](https://github.com/poojaranjan/pm/new/master/Archive/Dencun#peering)
    - [Getting Devnet-2 ETH](https://github.com/poojaranjan/pm/new/master/Archive/Dencun#getting-devnet-2-eth)
    - [Uploading Blobs](https://github.com/poojaranjan/pm/new/master/Archive/Dencun#uploading-blobs)
    - [Downloading Blobs](https://github.com/poojaranjan/pm/new/master/Archive/Dencun#downloading-blobs)
    - [Public Endpoints](https://github.com/poojaranjan/pm/new/master/Archive/Dencun#public-endpoints)
    - [Troubleshooting/assistance](https://github.com/poojaranjan/pm/new/master/Archive/Dencun#troubleshootingassistance)
    - [Known Issues](https://github.com/poojaranjan/pm/new/master/Archive/Dencun#known-issues)
    

## What's Changed?
Please read through this document carefully as there have been some changes since the first Devnet. Here's a summary:
- The geth and beacon clients have been updated
- New geth and beacon genesis
- Some beacon chain and execution networking parameters have changed
- New geth/prysm bootstrap node addresses
- Blob-utils has been updated to support Devnet v2

## Peering

To join the network, you'll need to build and install the following geth and prysm forks:
* geth - https://github.com/mdehoog/go-ethereum/tree/eip-4844-devnet-2
* prysm - https://github.com/Inphi/prysm/tree/eip-4844-devnet-2

Both geth and prysm contain preset configuration for the Proto-Danksharding network. Similar to the way geth/prysm can be configured for testnets using `--goerli` or `--ropsten`, you can configure both using `--eip4844`.

```
echo '[Node.P2P]
StaticNodes = ["enode://fdefa8b36717bd246ce338e952a3b949e608158d06c74c8b9e207439f70bfc63da27b7a4c4161a14722f7d4a256fda9c93a6dd5c26624b6a523dca2cd852ad97@34.121.33.53:30303","enode://13f2c3f2811231c384cbea2690e769321a4804a2eafb2e4c656f76c7e52624fffcfbc2a52a0a932b4dde0b321f29fb9229777126a91db9b10b26dfa2d93ce32b@34.122.190.151:30303","enode://71475ca7e915bfbe9958688fa3d5af127a0353ead52a2fff1216d374a5b8dd6a67ced237a9b52b1b9cb1a90160ce2019eaacfacbf750ecbeba8e0f439b7f930b@34.173.8.43:30303",]' >  /tmp/geth_static_nodes.toml


geth\
    --eip4844\
    --config /tmp/geth_static_nodes.toml\
    --http\
    --http.port=8545\
    --http.api "engine,eth"\
    --authrpc.port 8551
    
curl 'https://raw.githubusercontent.com/Inphi/eip4844-testnet/devnet-2/genesis.ssz' > ./genesis.ssz

beacon-chain\
    --eip4844\
    --genesis-state ./genesis.ssz\
    --subscribe-all-subnets\
    --min-sync-peers=1\
    --verbosity=debug\
    --http-web3provider=$GETH_RPC_URL\
    --peer=enr:-MK4QFURnlP5nu_JHdrj6XVYPo4an3tLVD3Ii_hLpFxAvdaVVLOOHPzmAYQQ4lk1U2fwb4oQIh-lYL3UbpTGYr-yJjKGAYO2dGzih2F0dG5ldHOIAAAAAAAAAACEZXRoMpCcZxEogwAP_f__________gmlkgnY0gmlwhCJ5ITWJc2VjcDI1NmsxoQIlwaxycUgJ_Ht4lYdDlInbIuRxu0HcHcFbu0D7As2SLYhzeW5jbmV0cwCDdGNwgjLIg3VkcIIu4A \
    --peer=enr:-MK4QCC-n6C8hHOsUacSgYR7E2UknE_Slz5Tt8h0FiSKxiXDBrki2iwIALq9FIPreXp2GgFJqFM4Bd-1oMlrHgOPKY2GAYO2dG08h2F0dG5ldHOIAAAACAAAAACEZXRoMpCcZxEogwAP_f__________gmlkgnY0gmlwhCJ6vpeJc2VjcDI1NmsxoQNJzjxNKr7-a-iEDs0KvaL_vo1UH91kefEiWzgAdwSntYhzeW5jbmV0cw-DdGNwgjLIg3VkcIIu4A
```

The genesis files are available [here](https://github.com/Inphi/eip4844-testnet/tree/devnet-2).

Alternatively, you can easily get started using this handy docker-compose [setup](https://github.com/mdehoog/eip4844-testnet).


## Getting Devnet-2 ETH
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

## Public Endpoints
If you don't have a node handy, feel free to use the following addresses to access the devnet.

Execution RPC: https://eip-4844-alpha.optimism.io

Beacon nodes:
- `/ip4/34.121.33.53/tcp/13000/p2p/16Uiu2HAkwy4MJBLsCvmuPwrfVX9GqNiGeppshnsbn2BgKskCtRDE`
- `/ip4/34.122.190.151/tcp/13000/p2p/16Uiu2HAmHd6WSHUEB7SrxdDR8dPVLTJqkzgPGbriej15udyQZugY`
- `/ip4/34.123.117.254/tcp/13000/p2p/16Uiu2HAmSLVoxaR1ztHqBjezWFSvFa3HeTWPZNswfS4aMWob59L6`

## Troubleshooting/assistance

If you have issues running the devnet, please reach out in the `#sharded-data` channel of the [Eth R&D discord](https://discord.gg/wNT8ghMbkw).

## Known Issues
- BeaconBlock merkleization is incorrect iff it contains a non-zero amount of KZG commitments. This bug doesn't affect normal user interaction with the devnet. But alternative clients may find it difficult to sync with the devnet.
