# Berlin Retrospective
To describe the process of preparing, activating and error handling during the Berlin upgrade.

## OpenEthereum Mainnet Consensus Issue

OpenEthereum's postmortem on the consensus issue can be found [here](https://docs.google.com/document/d/18BhIEB7V_f_GkL8NZptxq-xadu5sb8QUzego8YVVMUM/edit#). 

### Problematic Block Information
* Date and time (in UTC): Apr-15-2021 11:05:04 AM +UTC
* Block Number (Mainnet): 12244294
* Block Hash (Mainnet): 0x53c7b43c15c489b012053d156bc5ef95f3f5d498c2d01a0a3d9f3cc1dd007601
* Transaction: 0x7006f38fa2e6654fae1a781aefc5885fe0cb8f778b1add10636eaf7e34279247

### Timeline of Events

**April 15, 2021 (all times in UTC)**
* 11:12 AM: ["I think etherscan just went down"](https://discordapp.com/channels/595666850260713488/745077610685661265/832211783883423754) shared in Eth R&D discord by `Agusx1211`
* 11:17 AM: ["all our openethereum nodes just died"](https://discordapp.com/channels/595666850260713488/745077610685661265/832211783883423754) shared in Eth R&D discord by `Peter [beaconcha.in]`
* 11:30 AM: [Confirmation](https://discord.com/channels/595666850260713488/745077610685661265/832216373312618508) by `denisgranha` from the OpenEthereum team that OpenEthereum nodes are having an issue and that the team is investigating it.
* 12:21 PM: [Zoom link shared by OpenEthereum](https://discord.com/channels/595666850260713488/745077610685661265/832229172126547998) for other developers to help find the issue.
* 12:41 PM: Potential fix for the bug identified, [PR opened](https://github.com/openethereum/openethereum/pull/364).
* 12:41 PM - 3:30 PM: Testing of potential fix by deploying against nodes and syncing to the head of the chain. Preparation for official release.
* 3:36 PM: [Confirmation](https://twitter.com/OpenEthereumOrg/status/1382752559073529856) that the potential fix is working.
* 5:47 PM: [Announcement](https://twitter.com/OpenEthereumOrg/status/1382752559073529856) of OpenEthereum v3.2.3 which contains the fix for the issue.


### Suggested Corrective Action
[Discord Suggestion](https://discordapp.com/channels/595666850260713488/745077610685661265/832280444967190559):
> Client tests must be run against mainnet spec **directly**. Having separate test spec and mainnet spec could be the reason for slippage as fuzzing can't catch this bug.
> It probably increases CI time and extra development effort, since it needs to take into consideration of the whole mainnet genesis block, and will probably have to fake block numbers so that it passes the activation block. But it is important because The test spec or the ropsten spec doesn't have non-active precompile definitions.

On [AllCoreDevs 110](https://youtu.be/-H8UpqarZ1Y?t=732), a longer conversation about testing process improvements to catch such bugs in the future was had. The idea of having chain configurations on Hive be identical to mainnet was also noted as the only way to catch such an issue.

### Resources

A detailed Twitter thread about the issue: https://twitter.com/ralexstokes/status/1382750001026146304l.

## Besu Testnet Consensus Issue

TBA.

## Berlin Planning

### Upgrade summary
* Date and time (in UTC): Apr-15-2021 10:07:03 AM +UTC
* Block Number (Mainnet): 12244000
* Block Hash (Mainnet): 0x1638380ab737e0e916bd1c7f23bd2bab2a532e44b90047f045f262ee21c42b21
* Mined by: 0x1ad91ee08f21be3de0ba2ba6918e714da6b45836 (Hiveon Pool)

### Process of EIP selection

Berlin upgrade was following process described in [Shedding light on the Ethereum Network Upgrade Process](https://medium.com/ethereum-cat-herders/shedding-light-on-the-ethereum-network-upgrade-process-4c6186ed442c).

### Timeline - Backlog check
- May 15, 2020: Proposal, decision and initial selection of EIPs for Berlin to spin up an [ephemeral testnet YOLO](https://medium.com/ethereum-cat-herders/yolo-an-ephemeral-test-network-for-ethereum-356d43179b1a) in [ACD 87](https://www.youtube.com/watch?v=bGgzALuyY3w&t=4788s)
- May 19, 2020: [Meta EIP-2657](https://eips.ethereum.org/EIPS/eip-2657) created for ephemeral testnet YOLO
- May 29, 2020: Selection of EIPs, a decision on the state-test name as Yolo-v1 (and not Berlin) in [ACD 88](https://github.com/ethereum/pm/blob/5198ef636a0f2c443a5c99374563ef285b002b0e/All%20Core%20Devs%20Meetings/Meeting%2088.md#decisions-made)
- June 03, 2020: Finalized spec of EIPs for v1, commit hash [added](https://github.com/ethereum/EIPs/pull/2657/commits/fb2a20f2d87a272edf0925f1e347b36644268f9b) to YOLO meta EIP
- June 03, 2020: Yolo v-1 deployed with [Geth](https://twitter.com/peter_szilagyi/status/1268123563850170368)
- Jun 10, 2020: [Open Ethereum](https://twitter.com/vorot93/status/1270597961014218752) and [Besu](https://github.com/hyperledger/besu/pull/1051) joined the network.
- June 10, 2020: [YOLO stopped](https://twitter.com/peter_szilagyi/status/1270824487886426113). It went out of disk.
- June 11, 2020: YOLO is back as [YOLT (You only live twice)](https://twitter.com/peter_szilagyi/status/1270931154267504643)
- June 12, 2020: Restarted at AWS cloud
- June 12, 2020: Proposed EIPs for Yolo v2 in [ACD meeting 89](https://github.com/ethereum/pm/blob/master/All%20Core%20Devs%20Meetings/Meeting%2089.md#3-yolo-testnet-update)
- June 22: [yolov1 sealer/bootnode](https://gitter.im/ethereum/AllCoreDevs?at=5ef07f5cfa0c9221fc5288f9) is up with a new IP
- September 18: yolov2 EIP selection in [ACD 96](https://github.com/ethereum/pm/blob/master/All%20Core%20Devs%20Meetings/Meeting%2096.md#decisions-made)
- October 30, 2020: EIP-2537 is not considered for yolov3, and will be delayed until after the next hardfork, decided in [ACD 99](https://github.com/ethereum/pm/blob/master/All%20Core%20Devs%20Meetings/Meeting%2099.md#decisions-made)
- November 27, 2020: EIP-2930 & EIP-2718 added to Berlin EIPs, decided in [ACD 1010](https://github.com/ethereum/pm/blob/master/All%20Core%20Devs%20Meetings/Meeting%20101.md#summary)
- March 08, 2021: Ethereum Berlin Upgrade [Announcement](https://blog.ethereum.org/2021/03/08/ethereum-berlin-upgrade-announcement/)
- Mar 10, 2021: Ropsten at block #9 812 189
- Mar 17, 2021: Goerli	at block #4 460 644
- Mar 24, 2021: Rinkeby	at block #8 290 928
- Apr 15, 2021: Mainnet	at block #12 244 000
