# Eth2.0 #69

### Meeting Date/Time: Thursday 2021/07/29 at 14:00 GMT
### Meeting Duration:  60 minutes
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/229)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=NJWYZ0gABfg)
### Moderator: Alex Stokes
### Notes: Jared Doro

-----------------------------

# **Summary:**
- Altiar devnet went well, but there is a few minor fixes
- Rough consensus for forking Pyrmont in 3 weeks
- EIP-3675 has been merged
-----------------------------                                                                                                                                     
      
# 1 Altair Devnet 2

**Alex Stokes**

Welcome everyone Danny is not here today so I will be facilitating the call. 

Let me pull up the agenda but the first thing is the devnet

SO it seems like it went pretty well there might be some minor bugs with block production and sync aggregation.

But otherwise we successfully forked the devnet and yeah built a new chain, Is there anything anyone wants to add to that right now

**Paul**

we probably want to have a chat offline about wether we want to declare that a success or not, it did pretty well but its not an A+ I would say.

Maybe we will have a chat offline wether we will have another one

**Alex**

Yeah I mean we definitely want to do another one, but it is still exciting to see progress even from the last one

**Paul**     

Yeah well done everybody

**Zachary**

We did deploy some last minute fixes and I guess this didn't go that well, I have seen a lot of issues still on our side 

# 2. Client updates

**Alex**

Cool okay we will circle back to altair after the client updates, so I am sure we will have another touch point for that 

Lets start with lighthouse

**Paul**

Hello, so we have been working a lot on our 1.5.0 release we published a blog post this week that details the features it will contain

Our Altair progress is coming along well 1.5.0 will have Altair testnet support out of the box

We are also working on testing some upgrades to our networking stack.

There has been one last rare bug we have been hunting, but luckily we managed to get a back trace on it in the last couple of hours so we will be climbing through the function calls tracing that one down so that is a good sign.

We can expect to see the 1.5.0 release candidate in the next week or two and once we get 1.5.0 out we will start working on our next release.

That should include weak subjectivity sync, remote signer, and some nice CPU saving looking at perhaps an order or 40% reduction on CPU usage.

So that's it for us.


**Alex**

I am excited  for the weak subjectivity sync I was syncing the chain from scratch the other day and it took a while

**Paul**

I think use developers are going to be the ones benefiting from it so much because we can spin up nodes quickly

**Alex**

Great looking forward, lets go to nimbus next 

**Mamy**

So in the past two weeks we had a couple of people at ethcc besides that on the dev front we did a lot of updates to have a proper working validator client and the rest api and of course altair work so that current testnet goes well. 

I would like to mention that we are starting to work on weak subjectivity sync as well.
  
**Alex**

Great that is exciting, next lets do prysm 

**Terence**

So we released version 1.4.2 last week and it has teh awesome doppelganger feature so I encourage people to try it out.

We also most importantly contains updates for the london hard fork so don't forget to update it before next week.

Other than that most of our resources on altair optimization we have been doing works in trinity(internally?) we refactored rpc endpoints under one place and aside from Altair

we are mostly just bug fixes with the eth-2 api and then the slasher.

Thats it thank you

**Alex**

great and Terence are the eth-2 api updates are those in the release yet?

**Terence**

Yes those are in the release and we encourage people to try it out, and a lot of people have been trying it out then opening issues so that's awesome.

**Alex**

great yeah excited to see 
               
okay how about Lodestar 

**dapLion**

               
Hey everyone so I'm excited to share that finally we have validators running on mainnet and they are doing just fine 
               
almost ninety five ninety six percent of the total possible reward we are getting so super excited to join the club 
               
we on the side we have our lightclient prototype functional and hope to deploy to our proper domain soon
               
 demoed last night in Toranto that went super well on that line we will continue into the research on other stile because this one is rest based so excited to try other strategies, besides that we added support for the eth one fallback functionality and we're working hard on lowering memory consumption thank you Proto the for the help in this regard 
               
that's it 
      
thank you 

**Alex**

               
yeah very exciting so you guys have a validator client now so we have another client to add and that's great for client diversity so it's very good to see our progress on that definitely 
               
