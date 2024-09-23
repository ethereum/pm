# Execution Layer Meeting #196
### Meeting Date/Time: Sep 12, 2024, 14:00-15:30 UTC
### Meeting Duration: 1.5 hour 
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1143)
### [Video of the meeting](https://youtu.be/A_DuQRICW70)
### Moderator: Tim
### Notes: Alen (Santhosh)

| Decision Item | Description                                                              | 
| ------------- | ------------------------------------------------------------------------ | 
| 196.1 | **Pectra Devnet 3**  EF developer operations engineer Parithosh Jayanthi gave an update on the launch of Pectra Devnet 3. The devnet was launched on Wednesday, September 11. It includes fixes to validator consolidations in EIP 7251 and the updated specifications for EIP 7702. Based on testing so far on Devnet 3, both EIP 7251 and EIP 7702 appear to be working as expected. Jayanthi noted that there were issues discovered in the Nethermind and EthereumJS clients, which these respective client teams are working to resolve. Jayanthi added that since EIP 7702 is live on Devnet 3, it would be ideal to have wallet developers test out the implementation and provide their feedback on its use. All the information about Pectra Devnet 3, including the faucet to request testnet ETH
| 196.2 | **Pectra Specification Updates**  Geth developer Felix Lange has proposed changes to the encoding of EL-triggered requests in Pectra. As background, Pectra will enable smart contracts on the EL to initiate validator withdrawals and consolidations on the CL. During the last ACD call, Lange shared a proposal to reduce the amount of work needed by EL clients to parse through these requests. Since last week’s call, Lange has formalized his proposal and the work that will be needed from EL client teams to update the encoding of the following four EIPs:
| 196.3 | **Pectra Specification Updates**  Developers were largely in agreement with Lange’s proposal. However, a Nimbus developer with the screen name “Dustin” argued that the proposal was “pointlessly flexible” and not forward compatible with future changes to the serialization format of the EL. He also stressed that additional specifications are needed that clearly formalize the ordering of requests by the EL clients and the behavior of CL clients if an invalid request is submitted by the EL to the CL. Lange agreed to add more text to the Engine API to specify the ordering of requests. He also agreed with Dustin that deeper thought should be given to the behavior of CL clients in the event an invalid request from the EL client is detected by the CL client.
| 196.4 | **Pectra Specification Updates**  Ethereum Foundation Researcher Peter Miller pointed out that according to the logical behavior of CL clients under current specifications, CL clients should reject blocks from the EL that are not ordered in the correct way. Further, if there is an invalid request in the list that is shared by the EL to the CL, the CL should simply process all valid requests in the list and ignore the ones that are invalid. Dustin agreed with Miller and recommended that developers specify this behavior in appropriate documentation. Beiko said that developers should aim to resolve issues with Lange’s proposal and finalize it by next ACD call.
| 196.5 | **Pectra Specification Updates**  Erigon developer Andrew Ashikhmin proposed an update to EIP 7702, set EOA account code. He noted that the validity checks specified in the EIP are not consistent with the validity checks specified in older EIPs. Geth developer Matt Garnett, also known as “Lightclient”, said that he has an alternative proposal to address the consistency issue and simplify the validity checks on EIP 7702. Developers were largely in favor of finalizing Lightclient’s proposal and adding it into Pectra Devnet 4.
| 196.6 | **Pectra EIP Additions**  Developers then moved on to the topic of adding new EIPs to the Pectra upgrade. When kicking off the discussion, Beiko warned, “We already have a ton of EIPs in Pectra. It is by far already the biggest fork by number of EIPs [included].” Based on sentiments shared by developers before the call, Beiko said it was clear that EIP 7742, the uncoupling of blob count between the EL and CL, was the least contentious on the list of EIPs still considered for inclusion in the upgrade.
| 196.7 | **Pectra EIP Additions**  EF Researcher Alex Stokes raised again the idea to split Pectra into two smaller hard forks. “I think everyone agrees that it's a really big fork. So, a natural thing to do is just to break it into two. Generally, smaller forks are less risky. In particular, with Pectra right now, there are a bunch of cross layer EIPs, which really raises the testing, security, and review load,” said Stokes. Jayanthi, who had also raised this idea on prior calls, said that he is still in favor of this idea. “I think the main reasoning is that currently, we have a lot of EIPs, and we're tending to touch many, many layers of the stack, and the more we add slash, even with the current load, it's hard for any one person to have a global view of all the changes,” said Jayanthi.
| 196.8 | **Pectra EIP Additions**  About the way current Pectra EIPs could be split across two forks, Stokes recommended shipping the first part of Pectra with all the EIPs currently live on devnets and then shipping the second part of Pectra with PeerDAS, EOF, and a few other additional EIPs. Developers felt confident that in doing so they would be able to ship the first part of Pectra by February next year. “I think a split where we still only ship the first half in say June would be a failure,” said EF Researcher Ansgar Dietrichs in the Zoom chat.
| 196.9 | **Pectra EIP Additions**  Beiko was in favor of the idea to split the fork but cautioned against removing any EIPs from devnets, as this could create more work for client teams and extend, rather than shorten, the timeline for preparing these code changes for mainnet activation. Independent Ethereum protocol developer Danno Ferrin recommended polishing the EIPs live on Devnet 3 for mainnet activation as soon as possible and then beginning work in parallel to rebase PeerDAS and EOF on Pectra EIPs starting from Devnet 4 or 5. In effect, Devnet 4 or 5 would become Devnet 0 for the upgrade after Pectra, which developers were not confident about how to name.
| 196.10 | **Pectra EIP Additions**  On a prior call, developers had agreed to name the upgrade after Pectra Fusaka but they had also agreed to reserve this upgrade for the Verkle transition. About this, Ferrin recommended that developers refrain from reserving upgrades in advance before they are confident about code change readiness for mainnet activation. This drew ire from Geth developer Guillaume Ballet who has been leading efforts on the Verkle transition and who maintained that the Verkle transition was ready “a long time ago.” To diffuse tensions, Beiko said that the point of splitting Pectra in two was ultimately to try and ship Pectra code changes on a faster timeline, which is beneficial for clearing the way for the Verkle transition thereafter.
| 196.10 | **Pectra EIP Additions**  However, there is the risk that the second part of the Pectra upgrade could become larger with the addition of more EIPs and thereby take more time to ship than if the current list of Pectra EIPs were all shipped in tandem. Nethermind developer Ben Adams questioned how the testing process for Pectra would proceed if the upgrade was split in two. Given that this is a decision that would drastically change the scope of the next immediate upgrade on Ethereum, Beiko recommended that developers take a week to think over the idea. He asked that developers be ready to make a final decision about this on next Thursday’s All Core Developers Consensus call.
| 196.11 | **Network Configuration Structure Alignment**  EF developer operations engineer “pk910” shared updates on his work to clean up the Ethereum public testnet GitHub repositories and align their structures for easier usability. He asked client teams to review their node configurations for Ethereum mainnet and testnets and add any missing information to the respective repos.


