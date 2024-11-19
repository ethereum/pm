# [CLS] Ethereum Magicians Infinite Endgames: UX 

## [Ethereum Magicians Infinite Endgames Sessions 1](https://app.devcon.org/schedule/QRG8QW)

## Summary: 
UX has been at the forefront of Ethereum recently, as standards for Account and Chain Abstraction have been gaining significant traction in the space. Join us (literally! This panel will be “fishbowl style”) as we discuss the challenges that we will need to figure out first, such as cross-L2 key management, asset handling and transactions; avoiding fragmentation (liquidity, network, users); coordinating standards across L2s and wallets; and more

## Video: https://www.youtube.com/watch?v=63w7kHh737w

## Panelists: 
Niha (Safe), Cody Crozier (Coinbase), Derek Chiang (ZeroDev), Mark Smargon, Pedro Gomes (WalletConnect)

## Notes by:
June Manuel

## Devcon SEA - Nov 15, 2024


Here to talk about Eth user experience; trying to solve the problems of ux
tradeoff of ux and sexurity; cross-chain interoperability as a primary challenge
Gather here with people who are dealing with this on a daily basis.

Question 1: There are obviously many hurdles to user experience in the space, but in your eyes what are the biggest and most pressing hurdle for mainstream adoption?

Cody Crozier: Funding and getting wallets funded in the first place. AA is great, but we need better solutions through
native funding with things like debit cards or apple pay for real-time transactions

Pedro Gomes: funding isn't necessarily a blockchain problem, it's a wallet problem. account management is still the biggest problem. We have fragmented ourselves and we need to coordinate knowing that accounts are fragmented; all of these wallet types should be the same instance of the same account. Different from having multiple accounts; account design needs to be trule universal

Derek Chiang: Adoption of crypto in general vs. adoption of AA; adoption of crypto is blocked by onchain use cases; need more compelling on chain use cases; obstacle to AA is that it is impossible to use AA on preexisting wallet; requires moving assets.

Mark Smargon: We don't have a technology problem, we have a business problem. This cycle is more product led vs. last cycle was more developer led; the primary issue is user adoption, not the protocol. Trying to create the perfect protocol is not the best way to attract users.

Niha: Best products available make people's lives better; unfortunately with crytpo rn it's making lives harder. We need more compelling use cases and easier to use applications.

Tom: Thanks to AA, onboarding now is super smooth; but now we've introduced a different problem of wallet fragmentation (identity, liquidity,) what do we do about this/ can anything be done?

Pedro: The offering is 10x better but the accessibility requires too much effort; I don't think we need more compelling use cases, but we are asking people to climb a mountain. We might as well go back to silo'd apps; we broke the composability at the wallet; we can make interoperability at the chain but the wallets are too fragmented.

I write more tweets about ERCs thank about walletconnect. ERCs are the way to go to solve this issue. Everything in your product design can be an ERC and the beauty of an ERC is that we can project manage together. If we stay silo'd we will not be working together.

Derek: We have a tendency to standardize too early, which is just as bad as standardizing too late. When we do ERCs too early, we think we may be solving the problem in advance but it creates a deeper fragmentation problem. 
On the original question about fragmentation, I'm not too concerned for two reasons. 1. I know as a fact that all the wallets are trying to build global solutions and integration across all the dapps; 2. I see embedded wallets as a temporary solution in the sense that they are the first step in a user journey; embedded wallets lead to onboarding to a stand alone wallet-- once these become AA accounts, fragmentation is less of an issue.

c: I agree there is no real fragmentation problem because the pie is getting smaller. We confuse our users with our investors. The people who complain about fragmentation/ux are not necessarily the actual users. Consumers don't need to pay for gas, don't need to know new functions/habits

Niha: On the embedded wallet side, the UX is pretty good. You are already in the environment of the app. Most users trust the app their using. Embedded wallets will be the more popular pathway for the majority of users.

Standardization is pretty good; many standards that point to the same outcome but with different priorities, which also creates fragmentation and competition.

Tom: Standards competition is good, actually. Competition between two or three standards can be good, but it can be toxic if motivated by financial or commercial gains. It all depends on how it's done.

Derek: To clarify, I am not against ERCs or creating standards early, but as a space we need to careful not to shame companies that are not embracing ERCs. They are trying to build the best solution for their users and get it right before making an ERC. There is community pressue who don't appear to be enthusiastic about existing ERCs.

