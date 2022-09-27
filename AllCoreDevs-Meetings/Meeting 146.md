# All Core Devs Meeting 146
### Meeting Date/Time: September 1, 2022, 14:00 UTC
### Meeting Duration: 30 minutes
### [Github Agenda](https://github.com/ethereum/pm/issues/609)
### [Video of the meeting](https://youtu.be/GizYbtINRUs)
### Moderator: Ansgar Dietrichs
### Notes: Alen (Santhosh)


## Intro [0.52](https://youtu.be/GizYbtINRUs?t=52)
**Ansgar Dietrichs**
* Okay. Hello, everyone. Welcome to the which number is it to the 146? All core dev. I'm filling in for Tim, just for this call. it's hopefully going to be a rather short one. yeah, so we don't really have much on the agenda for today. the first and main item is just general merge updates. I heard that we had a very successful shadow folk. recently, do we maybe have anyone on the call that I think Pari unfortunately was not able to make it, anyone on the call that can give a brief update on this? 

**Justin Florentine**
* Hey, this is Justin. I was talking to Pari about it. He did use the phrase 'a perfect merge'. So things went extremely well. We actually had an increase in proposals, after it due to some, some, I believe it was the Nimbus client that was actually behaving a little bit better post-merger than it was prior to merge. so super happy with that mainnet shawdow fork work. 12 was pretty happy and, the word perfection was in fact used and I know Pari and he does not throw that out lightly. 

**Ansgar Dietrichs**
* Right. Yeah. I heard that as well. that, I mean, could, could not come at a better time, physically that we have, our second to last, shadow fork be the first one that's like absolutely. Perfect. great. So, yeah, with that, do we have, any, any specific updates, any client teams? Is there anything, for this call? 

**Andrew**
* Andrew, see, I end up, yeah, I'd like to say that, we recently, there was another issue that recently surfaced in Erigon that we don't filter out, transactions with, invalid, signature in our transaction for, so we need to make another release to ensure that, we don't produce invalid blocks. That's what separate, like they fixed a separate issue ever produced producing by the blogs, but unfortunately there is another one, whereas with a relaxed, not stringent enough checks on transactions. 

**Ansgar Dietrichs**
* Okay. That's that's good to know. So for anyone listening, basically, be prepared to upgrade your nodes, and just to be explicit, like, because we have the Bellatrix folk coming up, but this, this basically the time he would be, you could do that at any point before the actual merchant said, right. 

**Andrew**
* So it's yeah. the, the time is before the merge on the execution layer of for Aragon updates. So if it's, it's kind of, because it's only the Barca and, affects, both production and, we don't have any, pow, mining on Aragon, so it will be only relevant for, building proof of stake blocks. 

**Ansgar Dietrichs**
* Okay. Yeah. That's that's good context. Okay. Thanks. Ben, I see you also can handup

**Ben**
* Sounds good. yeah, for those who are using teku as a consensus client, we put out a slightly broken release yesterday. we have today about two hours ago, made a new release 22.9.0, and we would strongly recommend anyone using teku to upgrade to 22.9.0 at your earliest convenience.  

**Ansgar Dietrichs**
* Right. Thanks for that as well. I assume we'll see a few of these kinds of small, last upgrades. So in general, if you're listening to this and even if your client will have mentioned to you, do pay attention, they can always be kind of last minute releases. okay. And, yes. 

**Lukaz Rozmej**
* So, well, Nether mind doesn't have any bugs. We will probably also minor releases.

**Ansgar Dietrichs**
* Sounds good and schedule have any expectation already when, when the profit will be. 

**Lukaz Rozmej**
* Could you repeat? 

**Ansgar Dietrichs**
* Yeah, I was just wondering if you, if you already have a rough idea of when people can expect that the release, 

**Lukaz Rozmej**
* So we will start a good early next week. We'll be probably on Tuesday. Sounds good, But if you're running one thing, zeros. 

**Ansgar Dietrichs**
* Okay. Quick context. Gary. 

**Gary Schulte**
* Yeah. similarly, basically Besu it was going to be doing a release next week on Wednesday, the seventh, 20.7.2, there's. We don't have a critical bug that we're trying to fix, but it's just, you know, logging improvements. some additional, features not necessarily features just, fixes, that will be, not critical, but recommended for, the merge as that I believe the seventh is post Bellatrix, but, it shouldn't be available on the seventh and we will be recommending that release for the merge. 

