# (e)PBS Breakout Room #15

**Note**: This file is copied from [here](https://hackmd.io/@ttsao/epbs-breakout-16)
PS: There’s an inconsistency between the meeting number listed on the agenda and the notes. Also, please note that this meeting note was sourced from [Discord](https://discord.com/channels/595666850260713488/874767108809031740/1334900847443837110).

## Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/1269

**Date & Time**: [Jan 31, 2025, 14:00-15:00 UTC](https://www.timeanddate.com/worldclock/converter.html?iso=20240213T140000&p1=1440&p2=37&p3=136&p4=237&p5=923&p6=204&p7=671&p8=16&p9=41&p10=107&p11=28)

**Recording**: https://www.youtube.com/live/IDpahX3WXxE

# Notes

- The EIP hasn't changed. As long as there's one more client implementation, we'll start opening the fork choice spec update with ePBS (Potuz).
- Taku update: A single-node setup is working, but there are issues with two-node setups that are getting close to working. (Stefan and Enrico).
- Prysm will provide a Kurtosis image to share with Teku to try multi client devnet (Potuz and Terence).
- Lighthouse update: It doesn’t have syncing gossip yet, otherwise it could run a single-node setup (Mark).
- Ethpanda ops will support Dora. We need a Beacon API and a streaming endpoint for execution payloads. Enrico will open the PR. For Dora, we also need labels to display payloads separately and indicate when a payload is missed or orphaned (Pk).
- For the sync interface, we discussed having block-by-root and payload-by-root as cleaner for serialization. For by-range, it's unclear which approach is better since blob sidecars are requested separately. Client feedback is needed.
- For the rest of the meeting, Mark discussed pre-conference trade-offs in ePBS. I won’t summarize that here—if you're interested, please check the recording.
- Hopefully, in two weeks, we'll have Prysm and Teku interop.