a: There is a balance that you have to strike between using standards and shipping value to users immediately. Concern about embracing standards versus providing user value.

Pedro: Sorry for public shaming around standards. It's very important that people understand ERCs are malleable. It an ERC an outcome or philosophy? It's important to clarify that it is a specific outcome; creates successful community coordination and cohesion. ERCs should be community designed more than owned/authored by 1-2 authors. The issue is not ERCs themselves but the way that people do and think about ERCs. There is a problem with a sense of individual ownership of ERCs.

Tom: Coordination is a primary challenge. There are a lot of ERCs which are very beneficial to UX. Share important ERCs/EIPs.

a: 7702 is very important to us; there are a lot of users right now using EOAs and we need to get those users migrated.

d: ERC-20. We tried to innovate a few years ago and tried to use ERC667, but ERC-20 is a good example of simplicity. It shows that not the perfect protocol wins, but simple is good enough. 

Niha: Lately I have a crush on 7702. But I think UX started with 4337 for me; there's an ERC that improved wallet capabilities and I really like this one. 

d: What's the name of the ERCs with the plug ins? 6900.

Derek: For account abstracted wallets, it's hard for devs to read the balance amount of the wallet. If I'm connected a wallet across dapps, it's hard for the dapp to know that the wallet can 

Pedro: ERC-7715 which allows dapp to act on behalf of the wallet; acts like smart sessions

Tom: Going back to what Derek said about fragmentation of assets, when we talk about chain abstraction, we've seen some interesting conversations using the word 'magic,' but what are your general approach to solving the problem of cross-chain fragmentation of assets?

Derek: Very active area of research. Connection of smart accounts and intents; intents-based 
What chain abstraction wallets are doign is briding assets through a liquidty bridge; decreases transaction time 

Pedro: In this panel, I feel like there's a big focus on wallet, but chain abstraction comes with two big problems: 1. transaction layer and 2. liquidity layer. If every wallet supports intents, tokens are completed fragmented. Token fragmentation needs to be solved at bridge and token issuers layer, not the responsibility of wallet devs. 

Two problems to token fragmentation: non-native tokens have multiple bridged versions; issuer-bridge fragmentation causes a token fragmentation

Mark: We are not even at the point where we need to adress those issues; fragmentation is not yet a big problem until we have the users/use cases.

Pedro: You're right that the motivation for fragmentation was for cheaper gas and trasnaction, but the problem started earlier when we designed around the blockchain rather than the assets. In Ethereum you don't have a problem with token fragmentation as much because ETH is native, special class within the blockchain.

Tom: there is additional fragmentation that comes along with key fragmentation. You have to deploy smart contract across multiple chains and need to create keys across multiple networks.
What do you think about key / identity fragmentation as well?

Cody: Right, we need to make sure the signers are valid across all chains. 

Derek: Key stores are endgame to actually solving the problem; once you have a key store this won't be a big problem anymore.

Niha: Key stores will solve the problem, but each day we have new L2s. We will need to have a key store roll up; divided identity may not be 100% solved but definitely the right direction.

Mark: Looking at the future in which we have a billion users and trying to reverse engineer from that future, the problems that we think are currently the problem are not necessarily what we need to solve. 

Derek: Two unsolved problems with key stores: 1. economics-- the cost of running it will not be cheap. Key store rollup is not economically sustainable.

Pedro: It is very hard to spin up a new chain or new L2, but do we need a new EVM for key store roll ups?

Tom: Who is going to pay for this? The users won't pay for managing their keys, the dapps won't, so who will?

Pedro: We may be overexagerrating the cost. You only need to pay when you actually touch the rollup.

Tom: And we need to consider the security element of that.

Audience question: I wanted to make a weird plug; you were speaking earlier about EIPs and standards-- EIPs are not standards even if finalized. EIPs are only specifications that went through a process and got published; You can use Ethereum Magicians to share user stories etc and design in the open.

Tom: Question from audience is kind of in conflict with this: "What are you thoughts on product-led protocol development? Is ercs convention the reason we have no so many apps? Why no ERCs equivalent in web2?"

The web2 equivalent is RFCs. 

Mark: Web3 has a lot more rapid, open, and democratic approach and it's a much easier way to reach market and consumers.