**Ansgar Dietrichs**
* Sounds good. Sounds like a lot of, visibly small, optional, intro leases. I mean, I think this is, that's a great place to be in just this smallest minute, improvements. Do we have any, any other, merge-related items for today? Okay. 

**Mikhail Kalinin**
* I mean, Yeah, I guess we have like, yeah, one another small one. So we do want to give an update on the optimistic seen tests. 

**Hsiao-Wei Wang**
* Ah, yes. So, we have a consensus, spec text factor up dates here. Let me put the link here in the chat. So I'm Kyle and I are working on the optimistic test vectors. And so we, I attached the, the simple test vector TAROS in this PR. So, we are looking for more inputs from the consensus layer, a client, developers on the new test vector, format, especially. And so in this goal that, it would be great if we have at this one or maybe better two plantings to, implement the basic test runner and provide some feedback, for us before we merged this PR and make, no more release, for the whole test suit. So yeah, PR here, a request for feedback thinking. 

**Ansgar Dietrichs**
* Okay. great. maybe just because, I see some comments in the chat, I think, what else is still predicting more or less the same, same time for the merge, Thursday at around 4:00 AM, UTC of course, a little bit of variance depending on the country, hash rates. So actually that would be just for context, if you ask before our next, all core dev call. So, I think there's a very decent chance that this one is the last step, pretty much, a all coredev call, but you, who knows if, if the, if the hash rate, ends up dropping a little bit before the merge, we might, we might, just barely, slipped to after, after the call. And also, I think there are a few other kind of, merge, prediction websites out there they'd have slightly different estimates instead. Do we any chance to know specificlly. I mean, of course there's some uncertainty, but, I think Battelle has been so far kind of the most precise. so is that kind of the main place for people to, to look to, to be, not anything there? Mo Maria? 

**Mario Havel**
* Yeah, so, basically, but no, calculates the prediction with a bigger time span of data. currently like two weeks and other websites are using just the latest blog difficulty or the latest Ash rate. So a, it is up in past week or like five days. So, if you count just with this, the merge would be like they earlier than process says. but like statistically we'll probably get bit lower, so we'll know is more conservative in the prediction. but on the bordel website, you can also see, the last chart, we, where it's a completed purely on the daily hash rate. and you can see the, how much restrict is needed to achieve that on a given date. So if the history is stays at, as a now around 900, terahash, we will hit it on September 14, roughly they earlier than planned. yeah. 

**Ansgar Dietrichs**
* Okay. I think that's very helpful context specifically just for, for people who are not super familiar with all the technical details and who are just physically following along. Okay. Casually, I think it's a little confusing too, to physically have these different estimates out there, but I think, that's really helpful context. I mean, of course, you know, there's a state slightly like a somewhat statistical process. So we, we don't, we can't predict the precise moment of the merchant till we are closer. but, you know, I think all of these give a good kind of bend, for, for, for when, when the merge roughly happened. And also of course, that might drop back down a little bit before the much, so close like a day or so, like  as well. So I, anything in that range, for anyone listening, you should be prepared, for, for the merge to happen. But I think, Thursday, two weeks is still kind of, the most likely date. okay. with that, I think that's for much updates that we do with any, any, remaining, major updates, otherwise there's the, the other, point as well. 

**Trent**
* We will be having the final, merge community call on the 9th Sept. So, obviously you want to prepare for Bellatrix before that, but, there will be one more session. 

**Ansgar Dietrichs**
* That's good to hear. Do we, someone just, remind the listeners when exactly Bellatrix is expected to happen. 

**Trent**
* I believe it's September 6th, but I will double check on that. 

**Ansgar Dietrichs**
* Yeah. I think that, that seems what I remember as well. And of course I was Bellatrix. This, not the, not the proof work and predictability of the timing. So, yeah, I think, I think it is. So again, for anyone listening, you know, you should really have your setup ready by then because that's when the consensus layer forks. Okay. I might, I see you have your hand raised. 

**Ahmad Bitar**
* Yeah. So just need to encourage people to upgrade their clients because only right now, 53% of clients are merchant ready. So we need more people to update their clients, be ready for them. 

