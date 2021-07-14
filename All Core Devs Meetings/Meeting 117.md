

# All Core Devs #117


### Meeting Date/Time: Friday, July 9th, 2021 14:00 UTC
### Meeting Duration:  90 minutes
### [GitHub Agenda](https://github.com/ethereum/pm/issues/342)
### [Audio/Video of the meeting](https://youtu.be/OLCumSVoc0o?t=467)
### Moderator: Tim Beiko
### Notes: Jared Doro

-----------------------------

# **Summary:**

- London fork is on Goerli 

- client teams describe how they handle transaction pool sorting and price bump for transaction removal 

- [Merge Checklist is out](https://github.com/ethereum/pm/blob/master/Merge/mainnet-readiness.md)

- More discussion is needed on the topic of fork scheduling.

- More discussion is needed on the topic of post-merge update scheduling and coordination.

-----------------------------
starts at 7:47 
stream audio muted till 9:00

# 1. London Updates

**Marius** 

Everything went fine, we saw the base fee react as we thought and also the transaction pools being relatively salable
So I think there is no big issues there. 

**Karim** 

Yeah same for me it was fine

**Peter** 

Yeah sure one of the weaknesses I found after the fork is that a few hundred transactions were queued up and transactions were executing but there was about 700 that were so to say executable but miners kept rejecting it.

We looked into the whole thing and essentially what was happening is that geth has this miner configuration parameter called the gasprice you just set the price that you are willing to accept. 

Which every single miner on rinkeby net had set it to one gigabyte and this flag is also interpreted as post London as the minimum tip the miner is willing to accept transactions with.

So the moment we switched over to London it became instead of the one gigabyte transaction, we want the one gigabyte tip plus whatever the base fee is, now of course since post London the base fee needs to be jumped up it meant that none of the transactions were actually executable anymore.

But they were nonetheless still in the transaction pool and they were just lingering there so essentially I just reduced one of the miners gas Price limit by 20 wei and that solved the whole thing and essentially the reason there were several hundred transactions was because I think 400 of them was the faucet and probably a few more accounts that happened to block up the queue.

 I mean the first transaction was not executable so obviously everything else was blocking up the queue. 

So that is kind of what we saw, on mainnet I don't think this is going to be relevant because in general transactions don't really reach the limits that miners set rather there are always more expensive transactions, the pool is always filled and more expensive transactions always push out the cheaper ones.

 So I don't think this could happen on mainnet and even if it would happen it would sort itself out because more expensive transactions would stress the cheaper ones, so even if it happens temporarily, but I don't think it would happen.

I haven't investigated a possible fix for this specifically because I don't think it is an issue it's more like this weird transition. 
I mean it happens once in the lifetime of the chain.
It's not that big of a deal, but probably before London we will investigate it closer at that time just to make sure that it is fine.

**Tim**

Got it Thanks, Um sorry this was my bad I had us muted on the steam for the goerli  part
so just a quick recap. 

When we have the London fork on goerli  the geth and besu team ran a spammer and everything was fine there was a small issue found on rinkeby which peter was just explaining with regards to the minimum price that a miner will accept for a transaction and that was just fixed by changing the miner config. Sorry for the people who missed the first part of that.

With the three test nets forked successfully we also set a block for mainnet this week, we did this async but just to document it and to make it clear the block is 12965000 on mainnet.

I think most clients have already either merged it or have a pr open for it, it should happen on August 4th roughly, and we will obviously know better the exact date when we get closer to the actual fork time.

I think the last kind of open issue with regards to London was what do we do with regards to the effective gasprice field in the transactions receipts, LightClient I saw you opened a issue for that in the eth1-specs which I saw you kind of updated yesterday.
Do you want to give a quick update of what the issue is and what you kind of figured out yesterday.

**LightClient**

I made a mistake when I was talking to the open ethereal team they were asking about the spec and wondering if this effective gasprice value should be returned pre London transactions in the receipt and I just quickly looked at the geth code and I completely misread it.

I was thinking that geth also did not return the effective gas price and it seemed like there was an issue with the clients and the latest spec.

I saw it again yesterday and realized that I had made a mistake, but that still leaves the question do clients prefer to follow the spec?

Because open ethereum seemed to signal that they rather not provide effective gas price before London for transactions. 

I am like minor-ly against that but that the issue is about so if anyone has thought or preferences I am curious to hear.

**Peter**

I have a counter worry I think the spec also states that after London the gasprice field of the transaction should be dropped at least for 1559 transactions. 

Currently what geth does is that after a transaction is mined the gas price field in the transaction it is set to the actual gasprice state so if you pick up any past transaction the gas price will be the amount that the user paid for it

So essentially its exactly the same as the effective gasprice sepc but part of the transaction, and I don't think its a good idea to drop this field just now because that is what everybody is relying on.

So we could say that the field is deprecated and maybe drop it in the future, but I think it is a bit of a bold move to just nuke it out immediately when the fork hits and switch it over to a different location.

**LightClient**

So should we have both, gasprice be the effective gasprice thats in the transaction object and effective gasprice be an element of the receipt?

**Peter**

So that is what geth does

**Tim**

So what do other teams do right now?

**Dusan**

I am not sure I originally implemented it to transaction object not to contain the gasprice for the 1559 transaction, but I am aware that this discussion was mentioned a few weeks ago, and I am not really sure about the current implementation I need to check

**Rai**

Yeah, I believe we have the effective gasprice in the recipt and no gasprice in the transaction object I can check though 

**Marek**

I think we do the same at open ethereum on the other hand it think it is a good idea to return effective gasprice so maybe we will do that

**Tim**

So is there an argument against basically doing both?

And if we go ahead with both it seems like it's a pretty simple thing to add basically just keep the gasprice in the transactions and keep the effective gasprice in the receipt

like is there and reason against doing both those things?

**Peter**

The only catch with keeping gasprice in the transaction is that before a 1559 transaction is executed you cannot calculate the gasprice because it depends on the base fee so currently geth sets it to the fee cap meaning that that is the maximum you would pay.

And once the transaction is mined we could update this to the amount you actually paid and to kind of follow that user experience wise this is what kind of makes sense, but it is important to realize that there is this work

**Tim**

yeah, Its not just setting the value

**Rai**

So it seems that we always want to overload these fields why don't we just want to not have the gasprice for the 1559 transaction and if you are curious about the effective gasprice just ask for the receipt?

**Peter**

Because all the infrastructure that is in place currently in ethereum has only a single place to retrieve the gasprice from and that is the transaction object called gasprice so it means post fork every single software that ever touches an ethereum transaction needs to be changed and is violent in my opinion

so thats why we are suggesting that we keep it around at leas for a deprecation thing and remove it in I don't know in a few months.

**Tim**

I guess the other kind of concern here is this is like a non consensus change and if we set a fork block for mainnet we probably want have releases from clients out ideally next week that are London compatible so that people can start upgrading across the ecosystem because there is going to be roughly three weeks

I guess how important do people feel that this is harmonized before the official London releases are out, do we want to agree to kind of do both have the effective gasprice in pre London transactions and also have the gasprice field return the effective gasprice?

I guess a better question is like how much delay does it add to client teams to do both is it like a day that is needed or does it push things back by a week and if it pushes things back by a week I think I would have a weak preference for us to not necessarily harmonizing this before the fork 
and maybe clients will have to document better how they handle those two things

**Marek**

For it is like a day to fix it so

**Tim**

Ok

**Rai**

I think it would be good to converge and do those things and it wouldn't be difficult to do, but I also kind of like peter's suggestion of potentially signaling that this will go away just because of the overloading semantics of the gasprice in the transaction object

**Tim** 

I assume that that is something that we can just add as a comment in the JSON RPC spec

**LightClient**

Yeah I will update the spec right now I think it is really good to try and converge if at all possible before the fork. 

I think thats something that would be really good just to keep in mind as we go forward the easier it is to just swap clients in and out I think is better for the ecosystem
The more specific behavior the RPC's have I think you get into a dangerous place

**Peter**

One other question is and this is something that I don't have much experience with is how do we expect that someone is curious about the gasprice paid without caring about other fields in the receipt?

So essentially the effective gasprice can be calculated without the receipt so every other field is completely useless because I only need the fee cap the priority fee and the base fee and I can just calculate it, now if you put it in the receipt you just need to dig up the receipt and send it to the user even if they are only interested in what the final gas price was.

The question is is this a problem or not?

**Tim**

I feel like we discussed on discord why it ended up in the receipt but I forget why

**Peter**

I mean theoretically it is a better place I can accept that, but I am talking about the practicalities

**LightClient**

I don't think I quite followed what your argument was? Like are you saying people might only want the effective gasprice so why download the whole receipt or are you saying the inverse? 

**Peter**

So essentially what I am saying is if I only care about the gasprice I still have to dig up the receipt from the database just to calculate the gasprice which need many of the receipt fields, but the question is does this often happen that someone would be interesting in the gasprice and not the status of the execution or does it ever happen that is something I cannot respond to

**LightClient**

That is a good question I also don't know 

**Tim**

I assume its like a common use case imagine you go on ether scan its like something you want to see in your transaction, but then they also show you everything else right
or like I don't know metamask showing you the amount you paid Im looking right now at metamask if you click one of your transactions you see the gasprice that you have paid 

**Peter**

I guess I mean such wallet will show you if a transaction failed or not and there you kind of need the receipt so

**Tim**

Okay yeah if you need the receipt to show whether a transaction has failed it feels like there is not a lot of use cases where you would want to know the price paid and not the success status right?

**Peter**

Right, yeah that is what I was also thinking about now 

**Tim**

And like you said right you can actually recalculate the effective gasprice form the information in the transaction object itself, so I think if a wallet wanted to do that optimization they could also calculate it right?

**Peter**

Yeah of course it was just a question, I can also see that just fine because if you care about the effective gasprice you also care about if the transaction succeeded of failed

**Tim**

So I guess we can probably go with that obviously if someone feels very strongly in the future they can make an EIP to change it and if we announce that this field is being deprecated before the next hard fork or something somebody can also step up and say don't depreciate this it breaks my app for these specific reasons, does that make sense?

**Peter**

Yup

**Tim**

To summarize then we will go with having the gasprice field in 1559 style transactions which will return the effective gasprice.

We also agree to have the effective gasprice in pre EIP 1559 blocks and LightClient said he will add a deprecation notice in the 1559 transaction format in the JSON RPC spec so that people are aware that this is happening

**Rai**

And also that the gasprice field should return the fee cap if the transaction unmined.

**Tim** 

Yes that is right

**Peter**

So just to clarify that even after this field is deprecated and removed in the future, this mean that it is removed for 1559 transactions
But for legacy transactions we are keeping it forever so to saying

**Tim**

Yeah that is right

I guess kind of the next point on the agenda was the client releases for London do the team feel like they can get a release out like early next week given those changes is that still realistic?

**Rai**

We already released with the mainnet block

**Tim**

The reasons I am asking is if there is an ethereum.org blog post saying download this release for Besu you probably want the one with that transaction fix right?

**Rai**

Okay cool, Yeah

**Tim** 

But is that realistic to get early next week?

**Peter**

Yeah

**Rai**

We can do an update release

**Tim**

Okay if any client team feels they cannot have a release early next week now is kind of the time to speak up

**Dusan**

Is it Monday early next week or Tuesday?

**Tim**

Monday or Tuesday ideally and the reason I am asking is if its Monday or Tuesday we can have the blog post go out like Wednesday Europe
and thats basically 3 weeks before the upgrade so it feels like its enough time but If the releases come out Thursday or Friday then the blog post probably won't go up until the week after that
and that only 2 weeks before the upgrade 

So Monday or Tuesday would be ideal

**Dusan**

Okay I think it is realistic for open ethereal although we still don't have the history implemented completely but I think it will be

**Zsfelfoldi**

Yeah but the fee history is not consensus, so I guess that is okay

**Peter**

Oh yeah but it's the same question as the previous one, ideally you want all clients to behave the same otherwise you cannot just swap them out they do weird shit
It's not consensus critical but it would be super nice to have them work the same way

**Tim**

Cool
Okay it seems like there is no major adjustions 

If teams can have a release out early next week with those changes then I think we will be all set for London

One related thing I want to make sure it is said on the call so with London happening with 1559 in it the miners will have to target a block size thats twice as big as what they are current targeting pre London

so if say they are targeting 15 million they are going to have to bump that target to 30 million

The three mainnet compatible clients all have a JSON RPC call to do that I've linked them all in the agenda for the called
but geth has added minerSetGasLimit, open ethereum has parodies_setGasYeldTarget, and besu has minerChangeTargetGasLimit

so if you are running a miner it's really important to call that and double the gas target you are aiming for otherwise after the fork you are going to start reducing the blocks and just including less transactions in them

The links are in the agenda I think geth's doesn't have a doc link yet but its merged in the code

The last thing this came up Trent you maybe want to talk about it as you were reaching out to the ecosystem about London readiness there is a bunch of questions that came up about
some non consensus behavior for clients and that it would be good to clarify how different clients handle stuff, do you want to give some quick background on that and ask the questions that you've been asked?

**Trent**

Yeah just a short summary of it I think the two main things were how the different clients handle transaction pool sorting and the other one escapes me ... Yeah the percent bump that is required to replace a transaction

If the clients can just go over what they've done for each of those then we can have a record of it and to see what the differences are

**Peter** 

from geth's perspective our attempt was to keep the existing behavior mainly that the transactions in the pool are sorted by the gas tip so the amount of money that is going to the miner because that is the important things
so if you start including the transactions the miner isn't really interested in how much is burnt rather how much do they get and as far as I know the replacement logic is similar to previous you need to bump by 10%

I mean the stuff that the miner gets needs to be bumped by 10% to get a replacement

**Rai**

I think we do the same

**Marek**

We are doing the same too

**Ansgar**

Just to double check is it really only the tip? Because I think we the last version of the code I saw required a bump of both the tip and the fee cap so just wanted to confirm with whoever in geth has seen the latest implementation there?

**Rai**

So just off our end I think we check against the current base fee so its essentially a 10% bump in the expected effective gasprice

**Ansgar**

I see that makes sense, but yeah the point is if the fee cap is below the base fee a bump in the tip is basically free because you don't end up actually paying that 
and so a naive bump of just the tip has some unexplored and undesirable behaviors that need replacement.

I would recommend wallets and everything usually just have just a 10% bump in the both the fee cap and tip where it makes sense but like at least there you are on the safe side that you will achieve replacement

**Dusan**

Open ether does sorting and replacement based on the effective gasprice and if you want to replace a transaction we don't care if you bump the maxFeePerGas or maxPriorityFeePerGas you just need the calculated effective gasprice basis ed on that increased values to be bumped by 12% so again basied on the effective gasprice

**Ansgar**

Ok but a question there transactions can only be replaced if they are pending in the pool transactions above the base fee will always be included immediately unless we have extreme congestion and all blocks are 2x 
but like usually we only talk about transactions that are not included anyway so all of them will have an effective tip of 0

So I am just curious how do you bump an effective tip of 0?

**Peter**

I don't think you mentioned the effective tip you said the effective gasprice and the stuff that gets paid at the end

**Tim**

Sorry when you say tip you also mean the effective tip right? Like what's paid? You kind of broke up there Peter

**Peter**

Never mind I was jut trying to clarify but its just getting more complicated, and more lost in the details

**Tim**

Yeah I guess it seems like at a high level every client team sorts the transaction pool by basically the effective tip or what goes to the miner and requires a bump of the effective tip by at least 10% and 12% for open ethereum

**Peter**

So I am not sure who said it but I kinda got a bit unsure about it because maybe geth also does the effective gasprice
___ are you here by any Chance

**zsfelfoldi**

Yes I am here

**Peter**

Do you remember how the implementation actually does it take into account only the gas paid to the miner or the global effective gas state when we try to figure out if something is under priced or not

**zsf**

Oh I don't quite understand the question so the eviction rule yeah we have this minimum for the effective tip like this global minimum and well we have the priority ques but what are you asking about right now

**Peter**

When you send a transaction that already exists I mean the account balance already exists then previously we had a 10% bump you need to bump up the fee to

**zsf**

Yeah oh the bump rule 

so right now the replacement rule is you have to increase the parameters specified in the transaction by 10% so like the maxFeePerGas and maxPriorityFeePerGas parameters both have to increase at least 10% than you can replace a transaction
so the current effective tip doesn't matter here I think

**Ansgar**

Yeah so just to say I think at least that piece of the transaction pool might just be the unchanged version that I implemented and if that is the case then indeed geth requires the 10% bump in both fields

**zsfelfoldi**

Yes

**Tim**

Okay Trent does that help?

**Trent**

Yeah I think that was good to go over

**Tim**

Great its also worth noting that erigon is working on a different transaction pool design I think __ has shared the write up on it before I am not sure how final it is?
Artem do you have comments on that I am not sure if you have been involved in that at all

**Artem**

Yeah I haven't been very involved in it we are still writing it I think we just finished the design of it

I think we will have it ready by the London mainnet roll out but yeah I guess its better to ask ____

**Tim**

I just shared the link to the [wiki page](https://github.com/ledgerwatch/erigon/wiki/Transaction-Pool-Design#changes-for-eip-1559) in the chat here if anyone wants to have a look
Ans gar I see you have your hand up

**Ansgar**

Yeah I just wanted to make one last comment on the transaction pool topic as a whole 
I just want to briefly point out that I think right now the individual clients do have slightly sorting logic basically I don't that is a problem but just like before 1559 because it was one dimensional like basically everyone had the same rule and so the idea was identical

I mean up to the size of the transaction pool and now this will no longer be the case I think it wont be an issue 

because that just means that slightly different transactions will be retained by in slightly different clients that actually kinda increases the global size of the pool even but it is something to keep in mind and potentially watch for to see if it creates any issues going forward
I don't expect it to

**Tim**

Yea that is a good point like we will be able to see on mainnet if some client that just has less transactions or is less efficient at relaying them

Cool That is all we had for London unless anybody else had anything they wanted to bring up

**Peter**

I just want to mention that I did check the code just now and whether this is correct or not is up for debate but geth currently requires either the gas fee or the tip to go up 10%

**zsfelfoldi**

It should require both to be bumped I am pretty sure about that is the correct behavior

**Peter**

Yes that is what I am saying that it doesn't do the correct behavior

**zsfelfoldi**

So we incorrect code in master

**Peter**

Yes I am posting a [link](https://github.com/ethereum/go-ethereum/blob/master/core/tx_list.go#L299), and we can continue just for reference since I mentioned it

**Ansgar**

It looks like I am looking at right now in master it looks like only the comment is incorrect not the code itself but yeah it can be done offline

**Peter**

Only because it rejects it if

**Rai**

Let's do the geth paired programming later

**Tim**

Yeah, so I guess geth team I should probably just triple check that that is correct and yeah next all core devs we can have the geth paired programming session

anything else on London?

# Merge Checklist

Okay, so I guess next up Mikhail put up a merge readiness check list so basically trying to go over all the stuff that needs to happen on both the consensus and execution side so that we have a high level list of things to do

I think it probably makes sense for you Mikhail to share it and go over the high level details of it its something that is going to be really helpful in then figuring out when we can think we can do the merge

What do we think are the biggest open issues in that list that are going to require more attention and also is anything missing from this list that is important

**Mikhail**

Thanks, Tim

Before we go briefly through this list I just wanted to thank Danny for compiling it

Its not final obviously because there is an ongoing rnd and implementation work, so we will keep this list updated and as you mentioned it might not be whole 

Just want to encourage everyone here to take your time to go through this list and find anything that is missed in this list and you think that is important you can reach out and let's discuss

Let's go briefly through this list and get back to discussion

**Danny**

Also just want to mention it's the granularity of a publicly shared list obviously there is a lot of detail we could drill into but thats kind of not the purpose here

**Mikhail**

Yeah Thanks Danny Okay, so I can share my screen actually

Okay so the first section here is the consensus layer so consensus layer specs are feature complete and the next step is to rebase the spec with London and Altair also there will be some insignificant fixes on the other parts of the spec which is networking and API stuff 

SO the next part is the execution layer what do we have on the execution layer specs right now is the high level design doc that has been published a while ago and the rayonism spec published after it but that was a long time ago a couple of months

The next step and what is the priority now is to actually write a specification for the execution layer which will consist from a couple of EIPs on the consensus side on the core protocol side and also the specifications for the state and block sync

Also there is the change in the JSON RPC this should not be significant a couple of endpoints will be deprecated that are related to the mining process and probably one or two will be added like getMostRecentFinalizedBlock

The consensus API is also a major thing to figure out we have the JSON RPC specifications and implementations of it so it doesn't seem like it is perfect for production

This is what has been discussed recently and I think we should reiterate on it and come to a conclusion how do we want to implement at consensus API what will be the underlying communication protocol and so forth

Yeah there is a lot of testing items here I don't want to go into the weeds of testing yet because we have some other more important things to do like the consensus API and execution layer stacks yeah there are test nets and also there is an RnD section so not all RnD questions are answered 

as for today we have some kind of analysis to do with the transition process, and we need to do the treat analysis the attacks and attacks near the point of merge and analyze new attack vectors that can happen after the merge like this resource exhaustion attacks

There is the execution layer proof of custody here its listed here but it's likely to not be part of the minimal merge but yeah it's here because of its importance and its really to introduce it later on because it may affect some decision made on down in the execution layer services and thats why its here

So we need to figure out discovery to make sure if its anything major to do on that side and the historic state sync and sync during transition period is also a tricky one 

So thats all actually for the list

Thanks

**Tim**
 
Thanks for sharing it feels like at a very high level the next step is probably for the different client teams to look at this going over each of those check boxes and figure out what actually needs to be done

Obviously we have some stuff to finish with London and as that dies down we will kind of naturally transition there.

**Peter**

There is one point that is fairly new in the EVM execution it was reusing the difficulty field for the Random values and I would like to request either rethinking that or exploring it a bit more because the problem is

The idea behind that point is that post merge the difficulty will not be relevant it can be repurposed to feed the 32 byte random and the reason why this was field was chosen because EVM already has a difficulty opcode so you could just piggyback 
on that opcode and access the randomness oracle and in my opinion this is not the best idea because it doesn't cost us anything to add a new opcode called random, so I don't think we need to piggyback off existing opcodes

The other bigger problem that I can see is that currently the difficulty is a small number the in the ethereal world most of the fields can be 256 bits and the difficulty is insignificantly small compared to that and essentially you can keep adding it up to get to the total difficulty and every client does it Now if we repurposed the difficulty fields to be a random number and all of a sudden we will use all 32 bits and in the second block we will overflow with the total difficulty, the 256 bits 
now in theory its possible to fix clients so that this won't be a problem but in practice the notion of total difficulty is really deeply engrained all over the place and it just feels like playing with fire to change the baising vareint that all of a sudden after the fork this field will become very large 

so thats why my suggestion would be too maybe to pick ___ and add a new random opcode unless there is a very strong reason not to do it I guess

**Danny**

So there is another reason that that was selected is that although it's been bemoaned as a terrible practice difficulty is used almost only in the EVM today for randomness and so that was another consideration on that decision I am happy to rethink this decision I am not married to that

I would worry we would have to select something for that value to return

putting 1 in there or something might actually be dangerous because it could hide fork choice bugs because then you end up with some weird longest chain rule that maybe works some of the time, and so we would need to be careful

If we are worried that total difficulty is going to haunt us we need to make sure that it doesn't accidentally give you the correct value some of the time and trigger potential fork choice bugs so maybe 0 is a more perfect value but again I am not married to replacing that

There is another consideration if you do start putting in 0 or 1 it's going to break some applications that are using the bad randomness today

**Peter**

Yeah, just a quick reaction to that I am fine with going into this direction my request is that we investigate to make sure that we cover all the side effects

**Danny**

Yeah, agreed maybe we should do a deeper investigation of how clients are and will be using this in the future before we make a firm decision here

**Tim**

Thanks I see Mikhail and ALex you both have your hands up I am not sure who was first

**Mikhail**

Alex was first

**Alex**

Yeah, I just wanted to mention for what it is worth in solidity the difficulty field is considered a 256 bit number so it wont be truncated whether that is good or bad that is a question
but at least whoever is using it within solidity and in line assembly they would get a compleat value for the difficulty

**Tim**

Got it thanks 

**Mikhail**

I think that the fact that it is not truncated is good its as expected 

I do understand what Peters consideration is and I have a question here we can use the mix hash instead of the difficulty field, but then we will have to change the EVM context for the blocks that are produced by the POS chain and switch and jump between these two EVM contexts between the execution of POW blocks and POS blocks and if this path is less buggy and less controversial than reusing the difficulty field, so I think we can probably go this way

**Peter**

Yes, so I guess it has implications in both ways

So either way I don't think there is anything more to discuss except there is this quirky thing with this idea, and we will obviously find a good enough solution just people need to be aware that its not a thing that you can solve in a half an hour coding session

**Mikhail**

Right and yeah this Ransdom or random thing is going to get put into an EIP so it will definitely will be discussed with a lot of care 

**Tim**

Cool were there any other comments on the list in general

We have a merge call next week, so we can probably dive into more detail in some of those items on that call as well

**Peter**

I can add something a bit unrelated but touching so for the past few months we have been working in the background with super non priority on synchronization stuff for post merge and one of the things we kind of realize is that it is super annoying to implement a thing for eth 65 and below
eth 66 introduces request ____ which makes things cleaner and its just a pain in the ass to implement them both for the new request ___ models and the old non-request ______ models so as promised last year October geth will be dropping 65 after London ships so that we can focus on the merge work

Its just a heads up 

**Tim**

Yeah thanks for sharing that is good to know

**Danny**

Does that dropping get released in the London fork or do you mean you are going to do it sometime soon after the London fork?

**Peter**

No so the whole point was to wait until London is stable, so we know that we won't need any hot fixes or something like that, and we will only drop it then and this way we can actually maximize the lifespan of 65 
because most people will still just run the London fork release and not upgrade

**Danny**

Got it

**Tim**

Cool any other comments on the list?


**Mikhail**

I have a question what would be the best next step for us to do? 

in what is in mind is to write the EIP drafts or spec drafts and share them and discuss or should we do anything else before this

**Danny**

That's my intuition because also to do the next wave of prototyping I think we need to more clearly document a lot of the things even if they're not final and so at least what we need to focus on is specifications and the basis of testing those, so we can 
continue to talk about them and build more prototypes 

**Tim**

1:02:30
Also based on Alex's comment in the chat there is for each of these items on the list there's has been a bunch of discussions maybe adding some links I am not sure if that document is the right place but like how can we get people caught up on the latest thinking of these things right
And maybe thats actually writing the spec thats based on the latest thinking and kind of explain that with a good rational 

But I think that is one thing to kind of keep in mind like how do we bring people on the journey of understanding of how we got to the decision

**Danny**

I did add some PRs and links where relevant but I think we could probably flesh that out and keep adding them as we keep add things

but yeah the conversation has been on a lot of those merge calls and scattered throughout discord so writing everything down more and better will be a priority

**Tim**

Cool anything else on the list

# Fork Scheduling

The last thing so LightClient had a comment about having a higher level discussion about fork scheduling and others have reached out to me also about that in the past couple weeks even though we got the block for London three days ago

But basically we kind of agreed to after London we focus on the merge and potentially have shanghaied before the merge if we see that the merge is unlikely to happen by December or have Shanghai after the merge if the merge likely to happen by December

Yeah so it's obviously hard to know today what the odds are of the merge happening by December and if we want to maximize those odds we kind of have to start working on the merge and making progress on all of those things which was discussed

But I understand doing that obviously puts us in a spot where we might get to December and not necessarily have time to implement and test a whole fork with a bunch of new features in it

So thats where I am at in regard to that right now is I feel like we probably need to see a little more at least how the work around the merge continue or progresses before we can determine whether if we want to have a proper feature fork and consider stuff like 3540 and 3074 and whatnot and have those discussions so thats how I feel about things I don't know if others have thoughts or questions they want answered

**Peter**

My two sense is that we cannot focus on two completely different things so if we start doing work for the merge and then in the meantime well maybe we should do Shanghai then its just going to be weed of situations where nothing gets done

So my personal two sense would be to get the merge done and focus on features after and that does not mean we will get the merge done by December

**Tim**

I guess the worst cases scenario if that happens is we basically have Muir Glacier part 2 in December we can always have a single fork that just pushes back the difficulty bomb by however much long we need

**LightClient**

I think I was also curious like even higher level than specifically Shanghai and the merge with how as core developers do people feel about scheduling forks

We are pretty lucky that I am not the person who has to maintain the fork or maintain client and prepare for a fork, but it feels like if I was a core developer who did have to do that I would basically just have to assume oh 3-4 months ago we thought we would ship 1559 in the beginning of July and now it's the beginning of August so thats a lot of uncertainty for core developers, and I am curious if there is any desire to have a more fixed fork schedule

**Peter**

I think there were a few attempts to do fixed schedules and it always blew up really nastily, and we always just have fallen back to the its ready when its done or the its released when its ready state

**LightClient**

Is that something that you feel is going to be sustainable long term or is that something that you think is just how it is right now but its not really ideal

**Peter**

I mean the fact that you say the ETH2 merge will be done by December doesn't mean that it will be done so the question is you reach December and the merge is not done what do you do?

**LightClient**

I think the merge is kind of special thing because continuing on a proof of work chain we are spending lots of money for security and so its kind of lets do the merge as fast as we can
but beyond that once we go back to regularly scheduled feature forks is just doing things when they are ready a sustainable pattern for people?

**Tim**

Maybe one different way to frame that question "What is the target amount of forks roughly we want to have per year" I kind of feel that the difficulty bomb helped in a bit for London in that way that it helped reduce the scope and kind of keep us focused on shipping on the smallest set of things that would matter

Peter you had this comment in the all core devs earlier this week that if there's three forks a year on average you're out!

I think historically we have been between 0 and 2 I think knowing the amount we aim for can help be a loose constraint there

If we are saying that we want to do one or two forks a year for example it kind of gives you your cadence right its like 6 months

even though you are not ready at exactly the 6-month deadline you know that like 3ish months in you can't accept anymore EIPs and things just need to be kicked out in the next one

So aiming for a loose number of upgrades per year. 

**Peter**

Yeah, so the problem with hard forks is that implementing a hard fork is an insignificant amount of time compared to making a new client at least in the geth team

So we are always very deep in some weird refactors or optimization or experiments or what not and every time we get okay now London is coming up everything need to be put on hold or even if not on hold
kind of okay lets implement this ok now test it, oh it fell apart we change it repeat

So it just puts everything else on hold, and we kind of need the time in between hard forks where people can actually focus on getting their clients better and not just upgrading the consensus

For example if Turbo Geth or Erigon they figure out a new data model that is very promising, and they need 5 years to do it now if Erigon were a mainnet client that actually a mainnet client that was actually alive on mainnet then it would mean that during those 5 years they would have had to implement and constantly tweak their own new model to this old hard forks, and they would be nowhere with their new model 

If you just go hard fork hard fork I mean its perfect ally fine as long as clients only work on hard forks and nothing else, but if want clients to actually optimize and work on other stuff you kind of push people too much

The problem is that its super hard to tell a client you have 2 months to work on your crap then we are back to working on hard forks because several projects take more than two months

**LightClient**

I am just curious if other core developers have thoughts on how to deal with the next 18 to 36 months on ethereal because there are a lot of really significant changes that are theoretically in the works things like address base extension and changing the state trie?

Like how can we balance this in a way that clients can do their normal maintenance and improvements but also support these larger scale changes? 

**Peter**

Just a tongue-in-cheek comment changing the address base extension and changing the trie both will not happen in the next two years

**Ansgar**

Did you say the next two or three years?

**Peter**

I said two I was a bit more optimistic 

**Ansgar**

I see two I can believe but three I would be surprised

**Tomasz**

I think London fork was really demanding in the amount of work around the transactions so maybe some better road mapping and clear barriers

like this fending off the EIPs and different ideas and people trying to push them just to happen in this coming fork

It was very tiring and distracting like, so we could have the conversations and there were lots of conversions on the sides when we were discussing bigger changes the research bigger EIPs but the moment when they were changing into oh so maybe lest have them in London that was very tiring and distracting because suddenly it was a bit harder to plan the fork that was just like one or two months away.

I was happy to pick the bigger finds for the next fork and start having this conversation about next forks with people, and they will be less pushy for any big changes that were proposed

Then long term planning for a year and a half for the client development is also more reasonable, but we have seen that over and over again that we have some changes dropped like one two three weeks before the forks hitting the test nets and people thinking that this is okay because it is so normal.

**Ansgar**

I just wanted to briefly say that as one of the EIP authors of 3074 which was like a good case study here in the sense that I think if there was kind of clarity that lets say for example we have 2 feature forks every year, and they are 6 months spaced out 

Then it would be very easy to say yeah the EIP isn't ready yet there are some security concerns lets kind of take a step back and address them then we know if it's realistic to target this one or the next one.

I feel like a lot of these problems with EIPs really being pushed hard also comes form this uncertainty where people have the fear that if they don't make a specific fork its completely unclear how long they have to wait.

So this predictability around forks would also help greatly reduce the amount of pressure people feel to get their EIP into the specific next fork or else their EIP will be lost forever.

I mean of course I am being a bit hyperbolic here but I think the point generally stands and also I feel like relatedly things like the approach with the YOLO networks of basically of more liberal test nets where's you can just experiment with additional changes 

so basically we have these latent test nets where ones A fork we have a cutoff so say 3 months before fork, and then we basically look at the test nets and take all the uncontroversial EIPs that have been fully agreed upon and that have been also fully implemented and tested already and just take them, so we don't have to discuss much 

I feel like this general approach makes sense to me

**Marius**

Yeah, I think that the biggest problem I see is testing it's not really implementing the changes basically the testing team can start real testing of the implement ions after everyone has implemented their changes

Of course because different client teams have different people working on it and different amounts of funding and stuff so some teams are faster implementing a change some teams are slower 

The testing teams can only start working only after everyone else is done and then I think we need at least 3 months of fuzzing, state test, test networks to really be reasonably sure that this doesn't break on mainnet 

So I would be totally against having a more stringent schedule 

I think it might makes sense to have two forks per year but more than that I think is really heavy on the client teams and I myself have been pretty burnt out the last couple of weeks due to London, so I think some of the other guys feel the same way

So that is just my two sense

**LightClient**

It feels like we need a much longer term vision on things

I think 3074 is a good example of something that shouldn't have even been allowed to be discussed like it should have shut down in March 

Like I understand why we started discussing it because it seemed like a potentially good change that may have gotten rolled behind the merge and it may still get rolled behind the merge or never ship
but because of how soon London was I think we should do a Better job of getting the fork scheduled far in advanced having an idea of what is going into it far in advance not even allowing discussions of changing the schedule 6 months before the fork

Maybe this is just a naive opinion I don't know 

**Tim**

I strongly agree with the more long term planning and its something I have been trying to think about how we can do and I think there is a lot of legacies in the format of how we run all core devs that tends to bias towards shorter term planning

The one change with like I feel like we could plan one ish year out not too poorly but after that it gets very hard with the kind of speculative nature of stuff

SO like for example Ansgar mentioned address based extension and verkle trie migration right, and we could say we will do the verkle trie stuff and address based extension and 6 months from now you know there has been no progress on verkle tries and address based extension is kind of coming along

I know that when I was planning EIP 1559 I thought in March 2020 I thought we would get it done by the end of 2020 and the that early or mid 2021 which is now we would have stateless live and I really wanted to have that done before stateless 
obviously the path around state expiry has changed a ton, EIP 1559 took like 3 times as long 

So it's the uncertainty of when you do longer term planning gets much higher and if you have a bunch of different initiatives it's hard to stack them and the other challenge is that it gets much easier to plan the smaller stuff than the bigger stuff

For example its easier to plan for 3074 is easier to plan for than address based extension even if say address based extension was the thing we wanted to prioritize over 3074

I am not saying its impossible but there are a couple of challenges to doing it but I agree we probably need to move in that direction
and this will get even more complicated after the merge because not only do we have to coordinate with the execution client teams, but we are going to have the whole consensus layer on top as well

**Micah**

This actually an interesting question for post merge world how much work is needed by the various teams for upgrades do we have to upgrade both clients each time or is it possible to upgrade one without the other

**Mikhail**

From the changes that are related to the network I don't think it will require an upgrade on both clients each time for example beacon chain clients, beacon chain has a hard fork and an upgrade it will not require execution clients to be upgraded too

but if we something like coupling the consensus and execution clients in terms of set up and in terms of configuration like let me say geth and it downloads the consensus client that is specified by the user or by default then if they are kind of bundled then it will probably require the execution clients to get updated too

That is just my thoughts


**Micah**

What about the other way around when we want to do a feature change lets say add an opcode to the EVM will that require a consensus client upgrade?

**Mikhail**

If this is just pure EVM upgrade it doesn't require any information from the consensus layer like the beacon block roots

**Micah**

So there does exist a set of features that would only require execution client updates and a set of features that only require a consensus client updates and there will probably also be a set of features that would require both so update in tandem
and its only for that third set where we will really have to worry about the complexity of simultaneous updates and coordination

**Tim**

and that will probably hit us right after the merge because people will want withdraw their ether from the beacon chain back into the execution layer, so I suspect well get to test drive that pretty quickly 

Yeah I don't know if anyone has more comments on this I feel like I definitely need to discuss this conversation and think about it more but yeah if anyone has more thoughts now is the time to share them 

**Micah**

I am sure I have more thoughts but I missed most of the call, so I am not going to say anything

**Tomasz**

I would like to keep on insisting on naming the next fork always so when we have conversation about London the more time we mention the name Shanghai the more likely it will be that people will start feeling that it is a real thing that happens next, and then they can plan a bit more.

Just simply naming it in conversations would possibly already allow us in the previous weeks to move some of the EIP to be in the next one 

How restrained it feels I feel like just giving it a name and a rough date is enough.

**Tim**

Fair enough

**Ansgar**

I just want to barely mention because we were talking about shanghai specifically for example I think in some sense it shows what the problem with this is

because I distinctly remember when we talked about what to include in London I guess 3 months ago or something basically I was in the position that I said that it was unclear if we will have something else in between London and the merge
and people were saying no yeah we will have Shanghai it will be in November or December and maybe it will be the merge then there was this whole "The merge is Shanghai" meme 

Or if we don't have the merge ready by then we will do a feature fork instead and now it looks like even if the merge happens say q1 next year we will basically have the merge first and shanghai after

Kind of like there's is a danger of talking about later out forks too soon because this is the prime example where this situation ended up not being right so not being too concert, and we end up not doing it

**Micah**

There will be a Shanghai in November because the difficulty bomb goes off in december, so we have to do something like there will be a patch that will go out in november, and we can call it shanghai

**Tim**

Yeah, but it's a big difference whether thats Muir glacier part 2 or whether it includes say EIP 3540 or 3074

**Miach**

I agree with Tomasz we should call it shanghai no matter what is in it.

like we should stick to shanghai the thing that happens after London and the next thing after London is the ting that will happen in November, we don't know what that is going to include yet but that will be shanghai

**Tim**

yes but I think from the perspective of EIP champions if you tell them you might be in shanghai but realistically nobody thinks we are going to do feature work aside from the merge then it doesn't really solve the problem
right something will happen but it doesn't give them a feeling whether its likely that they will be included in that

**Tomasz**

At the moment we have two options it might go to shanghai or tell them it wont to go to shanghai. 

I would really like to tell people that "oh yeah it seems like something that should go into shanghai or I think this is more reasonable for Cancun and give them the rough dates of November and may.

**Alex**

This might be a dumb question but regarding the merge is um any of those sides like the execution side does it know about what epoch we are in vs does the consensus side know what block number we are in?

I am asking whether if there is like any consensus level coordination like what hard fork should be active or whether all the node operators just have to know what versions of both of the clients to run

**Mikhail**

Consensus layer is aware of the block number that is on the execution chain there is a link between.

yeah, actually beacon chain clients uses mainnet clients to grab eth1 data from it and put it on the to onbard new validators
but whether the caution side is aware of the epoch or the slot it depends on like what we will implement.

it depends on the consensus API obviously we will need slot for some of the codes like beacon block root in the future, and we will probably need epoch to signify the network upgrades after the merge

Its not like aware of epoch now but it can be it's up to us.

**Alex**

does that mean that the beacon chain side when it asks the execution layer through RPC method it would check what block number it is and it would just reject building a block if it just walled or something
so are we insuring that everything is in sync with the latest hard fork requirements is that then just driven from the beacon chain side

**Mikhail**

Yeah, that is a good question um are you referring to the hard forks after the merge or to the merge hard fork itself?

**Alex**

No its more of a general question after we are in this merged state

Just a question with was asked what happens when one side needs to be updated and what happens when both sides needs to be updated

Just in general how will node operators know that both of their client are properly updated

Just to maintain this independent ally seems to be prone to issues

**Mikhail**

Right I have been think for a little bit about hard forks after the merge and I have been thinking about a single point of hard fork coordination whether it be pure consensus, chain upgrade or execution or both

So it will likely be the focus of the beacon chain which makes a lot of sense  so and the execution client will need to be adjusted to be able to enable new logic based on epoch propagated down from the consensus layer
but this is just the basic thoughts on it

Does it answer your question

**Alex**

Yeah, that this needs to be discussed I guess

**Mikhail**

Yes definitely

**Alex**

Yeah, maybe if there is no specific point for this in the merge road map document then this would be an interesting one to be added to the

**Tim**

Yeah, that is a good point 

On that note we are basically at time do people have any finally thoughts questions or comments in the last minute

Thanks everyone see you all in two weeks


## Date and Time for the next meeting

July 23, 2021, 14:00 UTC
[Agenda](https://github.com/ethereum/pm/issues/354)

## Attendees

- Pooja 
- Tim Beiko
- Jared Doro
- LightClient
- Gary Schulte
- Guilaume
- Alex B.
- zsfelfoldi
- Danny
- Marek Moraczynski
- MariusVanDerWijden
- Rai
- Mikhail Kalinin
- Justin Florentine
- Trent Van Epps
- Karim T. 
- Bhargavasomu
- Ansgar Dietrichs
- Dusan Stanivukovic
- Micah
- Vitalik
- Peter Szilagyi
- Sam Wilson
- Tomasz Stanczak
- Piper Merriam
- Guillaume

## Links discussed in the call (zoom chat)

09:30:51 From  Tomasz Stańczak  to  Everyone:
	I think it is 10% for us

09:37:35 From  MariusVanDerWijden  to  Everyone:
	Code: https://github.com/ethereum/go-ethereum/blob/9624f92edef5e0a76a97efd302e983077acb6e35/core/tx_list.go#L279

09:37:45 From  MariusVanDerWijden  to  Everyone:
	We require bump in both fields

09:38:12 From  Tim Beiko  to  Everyone:
	https://github.com/ledgerwatch/erigon/wiki/Transaction-Pool-Design#changes-for-eip-1559

09:38:19 From  Tim Beiko  to  Everyone:
	Erigon’s design ^

09:40:37 From  Péter Szilágyi  to  Everyone:
	https://github.com/ethereum/go-ethereum/blob/master/core/tx_list.go#L299

09:41:11 From  MariusVanDerWijden  to  Everyone:
	Yep, stale comment

09:42:02 From  Mikhail Kalinin  to  Everyone:
	https://github.com/ethereum/pm/blob/master/Merge/mainnet-readiness.md

09:47:11 From  lightclient  to  Everyone:
	json-rpc spec PR with change discussed earlier: https://github.com/ethereum/eth1.0-specs/pull/251

09:47:12 From  lightclient  to  Everyone:
	PTAL :)

09:52:03 From  Tim Beiko  to  Everyone:
	Could we just leave the last totalDifficulty?

09:52:26 From  Tim Beiko  to  Everyone:
	It makes it clear that all clients converged at the same spot + that this is no longer a “valid” randomness source.

09:53:48 From  danny  to  Everyone:
	sorry, I didn’t do a hand up. will try not to jump my turn next time

09:53:57 From  Mikhail Kalinin  to  Everyone:
	:-D

09:54:29 From  danny  to  Everyone:
	Axic, it’s that total difficulty calculations might overflow

09:54:39 From  danny  to  Everyone:
	when they previously assumed that difficulty was a much smaller number

09:55:06 From  Alex B. (axic)  to  Everyone:
	I got that :)

09:55:20 From  danny  to  Everyone:
	:thumbsup:

09:55:23 From  danny  to  Everyone:
	ha

09:55:31 From  Alex B. (axic)  to  Everyone:
	In old contracts it would be wrapping around, in new ones it would revert

09:55:32 From  danny  to  Everyone:
	👍

09:56:22 From  danny  to  Everyone:
	and happy to discuss the list in discord anytime

09:57:21 From  Tim Beiko  to  Everyone:
	Yes! #merge-general :-)

09:57:41 From  Alex B. (axic)  to  Everyone:
	There were also many different discussions about these opcodes on different channels, would be nice pulling up those conversations and documenting the findings

10:01:23 From  danny  to  Everyone:
	have to run! thanks everyone. have a great weekend

10:01:31 From  lightclient  to  Everyone:
	c ya

10:05:55 From  Ansgar Dietrichs  to  Everyone:
	i feel like ideal would be 2 forks per year, 6 months spaced, and the understanding that we are fine if changes have to wait because they barely missed a fork

10:05:56 From  Tomasz Stańczak  to  Everyone:
	I was opting for more forks but only when people do not airdrop additional 3 EIPs each time

10:06:10 From  MariusVanDerWijden  to  Everyone:
	I think the difficulty bomb also greatly increased stress levels especially for london

10:06:15 From  Tomasz Stańczak  to  Everyone:
	like London -> I was fiercely defending less EIPs

10:07:12 From  Artem Vorotnikov  to  Everyone:
	difficulty bomb = sadomasochistic baton that we made to hit us and stress us for a very weird reason

10:08:34 From  Ansgar Dietrichs  to  Everyone:
	I think it is hard to speculate about the counterfactual, but in my view the difficulty bomb help keep Ethereum commited to a full PoS shift in the future, and avoid the risk of that being contentious

10:08:47 From  Ansgar Dietrichs  to  Everyone:
	although maybe looking back it might have been unnecessary

10:11:50 From  Tim Beiko  to  Everyone:
	Lightclient you can go next, and then Marius :-)

10:12:52 From  Alex B. (axic)  to  Everyone:
	We had the same conversations 2 years ago :)

