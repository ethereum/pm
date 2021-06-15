# All Core Devs Meeting 115
### Meeting Date/Time: Friday, June 11th, 2021 14:00 UTC
### Meeting Duration: 1 hour 30 min
### [Agenda](https://github.com/ethereum/pm/issues/330)
### [Video of the meeting](https://youtu.be/XYhN26UrJ5o)
### Moderator: Tim Beiko
### Notes: Shane Lightowler


## Decisions and Actions Made
| Item | Description | Video ref |
| ------------- | ----------- | --------- |
| **Decision 1**   | Fee history to be used as default. Number of blocks for history returned to be capped at 8-10 | [33:51](https://youtu.be/XYhN26UrJ5o?t=2031) | 
| **Decision 2**   | London testnet fork blocks agreed, Tim to document | [1:01:29](https://youtu.be/XYhN26UrJ5o?t=3689) | 
| **Action 1**   | Full sync to be performed to verify EIP 3607 | [33:51](https://youtu.be/XYhN26UrJ5o?t=3186) |   
| **Action 2**   | Document EIP 3607 (not going into London) in the yellow paper so we dont forget its been implemented in clients| [53:42](https://youtu.be/XYhN26UrJ5o?t=3222) |    



# 1.London Updates

## i. Calveras status and next steps

**Tim Beiko**

* Hello everyone welcome to All Core Devs 115. I'll post the agenda in the chat here. So first thing I had on the agenda was just basically to get an update on [Calaveras](https://github.com/ethereum/eth1.0-specs/blob/master/network-upgrades/client-integration-testnets/calaveras.md)
* I know marius kind of spammed it earlier this week 
* I don't think he's on the call but yeah 
* I don't know if another another team had just like an update about I know besu and nethermind there were some things found when when marius did this test I don't know if you want to walk through that?

**Ratan Sur**

* Yeah I think we were generating blocks that were too large and so they were being rejected but we're I think everything is working now we should be fine 

**Lukasz Rozmej**

* So from the Nethermind side I know there was there are some issues that we stopped producing blocks from time to time but i'm actually debugging this today and I think I found 
a solution so I will restart calaveras validator after i'm done 

**Tim Beiko**

* Awesome and I think those were kind of the two only issues it seemed like they're anyways I didn't find anything else I don't know if anyone had had any other yeah any other things to share about calaveras 

## ii. JSON RPC spec

[https://github.com/ethereum/pm/issues/334](https://github.com/ethereum/pm/issues/334)

**Tim Beiko**

* okay so the next one it's actually quite a big one is over the past like week or two there's been a lot of conversations about json rpc and 1559 and basically it seems like there's three open questions left that I was hoping we could kind of resolve on this call 
* the first one and this was martin's so he's not here yet the first one was ETH call we can maybe skip that one and see if martin comes in 
* the second one was probably the simplest so basically the idea of adding the effective gas price to ETH get transaction receipt light client you had a pr open for that already it seemed like everyone was roughly in favor of it but we did just wanted to check here to see yeah if there was any objections or if people all thought this was a good idea
* let me post the pr here [https://github.com/ethereum/eth1.0-specs/pull/206](https://github.com/ethereum/eth1.0-specs/pull/206)
* this would just make it easier for projects who are dependent on the effective gas price they want to show it to the users and whatnot to fetch it so they wouldn't have to manually calculate it they would just be in the transaction receipt

**Lightclient**

* so I think there was a discussion a while ago either on discord or maybe in some other channel where people were saying hey maybe we just have tx.gas price be set to the effective gas price and so when you do ETH get transaction it would return the effective gas price for for all transactions because the gas price is the effective gas price today and then for 1559 transactions that would be overloaded to be the effective gas price
* so I don't know I think that might actually be how geth is currently implementing it and I don't know if people want to continue having that behavior or if if going with this pr also means to revert that and only have gas price for non 1559 transactions 
* I know some of the people in this pr specifically want to do the latter where the gas price is not in the transaction object and it's only in the receipt and their arguments are that the effective gas price is this computed property and so it doesn't it generally computed properties generally shouldn't live in the transaction return value they should be things that are sent by the receipt rpc but that's just their argument

**Tim Beiko**

* does anyone from the other client teams have thoughts on that or at least like how it know how it's implemented now in your client 

**Ratan**

* I think that second one sounds more intuitive to me as a consumer of the api since setting us the gas price seems to imply that yeah it's you know it's a field that was set in the transaction I kind of like it being separate but that's not a strongly held opinion

**Tim Beiko**

*  yeah Nethermind any thoughts 

**Lukasz**

* not really so I don't have any opinion on this 

**Tim Beiko**

* okay and yeah do you know so right now what does transaction.gas price do in besu and nethermind does it also just return the effective gas price like I guessi don't know yeah 

**Ratan** 

* I think I think we don't do either yet I don't think we return the effective gas price as the gas price nor do we have the effective gas price in the receipt yet just waiting on clarity for that

**Gary Schulte**

* yeah we have a pr for that but we're waiting 

**Tim Beiko**

* okay and like client you said geth basically already does this thing where it returns the effective gas price in the transaction.gas price so we would need to revert that in geth and then move it to the receipt right?

**lightclient**

* i believe that is but if anyone else on the gas team is here they can better speak to it jump in

**zsfelfoldi**

* yeah unfortunately I didn't really follow this particular issue so yeah I can't really add anything

**Tim Beiko**

* okay yeah I seems like the one kind of has a strong opinion on it yeah 
* lightclient since you opened it do you have a preference for and you did a lot of the work on the pr as well do you have a preference for moving it like I guess would you be if we if we just like merging your pr are you okay doing the change in geth if it needs to happen so that's it sure

**Lightclient**

* okay that's fine I think like my I don't know again I also have a strong preference but I think that the people who wanted it in their receipts brought their arguments and so you know there's no one really opposing it at the point at this moment

**Tim Beiko**

* okay great so yeah let's yeah let's i'll merge the pr in today and we can use that as a reference so that yeah the effective gas price goes in the receipt and if any implementation already has it in like the tx.gas price then we can just revert that 
* cool that's the first one
* I see martin is just joining so we can probably do the ETH call thing hi martin 

**Martin Holst Swende**

* hi sorry i'm late

**Tim Beiko**

* oh no worries yeah we were just talking about json rpc and you had posted this comment in all core devs about eth call trying to figure out how does it deal with the base fee and the gas price 
* do you maybe just want to give like a quick background about that?

**Martin**

* so background about it is that for eth call Geth and parity back and they used to handle things differently geth would use whatever the account of the node that you made the column would use that as the like the caller if unless otherwise specified and that was a pretty yeah arbitrary choice 
* Parity used the zero address as the sender and gets switched over to that as well and the problem is that the zero address didn't always have funds and as a solution for that we use the zero gas price so we can do the eth call you can see what happens and it works you we can specify any gas limit you want because gas doesn't cost anything 
* and the problem with when we do eth call on 1559 is that it has to cost something because there's a base fee and if we use the base fee we have to charge whatever it basically is so if you use zero address then you we can run into this problem that there might not be any funds
* I am not the best person to speak of how we eventually fixed it but it seems like peter is not on the call and he eventually fixed it and merged into geth 
* I think what he did if I understood correctly is that unless you specified gas and he hacked around it a bit so if you do the operation the opcode basefee you get the correct one but charging wise it will not charge
*  I can't detail it further than that
*  there's a pr which was recently merged 

**Tim Beiko**

* I guess do other teams have eth call implemented yet?

**Ratan**

* so i'm not exactly sure what we do right now I can get back to you 

**Tim Beiko**

* I think it was open ethereum left a comment on the issue saying they would like to add the optional base fee to the parameter list 

**Dusan Stanivukovic**

* current currently open ethereum uses the base fee from the block header that is provided in a parameter list when you call the ETH 
* so there's there is actually no way to set the base feed to zero 
* so if I understand correctly the discussion on the discord we want for this function h call to work in two modes - one mode is to mimic the what happens in reality when you apply some transaction on a specific block, and the second mode is to just analyze the control code I guess while assuming that the base fee is zero and the gas price is zero so just to omit some of the of the data that is not needed for that for that mode 
* so I think the right way to discuss about it is to first decide what's the actual meaning and the usage of this function should we just assume that this function is used by default that is used to analyze what's happened what have what happens in reality and then if we want to use it in some other specific way then we need to provide additional conditions through the parameter list

**Martin**

* yeah I posted [the link to the pr](https://github.com/ethereum/go-ethereum/pull/23027) that peter wrote on discord he basically says there are two major use cases that need to be covered and then he has six different tests slash cases before and after 1559. 
* it would be interesting to know when whenever you guys implement something regarding this if you guys do the same thing or if you find reason to do something else if you can just post it somewhere

**Tim Beiko**

* yeah peter's pr description there is very good it feels like it probably makes sense to use that as like a reference and if yeah 
* if teams have like some disagreement with it we can deal with it then but it seems like he's really thought all the all the various scenarios 
* okay so yeah i'll link it in the ticket and yeah if if people have issues or changes they want to make we can we can discuss them next time 
* cool and the last json rpc thing was what was... so basically there was another long conversation on the discord this week about whether we should use eth max priority fee for gas to return kind of a value for the priority fee in the clients or whether we should just return raw data and allow wallets to kind of calculate their own priority fee because it will be much simpler post 1559 
* micah had posted a quick comment on the chat kind of summarizing that you know from the last call we had with a bunch of wallet providers you know it seems like the fee history approach would be better I think there's also you know like some issues that he and others had raised in in the the call with wallets that if we go with like the max priority fee for gas api it kind of becomes a crutch and maybe wallets will like never build better estimators whereas if we just start with the fee history api yeah things you know it it kind of forces people to actually build an estimator on top of that 
* Zolt I know you had worked on the fee history api do you want to maybe take a minute or two to just kind of describe how it works and what data it returns

**zsfelfoldi**

* okay yeah so the fee history api is well yeah it's this road data approach and like I came to like this this this conclusion that this could be the best solution based on like this long discussions and everything 
* so I also had an initial suggestion that that tries to try to like give like prices as results and I think peter was also kind of opposed to it so what fee history does it basically I just just returns so 
* you can you can specify like a number of blocks how many recent blocks you want to retrieve you can also like specify that you want to so you can also select a block range which can even be an order range or it can go up to the head block or if the supply the backhand node is a miner or has a or a full node and has a pending state and even the pending state can be accessed and what it returns for each block is well it returns the base fee it returns the relative like gas used and so that's just a number between 0 and 1 and it can return multiple percentile samples of minor reward and by miner reward I mean the effective rewarded effective tip so what the miner can keep and yeah 
* so basically basically the api in the api code you can specify either one percentile number which can be zero in which case it returns the smallest smallest miner reward in a specific block and in each each specific block and or you can specify like if you specify 10 then it will return the 10th percentile calculated 
* I mean I and when I say percentile I mean weighted by actual gas used inside the block
* the call even even allows specifying multiple percentile values and then it can take multiple samples from each block because calculating this is basically zero overhead and it can be useful so yeah this is this is a basic idea 
* and by the way about the other thing the max priority fee api so I can add a little bit to that and that's basically that 
* i also now I also kind of think that maybe it wouldn't be very good to just drive the wallet developers in a way that so that they can they just use this single number suggestion because I don't think that's going to like be a good direction 
* so the reason we have this thing is that we allow sending transactions where they where the price fields are fields are not set at all so we so get has this like auto fill feature for prices and if we want to send a 1559 transaction then we have to just fill in some very dumb default
* maybe what we should do is that we should have this number for the autofill but maybe not expose it as an api function so I now I think this would be maybe the best compromise and yeah 

**Tim Beiko**

* piper you have your hand up 

**Piper Merriam**

* yeah so I have some concerns with standardizing this type of thing because it requires nodes that serve it to have access to a like decent chunk of kind of like recent history block data I guess it's not a huge chunk but i'm thinking about kind of light nodes and light nodes that want to be able to expose json rpc still and this kind of thing is going to continue to make that more complicated 
* whereas this data is servable I understand correctly from I mean it's really just aggregated data over the recent history of blocks 
* so I recognize that it seems more like a convenience api that aggregates that stuff but by standardizing it it puts like further barriers to entry in kind of putting an onpar json rpc api for light nodes so anyways just voicing those concerns

**Tim Beiko**

* would that also be true of the max priority fee api? because you I think you still need to look at the transactions in the block right?

**Piper**

* uh i'm not familiar enough with this to answer that but I assume that that might be most recent block as opposed to like significant aggregated data over large recent block ranges but somebody can connect correct that for me

**zsfelfoldi**

* you are kind of correct so correctly if we serve the so with the like currently existing guest price oracle yes we need to access a few blocks and we need to like fetch the transactions in order to extract the data and that's what the old guest price oracle does and that's what the fee history implementation also does and 
* well yeah it works for the right client obviously if you want to retrieve like a long history which you you are not forced to do you can just if you if if you just want to operate a wallet you can probably fetch the last two three four five I don't know blocks and you can do that with a light client and yeah so having an api that's theoretically serveable by a light client and with some parameters it could be like expensive and take long
* well that's true for most of our apis you can do like clash filtering and you can do a lot of stuff that can that does work with the light client and these things do work with the light client without any problem it's just, yeah
* if you retrieve like a 100 block long history which you just don't need for for wallet but if you do then it will take long time so I think

**Piper**

* yeah you can i'm totally on board with you in the in that yes you can absolutely do this stuff from from a light client context i'm just giving a i'll call this just like a minus zero small pushback on adding a new standardized json rpc api that is kind of inherently...
* maybe the concern here is that it's very much not like 01 operation time that that like you said you know logs and points like that that have parameters that users might pass into them that make it that it could have unreasonable bounds in terms of how many blocks they want to process this stuff for and things like that and that you know the end expectation for users is these things just work right like you you say yeah give me the average whatever for the last you know 100,000 blocks and the expectation is that it will return that data 
* but on some level it becomes undefined behavior because what happens if clients start even not like clients start dropping old blocks and things like that or what happens if they pass in a 10 million block range or things like this yeah 

**Tim Beiko**

* the biggest difference here is that you don't need like a very large number of blocks to build a good estimation because 1559 adapts pretty quick 
* I think it's like every six blocks you know the base fee doubles so you can see you can see with like a handful of blocks what type of like regime you're in and so and that's what you could use and set your tip 

**Piper**

* maybe something that would make me feel a little bit more like less resistant to this was if the json rpc spec had some clear bounds on like expectations for you know longer ranges into history or longer ranges of blocks or even actual upper bounds say the behavior of this is undefined above this range

**zsfelfoldi**

* that's a good point 

**Piper**

* I would love to see that for the logging endpoints to say the behavior of this endpoint is undefined above this number of blocks or whatever so yeah

**zsfelfoldi**

* yeah that's that's that's a fair point so the thing is that already the fee history spec already allows or optionally allows like giving data about the pending block which is also obviously something that light clients can do so that's also specified as some backhands might support it but it's optional and the caller should be prepared for that that it might not work with some backends and maybe we can just do the same thing with block count because it's yeah it's not a one it's all block count and we can just say that uh like supporting these four block counts larger than five or 10 is optional and might depend on the back end whether it will be reasonable or not

**Piper**

* that'd be great 
* the other thing that I might ask for here is some way for the node to signal back to the user what is allowed into this endpoint 
* so whether or not this is some sort of like meta endpoint that we start exposing that displays information that that the node can hit and say how many blocks back am I allowed to go for things like this endpoint or logs or things like that 
* because that's the other hard point here is that even if we make it clear that nodes don't support this it still doesn't really quite address the issue because the wallet software still needs to be able to somehow figure out what am I allowed to ask at this end point and just sort of poking it until it stops responding empty probably isn't very good UX
*  we don't have to solve this on this call I just wanna like drop these ideas in here because they're kind of like problems that have showed up in past json rpc endpoints

**Tim Beiko**

* I was just going to say a quick question like how many blocks do light clients typically hold on to like what's like a is it like 2 20 200 

**Piper**

* I there's no real number here but I think 256 has often been just like a sane like...

**zsfelfoldi**

* really sorry yeah so that lifelines don't really hold on to blocks by default at all so in some sense the answer is zero but they can like request it but that costs some bandwidth and time
* So yeah definitely like requesting 200 block history with a light client is too slow 
* so maybe one thing that we could do about this thing is that the call format already allows like not supporting all the data that the caller has requested because the answer contains like the first block number of the results and then the lists of base fees and rewards and everything so it's totally possible and we can just specify that the back end can any time just limit and say that okay you have requested 20 blocks because maybe the full node will serve it but the light node only wants to serve eight 
* so yeah the answer can just point to a later block as the first block and contain like eight blocks of results and I think that could also work because the caller should be prepared that okay now this backend didn't give me so much history then I have to work with what I have 

**Tim Beiko**

* and yeah yeah and that generally makes sense to me I feel like eight to ten blocks is probably sufficient until I get a very good estimation because you know if you have like yeah that amount of full blocks you know you definitely know that like you're in a massive demand spike and you'll need to put a big a big priority for you anyways 
* so I guess just to take a step back would would all the teams be okay kind of going with the fee history as kind of a default and capping the number of blocks that it returns the history for to some small number around you know like eight or ten ish
* i see a plus one from besu
* any objections nope okay so great let's do that um 
* i guess we have the spec in your gis zolt, would you be able to open a pr against the json rpc specs or should somebody else do that 

**zsfelfoldi**

* no no i will add these clarifications to the spec first about the block count and yeah then I can open a pr again 

| **Decision 1**   | Fee history to be used as default. Number of blocks for history returned to be capped at 8-10 | [33:51](https://youtu.be/XYhN26UrJ5o?t=2031) |   

**Tim Beiko**

* okay awesome thank you very much cool so I think those were all the outstanding json rpc issues I don't know if anyone is aware of any other

## iii. Yellowpaper EOA clarification / EIP-3607 

[34:56](https://youtu.be/XYhN26UrJ5o?t=2096)

[https://github.com/ethereum/EIPs/pull/3607](https://github.com/ethereum/EIPs/pull/3607)

**Tim Beiko**

* okay if not there's one more thing that came up this week with regards to how we treat EOAs and smart contract accounts which could under some very tiny edge cases have the same private key 
* I know denkarad you've been researching this and wrote an EIP about it do you want to take like a minute or two to kind of explain the problem and what you see as a potential solution? 

**Dankrad Feist**

* so the problem is the simple like an address collision between an eoa and a contract and just just for everyone who's like less cryptographically inclined to summarize like how that could happen I mean we're talking about someone specifically creating a collision here 
* so like in order to do that like for in order for that to happen randomly that would be super unlikely like it's 160 bits like 2 to the minus 160 is like a super small number that's not going to happen like we can basically assume that that never happens 
* but someone can basically use collision finding algorithms to specifically create that and like to give you an intuition like it's it's much much easier because you only need to get to the so-called birthday bound and which is like root of of the difficulty of the problem essentially so finding a collision basically what you do is you generate 2 to the 80 end user accounts and you simulate the deployment of the contracts two to the 80 times and then an expectation you will have find about one collision between these and now you see like that is obviously much much much easier than two to the trying two to 160 times 
* this very simple description obviously has a problem that you would restore these two to the 80 addresses at least for one of those two lists you generate but in actual practice that's not true 
* so there are algorithms so-called cycle finding algorithms that do this without requiring these insane amounts of memory and that basically means there's a problem now 
* and the reason that's a problem so think about bitcoin mining... bitcoin mining currently solves a problem of this difficulty about once every year so dimitri covertow which one of our cryptographers estimated this and thinks like finding one of these collisions is basically about as difficult as like one year of bitcoin mining which costs about 10 billion dollars probably like developing the hardware plus paying for the electricity and all that
* just remember that these kind of estimates are are not an exact sign so like it could easily be off by a factor of 10 either way just I just want to make clear it's not completely outlandish to think that this could happen now basically someone could specifically try to prepare this now 
* and now why is this a problem? so like basically previously like we thought about the case where okay like what you could do is you like create this collision and then you don't deploy the contract but you somehow trick a user into sending funds into it and then you withdraw it using eoa key 
* I mean that is actually I mean that is of course possible but people don't tend to send large amounts to contracts that aren't deployed yet so it doesn't seem like a very serious attack vector if you like have to invest several billion into finding that collision however like when we started thinking about this last week suddenly we found that actually even after deploying the contracts you can still do that 
* right now we don't have any protection against that like it's basically it was assumed I guess when the spec and clients were first built there this never happens and so you just yeah you just deploy the contract first and then like it could be something that looks like completely innocent like let's say like craziest example would be something like rubbed ETH or something like that right you think it's just a wrapper contract it does nothing and you can always get your e-stack well that's not true if someone had the end user account key for that contract 
* but luckily this very bad attack back that we can just stop by just like making all transactions that that have send their equals and a deployed contract invalid and that basically stops this
* in my opinion most serious attack vector and all the other ones they're still kind of annoying but but they are at least for the next few years not really practical attack vectors 
* and that's basically what this EIP does I think 3607 has been assigned to it basically I think like we should basically we might not want to treat it actually as a full upgrade we might just say well we're kind of specifying what some previously unspecified behavior was and so we say like this does these transactions become invalid and then yeah this cannot happen
* cool yeah that's the summary for my site 

**Tim Beiko**

* so thanks dankrad. I think there's also one thing worth specifying i'll let micah speak right after this but one thing we're specifying is this eip doesn't actually require a hard fork but only a soft fork because it's like a tightening of the rules that doesn't introduce any new features so you know while there might be some value in trying to like time the deployment alongside london because people are forced to up update then this is actually something that can be deployed as a soft fork at any time 
* micah?

**Micah Zoltu**

* i'm just curious what the status of extending addresses to full 256 bits is like if that's close then this feels unnecessary if that's still like a year off and it feels much more necessary 

**Martin**

* it's at least a year away would be my estimate 

**Dankrad**

* I mean we haven't really even got a proper specification of that yet right

**Micah**

* uh yeah like last unless they heard 

**Dankrad**

* I definitely wouldn't call it wouldn't call it close I think that's the open field

**Lightclient**

* this is also something that can be soft forked in and out assuming you know there hasn't been an instance of this before so it's not really an issue for some reason we reverted it when we had larger address spaces

**Micah**

* no that's true 

**Tim Beiko**

* and as I understand it it is like a pretty small implementation change right like you're just adding one check when you verify the validity of the transaction 

**Martin**

* so the nice thing about this is that in order to whenever you want to do that check you must have already loaded these this try object this state object from this we already have it you have the code hash and you can immediately check if it equals to the you know empty code so there's no extra cost really to do this check

**Tim Beiko**

* so my my proposal for this was yeah given that it's like three lines in geth and you know it is like a small change but at the same time it's not something that's probably gonna happen tomorrow you know there is still like a a pretty high pretty high like I guess hash power needed to actually exploit this and because we've mentioned in the past we wanted to see london on test nets sooner rather than later I was wondering if this is something we could add into clients basically in the mainnet release for london so that we kind of go to the london test nets with you know the fork as it's defined now
* i think in the past there's also been some concern about like accepting something the first time it's presented on ACD because you know people might watch this meeting a week from now and come up with some objection or whatnot and want to raise that so that you know if assuming like you know no one has an issue with it on the next call we could just say this is something we add to the clients before the mainnet release of london but that we don't have to delay the test nets because of that i'm curious what people think about it
* thomas is against sorry 

**Tomasz**

* i'm i'm generally against of dropping anything more to london even if it's small so even even if you find those collisions I at the moment it's it's just a question whether it is consistent behavior of all the clients or not like they just sending the transactions from the contracts is not the problem of itself right

**Dankrad**

* no it is a huge problem because you could steal all the funds like say like someone had done that for wrapped ether like just to be clear I assume it's not be done for wrapped ether because it's been deployed years ago but like if someone had premeditated this and deployed that contract with this collision then now they could use their key and take all the ether that's right now in that contract and transfer to their private account

**Tomasz**

okay so that's what you mean that it might have been planned like a launch long-range attacker 

**Dankrad**

* or anyone yes or anyone could plan it right now 
* like I mean we we thought first thought about this like one week ago but someone might have thought about it last year not super likely but there could be someone basically ready to deploy this

**Vitalik Buterin**

* yeah it's I think also important to not overestimate the ease of doing this like we are talking about to the 80 computing power which is an insane amount of computing power and like yes it would be a medium difficulty if we had asics for it but nobody has asics for this at the moment 

**Dankrad**

* so yeah I mean I generally agree that it's very unlikely that someone has this right now I on the other hand if someone could start this now that that actually there might be worthwhile like one year ago probably nobody would have done that it's just the whole ethereum network wasn't worth that much but now it's very different 

**Vitalik**

* you know just like my feeling is that the urgency is nowhere near high enough to even think about doing like modifying london to put something like this in

**Piper**

* so one easy potentially low low friction way to include this would be to get the fixture test ready for this that would it would demonstrate compliance with it and then just to get them merged after london is out so that they are already part of whatever comes next and so by the time that we get to our next hard fork after that and clients are working on compliance with whatever new versions of the fixture tests are coming out these are already part of that base and they inherently have to add it in by the time the next port gets around 

**Dankrad**

* that would be the most then

**Tim Beiko**

* not necessarily because we're pushing back the difficulty bomb to december 1st assume the merge is not ready december first we're gonna need to push back the difficulty bomb again so that means that would be like I guess at the latest if we don't do it now we'll do it december 1st roughly 
* martin you've had your head up for a while

**Martin**

* yeah I think it's important that we you know agree on this and that there's consensus that it's something we should have I don't think we need to tie it to hard fork 
* I don't think all the clients need to say yes we're going to include it for london as long as we have this agreement I think your clients can just merge it whenever wherever as they see fit as fits for their release schedule and if someone exploit this and then they pay them billion dollar for consensus issue on ethereum which I think is a nice price I think it's a decent security
* yeah so I would just if we just get agreement I think being guest would probably merge it pretty soon probably before london maybe after 
* definitely not wait another half year and to the next park but whenever we feel like it yeah anyone agree these agrees with that?

**Marius Van Der Wijden**

* so the only the only thing blocking it from from merging it right now are the state tests because a lot of state tests assume that the sender has some kind of code 
* so we need to I already rewrote the state tests so that they don't do this anymore so they can be verified with the with a new change in and I now have to write some tests basically for the change to verify that a client has this query
* as soon as this is done the problem is that we have to merge the tests before wemerge the updates in the clients otherwise the testing pipelines for the clients will fail

**Micah**

* just for clarity if we go with martin's plan are we asserting that should someone do this from here on it's a consensus failure if anyone includes such a transaction and accepts that block regardless of whether you update your client or not the right or the canonical fork is the one that does not include such a transaction is that correct ?

**Dankrad**

* so it will only lead to a consensus failure if it's not the majority mining client like that rejects it 
* otherwise the longest I would 

**Micah**

* so like let's say another mind let's say another minomundus which has I think no miners and no one else implemented it and someone exploited it another minus canonical chain in this hypothetical chain split because we agreeing that is the rule if you don't update your clients that's your problem 

**Martin**

* they would fall off so it's yeah so it's it's I mean as long as it gets exist for london problem is solved 

**Tomasz**

* like nevermind is not mining on on main net so there is no chance that this will be included in another mind against what geth believes

**Micah**

* sure so I guess maybe we're saying is guest goes first everybody else will follow and then as soon as geth implements it at that point forward that's the canonical rule set

**Tomasz**

* yeah I think it can be it can be just assumed that this is currently the role the rule it just might be by getting implemented on the clients which means that if geth follows with the change it doesn't even have to go as a heart for it because it never happened on mainnet nor we plan it happen so it can go just like as a soft update and then just geth says like and then if we failed to update very quickly then we took a responsibility on ourselves in the undermined that that we have a split that nobody will follow because geth will have overwhelming majority and that's why 

**Martin**

* I think that's what the e means I think bankrupt it didn't put you know a rule where at block number x but I mean it's a retroactive rule so it's not it's not actually tied to hard work and this is just a practical aspects of everyone are going to update pretty soon so it would be neat to get it in for them but there's no time yeah

**Tim Beiko**

*  so does anyone disagree with just you know the nature of this change that this is what we should do 

**Tomasz**

* no i'm in favor of the change just didn't want to have it as like necessarily tested change for london because that's that's what I thought would be a quite a big effort for the testing teams but i'm totally agreed that geth can go with this change that we want to go with this change and we would go with it as fast as possible just didn't want to have it officially in london 

**Tim Beiko**

* does anyone have a different position than that

**Tomasz**

* quick question did someone verify that this actually never happened this kind of transaction 

**Martin**

* We would do a full sync with merged prs and then we're done 

**Tomasz**

* yeah so I would I would like that proof that it never happened it's very unlikely but

**Martin** 

* sure 

**Tim Beiko**

* cool okay so I guess just for the next steps
* yeah so we'll do a full sync verify this never happened 
* assuming that's the case clients can implement it whenever they want 
* we agree that's kind of the general vibe that's kind of the canonical behavior 
* my last question would be like where does this get documented?
* so if you know somebody wants to build a client one year from now if this is not in london you know it'll be kind of a weird EIP that's kind of standalone that people need to know is in 
* so is there like okay so we add it to the yellow paper?

**Tomasz**

* yeah that seems like right thing

**Tim Beiko**

* okay so yeah if we can make sure to add a pr to the yellow paper as well I think that would be good just so we don't just forget that this is implemented in clients thanks marius 

| **Action 1**   | Full sync to be performed to verify EIP 3607 | [33:51](https://youtu.be/XYhN26UrJ5o?t=3186) |   
| **Action 2**   | Document EIP 3607 (not going into London) in the yellow paper so we dont forget its been implemented in clients| [53:42](https://youtu.be/XYhN26UrJ5o?t=3222) |   

## iv. Testnet fork blocks

[https://github.com/ethereum/pm/issues/245#issuecomment-832122309](https://github.com/ethereum/pm/issues/245#issuecomment-832122309)

**Tim Beiko**

[54:20](https://youtu.be/XYhN26UrJ5o?t=3260)

* cool anything else on that okay 
* so I guess lasting related to london it seems like we're you know in a pretty steady spot i'm curious you know when if teams feel like they're there they know when they can have a release that they would be confident for to fork on the test nets there's like a few outstanding json rpc issues i'm not sure if they're all kind of must-haves for the test nets how do people generally feel about that?

**Martin**

* i think we should not wait with the testnet deployment due to these rpc issues and I mean jason rpc are part of the ux and yeah it's just good to continue developing the ux on the actual user-facing network

**Tim Beiko**

* okay does anyone disagree with that?
* in that case when the clients think they can have a test net release out is it a few days, a week, a couple weeks?

**Ratan**

* tuesday

**Matin**

* yeah I have not talked to peter about that but I believe we can do our next week about 

**Tomasz**

* somewhere next week not exactly sure today 

**Tim Beiko**

* okay so you know if I guess does any client team feel like they could not have a test net release sometime next week?
* so you know next week that'll be basically like june 15th 
* I guess depending on how much time we want to give people to fork the test nets we could probably we already have like a blog post ready that that explains all that we just need to fill in the client versions 
* there's 10 days after kind of the the releases are out seem reasonable to people for the test network to have the first test network to happen?
* and then they would be kind of scattered over uh one per week after that
* okay plus one from besu
* two plus ones from besu and Geth feels good 
* okay from guess so let me share my screen here so I basically put [this together](https://github.com/ethereum/pm/issues/245#issuecomment-832122309)
* ropsten's a bit tricky to find a fork date because the the blocks are so high that if you need like a palindrome block it's hard to get but we could probably go with the later one where if we forked robson on block 104 99 401 that would give us that would be a thursday so we can either get the tuesday or thursday thursday is probably closer to 10 days whereas tuesday is probably closer to eight days um yeah that would be june 24th and then we could have you know the two the two other test nets one week after each 
* we mention before we didn't want to set a mainnet block for now because we want to see how it goes on the test net so we we don't have to add that into clients 
* but would people be okay with kind of having these three days for the test nets so june 24th june 30th and july 7th?
* and yeah there's a comment in the chat that none of these scenarios have july 14 on the main net for sure we probably won't get a main net fork one week after the last tested fork so yeah 
* it would be later than that and you know I have some tentative blocks here but like those are not final depends on you know what happens on the test nets and whatnot 

**Martin**

* so ropston and gurley are both multi-client testnets and currently are there any other clients can get that does ranking 

**Tomasz** 

* so another mind can synchronize ranker b but i'm not sure if people are running actively we may be running one ring kobi node just to confirm that it's always fine 

**Martin**

* well at least there are I know that brinkley is all the sealers are guests

**Tomasz**

* we always during the forks we always run the rinkby node we fully sync it and then we go for the through the fork so that's for sure happens but we don't draw 

**Martin**

* I didn't mean that you didn't mean that you were lying but this meant that all the sealers are death so for 1559 it won't be very interesting from a ceiling perspective
* yeah i'm just thinking if we...

**Unknown**

* do you want to add another mind node as a sealer to rinkby 

**Martin** 

* yeah sure but we can take that plan 

**Tim Beiko**

* but I guess martin was your point that if it's only get cedars we could do rinka b earlier or later like 

**Martin**

* yeah well it it it kind of looks like it was building up in in priority I mean ropsten is the most throwaway we do that first 
* and it looked a bit odd to me that we do goerly and then rinkeby instead of rinkeby or maybe even ropsten and rinkeby at the same time then do goerli because
* i kind of thought that goerli was the more used well-used and high higher more valuable network but I don't know yeah 

**Tim Beiko**

* I think that's that's probably a decent assumption I guess one of the reasons why maybe I would put it first is because it's most used we probablywant to have more data on it right like we want to see more usage but you know I it's not very 

**Martin**

* i think it's fine as it is 

**Tim Beiko**

* okay does anyone else have thoughts comments if not we could go for like these basically these three blocks at the top i'll post them in the chat and then the discord yeah any objections to those ?
* okay great 
* so yeah i'll make sure to share that and then i'll follow up with the different client teams next week to see when the releases are out and when they are we'll put out a blog post to link everybody to the right releases for every every client and just to make this clear to anyone listening none of these releases will include a main net fork block so that means that there will be another release that download if you're running only against mainnet this one won't have the london fork activated 
* we'll figure that out at a later date once the first test net has forked
* that's everything I had for london was there anything else anybody wanted to bring up?

| **Decision 2**   | London [testnet fork blocks](https://github.com/ethereum/pm/issues/245#issuecomment-832122309) agreed, Tim to document | [1:01:29](https://youtu.be/XYhN26UrJ5o?t=3689) | 

#2 Other discussion items

## i. EIP-3074 audit report

[1:02:32](https://youtu.be/XYhN26UrJ5o?t=3752)

**Tim Beiko**

* if not so a few I think months now ago a light client discussed eip 3074 on this call and people wanted to see an audit for it to better understand the security implications 
* so that's been done and yeah the auditing team is on the call with us today they wanted to give a quick overview of their findings 
* so yeah maybe lightclient do you want to start by just giving you a quick recap of what 3074 is and the context there and then we can move to the audit 

**Lightclient**

* yeah that that would be great thanks tim yeah so if I could just briefly recap for people who haven't been following us closely and may have forgotten what 3074 does 
* 3074 introduced two new opcodes auth and authcall
* the auth opcode accepts a 3074 signature and it returns the address that signed the 3074 message 
* additionally there is a new context variable in the current frame of execution that allows the executing contract to then make arbitrary calls as the recovered address 
* and because the caller opcode is kind of a de facto mechanism for authenticating users and smart contracts that allows that essentially allows users to delegate control of their accounts to certain smart contracts
* so we refer to these contracts as invokers because they're the they're the contracts that are invoking auth and authcll opcodes and 3074 messages and signatures are domain bound to these invokers 
* and this helps protect users from replay attacks that might be tried to have their messages replayed on other invokers 
* and so this basically means that all the security functionality is implemented in the invoker contract and it's sort of a extension of these like protocol security in that sense 
* and this presents some some interesting security challenges which is why we've had some of these teams do these audits 
* we believe that like safe invokers can be written even if it's a small number of them and that with wallets having allow lists to avoid social engineering attacks that 3074 can be safe 
* even with these security challenges I think the 3074 is really important eip to consider including because it does allow for many desirable constructions and a couple good examples of their of those are 
* it allows for generalized transaction batchingfrom eoas 
* it allows for sponsored transactions that allow people to pay with tokens not other than eth 
* you can do social recovery mechanisms for eoas that can be signed off chain and then only be played on chain whenever the social recovery needs to happen and you can minimize on-chain accounting for state channels 
* and these are just the things that you know kind of we've thought of andthought that would be useful but I think that because it's such a flexible primitive that it does allow for a lot of other things that I think people will come up with in the future
* and so because of these unique security challenges we've been working with ethereum foundation to have the spec audited and there are two main components that we wanted to focus on 
* the first was an audit of just the specification itself in general, trying to think through the things that could go wrong, the security concerns that arise just from the spec and that has been completed by leased authority and i'll have them share their fines in just a minute 
* the other component that was really important to audit was there is a small part of 3074 that creates a breaking change for mainnet contracts and we really wanted to have this auditing from dw look into this and see how our mainnet contract is going to react if this change is included 
* and I want to stress that that this breaking change of 3074 is something that's optional the 3074.
* it does provide the nice functionality of allowing users to send 3074 transactions themselves without relying on some sort of sponsor system but 3074 without this change does not present breaking changes and I think it's still incredibly useful to have because it does allow for all these transaction batching sponsored transaction mechanisms
*  so just keep that in mind as they're discussing their findings 
*  so if there aren't any questions on 3074 specifically I can have the least authority team talk about their findings in their audit
*  okay yeah at least authority you guys want to go ahead and share 

**Nathan**

* yeah great yeah thanks like client and thanks for the opportunity to have us work on this it was a nice experience with the quilt team you're all very helpful and we had a good month talking back and forth about security around this 
* this is a bit of an interesting audit since it has a lot of potential things that can go wrong from the surface level this you know looks like opening up an account to the entire possible world of smart contracts and leaving yourself vulnerable to any random execution 
* so just to quickly go over our structure and what we looked into we we looked at you know current breaking changes as you had mentioned you have the do bob team working on checking the message.sender equaling tx.org assumption for the frame of execution and the use cases for that being used against flashlight entries 
* we looked at the signed data security what is actually being signed the type prefix the importance of including the invoker domain and why that's necessary and the address manipulation possibilities social engineering attacks on that incomplete fields maybe in the commit do 
* we looked at are there enough fields in the signed data to assume that this is reasonable went further into some replay protection looked at human readability of the signatures and decided that this was a concern for the wallets 
* we looked at the implementation security of invokers trying to reason about if it's possible to create such a trusted and important piece of contract code 
* we kind of did some brainstorming on all the ways that invokers can go wrong we kind of made a list of potentially bad invokers and how easy it is for an invoker to do the wrong thing which again stresses the importance of creating correct invokers and really spending time to make sure that these pieces of code are doing what they're supposed to be doing and you'll see that stressed throughout our findings.
* In our report we think a little bit about the permanent authorization aspect of this where you are signing your account to a piece of code and this piece of code will have that signature potentially forever 
* this is comparable to infinite approvals I think that that's kind of a good way to sort of think about these invokers and compare and contrast to that situation and infinite approval can be unapproved but an infinite approval is still infinite and the damage is going to be done if it's if it's taken advantage of 
* we look at wallet implementation security because this is particularly important since wallace will be in charge of securing these invokers or making sure that signers users are signing the correct invokers and this idea of allow listing and creating a set of invokers that the community and wallet implementers consider to be safe we find that very important 
* we looked a bit into the relationships the self-sponsoring case and the meta transaction sponsored case sponsor-responsive relationship and any potential pitfalls that that may create you know distributed network concerns similar to a gas station network and in those areas and 
* we have our general you know conclusion that I think is similar to some of the community members we independently came to the conclusion that an invoker is a sensitive piece of tooling and it's going to require a lot of care but if the if the rights implementation is created if they are perhaps simple enough if they are verifiable if they can be formally verified if if we are confident in their correctness then then these things should be able to make their way into a hard-coded list inside of wallets and you can sort of view these more as an extension of your wallet than giving total access to all of the contracts that you may be interacting with 
* um and I think it was dan finley on the ethereum magicians forum made a pretty cool post about how you can sort of view an invoker contract as you know giving specific access it's giving more functionality to your eoa if done correctly and this can bring about some positive changes in the current way that we are doing both meta transactions and infinite approvals 
* if if we can bring them to a central point then we can have more confidence and correctness that might bring up concerns about central points of failure the attack surface or the consequences might be more drastic if a single invoker fails and it's attached to a lot of accounts 
* however it's also a positive if you are able to trust that source is valid you don't have to rely on every application implementing something like infinite approvals correctly 
* so in general we think that this if done correctly they've taken time and if the right use cases are implemented and wallets implement only the right use cases that this has some net positives for security
* yeah that's I think our final conclusion

**Lightclient**

* thanks for sharing that nathan 
* I don't know if anyone has any specific questions for nathan or I think ryan from lisa thor is also here one of the other auditors but we also have the dedaub team here to discuss their findings so i'm not sure if it makes more sense to just go ahead and have them discuss and at the end have questions for both or if people have burning questions right now

**Artem Vorotnikov**

* so I have a question so basically the solution to your solution to the social engineering issue is the invoker whitelist is it correct in the words?

**Nathan**

* correct yeah the white list is very important and so I think that is the point that that allow list might reduce some of these fishing attempts that could be spread across multiple applications

**Artem** 

* okay and how are we going to call that white list? ethereum banking charter?

**Nathan** 

* that's a good question so that I believe would require some effort between the wallets and yeah I think that's a good question it's important that consensus is achieved and I think that it's a it's a very sensitive piece of code that needs to be done and implemented and white allow listed correctly right that is a good question 

**Lightclient**

* I actually don't think that it's something that has to have consensus
* yeah there's something that needs to be necessary consensus across wallets it's something that as a wallet you can you can say i'm going to allow this invoker not that invoker and then you can tell it to advertise this to your users as this functionality and you say look this wallet can do these sorts of batch transactions because we've done the work to make this invoker trust this invoker and that other wallet you know they have more features but they're trusting an invoker that's insecure and you know it's something that wallets can decide on their own time

**Ratan**

* in practice you can get convergence here as people try to avoid blame for you know like leaving the approved set and now you've got a relatively stable equilibrium of you know rent seekers so it's not a great look but yeah 

**Martin**

* it's I mean you you obviously trust the wallet provider with your private key
* so if you also trust them to tell you what which ones of these contracts are safe to interact with I don't think that's a big change

**Artem**

* um there are cold wallets too which you do not trust with your private key 24 7.
* it's basically it is you have to issue the transaction to do something now with the new mechanic it can be done for you at any time forever so it seems like the recreation of the banking system basically

**Martin**

* if you're a technical user you can make this kind of signature with your cold wallet or you can choose not to do this kind of signature right?

**Micah**

* yeah it's totally opt-in so if you don't want to use 374 wallets you definitely don't have to there's there's no automatic anything here

**Ansgar**

* yeah I think it's really best to think of these as like opt-in extensions to wallets and there will be standardized some standardizations so like you see like where basically there's probably one one specific implementation for for a simple bundling invoker or something just just so it's easier for for kind of wallets to kind of maybe expose an api that that tells the website if it supports the bundling or whatever but it's always just like opt-in functionality extension that that's all it is really

**Lightclient**

* we only have 15 minutes left I also want dedaub to share their findings and have a chance to answer questions so be honest if you want to go ahead

**Yannis Smaragdakis**

* sure so just to set up the context again we just did the analysis on existing contracts like the impact of 3074 actually the optional part of 3074 on existing contracts and the biggest impact to refresh everyone's memory is that tx origin equals message sender is no longer a reliable distinguisher of voas so anyone can impersonate message center
* so that's the biggest threat because this is being used in practice and we try to quantify how much it's used in practice and to also inspect both prominent and randomly sampled code and see what the expected impact might be for existing contracts again so there are lots of details in the report so I do invite you to have at least a quick look at it
* there was there were lots of automated analysis both at the syntactic level and the byte code level and semantic automated analysis and then extensive human inspection of pretty well-known protocols
* bottom line certainly it affects a lot of code I think that doesn't come as a surprise 
* probably it affects around we we sampled around 1.8% of actively transacting contracts right now have some kind of check that combines tx origin and message center 
* now does that mean 1.8% of the contracts are actually affected actually probably not in most of those contracts there are comments from programmers that say just to be extra safe or we know that this can be front run but I why not check for eoas
* some people certainly are not aware that there are issues already regardless of 3074. now what are these issues with nav kind of deals anyone colluding with a miner can actually exploit contracts exactly the same way so is this code already vulnerable it depends on where you think mev attacks are going to go in the future and i'm not sure if people have a formed opinion on that already or they'd like me to elaborate on that but let me get back to the main story 
* there is a significant impact
* we actually think that such code is already kind of half broken that it's not going to stay safe for much longer
* we think that the kind of mev attacks we're seeing they're becoming very sophisticated they will soon be proactive so 3074 is not actually going to break a lot of code badly not any more than code would be broken anyway so that's our subjective opinion
* at the same time we tried in the report to be to very clearly separate subjective opinion from objective fact so there are measurements that are objective fact and subjectively we assess that the risk is not that much greater than mev 
* so I can't fully keep up with chat questions let me try to sample a few
* how would the mev attack work? so current mev attacks they wait for a transaction and then they send you it they wait for a uni-swap swap for instance and then they sandwich it.
* future mev attacks could very likely have combined some analysis of vulnerable code that checks tx origin equals method sender so it can right now it ca only be called by an eoa and the moment they find such code and they find a vector to exploit it they issue atomically the exploit transaction first like they borrow from the miner they tilt the pool and then the attack transaction they make the victim contract lose money by calling the code that has that nested sender equals dx origin 
* so that would be a proactive mev attack that we think there will be coming within the next few months
* mev attacks have become very sophisticated already so I think I gave a quick summary maybe it was too quick and maybe I can go over specific topics if people have specific questions 
* is there something that you'd like me to elaborate on or should I go through the chat and try to read questions linearly

**Micah**

* you can ignore the chat I think just discussion mostly 

**Yannis**

* so just to add we did sample a few protocols we did sample some of the most prominent protocols inspected the code most of the uses of the guard comparisons of tx origin method center are for flash loan protection there are other uses like for instance for pricing there are services that give away their their services for free to eoas but they don't want to give away everything to a contract because a contract can aggregate lots of customers
* so that's one concern there was also a pattern of avoiding briefing attacks like making sure that nobody can turn down receipt of if because they are an eoa but all of those are secondary patterns the primary pattern by far has been flash loan, protection price manipulation protection that's the primary reason why people check that whoever called a function is an eoa and not a contract 
* reentrancy was a major concern. we found zero evidence of use of reentrancy maybe one contract maybe gsn actually becomes re-entrant if that guard is removed that was the only instance we found in both automated analysis and manual analysis 

**Lightclient**

* thanks, you guys did a great job on the analysis does anybody have any further questions for leased authority or dedaub on their audits

**Tim Beiko**

* i think you shared a [link to the full audit](https://docs.google.com/document/d/1itvPn7BhZ9N8h27d1Ig5C86_FZpyG5_cdpsuPJYmb-o/edit?usp=sharing) by dedaub on the on the issue from here for the call the first comment so if people want to read the whole thing it's available there and then the lease authority one I believe yeah will be published shortly is that right?

**Lightclient**

* yeah 

**Martin**

* yeah I don't have any specific questions I just want to say I think it's I think it was a nice approach that was done here where one one approach being just a kind of theoretical thinking about it and modeling it and the other being more practical hands-on static analysis 
* i've been skeptical about it and yeah I can't really stop it anymore so I guess I yeah 
* I no longer object to it if we had done two security reviews and both are kind of positive against it towards it 

**Ansgar**

* so i'm of course in favor of kind of bringing this domain it but I also think it is dangerous to kind of just do this by attrition so I would be hesitant to kind of go go ahead with changes even even if there's not no no kind of very specific objection but if it's still kind of if people are still generally concerned on some level um
* so i'm just wondering what what the best kind of path forward here then is would like for example i'm not sure of course might be only one of the people kind of concerned about it but I think one of the most prominent ones 
* so like do you like would you for example be willing to maybe sit down with us sometime try and really kind of hash it out and see if if if kind of we can find any specific concerns or if we maybe can I don't know alleviate some of your concerns or I don't know 
* i'm just kind of very hesitant to just kind of again to just basically go over something because we try it often enough to make people just not want to reject it like just keep giving up on the objections kind of that makes sense

**Martin**

* it's a bit late on the call now but yeah I mean we're going to talk about our future calls right because now we passed the security phase the security reviews that we said we were going to do and I guess that's some future call we'll discuss when or if to include it if or when 

**Lightclient**

* sounds good

**Tim Beiko**

* yeah and at least give you know weeks if not maybe a small number of months for people to actually read the reports and you know comment on them and whatnot

**Lightclient**

* so I don't know if they're like you know what is a good path forward for 3074 from here and like what is a good timeline to again discuss potentially scheduling because 
* I think there is quite a bit of value in having a reasonable amount of lead time because these invokers if this does go to maintenance and focus need to be developed and audited thoroughly so it's not I mean it's not critical but the sooner that we could say this is scheduled the sooner we can start building and auditing things and that means the sooner the users can utilize them 
* so I don't know if we want to plan for you know maybe like one month time 

**Tim Beiko**

* yeah I think maybe like taking a step back beyond this EIP you know once london is kind of out and whatnot you know possibly in around one month or so we should have like the main network out and at that point we're kind of just waiting I think there's like the meta question of like okay what are we doing next in general after london you know will we have like shanghai before are we gonna try and have the merge you know and what's even there so at least to me it feels like that's kind of the thing that needs to get resolved 
* if we if we think we are going to have like another fork on the execution layer this fall before there's a merge then we're going to need to start playing that one and then it would make sense to obviously consider a 3074 
* if we think on the other hand you know like we might actually not have a fork before the merge and have the merge first then I feel like it kind of pushes back those discussions
* to me that feels like the biggest like decision point

**Lightclient**

* okay yeah I mean these things are things we can discuss in future meetings 
* yeah I just want to say like one last thing on 3074.
* i've had the opportunity to talk to a lot of prominent developers and teams of the application layer who aren't generally representing this call and there's exceptional interest in the EIP on their side and you know I can help if people are unsure like who wants to do and how are they going to use it I can happily connect people with prominent teams to see like you know why they want it and how they're going to use it 
* so I just wanted to share like my experience with talking with application developers and make sure that their voices are heard on all core devs regarding the eip

**Tim Beiko**

* yeah I i think that's helpful yet to have that context because it we are sometimes pretty removed from like the end users and how they will use this and I agree there's been like some like there's been a lot of enthusiasm by app developers for for this 
* Ansgar asks in the chat what are the latest chances for emerge this year with three minutes late left i'm not sure you can speculate on that
* uh marius you have your hand up

**Marius**

* yeah so I don't think we should we should speculate on on merge times 
* and also I don't think we should take the application land into account in this decision 
* I think this should be a decision that we make about the security and if it if it's secure if it breaks stuff and this should not be driven by applications wanting to spend less gas or something 

**Lightclient**

* no I 100% agree more it's just a motivation for people to try and figure that answer out sooner than later
* you know if there is no interest in the EIP then maybe people don't look at it but i'm just trying to convey that there is a lot of interest and I would like us to figure out is it secure you know we did these audits and there's a lot of text now to determine for core developers to determine their own and so that's really the yeah 
* I don't want to push something through that's not that's insecure or leaves things in a bad place 

**Arteum**

* my suggestion would be to come with a better answer to the social engineering issue than ethereum banking charter with 

**Lightclient**

* the ethereum banking charter is not an answer that's 
* i'm not sure where you're getting this from this this is something that wallets will decide it doesn't have to be consensus among wallets
* it's can you can think of it like a an additional module on a wallet and you might choose to use one wallet over another because of functionality and so this isn't something there's no charter there's no you know community that has to say this is what we think is the best and here's like a voting process now it's just i'm going to use this wall because it has these functionality and I trust that it's going to do it's safe and if it doesn't then i'm not people won't use that wallet that's the most important thing all to have is the trust of their users

**Tim Beiko**

* um yeah we're kind of at time but clearly yeah we're gonna need more discussions about this in the future 
* there's two announcements that people wanted to make before we we cut off so one I see run in you're on this call and you post it in the chat that goerli  seems to have issues I don't know if you want to like take a minute to just kind of explain that I don't know if you have a mic - oh lucas you have your hands up I don't know if it's about the same thing

**Lukasz**

* yes we are syncing our note to produce a correct block I think it should block it I hope 

**Tim Beiko**

* okay awesome and then lastly pooja you had one
* the cat herders are working with nethermind on the survey. do you want to take a minute to just kind of walk through that 

**Pooja Ranjan**

* yeah sure thank you tim 
* so ethereum cat herders in association with nethermind team is conducting a survey on ethereum blockchain users and developers 
* research to better understand the future requirement of client developers in terms of tools and documentation 
* we thank everyone who already have responded and this list includes ethstakers community, the developers and researchers, and most if you haven't done it already consider responding to the survey if you are any anyone who is running ethereum 1.0 node 2.0 validator node and otherwise contributing to blockchain 
* it also includes hobbies minor wallets and launching projects because this survey is going to help us create a better infrastructure for the ethereum ecosystem we are we will be sharing the responses received in a form of report in the month of july 
* the [survey link](https://docs.google.com/forms/d/e/1FAIpQLSeugRHv93fizew0zeqXFOOnQIbjbWnVHoThLJR3f3g6gVvXhQ/viewform) can be found in the ACD 115 agenda. it's there and also at the cat herders discord 
* responses are accepted till june 30th midnight PST. Consider responding, we need your feedback to let everyone know what is needed in the system to improve it, thank you very much

**Tim Beiko**

* cool anything else anybody wanted to bring up in less than a minute?
* if not well thank you everyone yep see you all on the next call.

-------------------------------------------
## Attendees
- Tim Beiko
- Ratan Sur
- Lukasz Rozmej
- Lightclient
- Gary Schulte
- zsfelfoldi
- Martin Holst Swende
- Dusan Stanivukovic
- Piper Merriam
- Dankrad Feist
- Micah Zoltu
- Tomasz Stanczak
- Vitalik Buterin
- Marius Van Der Wijden
- Nathan
- Artem Vorotnikov
- Yannis Smaragdakis
- Ansgar Dietrichs
- Pooja Ranjan

---------------------------------------
## Next Meeting
Ethereum Core Devs Meeting #116, June 25th, 2021 @ 1400 UTC

[Agenda](https://github.com/ethereum/pm/issues/337)