**Micah Zoltu**
* Does that 50% to 53% of staker or 53% of users are not operators. 

**Ahmad Bitar**
* I'm getting my data from ethernode.org, not entirely sure. I'm pretty sure it's just node operators. 

**Ansgar Dietrichs**
* Okay. Yeah. That's, that's useful context, of course. for non-statin auto operators, there's always less incentive to make sure that they're fully, fully set up. So we, so we might expect that this will not quite reach a hundred percent before the merger, but if you are not a blatant, you want to continue following the chain. then, you of course, have dropped bit. So please do that. Any other much updates? I mean, it sounds like we're just not right on track. quite exciting. well then, let's just briefly go to the other general point, just other, do we, do we have anything, anything non-matriculated, we can become discuss, right now. Okay. Sounds like everyone is focused on the image as it should be. great. So then with that, this might be one of the shortest allcore dev calls in history. happy coincidence because, you know, I couldn't couldn't really break anything. It's a great like idea of anything in the, And they'll talk about it. 

**Micah Zoltu**
* I feel like we've been putting off planning Shanghai forever. Like if we've got everybody here for an hour, is there a reason we're not starting to plan Shanghai? 

**Ansgar Dietrichs**
* Well let me just ask what's what's the, do people have opinions and whether we should use the time today to talk about Shanghai or I'll leave it for a later day? 

**Trent**
* It In theory is, and I said, yeah, but I don't think people are prepared to do that today. 

**Lukasz**
* Yes. Very little participation. People are also competing. 

**Ansgar Dietrichs**
* Okay. Yeah. Then, I think, I mean, I can, I can just very briefly say because I've been somewhat involved with the kind of EIP-4844 for effort. So yeah, again, I don't think it's the best time to actually discuss the details of this. People are still working on this. so this is, you know, this, first kind of version of this, people are still trying to get it ready so that it can be considered an included, for Shanghai. So this is a very active effort. And if any, any of the, of the client teams, happened to have some return now that visibly everything is in place. And if they like bot waiting for the merge, you know, it's always there and we're as happy for, for anyone to reach out and terms of gives them early feedback before we kind of open it wide up after the merge when everyone is ready. And, but, but yeah, I don't think today's the day to really dive into this. And, I think turned out to just, linked, some, some, some treats for the team about 10 of us, which is another one of these really exciting, updates that are scheduled for, for Shanghai. So, but anyone interested to have a look I'm not scheduled for Shanghai because we still haven't had a meeting to schedule. This is why you need someone with experience. No, nobody. Yeah, exactly. So this is just a considered for tonight, but this is what I should have said. it's, yeah. Considered for inclusion all right. Now. and that is a very important distinction, so yes. Thank you, Micah. but yeah, with that, on last chance, but it sounds like we're a bit, close, so thanks everyone for coming. have a good day, have a good time before the merge. 
* Hopefully relatively relaxed, nothing super urgent coming up any more. That that would not be a great time, but, see y'all soon and let's, you know, most of this chain. 
* Bye bye. Bye. 

# Attendees

* Zuerlein
* Parithosh Jayanthi
* Micah Zoltu
* Afri
* Damien
* Gary Schulte
* Roberto Bayardo
* Terence(Prysmatic Labs)
* Ramon Pitter
* Ben Edgington
* jgold
* Adrian Sutton
* Ansgar Dietrichs
* Justin Florentine
* Greg
* Chris Hager
* Mikhail Kalinin
* Trent
* Sean Anderson
* Danny Ryan
* Sam CM
* Leo Arias
* Stokes
* Sam
* Stefan Bratanov
* Lightclient
* Pooja Ranjan
* Viktor
* Helen George
* Matt Nelson
* Marcin Sobczak
* George Kadianakis
* Dankrad Feist
* Paweł Bylica
* Ashraf
* Péter Szilágyi
* Daniel Lehrner
* Mario Vega
* Barnabé Monnot
* Potuz
* Fabio Di Fabio
* Felix
* Jamie Lokier
* Sam Feintech
* Saulius Grigaitis
* SasaWebUp
* Ahmad Bitar
* Ruben
* Alexey
* Marek Moraczyński
* DanielC
* łukasz Rozmej
* Soubhik Deb
* Protolambda

