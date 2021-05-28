


# All Core Devs Meeting 113 <!-- omit in toc -->

 ### Meeting Date/Time: **May** **14th**, **2021**, **14:00** **UTC** <!-- omit in toc -->
 ### Meeting Duration: **90** **mins** <!-- omit in toc -->
 ### [GitHub Agenda](https://github.com/ethereum/pm/issues/309) <!-- omit in toc -->
 ### [Audio/Video of the meeting](https://youtu.be/H_T2nNrTuWQ) <!-- omit in toc -->
 ### Moderator: **Tim Beiko**<!-- omit in toc -->
 ### Notes:  **Kenneth Luster**<!-- omit in toc -->

-----------------------------------------------

 # Contents <!-- omit in toc --> 


- 1.[London Updates](#1-london-updates)
  - i [Baikal Status & Next steps](i-baikal-devnet)
  - ii [EIP-3541](ii-eip-3541)
  - iii [EIP-3554 (EIP-3238 alternative)](iii-eip-3554)
  - iv [JSON RPC Spec Naming](iv-json-rpc-spec-naming) 
  - v [Block Numbers](v-block-numbers)
- 2.[Other Discussion Items](#2-other-discussion-items)
  - iv [Merge/Rayonism updates](iv-merge-rayonsim-updates)
  - iiv [1559 UI Call Announcement](iiv-1559-ui-call-announcement)

  - [Next Meeting Date/Time](next-meeting-datetime)
  - [Attendees](attendees)
  - [Zoom chat](zoom-chat)
 

-----------------------------------------------



 # **Summary**:
 
  ## **DECISIONS & ACTION ITEMS**
 | Decision Item | Description | Video ref |
 | ---------------  | ------------- | ---------- |
 | **113.1**   | **Baikal Devnet** will be around till the 1st Testnet is forked | [8:40](https://www.youtube.com/watch?v=H_T2nNrTuWQ&t=520s) |
 | **113.2**   | **EIP-3541**,will be added to **London's Spec.**| [13:10](https://www.youtube.com/watch?v=H_T2nNrTuWQ&t=587s) |
 | **113.3**   | **EIP-3554: Difficulty Bomb** Delay to December 1st, 2021- the difficulty bomb calculation should be reviewed 3-4 weeks down the line. | [14:08](https://www.youtube.com/watch?v=H_T2nNrTuWQ&t=848s) |
 | **113.4**   | **JSON RPC** Naming Convention for the various fields that **EIP-1559** will be the same as mentioned in the EIP.| [17:52](https://www.youtube.com/watch?v=H_T2nNrTuWQ&t=1072s) |
 | **113.5**   | **Block Numbers and Dates** restated | [31:00](https://www.youtube.com/watch?v=H_T2nNrTuWQ&t=1860s) |


 # 1. **London Updates**

 ## **Baikal Status & Next steps** [8:40](https://www.youtube.com/watch?v=H_T2nNrTuWQ&t=520s)
 
 
 **Tim Beiko**

  And, we are live. So good morning or evening, everybody. Welcome to the All Core Devs number #113. We have mostly London stuff on the agenda today. There's been a lot of work on that, over the past couple of weeks. No background today. No, I guess I can kind of blur it or put my Ethereum background if people prefer that or back in the Blockchain, cool okay. So, for London first thing. So, every team I think was thinking to **Baikal** this week, which was the new Devnet. I don't know if someone wants to give a quick summary of where things are at with, the network.


 **Marek Moraczynski**

 I can give you **Baikal Status**. So, instance we have five **nodes** two guest, two **Netherminds** and one **Besu**. They are all in sync. As far as I know to the book F is in sync too, I'm not sure about **Open Ethereum**
 in **Nethermind**. We implemented three fonts, the last **1559** doesn’t need changes and **EIP - 3541** , all Clients seem to be working fine, but it will be good to test it in the same way as Jochem from the **Ethereum JS Team** that tested the other **Network**. So, you all can feel free to do that, that's all, I think.


 **Tim Beiko**

 Yeah, is anyone from **Open Ethereum** on the call to give a quick update of where they are? I thought I saw, I'm not sure that they posted a **bootnode**? Yeah, anyone from the team wants to share where you're at?


 **Dusan**

 Yeah, yeah, we have the updated issue on a defect, we still are missing the guest three fonts, **EIP** implements for the **Baikal** also we are not able to see at the moment.


 **Tim Beiko**

 Okay, this is the last one you have to implement.


 **Dusan**

 I am


 ## **EIP-3541**  [13:10](https://www.youtube.com/watch?v=H_T2nNrTuWQ&t=587s)
 
 
 **Tim Beiko**

 Okay Got it.
 So, what did people feel makes sense in terms of next steps for **Baikal**? My personal preference is probably to keep it up and running you basically until the **fork** and the reason for that is it gives basically tool, tooling and whatnot. The you know, a network that they can use that's already up, if they want to play with **1559** or stuff like that. 


 **Tim Beiko**

 Does anyone disagree with that?
 Do people think there's other things we should do, with the **Network**?


 **Martin Swende**

 I think it sounds good. I don't know how much, how many transactions. has been sent over it. I am, I personally have not done anything. It would, yeah, it would be good to keep it up to. So, so other people can experiment more with the, their codes, and going up and down on the gas limit, there were some changes made on the **1559  Spec.** regarding to how much the gas limit, well the mechanics where how gas can vary up and down. So, that will be good at that also is tested, but I'm not sure if we have, if that has been covered, I suspect not.


 **Tim Beiko**

 Got it so, yeah, I think I agree that makes sense. I know I've had built a **tool** that we could use to spam. The networks we built when where **Developing 1559** , I suspect we should be able to use that on **Baikal** as well assuming there's an address with enough **Eth**. So, in general, just keeping the network up, obviously letting **Open Ethereum**, the time to sync up to it. Having both, manual transactions on it and people playing around with it and then trying to make sure we test the limits of the gas limit up and down. That seems reasonable. Anything else on **Baikal**? 

 **Tim Beiko**

 Okay, so next up on the agenda, I had the **EIP 3541**, which is the **EIP** by **Axic** which has been implemented in **Baikal**. We didn't want to make a decision about inclusion in **London** last time, because it was kind of the first time that it was brought up on the call. I'm curious how the people feel about, including it in **London** now. It seems everybody's had it implemented, so yeah. Any yeah thoughts, objections, support.


 **Martin Swende**

 I’m in support


 **Artem Vorotnikov**

 Let’s include it


  **Tim Beiko**

 Cool

 ## **EIP-3554: Difficulty Bomb**  [14:08](https://www.youtube.com/watch?v=H_T2nNrTuWQ&t=848s)


 **Tim Beiko**

 Anyone disagree with that? Okay, I feel much better because when we take stuff out at the last minute, that's usually a bit risky so let's include **3541**  into **London**. I'll update the spec right after this call.
 Similarly, over so two calls ago I think we agreed to move back the **Difficulty Bomb** to uh December 1st, roughly rather than Q2 which was originally proposed in **EIP 3238**. James has been working on an alternative **EIP** so **3554**  which pushes back the **Difficulty Bomb** so uh I think the first, the first increase would happen I believe around December 7th you said James.


 **James**

 Yep


 **Tim Beiko**

 So, you want to take a minute to walk us through it? 
 Like, I know you worked on some back tests for it to make sure it lined up rite, do you want to?


 **James**

 Yeah, yeah so the there’s a script in the **EIP** itself you can run to check at this and it looks at the difficulty adjust coefficient based on the current Epic what it would be that's kind of pushing up the difficulty so the block time increases, and I went back and looked at the last three times that we first saw the **Difficulty Bomb** go off and all of them were right as it hit 0.1 on this ratio, which if we were to do this 9,700,000 than 0.1 is reached on the December 7th, which is when the first time that Epic of every 10,000 blocks, the Epics switches over on December 7th. So, it looks like it's pretty good I use, yeah, I don't know if anyone else looked at it, but I went onto as many avenues as I thought to double-check and so at this point, I'm pretty confident about it. The only risk is if the difficulty on the network changes significantly then when that 0.1 ratio happens could happen earlier or later.


 **Tim Beiko**

 Yeah, I just, I evolved and looked at the numbers you know the current **EIP** that we added in near glacier, which is going to go out soon and basically, we're adding an extra 700,000 blocks to that **EIP**, which is roughly four months so July plus four months was December.  
 So that was my very low-tech way of eyeballing it. Did I, I think I saw **Geth** has already **Geth** has a PR open for this?


 **Tim Beiko**

 Uhm, I don't have a


 **Martin Swende**

 Uhm yeah


 **Martin Swende**

 We actually, we merged the original number, and we have a PR for the second, so we have 9.5, but we had an open PR for 9.7 and


 **Tim Beiko**

 Okay, does anyone else have thoughts about this? 
 Yeah, sorry there was a comment by James in the chat that like yeah July plus four months is November, but the bomb was going off end of July not beginning of July it's basically end of November not November 1st. Cool does anyone, is everyone okay basically moving this into **London** and updating a **3238** to have instead of **3554**? 


 **Tim Beiko**

 No objections?


 **Martin Swende**

 Yes


 ## **JSON-RPC Naming Convention**  [17:52](https://www.youtube.com/watch?v=H_T2nNrTuWQ&t=1072s) 
 
 
 **Tim Beiko**

 Yep, last call. Okay so, in **London** this is going very quickly now to something I think might take a little more time on the call.
 **JSON RPC** naming I was hoping we could resolve this async, but it seems like it's an impossible problem. 
 Basically


 **James**

 Tim, can I say one thing bomb first?


 **Tim Beiko**

 Yep


 **Tim Beiko**

 Go for it, yeah.


 **James**

 Which is, I think if there's some way to schedule this, we should come back in two months and rerun and have someone rerun those numbers to check that the ratio doesn't change at all. 
 So, like four or five **All Core Dev’s** from now.


 **Tim Beiko**

 Yes, I will absolutely uh do that yeah.


 **James**

 Sweet


 **Tim Beiko**

 Yeah good 


 **Tim Beiko**

 Yeah, good call cool. **JSON RPC** naming, so I’ll try to summarize where things are at, and hopefully we can come to a decision on it now and the main reason why it would be really good to come to a decision on it now is we're building these **Testnets** for **Infrastructure providers** and basically the naming of the fields is the main thing that's blocking people from playing around with this and obviously they can support it  you know then changing names in the future but that's kind of a bad experience. So, I think it was two weeks ago the **Geth Team** put up, put up a **Gist** talking about basically the **JSON RPC** renaming and the Header Field renaming, we got their pretty quick consensus on how we would rename the headers.
 But for the **JSON RPC** the argument from **Geth** was, we should use kind of variable names that were shorter than the ones in the **EIP** so that **EIP** uses max priority fee per gas and max fee per gas, and stuff that's kind of aligned with the other naming conventions that are used in **JSON RPC**. 
 The two that were proposed were gas tip cap, and gas fee cap which obviously aligns with gas, limit gas, use gas price then we kind of had this long conversation on discord with a vote, and it seemed people liked base fee per gas too to specify the base fee, priority fee per gas for the priority fee, and fee cap for gas for the fee cap.
 One problem with that is that priority fee per gas, doesn't make it clear it's a maximum value. So, it's not actually the value that you pay but it's maximum that you're willing to pay so the obvious suggestion there is you changed up the max priority fee per gas. Then you're basically back to a spot where two of the three terms have the same name as the **EIP**. 
 It would be weird to also not switch back to just using the **EIP** obviously **Geth** suggestions were moving away from using the terms of the **EIP** and the one concern that people seem to have with **Geth** suggestions or at least the biggest one was people didn't like the fee term instead of that we could use gas price cap. One challenge with gas price cap is it's obviously very close to gas price and it might be more error prone, and people also don't like the tip term and so an easy fix there is gas priority cap so that's kind of where things are at.
 I don't know, yeah if people have opinions or thoughts this is the time.


 **Martin Swende**

 Yeah, sorry for asking this question rite when you summarize everything but is there anywhere a kind of concrete summary it's not suggestion of yeah, what the current or what's the let most recent proposal


 **Tim Beiko**

 Yeah


 **Martin Swende**

 Is?


 **Tim Beiko**

 I just posted it on **GitHub**. I added a comment to **Peter's Gist** to yesterday to **summarize** it so I think as I understand it not everybody agrees on this obviously, but base cheaper gas seems universally agreed upon the two that I think could work for the other fields would be gas price cap, and gas priority cap.


 **LightClient**

 So, I don't know this is kind of hard to really bike shed the specifics of the naming just for the voice.


 **Tim Beiko**

 It's kind of hard with text as well.


 **LightClient**

 Yeah, I personally prefer to not have the per gas postfix I'd rather have the gas prefix and then describe. I think that lends itself to shorter names and it's similar to how we already describe the gas price.


 **Martin Swende**

 I was, I was leaning towards that earlier because of the following, the reasoning that gas price oh that meant per gas but then I read Micah wrote that. Yeah, it's a different thing because with the gas price, it's kind of obvious because of the connotations with price that it's you know the price you pay per unit whereas for the other I don't actually I think it's more clear if it's per gas than if it's a gas prefix yeah so, I, I'm leaning I'm personally more in favor per gas as it is more explicit.


 **Artem Vorotnikov**

 I'm sorry, so this is just about the naming right now.


 **Martin Swende**

 Yes


 **Tim Beiko**

 Yes, it might seem like it's a waste of time, but we tried for.


 **Artem Vorotnikov**

 But I think, I think nobody gives a shit.


 **Martin Swende**

 I think you are wrong there, there are people


 **James**

 You are very wrong


 **Tim Beiko**

 My experience is people have pretty strong opinions about it and are not willing to like, or at least it's hard to get the consensus on it. Async, yeah


 **Martin Swende**

 Yeah, the thing, the thing to kind of bear in mind is that we can make this choice once and it's going to be a pain in the ass to change it later and if we do a bad choice, it means the UX is going to suck and it's going to be confusing and people are going to shoot themselves in the foot they're going to not understand that this is actually not the value. The, the cost for me is going to be multiplied by 25,000 because it's per gas and it's not an absolute so if we can avoid that I do think it's important.


 **Tim Beiko**

 Yeah, and one thing I think Micah was the one who mentioned that on discord a lot of apps will you know just pass through these parameters that our users like they'll take whatever's from **JSON RPC** literally exposed that so yeah, I agree if we can have stuff that's more descriptive that probably makes sense.


 **Rai**

 Matt, did you have another reason to prefer the gas prefixed ones other than uh the shortness and consistency, I guess?


 **LightClient**

 No I think those are my main, this is the main reason, you know the like if we start doing max priority fee per gas, now you're having you know 50% or more just describe you're trying to set up what this even means you're saying max, you're saying per gas, you're saying priority fee that's the thing whereas you could just say gas fee cap, or gas tip cap, and so now it's a much I find that easier to reasoning about it and I, I don't really agree so much with Mica's reasoning that prices what's giving it the per unit of gas. I think that's it I think gas what's it saying that this is per gas because you could have TX price and that would not be you know per gas though that would be per TX.
 So, I think I'm one of the few people at this point still on the gas prefix train. I'm not gonna die on the Hill but I, I prefer it maybe my preferences on founded because I have spent the last few months staring at these names and the thought of having to type two X more characters to do something is probably not something that we should be using decide how everyone else is going to interact with it but those are my thoughts.


 **Micah Zoltu**

 I will personally buy you a text editor that has auto complete.


 **LightClient**

 I thought you were personally going to hire someone for me. It's just to fill out the remaining characters,


 **Laughing**


 **Micah Zoltu**

 Excuse me. I need to swap places with you Okay, go ahead.


 **Rai**

 He will, he will write to a macro so that those names are just one Keystroke that.


 **LightClient**

 We can fill a grant out for that, I think.


 **Laughing**


 **Tim Beiko**
  
 So, I guess aside from my client does anybody else like strongly in favor of the gas? Cause I, I, I think Martin, Peter's not on the call but he was also in favor of that.


 **Martin Swende**

 Yes


 **Martin Swende**

 Yeah, I was just gonna say uhm, so I don't speak on behalf of the whole **Geth Team** uhm, Personally


 **Tim Beiko**

 So, nobody else is willing to defend gas, in that case it feels like there's also more clarity and just we would be using the same we'd be using basically the same terms as the **EIP** rite we would have max priority fee per gas, fee cap per gas and base fee per gas. that would just yeah, so we basically do not need additional names for **JSON RPC**.
 Does anyone oppose that last chance? If not, I will let the folks working under the spec for **JSON RPC** know, oh somebody speaking **Ansgar** is he is on the call.


 **Ansgar Dietrichs**

 Oh yeah, I uhm I think I'm weakly kind of in agreement with LightClient but I that I don't have like any strong opinion. I personally don't think like I also have like of problem with priority fee, but I think the proper place discuss that would just be the EPI itself so.


 **Tim Beiko**

 And luckily, regarding after the merge we will need to do some changes to **1559** so we can reopen all these cans of worms.


 **Laughing**


 **Micha Zoltu**

 Regarding priority fee that like the word priority there we've gone between, I think, six different words in the **EIP**. trying to find a solution if someone has something novel and new and we can give it a try everything is problematic. I think the core reason why we're struggling is because that's that particular value means two different things to different people so if you are gas warring then it is the thing that gets you to the front of the line. If you are just a regular user with **1559**  it is the thing that gets you into the block.
 So, it's serving dual purposes sort of and so finding a name that satisfies both is very hard and so we ended upkeep changing it to kind of just swap between naming it for the favoring of the one thing, and then we name it to favor the other, and back, and forth. 
 If anybody come up with a word that handles both, please share it.


 ## **Block number discussion**  [31:00](https://www.youtube.com/watch?v=H_T2nNrTuWQ&t=1860s) 
 
 **Tim Beiko**

 And we will use that word any too but yeah, I guess okay let's just stick to using the terms that are in the **EIP** and expose that in the **JSON RPC**, and hopefully we'll have the adjacent **JSON RPC** back ready within the next week or so. 
 Anything else on **JSON RPC**?
 Okay I guess the last thing I had on **London** is trying to figure out how people feel with regards to timing for the upgrade. I believe everybody aside from **Open Ethereum** has the **EIP**’s fully implemented a couple what is it months or calls ago?
 We had kind of this, this tentative timeline where we would basically try to agree to a client freeze today which is I think where we were at so that teams would have another two weeks to release client that's London compatible, and then we could have our first **Testnet Fork** on June 9th and the first **Mainnet Fork** on July 14th. 
 How do people generally feel about that schedule? 
 Did it feel, something that's realistic, is it something that we want to push back a bit?


 **Tim Beiko**

 Yeah, any thoughts there?


 **Martin Sweden**

 I mean, I think that it is a bit optimistic, and I think that maybe I have the feeling that this might be most **YOLO, Hard Fork** we've done so far but yes still I think it maybe we should just bite the bullet and do it anyway because we have this when we need to get the next **Hard Fork** out and we've been working on **1559**  for a long time but I think the big problem at this for the **Geth Team** is that well I mean the consensus changes are one thing but there's you know a lot of things that need to be touched in the transaction pool logic, it's a lot of touch changes needed to be done for the miner, and where various other subsystems. So, it's big upgrade and we're not going to be able to do it Client freezes anytime soon I think because yeah there still even if we have the base functionality. We, we don't even have that much but even if it did there was there'd be another two or three PR’S follow up PR’S to add this other stuff.


 **Tim Beiko**

 Unless


 **Martin Sweden**

 I think that we can live with the dates, I think but yeah, I'm just throwing it out there that it’s we need to do a lot of testing.


 **Tim Beiko**

 Is this something where like changing it by two weeks would you know would help a lot too or is it something where you know in a perfect world. You'd have two extra months to do the testing, and I guess that there. Sorry, the reason I asked that this date was mostly set because of the **Difficulty Bomb** there's been kind of an increase in **Hashrate** on the network. 
 So, I suspect we probably have you know a few weeks of leeway if that makes a big difference for **Clients**


 **Martin Sweden**

 So


 **Tim Beiko**

 We definitely don't have like months of leeway so that's kind of it.


 **Martin Sweden**

 So yeah, for me personally my I always think that **Testnets** ultimately are there to test to prepare for Mainnet. So, I don't think we should post hone **Testnet deployments** I think if anything we should do them sooner so that we have more time to actually test everything on the **Testnet** before it hits **Mainnet**, but I know that other people feel differently about **Testnets**.


 **Tim Beiko**

 Got it, how do other client teams feel when they’ll assume that they are mined on **Open Ethereum** Tooling throughput yet?


 **Asz Stanczak**

 We are generally okay with the timings yeah, I think I agree that we want to say that the community to move with the **Tooling** connection experimentation, and if they have the tests earlier, the solving the better, I think that's date was announced for a while and we haven't changed it in a month or so if we see any problems whatsoever in the **Testnets** then we should review and consider then to have **Mainnet** bit further down but for now I would stick to this, mid-July date.


 **Rai**

 Yeah, I agree that I don't think we should be postponing the **Testnets**. Also, I don't know whether we're ready for a code freeze, yet we definitely have the meat of the **EIP**’s all in, but similar *ancillary logic, like mining, and transaction pool** we need double check.


 **Tim Beiko**

 **Open Ethereum**?


 **Dusan**

 Yeah. I agree with last statement. Yeah, we’re not fully prepared for the freeze, freezing and we're already a bit late for that but in general for the July 14th I think that will be a problem.


 **Tim Beiko**

 Okay and so rite now basically the first **Testnet** would be on June 9th, which is 3-ish weeks huh is that rite?
 Yeah, Three and a half weeks.
 You know Martin seemed to feel that keeping it close is better. Does everybody also agree with that? Because we could also push to **Testnet** that back one week and or if that made a difference but then it's like we get less time on **Testnets** before we go on **Mainnet**. Would be I guess if people want to push back the **Testnets** to get more time for **Client Freeze**. Now's the time to speak up otherwise, we can keep the first one on July 9th sorry, June 9th.


 **Martin Sweden**

 Which is the first one?


 **Tim Beiko**

 So, I had **Ropsten** the first one but then this is just because that's what we did for **Berlin**.
 So **Ropsten, Gorli, Rinkeby** we can absolutely change them if there is a reason too.


 **Artem Vorotnikov**

 And the main, the Mainnet date would be?


 **Tim Beiko**

 The **Mainnet** date is July 14th as of now, so the **Ropsten Testnet** would be live before like four huh six weeks before the hard fork then it would be five weeks then, like, oh sorry, five weeks, then four weeks, then three weeks, between the last **Testnet** and **Mainnet** and obviously I see if anything goes wrong on the **Testnets** and whatnot, we can push back that yeah, but assuming everything goes smoothly, that would be the schedule.


 **Martin Sweden**

 Think that sounds okay.


 **Tim Beiko**

 Yeah, James has a comment like, if we push **Mainnet** two weeks back we could get five weeks on the **Testnet** yeah, okay. 
 So, uhm so basically let's do that. I had proposed some blocks for those dates in the **GitHub** issue yeah so, I just if people want to like to put them in the **Clients** now but basically a block on 
 **June 9th** on **Ropsten** would be **10399301**
 **June 16th** on **Gorli** would be **4979794**
 **June 23rd** on **Rinkeby** would be **8813188**
 The **Mainnet Fork Block** on **July 14th** would be **12833000**
 Uhm unless anything is wrong with those blocks, I double-check them yesterday.
 I propose we go with those, and this way **Clients** can start putting them in whenever they're ready and working on their release.
 Does that make sense?


 **James**

 This might be 


 **Yuga**

 Yeah


 **James**

 Harping on to an earlier conversation but if we just did the **Testnet Blocks**, but then didn't set the **Mainnet Block** until we know a little more about how the **Testnets** goes or do we want to do them all kind of now-ish? 


 **Yuga**

 I guess like one question I'd love to get a sense of is like if like we run the Testnet and it's like we need to push Mainnet out by a week would that be a big deal or like is that kind of okay.


 **Tim Beiko**

 So, I think a handful of weeks is okay and the only challenge it's basically the same challenge in why you want to hard code all the blocks at first some users might download a version which has **London** enabled only for **Testnets** that they think they upload. They think they've upgraded, but there actually isn't like a block number in for **Mainnet**. So, you kind of get the similar thing where if we do push back the **Fork Block**. Uhm it's not the end of the world but you risk having some people think that they've upgraded they don't read the blog posts or the announcements and whatnot and then they're on a version which has the wrong **Fork Block** for **Mainnet**. It's not you know it's not something I think we should do unless we find like a major issue, or we realize you know we're absolutely not ready but it's also not impossible.


 **James**

 Yeah, and the other end is if we have the **Mainnet Blocks** in and everyone's installed the **Clients**, and then we need to delay two weeks, then there could be an important part of the network that's splitting two weeks earlier than the other one if they didn't if everyone has to change the client that they have.


 **Asz Stanczak**

 Yeah. We usually avoid a hard coding, Mainnet blocks together with the Testnet blocks. So, we add Testnet box numbers first and then we release after the first Testnet’s going successfully or at least the next version with Mainnet set like any historically the same Mainnet block number changing, until the last weeks and we didn't want that to risk that like not switching felt for us less risky than switching and the wrong block and trying to revert it. 


 **Tim Beiko**

 Yeah, that's totally something we can do for **London**. If people are more comfortable with that we can wait until the **Rospten fork** and then we can keep the current block like tentatively and if everything goes well use that one but yeah, if people want to wait before we hard coded in **Clients** yeah to see that the **Rospten** and maybe like the **Gorli Fork** goes smoothly.
 Do people prefer that? 


 **Martin Swende**

 Yeah, that's probably what we, I mean that’s what probably, 
 that's what we've done historically in **Geth** as well. I think.


 **Tim Beiko**
  
 Okay


 ## **Speeding up transactions by clients/wallets** [43:42](https://www.youtube.com/watch?v=H_T2nNrTuWQ&t=2622s)
 
 **Tim Beiko**

 Okay let's use let's basically use the current Testnet blocks that where proposed. I see Thomas has a comment about the main block that to add one more zero so anyways we can kind of bike shed around that one offline but yeah, let's use the current **Testnet** blocks for **Rospten, Gorli, or Rinkeby**, assuming the **fork** goes well. We'll basically have a fork rite after the we'll have an **All Core Dev** call rite after the **Rospten fork** we can decide there if we feel comfortable setting the **Mainnet Block**.


 **Tim Beiko**

 Yeah, Cool


 **Micah Zoltu**

 Before we move on out of the **London stuff**. 
 So, someone brought up that in order for wallets to correctly do **transaction speed up**. They need to know what the Clients are going to accept and gossip for transaction speed up there is value in us kind of coming to some general consensus on what the requirement what each client requires for speeding up a transaction, speeding up the transaction and being replaced by fee basically so, I guess the first question is do Clients have the various Clients decided what you guys are going to do for that yet?


 **Asz Stanczak**

 Yeah, we'll calculating the miner's fee I'm in like the payment to the miner as the selection process for which transactions to evict and which to keep.


 **Micah Zoltu**

 Okay So, so you calculate how much is going to the minor specifically, and then you sort by that, and then you kick out the Okay. 


 **Tim Beiko**

 Anyone else?


 **Ansgar Dietrichs**

 I think that for the **Geth Implementation** specifically, that LightClient and I helped with, we had like of a little bit of an internal debate like I personally kind of prefer the like specifically for replacement not for general eviction, but just for replacement from the same sender, same nonce. 
 I think there are two alternative approaches you can either just you can either basically enforce like a bump of both the fee cap and the tip, or you can basically just acquire a bump of the tip as long as of course the tip is remains smaller equal to the fee cap and I, I think both basically work it should just be like playing should just do the same thing because otherwise the pool gets fractured which is not ideal.


 **Micah Zoltu**

 Doesn’t the letter if you just bump the miner’s portion doesn't that allow someone to spam a transaction that they know won't get mined because you set your advantage that your fee cap to zero, and then you can just bump the miner fee over and over again. 


 **Ansgar Dietrichs**

 So, we


 **Rai**

 We don't allow transactions with a tip greater than a fee cap.


 **LightClient**

 MemPool


 **Ansgar Dietrichs**

 Exactly. So, so basically like because, because we are already it's basically the same situation that we have today without **1559**  we enforce like a minimum Eth tip or like a minimum today of course minimum gas price and, and so basically it is like there is a minimum of how costly like the first bump is and then each subsequent bump will be more costly. 
 Similarly, today if the gas prices I don’t know, 60 gwei or like a 100 gwei or something and your transaction right now as a guest price of one then you can pump a couple of times before you'll get close to the inclusion zone and this basically property will kind of be the same afterwards, basically like the but given that like your total fee cap must be higher than the tip basically every time you bumped the tip you kind of also have to keep up the total cap you're getting closer and closer to inclusion and so it's basically the same as it does today.


 **Micah Zoltu**

 Okay. I think the key there is that you do not gossip transactions and have a tip higher than the cap. Is that correct? Under any situation?


 **Ansgar Dietrichs**

 That's correct. 


 **Unknown Speaker**

 Yes


 **Ansgar Dietrichs**

 I think technically they are includable in the book, but at least we **Geth Implementation** right now would not gossip them. 


 **Micah Zoltu**

 Okay, whatever we decide on, we, I definitely do think we should make that available to wallets as soon as possible so once each of the teams has decided what your strategy is going to be please share it somewhere. It can be in like in the **1559** the channel, **R&D Discord** or somewhere they can get those correlated and out to wallets because they will need to kind of use the lowest common denominator strategy for dumping if they want to be able to gossip across the whole network it's like, whatever the most strict client is what the left follow.


 **Tim Beiko**

 So, yeah on that Trent I don't know if Trent's on the call. Ahh yes, he is, Trent is going to be working on sort of a cheat sheet for **Wallets**, regarding **1559** so if people can just yeah just thumb that into discord Trent and I can definitely keep track of the responses and share it out with wallets.


 **Ansgar Dietrichs**

 Maybe as a follow up on this specifically on the replacement there was anything left to discuss but like as a follow up. I think a couple of months ago we talked about the kind of like the rules around include in general as well and I kind of flipped and looked into that as well. And I think while it's not consensus it's critical it's also valuable to have those this be in sync as well between different Clients otherwise again there's this structured situation where different Clients keep different transactions in the **Mempool** and different ones then there's just like really inefficient for the because you might Re-Gossip some transactions a lot an so and so I just wanted to kind of ask what the best process would be to maybe offline or something just double check that Clients ideally to the same and if they don't kind of maybe come to agreement or something yeah.
 Like what would be the best way of just kind of reaching out to our **Clients**.


 **Tim Beiko**

 Maybe we can discuss this on **Discord** and on the **1559 Dev Channel**, I think some folks are actually discussing this right now I, and Ansgar I shared the writeup you had done of that kind of explains in more detail which you basically went over just now. So perhaps it's useful to like have people look at that and explain how they differ or like don't differ from it yeah, we can definitely document the differences and yeah


 **Ansgar Dietrichs**

 Okay Sounds good I'll look over it again today and just make sure it's still in sync with the fork Geth is the Geth’s limitation at least just doing today. 


 **LightClient**

 If I can also just make one last comment the way it sounds like several Clients have implemented is like I think the most correct way you're using whatever the effective gas price the transaction is so you're subtracting the base fee and then determine service turned out some of the miner is going to earn and that's sort of is like what the network deems is the best transaction but since the base fee is constantly moving that's needs to be recalculated each transaction and it's not a linear relationship as you began to get to the point where transactions become invalid their fee cap the basically goes past the fee cap you would need to start removing those transactions you have to recalculate this ordered list every block whereas if you use the fee cap which is not changing as your order list then you don't need to reorder all transactions every block and the way that we're doing that with Geth is there's a heap of transactions so you will only re-heap once the heap has been has seen some number of new transactions and structurally needs to be re-heap so it's not clear if that it's not clear to me if we can allow the resorting on every block generally I'm trying to avoid any degradation of performance and so I can run a benchmark to see to compare how those would look but that's just the main difference between those approaches.


 **Ansgar Dietrichs**

 And so I would take issue with saying that this would be the most correct way of doing it because I think, the main kind of consideration that went into recommending the fee cap instead of the current effective tip basically as a criterium it’s just that we expect like most normal conditions like the vast majority of the **Mempool** and ****1559** **  to below the count base fee because like this only on average like one block worth of transactions kind of above the Includability zone basically and so like especially for eviction we be most interested about the, the most least valuable transactions those will always almost always be below include Includability the effective tip rite now will be always be zero for them just sorting by tip generally doesn't work as well because usually like the effective tip that you end up paying will be much lower than the tip if the tip is large but you’ll lower Includability because you will barely be able to get in so like effective tip will be small and so I think actually like the fee cap is the most correct way for sorting and not the effective tip and not the tip but again I think it's probably better a benefit for our client and it's not consensus critical and so it's not kind of like critical to have that be in sync and time for the Testnet but yeah.


 **Tim Beiko**

 It's also something we can update once **1559**  is live rite so obviously we want like the best behavior that we know of now but once we actually see usage on the network and how the **Mempool** is working, we can definitely change yeah how transactions are started based on that. 


 **Ansgar Dietrichs**

 Yes, I think that's correct


# **2. Other Discussion Items**


 ## **Merge** And **Rayonism** Update [53:26](https://www.youtube.com/watch?v=H_T2nNrTuWQ&t=3206s)

 **Tim Beiko**

 Anything else anybody wanted to bring you on **1559** or **London** in general? 
 If not LightClient had asked for an update on a **Rayonism** and word the merges at, I see we have Danny on the call. 
 I know you've been on top of that there and I know also a lot of the actual **Client Teams** have been working on this.
 So, does anyone want to kind of walk through maybe the past couple of weeks of what happened with **Rayonism** and where the work related to the merge is at.


 **Danny**

 Yeah, I can give a quick high level uhm so there was the **Rayonism, Nocturne Devnet ** that launched I believe a couple of days ago uh there's a block Explorer up and a Fork Monitor up. If you want to check it out. I believe all **12 Client** Combinations are working on that which means there's kind of four **Eth2 Clients** and the three **Eth1 Clients** and you can mix and match all of them they're all running there and running validators which is very exciting this was definitely a major success but also definitely kind of in this prototyping zone we did not test the Fork Transition and we are not testing like historic facing which is two critical things uhm definitely in the wrapping up phase that we validated all the things that we wanted to but now I think it's time for production engineering on the finale things for London and the **Altera** Fork at the same time we're working on specifying a couple of last things and greatly enhancing testing on the spec for the merge spec based off of some of the stuff we did here and some of the stuff that we've just been committed to do and so I think the idea is to shift back towards some other production engineering and get the merge specs and the next iteration and then once we get **Altair** in London releases out a shift back into some production engineering here uhm so Devnet’s up. Devnet went really well, Devnet will probably go down early next week, and we have shift back into other things post **Altair** post London we'll do some more **multi-client** Testnet stuff and probably have much more of a conversation here on all the things and I guess over the next like couple of **All Core Devs** we can talk more about planning and stuff. The client teams here if ya’ll need to ask please do and otherwise I can help with any questions if anybody has or wants to dig deeper on that. Cool another thing to note is we're doing some bike shedding if you'd like to jump in on **API, Transport, and Format**. 


 **Micah Zoltu**

 For all those that enjoyed the naming discussions so much go join consensus client name on the discussion.


 **Danny**

 And a quick announcement.
 I think this was shared in another channel, but the **Merge Calls** will now be on the same week as the **Eth2 Calls** on **Thursday** at the same time we're going to be doing a three week break rather than two-week break uh this is to try to help with some of the folks that are up pretty late for **Eth2 Call** and the **Merge Call** to kind of stack them together, so we’ll do Merge than immediately enter **Eth2 Calls**. Each two calls usually aren't very long usually like 30 or 45 minutes depending on what's going on there shouldn't be too bad so we're gonna try that out.


 **Tim Beiko**

 Thanks for the update any Clients have anything to add. Okay that's Oh Trent you had the


 **Danny**

 I just want to say a huge shout out to Proto 


 **Tim Beiko**

 Yes


 **Danny**

 Proto like incepted this Rayonism idea and like did a lot of work if you were involved in that that **Proto** has been out there at night making this thing happen, I mean same to all the engineers but thanks, **Proto**


 ## **1559 UI Call Announcement**  [57:32](https://www.youtube.com/watch?v=H_T2nNrTuWQ&t=3452s)


 **Tim Beiko**

 Sweet yeah Trent, you had you wanted to talk about the **1559 UI Call**.


 **Trenton Van Epps**

 Yeah Thanks Tim. I know you mentioned it earlier but I can just go over it again and reiterate what you already said which is similar to the London readiness call we had a week or so ago we're going to be doing something similar but focused on people that work on wallets and interfaces this would be like **MetaMask, Argent, Rainbow, Status**, things like that so if anybody's listening to the call and you work on a wallet please reach out we're going to do two things which is put together a cheat sheet of basically what you need to know and hopefully keep it updated as things become more solidified and to solicit resources that Dev's could look to and then there will be a call I think about in a week two weeks from now we don't have a time yet but we'll try to pick a slot that works for everybody that's interested in being involved with this we'll just go over what people have been thinking about so far with regards to how they're presenting these new transaction choices to users and hopefully get people on the same page with what the best practices are so yeah like I said please reach out and just let me know if you'd like to be added to that I'll be sending out an email probably early next week to figure out a time.


 **Tim Beiko**

 Great


 **Trenton Van Epps**

 That's it 


 ## **Core Dev Apprenticeship Program**  [59:03](https://www.youtube.com/watch?v=H_T2nNrTuWQ&t=3543s)
 
 
 **Tim Beiko**

 In the chat, there was one more comment so Piper has been working on an **All Core Dev Apprenticeship Program** to get folks who want to start working on Core Development for Ethereum to work on it over the summer and receive a stipend for that work there's a blog post that went out on the Ethereum blog yesterday so if you just go to **blog.Ethereum.org** it's the most recent post it's called **Core Dev Apprenticeship** asks if anyone listening is interested in that there's all the information in the post about how to apply and **Piper** can answer all of your questions about the program.


 **Tim Beiko**

 Cool, anything else anybody wanted to discuss or, yeah, give it a shout too.


 **James**

 I wanted to say one thing.


 **Tim Beiko**

 Go


 **James**

 That, so I've been slowly handing things over to Tim over the last couple of months for the **Hardfork Coordination Rule** role. I've done it for about a year almost two years It feels like, and I'll be moving into some other things this will probably this will be like my last call as that I'll be leaving the **EF** as well I don't know exactly what I'm going to do next but part of it's probably going to be **EIP** stuff cause I keep getting drawn into it and I like working with you guys so it has been a pleasure.


 **Martin Swende**

 It's been a pleasure having you


 **Tim Beiko**

 Yeah


 **Asz Stanczak**

 Thanks James


 **Tim Beiko**

 Thanks for all your work.


 **Rai**

 Thanks James


 **Tim Beiko**

 Yeah, and yes there's definitely more than enough work on the **EIP** side if you're not sure what to do.


 **James**

 I'm gonna I'm going to try and wait at least four weeks before jumping into things, but I can already tell that'd be I'm, I'm excited about stuff so.


 **Tim Beiko**

 So yeah, that’s a good call to take some time off.
 Cool, anything else anybody wanted to bring up?
 Okay well, thanks everybody.
 I can't believe we finished half an hour early given everything that was on the agenda. 
 So yeah, I appreciate it I will see you all in two weeks.


 **Multiple Participants**

  Thanks Everyone
  Thank you
  Cheers
  Thanks



 ## Date and Time for the next meeting 

 **May 28th, 2021, 14:00 UTC**


 ## Attendees

 - **TIM BIEKO**
 - **TRENTON VAN EPPS**
 - **POOJA RANJAN**
 - **JAMES HANCOCK**
 - **MARTIN SWENDE**
 - **SASAWEBUP**
 - **ANSGAR DIETRICHS**
 - **ALEX STOKES**
 - **TRENTON VAM EPPS**
 - **PRESTWICH**
 - **ASZ STANCZAK**
 - **KENNETH LUSTER**
 - **LIGHTCLIENT**
 - **JOCHEN**
 - **ARTEM VOVTNIKOV**
 - **ALEX B. (AXIC)**
 - **GARY SCHULTE**
 - **MAREK MORACZYNSKI**
 - **SAJIDA ZOUARHI**
 - **MICAH ZOLTU**
 - **DANKRAD FEIST**
 - **PAWEL BYLICA**
 - **KEVAUNDRAV WEDDERBUM**
 - **LUKASZ ROZMEJ**
 - **YUGA**
 - **PUAL D**
 - **RAI (RATAN SUR)**
 - **DUSAN\ALEX VIASOV**
 - **JOHN**
 - **DANNY**
 - **ALEX VIASOV**
 - **DUSAN**



 ## Links discussed in the call (zoom chat)
 -  **Ansgar Mempool write up:**   https://hackmd.io/@adietrichs/1559-transaction-sorting-part2
 -  https://gist.github.com/karalabe/1565e0bc1be6895ad85e2a0116367ba6
 -  https://gist.github.com/karalabe/1565e0bc1be6895ad85e2a0116367ba6#gistcomment-3740453
 -  https://github.com/ethereum/pm/issues/245#issuecomment-832122309
 -  https://github.com/ethereum/pm/issues/245#issuecomment-832122309
 -  https://blog.ethereum.org/2021/05/13/core-dev-apprenticeship/




