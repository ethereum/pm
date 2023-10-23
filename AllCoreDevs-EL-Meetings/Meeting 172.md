# Execution Layer Meeting #172
### Meeting Date/Time: Oct 12, 2023, 14:00-15:30 UTC
### Meeting Duration: 1hour 30 minutes
### [GitHub Agenda](https://github.com/ethereum/pm/issues/879)
### [Video of the meeting](https://youtu.be/t25IIQWfCnY)
### Moderator: Tim Bieko
### Notes: Alen (Santhosh)

| Decision Item | Description                                                              | 
| ------------- | ------------------------------------------------------------------------ | 
| 172.1 | **Dencun Testing** Devnet #9 now has a 93% participation rate, which means 93% of validators are actively participating in network consensus.
| 172.2 | **Dencun Testing** The 7% of validators that are not operational are comprised primarily of Geth (EL)/Teku (CL) validator nodes.
| 172.3 | **Dencun Testing** There are also issues with the Erigon (EL)/Prysm (CL) client combination, as well as the EthereumJS (EL) client.
| 172.4 | **Dencun Testing** The Flashbots team is testing an MEV-Boost relay and builder on Devnet #9. Busa encouraged other relay and builder operators to reach out to him so that more MEV infrastructure can be tested on Devnet #9.
| 172.5 | **Dencun Testing** Blob transactions are not yet being tested through MEV-Boost builders. Blobs are being dropped by builders, and developers are unsure if this is because the blobs are actually invalid, that is not meeting the minimum base fee requirement, or being dropped for some other reason.
| 172.6 | **Besu** Devnet #10 will not be ready this week but hopefully next week. For Devnet #10, developers expect to test the trusted set up file from the EIP 4844 KZG ceremony.
| 172.7 | **Dencun Testing** Devnet #10 will feature a large validator set, 330,000 active validators. At the genesis of the devnet, there will be an influx of validator deposits and exits to trigger a change to the validator entry churn limit from 5 to 4 roughly a day or two after network launch. The actual maximum entry churn limit that will be imposed on mainnet is 8, but developers will use a limit of 4 for ease of testing EIP 7514 on Devnet #10.
| 172.8 | **Dencun Testing** Busa emphasized that right now developers are still working through “big questions” in the process of testing Dencun. Until these questions are answered, developers will not move forward with the launch of Devnet #10, possibly the final devnet for Dencun before the upgrade is activated on public Ethereum testnets like Goerli. Summarizing what developers are looking for before launching Devnet #10, Jayanthi wrote in the Zoom chat box:Updated trusted setup files from the EIP 4844 KZG ceremony,Better visibility for blob transactions,MEV pipeline,Network stability   
| 172.9 | **Dencun Testing** Jayanthi encouraged client teams on the call to add support for this Beacon API to support better visibility for blob transactions. Beiko asked whether developers would feel comfortable upgrading the Goerli testnet after the launch of Devnet #10. Busa recommended waiting to see the results of Devnet #10 before deciding about next steps for upgrade testing.
| 172.10 | **EVM Object Format Development** Discussed the latest developments for EVM Object Format (EOF). EOF is a bundle of EIPs focused on changes to the EVM, which is the virtual machine built atop Ethereum that executes smart contract code. One of the champions for EOF, Danno Ferrin, presented a high-level summary of the work that has been done for EOF in the last several months.

# Intro
**Tim Beiko**
* Morning. Give people one more minute to show up and we can get started. I think we have most of the teams. Okay, let me post the agenda in the chat and I'll move us over. Okay. Oh I was muted okay. We should actually be live now. Um. Welcome everyone to 172. not a button on the agenda today, but we'll obviously cover Dencun. So updates around devnet, around client implementations and any issues that that are coming up. and then after that we have an update on the work.
* So there's been breakout calls happening for the past several months. so yeah, the folks working on that will let us know what's been happening there. but maybe to kick it off, I don't know if someone from the DevOps team wants to give Devnet update, and we can start from there. 

**Barnabas Busa**
* Here, I can begin. So definite nine is still running. We have about 93% participation rate right now. We have guests and Taku submitting bed blocks. So that's about 100 validators of the 1300 that we have around. So that's another 7%. So if we would bring guests into Quebec online, then it would be very close to the 100% participation rate. We have a few pairs that are not working though. Think Prism and Aragon is one of them.
* And Ethereum is struggling to keep up with the rest of the chain because we've been submitting transactions and blobs pretty much nonstop, and certain certain blocks have have over 200 transactions, and is just unable to keep up with that. So ten is supposed to launch this week, but I don't think we're going to be able to manage that.
* So we postponed it to next week and hopefully next week we can launch it. We would want to have the library available in the consensus spec repo, so each of the clients can include the proper files in their next release. Another note boost is working in progress. We have working really powered by Flashback Steam, and they also have a working builder, and we have quite some blocks that were proposed by them, proposed by their builder. So things are looking good, but I haven't been able to replicate their relay infra just yet.
* But we have the relay running right here. I just think the. Thank for that. And currently we have 265 validators registered for this relay. All of those are lodestar.
* I haven't had time to mess around with their clients just yet.thanks. Are all these seals ready to test the builder flow? 

**Tim Beiko**
* But guess it's not ready. Okay. Yes,For prison. Yeah. 

**Barnabas Busa**
* Yeah, that's a better way to ask it. 

**Parithosh**
* Setting. The only open question was if Nimbus merged the required pairs, because earlier I think all the other clients, we were able to test them on kurtosis, but we weren't able to do Nimbus yet. Is anyone from? Okay. We can ping them later on. Yeah. 

**Tim Beiko**
* Yeah. Look, you got a screen, but there's more than one screen. 

**Barnabas Busa**
* So there's a good question regarding blobs going through, and we have not been able to confirm any blob transcription using the imagery. So. Is anyone from Fleshpots here? Riddick or any other. 

**Stokes**
* I think they have an offsite this week. But yeah, that's just something we should pay attention to in the next couple weeks. 

**Barnabas Busa**
* Yeah, it would be very good if, if we could have block transactions going through also because right now it feels like all the blobs are getting dropped. Even when there's some blobs in the pool. 

**stokes**
* So like the builders ignoring them or there's some error. Okay. 

**Barnabas Busa**
* But this is this is like not confirmed behavior just yet. It's just a few examples that I've taken a look at where. 

**Parithosh**
* The main issue is that were spamming so many blobs that were almost always hitting the limit, and that just increases the base fee. And we're not necessarily sure yet if the missing blobs are due to the base fee being too high, and there's no valid blobs that could be included. Or if the builders in fact actually not including blobs that would have been otherwise included. But we'll try and get an answer for that over the next day. Cool. 

**Barnabas Busa**
* And I don't know if there's any other builder other than the flashback one. It would be very good if we would have at least one more that we could test out. 

**stokes**
* Yeah, I'm working on one and it should be ready soon. But yeah, I can circle around with you guys and we can work on that. 

**Barnabas Busa**
* Yeah, sure. As soon as you have any kind of prototype, we are happy to give it a test also. So just let us know. And regarding the. So we would like to iron out all these questions before we proceed to anything, because there's not much point of running with 300,000 validators if we still have open questions regarding billing. So we can now hold off with that until we have all of this confirmed. 

**Parithosh**
* And the other thing is because Devnet ten will be bigger, we want to make sure we have enough of the visibility tools to understand how block propagation looks. Tsatos added support for the event, monitoring the event stream for for blob related events and as far as I can tell, has already included that PR and Prysm has the PR as well. If the other clients could include that soon, that would be really helpful, because then we can get a visibility on every every client and when they're seeing blobs. 