and next we'll do teku

**Adrian**

               
hi, so we put it out 21.7.0 release this week its got mostly just a few bug fixes couple things you mentioned before that now actually in a release  the main one is a file handle leak jpm lead p2p a bit of a corner case there that slowly leaked file handles

so that is cleaned up

coming up so it's still in the in 
               
in the development branch  
               
is a whole bunch of changes to discovery is both a lot of work that to be more standards compliant have more notes in there when a table on and do it all nicely  that's looking pretty good  
               
and starting to investigate improvements around how we store historical states so we can create that faster 
               
plus a whole bunch of little clean ups and getting ready  alter wise probably the only thing is that we now support the contribution of proof event it on the on the events endpoint so that you can track that also because it comes in as well 
               
I think thats us 

**Alex**
               
great 
               
let's see and then yeah Saulius did you have anything you want to add  grant died out right 

TODO

**Saulius**
               
yes  solos from Grandine team so we work on various small fixes and optimizations and problem the biggest one was the implenent of  our attestation packing algorithm and another major 
               
thing is that we requested them to to this experiment I talked about last time I will try to rum multiple forks at the same time and its taking a bit longer than the expected but hope we will have some results in a couple of weeks of running client 
                              
but otherwise I think we will need only about another two weeks but it basically 
               
I would say it's such a major thing and big if somebody will try to experiment with something like this then it's probably much easier  to take just an existing find and that does hard forking in a regular way and just run this client in on the two nodes so basically so you have two separate clients  

instead of one client running two hard forks 
               
so far that's all from us 

# 3. Altair
**Alex**
               
Great thank you 
            
and let's see was there anyone else  I think I got everyone 
               
we keep adding more clients
               
okay  then in that case so we can move to talking about Altair so there is a devnet this morning and it seems like things went pretty well but there's still some places for improvement it sounds like 
               
in the meantime on the spec side we've had 
               
one release kind of two releases  the last couple weeks so things to improve both testing and and then also improving the aggregation counts with sync aggregators and then also tightening the gossip validations in its most previous release beta 2 that one I think was supposed to be in the devnet this morning but maybe didn't quite make it out  but either way these help harden the sync committees 
               
duties on the network and  yeah we to lead to better a better chain
                           
there's a yeah like I said lots of testing  with most of the both the spec releases so please clients take a look at that if you haven't already 
               
so yeah next we can move to planning and like Paul said earlier perhaps  
               
you know we moved to more asynchronous thing here but he has anyone have any any thoughts there  I think we want to see how devnet 2 went and it sounds like we want a devnet 3 so that might push back Altair itself but you know that's something we all need to decide 
               
**Paul**

I'm open to an Altair 3 next week if  if Pari's up for it 
               
**Perithosh**

yeah that sounds good to me as well 
               
does this mean we decide today when we went on to do mount?? Altair fork and then decided to abort it if next week goes badly or do we just take calls in two weeks 
               
**Alex**

we could probably talk more asynchronously   
               
I don't really expect devnet 3 to go poorly  but I guess we will have to see how it goes 

**Adrian**
               
yeah I mean we're consistently seeing the transition work well the peace we are not seeing is the 
               
yeah perfect inclusion rights on sync committee signatures, I think I'd be tempted to push it out to Pyrmont  at this point and get that feedback given that we want to kill Pyrmont  after this anyway so we really decide but to make massive changes its not the end of the world but it just gives us a somewhat more realistic use case to see 
               
you know how inclusion goes on sync committees and so on 

**Paul**
               
yeah I support that as well that's really pretty good I wouldn't mind  getting rid Pyrmont  as well to that so it 
               
something to consider if we deal with Pyrmont  is that we have to get we're getting users around it now so we have to make sure it's all included in the release and things like that  just something to consider 

 **Zachary**

and I hope we'll be able to use the next few days to kind of run out these issues that we are seeing 
               
**Alex**

That would be great we should definitely keep an eye on the sync committee aggregation like Adrian mentions and 
               
yeah I mean generally I think that progress is going well so we'll just keep pushing forward 
               
**Adrian**