Derek: The problem is not with people making ERCs; the problem is when we as a community shame projects into prematurely using ERCs when they may not be ready.

Niha: This is all too primitive for the consumer and typical user today.

Tom: I'd like to hear your thoughts on EIP-7702.

Pedro: I like the fact that the core devs included a wallet EIP. We have been designing wallet experience through EIPs and we reached the limit of how much we can provide to consumers without touching the chain.
Brought 3074 back from the dead and we got core devs to care about wallets, which was a massive achievement.

Niha: Very cool for EOA users who want to begin using smart accounts. 7702 gives you features that enable a seamless UX environment; need to get a point where every EOA is a smart account.

Cody: EIP-7702 is great for onboarding EOA users. Inherently, a 7702 wallet has a higher risk profile than a standard 4337 wallet, but at the same time out of the box users gets a fully self-custodial wallet with 7702.
Overall, excited but there are some risks.

Derek: I'm a huge fan and think it's great for the space, but there's a specific implication for this design. Gives power entirely to wallet for user smart account logic. Special type of signing not yet available today; we still all need to wait for leading wallets like coinbase and metamask to embrace.

Pedro: How are these specifci problems any different than current 4337 operations?

Derek: The functionality already exists for 4337, but not yet for 7702. Cannot product a valid 7702 update.

Pedro: But 7702 is not yet in production.

Derek: But even if it was, a wallet today could not sign a valid 7702 upgrade transaction.
With 7702 you need the wallet to explicitly support 7702.

Niha: With this EIP, they introduced a new transaction type (type 4) that current wallets don't have functionality for.

Pedro: I feel like this is a feature because it gives ownership to the wallet. A problem of 4337 is that it doesn't give ownership to the wallet. The fact that it doesn't yet support type 4 transactions is just a matter of time. The question is whether you have any control or if the wallet takes over.

Mark: I can speak on the wallet design side. (...) We will get there.

Tom: Question about modular accounts?

Mark: Modular accounts are our bread and butter; the web3 equivalent of a bank account and enables us to go beyond where traditional banking can go. 

Pedro: How do we feel about modular accounts and 7702? I believe that the design of 7702 limited the actual use cases for modulars. 

Niha: With 7702 we can for sure set the code with EOA, but the code could be set to 7579. As an app developer, you can plug in customizable modules. With 7579 we can question modularity; app developers may have a glass ceiling with present modules but with 7579 we can have more customization.

Derek: The concept of modular accounts is a bit overrated, most of the time peolpe really just need  session keys. We should be focused on use cases.

Tom: Can you give us some examples for use cases for modular accounts?

Pedro: Recovery is a good case for modular accounts. The base contract should be as lean as possible and everything should be pushed to modulars specific to account management.
Back to risk factors of 7702 - pull payments can essentially be reverted by the EOA by overwriting them; you can overspend or try to overspend. Have to put 7702 in separated mempool because of potential conflicting transactions. 

Mark: There is also KYC - digital attestations about your account that does not need a modular account. What is the statistical probability that I'm double spending from my account?

Niha: Ultimately, your EOA can override your delegated transaction.

Tom: It's a question of who to trust.

Pedro: With 7702 you can double transact without protecting the wallet account.

Tom: And doesn't protect user in cases where key is compromised.

Niha: I see 7702 as a facilitator to migrate to smart accounts rather than continuing to stick with EOA.

Mark: It is a very short term problem we're tyring to solve. If focus is on migration, it's different than onboarding. We can talk about all of these different payment and transaction types once we have onboarded everyone.

Tom: I want to hear from everyone, what are some cool UX solutions you have come across in the past couple months?

Cody: We are building ERC-20 paymaster. Excited about general commerce using AA and for users to use USDC for entire transaction. Can do that really smoothly with the paymaster.

Pedro: Smart sessions are great tool for most use cases; 99% of the problems are 'can I stay in the app without going back to the wallet?'

Derek: Smart accounts / magic accounts; transactions across chains seamlessly

Mark: We are seeing the first implementations of account abstraction globally for use cases not just for investments. Much bigger target audience -- people who want savings than people who want to invest/trade. Under the hood, all using USDC and account abstraction.

Niha: From a purely UX perspective, the UX endgame would be the ability to pay with any asset anywhere. Abstract blockchain completely.

Tom: Applications I saw that are really cool: Mina Wallet and Fileverse.