**Barnabas Busa**
* Got it. And one more quick note that we plan to have about 330,000 validators, which is a churn limit of five, and we're hoping to make some deposits and exits right after Genesis. And then we're going to have Duncan, maybe a day or a day and a half later when all the deposits have reached the chain. And then hopefully we're going to see a cutback from 5 to 4, because we're not going to be able to test for the defaults or there's no point of testing for the minute defaults. I think it just makes sense to test going from 5 to 4. 

**Tim Beiko**
* Yeah, that would trigger. That would trigger the same code base, but using the the smaller presets. Minimal presets. Is that right? 

**Barnabas Busa**
* Yes. That's correct. 

**Tim Beiko**
* Yeah. And I guess I assume we'll keep mine running as well while we have at ten if we're still doing testing on it, because I think. It's probably valuable to have it, at least for a while. You know, in the case that, say, the 300,000 validators causes an issue or whatnot, like the to have them that mine still as a fallback. Is that possible? 

**Barnabas Busa**
* Yeah, that nine is pretty low cost. So yeah, we don't mind to have it around, but we don't know how long we plan to have them at ten. And the whole idea is that nine should be very stable before we proceed to them. But then we'd like no more big questions, which we still have at this point. 

**Tim Beiko**
* And so the. Yeah. So in terms of getting ready for Devnet ten. So you said there's the, the the PR that Perry just just linked that helps better track the blobs. making sure that the pipeline works well. making sure things are relatively stable on Devnet mine. And you think in the next week or so we can probably deploy them at ten. Is that right? 

**Parithosh**
* Yes. Oh, yeah. 

**Tim Beiko**
* And the trusted setup. Yeah. Thanks, Barry. 

**Barnabas Busa**
* And yeah, the trusted app needs to be updated, but all the different clients and I think some of them need like some recompilation or whatnot. So. 

**Tim Beiko**
* Yeah. Guess. Do. Any clients feel like it's not realistic to get this up in the next week or so. Okay. And then I know we had talked a couple times about Devin at Penn being like the last dev net if things go well. so assuming that net ten goes well in the next week or so, does it make sense? does it does it make sense to then start targeting Gaudi in the weeks after that? So either I don't know if by next call we'll have seen the results, but varies by the next dev we should have. Um. At that point, assuming things are working smoothly. are people comfortable moving to say, Gordie? I guess any oppositions or pushback. 

**Barnabas Busa**
* I think we should definitely wait for the results of that midterm.

**Tim Beiko**
* Okay. Yeah. Think that makes sense? So, yeah. Think if we can have that by. If we can have launched it by the next call next Thursday. That would be amazing. yeah. And we can we can discuss it further there.I guess any any client team want to share more about their progress or any issues they have or anything related to the to the fork itself. And there's a comment by Marius in the chat about Peter wanting to have a discussion about bandwidth. I don't know. Is Peter on the call? 

**Tim Beiko**
* No, I don't know. Marius. Yeah. Do you want to? 

**EF Security**
* Yeah. I don't, doesn't seem like he's here. I don't fully remember, but, he managed to get his node up and running on definite line and kind of saw the bandwidth that it was using because of all the blob spam, and it was kind of ridiculous. So we started implementing  a transaction handler that will only fetch one blob transaction, per run, whatever time that is. So it will not over like our current transaction handler would, would just overload itself because like if you connect to someone that has like a lot of blob transactions, they will announce them all and we will just fetch them indiscriminately.
* And so, yeah, I don't know if other clients have thought about this or if other clients also implemented it the way we did, because like the transaction pool actually now tops out at ten gigabytes for blob transactions. And if you like, if if you like, if you connect to a guest node and the guest node announces, for 4000 blob transactions, it will like murder your bandwidth. so yeah, just I think we should have a discussion about. I think the consensus layer should have a discussion about three six, like the bandwidth for blocks and like blobs in blocks. And we should also have a discussion about the bandwidth  for just the transaction spam. 

**Tim Beiko**
* And when you say have a discussion about three six, the implication being like two four. Would require less bandwidth. Or. 

**EF Security**
* Well, definitely two four would require less bandwidth on the on the consensus layer, but it doesn't have anything to do with the with the execution layer. So  the execution layer client teams have to make that decision if they they can support it. But they have to keep in mind that there will be blob spam. 

**Tim Beiko**
* Yeah, I know that there were there was some work done on the gossiping on the CL side. I don't know if anyone who's familiar with that is on the call right now. 
* Yeah. And yeah. Otherwise, I don't know if any of the other, um. Okay, like I said, the networking issues is different. I don't know. Yeah. You have the other else have thoughts on this? 

**Marek**
* I think we are working on similar thing in other mind right now, but Martin, could you share details? 

**Parithosh**
* Yes. We are planning to have some kind of throttling about, sending and requesting block transactions, but  it's not done yet, but it will be done before the. 

**Tim Beiko**
* And. Guess. Does it make sense to maybe go into this in more detail on Monday's testing call? Don't know if this gives a couple of days for the EL client teams to, like, look at it a bit more and then maybe we can have Peter come up there or or otherwise someone else from get sort of walk through it in. More details. 

**EF Security**
* So. Okay, okay, Marius. 

**Tim Beiko**
* I will be waiting for you on Monday. And then. Yeah, if other client teams want to look at that, um. Yeah. By then we can. Yeah, we can discuss it more then. 
* Any other issues that any kind teams want to bring up about the fork. Okay. anything else that we want to cover before going into EOF. Otherwise. Daniel, I think you're the one who's going to share the update. All right. 

**Danno Ferrin**
* Well, I think so. don't see any of the other typical people on the call who'll be giving feedback on my slides. do I have screen sharing capabilities? 

**Tim Beiko**
* Try. We'll see. 