yeah I mean in terms of the fall of ?? I think it needs to be over at least a couple of weeks out anyway because we need to get back the config for ??  updated in each client and a release so everyone has to get a release out and then we go to convince users to upgrade or it'll just go into non-finality and kind of
               
cause chaos just because people didn't upgrade more than because there is a problem with the fork, So we would want to do a fair bit of lead time I would say

**Paul**
               
was there a tentative date for forking Pyrmont  already
               
**Adrian**
               
no I think we were going try and decide that on this call
         
**Paul** 

I mean ???? ??? ??? ?? for me is a month maybe three weeks or four weeks

**Adrian**    

yeah I am thinking the minium would be two three is probably better 

**Terence**
               
yeah I think three or four weeks works for us since we still have to merge our hard fork changes into our master branch 

**Paul**

So is that a vote for four weeks was it Terence?

**Terence**

I would say between three to four weeks yeah 
               
so three is fine too 

**Alex**
               
okay I mean it sounds like there is rough consensus for three  the obviously if something comes up we can reevaluate 
               
but yeah I mean the sooner we move Pyrmont  the sooner we get to mainnet

**Paul**
               
yes totally if it's if it's useful I don't mind  like if we want to spin up another devnet next week I'm I don't mind doing that it's fairly low  input on my end  maybe I just wanna stay up for it but we could we could spin one up if if that's gonna be useful to anyone having problems I'm happy to do that so 

**Alex**
               
right and that may be helpful but  yeah it does seem like the forking part is going well so then maybe we can just keep the devnet 2 running for these various debugging issues 

**Paul**         

yes sure

**Alex**

I guess if anyone would like very strongly preferred a devnet 3 then  you know let's chat but 
               
I guess we'll just see how right if there's demand 

okay so sounds like maybe devnet 3 maybe we don't need it  I guess we will look a lot more at devnet 2 from this morning and have a better idea 
               
and we can discuss that asynchronously 
               
and then it sounds like there is rough consensus around ?Pyrmont  fork in say three weeks once we've gotten some more debugging updates and and releases and to clients and then that pushed users everyone's aware and  then we can do that 

**Paul**
               
Nice one that made me proud 

# 4. Research updates

**Alex**

great let's see from here I'll move on to other different types of updates was there anything with Altair anyone wanted to race before and move on 
               
okay 
               
that case  let's move on to research updates or updates with that spec generally does anyone have anything to add here 
               
okay sounds like no in which case we'll move on to our next topic the merge updates 
               
# 5. Merge updates

does anyone have anything to present here Mikhail not to call you out but maybe if you have something to update there 
               
**Mikhail**

yeah I can give a short update on that 
                              
first eip-3675 has been merged recently 
               
thanks a lot for EIP editors to give it a green light  
               
and it's in a draft status anyway so it will be updated further and more clarification will be added on demand  there is already a follow up discussion in the PR thread regarding some points so 

yeah but anyway it's already should be considerate by 
               
client developers as being one of the things that will be implemented
               
it would be great if they started to take a look in order to  facilitate the development of the spec
               
also on the beacon chain side,  the beacon chain aspect on the merge stack has been rebase on altair many thanks to proto who did the job

I've also opened a pull request that the spec of london actually adds the bass fee per gas  field to the execution payload and adds a couple of verification rules to the gas limit and the base fee, so it's open now 
               
I guess yeah it's it is pretty straightforward I guess can be merged relatively soon and also there is an open pr for the p2p interface for the merge stack as well 
               
well so that's all on the merge side at least from up for myself 


**Alex**
               
well thank you yeah it's very exciting to see all the EIPs and the continued progress on  the beacon chain spec 
               
and you know that all sounds like that'll be the thing we focus on after Altair so good that we are getting it all ready 

# 6. Spec discussion 

okay  we can name to general spec discussion anything else anyone wants to bring up is there anything anyone would like to discuss 
               
**Paul**

Just regarding the forking Altair  
               
