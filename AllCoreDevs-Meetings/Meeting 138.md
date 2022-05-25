# AllCoreDevs Meeting 138

### Meeting Date/Time: May 13, 2022, 14:00 UTC
### Duration: 1:38:56
### [Video Recording](https://www.youtube.com/watch?v=BFxkGdPv4F8)
### [Agenda](https://github.com/ethereum/pm/issues/518)
### Moderator: Tim Beiko
### Notes: Metago

## Agenda

### Merge Updates

#### Shadow Fork updates

**Tim** ([3:04](https://youtu.be/BFxkGdPv4F8?t=184))
Okay, I’ve moved us over to the main screen. Welcome everyone to all core devs 138, tons of merge stuff today and then if we have time, there's some updates to what was 4938, oh Felix had a networking EIP he wanted to talk about and then there's two other EIPs that wanted technical feedback. Hopefully we get through them. I guess first we had mainnet shadow fork 4 earlier this week, Pari, do you want to walk us through how that went?

**Pari** ([3:50](https://youtu.be/BFxkGdPv4F8?t=230))
Yeah, hey everyone, so we had mainnet shadow fork 4 yesterday, we hit TTD around 4 pm and it was a relatively, like nothing big happened. I think all the clients that were there before were also there after. We added a bunch of validators to minority clients that we didn't have in previous shadow forks, for example Besu, Lighthouse etc instead of purely just Besu, Prism um just so that we can track the attestation of proposals and the one thing we noticed was the Nethermind team mentioned that a couple of client pairs are proposing empty execution payloads. So we're getting proposals but the proposal itself is an empty execution payload. I know they're talking about it and potentially have a fix. I think there was a prism fix that they pushed yesterday I’ve updated a few nodes with it, but in general it was a really good run. We did have an issue with Aragon syncing up but that I think is an unrelated non-merge code base related issue. 

**Tim** ([5:09](https://youtu.be/BFxkGdPv4F8?t=309))
Got it.

**Danny** ([5:09](https://youtu.be/BFxkGdPv4F8?t=309))
Did you end up getting Aragon synced?

**Pari** ([5:09](https://youtu.be/BFxkGdPv4F8?t=309))
I think that's still not at head I need to check up on them now. Yeah.

**Andrew** ([5:21](https://youtu.be/BFxkGdPv4F8?t=321))
Yeah um yeah so we are working on a new sync mode and as Pari said the issue is not related to the merge or like yeah so we have a fix but it's not merge related.

**Tim** ([5:28](https://youtu.be/BFxkGdPv4F8?t=328))
So you have a fix for the issue that we saw?

**Andrew** ([5:35](https://youtu.be/BFxkGdPv4F8?t=335))
Yes, for the we have this new sync mode which we are still debugging and like the finishing and things like that but the old sync mode works fine.

**Tim** ([5:53](https://youtu.be/BFxkGdPv4F8?t=353))
Got it okay, cool and anyone from Nethermind want to chime in about like the empty blocks issues?

**Marek** ([6:04](https://youtu.be/BFxkGdPv4F8?t=364))
Yeah so the problem is that still the timing issue that I mentioned many times so, for example lodestar not giving enough time and…for block production and because of that we have empty blocks and if we do not have empty blocks on something else it is also probably something wrong.

**Lukasz** ([6:35](https://youtu.be/BFxkGdPv4F8?t=395))
Yeah and as of yesterday, I think Mario's changed that behavior in Geth async production of blocks on fcu that would probably manifest on that code base too.

**Marius** ([6:49](https://youtu.be/BFxkGdPv4F8?t=409))
Yes exactly, so that's coming in Geth 2 to have the block production async and then we should be also seeing empty blocks on Geth. So please, the nimbus and lodestar or prism and lodestar, I don't know, the clients that don't give us enough time, please fix this as soon as possible.

**Danny** ([7:11](https://youtu.be/BFxkGdPv4F8?t=431))
And for anyone listening there's kind of like a prepare, like where you're saying hey execution engine, I’m going to ask for a block, and then you call and a little bit later and say I want the block and if you put those too closely you know you just get an empty block from the executioner. 

**Tim** ([7:36](https://youtu.be/BFxkGdPv4F8?t=456))
Anything else people wanted to discuss about the shadow fork itself? Okay and then Pari, as I understand it, next week we are doing another mainnet shadow fork, but instead of using the client’s distributions that mirror mainnet where there's obviously some like majority clients, we're gonna do kind of an equal split across CL and EL. Is that correct?

**Pari**([8:13](https://youtu.be/BFxkGdPv4F8?t=493))
Exactly. We’re just gonna do an equal split and I think the other plans to have the configs out later today. 

**Tim**
Awesome.

**Danny**([8:31](https://youtu.be/BFxkGdPv4F8?t=511))
Okay one thing maybe worth noting just with the issue that was seen, you know, if there are some amount of blocks that they do produce, beacon blocks, but they don't have any transaction payloads, the elasticity from 1559 in that case as long as it's not the majority of blocks, would allow for no reduction in capacity so that would almost you know be something we wanted, would want to fix if we saw it on mainnet but would have been kind of a no-op for users, which is nice right.

**Tim** ([9:01](https://youtu.be/BFxkGdPv4F8?t=541))
Right, you get slightly slower inclusion but you know right...

**Lukasz** ([9:15](https://youtu.be/BFxkGdPv4F8?t=55t))
But that would discourage client diversity.

**Danny** ([9:20](https://youtu.be/BFxkGdPv4F8?t=560))
Yeah, I don't mean it's a good thing, I just mean that it's not that bad.

#### [RFC: Engine API response status when merge transition block is INVALID execution-apis#212](https://github.com/ethereum/execution-apis/issues/212)

**Tim** ([9:34](https://youtu.be/BFxkGdPv4F8?t=574))
Anything else? Okay next up on the last call, Mikhail, you had a request for comment about like an engine api status response when the merge transition block is invalid so I believe we just went with like the third option you proposed. You want to just give a quick update there?

**Mikhail** ([10:06](https://youtu.be/BFxkGdPv4F8?t=606))
Yeah, we just figured it out and it's now on the spec, it's converged like a few moments ago, so yeah invalid terminal ball cache is now replaced with the invalid status class latest valid hash point to all zeros block hash, in this way it's like less complexity for a CL client side and I don't think that adds any complexity to EL as well, and also it helps to fix the blind spots which is mentioned in the rfc that we previously had in the spec. 

**Tim** ([10:53](https://youtu.be/BFxkGdPv4F8?t=653))
Any client teams have thoughts or comments on that? All right if anyone…go ahead.

**Marius** ([10:53](https://youtu.be/BFxkGdPv4F8?t=653))
I think the change is fine it's just like I was a bit surprised that we did this change and so like these changes should not come this late in the pipeline and they also should be communicated otherwise I’m fine with this. 

**Marek** ([11:16](https://youtu.be/BFxkGdPv4F8?t=676))
My one comment is to have hive test for this change. Yeah.

**Danny** ([11:28](https://youtu.be/BFxkGdPv4F8?t=688))
I agree in you know anything that is being changed right now is primarily only related to edge case errors but even in that case I would prefer to not I think it's at this point we really need to be halting that.

**Mikhail** ([11:45](https://youtu.be/BFxkGdPv4F8?t=705))
Yes I agree but we had to have something here yeah and it's been communicated. I know everyone is busy with engineering so I understand that it didn't get too much attention but anyway it's been communicated in advance and the…will have a hive test for it. Basically one of the, yeah when the work and test was like on this test checklist, this blind spot has been discovered. That was the initial like reason to have this kind of you know change. 

**Tim** ([12:38](https://youtu.be/BFxkGdPv4F8?t=758))
Okay. Any other thoughts on that?

**Andrew** ([12:45](https://youtu.be/BFxkGdPv4F8?t=765))
Yeah I just, my thinking is that when do we finalize the engine api so because because like we would be finalized for Ropsten or for which test net because we should say okay this is we have merged all the pull requests that we already under consideration the engine api is final like mark will have a release give us some time to like double check that we do implement the final revision because it's otherwise some things might like with so many clients we will get 

**Danny** ([13:31](https://youtu.be/BFxkGdPv4F8?t=811))
Yeah I think we're at the place where we should probably put up a pr that's called a release candidate and not have anything go into it unless it's heavily discussed and noted by client teams and that release candidate would probably stand until we're pulling the trigger on choosing mainnet, but I think that release candidate should be up for review pretty much now as we're trying to make decisions on Ropsten. 

**Tim** ([14:01](https://youtu.be/BFxkGdPv4F8?t=967))
Are there other things that we anticipate needing to change with the engine api now?

**Mikhail** ([14:08](https://youtu.be/BFxkGdPv4F8?t=848))
I think it's more or less final. There are a couple of things that in terms of like clarification, so it's not like changing behavior whatever but I think we can do them shortly, so there were a couple of requests to clarify responses in some cases and likes and like safe block hash set to zeros should not be responded with any errors this also should be clarified in the spec. Yeah and yeah but that's like that that's not the updating behavior and in design it's just clarifications I think we can do that and then cut release…straight forward. 

**Tim** ([14:51](https://youtu.be/BFxkGdPv4F8?t=891))
So we don't expect any other kind of semantic changes basically.

**Mikhail** ([15:02](https://youtu.be/BFxkGdPv4F8?t=902))
We don't unless it's like necessary change.

**Tim** ([15:02](https://youtu.be/BFxkGdPv4F8?t=902))
Right obviously you can find a bug or an error. But when do we think like we can have those small clarifications and then a release candidate can we do that like sometime next week or is it does it?

**Mikhail** ([15:26](https://youtu.be/BFxkGdPv4F8?t=926))
Yeah, definitely next week we can do this. I'll take care of these changes and then we can communicate and cut release next week I guess, unless there are any other opinions. 

**Danny** ([15:39](https://youtu.be/BFxkGdPv4F8?t=939))
Similarly we'll cut a release candidate this coming week in the consensus specs as well and I don't think anything has changed in the execution specs for like 4 months now, there's two EIPs in it.

**Mikhail** ([15:59](https://youtu.be/BFxkGdPv4F8?t=959))
Yeah, the EIP is a pretty stable yeah.

#### [JSON-RPC: Add finalized and safe blocks execution-apis#200](https://github.com/ethereum/execution-apis/pull/200)

**Tim** ([16:07](https://youtu.be/BFxkGdPv4F8?t=967))
Okay, anything else on the engine api? Okay, the other thing that we did finalize was this discussion over the json rpc, finalized in safe tags. Mikhail, do you want also give a quick update on that?

**Mikhail** ([16:28](https://youtu.be/BFxkGdPv4F8?t=988))
Sure. So there are two new blog tags that we have added to the eth namespace so we have like we had the earliest, latest, and pending right, and now we have all this and also finalized and saved in addition to the previous ones. There was a discussion to have unsafe and as an a and the alias latest unsafe so yeah we decided not to introduce unsafe at all so it's now latest will always point to the head of the chain as it's been previously all the way and yeah one thing here is that execution layer clients should respond with error and this error is specified in this change, in this pr, the EL client should respond with error if the safe or finalized blocks acquire it before the transition gets finalized. That's one thing that's worth mentioning. 

#### [Sepolia beacon chain #526](https://github.com/ethereum/pm/issues/526)[Ropsten beacon chain #525](https://github.com/ethereum/pm/issues/525)

**Tim** ([17:56](https://youtu.be/BFxkGdPv4F8?t=1077))
Any thoughts, comments on that? Okay, next up, so yeah, we are kind of getting close to test nets and then one thing  to note there is that while Goerli has an existing beacon chain associated with it, Prater, Sepolia and Ropsten do not and there's been some discussions over the past couple weeks about like how do we structure those chains. Danny and Pari, I know you've thought a lot about this, this week, do you want to give kind of a quick update of where, what you're thinking for both Ropsten and Sepolia at this point?

**Danny** ([18:52](https://youtu.be/BFxkGdPv4F8?t=1132))
Yeah, so first of all naming wise, I think we should just call them Ropsten beacon chain, it's Sepolia beacon chain and the unification of the networks after, it's just Ropsten that's Sepolia, that's easy the Ropsten as far as I understand will be support would be deprecated probably after this in the order of some amount of months, and so doing that, there's two options one would be you know have a conservative size validator set just kind of get it up get it going with an open validator set or do a permissioned validator set with the erc20 contract based on some discussions, I think doing an open one is most beneficial to the community and we can start with just a hundred thousand validators that we control and community members can add and it would be unlikely that the community members would add so much that it would disrupt you know our stable backbone that we've added Ropsten, I think is going to be the first test that worked so we really should get this beacon chain up in the next couple of weeks  and then Sepolia beacon chain I think the idea would be to do a 2x validator set size in comparison to mainnet today also make it unpermissioned so that other people can jump in. This would give us the chance to or was it permissioned I’ll let Pari chime in but this would give us the chance to kind of see if anything shakes out with such a large validator set. Prater, which would become Goerli, is about the same size as mainnet and we try to track it poorly okay we try to track that so pretty much we need to launch two beacon chains. The Ropsten one will be unpermissioned hopefully people will join. I believe the Sepolia one will be unpermissioned as well but I can't remember, Pari, did we have one way or the other we were thinking there?

**Pari** ([20:58](https://youtu.be/BFxkGdPv4F8?t=1258))
Yeah we were thinking we can use the token contract so to be permissioned but we can just open up a faucet for the token yeah.

**Danny** ([21:09](https://youtu.be/BFxkGdPv4F8?t=1269)
Right. One of the one of the reasons we might permission that one is to do random testing on it in the event that we want to turn up at the validators or have a more controlled environment. I think the thing that we'll do is pretty much have suggested configs, have suggested distribution of validators and kind of make the rounds and get quick thumbs up and have the teams join us in kicking off these beacon chains. 

**Pari** ([21:42](https://youtu.be/BFxkGdPv4F8?t=1302))
Yeah the main thing that's so with Ropsten. I agree it's pretty much straightforward, we can start with something that's like 100k and people can join in, should be relatively easy to set up and anyway it's going to be deprecated in a few weeks, months so we don't have to worry about it too much, but the one I would like to discuss and get some consensus on is Sepolia. We essentially have two options, either we want a large beacon chain there or a small beacon chain. A large beacon chain means that we essentially saved early prater because we don't have to keep growing prater if we go with the small beacon chain for Sepolia then we're gonna continue to eat up a decent amount of Goerli, and that's mainly because we want to continue growing prater to keep up with mainnet. 

**Tim** ([22:39](https://youtu.be/BFxkGdPv4F8?t=1359))
Right so Sepolia if it's big becomes kind of our main net plus testing environment. 

**Pari** ([22:46](https://youtu.be/BFxkGdPv4F8?t=1366))
Exactly and the question then would be if we have a really large beacon chain for Sepolia, that means client teams have to now run two times a decent number of validators and have no idea how open they are to them. 

**Danny** ([23:03](https://youtu.be/BFxkGdPv4F8?t=1383))
Yeah to answer your question…, I mean I think most client types can handle thousands of validators per node. I don't know I mean you can also throw more resources in a node and handle lots of validators for now so I don't, we don't have to spread them necessarily too widely, I don't think it looks much different than what you would do on prater today.

**Pari** ([23:31](https://youtu.be/BFxkGdPv4F8?t=1411))
Yeah definitely it wouldn't be that different from what we have from prater today.

**Tim** ([23:38](https://youtu.be/BFxkGdPv4F8?t=1418))
Given we have Afr on the call and you came on Afr a few weeks ago to talk about the issues around Goerli ether, do you have any thoughts, about like if we should keep prater / Goerli as the large beacon chain, if that negatively like affects Goerli in other ways, yeah.

**Afr** ([24:06](https://youtu.be/BFxkGdPv4F8?t=1446))
Yeah, sure. I mean Goerli and Prater are already fairly big, it has a lot of users and it has a lot of validators. Sepolia is kind of still very unknown, so there we don't have a beacon chain yet and we don't have many users building on Sepolia yet, naturally. We have to keep in mind that we are deprecating a lot of
testnets in the coming months or years, so I would, my personal opinion is that we should use Sepolia as like a fairly stable application developer testnet, because it's fairly new and we still have the time or the chance to define how the consensus layer would look like or the Sepolia beacon chain would look like and I would personally just keep it simple for this network, and I would personally say that we should continue growing prater, but then again it's not that easy because we have a limited supply of Goerli ether but putting it aside, the main reason why we should grow prater and Goerli is because it's already fairly big and we have a lot of, much more interesting  foundation for testing and for growing this network. Does it make sense?

**Tim** ([25:29](https://youtu.be/BFxkGdPv4F8?t=1529))
Yeah, if you see it as a positive I think it's yeah, that seemed like the biggest like reason to not have a large beacon chain. 

**Pari** ([25:42](https://youtu.be/BFxkGdPv4F8?t=1542))
Exactly, I think that was the biggest point if we wanted to save on Goerli ether, it makes sense to have a big one on Sepolia but I also agree we can have really stable permission consensus engine and have Sepolia to be quite rock solid. 

**Danny** ([26:01](https://youtu.be/BFxkGdPv4F8?t=1561))
Yeah that was my original intuition and then I was convinced to maybe do the 2x. I think that's totally fine to do a smaller permission, very stable net, something that kind of feels like clicked in users, that doesn't have to…box and…I there are a number of kind of emerging ways for us to test load across many nodes that aren't, they're more in like transient type test nets and not public test nets so if we do want to test, you know, 2x, 4x, 8x, we can change sizes that we might instead just kind of take it into those test environments rather than only public testnet.

**Marius** ([26:37](https://youtu.be/BFxkGdPv4F8?t=1597))
Quick question, if we were to do the token beacon chain, this might interfere with withdrawal testing right? or..?

**Danny** ([26:58](https://youtu.be/BFxkGdPv4F8?t=1618))
No, it's independent so it's very transparent to the beacon chain. It has the same interfaces as the deposit contract and then withdrawals are totally totally unrelated to the deposit mechanism, so I think it will be fine.

**Marius** ([27:10](https://youtu.be/BFxkGdPv4F8?t=1630))
Oh right I’m stupid. Sorry, but yeah, but doing this way on Goerli if we were to do the token deposit on deposits on Goerli we could create new Goerli eth, we could inflate Goerli eth with withdrawals.

**Danny** ([27:29](https://youtu.be/BFxkGdPv4F8?t=1649))
But we'd have to like hard wait. What was that, what was the suggestion talking about

**Marius** ([27:35](https://youtu.be/BFxkGdPv4F8?t=1655))
Yeah, but you like it yeah but it doesn't make sense to throw away prater anyway, so 

**Danny**
Yes

**Tim** ([27:46](https://youtu.be/BFxkGdPv4F8?t=1666))
And there is a separate, just don't know what I saw I guess one interesting thing though there was a suggestion to like upgrade Goerli to give the clique signers a huge amount of Goerli eth I guess you can still do that even after the merge on Goerli, cause you still know the accounts, but it's kind of weird because you're like it's like a retroactive thing, yeah okay, anything else on the beacon chains? 

**Marius** ([28:32](https://youtu.be/BFxkGdPv4F8?t=1712))
How long would it take to set it up?

**Pari** ([28:32](https://youtu.be/BFxkGdPv4F8?t=1712))
Yeah, I was thinking of maybe setting it up on Monday or Tuesday, so clients could already bake in releases but we need to figure out some timelines for that, as in when does genesis happen.

**Tim** ([28:52](https://youtu.be/BFxkGdPv4F8?t=1732))
Right, and yeah and not only genesis but also how we want to run through Altair and Bellatrix, right?

**Danny** ([29:09](https://youtu.be/BFxkGdPv4F8?t=1749))
Right, I would suggest on Ropsten we just kind of like make it happen very quickly, in the sequence of initial 2800 epochs and then maybe for the Sepolia one maybe plan it a bit more like it's an event it's a thing that's happening, run your node before it happens.

**Tim** ([29:28](https://youtu.be/BFxkGdPv4F8?t=1768))
Okay, for the Sepolia and then the Goerli…

**Danny** ([29:34](https://youtu.be/BFxkGdPv4F8?t=1774))
Yeah so on Ropsten just kind of like yeah Goerli we'd have to schedule anyways so anyone running Goerli currently would have to upgrade their node for the Bellatrix fork.

**Tim** ([29:47](https://youtu.be/BFxkGdPv4F8?t=1787))
Right, and then that means that if on Ropsten, we want this close kind of  upgrade of genesis Altair, Bellatrix, we need the TTD for the Bellatrix upgrade. Correct?

**Danny** ([30:04](https://youtu.be/BFxkGdPv4F8?t=1804))
Right. I guess you would want to know it at that point in time.

**Tim** ([30:10](https://youtu.be/BFxkGdPv4F8?t=1810))
Right, so if you have a single release upgraded again yeah 

**Danny** ([30:16](https://youtu.be/BFxkGdPv4F8?t=1816))
Okay yeah so if that is a complicating factor then you just launch the Ropsten network now and then ships it to the upgrades when you know, but I guess that would, the distinction on what to do there I would defer to when we're having a Ropsten upgrade conversation, which I think we're having soon.

**Tim** ([30:46](https://youtu.be/BFxkGdPv4F8?t=1846))
Yeah I guess yeah just before we go there any other like concerns or thought about the general architecture or setup of the two beacon chains? Okay um okay yeah Pari thanks for the summary in the chat so Ropsten is 100k validators plus unpermissioned for people to join and Sepolia will be more like 20k and then be permissioned, probably would have not an option for people to join as well if maybe like not as easy.

**Pari** ([31:27](https://youtu.be/BFxkGdPv4F8?t=1887))
Yeah, exactly. We'd have a bunch of tokens and whoever wants to join needs to ask us for tokens.

**Tim** ([31:34](https://youtu.be/BFxkGdPv4F8?t=1894))
Right yeah, but then more stable obviously, great. Okay so yeah I guess you know on the last call we kind of briefly talked about Ropsten and I over the past two weeks like I’ve tried to talk with the different kind teams and testing teams and it seems like my general impression is like client teams are not, don't have like quite stable releases yet where there's still like some kind of open issues that they're looking at, there's still kind of some failing hive tests here and there, and so it's clearly not like a spot where the code we would deploy today is what would go on mainnet. That said, Ropsten is basically like a kind of testnet we intend to deprecate and one thing we also talked about in the past is because these upgrades are like a bit more hands-on for node operators where previously they would just like download the new version of whatever kind they're running and upgrade that, now they need to like figure out you know running an EL and the CL in parallel, and making sure that like that whole setup works, and that their infrastructure still works it and what not, it might be worth moving to like Ropsten a bit a bit quicker than we otherwise would because then you get people like another you give people like another chance to try the software and make sure that the overall setup works, even though obviously like what's going on Ropsten, what would go on Ropsten is not what would end up going on mainnet, we'd probably still have like some bug fixes and whatnot. So I guess I’m curious you know how the people generally feel about that, do we feel like it makes sense to do Ropsten, even though we're you know still kind of working heavily on testing, do we prefer to wait to do Ropsten, and then the risk there is potentially, you know we might have to push back the bomb, but that might still happen obviously if we find an issue, a critical issue at any point in the process. So yeah curious how people feel about that.

**Lukasz** ([34:04](https://youtu.be/BFxkGdPv4F8?t=2044))
So Nethermind is fine, the only potential issue is that it will take us a bit to release a version that we could use on Ropsten, so depending on the date, we might release version let's say a little bit late of course before the merge on Ropsten, but a little bit later than usual.

**Tim** ([34:29](https://youtu.be/BFxkGdPv4F8?t=2069))
Okay. And what does late mean just to get like a rough feeling?

**Lukasz** ([34:45](https://youtu.be/BFxkGdPv4F8?t=2075))
I think it would mean in two to three weeks we can release the version to Ropsten, two weeks is probably doable, but not like in a week, not like in a few days.

**Tim**
Okay.

**Marius** ([34:42](https://youtu.be/BFxkGdPv4F8?t=2092))
So for Geth, we want to create a release anyway next week and if we have the TTD for Ropsten, we can bake it in, there are a couple of open prs still to merge for the merge stuff, but those are only like minor issues um they were found by hive and so it's like not really relevant to the node operation and to the test nets, and so we can bake them into the release, or we can also just release them in the release afterwards. 

**Tim** ([35:45](https://youtu.be/BFxkGdPv4F8?t=2145))
Peter, I see your hand is also up. 

**Peter** ([35:51](https://youtu.be/BFxkGdPv4F8?t=2151))
So I just wanted to add that also I kind of agree with what you've said previously that this hard fork is a bit special in that all operators need to do a lot of extra work to figure it out and set it up so I am very very supportive of the idea of forking Ropsten. Let the shit hit the fan and so that everybody kind of figures out what it actually means to be part of this merge network, and then see where we go with the rest. So I think it's a good idea to do fork Ropsten early before making any commitments on the other ones.

**Tim** ([36:30](https://youtu.be/BFxkGdPv4F8?t=2190))
Got it. One thing I'll also add on that front is I think for mainnet there's a world where like the hash rate is, you know potentially going down and whatnot, and we may want to fork like to have the TTD happen quicker, than like the block times we said usually happen so I think that the thing we also want is like to train people in a way so that when mainnet comes they're able to upgrade relatively quickly, and maybe a bit more than like in a normal upgrade just because it's hard to estimate the TTD, especially in a world where the hash rate is all messed up. Besu, Aragon, any thoughts?

**Gary** ([37:19](https://youtu.be/BFxkGdPv4F8?t=2239))
Besu similar to geth, we have a release regular scheduled release next week and if we have TTD configs, we should be able to make Ropsten merge into those configs, we also have some failing hive tests that we're working on so we want to get those as sorted out as quickly as possible. Our release is planned for Wednesday of next week, so depending on when we have TTD configs, I think we should be able to get that baked in. 

**Tim** ([37:45](https://youtu.be/BFxkGdPv4F8?t=2265))
Okay, sorry Marius, you were gonna say something?

**Marius** ([37:52](https://youtu.be/BFxkGdPv4F8?t=2272))
Yes, it's really unrelated, but I think we should think about moving the Sepolia fork up a bit because it's relatively hard for solo stakers to set up nodes on Ropsten and Goerli because they have to sync so much, and like giving them the ability to test on a newish testnet so that they don't have to sync too much might be a good idea.

**Tim** ([38:30](https://youtu.be/BFxkGdPv4F8?t=2310))
So you would do like Sepholia, before Goerli, or even before Ropsten?

**Marius** ([38:39](https://youtu.be/BFxkGdPv4F8?t=2319))
No, I would do Sepholia before Goerli.

**Tim** ([38:39](https://youtu.be/BFxkGdPv4F8?t=2319))
Okay, okay we can definitely consider that. Yeah, once we, once Ropsten has survived the merge. Aragon any thoughts?

**Andrew** ([38:56](https://youtu.be/BFxkGdPv4F8?t=2336))
Well, next week I’m on holiday so we can, we still have quite a few things missing or like not fully implemented for the merge, so we haven't updated, we haven't updated to the very latest engine api, and also we have a lot of tests failing in hive, because the what's the click mining is not set up there, and also I haven't fully tested our sync performance. It's quite a few things, but we can provide a kind of raw alpha version, if the TTD is known.

**Tim** ([39:43](https://youtu.be/BFxkGdPv4F8?t=2383))
Okay and I’m curious on the on the CL side like I see there's like some prismatic people here, I don't know if there's any other CL team present. There's more people that can fit on it on the zoom screen right now but yeah anyone from the from the CL side have thoughts?

**Terence**([40:02](https://youtu.be/BFxkGdPv4F8?t=2402))
I pretty much agree with what everyone said, so yeah no thought on my end.

**Danny** ([40:15](https://youtu.be/BFxkGdPv4F8?t=2415))
You know, I don't have direct answers from the rest of the teams but we have talked as though this was very likely to be the next step, and to happen around me now so I don't expect much pushback for any question.

**Ben** ([40:32](https://youtu.be/BFxkGdPv4F8?t=2432))
Yeah no issue from Teku side I think. 

**Tim** ([40:38](https://youtu.be/BFxkGdPv4F8?t=2438)
Okay, and so I guess the does it make a difference, like so it seems like Geth and Besu can pretty much release something next week without too much issues, and Nethermind still needs like a bit more time and then Aragon…literally something like right now or then also needs more time, does it make like a difference if we choose the TTD today or like in the next, basically in the cl call next week, like does having one extra week before you know the TTD and then we can put out a release which combines everything, does that help people, or does that not really make a difference? So it's like if we choose it now and have a release next week versus choosing yet next week along with a slot I guess for Bellatrix in the CL call and then having your release like the week after, so like two weeks from now, yeah does that like move the needle for people or increase the confidence or is it kind of all the same and we should just…

**Marius** ([41:48](https://youtu.be/BFxkGdPv4F8?t=2508))
I don't think it makes sense to not choose TTD right now we can always, we like if you want if we want to have releases out in two weeks then we can have releases out in two weeks, but like choosing the TTD next week is just really weird to me, so we should choose it right now and either decide to have the releases out by next week, or by the week after but like artificially postponing the decision to choose to TTD doesn't make sense to me at the moment.

**Tim** ([42:28](https://youtu.be/BFxkGdPv4F8?t=2548))
Okay Andrew you have your hands up as well.

**Andrew** ([42:33](https://youtu.be/BFxkGdPv4F8?t=2553))
Yeah I would prefer to have a two weeks window for the release because as I mentioned next week I am on holiday and I’m not going to work on anything like maybe like only TTD, the bare minimum, so another week would be helpful.

**Tim** ([42:52](https://youtu.be/BFxkGdPv4F8?t=2572))
And that's knowing the TTD or

**Andrew** ([42:52](https://youtu.be/BFxkGdPv4F8?t=2572))
just another week to ship a release

**Tim**
Peter?

**Peter** ([43:06](https://youtu.be/BFxkGdPv4F8?t=2586))
…picking a TTD I kind of I think we can might as well do it I mean there's no harm really the only catch is that Ropsten is fairly easy to attack so to say meaning that we can TTD now and somebody just starts keeping mining with say 4…and that TTD might arrive tomorrow or something so we need to also have a contingency on what happens if somebody goes crazy.

**Tim** ([43:31](https://youtu.be/BFxkGdPv4F8?t=2611))
Right, so basically it's what happens if we think the TTD is gonna get hit before the Bellatrix slot gets hit, and then we need like an emergency TTD override.

**Danny** ([43:46](https://youtu.be/BFxkGdPv4F8?t=2626))
The Bellatrix slot I mean we plan on just launching with beacon chain right, so we just need to we need to launch the beacon chain before we hit TTD all right so 

**Martin** ([43:57](https://youtu.be/BFxkGdPv4F8?t=2637))
But hold on, that's not a problem is it, it will just mean that the client's course what would be a problem would be if we hit the TTD before we actually made
the release, before clients have been released so…right.

**Danny** ([44:09](https://youtu.be/BFxkGdPv4F8?t=2649))
Right, yeah otherwise it would be a live mass failure.

**Martin** ([44:20](https://youtu.be/BFxkGdPv4F8?t=2660))
Yeah that's totally fine. 

**Tim** ([44:20](https://youtu.be/BFxkGdPv4F8?t=2660))
Yeah okay so I guess I mean oh go ahead Peter, sorry.

**Peter** ([44:28](https://youtu.be/BFxkGdPv4F8?t=2668))
I mean in theory it's time to hit the TTD before the weekend thingy but if we're going to hit the TTD 4 days before the beacon chain launches, then you're going to have so many siblings at the top, so many sibling TTDs and essentially when you launch, everybody will be on their own little chain.

**Danny** ([44:47](https://youtu.be/BFxkGdPv4F8?t=2687))
Will there be a bunch of sibling TTDs? Would the miners keep mining or they would they just stop mining?

**Peter** ([44:54](https://youtu.be/BFxkGdPv4F8?t=2694))
I mean I will make one just for the fun of it.

**Danny** ([45:01](https://youtu.be/BFxkGdPv4F8?t=2701))
Yeah but you might you right but if you're running a Ropsten miner, it's just going to keep building on a single chain likely, rather than making a hundred little fork chains around TTD.

**Peter** ([45:12](https://youtu.be/BFxkGdPv4F8?t=2712))
So if you're running a stock geth code at least then your miner will as far as I know will stop finding everyone…actually that's a good question.

**Danny** ([45:25](https://youtu.be/BFxkGdPv4F8?t=2725))
No, I meant if you don't run if you're a miner and you don't run the upgrade, which is the only reason you would stop, you wouldn't stop. 

**Marius** ([45:31](https://youtu.be/BFxkGdPv4F8?t=2731))
No, you would mine the work chain, it would continue.

**Danny** ([45:39](https://youtu.be/BFxkGdPv4F8?t=2739))
Which would create a really nice stable TTD for everyone else. 

**Tim** ([45:44](https://youtu.be/BFxkGdPv4F8?t=2744))
Okay, so once we have the releases out, you know there's like the blog post on the EF blog, how long do we think we want to give people to upgrade their Ropsten nodes, like, so you know, we're basically like, yeah so say like two weeks from now, we have a blog post that goes up, and says these are the versions for Ropsten, is like another two weeks before we hit TTD sufficient? For people?

**Peter** ([46:18](https://youtu.be/BFxkGdPv4F8?t=2778))
Yeah. I think so nobody really oh okay apologies if I offended anyone, nobody really uses Ropsten, okay so time to be a bit aggressive and do yolo with it a bit just to get things rolling. 

**Tim**
Mikhail?

**Mikhail** ([46:35](https://youtu.be/BFxkGdPv4F8?t=2795))
On the related topic I would just like to remind people about fork next value if we are deciding about forking Ropsten I think it's also need to be decided what to use for the fork next value. 

**Tim** ([46:58](https://youtu.be/BFxkGdPv4F8?t=2818))
Oh because oh so that means you basically disconnect the peers, this is like for the fork id right?

**Mikhail** ([47:08](https://youtu.be/BFxkGdPv4F8?t=2828))
So in theory you shouldn't make any decisions based on the merge fork block. I know that in the past some clients have implemented some stuff differently, like except for the fork id change, and so we can set the merge fork block either before or after the actual fork so.

**Felix** ([47:32](https://youtu.be/BFxkGdPv4F8?t=2852))
Yeah, it's also important to notice that the fork next, it was kind of like invented for this world where forks are scheduled at a specific block, so it might be better to ignore, like to not set it for the merge fork, like 

**Marius** ([47:50](https://youtu.be/BFxkGdPv4F8?t=2870))
Felix we have we have a merge fork block specifically, that is not the fork where the merge actually happens,, but that that is only for the to split the networks afterwards. 

**Tim** ([48:10](https://youtu.be/BFxkGdPv4F8?t=2890))
And do we want to set that before, like in the release for the merge, or in the release after the merge happen, and we know what the actual terminal block hash is? 

**Felix** ([48:17](https://youtu.be/BFxkGdPv4F8?t=2897))
Yeah we need to know what yeah we need to know what the block was, yeah, don't think it makes sense to set it before.

**Mikhail** ([48:29](https://youtu.be/BFxkGdPv4F8?t=2909))
We were discussing one way, one reason to set it before, is it will force users to upgrade their nodes, because they will see that they are starting to lose connections, like with other peers, but I don't know if like, this is valuable to do and I don't know if it will work as discussed.

**Marius** ([48:53](https://youtu.be/BFxkGdPv4F8?t=2933))
And like the downside to it is that you will alienate all the people that are not upgrading, and this might include miners, some miners might be, like forked off from the network, and so I think it's very little gain for a potential bad situation. 

**Tim** 
Martin, I see you hand up.

**Martin** ([49:26](https://youtu.be/BFxkGdPv4F8?t=2966))
Yeah, I have a question slash thought. So if we set fork…next to a high value, that won't split the network with it until that high value has been hit, because I was wondering if there might be any value in setting up or next to some high value just so that we more easily can determine on the peer-to-peer protocol level, kind of how large percentage of the network is upgraded…just…

**Micah** ([50:10](https://youtu.be/BFxkGdPv4F8?t=3010))
High value meaning like I don't know six months from now?

**Martin** ([50:16](https://youtu.be/BFxkGdPv4F8?t=3016))
No, I mean like for Ropsten, we do the release and then we can get a kind of good estimate by just connecting to 100 pairs and checking how many signal that this new fork id next and know how large the census network has upgraded.

**Tim** ([50:39](https://youtu.be/BFxkGdPv4F8?t=3039))
Right, but I think otherwise we would have to…how big do you just like how far in the future do you pick the block, you just picked like a random, you know that's not like… 

**Martin** ([50:45](https://youtu.be/BFxkGdPv4F8?t=3045))
I mean you could you could put it to three years in the future. 

**Danny** ([50:50](https://youtu.be/BFxkGdPv4F8?t=3050))
Yeah but would it maybe be valuable to put it like plus two months past what we think TTD is so that it actually does take an effect.

**Martin** ([50:56](https://youtu.be/BFxkGdPv4F8?t=3056))
Probably more because if we ever do hit that then we will actually cause a split so we should I mean if we use it only for that purpose then we should set it to like three years in the future so that we know that two years from now, people use a different software where we have kind of disabled this, or not have this.

**Peter** ([51:20](https://youtu.be/BFxkGdPv4F8?t=3080))
But the point is actually to have that split the network so that's the entire point, otherwise why not disable it all together, if we are going to set it three years into the future.

**Martin** ([51:42](https://youtu.be/BFxkGdPv4F8?t=3102))
Right, but we don’t know, until after the fork, what number to set, right, so when we do the next release, we can set the fork id to whatever it was.

**Peter** ([51:50](https://youtu.be/BFxkGdPv4F8?t=3110))
I mean you can just punch it and set it to, I mean if you send it two months in the future there's no way you're going to reach that, I mean somebody might attack Ropsten, and my two months’ worth of blocks that seems a bit excessive, but definitely won't be able to do it on any other testnet.

**Tim** 
Andrew, you've had your hand up for a while.

**Andrew** ([52:19](https://youtu.be/BFxkGdPv4F8?t=3139))
Yeah I think how far as far as I understand it if we set it too far into the future then it won't cause a split and we already see this happening on shadow forks so for the main net I would think we should set it to something happening reasonably soon after the TTD is reached, like maybe two weeks or something like one week after the TTD. 

**Tim** ([52:41](https://youtu.be/BFxkGdPv4F8?t=3161))
That means that am I right in saying that means that miners then need to upgrade their nodes?

**Andrew** ([52:48](https://youtu.be/BFxkGdPv4F8?t=3168))
Well if it happens after the merge that they then they don't. 

**Tim** ([52:53](https://youtu.be/BFxkGdPv4F8?t=3173))
Okay because you don't, you don't pre you don't disconnect peers until that block has actually been hit, correct?

**Andrew** ([52:59](https://youtu.be/BFxkGdPv4F8?t=3179))
Right right well ideally you would want to set it like maybe an hour after the merge, but how can you get…What if, is it possible to change fork id to actually be based on the TTD rather than…

**?**
No

**Felix** ([53:33](https://youtu.be/BFxkGdPv4F8?t=3213))
Running into it, yeah, so it's designed to be a block number and we cannot change the definition now because all the other software also publishes as a block number. We could make another, we could make a new version of the, of the sort of like ? entry and things like that like we could just create like, we can create a new system that like works a bit different, but then it won't really be supported by the older software, so it's like the, this is, we know that all of the nodes right now with that implement the protocol will behave according to the previous definition and it's the this one that is given in the EIP also with the rules and they are based on the block number so

**Tim** ([54:14](https://youtu.be/BFxkGdPv4F8?t=3254))
Yeah, and we'd also be doing all of this work basically just for one time right? like there's no, like we're not, after the merge basically we're not gonna need this because you can keep using your block number. So it seems like I don't, it just seems like a lot of work to basically solve for this edge case.

**Lukasz** ([54:44](https://youtu.be/BFxkGdPv4F8?t=3284))
All right, block number need to be chart coded? Can we just like when we finalize the transition block, can we just use this as dynamic fork id?

**Peter** ([54:57](https://youtu.be/BFxkGdPv4F8?t=3297))
No, so the problem with fork id is that the moment the fork passes the block number, all of a sudden it gets enforced and anyone who tries to connect to you and saying that let's say they are up to date with the network but they don't know about this 

**Tim** ([55:22](https://youtu.be/BFxkGdPv4F8?t=3322))
And so, given that and you probably, it probably means that you want people to retroactively upgrade the fork id kind of at the same time, does it make sense to target a block number that's at least over a year out, so that when we have the next hard fork after the merge we can update both block, both fork ids so we can like update this fake one and we can update the real one to whatever the next fork block will be, would that, does that make sense because otherwise if you have clients like changing it right after the merge and they don't already put out releases at the same time, like basically we're not coordinating your hard fork, then you might see some weird stuff happening there. 

**Felix** ([56:09](https://youtu.be/BFxkGdPv4F8?t=3369))
This is kind of what we were saying right? So it's okay I think to basically let's just try and work around the fork id for the merge. So the consensus that I’m hearing is the fork id will just, like, it's a potential source of trouble with the merge, and it's also not possible to set the block number, so we just kind of want to ignore the fork id for the merge, and like why should we set it at all to something for the merge then. 

**Marius** ([56:40](https://youtu.be/BFxkGdPv4F8?t=3400))
Well like in order to like disconnect from the nodes, from the unupdated nodes quickly after the merge…yeah like if we were like if we were to schedule a new fork one or two months after potential TTD, then this would happen right?

**Tim** ([57:05](https://youtu.be/BFxkGdPv4F8?t=3425))
Sure but also one or two months is like way too long of a delay to fix the like yeah.

**Felix** ([57:12](https://youtu.be/BFxkGdPv4F8?t=3432))
Why not just make yeah so basically I think the fork id will not help us with the merge, so basically we should try to get the fork id out of the way for this, for the merge, it's not it's not a regular hard fork in that sense, so it cannot it should, just not have the we should just not use the fork id it's not possible to schedule it correctly, and we will just schedule it for the next fork again and if the merge goes really well we just schedule like the next fork very soon and I mean people will be I think very ready to upgrade their nodes after the merge, like I mean we will see the people who will upgrade for the merge will also upgrade for the fork after, I think, and this fork can literally only be about I don't know, probably something has to be fixed anyway, and then you know we can schedule it by the block number, and make the fork id and it will everything will be fine again, but I think for specifically, for the merge since it is not scheduled by the block number the fork id system cannot help at all, it was designed with the specific goal of like providing what it does when the fork is scheduled at a specific number.

**Tim** 
Danny?

**Danny** ([58:30](https://youtu.be/BFxkGdPv4F8?t=3510))
Yeah so I, there is potential value in being able to crawl and know what nodes have upgraded and what nodes haven't.

**Tim** ([58:36](https://youtu.be/BFxkGdPv4F8?t=3516))
But we can do that with the graffiti and the client versions right?

**Danny** 
You tell me on the client version, graffiti, not necessarily.

**Tim** ([58:49](https://youtu.be/BFxkGdPv4F8?t=3529))
That's what ethernodes does, they look at like client, if client version is bigger than x across every client. 

**Danny** ([58:56](https://youtu.be/BFxkGdPv4F8?t=3536))
Yeah then that's fine. I also but I also think it's not necessarily unsafe if we do want to quickly upgrade this after, to just firmly put it plus three months of what we think the longest TTD would be, and then you get the natural segmentation after anyway, without having to upgrade the nodes again. I don't really care, I think that that's like relatively clean but otherwise it's fine to also just do nothing.

**Tim** 
Jamie?

**Jamie** ([59:27](https://youtu.be/BFxkGdPv4F8?t=3567))
Yeah, I just wanted to mention a kind of counter intuitive aspect of the fork id when it's added that was found working on Nimbus. When you add a next fork id, it's not true that all of the nodes that haven't upgraded will sync up to that fork id, the block I mean of that fork id, if they're sufficiently far behind they actually stopped syncing at the previous fork id, so we had a situation where once London was passed and everybody else had reached consensus on London, when we were running software that didn't know about London, it actually only synced up to Berlin, and then it wasn't able to connect to nodes after that, so it's perhaps just something to keep in mind, because you mentioned earlier that you believed all the nodes that haven't upgraded will keep syncing up until the next block associated with fork id. It doesn't always work that way.

**Tim**
Got it.

**Micah** ([1:00:45](https://youtu.be/BFxkGdPv4F8?t=3645))
Is there some argument against what Danny suggested, just set the fork id to three months after whatever we think the longest out is?

**Andrew** ([1:00:57](https://youtu.be/BFxkGdPv4F8?t=3657))
Well, the problem is that you'll have a lot of like, we observed it on shadow forks and for some reason when you ask for a certain header by hash, you get incorrectly, I don't know who sends it, but you have headers from the wrong shadow fork on like from the main net, when you're on shadow fork, and so on so, and that happens because on shadow fork, the merged block is set so far into the future that it doesn't cause a split, so for if we set it four to plus three months we'll have for three months, if we don't do anything we'll have this weird situation when you have forks from both proof of work and proof of stake.

**Micah** ([1:01:40](https://youtu.be/BFxkGdPv4F8?t=3700))
Let's see, so I understand correctly there's basically three options: one we don't use fork id at all and which would still result in the same problem that you just described, or we set the fork at three months in advance in case we have three months of that problem, or we do like a quick upgrade right after TTD, and set it or do some sort of manual turnaround so that we don't have that problem at all. Is that accurate? 

**Andrew** ([1:02:05](https://youtu.be/BFxkGdPv4F8?t=3725))
Well we can try to calculate it so that it happens like last two weeks, and then that like 

**Marius** ([1:02:17](https://youtu.be/BFxkGdPv4F8?t=3737))
I wouldn't, I think trying to calculate it plus two weeks is a bit dangerous because we don't want to have it before the fork, because we don't want the majority of miners to drop off before the fork, so I would say let's do something like plus one month plus two months and that's it and that's basically been the idea from the beginning.

**Tim**
Lukasz, your hand is up.

**Lukasz** ([1:02:47](https://youtu.be/BFxkGdPv4F8?t=3767))
Yeah, so we had still have this issue somewhat, and shadow forks when we tried to sync, we were trying to sync from wrong peers, so our work workaround there was to when we connect to the peers ask about of one of the latest blocks we got from beacon chain, about the hash if they have it and just disconnect, if they don't so that's kind of a workaround that we disconnect peers I mean without those 

**Micah** ([1:03:24](https://youtu.be/BFxkGdPv4F8?t=3804))
Does that mean that you can't sync from peers that are currently syncing?

**Lukasz**
Yes, to some extent. Depends on their stage.

**Micah**
Yeah, sure.

**Marius** ([1:03:40](https://youtu.be/BFxkGdPv4F8?t=3820))
Also these issues on the shadow fork are only this like harsh, because you have like 100 nodes on each shadow fork, but you have like thousands no thousands of nodes on mainnet. If you turn it around and like most of the nodes are actually having the canonical chain then you won't have to, won't have these these issues syncing from the wrong piece. 

**Micah** ([1:04:16](https://youtu.be/BFxkGdPv4F8?t=3856))
Yeah, but I'm concerned because upgrading this time around is so much harder. I have a small fear in the back of my head that we will have significantly more people that don't upgrade correctly, or don't upgrade at all just because it's hard this time whereas previously, as you know, just update your docker image update, your package, whatever, now it's like, oh I gotta do a bunch of work, maybe I’ll put that off and not do it and so I’m concerned we might end up with actually a significant number of nodes not updated.

**Lukasz** ([1:04:39](https://youtu.be/BFxkGdPv4F8?t=3879))
So to clarify we're asking only about the header so currently after the, after the merge, everyone starts with syncing the headers like backwards probably, so that's you don't really disconnect anyone that's on the after the merge, right? 

**Tim** ([1:05:04](https://youtu.be/BFxkGdPv4F8?t=3904))
So just to kind of try and wrap this up does it make sense to try to just do nothing with the fork id on Ropsten, see how that goes and if we see that like it raises a bunch of issues we can then try and do like a plus three month thing on Goerli and Sepolia, and see how that goes? I think like Micah like your concern about people not upgrading will be at its truest on Ropsten because this is where people have the least incentive to actually upgrade their nodes, so like if you know if it's all right on Ropsten, and it doesn't cause any significant issues you would think on mainnet, they would also be right because the stakes are kind of higher for people to monitor that network.

**Micah**([1:05:55](https://youtu.be/BFxkGdPv4F8?t=3955))
If they understand correctly. We've already actually we've already seen the problems it caused and we know there's going to be problems right? 

**Tim** ([1:06:01](https://youtu.be/BFxkGdPv4F8?t=3961))
On mainnet shadow forks, though which are very different because mainnet shadow forks, there's like a hundred nodes that we control and like thousands of nodes that we don't and so that means that just like statistically, the peers we get, they're all on the wrong fork from the shadows forks’ perspective, which won't be true, it might be true on Ropsten then to like a 50:50 degree but not to like a 90:1 degree yeah.

**Micah** ([1:06:28](https://youtu.be/BFxkGdPv4F8?t=3988))
I hear you're saying my gut tells me that having two peer-to-peer networks that are incompatible with each other, that don't have a way to distinguish between each other is likely to cause problems that we may not even foresee until mainnet, or may not hit until mainnet and so I’m hesitant to just kind of yolo and just hope we don't run another thing but that's just a gut thing, I don't have any actual evidence.

**Marius** ([1:06:53](https://youtu.be/BFxkGdPv4F8?t=4013))
And that's exactly why we don't want to have to fork before mainnet, but before TTD hits, we want to have the fork after TTD head so that we have the split network post TTD. I would just say let's shove this discussion for now, let's just say we're not going to schedule a merged fork block on Ropsten, we're only going to do the TTD one, and I don't know, Geth never had issues finding a good peer and syncing from them so, yeah but we can like 

**Micah**
Sorry, go ahead.

**Marius**
Yeah no I'm finished.

**Micah** ([1:07:43](https://youtu.be/BFxkGdPv4F8?t=4063))
So the only reason I would push back on that a little bit and this is pretty weak is just that if the final solution we come to involves doing something other than just setting a number, like if we decide to write some extra code, I would really like to see that tested on Ropsten, and so not deciding until later kind of I feel like we'll cut out a handful of potential solutions whatever this might be.

**Marius** ([1:08:10](https://youtu.be/BFxkGdPv4F8?t=4090))
Yeah, we are not going to do anything except for setting this number.

**Tim** ([1:08:16](https://youtu.be/BFxkGdPv4F8?t=4096))
Yeah, I would not write extra custom code that we're testing super late in the process on like zero of the shadow fork, like the minority of the shadow forks. That seems like the most error-prone thing. Okay so any other strong opinions against doing nothing on Ropsten for now and seeing how it goes? Okay sold, so no fork next value on Ropsten, and then back to the TTD discussion...

#### [Difficulty Bomb Tracking](https://ethresear.ch/t/blocks-per-week-as-an-indicator-of-the-difficulty-bomb/12120)

...so if we say we want the releases for Ropsten two weeks from now, so that's like the week of May 23rd that means we and then we give people kind of two weeks to upgrade their nodes, so that means we want to like have the fork happen on Ropsten, the week of June 6th. We had someone on our team, Mario, not Mario Vega, Mario ? have kind of tried to estimate TTD's on mainnet and Ropsten for a while now. He tried a bunch of different models and this is just like a simple polynomial regression, and that seems to work the best, and it seems to work relatively well up to like a month, a month out, so I would just suggest that we go to like the June 8 value, which is roughly in the middle of that week, and this gives us this TTD value, which I’ll paste here. Anyone have an issue with that? We can make it look like a palindrome if people really want that, but otherwise also happy to just go with this estimate. I’ll also share the GitHub repo in the chat here, in case people want to have a look more. Oh yeah, good question, TTD is terminal total difficulty, it's the total difficulty value on the proof of work chain at which we trigger the transition to proof-of-stake, and so the one I posted in the chat here is the one that would happen on June 8, which is basically yeah, 4 weeks from now, and so it gives us two weeks for the client releases, and then two weeks for people to upgrade their nodes to a release that contains this value.

**Micah** ([1:11:12](https://youtu.be/BFxkGdPv4F8?t=4272))
So as was brought up earlier, scheduling the Ropsten fork far in advance risks someone trolling us and hitting it you know next week or tomorrow. 

**Tim** ([1:11:20](https://youtu.be/BFxkGdPv4F8?t=4280))
In that case we need to do a TTD override but I don't know that there's a way we can get around this, because that can be true like as soon as the blog post is out, if we give people two weeks anyways it's always gonna be the same problem. 

**Micah** ([1:11:45](https://youtu.be/BFxkGdPv4F8?t=4305))
I mean what one option would be to just use the override exclusively for Ropsten like we just say we're going to do an override we'll tell you what the TTD is, you know three days, before June 8. 

**Marius** ([1:11:56](https://youtu.be/BFxkGdPv4F8?t=4316))
I think that's really bad because then we don't exercise the real path.

**Micah**
I see what you did there, Marius.

**Marius** ([1:12:03](https://youtu.be/BFxkGdPv4F8?t=4323))
Yes. Basically that's exactly what we win yeah that's exactly what we did on uh what we do on the shadow forks and I think there might be a bunch of issues there.

**Micah**
Yeah okay you win. I can see. 

**Tim**
Andrew, do you have a hand up?

**Andrew** ([1:12:22](https://youtu.be/BFxkGdPv4F8?t=4342))
Well my preference would be to postpone it to the TTD to the 15th of June, but if like if everybody thinks that it should be the eighth, I’m okay with that, but my preference would be the fifteenth. 

**Tim** ([1:12:47](https://youtu.be/BFxkGdPv4F8?t=4367))
Anyone have a strong preference either way?

**Lukasz**
I have a weak preference for 15th.

**Marius**
I have a medium preference for 8th.

**Tim** ([1:12:57](https://youtu.be/BFxkGdPv4F8?t=4377))
Besu?

**Gary**
Weak preference for the 8th.

**Martin**
Weak preference for the 8th, but yeah guess as well so Marius already yeah.

**Micah** ([1:13:12](https://youtu.be/BFxkGdPv4F8?t=4392))
What are the reasonings for 8 versus 15, like why are people preferring one versus other? 

**Gary** ([1:13:21](https://youtu.be/BFxkGdPv4F8?t=4401))
From my perspective, the very first test, that wouldn't merge until June that's definitely getting us into territory we would need to push a difficulty bomb in my opinion. 

**Andrew** ([1:13:35](https://youtu.be/BFxkGdPv4F8?t=4415))
That's probably true but I don't think that pushing the difficulty bomb is that bad, it gives us more time to prepare a release, a better release and more time for testing, but I don't insist if the majority thinks it should be the eighth then its all right. 

**Martin** ([1:13:58](https://youtu.be/BFxkGdPv4F8?t=4438))
Well, I would I would agree but my view is that this is testing if it were I don't consider Ropsten in a production network it's a test network so therefore I think the sooner the better because it gives us better testing for when it's for the real thing.

**Tim**
Anyone else have whats 

**Lukasz** ([1:14:28](https://youtu.be/BFxkGdPv4F8?t=4468))
Mine is the same as Andrew, I still see work before us and yeah that's pretty much it. So more time we have to polish the release, the better for us but life is doable, and also I don't see a problem delaying difficulty bomb when we are already going to testnet, so if it's a short delay, but except it is a little bit additional work for and scheduling, but I don't see this as a that big issue, but that's just opinion that might not be correct.

**Andrew** ([1:15:11](https://youtu.be/BFxkGdPv4F8?t=4511))
I guess one objection against delaying the difficulty bomb is that it will imply that the miners will have to update and what if there is a revolt among the miners.

**Tim**
Right yeah, they do need to run. 

**Micah** ([1:15:34](https://youtu.be/BFxkGdPv4F8?t=4534))
Now so from miners’ perspective just play to the devil's advocate here a little bit, us pushing the difficulty bomb indicates that we are going to delay the merge which is good for them and so that feels like something they would be on board with.

**Andrew** ([1:15:52](https://youtu.be/BFxkGdPv4F8?t=4552))
Fair enough. 

**Tim** ([1:15:52](https://youtu.be/BFxkGdPv4F8?t=4552))
Yeah I can see both sides of this, and so okay, so if we did do like the June 15 rather than the June 8th, it also means I guess both for like Nethermind and Aragon, you also want to delay by one week, when we actually announce the releases right, because it's not just announcing the releases and having three weeks to hit Ropsten, it's more like we announced the releases one week later and instead of announcing those releases in two weeks, we announced them in three weeks, and then we hit Ropsten in two weeks after that. Is that correct?

**Andrew** 
Yeah.

**Tim** ([1:15:52](https://youtu.be/BFxkGdPv4F8?t=4552))
Yeah there's like a weak majority in favor of June 8th. Yeah I don't know, Geth, Besu do you have any updated thoughts?

**Gary** ([1:17:08](https://youtu.be/BFxkGdPv4F8?t=4628))
Still June 8 weekly held, I like the palindromic TTD after he's already put the effort in. 

**Tim** ([1:17:16](https://youtu.be/BFxkGdPv4F8?t=4636))
Okay, and Teku would also like the June 8th, anyway I think Ben you're the only CL representative left, if that's correct.

**Martin** ([1:17:28](https://youtu.be/BFxkGdPv4F8?t=4648))
How about Danny?

**Tim** ([1:17:35](https://youtu.be/BFxkGdPv4F8?t=4655))
Danny left. I think Danny favors, I can vouch that Danny would prefer earlier rather than later. I don't know if that's his personal preference or the aggregated preference of like CL teams, yep, so I think I would also slightly land on like June 8 and one of the reasons here is we can definitely upgrade the releases that like clients put out, and we've done that in the past even for like mainnet, if you look at the London blog post fork there's like a couple scratched out releases. So I think if there are going to be some clients and like most of them that are ready, and if Nethermind and Aragon have like a release that's maybe not like the one that they would prefer, we can kind of start with those and then if like a week later, Aragon and Nethermind have like an updated release we can definitely like just upgrade the blog post and communicate that, and I also think like if one of the things we do want to test is like people configuring their nodes, then if we do like, the sooner the better I think is good there, because we might find some issues that we're not aware of about just people running these kind combos, and it's something where like I think the fact that the release is like a bit more polished, probably is not like a huge deal breaker, so I, my weak preferences also I would rather get this into the hands of people to like try, to like combinations as soon as possible and then just like make sure that we also upgrade the release versions for Nethermind and Aragon as soon as there's like a new one, I don't know, does that generally make sense?

**Andrew** ([1:19:25](https://youtu.be/BFxkGdPv4F8?t=4765))
Yeah, its fine.

**Tim** ([1:19:25](https://youtu.be/BFxkGdPv4F8?t=4765))
Okay. Marek? Lukasz? Okay. And so, thank you Afr for the palindrome, , which I was too tired to recognize and so I’ll copy paste it here, also I’ll just share it in all core devs right now, so consider this the TTD value, I'll make it a proper upgrade to the Shanghai spec in the execution repo, and the thing that clients on the cl side need to figure out in the next week is basically the slot heights for, well basically the genesis for the beacon chain, and then the slot heights for Altair and Bellatrix based on this. Does that make sense?

**Marius**
Yes.

### EIP Discussions

#### [EIP-4938](https://eips.ethereum.org/EIPS/eip-4938)

**Tim** ([1:20:29](https://youtu.be/BFxkGdPv4F8?t=4829))
Okay thank you Marius. Okay. So there's three people who wanted to discuss EIPs that are on the call. I doubt we can get through all of them, but if we stay on an additional five minutes, we can give them each five minutes, yeah so first up, Felix, you had EIP 4938. 

**Felix**([1:21:03](https://youtu.be/BFxkGdPv4F8?t=4863))
Yes. So and this can be really quick, so this is pre-agreed. I just wanted to let you guys know that for formal reasons, we are pursuing this EIP, the EIP 4938 is about removing the GetNodeData message from the eth wire protocol, and we have discussed this extensively with all client teams that we are aware of, that we want to make this change in Geth, and we have been wanting to make this change in Geth for a very long time, and I can only really repeat what is in the EIP. We are set on making this change, because it will allow us to for example restructure our database to not store all of the tri nodes, for example by their hashes and we do provide an alternative to this protocol message in the snap protocol, and all of the existing users of Geth node data can be replaced by the messages in the snap protocol, so it is not but so can we just very quickly, can I just very quickly get from the client implementer some signal that this is okay.

**Andrew** ([1:22:22](https://youtu.be/BFxkGdPv4F8?t=4942))
Okay, from Aragon.

**Marius** ([1:22:29](https://youtu.be/BFxkGdPv4F8?t=4949))
I think Nethermind still uses Geth node data for testing.

**Lukasz** ([1:22:29](https://youtu.be/BFxkGdPv4F8?t=4949))
We are currently using it for healing. There is work being done to move to snap sync healing but it's not done yet. 

**Marius** ([1:23:01](https://youtu.be/BFxkGdPv4F8?t=4981))
And I guess Besu will keep it for their other networks.

**Gary** ([1:23:05](https://youtu.be/BFxkGdPv4F8?t=4985))
Yeah. Presumably we would be keeping that for, we should probably get back to you on that actually, because the snap sync implementation that we have is pretty solid, but it's not really production ready yet, so we probably want to discuss, before we have an opinion.

**Felix** ([1:23:29](https://youtu.be/BFxkGdPv4F8?t=5009))
So what should be, what I wanted to say here is that even if there is no need to implement the complete snapshot algorithm to use the snap protocol for this purpose. Basically, this is just for us like a way to say that we want to roll out this new protocol version eth 67 which will not have Geth node data. It doesn't mean that eth 66 will go away immediately, we will keep having eth 66 for a while because phasing out the protocol version takes a good while so all we just really want to do is basically move forward and define the protocol version 67 which does not have the message, and then later we will remove version 66 and then it will become unavailable. So for the time being eth 66 will be served by Geth, and I mean, I'm not sure, I guess all the other clients will serve it in the same way that they have been serving it already, for example, in some clients like Aragon, the message is not implemented, so yeah. 

**Lukasz** ([1:24:30](https://youtu.be/BFxkGdPv4F8?t=5070))
So question mark, when would this go in like in the timeline and when Geth no data won't be served?

**Felix** ([1:24:46](https://youtu.be/BFxkGdPv4F8?t=5086))
Well we can make some promises now. I mean, I guess, we would like to have it like in as soon as possible for us, it is really simple to, like in Geth, to make this change so we can literally just release like this protocol version next week. It doesn't change anything, it only changes that there's this new version available, and then removing the version 66 will be a bigger step, and we feel like yeah we'd be optimistic about maybe like the autumn or so or the very… 

**Martin** ([1:25:22](https://youtu.be/BFxkGdPv4F8?t=5122))
Yeah, not gonna happen before merge.

**Felix** ([1:25:22](https://youtu.be/BFxkGdPv4F8?t=5122))
Yeah, definitely not for the merge this is for much later. We just want to set this process in motion, we have been talking about this forever, and we just wanna, like, this is like the next step on the way toward removing this feature so yeah. 

**Lukasz** ([1:25:35](https://youtu.be/BFxkGdPv4F8?t=5135))
So in terms of defining the protocol as that, I’m fine in terms of like phasing out eth 66, could we have a guarantee that we have a discussion before that and?

**Felix** ([1:25:52](https://youtu.be/BFxkGdPv4F8?t=5152))
Yeah, it doesn't mean, it doesn't mean it will go away tomorrow. We are not we definitely open to discussing it.

**Lukasz** ([1:26:05](https://youtu.be/BFxkGdPv4F8?t=5165))
In terms of the days, because we are planning, we are actively working on it. I think we will be ready for the autumn to stop using Geth node data, not sure if we'll be ready to serve data in from for snap sync which is the harder one, but yeah so I’m fine with generally general idea direction. 

**Felix** ([1:26:34](https://youtu.be/BFxkGdPv4F8?t=5194))
Okay, so I don't know what this means in EIP terms, is it like, anything needed or?

**Tim** ([1:26:34](https://youtu.be/BFxkGdPv4F8?t=5194))
I guess can we just discuss that offline for the 

**Felix**
Well, yeah but okay. 

**Tim** ([1:26:47](https://youtu.be/BFxkGdPv4F8?t=5207))
Okay, no objections to the new protocol, we're not deprecating eth 66 now, yeah. 

**Justin** ([1:27:04](https://youtu.be/BFxkGdPv4F8?t=5207))
Hey yeah, this is basically just to clarify what Gary was saying. We're fine with the new protocol version, it's the deprecating of the old one that gives us a little bit of pause. 

#### [Proposal to add EIP-5022 to Shanghai #519](https://github.com/ethereum/pm/issues/519)

**Tim** ([1:27:04](https://youtu.be/BFxkGdPv4F8?t=5224))
And we can discuss that well after the merge. Okay and we can yeah we can discuss that well after merge yep. Okay moving on, sorry just to make sure we at least give other folks the opportunity to speak green lucid was the GitHub handle. I’m not sure who that maps to on the call, but wanted to discuss, get feedback on EIP 5022, which increases the cost for s-store when you go from a zero to non-zero value. Are you on the call? Greenlucid? Once, twice. Okay, I will post their issue in the chat here if people want to chime in eth magicians. One thing I did mention so that the issues phased for like shanghai inclusion, I reiterated that we've kind of paused this decisions there but then they said they would just like to get technical feedback on the EIP, so yeah folks who are interested can have a look there, and then last up, we had, I can't even pronounce this this handle belnv, hopefully I got it. Right, oh well, perfect. Walk us through your presentation. We can't hear you yeah yeah.

#### [EIP-5081: Expirable Transaction](https://github.com/ethereum/EIPs/pull/5081)

**Xinbelv** ([1:28:29](https://youtu.be/BFxkGdPv4F8?t=5309))
Yeah. Hi my name is Zainan Joe or Victor and then a quick presentation for the question, early feedback wanted for the team, so basically the proposal is to get an expiration in the payload and one question one valuable feedback I got from Mikhail is the potential denier of service attack if exposed to basic someone is possible to throw a very quick soon-to-expire transaction and get it propagate over the network and cause a denial of service attack. Now my question for the group, I know they're very…

**Martin** ([1:29:12](https://youtu.be/BFxkGdPv4F8?t=5352))
What does this expire by?

**Xinbenlv** ([1:29:12](https://youtu.be/BFxkGdPv4F8?t=5352))
It is expired by, its a block number that's like, I’m proposed that we add a new a field in the payload for a transaction, and for that block to be valid, all transactions has to not expire. So expired by is a block number requirement.

**Martin**
Yeah.

**Xinbenlv** ([1:29:33](https://youtu.be/BFxkGdPv4F8?t=5373))
And then so if that's a block number is 100 and then someone throws in a transaction within 101 with a high transaction fee and so it is possible that it give propagate over the network, but then soon to expired and then within 101 and 102 didn't get executed at all, and thro, and could that cause a deny of service attack? That's the first question and so I put a bunch of question here. First of all is that really a problem, because for me it's like, it's very natural that some of transactions become invalid in the network, for various reasons, and expired by is just one of the reasons it comes by not invalid and so the argument was that attacker can have very low cost to generate a crossed network attack by have a low expired by number specified, but for me, my first under, my argument is that it seems like, if they want to attack, there's also risking some fees, and so that's one thing, and the second thing is that I have some network layers of a proposal, and my question to the implementer of clients, to the client authors, is that whether not nodes are incentivized to adopt a counter-DOS approach at all, I believe they are…

**Martin** ([1:31:24](https://youtu.be/BFxkGdPv4F8?t=5484))
But they don't made a…an e proposal about expired transactions and I know this because I also made one like a year after and had forgotten that he had made one so there are at least two previous attempts on this. I don't think there's anything like dramatically preventing this like from a node implemented point of view saying that oh we really cannot do this because then we get lost. Yeah Micah may want to…I just think this has not been picked up because there have always been other stuff more interesting modifications from transactions that have been on the table and this has kind of been seen as nice to have. 

**Micah** ([1:32:30](https://youtu.be/BFxkGdPv4F8?t=5550))
I’m surprised you're here to say that Martin, because I could have sworn you were the person that argued fairly strongly that attack vectors from expiring transactions were a problem because someone can expand the network and be confident that they not have to pay for it and be confident that they won't have to pay for it, if they can avoid getting included within you know inbox.

**Martin** ([1:32:50](https://youtu.be/BFxkGdPv4F8?t=5570))
No, I don't think I meant that, so there are other transaction types which I rejected because for that reason, for some of the batch ones where you can do this kind of thing, but for expiring ones, I mean we already have right now the case where there are like big activities, thousands of people sending in transactions, but instead of them being expired, and can be rejected and flushed out, they just have to slow through the system in like days after this big event and they will fail, they cost a little bit but they just hook the bandwidth so yeah I think it would be nice to have expire. 

**Micah** ([1:33:31](https://youtu.be/BFxkGdPv4F8?t=5611))
I agree that transactions are super useful and I would love to figure out a way to get them in. My concern, which I thought was actually your concern, but I will say it as mine since apparently I was wrong there, is that currently, if you submit a transaction you have no way to purge it from the mempool and there are some people out there who have insanely large mempools, and can store basically everything forever and so if you force the network to propagate your transaction you are nearly guaranteed, you will eventually have to pay for that transaction, like it is it is never free. Like you will have to pay for that or some other transaction that replaces it later, but that's going to have you know that 12.5 increase, and so there's a very limited amount so given an account or a set of accounts that have just enough gas for one transaction each, you basically can spam you know once maybe twice, and then the fees start getting too expensive whereas expiring transactions you can spam quite a bit if you're really good at throwing transactions in the pool that are very unlikely to mine…

**Martin** ([1:34:36](https://youtu.be/BFxkGdPv4F8?t=5676))
But the nodes can always choose to not, if you see that this will expire in five seconds, it can just stop relaying it.

**Micah** ([1:34:43](https://youtu.be/BFxkGdPv4F8?t=5683))
Sure, but I mean you could just have a thousand accounts that each have enough gas for one transaction, and they expire in five minutes or ten minutes or something like that, and I mean if you're good with a base fee, you can you know look at base fee history and you can do a little bit of math and figure that you know it's unlikely the base fee is going to drop, you know because this is a Monday afternoon and Monday afternoons it never drops below 20 or whatever so I just set to 19 or something. 

**Tim** ([1:35:10](https://youtu.be/BFxkGdPv4F8?t=5710))
So sorry, yeah we're already a bit over time and so I guess if what's the best place for people to comment, do you mind sharing that in the chat as well? 

**Xinbenlv** ([1:35:29](https://youtu.be/BFxkGdPv4F8?t=5729))
Yeah the best way is to share on the yeah is magicians, which is also appear on EIP discussion too as usual. 

**Tim** ([1:35:36](https://youtu.be/BFxkGdPv4F8?t=5736))
Okay awesome, and one thing I’ll highlight from the chat. Lightclient had two comments about EIPs 4337, 3074, so it's probably worth to look at those and yeah see if they're like a good replacement, because like, Martin was saying you know even if there are no dos concerns, there's still like a high chance that there's just higher priority EIPs that end up taking most of the fork and 4337 specifically is not core EIP, so it means that basically clients can implement it and not require changes to the consensus protocol, and I’m pretty sure Nethermind already has support for this in at least one project I think.

**Xinbenlv** ([1:36:33](https://youtu.be/BFxkGdPv4F8?t=5793))
Yeah that actually answered a good question of mine which is whether we need a new transaction type or can we use to reuse the existing transaction tag and append a new one and it seems like if people want backward compatibility it has to be a new one so that some of them if they don't want to adopt it sooner then they can just avoid, like avoid seeing it, before using it.

**Tim** ([1:36:53](https://youtu.be/BFxkGdPv4F8?t=5813))
Yeah and yeah I would recommend Micah if you want to share your EIP number yours was basically that if I remember correctly it was like a new transaction type with an expiring transaction so that might be helpful to look at as well. 

We're already over time, so yeah I guess we'll wrap this up yeah thank you for the presentation as well this is the higher budget quality EIP presentations that we had, and yeah thanks everyone, yeah thanks everyone for joining. I’ve posted the TTD value in the all core devs chat so we can use that for releases on Ropsten and I guess we'll expect to put a blog post together sometime in the next two weeks and yeah and then we'll figure out all the stuff about the beacon chains for testnets on the consensus layer calls, if it's not already done before then. Yeah thanks everyone.