**Danno Ferrin**
* All right. Cool. So let me get to. Um. So the big proposal today, well, in the update is to move Prague towards being headliner for to make headliner for the upcoming Prague release. And we're going to give an update of where we're at and what's been developed and what is. Make sure everyone's on the same page for what it is. So first, when I say we in our I think that's important to. Talk about that and I can figure out how to work the slides. Okay. And there's four major groups of people working on the object format. The first team, the team that created and and did a lot of the early legwork in getting it up and running is Team Epsilon.This is an EFF funded team and it's focusing on improvements.
* They also have another project that they run. They make a standalone C plus plus interpreter one, and they used to work on the Wasm. So they know a lot about why Wasm won't really work from doing it, which is really important to know that through doing it. Why it won't work. Second group of people is we have execution clients, representatives from there that people from GitHub who never mind. And occasionally we've had some arrogance, but they're going to, you know, work with mostly gets VM. So it's going to be fairly easy to port there. And at least back in January, all the teams had the same quote unquote big implementation.
* And we were actually doing fuzzing on the container format and on implementations before it was decided that was not ready for Shanghai. Part of the reason we discovered why wasn't ready for Shanghai was this third group that's been involved, very involved in the past few months, the compiler teams, we've had representatives from Solidity and Viper giving very valuable feedback on some details of a few new features have been added to support them, but mostly it's been working on the finer grain details of, you know, we need this for the compiler. 
* This will solve some size regressions. It's mostly there. We have most of the solutions we have we know that we need to do in either this release in a big release, or maybe in a few opcodes in the next release, but their input has been invaluable and validating that what we've worked for is going to work within the compiler teams. And another important thing is that the downstream users of the compilers themselves are on board with it. And I think another important group that has shown up is we had some people come in from from various data contract teams that Store2 is one of them. They want to use the contracts for data.
* And they've been, you know, interested to see how some of the changes we've been doing from will impact their work and what we have. You know, there's one opcode they have proposed that would make their job a lot easier. But even if we don't have that opcode, they're confident that what they're doing test or two will work with and will be acceptable for what their needs are. So what is the object? Format is mostly a container format for code. The big thing is it separates code and data, which is one of the big bass problems when it comes to taking EVM and converting it to any other format is where's the code and where is the data, and can we make hard and fast rules about it? Solidity and Vyper have adopted some conventions, but those aren't enforced as part of the container format.
* Container format makes a separation a mandatory, and it also requires that all code is valid.
* So if you see bad data in there, you know you can't see bad code in there that is masquerading as data or data masquerading as code. 
* If it's code, it must be valid and it must be executable, and data can be whatever it needs to be. And the two never mix. And because of this, we're able to fix a lot of evolution problems. A famous one is we're not able to add any opcodes that take immediate arguments because of an interaction that if a jump test is inside of what would become covered by invalid code, that would make the next immediate a jump target and get jump target in theory. You're changing the execution of the contract. So that was something that was was done away with pretty early in the product in the process. And we're also able to prohibit a lot of problematic behavior.
* A lot of things that get in the way of supporting things like ZK and translation to other formats, and just translation between different versions of the EVM if we need to change things. So that gets it to the next question. You know, how many versions of are there going to be? How is it going to work? The idea is that will operate in parallel with legacy smart contracts. I don't think there's a reasonable way. Short term, to ban legacy code. Maybe in long term once has wide adoption and we can lock down the addition of new contracts and do that deliberately. But as far as I think the plan is, there will only be one version, and it would be if we need to update the format, there would be standard translations between the two, but that's not set in stone.
* But what's planned today is there's just one version and one legacy version. Now it sounds like you're putting two VMs in Etherebut we're not. The difference between legacy EVM are almost entirely in the packaging and the validation of the code, and in some of the opcodes that are supported. 
* But once you get away from that, the EVM legacy and are the same. They use opcodes, they use stacks, they access storage in the same way, the access accounts, in the same way they work with message frames, the same way they revert in the same way memory and transient storage are performed in the same way. It's just a different way to package it. It's whether you're, you know, whether you're driving a truck or a car, I guess is probably the best way to describe it. There's still four wheels. You still have to follow all the traffic rules. there's just a different place to put all of your all of your equipment goes in the back of the truck. So, um. I would say is the truck, because we separate the cargo from the people.
* Now, what are the major features of now that we got, you know, an overview of how we're going to do it and where it fits in.
* What are these big major problems that is fixing? And I've identified about eight major things that addresses. The first thing is the container itself is a big feature set of two separate data and code static jumps, something that people have been asking for for years. Now that we can do a media to something we can build into. Another thing that people have been asking for for years is subroutines. We have a facility that does subroutines really nicely. Code and data separation is another issue that gets up. and finally, some of these things down here are some more recent discoveries as we're working with and working with these SSC systems and everything else, some things that would be very useful and valuable to make sure that we don't have to mess with that. 
* In theory, this version of could be the one and forever. If we get everything done right, the first thing is we're removing code introspection capabilities. That means that you can't take code, put it into memory, and then deploy that. What you execute and what you deploy come in two different streams. I'll talk about that in a slide later down. Gas observability is another problem. Let's say we need to change this gas schedule dramatically. Again, if you can't tell how much gas you're using, you can't control some things about gas. Then there's easy solutions to change those schedules. Code and stack validation is another important thing, that we can make sure that we're actually putting in real code.
* And that makes it easier to to add things to without having to reboot the world. If we can guarantee that the code that is not used doesn't show up until it's used. And the last one that came up in the past couple of weeks that we've been talking about, haven't committed to, is to maybe prepare for address based expansion, a little bit of trivia. Any opcode that takes an address will only take the lower 160 bytes of the stack argument, and the top 100 or so bytes, or whatever's left over, are trimmed, and this is used sometimes it's useful in some, decoding tricks. But if we want to use address space expansion, we need to make space for that and be the right time to do it.
* If we're going to break things that need to be broken for the future, let's break them down in the container. So that's kind of the theme going on there. So the first thing is the object framework described in 3540. It defines a container format and it's got basically five sections the header, the types for stack validation, the code itself, sub containers, which is something we'll talk about in code creation. 
* This is basically if you have a factory contract that's deploying other contracts, it's going to show up in these sub containers. And finally the data section where you can store your data and your constant variables. the next 4200 static relative jumps. Fairly simple. We ban three instructions jump, jump, and PC and we add three instructions. Our jump, our jump AI and we take the opportunity to add a really useful instruction, a vector jump operation, which will save a lot of code in things like Solidity and Viper compilers. They can do some really useful things with that operation. 4750 we add functions aka code sections and this is the subroutine support solution.
* Code is broken in a separate code sections that are self-contained. To support this, we need to add three opcodes. Call F, return F, which is basically your gosub and your return sub and jump F, which is basically tail recursion support. This is something that can be really useful. for a lot of recursion solutions you could jump f into yourself and other things. It's something that compiler people get really excited about. Java wishes they have it and we don't. So we're going to put it in F. and there's also stack height restrictions that are enforced with the opcodes when you go between the functions. So they actually act like functions.
* You pass in three stack items. One stack item comes out. You can conceptualize it like that. VIP 663 unlimited dupe and swap is really old. Request to access the full depth of the of the stack. Right now it's looking like it's going to be a dupe, in which dupes an arbitrary depth in an operation called exchange. This used to be swap in where you'd have two immediate arguments, but there's duplication like a swap two three and a swap three two are doing the same thing. 
* So if we do some neat tricks with requiring them to be in order of the stack, you can access twice the distance with smaller operation codes, and we may have a two byte variant of the exchange. These are some of the details we're working through out now. The old dupe and swap instructions will remain even though we could get rid of them. We don't want to disrupt the instruction set too much. Yep, 7480. so now we're getting to some of the higher level requests. And this is for remove code inspection capabilities. And this is the read half of that. So in order to prevent code from being intercepted, you shouldn't be able to read code that other contracts have.
* So we're going to have to ban the ability to read your own contract code, code size and code copy, and also to read other people's contracts codes. The code size code copy code hash. So the problem is we discovered in Shanghai is that solidity will use this data to write immediate to write constants. They'll rewrite their code sometimes for constants for the constructors. So to accommodate that, we allow access to the data section from within your code. You can load data from your data section. Data load data load in as an immediate argument. Variant data size data copy.
* And you can access your data in your contract and you can expose it to other people if you want through methods. you know, it goes in the stack and the data works just fine. now, a couple of compatibility things is that the legacy will not be able to use code into contracts to ensure this readability results.
* There are some standard responses that we have planned. It'll look like a really short contract and they can't read it.
* And also, Data Star, I should have dropped that last line that that is something that's under discussion. These may or may not be available to. There is an data copy that may or may not be available. So should have fixed that um last night. The right half of the code introspection capabilities comes from the create. And as we know, when we do creates now we take the entire contract. We put it into memory, we wrap around it the memory, and we deploy those bytes. That is not something that's going to work when the underlying execution is not necessarily interpreted. Even if you're taking these contracts and compile them to a circuit. It makes it really difficult. And you got to have these like terabyte Ram systems to generate the proofs when you do that.
*  So we're going to propose a replacement called create three and create four where you create your contracts.
* But the code does not exist within the EVM. It comes from outside of the EVM from two different places. Create three handles it where the container contains the code you would be deploying, and this is useful in factory situations where you like deploying another liquidity pool. You know what that pool looks like. So it's going to be in the code and you're going to deploy it straight from there. So you get your factory together and it comes all in one contract and it's all self-contained. So you never have to see the code. You can deploy it. And the other option is create for and that's where you get it from someplace outside of the container or the EVM completely. And the initial plan is to have it from a new field and a new transaction type.
* That's gonna we're going to need to see where winds up in the next few months, or we're going to need to put a new type to get these transactions, to get the contract data in a transaction type. 
* And, you know, that's great for it's a bit flexible. We could go crazy if we want. With layer twos, we could have layer twos that have a small stable of contracts that'll allow you to do and create fork and access those. But for main net we're just going to do it in transaction type. we need a new return code to handle adding data onto the end of these contracts. And this is something that solidity have explicitly requested for their immutable values. So they can. If you say that you have a constant file that you initialize in your constructor, we actually write that into the code that's deployed as part of data at the end of the existing data section. So return contract also allows for auxiliary data to be added on to these contracts. Just data, no code.
* Now to handle the remove gas observability capabilities, we need to address gas and the call operations. So call codes on this list.
* But whether or not 7069 advances call code is not going to be an it's going to be one of those banned instructions. Call code and self-destruct will not be an off, regardless of how things shake out in any of these other chips. But the remaining four operations banned would be gas. You can't query how much gas do I have left and call static calling delegate call. The reason we need to replace call with call to data, call to and delegate call to is to remove the ability to specify how much gas. Instead, replace it with passing in all the gas you have with some stipend restrictions and reserve restrictions, so that it's mechanical and you know whether the 63/64 remains or gets changed is all transparent to the contract. 
* And what's interesting is we're also going to take the opportunity to remove the output location, stack operands to make it even tighter and smaller, because a lot of people just use the return data. And there's we could do return data copy, add an opcode. They can make things smaller and tighter. So your calls can be as low as four bytes or three bytes, depending upon which variant that you're doing. If you're passing in value or not. Delegate calls, not three bytes. Delegate call would be like a three stack argument, which would really, you know, make things a lot more compact on on calls. Now the fallout of this is is really valuable thing.
* If we need to change the gas schedule and increase store operations five x, there's not going to be any contracts in that are going to be frozen because you can't specify too little gas going on to the next call.
* This is the problem we had back in Constantinople and something we fixed in Berlin with the access lists. But if you can't specify gas, which is, by the way, that's the default operation of all compilers. When you do a call, unless you specify gas, it sends it all, that if we increase the gas, then the solutions with gas schedule changes always send more gas at the top level transaction. And finally we get to some of the more just details of making sure that it works well. 3670 specifies the code validation. We check things like make sure the jump destinations are fine, code sections exist, the containers exist. and it also makes it so we can make some future evolution of if there is code that is not going to show up, we can use an opcode and we can be sure that it's not being used elsewhere. 
* 5450 ads stack validation. this is some, some inside stuff for for compilers to make sure that we can do optimizations and interpreters. This will allow us to create minimal sized stacks for contracts, rather than creating the Big 1024 stack and hoping they don't overflow. We can guarantee through code it's only going to consume ten, and we only need to make a stack of ten, and we can optimize a lot of performance in the in the interpreters because of this. Um. I'll come back to Mary's discussion at the end of this, but that's a good point. so. Miscellaneous notes. there's there's some corner cases that we need to put in to make sure that things work out well. One notable thing is, and legacy can freely call each other with one exception.
* You cannot delegate call legacy. And the reason we do that is because the next point which is self destruct is banned.
* So if you have an contract, you could delegate call to a legacy contract that all it does is self destruct. And all of a sudden we have to deal with self destruct instead of. So that's why we don't delegate calls. So you can't use delegate call as an escape hatch to get access to functionality we banned inside of the. and another thing is and legacy cannot cross create. Your factory can only create contracts. Your legacy can only create legacy contracts. This keeps the two worlds a little more rational and a little more sane. So we don't have to deal with this big matrix of what if this happens and what if that happens? It's just a lot easier to implement. So a quick summary on the opcodes. There is a net plus two of opcodes available inside of EVM.
* There may be some more coming. There may be about four more coming to accommodate compiler performance regressions. Size and mostly size regressions for code. but the minimum required. Um. The men required are these opcodes to address Ansgar. We were kind of removing self-destruct in Duncan, but in the code you can't even have the opcode. We can't even have the sweep operation. We're just getting rid of it completely. There's none of this game's about. Can you do it in the same transaction? so we have nine operations that we are replacing functionality with to deal with, the improvements we're trying to do within and the worlds we're trying to change. There are seven opcodes that we are straight up removing with no replacements. gas self-destruct call code.
* The ones and we are adding nine opcodes to, to add features that make sense within the vector jumps, subroutines, unlimited dupe and swap, and the data support to handle the code.
*  It's kind of a replacement for the but kind of not really for the code copy and code size and return contract for creates. Um. So talking about some of the more inside baseball features of what's going on. One of the biggest issues is, of course, testing. When you ship things for hard forks and think we're going to have a little bit of a different, a little easier time, a little more well-defined time than some of these larger network changes. The reason is the is fairly self-contained. We don't need to worry about network interactions. We don't need to worry about pairing with different combinations. I don't think we're going to need the same level of dev net and test net, and that's because of the way that we're able to test it. 
* We're going to write explicit reference tests. These are the gold standards for are you a compatible is do you run these tests. The client teams can help out because we need to test our own code. And some of our tests become great reference tests when we test the edge cases. The big advantage that we have is this differential testing that's been going on. Martin wrote some differential testing. Marius wrote some, Guido. Guido wrote some, and they've made some amazing findings. And it's been pretty boring recently with their differential testers. They've been running them for a while and have been finding much. Guido's got some, you know. The would was be able to find four bases so far as a few performance issues, some corner cases that are really creative and inventive that the Fuzzer was able to find.
* Probably get a blog post about some of his findings here in a few months, once it's shipped on Hedera's main net. But these fuzzers are great at finding these strange problems, and we also have container fuzzing that Martin had written back in December January to test the container fuzzing. So we can we can test that. so the big proposal is when is that? It would be the headliner for Prague, and I would think it'd be 3 to 6 months after Cancun actually ships on May. Net is when we would start or actually ship it on May net. My my thought of you would ship at least three months after Cancun. We would start the test net cycle, but we'd be doing dev net cycles well before then. So that over three probably so I think Martin said we can't modify the gas schedule anyway since most contracts will be legacy. 
* So. Right. So this gives us the flexibility for to charge different gas schedules. but as far as thinking outside of main net, if we had layer twos that were just, they could have much more flexibility in their gas schedule definitions. If we had systems that were all, they already are doing crazy things with their gas schedules, and self-destruct. You used to have a consensus issue, which some network issues don't happen. Yeah. That's why we need a that's why we test very thoroughly on the EVMs and very extensively. So it's not that it's without risk and testing. The risks are just shaped differently. Um. At Ansgar. In my opinion. I would really like to see one more round of.
*  Is this as Ford compatible as possible regarding gas introspection without excited, we just brought to me that ideally in the next work. So yes. So if anyone has any opinions on things that need to be addressed to ensure that is maximally forward compatible, please bring them up. We have calls every every Wednesday on weeks off of the execution call at about roughly the same time, call in the channel. Share all the information that you have. Share your opinions. Now is absolutely the right time to bring anything else up. Um. Yeah. And there's. Yeah, there's there's still some. The best discord channel is going to be in the discord. That's the best place to discuss this. So that's the end of my presentation. Um open for questions, concerns, comments. 