it might be handy to have like maybe Eth Staler to be involved in this or something, but it might be handy to have just a resource  that's a table of all the clients and which version you need to be on for the Altair fork this is the Pyrmont  that is and whether or not that version is being released it yet or not yet kind of like a canonical source of info  I don't think anyone from Eth Staler on the call anyone is interested in doing something like that 
               
I think it might be good take to start to get the word out asap that you know you're gonna have to upgrade your client because we are going to fork altair on a full ?? with Altair  and this is where you should look for updates 

**Terence**

we are planning a blog post about that for Prysm, but I do think it may be beneficial if something comes from eth stater or like EF for a more general blog post 

**Adrian**

yeah the more channels better 

**Pau;**

cool yeah I will blog posts as well make lots of noise about it on our end

**Alex**
               
yeah definitely a great idea  so we should definitely do and yeah and the more channels better 

**Mikhail**

I have a quick question to ?? about the weak subjectivity sync what is like rough targets in terms of date
               
for releasing this feature is like Altair o?
               
**Paul** 
               
I teku already has weak subjectivity  for us probably before Altair I would say maybe in the coming month or so, not sure about anyone else 

**Terence**

for Prysm it will be after Altair probably I would say a month after Altair-ish
               
**dappLion**

loadstar already had this implemented since a month ago 

**Zahary**

we have also had some progress on this channel plan to finish it within the next month 

TODO

**Saulius**

we will also have in a months or so 

defined defined general raduis as the tolerance loads the sate from the anchor state but I would like to trust the other teams what were the main things that you found in there this weak subjectivity implementation 
               
as fas as I know you need to the back syncing of the old blocks  before the sate that you load and is there is there anything else that needs to be done during this weak subjectivity sync 

**Adrian**

one of the surprising since we need to check the signatures when doing the back syncing of the blocks because they're not included in the hash 
               
but otherwise I think it was fairly straightforward I mean it was much as anything ever is all but nothing nothing surprising it's being able to start from the state go forward form there 
               

**Saulius**

and do you like the syncing in reverse basically do it and do you do use some mechanism which actually verifies that you end up in that state that you were just a loaded 

**Adrian**

yeah so we we work backwards we work backwards in batches so we request I don't know what the actual numbers but lets say a hundred blocks at a time  
               
kind of from the state we started with a hundred blocks forward and we checked that matches we get to keep walking backwards  it's it's a little optimistic we've got a few batches from different peers at the same time and then check out line up in that kind of stuff but ultimately it lets you 
               
not download too many blocks from the wrong branch before you discover that it doesn't actually line up with state you have got 

**Saulius**

and the and then do check that you are at the genesis that so you expect them to be 

**Adrian**

no we treat the state we started as 
               
as definitive because you can put anything you like in the block ultimately 
               
the only the only reference point you actually got is the hash and the state you started with

like you you have to check signatures but if you are as long as you own one valid device because it's something that lines up back to the genesis block is you just sign a blocked that has the parent hash of genesis 

and it'll look completely valid because all of the hashes line up 

**Saulius**
               
okay but theoretically I don't think that it would be possible to make a different chain which   let's assume you're you've got the wrong 
               
snapshots from an attacker and you'll  probably would be able to end up with a different genesis not the main one or the community one
               
This is theoretically possible right?

**Adrian**

it is possible that the attacker would be sloppy and make it obvious that they lead you astray but more likely they would just line it up to the genesis so the check doesn't give you any extra security 

**Saulius**
               
ahh okay yeah interesting 
               
I think the solution would be maybe to have some checkpoints insides there I mean between them the expected genesis and the snapshots
               
yeah as long as you as these checkpoints are burned into  the client and we assume the clients are  not adversaries and then probably that would work do you think so

**Adrian**

kind of the same thing so if the checkpoint you have is within the week subjectivity period then yes you could verify fully from their that ultimately want the state from this you can actually verify the block transitions for it
               
the checkpoint state starting from is the checkpoint like it is the one known state you're being told this is on the chain 
               
you can't easily trust stuff before that  because it  you might've had violators that have exited and withdrawn all of their funds and then sign a completely valid looking thing so there is a number of heuristics you can do to start detecting that and so on but ultimately your key thing is that you want to start for a state that's known to be valid within the week subject period and you can do that either with the state or with a root hash and what is kind of the big question I think in all of this 
               
