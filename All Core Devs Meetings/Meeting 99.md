# All Core Devs Meeting 99 Notes <!-- omit in toc -->
### Meeting Date/Time: Friday 30 Oct 2020, 14:00 UTC <!-- omit in toc -->
### Meeting Duration: 1.5 hrs <!-- omit in toc -->
### [Github Agenda](https://github.com/ethereum/pm/issues/219) <!-- omit in toc -->
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=GOWSrHtNZOQ)
### Moderator: Hudson Jameson <!-- omit in toc -->
### Notes: Edson Ayllon <!-- omit in toc -->



---

# Contents <!-- omit in toc -->

- [Summary](#summary)
  - [Decisions Made](#decisions-made)
- [1. YOLOv3 & Berlin discussion](#1-yolov3--berlin-discussion)
  - [1.1 YOLOv3 spec](#11-yolov3-spec)
    - [Besu](#besu)
    - [Geth](#geth)
    - [Nethermind](#nethermind)
    - [Open Ethereum](#open-ethereum)
  - [1.2 Discord conversation](#12-discord-conversation)
    - [Decisions](#decisions)
  - [1.3 EIP-2537 fuzzing update](#13-eip-2537-fuzzing-update)
- [2. Other updates / discussion](#2-other-updates--discussion)
  - [2.1 EIP-2938 (Account Abstraction)](#21-eip-2938-account-abstraction)
  - [2.2 Ropsten issues](#22-ropsten-issues)
  - [2.3 EIP-2666](#23-eip-2666)
- [Annex](#annex)
  - [Attendance](#attendance)
  - [Next Meeting Date/Time](#next-meeting-datetime)

---

# Summary 

<!--
## EIP Status

EIP | Status
--|--
2718, 2929, 2935 | Going into YOLOv2
2930, 2315 | Continue discussion for YOLOv2
-->

## Decisions Made

Decision Item | Decision
-|-
**99.1** | For now, 2537 is out of YOLOv3, and delayed until after the next hardfork.


---

# 1. YOLOv3 & Berlin discussion

## 1.1 YOLOv3 spec

Video | [3:59](https://youtu.be/GOWSrHtNZOQ?t=239)
-|-

Each client status on YOLOv2:

### Besu  

Merged and syncing. On YOLOv2, 2537, subroutines, access lists. Aligned with 2929 requirements. Haven't done YOLOv3 work yet. 

### Geth

Merged and syncing. Done with YOLOv2. Composite tests regenerated with Berlin named tests. Should start seeing failures within the next few days for clients who haven't been made activatable. YOLOv3 open PR. Merged 2565 PR, but not activatable. 

### Nethermind 

Merged, not syncing. Some failure on the Besu Nethermind EIP-1559 equation. For Berlin YOLOv2, will join as soon as Geth and Besu has a running version, which should be done for 2929, so soon. Still looking for what's being added. 2935, 2666. Trying to build and connect library to support modex repricing. 

### Open Ethereum

Not participating on YOLOs at the moment. 


## 1.2 Discord conversation

Video | [12:16](https://youtu.be/GOWSrHtNZOQ?t=736)
-|-

Things to figure out:
1. Do we agree that successful YOLOv3 EIPs can go into Berlin?
2. Are client teams comfortable implementing YOLOv3 in 2-4 weeks development time?
3. How comfortable are people moving forward with 2537?

2565, why not pull it into YOLOv3? The argument last time was that it was so small, there's no need to put it in. But, on the counter, it's so small, why don't we put it in? 

Besu states it will be easier to implement YOLOv3 with 2565, than without it.

Martin noted that 2537 and 2315 are linked with a certain commit hash in the specification. He asked if that's the same hash that was used in YOLOv1 and v2. It is the same. 

Once gas is redone, there needs to be benchmarking. Alex Vaslov will merge an update to the EIP to have a new commit hash for YOLOv3.

The updated spec won't change the logic, only constants. 

Besu thinks 2-4 timeframes is reasonable for YOLOv3 implemented for launch.

Geth can possibly do in 2-4 weeks. 

Nethermind is on their way, so 2-4 weeks is good for them.

Open Ethereum is not participating on YOLOv2, but will be ready in 2-4 weeks for YOLOv3. 

As for 2537, some consider EVM-384 as a safter alternative for the BLS precompiles. There are still unknowns for the EVM release date. There are also questions about how optimized EVM-384 is for gas prices on mainnet. 

**Alex Vaslov**:  Has a proposal to salvage work done with 2537 while using EVM=384. The same work, op codes, addition, subtraction, multiplication, we can migrate the precompile using these set of op codes. It can be EVM without all the functions of EVM. The functionality just hidden one layer down. 

**Martin Hoist Swende**: This proposal will capture the worst in both cases. It would reduce the concerns for consensus flaws. 

**Alex Vaslov**:  However, without numbers for performance, with how the final contract will look, we can't make judgements on this proposal. 

**Alex Vaslov**:  would like see both, in case there is something needed, we can get it immediately without waiting for another precompile. If there is an implementation that is faster, he'd like to optimize for performance.

**Martin Hoist Swende**: Wouldn't like to optimize for performance if it means adding new precompiles for each curve that would like support, if we can add the basic bricks.

**Alex Vaslov**:  In regards for "every new curve" the number of curves is very limited.

**James**: Would this already be sufficient for BLS6?

**Alex Vaslov**:  It wouldn't, because the fill size is different. However, right now, I don't know how many curves people would want to use. But I cannot project into the future.

**Axic**: In regards for BLS12 using EMV384 will be hard to achieve, there's almost a completely working implementation. It's a system to write these operations. It uses a code generation script. This way, it's easy to change how the arguments are encoded. This is almost finished, which wasn't the case when the discussion started. It is still limited to 384 bits. But the same instructions can be introduced to bigger bits, to cover more curves. 

**Danny Ryan**: Given the limited amount of people who do understand these curves, putting it into EVM might be risky, I'd be worried about the safety of putting these low level operations into EVM. In libraries, it's hard, but experts are available to audit. 

**Alex Vaslov**: Even if there is a tooling, we'd also need to worry about the safety of these tools as well. EVM 384 is progressing. The question is, how will it perform in different clients, as we've seen different performance in Go.

**Axic**: EVM 384 performance requirement has been met. Upgrading precompiles is a lengthy process. EVM updates don't need a hardfork. With complexity, the EVM 384 op codes in most cases are the building blocks which BLS12 implementations use internally. 

**Danny Ryan**: If these implementations are completed, do we have someone capable of audititng them?

**Axic**: I would say we do. I don't think it would take an order of 2-3 years. 

**Hudson Jameson**: Not to take all the time on this topic. The question wasn't if EVM384 is a good idea. But if EVM384 should replace EIP-2537 in Berlin. Otherwise, Berlin could be pushed well into next year if more discussion keeps happening. Personally, I think we should have both of them in. 

**Martin Hoist Swende**: There's a safety concern.

**Tim Beiko**: Well, there's a safety concern with both of them. Having both of them just doubles the concern. But the risk doesn't multiply in any way.

**Martin Hoist Swende**: Well it's not one to one. They both have unique attack surface.

**Alex Vaslov**: Will we take a year testing and optimizing to give users a tool as cheap as possible to use? Or we ask them to pay 3x the price.

**Hudson Jameson**: Also, Open Ethereum may have an audit for this EIP.

**Marcelo**: Yes, the audit for this may be quite expensive, so we want to be sure it's going in. 

**Hudson Jameson**: It seems people are more on the fence on it. Martin, how do these security concerns level up to security concerns on other EIPs. 

**Martin Hoist Swende**: The client implementors can't audit the EVM code, or the test cases. So, it's a big unknown. If we implement it, there may be consensus issues, which may not be the end of the world. I have a preference for having a smaller service on the platform layer, and have people build on layer 2 (EVM layer) as much as possible.

**James Hancock**: Say we do go ahead with it. It feels like this may take longer than 2-4 weeks to figure out. 

**Hudson Jameson**: How long until 384 is ready?

**Axic**: The op codes are ready. But, I guess the question is whether a pairing operation will be ready. It's really hard to tell. Based on the progress of the past 4 weeks, I really hope we should have it done by next All Core Devs. 

**Martin Hoist Swende**: That work wouldn't need any hardfork to finish. We just deploy it, right?

**Axic**: Having this pairing implementation, the reason is to have a fair comparison in terms of speed and cost. 

**James Hancock**: Let's say we decide this will not be in Berlin, but the next fork, how hard is it to remove from YOLO?

**Martin Hoist Swende**: 10 minutes.

**Danny Ryan**: When's the earliest and latest you estimate Berlin may happen?

**Hudson Jameson**: Earliest is 2-3 months. 

**Tim Beiko**: If we rush, we could get it out by mid-December. But mid-January is probably a better estimate. That's by not considering arguing about BLS. 

**James Hancock**: My concern is less the performance, but the timeline with the community. There are scaling solutions who want to use the bLS curves.

**James Hancock**: I'm leaning towards taking BLS out of Berlin, and putting it in later.

**Danny Ryan**: As far as Eth2, people want it to add verification to avoid loss of funds. This is not a pre-requisite. For genesis deposits, this won't help. So it would be in subsequent deposits. The longer term thing is Eth2 client verification inside of Eth1. That's the major one, 10-12 months out. 

**Alex Vaslov**: For this particular purpose, with addition operations that require inversion may be prohibitively expensive, about 3x, on top of suboptimal performance. Specifically on BLS aggregation.

**Danny Ryan**: It may be one transaction, out of 128, maybe 256, per 6.5 minutes. I don't know if that's cost prohibitive. 

**James Hancock**: Say the timeline is March/April of next year, does that timeline work?

**Danny Ryan**: On the longterm, yes. 

**James Hancock**: I don't feel comfortable making a decision between EIP 2537 and EVM, but will push the EIP out of Berlin because it's taking too long. It keeps holding back all the other EIPs. 

**Tomasz**: I think we should separate Berlin into 3 paths. 

**James Hancock**: Berlin may come out in December, maybe January, but BLS would come after that.

**Tomasz**: People will be pushing for additional new things. So, we may do some work in parallel. 

**Hudson Jameson**: Let's not have 2537 or EVM 384 in the next hardfork. We may do something where we split Berlin into two, as done with other hardforks. Hopefully by Berlin, we'll have a clearer way to show how people can push their EIP through the process. 

### Decisions

- **99.1**—For now, 2537 is out of YOLOv3, and delayed until after the next hardfork.


## 1.3 EIP-2537 fuzzing update

Video | [59:43](https://youtu.be/GOWSrHtNZOQ?t=3583)
-|-

Fuzzer was running on 8 cores, but bumped up to 32.

The fuzzer generates valid and invalid inputs to Fuzz the Rust against the Golang implementation. 

Ran over a week, with 270 million iterations with no issues or incompatibilies. And an additional million rounds using the Geth RPC to get the full end-to-end intregation test.

We expect to keep running this several more weeks. 


# 2. Other updates / discussion

## 2.1 EIP-2938 (Account Abstraction)

Video | [1:15:28](https://youtu.be/GOWSrHtNZOQ?t=4528)
-|-

We left off looking for feedback from last time. The author is interested in knowing what the remaining steps to be `CFI`? The author is looking to motion it into CFI the next ACD meeting.

May review in a breakout room in Eth research discord. 

## 2.2 Ropsten issues

Video | [1:22:53](https://youtu.be/GOWSrHtNZOQ?t=4973)
-|-

Very few people mine on Ropsten. If anyone decides they want to take over Ropsten, it's random what damage they do. The only thing we can do is get people to mine on Ropsten.

A few people have reached out for fixing Ropsten. 

Tomasz suggests creating a permissioned Ethash. Where it is PoW, but the block producers are under our control. That would solve the issue, otherwise, we just wait for the attacker to get bored, and it'll fix itself. 

Clients can make a list of addresses that are allowed to mine. 

Looking for someone to lead this. Will be discussed in the ACD chat, or maybe on the next agenda.

## 2.3 EIP-2666

Video | [1:28:14](https://youtu.be/GOWSrHtNZOQ?t=5294)
-|-

All developers have sent the benchmarks. The final numbers on the proposal are the status of things. Should not add any DOS attacks, but will streamline prices of operations. It's a simple constants change.

Will discuss in the next meeting. 

---

# Annex


## Attendance
- Adri Massanet
- Alex (axic)
- Alex Vlasov
- Ansgar Deitrichs
- Brent Allsop
- Danny Ryan
- Dragan Rakita
- Greg Colvin
- Guillaume
- Hudson Jameson
- James
- James Hancock
- Jim Bennett
- Kelly
- Lightclient
- Marcelo Ruiz
- Martin Hoist Swende
- Micah Zoltou
- Peter Szilagyi
- Pooja Ranjan
- Rai Sur
- Sam Wilson
- Tim Beiko
- Tomasz Stanczak



## Next Meeting Date/Time

Friday November 13, 2020 14:00 UTC
