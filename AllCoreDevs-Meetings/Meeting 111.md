# All Core Devs Meeting 111
### Meeting Date/Time: Friday, April 23rd, 2021 14:00 UTC
### Meeting Duration: 1 hour 30 min
### [Agenda](https://github.com/ethereum/pm/issues/301)
### [Video of the meeting](https://youtu.be/C9hzAYkklQM)
### Moderator: Tim Beiko
### Notes: Shane Lightowler


## Decisions Made
| Decision Item | Description | Video ref |
| ------------- | ----------- | --------- |
| **1**   | Revised EIP for simplified version of 3403 to be created by Martin ahead of next ACD call | [16:17](https://youtu.be/C9hzAYkklQM?t=977) |     
| **2**   | Scope for London is confirmed as 1559, 3198, 3238, and an alternate for 3403 which is to be discussed next week. |  [40.03](https://youtu.be/C9hzAYkklQM?t=2403) |  
| **3**   | The post-London feature fork is to be called Shanghai. The Merge upgrade to be officially known as The Merge. |  [40.03](https://youtu.be/C9hzAYkklQM?t=2403) |  
| **4**   | The difficulty bomb push back to date will target ~1 December. |  [44:54](https://youtu.be/C9hzAYkklQM?t=2694) |  
| **5**   | 14 July set as target date for London. |  [52:08](https://youtu.be/C9hzAYkklQM?t=3128) |  
| **6**   | CFI status for EIPs is to be reset after every hard fork |  [58:04](https://youtu.be/C9hzAYkklQM?t=3484) |  

# 1.London Updates

**Tim Beiko**

* Has checked in with the client teams re: bandwidth for London
* Smaller-sized London is consensus (except for one team who advocate less upgrades in general)
* 2 teams wanted to aim for July due to difficulty bomb and its effects in Aug/Sep.
* 1 team - July is a stretch, but can aim for it.
* Fear that a small London means other EIPs could miss out - should we plan another feature upgrade in parallel with The Merge? Most teams are ok with this notion (Merge + Shanghai in parallel). Rayonism would help flesh out how possible this is.
* EIP-2677 - noone pushing for this very strongly in London. 
* EIP-2537 - already implemented by several clients. Could be done at same time as Merge if we take it out of London. If we do change the library/BLST and gas prices then extra testing and benchmarking will be needed. This would grow the scope for London a lot.
* EIP-3403 - noone opposed if we think it will help security with 1559. Some do have quibbles - too many edge cases/a more elegant mechanism is needed. Not strong opposition though.
* EIP-3074 - some strongly in favour, some strongly opposed. Feels contentious. Needs a security audit and community feedback. Likely not for London.

**Martin**

* [Peep an EIP call on 3403](https://youtu.be/jqmM3xL6Ny8) happened this week. Check the call to see detail on the changes. 
* Vitalik has various tweaks to the 3403 spec based on this discussion.
*  New simplified alternative for 3403 will be created.

**Ansgar**

* Is 3403 with the new changes relevant to London or is it too late?

**Martin**

* We can have the new EIP ready in the next couple of days.

**Tim**

* Clients need to be ready for London mid-May.
* If we want 3403 in London we need to agree to it on the next call.
* **DECISION 1:** Martin to get new EIP out early next week for feedback. [16:17](https://youtu.be/C9hzAYkklQM?t=977)
* Reducing complexity in EIPs is good.
* Consensus on 3074, 2677 and 2537 seems to be to keep them out of London.

**Kelly**

* Re: 2537 - is the plan to use Blast? Will the gas prices be changed?

**Martin**

* All the testing and cross client testing has been done on the existing implementations. If these gas cost changes are based on the assumption that the blast library is used, which would mean all of the other implementations would want to switch to that, then that sounds like a big project.

**Kelly**

* My understanding is that the gas cost changes weren't based off of blast, so they're based off of the current library. There may be a new release of that existing library. Just wanted to clarify that the gas price reductions were suggested for the existing library, not with a library switch.

**Martin**

* I havent looked into the exact implications of the gas changes yet but feels like a bit of work needs to be done.

**Kelly**

* Let's catch up offline, Martin.

**Micah**

* If clients are happy with the current gas costing we can always release BLS with the higher gas costs and adjust them later if needed. We dont need to do them simultaneously.

**Kelly**

* I think that makes sense, if there was a desire in future to switch to blast then gas costs could be reduced even further below whats suggested in the doc now.

**Martin**

* Sounds like a good approach to when we introduce a computationally intensive pre-compile. We can then lower gas costs once it is in peoples machines and tested.

**Tim**

* 2537 requires an audit. How would that work in OpenEthereum's roadmap?
* Teams see mostly fine with BLS... do we want this for London?

**Dusan**

* Is this for BLS? If so, we have this already implemented but we need an external code review. I dont think this would be a problem for London.

**Kelly**

* Blast does now have Rust bindings that could be used if they need to use a library that has undergone a security review.

**Tim**

* Any other comments on BLS?

**Paul D**

* With EVM384 we were within 2x - we had a bunch of breakthroughs and are now even better than 2x runtime and gas.
* Worst case if something doesnt work out, we're looking at less than 2x slowdown if we just do it with EVM384.

**Tim**

* People seem mostly fine with BLS but what are peoples thoughts on inclusion for London?

**Lightclient and Micah**

* Seems like we need to decide first if there is a feature fork after London?

**Martin**

* Prefers smaller, more frequent, upgrades. In favour of feature fork shortly after London.

**Danny**

* What do we mean by 'shortly after'? One month? Three months?

**Tim**

* I would have thought 3 months, given how Berlin eventuated.
* London - client release in June. That's when we could start working on the next feature fork, while running London testnets.
* Feels like October-ish for the feature fork mainnet, testnets in August.

**Ansgar**

* The previous assumption was that teams are ok with a feature fork if it doesnt delay the merge.
* An October fork seems like it would delay the merge until 2022.
* Any chance we can feature fork in Sept? If it's just BLS + 3074, these are already implemented (not much additional effort).

**Tim**

* An October feature fork would assume working on the merge in parallel.

**Danny**

* Co-ordination overhead doing an upgrade is significant. An October feature fork in parallel with the merge seems ambitious.
* Rayonism will enlighten us here re: timeline, complexity, specs. Difficult to make an informed decision on this timeline right now without that input.

**Tim**

* There is a desire from all to keep London small. If we add things to it London beyond 1559 will be delayed. 
* If we keep London small we dont know yet if this will impact the merge.
* Teams are focussed on London and the merge right now. 

**Gary**

* Only 3074 is a significant piece of work and is dependent on an audit. The other EIPs seem small.
* In favour of a skinny London if we want certainty on London.

**Micah**

* Also in favour of skinny London, and plan for a follow up feature upgrade in October.
* If it turns out that the merge is being held up by that, we can pivot. If Rayonism reveals the merge is really easy we can drop the October fork and focus on the merge. If not, we are already on track for an October fork anyway. We should keep going, plan with the info we have, and be prepared to pivot as new info comes to light.

**Danny**

* That sounds very reasonable.

**Vitalik**

* Can we plan a feature fork but leave the decision to activate it as late as possible?

**Tim**

* Yes. A quick date = small scope. The 2 big EIPs that people want but will be difficult to accomodate in London are 2537 and 3074. It feels like we should signal now that the post-London feature fork should focus on those.

**Micah**

* A good plan for all feature forks is that we try to get rough consnesus for included EIPs up front. The 'just work on stuff and see where they can fit' seems to have lost favour lately.

**Asngar**

* We should plan a feature fork, have it ready, depending on progress of the merge. Apply the fork at first possible moment when we are free, without impacting the merge timeline.

**Tim**

* Yes. Consensus seems to be keep London small, and plan for a feature fork. If merge is ready before, we do it before. If the merge is ready after, we do it after. Anyone strongly against?

**Martin**

* I'm on board with that.

**Tim**

[40:03](https://youtu.be/C9hzAYkklQM?t=2403)

* **Decision 2:** In summary, the scope for London is the items already on Aleut - 1559, 3198, 3238, and an alternate for 3403 which is to be discussed next week.
* **Decision 3:** 2537, 3074 to be considered in the subsequent feature fork aka Shanghai. The Merge 'fork' (it may not technically be a fork) is to be called 'The Merge'.
* Re: 3238 - difficulty bomb pushback... what should the period be? The current EIP pushes back to May 2022.

**Micah**

* If we are planning upgrades in October we should bring it in to October to force us to keep to that.

**Tim**

* Lightclient suggest 1st Dec. Slightly more pragmatic.
* I'd be fine with 1st Dec. We ok with that?

**Micah**

* Once holiday season starts, its unrealistic to expect much to be done.
* If we want to target this year we should expect to get something out before thanksgiving.

**Tim**

[44:54](https://youtu.be/C9hzAYkklQM?t=2694)

* Cool. **Decision 4:** is to target the 29 Nov - 1 Dec range. I'll leave a comment on the EIP to this effect.

## London Timing

**Tim**

* London timeline... we can set candidate test/mainnet block numbers in the next call.

**Lightclient**

* Are we set on mid-July or can we bring it forward to early July?
* I weakly push for early July.

**Tim**

* Mid July gives us a better/longer rollout period.
* Tomasz agrees with mid July.
* Noone strongly pushing for sooner.
* We need to give tooling time to get ready for London (eg all the libraries/Ethereum JS, Infura, Etherscan etc). These have expressed a strong desire to be ready for 1559. We should give them sufficient time between the launch and announcement.

**Lightclient**

* Would like to figure out block numbers today rather than spend another week on it.

**Martin**

* No time is saved by setting blocks today...

**Lightclient**

* The sooner we can give the other parties the block number, this gives them more time to implement changes.

**Martin**

* But we are setting the date now anyway.

**Ansgar**

* Going a week earlier would require a client freeze a week earlier also. ie earlier than 12 May. Is that realistic?

**Tim**

* Yes, we are bottlenecked there.
* The other unknown is that we have an EIP that needs to be replaced...
* Any other strong opinions?
* Let's keep the dates we have (14 July) and set the block number next week. 
* **Decision 5:** 14 July is the mainnet target date for London. [52:08](https://youtu.be/C9hzAYkklQM?t=3128)

# 2. Other Discussion Items

## EIP-3521

**Tim**

* Lightclient, you wanted to discuss EIP-3521 which changes the access lists from EIP-2930...

**Lightclient**

* Summary: If you want to create an access list for a contract that the transaction is immediately executing in, you have to pay the 2930 cost of that address to provide keys. For it to be economical to provide keys for that immediate target of the transaction you have to use ~25 storage slots. This EIP reduces the cost to just the cost of call data. This is ok to do because 2929 already adds the transaction target by default to the global access list. So it's basically being charged twice right now. With this change it's economical to use an access list after youve read about 5 slots. This is a small change.

**Tim**

* Any comments?

**Martin**

* Already commented on Ethereum Magicians... I agree with what you're saying, right now it's ugly. However it's solving a small problem, not a big problem. If users just blindly add slots then when they submit a transaction it may fail early because something changed from when they made the access list to they were included in the block, which makes you pay the full cost for everything you were going to access if the transaction had followed the path you thought it would.
* What parts of the state to include/exclude is a tricky situation. It becomes less tricky if we remove this particular word. We are solving a little bit of a very complex problem.
* I dont think this is very urgent, but is a positive change.

**Tim**

* Tomasz says it makes sense but needs more discussion. Ansgar thinks this could be a candidate for the feature fork.
* Any other opinions?


**Lightclient**

* Agree with Martin. People use access lists with considering the ramifications.
* Am fine to push this off to further discussion.

## Resetting the CFI status between network upgrades

**Tim**

* We have this 'Considered for Inclusion' status...  this was given to an EIP that seemed to be a good idea but yet not ready to be included in a fork. There was an implicit assumption that this would be reset between forks - lots of EIPs where they are proposed for a certain fork but not included go stale.
* This is a proposal to say that CFI does formally reset after each fork and that people need to ask for them to be considered again for the next fork, eg like what Kelly did for 2537 so it shouldnt be an onerous extra process.
* The rationale is that when people look at the EIPs for inclusion after a fork they wont just see a bunch of old EIPs that are no longer relevant. Having CFI reset after every fork clears this list down.
* No objections? Will take it then that people are good with this.

**Decision 6:** CFI status for EIPs is reset after every hard fork. EIPs then need to be put forward again for consideration. [58:04](https://youtu.be/C9hzAYkklQM?t=3484)

**Tim**

* For London, we don't have any CFI EIPs as everything is already in. We can use this process though for Shanghai.

## Frequency of calls discussion

**Tim**

* Martin has a comment re: should we not be making too many decisions on this off-schedule ACD call? Shouldn't the big decisions be made on the regular scheduled calls?

**Micah**

* We should make this an official ACD call.
* Our regular bi-weekly ACD calls are too full. We should make this a regular one and increase the frequency of ACDs as we are benefitting from this.

**Tim**

* I don't feel there is strong appetite to make ACD weekly.

**Lightclient**

* We should use breakouts more liberally ahead of ACD calls.

**Micah**

* Agree that would be ideal, but this doesnt appear to have worked over the past 6-12 months.
* Think we are now in a position where we should own that, with the consequence being we now need to have more frequent meetings.
* If our meetings start getting empty due to more breakouts, we can reduce the frequency of meetings.

**Tim**

* Feels like we do get through the most urgent things on our existing calls.
* Cant easily see examples of where we failed to make critical decisons on time. Eg we're in a good spot for London with decisions made. Some topics need more discussion eg 3074.

**Micah**

* Concern is mainly not that we are not taking decisions, but that there isn't enough time on the ACD calls to prperly discuss the EIPs. EIPs seem to get held up on discussion, not coding. Eg BLS. Time taken to achieve concensus is the biggest holdup. We seem to often decide to not do a thing because we havent spent enough time talking about it. We need better/more frequent ways of talking and agreeing.

**Tim**

* One of the causes feels like we often have new urgent things come up to discuss. Eg BLS not making it into Berlin because the other things were higher priority. 

**Micah**

* This one extra meeting seems to have really helped.

**Tim**

* People are in the chat are suggesting that I/Tim have more meetings rather than everyone else :)

**Tomasz**

* It wasn't just this meeting that caused things to move more quickly, it was team calls in between as well. We all went in aligned ahead of the call which meant the call today went smoothly. Good effort.

**Tim**

* I'm happy to carry this on ahead of calls.
* Concern around not wanting it to seem like things are happening behind closed doors. Happy to keep doing it if people are in favour though.
* Anything else to discuss?

**Lightclient**

* We'll be chatting after the call in Discord lounge on 3074.

**Pooja**

* Reminder that the Ethereum Cat Herders are hosting a [community call on EIP-3074 on Monday, 26 April, 16:00 UTC](https://medium.com/ethereum-cat-herders/eip-3074-community-call-ec87b66672e1).

**Tim**

* Thanks everyone!





-------------------------------------------
## Attendees
- Lightclient
- Peter Szilagyi (GETH)
- Tim Beiko
- Danny Ryan
- Vitalik Buterin
- Ansgar Dietrichs
- Tomasz Stanczak (Nethermind)
- Martin Holst Swende (Open Ethereum)
- Micah Zoltu
- Afri Schoedin
- Pooja Ranjan
- Gary Schulte
- Trenton Van Epps
- Paul D
- Dusan
- Alex Stokes
- Tukasz Rozmej
- Marek Moraczynski
- Yuga Choler
- Piper Merriam


---------------------------------------
## Next Meeting
Ethereum Core Devs Meeting #112, April 30th, 2021 @ 1400 UTC

[Agenda](https://github.com/ethereum/pm/issues/302)






