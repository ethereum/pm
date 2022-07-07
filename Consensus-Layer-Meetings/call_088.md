## Meeting Date/Time: Thursday 2022/6/2 at 14:00 UTC
### Meeting Duration 1.5 hours
### Meeting date and time
### [Agenda](https://github.com/ethereum/pm/issues/536)
### [Audio/video of the meeting](https://www.youtube.com/watch?v=4oI48BEijVw&t=15s)
# 1. Merge
 ## Ropsten deposit tracking
 **Danny:** [This](https://www.youtube.com/watch?v=4oI48BEijVw&t=15) is issue 536 on the pm repo consensus layer call 88 we'll focus on the merge talk a little bit about the reorg um that happened on my birthday and um then open up this is any other discussion I want to handle um okay cool so merge we have a number of agenda items um first of all can somebody give us an update on what's going on with ropsten deposit tracking and if this has if this is isolated to specifically what we're seeing in robson or if instead this is some more fundamental issue that we might see on mainnet or might see during the merge or anything like that who has the update on this

**Paul:** [paul](https://www.youtube.com/watch?v=4oI48BEijVw&t=72s) from lighthouse here I know we had some problems on our end due to the really long block times up to like a minute or two I think um so we were kind of voting on some old blocks so um not a threat for mainnet unless the block times get to be in more than a minute or something like that um we've got a pr up that solves this moves to a kind of a more dynamic approach in building a block case similar to what tekku does I think that it's looking good on robson now um so that'll be in the next release got it 

**Danny:** [okay](https://www.youtube.com/watch?v=4oI48BEijVw&t=98) and the player comes really long on robston because of the amplification of the difficulty in the prior week and then it slowing down again

**Paul:** [i'm](https://www.youtube.com/watch?v=4oI48BEijVw&t=122s) not sure exactly why I would assume that's the case I haven't I haven't looked into why i've just been kind of fixing the what happens if

**Tim:** [why](https://www.youtube.com/watch?v=4oI48BEijVw&t=133) do longer block times make things worse like I naively I would assume shorter block times would obviously make things worse because like it might be harder to catch up or to follow them but like i'm curious what is the why isn't I guess why do longer blog times not make it actually easier to track the head like what is the thing that breaks or 

**Danny:** [it's](https://www.youtube.com/watch?v=4oI48BEijVw&t=155) not trashing the head it's tracking a depth and then we have to agree on on this depth and the depth is based off of time oh time stamps so that's going to be at least the the the grounding of the reason and maybe there's some sort of assumption incorrectly being made paul was there some sort of assumption correctly being made **Paul:**yeah that's right um just I guess trying to avoid um unnecessarily downloading blocks so you make some mishaps and it's about block time so you don't have to download all of them um yeah that's right 

**Danny:** [oh](https://www.youtube.com/watch?v=4oI48BEijVw&t=191) I got you okay so there's like a certain range that you're you're you're like it's got to be within this range we're going to download those blocks and not more but then that assumption failed guys

**Tim:** [yeah](https://www.youtube.com/watch?v=4oI48BEijVw&t=207s) I think we had a tolerance factor I can't remember what it was but um we're well outside of that got it yeah that okay that makes sense and was this a lighthouse thing or is this like a beacon chain spec thing 

**Paul:** [at](https://www.youtube.com/watch?v=4oI48BEijVw&t=221) least for us it was a lighthouse thing the way that we were doing the caching um I think there might have been some other clients who are having having issues as well but I can't I can't speak to that 

**Terence:** [yeah](https://www.youtube.com/watch?v=4oI48BEijVw&t=236s same with prism as well we have adopted a similar approach as everyone and the face has been pushed into our product cluster 

**Danny:** [right](https://www.youtube.com/watch?v=4oI48BEijVw&t=246) so this is not a spec issue per se this is a you know an assumption around what you might see in the wild that then was broken more of an engineering assumption

**Paul:** [yeah](https://www.youtube.com/watch?v=4oI48BEijVw&t=265) that's right I think what's worth mentioning as well is that f1 we we call it voting so it was is um for better or worse just kind of it's always been a little bit a little bit wonky of room kind of it's got room to move room to be wrong so it's been a part of the code that hasn't received um the same attention as say what an incorrect state route might receive um so yeah it's I guess it's worked it's it's always worked well enough for mainnet and um it's been the case that when block times get really weird and wonky um it's something that we can release a patch for um so yeah it's kind of one of those flexible parts of um of the code but clearly we could have done better

**Danny:** [okay](https://www.youtube.com/watch?v=4oI48BEijVw&t=328) I think there's certainly a desire to simplify this mechanism um and in doing so potentially make it a faster mechanism um you know now that we are much more tightly coupled to the execution there um I this isn't a merge discussion but I think it's something that myself mikhail and others want to spend some cycles on thinking about um because it's actually been when something goes wrong on a test net or even main net you know it's a likely culprit should say assign if there's some unnecessary complexity here intend to just confirm that the disappearance of the high hash rate hash rate is probably still affecting block times there okay um anything else on robson deposit tracking its impact on robson beacon chain sorry bobstone um or any of the or main net are we good in this okay great 

 ## Sepolia beacon chain launch date
**Danny:** so the next thing is we need to launch a sepolia beacon chain it's generally there's an issue standing on the pm repo um I just updated this morning based off of the conversation we had maybe a month ago about keeping it the validators small validators that small and generally permissioned um and utilizing that I think we just need to agree on the final parameters and get this thing launched and I think there's also general agreement amongst the people that i've spoken with that launching it sooner rather than later just for the best so that we are just generally prepared for sepolio perry is out I think perry would when he comes back and help us finalize some configs is there any reason not to do this in the next two weeks okay 

**Tim:** [not](https://www.youtube.com/watch?v=4oI48BEijVw&t=471) exactly that but one thing also we mentioned on awkward devs is um we should launch a separate speaking chain and run it through altair asap but not necessarily belatrix so that it's in the same state as like mainnet and and and we kind of work through the process 

**Danny:** [yeah](https://www.youtube.com/watch?v=4oI48BEijVw&t=495) I think probably all in agreement on that okay so when um perry gets back we'll propose a date and a config that'll be approximately in the next couple of weeks and get it up the I think the validator set size is going to be on the order of a couple thousand and permissioned okay any other things on would that be the secant chain terence I think i'm in charge of naming beacon chains 

**Ben:** [can](https://www.youtube.com/watch?v=4oI48BEijVw&t=530) I just clarify not on naming um have we decided gurley um prata merge before sepolio or sipolia first because i've heard both recently yeah

**Tim:** [so](https://www.youtube.com/watch?v=4oI48BEijVw&t=554) the rough feeling that I had was we would do gordy first and the reason there was um we will get more like data out of gordy because it's like a network with more activity there's more people running validators on prater um and I think maybe the the only argument I could see for doing sepolia first if we if we did is like if we do sepolia perhaps like when we're not quite ready when we don't have code that's like quite ready for mainnet but we do want to get another test that run in somehow um and and because it feels like gordy what goes on gordy should probably be like extremely close to what goes on mainnet because it's like what most users will use um and and test on so that's like the only reason I could seem to do support before is if we want another run on a test net with stuff that's maybe not quite ready to find that yet 

**Danny:** [yeah](https://www.youtube.com/watch?v=4oI48BEijVw&t=618) I find that argument compelling um actually just to be able to kind of keep things moving and save orly for I mean no matter what the last test net is going to have the code closest to what's aro und the main net um so I I buy that argument and I we do do gorly and main net shadow forks um which help us understand some of the things that come out of that obviously something you mentioned was actually having a much more open validator set and having validators and stakers actually test this stuff at scale um that's definitely one of the big things that comes out of gourley 

**Tim:** [right](https://www.youtube.com/watch?v=4oI48BEijVw&t=661) so it's like we've had and we've had that for erupting as well so sepolio will be the only one where we don't have like community validators

**Paul:** [i](https://www.youtube.com/watch?v=4oI48BEijVw&t=677) also like the idea of um pushing goalie to afterwards to give us a little bit more time and make sure that the code is close to reduction

**Arnethduck:** [I](https://www.youtube.com/watch?v=4oI48BEijVw&t=700) like the idea but I wouldn't want to sign up for a guarantee that the release would make for girlies the exact same release that we later recommended for mainland

**Tim:** [oh](https://www.youtube.com/watch?v=4oI48BEijVw&t=708) yeah I don't think you'd want to guarantee that but I think you'd want high confidence that it's as close you know um yeah but but we definitely would not like frame it to users like download this for both gordy and mainnet

**Danny:** [yeah](https://www.youtube.com/watch?v=4oI48BEijVw&t=739) agreed all around I saw america a thumbs up as well um was this touched on all core devs last week not the order no okay we can do um maybe do a round of communications over the next few days and just see if we do want to swap I guess there's nothing been quite official here but nonetheless I think we should get this polio beacon chain out soon just so that it's out and ready for our use no matter the order okay we'll circulate a suggested date and configurations um probably in about a week when perry gets back and we can kind of finalize that 

## Ropsten ttd

**Danny:** okay something perry pink me about this morning was robson ttd and discussions around that and the choice of that I think we tim we need to choose that monday so we need to choose that now 

**Tim:** [no](https://www.youtube.com/watch?v=4oI48BEijVw&t=802) we need so I think I have a very strong preference for a number um so the thing I think yeah the thing I think probably makes sense is um picking a number and we've had someone on our team at the ef mario look into that um communicating that number with the folks who run validators like on the client teams and and on the testing teams making sure all those are upgraded and then basically publicly communicating the number so that in the worst case you know it doesn't affect the network if somebody decides to mine upload the wickfctd um so my so I guess what I would suggest is like um we have a number suggestion and and like some hash rate assumptions around it right after this call we can send it to all the client teams to make sure that there's no major objections um and then once once the latricks hits which is tonight like in I think like 10 hours or so from now um then we run a ttd override on the validators that are controlled by by client teams and and the ef um and then tomorrow basically like exactly 24 hours from now we publish this number so everyone has a chance to upgrade um and then obviously as soon as we published number there might be some incentive for people to mine towards that um we've purposely chosen something that like gordy should not hit by next week but that we can then rent hash rates to accelerate ourselves um so the goal would still be for it to be hit you know sometime late next week um but like given the current hash rate on gordy it's it's it's targeted for much farther than that

**Danny:** [okay](https://www.youtube.com/watch?v=4oI48BEijVw&t=930) so the quick on that is we plan on circulating a number today and to release that number publicly tomorrow morning

**Tim:** [yes](https://www.youtube.com/watch?v=4oI48BEijVw&t=935) and assuming yeah obviously this assumes that the electrics goes live without a hitch tonight and you know there's there's no issues there but yeah 

**Danny:** [okay](https://www.youtube.com/watch?v=4oI48BEijVw&t=947) and this will all be ttd override by the cli this will not be cut into releases which

**Tim:** [so](https://www.youtube.com/watch?v=4oI48BEijVw&t=959) at least from the ethereum blog we're just pointing we're pointing people towards the latest releases for robsten and then telling them they need to do a ttd override on those releases

**Danny:** [got](https://www.youtube.com/watch?v=4oI48BEijVw&t=973) it okay any other questions or comments on how we're going to handle wraps in ttd and fork over the next week

**Mikhail:** [are](https://www.youtube.com/watch?v=4oI48BEijVw&t=981) we expecting releases out with this new ttd value after announcement

**Tim:** [so](https://www.youtube.com/watch?v=4oI48BEijVw&t=997) the only reason I would see that is do if if I run a node on robson like two months from now does that node need the right ttd as part of his config still after the mergers happen

**Danny:** [um](https://www.youtube.com/watch?v=4oI48BEijVw&t=1018) it kind of depends on how it's synced if you are sinking from a state from genesis or from a week so we tried to say before you definitely need it if you were after then it's not going to be relevant anymore 

**Tim:** [okay](https://www.youtube.com/watch?v=4oI48BEijVw&t=1030) yeah yeah right so so I think that the what I would suggest is like whenever because like right now there are client releases with a ttd in it for robsten whenever the next client releases they should update that value to what the actual ttp ends up being um but I wouldn't like rush releases to just have that value asap and we should just communicate that people need to do an override

**Arnethdcuk:** [yeah](https://www.youtube.com/watch?v=4oI48BEijVw&t=1047) I agree I think it's a good idea in general to get people used to the idea of overriding ttd yeah it's a good practice I think it's a good skill to have oh and 

**Tim:** [one](https://www.youtube.com/watch?v=4oI48BEijVw&t=1059) last note on that um I shared this in the awkward devs chat but i'll repost the hackmd here i'm using like a hackmd that was put together last week by mariusz which which kind of mentions how to change the ttd on every single client i've posted it in the chat here if there's something that's missing or wrong for your client please send me a message and i'll make sure that the blog posts obviously does not have the wrong information all the values in this posts have the fake ttd so that will be changed everywhere but just generally the command the the flag name all that would be good if people double check that it's accurate

**Danny:** [okay](https://www.youtube.com/watch?v=4oI48BEijVw&t=1140) thank you anything else on robson ttd the rosten game plan 

## General updates/discussion

**Danny:** excellent any other discussion points related to the merge 

**Terence:** [um](https://www.youtube.com/watch?v=4oI48BEijVw&t=1161) this is unrelated and I know perry is not here but I think that it's worth bringing up once robson has merged we probably can defecate kyung just because I would love to save some money if we can and I don't think we have to come to conclusion right now but it's just something to note is

**Tim:** [is](https://www.youtube.com/watch?v=4oI48BEijVw&t=1186) it like a significant cost to keep killed up to the main net merge because we do have like a bunch of applications you've deployed on it to test stuff and they might not already have deployments on roxton so if it's not like a significant cost I think keeping it until the main net merge and deprecating it like really close after that would be a bit better

**Terence:** [oh](https://www.youtube.com/watch?v=4oI48BEijVw&t=1200) I see I was like aware there's application you said 

**Tim:** oh yeah is still up I don't even know that I think we can deprecate like literally today I don't think yeah yeah um but but for kill itself like uh yeah there's at least like five or ten big applications that i'm aware that i'm not sure if they're still actively using it but they've deployed on it and then it makes it easier for others to then come and deploy and try stuff so I I would keep it up to the main gun merge 

**Danny:** [and](https://www.youtube.com/watch?v=4oI48BEijVw&t=1210) if you're listening kiln will be deprecated at the main net merge might as well start signaling that now thanks aaron other discussion points around the merge today

**Tim:** so someone mentioned on twitter today that they're they haven't been able to add validators to robson since genesis has anyone like successfully done that or can I quickly sanity check that it is Possible

**Danny:** I mean if eth1 data voting was forked that would prevent I would slow it down being processed period well I mean it depends was there still a majority consensus even when there was an issue anyone that followed that closely

**Ben:**` [the](https://www.youtube.com/watch?v=4oI48BEijVw&t=1307) roxton beacon chain is showing zero new validators zero pending validators so it looks like the beacon chain can't see the um can't agree on the deposit contract state at all
**Danny:** [the](https://www.youtube.com/watch?v=4oI48BEijVw&t=1325) fixes on lighthouse and um prism are those are not yet released onto those nodes
**Paul:** [as](https://www.youtube.com/watch?v=4oI48BEijVw&t=1337) a release onto the nodes my I think my last understanding was that we were voting correctly but i've been kind of not the lead on this i've been kind of the reviewer so um my knowledge is patchy
**Terence:** yeah ours is for this as well
**Danny:** [okay](https://www.youtube.com/watch?v=4oI48BEijVw&t=1355) um let's circle back on that right after the call I think we need to make sure that if those fixes are out they should be agreeing on a value at this point and inducting new deposits and if that's not the case that's certainly I mean tim the fact that if if people can't come to consensus on this value then deposits cannot be added to the beacon chain and so that's almost certainly what's going on here which is not great I can we see can somebody investigate how many deposits were made to the bobston beacon deposit contract just curious okay someone can investigate that while we move on
**Arnetheduck:** we deployed one fix to numbers but um there might be more needed we'll see our resident expert is on vacation the ethon data expert hey that's almost a full-time job
**Danny:** it's funny the things that you design for redesigned that I would have never expected that to be the you know a major source of error but it has been um and there's other seemingly more complex things that work follow all the time 
**Paul:**it is the grossest wonkiest mechanism though that we have 
**Danny:** [I](https://www.youtube.com/watch?v=4oI48BEijVw&t=1441) guess everything else is um you could argue more elegant okay so there's been 376 transactions there um we can clear that cube pretty quickly once we begin voting correctly but there's that's in there's also the follow distance to contend with there um I think that we can definitely if we can patch this up in the next day then these validators will be inducted before the merge so let's try to do that okay other merge related discussions
**Tim:** [was](https://www.youtube.com/watch?v=4oI48BEijVw&t=1528) a shadow fork yesterday oh yeah um yeah we don't even realize that I think there were a couple el clients which still had this issue where they struggled to produce blocks with transactions in them they would just return an empty block um off the top of my head I think it was based through an aragon but i'm not a hundred percent sure 
**Danny:** yeah it was but i'm not sure if it was every combo or if it was just specific combos
**Tim:** [okay](https://www.youtube.com/watch?v=4oI48BEijVw&t=1565) perry has it yeah sent some stuff um I think for aragon it was ever for aragon it was every combo for base two it was every combo except lighthouse and then for nethermind there was one combo with nimbus um that didn't work but it's not clear for another mind if 
**Marek:** [it's](https://www.youtube.com/watch?v=4oI48BEijVw&t=1584) just because it didn't happen yet or if there was actually an issue there it's because I I assume that anyone would have issue with timing so that is the reason another mind issue to be honest we prepare something similar to death that we will wait for um some amount of time and we will prepare the the payload but we only mask this issue we hide this issue and this is still need to be fixed on cl side
**Danny:** okay so there's still the issue where there's almost zero lead time between the prepare and get on a number of cells
**Marek:** I think only nimbus from my observation of course it would be good to check it right
**Danny:** okay any other comments on mainnet shadow fork six
**Marek:** [I](https://www.youtube.com/watch?v=4oI48BEijVw&t=1680) think there was a problem with not sure exactly but um definitely not nedermite probably erican and participation was lower right now so i'm not sure what happened maybe barry or marios will share details
**Danny:** [okay](https://www.youtube.com/watch?v=4oI48BEijVw&t=1693) and neither of them are here if there's any follow-up discussion on the shadow fork let me take it to discord or any other merge related items for today great so I did want to give a little bit of air time to the reorg that happened on may 25th you know I think the core of this was a an update to the fork choice that was deemed safe to roll out continuously but then an additional um bug in the spec was found that compounded that issue casper or anyone that's been close to this do you want to give us or I think a lot of people here are familiar with it but give anyone listening also some familiarity with what happened um a week ago
**Casper:** [sure](https://www.youtube.com/watch?v=4oI48BEijVw&t=1788) um yeah I mean so essentially the initial setup was that two blocks virtually arrived at the same time both blocks accumulated roughly the same weight and then essentially the validators were roughly split in half between running the proposal boost fork choice and the slightly less than half not running it and not the other way around so slightly more people were not running it and the problem was that then six block proposals in a row were running proposal boost but basically because of this known bug where proposers don't rerun the fork choice before proposing they essentially um falsely attribute the boost to the proceeding proposal instead of just looking at the attestations itself and that way essentially because we had six block proposals in a row running the proposal boost and not re-running the fork choice before proposing they basically extended this slightly less heavy chain and eventually one proposal was not running the proposal boost and therefore saw the heavier chain is leading and yeah that kind of concluded the seven block reorg and as danny already mentioned it's kind of a unfortunate situation where validators were split between running proposal boost and not running it and on top of that this bug of not re-running the fog choice so if proposers were re-running the fog choice this actually wouldn't have happened 
**Danny:** [right](https://www.youtube.com/watch?v=4oI48BEijVw&t=1896) and that was our assessment when we rolled it out was that although this might have lead to a split view on the order of a slot that would quickly be resolved um but then the compounding with this additional bug on the timing of when to run for choice that assumption was totally broken um so I think there's there's a bit of a discussion on you know if we are rolling out fork choice changes um to one ensure that we do an analysis on the safety of how to roll it out and whether that should be on a coordinated point like a not necessarily a hard fork but essentially telling everyone to update their nodes um for this event and to enable it at one point and the other question is obviously if how to account for potential unknown bugs that when we're doing such an analysis um one of I think the primary reason given the analysis that this would not lead to long term splits without this other bug it's very nice to not have to manage two code paths that are conditional upon some epoch and so I would potentially argue for being able to do it in the future um but I guess the one thing to note here is that you don't have to manage these code paths in perpetuity like a like a hard fork when there's a logic change you kind of after the after you pass the epoch on the next release you can actually do a um you can eliminate the old logic entirely um with the fork choice changes so even even if we do go to the point where you do these in a coordinated point you have two logics in one place you don't have to maintain them in perpetuity which is nice any other any comments or questions or thoughts on love's morning here thank you everyone for digging deep and figuring out precisely what happened there I guess my recommendation would be when we run into something like this again just to make sure that we discuss it much here and and right write down at least our analysis of why we're making the decision to roll out on a continuous basis or to roll out at a coordinated point okay so I also had a question about seconds per ethel in block this this is an estimation to get to an approximate depth um this does not actually matter like so if you if there were three blocks in that range you would still you could still agree on the block even though the depth wasn't exactly what you estimated so it's not um the problem isn't actually related to the spec that would just change the amount of blocks that you're kind of digging through or the depth that you get to but it doesn't change the ability for nodes to agree at that depth and it did used to be a precise block depth if I remember correctly but was simplified to the seconds estimation for simplicity reasons but I would have to pull up some old issues to see exactly why that was the case
**Paul:** [yeah](https://www.youtube.com/watch?v=4oI48BEijVw&t=2140 it was kind of ultimately because we we have to make assumptions about the time stamps so we decided to try and only make assumptions about time stamps i'm not sure if it was right or wrong but um it made sense at the time
**Salius:** okay so so if the second spear eat one block with a different value it's didn't solve the problem right
**Danny:** [well](https://www.youtube.com/watch?v=4oI48BEijVw&t=2176) think about like if if seconds worth one block is 15 and you want to get to usually about a thousand blocks deep but in mainnet or in on the network you saw the actual time between blocks was 30 seconds then you would only get to 500 blocks deep but that you can still come to agreement with each other even if um that average is is off I think that again the problem emerged in that there were assumptions made about what blocks needed to be downloaded and investigated with some margin of error and being outside of that margin of error on blockchains um okay cool thanks for the reorg chat I linked we linked to the barnabas discussion visualization of the seven block reorg it's very good if you want to take a deeper look 
# 3. Other client updates 
**Danny:** okay are there any client updates people would like to share today cool 
# 4. Research, spec, etc
**Danny:** um any research or spec discussions
**Arnthdck:** [I](https://www.youtube.com/watch?v=4oI48BEijVw&t=2284) would highlight one thing which is that we've started posting a bunch of pr's on on litecoins now um two things have happened there were discussions in amsterdam around light clients in general and a lot of that feedback has been incorporated into those pr's now so I think they're they're getting to a point of of what being really nice um I think the approach we're taking right now is to try to split them up into slightly smaller pieces and then get reviews on those smaller pieces and then try to get this ball rolling um what we're using it for well one one cool use case that that has come up is that if you're not running a validator you're just running some random infrastructure and want to read the you know your state at some point you don't really need to run the full consensus protocol um so to that end we've actually developed a little standalone application that uses the lifeline protocol to kind of feed an execution layer with what's called purchase update and the blocks it's really tiny and uses very little bandwidth which is nice of course that depends on these pr's getting getting some attention as well and then eventually that people um run with the electron protocol enabled so i'm kind of I wanted to plug those pr's right now as as has been really interesting for those use cases in particular hoping to get some eyes on them
# 5. Open discussion/closing remarks
**Danny:** [thank](https://www.youtube.com/watch?v=4oI48BEijVw&t=2408) you I will put my eyes on them I ask for a few others to do so as well okay any other discussion points for today research spec or otherwise okay um and I would encourage teams to send a person to all core devs for the next couple of all core devs because I think we're going to continue to be talking about timing test net launches and different things like that that we we generally need some agreement on both sides for so if you can please join us there and I will encourage them to join us here okay thank you everyone take care have a good one thanks thank you thanks everyone bye thank you thanks man all right you All 
### Attendees
* Danny
* Paul
* Tim
* Mikhail
* Terence
* Ben
* Salius
* Arnethduck
* Marek
* Salius
* Casper
* Pooja
### Zoom chat

From terence(prysmaticlabs) to Everyone 03:02 PM

https://barnabe.substack.com/p/pos-ethereum-reorg?sd=fs&s=r

From danny to Everyone 03:02 PM

https://github.com/ethereum/pm/issues/536

From Tim Beiko to Everyone 03:03 PM

Might be worth touching on this too: https://twitter.com/calamenium/status/1532355860034371584

also there was a shadow fork yesterday!

From Tim Beiko to Everyone 03:08 PM

looking at Ropsten etherscan, the difficulty is still going down each block so the cause is very likely just the disappearance of the high hash rate

From Tim Beiko to Everyone 03:20 PM

+1 about training the override muscle :-)

https://hackmd.io/ngKLqVvvTTGZLj1bGPuCoA

From Lion dapplion to Everyone 03:25 PM

The name of the Ropsten beacon chain is just “Ropsten beacon chain”?

For mainnet is easy because there’s mainnet beacon chain, and mainnet “eth1”. But for Goerli, there’s two names: Prater and Goerli. Will some name take over? Or it will be a dual named merged testnet

From Tim Beiko to Everyone 03:26 PM

does anyone have a quick link to the contact?

trying to find the address

0x6f22fFbC56eFF051aECF839396DD1eD9aD6BBA9D

From Fredrik to Everyone 03:26 PM

https://ropsten.etherscan.io/address/0x6f22ffbc56eff051aecf839396dd1ed9ad6bba9d

From Tim Beiko to Everyone 03:27 PM

376 transactions to the contract

not sure if any are failed

From Fredrik to Everyone 03:27 PM

last deposit ~3h ago

From Tim Beiko to Everyone 03:27 PM

there are some few failed, but the bulk of them seem valid, so definitely 2-300 validators pending

From danny to Everyone 03:28 PM

https://notes.ethereum.org/PhbNw_cGSQ-VKqzGl4bPcg?view

From Fredrik to Everyone 03:31 PM

336 validators pending: https://beaconchain.ropsten.ethdevops.io/validators/eth1deposits

here’s one pending activation since 7 days (deposited by the “TTD miner”): https://beaconchain.ropsten.ethdevops.io/validator/0x96d8d5d511d6b1b3169369306baf2207983f3f54b8056e7882dd103d63583f44ddb836be26e22fb447da853c25e51432#deposits

(1 invalid)

From danny to Everyone 03:32 PM

https://barnabe.substack.com/p/pos-ethereum-reorg?sd=fs&s=r

From Hsiao-Wei Wang to Everyone 03:34 PM

ropsten pending validator

I guess beaconcha.in doensn’t have Ropsten Eth1 chain node to provide the pending validator number on index