# Intro
**Tim**
* And we're live. I welcome everyone to a ACDE number 196. today I will talk about Pectra, as we have been lately. And then that three got stood up this week. So we can chat about that and then we can continue the conversation. We started on the CL call last week around all of the encoding changes for the different EIPs in Pectra. there were two other, Petra EIP issues that people put on the agenda. So one around 7702, signature checks and then one around the pricing of the some of the BLS precompiles and then, probably the biggest thing, are trying to wrap up the conversation around potential additions to spectra.
* So we discussed those two weeks ago, and then some teams have already shared their views. And then lastly, there's just a small heads up around the way the network configs are being documented in the different repos for mainnet and testnet. So we can just quickly cover that. but to kick us off, Perry, do you want to talk through the launch of Devnet three? 

**Parithosh**
* Yes. So we finally have Devnet three up and running. The main change from Devnet two is the fix to the consolidations issue, as well as adding 7702. since yesterday, we've also tested that consolidations work as expected now. And they do. And we have had some 7702 calls. And they also work as expected. We're currently seeing some issues with Nethermind as well as Ethereum JS and I think both the client teams are aware and looking into it. in case someone from the client team wants to mention where they are, maybe now's the time. 

**Marek**
* Think our issue was fixed, so I see that in fork monitor. Our nodes follow the chain.

**Parithosh**
* I haven't checked up after the update, so that's good to know. and besides that, there was one minor thing I wanted to bring up. our EL teams, under the assumption that we're running the spec version 1.5 or 1.4 purely for updating the spec document, it seems like there isn't any material difference. But yeah, just so that we have it on record properly. 

**Tim**
* You mean CL teams, right? 

**Parithosh**
* Yeah, teams. There's also the execution spec task. 

**Tim**
* Okay. Oh, sorry. Execution test. Okay. Yeah. 

**Sudeep**
* Erigon was under the assumption of running 1.5

**Parithosh**
* Okay. I think according to Mario's message, it was also that they're mostly the same, except for a few extra tests and disallowing. Yeah. Okay. so I'll just update the spec version so that it's also clear for, people looking at it. I think that's it from the devnet side of things for Pectra. 

**Tim**
* Thank you. Anyone else have comments? Thoughts? Questions about devnets? 

**Parithosh**
* I guess if you have a wallet developer you like, please ask them to test 7702 now. Okay. The fork is running so you can get funds and you can deploy contracts and you can, I guess, break it. 

**Tim**
* I said, yeah, that's great. So we'll give a shout out to that also outside of the call. But yeah, you can start testing and. Yeah. Perry, do you mind sharing the link for just the Devnet config page in the chat here? I believe that also has a link to the RPC on it, as well as all the other, things like the spec. Or adding it to MetaMask. And, Anything else on Devnet three? Okay. if not, then, moving on. Next. we had all these proposals to change the encoding, of the data that's been passed from the ACL to the ACL.
* We discussed this on the, we discussed it on the CL call last week, And then Felix said he would open up some PRs for them, which he did. And then effectively, I believe all of the PRs do sort of the same change, just in the context of the different types. I know there's been a bunch of conversation about this on the discord in the past day or so. I don't know if Felix is on. Yeah. Oh, yeah. Felix, maybe you want to start by giving you a bit of context on the PRs, and then we can get into the discussion that we were having on the All core dev channel. Yeah. 

**Felix**
* So, I mean, there are two sides to this. And the discussion we've been having is mostly on the CL side. So this being ACDE, I think, the changes that I'm proposing are like, I think very uncontroversial for the EL. So basically, this is going back to some stuff that we've been proposing kind of before. So in the. It all kind of started when we when we were seriously reviewing the implementation of the requests mechanism in Geth, and we kind of noticed that there are two big problems with there. So one problem is we used to be able to turn a block into executable data and back with basically no knowledge of the fork configuration, and this is something we would like to preserve.
* So at the moment when you create a block, you can sort of pack things into it and without having a lot of context. So it's kind of a freestanding object for us. And this would change a little bit with the introduction of the requests, if they were to be done as separate lists. So we both, like Matt, originally just proposed turning a request into a single list. And on the CL side, this was met with some criticism.
* And I mean, when I started reviewing his implementation of it, I also kind of felt it just like the EL just has way too much knowledge of these requests because in the end, the whole the point of the requests construction is that it's some data which is technically, I mean, it is generated by the EL, but the EL shouldn't really know too much about, like what's inside of these requests because they are supposed to just supposed to be for the CL to process, and they are meaningless for the ELs. 
* So in the changes that I'm proposing now, we're basically removing responsibility for the EL to ever decode these requests. So what we want to achieve is that the EL should call the system contracts, and then whatever is returned by the contract, the only thing it has to do there is basically just it has to turn the buffer returned by the contract. It has to turn that into a list. And for that it has to know the size of each output request. So that's like one data item we still have to track. But other than that we don't really have a knowledge of the structure of the returned requests. Do we turn them into a list of just byte arrays.
* And then basically we are supposed to return them to the class for processing and they will be put into the EL block as well. I can quickly finish my description. Or do you have a very urgent question? Yeah. 

**Tim**
* You can. No, urgent. I'm just in line.

**Felix**
* So let me just finish the tangent. So basically the whole point of the of the PRs to change the EIPs, is to just make it so that the output format, is exactly equivalent to what is returned by the contracts. So we don't have to parse them at all. We basically just pass them through. And then there is one PR to actually update the request type itself because it turns out that it was defined to use this tree hashing function that we also use for receipts.
* But actually we realized that it's totally unnecessary because nobody is supposed to make a proof against this root hash. the request root hash in the EL block is meaningless because the requests that are in there have not been validated for correctness by the CL. So, for example, let me remind you, for example, for the withdrawal request, any withdrawal request can be submitted on chain even for a validator that doesn't exist or has already withdrawn or whatever. So just this request alone is meaningless, and just creating a proof of that would actually be kind of dangerous, because then you'd be proving that, like this, this request exists in the EL chain, but you don't know if at that block the request is actually valid, or the validator can cover it or whatever.
* The thing that people should make proofs about is when it's processed and validated in the CL, and for this reason, the validated request they will be put into the CL block and as an SSZ list. So there can be an SSZ markup proof, about these objects.
* And so for this reason, I am proposing that we change the hash that we the request hash that we put into the EL block header, we change that into a flat. 
* And this is similar to how we treated the like the Omers they're called basically it's just a hash of the list instead of having this like Merkle tree construction there. Anyway, so this is my overview of EIPs. And now I'm ready to answer questions. 

**Tim**
* Thanks, Felix. yeah. 