**Tim Beiko**
* Thank you. Okay. Barnabas has a couple questions. Do you want to read them off? And? Yeah. Answer them. 

**Barnabas Busa**
* Yes, sir. So my main question is who is the EOF champion and who is pushing for all of these changes to happen? 

**Danno Ferrin**
* I would say Team Epsilon probably has the strongest ownership of it. I happen to have some slides ready because I presented about this at East Chicago. I'd be willing to slide in that role if Epsilon doesn't want to, but I think Epsilon is the strongest, has the strongest stake in this right now. 

**Barnabas Busa**
* Okay. My next question would be do we have a spec list ready? And is this spec list like pretty much good to go? Is it ready? 

**Danno Ferrin**
* So we have a hack that is a fairly complete list. Basically it's a complete list. We're not adding new features. We might add some things like jump for. conditional jumps and conditional calls and an code copy. But the list of possible adds is really slow. And yeah, like client pasted it and that's well, that's the full spec right now. There's some additions that, we're talking over with, with Viper and Solidity that might be added, but that list is also small. There's another list that has the open issues and those are discussed there.
* I don't have that on hand currently, but if you go into the channel and scroll back, you'll find the open issues link for sure. but as far as specs, I think the only specs we are missing are the data spec and the create three create four spec.
*  And I think what's holding off the create three create four spec is we're trying to get some signal on whether we should propose a field in the SSD, or whether we should propose a new transaction type, like the blob type. not, you know, not where instead of patching in blobs, you pass in contracts. and so there are a couple more chips that will be posted. And also just the whole drama with the split have been writing until we get more clarity on that. because we're weren't sure where those were going to land for the for the Prague release, but it looks like the split is actually going to happen.
*  They're just working on final technical details. can we begin planning only devinettes? so you said about a month away from. Go ahead. 