10:13:12 From  Tomasz Stańczak  to  Everyone:
	yeah :)

10:13:16 From  lightclient  to  Everyone:
	how do we avoid having the conversation again in 2 years?

10:13:35 From  Alex B. (axic)  to  Everyone:
	The result then was to try a process where eips are considered based on readyness and not tied to a HF.

10:13:39 From  Tomasz Stańczak  to  Everyone:
	but it intensified, we are doing 4x more now?

10:13:45 From  Tomasz Stańczak  to  Everyone:
	which is good

10:13:56 From  Tomasz Stańczak  to  Everyone:
	the teams are bigger

10:13:56 From  Alex B. (axic)  to  Everyone:
	Even though that was the plan, we ended up doing a "lets do 2 HFs in a year".

10:14:30 From  lightclient  to  Everyone:
	it feels like we need a much longer term vision of things, we shouldn't even allow the discussion of new eips added to a hard fork < 6 months before the fork

10:15:05 From  Alex B. (axic)  to  Everyone:
	Maybe there are enough teams now to maintain the pace we wanted to have 2 years ago. But now we want to increase a pace again ahead of the throughput teams have 😅

10:15:18 From  Tim Beiko  to  Everyone:
	That’s very well put, Axic :-)

10:16:57 From  Ansgar Dietrichs  to  Everyone:
	would there be value in having regular & hard cutoffs for inclusion decisions, but then a “whatever time it takes” for testing & rollout after? so e.g. “we decide which EIPs to include in the next fork on the first call in April and October, and then fork whenever ready after that”