**Potuz**
* So I had a quick question. so you're. You're calling the system contracts, and I assume that you're calling them in the order that you're getting these requests in the block. You're calling the system contract, getting whatever is returned. You treat it as a flat slice of bytes, and then you want to store this somewhere so that you send it to the CL. What I don't understand is if this system contracts are different system contracts and you know which which ones they are, because we are prefixing the return with whatever, a number that just indicates which system contract was. Why would it be difficult for the L to just collect many different lists and just put them in the order that you're getting?
* So instead of using the index as a prefix, use the index as the the index in the outer list to put the and then complete the the inner list with the flat array. 

**Felix**
* Yeah. I mean this is something that if you guys absolutely wanted, we can have it as a separate list. But the way I see it is that, we can make this list of list construction, but I would. So from our point of view, yes, there is a point in the code where we will be calling the individual system contracts, and we know there we have the fork configuration so we know which ones we should call. But we also have obviously we have the knowledge of like which contract is it and so on. So there is some some knowledge there. But what we want to avoid is like having any more knowledge of the system outside of that. So there's a lot of other places in the client code bases where we have to deal with these requests, and we just want in these places to have as little complexity as possible. it has not.
* It's yes, there will be like when we are actually making these system calls, we have all the knowledge that's required, but it's just more of like a convenience for us. That's why we proposed this like flat list. If you must have it as three separate lists, it can be arranged, but we would be happier to just have it as a single list to be honest. 

**Potuz**
* This quick comment, is that so? Someone will do this. Like either you do it or we will do it, but we will definitely grab this list which is prefixed, and then make this list of lists anyways. So and the one advantage that I see of having already the list of lists on this API is that if we ever move to a SSZ, that's exactly what we will use in the as a SSZ object. That will be a list of lists. So that's that's perhaps why it's more future proof to get it on the API as list of list. But as I said before, Prism will not disagree with implementing this. If this really makes the EL life easier. 

**Felix**
* It kind of does make it a lot easier. Because we have this, we basically don't have to know anything about the request further down the pipeline. We only have to know about the request in this one place where we actually perform them. And yeah, from that point onwards, we just don't think about it. And this also goes, for example, for decoding blogs and things like that. Like whenever we we have to deal with a blog, we can. Assume that yes, there's this list of of opaque objects there. sorry, Tim, what was the question? 

**Tim**
* Oh, sorry, I was, Reith said in the comment. They already do this, but I'm wondering if by this they mean compiling the three different lists. Yeah. 

**Oliver**
* Yeah. We. So because we need to, deserialize the rope to get a JSON representation of each of the requests. These are different types. So we end up doing, three different lists and then doing a wrapper type and then collating it into one list. 

**Felix**
* Yeah. Yeah. This is exactly what I meant. So all of this complexity is totally unnecessary for EL. And this is why I'm proposing to remove. And yes, on the CL side it will mean that you have to pick apart this list and figure out by the prefix. But I mean, to be honest, it is. This information is like kind of pre dated. So there won't like in the normal case there won't be any like wrong. I mean the requests won't really come out of order. So for example because they are just generated in the right order by the EL, I mean the we can argue if it if it somehow improves. So if there is a specific proposal that would make it way better for the CLs, then I'm happy to integrate it as well. But as it stands, the way we see it, it's the best for us and that's why I propose it. 
* So yeah, like we need to I don't really know how we should put this to a vote. I do think that we should kind of decide this today because, yeah, I mean, it's we're sort of like in the kind of late in the, in the whole, like, fork changing game, even though the fork is probably not going to happen this year. But I still think that, like, if we're going to have it the next Devnet or something, we should probably have it in by then. 
* So yeah. And I have, created a separate PR to change the, withdrawal system contract to return, the output in a way that's more friendly to the to the CL specifically, there was this one field in there that is big endian, and I've changed it to little because, yeah, it makes it easier for the for the CLs to decode it. 
* But and this should probably then also be integrated into the EIPs and stuff. So we have to I would have to update my PR to include the new system contract code into the EIP. 

**Tim**
* There's a comment about, by Dustin about the ordering as well, and that we if we do move forward with this, we want it, we want to have like effectively the ordering guaranteed. and adding this in the, basically the the engine API spec. Yeah. Does anyone have any issues or concerns with that? 

**Felix**
* I mean, it's simple for us because we can literally just I mean, I'm totally happy to just put it into the spec. Like right now, I the sentence I would add is something like the requests have to be ordered by type and within the type, they have to be ordered in the same way that they were returned by the contract. But honestly, this is just what's going to happen automatically because the the during the processing we create them in this order. So the ordering is I feel fully defined by the semantics of creating the requests. 

**Tim**
* Right. Okay. So so if we make this explicit in the spec yeah. As I understand it's like yeah clients already sort of do this, but then we should make it explicit to make sure that, yeah, that all the clients follow this. so, yeah, I think if we can. Yeah, if we can add a PR to the engine API that just adds this. 

**Felix**
* Yeah. I mean, I'm fine with adding that into into the existing PR. I mean, this is definitely the I am absolutely not against adding as much text as you guys want about this in the specification. Okay? 

**Tim**
* Okay. Perfect. So let's, I guess this like, concern aside, which seems like it can be resolved. Does anyone have like, a strong objection to moving forward with this? And I know like, yeah, the the issue is more of like a CL one around the decoding. And I don't think Tercek is on the call and he's the person who left the big comment. yeah. 

**Dustin**
* Oh, hey. Hi. Yes. Yeah. 

**Tim**
* Okay. Yes, yes. Sorry I didn't. Yeah, I had a brain freeze between you. The GitHub handle and, zoom name. so. Okay, so aside from the specification being more formalized, are you okay if we move forward with the EL not compiling the individual lists by default? 

**Dustin**
* Well, okay, it would be. Of an acceptable compromise, I guess. but that is I really I mean, I see this all this  really dismissive stuff about, oh, the The Executioner API just provides what's in the, what's in the what the EL is doing. We can I think I need to repeat this. We absolutely must not and cannot rely on Geth. Does this right Or does this or like this is this is not this is an absolute non-starter. I really need to emphasize this. 

**Lightclient**
* I this is not how it's specified. It says very specifically in each EIP how the request should be ordered within the list of requests. 

**Dustin**
* It doesn't address the. I assume you read my GitHub comments that it does not address the interleaving case. It doesn't I specifically it does. 

**Lightclient**
* It does. It does explicitly say the interleaving case. It's exactly like Felix just said. You order by the type. And then intra type is defined by the EIP 6110, 7002 max EB. 

**Dustin**
* Within that's within the EL block. That's. 

**Lightclient**
* And the engine API is defined to send the data from the EL block over to the CL in the same way that's ordered in the EL block. 

**Dustin**
* Not precisely. 

**Felix**
* Well, I mean, we can add this, like, look, Dustin, it's fine for me to add the sentence. The intent of the change is to relate the request exactly as it is in the EL block, because this is what creates a simplification for us. Like this is why I'm proposing this, because then we will be able to just put into the engine API what we have in our block object, and we don't have to think about it like anymore. If I understand your concern that like these are different specifications and they each need to be complete, and I will add the sentence. So given that this sentence will be added, do you have any other comments about this? 

