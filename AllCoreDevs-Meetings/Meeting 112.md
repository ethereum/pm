# All Core Devs Meeting 112
### Meeting Date/Time:Friday, 30 Apr 2021
### Meeting Duration: 1:35:21
### [GitHub Agenda:London Updates](https://github.com/ethereum/pm/issues/302)
### [Audio/Video of the meeting](https://youtu.be/_QLDhNMwoe4)
### Moderator: Tim Beiko
### Notes:David Schirmer

## Decisions Made
| Decision Item | Description | Video ref |
| ------------- | ----------- | --------- |
| **1**   | 3529 being included in London | [4:40](https://youtu.be/_QLDhNMwoe4?t=271) |     
| **2**   |3238 Being re-written this week |  [40:30](https://youtu.be/_QLDhNMwoe4?t=2433) |  
| **3**   |3451 considered for London inclusion |  [44:26](https://youtu.be/_QLDhNMwoe4?t=2666) |  
| **4**   | Baikal devnet launched |  [1:16:00](https://youtu.be/_QLDhNMwoe4?t=4611) |  
| **5**   | New London infrastructure call |  [1:24:00](https://youtu.be/_QLDhNMwoe4?t=5074) |  

  
#### Moderator:
* Tim Beiko:
Hello everyone, Welcome to All Core Devs number 112.  Yeah we have a lot of London stuff on the agenda today as well as a few new EIP’s. First thing we had is under last call we spent some time discussing EIP 3403 and Martin and Vitalik said they had a new proposal for it and give it to something you wanted to do in London. We said we wanted to review this call and hopefully make a decision about it today so that has actually been formally proposed it see EIP 3529.

##### 3529 being included in London

* Vitalik:
 Sure the core idea behind EIP is basically that instead of completely removing gas refunds it reduces gas refunds if in most cases from 15000 to 4800 and the two exceptions for that are the self-destruct refunds which are still completely removed and the refund for a storage slot going to 0 when it started at 0 1 and so I got increase the one before and I think it said 19900 so the core idea behind this is basically that core idea behind this is basically that we reduce refunds to such a level that in order to get the refunds you has to spend the same amount of gas on that trade on that same slot at some point earlier in the transaction. Basically it means that like there's no way to get more gas out of a particular storage slot in a transaction that you put in and so gas tokens stop working and also the maximum amount of extra gas that you get out of execution is all so much lower. So still satisfies both of the original objectives of removing or restricting refunds but it has the benefit that it still maintains a very substantial and said actually clear storage and not just replace values with 1 instead of 0. 
* Beiko:
 Got it thanks anyone have thoughts/comments on the EIP if they wanted to share. So no strong opinions, I guess, on the last call it seems like people were generally favorable towards this idea and into the London is that something that people would still want to do I don’t know some of the teams have thoughts on this.
* Piper Merriam:
 Yes, in favor yes, I was just saying not a client team but in favour yes.

* Tomasz Stanczak:
 I would try to avoid it for London unless Martin is generally suggesting this is needed for security. I like for just for the sake of removing this token. I don't see the need for that now but if that's important for security of the gas, sorry, the low gas limit elasticity and this unpredictable size is then I would go for it.
* Martin Swende:
 So I can't really say how important this is for block electricity and how bad can service issues could be with the doubled capacity. I don’t want to Cry Wolf too much I do think it's a concern I am familiar with gas naturally. I assume that there would be denial of service issues for the client I think. It's good to do this in like conservative gesture but I also want to basically set up my personal main motivation why see I this is important is because I think it's good if we get rid of this gas token because I believe that gas tokens are used to just mend little bit instead of picking some cheap transaction and this drives up the transaction prices and closest bad UX for users and that's really my primary motivation. I'm for it I don't want to speak for the gas team though. Peter what do you think?
* Peter: Unintelligible 
Tim:
 Peter you sound kind of like a robot your audio is choppy.
* Vitalik:
 I'm still getting Echoes from someone in there by the way.
* Rai:
 it's Peter I think. 
* Tomasz:
 I think Greg is the only person not muted.
* James Hancock:
 Doesn't gas tokens also contribute to state bloat more so the longer that they're there when we don't need them wouldn't that be adding additional pressure to the state that we don't need? 
* Martin: 
yes that is one of them, it’s a UX problem, I think gas driving the gas prices up but it’s also a state management problem.
* Piper: 
Seems like we've got two decent reasons here for going ahead and including it in London so I just wanted to add for some. It's enough just including transaction because you can always sell gas tokens so that’s another problem so that miners can just decide not to include transactions and this is actually a self-reinforcing problem because then blocked congestion just goes up and that just drives gas prices up. Its actually it is worthwhile to mint gas tokens because you can extract more value from the network end of the same time you'll raising the gas prices so your gas tokens become even more valuable so it’s kind of a perverted thing to leave that in. All in all, I think the biggest problem (unintelligible) block elasticity having the potentially 2x blocks and it hard for me to reason about it. For example if somebody were to ask can we raise the estimate and we always have to think about the worst case scenario and since refunds allow us to 2x the gas limit it doesn’t make sense I mean we can’t raise it to 20 million simply because that would mean 40 million .Its much easier to have these conversations about raising the gas limit if you know that gas limit means a certain thing and not potentially 2x. I guess last but not least what I wanted to mention was traffic but ill just go one step further and see that I think we’ve hinted at it quite a bit over the past years that the Ethereum network isn’t that particularly safe from a determined denial-of-service attack and  Berlin included EIP’s that made those attacks very un-probable. We’ve got included snapshots which again made those attacks super un-probable. Details which we’ll hopefully do in about two weeks but in essence we’ve been trying to push towards making block sizes deterministic and state access more meaningful for a specific reason so it's it wasn't really just randomly trying to make things. Personally, I would really strongly suggest we go towards this but we can get you guys more information in two weeks and then you can make up your minds.

* Thomas:
 There is one thing that I wonder if you take into account. So currency of lots of gas minting happens and 0 gas prices as the miners fill the blocks with gas minting and also any gas miners have to do that to low gas prices right which means that's in the end of time so if it went after we introduced to get EIP 1559 witches in London anyway we'll have base fee so actually minting gas will be no longer viable because you’ll be burning the gas so miners will no longer be able to simply fill the blocks with gas minting because they would have to pay the base fee and they would generally raise the base fee so that would contribute to them the revenue is falling probably and also I’m not even sure if there is enough of the gas stored in the gas tokens to provide any substantially long attack on the blocks. So I think it might not be necessary at all because of the EIP 1559 and basically it will simply die out.
* Piper:
Thomas still having trouble understanding the perspective here you're wanting to just do this later is that the intention?
* Thomas:
No I think that it may not be required if the motivation is that.
Piper:
What about state bloat?
* Thomas:
If gas minting stops be viable after EIP1559 because of the burning of the base fee then we don’t have state bloat because it simply doesn’t happen anymore.
* Piper:
What about cleaning up the EVM in general and just being able to reason about the gas limit better and that gas tokens are an unfortunate side effects of refunds and that refunds aren't an effective mechanism and that getting rid of them in this context in the EVM makes the EVM easier to understand and reason about.
* Thomasz:
Well that was not raised as a motivation so far obviously for the future implementation that sounds good but I think there will be lots of other cleaning and changes that will happen as part of the merge that we cannot really predict that this particular change is slightly rushed for London. This particular change taking to count all the other work on stateless Ethereum.

* Piper:
Last question your opposition is it strong enough that you want to change all of our minds or you voicing your opposition but you're okay with things going whichever way?
* Thomasz:
 No it's slightly more towards neutral as I said like I would listen if you if your think this is for the security reasons that's definitely I'll be convinced. what I'm not convinced by is that is if it's targeting the gas token then I'm not convinced that all the this is needed also because of the basic if it's for security purposes and if it's kind of analyze then we can show like how it leads to that security issues then then definitely I would like to included.
* Peter:
 I'm I really think that we should get rid of the merge we should do change this incremental.
* Piper:
 It sounds like we don't have a strong point of contention here there is definitely a worst-case denial-of-service scenario here where it is possible for this to muck with the total amount of gas used in a block and I don't think that anybody made this specifically to get rid of gas tokens it's more focused on the affect the gas tokens can have and then there's a bunch of other beneficial side effects so anyways just contextualizing this discussion it sounds like we don't have a strong disagreement here and that we do have people who are strongly in favor of it 
* Tim:
Danny I think you had your mic unmuted for a while?
* Danny: 
so there is a relatively new issue with the miners minting 0 fee gas tokens and yes that would be changed after 1559 because they would have to burn but that's a relatively new exploit and that's actually probably pretty dangerous exploit but I don't think it actually changes the other mechanics of 1559, would be potentially profitable for like use case feels low for people to be sold.
* Vitalik:
 Even today when miners are making zero fee transactions they’re not really zero fee. They are paying opportunity cost so they're willing to pay opportunity costs down they will be willing to pay the base fee when its low.
James:
 That line will exist somewhere even if it might be less or more than we think it might be when the base fee happened. I think that the economic argument against the base fee being reason not to make (unintelligible) since I don't think that'll hold up very well.
* Beiko:
 I'm curious if I don't know anyone on the base team or open Ethereum team has an opinion on this?
* Rai:
 I like Piper's point about just keeping in mind and the relative ranking of the reasons for and against that the primary 1 is that might eclipse all others is just to think about the reasoning of the max block size estimate and then beyond that if the set on that then you can kind of use the other is the tiebreakers.
* Beiko:
 anyone from open Ethereum and if not though I’ll go to the raise hands. 
* Jochen:
I think it's only me from the open Ethereum today. it's really that simple of a change it would not make to worried.
* Beiko:
Ansgar and then Thomas
* Ansgar Dietrichs:
yes so I was basically just curious if you like do we all expect that the that would EIP would have a significant impact on the safe gas limit or naively to me that it seems like at least to the extent that we are limited by peak throughput. EIP would allow for up to a 2x increase of the same gas limit because we would only kind of like a peak of 2x and not 4x and of course we might be limited by other things. I’m just wondering because to me if it really makes a big difference for the safe gas limit then I personally would be strongly in favor of it but if it is more complicated and maybe doesn’t have any impact on the gas limit then. I’m curious if people generally agree that it has an impact on the safe gas limit of if there are some reasons why it might not?
* Beiko:
Thomas?
* Thomasz:
 just to come back to some arguments are when we were talking about all right when we were talking about the cleaning the EVM on so this particular EIP doesn't clean the EVM on because it just changes the parameters to reduce it which means that cleaning of the EVM doesn't happen at all with this DCIP so Piper maybe.
* Piper:
 It's a precursor to cleaning the reason that the EIP was changed to not fully remove them is so that we don't introduce a perverse incentive for smart contract devs to 1 instead of zero. The intent is that when we move to state expiry, we fully remove refunds this was sort of a compromise to make sure that the smart contract developer correctly align
* Thomasz:
 so I think I can really talk about this particular EIP and it doesn't clean EVM and it's like we had this conversation about this step toward something with the EIP 2315 weren't actually later doesn't really make that much change let's just two steps and the difficulty they also assume that if the miners mint a lot of gas tokens nowadays then those attacks on the block with the double block limit it is not only opportunity cost because of raising the base fee their revenue will fall significantly after such an attack because of the bay fee growing their opportunity cost will be huge in the case of such an attack and attack should dissipate quite quickly that's my intuition. 
* Vitalik:
So one way to contextualize this discussion I think is that there is an EIP maybe let’s say for example a 30% chance that the block size barrier issue is important enough stuff is like a really important and maybe a 70% chance it doesn't matter much there's also a 30% chance that getting rid of gas tokens is something that's going to be really valuable and not save you 70% sure I have not heard any arguments that it's going to that this could be actively harmful right so two 30% chances of solving significant security issues is still worth the fairly small number of lines of code that the EIP contains at least I think. 
* Beiko:
Peter I know you came up you came off mute a minute or two did you have something like the add. 
* Peter:
Yes I just wanted this discussion to move tangentially over into management and miners minting gas tokens but that’s not the priority. I’m looking to keep the size of the block deterministic and not allow doubling of it all of the sudden so that’s the primary goal here. Piper:
yeah it's worth saying that you can do that without gas tokens.
* Thomaz:
 I mean you would have to have a significant storage to unlock to execute such an attack for a longer time I mean I see clearly massive support for this one so it’s totally fine. So just to claim the arguments against why am I even talking about it and potentially even suggesting it. there are two reasons so I think they'll be some additional phasing and testing efforts that which may lead to potential delay of London making it slightly harder to start Network upgrade to introduce. The second one was historically the changes to the gas calculations were potential risky for the consensus split which I think this is also the kind of risk that we want to avoid. So these were the only all new arguments I had against this is just a question with the proposed reasoning in favour of is correctly calculated the detail calculated but I agree with the statement that there is a 30% risk of the this a negative consequences then yes it should be introduced however this exists now but here is the statement that the EIP 1559 because of block elasticity can cause some damage but it's also it's in the end of case of longer attack is to resolvable by miners decreasing the block sizes and so sorry I won't be making more statements about this one. it's it really makes sense also lots of things that you say here.
* Beiko:
thanks for sharing Alex is your hand up to related to this EIP.
* Alex B:
 yes just a quick question maybe this has been discussed since the refund for self destruct is removed that means at least I believe the chi and the GST 2 gas tokens they would make no sense to be self destructive anymore and I wonder if I'm assuming to see EIP today except it today and between now and the London hardfork itself will the time be enough for people to actually I guess they still will keep using the gas tokens but at some point maybe they will start to destroy them in order to reclaim the refunds before the hardfork happens and I wonder if this actually going to happen and whether the time is enough or will end up having a lot of stuck gas tokens because they are not economical to be retained anymore and whether the goal is that state expire going to deal with those remnants
* Martin:
 I am I don't know burn rates of these I would like you expect them to be more not minted anymore but mainly only burned from when we decide to go see but I don’t know the burn rate and it’s not necessarily still what they will stay on forever. It might be worthwhile for someone to just pay and get rid of them I don’t know that depends how many there are I think that Marius checked into this a couple. There is some public chi token tracker and if I recall correctly, it’s on the order of three or six million such contracts right now. If anyone else has more info about how many there are and what the burn rate is feel free to jump in 

* Piper:
other part of your question about like kind of do we expect state experts to clean this up yes and in theory state expiry makes it not matter at all if they constructed or not and it shouldn't make a difference either way.
* Alex B:
 Yeah I don't have anything to say it was really just a question to you to understand this part
* Beiko:
 got it the other argument that you mention Thomas was around testing so I guess just two things I would want to check as you know in terms of implementation would all client teams feel like this is something they can Implement and in terms of testing they know is this something we think we can test properly over the coming weeks and we feel comfortable including it in London?
* Martin:
so if I can just speak quickly of testing we have performed so we have the test written for 1283 and 2200 which did test for gas changes to have quite a lot reference test covering  modifications to we have particular Fosters written to try out various combinations of storage changes and doing calls and source changes which were written or reused when we wants to EIP 929 so I think the pretty good and pretty easy to just use the one that go to have with a new rules and thought I don't think there are any explicit new testimonies 
* Beiko:
got it thanks and does anyone I guess on the client side think like they could not implement this in time for London timeline that we had.
* Artem:
I don’t think that it is hard to implement. 
* Beiko:
then in the chat Micah has a comment about like the Chi mint said it would take 80 to 320 days to get rid of them is that based on like that the historical how much get the burns per day. 
* Micah:
Yeah just looking at that first one likes it looks like on any given day the economy burns 5K to 20K, very rough ballpark.
* Beiko:
 So at 20k that’s 80 days from now basically July 19th which is you know five days after when we said we wanted to fork on maintenance. you assumed I guess you know if people really wanted to burn them they could probably have the rates go up.
* James:
are there are days where it is higher than that to that happens or so it could be like that that being the general that isn’t the limit.
* Micah:
 keep in mind that the people who are burning these are almost exclusively boss and the bots and 1 inch users and fairly stable the bots come and go in terms of their volume based on what opportunities are available and so those days where there's lots of cheaper usually because there's some EVM opportunity the bots really trying to leverage heaveily and so I don't know that the broader Community actually has much control over the burn rate it's more like when the opportunity presents itself they burn and when it does so they don't burn like they're just burning all the time for fun.
* Beiko:
 got it well yeah.
* Peter:
I guess your opportunity cost will go up as the gas tokens go down in value eventually it will be worthwhile to always burn.
* Micah:
 I'm not convinced for that because they bots generally will always burn Chi because their goal is to get there or they're like high-value transactions when they're doing gas working with and they’re putting gas prices at thousand they want that to have the lowest gas possible and they're willing to pay whatever the charge going rate is tokens for that transaction like the cost of doesn’t matter to them what matters is getting their gas down I Peter:
 I got it so you by opportunity cost if the chain is idle I mean there aren’t insane trades to be made then there are essentially the bots will be idle. 
* Micah:
Exactly they’re not going to be doing anything they aren’t going to be doing anything.
* Beiko:
Ansgar you have your hand up?
* Ansgar:
I just quickly wanted to ask and this could be like naïve or anything but basically one possible alternative to EIP that I just to articulate was what if after EIP1559 you don’t have the refund. Basically, the refunded gas still counts against the block limit so basically refunds can’t have any elasticity kind of properties anymore. So you have a transaction with 200k gas usage but like 100k refunds then instead of like only counting 100K block space it accounts for the full 200k and it has to pay the tip part of the transaction fee for the full 200k in order to make miners indifferent of including it but it still gets a discount on the base fee. It would only have to pay like, in this case, 100k on the base fee that would be just in case people are still kind of feeling like maybe they don’t want to think about this EIP more and only included in the future block after. This might be a very simple change that would get rid of the elasticity problems while keeping most of the properties of refund savings intact. I could be missing something here but maybe this would be practical kind of interim solution while we discussed like a good long term one.
* Peter:
I don’t see a problem with nuking out gas tokens. I don’t see that as a problem needing a solution.
* Piper:
Yeah it doesn’t seem like we need an alternative solution but if we do we can look at this. route. 
* Vitalik:
I feel like we’ve been looking at routes for long enough and we need to just decide. 
* James:
This is the fourth iteration of EIP already. Which has been great the progression has been awesome.
* Micah:
What do you think our timeline on state expiry is since that seems to be a interrelated. Are we talking 2 years or 6 months after the merge.
* Vitalik:
1.5 to 2, I don’t know.
* Bieko:
So another thing worth noting is we have to make a call I think today otherwise we’re going to be pushing back the London timeline. Yes, there might be another feature fork after London but we also said on the last call if the merge was ready we would do the merge before this feature fork and given that this is a solution that helps with the block time consistency and this is also something we’ll want for Eth2 it might actually be the last chance we get to make the block times a but more predictable before we have to merge. If this is something you know we need and you know that it solves two or possibly more 30% risks I would favor including something today because otherwise we just might miss the London deadline and if we missed the London deadline then we might miss the merge also and this is probably not the type of change you want to include right when you’re doing the actual consensus swap
* Piper:
 so maybe the open question here is would anybody else like to argue against including this in London.
 
 ##### 3238 Being re-written this week
 
* Beiko:
So if there is no opposition we include it. Last chance for anyone to step up. Okay great so included. I know this has been like pretty long discussion but it was the biggest thing on the agenda other things should be should be simpler to get through so moving on at the next one so just a difficulty bomb delay we agreed on the previous call to have it around December 1st but I asked EIP to be modified and in the champion is on vacation so I don't know what's the best way to go about this do we can somebody else submit a PR to the eve should we just have a set different difficulty bomb EIP that we sets the date to December 1st I just want to make sure we actually don't like forget about this and come to the spot where we need to actually set it on mainnet and we don't have a number
* Micah:
 Is this person permanently on vacation or temporarily on vacation?
* James:
 I pinged them, they didn't answer which is reasonable because on vacation but I don't know 
* Pooja:
it seems like he's unwell and that's the reason he is unavailable to answer. 
* Danny:
I would expect maybe to not be able to get in touch with them for now and maybe an easy solution is to copy the EIP with the new data and actually put him in the co-author on the new one. 
* Micah:
yeah I think that would make sense just have a new EIP so we can merge to it it's obviously I give credit as an author and targeted December 1st does anyone want to do that?
* James:
 Is the number already been calculated for what we would need to do for that. So that needs to be done?
* James:
 So you need to calculate basically by how much do we put back the bomb so that it goes off around December 1st
* Beiko:
 if no one is no one's interested I'm happy to take a stab at it and work with folks to get the number.
* James:
I can look at it and then I'll ping you if I start if I have troubles before next week maybe before it's over next week I'll look at it and if I'm having troubles on make sure 
* Beiko:
let's do that so James. 
* James:
by the end of next week like Friday or the week after.
* Beiko:
Okay sounds good and Alex you have a comment in chat about December not being too ambitious. We have discussed this on previous call and the reason was we expect to either have the merge or Shanghai ready before December we still don't know which one will come first and we wanted to keep the bomb as a forcing function to do that.
* James:
 Basically we would have the fork before then.
 
 ##### 3451 considered for London inclusion
 
* Beiko:
Exactly firmly before then and we have also agreed nobody wants to have a fork over the holidays so it’s like if you put it on January 1st then it’s basically the same thing because we’re not realistically going to fork on December 20th or something like that. Okay so you will follow up with a new EIP that supersedes the previous EIP. next up was EIP 3541 so we were discussing a bit on the cordev’s chats this morning. Alex do you want to give a quick overview of the EIP.
* Pawel:
We agreed I will try to do the overview of that if that's fine with everyone and so the bigger picture of that is Ethereum object format which is proposed as EIP 3540 and this introduces some kind of container for EVM code so it adds some structure to the EVM code. it's not it's not a sequence of bites anymore and important things about this one is that it starts with some magic sequence of bits which is a prefix of this container and the second field there is the version number so the first feature provides is versioning of the EVM code so it has some benefits over previous proposal that workers getting the same thing which doesn't require the change to Dad because all of the information about the person would be keep inside the bit code and second most important thing about that we were together with this object format we also introduce validation of the code and all the other codes deployed on the blockchain starting from this EIP I mean EIP that introduces the object format will be will be validated and we have some guarantees that in the state the object that is in the state is already valid. One more thing about Ethereum object format the version first which also is part of the EIP is that in the first version we want to introduce code and date of Separation so this is kind of alternative to the beginning data instruction proposed in other places. I think I should mention that the exact feature set of the first version is up to discussion and tuning so that's about this Ethereum object format as a goal we’re aiming for and now what is proposed for London. For London we propose starting with that to have these guarantees about contact code validation and deploy time we discovered a way of doing that in the like the most Backward Compatible Way by doing the deployment of this into two hardforks and because we need to come up with this this Magic sequence of bits  by creating EOF prefix and in the first hardfork what you want to do is the freeze the first byte of that  so no longer  contract starting with this byte are allowed to be deployed after the 1st hardfork and the first harfork which is proposed for London which is EIP3541 and after this happened will be able to find the sequence the remaining sequence  of this prefix because mostly that the search space is freezed at this point. Hopefully I more or less explained the situation and did that so that's why we wanted to include the first change as soon as possible so later deployment with the full feature set it's not blocked by some other dependents. EIP3541 we think it's relatively simple it's mostly at when you create a contract you need to check if that the codes to be deployed doesn't start for this special byte this is not used correctly and if this byte has this value you failed the contact creation and that's mostly to change that has to be implemented. Lastly I did some I guess like proof of concept implementation and based on that we generated consensus test in the format of this official repo and that is all from me on this subject if anyone else from the from the people that worked on that wants to add something 

* Vitalik:
Yeah, just one quick question or request for confirmation this EIP it that youre proposed that your proposed like that you are surely soon is does not require any kind of agreement on what the structure of this and structure EVM code is actually going to be.

* Pawel: 
Yes I think Martin has some valuable comment about that today on the chat. It doesn't have to be even this you have for much of the other options that can go to go later on.
* Vitalik:
 right my strategy longer-term strategic concern is that we are going to or at least I think we wants to do code verticalization at some point and code verticalization introduces some new criteria in terms of like how we were in what way it's good to optimize the structure of EVM and that’s something that the structure format should be designed and so just even if just for that reason it's probably good to not rush into it like this making decisions on the code format that we can't go back on to quickly.

* Martin:
Yeah so it is good points and this first step is a good first step if you want any kind of structure no matter what they look like.
* Piper:
 got it I’m definitely in support of this. I’m wondering if you guys have given much thought into how this ends up with interplay on test nets and things and whether or not you guys see us ending up with like meeting different prefixes for testnets or things like that
* Martin:
 yeah so it's just a matter of after this has been rolled out on all testnets that we know of we just find the best prefix and at that point we can choose to say well we extended with three bytes or a even four bytes because someone created 4 million contracts on ropsten or or we may choose to say let’s screw ropsten over and start a new testnet because we can choose later on if you want to make it longer magic or we can live with some testnet being wonky and we can ask if there are any public or private networks that have any anything if they have any concerns about particular validators it's something we need to solve later
* Piper: 
I don’t see it as a strong concern, I was just wondering if there’d been consideration put towards it thanks.
* Beiko:
Paul you've had your hand up for a while?
* Paul:
 in general I'm in favor of the big picture the code verticalization that the Vitalik mentioned it brings some Global properties then there has to be design interactions with these various features that are coming up including code verticalization the other one is in particular I want to say there are code verticalizations is local if it's everything is local and all decisions are made locally but when we have Global properties like you know versioning and offset some things like this than this has to be resolved soon and the other interaction we have with this one is address extension to 32 bytes which gives so this could be become redundant I don't know but I would like some may be mentioned somewhere about how this interacts with address extension to 32 bytes which gives us versioning for free so this could become redundant. I don’t know but I would like some mentioned somewhere about how this interacts with address extensions to 32 bytes that’s it
* Beiko:
Alex you had your hand up?
* Alex B.
Yea I wanted to respond to what Vitalik said regarding localization and meralrization was actually considered. The current proposed format which is not even proposed for London but the currently proposed format has headers in front so that would mean that the first shank would have the headers and one of the reasons we prefer deploy time I mean contract creation time vs. execution time validation is exactly code mercalrization because if you would have execution time validation you would always need to have all the chunk so which render mercalization moot. Regarding the address extension address extension was actually one of the motivations to this whole work with the seat expire proposal an idea is that it would be easy to disallow old legacy code for new addresses all together there is a good interaction with these proposals but as it was stated address extension and state expiry might take upwards of two years and it would be nice to make some progress on this topic before that
* Beiko:
 I'll be curious to hear from the different client teams seems like obviously we just barely got another EIP in the London I understand this is a small change, but it feels like we are coming out in small change after small changes im curious what did the different client teams feel with regards to including this in London is it smaller nothing valuable enough and I guess future proof enough that it's worth it? So maybe I can go does anyone have a strong preference either way or are people mostly neutral.
* Martin:
 So I have been apart a little bit in defining this this so I this partial but I am a proponent don't know if peter is as well 
* Rai:
can it be a nice to have like is it something that we I really need for a London or we could at least have it out of the backlog like a signal to the client's height of teams OK work on these other ones and then if there's time then work on this one
* Beiko:
 I don't think so because assuming we don't want to delay London we basically with you to choose blocks on the next call and ideally we probably want to be pretty finalized in the implementation before then. So I suspect we probably need to tell people either it's in today and you have two weeks to implement it or it's not in unless we delay London then but I think we've signaled pretty strongly that we don't want to do that 
* Micah:
Do any clients think that implementing this will be challenging in any way.
* Rai:
I think it should probably be fine.
* Martin:
 I believe so too because I suppose a lot of other changes there are only very few places where creation actually happens so this change is really localized.
* Peter:
 Yeah I guess so the other thing that in order to continue defining and working on these specs you kind of need to reserve so I guess I'm kind of put some urgency to get it into London because if there is a follow up EIP this one is enabled for London.
* Beiko:
Any thoughts?
* Thomasz:
No comments I didn’t have enough time to analyze this in details. 
* Rai:
So is it the end of the world if it doesn't go into London I agree that it is a is a good step and it makes sense but could it not just going to the next one.
* James:
 I think the nuance there is that for most of the EIPs and next one means like where the features would happen would be over just going to move to the next Fork but for to do that for this one we're actually pushing it two forks further because we still have to have these interim steps
* Rai: Yeah I understand my question still stands.
* Paul:
 I think that if it doesn’t get into London then a case could be made later that this is redundant with address extension because address extension gives us versioning for free so I vote in favor of getting it in the London otherwise it's going be interactions I think. It’s good anyway even if there’s redundancy. It’s good to decouple addresses from the byte code and then just have a piece of byte code you know and how to execute it without having an address so I think it's useful anyway so I vote for EIP London but I know that my opinion doesn't mean anything. 
* Rai:
you can still decide to decouple them down the line you can understand that address extension can get it get you it for free and chose not to leverage that. 
* Alex:
if you allow comment on the address extension it means that intrinsically you can introduce new versions on each epoch and you would tie the allowed versions to epochs I guess that's the way it would work but the problem is you mentioned is that you need to know the address in order to execute the code you cannot execute a code outside of knowing the address
* Micah:
it doesn't have to be tied to the epoch address extension leave some space for bytes that are unused Reserve future use with you one of those don't we don't have to piggyback on that stuff.
* Alex:
 Yeah I guess it would be less complexity if it just title epochs right 
* Micah: Yea sure that would definitely be an option.
* Beiko:
Ohh, Greg you had some comments.
* Greg: Okay I’m muted I haven't had time to follow this one in any detail I'm partly concerned because there was a lot of discussion about this and Martin probably remembers with the way back in the EIP615 which required something and all kinds of issues involving a code that creates other code that needs to go on and that code can't be changed contracts that aren't really code there actually data it just there were a lot of issues that I don't know for sure whether this one is going to bump in to those sorts of issues and also to remind Christians attitude about begin data some point he just said I don't care how you do it but there has to be a way for solidity to hide the data that it needs to have without playing the tricks it has to play to force the date there's to be are not accessible as code he has to do ugly things so I'd be a little happier actually if I was sure that they didn't run into those same problems and could actually get a little bit more fleshed-out so that solve the beginning data problem at least 
* Martin:
yes so you are yeah I also recall all those discussions way back with wait time and a lot of people were trying to devise a scheme to have both is kind of opt-in validation saying hey I want to play by these rules and also these kind of validation or certification rules that meant sitting a one-day by these truths and also these kind of validation or certification rules that meant that's in EVM could know about the run this code I don't have to do any jump test analysis because it’s already been validated but we never could get there because we have to modify the accounts in the state we should modify the state we run into problems with above how does this kind of change if you have this new kind and create something else and it becomes tainted or does it before the same old rules or whatever yes there were all these problems that's why I'm so optimistic about this first step because it's just I think it's really clever step that solves all these issues and as for Christian they begin and also Martin’s proposal about the format this is kind of the next step. Those ideas implement I mean this stuff makes those things possible in a good way that’s my opinion about that. 
* Greg:
It makes them possible, but the next steps could get so delayed that the way our forks are getting laid out and the way the merge is interacting and the uncertainties there that we could make this step and then not be able to make the next step for like another year or more
* Beiko:
 that’s true of every EIP though to be clear so I think we're kind of a spot where no matter what whatever is not in London yes could be delayed another year and we had a similar conversation all about 3074 and it seem like people were comfortable that you know we can aim to have another fork after London if the merge happens first it happens first but yeah we don't have this certainty I think that's just like our situation right now but this kind of makes it possible. Micah you have your hand up? 
* Micah:
I think what Greg is alluding to is that we can if we don't know what's the second half of this looks like and we might not know what the second half looks like for years and so we could put this in now and then by the time we actually know what the second half looks like realize it doesn't actually line up the way we want and see where is an alternative path would be we don't do the first hardfork until we know what the second hardfork looks like so we can guarantee that they will come one after another like hardfork and hardfork rather than hard fork in two years and then hardfork 
* Beiko:
Alex
* Alex:
 a couple of comments maybe to Greg if I understand correctly maybe you you're also concerned whether what's Christians opinion on test and the Christian has been actually following an interacting with this proposal so he's fully aware and of The Proposal There's an actual implementation in solidity and by proposal I mean 3540 which is not planned for London into a comment to you Micah we do have a good idea what would be the next step which is 3540 but as Martin said on the chat even if he end up not doing 3540 which I hope it will this first step that could be used to introduce you know something like the backend date 
* Beiko:
There’s a comment also in the chat I’ll just highlight from Ansgar that the EIP is low risk because it only reduces functionality and could always be reverted in the future if we don't want it seems like people are generally in favor like would anyone have a a strong objection to put in to London? okay well I guess if no one disagrees yep we included in London Last chance the voice your disagreement
* Greg:
 when's the last chance for us to actually make the decision?
* Beiko:
 last call literally.
* Greg:
 we’ve learned at the last chance to make a decision is very much later than that.
* Piper:
let's just make the decision. 
* James:
Let’s skip the comment on previous politics. 
* Greg:
So this isn't a political thing it's like there's some uncertainty here and can this way to one meeting for people to look at it a little bit more closely to know if there really are objections or not or is waiting one more meeting going to make it too late to make the decision well
* Martin:
Sorry if I'm jumping in so I would propose instead if it seems like we are leaning towards it's that we decide to do it and then at the next meeting if the opposition has grown stronger let's revisit that decision and potentially put it out again but in the meantime I think it's good to signal with doing that we want to do this and implementers should implement it Etc 
* Beiko:
so maybe one thing we can do based on that yeah so basically Thomas has a comment that the next meeting is 3 days before the client should be locked for London so maybe what we can do instead is you know make it considered for inclusion for London we're going to have a conversation about like the devnets right after this so potentially added to the next devnets and if people feel like in in the next two weeks we've got it implemented it's on you know a devnet or close to beyond the devnet and there’s no objections that's come out then we officially move it into the hard fork and otherwise we don't but at least we can move forward with the implementations and whatnot and I agree to some comment to the chats about you know that EIP is not even addressed it's the first time it's brought up on coredevs so there’s some uneasiness about including it directly so at the very least we can move it the CFI it'll be there we can add it to the devnets and if that's if that's ready by the next call if we can decide to include it in London but we don't have to make that call right now and it'll be implemented in clients 
* Alexey A.:
may I just comment something I just joined specifically to make his comment about this EIP this specific suggestion about banning the contracts with this particular starting code we could have presented it like maybe months ago but the reason it wasn't presented month ago was specifically what people now are criticizing it for his like because we don't know what will come next but actually this whole month has been spent Pavil and Valask to try to present in these two piece there's a lot of text there what will happen that's unfortunate. I took some time and you know we could have just put in the is very short phrase like after the fork we do this and that it would have been done months ago but you know unfortunately this time has been spent on trying to flush out what will happen next and you know it's unfortunate the got us to this very tight spot
* Martin:
 So I think Alex talked about it and you were not present would you now like to voice your official opinion.
* Alexey:
Yes I am for it, it’s a very useful thing and of course I am I also suggested the idea about the this first step because when it gets through it it's basically to wait you to stop procrastinating
of like what mikah is suggesting is that okay let's figure out will happen next all the details about what happened next this is what we try to do before for years in fact and it never work because you know we never made the first step but this first step is basically gets rid of all procrastination because when it's done and its provable you can figure out the way to work around of anything that happened before the fork so in terms of like who wants to deploy this and that and we can always choose the magic which will defeat any adversary that will try to stop us from doing what we're doing.

##### Baikal devnet launched

* Beiko:
I guess based on you know Martin and Alexey comments and a bunch of comments in the chat about you know the bad process of including it today does anyone disagree with making it's considered for inclusion today I didn't get to the devnets which we need to basically restart anyways because of this other refund EIP and making Final Call on the next call two weeks from now so that actually leaves times for people to digest it to bring up objections and whatnot and that's obviously not just people in this call also like everyone that I think if we included it today there's probably a lot of people who would be like surprised by it because it just showed up a few days ago and that its schedule for London yeah so any objections to make a get CFI and adding it to the next iteration of the devnets? okay I guess we'll go with that then I guess kind of brings us to the devnets so I know there’s been a lot of work done on alut in the past two weeks anyone want to give a quick summary of where things are at with that I know there was a lot of discussion even this morning prior to call 
* Jochem B:
hey guys I'm Jochen from the javascript team and I’ve worked in the past week here by sending a lot of transactions to this testnet and I noticed that when I start syncing this network there were only 20 transactions or something and most of them were just falsehood transactions or legacy transactions. I found some works and as some general comments I think the testnet needs a lot more attention because there are only 20 transactions up to the point where I started sending some things in the next testnet. We also need to prevent these precompile accounts because that is not the case for the testnet and I also think that we should if you are going to use a click again then we should use multiple signins because I just noticed this afternoon that I cannot send access list transactions for some reason. Well I can send them but they do not get mined and that might be because bazel is not including those who do not want to do these things and that’s not very nice because I want to test that this access list also work with the new gas prices and stuff. These three points which I wanted to raise. 
* Alexey:
I just wanted to say I just wanted to say really thank you for doing what you have been doing. It’s great to just find all these issues.
* Jochem:
Thank you, it’s a lot of fun to try to nuke this testnet. 
* Rai:
Reach out to me offline and we'll discuss the basic issue with access list. 
* Beiko:
right great job thank you for doing that like it's really valuable to have people poking at it so yeah because we have two new EIP’s that we want to test the refund one and 3541 I guess we should restart a new devnet with those and then yeah ideally following the two suggestions here where we pre-fund the precompile addresses and you have more than one signer how did people feel about that 
* Alexey:
I mean that's definitely needs to be done and then now essentially do we want to wait till somebody Implement these two things or do we just want to do one by one. 
* Beiko:
we should probably have both in I suspect if we can’t get both in it’s kind of a signal that we probably can't get both into London I'm so I would favor leaving the current one up waiting until you know someone has the to be two EIPs implemented and then the start a new network with all of the EIPs that were in the previous one and the two we agreed today.
* Alexey:
But if we need multiple signers then we will need multiple clients implementing these right?
* Martin:
Well not necessarily we just need to make it so that we can have multiple signers and then we can run them. If guest is the first one then we can run three guest signers. Some of them whenever is ready we can just give them one of the keys.
* Beiko:
Okay so I guess we can probably coordinate offline for the details of that but at a high level multiple signers pre funded the pre-compiles having I think it would be 5 EIP’s like whatever was in a new two today the only EIP that would be in London but not in the devnet is the difficulty bomb one  yeah I think light client had propose a name for it on the Discord so baikal I think was the second fault line that we had after elute so we can use that as a name I'll put together a spec for its today and just share that. 
* Alexey:
Can I just have another suggestion for to simplify the this this fork and I just I just had another thought I know we had this conversation before and we can take him to take it offline but I do believe that we do not need to reset the difficulty bomb but simply remove it because both of the reasons why we keep resetting it do not apply right now because first reason was that the minors with a hybrid POS approach would stole the a migration which is not the case because the merge will happen regardless of what they want and second reason was to prevent statis for the development which is exactly the opposite of what was happening right now so I don't actually see very big reason to keep pushing the fork
* Beiko:
 Can we discuss that on the next call 
* Alexey:
Yes because we can do it offline because I can see like Afris is on holiday like we can’t calculate the let me know we can but it's a bit of like why do we create more complexity for ourselves this just remove it.
* Beiko:
 so we discussed it I think it was two three calls ago and people were strongly in favor of keeping it but yeah if we don’t have time in the next six minutes to go over this we want to discuss it again in the next call it's fine because it's like a small technical change and we don't need it for the devnets does that make sense
* Alexey:
 Yes thank you but I just wanted to bring up that Varis comment this needs to be reopen the discussion
* Beiko:
Let’s try to be as async as possible because this can easily take up 90 minutes. Two weeks from now if we did it and just in terms of process if you can bring this up on the next call just open an issue on the Ethereum pm repo and I’ll make sure to link that issue in the next call.
I guess I just back to the devnet so I can put together a speck today and I guess I'll follow up. So back to the devnet I can put together a spec today and follow it up so ill post it but clients will need tome to implement these two EIPs so I suspect we probably won't get it up next week but maybe the week after. So I'll make sure to follow up like a week from now to see what the status for the different teams are and you know what we can do with regards to the starting the devnet and I guess two more things we had on the agenda  kind of more announcements than anything else but next week at the same time at this meeting starts we plan to have the infrastructure Readiness break out room for London so there's been a lot of talk on the Discord about having infrastructure providers ready to support London and you know having clients kind of enable them with stuff like the json rpc aps and whatnot so if I guess you are an infrastructure provider that is affected by London this would be kind of the right place to show up with your concerns or questions.  I'll post a link in the chat here it's also on the pm repo yeah so just hopefully we can get a different teams working on infrastructure we don't need like all of the client devs to be there it’s not like a mandatory call or anything but just wanted to highlight it so people are aware of it and I know you've been working on that. So do you have any other thoughts you wanted to share.
* Trenton:
That was the big thing and I can see their components that similar to how EIP using client's Readiness are track typically in that same place that will also be tracking no libraries tooling and other infrastructure providers leading up to the fork. You know for which EIP’s they have implemented and their general readiness. I will drop the link in the chat.

##### New London infrastructure call

* Beiko:
Last quick announcement was we discussed on the last call potentially picking blocks for London today that feels still a bit premature I guess given today’s discussion but if we do want to have a client freeze on the next call then we should pick some blocks by then I'm so if people want to look at the dates and proposal blocks over the next two weeks that would be really valuable so we can assuming nothing changes just agree to them on the next call and I have clients add that into their configs and that's all I had any everything else anyone wants to bring up in the last 2 minutes. Great well thanks everybody appreciate you all coming out here.
-------------------------------------------
## Attendees
- Thomasz Stancsak (Nethermind)
- TimeBeiko
- James Hancock
- Rai
- Pooja Ranjan
- Trenton Van Epps
- Lightclient
- Martin Holst Swende (Open Ethereum)
- Danny 
- Marek Moraczynski
- Pawel Byilca
- Vitalik
- Paul D
- Alex Vlasov
- Alex B.
- Ansgar Dietrichs
- Jochem Brouwer
- Dankrad Feist
- Piper Merriam
- Sam Wilson
- Greg Calvin
- Peter Szilagyi
- Lukasz Rozmej
- Jason Carver
- Gary Schulte
- Micah 
- Jochen


---------------------------------------
## Next Meeting
May 14, 2021
