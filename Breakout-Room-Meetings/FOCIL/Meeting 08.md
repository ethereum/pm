# FOCIL Breakout Room #08
Note: This file is copied from [here](https://github.com/ethereum/pm/issues/1435#issuecomment-2791712894)

### Meeting Info
- Agenda: https://github.com/ethereum/pm/issues/1435
- Date & Time: [April 8th, 14:00-15:00 UTC](https://www.timeanddate.com/worldclock/converter.html?iso=20240213T140000&p1=1440&p2=37&p3=136&p4=237&p5=923&p6=204&p7=671&p8=16&p9=41&p10=107&p11=28)
- Recording: [here](https://youtube.com/live/JKkkvq9ToUc?feature=share)

# Meeting notes:
## Research
### IncluderSelect

- IncluderSelect allows users to become includers themselves and is compatible with zkFOCIL. The intuition behind IncluderSelect is that users are inherently incentivized to create a high quality inclusion list for their own transactions when facing the threat of censorship. This intrinsic motivation means there is no need to provide additional rewards to these includers.

- IncluderSelect operates in three steps. First, users bid for the right to become includers. Second, the protocol deterministically selects auction winners. Third, the standard FOCIL mechanism takes effect to enforce transaction inclusion.

- The primary focus of IncluderSelect is on appointing includers. Bidders specify how many bytes they want to consume for their inclusion lists. Remaining bytes can then be allocated to other includers selected by the FOCIL mechanism. Alternatively, the protocol may split the total bytes evenly between bidders and FOCIL-selected includers.

- Bidders specify their includer IDs in their bids and the IL committee is formed based on these IDs. This approach enables bidders to bid anonymously and connects well with zkFOCIL.

- Implementation is expected to be straightforward. Bids themselves are transactions, so the auction could be easily implemented using smart contracts. Additionally, bidders don’t have to be validators; it’s sufficient for them to hold ETH to cover their bids.

- For someone to censor transactions, they would have to buy up all available bytes, preventing anyone from becoming includers. This raises the cost of censorship significantly: Cost of censorship = total bytes / censored bytes > ~1

- Given that most transactions will not face censorship, the demand to become an includer will generally be much lower than transaction demand, making the cost of inclusion effectively negligible: Cost of inclusion ≈ 0

- Note that the auction can be viewed as a technicality. You won’t need to participate in the auction unless your transaction is being censored.

- Lastly, a notable advantage is that even a light client can include transactions trustlessly. A light client can fetch state, construct their transaction and submit it through IncluderSelect.

Q: Can the IncluderSelect auction also be censored?
A: Supply would vastly exceed demand and the bids are simply transactions whose inclusion can be enforced by FOCIL.

Q: In a world with censorship, would people outsource their bids to price them, resulting in the loss of some censorship resistance properties?
A: With IncluderSelect, there are multiple layers to censorship, making it more difficult to censor your specific transaction compared to vanilla FOCIL. An attacker would need to prevent you from winning the IncluderSelect auction, censor your transaction from inclusion by other includers, and lastly, censor your transaction from inclusion by the block producer.

### zkFOCIL

- In vanilla FOCIL, all IL committee members are publicly known, which can make them potential targets for some attacks such as DDoS. Furthermore, IL committee members are aware that their identities are linked to the inclusion lists they publish. This linkage may lead them to censor transactions out of fear of potential repercussions. Therefore, zkFOCIL aims to unlink validators from their published inclusion lists and conceal the identities of IL committee members. Additionally, zkFOCIL aims to be feasible by being efficient, conceptually simple and requiring minimal protocol changes.

- We plan to use linkable ring signatures to achieve these goals. A linkable ring signature is a cryptographic primitive where a signer anonymously signs a message using their secret key, which corresponds to one of the public keys in a “key ring” (a list of public keys). Alongside the ring signature, the signer publishes their “key image,” which is uniquely derived from their public key. Anyone can verify this signature against the key ring and key image without discovering the identity of the signer. It’s called “linkable” because each key image is uniquely tied to a public key, enabling the detection of double signing without revealing who the signer is.

- Here is how zkFOCIL would work. First, all validators derive key images from their public keys without revealing it. The protocol then runs a random election based on these key images, in contrast to vanilla FOCIL, which uses public keys. This approach is as good as using public keys because key images are uniquely determined by publick keys. Then, IL committee members sign and publish their ring signatures along with key images. Anyone can verify these ring signatures with respect to the key ring—a list of public keys—and key images but cannot learn the identities of the signers because the link between key images and public keys remains hidden.

- The next steps for zkFOCIL are threefold. First, we’ll prototype linkable ring signatures using generic zkSNARKs to evaluate their efficiency because generic zkSNARKs are complex and come with certain security concerns. Second, we aim to find a simpler and more efficient way to implement linkable ring signatures without relying on generic zkSNARKs. Specifying zkSNARKs in the spec is challenging, so further research is required to find a less complex alternative. Lastly, we need to ensure there will be no legal repercussions as zkFOCIL enshrines a degree of anonymity directly at L1.

**Q**: What happens when new validators join?
**A**: Existing validators do not need to recompute their key images but it comes with an implication of potential privacy leakage. For example, if there are five validators and one signs, then four go offline, and afterward one signs again, this scenario could leak the signer’s identity. Changing key images all at once may help mitigate this issue, but it’s an open question how often key images should change and how to handle scenarios when new validators join.

**Q**: If validators don’t reveal key images, how can you run a random election based on key images?
**A**: One approach is to take the leading three bits of the hash of your key image and compare it against some random beacon such as RANDAO. In this scheme, it remains unknown which validators are part of IL committee but once IL committee members publish their ring signatures and key images, anyone can verify their membership. Note that this approach means the IL committee size won’t always be exactly 16.

**Q**: Do you have any alternatives in mind beyond classical constructions or generic zkSNARKs?
**A**: It would be quite challenging because we want zkSNARKs, not just SNARKs. We want both succinctness and privacy-preserving properties. Although offloading zkSNARKs from the protocol would be very nice, we currently don’t have a concrete solution yet.

## Development
**Prysm <> Lodestart interop**

- After rebasing onto Electra and fixing a couple of issues, we now have Prysm and Lodestar interop. Teku and Lighthouse are also on their way, so we’re looking forward to seeing more clients come onboard.

[Image](https://private-user-images.githubusercontent.com/6879002/432153982-38a62fce-a1be-42c1-a20e-a718aab6fdf4.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDY3MjMzMjUsIm5iZiI6MTc0NjcyMzAyNSwicGF0aCI6Ii82ODc5MDAyLzQzMjE1Mzk4Mi0zOGE2MmZjZS1hMWJlLTQyYzEtYTIwZS1hNzE4YWFiNmZkZjQucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDUwOCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTA1MDhUMTY1MDI1WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9OWU2ZTFmNDUyYTBkMzNkOTRhZTVhNTViYTM5MDI4ZGZkNmNhN2RkMTk0YWJiZWEzZTc1ZWU1OWMxNDA3NDZjOCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.1uYyRuUMqLdEB3yambpEfcNo6MtuFGUEQRb-23Gsev8)

"Activation Epoch" vs "Custom fork" discussions

- There are two approaches for handling fork activation in the prototype. The first is the activation epoch approach, where the fork activates at a specific epoch. This method is straightforward to implement and thus allows for faster prototyping. The second is the custom fork approach, where the upgrade is triggered and the fork version changes. This method is closer to the final implementation but may involves more effort and boilerplate code.

- In FOCIL development, clients have been used the custom fork approach. While FOCIL doesn't alter any block or state, it uses a different fork version. Some clients require thousands of lines of boilerplate code to support a custom fork, while others could implement it in about 200 lines and have their code structured by fork version. This variation led us to a discussion about which approach is most appropriate.

- Given that most clients have already implemented the custom fork approach, we’ve leaned toward continuing with it. However, in future prototypes, we would first consider using the activation epoch method as it's way simpler and worked well in PeerDAS prototype.

### Implementation Updates

- **Prysm** has succeeded on CL interop with Lodestar and will be working on interop with Teku.
- **Lodestar** has succeeded on CL interop with Prysm.
- **Teku** is working on CL interop with Prysm and Lodestar and handling the Dora crash issue, which occurs after eip7805 activated epoch is passed.
- **Lighthouse** will be working on supporting eip7805 fork and then proceed to the CL interop.
- **Nethermind** has been improving its codebase, addressing PR review comments and will be working on supporting eip7805 fork.

[Image](https://private-user-images.githubusercontent.com/6879002/432153930-9c241a00-c8b9-461f-bff6-11db527fc75c.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDY3MjM1ODUsIm5iZiI6MTc0NjcyMzI4NSwicGF0aCI6Ii82ODc5MDAyLzQzMjE1MzkzMC05YzI0MWEwMC1jOGI5LTQ2MWYtYmZmNi0xMWRiNTI3ZmM3NWMucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDUwOCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTA1MDhUMTY1NDQ1WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZTFjY2YwMDM3ZWYwMjI3NWQzMTRkNWI5YTZlNGU2YWFhZjA5YTY2Njg3MTkyMDZmYWRhM2ZmM2VmMDI3OTc3YiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.wrznTk_vyrRGtbABGg5y8jc4538fYrCBSrvAemYobqw)

**Questions**
**Q**: How does EL handle eip7805 fork?
**A**: Currently it doesn't but ethereum-genesis-generator will soon set eip7805 timestamp. The EL can compare current time against it to determine if it's in eip7805 fork.

### Links

- [IncluderSelect: Leveraging External Incentives in FOCIL](https://mirror.xyz/julianma.eth/G15Gs2TGfnU93t8R7fuyFjTmZGIwwhRFhNhH_M0dgGE)
- [IncluderSelect Slides](https://docs.google.com/presentation/d/1cwdt9YT9HZGRDD3XTSwArHiw9_hHJRzGfxlXVnQ7zng/edit?slide=id.p#slide=id.p)
- [IncluderSelect Twitter Thread](https://x.com/_julianma/status/1909622204112699702)
- [zkFOCIL: Inclusion List Privacy using Linkable Ring Signatures](https://ethresear.ch/t/zkfocil-inclusion-list-privacy-using-linkable-ring-signatures/21688)