**Dustin**
* I think I mean, some I've said before and that Potuz has, I mean I have other concerns, but and I do I do want to echo what POTUS was saying, for example, about the, essentially, this is not SSZ friendly. I know you've already or. Well, that it, it has been responded to in other ways in other ACD calls. and but it would borderline work. Sure. I mean, it's not it's not difficult to parse exactly if the other thing that needs to be defined here, and this is not just an ordering issue, I'll say is and
* I actually did not see this defined in the EL semantics or the, the engine. The CL semantics either is the invalid type thing. So what now what happens for example, if you get a type this is both meant as a general question, but also I mean operationally if you want to answer, I guess, but that right now we have three request types currently.
* And what if somebody that what if this click something where the request type number three like a fourth request type coming out of  EL. What what is it. I mean, is it defined what the CL is supposed to do because this this becomes as I mentioned there, this is a consensus issue. Now one can dismiss this as a oh that's buggy. EL I mean, assuming it's premature, we don't have one yet, but that's another example of, on the execution API. This this is maybe not a concern for the EL. I understand for the El. as you have said, this is they're supposed to be black boxes. They're supposed to be opaque, and the EL doesn't actually care. 
* It's just conveying some bytes. but obviously the CL does care about the semantics of this. and the CL does define the consensus. And so there are questions that come up that on top of this as well, that I think should be dissolved and should be resolved hopefully sooner than later. For honestly, broadly the same reasons as I think you have been pushing to get this in soon, this sooner in sooner than later, which is to say Consensus issues of this sort are things we want to discover early in testing. not not wait. 

**Felix**
* Yeah. So I think what we can add a bit more text on the pull request onto engine API as well. So I see it is that obviously the correct answer is for the CL to reject the block. If A contains request that it cannot sort into any of the available request lists into the CL blocks. So the algorithm that the CL seal has to perform is basically when it reads the blog information from the EL, it has to go through the request and it has to sort of put these I mean, it has to validate the request and then it has to put the valid ones into the seal block and enclosure. And if it finds a request that isn't supported under the current fork, then obviously, it's an invalid block. So it has to be treated as, as invalid in terms of the fork choice.
* But I think this is somewhat similar to if, for example, the EL had returned that the block is invalid, so it has to be treated in the same way. whereas like, yeah, it's basically the same as having an invalid execution result or something. 

**Dustin**
* I mean that's very reasonable. I, that's my inclination personally as well, is to say if any single invalid thing makes the whole thing invalid. That said, there's precedent I'm not, you know, so the invalid deposits don't make an entire. Invalid in the CL, for example. And I'm not saying that here, but but I'm saying that they're interesting point. 

**Felix**
* Yeah actually that I don't really know how it works for these. I mean, if you make how does it actually work, maybe you can quickly give a comment. I'm sorry for stretching this out so long, but this is honestly super interesting. Like what happens if the like if a withdrawal request is submitted, for example, that isn't covered by the validator, then it's just ignored or I mean it doesn't obviously mean that doesn't lead to the block being invalid, but it's another kind of invalid, right? So you basically just discard this. 

**Dustin**
* Yeah. Basically for the request, invalid requests are skipped. Yeah. but but whatever we do, I guess my point is and and I take your point, but not wanting to stretch this, but I do regard this. I'm bringing up specifically in this context because I regard this as part of this at some level. I mean, PR that you're trying to get in, which is to say there are if there are new error conditions that are not possible now that are possible after your PR, then those should be discussed as part of getting your PR in. And one of them is for example, you know this, let's say this this Interweaved case, you can I mean this maybe that's just an automatic reject, but then that should be again specified.
* I mean, I know we already discussed, but specifically a specific aspect of that to say that is an invalid thing somehow that should be specified because otherwise the risk is we get people trying to follow Postel's law. Right.
* The be liberal in what you expect accept thing. And this is this is dangerous in a way. This is what. 

**Felix**
* Absolutely agree with this. Yeah. 

**Dustin**
* So if we want to prohibit helpful quote unquote CL saying, oh, well, we see request type one, then two, then zero, then one. Let me just like sort that for you. Like we because the first one who sorts it, they'll be more compatible with with other with with random bugs. And this is and now that's a now everyone has to do that. That will get HTML5 you know in in JSON, RPC. And so like this is something that has to be prevented upfront from, you know, day zero. 

**Felix**
* Yeah I understand this and this, these concerns I will deal with by just adding additional text. But you are right that these things exist and maybe like some of that wouldn't exist as much if we had, put it differently in terms of the encoding. So it adds like these cases to the to the consideration. I agree with this. Okay. Okay. 

**Peter Miller**
* So the position from the from ELs perspective on this, is that when you execute the block, you deterministically generate a set of requests so that are, that are put in a block and there is no choice here or no discretion at all in the execution. You run the execution, you get a list of requests. And if the list of requests in the block is different than the one you generated during the execution, including if it contains extraneous requests or if it contains the request in a different order, it's just invalid. So there is only one valid form of the requests. So the EL, unless it is broken, guarantees that the what order the requests come in and there's only one deterministically valid order. and the second thing and the thing. And so from our point of view, if it's an ordering issue, it's broken.
* And like if the CL receives Receive something from the EL, and it concludes that the only possible way this could happen is that the EL is broken. It should reject the request and complain. the other thing that this was compared to is there are other situations where a request can be invalid, but in a way that the EL can't tell. The EL does not check deposit signatures, it does not check whether withdrawal requests are valid. So it just passes them on to the CL, and the CL processes them if they're valid and ignores them if they are invalid. so yeah, this this I don't think this this should be an issue. It should just be clear that there is only one acceptable order ring that the EL can produce, and that the CL, can rely on this if it wants to. And if it detects that this has not happened, it is welcome to just reject the request as invalid. 

**Dustin**
* I mean, I think as long as that's codified, that that mostly resolves the specific concerns, I listed, I mean, it still strikes me as a, kind of pointlessly flexible, like, it's it's a false flexibility as described. But sure, if one wants to insist on having that falsely flexible list and then, you know, adhoc, constraining it, or put rather, post hoc, constraining it, I guess that that works. 

**Tim**
* Okay. yeah. In that case, I think we should. Yeah. Wrap up this discussion. yeah. At this point. So, as I posted in the chat, I think the next steps here are, making the changes to the spec specifically just having some stronger wording around ordering guarantees and how we deal with invalid requests, making sure that's reflected not just in the EIP, but also on the, also on the execution APIs. And then hopefully we can get these merged async in the next few days. but let's try to get this done at the latest before next ACDC so that we have like the finalized set of specs for all these EIPs and the engine API as it relates to encoding these requests by next Thursday. Does that sound reasonable to people? Any concerns? Objections?
* Thoughts? Okay. Thanks everyone. And yeah, thanks Felix and Dustin for going to the details around the implementation specifics. okay. Next up, 7702 I forget who put this on the agenda. Oh, Andrew, are you on? 

