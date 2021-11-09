# All Core Devs Meeting 125
### Meeting Date/Time: Friday October 29, 2021, 14:00 UTC
### Meeting Duration: 1 hour 30 min
### [Github Agenda](https://github.com/ethereum/pm/issues/401)
### [Video of the meeting](https://www.youtube.com/watch?v=5cOWjMAuReI&t=4646s)
### Moderator: Tim Beiko
### Notes: Shane Lightowler

## Decisions Made / Action items
| Decision Item | Description | Video ref |
| ------------- | ----------- | --------- |
|125.1 | Ansgar to propose time for breakout session | [42.57](https://youtu.be/5cOWjMAuReI?t=2577)|


## Intro

**Tim Beiko**

* welcome to ACD 125. A couple things on the agenda today. Merge updates, updates on arrow glacier and then Ansgar has an eip which would modify the eip1559 mechanism to better account for missed slots after the merge and then finally dankrad and guillaume are here to chat about verkle tries and the general stateless roadmap and we could kind of get through the first three things and then give dankrad and guillaume the rest of the call to go over their stuff.
* So first any client team want to share updates about the merge where things are at any issues they've encountered?

## Merge Updates

**Marius (Geth)**

* i can start so we're currently looking into merging all the code from amphora from from the interop. until now nothing major came up.
* i've also started setting up a server for merge fuzz and m fuzzing gas right now but i'll add some other other execution layer clients to it for those who don't know, merge first is a differential fuzzer that basically just calls the engine api of two different clients and sees if they do exactly the same thing. so that's that's our update.

**Tim**

* did you find anything with the fuzzer so far

**Marius**

* we found something in the synchronization call in the sync code that was not final yet nothing really major

**Tim**

* awesome
* merrick i think you were about to start speaking 

**Merrick** (Nethermind)

* yeah we continue cleaning up our merge code or we set up all consensus client in our infrastructure with nethermind as executioner engine of course 
* we are in contact with nimbus team because something not working with nimbus and nethermind yeah it looks like we are working after mario's test and that is all i think

**Danny**

* i can yeah i can give an update we are primarily make io myself and some others are quickly closing in on the final updates to compensator specs extrusion layer specs and the engine api that came out of amphora
* i might do a pre-release later today and point to a commit on each that kind of gives you pretty much what's happening but we likely will finish more on monday there's a little bit more work to patch up between now and then but very close and then that would be breaking with respect to pithos and we would start kind of a new wave of testnet targets in november
* and just for context if you don't have the context it's largely similarly structured there's probably a few edge cases that are patched up and generally simplifications and reductions in the engine api so it's not throwing a ton of stuff out or anything like that

**Tim**

* is anyone from Besu on the call?

**Justin** (Besu)

* yeah we don't really have any updates right now we're cruising along we're merging in all of the code from the interop exercise that's that's still in progress so nothing nothing new or major to report
* that's all gary by the way so i don't have any hard details on it

**Tim**

* no worries. cool so any anything else anyone wanted to discuss about the merge?

## Arrow Glacier

[5:20](https://youtu.be/5cOWjMAuReI?t=320)

**Tim**

* next up is just arrow glacier. so on the last call we kind of decided for a block number and a delay for the difficulty bomb. i guess i'm curious to see how far along our clients in implementing this and like how realistic is it to have a release in the next week from client teams with this just so we could announce it about a month in advance.
* yeah i guess anyone from any client team want to go first?

**???**

* so we haven't done it yet but of course we can release it in the next week it should be very very easy so yeah okay 

**Tim**

* so next week is possible

**Marius** (Geth)

* martin implemented it we've merged into the code and our next release should contain it i'm not sure if we're going to do a release next week but i think so so yeah

**Tim**

* aragon

**???**

* yeah we haven't done it yet but we should be able to do it next week and should be yeah probably we'll release it next week

**Tim**

* okay cool and Besu?

**Justin**

* uh same story here we haven't implemented it but we have a quarterly release scheduled in the next week we'll likely have it included there

**Martin**

yeah i just want to as far as i know there are new difficult tests in the test repo so when you implement it you can check out the new tests as well

**Tim**

* anything else on arrow glacier??
* cool so i guess for people listening and who are looking to like plan their upgrade the fork block is gonna happen oh the fork is gonna happen at block 13 million seven seven three zero zero zero. that's expected to hit around december eighth so a bit more than a month from now 
* and one thing that would also be useful i guess only geth has it implemented now but if somebody can just share the fork hash like the 2124 hash so we can add it to the spec that would be great

**Martin**

* sorry, the fork identifier? it's in my pr i can paste it on the vm pm

**Tim**

* awesome thanks cool anything else on arrow glacier?

## Proposal to Include EIP-4396 to the Merge

[8:26](https://youtu.be/5cOWjMAuReI?t=506)

**Tim**

* Ansgar has been working on an eip which would basically modify eip1559's mechanism around the merge so that we can better account for missed slots in how we update the base fee i think he literally finished a draft yesterday do you want to take a couple minutes and start to kind of walk us through how this changes things and why this might be important to to do for the merge

**Ansgar**

* so basically the situation is just that with 1559 right now the base view of course looks at the gas used in the parent block to determine whether the place we should grab or go down and with the merge we'll have these usually regular slots every 12 seconds but then if there's a missed slot of course that's that basically means that there's like a 24 second window and just because transactions continue to accumulate right they could basically always expect a 24 seconds a block basically to have on average twice as many transactions so missed slots would usually result in little base fee spikes and so the question was just a is this a big problem was it just a small annoyance and then b is there something small we could do to to to mitigate that and so basically this is just one proposal so the question is just basically the actions we could take you would be do this do nothing at all do something else or just wait wait wait for shanghai basically.
* yes so so the approach here is relatively simple it's just because like the kind of the core problem here is that we don't really account for block times it adds like a a simple block based rule to the to the calculation
* important to note that under proof of stake there's no way for blockpurposes to manipulate the block time because it's like it's always enforced on the beacon chain side that the like every slug only has one valid timestamp that it could use so there's no there's no wiggle room or anything so it's really like a very simple way similar it's basically and this has the same properties as the slot number but it's easily accessible from the execution side 
* and so for yeah first why could it be kind of like important to do that with the merge so it's for one of course it's a little bit annoying with these with the base free spikes i think that's the least of the problems 
* the second thing that is a little bit more important i think is that basically every lost slot is like a permanent lost throughput for the chain so if we if basically the slot missed that means that we just have 50 million or whatever guys we have in the blog and just less of overall throughput and one i think i would argue that this is just not desirable because when we reset these throughput targets to reach them or to have to stay below them but also more importantly this kind of like gives a more clear incentive for a denial service attack against proposals
* so just because we don't have yet like these secret selections there are some concerns that potentially what was this could be anonymized and targeted in our service attacks and in the under the current situations every bulk deposit that you can basically stop from from producing a block means the throughput of the chain goes down which kind of increases the incentive and if we could mitigate that of course that would kind of like make you know our service attacks less useful for attackers which would be really nice and then the last concer is whatever we i'm describing here and they like degradation during consensus issues so i mean of course hopefully this will never become relevant but if we ever have situations where like a large number of validity goes offline at the same time and approved work right now this is really quickly self-healing where basically you just they have the difficulty adjustment and so while the block times go up for a little while they'll they come back down quite soon and so the throughput is only like impacted for a very short time and if we stake we still have a self-healing mechanism but it could take much longer right like especially if it's less than a third so the same change still finalizes it could take literal months even if we like below the finalization threshold and we have difficult and inactivity leaks it could still like be weak so basically like 
* and of course we could then start to manually intervene and just increase the gas limit but again also this manual attack intervention would take quite some time so so with much more permanent impacts to the throughput of the chain and that is physically during times where the stress on the chain is already at the highest because like we have these consensus right so not only do we have like a period where there will be more more activity because people will want to react to the consensus issue but it's also reduced throughput which is just like not ideal for the stability of the chain
* so obviously i think it would be important to do this at the point of the merge already so we don't have a period of proof of stake without without this adjustment 
* the specification that i proposed was like really motivated to be as minimal as possible so this is kind of taking the eip 1559 update rule and just basically it's really if you look at it's just basically it changes like five lines of code or something it adds like these two constants just block them target and basically a maximum of what we want to allow so basically this this just means that we basically allow up to 95% of a block to be used as basically like a as a target so say right now with the elasticity of two basically this would mean that like we basically allow the the gas target to go up to 1.9 times the block um and then the only changes in here is that we have this extra sorry it's extra line that that does this adjusted gas target calculation and then uses it down here but it's yeah so this is basically like four five lines of change so it's really minimal so it shouldn't impact the much work too much 
* it what it does do is though it means that now the basic operation does depend on the grandparent of a block as well not only on parent because we need to access its timestamp so that is one more block that you need to have available to validate the header that is a significant change right and that's basically that's basically that 
* the one important thing is to maybe briefly talk about limitations so because basically in the account in this minimal change all you can do is really kind of account for more or less for one missed slot but if as soon as you have two or three slots in a row basically you you just can't because we only have a elasticity of two there's just no way of kind of like recovering all these transactions and so as you can as you can see i put like a little graph in here so basically like with the depending on the percentage of offline poker process the throughput of course does go down the blue line would be what we have today and then of course like what up first would be like for the brown line here so basically like as you can see we have a much more gradual decline initially which is exactly what we need for dust protection right so basically there's almost no decline initially and then even even in situations where like 20 30 40 percent of what proposes offline we still have like much less degradation than we would usually have but of course it's it's not perfect and 
* so like the last thing is where maybe i would want some input is there some extension so you could you could make this much better basically much much less degradation until until you go down way way further but those would require slightly more involved changes so this would add one header element or alternatively could also do this by accessing not only the parent and the grandparent of the book but like the last 10 15 20 30 and ancestors but that also seems like a more more kind of like substantive change and this year would be if we were to increase the elasticity of a block from two to two point five or three or something that would also help quite a bit 
* i would argue this might actually be feasible just because under proof of stake we have these 12 second block times as a minimum and so it's already much reduced stress right now we could have block times of three seconds if we basically if the randomness of proof of work turns out against us and so the strain is already much reduced and approved work so i think there might be a case to do this as well but again the objective was to keep the change as minimum as possible so these are optional additions
* i think that's basically all and so then just basically for context it's it's really just because as then you were saying we kind of the kind of the specs for the execution side for both execution side and competitive side kind of are supposed to be more this final very soon so if we really want to consider this for the merge which that would be the call we'd have to make very soon um yeah and so feedback would be appreciated that's all.

**Martin**

* i have a question. i had a bit of a hard time understanding what you meant by denial of service how it improves the situation against denial of service and as i understand it and please correct me if i'm wrong like what if there is some transactions that for whatever reason causes a large majority of the nodes to process the blocks very slowly so the block time increases 
* i think it i mean it can be seen as if like 50% of the seeders go up line
* now if i understood you correctly the what would happen is that the base fee would go down and the actual transactions included in the blocks would go up to basically the top miners go down and block times double then you would have double the amount of transactions in the block so it feels like that would make the denial service attack worse
* now did i misunderstand something

**Ansgar**

* exactly that's it so basically that they're truly service problems one is as you're saying like transactions that take a long time to execute but the other one is to target specific block proposals so you can like there are some worries that you can just basically based on message relay patterns you can you can de-anonymize the like the appeared addresses behind specific validators and then because it's known in advance when it's their turn to produce a block you could like specifically target them just before that time and make them go offline for a short amount of time so that they are not able to to produce a block

**Martin**

* right so the context which you are discussing is the like easter world the post merge

**Ansgar**

* right

**Martin**

* so in the context of the pre-merge world what i said do does it make sense or did they still misunderstand something

**Ansgar**

* right so well this was more small thing just it would not actually decrease basically it would just stop the basically from increasing when the block be like if say like basically only only every other blog proposal actually well okay if you're talking about proof work of course right if basically the block times start going up then that would basically mean that the blocks were allowed to be more than half full on average
* that does mean indeed that if we have a proof of work attack similar to like this shanghai attacks where we just have like very slow to process blocks that that would basically mean that the well it wouldn't actually change much it would just basically mean that like the new equilibrium would be a little bit different instead of basically having say i don't know if if as you were saying your example usually like say the block times would double now they would basically go up 4x but every bug would be twice as full on average it would still like reach a new equilibrium where basically 

**Martin**

* Would it reach a new equilibrium though? i mean if if if the throughput as in you know gas per second while gas per block should be constant and the nodes cannot i mean wouldn't at least like form some kind of cycle where the block gets slower and so we have more transactions go into it and that makes it even slower and more transactional when ended like some kind of self-reinforcing cycle and 

**Ansgar**

* the nice thing is that we just that that can't ever happen because we have this strict upper bound of the elasticity right so right now we have like a 2x maximum size and we just can't go beyond that so even if we end up with 2x the block size that's that's the limit so so basically there is no no kind of room for for any of the for the cycle if you were to completely remove the scissors yeah you're right that this 

**Martin**

* all right so so it would do that to a point and then there would be a steep and there's a much more steep drop than at some point 

**Ansgar** 

* right but but again i would i like basically i would say that that's what we have the gas limit adjustment mechanism for right like i mean similar to what happened during the function high techs that in that scenario you would just basically advise miners to reduce the gas limit 

**Martin**

* right but i wasn't really sure how your proposal interacted with the gas limit if it did 

**Ansgar**

* no no it does it does not in any way change the gas limit and i think that it's important because indeed like the test limit is this is irrelevant for security considerations so it just acts within the gas limit it just basically sets the gas target instead of always targeting half full blocks it allows more than half of blocks to be targeted
* if bugs basically come in slower than expected so so that it balances out but it never changes the gas limit

**Martin**

* yeah okay then that i think that alleviates my concern i think that was the part i missed them

**Mikhail**

* yeah i have a simple question why can't we iterate over this is slots treat them as an empty block and just re use already existing formula and with each iteration apply this formula to compute the base fee of the block that finally exists

**Ansgar**

* yeah okay so so if we just basically insert artificial empty blocks into missed slots 
* the problem is that that kind of set basically just sends it incorrect signals would be because an empty block would signal that there's no demand so so that will basically lower the base fee and but it would end up resulting more or less in the same situation because you'd lower the base fee before the next block and then in the next block you because it would on average be twice as full you increase it back up but that just basically means that we have the incorrect base fee 
* it would end up in almost the same situation as in my proposal just that these the slot after in this slot would just basically have artificially too low base fee and so too much extraction by the miner like p extraction by the miner and but it would honestly 

**??**

* it just feels more complex doing it that way because you still need some scheme like what happens if several blocks are missing and so on and just breaking this one into one block correspondence seems wrong

**Ansgar**

* right yeah i also would say that these artificial blocks would be more complex but i mean otherwise i mean the comment was i think it makes sense right because like the effect would more or less be the same um it just yeah again 

**Mikhail**

* my concern is just that we changed the logic and it's it's it's from some certain points it's more complex than use already existing logic just apply it like in and specifically 

**???**

* but inserting empty blocks is also changing the logic right 

**Mikhail**

* no we don't need to insert those blocks at all so we just need to apply this formula like 10 times if we if we have 10 slots missed before this block

**Ansgar**

* right but the length of the problem there is that basically that means that the base fee goes down in situation where it should not go down that that is the main problem and especially if you do it iteratively if you don't only don't don't know

**???**

* i don't think that's true i think it's equivalent right more or less like i think it's equivalent because i don't think that's right so i don't think that is the argument it's purely about complexity which one we consider more complex i feel like this is the better solution

**Danny**

* i mean both are similar complexity pretty much if you do the diff and time stamp mod slot time and then run a formula that number of times versus doing a slightly different formula i think it's pretty similar to complexity 
* i'm not arguing for one right here 

**Tim**

* but the execution client doesn't have the slot numbers right 

**Danny**

* no you have that's the time stamp that's why i said mod plot time so so right block time at target is proxy in here for slot time 

**Tim**

* right right okay that makes sense

**Ansgar**

* yeah maybe if these two formulas are kind of equivalent down yeah cool
* i thought that this like a bit the mechanism that you have proposed is just a bit different from what i've been thinking about it 

**Danny**

* why is parent why is parent block time why why are we doing that like using a grandparent instead of just the diff between current block and parent 

**Ansgar**

* just because like the way we like the basic calculation just happens when we validate the base fee in the block but that just means we have to look at the situation in the parent and then so within that we need the block time of the parent the block time of the parent is the difference between its grandparent and the parent right because because the base fees never adjusted for the block itself it's always suggested for the next book

**Vitalik**

* what would break if we just make it based on the time delta between the black and the parent instead because like i guess the way that i philosophically think about this is that i think of the base fee update as being two separate updates 
* there's always a positive update as a result of guests being consumed and up and always negative update as aresult of time passage so like in theoryit shouldn't matter if the order of the two gets flipped 

**Ansgar**

* right that's a good point i'd have to think about it yeah who happened if yeah there is also the like miss slots before the parent block like missed slots between the grandparents and the parents 

**Vitalik**

* like no matter how you do it like every single span of two blocks gets or every single span between two blocks gets counted once right so it should be fine anyway

**Ansgar**

* yeah yeah that generally sounds possible 
* um just again i think that yeah just have to have to think about it briefly just to make sure that there's no even no small within a block inconsistencies where like the basically in a block is not the one it should be and then even if it like basically this returns to the correct one in the next clock ideally you you never want to individual blocks where the miner basically has it too too low or too high basically 

**Micah**

* does the execution client know the slot time currently

**Danny**

* no it could i mean it knows the time stamp and the timestamp is ensured to be congruous with slot time by the consensus player but it does not know the kind of like beacon genesis time and the slots per second which if it did if that was just baked deeply into the configuration the execution client could calculate plot time based on timestamp 

**Micah**

* i would be a little hesitant to bake that in the configuration of the execution client because one can imagine a point in the future where we want to change that and having change in both

**Danny**

* yeah it doesn't seem super valuable to be in there although if you look at this pr the vip block time target is essentially a proxy for slots per second and so if it makes it into this eip then it is making its way into the configuration there 

**Micah**

* yeah that feels...

**???**

* well you basically do need this if you ever want to do anything about miss thoughts on the execution side yeah there's no way of telling if you have a mistake 

**Micah**

* yeah i agree that it's necessary it just changes this from oh this is a nice clean simple solution to now we're bleeding consensus layer logic into the execution client and that that's what makes me feel less positive about it that's all

**Ansgar**

* i guess it doesn't have to be that way can't we just simply say the gas target is per second rather than per per block and then this content constant would disappear

**???**

* right yeah

**???**

* yeah that means it wouldn't need an update if the slot time change in the future 

**???**

* i mean we could argue it right now it doesn't need that update anyway it's just that we would still be written as a quotient

**Vitalik**

* right yeah i guess like one one nice benefit of making it entirely timestamp based is that if we do change this a lot time in the future we don't need to do anything else to ensure that capacity stays the same across the change 

**Mikhail**

* but if we do it per second it's just basically we still it's still baked in it's just hidden a little bit more because then it's in the elasticity multiplier because right now it would be 2 and then would be 24 and the 24 would just come from 

**Ansgar**

* but the point is fundamentally fundamentally the constant should be per second right i mean it's a like if we for some reason decided that like poor pos has to be two times slower for some reason then we would increase it by a factor of two so i would argue that the fundamental dimension of the constant is gas per second 

**Danny**

* but the it's the elasticity that you want on a per second basis or right now 

**Ansgar**

* i don't see what it has to do with the elasticity 

**Tim**

* because the blocks are in the past and then the you still have future blocks coming right like so imagine you missed three blocks and you have like you know a three times bigger block than because your elasticity gives it to you you still need to be able to process that three times bigger blocks before the next block which you assume won't be missed arrives so it's like you can't accumulate all the past misses that you've had 

**Micah**

* so it i think that if we ignore what we have implemented today and we just think like conceptually what what do we want what we want is we want the chain to have a certain number of amount of gas per second how many blocks per second are unrelated to that like fundamentally we want gas per second and the execution client does know you know when was the last block and how much gas did that last block use and how much time has passed since that last block and so i think we should again purely theoretically ignoring currently implementation we should have enough information to do gas per second without knowing the future slot time without knowing what the intention intended slot time is we should have enough data to answer that question i don't know how we convert it 

**Ansgar** 

* in that scenario it would just replace the elasticity multiplier because we don't right now we don't actually explicitly set the gas target we set only the gas limit and instead there's a decision multiplier to calculate the guess target and if we would set the guess target on the per second basis and we would set the block gas limit which we still need in order to know what the maximum block size is then we would just no longer need elasticity which would just be implied then yeah 

**Micah**

* so i guess i guess my argument here is weekly that i would rather see us come up with a larger change that makes it so we don't need to have the execution client know what the block intended block time is when for the merge like with the merge i would rather not have to leak information about block time into the execution client if we can avoid it if that means making a larger change i think i would prefer that personally like a larger change to this formula i would prefer that over a simpler change that does result in a leak of information

**???**

* it feels like you that purity is no i know 

**Danny**

* anytime you like information you type you more tightly couple specifications and upgrades

**Ansgar**

* right but i think i think they are that tightly coupled simply like i mean it happens to be like easy because the current slot times are very close to each other with 12 and 14 seconds but if we had very different slot times we would have to make other changes like i i would just say like they sorry they are coupled 

**Tim**

* lukasz you have your hand up

**Lukasz**

* yeah i will probably throw a wrench into the works but it feels like we are thinking about fixing a consensus problem in execution engine in general so the question from me would be why the consensus potentially cannot handle this like more like click does that you can produce out of order blocks if someone misses their slot or something like that 

**Danny**

* you can't you can but i mean the way that the way that a proposer is selected is just fundamentally different than proof of work improvement and so you could do some sort of backup model where it's bought in if somebody doesn't show up in a second you could have somebody do a backup but that's still even if you did that you could have mislaws and result in reduced capacity which it seems natural for the EVM to be aware 

**Ansgar**

* i just wanted to briefly say with the guts the to the conversation about leaking information about the block time slot time and to the execution client i don't actually think that this is avoidable just because even if we set the gas throughput per second and the block gas limit separately we still want them to go up and down in lockstep right so like because otherwise we don't have a mechanism and so we would still need to hard code the elasticity and if we had got the elasticity of 24 between the two then we are already hard coding again that the slot time just in a hidden way so 

**Micah**

* why do we want them to go up how would you 

**Ansgar**

* how else would you ever was over the yeah the gas limit and the car started up and down separately

**Micah** 

* i'm sorry i thought you were saying the guest on the block time when that increases you would want the gas limit to go up at the same time i misunderstood 

**Ansgar**

* i know i mean i mean actually like with the signal like with just like just s right now and i don't think we want to have the eap that would remove the control by the vocal poser from at the part of the merge so right now blockcomposers can slightly nudge the gaslimit up and down right and if they continue to be able to do so we would hope that also the guest target per second would go up or down by the same like fraction 

**Micah**

* we could we could make it so so so this is this is where it gets into the a bigger change to avoid the data the information leak but one can imagine a change where the way that they increase is now you increase the gas per second rate instead of the gas for block rate and so the limit that would go up is the per second rate and so every proposer can do 1 10 24 increase or decrease in the gas or in the gas per second rate 

**Ansgar**

* how would the limit go up

**Micah**
* so just like the rates like if we want you know 10 gas per second or 1000 gas per second or whatever and that's our target then each proposer can say i would like to increase or decrease that by up to 1 10 24 which would be functionally the same as them currently increasing the block limit by 1 10 24th but but what would be the block limit in that world like would the block limit be set separately or would that just be automatically part of that or would you get it the block when it would be the block would automatically be character seriously 

**Ansgar**

* but if it's automatically calculated this by 24 times that number there is your block. 

**Micah**

* if the rate goes up then our if the rate goes or if the slot time goes up then it means that the block limit would also go up and that isn't necessarily what we want like we may want blocks to come every i don't know i'm just going to stop talking for a minute while i think

**Ansgar**

* right and just to briefly put maybe out here i i think it's probably not not ideal to just talk about these details too much yeah i definitely think that like this is just a specific proposal that just came out of me talking to a couple of people so i think they're definitely other flavors of this that would maybe even be better to reach the same goal the question is really more do we think a this is just necessary for the merge itself or could we just wait for shanghai to come up with like a really solid and well worked out solution and if we think we should want to do it as part of the merge um maybe just talk briefly about how we go from here and then do the actual discussion offline i think

**Tim**

* yeah that seems reasonable. i guess does anyone think yeah we should not do this at the merge like is anyone strongly opposed and there's kind of the weak objection around like the information leak that micah just posted in the chat but like assuming we yeah i guess that aside does anyone feel like it's not something we should do

**???**

* like i said before i'm not convinced this this is a execution client problem

**Tim**

* right right so but it could be on the consensus center side sure but it's it's and i guess the trade-off there is obviously you know if we do it and it's non-trivial it does add some work related to the merge but it does seem important and verdi's kind of seem worth exploring more 

**Danny**

* just to speak to that there's always additional things you could probably do in the consensus layer to try to avoid missed slots but there is just a stronger notion of time and there is a notion of something not happening during the time even if you do shore it up in some ways and so there is this notion of like you can have missed slots and i don't think that's going to go away and thus the evm can either react to that or not with respect to its capacity.
* so there are certainly concerns like this compensator and you probably want to make sure that try to make sure that slots aren't missed or there's recovery in the case of slots being missed but the thoughts will always be able to be missed 

**Tim**

* right does it make sense to maybe just schedule like a breakout room for this sometime next week or the week after something like that it does feel like we probably want to think through the like design space and like come with some proposal that at least you know yeah we we all agree makes like the right trade-offs 

|125.1 | Ansgar to propose time for breakout session | [42.57](https://youtu.be/5cOWjMAuReI?t=2577)|

**Danny**

* i'd definitely suggest this coming week i do think that this if we do anything to the evm that this is the thing to do with the merge. i do think that 10 of block proposals going offline because of some reason or other is like totally something that could happen and having reducing the incentive for that to be happened from from an attacker and reducing the impact that has on the execution layer and on capacity i think it's very nice to have and if it's going to happen then we need to really make a decision 

**Ansgar**

* but would it really decrease the incentive like if i if i have a validator and i know that the validator right before me i know the ip of the validator i can just toss the validator right before me and then create a block that's double as big 

**Danny**

* so there's two types of i guess attack and sounds one is validated and validator and the other would be external and it reduces the external incentive to attack and it might actually increase as you noted the some of the intravalidator attack incentives so yeah we should think about that

**Tim**

* okay so yeah maybe as a next step ansgar can you maybe propose a couple times that work for you and All Core Devs for next week and we can we can have like a round table there awesome yeah thank you for for working on this and presenting it today

## Verkle Tries Update

[45:01](https://youtu.be/5cOWjMAuReI?t=2701)

**Tim**

* okay last thing on the agenda i suppose probably take up the bulk of the call is dankrad and guillaume have been working on stateless and verkle trie implementations to facilitate that and they wanted to share just kind of the a the general road map around stateless and why it's important and kind of the solution space they're in and then why specifically vertical tries are an important step in that direction

**Dankrad**

* okay so i wanted to give a quick overview over the Verkle Trie work for evernote on this call so that you know where we are and like why we are proposing these changes and that are quite fundamental and so i'll start by quickly like just giving a very rough idea on on on on the whole thing 
* so so what's a Verkle Trie vocal stands for vector commitment and merkel and so it's basically a tree that works similar to merkle trees but the commitments are vector commitments instead of hashes and tri stands for tree and retrieval so like it just means a tree where each node represents a prefix of keys which is already the case in the current merkel partition trees 
* and so what does that mean so when we look at a marker proof i made an illustration here if we want to prove this this green leaf then when we go up the tree we need to compute all the yellow nodes all the hashes at the yellow nodes right and for that we need to provide all the siblings of either the green or yellow nodes so that we can always compute the parent hash 
* okay if we change this here i i showed like what what happens if we go to with four instead of the binary tree that i've shown just now for a merkle tree then what happens is we've reduced the depth but now we need to give three siblings at each layer instead of the one we had previously and so actually by increasing the width we increased the size of the proofs which is like currently one of the big problems with ethereum state and that merkle partition trees are actually with 16 so the proofs are huge and 
* so how do verkle trees change this so here is an illustration of what happens in a vocal tree for the same situation we again have the green leaf that we want to open and instead of having to provide all the witnesses in a in a good vector commitment in quotation mark so like in one of the ones that we are going to propose instead of having to give all the siblings which is happens when you use a hash as a vector commitment which is what merkle trees do you only need one opening for each of these layers and that opening is constant sized so that's why suddenly it becomes efficient to increase the width because the proof size doesn't suddenly increase but instead it decreases and so if we have this very tiny example then then we have to just provide this inner zero one node as part of the proof and these two openings as part of the vector commitment openings 
* and even better typically we're going to use additive commitments so all these openings will collapse into one 
* so that's basically like a short summary like here basically what happens is you have to give this one in a node and one opening that gives a proof that leaf zero one one zero was part of inner zero one and inner zero one it was part of of the root 
* so there you can see where vertical trees gain the efficiency it's from this this property that you don't need to give all the siblings anymore but only like a small proof that everything is a part of the parent 
* okay so i made a short illustration here like on how how good they are so basically like we are we're going to suggest that the proposed gas cost per state access will be 1900 gas and at the current gas limit that would mean about 15000 state accesses if you use a hexary merkle tree then currently the witness sizes are about 3 kilobytes per witness and that's 47 megabytes so that's absolutely huge 
* if we change this to a binary merkle tree we would have about half a kilobyte per witness and then we would be eight megabytes that's still pretty big now if we use a width 256 verkle tree instead with a 32 byte group so like each commitment has 32 bytes as it has now but it's going to be a different type of commitments then it would only be about 100 bytes per witness and so that reduces it to 1.5 megabytes and now we're finally in a range that we can consider is is reasonable and lets us do statelessness 
* some summaries on the course so i made some estimates here if we want to do 5000 proof so each each of the 25 000 openings that you would have to compute would need 256 times for field operations each of them costs about 30 nanoseconds so that's 750 milliseconds for such a proof so that seems pretty reasonable in terms of prover time so that's the one that a block producer would have to do and the verifier would have to do a multiscalar multiplication and the size of it is determined by the number of commitments that are opened so it's an msm of size 15 000 for these 5000 truths and that we estimated can be done in about 50 to 150 milliseconds these are all estimates based on like the raw speed of the space operations so benchmarks are still coming in and we need more optimizations to actually get there 
* okay so i'm going to come to the tree structure that we're going to suggest and because that's important for the road map and why we are suggesting doing these changes in a certain order and the design goals that we had in mind when we when we came up with a structure is that we want to make access to neighboring code chunks and storage so that's cheap but at the same time distributes everything as evenly possible as possible in the tree so that state sink becomes easy these two goals might seem contradictory but the way we do it is that we we aggregate this neighboring code and storage slots into chunks of 256 and only within these it's cheap and then these can be fairly evenly distributed 
* and then we want this whole thing to be fast in plain text which means fast in the direct applications as we're suggesting it now but we also want it to be fast and snarks so we envisioned that within a few years it will become very feasible to to compress all these witnesses using snarks and for that we optimized everything so that it can be done very efficiently in snarks and that would also help anyone who designs roll-ups with us or anyone who wants to create state proofs and feed them into a snark 
* finally the whole thing should be forward compatible so we're basically designing a pure key value interface with 32 bytes per key and per value 
* so keys are basically derived from the contract address and the storage location and what we're going to do is like the two will be used to derive a stem and a suffix and the stem is simply pedersen doesn't as a type of hash but when that's also efficient to compute in a snark of the contract address and the storage location except for the last byte right so we're extruding the last points on this and then us there we put the last byte of the storage location directly into the suffix 
* and so for any storage location that only differs in the last byte the nice thing about this is that and the stem will be the same and only this last bite will differ 
* and then we're going to put them into a tree that looks like this we basically have this vertical try at the start that locates the stem and that works very similar to the current account try and then at each stem there will be an extension node that commits to all the data in that extension and so that means that like opening several points of data in the same extension which we yeah or like the same suffix tree which you also call it is very cheap because like the whole stem tree is already opened at that point there's nothing new to do and you just have to open another point in these polynomials c1 or c2 and so that is that is a very fast operation and very cheap
* so as a as a rough summary basically we have a huge reduction in witness size it's about five times smaller compared to binary merkle and more than 30 times smaller than the current hexary trees so that's pretty huge and verification times are pretty reasonable like similar to a binary merkle tree the prover overhead isn't huge so like even in the worst case it's i estimate it can be done in a few seconds our solution doesn't need any kind of trusted setup so it's all basic elliptic curve arithmetic which we're already using in ethereum just the discrete logarithm assumption and i think it's currently the only known solution for ethereum state that doesn't come with like huge trade-offs in terms of how big the witnesses are and everything 
* right so yeah this was my quick introduction i can't see are there any questions about it at the moment 


**Tim** i don't think there were any well there were a couple like technical questions in this chat but i think they all got answered 

**Dakrad**

* please feel free like if anyone has any questions about this like reach out to me i'm very happy to explain anything i also wrote a few blog posts about it yeah it's obviously like some something to get into and it has a big change but i think it it also comes with huge advantages so i also gave a peep and eip and eep talk if anyone wants to i think it has some more details so identity 

**Danny**

* i did have a question from the chat you showed the max witness like worst case witness size do you have data on what the witness sizes would be with you know current average main size domain network 

**Dankrad** 

* so that's not so that's not technically the max witness size that is i mean they're different different definitions of max like that is the max if you don't spam the tree so what i shared here was a rough estimate if you have like a block that does only state accesses for the whole block but that's the slide right but it's not about so if you spam the tree there are some worse things that you can do in all of the cases obviously 

**Vitalik**

* i think the average cases occur should be a couple hundred kilobytes 

**Dankrad**

* yeah i do have actually and i wanted to share that as well i actually made a little calculator which i can share where you can play with these things
* so it's this one and basically how you can use this one this one uses all our suggested parameters and you can adjust how many elements are in the tree it will compute what the average depth is this is all the input forces suggested gas changes and then you can enter numbers on what you think like 
* so this is an example where we access one thousand different branches or one thousand stems essentially four thousand chunks then we have like 400 update different branches update and 1200 chunks updated then it gives a number here that would be the gas cost for that so this example would spend more than 6 million in gas just on the state axis so that seems maybe like a roughly reasonable average case i don't know maybe even high average case i don't know if people are gonna spend that much i don't know how to estimate right now because people are obviously also going to adapt 
* so in this case the total data so this is any any scheme has to provide the data right so that that's an absolute must unless you snark the whole execution you have to provide the data the data size here would be about 200 kilobytes and the total proof size so that's all the commitments and the opening that you have to give in addition would be 110 kilobytes so the total witness size would be 308 kilobytes so that this is like a roughly average case and i put this on there on the acd call as a link as well so please like feel free to make a copy of the sheet and play with it and yeah here are numbers on like what the prover time would be like 250 milliseconds and the total verification time and 64 milliseconds obviously all of these are estimates at the moment

**Micah** 

* those benchmark those benchmark estimates are they on just like what kind of very rough class of hardware is that estimating 

**Dankrad**

* that that's that's a recent like intel cpu basically like like a laptop or like a server it's not parallelized so it shouldn't really make any difference like it's single thread okay yeah so one thread on a modern intel cpu-ish yeah that's my estimate like as i said so these are basically based on what's the dominant operation for each of these things and like estimating how many of these are of these you need 
* i think these two things are like fairly i can estimate fairly well however this does depend on eliminating all the other bottlenecks so just to be clear here the prover time this would only be the time to actually generate the proof and i would say like it's very likely that most of your time will actually be spent like getting the stuff from the database like that's you still need to do that that's separate 
* cool and so the reason why we brought this to the call now is that what we want to suggest is that we we basically have created an idea for a roadmap how we how we make ethereum stateless and the idea is this the idea is to spread the changes over three different hard forks and at the end of it well actually like if ethereum would not be stateless in itself but but it would would gains optional statelessness and i will explain in a minute what that means
* and the changes would be for the first hard fork which i suggest to be shanghai would be to make the gas cost changes in order to like enable all this and the reason for making the gas cost changes first is well one is they are relatively a bit easier to implement than the whole database structure or well actually we need to make some changes to the data structure but the whole commitment structure and two the most important thing is i think to give signals to like developers as early as possible on like how they how they should handle state access in the future basically each month where like state access remains cheap and everything remains as it is is another month where like new contracts will get deployed and they will all depend on the current gas schemes and they will all be upset when later everything changes and some stuff becomes super expensive or they could have developed in the more efficient way so that's really annoying so it would be just so much better if like as early as possible we could get them to the right numbers and i think realistically let's be honest the only way to do that is to actually change the gas costs 
* and so that is why i suggest in the first hard fork to make these gas cost changes, in the subsequent hard fork and i call it like shanghai plus one here cancun or whatever that is what we do is we just freeze the current market partition tree root as it as it is exactly at that point and we add a verkle trie commitment and that is initially going to be an empty commitment and we'll just track all the changes from then on and at shanghai plus two we replace the frozen mercury tree root with a verkle trie route and the reason for that is that with this roadmap they're at no point does there need to be an online recomputation of the state like all the recomputations on database and commitments can be done in the background and that don't have to be done online
* okay and so the gas cost changes i sold and well i mean it's based on work by vitalik but yum has separated them here into a separate eip draft and the idea is basically this so i like keep in mind this design for the verkle tree so we have this these different parts we have the stem tree where you basically try to group things together that that are in similar storage locations and then extension nodes which is like a a node representing like 256 storage locations that are close together and so basically we have typically two different kinds of costs we have like a cost if you access any of these stem trees and a separate course when you access chunks that are within a stem tree that you've already accessed and so the sorry within the suffix that sorry within a stem that you've already accessed in the same suffix tree
* so okay and so the nice thing about that is that some things will actually get cheaper so and i mean that that's i guess like one good news for smart contract developers not everything was every state access would suddenly become crazy expensive if they designed things well then then they can actually save some gas and so we have here suggest that basically there's five different costs that depend on what you do so basically if you access any stem for each stem that you access during transaction you pay 1900 gas if for each chunk that you access you pay 200. so if you access say 10 chunks within the same stem then you would get a cost of 2 000 gas from that plus 1 900 for the stem so a total of 3 900. and then in addition like writing so for each stem that you write to you pay a fixed cost of three thousand again for each chunk within that stem you pay 500. so if you added 10 of these then you pay like five thousand but you only pay this one once if they're all within the same stem and finally when you when you fill a new chunk so when you when you add another node here that has never been written to before then you pay 6200 so like adding your state is still somewhat expensive 
* and finally this might be one of the most controversial of all the changes but i think it's overall just important and we should do it and figure out a way to do it basically deactivating the self-destruct so the way we deactivate this we name rename it to send all and it moves all eth in the account to the target but it doesn't do anything else so it doesn't destroy code it doesn't destroy any storage and it doesn't refund anything for this for destroying those because they aren't destroyed yeah so that's that's basically that would be the suggested changes for the shanghai hard fork
* so i mean it's mainly gas cost changes however unfortunately they do require and that's one of the things why we're trying to introduce this whole thing early and get feedback on it and it will require changes to the database because we are basically reducing the costs for this chunk accessors and that means if in practice they have they have the same cost still like as they have now then that's a dos vector and that would be annoying so it would require that clients already make some of the adaptations to their database so that accessing this the chunks within the same stem tree with the same stem would be cheap and i think the reasonable way to do that is if people would just store this whole thing this whole extension in one location a database so that's the easy way like it's even if if the suffix tree is full that's about eight kilobytes of data and so that's not a huge amount and basically every time you read that you just read the whole thing from this and then basically because like whether you read 32 bytes or like 10 kilobytes from this like makes almost no difference it's always the number of io operations that actually matters that that should alleviate that concern
* so that would be the suggestion for the shanghai hard fork the next hard fork we would freeze the merchant practitioner route and add a verkle trie commitment so we would say like the current state route is frozen exactly as it is and no changes are made to it and then we add this empty verkle trie route that contains nothing but whenever anything from the state is written to or even read from we just transfer it into the verkle trie rule but that doesn't mean we remove it from the worker participate we leave that as it is and then in the background at any point
* between this and shanghai plus two you can make this background computation where you where you can recompute this mpt root as a verkle root and we would then replace the mpt root with a verkle tri-root and so that's yes so basically you can do that either you can do that locally but it can be done in the background because all the data is cons is constant so even if you have to access the same database like you can do that in some in another process or anything people can run that at any point and so that's nice you have several months to do this it could also be even a simpler solution for some clients to simply say like provide the converted database as a torrent i guess there should be still a way to like verify it but maybe not everyone has to absolutely do that it's i mean the trust model if you just don't know that as a torrent is not really different from doing a snap sync so like as long as we have reasonable number of people doing this i i don't see like that there's a security concern there 
* and if we actually do already have state expiry ready at that point then we don't actually need to do a database conversion for most clients because we can simply use state expiry for the last step. we can simply say from now on this first database has expired and then you only need to literally replace the root and you normal clients normal nodes that don't keep all this old state don't even need to convert it anymore they can just forget about it 
* and what's the result of this basically we get optional statelessness so at this point anyone can add block witnesses to a block and we have made sure that they are reasonably small and quick to verify and everything and also reasonably easy to produce and so what it means is we can create separate networks where we have status blocks for example one obvious one would be to simply use the what is now the consensus network the lib p2p network on which all these two clients run and simply distribute status blocks on it but there could also be more experimental other networks that's that do things with these status blocks and then i guess like as an optional future thing or very likely future thing is like we can for example one way how we come to full statelessness is we just deprecate the old devp2p network say like consensus is now 100 percent just on lib p2p and the fp2p remains as a state certain network so anyone who wants to have full state goes on there and that's like a network that's mainly used in order to get full state and p2p is used by all the consensus nodes light clients and so on whoever one wants to get blocks with witnesses
* yeah that's that's my that's my introduction of the whole thing maybe and do we have any questions at the moment 

**Micah**

* so first question so the change in shanghai it feels feels like maybe i'm missing something here it feels like that's a pretty significant change like changing the database structure in a way that so that current execution clients can correctly calculate the future gas costs 
* i'm concerned that that may be something that's they can't even do 

**Dankrad**

* so to be precise you don't need so you you can easily compute the gas cost so that's that's not the difficult part like all these costs can be we can add that to a client right now to compute these correctly, so without database changes you can compute all that you you need to compute the new keys and you need to have like some some array where you where you store like everything that has been accessed but that's that's all tiny that's that's not a problem 
* so the problem is that we are making some things cheaper with these gas changes and that realistically requires some database changes in order to yeah 
* i mean i i agree it was a concern but i yeah that's also like one of the things i want to bring here for feedback 

**Micah**

* we could do it marius i think is suggesting which is to calculate the new gas cost and use the higher of the two so calculate what the gas cost is using the old database layout and also calculate what the gas cost will be and then just use rights of those two for each operation 

**Dankrad**

* yes, the downside of that is of course we're giving nothing when giving nothing to smart contracts developers right you might making everything strictly worse 

**Micah**

* so the second question on the shanghai plus one fork if i understand correctly every database lookup will require two reads one to read the vertical tree to see if it's present and then a second one to check the old mpt tree and then potentially then migrate it as well are we accounting for that in the gas cost the cost of the double read and migration or are we just going to say that hopefully this is uncommon enough that there's not attached by like triggering a huge number of migrations 

**???**

* as a precision you don't actually need to go through the tree right you're just you're just going to keep because the tree is frozen you can just store the data that was in the mpt as a key value store so it's still costing something but it's not as expensive as going through a tree 

**Dankrad**

* right so i mean i guess the point is also maybe to be clear here i don't think there should be two databases right so at least the data only has to be in one database like the actual keys and values like there should be maybe currently that's not the way it's implemented but the right way to think about it is i think that data and commitment scheme are two independent things and so basically there there are two different commitment schemes at that point but they aren't necessarily two different databases that makes sense 

**Micah**

* i see so the actual key values you're imagining are in a third air quotes database and then these other two databases are just like 

**Dankrad**

* basically yes and that database simply has like a little marker that says is this already in the verkle part or is this still in mpg gotcha 

**Micah**

* out of curiosity for the client devs does that align with your guys's current database layout particularly interested in ergon since i know their database is very different 

**???**

* well in aragon we have so-called plane state which is separate from the hashed state required for the merkle partition to try so we already have that in aragon and for us it will be relatively easy to implement this additional local try commitment 

**Micah**

* is that also true for the other four clients three now four?

**???**

* that's kind of hard to say i'm not sure about you know the treeing but we do have the ability to kind of swap things out as far as the underlying data structure itself so it's a real tough question for me to answer right now but we'll keep an eye on it is one of the things we're tending to modularize the same way aragon does

**Micah**

* so related to that the question will we need to have gas accounting for the migration step since i'm guessing that's a non-free operation like if something is the first time the first time you read something from the mpt tree and you need to write it to the verkle tree do we need to have that cost more gas than any subsequent reads because there is you know database work disc work and i was worried that someone could you know manufacture a a block that just does a huge number of migrations in one block and potentially blow things up 

**???**

* maybe i misunderstood but since the migration is happening offline first you can do you can get someone to do it for everybody else and share it yeah i'm not quite sure why 

**Dankrad**

* no i i don't think i don't think the question is actually about about like the third step where you say like it's good yeah i think exactly so basically like now we are in the state where you can access things that are in the merkle partition tree you can access them cheaply because they already like like for example you can write to it without it carrying the 6200 gas i guess 
* yeah it's a good question and i haven't thought it through i don't know if vitalik has because he created this the gas the ideas and gas costs 
* one way to potentially think about it is to apply the costs from the perspective of the verkle tree so if we say this guy yeah 
* we can say like if you access something that isn't in the vocal tree yet then it's a right basically 

**Micah**

* yeah basically you charge rate costs or maybe write plus read costs whatever it is 

**Dankrad**

* yeah that could be one way of doing it yeah vitalik have you thought about it i don't know she's still here i think he left 

**Tim**

* i thought andrew you had a comment about the target costs do you want to kind of bring that up 

**Andrew**

* yeah just i think because the new target costs are already on average higher than the status quo so then if we defensively make them even higher in the transition that might potentially be to prohibit too expensive for smart contracts so i'm thinking maybe if like moving if having the new target costs requires some kind of database refactoring perhaps it's still worth doing that and delay the gas cost not not to shanghai but to a later fork but probably to my mind is this some kind of database layout refactoring is a pretty much a prerequisite that's my impression

**???**

* yeah i agree

**Tim**

* yeah we're about that time what's the best place to continue this conversation Dankrad there's i think we have a channel for this on the r d discord? we have a state expiry channel right i think that's a separate, maybe we have verkle migrations?

**Dankrad**

* yeah if you look at so basically we intentionally designed everything so this is that it's independent from state expiry and address extension so that all of these can be worked on independently and they aren't blockers for each other yeah 
* so i think next steps yes so i mean i'm very happy like if anyone wants to understand more and if they want to ask any question like please reach out and also i guess maybe the big yeah the big questions here like if i would be discussing about these database changes that would be required for for the shanghai gas cost changes that we're suggesting if we can discuss that see where each client is on that and how how big those are yeah that would be great to understand

**Tim**

* okay great yeah i think we can use just the vertical tries channel here so oh yeah i'll just type the name in the chat here in case people are not on it yeah 
* yeah thanks a lot i Dankrad and guillaume for sharing and obviously working on all this any kind of final questions 

**Micah**

* anyone has any ideas on how we can do address state extension and that would allow us to prioritize state expiry and i think this proc transition process is actually significantly easier if state expiry can be done simultaneously or first 

**Tim**

* great and there is also an address space extension channel on the discord one thing i'll note before we head off at least in north america daylight savings time is changing before the next call i'm not sure about europe i think so as well but please double check the time so the call stays at 14 utc two weeks from now but at least in north america that's one hour earlier in your local time and i think that might also be true in europe yeah so please just double check that before we meet again in two weeks. thanks everybody

-------------------------------------------
## Attendees

* Tim Beiko
* Mikhail Kalinin
* Danny Ryan
* Martin Holst Swende
* Lukusz Rozmej
* Guillaume
* Alex Stokes
* Dankrad
* Andrew
* Justin Florentine
* Hal Press
* Jose
* Roberto
* Yuga Cohler
* Ansgar Dietrichs
* Corwin Smith
* Fabio Di Fabio
* Ben Edgington
* Protolambda
* Matthew Rodriguez
* Micah Zoltu
* Alex (axic)
* Pawel Bylica
* Andrei Maiboroda
* Samni Egwu
* Ognyan
* Pooja Ranjan
* Gottfried Herold
* Marek
* TurboTrent
* Terence

---------------------------------------

## Next meeting on: November 12, 2021, 14:00 UTC
[Agenda](https://github.com/ethereum/pm/issues/407)