**Barnabas Busa**
* Yeah. You you mentioned we don't need, like, proper devinettes for Inter, but I think think the transition is one of the major questions here. No. 

**Danno Ferrin**
* So yeah we can test the for transition for the devnet. I guess my comment about the devnet is, we're not really testing. We're not adding new network behavior. We're not shaking out network behavior in the new clients. So doing a shadow fork really wouldn't do much unless we're going to inject new transactions and put a new contracts and execute and exercise the new contracts. whereas versus when we were doing the merge and when we were doing withdrawals, shadow forks were invaluable in the best way to test them, I think.
* So that's, you know, when say, testing is shaped differently, things that were invaluable for, for the merge, I think more more useful is going to be the fuzzing and, you know, probably test networks.
*  And I think the best thing we could do is just get everyone to get their contracts when the, when they got versions of Solidity and Viper that will commit and just compile them down into and see if see how things work out there. Of course, some features won't work if you're relying on code copying the stuff that does work, you know that would be. Probably the best thing is to take these existing contracts is probably go through ether scan, get all the contracts and just compile them down and just turn on the flag. So that would probably be the replacement for Shadow Forks. 

**Barnabas Busa**
* Yeah. My next question would be is any clients have any implementation of this? 

**Danno Ferrin**
* Since we're not finalized on the spec? No. We did have stuff on big that was going to be finalized in Shanghai. That was finalized in Shanghai. I think Nethermind. Geth and Besu had PR ready that were fuzzing to the same results. so that's that shouldn't take too long. All the heavy lifting has been written into the clients or in the PRS, which is parsing the container and making sure that there's interop between the legacy and the EVM. And a lot of the stuff is already still there. We're using the same opcode loops, we're using the same facilities to access accounts and storage. So it's just wiring those things in there. 

**Barnabas Busa**
* Okay. Thanks for all the answers. 

**Tim Beiko**
* And there's a question around ERC. So some have tests for contract like 721 on received. How would that work without the code in introspection. 

**Danno Ferrin**
* So if it's what I'm thinking of is, it's they're supposed to be an interface where you can send a recall, a contract with a certain interface with a certain  function, and if it understands the interface, it says, yes, I support that. Otherwise it returns don't have that interface. So when you check for on received, you're not actually inspecting the bytecode because in theory it could be solidity doing it. It could be Viper. It could be for faking it out and accepting a non received API. So that preambles for these various even solidity versions change a bit differently.
* So you don't actually check the code to see if you're compatible. You call a function that says hey, do you support this?
* And if it understands it and comes back and says yes, then you know it's a 721. EOF supports the current framework transparently. Expect it to. 

**Tim Beiko**
* Thanks, Ben. Don't know if that answered your question fully. If not, feel free to either speak up or post a follow up. 

**Danno Ferrin**
* Yeah, think it's EFC-165 is the one I was thinking of. So that's got the standard of how you would call a function to say, hey, do you support? And you would be doing that off chain typically to test for it, although sometimes you wouldn't when you're being sent stuff. But. 

**Tim Beiko**
* Okay. Yeah. And and Alex says none of the widely used is actually inspect the code of contracts. Um. Okay, so there's a Lucas has a question, I think, Daniel, you sort of covered this during your slides. But what are the direct benefits of EOF what does it solve? The complications of the EVM are quite huge. So why is it worth it? Why should we ship it? And I know you had a slide with like eight benefits, so maybe. 

**Danno Ferrin**
* Yeah. Let me go back there. So these are the eight themes that we're going to support in. And probably the biggest reason we need to change some of these things is the core of the EVM was written over the weekend. You know, these are people that knew what they were doing with computer science. They'd done compiler stuff, but they only had a weekend to work on it. And some of these design decisions, they didn't have time to to think about what were the ten, 20 year implications of it. and one of the things that I think that snuck in is the push with Immediates and that blocks out the ability to add other immediates.
* And then there's also the segmentation of the code that you can't have code and data separated. so. In order to support all that. We can't change those with legacy. But in Object Framework we get a format where that is logical. So what this is providing us is an opportunity to get a path to make this rational to where when we get broader adoption, we can slowly tamper down the legacy, make it more expensive to support legacy, maybe just shut off legacy and get all the features in, and then we could possibly figure out a way to transition legacy to off. So that is one long term possibility.
* But I think the bigger problem that this solves with is the ability to evolve the EVM in a more efficient and modern way, because otherwise we're going to start losing language development to other systems.
* And that may or may not be a bad thing. But, you know, if it's not the main system that Maynard is using, there's a risk that, you know, we lose, that the sum is greater than the, the the sum of the parts.
* The whole is greater than the sum of the parts. So yeah, there is, you know, risk in doing this and risk that it may not be valuable, but as far as you know, making an making the whole combination of Ethereum main net valuable. This provides a path to to solving some of those little problems. 

