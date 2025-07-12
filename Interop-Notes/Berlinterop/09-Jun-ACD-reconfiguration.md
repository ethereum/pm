## Resources

- [Pre-read](Slides-notes/09-Jun-ACD-reconfiguration-preread.pdf)

## AI-generated notes

### Summary

* The group reviewed how *headliner* EIPs are currently selected and agreed that explicitly decoupling **“choose the headline”** from **“fill the rest of the fork”** would improve decision quality.
* Existing “headline submission” templates have not prevented weak or redundant proposals; clearer evidence of urgency, affected stakeholders, and expected impact is still required.
* Participants debated which signals should drive headline selection: core‑dev consensus, open community polling, structured “protocol‑research” roadmap calls, or direct outreach to L2s, wallets, roll‑ups and application teams.
* Several argued for a single, well‑advertised annual “road‑mapping call” where *all* stakeholders can advocate for problems to solve, while others warned a giant call is exclusionary and unmanageable.
* A recurring theme was the absence of a **product‑owner function**: some favoured letting the Ethereum Foundation supply an initial roadmap (“baseline to push against”), others feared EF gate‑keeping and want a public “problem backlog” curated by a neutral working group.
* Roll‑up, staking‑provider and application representatives stressed they can surface pain‑points but lack capacity to champion them long‑term; the process must solicit, track and re‑surface outstanding issues.
* There is broad agreement on three strategic goals: **scale L2 (PeerDAS / blobs), scale L1 (higher gas / cheaper op‑codes) and UX & interop improvements**, but concern that AllCoreDevs (ACD) reached those goals through ad‑hoc, private outreach rather than a transparent process.
* On **timeline discipline**, the group recognises a three‑way trade‑off: *scope ‑ time ‑ quality*. Nobody will sacrifice safety, so either scope or schedule must move.
* History shows that major upgrades (1559, Merge, 4844) shipped only when the single headline was ready; fixing dates too early often forced repeated slips.
* Fast‑follow forks were deemed unrealistic unless strictly limited to “parameter only” changes (e.g., gas‑limit bump, pre‑compile pricing).
* Resource constraints persist: EL/CL client teams are small (often ≤10 engineers) and already behind on maintenance; tighter feedback loops require more engineers, not more meetings.
* Polls at the end revealed no consensus: some favour a fixed 6‑month cadence even if the headline drops, others prefer keeping the headline even if that pushes to 9‑12 months.
* Immediate open questions:
  * Should Fusaka (blob gas limit raise + PeerDAS) ship in 2025‑Q3 no matter what, or slip if gas‑repricing work expands?
  * How and when to lock Glamsterdam scope (ePBS, block‑access‑lists, etc.) and publish a realistic target date?

### Chronological notes

* **Opening & agenda**

  * Two topics: *improving headline/EIP decision quality* and *coordination & timelines* for upcoming forks.

* **Why headline selection matters**

  * Picking the wrong centerpiece wastes effort and adds upgrade risk; historically successful forks rallied around a single clear goal (Merge, 1559, 4844).
  * Proposal: make headline choice explicit and require a richer template (impact, beneficiaries, urgency).

* **Evidence that current template is insufficient**
  * Recent headline submissions (EOF re‑proposal, CL execution quality proposal) lacked context and re‑ignited old debates, showing no quality uplift.

* **Which signals should count?**

  * Option A: continue relying on core‑dev consensus (“cords decide”).
  * Option B: crowd‑source from “the community” – but who qualifies? Twitter polls and open forum posts risk bias.
  * Option C: elevate “protocol‑research roadmap calls” as an upstream venue to debate priorities before ACD touches specifics.

* **Call‑based outreach idea**

  * Suggestion: announce one mega‑call per fork a month in advance, invite *everyone*, and decide the headline live.
  * Pushback: single call excludes unavailable contributors, favors loud voices, and may devolve into 300‑person chaos.

* **Alternate outreach**

  * Proactively solicit L2s, wallets, Solidity, infra, etc. for proposals; possibly rotate who leads the discussion (e.g., L2‑hosted sessions).

* **“Who is the product owner?” discussion**

  * View 1: EF should own product direction, present three strategic priorities, let ACD critique.
  * View 2: That concentrates power; EF‑funded contributors should speak only as individuals.
  * View 3: Regardless, Ethereum lacks marketing, user‑research and technical‑writing resources to convert raw ideas into actionable EIPs – those functions must be staffed.

* **Gate‑keeping vs openness**

  * Some fear EF filtering will hide dissenting ideas; others fear zero filtering invites spam or capture (large exchanges requesting KYC op‑codes).

* **Need for sustained champions**

  * Stakeholders can describe pain (e.g., 4 KB calldata limit, signature UX), but cannot attend ACD every fortnight; a process must keep issues alive until solved.

* **Capturing signals without noise**

  * Too much friction deters input; too little invites DoS‑level proposal floods. Continuous, structured interviews (one‑on‑one) may outperform giant public calls.

* **Coordination & timelines segment**

  * External ecosystem values predictable schedules, but fixed dates clash with headline readiness.
  * Quality is non‑negotiable; only scope or schedule can flex.
  * PeerDAS example: would it have been better to ship a PeerDAS‑only fork instead of bundling extras into Pectra?

* **Hard‑fork cadence trade‑off**

  * Proposal: lock content once “next devnet” launches; anything not in DevNet‑N waits.
  * Gas‑limit raise and pre‑compile repricing surfaced as additions that might derail Fusaka timeline.

* **Fast‑follow forks reality check**

  * Parameter‑only mini‑forks (BPO) could work; “full” fast‑follows fail because every group stuffs extra features once the door is open.

* **Gas‑repricing debate**

  * Benchmarking shows some pre‑compiles under‑priced; repricing could require app‑layer changes (e.g., wallets with hard‑coded gas estimates).
  * Decision deferred: team will study impact and report by week‑end; fork scope may adjust accordingly.

* **Man‑power & feedback loops**

  * Each client team only has \~7‑10 core engineers.
  * More calls cannot replace headcount; scaling teams (QA, benchmarking, release) is prerequisite to faster cadence.

* **Setting Fusaka ship date experiment**

  * Straw‑poll windows (Aug 1, Sep 1 … Jan 1) revealed spread; most expect post‑Devconnect 2025 (Nov‑Dec) if scope unchanged.

* **Timeline vs headline poll**

  * Question posed: should Ethereum commit to a fixed date and drop the headline if late?
    * Minority favoured “ship on time even if empty”.
    * Majority prefer “keep headline, slide schedule”; real goal is *both* but safety wins over optics.

* **Suggested next steps**

  * Use the current in‑person week to:
    * Finalise Fusaka scope (PeerDAS + minimal extras) and decide on repricing.
    * Draft a transparent process for headline intake, signal weighting, and cadence target (6 m vs 12 m).
    * Identify resourcing gaps (client engineering, testing, writing, product research) and propose funding.

### Relevant links

- EthMag: [Reconfiguring AllCoreDevs](https://ethereum-magicians.org/t/reconfiguring-allcoredevs/23370?u=nixo)
- EthMag: [Community Consensus, Fork Headliners & ACD Working Groups](https://ethereum-magicians.org/t/community-consensus-fork-headliners-acd-working-groups/24088?u=nixo)