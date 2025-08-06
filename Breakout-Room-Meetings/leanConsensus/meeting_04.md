# leanConsensus (fka beam chain) call #4: research updates | exit queue

**Prev:** [Call 03](https://github.com/ethereum/pm/blob/master/Breakout-Room-Meetings/leanConsensus/meeting_03.md)

**Meeting Date/Time:** Friday 2025/4/18 at 14:00 UTC

**Meeting Duration:** 1 hour

[GitHub Agenda & Links to Presentations](https://github.com/ethereum/pm/issues/1446)

[Audio/Video of the meeting](https://youtu.be/M6oRqhjMFQc)

Moderator: Justin Drake

Facilitators: Ladislaus von Daniels & Will Corcoran
- Facilitator emails: ladislaus@ethereum.org // will@ethereum.org
- Facilitator telegrams: @ladislaus0x // @corcoranwill

## Agenda

| Agenda Item | Topic |
| --- | --- |
| 01 | Social Layer Updates by @justindrake |
| 02 | Minslack: Proposal to Add Flexibility to Ethereum's Exit Queue by @michaelneuder and [Mallesh Pai](https://x.com/malleshpai) |


## 01: Social Updates by @justindrake

| Topic | Subtopic | Details |
|-------|----------|---------|
| beam Roadmap Updates | Schedule | - Added more information to 2025 tentative schedule<br>- First half of 2025 (Q1-Q2): Research updates<br>- beam day Cannes on June 29th<br>- Upcoming calls: APS with Julian, 3SF with Roberto/Francesco/Luca<br>- May 30th tentatively for Rainbow Staking (Call #7) |
| | Second Half 2025 | - Dedicated to specification development<br>- Start with subspecs for specific modules<br>- Develop holistic spec toward end of year<br>- November Beam Day in Buenos Aires during Devconnect<br>- Possible final call on December 26th (Boxing Day) |
| beam day Cannes | Logistics | - Luma registrations now open<br>- Limited to approximately 60 spots<br>- Precedence given to researchers and developers<br>- Takes place one day before ECC starts on June 29th |


## 02: Minslack: Proposal to Add Flexibility to Ethereum's Exit Queue by @michaelneuder and [Mallesh Pai](https://x.com/malleshpai)

| Topic | Subtopic | Details |
|-------|----------|---------|
| Exit Queue Research | Background | - Speakers: Mallesh and Mike<br>- Academic paper published June 2024<br>- EIP published March 2025<br>- ethresear.ch post published April 2025<br>- Aligns with beam chain principles of simplicity and optimality |
| | Overview | - Exit queue importance highlighted by discussions around staked ETH ETFs<br>- Research examines implications of long exit queues<br>- Presentation will start with academic results followed by practical implications |
| Theoretical Background | Accountable Safety | - Definition: If inconsistency occurs, a fraction of validators can be identified as having provably violated protocol<br>- Foundation for economic security in proof-of-stake<br>- Tension between static validator model and need for entry/exit |
| | Decreasing Security | - Economic security/accountable safety of finalized transactions decreases over time<br>- If validators exit before violation is detected, they can't be held accountable<br>- Rate of decay is slow but real |
| | Validator Set Consistency | - Can be expressed as constraints (e.g., "no more than 10% stake can exit within 7 days")<br>- These constraints ensure accountable safety |
| `minslack` | Algorithm | - a) At each period, look backward in time to process as many withdrawals as possible within constraints<br>- b) Greedily process withdrawals while maintaining system's safety invariants |
| | Example | Example constraints:<br>- a) 3 units stake can leave in last 4 periods<br>- b) 5 in last 10 periods<br>- c) 15 in last 20 periods<br>Calculates "slack" for each constraint and takes minimum value |
| | Optimality | - minslack is optimal under common values (when all validators have same disutility from waiting)<br>- Not optimal with heterogeneous time preferences |
| | Priority minslack | - Enhanced version that respects priority and accounts for future option value<br>- Performs well in numerical simulations |
| Current Ethereum Setup | 1) Withdrawal Flow | Four timestamps:<br>- a) voluntary exit initiation<br>- b) exit epoch<br>- c) withdrawable epoch<br>- d) withdrawal processing<br>Gap between exit and withdrawable epochs for slashability period (27 hours)<br>Rate-limited FIFO queue (16 validators per epoch) |
| | 2) Sweep Mechanism | - a) Every validator gets withdrawals processed in round-robin fashion<br>- b) Processes partial withdrawals automatically<br>- c) Takes approximately 9.2 days to complete a full sweep cycle |
| | 3) Pectra Changes | - a) EIP-7251 changes denomination to ETH instead of validator count<br>- b) Allows compounding stake (opt-out of automatic partial withdrawals)<br>- c) Validators can trigger exits from withdrawal address |
| Proposal: Single Constraint `minslack` | Design | - Single constraint instead of many (e.g., "no more than 5% stake exits in 2 weeks")<br>- Uses retrospection (looking backward) instead of forward-looking constraints<br>- Maintains rolling window where constraint is always satisfied |
| | Implementation | - Uses exit churn vector with 16 generations (27 hours each)<br>- Simplifies accounting by tracking generations rather than epochs<br>- Determines available slots based on historical usage |
| | Technical Details | - Maps exits to future generations due to existing Ethereum exit architecture<br>- A cleaner approach would maintain pending exit state |
| Recommendations for beam chain | Key Changes | - Remove or separate partial withdrawal sweep<br>- Implement single constraint `minslack`<br>- Consider priority fee ordering for withdrawals<br>- Carefully design integration with execution layer |
| | Priority Fees | - Allow users to bid for faster exits<br>- Suggests implementation through execution layer contract<br>- Market design questions on fee distribution |


| Question/Topic | Response/Notes |
|----------------|----------------|
| 1) Cost functions for disutility | - Discussion around linearity assumption in disutility model<br>- Possible alternatives to linear disutility (exponential, constant+exponential)<br>- One defense of linearity: outside options like borrowing ETH with interest rates |
| 2) Historical data analysis | - Question about running algorithm on historical data<br>- Only one period where exit queue exceeded one day<br>- Primary concern is preparing for potential mass exodus scenarios<br>- Could test on testnets with large queues |
| 3) Slashing detection timing | - Average attester slashing detection time is about half an hour<br>- Current 27-hour delay between exit and withdrawable epochs may be overly cautious<br>- Made without empirical slashing data when PoS was implemented |
| 4) Entry queue improvements | - Similar principles could apply to deposit/entry queue<br>- Entry queue has had longer waits historically (2-3 weeks after withdrawals activated)<br>- Rate limiting entries prevents validator set from changing too quickly<br>- Influences finality and fork choice |
| 5) Implementation in Ethereum vs beam | - Most suggestions could be implemented as Ethereum hard forks<br>- However, core devs may prioritize user-facing rather than validator-facing changes<br>- After EIP-7251 complexity, appetite for exit queue changes may be limited<br>- beam chain provides opportunity for ground-up redesign |
| 6) Generation boundaries | - Generations used to minimize state bloat<br>- Concern about spikiness at generation boundaries<br>- Engineers requested avoiding work at every epoch boundary<br>- beam aims to reduce arbitrary timeframes and process everything slot-by-slot |
