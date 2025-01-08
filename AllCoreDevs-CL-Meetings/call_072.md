# Consensus Layer Call # 72



### Meeting Date/Time: Thursday 2021/09/09 at 14:00 GMT
### Meeting Duration: 30 minutes
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/235)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=k3heiZA5j5s&t=690s)
### Moderator: Danny Ryan
### Notes: Jared Doro

-----------------------------

# **Summary:**

* Prater forked successfully
* Look into why we are seeing lower than expected sync aggregate participation
* plans to do a release late September and upgrade in October
* engine API discussion will be moved to issues in the execution APIs repo
* A PR [Set the value of the random field to the previous randao_mix](https://github.com/ethereum/consensus-specs/pull/2581)


****
-----------------------------
# 1. Altair
**Danny**

Welcome to the call here is the agenda I think probably the most pressing things to discuss is Altair
and Altair time lines and what we need to do to get from here to there
to that end the first thing we'll talk about is Altair, Prater forked
I think generally successful and there were a couple of bumps that were ironed out relatively quickly and I think one of the main bumps was self healing after like epoch or so which is good 

I have to take a look at the prater explorer or the Piermont explorer we're still seeing lower than expected sync aggregate participation I think that we certainly need to do a bit of digging and analysis on
if there's a pattern to who is being missed this is a a single client issue or if there's it's more in the aggregation protocol itself so
try we'll to look into the next couple days to see what we find and let you know any comments or discussions on prater?

okay in light of the standing issue with sync aggregates that we still need to uncover and after some discussions with the Prysm team who is simultaneously trying to release Altair and they're big V.2 I think this been on their end requests for 
at least a couple of weeks delay, so rather than doing releases next week and fork at the end of September
do releases in September and fork at October I think that generally
although we need to ship we need to get it right so I lean towards
doing that but also simultaneously during this month shifting and share resources to ensure that we have kind of the next wave of merge implementations ready to work with the execution side because they are heavily in progress and I want to make sure that Altair does not begin to be a blocker on that or that the consensus side isn't being a blocker on that

also I think we are continuing to enhance test coverage on Altair and our immediate release today but then maybe another one at the end of next week as we continually kind of go back and forth with the clients on on different edge cases and bugs that were identified.
general planning other than extended time and identifying the issue on the sync committees on the test nets we are observing what else needs to be accomplished in this next months some some where the musts on y'alls end?

**Terence** 

I will say just more enhanced testing on test nets by enhanced testing I mean slashing, deposit, withdraw or these or the manual operations and it would be fun to trigger some like chaos monkey tests with wave timing such as like sending the blocks really late, and sending the attestations really late  and just see what happens from there

**Danny**

right so Piermont especially for the chaos monkey stuff might be the better target I think one of the easiest things you can do is force times to be off so force subsets of nodes to have their clocks skewed I think that would induce quite a bit of what you're eluding to which is I think probably we could do without to much issue we do still have this remaining there still are a few things to get done on Piermont under scenario testing
if you do have updated releases please make sure you're getting them out on Prater and Piermont
I know that a number of us have discussed the shifted timeline outside of this call I do want to leave some room if people want to chat about a bit more here obviously no pressure either way on that

**Adrian**

so is that saying we've been trying to set a fork epoch next meeting the meeting after?

**Danny**

Lets see, I mean we could I think it might be my calendar is asking me to sign in just give me one second
I mean if we are going to do releases in the last week of September then we must pick a fork two weeks from now

**Adrian**

yeah I mean I'd rather sooner rather than later but basically picking the fork even if we pick an epoch decent way in the future

**Danny**

yeah I mean we could do that right now I am especially with the sink aggregate issue not resolved rather than to put it on the calendar

**Adrian**

yeah I think that is reasonable

**Danny**

okay after this call I am going to circle back with my team and client teams and see who wants to do some of that investigation on the sync aggregate bits and what we can do to make sure we get to this list on Piermont and any other sort of wacky testing cases like messing with our clocks and things anything else on Altair with respect planning
onward thank you
# 2. Client Updates
let's run through some client updates we can start with Lodestar
so I'm having a lot of trouble hearing you Lion are you can you get closer to the mic
can anyone else hear Lion?

**Lion**

so yeah we we started to implement the merge not a lot of progress but working on it
we have also reduced the memory cost of our states by half so lot of less to see
and we have shared documents with our proposal for implementing our light client with the teams we got some feedbacks and will appreciate anymore I also reach out if you are interested in implementing that
that's all thank you

**Danny**

excellent thank you nimbus

**Zachry** 

Hi, for the Prater route we achieved another Altair beta but we're now working on preparing to stable released with testing the same code form mainnet the other other notable feature that will be implementing during this release is the (Multi-Core)? POS verification support that we've been working on which will be initially update feature we've also prepared system packages for linux and installers for Windows and Mac OS
on the two we also released the (abs installers)? set up beacon node service on user machine automatically after installation
on the development front we have added (SSZ)? payloads the rest API and we started work on a live ? as well
the main focus I guess for us for the rest of the month will be preparing for the merge and the work here we will be both on the Nimbus-Eth2 side and the Nimbus-Eth1 side so we want to you have the capability to
operates on it or not so much we both glance
we've also hired Ajewel Mohamed who should be known to someone you
he'll be working to help us create the mobile UI  for monitoring and managing your beacon node

**Danny**

very nice Grandine

**Saulius** 
yes this service ? so worked on some optimizations and full focus is still on this
there are multiple runtime so to to accommodate to the Altair hard fork looks like we are getting closer to kind of a working machine that that's all thanks

**Danny**

got it and Lighthouse

**Paul**

hello so aside prepared for our next major release which is going to include week subjectivity thinks we've done a bunch of successful syncs this week which is cool it's also going to have support for the web3 signer remote signer I've also doing been spending a lot of time on analysis of Main net we working to try to understand why Lighthouse seems to not receive some consistent numbers this number of attestations we also identified some issues with other clients regarding attestation packing inefficiencies in the communicated those
we've been running analysis on late block proposals identified in an outstanding staking pool and contacted them I'm not exactly sure which client they use I haven't gotten much detail we've made said oppositions Lighthouse to reduce the impact of late blocks, we have added some more metrics to a special server side end point to try and track the peers and gratifies and other indexes that late blocks coming from
and we are also starting work on implementing the latest merge stack, and participating in a new round of test nets next month that's it for us

**Danny**

great
I'm on the attestations that you're not receiving those are actually used to figure out there they're not hitting your mempool at all?

**Paul** 

yeah that seems to be the case the way we did this thing where it like shadow proposing blocks so when we see a block we also propose a block and compare the attestations on and we can see that there's some less in ours and then if we go in take those additional ones in feeding then into our mempool then we do include them so yeah I was still way we've got it cleared from the consensus layer I guess you know you can be free because of some kind of figure out what's going on there

**Danny**

very interesting okay thanks Paul and Teku

**Adrian** 

Hi so we have had a few key things going on so we had an issue with the Altair upgrade on Prater where we were shoving invalid attestations into blocks and then correctly rejecting our own blocks which is good
So thats been fixed up it was an interesting interaction with the gossip validation and signatures where we had a state before the fork activated so ___ won't pick up what the attestation should have been __ the different fork id
So we fixed that so we actually no longer use in the spec theres the getDomain where you pass in the state and it'll take the fork from the state, we removed that function from Teku entirely
So that we are always deliberate about forks so we don't run into these kinds of problems again. We have put in a bunch of fixes for redundant attestations that we were including in blocks
So that should help with some of the issues on mainnet once we get that out in terms of making space for other attestations and reducing inclusion distances and our Paul has been doing a bunch working digging into
where we are seeing duplicate attestations and the value the ()? at the application level. So what we have found is that anything that is going to be detected as a duplicate is done at the gossip level through the __ P2P __
and nothing useful ever gets ported out at the application level primarily because the application level sees so many attestations that it overflows our current cache straight away and we have had to make it dramatically bigger
and P2P is already holding onto the message for 32 slots which is as long as they should be valid. So we are going to do some testing on Prater and Piermont if not having that cache on the application level and just depending on seeing messages from the P2P 
I think Lighthouse has mentioned before that you've some attestations that have come in very late and we have certainly seen that as well its a small number but its well after they should have been invalid and some kind of odd little duplicates kind of filtering through there
Beyond that a bunch more optimization work has been going on strictly between the number of calls the validator and the beacon node stuff like that, just kind of carrying on and improving the world. So we will probably get that into releases probably relatively soon if we are not setting a Altair fork epoch, keep an eye out.


**Danny**

got it thank you

**Paul** 

We have been seeing lots of old attestations around I think Lodestar also noticed old blocks floating around we haven't looked into it but I do remember having to
make some changes to be more defensive against us I'm not sure if Michael communicated that we also identified an actor on the network that was sending duplicate aggregate attestations as well which is probably making people's cases struggle as well yeah 

**Danny**

define duplicate aggregate association

**Paul**

basically producing the same SO two aggregates for the same epoch from the same aggregated index
with different values different roots

**Danny**

gotcha and consistently like many of them

**Paul** 

yeah I believe it's because this I didn't look into it but I believe it's very consistent
we've reached out to who we think it is

**Adrian** 

aren't they at the risk of getting slashed we do that if you had the same keys in two places
one of the things where your attestation will appear the same but your agragated are likely the different you'd get away it until you propose blocks

**Paul**

I don't I don't believe so

**Adrian**

interesting early warnings though

**Danny**

okay and prism

**Terence** 

yep Hey guys Terence here so last two weeks we have been mostly on merging Altair code from development branch to the master branch making really good progress on that one from ten thousand lines to two thousand lines and then we are also going through intense code review off the consensus code and the code that uses cache so those are mostly where the issues are and then were preparing for V2 release we are cleaning up all the features and getting ready for those to be merged to the master and then just want to shout out to the beta 3 spec tests for the people that worked on it we found the consensus bug regarding validate life cycle when processing rewards and the bug has been fixed and it is in the latest release and that's all the test nets will host reviewing for the test coverages regard validator life cycles and then regarding mainnet           
we have been reviewing our cache implementations when we first implement those cache we were prepping the validators to be around three hundred thousand ish and now the validator sizes has grown tremendously so we're reviewing all the sizes again reviewing all of that uses again and then last but not least we have a few new hires James which is on this call and Jim is working on the front end UI with us and then Zahoor which someone you just met already as always working more on the political and the and the research from what with us and that's it thank you

**Danny** 

in turn see also had kind of an over packing attestation side too and and that went on to release last week

**Terence**

yes that it

**Danny** 

so if we look at mainnet we should between Teku and Prysm would likely see
many much fewer one twenty eight blocks I guess over the next month and have certainly after Prater because everyone would have upgraded

**Terence**

yeah yeah that's right

**Danny**

okay cool

**Adrian** 

Actually I do have a little tool that's been monitoring redundant attestations in the node it could use some cleaning up but it's
it happily logs each time a new block comes in with a redundant attestation and it does a pretty good job of protecting
it's kind of scary how often they come out but hopefully we'll get we use that to see it go down a bit more accurately than just at the state capitol

**Danny**

yeah I imagine we're over two thirds on redundant that decision box right now
before the upgrades kind of ripple outward

**Adrian** 

yeah most blocks seem to have some redundancy 
it's usually one of a couple of electing out of attestations in there 
it could be worse but every now and then you kind of just see a whole bunch go by and look at numbers to be deeply because it doesn't login to a database at this conference the
still useful


# 3. Merge discussion

**Danny** 

okay moving on Merge discussion I just wanna let you know that later today I will be working on a document to help coordinates
our initial targets for Dev nets between consensus and execution for merge dev nets in October and I will share that with you all today so that we can begin to be on the same page and kind of have a target for that
in other news there was the continuation of the engine API discussion this morning led by Mikhail you can see his latest doc has all of the latest and greatest although I'm sure of it came out of the conversation changes that might ripple through their there's like a a core set a minimal set of this that will be targeted for the initial wave of dev nets and we will make that clear
other merge related discussions for today

**Mikhail**  

I'd like to share a couple things Dmitry from TX/RX started to work on test vectors for the Merge part of beacon spec.
this work has been initiated by proto during Rayonism so Dmitrys goal is to add more test vectors for methods that are not yet covered by tests and also some code branch that coverage that already has unit tests our data would say next week
for it's been ready     

**Danny**

are these unit test of some of those smaller functions are these like consensus test vectors that would be released to clients or both

**Mikhail** 

yeah the goal is to have the consensus test vectors could be released yet but will be with the stock execution engine
it could be could be like at yeah it could be just adopted by consensus clients without any other external dependencies
now the other one is first PR drop it here which propose to use the
RANDAO mix for the previous slots instead of a RANDAO mix of the current slot as a random value that is passed through execution client and eventually put it into the execution payload there is the original in the PR and the discussion related to this so

**Danny**

right another point so I at least put something of an argument against it I think I've softened up and and now in favor the PR and another
points in favor of the PR is an earlier design goal which was to be able to rip the execution layer out into an independent shard if if we wanted to and the lagging of the randomness that's embedded in their would also help enable local

**Mikhail**

no yeah that's interesting yeah like the initial goal was to one of the goals is to like make it future can make this design feature compatible with proposer and validator separation
without making it too complicated to and for builders and proposers that to to be on the same set of data that are required for building the payloads like if we use the current RANDAO mix and the proposer will have to communicate these RANDAO mix upon receiving the parent block at through some channel to all block builders and actually it means that anywhere ____ random field in advance well so this kind of stuff is like one of the reasons for this pr

**Danny** 

I'll catch up on the thread I just know this is a bunch of comments and try to get that through soon
thank you Mikhail any other merger related discussions for today
great

# 4. Research updates

any general research indicates got it

# 5. Spec discussion/Open Discussion/Closing Remarks

any other discussions for today speculated open discussion in closing remarks
and 

**Mikhail** 

I have like a small question how do you want to proceed with the engine API stuff
do you want to make another call?

**Danny**

I'm a bit resistance to doing another hour call we walk through it I think instead it might make sense for this to go into 
maybe the execution API's Repo or an independent repo where we can probably do a P. R. per set of methods and take some discussion there and just start hammering out yeah the repo will allow more people to engage with it too

**Mikhail**

right and it also makes sense to crystallize the minimal set up methods to be implemented for the merge interop stuff

**Danny**

yeah I mean ideally a week from now you know we have something in a repo that we can point to and even if it still might be interacted on people can begin to to work on some implementations
do we want I know a couple of months ago we thought the execution API's under different names space would be the appropriate place is that where you're thinking

**Mikhail**

yeah probably number so this doc yeah I was like looking at the RPC stuff the execution API is there and it's just pure specification without any additional comments on that so I don't think about it

**Danny**

sure Lightclient is here think he's he's one of the gatekeepers is that still make sense for the engine API to live there

**Lightclient**

I definitely think the ultimate goal is to have it specified in the repo but you know like Mikhail it is just a JSON spec and so as some of the work is still going into
deciding exactly what these are named, exactly what they look like it might make sense to open an issue in the repo or keep working against the HackMd
until we get it to the place where once we finalize and then we can convert it to the schema

**Danny**

okay I'm a bit hesitant to leave it in the HackMd doc just because from prior experience there's just like a lack of depth on how people can engage with that

**Lightclient**

so how do you feel about an issue issue

**Mikhail**

okay yeah I agree also yeah the HackMd is difficult to follow any updated

**Danny**

if it's an issue well again I would probably argue moving towards code towards something that you can follow the a dif on sooner or later but if it's an issue it open like three issues for each subset of engine API so that conversation can be
a split up of it anything else you would like to discuss debate or ruminate on today
great let's plan on picking fork epoch for Altair in two weeks time and doing a lot of testing analysis between now and then so that we can confidently move forward on that and like I said I'll come to share a document with you all later today about
the beginnings of coordinating on the next wave of dev nets for the merge
thanks everyone thought you'll soon

## Date and Time for the next meeting : Thursday September 23 at 14:00 GMT

## Attendees
* Paritosh
* Danny
* Mehdi Zerouali
* Ben Edgington
* Lightclient
* Paul Hauner
* Protolambda
* Lakshman Sankar
* Dankrad Feist
* Adrian Sutton
* Saulius
* Lion
* Mikhail Kalinin
* Cayman Nava
* Carl Beekhuizen
* Micah Zoltu
* Terence
* Pooja
* Zachary Kardjov
* Leo BSC
* Hsiao-Wei Wang
* He, James
* Mamy
* Trenton Van Epps
* Alex Stokes
* zayd
* Ansgar Deitrichs
* Zahoor(Prysm)

## Links discussed in the call (zoom chat)
From danny to Everyone: 03:06 PM
: https://prater.beaconcha.in
https://github.com/eth2-clients/eth2-networks/issues/59

From Adrian Sutton to Everyone: 03:24 PM
: https://github.com/ajsutton/validator-monitor 
for anyone interested in the redundant attestation detector. I’m thinking there’s probably a few bad behaviors it could detect over time.

From Mikhail Kalinin to Everyone: 03:26 PM
: https://github.com/ethereum/consensus-specs/pull/2581