**EF Security**
* Yeah. So I just don't see how like which use cases would this unlock? Basically everything this this kind of unlocks is just making existing patterns and compilers kind of cheaper. But is this really what we're like? What what a manor should evolve to? I think I like this idea of having, having like only l twos, but, then. I think in order to support this kind of, we need to we need to completely have these two separate EVMs have the legacy EVM and the the the EVM, and they cannot interact. And this will break composability. So it's kind of a non-starter. yeah. I'm just not I and I've I've been quite vocal about it that I don't think is a good idea at all. and it's just like, yeah, we're adding some stuff, but we can add these most of the things.
* We could add in the existing EVM. And the things that we can't are not quite worth it for me. then, like, I haven't really seen a big push from compiler teams really wanting this. maybe they want this, but, um. And the other thing that I really dislike about it is that now the kind of this verification of the code becomes part of the consensus when you deploy a contract. Thus the contract code has to be verified, right? and this thing. 
* We can shoot ourselves like it's the verifications. As I understand, are not that complex, but we might want to do more complex verifications in the future. And the thing is, like if we if I deploy a contract that can evade one of those verifications, then I've kind of totally broken the chain. And so there's a new like it's a new big class of, of consensus issues, that of potential consensus issues that we might get with this. Right. 

**Danno Ferrin**
* Yeah. Ansgar's got his hand risen on this question, so I'll let him. It seems like he wants to answer some of it. Or do you want to ask a question? 

**Ansgar**
* Well. No. Yeah I was. This thing. Like. We can shoot ourselves like it's the verifications, as I understand, are not that complex, but we might want to do more complex verifications in the future. And the thing is like if we if I deploy a contract that can evade one of those verifications, then I've kind of totally broken the chain. And so there's a new like it's a new big class of, of consensus issues, that of potential consensus issues that we might get with this. Right? 
* Yeah. Um. Ansgar's got his hand risen on this question, so I'll let him. It seems like he wants to answer some of it. Or do you want to ask a question? 
* Well, no. Yeah. It was. It's only a partial answer, but basically to the question of what is this useful for and why would we want, want this? To me, a value of this that I think is maybe a bit less tangible, but also very important, is that right now, a lot of the times when we want to make changes, we were always very hesitant because it breaks existing code or at least potential edge cases, like anytime we want to do repricing of opcodes, we have to be very careful. And with address space extension, one of the reasons we didn't end up doing is, is that it kind of is really hard to make backwards compatible.
* One of the things that would excite me a lot about UF is just that. Of course it doesn't fix that.
* We have existing contracts that will still have these same problems, but once we have this out there and maturely supported with all the compilers, we can tell people that best practices to start using UF. And then at least that means that 2 or 3 years down the road, we can be a little we can start to be a bit more easy with making some. Breaking a small amount of legacy contracts in a somewhat more aggressive way with re pricing and all these kind of things, because we have this great new, more robust world that we want everyone to be in anyway. So to me, it just makes it a really nice transition to, hey, this is the world.
* If you really want to make sure your contracts are long, long lasting and have completely reliable behavior, please move over there. You know, over the next one, two years something. So to me that's that's very appealing. 

**EF Security**
* Yeah. But this only works if, if we suppose that is the end all be all of always. And I don't see it this way. Like, like there have been changes to EOF even quite recently and so I don't I think like in five years we will say, okay, if version one wasn't, didn't have like these five features that we really want and we're going to do version two now and then we kind of like we're pushing all this, this work onto onto client teams. They have to maintain two different versions of the EVM and maybe in the future even a third version. and also like the argument that layer two specific versions would be nice because the L1 teams have to maintain the or are maintaining the EVM.
* Yeah, sure. Like L2 teams, they don't want to maintain the EVM because it's honestly a pain in the ass. And so now because they don't want to maintain one EVM, they're going to push this all this new EVM work onto the onto the client teams as well. And we have to maintain two. So. I don't I don't see this as, like, just conceptually as a great way. I think two teams should maintain their own software and, and not really depend on one teams kind of providing the software for them and then building like small pieces on top. But that's just a personal opinion. Everything I'm saying is a personal opinion. Right. 

**Danno Ferrin**
* So there's there's a lot of issues there, but the one I want to pick out is the idea that, you know, in five years you're going to keep adding features. We've been adding features to legacy since the beginning. We've been dribbling off codes. We just added up code two weeks ago. But there's two categories of changes that and would both still support. The first set of changes are compatible changes you drop in a new op code. That's easy. and there's incompatible changes like, say, we change what self-destruct. Does those take a lot more changes? So we're trying to do an you're trying to make as many of those incompatible changes at one time.
* So we do it once.
* So the container format ideally doesn't have to change again and can evolve in compatible ways. So if we need to add a new profile type section there is an about profiles. We could add a new header type. And that falls into the the second point on the left as we make invalid byte sequences valid. So if you had that before you would add it, you could now have it by requiring validation and requiring things become valid, we make sure that garbage doesn't accumulate on the chain by submitting random bytes to the chain. We're not blocking out stuff that we couldn't do before.
* There's the only validation that happens in EVM right now is at runtime, and we make sure that your jump destinations are not in the immediate arguments of pushes.
* So we really do some validation, some jump test analysis. But the validations we define are they're linear time. We're charging for them now with with with deploy. And a lot of these decisions that we're making for these compatible changes make it so that all the things that we need to add to don't require us to change the operating structure and don't require us to change new byte code so it allows it to live there just the same. 
* One example would be max. If we want to add modular exponentiation, we can add operations that have immediate arguments on it. Now, which we cannot do in legacy. If we want to add a new argument that has legacy operations, we break stuff. a couple of my slides here show the story of how, if we wanted to add, our jump with EVM , we would take stuff that was invalid and all of a sudden move it into immediate data. So we change a jump test and we move it into immediate data and we break things. If we add an immediate. So stuff like that is what we're trying to fix so that we can grow the in the future.
* I don't think that, you know, we're not going to be able to ossify the EVM until we ossify the consensus layer so that, you know, the EVM is going to be frozen forever, is only going to work once we freeze forever.
* The consensus layer, once things stop changing, then things can stop changing. But this structure allows us to to grow rationally and to be able to do more things and grow in better ways to deal with these new features. So. 

**Tim Beiko**
* Thanks. Andrews had his hand up for a while. 

**Andrew**
* Yeah, to my mind, a big benefit of EAF is that it's more constrained. So you have separation of code and data and you disallow dynamic jumps. So because it's more constrained, it should improve security of smart contracts and facilitate like verifications, verification of smart contracts, either manual or automatic or semi-automatic. So I think it's a step forward. 

**EF Security**
* So I kind of disagree with this, that we cannot freeze the EVM without freezing the consensus layer. I think those are kind of different things, and at least I like this assumption that once you deploy a contract, it's mostly immutable. but. I don't know, like it would not be. Like we are breaking this assumption with self-destruct. But I see the need for it, and. Yeah, I don't know. And for EVM max. I think we can build even without Immediates. It would just not be. super gas efficient. And that's where we're. 

**Danno Feerin**
* Going to start losing compiler people. If we say you can still do it, just not gas efficient, they're going to say, well, I should just build it in sway or I should use stylus. So that's that's the risk that we're looking at. 

**EF Security**
* I see. I understand the risk. I have to think about it. 

**Danno Feerin**
* Yeah. It's not a security risk. It's more of an existential game. 

**Guillaume**
* Yeah, that was actually a question for Maurice. I don't see exactly I don't. Could you detail the argument where it would be harder to maintain, you know, different versions of EOF as opposed to a different fork? To me, it looks exactly the same. 

**EF Security**
* I don't think so. Like if we change the behavior of an opcode in in different versions of the EVM. Yeah. in different versions of, for example, if we have now one opcode that does gas introspection and one opcode that does not. in our code, that's twice the amount of opcodes. And testing. Kind of Explodes.
* Because we have to test all possible. All possible versions of it. And if we go like if, for example, like now we have one call and making something up. No. But if we have one call up code that does gas introspection, one call up code that does not gas introspection. And now we have a new version of the we have, sorry, we have a hard fork that changes. The order of arguments for the call opcode. Then we will have to maintain four versions of the of the call opcode. That's kind of my. 

