# All Core Devs Meeting 92 Notes
### Meeting Date/Time: Friday 24 July 2020, 14:00 UTC
### Meeting Duration: 1.5 hrs
### [Github Agenda](https://github.com/ethereum/pm/issues/195)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=RWX9vkY7Oas)
### Moderator: James Hancock
### Notes: Edson Ayllon

---

# Summary

## EIP Status

EIP | Status
--|--
2315, 2537 | Accepted for Berlin and YOLO testnet|
2565 | EFI, proposed for Berlin, currently not included in YOLO|
2046 | Proposed for Berlin. Under Discussion to evaluate for adding to Yolo|
EIP-2718 | EFI


## Decisions Made

Decision Item | Decision
92.1 | EIP-2565 moved to `Last Call`
92.2 | EIP-2718 motioned to `Eligible for Inclusion`

---

# Contents

- [1. Retrospective on call 91](#1-retrospective-on-call-91)   
   - [1.1 Client Diversity](#11-client-diversity)   
   - [1.2 State Bloat](#12-state-bloat)   
- [2. EIP Discussion](#2-eip-discussion)   
   - [2.1 EIP-2565](#21-eip-2565)   
   - [2.2 EIP-2718](#22-eip-2718)   
- [3. Other Discussions and Closing Comments](#3-other-discussions-and-closing-comments)   

---

# 1. Retrospective on call 91

Video | [6:06](https://youtu.be/RWX9vkY7Oas?t=366)
-|-

Alexey wrote a retrospective on EthMagicians, [CoreDevCalls 91 Retrospective: How did we do with “Five Why”s?](https://ethereum-magicians.org/t/coredevcalls-91-retrospective-how-did-we-do-with-five-why-s/4441).

## 1.1 Client Diversity

Before we start asking why, we start by identifying the problem. The problem stated is one client runs the majority of critical installations. We don't have certainty that statement is true.

If we assume the problem does exist, then we ask questions, "Why is this the case?"

Answers discovered:
- Users go with the oldest and most trusted implementation
- Other implementations don't follow the same functionality
- Lack of standards for external interfacing
- People can run multiple implementation, but may bring extra cost, unjustified from business PoV.

We can start by measuring the critical installations. This will answer if Geth is really the market dominant client. And we'll be able to measure our progress once we make changes.

The Cat Herders have started collecting data for the major installations.

The results so far indicate that Geth is the most used client. And for organizations willing to have a backup client, the most selected alternative is Besu.

There is a list of operators we contact during hardforks. We can go through that list and see what percentage has answered.

Another thing we can do is use published ENR data.

One benefit of manually collecting the data is we see which data belongs to critical installations. Also, ENR doesn't communicate if a client is a light-client or a full-node.

Something to be considered what the damage will be if the survey responses are leaked? Currently, the information is saved in a spreadsheet with limited access. But more secure solutions can be made in the future.

We can form the questionaire in a way to minimize the impact of a potential leak. To do so, we should know what the negative potential of a leak may be.

If we can make public some of the data to show the current landscape, as well as provide a description of possible negative outcomes and that they could be affected, we could justify extra spending to reduce risk.

Another thing is, if operators do have a backup client, have them explain how they did that for others.

The survey could be a funnel for individual interviews where we can collect more information.

**Alexey**: For the Geth team, what's your biggest fear in this case?

**Martin**: Some issues have historically happened--consensys issues, denial of service issues. If DoS happens on a node that has 70% of the netork, it's not the worst case that only 70% goes down, as it can get worse.

**Alexey**: 70% is an assumption?

**Martin**: Yes.

**Alexey**: It's good to actually check for that.

**Martin**: Right, until proven otherwise, I assume the worst case, of a 70% dominance.

**James**: Even if it's not that worse case, we should still take actions to reduce risk.

**Alexey**: The first thing to deal with a fear is to confirm that it's true with data. And if the data confirms it, it's not just you that is worried, but everyone else will work towards a solution.

## 1.2 State Bloat

**Alexey**: Another conversation that's happening is the gas price limit. What will happen if we raise the gas price limit to say 20 million. Can we even think about what problems will happen? Most people don't see a problem because they assume nothing bad will happen.

**Peter**: It could become possible to create blocks that take 30 seconds to process. This would re-enter the Shenghai denial of service vectors.

**Alexey**: From the miners, they are saying to be profitable, they need to process a block within 42 miliseconds. That may be the average case.

**Peter**: The average case may be pointless. What I care about is that the network doesn't go down.

**Alexey**: If everyone is relying on average cases, as opposed to looking at the worst cases, can we demonstrate the worst cases?

**Vitalik**: It would cost over $300 a block.

**Alexey**: If we do that, how long is it going to be processed? How would we produce that block?

**Martin**: Would you like us to deliver the blueprint attack on Ethereum?

**Alexey**: If that's what it takes to demonstrate it. Right now it's a hypothetical situation. There's a rift betweeen the community and the core developers, since all the community sees is the network operating normally. How do we get this message across?

**James**: Users only see transactions going through today, where core developers are lookiing at function 10 years from now. Even miners aren't thinking that far in advance.

**Peter**: Etherscan has charts. What we can do is have future estimates, how the network will look like. Maybe that will show what these changes will do.

**Alexey**: One thing I'm trying to understand is why the conversation around gas price limit, especially when a lot of attention is oon 1559.

**Vitalik**: One thing is that there isn't a clear direction to what the proposed fix is. 1559 has attention because it is a formal proposal with a name that fixes something.

**Tim**: Isn't that what Eth2 is? As long as demand for block space exceeds the supply, the prices will go up. We need a few orders of magnitude fix, which won't happen in the next 6 months to a year.

**Vitalik**: Roll-ups can do it before a year. But Eth2 will take longer.

**Tim**: 1559 people see as a solution, but it won't solve this. Increasing the block gas limit won't solve this.

**Vitalik**: Another concrete fix is the skinny gas repricing that I proposed.

**James**: Isn't the problem state size growth?

**Vitalik**: One problem is the DoS attacks, and the other one is state size growth, which is long-term. We do want to treat those problems separately to solve them separately.

**James**: Is there an inflection point for state size growth where things become terrible?

**Vitalik**: The problem is the cost of accessing state is logarithmic to the size of state. For an individual computer, there may be a point where it goes full and defrags everything. The chronic problems we do need to take seriously. Acute problems are easier to coordinate solutions around. But chronic problems never come all at once.

**Peter**: For the Shenghai attacks, it started with bloating state. After the state was bloated, we had various attacks on caches, etc. The solution to that was to make state bloat expensive, and to delete that bloat.

Now if we were to increase the gas price limit to what the network can handle, the state keeps growing, but at the inflection point, there's nothing we can delete.

The core devs have a feel to how the network will change on quickly increasing state, but it's good to get concrete numbers.

**Jame**: Having charts and maybe a report.

**Peter**: Having a report explaing what the core devs are afraid of won't solve the underlying problem.

**Alexey**: I didn't want to jump into proposing solutions today, due to time.

Going back to the retrospective, there was an agreement that it was difficult to write a fully functional Ethereum implementation that's performant. Due to the large amount of data being transfered, optimizations need to be made, which may sacrifice modularity.

There's nothing inherently wrong with the protocol, we just started with bad infrastructure a few years ago.

The question is, will this be worth it? Do we have enough resources? Or do we wait until Eth2.

**Peter**: Eth2 will introduce 64 shards. It will cut down the problem into 64, 2 orders of magnitude. But we're just kicking the can down the road.

This problem will still exist, but will take longer to show up. We can't just wait for Eth2.

**Alexey**: I'm not suggesting we wait for Eth2. I'm talking more about organizational problems.

**Peter**: Ethereum 2 is on a unique position. One shard will be Ethereum 1, which will bare those bad decisions. But all other shards are a clean slate.

State rent cannot be introduced in Eth1. But in Eth2 it can be. Maybe that is a good position. What are the simple changes that can only be done in the beginning but can't be done now?

**James**: We could push a lot of resources to have client distribution. Or we could set a condition, such as no more hardforks until a distribution is achieved, then the rest of the ecosystem will adjust to the new distribution. Orient everyone to the same goal.

**Alexey**: I see where this is coming from, adding gatekeeping. But by doing this, we may unfairly affect people who are doing the work, while the ones we want to take action don't. It may be harmful to impose restrictions. This assumes that the people who want new features are the ones running critical installations, which may not be the case.

**Tim**: This also assumes the people who want the new features care about client diversity.

**James**: If we say 1559 won't happen until client diversity, then we may see action.

**Rai**: How would we know they don't take that action just to appease us, and once there's the decision for a release, they just change back?

**Tim**: How I see, people won't install Besu just to get 1559. They'll just say, "this is bullshit, just install 1559 in Geth, and we'll pay and download that." It may be more adversarial than collaborative.

**Alexey**: I don't want to create an incentive for people to lie to us. And if we wrap together this with other things, instantly we create an incentive for people to lie.

**Artem**: And there's no stopping people taking Geth and just changing the client identifier code.

**James**: I don't want to derail the conversation. I'll respond to Alexey and we'll move on.

**Pooja**: If we are in doubt of the accuracy of the data, we can make the organization name is required.

**Alexey**: I think the only way we can make sure the data is correct if they willingly provide it.

**James**: All clients are ready for Berlin. But even though all the clients have it integrated, it's not ready to go. We have to make sure state tests are suffiicient. I'd like at least something to come out of these conversations to address these longterm problems.

**Tim**: I think Martin wanted to host a fuzzing call, but after July. That still feels like a good idea to me.

**Martin**: I did send out the invitations.

**Alexey**: The reason I suggested a feature freeze was to give developers sufficient time to remediate the immediate things. If this is a long game, do we want to play that long game or not? We haven't figure out a specific solution.

**Piper**: I still feel that client diversity is on the network level. That we don't need monolithic clients. I think we know what needs to be done.

**Peter**: It would be nice if one team could work on full nodes, and another team could work on light clients. However, a light client needs a server which is a full node.

**Piper**: I think we can still build infrastructure that doesn't need servers.

**James**: My concern is that solutions may take multiple months. Is it possiible to freeze features for that long?

**Piper**: Stateless will take a while. I'm still a big proponent of building out a BHT based state network, which can help in a lot of areas. That alone takes a lot of burden off of full nodes. That should be deliverable within a small number of months.

We have good direction on how to handle systemic problems. I think we need to focus on them.

**Alexey**: If we decide we want to play the long game, I would suggest we do find points to introduce modularity.  

**James**: Do we still feature freeze?

**Alexey**: No, we feature freeze until we reach a point where we figure out what we want to do. Figuring out which approach is going to work is not quick.

We are in a shitty situation. We either get out of it, or make sure things don't break. Because if we keep pressuring it, we're just going to make things worse. Things may happen that may not be reversible.

**Artem**: We either make a great jump now, or we die. Given the problems for scaling, we can shift development of clients today to make new modular clients.

**Peter**: Who are you suggesting moves to other clients?

**Piper**: We should hard stop this. We only have 15 minutes.

**Alexey**: I suggest if we want to keep talking about this, we can schedule a separate meeting or continue in a chat. I want to make sure we don't make things worse, and especially not in an irreversible way.

# 2. EIP Discussion

Video | [1:12:57](https://youtu.be/RWX9vkY7Oas?t=4377)
-|-

## 2.1 EIP-2565

Moved into last call. It's now been finalized with all the feedback. We still couldn't find a better library for OpenEthereum, so that may be a 2-3x performance difference between Geth and OpenEthereum. But that can be something we solve in the future.

## 2.2 EIP-2718

**Peter**: My only concern is the same I had with account abstraction with version numbers. Whenever we introduce versions for transactions that we introduce the first new version of a transaction.

**Piper**: So this EIP spawned from another EIP which introduced a new type of transaction. We could bundle this with 2711, which introduces the next type of transaction.

**Tim**: With 1559, we didn't use typed transactions, since it was just a draft. But it would simplify the implementation a lot if it was part of the protocol before.

**James**: Any opposition to moving this to EFI?

Moved to EFI.

**Peter**: Wouldn't transactions have 2 hashes?

**Piper**: We settled at the protocol level, only the new format will be allowed, and that the hashing would be the same.

**Peter**: So we would forbid the old format?

**Piper**: The old format can be mapped to the new format.

**Peter**: From the signature perspective, they would be signing the old one?

**Piper**: Signing on the old and the new will be the same.

**Peter**: What if I introduce a new type?

**Piper**: The new type would be whatever is specified. It's backwards compatible, but we force the legacy format into the new format.

**Peter**: You still end up with a mixed bag.

**Piper**: There's no problem with a mixed bag. Because at the protocol level, only typed transactions are represented.

**Peter**: If I mis-sign the internals of the transaction, I can change the type.

**Piper**: We would need to look at that. But I wouldn't believe there would be a new problem. The spec requires the type is in the signature.

**Peter**: If you force the transaction type to be part of the signature, that calls for a legacy type too, no?

**Piper**: We're not forcing it. Just a strong recommendation in the base spec. I would reecommend you read through the EIP.

**James**: I would like to remind that EFI doesn't mean the EIP is going into the core clients. But that it's the first step in many stages.

**Alex V**: Can we also discuss the current state of testing tools? I would say the state is quite low, and it was very painful to write tests. For people wanting to introduce new changes with EIPs, it shouldn't be prohibitively hard.

**Martin**: It has been the case. And not been something we've been able to solve.

# 3. Other Discussions and Closing Comments

**Alex V**: Maybe this is a better priority with a clearer direction for a solution, as opposed to trying to solve client diversity. To ensure performant clients, rather than relying on client diversity as a fail-safe. Also, if it's done, it won't make things worse.

**Martin**: It's not a bad idea. But we have been trying to improve the tooling for a long time. We are actively looking for someone to take a lead on that.

**James**: Thank you everyone for joining. I'll ping people on a client diversity call next week.

---

# Annex


## Attendance

- Alex Vlasov
- Alexey Akhunov
- Artem Vorotnikov
- Daniel Ellison
- David Mechler
- Guillaume
- Hudson Jameson
- James Hancock
- Kelly
- Martin Hoist Swende
- Micah
- Peter Szilagyi
- Piper Merriam
- Pooja Ranjan
- Rai
- Tim Beiko
- Vitalik Buterin


## Next Meeting Date/Time

Friday August 7, 2020 14:00 UTC