# Update EIP-7702: consistent signature validity checks EIPs#8865 [36:02](https://youtu.be/A_DuQRICW70?t=2165)
**Andrew**
* Yes, I am. Yep. Okay. yeah. So basically, at the moment, how 7702 is specified, it restricts, like one part of the signature, namely S it should be. It says  S that's must be less or equal than this sect 256 K1 and divided by two, as specified by EIP two. But the problem is that so that EP two is actually a refinement of a pre homestead check that actually puts some constraints on R as well. as I mentioned in the PR. So we should either make it consistent and, like, check that the signature all signature values are valid. and yeah, there is for, like, you can look at the message in Geth, but it's kind of, basically it has two flavors pre homestead and post homestead.
* And we should use Post Homestead. also there is an alternative option by lightclient to actually, actually not check authorization signatures for validity only check that like that. Let's say all all signature values name namely why parity. R & S are fit into 256 uh bits. and basically think like the say in 7702 that, in case of invalid like the signature values outside of the EIP2 range, the transaction is not invalid itself, but that authorization is actually will be ignored when executing the transaction. I don't care much which option is adopted, but I think like how 7702 is specified now is inconsistent. 

**Tim**
* Thanks. yeah. Like, do you want to just give a bit more context on your PR and. 

**Lightclient**
* Yeah, so I think originally there was a PR that I merged by Dragan that added some, basically some instructions about what the serialization should look like in some reasonable bounds for the values in the seven. 702 transaction. And when I merged, I don't think I quite understood the implications it would have on the validity of the transaction. And I've generally had this, this idea that the transaction, the validity of the transaction should really just be based on whether the sender of the 772 transaction can pay for the authorizations that exist in the transaction and has like a correct nonce. So my PR is basically trying to bring us back to that world where in the PR that I had merged from jargon that said some specific sizes of the different types of the transaction, it also included this signature check that exists for the authorization list.
* And in my perspective, I don't think that we need to have these validity checks because it really just adds complication to the protocol that it's not really. It doesn't really feel necessary because if the sender of the transaction can pay for an invalid authorization, then we should let them pay for the invalid authorization. They're incentivized to not send junk data to the chain, but the data should be priced in a way where if they do do it, then it's, you know, it costs correctly. It's just the same as sending kind of no OP transactions to the chain. I think by having the validity checks, we have to iterate through all the authorization lists before we accept the transaction. And. It just adds a lot. It adds a lot more testing that we need to do to make sure that all of the different validity checks are correct. 
* So my preference is to remove as many of the validity checks as we can. I think in my PR, I've just made the validity depend on the data, the width of the different data types. So I think most things are just u-256. That's what I would prefer to go through rather than fixing what exists here, which was what Andrew's PR was doing. 

**Tim**
* Thanks. does anyone else have strong opinions? 

**Peter Miller**
* I'm very keen on the approach. but, like Trent suggested, it's probably worth, like, pointing out. Like what the issue actually is here is that there has to be two stages of, like, investigating these authorisations. Firstly, we have to like, basically pass them and make sure that they are actually authorisations and that they've been paid for. We can't allow people to stuff arbitrary data of arbitrary size in there for obvious reasons. but we can't actually validate the authorisation because that requires doing some curved math that's too expensive. And we don't want to, like, require people in the mempool to go and do large amounts of curved math in the mempool. We just want to do one check, make sure the thing is paid for, and then include it.
* Lightclient PR takes a very sensible approach that basically we just pass the request, we take the request to LP, we pass it if it doesn't pass because one of the data types is too big or the structure is wrong, then the entire VAT transaction is invalid because the LP structure of it is invalid.
* But we stopped. We stopped strictly there. We do not investigate at all anything other than is stuff the correct size? And I think that the advantage of that distinction is that it's a very clear distinction. It is this check does the transaction pass rather than are these authorizations valid. So I would support the client's approach. 

**Tim**
* Does anyone disagree or thinks an better approach would be better? 

**Oliver**
* I think I generally agree with the approach. I'm just wondering why the V component of the signature needs to be 256 bits. Like, why would it need to be constrained to that? Is it not in practice, a lot smaller? 

**Lightclient**
* The main reason is just this has been the signature width that we've accepted in the past, and I think it's much better to reuse all of the exact same signature tooling rather than have multiple signatures in the protocol, where we have different widths that we're accepting. So if we wanted to change the signature width, I would rather that be separate EIP to do it across, you know, many different signature types. 

**Oliver**
* So you're saying it's because we have an EIPs where we already do this constraint and it's 256 bits in those gaps. 

**Lightclient**
* I think all transaction types V is allowed to be up to you 256. Like in practice, I don't think it's really ever valid, because the only way you would get that high is if you had a chain ID that high. So there is kind of this implicit, there is an implicit idea that it is the size. But. Yeah, I could be convinced. I could be convinced to reduce the size of V. I in general don't think it's really that necessary because the people will pay for the data. People will overpay for that data. And it seems like an extra check that's, you know, not really doing that much. Like the signature won't be valid. Right? Ultimately. So it just like, feels like we're adding an extra way for a transaction to become invalid that doesn't, you know, it doesn't seem super necessary. I guess that's generally my take. 

**Oliver**
* I think, let's discuss async and then I'm fine with merging this. If it's like if this is already the standard, then I won't push too much back on it. But I think in practice, obviously it's not 256 bits. And it does have like some implications for performance, but I don't think it's like so major that we should block on it for now. 

**Lightclient**
* Yeah, let's look into it a little bit async. Thanks. 

**Tim**
* And I guess, if we're arguing about potentially reducing it, we could also bias towards merging this and then adding the like more constrained version after. 

**Lightclient**
* Yeah, that's my preference. I think in general people support this direction. So let's merge this after the call and expect that we'll have these changes for Devnet4 for and in the next week or two, we could look async about constraining the size of V. Yeah. 

**Tim**
* Does that does that make sense to you, Oliver? 

**Oliver**
* Yeah. Okay. 

**Tim**
* Anyone disagree with merging like PR which would supersede Andrew's and then using that as a basically a spec for Devnet for assuming we don't make further changes. Okay. Awesome. Then let's move forward with that. And yeah, continue the discussion about the different bounds on the V value. yeah. Thanks, Andrew and Lightclient for bringing this up. Then our last, issue about an existing texture EIP. The pricing for the BLS Precompiles, I don't know, Jared, put this on the agenda. I'm not sure if Jared is on the call. 

**Jared**
* Yeah. I'm here. 

**Tim**
* Hey, do you want to walk through. 

