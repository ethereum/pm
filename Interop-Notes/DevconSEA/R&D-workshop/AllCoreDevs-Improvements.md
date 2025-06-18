# AIP: AllCoreDevs Improvement Proposals 

**Summary:** Retrospective on Pectra, broader potential process changes for AllCoreDevs and follow ups from the Nyota Interop session. 

**Facilitator:** Tim Beiko

**Note Taker:** Trent Van Epps

**[*Required*] Pre-Reads:** 

* (Post Kenya Interop) [AllCoreDevs, Network Upgrade & EthMagicians Process Improvements](https://ethereum-magicians.org/t/allcoredevs-network-upgrade-ethmagicians-process-improvements/20157)
* (2022) [Bogota R&D Workshop Slides](https://drive.google.com/file/d/1X4Qwgsi0836PClvu5_oIUEFeIDQoZ88W/view?usp=sharing)
* (2021) [ACD's thoughts on ACD](https://hackmd.io/@timbeiko/acd-feedback)

## Action Items 

- [ ] Tim to draft a proposal for a "Declined from Inclusion" status, to allow teams to formally reject a proposal from a fork 
- [ ] Tim to draft a proposal to include non-consensus changes (e.g. EIP-4444) to network upgrade Meta EIPs as a way to prioritize them alongside consensus changes. The upgrade date would be the latest possible date by which we expect teams to ship the change, but they could start deploying it before. 
- [ ] Nico to host a session to discuss EthMagicians UX feedback 
- [ ] Rough agreement to better formalize the CFI -> Devnet -> SFI flow, but not enough time to iron out specifics. 
    - Need to differentiate "fork devnet" vs. "random EIP devnet" to avoid EIPs sneaking in upgrades just because they have a devnet. 

### Open Questions
- Is it worth having a more formal mechanism to track issues/questions about specific EIPs? 
    - Idea: tag on EthMagicians `discussion-to` comments that a bot can aggregate into the main topic thread. 

## Agenda 

The session will be broken into three sections: 
1. Tim's perspective on the various ACD improvment efforts 
2. Collective discussion about most important things we _should_ be doing
3. Practical proposals for ACD Process Improvements 

### Tim Perspective 
_note: treat these as a rough braindump which I'll expand on at the session_

* Sync vs. async culture: most improvements proposed are async, but fail to be adopted. 
* Roadmap vs. "Implementation details": desire to split both these convos, but hard to isolate in practice. 
    * TradCo solution: "eng mgmt sets roadmap, others work on tickets"
* Bottlenecked on high context ppl, otherwise rehash forever 
    * More and more, high context ppl are outside ACD! 
* "High Hanging Fruits": most things we consider have significant tradeoff, and more people to align around them. 

### What _should_ ACD focus on? 


<details> <summary>Next Fork vs. Endgame Mentality</summary>
    
![](https://storage.googleapis.com/ethereum-hackmd/upload_5559e95e25be41c27522a4fe50a2ef88.png)

</details>

<details> <summary>Hard Forks vs. Other Improvements</summary>
    
![](https://storage.googleapis.com/ethereum-hackmd/upload_5546123555cc8c82d2db128aeac0d9e9.png)

</details>


<details> <summary>Providing Value vs. Reducing Risk</summary>
    
![](https://storage.googleapis.com/ethereum-hackmd/upload_589133fb64adab4c140e34906a80d942.png)

</details>


<details> <summary> Ossification vs. Functional Escape Velocity </summary>

![](https://storage.googleapis.com/ethereum-hackmd/upload_3fbd5c52dcbf0d2ea80aedb0c71e03dc.png)
</details>

### Practical Proposals 

* `Rejected for Inclusion` status on EIPs, implying we don't discuss the idea again until the next fork 

## Notes (edited with ChatGPT for clarity)

**Summary**

The workshop centered on evaluating and enhancing the AllCoreDevs (ACD) process, reflecting on past improvement efforts, and discussing practical proposals for future enhancements. Key themes included the challenges of synchronous versus asynchronous communication, the asymmetry in the Ethereum Improvement Proposal (EIP) process, and the tension between focusing on immediate upgrades versus long-term development goals.

Participants acknowledged the limitations of synchronous calls due to global time zone differences and debated the effectiveness of asynchronous methods like written stances or pre-call discussions. While synchronous communication is valuable for decision-making, there was consensus that improvements are needed to make it more inclusive and efficient.

The group discussed the lack of a clear separation between roadmap planning and implementation details within ACD, noting the difficulty without a typical corporate structure. The asymmetry in the EIP process was a significant concern, where EIP champions are motivated to push proposals, but critics lack incentives to consistently oppose them. Introducing a "Rejected for Inclusion" (RFI) status for EIPs was proposed to provide clearer feedback and prevent unproductive cycles.

Balancing immediate hard fork preparations with long-term planning was also a focal point, acknowledging that the community often seeks certainty about the future but struggles with long-term commitments. The role of non-consensus changes, potential voting mechanisms, and the need for better documentation and communication platforms were discussed to enhance the ACD process.

---

**Workshop Notes**

- **Tim** doesn't like synchronous calls; they're a good forcing function but have limitations.
- **Roadmap vs. implementation details**: There's no clear high/low-level distinction like in corporate structures.
- **Speedrunning arguments**: Questioned if anyone can quickly navigate complex past discussions (e.g., BLS in 2018/19).
- **High-hanging fruits**: Proposals like FOCIL and ePBS have nuanced trade-offs, making consensus harder with more stakeholders.
- **Tension**: Should focus be on the next hard fork or long-term planning? The group acknowledged a collective desire for future certainty but admitted challenges in long-term execution.
- **EIP-4444**: Not controversial but hasn't reached mainnet, highlighting issues in prioritizing improvements.
- **Value vs. risk**: Debated using account abstraction as an example.
- **Ossification vs. functional escape velocity**: Transitioning from a shipping culture to ossification is challenging despite being theoretically easy.
  
**Asynchronous vs. Synchronous Communication**

- **Lucas**: Time zones (NZ/AUS) are challenging; having people in Europe helps but isn't a complete solution.
- **Decision-makers**: Those on calls might not be the best for decisions; synchronous communication is valuable but needs improvement.
- **Moving timeslots**: Has been tried; attendance remains hard to coordinate.
- **Two classes of calls**: There's reluctance to create separate tiers.
- **Terence**: Suggested teams provide written stances before calls.
- **Tim**: Prefers teams to discuss live to allow internal disagreements.
- **Pari**: Written positions might lose context.
- **Marius**: Likes discussions in the PM repository.
- **Trent**: Notes that Discord isn't indexed or controlled by the community.
- **Breakouts**: Suggested scheduling at better times; concerns about reporting back effectively.
- **Guillaume**: Challenges in sifting through discussion noise.
- **Tim**: EthMagicians could categorize posters to manage content.
- **Late contributions**: Posting issues 24 hours before helps but doesn't eliminate last-minute inputs.

**EIP Discussions and Feedback**

- **Pavel**: Asked about the decision-making process and discussion topics.
- **Tim**: Differentiated between new EIPs and spec changes; each requires different decision levels.
- **Ansgar**: Highlighted considering new factors even after prior decisions.
- **Voting on EIPs**: Debated as a method.
  - **Tim**: Emphasized speaking up against bad EIPs and being comfortable with contention.
  - **Pooja**: Suggested pre-collecting opinions on EthMagicians.
  - **Tim**: Voting has issues; excluding a good EIP is bad, but including a bad one is worse.
  - **Danno**: Warned that voting structures can be captured.
  - **Potuz**: Consensus is achieved subjectively, influenced by moderators.
- **Asymmetry in EIP Process**:
  - **Tim**: Champions push proposals; critics lack incentive to oppose persistently.
  - No mechanism for a hard "no" on EIPs.
- **"Rejected for Inclusion" (RFI) Status**:
  - **Tim**: Doesn't want RFI to imply an idea is bad.
  - **Mikhail**: Objections should be in EIP threads or PRs; authors should manage the process.
  - **Ansgar**: Suggested "Declined for Inclusion" to provide clear feedback.
- **Negative Feedback**:
  - **Tim**: Negative feedback is essential but can spread on social media.
  - **Nico**: Centralize feedback, possibly on EthMagicians.
  - **Ansgar**: Concerned about unfair criticism within EIPs.
  - **Pooja**: Consider flagging strong opposition but avoid adversarial approaches.
  - **Tim**: Sometimes rely on experienced individuals for decisions.
  - **Ansgar**: A single voice can be significant.

**Non-Consensus Changes and Development Priorities**

- **Tim**: There's a bias toward what gets included; non-consensus rule changes are often secondary.
- **Decision-Making Gaps**: ACD lacks methods for some decisions, like those involving high consensus layer validators.
- **Non-Consensus Improvements**: Should focus on items like EIP-4444, peerDAS, and networking updates.
- **ETH-69 Implementation**: Recognized as necessary.
- **EIP Education**: **Pooja** expressed concerns about educating on EIPs.
- **Networking Issues**: **Potuz** noted current problems in clients like Prysm.
- **Devnets Inclusion**: Such changes should be in development networks.
- **Negative Feedback Timing**: **Tim** cautioned that it might not always be beneficial.
- **EIP Discussion Return**: **Mikhail** asked when authors should revisit discussions after a decline.
  
**Breakout Sessions and Efficiency**

- **Ansgar**: Breakout calls shouldn't occur during main calls.
- **Tim**: Sometimes brief discussions can save time; defaults should align with the current fork.
- **Asymmetry in Participation**: Champions and implementers attend calls; detractors often don't.
- **Time Management**: **Barnabás** suggested setting timers for discussions.
- **Summarizing Feedback**: **Guru** emphasized summarizing negative feedback; proposed editable thread posts.
- **Searchability**: **Pari** noted EthMagicians isn't easily searchable; AI summaries could help.

**Voting Mechanisms and Decision-Making**

- **EIP Acceptance Criteria**: **Tim** proposed only accepting EIPs with accompanying code.
- **Voting for Devnets**:
  - **Barnabás**: Suggested it.
  - **Tim**: Disagreed; devnets are informal.
- **Gating Devnets**:
  - **Pari**: Supports signals from ACD for non-fork devnets.
  - **Potuz**: Views devnets as informal.
  - **Resource Allocation**: **Barnabás** questioned spending time on random devnets.
- **EELs (Ethereum Execution Layer Specifications)**: **Trent** asked if they will always be backward-looking.
- **Sybil Resistance**: **Guillaume** inquired about preventing vote manipulation.
- **Voting Concerns**:
  - **Tim**: Assigning votes is problematic; voting gives false confidence.
  - **Danno**: Structures can be captured.
  - **Marius**: Joked about voting by network share.
- **Role of Non-Client Teams**:
  - **Tim**: Trust doesn't transfer with personnel changes.
  - **Breakouts**: Should be more open, but client teams decide ultimately.
- **Devnet Gating**: Should be based on current inclusions, not an extensive list.
- **Internal Priorities**: Recognized that teams have different focuses.

**Conclusion**

- The ACD process is moving forward but has room for improvement.
- Addressing the asymmetry between EIP champions and detractors is crucial.
- Enhancing documentation of negative feedback and providing clearer guidelines for EIP inclusion or rejection are priorities.
- Maintaining subjective consensus methods is preferred over formal voting to avoid manipulation.
- Improving communication platforms and considering timing and criteria for devnets are important steps.
- Accommodating different internal team priorities while striving for consensus is essential.