**Guillaume**
* Wouldn't you just change the format and then maintain one per performance version? 

**Barnabas Busa**
* Sorry. okay. 

**Guillaume**
* Maybe I misunderstood, but, I mean, like, I don't see where the four comes from, because for me, if you change the code up code, you would just. I mean, we can also take this conversation offline. I'm not trying to to hog the whole thing the whole time, but yeah, basically, I don't understand the for the for the four version, I only see two because one of them would be associated to one format version, and the new version of the op code would be associated to the new to the new format version. 

**EF Security**
* Yeah. But then we have. Then we have a hard fork that changes, that changes the ordering of the, of the arguments, for example. And then we would have to, either, like we would have to apply it to both versions. And with this we would have to maintain four versions, two old one. 

**Guillaume**
* Okay, I get it. Thanks. 

**Danno Ferrin**
* I think a more concrete version of that would be address space expansion. if you have a balance operation, one that takes the 20 byte version, one that takes the 32 byte version. you know, that's something that if we're going to do, address space expansion is going to be a real issue. And that, I think, is the best example of how one might use choose or things you can't do in EVM because we can't just, you know, take off the top 12 bytes of, of all address operations because there are decodings that depend on the top bytes being ignored.
* And there are some called datas that you can put in that will break if they are not trimmed with some of the PAC call data. So there are contracts that would break with address space expansion. And that's why, you know, even though it's a recent thing that's brought up, is what if we wanted to address space expansion for, you know, for rent or whatever other use for it? if we don't bring it in in a situation like this now, we can't just break old contracts. And with container format, you know, we could flag to say, hey, this one trims, this one doesn't.
* That's probably not the best solution. I think the best solution is just from day one to not trim address arguments in in operand stacks and have it be different in an EVM, but these are some of the things going in.  Given all this complexity, is 3 to 6 month timeline posed realistic? I believe it is, because we're shutting down the final features. and we're there's no new features added. We're adding, you know, maybe a few more opcodes to address these features. 
* And we're going to spend a lot of the time testing and implementing. I have been very impressed with the differential fuzzing work that's been going on, and it's found a lot of strange corner cases and very creative ways that I don't think we could write tests to cover. So in addition to writing the deliberate tests, I think the differential fuzzing is going to be a game changer in our testing. Think differential fuzzing and compiling old contracts are going to be, which is kind of a different way of doing differential testing is going to be our equivalent of shadow forks for. 

**Tim Beiko**
* I'm sorry you've had your hand up for a while. 

**Angsar**
* Yeah. I just wanted to say, I mean, it sounds like it's probably going to be a multi call conversation around whether is a good, good idea or not. I do think basically one aspect of this that came was briefly mentioned, but I think will be important is kind of the the relation going forward between layer one and layer twos. And with regards EVM governance, I think so far, basically, for better or worse, it always felt felt that we evolve the EVM and then later was in a way almost blindly follow.
*  And I think in the past there have been some ideas around at some point, maybe later, just forking off having their own layer two EVM standard layer twos don't seem to love that idea so far at least. And just one thing I wanted to point out in that context is that, Kyle and I, we recently decided to initiate some sort of layer two EVM governance call for like more layer two specific topics. that that's going to kick start like, start of next week and then have an in-person event during Dev Connect.
*  I think basically there will be a lot of similar questions coming up from the other side, and might be one example of, you know, to what extent layers want to just follow the layer one EVM. And so I just want to already flag obviously it's too soon now to talk about that, because obviously that hasn't happened yet. But I think this will be a more, more important conversation around like basically how do we govern the EVM? Will we ever have the same EVM between layer one and layer twos? And how do we basically merge the interests of these different groups? So I just wanted to raise awareness for. 

**Tim Beiko**
* Thanks. Yeah, and maybe we can post the link in the chat as well, but it's on the Ethereum slash PM repo. so the call is next. The first call is next Wednesday, and I believe. Yeah. Guillaume. You have. You were next. 

**Guillaume**
* Yeah. I just wanted to give some pushback on the claim that it's going to take that we could have a four, three months after Cancun. It's true that that the differential fuzzing tools are really useful. But if they had, they've been around for a long time. If they had sped up forks, you know, just just by the  magic of their might, we would know that already. And I think, yeah, we're looking at a much longer time because I mean, this is, you know, then Dencun was also supposed to be a fast fork. I don't think if we look at the two options vertical and both of them are we're looking at at one year of work in any case.
* And the problem with vertical is that the clock is ticking. Whereas all those advantages that have been touted by brought by they they're very nice to have. I mean, I want to make that clear. I am a supporter of EOF. I just don't think it should be coming before vertical because vertical we have to go through the transition and the more we wait, the worse it's going to get. And there's really bandwidth like core development bandwidth for one team. I don't see the urgency for pushing right now, especially if if it is that complex. In my opinion, there should be since this is a format, you can have several format version you could deliver.
* All those features little by little. And if was a very simple container, like if that was the only thing the fork was about, I'd have no problem delivering. Having it delivered before, before vertical. But because of that complexity, I think it's very important to focus on vertical right now and deliver a deliver afterwards, or simplify greatly the scope of of that first fork. And then, yeah, I don't have any argument against it. 

**Tim Beiko**
* I guess. Yeah. Just to chime in on the timelines. Like, I think historically, like three months is. Like extremely unrealistic. Like what we've done in like a three month range is like a difficulty bomb push back. I think as soon as you start to have actual features, regardless of what they are like, somewhere between 6 and 9 months seems to be our pace. it's also worth noting, like there's a bunch of other stuff people are going to want to do in the next fork. And so, you know, it's it's probably unrealistic to say we're just going to do EOF and nothing else and therefore forks going to take that amount of time. So same thing with Verkal.
* And so yeah, I think it's probably a mistake to it's probably a mistake to like analyze it at any level beyond like just relative complexity. Like is Verkal going to be more work than or not? and then, you know, as you said, is there like more urgency to do Verkal, because. And yeah, historically as well. Like over the past couple of years, it's been kind of interesting where we've tended to do like one big fork and one small fork. So like, you know, we had 1559 and then a couple difficulty bomb forks and then the merge and then withdrawals was much smaller. And I would argue then is actually a pretty big fork. I don't think it's like a quick fork.
* The amount of work on the blobs is quite huge. so like, yeah, coming out of this big fork, I think it's worthwhile to consider, like, do we want to move on to something, you know, really big right now?
* And if there's a time pressure with regards to Verkal, because of the state growth, you know, does that like, raise the urgency or do we want to do something that's potentially smaller, and then do Verkal after that? 
* And I think. Client teams should start thinking about that. I understand that, like, obviously a lot of the bandwidth right now is spent on on Cancun. And so it's worth it's worth keeping the focus on Cancun and like shipping that before we make a decision about what the next big thing is, at least having it, you know, starting to roll out on test nets and whatnot. but I think it seems, at least on the execution side EOF that and Verkal are the two biggest potential candidates so far.
* So yeah, I think if EL teams can start just looking into those more closely and understanding the tradeoffs and both in terms of like the value they bring and then the timelines, hopefully in like the next month or two, we can start having like a more focused conversation on like, what do we actually want to prioritize? and by then, yeah, we should be rolling out Cancun on to test nets.
* So the, the amount of work that's actually focused on Cancun should be, should be going down. And, and we'll obviously have dev connect as well, where we can spend plenty of time going over both all the Verkal and EOF updates. Yeah. EF security measures. Is that still you? 