**Jared**
* So, Yeah, totally. So. Yeah. Well, benchmarking. The performance of the various precompiles in the Geth implementation, I discovered that the MSM precompiles, use, multithreaded execution. and that reducing them to single threaded, results in performance. That makes the, that makes them heavily underpriced, relative to both the other BLS Precompiles and, the recovery precompile and especially for the case of the G1. And so, yeah, I mean, this is just our implementation that I benchmarked so far, but, yeah. But basically, I want to broach the idea that we should, reprice these against a single the performance of a single threaded implementation, because, introducing concurrent execution to the EVM kind of breaks a previous precedent that we've set.
* And not only that but it essentially takes resources that could otherwise be used by the client and does not pay for them. so, yeah. So as far as, like, how to reprice them, the easiest idea that I came up with is just to across the board. So just to recap, in the pricing model for the MSM, Precompiles, there is this, table of values, a discount table. and that is basically if we, scale that by a factor of two that would be the easiest way to bring the price up to the level of the EC recovery precompile in the worst case. and then, like, obviously, if we wanted to get more complex, we could, change the each entry of the discount table and price it to or, and set the entries to the target the performance to some target like, I don't know, for example, the EC recovery precompile. So yeah. yeah. That's kind of what I had to say. 

**Tim**
* And just One quick comment. When you say, you know, increase the discounts by a factor of two, I assume you may. You mean make like reduce the discount by 50% for those curves? Well make them twice as expensive. 

**Jared**
* So the naming of the table is a bit of a misnomer because the price scales inversely with it. But yeah, exactly. Make make them twice as expensive across the board. 

**Jared**
* Got it. Yeah. 

**Tim**
* Just to make sure we're we're clear there. Thanks. Anyone have comments questions? Thoughts about this? yeah. There's a comment about checking other implementations and then plus one by Nethermind, I guess. How easy is it for clients to, how easy is it for clients to replicate these benchmarks? 

**Marek**
* So we have solution, we created a tool that can benchmark all appliance some time ago, but we haven't written the last test here. So if we if we do that work, then we will have benchmarks across all the clients. Okay. 

**Jared**
* If I can just jump in also. So I have the benchmarks I've implemented, I've also translated them to execute as state tests. So, if clients have the ability to benchmark state tests, then they would be able to replicate the inputs that I've used, without much difficulty. 

**Marek**
* We use engine API requests, but we can talk about it async. How to translate. Yeah benchmarks.

**Lukasz**
* Just one, one comment here. This is the tool. This tool was built because benchmarking is hard, especially for some managed languages like C Sharp and Java, because there is like multi-tiered, compilation going on. So you need to properly warm up everything. Etc. So it's generally complicated. So that's why this tool was built to have a proper benchmarks. and I would advise to use something more complicated than just a single run. 

**Tim**
* And I guess, yeah, if different teams potentially have different approaches here, is it reasonable for like Geth Basu, Aragon and Nethermind to just look into benchmarking these, on their clients individually in the next couple of weeks and then kind of report back as we have those benchmarks and hopefully by the next, ACD we're able to have like agreement about changing the prices. And I think it's probably good to use Jared's like, suggestion like simple idea of like using a factor of two x on the discount table and then, yeah, having other teams look at whether this is reasonable and if for whatever team or whatever other issue it's not, we can discuss it. But yeah. And I know two weeks I assume would be sufficient for people to look into this. So I'll take the silence as a yes. 
* yeah. So I guess in terms of next steps, let's yeah, have each team look into it, run the benchmarks. we can report back. Is there, like, an issue or like a channel? I guess we can just use the execution layer channel in the R&D discord to discuss this. like the execution dev channel, which Jared was already posting, benchmarks in, and then, um. Oh, maybe. 
* Justin, is that on the timeline or on whether it's possible for Besu, too? Okay. Besu is a yes now. Okay. So. Yeah. Let's follow up. Let's follow up on this on the execution dev channel. But then hopefully, at the latest two weeks from now, we'll have the benchmarks from all the teams. And then as soon as we have that, if, they're all roughly similar, we can just 2x the, the costs. And if there's like big, big discrepancies between different client teams benchmarks, we can look into that further. does that make sense? Okay. well, yeah. Thanks, Jared, for sharing this.
* And, yeah, we can now move on to, last, I guess, big thing on the agenda. So on the last act, there were a bunch of potential EIPs that were brought up to consider for inclusion in Pectra. We already have a ton of EIPs in Petra. It is by far already the biggest fork, in terms of number of EIPs. but there's still some other stuff. So, we had, for EIPs that were CFI. So, the R1 Precompile, inclusion list was I think we agreed we're not going to do the call data cost increase, and then the decoupling of the blob count between the EL and the CL. And in addition to this, there were a couple more EIPs. So we had, these SSD EIPs we've been talking about, for a couple of months.
* There was this EOF related EIP has code which would allow, effectively to check whether an EOF account is a smart contract account or calendar and EOA. And then lastly there was Max's EIP to increase the minimum base fee per gas. and so I asked the teams to sort of share, what their perspectives were on these, on these different, these different EIPs. We heard back from Roth, from Ethereum JS and from Nethermind. each of them you can see on the agenda their, their, their opinions. And it seems like across at least these three teams, the decoupling of the blobs is like the least contentious. So it probably makes sense to start there. 
* So yeah, for EIP 7742 I don't know. Yeah. Aragon, Besu, Geth. how you all felt about this one. Does anyone have concerns? but it seems like the the one thing that had the broadest support, and that's also pretty straightforward. 

**Matt**
* Yeah. This is Matt from Besu. I think the same normal scope creep considerations. But yeah, we're in favor of specifically the decoupling and loosely in favor of those other two as well, just to get that out there. But we can discuss those more as we go. Thanks. 

**Tim**
* Anyone from Aragon or Geth? 

**Andrew**
* So I think we are slightly in favor. No strong opinions. 

**Tim**
* Okay. And then there's some comments in the chat that, yes, the fork is big. And, you know, should we consider removing some EIPs. yeah. Like, I'll also echo this where we have a lot of different things in this fork. Yeah. I don't know if anyone has thoughts there they want to share. Alex has a comment saying instead of removing, we could consider splitting it into two forks. Alex, do you want to expand on that? 

**Stokes**
* I mean, I think everyone agrees that it's a really big fork as scheduled. So a natural thing to do is just to break it into two. you know, generally smaller forks are less risky. In particular with touch. Right now there are a bunch of like, cross layer EIPs, which really raise the like, testing and security review loads. So that's not great. And yeah, I mean, I'm curious how people think about this. 

**Tim**
* Yeah Lightclient has a comment about Perry proposing this. I remember there was like a DevOps doc that had like 4 or 5 different options and Perry saying plus one to a split. I don't know. Perry, do you want to share? yeah. share more context there. 

**Parithosh**
* Yeah. I think the main reasoning is that, currently we have a lot of EIPs, and we're tending to touch many more layers of the stack. And the more we add slash, even at the current load, it's hard for any one person to have an overview of all the changes. at least the approach we're taking right now to testing is one level. The testing team looks at more the EL EIP,  and we're looking more at the CL EIP. But I do think it's it's a lot. but yeah, just want to put it up out there as well. 

**Stokes**
* Yeah. And maybe it would. Be specific. Like one option is just looking at sort of the core pectra. That we have right now say on three. And there's things that we're discussing. Say like EOF or pure dos. I think those could very naturally go into a second fork. Just given development timelines and again accounting for how big picture. Would ultimately be if we do it all at once. 