but but it is that it's the checkpoint starting from that's that's what's giving you security and check it back from there is less useful because all your  transition are from the state you started from anyway

 **Saulius**  

if you try to sync from the genesis I mean  the other way around not backwards but the forward 

I'm just thinking is is there any benefit in terms of security here 

**Adrian**

so then you should be led astray by validators that have exited right because the because of the weak subjectivity I mean sudden not enough validators have exited yet but theoretically it could have happened by now I think and certainly at some point in the future become up a possible attack 

that you may have a chain made up of  signatures where you have nothing that's slashable 
               
which makes two completely valid chains one of them is the canonical chain because it happened in real time and one of them came along afterwards 
               
unless someone tells you which is the canonical chain 
               
or you start heuristics like I can find more nodes on this chain then that chain

**Saulius**

yeah I think I remember the discussion sometime before as I look at this 
               
okay so so basically just to sync backwards and and that's all 
               
in terms of checking the signature controller 

**Adrian**
               
yeah and the rest of things is just details so making sure that your client is able to handle rest api requests from before you have any states 
               
so there is a whole bunch of rest apis  that you cant answer because you don't have a state for Teku that was natural because we have a node that will prune anything any finalized states anyway to save space 

**Saulius**

is there in the goals that that would affect the  gossip ???
               
**Adrian** 

No the operation like 
               
in terms of tracking the head of the chain and preforming validated duties and participating in network you don't need any states prior to the latest finalized  you do need to backfill those blocks at the moment hopefully once client support checkpoint sync and we can not necessarily download all the blocks but then there is questions around who is storing them are they going to be lost forever thing and so some of the problems to solve there
               
**Saulius**

okay so to summarize there is no  magic they're just basically loading the state and syncing the blocks backwards so that was and that's all 

**Adrian**
               
yeah correct 

**Saulius**

okay thanks 

**Mikhail**

is there a very detailed description of the algorithm of this sync 
               
like starting from getting the checkpoints and going through the sate downloading and so forth 
               
**Alex**
            
I was gonna say yeah that there's nothing written down but  
               
yeah basically to start from the state and then our work your way backwards but it is very important I would say to back fill and you know it's I think given kind of on us to like say that we have the norm that you should backfill because unlike what Adrian was hinting at 

you might have this huge problem where suddenly no one has the blocks and I don't think we want to get to that state 
               
**Adrian**

I mean in terms of how to work the whole spec is is designed to be able to take a state and a block and you can always apply so it's kind of nice that 
               
there's no real reason to start from genesis in terms of
               
what you have in your client you just don't need it, but  yeah absolutely please do backfill all blocks don't make it optional don't even provide a flag to not do it just do it it'll be good for the network at the moment 
               
**Paul**            

yes thats our approach as well 

**Dankrad**
               
right I mean long term it would be nice if people could run 
               
like validators or generally for nodes without having all the history always present 

**Adrian**

yeah absolutely there's a chicken and egg problem that's been going on for a while here in that
               
we didn't support checkpoint syncing in a lot of clients because there's no way to get checkpoints states from 
               
It was a real pain to start with, now that Infura is providing it it's kind of centralized which isn't ideal would like more than just them but at least it's a starting point  so small client stopped supporting it it becomes more viable for everyone to do it a few more places to get it from

hopefully then we start to address this problem of where we store all blocks but so not every client has to have it  and I just 
               
keep working this problem until we  we are able to just store the very latest stuff in each running node and have reliable ways of getting all the stuff 
               
**Mikhail**

when you need to verify the blocks and blocks signatures when you are backfilling the block hash that's included in so the parent roots of each block is actually the 
               
hash tree root of the beacon block not signed beacon block so the signature isn't included in it so most likely you're going to get a signature and it's not going to be an issue but it's possible that I can give you the right block with the wrong signature via rpc 

I guess if you validate it there that's fine but you've got to validate it somewhere along the line there  
               
to make sure that the signature is actually the one that matches that block otherwise you'll store the wrong signature and then potentially serve those wrong signatures to all other nodes when you request them from 

