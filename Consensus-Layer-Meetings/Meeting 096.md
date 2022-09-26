# Cl Layer call 96
### Meeting Date/Time: September 22, 2022, 14:00 UTC
### Meeting Duration: 650 minutes
### [Github Agenda](https://github.com/ethereum/pm/issues/629)
### [Video of the meeting](https://www.youtube.com/watch?v=_yogw67HxZY)
### Moderator: Danny
### Notes: Darkfire-rain

**Micah:** Thank you, welcome. This is call # 96, issue 629 in the PM repo. The next couple of calls are canceled, one is during devcon, one is during the break after devcon, this is primary to recap if anything needs to be discussed after the merge, and any of our other discussion points, to kick it off, first item is the merge, I think by any standard the merge was successful, congratulations. Are there any particular discussion points today about the merge, about what happened, any issues that need to be resolved, any unknowns that surfaced. Okay, I know there are a couple of teams in the execution layer that had some stuff bubble up and they are very actively working on releases, but I'm unaware of any similar issues that have bubbled up from the consensus layer. Anything else on the merge.


**Tim:** Matt, do you want to take a minute or two to talk about the base you were using?

**Matt:** We have a bunch of fixes that were ready for yesterday, but we decided to delay 48 hours to probably be Friday at midday eastern time. Reason being we had even more fixes, but we wanted to test everything in combination, so as to not ask users to upgrade twice within the span of 5 days, so we are putting something out on friday to hopefully resolve these issues, that we identified that is kind of centered around the block import step, which is causing some of the wonkiness around the consensus layer. And then again with some of the things around empty block proposals, we have identified a bunch of cumulative fixes, but we want to test if we can put something out on friday. More news on friday but that's kind of a run down for now.

**Danny:** Cool, anything else on the merge?

**Marius** We have this one. It's not really an issue, it's more like a quirk, that gas is stalling a block when we get the signal from the consensus layer, and we don't upgrade this block until the block has returned from the consensus layer. That behavior will change, and what also changes is the additional 100 milliseconds that we currently wait if no block has been created yet. That means for consensus layer clients, if they send us the ??? updated, with perimeters and then immediately send the new get payloads, then we will return an empty block. None of the clans should do this anymore, it would be good to double check.

**Mikhail:** You mean that previously there was a timeout of 500 milliseconds that the gas would use in this case to build a fog, and return it back right but that will not be the case anymore.

**Danny:** Is there an experimental build that clients can test if there is any concern

**Marius:** Yes i can link a PR

**Mikhail** I was just curious why you have decided to remove this timeout. 

**Marius:** Because we have this recommit now that rebuilds a new payload every 2 or 3 seconds, and it's just not as convenient to have this listening on this anymore. 

**Enrico:** There are some high edge cases where we do send for choice, update with attribute, and then immediately get payed out, and there are the cases where the beacon node doesn't know anything about the prosper, so the api gets the beacon node to say “here I am I am a proposer” there are some cases where this code never reached the beacon node, and the clients immediately asked for a block, and in this case we send attributes and immediately get the payload.

**Terence** Yeah so another behavior which i wish you would eventually address, is that we would like to support some sort of concurrent payload building, so for example, at slot we send a preferred payload, and then at slot 5, and it becomes head, and then at slot 8 we process all the aggravated allegations. And then we basically revert back, so we kind of have this back and forth, so I think it's very useful to support concurrent payloads, just to make bets on what we think the head will be.

**marius:** How long before you actually want to payload, do you do this? I would suggest that if you would give us the perimeters right before. So we only maintain the payload for 12+ seconds.

**Danny:** I think terence means in the interemin of the slot, if the head were to change, it would be worthwhile to support concurrente building, this would be a very fundamental and deep change, and it is probably an extensive process

**Marius:** So we support concurrent payloads.

**Terence:** So if i call a new prepaid payload, you would not cancel the previous one right, until the second timeout. 

**Danny:** So if I send 2 prepared payload messages with slightly different heads, and call git for both of them, I would have results for both?

**Marius:** It might actually not really work, because the second one would stop the payload, so it's actually not working.

**Danny:** Okay thats what i thought.

**Chris:** Because we are on the topic of triggering block building, I was thinking it was a good point to touch on the subscription request. The question is how can block builders get a trigger for stopping blocks. Currently they are using a fork of a big denote that sends a triggered payload event. Or after a timeout if a slot is missed. Typically this is about 12 seconds before the requester asks for a payload, giving the builder time to improve the bit. It would be ideal if this would just be an sse subscription available on all beacon nodes, doesn't seem too hard to implement and there would be no need for any custom forks. Any thoughts or opinions?

