# Ethereum 2.0 call 70 notes
### Meeting Date/Time: Thursday 2021/08/12 at 14:00 GMT
### Meeting duration 1.5 hours
### [Github Agenda](https://github.com/ethereum/eth2.0-pm/Issues/232)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=24MRTRDJ-Iw)

## Agenda
* Altair-devnet-3

* Altair

  * Release and testing

  * Planning

* Client updates

* Research updates

* Merge updates

  * Unit256 calculations

  * Client security settings

* Spec discussion

* Open discussion/closing remarks

## Altair devnet 3
**Danny:** Okay I think the most topical thing that we can talk about immediately is Altair devnet 3, this was led by pari And has a different client ration that are even split on the past view to represent at least what we know of mainnet today and 70% of prysm. And last I saw there were a few things beIng worked out this morning, is there an update on that, I guess mainly because we're gonna talk about Piermont and I just want to make sure that we are still good to go. I imagine anything that has opened up on that we should be able to settle over the next few days, so I think paramount is still good, but where are we at?	

**Paritosh:** Sure so I can start with a brief of where we are right now, we had a bit of config error In the beginning but everything’s outs later on but today morning we noticed that the lighthouse client seems to have lost a lot of peers and In general the performance doesn't seem to be what we’d expected to be. I think lodestar is doing a lot better now they said they were overloaded and besides that there was an Invalid signature that was noticed and yes some peer scoring related things for lighthouse.

**Paul:**  We're still trying to figure out why we're downloading videos. I think what we're seeIng In some valid signatures from a perspective of so they get Into that.

**Parithosh:** Another thing that I  don't think I have mentioned otherwise is that there seems to be a loadstar peer that both lighthouse and prysm have banned for Invalid sequence number, im not particularly sure why that's happening but I can show the logs

**Paul Hauner**: One of the things when a down scoring people heavily floor at the moment is for sending is the light sync messages which were probably going to lighten up on that  because it  seems fairly likely that  the messages are so short lived.

**Danny**: Right so youre right thats going to be an ongoing very tight on a single slot scope whereas we should maybe expect a few to be lagging.

**Nishant**: Yeah we have been Ignoring them rather than object and down scoring peers who send you late messages.

## Altair
### Release and planning

**Danny**: im going to sanity check that is an angle or condition yeah it isn't In your condition but might make sense to lighten that up at least one shoe figure it out. So I moved the client updates to after this so we can talk about Altair. I just want to sanity check that we still expect to fork paramount In a week even If that means cutting some released monday tuesday based on the issues we found today. I think devnet 3 is serving its purpose is that a signal to not update paramount or is that a signal to fix things and continue with paramount

### Planning
**Danny**: By default I think we are going to fork paramount on thursday unless people have a strong objection.

**Parithosh:** I think In general the decent is also finalizing and everything so Id say there is no reason to delay or delete so we will do it on thursday

**Danny**: Alright, so that's primarily what I have planned for Altair we could discuss the theoretical dates for prouder and or mainnet, but my Intuition is given some issues seen on the devnet and with the paramount launch In a week that we were better suited sorting through these issues before we put a date on anything. Are there any other Altair items we would like to discuss before we move on?

## Client updates
### lodestar

**Danny**: Great, lets get started with lodestar

**Lion**: Hey lion here, so we did participate on the Altair upgrade and it went well, we overestimated our machine so I had a bit of a rough time but we are actively working on  loading our memory research and we have found three strong strategies so hopefully we can get that merge soon and we should release an article by monday, with a working demo that would be connected to others.

**Danny**; Thats very exciting, thank you, prysm?

### Prysm

**Nishant**: Hey guys, sean here, so for the last to weeks we have mostly been focusing on bringing down our changes from our hot fog branch of our developer branch, In the process we have been carefully reviewing the cold beer implemented multi-year and In the process we found a bing In our state transition function as we mentioned earlier so is uncovered by spectators or this has been Invaluable In finding different edge cases also along with that we've been running short term test net with other clients for all day so this has actually helped us quite a bit In filling subtitle networking bugs that are much  harder to find In the bigger dev net so specifically to do with gossip scoring and In for keeping our transition so you are happy to have that sorted out. Along with that we have  actually finally implemented all the official api endpoints In our develop branch so this has been In the works for a long time. So we are happy to have done it and now we’re In the process of v2 and points for all tires.

**Danny**: Cool, you go shawn!, and lighthouse.


### Lighthouse

**Paul**: Hey its paul here Another report this time we did it publish a pre-release which is 1.5.0.0rc00 so this is the release that's we're going to ask users to use for the pyrmont fork. it may or may not take another release In the meantime. We just want to try and get everyone ready for it early. We probably won't publish a full 1.5.0 before pm. Were just trying to prioritize those stable release. He wont dictate the pace In which we do things for main that were now  that we've got kind of say to get the release at the door which Includes dopple ganger, a bunch of other cool features it also means all of our LTS tough is down merged out of. its know what no longer living In separate branches and lives.

**Danny**: Gotcha, and grandine

### Grandine
**Saulius**: Yes hi this is saulius from the grandine team we have been working on some fixes and optimizations and the focus is now on the mowgli runtime  support and this is  also a part of abdel tiara support so hopefully we’ll cow it working In a couple of weeks	

**Danny**: Got it thank you. Teku

### Teku

**Adrian**: Hey this is Adrian, we've got 201.8.0 release that came out today and that has Altair support finalized an ready to go, it is scheduled to active on the piermont front point. So reality important that everyone upgrades that. But nothing that needs to be particularly called out here.
**Danny** Alright thank you Adrian, and nimbus

### Nimbus

**Mamy**: “ Hi mamy here, so the updates for the past 2 seeks we know how much architect docker images also released also we release 1.2.2 which is an update just before london, because we had a lot of before running client, and they had issues. Otherwise we have been catching up with Altair, we have a dedicated branch and we don't want to mix updates.

**Danny**: great, moving on, research updates, lets talk about the merge.

## Research updates

**Proto**:  so we are open for sharding for separate builders and proposers this is based on like earlier post  from pathetic and others about data. And this should also help for example ease the burden Infidelity every single layer 2. 

**Danny**: Any other research updates? Okay, moving on to the merge.

## Merge updates

**Mikhail**:  This has been Introduced by beIjing with london and when I was doing this I was like thinking that you end 64 would be pretty much enough In general case because its very that we all see base fee per gas like lets say 30 eve which is a really crazy number but then proto pointed out that during the transition process If you might be valuable attack the ghost of the attack is related with is high but the depends on the different conditions so we don't need to perry about it. Were creating the technical depth that will need to be resolved at some point In the future by c2 is a viable option also as I understand it matters for charlene as well so proot might comment on that so it might also be valuable to Introduce you. 

## Spec discussion.
**Danny**: There are new BLS test vectors available. Now BLS libraries can be tested outside the Eth2 test suite, and the tests can be used by other projects.


## Open discussion
None 
## Attendees
* Lion
* Danny
* Saulius
* Mikhail
* Pooja
* Nishant
* Lightclient
* Medhi
* Alex
* Paul
* Carl
* Cayman
* Paritosh
* Mamy
* Dankrad
* Ansgar
* Ben
* Adrian

## Next meeting
Thursday, 8/19/2021, 14:00 GMT