**Micah**  

So basically the block signs the signature 

**paul**

Yesik the proposals to add an extra fields the beacon state to include the block signatures  as well in that so you could just go backwards that by referring signatures, but it didn't make  into Altair but maybe we will include it one day  
               
I think it's probably still out on the eth specs repo as a pr if anyone's interested 
               
**Mikhail**
               
and you will also need to recreate some states to verify those signatures right 

**Adrian**          

no you can do it without creating states in fact there's no way to create older states when you start from before the checkpoint you start with so you cant run the process backwards 
               
but it's just verified with the validators public key which you can get from a current state because we never lose that 

**Mikhail**

oh I get it

**Adrian**           

so you cant verify that that validator was due to propose that block but the proposed indexes in the hash so if you're following the hashes back then you've already verified that its right

**Mikhail**
               
yeah thank you for thanks a lot for clarification 

**Saulius**
               
regarding the history I'm just wondering will there be a big demand for a history of beacon chain after the merge point maybe somebody was discussing about that because it looks like after the merge that there wont be

I don't know maybe maybe stakers will like to see their past performance this history of the beacon chain until the merge point doesn't have an execution layer or 
               
history of data don't you think that maybe after the merge clients will sync the sate before the merge and maybe this will become common behavior

Is there such a discussion?

**Alex**
               
I don't know if I've heard something like that I would kind of suggest to keep the full state and you know our history I should say you know as much as possible I think we should have a norm that we have the full history  some of these things are discussing around like you know these longer term 

projects around certain historical state are super important I'd say they're like parallel streams of work  
               
but yeah and until then beacon node should store everything they can and yeah maybe down the line there's different sync modes or pruning modes that you know drop state before the merge but we're not there yet
               
**Micah**

I think if no client includes an option to prune old blocks than most people will just use what's available if clients start including option to prune old blocks then I think you will see a lot of people using that option 
               
**Adrian**

yeah absolutely that's been that's what we've seen eth one side 

geth downloads and stores old block by default so most people have them available 
               
**Saulius**               

Yeah I think this question came to me because I was thinking that for users that it may be a bit hard to  use the api of past blocks for instance you may have a past block 
                             
after a while there will be a block that has the same lot numbers on both chains so there will be a block number 1000
               
it exists both on chain and on beacon chain and from the user perspective well there will be maybe some confusion on 
               
which block is number 1000

**Micah**

I was gonna say we we could just say like just from a social consensus standpoint that all beacon blocks are plus one hundred million or something just to make sure we don't have collisions on the numbers for you UX purposes 

**Adrian** 

it is an interesting question because mainnet is five million blocks or so also ahead of where the beacon will be 
               
so when the merge happens the head block number drop backwards by a few million 

**Micah**
               
consensus blocks we still have the excursion block counting up from ,five ten million or whatever there at forever so they will always be conflicting

**Adrian**

yes I think 
               
I think it is something that we just need to be clear in the rest apis of how you're referring to things or in the json rpc rather 
               
I don't know how much work has been done on this to date it hadn't occurred to me until now so 
               
I might just be a bit slow 

**Alex**
               
yet I just want to add that it's almost a bit of an API issue  
               
but yeah I mean the more I think about it the more I do see the complex so 
               
one thing I can say is like Hey this is a slot number on the beacon chain and then we can keep the block numbers as they are on execution chain
               
but yeah that is a good point 
              
**Paul**

yeah we are also gonna have shard blocks I guess people just have to get used to be specific about what type of block they're talking about 
               
**Alex**            

and reload blocks and we will just keep adding more blocks

**Micah**

all block numbers have a prefix basically which indicates where they're from and we keep a list somewhere

you know prefix zero is execution client prefix one is the consensus client, prefix 2 is shard n and these prefixes you know are a billion plus whatever the actual block is
               
so that way when you're seeing a block number it's always a big number but it always starts with a hint as to what kind of block numbers it is 

**Saulius**

I think the prefixes or some magic with numbers may be affect the current execution layer 
               