**Danny:** So the trigger is a new head, or some timeout into the slot if no new head. So you  see this is critical to not have a monoculture on a beacon node.

**chris:** Because now all the builders and all the relays seem to be using the prison fork that has functionality added. Ideally there would be no need for any custom fork. Would be ideal if consensus layer teams were on board here, this would be a really nice addition to the ethereum ecosystem.

*Danny* Any dynamic input from consensus layer devs today?

**Gajinder** I think the lode star troops are providing the sse rent for the change. And when we talk about how we possess fcu’s basically we stand up to you before the fork starts. Basically we get based on a pedient, because of the proposing slot. At the time of the proposing slot, we basically examine a new FCU, and basically wait  for 500 milliseconds on our own file. This is the way how we possess.

**Chris:** I think the issue is the head even though it is just coming way too late, and we want to trigger block building a long time before that, as soon as possible, which is the new payload event.


**Danny:** And the alternative event would be to manage timing on even on your own?

**Chris:** I think they would just keep continuing the current limitation on the beacon node as long as it is not seen internally. Currently our beacon node is triggering the work of the builders.

**Danny:** So this is an express fortress update of timing, for every single slot instead of validators.

**Mikhail:** Just as a quick idea you can have an interceptor and make the essence depart in this middle way. 

**Danny:** I think we’ve avoided putting the software between cl and el, such that the piece of software does not break the node, so I would argue against that. Fork choice update is still not sufficient. 

**Chris:** It doesn't include all the attributes I think we need.

**MIkhail:** This Is mainly because we can have these 2 competing forks with no builder	with no builder, we don't know which one will be requested by the proposer. So we view payload A as the hat, it should also build on top of payload B.

**Danny:** Okay i know we’re moderately low attendance today, let's take it to the issue and discuss it there. Any insights, issues, discussion points on the merge?

**Mikhail:** According to the beacon chain, the block explorer, I can see some block donations in the upper suspicious, has anyone investigated into these?

**Danny:** So a drop in 3 percent usually represents some amount of miscoordination. That would be my hunch for some of this. Especially when you see 99.3 to 96.4, but if there is an additional thing going on here that would be interesting

**Mikhail** Yeah I haven't looked too closely into this so that's why I think it isn't related to the merge. 

**Danny:** Okay Chris, you wanted to show an update on the first week?

**Chris:** Yeah I just wanted to show how it is going on the first week, the merge is going great. In total 5 parties are running relay block relays manifolds. Before closing i want to touch on the problem that the blocks are not relaying before the bits, which means proposers that included the blocks throughout relaying and the blocks having the best bits, would assign the beacon blocks, and not getting the payload for it, this was a problem for about five hours yesterday, notifying people as soon as we found something was off. I think there should be a current breaker, or at least a really easy way to stop sending out bits, that as soon as problemsoccour, you can instantly stop the bits, basically just means return to s afr taste of code on the getheader api. We also relay to populate post-mortems on any such incidence. The blocks team was saying they are going to reimburse for the loss of bits, I wanted to mention that here as well. I’m able to ask any questions about this for as much as I have information for. I can confirm this has been resolved yesterday after five hours. 

**Micah:** The validation registration count in the image state, is that the actual validators using the relay or is that just a form filled out online.

**Chris:** No this is registration api system proposers, cumulative since the beginning, this does not necicsarrilty mean active proposers, we are not currently tracking those. 

**micah:** So we don't have data yet on what percentage of blocks are being built yet?

**Chris:** There is some data.

**Terence:** I want to add on to micahs question, i think we do send registration every epoch, so you can also do some tuning, for example the validator who has not been responsive since the last epoch, you can remove them to make the data more accurate

**Chris:** Yes absolutely there is ways to get more accurate information, but we just have not gotten around to that yet

**Danny:** Any other questions for chris? Okay great thank you. On research specs, etc, I do want to comment that what is going on in Shanghai is not set in stone, certainly withdrawals and 448 will be part of the conversation. So on the consensus layer side, if you are intending to do deep dive, review, testing, or anything related to these specs, now is the time. I think there will certainly be many conversations at devcons, and our top priority will be to sort out what will go into the next update. Naming wise, there is a desire to vote as the past. And then there is also a bit of a call for unified naming, which if anyone wants to take the charge on that as a discussion point today by all means, I don't have much on that myself though. Anything else on research sepc domain. Any other discussion points or closing remarks? Okay, great work. Enjoy the break for these calls and see many of you in devcon.