10:19:31 From  Alex B. (axic)  to  Everyone:
	After the merge the system will be complete, no updates needed 😅

10:20:21 From  Ansgar Dietrichs  to  Everyone:
	ah right, forgot about that, Ethereum will finally have reached Serenity! ;-)

10:21:18 From  Mikhail Kalinin  to  Everyone:
	:-D

10:22:42 From  Micah Zoltu  to  Everyone:
	I know when I named my lab grown meat, it made it feel more real.

10:23:03 From  Tomasz Stańczak  to  Everyone:
	you see, it works :)

10:23:09 From  Micah Zoltu  to  Everyone:
	💯

10:24:34 From  Tomasz Stańczak  to  Everyone:
	Name Cancun please

10:24:44 From  Tomasz Stańczak  to  Everyone:
	always two ahead

10:24:52 From  Ansgar Dietrichs  to  Everyone:
	and for the record, I prefer a strict “merge first, feature fork after” approach

10:25:02 From  Micah Zoltu  to  Everyone:
	We could just name 100 out.  🤷‍♀️

10:25:10 From  Tim Beiko  to  Everyone:
	Prague, Osaka

10:26:13 From  Micah Zoltu  to  Everyone:
	I would love it if we could have a document like:
	Shanghai - Q4 2021
	Cancun - Q2 2022
	Prague - Q4 2022
	Osaka - Q2 2023

10:26:40 From  Tim Beiko  to  Everyone:
	The challenge with that is how do we call + when do we schedule, say, the Withdrawal fork?

10:26:42 From  Micah Zoltu  to  Everyone:
	Then we can just target difficulty bombs at each, and at the least we'll launch "on time" with difficulty bomb adjustment only, and the fork will happen around that schedule.

10:26:47 From  Tim Beiko  to  Everyone:
	Do we make that Cancun?

10:26:51 From  Micah Zoltu  to  Everyone:
	Whenever it is ready.

10:27:02 From  Micah Zoltu  to  Everyone:
	It goes into the next hard fork after it is "ready".

10:27:21 From  Micah Zoltu  to  Everyone:
	And we can always do one-offs for emergency/time-critical things.

10:29:29 From  Micah Zoltu  to  Everyone:
	FWIW, I can appreciate how stuffy and anti-agile pre-planned hard forks is, but I think Ethereum core development has reached a scale where the coordination value of having a relatively strict schedule outweighs the benefits of a more agile solution.

10:29:49 From  lightclient  to  Everyone:
	+1