we do we do there are some contract that are using what numbers the or maybe indirectly are you in that but the only one way that they just came to mind and I don't know is not nice but maybe it will contribute to the discussion maybe we could during the merge we just roll the

beacon chain slot number to the future which is aligned to the last proof of work block and I believe that maybe in future absolutely we will just forget that the beacon chain for the merge I personally don't see much value for our 
               
or users this history and then we would have a liner block numbers so just to repeat that during the merge we just roll all 
               
slot number to the future  which is like the next number after the last proof of work block so this makes a linear very nice numbering 
               
just an idea maybe it's not the best but yeah lets discuss maybe after this call 
               
**Mikhail**

all rights slots as mentioned in my pr  skipped slots will get this thing to diverge anyway 
               
I go over slots with no with no block in it and execution block numbers will be behind the slot number and eventually 

**Proto**

the slot numbers are much more like time stamps than block hights

**Saulius**
               
yeah unless we changed the logic in the clients yeah 
               
but I think of course this this would add extra complexity but otherwise I think it would be possible 
               
of course the complexity consequences add to just handle this roll in the code 

**Proto** 
               
which problem are you trying to solve the height is already embedded in the beacon block and if there's an index in the clients to map slots to block heights everything just works fine

**Micah**

I don't think there's a a code problem I think this is just from a user standpoint

users are going to end up incredibly confused when you have a block number five slash seven like what what is that like for users it would be nice if there's an easy way when they're communicating with each other and when websites present data to them it's an easy way to identify

oh this is the consensus block or oh this execution block 

**Alex**
               
right a prefix to the hash might be kind of like Mikhail was suggesting

**Adrian**  

yeah I mean post merge either you have to talking slots which that's how we number the consensus block or you are talking height of execution blocks I mean the place at this 
               
hits it probably hurts block explores or things like that a bit but the biggest issue is going to be around that the json rpc client which is where execution clients so yeah but the execution clients are really exposing the stuff and I had to backwards compatibility concerns from a beacon node perspective we're always gong to talk in slots we'll probably have some apis is to let you query by  execution height but it potentially maps to multiple beacon blocks
               
but  all the all the challenges in the backwards compatibility making this understandable for uses is really gonna be 

the execution clients so I wondered if this is something to bring up tomorrow on 
               
Core Devs more than here because they have the context in the actual ability to do something about it 

**Micah**

just so we were prepared for that call it is it's 
               
terribly unreasonable or reasonable to at some point before the merge or on the merged to just move the block number forward by a very very large number 
               
is that going to be hard or is that easy

**Adrian** 

personally I would say that would be coming yet so slot number so the advantage right now is that you can take your time and calculate the slot 
               
and it just works you know you need to add a genesis time  but it's a simple division  if you change and you've got a simple division prior to this number and then a bunch of blocks that don't exist at all its weird and then simple division from a different genesis root so its kind of 
               
at some point we might be point of doing that if we have a change the slot time but if we can put it off as long as possible it would be really nice 
               
**Paul**

yeah I would also say that skipping forward the slots is gonna be really complicated the f2 spec relies a lot on the idea of the current epoch and the previous epoch being thirty two spots and to have gaps in that it's going to be should the edge Casey I can just imagine heaps of clients just all over the place finding bugs in that yeah every time you subtract one from that slot  now you need to stop and subtract one or five million or something so I'd say that's it big big complicated my opinion 

**Proto**

it gets worse the whole fellow data registry has references to slots multiple prevalent data for their life cycle data and so if a validator tries to exit they certainly gets into some very weird states 

**Micah** 
               
so I'm hearing very hard 

**Adrian**

yeah that's right 

**Saulius**           

Maybe wa can have two numbers actually the ones thats the classical execution layer eight or something and another one is there consensus slot this 

maybe it would not basically this would not break anything but also on each end it doesn't interfere with each other 
               
what do you think?

**Micah**

you're saying just when you expose the slot number to the rest of the world you just like you know at five million to it but it for internal communication you're using the real site number

**Saulius**

no I would say maybe we keep as a public number we keep the execution layer number which is the current eight but internally which of these slot numbers which we were just 
               
