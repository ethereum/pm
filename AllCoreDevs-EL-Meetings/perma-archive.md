## Synopsis
The "All Core Devs Meetings" repository on [Permacast](https://permacast.dev/#/podcasts/Dx0lrz1eCh00Xbfqsfx3IHUU7wmBqI4GiwKthEFBS7k) is a repo that archive permanently the audio recordings of [AllCoreDevs-Meetings](https://github.com/ethereum/pm/tree/master/AllCoreDevs-Meetings). 
The purpose of this is to preserve the historical and valuable core developers discussions and save it from getting vanished (probably) from the web2 hoting services. The audio files are stored on the Arweave network.

## Links
- [Archiving Repository]([https://permacast.dev/#/podcasts/Dx0lrz1eCh00Xbfqsfx3IHUU7wmBqI4GiwKthEFBS7k](https://www.permacast.app/podcast/lM27ylbkuBctxlit4kD71cSRvnXrMCSwgIGKNu2XRC4#start)). Status: ongoing
- Data uploader(s) / Repo Maintainer(s): [AeK_9yb3f3HEK1Gzwky6tIx8ujW9Pxr_FkhCkWftFtw](https://viewblock.io/arweave/address/AeK_9yb3f3HEK1Gzwky6tIx8ujW9Pxr_FkhCkWftFtw)
- Arweave mentions by ethereum.org. [link](https://ethereum.org/en/developers/docs/storage/)

## Guide for Repo Maintainers
This section is only for the podcast maintainers (that have the JWK) to enlight how to add a new episode.

### Requirements to upload a new episode:
- [Arweave wallet](https://arconnect.io) || The JWK file
- Using the maintainer wallet `AeK...Ftw`
- The episode's audio file. Supported MIME type: `audio/*`

### Upload a new episode: 
The methods are stated below assuming you have the `AeK...Ftw` wallet's JWK

#### Method 1
This is the simple non-technical method to upload a new episode via [permacast.dev](https://permacast.app) frontend

Steps:
- Navitgate to the [podcast's page](https://www.permacast.app/podcast/lM27ylbkuBctxlit4kD71cSRvnXrMCSwgIGKNu2XRC4#start) & click `add new episode`
- add the episode's name & description, then upload the audio file
- click `Upload` are you are done! 

#### Method 2
This method guide you on how to interact with Permacast's protocol via [MEM](https://mem.tech) CLI

Pre-requirements:
- [MEM CLI](https://github.com/decentldotland/mem-cli) installed (npm package)
- Audio file's TXID: uploaded to Arweave via the [JS lib](https://github.com/ArweaveTeam/arweave-js) or [ardrive (non-technical UX)](https://ardrive.io)

Steps:

- Open your terminal and run the following command

```
mem write --functionId umgZPnh_b_AfHHk9x4eCcFGy6QF0OYd9_7oe5ki3Afs --inputs "{'function': 'addEpisode', 'pid': 'lM27ylbkuBctxlit4kD71cSRvnXrMCSwgIGKNu2XRC4', 'name': 'EP NAME', 'desc': true, 'content': 'AUDIO-FILE-TXID', 'jwk': 'Arweave_JWK', 'sig': 'Arweave_Signature'}"
```
