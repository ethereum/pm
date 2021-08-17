# All Core Devs Meeting 119
### Meeting Date/Time: August 6, 2021, 14:00 UTC
### Meeting Duration: 30 min
### [Github Agenda](https://github.com/ethereum/pm/issues/365)
### [Video of the meeting](https://www.youtube.com/watch?v=jNxAB3WpAD0)
### Moderator: Tim Beiko
### Notes:David Schirmer

## Decisions Made / Action items
| Decision Item | Description | Video ref |
| ------------- | ----------- | --------- |
|118.1 | London Updates | [3:13](https://youtu.be/jNxAB3WpAD0?t=193)|
|118.2 | Other Discussion Items | [15:20](https://youtu.be/jNxAB3WpAD0?t=918) |



**Tim Beiko**(London Updates-3:13)
Okay hi everyone welcome to all core devs 119 we don't have a ton on the agenda today basically going over the London fork yeah which happened yesterday in case anybody missed it seems to have generally gone well there were no consensus issues most nodes even upgraded there was some small issue where some of the miners were still targeted at 50 million gas limit because I was kind of the default but then by reaching out to them I think it's been mostly fixed we're now with roughly at 30 million gas blocks I think there are one or two small mining pools still targeting the old ones but they're not significant enough to drag everybody down yeah that's basically what I saw in my end I don't know if anyone else has anything they wanted to share about just the fork or what they've seen that happen?

**Danny**
do we know if most of the functionality has been tested on mainnet? like people try to send an ef.


I haven’t seen it. I posted on Twitter yesterday the only thing I've seen is somebody trying self destruct so testing parts of 3529 but I haven't seen somebody posted Basie up code I haven't seen the 0xef and I haven't seen the kind of other conditionals for the gas refunds although I expect those with the trigger I think in a lot of like dex's but I'm not a hundred percent sure about that actually


**Trenton Van Epps**
Sort of a half test but acts like put together a dashboard checking there any contracts starting with 0xeff and there is zero so far but yes someone should definitely actually test it

**Tim**
For the 0xef would it actually what would happen would it be just that your transaction reverts right?

**Martin**
Yes.

**Tim**
 Okay. 

**Martin**
(microphone feedback)

**Tim**
Got it and yeah Trent posted the link above which is counting them but yes if anyone under call listening wants to kind of test those basically 3529 there's a couple of kind of edge cases Beyond just the basic self-destruct if somebody could send a hash of a transaction that tried to deploy a 0xef contract and then just calling the base fee opcode also I don't think anyone's done that yet. Anything else about London that people wanted to share that they noticed?

**Danny**
Do we have a node count? Did it greatly reduced like normal?

**Tim**
let's look at what I looked yesterday before the upgrade and it was something like yeah we were at 80% yesterday right before or right after I forgot, the upgrade. now Ethernode shows 96% that has upgraded and there are ether nodes tracks 1400 that have updated and you basically so I'm ether nodes you see a drop but the drop is from when we released, March, I think this is for when we released Berlin there was this massive drop because we hadn't had the fork in like 2 years and now they're showing we're still at like 5700 nodes on the network so I'm not sure what it smells kind of the discrepancy in there two pages like their total notes count shows 5.7 thousand and then their London page shows 1.4 thousand with 96 of them being updated saw the total of you it doesn't seem like it's dropped and then on to London view it seems like 90 / 95% have updated.

**Martin**
Another random datapoint regarding update this up to you if you look at fork node for the legacy node has not seen an update, it got stuck on 99, so there has been no miner that has reached legacy geth node.

**Tim**
This is bad blocks one because it got the fork block and then got rejected?

**Martin**
Yes

**Micah**
Did I understand correctly, not a single miner fork?

**Martin**
Yea its only one node

**Danny**
It could be a single GPU that hasn’t found their block yet

**Micah**
Sure but is this the first fork that actually went perfectly smooth? Don’t we always have some miner that stays behind, like every fork in history? So the one that everyone thought was going to be the most contentious became the least.

**Martin**
It always takes a while though before the post for nonpanel node gets seen but its been a while now.

**Micah**
Yea I would be curious, if someone sees one please share on ACD, because this is a pretty big milestone if we get everyone to fork correctly

**Martin**
Yea the thing is also if the percentage is smaller than it will be much harder for a single miner to propagate because everyone would just reject it

**Micah**
I think the moral of the story is that every fork needs to include a highly contentious change that way it goes smoothly

**Cary**
Has anyone done analysis on the intermittent zero transaction blocks to see if there were really no transactions that were suitable at that base fee or really just zero transaction blocks that were produced

**Micah**
So I haven't done a thorough analysis but just glancing that etherscan I think it there is at least some of them are 0 I can look at 1 that the preceding two blocks were below the threshold so the base is going down picking up this block and the block immediately after this had was very full suggesting there was lots of stuff pending and there's the time between blocks is really short so we can have like a super short block or anything it looks like super long block i mean against anecdotal yeah

**Tim**
 and I think Vitalik I saw you posted on on Twitter basically the distribution of gas gas usage we should expect you want to just give a couple thoughts on that?

**Vitalik**
yeah I like basically all that was just need scans through of 500 recent blocks and like I just made a chart of like what the gas divide the gas fee of each one and that's just a plot of distribution by percentage with the things that I compared it to it was basically a simulation I made about like 1 and 1/2 months ago where is pretty simple and basic it assumes that the transactions happen at a very uniform rate like basically you got quene full up of once every couple hundred milliseconds and then blocks have some probability and when a block comes it grabs all of the transactions that are in the pool or if there are to many then it grabs the max and the pool goes down by that amount and the two look very similar the each other which is a good side first of all of it and it also shows that there is not that much empty blocking  going on but also it's just a nice sign that I guess nothing very unexpected is happening just remember this is different for roptsen and roptsen distribution was much more difference and irregular but not mean that is looking quite healthy.

**Tim**(Other Discussion Items-15:20)
Nice thanks for sharing anyone else have thoughts or anything related to London they wanted to bring up?

**Pooja**
Just one small announcement from the cat herder side a contributor has created a NFT for the london upgrade so we will be making a distribution of that, distribution has already been done from the public wallet but we are in process of collecting more and thank you everyone.\
**Tim**
Thanks, and yeah one more thing is all I have is we have a call for infrastructure providers wallets and whatnot next week given that a lot of them wanted to wait and see kind of 1559 being deployed on mainnet to get some data before they actually launched their products so next Friday at the same time as ACD 1400 UTC I will have a call yeah with wallets and other infrastructure providers to discuss yeah and then and we can kind of analysis you know how the tools you have rolled out London support are doing and kind of what's missing for everybody else to add it because it's worth noting the percentage of 1559 native transactions were seeing on the network is still quite low I think my crypto has supported by default in metamask has it been kind of a Beta release so hopefully yeah in the next couple weeks more and more products will just enable these by defaults and we'll get kind of the higher update in adoption. Yeah, so that was pretty much kind of the only thing we had on the agenda recognize everybody's been very busy these past couple of weeks trying to get London out and we've done it successfully so that's pretty good, was there anything else? Okay well then I’m happy to keep it short and give an hour back to everybody. I’m sorry what do you mean Pooja?


**Pooja**
Like what is coming up next, it’s not very urgent, the last meeting we were discussing the next upgrade, and if we have time we can continue the discussion.

**TIm**
Sure does anyone have anything they wanted to share regarding naming and the next couple of upgrades?

**Vitalik**
Are we talking about the merge or are we talking about the next nonmerge upgrade?

**Danny**
There was a debate last week about what you call the fork next fork regardless if there were an contingencies. If it’s only iceage is it named after a glacier?

**Tim**
My read on those conversations is that if it’s just an iceage fork then people think the two-word names are kind of like near glacier and I think asic recommendation for another glacier we could use so it seemed like that was the most popular option I think people were split on whether the merge should be called the merge or like have an actual you no more Ethereum sounding name and I think there was a conversation about like how do you call upgrades after the merge which is definitely not something we need to it to figure out now and whether they'll be both kind of consensus and execution layer coupled or not but assuming that they are coupled we could just keep using kind of the consensus nomenclature around I think it's star names if I'm getting this right start our galaxy names.

**Danny**
yeah I can be Altair London you know if it touches both layers you can have two names I don't know I don't I don't actually want to throw my hat in the ring cuz I don't like yeah.

**Tim**
 so there is an async discussion thread there if people want the comments yeah I think the question around like whether you know you name the December fork like a two-for-one name kind of depends on what it is and we're still not ready to make that call so yeah we really don't need a decision now but Micah you have your hand up.

**Micah**
Oh yeah, it was fun to get a temperature check assuming that we would like to make just a single parameter change to 1559 so like after we used to research we have some data or any of the client’s teams opposed to including that with the iceage push back let’s just assume it’s like a one-character change 1 divided by  8 2 divided by 10 is that acceptable and reasonable and not interrupt people too much?

**Artem**
 well, Aregon is still looking for a real feature fork for what it's worth.

**Martin**
As for me, I would prefer to not do a feature fork it's up to the change if it's the right time to change.

**Lukasz**
Nethermine is okay with something very small and that's about it.

**Tim**
I guess what you're saying you say we found it like you had the base fee is moving too fast and it would be quicker it would be better to adopted that like yeah update slower or quicker than this is just a constant that was changing but it's not something like actually changing how 1559 works right?

**Micah**
Yeah, you like this would be we've long known that we weren't like 3 divides by 8 and a couple of those parameters we use for just kind of gases and we wouldn't know if they actually work until things are production and so by November long enough you might have some better data and soon I'll be able to change some of those constant all definitely not lobbying here for a big change just like if there's something small like this tweaking a constant or something applicable to think that are eligible.

**Micah**
 I just want to qualify why I don't want to do a feature fork right now and want to focus on the merge and get that right.

**Tim**
I think I just to reiterate from the last call it seemed like everyone was kind of on board to getting to a spot were we have actually have merge test nets up and running and and then kind of making a call based on how much time taken and how much work we anticipate is left with the merge one thing that I think Thomas you know how brought up this idea in the past of leaving the merge testnets up for like much longer than we leave regular testnets that might actually give us some time for a small feature fork and regardless of whether or not there is a feature fork I think this is some feedback we've got in from a lot of people regarding London where they would have liked to see kind of a longer more time between when it's on the testnets and when were busy when we stopped making consensus changes and we're confident in forking the testnets then have more time where we can actually iterate the API before we actually have the mainnet fork it so as you know people on this call are aware they're still like some tweaks that are being done to some Jason RPC calls and for the merge, people would like for those to happen before it is deployed on mainnet because it become cemented behavior. Ansgar has a question about if the merge in Q4 is a realistic possibility?

**Ansgar**
The reason I was asking is really just that I think just for clarity and planning I think it's best to be as open as possible about these things and Q4 seems to slip into the very unlikely territory. I just in case at some point we feel like that but now it's really clear that we won't be able to make it I feel like it would be best to communicate that but maybe it's still like in the cards so if there not it’s fine.

**Tim**
 I suspect it'll be a much easier question to answer once we've actually started putting testnets together and devnets yeah I don't know if any client has a better estimate than that's but it seems hard to know yeah when it will be ready given we don't even have it implemented in part I know there's something that's been implemented in clients with them but we don't have kind of the latest spect implemented in clients and network setup between kind of the consensus and an execution teams I don’t know if anyone has a better answer than this? I guess not and I guess one last thing just related to London I'm going to try and reach out to the different client teams over the next two weeks to chat about you know what we can do like what they think was well what do you think we could have done better and and try to kind of document that so as we're planning to merge we ideally have a smoother process that we did with London I think we did do alot of things well in London but like there's definitely like I've heard a lot of people who you complain about various aspects and things that we could have been improved so I'm going to try and document that to the next couple weeks and and be able to share it so that hopefully we yeah we can learn from from everything that happened in London and have them merge go at even smoother yeah and I guess yeah kind of related it probably makes sense for clients to start looking at the merge stuff over to next couple weeks so we can start on the next call and discussing the actual technical bits around the merge I know Micah has been there on the previous call to get the high-level overview of the EIP and they're still kind of a couple open questions that were tracking and what not so I think kind of going forward we can probably start going through those and and  working on on on getting it implemented on clients and running on devnets Danny you're saying something?

**Danny**
Just excited 

**Tim**
Anything else anybody wanted to discuss?


**Trenton**
 oh yeah, I guess it's related to the call next week but do we know when Geth will have the 1.7 release I don't know how crucial that is for APIs but I think it's related to fee history unless I'm mistaken.

**Martin**
No, we don’t, sorry yeah I've been away the last few days and I’ll coordinate with Peter on that.

**Trenton**
 okay yeah that's fine just wanted to check I guess I'll just keep going I don't know if you already mentioned it Tim but next week will be having at the same time the fourth of the ecosystem ordination calls this time it's obviously post-London so it's a 1559 assessment or anybody wants to join that again you having a lot of the ecosystem providers wallets, API providers on the call just to assess how they are implementing after one and a half weeks of mainnet data to look at. So that’s next week at 1400 UTC Friday.

**Tim**
Cool, anything else? Okay, thanks everyone. Once again great job and I’m happy it went out smoothly and I will see you all in two weeks.


## Attendees

* Tim
* Lightclient
* Pooja | ECH
* Micah Zoltu
* Danny
* Trenton Van Epps
* Marek Moraczynski

* Lukasz
* Dankrad Feist
* Martin Swende
* Artem Vorotnikov
* YDXTY Thi
* Sam Wilson

* Vitalik Buterin

* Ansgar Dietrichs

* Gary Schultz
* Sridarian Sharingan

---------------------------------------