we may show it somewhere in the explorers or something like that but the actual block numbers would be  
               
just as it is now in the proof of work so there would not be any gaps I mean for for the for the execution layer 

there won't be any gaps  it'll just proceed but the at some point during the merge there will be a two numbers one number will be the exclusion layer that is additionally but where number one will be a so so there will be periods that at the time  and  the number is the slot number of consensus 

**Adrian**

so the execution payload will still have the incrementing block number the execution environment will still executed at that separation still exists you still got slot amd execution block number 
               
it just flows through it's just about avoiding confusion of which one you are specifying  
               
which I think really just comes down to which api are you talk to, if you are taking to the execution client then your talking execution block numbers if you talking to the beacon node you are talking in slots 

as the apis evolve we might get into points where that becomes more confusing but then we can design the apis to take on the role and and specify which type is and that type of thing

**Saulius**
               
yep  for users I believe that they probably should see one number as a main number and it would be great ad so that that' it's just a continuation of execution layer numbers 
               
I think this is an interesting topic overall 

**Adrian**

yeah I don't think we'll get to one number because slot and height are always going to be two different numbers they just don't increment at the same speed 
               
today in the in the consent strain we don't really track height at all we just use slot but it becomes more important the execution thing
               
I suspect we might have covered this is much as we possibly can given where the beacon node side of this like I said that there's going to be confusion and problems it's gonna come up with the JSON rpc apis
               
so I wonder if we need to spend more time on this here if we just shelf it and see what what the execution guys want 

**Alex**

yeah we can move on I mean it kind of sounds like just having a pair of these numbers and just being clear about sort of the types of what you're referring to 
               
is the simplest path forward and we can leave it open for  you know experimentation with other options 
               
So on that note does anyone have` anything else 
               
**Leo**

yeah I want to mention I have been talking about a crowded and a dashboard three times before and I wanted to share it with you today mostly we show the information about the geographical distribution of the notes and also the different clients distribution 
               
which is not on what we might expect I mean it could be better in terms of software distribution  and we have a couple of other things that you can see in the dashboard and so I also want to mention that  the press release for the standardization of the metrics has been merged thanks Pari for that 

and so I would like to ask the different plants implementers to please  do the few changes that are necessary so that we have standard metrics across clients in a couple weeks if possible 
               
yeah I think that would be all thank you 
               
**Alex**

right here it's very exciting to see this [dashboard](http://migalabs.es/crawler/dashboard) 

**Leo**       

thanks 

**Alex**

okay anything else from anyone otherwise you can go ahead and call it early today 
               
**Terrence**

this one thing I realized that when I am looking at the mainnet validator coms is  that it's slow the creaking of to be to be the same as the Pyrmont  number so we'll have to make a decision on but I do think that we should increase the availability of the con on the ?? side 

whether thats post Altair or before it but the we will have made a decision today but I just want to notify people that 

**Paul**

I agree with that sentiment 

**Alex**
               
yeah thank you Terence for bringing that up its definitely important to keep an eye on 
               
just to add we probably don't want to fork ?? and ?? at the same time but  because I get to prod  you know after ??  
               
okay any final things arise we will wrap it up 
               
okay sounds like no thanks for joining everyone, again very very excited to see our progress on Altair and  we will keep pushing on that 
               
and  yeah I think that'll be it 
               
---        
## Date and Time for the next meeting

July 23, 2021, 14:00 UTC
[Agenda](https://github.com/ethereum/pm/issues/354)

## Attendees

- Paul Hauner
- Pooja
- Jared Doro
- Micah Zoltu
- Ben Edgington
- Parithosh
- Hsiao-Wei Wang
- Lakshman Sankar
- Alex Stokes
- Saulius Grigaitis
- Mikhail Kalinin
- Zahoor
- Protolambda
- Adrian Sutton
- Potuz
- Terence
- Lion dappLion
- Carl Beekhuizen
- Caymen Nava
- JosephC
- Leo
- Mamy Ratsimba
- Zahary Karadjov
- Lightclient
- Dankrad Feist
- Preston Van Loon
- Ansgar Dietrichs

## Links discussed in the call (zoom chat)
