# (e)PBS Breakout Room #12

Note: This file is copied from [here](https://hackmd.io/@ttsao/epbs-breakout-12)

## Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/1188

**Date & Time**: [Oct 25, 2024, 14:00-15:00 UTC](https://www.timeanddate.com/worldclock/converter.html?iso=20240213T140000&p1=1440&p2=37&p3=136&p4=237&p5=923&p6=204&p7=671&p8=16&p9=41&p10=107&p11=28)

**Recording**: https://youtu.be/fs6rNxHQ3f0

Today, we were joined by Francesco, who shared the latest thinking on the [All-in-one fork choice design](https://hackmd.io/UX7Vhsv8RTy8I49Uxez3Ng?view). For a deep dive into the new design, please watch the recording, as it covers much more nuance than these notes.


### Design Motivation
- Payload and withheld boosts add complexity. Given the challenges with proposer boosts, it’s preferable to avoid them.
- Granting builder boost power feels "wrong" to begin wtih.
- The goal is to harmonize fork choice designs with major features like IL and peer DAS. All these designs share the principle of voting against blocks that don’t satisfy DA or IL requirements. ePBS supports this by preserving consensus liveness without needing execution.
- While theoretically simpler, this change may not make implementation easier. One tradeoff in this design is the need for stricter timelines (reveal 5s, freeze 10s), which requires additional testing.

### General Timeline

- New: this new design includes a freeze period, but it’s relevant mainly for peer DAS and IL.

### Discussion of Roles
We then walked through the roles of builder duty -> proposer duty -> attester duty -> AC (formerly PTC) duty.

- **Builder Duty**: The new payment processing logic is delayed until n epochs after chain finalization. This adds some complexity to consensus beacon state, but Potuz pointed out that even in the current design, payment should be delayed to prevent misuse by proposers/builders following slashing.
- **Proposer Duty**: The new freezing logic ensures that proposers don’t sample DA and provides enough buffer to meet IL requirements. In cases of AC vote equivocation, the proposer's AC vote is given canonical preference.
- **Attester Duty**: This role remains largely the same as today’s EIP-7732.
- AC Duty: Similar to attester duty, with minimal changes in the context of EIP-7732.

### Next Steps
To conclude, we outlined next steps with devnets already in progress:

- The new design has sufficient support so far. Potuz will open the consensus spec with eip7732-only changes shortly after devnet.
- The devnet will proceed as planned, with a focus on testing the minimal viable function of pipelining.
- **Consensus spec changes**:
  - The payload envelope will look different without withheld elements
  - Payload attestation will be updated
  - Beacon state will now track attestation votes
- Validator and builder guides will undergo minor updates
- The fork choice spec will see major changes due to a new format