**Ansgar**
* Yeah, I just wanted to. Basically very briefly say in support of PeerDAS, because I do think kind of a split. Might make sense. And I'm actually conflicted on PeerDAS as well, but I. Wanted to at least give voice to the point that to me, over the next year, this is. kind of the the part of the upcoming upgrades that is the most core to kind of the strategic roadmap of Ethereum. And so at the very least, it might be unavoidable, but it would have to go into the second part of the split. But I would at least say that we should at least try to basically give it like give it a try, evaluate. Like, is there any chance we could have it be in the first part? And and if not, then yeah, of course it has to go into the second part.
* But I just wanted to mention to me that really is stands out in terms of its strategic importance to Ethereum. 

**Jared**
* Thanks. 

**Tim**
* There's a question by Oliver, like how we would split. I think one thing we should consider there is that when we start bundling things in devnet and testing releases and whatnot, like there's then a cost to unbundle them. and so like, not that what we already have in Devnet should exactly be Pectra, but I think we should like that should basically be like our default of, like, stuff that's already bundled and being tested together is going to be quicker to ship together than if we both add more stuff and also remove more stuff. and in the past we've seen like mainnet consensus issues happen when we like remove EIPs from forks as well. So we shouldn't. Yeah, we shouldn't treat removing something from the current scope as effectively like free.
* We should assume that will also take some testing and engineering work. And so like.
* Yeah. So there was a comment about Devnet 3, like, I'm trying to find the spec real quick. but basically Devnet 3 right now comparing it to Pectra. So 2537, 2935, 6110, 7702, Max DB 7549, are all in. so I think, this means that the the two EIPs included in Pectra today that are not in Devnet three are PeerDAS and EOF, which is a whole set of EIP, and then none of the additional EIPs that we've considered, in the past couple of weeks that we were just talking about are included yet either. so that's kind of the way to think about it, where Devnet 3 has everything except EOF and PeerDAS, and then which are also being prototyped in, in devnet right now, and then all these other EIPs like 7623, 7742 and whatnot. don't have any prototypes or implementations as far as I know. 

**Jared**
* Yeah. Please. 

**Parithosh**
* Just one other point to bring up and already kind of playing the devil's advocate. if we do split EIP today, what's the guarantee that we're not going to add more EIP to the next fork and kind of be exactly where we are right now, just six months down the line? And how do we prevent that? We don't do that I guess. 

**Tim**
* Yeah. I guess maybe to touch on that and like Kev has a comment saying, like if we split, when would the second fork be? I don't think that we can I don't think it's useful to like, think about when the second fork would be, because we're just going to like optimistically. say something and then probably be wrong. the way I would think about it is assume everything that's already in Pectra is like the set of things we want to ship as quickly as possible. Does bundling it all in one release make the whole thing ship quicker? Or do does isolating some of these changes together make the whole thing ship quicker?
* And my intuition is like, if you just look at what's already in Pectra today, it's potentially quicker to like literally ship, you know, Devnet three separate from PeerDAS and EOF and that the date when all of this is live on main net is earlier than if it was all combined.
* And there was all these weird, interactions across it. but yeah the other question there is like if six months from now, if six months from now we keep adding a bunch of stuff to like whatever Pectra two is. then we're kind of in the same problem. So in terms of scope, yeah, we, I think we'd want to basically limit things as much as we can and like potentially start planning for like the fork after that. But yeah. dunno. 

**Danno**
* So I think the model we should probably consider  is basically, as you've been talking about, is it in the dev net? then it's set to go for the next fork and we could just close the door on Devnet three right now. polish it up, fix it, bug, fix it, only add absolutely essential changes and start on devnet zero on Pusaka. So we ship Devnet Devnet four becomes Devnet of Pectra becomes Devnet zero. Pusaka was put in there. We put all the other things that are ready to go in. We start testing that in parallel, but we also polish up Devnet three ship that just as soon as we get it polished and ready to go.
* That's that's something that I can get behind if we, you know, start putting a stake in the ground that this is already what's in the next devnet, the next hard fork with the devnet zero, that hard fork that would have solved a lot of concerns to say, well, when is it?
* Well, look and see which devnet it's in. And that's your answer. 

**Tim**
* I like htis idea. I think maybe the one net I'd say is like maybe there's like a devnet 4 that's like spectra 1. And then devnet 5 is like spectra 2 or something like that. Given that there were maybe things we wanted to add, that are simple, like, I don't know if people still feel that strongly about decoupling the blob count or like increasing call data cost, but like those EIPs are like relatively simple and like so I yeah, like maybe. Yeah. I'd be curious to hear from people like if we went with something like this, do we think Devnet 3 is the thing to ship. Do we think there's maybe still a couple things extra to ship as part of Pectra? And then, Pectra two becomes devnet 5.

**Stokes**
* I think that's a good way forward. And maybe just to add another plus one here. Like, I think the scope has been decided because we kind of just scheduled two forks with Pectra already. And so this is just recognizing that, like timing wise, risk wise, you know, production wise, it makes a lot more sense to have two here rather than one hard fork. 

**Jared**
* And yes. 

**Tim**
* To be clear, Kev, I think Pectra two I don't want to use like because like we already have Verkle scheduled for that. But like, yes, I would think of Pectra two, whether it's eventually called Verkle and you renamed the EOF fork. But like Pectra two is say you know, EOF and PeerDAS, but but yeah. Like it doesn't also include Verkle and we can like we can call it usaka or whatever. Like we can sort this out outside of this call, but just want to be clear that, like, this is, a separate thing than like the fork that has Verkle. 

**Danno**
* So my controversial take on Verkle is that it gets a third test line that is the current fork, whether it's Cancun or Prague or whatever comes after Prague. And it is that baseline. And when it passes its quality metrics, that is when we ship it independent of any other feature, because it's so big, it wants to be its own thing. So we let it be its own thing, let it grow when it's ready to ship and passes the quality metrics, that's when we pull the trigger and start scheduling it. So it's not tied to the regular release train. Something that big, is causing scheduling problems because we're really talking about inventing new fork names and moving stuff around because we can essentially tie this to a name for it.
* Now it ships when it's ready, and we give it its space to cook and make sure it's ready when it passes its quality metrics out the door it goes. 

**Felix**
* This is a good point, but you have to agree that it will only really start passing the serious quality metrics when we put it as the next fork. Like this is traditionally how things have been going. I mean, maybe for Verkle different because there have been dev nets and all this kind of stuff, even though it's not scheduled right now. But I mean, for sure, the finish line is sort of when it becomes visible by something being scheduled. That's when we really start putting all the effort in. 

**Guillaume**
* And more importantly, this, you know, like Verkle was more ready than many things that were, that were scheduled. And we pushed it because it was big. Yes. But okay. Sorry. I also have to do a babysitting at the same time. But, yeah, the the fork was already ready a long time ago at least. Like the quality metrics were already pretty advanced. we can't really push this because otherwise you're sending a signal that is very, I mean, no one will ever invest in it, but no one will ever invest in, in larger forks. And sorry about the noise. 