**EF Security**
* Yes, that's that's still me. I think Ansgar said something interesting. He said maybe Devconnect could be a good place to have that. Do we want to go with at all discussion. And I think just the fact that this is still a discussion means that, like, we cannot make a we cannot even talk about timelines like we did not there's no consensus that this is happening at all. So we shouldn't talk about timelines. We should talk about whether it makes sense to have this, whether it's a it's a good technical change. And if we all say this is something that we that we want. And if this is the consensus, I'm fine with it.
* But then we should talk about is this a priority over Verkal or not? And then we can talk about timelines, but talking about it right now where we don't even we have no clear this is good or this is something that we want. it makes no sense to me. It. 
* I seem to be in the minority in this course because I'm the only one arguing against it. But I know that a few people are also not very happy with it. So I would like to I it's  I know the, the Epsilon team and and Danno have spent a lot of time working on this but. I think it and  it's quite harsh to say that after all this time we might not be shipping it, but I think it's even worse to say. let's see. And,  then in like, we push it another two years and then we say, oh, we are not going to ship it after all.
* And so I think it we should make a decision at Devconnect, that whether this is something that we want and if it's something that we want, then we are going to do it except for like technical challenges.
* And if we are saying this is something that we don't think is going to happen, I think it's just fair for for the team that has been working on it for all this time to have like a clear decision from everyone. And, yeah, I already talked to the Epsilon team about this, and I think it it would be really nice to, to all come together at dvconnect and, and discuss in person and make a clear decision about it. 

**Tim Beiko**
* Yeah. Think. It's like, don't think anyone disagrees that figuring out if we want it is is sort of a first thing before, when, when we'd want it and how long it could take. I also think, yeah, it makes sense to discuss both EOF and Verkal quite extensively at Dev Connect. I'm not sure that we necessarily want to take.
* Yeah. I'm not sure if, like a month from now, we'll be in a spot where we're ready to, like, take a final decision. but I know my hope is we can if teams can get up to speed on both Verkal and dev connect at both Verkal and in the next month or so, that we can spend the time on dev connect, like going deep into both of those as well as a bunch of other proposals. yeah.
* After that, we should be in in a pretty strong spot to take a decision. both for the next work, what we want to prioritize.
* But also, yeah, if for whatever reason, we don't think EOF is viable. yeah, that makes make that called at that point as well.
* Yeah, I feel like we've been going on EOF for quite a while at this point. Obviously use the EVM channel we can use to discuss it, but. Yeah. Does anyone have any? New topics or questions, things that we sort of haven't covered. obviously there's a bunch of objections around, you know, the backwards compatibility and figuring out, you know, how this works with Altus. is there any other potential concern or question that people feel we haven't touched on so far? Okay. If not, then yeah. So there is the EVM channel on the discord. We're going to have the L2 call next Wednesday. 
* I forget the exact time, but the agenda is in the repo. anything else anyone wanted to cover before we wrap up? 

**Georgios**
* I have a question on this general set of changes that we're discussing around the overall, what is the right way to think about L1 and L2 divergence? For example, you implement Verkal. Maybe it's not implemented on L2. Push zero is not implemented on L2. EOF plausibly take some time to make its way on L2. 

**Tim Beiko**
* Yeah, I think that's exactly what we want to discuss on the L2 call next Wednesday. Got it. And I think and part of the reason why it's probably worth discussing there is to have L2 people chime in, right. Like. Yeah. Because yeah I agree. Like I think a lot of people realize that we don't have, a super clear vision there. So like at least getting that conversation started with,
*  Yeah, it's a good start. Yeah. And then, yeah, Ansgar is a comment like the first step of this is also getting bringing the two together to chat about this stuff where there isn't as clear of a forum as for L1 devs and L2 are obviously way more divergent in how they approach things. So. Yeah. Hopefully . 

**Ansgar**
* Just want to make sure that people like if people want to show up next week, that's fine. But they shouldn't expect like it might just be a one hour call where five 55 minute is about just like, you know what, weekdays do we want to have this call and who should show up and these kinds of things. And then maybe we have five minutes of briefly touching upon already, like, how do we see our relationship with layer one, the layer two relationship, layer one or on EVM. But it won't be a big topic yet for next call because it's just too early in the process. Yeah. 

**Tim Beiko**
* And then yeah, we're also planning, though, a full day at Dev Connect as part of the L2 days focused on this topic as well. So expect in the next few weeks there'll be more information coming out on that too. Anything else before we wrap up? 

**Tim Beiko**
* Oh, yes. Please. 

**EF Security**
* Can you make sure that we all get that we all get invites to those, to those events so that we can participate? 

**Tim Beiko**
* Yes. If so, I mean, all the L1 teams should have events for the L1 workshop. And then if anyone wants to join the L2 day. so you can apply publicly tickets to L2 event, but if you have an issue getting in or getting a ticket, then you work on L1. yeah. Guess. Ping me and I'll try to, to help get you a ticket. Thanks. Yeah, or just tag beats on Twitter and ask them for one. Um. Anything else. 

**EF Security**
* Okay, well. 

**Tim Beiko**
* Thanks everyone and talk to you all Monday on the testing call. 


-------------------------------------
### Attendees
* Tim Beiko
* Danny Ryan
* Pooja Ranjan
* Mikhail Kalinin
* Marius
* Wesley
* Barnabas
* Saulius
* Danno
* Lightclient
* Pari
* Ethan
* Mario
* Tomasz
* Oleg 
* Kasey
* Marek
* Crypdough
* Fabio Di
* Terence
* Andrew
* Roman
* Marcin 
* Pop
* Guilaume
* Protolambda
* Carlbeek
* Mike
* Gajinder
* Stefan
* Hsiao-Wei
* Josh
* Phil Ngo
* Alexey
* Holger Drewes
* Dankrad
* Guillaume
* Proto
* Holder Drewes
* Stokes
* Peter Szilagyi
* Sean
* Micah Zoltu
* Jiri Peinlich
* Marius Van Der Wijden
* Potuz
* Evan Van Ness
* Moody
* Tynes
* Alex Beregszaszi
* Marek Moraczyński
* Justin Florentine
* Ben Edgington
* Lion Dapplion
* Mrabino1
* Barnabas Busa
* Łukasz Rozmej
* Péter Szilágyi
* Danno Ferrin
* Andrew Ashikhmin
* Hdrewes
* Crypdough.eth
* Ameziane Hamlat
* Liam Horne
* Georgios Konstantopoulos
* Mehdi Aouadi
* Bob Summerwill
* Jesse Pollak
* Stefan Bratanov
* Sara Reynolds
* Caspar Schwarz-Schilling
* Ahmad Bitar
* Marcin Sobczak
* Kasey Kirkham
* Sean Anderson
* Saulius Grigaitis
* Ruben
* George Kadianakis
* Dankrad Feist
* Andrei Maiboroda
* Gcolvin
* Ansgar Dietrichs
* Jared Wasinger
* Diego López León
* Daniel Celeda
* Trent
* Mario Vega
* Kamil Chodoła
* Ziogaschr
* Kevaundray
* Antonio Sanso
* Oleg Jakushkin
* Leo
* Nishant Das

-------------------------------------
Next meeting on Oct 26, 2023, 14:00-15:30 UTC
