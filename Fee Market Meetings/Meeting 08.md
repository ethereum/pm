# 1559 Implementers' Meeting #8 Notes
### Meeting Date/Time: Thursday  17 December at 15:00 UTC
### Meeting Duration: 36 mins
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/229)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=mCOfz50Wcmo&feature=youtu.be)
### Moderator: Tim Beiko
### Notes: Avishek Kumar

----
# Contents <!-- omit in toc -->

- [Summary](#summary)
  - [Actions Required](#actions-required)
- [1. Status updates from researchers and implementers team](#1-status-updates-from-researchers-and-implementers-team)
  - [1.1 Transaction pool management](#11-transaction-pool-management)
  - [1.2 Update on the large state testnet](#12-update-on-the-large-state-testnet)
  - [1.3 EIP-2718 transaction type for EIP-1559](#13-EIP-2718-transaction-type-for-EIP-1559)
- [2. Mainnet readiness checklist review](#2-Mainnet-readiness-checklist-review)
- [Annex](#annex)
  - [Attendance](#attendance)
  - [Next Meeting Date/Time](#next-meeting-datetime)
  - [Zoom chat](#zoom-chat)
---------
# Summary

## Actions Required

Action Item | Decision
-|-
**8.1** | Getting Besu, Nethermind and Geth onto our large state testnet, and scheduling a “transaction spamming” session and gather metrics from all three clients.
**8.2** | Adding EIP-2718 support to EIP-1559 once Berlin is complete
**8.3** | Updating the transaction pool behavior

---

# 1. Status updates from researchers and implementers team

## 1.1 Transaction pool management

**Tim Beiko**: Welcome everyone to 1559 call # 8.Yeah we have probably a lighter agenda than last time. So there's only been two weeks between the calls rather than a month. So, we might not last the whole time. 

First thing on the agenda was just status updates from the different research and implementer teams and first one there was transaction pool management. I do not know, Ansgar did you have any updates that  you wanted to share.

**Ansgar Dietrichs**: Yeah I can give a very brief update. So basically after the kind of this preliminary write-up from last time, we kind of took a step back I mean ofcourse I am the one
in the team currently working on this but then we also  for example we had a call with Martin from Geth earlier this week and we went through some of the details of the current Geth implementation. If some of  our assumptions were basically good and it seems like we actually kind of were a little bit off on some of the small details, for example turns out for the minor. There are actually some significant rebuilding of the sorting already ongoing after every single block and so it seems like that is less of an issue. Now for 1559 to just basically use a similar mechanism. So it seems like basically it is a little bit probably a little bit more optimistic or a little bit simpler than it looked two weeks ago. But yeah going forward so, the idea is if the next call is only if it ends up. Being in a month or so I would hope to basically have a full write-up including
some maybe some simulation work and so on done  like a proposal for how to do the sorting. And I think last time you were saying that it all looks like this should be very doable and I would like to preliminarily agree. That seems like some details are still to be determined but all should not be like sorting, should not be an issue going forward.

**Tim Beiko**: That is really good news. Thanks and it is great that like the Geth team is out or the get code base already resorts every block for miners that is really good news yeah.

**JosephC**: So what are your current thoughts at their ends are?

**Ansgar Dietrichs**: Oh yeah sure so, I mentioned the kind of the mining because that is where we are seems like we were a little bit off on the exact details of Geth. Although to be fair like again we talked with Martin. He is more of an expert on the memphis side of things. We also like when we want to reach out to the people within the guest team. Who is more like, responsible for the mining site but I am reasonably confident that this is actually not very correct. Yeah on the eviction side I think like basically the only change for now. Like that I had so far was that I think I am a little bit more optimistic on just basically using a very simple heuristic that might be very inaccurate but like just precise enough. So, we like it because again, for mining it is really just important that the top end of the memphis stays very precise and then if at the low end there is like some eviction that is not like not ideal ordering wise that doesn't really matter. So you can get away with very  efficient implementations like only resorting. Once every so often and so I think the main focus on the victim side really will be testing it. Like under a huge variety of different base fee behaviors. Just to make sure that under all of those it hits some minimum
Stability. 

**JosephC**: What is the accuracy? What are some heuristics that you are thinking of?

**Ansgar Dietrichs**: well again something basically where it is like a very simple way of
calculating some expected  future and effective minor mining tips. So for example you take the current base fee and then you take for example historically you always maybe the mempool  always keeps track of the variability  within the last I do not know 24 hours or something or it
could be a different approach but then you just do it very simple. For example you just do
like 50% of the current basically plus, like 25% of one sigma above and one sigma below basically just to give you some idea. Right again that might be as simple as that sounds like that might already be good enough that you have liked. It is not just the count base fee but you also
like take into account like the higher one and the lower one or something and then you just update that maybe even just once every. So many blocks and as long as you can do that efficiently and as long as basically that is good enough that like on the high end your sorting is
never is still absolutely like perfectly precise. But again I am right now not confident enough that this would work already. But that basically would be like currently, like one of my candidates for like a very simple heuristic that might be efficient but still good enough, yeah if that makes sense thanks. 

**JosephC**: Yeah that does make sense.

**Tim Beiko**: Yeah, cool anything else on the transaction pool management. 

## 1.2 Update on the large state testnet

**Tim Beiko**: Okay next up Abdel do you want to give a quick update on the large state testnet generator and where we are at?

**Abdulhamid Bakhta**: Okay, yes so we currently have set up the new testnet so, this will be a
profound testnet and the goal is to have a state comparable to mainnet. So far we have generated 100 million accounts and we are now using a smart contract and we aim to generate 100 million entries in this smart contract. And yeah when this will be ready we will share the url of the different nodes and the block explorer and the headset so that other clients can think of this new testnet and yeah that is pretty much. So, we have four nodes running and the generator is still running and I will share everything when it will be ready. That's it.

**Tim Beiko**: Cool yeah and I think for that once we have it up and once we have you know the testnet up and running on Besu and Geth then we get Nethermind and get syncing to it. I think we should probably just **schedule a time to then spam it with a kind of transaction and gather metrics from all three clients**. Hopefully we can gather metrics and it does not you know just fall over but if it falls we fix it and try again. But I think, if we have at least one or a few shots of like saying look we spammed the testnet for you know two hours with transactions and like the node stood up. I think that is like more than the worst case. We would see on mainnet because in two
hours the base you would probably go up. Like you know a hundred thousand x or a million x and it is just not realistic to even do such an attack.

**Ramil Amerzyanov**: Hi it is Ramil, I just do not join it. Sorry for being late.

**Tim Beiko**: No worries. Any thoughts or comments on the testnet.

**Nethermid**: I think it would be important to make sure that every single node is publishing transactions of their own. Respective transaction pools so we know that we can not only consume the transaction load but also that every single one can generate them.

**Abdulhamid Bakhta**: Yeah, so we have set a very low difficulty. So everyone can be a miner on this testnet. 

**Nethermid**: Oh! no not even it is a minor one thing but also the client can be a
source of broadcast for this. 

**Abdulhamid Bakhta**: Yeah that makes sense yeah 

**Tim Beiko**: And I think the tool is about I hope again. 

**Abdulhamid Bakhta**: Yeah you can use it on every client.

**Tim Beiko**: So cool so yeah so maybe when we schedule the things like every client
can kind of spam the network.

**Nethermid**: You know we have been using your tool already for spamming the network when we were working with Besu network on this current solution. So, we were pushing transactions to test that problem was reported before and it is all fine and we can broadcast.

 **Abdulhamid Bakhta**: Nice and yeah I will update also the web front end to add the list of the different nodes and the the type of the node and I will add if you give me some url of network 
nodes. I will add them to the front end so that the user can choose which node to send the transaction..

**Nethermid**: Perfect. 

## 1.3 EIP-2718 transaction type for EIP-1559


**Tim Beiko**: Yeah cool so, I suspect we will probably have the testnet filled up you know sometime over the holidays. So early January we should be able to share the information and then it might take you a week or something for people to sync to the testnet because it is big  and then yeah sometime in January we can probably run this kind of spamming test. Cool any other thoughts questions on that.Next thing on the agenda I think I just copied this over by mistake but like eip 2718 I think we should wait until after this testnet thing is done and then add 2718 support to all the specs. It would not change anything for performance but at least like
we will get the actual testnet data before we have everybody changing their specs. Does that still make sense for people?

**Nethermid**: Yeah sure we still want to run some transactions spamming after adding it but
Yeah, just a formality.

**Micah**: Do people in here have a preference for feelings about ssz versus rlp since
that's almost certainly going to come up again.

**Nethermid**: No preference

**TimBeiko**: The only thing I guess is on the last of course we talked about maybe doing ssd  as the dev p2p layer first and then bringing it to consensus. So, I do not have like a strong opinion but I would not want to go against you know the rest of like all core devs on like having ssc in 1559. Yeah if that is gonna be a blocker.

**Nethermid**: Oh actually sorry as for eip1559.  Obviously I would like to keep it as separated from other things that we are adding as possible. So, I am generally adding to 2718 and adding a z. I think it is a z itself may add something like two months delay 1559 sir. So, maybe for that reason I have a strong preference for rlp. I thought that you were talking about  2718 in general but yeah if 2718 is bundled with 1559 like it has to be with 1559 then I have a strong preference for lp. I generally have a preference not to
bundle eip 1559 with 2718.

**Micah**: Wait, you want  1559 without 2718?

**Nethermid**: Ideally yes.

**Micah**: Even though 2718 was going in Berlin

**Nethermid**: as I say I would like to keep eip1559 separate from the Berlin discussion. Building discussion can be delayed massively, I mean it  keeps being delayed. I want to keep eip1559 totally separate if possible. I mean obviously if you have 1559 already deployed then it will be.

**Rai Sur**: Yeah okay

**Micah**: Yeah so, it is I am like 98% sure 2718 is going to make it into Berlin and so which means that we will want 1559 to be 2718. And if 1559 and  2718 then we have to decide whether we are going to do what we said in core devs that talk about ssz again after Berlin and it is gonna that means that discussion is going to be around 1559. 

**Nethermid**: Generally target a1559 before Berlin and this conversation I would keep it like we do not have to think about Berlin because Berlin might be delayed. I mean I see what is happening there and there is every chord of call we are adding one or two issues that are highly contentious recently like as a zero p is. It will take time, the 2718 it will take time and people are not on board and they do not feel like there is so much of a push on Berlin. So I would just keep it separate. I mean on the burning calls like all core devs I will be pushing for Berlin to happen as fast as possible on the eip1559 calls. I would aim at pushing for eip1559 to happen as fast as possible and if both of those attempts are successful who can come very happily together with everything in place but I would not like them to wait for each other.

**TimBeiko**: Oh I think  that makes sense.I suspect that like we are coming towards the end of Berlin and there is a very high probability that it is ready to ship you know before 1559. That might be wrong but assuming it is not. I think then the path of least resistance is adding 2718 for 1559 because we will already have 2718 in the code bases to handle 2930 and not doing ssz because I think for ssz. Like Peter from Geth's point in last ACD call was we should probably do it on devp2p. we are gonna find bugs if we do it at the you know networking layer. we are gonna fix those bugs that will take six months nine months and then you know maybe like once that
is done we're ready to actually move it into the protocol or consensus layer. And I think that is fine. So,if for some reason you know there is a decision made on all core devs that we switch everything to see now then like you know we will have to do it for 1559 but I would not want to take the path that is like opposed to all core devs. Like if everybody's switching to ssz you
do not want to be like rlp and then slow things down and vice versa. I do not want to slowly
run down because we want to do it.

**Nethermid**: Yeah I mean when I say there is no preference for us as rlp. It is because I know that we already have it right but also know that implementing ssd and understanding it and testing it took me proper time and it was not a trivial task and I think that there is no chance it will be faster than like a few weeks on guest site to properly test it and implement it into the code base even if you have libraries for it. I mean okay unless unless you I am maybe I am not
thinking about the fact that prism has the go library for SSZ and it might be more general. Like because our approach was a bit more like optimize and make it not so reusable. So it might be that the Prysm library is very reusable.

**Ansgar Dietrichs**: Matt I was under the impression that you were currently working with the guest team together on 2718. Could you maybe give a very brief summary of what your take day is, what do you think, what is the timeline there? How does that side look?

**Lightclient**:  I feel like Berlin islocked in. It is just a matter of getting the client test that is tested and deciding on a fork block. I really think this is going to happen in the next three months which I believe is still going to be far ahead of 1559. I think the original point for the
question though was just discussing like. We decided to go with rop over sse for the berlin hard fork and this is a discussion that is going to come back up after berlin because it is a desirable thing to have ssc of the protocol and unfortunately the more things that we add in that relies on rlp. The more complicated it may be to do sse at some point. 

**Ansgar Dietrichs**: How like how much of luck inward would a decision for one for on the 1559 side for rlp, but as a cb so let's say we go with rp for now but then it turns out that may hard will already like we will basically want us to or will 1559  to arrive with ssc instead like how much per delay would that cause on the one four man side.

**Lightclient**: Yeah I do not really have a good feel for what and what it would take to like you know transition 1559 time from rlp to ssc. I think that generally we have complete control over these things in the protocol. The one thing that we are introducing as like an external api is how we sign 1559 transactions so if we sign those with rlp and by switched ssd that means we also
want to change how we sign then. That is something that would be very difficult to change because we would already start having wallets and external providers adopting that exciting mechanism.

**Nethermid**: So when you say ssz you mean even serializing transaction objects with versus z but it is interesting. 

**Lightclient**: Yeah serializing transaction objects and using the verticalization functionality to create the roots in the block.

**Nethermid**:  That is a very big change. It is a big change because it affects all the web free components, all the smart contracts that is. This will be like a massive delay if we go for it and you know now. we already have a method of expressing keep 1559 transactions in a traditional
sense with just like two additional fields and I feel like this change is far far from being significant for adapting the current processes. So yeah like ssc would be one thing that would probably delay eip 1559 the most from the current state of things.

**Ansgar Dietrichs**: Yeah so I think I would very much agree in the sense that I think 1559 should not try to basically be taken as an opportunity to also push ahead other changes together with it. So there is no reason why 1559 should also try to push ahead. As I see right if it is ready and as  the z is not then yeah of course we should not be part of it. we are in the unfortunate kind of position of course to have to make basically like preliminary decisions on what we assume.It will expect from 1559 once it is ready and so I do not know I think we basically have to try to keep like the effort minimal but it would kind of take either way to walk back on this decision. If it turns out that we made incorrect assumptions so I do not know for example for me. Right now seems like the max the maximum likelihood situation would
be that we arrive after 2718 but before ssc but of course could be either way it could be like that we arrived before even 2718.I do not know seems unlikely but possible or even after ssc. Again and  in all cases of course if that delays 1559 by months. That is not a good place to be, so Yeah I unfortunately do not really have a good solution but but yeah that is important to kind of
keep them. 

**Micah**: So the reason this keeps coming up is because while I agree with.I forget who just said it that it is better to not bundle things like get ssd in first and then switch transactions over to it. Historically that has never worked with ethereum, that I know of the problem, there is
a subset of the coordinates who do not like including changes unless they are needed for something and so adding ssz before ssd is needed. There is a good chance that means we will
never get ssc in and sse by itself gives us a lot of big wins down the road which we would like to have but we can not get that in until we have something to put it in with. And so no matter what I think that if we want ssa to go in eventually it has to bundle with something and to stress the point that my client made the longer we wait the more painful. It will be to do that because we will have more and more stuff. Particularly more and more things that are being signed by third party tools.

**TimBeiko**: And I guess before that is kind of a core devs discussion though because there is
not just 1559 involved here right. Like for example there are account obstructions is the other one. Right like so there is like this meta problem of like  where is the line for ssd, where do we want it to be and for sure wherever we draw that line is gonna slow down every other feature
by like. I do not know call it three months optimistically right and  but yeah I do not think like
we can do much at the 1559 level to change that right. Like we can say you know on the core devs called this is the stuff we maybe want before or this is the stuff we absolutely do not want before because you know it will be such a big piece of technical depth to deal with that it is not worth it. Yeah but because it  just feels like there is so many things that are coming in that might
touch that  we we probably want a higher levels solution than just do we do 1559 or this with sse or not,

**Micah**: Yeah that is sir. I am okay with not discussing here. It sounds the gist I got is that people are very hesitant on anything that will delay 1559 and I generally share that sentiment
and definitely appreciate it.

**James Hancock**: Yeah, just my perspective from trying to deal with some of these things and I know this is just coming from an opinion place nothing like knowledge or a fake place. But that there probably will be something that needs to do what you are saying Micah but it probably should not be 1559.

**TimBeiko**: To do what exactly?

 **James Hancock**: To put in we need ssc for this. They will probably be something where we kind of have to decide that we need it even though technically we could maybe not need it.

**TimBeiko**: The eth2 merge.

**James Hancock**: Yeah but then about 1559 would. It should not be the one to do that but it is a good idea to be thinking about what should be in the down the line.	

**Nethermid**:  Yeah but let's keep it then on the old core devs like our goal should be to deliver eip1559 and I think the best thing that we can do is to ensure that it is ready and tested for any of those scenarios like whether it is with 2718 or without whether it is with ssd or without and we have one solution that we are testing without those changes.And it means that we can move it all the way to the end where we have already tested with all the clients saying. We are capable of handling keep 1559 and this is the spec that we are working with. so,the people who build tools can already start adjusting their tools and we can show them also like two alternative paths that here is the simple path now. This is how you have to adjust the tools and these are the alternative paths. Pay attention to what happens to 2718, pay attention to what happens to ssz
because maybe you'll have to adjust those tools a bit a bit more depending on whether those go
before but people will be more prepared they will already start looking at it. Implementing the first version and I think overall everything will go together faster.

**TimBeiko**: Yeah that makes sense so tabling the encoding discussion for now. Was there I guess Barnaby, Thomasz and anyone else or Ramil do any of you have updates you wanted to share?

**Nethermid**: So they for because I think that we are planning the next call for 14th of January, So I spoke to Mikha will a lot recently and he was working on this analysis of the potential attack scenarios when you like not really attack on the network in general but just the attacks where you slightly modify the base fee and this is because we are exploring like the cost of manipulating the markets. If you introduce the gas markets to the equation and here is the lot of results already calculated with various different network parameters but was not ready yet to share it today. But he is very confident about sharing it on the 14th. So be able to look at these Jupyter notebook numbers and all these charts and show you actually how it behaves. when
you want to push the prices down or push the prices up.

**TimBeiko**: That is really cool yeah looking forward to seeing that. 

**Ramil Amerzyanov**: I would like to share an update about pull requests with the guest. so we review with the comments and yeah from Abdel hamid and we are going to start working on the
on it on monday.

**TimBeiko**: Cool that is great um and I think once those are addressed it might make sense to get like a more you know thorough review from the Geth team.I know that like basically the Geth team has shared it with them  but I think once we have the code in a spot where like it is up to date with the latest spec. Yeah it will be valuable to get their thoughts and I think one thing I believe joseph you shared this with me was that the Geth team would like to see it kind of split up between the consensus changes and everything else. Was that right?

**JosephC**: yeah yeah yeah to if 1559 could be yes  phased in two phases yeah one with consensus. Just the consensus changes and then the second one where the mempool changes and you know other non-consensus changes would be that was a suggestion from Martin, yeah
just to clarify. Of Course that is what you were saying as well.

**Ansgar Dietrichs**: Just to clarify so,it is not not of course about like an actual two-phase
approach but it really just is like a logical structure split into two pr's so they still would have to
arrive at the same time and are dependent on each other.

**TimBeiko**: I guess remember what is like the best you know. Does it make sense for you to
do that now? Do you want to rebate? Do you want to address all of the spec level comments first ? Yeah I think whatever you think is best to get to that spot.

**Ramil Amerzyanov**: Yeah so I think  we will update to the latest spec version again.

**TimBeiko**: Okay and then.

 **Ramil Amerzyanov**: Yeah we can look at splitting  yet into gprs. Actually it is not clear for me for now 100, how to implement that splitting but I think we can discuss it later on the chat.

**TimBeiko**: Cool, yeah that makes sense. Anyone else had updates they wanted
to share?

**Baranbe Monnot**: I just shared on the talk paper that my co-author has presented in a workshop recently. It is very preliminary work but it is kind of looking at 1559 as a dynamical system so trying to get some ideas on how fast it converges. What are the let's say guarantees that we can find and perhaps using that as a springboard to look at the more controlled theoretic
questions. well how fast should the updates happen? I know Tim you have sent out a call to people who might be interested and I think this work might be interesting to them as well and what I discussed also two weeks ago is a follow-up to Michelle's notebook on the transition. I have a pretty final draft. Just getting it the last review and I will be ready to share it either end of this week or next week.

# 2. [Mainnet readiness checklist review](https://github.com/ethereum/pm/blob/master/Fee%20Market%20Meetings/mainnet-readiness.md)


**TimBeiko**: Cool does anyone else have updates? If not I will just kind of share my screen real quick to go over to check this but I think we have covered a lot of it already. So just at a high level in terms of implementations. You know the same teams are working on it. Open ethereum worth noting that they have a job posting out to hire somebody full-time to work on
1559. So if you are a Rust developer and you are interested in working on 1559. Please apply to it as opposed through gnosis but to work directly on open ethereum. Aside from that just in terms of the open issues denial of service risk. 

Actually I have been thinking about the DOS risk more and I suspect that 1559 might make things better and not worse and one of the reasons for this is that today on the network. If you just spam the network your cost is constant for doing so, like you and if you are like a miner deciding to do the network. You know you can include your transactions kind of for free in your blocks. Whereas under 1559 what is nice like even if you were to spam the network and aim to not increase the base fee to keep blocks. Just 100 full the rest of the demand for the network. The base fee increases and that means your attack will get more expensive over time. Which is a property we do not have today and also it kind of blocks that hole of like miners being able to dust the network for free. So coupled with stuff like 2929 and you know just clients being generally more resilient towards the large states.I think it is not as big of a risk as it might have been thought to be. So yeah let's just quickly update there. It is not formalized at all but it is just like my intuition of how it would play out.

 **Nethermid**: Yeah so team it is exactly what Mikhail was working on. He was analyzing the cost of attack when you want to spam and make the blocks field by just publishing transactions with very expensive transactions and obviously very quickly all the rest of the network stops including their transactions and you are the only one who has to pay for that. Like today just to share some of the results that we have seen like the raising base fee from 50 to 500. Required some pretty solid  participation of the miners at levels of around 40 to 48 percent of total mining capacity and it was with some ranges of success ratio like between 01 and 02. So 20% of success with a cost of around half a million dollars for 10 times increase in gas prices. So yeah the pushing it up was quite inefficient and quite expensive,but also like it would be great to see how the network behaves if miners. Actually do not participate in this kind of attack but people actually push the transactions.

**TimBeiko**: Yeah looking forward to seeing that but I think this was me the biggest showstopper potentially for 1559 and I feel like we are heading to a spot where it is . It is not a major issue anymore which is great. So transaction pool management we already covered this.
So, you know we are working on the solution. I think we should be good there. The base fee update rule so like Barnaby just said I have been reaching out to different people to see if we can improve on it. I don't think this is a blocker for 1559. So worst case we just ship it with the current update rule and if somebody takes a year for somebody to spend time to come up with something better. We will update it in a future hard fork or when we go on e2 but it is not a blocker.

 In terms of testing we have not made a ton of progress there but I think it will kind of
resume once 1559 kind of visit more of the all core devs process rather than this side track. But we wrote Abdel I say we but Abdel wrote a couple of heaps for the Json rpc spec and you know there is more to do. It is not rocket science. It is just work we have to do. But I do not think  there is a ton of value in doing it now because of how early it is and in terms of testnets.Basically I think we are combining these last two into one and that were the last two things.We have not tested so just like a multi-client proof-of-work testnet and then a large state testnet so if we can  get the two of these done that will be great. It feels like in terms of rd you know there is a lot more stuff that is going to be coming. I feel like Tim roughgarden's analysis was like the last
big blocker that we had um and now you know. I am pretty confident we have done more  analysis of 1559 than probably any change that is you know has gone on to the network. And they all  know modular some small issues. Everything seems pretty positive and finally just in terms of community. Outreach  we have been a bit slow of doing another kind of round of feedback. I think personally I would do like maybe a more aggressive round of like reaching
out to projects once we have another test nets that's like more usable and that we can point people to and have some documentation for it because in the meantime it feels like the main thing people were asking us. On these calls was like when can I  try it out. How can I try it out? So, I would just wait another few months until we have something a bit more stable that we can share and that was the last thing on the agenda. The next call I had temptatively put January 14th because I think we have an all-core devs call on the week of the eighth . So it is the off week that generally makes sense for people. Yes cool anything else anyone wanted to discuss or bring up. okay well yeah thanks for making the time everybody.

**Abdulhamid Bakhta**: Thanks
 
**Ramil Amerzyanov**: Thank you

**JosephC**: Cheers



----------------
## Attendance

- Ansgar Dietrichs
- Abdulhamid Bakhta
- Ramil Amerzyanov
- Baranbe Monnot
- Micah Zoltu
- Rick Dudley
- Tim Beiko
- Tomasz Stanczak
- Pooja Ranjan
- JosephC

## Next Meeting Date/Time : Thursday  17 December at 14:00 UTC

## Zoom chat

11:00:43     From  JosephC : I can look it up

11:01:28     From  lightclient : Paul D.#9606 

11:15:19     From  JosephC : link in the agenda seems wrong https://github.com/ethereum/pm/edit/master/Fee%20Market%20Meetings/mainnet-readiness.md   (needs some login)

11:15:28     From  Tim Beiko : Argh, my bad

11:15:43     From  JosephC : (no prob just letting u know)

11:15:53     From  Tim Beiko : Fixed :-)

11:16:37     From  JosephC : ah thx Tim the fix looked like /s/edit/blob  (I just deleted "edit" in url and it alone wasn't the fix :slight_smile: )

11:26:24     From  JosephC : is there an "EIP" linking 2718 to SSZ ?

11:26:42     From  Tim Beiko : I don’t think so, no

11:32:29     From  Barnabé Monnot : Preliminary work on 1559 as a dynamical system, towards control perhaps https://econcs.pku.edu.cn/wine2020/wine2020/Workshop/GTiB20_paper_7.pdf

11:33:44     From  Ansgar Dietrichs : also, I think the split would just be a “nice to have”, so that the geth team can easily adapt the thoroughness of their review, given that the consensus changes are of course even more critical.
	