**Danno**
* Well, the quality metric I had in mind was 2 or 3 successful main shadow forks. So you move towards the full rehearsal and the rehearsal is ready. You just swap in and say, that's the one that's going next. I don't think you had a successful main net fork yet. You've had some test net forks. No, no, it's pretty full size. 

**Guillaume**
* This is this this is unprecedented. Like this is the amount of quality EOS was never held up to. And this this is completely unacceptable. 

**Tim**
* Yeah, I think another way to look at this is like when we when we scheduled Verkle for the fork after, Osaka or, sorry, Pectra. we then started adding a bunch of stuff that we thought we should do before Verkle. And that list sort of grew longer and longer and longer. And there's a sense in which, like we effectively prioritize this ahead of Verkle, one way or another. And whether it's like one fork or two forks, I'm I guess that's the main thing, that at this point feels like a decision to be made, but, yeah, it seems like I know teams wanted to work on before work, and we made this decision. We're already, you know, quite far ahead in the testing. and again, we can always like, revisit these decisions, but there's also a cost to that.
* So I yeah, I think when you look at it is like assuming this is the set of things we want to do now and that we've already committed to doing before. Verkle what's the quickest way to ship all those things? and yeah, I think my sense and like, what a bunch of other people have echoed is like splitting this set of things we wanted to for vertical into two separate forks is probably quicker than keeping it bundled together, because there's like a effectively non-linear cost in testing and engineering complexity of having a massive fork rather than two small ones. And then I think the big risk, though, if we do this, is that we split in two forks, and then we look at the second one and we're like, wow, this only has ten EIPs. Now we can like bump it up all the way to 20. And then, you know, we sort of end up in this infinite loop of. 
* Splitting forks over and over. My hope is we're like slightly better than that. And we can commit to, like, keeping the scope relatively tight. yeah. I guess, yeah, maybe. yeah. Another question is like, is there anyone or any team that feels like a single unified fork, including like, regardless of the additions we're talking about, but like, just including the stuff that's already, in Pectra would be quicker than, like, yeah, two separate ones. Um. yeah. Ben. 

**Ben Adams**
* I mean, it really comes down to the devnet process, I think, isn't it? how much, splitting it into two. Because now we have to do two sets of devnet, versus doing M1. I don't know the answer to that, though. 

**Tim**
* Well, I guess the so we already effectively we have today three sets of devnet, right. There's there's textured devenet. There's the EOF devnet. There's the PeerDas devnets. as I understand Danno's proposal, it's basically we say we use Devnet three as the basis for Pectra one.  We you know, we do that, we keep working on it, we ship it. And then the work that was currently happening in the EOF and PeerDAS, Devnet tracks, gets bundled into and that we were planning to include in Devnet 4 for instead of Devnet4 for being just like a continuation of Spectra spec, definite for just gets rebased on Pectra and effectively becomes, you know, Devnet zero of Pectra two or something like that. But, yeah. 

**Parithosh**
* And also just want to make a point that, PeerDAS hasn't been rebased on Pectra either. So it was kind of a commitment we had to make anyway, so we can just continue to keep the PeerDAS line of Devnet separate and just pin like a Pectra branch we would consider canonical for PeerDAS. And I guess we would do the exact same thing for EOF. But I guess we can discuss those details more in the breakout rooms that we would eventually have. 

**Tim**
* And I guess so. We have Devnet three that's launched today or sorry, yesterday. I assume teams still have like some work on this. but at the same time, like this is kind of a huge decision to consider. So we probably should give people time to think about it. But what's the timeline by which teams, you know, like feel we need to make a call here. where like, yeah, if we if we don't have a decision on the specs, then we effectively won't know what to implement in the next devnet. like, do we need to make this call today? Do we want to give people, like, a week or two to think about this? Um. Yeah. My sense is, like, a week would be reasonable, especially if we're considering different ways to split it. But. Yeah. Sorry, Alex. I think you came off mute. 

**Stokes**
* Well, I was going to say if we don't decide today. Yeah. Then I would say either, I mean, next week would be great or definitely by next ACDE. Yeah. 

**Tim**
* Yeah I think. Yeah. I think ACDE feels like almost a bit. Yeah. Too far. but my yeah, my suggestion would be, by the next week looking at yeah. Like sort of what first the binary decision. Do we split or not? Second, if we split, are we happy with the scope of Devnet three as spectra one, or are there things that we feel strongly that we should include? and then and then also like, you know, if we do make some changes to the actual EIP already in Devnet three, like we discussed in the earlier half of the call how to approach those, and how do we want to get to a spec freeze? yeah. But I think that's that's kind of reasonable. And there's a comment in the chat as well around, timelines.
* So like, I think there's also broad agreement that if we split the ideas that we want to ship Pectra one quicker than, or as quick as possible, and, you know, early next year should be like our target.
* So if we think about, like, stuff we would consider adding to Pectra 1, you know, it should be stuff that doesn't really change the timeline under which we'd expect the ship to fork. 
* Yeah. So maybe. Yeah. So I guess. Yeah. A week from now on, ACDC, we can continue this discussion and see if, like any teams strongly oppose splitting, and if there's consensus toward splitting, then what's the set of things that we can optimistically ship, you know, some time between the end of this year, early next year. And do we need to bring anything else in that feels urgent and take it from there? Any other thoughts? Comments? Okay. well, yeah. Thanks everyone. 
* I'll try to write up some summary of this as well after people who weren't on the call, but let's continue this discussion on next week's call. okay. And then the last thing that we had on the agenda today was, some updates around network configs, for maintenance mainnet, sepolia, holesky. Keep you posted about this. do you want to give a quick overview? 

**PK**
* Yep. Can give. yeah. There is a set of PRs to align the format of the three public Network Genesis repositories. there isn't a big change, just aligning the format of all and to have a consistent format of all these repositories. So in particular we have that the execution layer genesis for mainnet and sepolia. And we started tracking the execution layer boot nodes for uh yeah for these networks. So it would be great if client teams could have a look at it and add, potential missing boot nodes that are operated by them. So later on we can ping these boot nodes and have some monitoring and blame the offline ones. That's basically it. 

**Tim**
* Thanks. Any questions? Comments? Okay. And then that's everything we had on the agenda. Anything else people wanted to cover? Okay, well, thanks a lot, everyone. Yeah, we covered a lot today. and again, yeah. Reminder to think through, the options for the fork before next ACD. And in the meantime, we'll also finalize the specs around, the encoding stuff. And, yeah, if teams can start looking at the benchmarks for the BLS Precompiles, that would also be great. So we can get the pricing done. and yeah, I think that's it for today. Thanks, everyone for joining and talk to you all on next week's calls. 


-------------------------------------
### Attendees
* Tim
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




