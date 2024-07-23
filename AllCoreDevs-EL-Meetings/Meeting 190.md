# ACDE Meeting 192

**Meeting Date/Time: July 18, 2024, 14:00-15:30 UTC**

**Meeting Duration: 1 hour 30 minutes**

**[Github Agenda](https://github.com/ethereum/pm/issues/1098)**

**[Audio/Video of the meeting:](https://youtube.com/live/kL58hvM0E68)**

**Moderator: Tim Beiko**

**Notes: Emmanuel Eclipse**

| S No  | Agenda                                                | Summary                                                                                                                                                                                                                                                                                                                                                                    |
| ----- | ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 192.1 | **_Dev-net-1 update_**                                | The DevOps team focused on local testing of the CTOAS package over the last week, resolving several client issues, and plans to launch Definit 1 next Thursday, pending readiness of all client pairs.                                                                                                                                                                     |
| 192.2 | **_EOF concerns_**                                    | The decision that EOF is going into Pectra is reinstated.Concerns were raised about including Geth's neutrality, the need for extensive testing and security by its proponents, the possibility of reconsidering its inclusion in the fork if unresolved bugs persist close to release, and the importance of civil, collaborative efforts to ensure safety and readiness. |
| 192.3 | **_EIP-7702 proposed changes_**                       | No resolution at the moment. The proposal's complexity and the introduction of new mechanisms, like code reset, have sparked debate about its implications and whether it meets the community's needs effectively. The next steps involve thorough discussion, testing, and refinement before any final decisions are made.                                                |
| 192.4 | **_Adding logs to system contracts_**                 | LightClient noted a PR for adding logs to system contracts, agreed upon in a previous all core devs meeting, which would involve triggering events when users submit to the queue, and the moderator suggested an asynchronous review to merge the changes before the next All Core Devs call for a more focused discussion.                                               |
| 192.5 | **_EIP-7742: Uncouple blob count between CL and EL_** | The decision was made to have the teams review it during next week's all core dev call since it’s a new proposal.                                                                                                                                                                                                                                                          |
| 192.6 | **_RIP/EIP-7212_**                                    | The discussion on RIP/EIP 7212 focused on its potential integration into Ethereum's Layer 1, emphasizing its benefits for account abstraction, ENS, and rollups, while noting the need for further review and consideration due to the existing workload on other proposals and concerns about the cost-effectiveness of precompile options                                |
|  |
| 192.7 | **_EIP-4444 Updates_**                                | No Update/Not discussed.                                                                                                                                                                                                                                                                                                                                                   |
|  |

# Pectra [5:10:](https://www.youtube.com/live/kL58hvM0E68?si=mwkvA4QUY7FXCNWV&t=310)

## Devnet-1 updates

**Pk910:** I think I can give a quick update from the dev Ops Team, over the last week we focused on local testing with the ctos package and we are still waiting for the remaining client images to get ready we found several small issues with various clients but most of these issues are already fixed by now and we also have received images for Pectra definit one from all clients now but we are still facing problems with two of them specifically prism is splitting out with some pairs at slot 32 and Aragon is splitting out with the first block with deposit requests.

Unfortunately we also reached a limit with local testing because we can't spin up all the client Pairs anymore locally so yeah next stop is probably definit one, and our current plan is to launch definit one next Thursday with all clients Pairs if they're ready by then, so yeah that's all from us from.

**Tim Beiko:** Awesome thanks okay sorry yes the sound for YouTube was muted okay so tldr we've received all of the client pairs for all the images for devnet-1, had some issues with Prism and Aragon and we're hoping to launch this next Thursday with all client pairs. Any of the specific teams want to share an update? Okay, and then I guess in that case if we launch devnet-1 next week we can see how things go and if things go very smoothly and we don't find more issues then we can put us back together for devnet-2 next week. But yeah it seems like we're in a good spot for devnet-1. Any concerns or other comments? Okay in that case is Marius on the call? Marius, do you want to give a quick summary of your EOF blog post and we'll start things from there?

## EOF concerns [7:20](https://www.youtube.com/live/kL58hvM0E68?si=NS10megCiawQic42&t=462)

**Marius:** sure so I've said in the past multiple times that I not a big fan of EOF and I decided to write my thoughts down why it shouldn't be in Petra and so I did that in the post basically my argument boils down to it's an extremely complex change and the benefits are small in my opinion or not enough to justify such a large change and especially because we can never get rid of the Legacy EVM we will all always have that and now we need to maintain two versions of the EVM in perpetuity at least two versions with every larger update of EOF we might add some new version of EOF that we need to maintain in parallel and that those was kind of my thoughts, it feels like a bunch of people are sharing my thought and sharing my general feeling but also a lot have come up against it.

At this point I'm kind of tired of arguing to be honest I've said my grievances multiple times and it seems like people still believe this is a worthwhile change that is worth taking the risk I don't believe so but I would like to make it very clear that I'm not for this change I think it's risky and I think the risks outweigh the benefits and if we decide to do it then I don't want to be held responsible for anything that basically this is my position, I would still keep working on it if we decide to do it, I will provide the code but I don't want to be involved in anything if anything breaks. I have a clear conscience. Also there's a really funny threat on ACD if you want to read up on all of the discussions that we had.

**Tim Beiko:** Thanks and off like that I appreciate you putting the blog post together and out there and sharing your perspective even though clearly there's high disagreements around it. I think we should encourage people sharing their views, especially when it evolves as you've spent time working on EOF itself. So, there were many messages exchanged about this on the R&D Discord. I guess one thing that came up a lot was around just like the support for EOF. Would Solidity and other teams actually support this? Does it benefit them? It seems like it clearly does, but we do have Daniel on the call from the Solidity side. So, do you maybe want to take a minute or two to talk about how Solidity thinks about this change, why EOF makes things better for you all? I know you posted a few messages about this already, but just so everyone here has the context.

**Daniel:** Yeah, of course. We've always been strongly in favor of EOF, the previous version and the current version. There are a few aspects that were raised in the blog post and in the channel that I would like to address, particularly the claims that there are alternatives to solve the technical problems that EOF addresses, which I would like to debunk. We have swap “N” and top “N,” which significantly simplify our compiler infrastructure, and we have been trying to get into Legacy AVM for years. The IP number is 663, but it can't be done without immediate arguments, which rely on EOF. There have been a lot of arguments about that for years. Deno made the point in the chat, and I think he would be happy to elaborate if there are any questions about that.

The other thing is getting rid of jump test analysis and bending relative jumps, which is also not possible without EOF. We have function calls that have return locations, which are inherently dynamic. People build jump tables and whatnot, and all these things rely on a construct like EOF. Even if it were theoretically possible to build all that, it would be a series of hacky changes that would never get the support to actually be done in Mainline EVM. So, EOF is the proper solution for these issues. In that sense, EOF is, for us, the simpler and superior design by orders of magnitude. It's not only the compiler infrastructure that we get but also verification and auditing bytecode analysis. All that becomes simpler with EOF. There's the other argument.

**Marius:** Quick question, when you're saying all of this becomes simpler, will you not support the normal legacy version of the EVM, or will you move the whole compiler to the new version, or will you just need to maintain two versions in Solidity as well?

**Daniel:** We will move to EOF by default because it's superior in all metrics once it's available. I imagine that we will need to maintain the legacy compiler version for some time until the community has caught up with the change. But long term, I would prefer to only support an EOF backend. There is no incentive, once EOF is live, to produce more legacy contracts because the metrics are superior in all aspects, really.

**Marius:** So L2s will need to follow EOF at this point.

**Daniel Kirchner:** Yes, I would. I mean, that’s also an interesting question about L2s in general. I would say there is this idea that EOF could just be done on L2s, but there is no evidence for L2s actually going beyond main compatibility. That’s the first and foremost goal of layer twos at this moment, which is understandable because we are not the only things that you need to actually produce an ecosystem that works on layer 2s. There is an entire stack below us that also needs to have that support. So, you not only have invaluable properties for L1 in gas cost simplification of bytecode analysis and whatnot, but if you want to have more development of L2s, actually putting EOF on L1 makes things simpler because you can use EOF contracts and transpile them to a new kind of execution engine.

Alex made the point for ZK implementations earlier; all that becomes simpler once EOF is on L1. So, I would even argue the opposite: if you want to have layer 2 innovation and want to facilitate that, putting EOF on layer one is probably the missing link that actually makes it possible to import the entire ecosystem to layer 2 while still innovating on it without losing the entire infrastructure that's built for L1.

**Tim Beiko:** Okay, thank you. Peter, you had your hand up as well?

**Peter Szilagyi:** Yes, so I think Daniel mentioned a few things that basically simplify the EVM, such as removing the need for jump test analysis, gas introspection, and code introspection. I completely agree with those improvements. My only concern is that when we talk about how many things we won’t need after EOF, it might be a bit of a false argument. As long as we don't have a way to deprecate legacy EVM stuff, we will still have to support everything besides EOF. There’s been some discussion that EOF can be better in several aspects, which I agree with, but essentially, we could end up with two independent EVMs that we need to maintain, plus we would have to manage the interplay between these two EVMs.

Every argument that suggests we can solve various thorny issues in the EVM is undermined if we allow EVM and legacy EOF to interact with each other. For example, removing gas introspection in EOF is meaningless if I can call a contract in the legacy EVM that still has access to it. Personally, I would feel much better if there was a way to transition out of the legacy EVM, either by stopping support for it or by implementing some mechanism to prevent its use. If we had a plan to transition everything toward EOF, even if it's midterm, it would make the case for EOF a lot stronger. The problem isn’t that EOF isn’t worth it; it’s the risk of having to maintain a dual system.

**Tim Beiko:** Thank you. Ansgar?

**Ansgar Dietrichs:** Yeah, I just wanted to say that I definitely agree that with the current situation on mainnet, having so many legacy contracts, we'll have to support both versions indefinitely. The benefit-cost trade-off is a bit unclear. But I think at the core of this issue is the question of the relationship between L1 and L2. We have a responsibility to acknowledge that, at least for now, L1 still very much sets the defaults for L2 in terms of client, Solidity, tooling, and everything else. If we don’t support something on mainnet for now, it just won’t reach L2s in the near term. We can say it should, but it just won’t. I hope we can work on changing that, and hopefully in two to three, or four years, L2s will be in a position where they can ship things independently.

Our decision here would be to delay progress on layer 2 EVMs where it would have a beneficial impact for a few more years. This issue will not only come up in this context but also in the future with account abstraction and similar matters. Managing both legacy and new systems introduces extra complexity, and it’s messier than starting fresh. We have a responsibility for the overall EVM ecosystem, so I would still be very much in favor of bringing EOF to mainnet.

**Peter Szilagyi:** Just to interject, I kind of agree with Ansgar on that. L1 basically sets the stage for L2, so if you want EOF on L2s, you need to get it into L1. Whether that would be ideal in an ideal world or not, that's the reality we’re in.

**Tim Beiko:** I think this is at least true for now. You could imagine a world where, four or five years from now, the second EOF version is something that L2s can ship on their own. But today, they can ship their own pre-compiles and maybe coordinate on a standard address for them. There are clearly a few years needed to standardize things a bit more. Daniel?

**Daniel:** One of the questions that was posed was about the plan to get rid of the Legacy EVM. I think we should absolutely aim to do that, starting with banning new deployments at some point. Once we have that, we can better handle the bad behaviors we’re banning in EOF and figure out how to manage existing contracts. EOF has the mandate to ban certain things that Legacy EVM has deployed today, and we must support them. No matter what that ban looks like, we will have to support it for existing contracts, even if we expire contracts. All expiration proposals had resurrection provisions. If a behavior exists, we have to support it. We can ban new deployments but need to manage the existing ones, understanding their issues, much like empty accounts and account number 3.

**Tim Beiko:** Obviously, step one towards banning Legacy deployments is having an alternative on mainnet. Considering our fork cadence, if we ship EOF at this fork, I don’t know if the next fork banning Legacy deployments will be quick enough or long enough. So, realistically, we might need to wait another three years or so before banning these deployments, and the time needed to figure out backward compatibility could add another year or two. So, we’re looking at possibly five years for this transition. Not that it isn’t a good or possible thing, but we should assume for the foreseeable future that we’ll need to maintain both versions. Peter?

**Peter Szilagyi:** I don't really think that’s realistic, honestly. If you’re going to ship EOF now and expect to address Legacy EVM issues in five years, then in five years, either Ethereum faces significant problems due to a chain split, or if nothing bad happens, everyone will probably just accept the status quo and say, "Well, okay, it kind of works, don’t touch it."

**Tim Beiko:** So I guess that’s my point: deploying EOF with the premise that we can then migrate from the Legacy EVM feels wrong. I think what Ansgar said, that L1 might just have to accept more messiness because of its higher historical state, is something we should accept as the status quo. Then maybe we come up with a solution for legacy contracts, but I would almost treat that as a bonus and not our base case going into this.

**Danno Ferrin:** Another thing I want to address is the notion that we’re maintaining two separate EVMs. We aren’t. If you look at the code of all the clients, it’s essentially the same loop. We are adding new container parsing functionality that is new and only supported by EOF, but when it splits out and we have the containers in the code, the loop runs through the same set of operations. We just have more operations that are context-dependent—whether the current stack frame is EOF or not. Certain operations will be valid, and certain operations won’t be. But the memory model is the same, the transient memory model is the same, the storage model is the same, the PC model is the same, the stack limits are the same. A lot of the stuff between the two EVMs is essentially the same, to the point that it even uses the same loop.

**Marius:** Yes, but it’s 19 new opcodes, and in the past we’ve shifted maybe two opcodes per hard fork. Even then, we had issues with consensus splits. EOF has already introduced three consensus issues, not in the EOF code itself but in the Legacy code. I’m not comfortable with the risk of introducing so many opcodes, so many gas computations, and the complexities of code and state verification. These are incredibly complex changes in a very important part of Ethereum, and I don’t see them being tested thoroughly enough. There have been good tests, but in my opinion, the risk is extremely high.

**Danno Ferrin:** It turned out well-tested when there were only two complete implementations. Just in the past week, we’ve finally been getting more complete implementations of clients. Now we can do the real testing with the implementations we have.

**Tim Beiko:** Thanks. One thing that might be valuable is to think about what our ideal test coverage should look like, even though we don’t have full coverage today and depend on implementations for that. If we can define what our bar for feeling comfortable is ahead of time, it might help us avoid making decisions based solely on the current state of testing. What would we want to see? I assume we’d want to fuzz this extensively and ensure we have comprehensive static tests. Are there specific test suites we think are missing? This might be a better discussion for the EOF call, but defining that bar ahead of time could be useful.

**Danno Ferrin:** By no means are we done writing tests. We’re maybe halfway through the test cycle, so judging the quantity of the tests while being halfway done is a bit premature.

**Guillaume:** When Danno says we don’t have to touch the state, that might be true today, but it’s definitely not true for the future. Not that it’s a showstopper, but I want to remind everyone that this claim won’t hold true for very long.

**Andrew Ashikhmin:** I agree with Marius that this is a very big and complicated change, but I think we have time to concentrate on it, push for it, and extend the tests to make it work. The merge was also complicated, but we managed to pull it off. I’m confident that if we put enough effort into it, we can make EOF work as well. If we don’t pursue it, we risk freezing progress on EVM development. EOF presents a coherent improvement to the EVM and opens up potential future enhancements, like EVM Max. Not shipping it in the upcoming fork might lead to disappointment and potentially abandonment of EOF and other improvements, which would be detrimental to Ethereum and the blockchain ecosystem.

**Lucasz:** While I agree that the changes are very complex, they need to be because we don’t want to ship them in parts, or in some cases, we can't. We want to avoid future fragmentation, so if we want to make significant improvements to the EVM, we need to ship them as a whole. If we don’t ship it now, we might not ship it for years, which is another concern. In terms of testing, I’m optimistic. We’ve already identified multiple issues with the current testing setup, and the tests are showing these effectively. We have plans for DoS benchmarking for all new opcodes and throughput comparisons across clients. I’d also like to see extensive fuzzing, which requires multiple implementations, and we’re just starting to get those. Before discussing the fuzzing state, my opinion is that we should continue as is and revisit if necessary.

**Marius:** My question would be: Are we going to delay the fork if we find more issues with EOF?

**Lucasz:** It depends on when we get there. If we find significant issues, we’ll address them, and if necessary, we might delay the fork or move EOF to a subsequent fork. We’re speculating at this point.

**Tim Beiko:** I agree that it's challenging to determine the readiness of things, especially with other significant changes. I would suggest focusing on whether EOF is valuable overall, rather than if it’s the right time or if we find a bug whether we should remove it or not.

**Dogan Alpasian:** I see two arguments against EOF. One is its complexity, but that can be mitigated by creating new tests. The current test suite isn’t enough, but we are working on new ones. The second argument is that it reduces complexity that might not be needed for L1. Against that argument, if L1 wants to improve itself and L2s, the change needs to come from L1. EOF extends the existing opcode set rather than introducing new complex logic to legacy bytecode. Even with two versions of bytecode, there won’t be significant divergence. With a good framework for testing the EVM, we can reuse tests for new opcodes. That’s all from me.

**Marius:** There are a bunch of bytecodes that are different. For example, <span style="color: green;">XCall</span>, <span style="color: green;">XDelegateCall</span>, and other calls are similar but differ in gas calculation and arguments. These are not just slight modifications but new opcodes. While most of the 80 opcodes are the same, there are 19 new opcodes.

**Dragan Rankita:** For example, in our EVM implementation, I’m using the same framework for the calls. The change is that the gas is changed and how the gas limit is calculated. There is additional code that’s duplicated but it uses the same framework as the ordinary calls. Additionally, interaction between legacy and the EOF is between how the external code is fetched. And additionally, there is a change in how the EOF gets created—those like interactions, basically the points where the legacy and EOF cross paths, there are not a lot of those.

**Guillaume:** I actually just wanted to ask a practical question, although I would like to note that I can see another issue with EOF: it's the lack of future-proofness. And I would like to know if, when Daniel says it's going to make things simpler for ZK, if you have references about this, that EOF indeed makes it easier for ZK stuff. But my question was actually: when EOF launches, will we already have compiler support or not? Or do we still have to wait a bit longer for that?

**Daniel:** We will have compiler support. And just quickly, the point about ZK is also in general. The point is that EOF code can be transpiled to a new execution engine, be that a ZK one or an improved non-ZK execution engine and whatnot. That's possible by the design of EOF. That's a nightmare or impossible for legacy EVM.

**Andrew Ashikhmin:** I'd like to note that I don't want to delay Pectra, but maybe delaying Pectra is not a bad thing because, from the panel on account abstraction, it looks like the design of 7702 is not settled yet and people need more time to figure out the proper design, a good design for that’s it.

**Lightclient:** I feel like the conversation is very focused on the practicalities of shipping EOF, but I don't think that's the right direction for the conversation, or at least the conversation that we should be having. EOF is useful; I don't think we're generally arguing that there isn't usefulness in the things that EOF provides. I think, in general, we can ship EOF given enough time and resources. So, I'm not questioning whether we can do it.

There are questions about how long it will take, and we've been talking a lot about that, and will we be able to get the testing done in that amount of time. If we spend a couple of years on EOF, I think we can ship it. But we're not asking the question as much: should we be making changes to the EVM? Should we be making this big of changes to the EVM? Why are we actively making L1 more complicated for a proposal that clearly is not necessary to the survival of Ethereum? I would rather focus L1 on doing things that are necessary to the survival of Ethereum, like looking at an inclusion list, reducing the size of L1 clients, making it easier for people to run L1 clients. We, as a core dev group, have sort of said that we want to focus on being a settlement layer and allowing L2s to take the baton on developing the execution layer for Ethereum. Yet we are trying to centrally plan the future for them, and I don't think that's our place. I don't think that that is useful for the future of Ethereum.

**Tim Beiko:** Danno thinks it's actually necessary, so I don't know if you want to maybe expand on that.

**Danno Ferrin:** I think it's not a two-year threat; like an inclusion list or some of those things might be a two-year threat. I think it's more of a 5 to 10-year threat for Ethereum if we don't improve the base case of the EVM, because I very reasonably see a future where if we don't improve the EVM and there are other alternative VMs out there— I won't name them on this call— there are some really good ones out there that the recommendations from Smart Contracting and other sources are going to be to use a modern VM. If L2s use those modern VMs, we're draining a moat that keeps Ethereum being Ethereum. These are EVM chains we're talking about, and if the recommendation is not to use the EVM chain, then we're draining them out. So I think it's a 5-year to 10-year threat. I don't think it's a next-year threat, but it's something that we need to keep in mind as we go forward building Ethereum.

**Lightclient:** I really don't like that framing, that we're forcing the entire community to use this new VM just so that Ethereum can retain users and keep a stranglehold on the innovation of execution. That's not what we're trying to build here. We're trying to build an open platform for people to experiment and build different virtual machines, and if a good virtual machine comes that doesn't start with E, then we should be very supportive of it.

**Danno Ferrin:** And that still exists in the world, but the default of L2s is to just fork an L1 client and work from there. So we're not foreclosing these other VMs; they're building and they're going to be out there, but the EVM is the last choice. Why use the EVM as a main layer? We need to make it better for L2s and L1s to align. If they're not aligned, that's the 5- to 10-year threat.

**Lightclient:** We're using it on the main layer because it is what is on the main layer. No one here is going to say that this is a great VM, the best VM ever built. It's just what we have, and we should try to make some incremental improvements to it, but we shouldn't ever go back and say this is the second version of the EVM. We're past that point now. It's time to let the L2s make the second version of the EVM or whatever other VM they want to make.

**Marius:** I don’t get the argument of saying L2s will move to these other VMs or these other VMs and we can stop them by making EOF on mainnet because if they see a benefit in moving to something like Stylus or whatever, then they will move there, and no amount of EOF will ever make them reconsider. And if EOF is like this great improvement over the EVM, then there should be no argument for L2s to adopt it.

**Danno Ferrin:** What we’re doing is bringing the EVM up to standards established in years like 1941 and 1996 with some of the container structures and static jumps. I mean, no one's getting a PhD off of EOF; we're just applying stuff that is known to be good. If we don't have that good base, it's about remaining competitive.

**Lightclient:** The base has clearly gotten us to be one of the biggest blockchains in the world and one of the most successful development blockchains in the world. So I don't think that we need to go back and rebuild the base from first principles.

**Marius:** I don’t know if I agree with that. I think maybe there is a case to be made to rebuild the main blockchain from first principles, but is EOF what we would end up with? Is this the best version of the EVM or virtual machine? Or is something that really doesn't look like the EVM at all, something better for L1?

**Tim Beiko:** I guess my sense at this point is that the Geth team is still opposed for a bunch of different reasons, and other teams still see EOF in favor. So my sense is at this point we would keep it in and obviously focus on testing and whatnot.

**Guillaume:** If I may dissent, we actually started the conversation by saying we will let it through; we're not going to try to block it. We're just not going to support it like we usually do with the rest of the forks. Meaning, other people will have to do some testing as well.

**Danno Ferrin:** Soylon and I myself have been writing most of the tests for EOF, we're already there.

**Marius:** And if it blows up on Mainnet, I will not stay up on a Saturday at 2 a.m. and try to fix it. I think this is the decision that I'm going to take if it ever happens. It might not happen; everything might go perfect. But if it happens, then I will not be there to help, sorry.

**Tim Beiko:** Okay, and yeah, I think there is a capacity from other teams to help with the testing and shipping this. So, I think my sense is we would keep it in the fork for now and obviously, like with any change, we'll reevaluate as we get farther down the testing stack. You know, like is this too complex? Do we think there’s too great a risk of bugs and consensus issues? Given that we don't have full finished implementations yet, we haven’t started fuzzing, there’s still a lot of static tests that need to be written, it seems like there’s still a lot of work to do to even get it to a spot where we can have this final call around security. Other client teams seem to be willing to take on that work. I think that’s my read so far. We can close with Guillaume, Greg, and Matt. And if anyone has any final comments on it, please raise your hand so that we can have them all on the screen. But otherwise, I think we can move on to the rest of the agenda.

**Guillaume:** So I'll try to be quick, but I had a question about the conversion, like deprecating legacy in the future. What if we had some kind of, I'm just basically throwing mud at the wall here, but if we had some way to deactivate all the introspection instructions before we actually deprecate our Legacy code, would that be an interesting medium step, let's say. I'm just curious. I would like to ask the EOF people and the compiler people.

**Danno:** There’s a whole category of contracts, data contracts, that would break, so we need to put in special handling for that. They start with code 00 and they just put data on there because the gas schedule currently encourages it. That’s going to change with vertical, but the data is out there and they still want to access it. So even if we deprecate it, we need to have facilities for them to access some of these things that, you know, they’ve been building their NFTs off. So we would definitely need to audit it and make sure that we know what we’re getting into. The first step is to ban Legacy deployments, and then we can analyze what the close set of the real issues are and what we really need to fix, rather than having all possible trolly issues come out when they find a new way to cause problems with the solutions we proposed.

**Greg Colvin:** I just wanted to go into one paragraph of Marius's critique, which is static program analysis. He points out correctly that as long as we have non-static jumps, the analysis of a program is in the worst case "order N squared." EOF removes dynamic jumps, which reduces the analysis to "order N" in the worst case. Over and over people seem not to get how very important this is. Marius goes on, "I'm not convinced that the difference is significant." Someone not being convinced doesn't mean that it's not significant. The people who care about this are totally blocked. The difference between linear time and quadratic time is the difference between being able to do something and something being impossible. In particular, this is so important.

**Marius:** What do you want to do, Greg?

**Greg:** I want, for nine years, to get rid of static jumps and introduce a subroutine instruction. This, I believe, is pretty much our last opportunity to do it. It's bigger and more complicated than we'd like because we haven't been able to do it incrementally over the last nine years, but it is good enough. We can't just keep trying to get it perfect. It's good enough, and if we don't solve the problem, we simply create a dead end for all kinds of research and improvements involving this. It's very diffuse. You asked on another channel. I'm not hearing people complaining about this. No, they've gone away. They have work to do. Pushing on the core devs to make their life easier is a waste of time. They have to improve the speed of their code now; they have to validate that their customers' code is correct now. We can help them hugely. The ZK people, some of them are going to heroics, using GPUs in parallel because their proof size is blowing up quadratically when they hit these jumps. This is a small kernel that's very important to get in. If EOF fails, I'll happily write a proposal that puts in again just those two instructions and a validation routine. But I'd rather see all of EOF go in because there's so much work and support and so much good that can come out of it.

**Marius:** I understand that you want to get this in. My question is why? What is the use case that you're trying to make that you need to get rid of the dynamic jumps for?

**Greg:** I've been trying to explain this for nine years. Lots of people have been explaining it for nine years. I don't even know how to answer a question that's—I don't know where to start.

**Tim Beiko**: Then, yeah, sorry. We're already pretty deep into this. I think let's—and you know, it seems like we're just going to keep working on it for now. So, yeah, Matt, you had your hand up as well.

**Matt Nelson:** Yeah, I'll make it super quick. We keep talking about, in many instances, trying to push this innovation to layer twos, but in very real circumstances, they're reliant on the L1 clients for most of their infrastructure and operations. So, it's not worth understating the fact that if we ship it into the clients themselves and use the kind of L1 mechanism to get that forward and push all of this stuff, then it opens the door to this type of innovation on layer 2 with the EVM specifically. I think this is what Danno was discussing when he talked about the moat that we would have. And, you know, there are proposals for basically being able to extend the capabilities of the EOF container and the versions. So, I think that it can't be understated that right now, the developer push on layer two is broad compatibility, so that people can deploy their dApps across all of these chains. Making sure that we can meet people where they are now is valuable, as opposed to saying, let’s kind of punt this innovation and see what shakes out. I think that would remove the reality of the situation we have now with both clients and layer twos' marketing and positioning with developers. At least that's my take here.

**Marius:** One last quick thing: What is stopping us from merging it into the client and not activating it on Mainnet? Then the L2s can take the code and run it and do whatever they want with it. I don’t get this argument that we need to do the work for the L2s. We already did the work for the L2s; they literally just need to take our code and run it. I don't know. It's fine, we've had this conversation; it’s still in. It’s going into Petra. I don’t think we should have any more discussions on it.

**Tim Beiko:** Yeah, I think this is a good spot to move on, especially given there are no L2s on this call speculating about why they won't support it. Yes, the recap: We keep it in Pectra. I think Geth has been pretty clear that, even though they won’t actively support the change, they won’t block it either. The usual amount of testing and security work will need to be performed by others who effectively want to champion EOF. This has already started happening, but we should double down on that. As always, you know, if we get to the point where we're close to shipping the fork and we feel uncomfortable with the safety of EOF or keep finding bugs that we don’t think we’re going to fix in time, we should reconsider having it in the fork. Yeah, we should continue working on it, testing it, and as soon as we have multiple final implementations, start fuzzing them against each other to find other bugs. Does that make sense to people? Okay, thanks everyone, and I appreciate people being civil in this discussion on the call. I know that a lot of people have very strong opinions about this.

## EIP-7702 proposed changes [58:30](https://www.youtube.com/live/kL58hvM0E68?si=3a7ZH-eABvMqnl9w&t=3510)

**Tim Beiko:** And so moving on to something else where people have very strong opinions:

There was, I believe, a Meetup around 7702 near ETC. A proposal came out of this to add the code reset functionality, and then there was a response posted on the agenda sort of opposing this. I've posted both of these links in the chat. I don't know if any of the supporters of code reset are on the call and want to give a quick overview.

**Ankitchinplunkar:** I wrote some of the proposal in the doc and I can give a brief overview of the overall discussion and what was proposed. I’m from Frontier, and I do research over there. To give some context, the proposal addresses some of the concerns a few teams have about the latest version of 7702, which makes smart contract code persistent. Before this latest version of 7702, or even before 7702, there were generally two types of accounts in Ethereum: EOAs (Externally Owned Accounts) and smart contract accounts. The current proposal introduces a new type of account where, in EOAs, you have a private key that can issue transactions. In a smart contract account, you have code on-chain that needs to run and validate before you can do things with that account. With the 7702 spec, a new type of account is introduced. This account has code, but it also includes an EOA private key, which acts as the superuser of the account.

So, this new type of account adds to the existing types: EOA and smart contract accounts. Now, there’s a new smart contract account with an EOA private key as the superuser.

There are two main issues with this setup:

1. Because this is a new type of account, there are some potential ways to perform a Denial of Service (DoS) attack on the network layer. While there are proposals to mitigate these risks, one of our suggestions also addresses this issue by reducing network load.

2. Since the EOA private key can function as a superuser, it can bypass the constraints that were previously put in place in your smart contract account. People also call these policies; the user can bypass these policies using the EOA private key and move assets. This makes some use cases unviable.

This makes some of the use cases unviable to give an example, if you have a multisig, the security of your assets is still dependent on the obscurity of your private key and not on the multisig. Or if you have some type of resource lock mechanism that would be beneficial for instantaneous multi-chain transactions, the user can bypass these resource locks because they have the ability to unilaterally move assets.
The proposal consists of three parts, each somewhat independent but aimed at solving these issues:

1. Removing EOAs' ability to initiate transactions on their own using private keys.

2. Introducing a mechanism for switching from a smart contract account back to an EOA. This involves the concept of "code reset" to delete the code, allowing users to revert to an EOA.

3. Addressing the current lack of a way to atomically initialize storage in the smart contract account when deploying 7702. This is referred to as the "option call data."

Those are the three different proposals, each trying to tackle different things.

**Tim Beiko:** Thank you. I believe there was a response to it. I don't know if the authors of that are on this call. If not, Ansgar, you also have some concerns. Okay, Julian and then we'll do Ansgar.

## - Response [1:03:56](https://www.youtube.com/live/kL58hvM0E68?si=YxecQ8jF7RIC14Wm&t=3836)

**Julian Rachman:** I won't spend too much time. Thanks, Ankitchin, for the proposal and the explanation. I thought I would provide a small analysis from the other side, trying to balance both technical stewardship and the interests of end-users and account holders and what they actually like want at the network layer. I'm the CEO of Otim Labs. We spent the greater part of the past nine months thinking really deeply about how to get to this next future of smart accounts. Broadly speaking, we spent a lot of time implementing 3074 on the contract and client level. We've obviously moved on to 7702, spent a lot of time thinking deeply about that, and have been there end-to-end for the process, seeing the proposal grow.

I won't dive too deeply into it, but our document is posted in the chat. There are clearly a couple of things here that are extremely important. One is ephemeral delegation and the concern for DoS, which I need to do some more reading on my end to better understand. Also, just the greater high level of what this proposal is bringing to the current spec state.

We are firm believers that, given this new proposal, being able to take a step back and think back to the original proposal or the current proposal that Matt wrote, it's more in favor of open innovation. Obviously, it's not going to push back 7702, which we would absolutely hate. Not introducing additional things, this would technically be a new opcode. I understand it's a variant of self-destruct, but understand that the current version of 7702 doesn't actually touch or edit the behavior of the VM. Rather, it's something that doesn't involve interacting with it.

We propose a potential alternative if ephemeral delegations must be included, proposing a flag to add to delegations in the authorization list that would designate this particular thing as ephemeral and then clearing the code hash at the end of the execution.

We've been writing a bunch of experimental contracts on some 7702 implementations and thinking about other ways that we could do this without touching the VM, etc. There are other things about shared storage. We've obviously read the namespace PR, which has gotten some pushback as well.

I'll stop there to keep it as high-level as possible, but feel free to take a look at the document. I'm happy to answer any additional questions in the chat.

**Ansgar:** I just wanted to say that I also wrote it down in chat that I personally don't like this new idea with code reset, primarily because it basically goes 90% of the way to a permanent upgrade but then stops 90% of the way, which I think is a really weird spot to stop because it still has this now special type of contract that in principle at some point in the future can return back to becoming an EOA, which just makes it so much harder to reason about. It basically creates this false sense of extra security over a permanent upgrade that really isn't there. It's basically the same security guarantees as a permanent upgrade.

So then I think if we want this, if we like this, then we should just commit and make it a permanent upgrade. The alternative should be that. So basically, just for people that maybe haven't followed this, because I feel like we are on level 25 of the discussion now, if you stopped paying attention a couple of weeks ago, initially, the swapping in the code was only done within the scope of a single transaction. At the end of the transaction, you are back to an EOA.

We changed that specifically because it is kind of nice to actually have the delegation targets stored in your account. But my proposal would be that storing it doesn't mean it has to be active all the time. I think storing it was an improvement, but now we decided as long as it's stored, it also has to be active. I think we should store it but then still only flag on an individual transaction scope whether it should be active. By default, it should still be an EOA while it's sitting there. I think that would be a much cleaner version that is closer to the original idea.

In terms of what we should do next steps, I just want to say that I think clearly we keep having these discussions, meaning we are not close to a super final spec yet. So we should keep having breakouts. I don't think this is necessarily the right forum for this. In the meantime, I think the current merged version, which is the change from Matt a couple of weeks ago that added this on-chain storing of the delegation target, is a very reasonable target for testing. I think any changes we will make from here on out will be relatively small. So my proposal would be we just stick with that version for now. We keep with dev nets targeting that version, and in the meantime, with breakouts, we try to get to a final spec and only once we have an actual final spec do we then move to that for testing.

**Tim Beiko:** Thank you. I agree that there's a lot of context in these conversations, and we may not be able to resolve everything here. Before accepting the change, we should have teams be much more confident in the actual proposals. Ankitchin?

**Ankitchinplunkar:** Yeah, I agree. This proposal was made to get feedback on where everyone's head is at. I agree this proposal is not to say, "Hey, let's change the 7702 spec right now," but I also wanted to highlight some of the things that smart contract wallets care about. If you give the user the ability to bypass the on-chain policies they have encoded, it makes the current migration path less secure and removes some use cases, like instantaneous chain transactions, making them unfeasible for these types of accounts. I wanted to highlight that. I'm happy that a lot of people who were in the whiteboarding session and reviewed the doc are willing to come to another breakout session where we can have a video call to update the spec or propose changes.

**Tim Beiko:** Do we think that we can resolve this asynchronously in the next couple of weeks, or do we feel like we need to have a breakout to discuss this more thoroughly? Pedro?

**Pedro:** Like I said in the chat and on Discord, this is something that just reopens the concerns we had around EOA migration. Specifically, how do you deal with the fact that a user might think they've migrated their wallet to a more secure access control policy, yet the private key still is able to sign messages that are accepted on-chain via EC recover? There is a reason we stopped going down the path of full EOA migration: we didn't have good answers for that. That's not to say there isn't a good answer, but we couldn't come up with something, and it felt like the right thing to do was to give users the hybrid ability to be a smart contract in some cases but always have the EOA private key as the master control for the account and allow it to originate transactions. That's why we ended up with 7702. I don't really think there’s a need to change that direction, because we spent a lot of time discussing it earlier this year and didn't find a better solution for EOA migration. Unless someone finds a better solution to full EOA migration dealing with EC recover, this seems like not a viable change to make to 7702.

**Tim Beiko:** Got it. Pedro, Richard, were either of your comments specifically about this?

**Pedro:** Yes, my comments are about 7702 as well. Basically, I think the most problematic thing that this proposal addresses is that one line exception. It feels like 3607 made it very clear that if there is contract code, then it cannot send transactions. This one line exception overrides that and makes 7702 do 3607 but if it does have a delegation, then it still can send transactions. I think that one should be addressed where you're either with contract deployed or you're not. You shouldn’t be in this in-between state where sometimes you're an EOA and sometimes you're a smart contract.

**Lightclient:** You have to look at why 3607 was implemented in the first place. 3607 was implemented because we were worried about somebody potentially deploying a smart contract with a private key in secret and then using that private key to drain the application's funds. With 7702 allowing them to submit transactions, it’s very clear that this is not an application; it’s a user wallet. It's got this delegate designator in front of it and so you can just see on-chain that this is not an application, it's a user wallet, so that's why it's okay to break the 3607 requirement.

**Tim Beiko:** Thank you. I agree that there's a lot of context in these conversations, and we may not be able to resolve everything here. Before accepting the change, we should have teams be much more confident in the actual proposals. Ankitchin?

**Ankitchinplunkar:** Yeah, I agree. This proposal was made to get feedback on where everyone's head is at. I agree this proposal is not to say, "Hey, let's change the 7702 spec right now," but I also wanted to highlight some of the things that smart contract wallets care about. If you give the user the ability to bypass the on-chain policies they have encoded, it makes the current migration path less secure and removes some use cases, like instantaneous chain transactions, making them unfeasible for these types of accounts. I wanted to highlight that. I'm happy that a lot of people who were in the whiteboarding session and reviewed the doc are willing to come to another breakout session where we can have a video call to update the spec or propose changes.

**Tim Beiko:** Do we think that we can resolve this asynchronously in the next couple of weeks, or do we feel like we need to have a breakout to discuss this more thoroughly? Pedro?

**Pedro:** Like I said in the chat and on Discord, this is something that just reopens the concerns we had around EOA migration. Specifically, how do you deal with the fact that a user might think they've migrated their wallet to a more secure access control policy, yet the private key still is able to sign messages that are accepted on-chain via EC recover? There is a reason we stopped going down the path of full EOA migration: we didn't have good answers for that. That's not to say there isn't a good answer, but we couldn't come up with something, and it felt like the right thing to do was to give users the hybrid ability to be a smart contract in some cases but always have the EOA private key as the master control for the account and allow it to originate transactions. That's why we ended up with 7702. I don't really think there’s a need to change that direction, because we spent a lot of time discussing it earlier this year and didn't find a better solution for EOA migration. Unless someone finds a better solution to full EOA migration dealing with EC recover, this seems like not a viable change to make to 7702.

**Tim Beiko:** Got it. Pedro, Richard, were either of your comments specifically about this?

**Pedro:** Yes, my comments are about 7702 as well. Basically, I think the most problematic thing that this proposal addresses is that one line exception. It feels like 3607 made it very clear that if there is contract code, then it cannot send transactions. This one line exception overrides that and makes 7702 do 3607 but if it does have a delegation, then it still can send transactions. I think that one should be addressed where you're either with contract deployed or you're not. You shouldn’t be in this in-between state where sometimes you're an EOA and sometimes you're a smart contract.

**Lightclient:** You have to look at why 3607 was implemented in the first place. 3607 was implemented because we were worried about somebody potentially deploying a smart contract with a private key in secret and then using that private key to drain the application's funds. With 7702 allowing them to submit transactions, it’s very clear that this is not an application; it’s a user wallet. It's got this delegate designator in front of it and so you can just see on-chain that this is not an application, it's a user wallet, so that's why it's okay to break the 3607 requirement.

**Pedro:** But then do you still have the ability to revoke? The idea of code reset is that you're able to essentially come back to being an EOA experience. The reason it was chosen to be an OP code is to be able to do that either after several transactions or atomically in the same transaction. That's why this proposal is broken down into multiple pieces—because it's trying to address users who want to have smart contract capabilities per single transaction, some that want to have it for multiple transactions, and most importantly, to have the ability to unmigrate as well.

**Lightclient:** Yeah, I mean, you can unmigrate by simply setting your delegate designator to the zero address. It's not possible in the same transaction currently, but 7702 is not designed for users who want execution abstraction on the single transaction level. It's supposed to help users use a smart contract wallet-like experience for the longer term, and if they want to completely turn that off, there is a way, but you just can't do it in the same transaction.

**Pedro:** Why is there any concern about doing it in a single transaction? Because this proposal does the same thing, but in a single transaction to be ephemeral.

**Lightclient:** One thing that we realized is that if you make it ephemeral, this is the problem with 3074: if you are allowing people to make things ephemeral, then you're sort of allowing them to have this different user experience from how smart contract wallets work. One thing that we have shifted the thinking on a lot in the last six months is that we want users to, however they're going to interact with the chain, whether it's a smart contract wallet or whatever, to interact with the chain as if they have a smart contract wallet. That allows us to streamline a lot of the way the tooling works and the way that applications can expect user accounts to look. If we also have this other alternative path for users to do execution abstracted things, then now we have this whole other ecosystem side quest world for developers to go down and build out different experiences. It's just not something that is a priority for the people working on accounts abstraction.

**Pedro:** I just feel like there are two camps. I was also a big proponent of making it permanent because single transaction was not sufficient, and I’m glad that change went through. But now the single transaction is not possible as well. So why isn’t there a solution that essentially makes it optional? You can do it in a single transaction or you can do it in multiple transactions. The OP code approach, which is actually just a rename of self-destruct, seemed to be the best of both worlds.

**Lightclient:** Why do you want the single transaction approach?

**Pedro:** One example of the single transaction is because in some cases, like a little bit more institutional, they already have these policies built off-chain with MPC and other infrastructure, but they still want the batching and the gas sponsoring. They want some of the functionality that is enabled by 4237 without actually having the permanent contract code on-chain that puts the policies on-chain. It’s a little bit more the retail case where the smart contracts would like to be more permanent. I think this is a more opinionated case where we went from single transaction to permanent, and I think we can have both. I don’t think it’s problematic to have both.

**Lightclient:** We can add everything; we can put the whole kitchen sink in there, but everything we add makes the proposal more complicated. Now what we're proposing is this code reset, which involves adding a new OP code and dealing with implementing this instruction. We can do these things; there are no theoretical reasons we can’t do them. It’s just that everything we do adds more complexity, and I’m trying to minimize the complexity of L1. As you heard with EOF, I don’t think we need to add anything to 7702 that's not absolutely critical. Additionally, I don’t think we should constrain the design of L1 to support existing business use cases. We need to do the right thing for L1 today and not overly focus on the types of businesses already built around the things.

**Pedro:** That’s one point of view. I’m not going to respond to whether we should cater to existing businesses, but I wanted to point out that the OP code is more like a renaming of self-destruct rather than adding a new OP code. We tried to make this proposal a bit more frictionless by bringing back self-destruct with a code reset that is specific.

**Tim Beiko:** I think we're not going to resolve this on this call. Let's move this conversation back to Discord for the next couple of weeks. We don’t even have Devnet 1 fully launched yet, which is based on an old spec of 7702. Let’s keep discussing the spec, and once we have something more concrete and we’re discussing future Devnet, we can figure out what to include.

**Richard Meisser:** Can I ask a quick question? Especially regarding the comments about the specs, it feels like they are still moving extremely. As someone coming from the smart contract perspective, I would be happy with these changes, but I'm more concerned about the timeline. Moving specs and changing them constantly makes it very hard to build tooling. I've been talking with Julian for two months now to get a test net up. If you change the spec constantly, it doesn’t make it easier and it's hard to understand how the current IP will turn out because we don’t have a test net to play with. What’s our timeline for freezing the spec and launching a test net where we can experiment before making further changes? It’s very challenging for application developers.

**Ankitchinplunkar:** We have a Devnet launching next week with what I believe is an old version of the spec, so we've effectively already done this. Maybe the approach should be to use Devnets to find bugs and resolve issues. When Devnet 1 ships, we’ll find bugs, address them, and see if it makes sense to fix them on Devnet 1 or relaunch Devnet 2. I think when we launch the next Devnet, that’s a logical point to look at what the spec is and see if there are changes we want to bring in Realistically, in a week, we’re going to have a 7702 version live on a Devnet with an old spec. Then, a couple of weeks after that, probably another Devnet. Whether or not we update the spec on that one depends on if we feel there's something stable enough that we could learn more from changing implementations than from keeping the old version. I know this isn’t ideal in terms of building tooling, but for shipping the fork as a whole, it’s probably the best we can do.

Also, like Pari and everyone else is pointed out in the chats, there are various ways we can launch local Devnets or run Dev branches with specific commits or spec versions. For the Devnets as a whole, we have to consider the entire fork, and when planning the next one, we need to evaluate the state of 7702 and decide if there’s something we want to include.

**Tim Beiko:** Okay, so we only have 8 minutes left. We didn’t get through nearly everything on the agenda. For the three other proposals that were there—the log system contracts, the coupling blobs EIP, and EIP 7212—it would make the most sense for the champions to give a quick update and then invite people to review and discuss asynchronously. We need to decide about any of those proposals on today’s call.

# EIP discussions

## Adding logs to system contracts [1:26:29](https://www.youtube.com/live/kL58hvM0E68?si=JRV6IcyngLfCV1YS&t=5189)

**Lightclient:** Regarding the logs proposal for the system contracts, do you have a PR for this?

**Lightclient:** I’m not the original proposer; I think PK was. We sort of agreed on this last All Core Devs. I just wanted to confirm that for Devnet 2 and going forward, we deploy the system contracts with the events. This is an event that happens whenever the user submits to the queue, not related to the system call.

**Tim Beiko:** The PR was recent, but I’d push for getting people to review it asynchronously in the next week. We can aim to merge it by the next Devs call. Does that sound good?

## EIP-7742: Uncouple blob count between CL and EL [1:25:26](https://www.youtube.com/live/kL58hvM0E68?si=K4nAiJSL1JgxjUSU&t=5126)

Okay, next up, Alex has a new EIP for Petra, EIP 7742. I don’t know if Alex is on the call, but this concerns the decoupling blobs count of EL and CL and have this just be a CL concern. This is a fairly new proposal. Having teams review it in the next week and I don't know if discussing it on this call makes sense.Any quick comments?

## RIP/EIP-7212 [1:26:11](https://www.youtube.com/live/kL58hvM0E68?si=adLBE2GCXC-zB-Se&t=5171)

**Tim Beiko:** Next up is RIP/EIP 7212. Ulas wrote a summary of the current state of things. There are a couple of decisions to be made here: first, do we want this on L1? And second, if we do, how do we approach it? Personally, I’m a bit skeptical about adding more to Pectra, given that we’ve spent almost the entire call discussing spec changes related to core elements of the fork. But Ulas, do you want to give some context? And if anyone else has strong opinions, feel free to share.

**Ulas Erdogan:** Sure. There’s been some debate around the EIP and RIP aspects. I want to clarify that the EIP documentation is outdated, and we have migrated everything to an RIP. The final spec is available, and it has been accepted by most of the rollups. It’s already live on mainnet for several chains. Adding it to L1 would be relatively straightforward since it’s already in use on some chains.

This proposal represents a small change with significant benefits. The elliptic curve it introduces is important for account abstraction as it provides additional signing methods. It’s widely supported by hardware and devices. Moreover, the ENS team is looking to use this curve for DNS-SEC and verifying Web2 domains. Rollup teams like Scroll, Taiko, and Flush are using trusted execution environments that only support this curve, making this proposal valuable for improving remote attestations and other use cases. So, it’s a meaningful proposal for L1 and should be relatively easy to implement.

**Tim Beiko:** We only have two minutes left. Any quick comments on this? Otherwise, it seems like there’s a lot of work on Devnet 1, EOF, and 7702 before we can consider additional proposals. Marius?

**Marius:** There’s another proposal in the RIP, I think 7969 or 7696, which adds a generic verification precompile. It’s apparently much more expensive. I just wanted to flag this; I would prefer specific precompiles rather than a generic one, as generic ones tend not to be used effectively. We’ve seen this with PL to F and it wasn’t used. Just wanted to mention this.

**Tim Beiko:** Thanks. Okay, we have only one minute left. Any updates on 4Forest or other items people think we should look at outside of this call?

**Tim Beiko:** Guess not. Well, in that case, thanks everyone. Please review the last three proposals we discussed, and we’ll continue the discussion in the next calls. Any final comments or questions?

**Tim Beiko:** Alright, thanks everyone. Talk to you all soon.

# Attendance list

Here's the updated list with **Mark Mackey** added:

**Zsolt Feffodi**  
**Zheng Leong Chua**  
**Daniel Kirchner**  
**Kolby Moroz Leibl**  
**Guillaume**  
**Danno Ferrin**  
**Lucas Lim**  
**Potuz**  
**Justin Florentine**  
**Mikhail Kalinin**  
**Mega**  
**Milos**  
**Richard Meissner**  
**Pooja Ranjan**  
**Ulas Erdogan**  
**Ansgar Dietrichs**  
**Mark Mackey**  
**Hadrien Croubios**  
**Danny**  
**Martin Paulucci**  
**Ben Edgington**  
**Pedro**  
**Terence**  
**Kevin King**  
**Ignacio**  
**Dogan Alpasian/Clave**  
**Daniel Lehner (Besu)**  
**Peter**  
**Draganrakita**  
**Ankitchiplunkar**  
**Lightclient**  
**Manu**  
**Scorbajio**  
**Tomasz Stanczak**  
**Greg Colvin**  
**Lukasz Rozmej**  
**Julian Rachman**  
**Pk910**  
**Kamil Sliwak**  
**Oliver**  
**Ben Adams**  
**Andrew Ashikmin**  
**Carl Beekhuizen**  
**Nicolas Consigny**  
**Saulinus Grigatis**  
**Trent**  
**Tim Beiko**  
**Justin Traglia**  
**Toni Wahrstaetter**

# Links discussed in Zoom chat

1. **[EIP-7480](https://eips.ethereum.org/EIPS/eip-7480)** - Provided by frangio
2. **[Solidity Version](https://github.com/ipsilon/solidity)** - Provided by draganrakita
3. **[EIP-7742](https://eips.ethereum.org/EIPS/eip-7742)** Provided by Tim Beiko
4. **[HackMD Document by Tim Beiko](https://hackmd.io/@ulerdogan/B1QikMxdC)** - Related to EIP discussions
5. **[GitHub Counterproposal for RIP-7696](https://github.com/ethereum/RIPs/blob/master/RIPS/rip-7696.md)** - Counterproposal adding a generic verification precompile

# Next ACDE

Aug 1, 14:00 UTC
