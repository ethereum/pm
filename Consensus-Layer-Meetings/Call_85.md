### Meeting Date/Time: Thursday 2022/4/7 at 14:00 UTC
### Meeting Duration:  1 hour 23 minutes 33 seconds.
### [GitHub Agenda](https://github.com/ethereum/pm/issues/510) 
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=rYWF7N8tS0g)
### Moderator:  Mikhail Khalinin
### Notes: Metago

## Kiln office hours

**Mikhail**
It’s so cool. Let us get started. Yeah, it’s an honor for me to run the call. Okay, welcome to the Consensus Layer call no. 85. Thanks, for the agenda. Let’s start with the first item, which is the kiln office hours. And I will start with testnet updates, testnet and shadowforks. Pari, do you want to give an update on that front?

**Pari**
Sure. The last shadow fork we had was on Monday, that's Goerli shadow fork 3. Since the last week, we had Goerli shadow fork 2 and shadow fork 3. Shadow fork 2 just had an equal client split, , and we didn’t notice any major issues. I think Nethermind was able to figure out a few issues and Besu as well, and maybe one or two other clients, but in general, things went ok. Goerli shadow fork 3 was on Monday and we replicated mainnet client split. Since then, I think the geth team has been debugging a specific issue but its just affecting a subset of nodes, the network is still finalizing and people can try all sorts of sync tests against shadow fork 3. And just as a general announcement, shadow fork 1 and 2 will be deprecated later today, so please migrate to shadow fork 3 as soon as possible.

**Mikhail**
And what about the mainnet shadow fork?

**Pari**
Yeah. So I sent the configs for mainnet shadow fork yesterday on chat. The shadow fork is planned for Monday. I am currently syncing the nodes, and the corresponding beacon chain will be launched tomorrow. Config for everything is already on Github. There are group nodes, genesis configs, etc. 

**Mikhail**
Cool. And is anybody welcome to join the shadow fork?

**Pari**
Yeah. Feel free to join. Because it is limited to genesis validators, I am running all the validators, but the main purpose of these tests are to test sync, so anyone can sync up nodes and join in. 

**Mikhail**
Great, and yeah. Just a reminder that this is the mainnet so the disk space requirements are much higher than on Goerli, right?

**Pari**
Yup. Definitely. You have to sync up a complete mainnet node. So I do suggest if anyone wants to joi, you start now, so you have a couple of days to sync.

**Terence**
You know how big of a disk space is required for minimum, at this stage? 

**Pari**
I think about 5 / 600 gigs is enough? I have provisioned a 1 terabyte machine just to be safe. 

**Mikhail**
Got it. Thanks.

**Micah**
I mean, that depends on what node and what settings we are running, right? Nethermind, fully pruned, is under a 100 gigabyte? Maybe? Its kinda rude for the …network to run that way, but if you have to need to run something and you don’t have much space, that can work. 

**Mikhail**
Agreed. Very excited to see the first mainnet shadow fork. Is there any comment on the Goerli shadow fork that ...developers wanna make? Anybody else?

**Marius**
Yeah, so we are still investigating an issue on geth that happened on the last shadow fork and yeah, but it only happened on a small subset of nodes so if you see a bad block happening, then it might be because of the issue. 

**Mikhail**
Yeah, Is it like a...the issue is about the bad block production, or any other relations to...?

**Marius**
No. Its...a valid block group is seen as bad and yeah...

**Mikhail**
...to debug...ok, got it. Any other testing updates?

**Pari**
I just one more tiny note about the mainnet shadow fork. Just be wary when using the mainnet chain id, so when anyone's trying weird transactions etc, they might gossip to the actual mainnet and you will be wasting mainnet ether, so please be careful. By default, there will be no other transactions running on it. I don't think anyone is reimbursing me for that. 

**Mikhail**
Yeah, thats a very good note. Thanks Pari. So be aware that the shadow fork shares like a state with the mainnet so transaction on there may also be included in a block on the mainnet, so it may accordingly change what the runtime time of this transaction will be. Okay, cool. I have a small testing update. I have been working on this...document. Just dropped the link in the chat. There is  transition section that I have been focused on, in recent days, and yeah, the shape of the document, what it would look like. This transition section

**




## Attendees (30) 
- Mikhail Kalinin
- Tim Beiko
- Lightclient
- Terence
- Pooja Ranjan
- Micah Zoltu
- Lion Dapplion
- Zahary Karadjov
- Saulius Grigaitis
- Ben Edgington
- Marius
- Ansgar Dietrichs
- Paul Hauner
- James He
- Casper Schwarz-Schilling
- Hsiao-Wei Wang
- Carlbeek
- Pari & Proto
- Enrico Del Fante
- Stefan Bratanav
- Trenton Van Epps
- Cayman Nava
- Arnetheduck
- Stokes
- Dr
- Mario Vega
- Leonardo Bautista
- Marek Moraczynski
- Tukasz Rozmej
- Shana
