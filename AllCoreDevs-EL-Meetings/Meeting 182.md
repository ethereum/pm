# Execution Layer Meeting 182 [2024-02-29]
### Meeting Date/Time: Feb 29, 2024, 14:00-15:30 UTC
### Meeting Duration: 99 Mins
#### Moderator: Danny Ryan
###  [GitHub Agenda]( https://github.com/ethereum/pm/issues/961)
### [Audio Video of the Meeting](https://www.youtube.com/watch?v=4ioJwNPe6RU) 
### Meeting Notes: Meenakshi Singh

## Summary
	


| S.NO:  | Agenda Items| Summary|
| -------- | --------|--------|
| 182.1|Dencun Updates|The team discussed retiring Devnet 12, a dedicated test network launched in November for testing Dencun upgrade implementations.Developers agreed to shut down Devnet 12 shortly after the Dencun upgrade goes live on Ethereum mainnet.|
| 182.2| Retroactive EIPs|[**EIP 7610**](https://ethereum-magicians.org/t/eip-7610-revert-creation-in-case-of-non-empty-storage/18452) extends a rule restricting smart contract creation to addresses with pre-existing storage. [**EIP 7523**](https://eips.ethereum.org/EIPS/eip-7523) will be analyzed further to ensure no impact on accounts across Ethereum networks (mainnet or testnet).|
| 182.3| [Prague/Electra EL Proposals](https://ethereum-magicians.org/t/prague-electra-network-upgrade-meta-thread/16809?)| Developers did not reach a consensus on these three EIPs and will continue discussing them in the coming weeks.|
| 182.4| Engine API & JSON RPC changes [context](https://github.com/ethereum/pm/issues/961#issuecomment-1968670529)| Due to time constraints, a detailed review of these changes will occur during the next ACD call.|
| 182.5     | Light Clients Breakout Room [#971](https://github.com/ethereum/pm/issues/971)|A dedicated meeting on March 6 will discuss the light client roadmap for the Pectra upgrade. Van der Wijden is preparing a formal EIP for the new version|

___


 ## Dencun Updates
    
**Danny** [5:14](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=314s): Let's go for it. This is the execution layer meeting 182. That's issue 961 in the PM repo. We'll spend as much time as we need on Dencun as that's coming up. We have a couple of touch points on these retroactive EIPs. I think there was some diligence that people wanted to do before they were put in. Then moving on to a number of Prague Electra EL proposals. A quick discussion around in Engine API, Jason RPC changes from Mikhail and then note about Light Clients Breakout Room on the six. Okay well we have an upgrade coming hard fork coming Dencun. There is a blog post out on the Fierceburg's blog with all the latest releases. I believe if you do have updates let us know. We'll get it in there I've also seen on release newsletters and things from client teams information coming  out that way so great. Are there any other updates related to testing, related to releases, related to anything unexpected. Barnabas?


**Barnabas** [6:55](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=415s): Yep. So I can conclude what happened with the mainnet Shadow Fork last week. We tried to run with everyone's latest release. There was a couple of clients that had an RC release that have since made a release. During the test we did a different kind of spam transactions and everything was handled very well. We had very close to 100% participation but the machines are very much overpowered. So each of them had 64 gigs of RAM and of CPU overhead just to be able to run them in that we had to choose bigger instances. 

**Danny** [7:43](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=463s): Was that across the board on a particular client combo that required 64 gigs or is that just firmly to Get. 

**Barnabas** [7:53](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=473s): So the primary reason is the disk requirement. So in order to get 1.5 teraByte of disk we had to pick up bigger instance. That's why we just had a few nodes with very big CPU annoy.


**Danny** [8:10](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=490s): Gota any questions about the Mainnet Shadow Fork? Cool.

**Barnabas** [8:27](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=507s): There's one more thing I would like to mention that Goerly is going to be deprecated very soon or it's already deprecated but it's going to be shut down and client make their exits three months after the Dencun activation or one month after the Dencun mainnet activation whichever comes later that was the sentence we put out in the blog post. So the Goerly Fork was on the 17th  January and Mainnet Fork will be on the 13th of March. Which means Goerly is going to pretty much die on the 17th April. So everybody has a date in mind now. 

**Danny** [9:12](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=552s):  And is it I'm looking at it right now it seems to have participation on the order of like 70%. So fluctuating right around the finality threshold. Did it did people already begin exiting or turning their machines
Off normal?


**Barnabas** [9:26](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=566s):  We have seen some large mod operators that have decided to exit their Validators and this caused some finality issues last night starting from last night. They seem to have recovered since then but yeah the participation rate is still quite low. I do not expect it to even last till the 17th of April to be honest but let's try. 

**Danny** [9:53](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=593s): And something interesting to watch nonetheless. And that we kind of floating that. Thank you. Other Dencun related items?

**Barnabas** [10:09](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=609s): We could possibly also discuss devnet 12. And when we want to shut it off maybe a few days after mainnet Fork.

**Danny** [10:23](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=623s):  Is anyone using devet 12? 

**Barnabas** [10:28](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=628s):  It's basically just still place where we can quickly roll out some new client releases if anyone needs to test something. So it's nice to have around.

**Danny** [10:36](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=636s): Gotcha yeah deprecation after soon after mainnet that sounds great. Yeah just I'll Echo Justin's comment just overpowered machine seems like a repeat of mistake we made on Paris. Can we kick around with some ideas to in subsequent versions of this type of testing get to more types of resource machines that we'd expect. Obviously there are probably extremely high powerered resource machines on the network but seeing some sort of distribution there might be good. Is that because of the cloud info that we're using? 




**Barnabas** [11:14](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=674s): Yeah so the cloud infra basically offers us two different options. If you want NBME we have to go with a bigger machine. They don't offer large disc low CPU and low machines. Alternatively what we could do is attach volumes to the different machines and think that way but it's possible that the iops of those mounted volumes are not high enough for me not to be able to sync. It's something we are testing right now and possibly we could encounter going forward in the future mainnet Shadow Forks.

**Danny** [11:56](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=716s): Right okay. Yeah it's definitely worth investigating something here and we can pick it up down. Anything else related to the upcoming upgrade? Cool. Well in +2 weeks it will have happened. So we can talk about it then and of course in one week there's anything else to discuss we'll discuss it then. Thank you everyone. 

## "Retroactive" EIPs. EIP-7610
**Danny** [12:41](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=761s): Okay there are a couple of retroactive EIPs that were discussed two weeks ago. Let me look at my notes. I believe 7610. There was going to be an investigation just to sanity check. There' be no verkle issues. Did anyone look into that? This is Revert Creation in case of non-empty storage.

**Gary Rong** [13:08](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=788s): I think the Blocker of this is this EIP is whenever we switch to verkle there is no easy way to determ if the account has the empty storage or not and Martin has this idea that actually we can. So whenever we switch to the verkle and the doing the transaction we can whenever we encounter a account has zero nonce empty runtime code and non-empty storage. We can just discard the storage which means we will not move the leftover storage from the Merkle to verkle and in this way after the transition we can make sure that in the extreme state this kind of accounts will no longer exist. And we can then deprecate this the idea is that because for this storage it is impossible to access them. And also impossible to modify them because of the empty runtime code. So it is totally safe to discard them. And also for this account they all have nonzero balance. So they will still be kept in the state even after discarding the storage. So if we discard the storage then it will not be a blocker for verkle. So maybe Guillaume you have something to add or want to mention.


**Guillaume** [14:48](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=888s): Not really yeah whatever  it seems like it will deactivate itself. And it's not going to temper or destroy anything during the transition or impact anything during the transition. So I think this is the right approach.

**Danny** [15:11](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=s):  Danno?

**Danno** [15:13](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=913s): Have they taken the potential of EIP 5806? I mean it's not committed. Yet but it's on the table. And that's where you can do a delegate transaction from EOA. EOAs might gain storage, how would that interact with that? We might not do the EIP but it's something that's been discussed in the EOA circles.


**Guillaume** [15:33](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=933s): So I don't know if Adrian is here but if he's not I can just add that I've been thinking about that as well. So what my understanding is that those accounts have no code so you cannot delegate call them and they were created as the result of a contract so there's no private key controlling them. So you cannot use EIP 5806. Yeah they are not affecting 5806 at least. That's my point of view.

**Danno** [16:19](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=979s): But 5806 would be fine for verkle if we put if regular end user accounts gain storage.


**Guillaume** [16:28](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=988s): Right you mean in that sense yeah I mean regular end user would gain storage. Yes, but so you would not be able to create oh yeah you should be able to create a contract to deploy code at this time right. This is exactly what Gary was saying: we forbid this all the way to verkle.

**Danno** [17:05](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=1025s):  I'll follow up on Eth magicians or somewhere I'm still a little concerned.

**Danny** [17:13](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=1033s):  Okay so there might be a couple more things to talk about here. If those are resolved then the intention is to add this to pectra and with a note that in the event of verkle it's deprecated or it would be an additional EIP at the point in verkle to deprecate. Or does it auto deprecate can someone
Clarify.


**Guillaume** [17:39](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=1059s): In its current definition it's Auto deprecate yes. 


**Danny** [17:45](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=1065s):  Got it. Okay so it seems like there's at least a couple things that people want to still mull over. This will likely show up again in +2 weeks to just bad around those hopefully final couple of issues.

### EIP-7523


**Danny** [18:03](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=1083s): Okay the next one was 7523 which I believe there wanted to be a final validation that there were no more empty counts on Mainnet because I think there was some unexpected ones found. Previously that were handled but just a final check. Didn't anyone do that final check? I'm also not 100% sure who was going to do that? Okay we'll kick this two weeks Tim will be able to carry the thread better than I apologies. 


## Prague/Electra EL Proposals – Future EOA/AA Breakout Room #962 recap


**Danny** [18:54](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=1134s): All right. On to Prague Electra there was and account of traction future of EOA/AA breakout room yesterday I think there's two things that we want to touch on here one is if one or maybe two people can give a recap if one person gives a recap and if anyone wants to fill in the gaps that'd be great. Also Vub was not able to join the call yesterday. So if Vub can help give some additional context on 4337 or I can't remember the number but the native version of that and open up any followup questions from yesterday's discussion that'd be great. So let's start with that recap. Does anybody want to take that?

**Vub** [19:38](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=1178s): Yeah I can just start by summarizing some of what I think one of the big topics then was just making sure we were aligned on longer term goals of account abstraction. Basically like the longer term just fundamental desire that at eventually we have to have some kind of account system that is like one allows key rotations and key deprecations two allows Quantum resistance three allows batching and look for allows us allows sponsor transactions. And a couple of other smaller things and out of those of course the first two goals are like very clearly not satisfiable with EOAs. And so present a pretty clear case for moving the ecosystem to a place where it's beyond EOA Centric but then this brought the discussion to what are actually the means to get there and like what are some of the specific details that are less resolved here. And like what actually is a shorter term road map that is like gets us goals that people want in the short term. But it is at the same time compatible with this longer term future.  So like one of the question is basically know like trade offs between like 2938 style design and for 4337 style design questions around like short-term trade-offs between 3074. And I think it was 5806 which is basically EOA being able to delegate call us. From my inside of a transaction and like which would essentially let them execute code So I don't think we came to particular conclusions on that. Though I think there's a general agreement that the longer term stuff is something where there's a lot some kind of medium urgent need to try to like actually align on that and sort of figure out the remaining dis alignments. And then at the same time for kind of there is this short term need to improve functionality for existing users. And that's something that has more urgency because there's upcoming hard Forks. So I'm going to let other people continue from there.


**Danny** [22:53](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=1373s): Yeah before we move on to Andrew. Does anybody else want to add unless Andrew you want to add a bit more to the recap or provide any sort of competing view on what went down yesterday
Andrew.




**Andrew** [23:03](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=1383s): If somebody wants to add something to the recap please go on.

**Danny** [23:15](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=1395s): Yeah go for it Andrew. Thanks.

**Andrew** [23:18](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=1398s): Okay. Yeah. I was thinking about because my worry about EIP 3074 is that if you just use you can sign a blank cheque forever. But then I think it was that concern was addressed recently. And now it's it's revokable so and and light client during the breakout light client raised an issue like raised a question that if we want to do something in the short run then between 3074 and the delegate transaction 5806 we should choose 3074 because it's more generic it allows sponsored transactions. So I kind of think if we make if we consider 3074 for Prague and if we have confidence then it doesn't prevent us from the end game Vitality talked about then if we have and the 3074 is a reasonably complex proposal but it's also it will bring substantial benefits. So yeah if if there is confidence then it will not break things in the future or like prevent things in the future I think we should do it in Prague or at least consider it for inclusion.


**Danny** [24:54](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=1494s): Right vitality l do you have a response to that before we move on to Ahmad. 

**Vub** [24.57](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=1497s): Yeah. No I think that's  one good set of thing like yeah the security concern issue is definitely one of the big sticking points. And I think it's good that we're talking about and have made a lot of progress. I think the other one that I feel like has been brought up less is basically that like one thing that would be good to avoid is essentially creating two totally separate developer ecosystems for smart constract wallets and for EOAs and like 3074 bytes like the opcode is fair in its current form fairly EOA specific. And like I looked at it yesterday and it feels like there's a pretty natural path to eventually extending it to be smart contract focused as well. But then there's basically the long-term issue then which is like five or 10 years from now. There's going to be a lot of applications that have this like extra entrenched workflow where things happen using the AUTH opcode and are we like does it feel right to have that to have that kind of workflow just continue to exist. And be part of the EVM in the long term right. Basically a long-term complexity concern and then there is it's like not an argument against 3074 but just like a thing that needs to be kept in mind which is like the POS the question of whether or not it should be extended to also cover smart contract wallets at some point.




**Ahmad** [26:50](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=1610s):  Yeah so just one thing that I think wasn't clear from the last call. I think there was a notion that in the call that EOAs are not to be continue with to be supported kind of. And I feel like this is not the way to go. This is something I wrote in the comments but I wanted to voice it clearly that I believe that EOA needs to be supported up until smart contract account are properly usable. And right now we're not there we need to if we need to keep supporting EOAs and making their user experience better until smart contract accounts catch up to become user normal user usable. That's just what I want it. 


**Vub** [27:57](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=1677s):  Yeah I mean I think there's a lot of support for that and I think like that's exactly why both 3084 and 5806 are being discussed and then I think one other thing that's and that's short term right I think one other thing that's important for just people listening to this to keep in mind is that in the long term you know like Besu if there is an endgame where like literally always get removed as a protocol future then like that does not that will not mean any kind of you know like forced wallet change for users right like if that gets done the way that that would have to get done is basically that the EOAs would get automatically replaced by smart contract wallets that have equivalent functionality. 


**Arik Galansky** [28:54](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=1734s): Thank you so yeah I think yesterday was a very interesting conversation. And a lot of good concerns came up. Coming from the wallet side I think one of the important things for us to say is that sponsored transactions is a very important Capability. And for us at least this is one of the big differentiating factors between 3074 and  5806. Although they both bring value. But I think so kind of one of the main things that came up yesterday is how could we possibly align the road map between 3074 and 4337. We've been thinking about this today we came up with some suggestions. I'm not sure they're by definition the solution but it does feel like there could be like vitalic mentioned there could be good alignment between 3074 and 4337. If we make the effort to make this alignment. And so that makes me a lot more positive about this.


**Danny** [29:58](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=1798s): A couple more comments and then I want to give some time to talk Ansgar and then Dror.

**Andrew** [30:05](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=1805s): Yeah I just wanted to briefly mention that back when we kind of first talked about 3074 three years ago. That and some of course we kind of gave a pushing for it but basically this kind of forward compatibility with smart contact worlds was kind of the last thing. We did think about and we basically were thinking back then that we could have invok has become the de facto standards for new features across smart contract wallets and in EOAs so basically like say if there's a batching invoker right for Bing multiple transactions. Then that could also we can structure it in a way where that same invoke can also be used my contract wallets. But that does mean I mean thetic already kind of touched on it a little bit that we would have to be okay with the future where for all of these features forever. We are fine with smart contract wallets having to make this extra call to the specific invoker. That then does that for them or something. It does not necessarily like a very natural flow like it basically it adds extra overhead forever to the Smart contract wallets. And it's very opinionated on that side but it does give us this kind of interoperability and it does kind of keep us from fracturing these two paths. So if we want to go with 3074. I think it should really come with the understanding that that would mean on the smart contract quality side we also start using invoke us for standardisation for the of these features. 

**Danny** [31:28](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=1888s):  Dror did you have anything to add before we give you off a minute. NO. 

**Vub** [31:36](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=1896s):  I did not.

**Danny** [31:37](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=1897s):  Yeah okay. I just want to give you a chance to add some more context around both 4337 as well as the native version and where you see this fitting into either the short or even the the longterm in game of account of protraction. Yoav?


**Yoav** [31:58](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=1918s): Sure. So yeah I'll give overview for those are not familiar and then we can talk about what we can do now. So can I share my screen? Okay so first I what we're trying to build in the long term is Full Account Abstraction. And so what are we what are we actually trying to to abstract sometimes in the in some conversations. It's not clear to everyone. So our definition is we abstract all the aspects of the account which means the authentication meaning proving who you are baring your identity to the account. Then we have a authorization which is something that usually there's a separation in in every security system except the blockchain there is a separation between authentication authorization like who you are and what are you allowed to do. So in EOA this is implicit if you have the if you prove that you are the owner you can do anything otherwise you cannot do anything. So it's authorization we have a replay protection we want to enable like a parallel transactions when the order doesn't matter for example. And we have in some multitenant used cases. There is a gas payment of course. We want to be able to pay with LC20 you want to do gas sponsorship. This is a very popular feature. And which is execution abstraction which means allowing things like like batching and like batching delegation that's the kind of thing that 3074 for example does. So we want to obstruct all of these. Problem is that this is a hard problem because we have to you I mean doing State dependent validation means that there are many ways to invalidate to do mass invalidation. And therefore to do denial of service attacks against the system. And the easiest way to solve it of course is by using a centralized relay. But that's not what we're here for. So instead we need to have a complex mempool protection, something that allows us to have a permissionless mempool. And the first meaningful work in this space was 2938 which really paved the way to this line of thinking. And we learned a lot from it. But we also notice that when it hit a certain dead end because some basic account obstruction features are broken by requiring the AA prefix which is really a must if you don't have this protection then block Builders can be easily attacked by transactions that invalidate each other. And the validation rules are also far more restrictive than in more recent proposals which actually preclude most of the most of the used cases that we're already seeing live in some 4337 accounts. So the goal ERC 4337 and later RIP 7560 is to solve this problem. And it does so by separating validation execution. So that and since we have a separate validation stage. We can avoid many of the do vectors without being too restrictive. So 4337 was never meant to be enshrined. It's an ERC. It's me, it's meant to be the test, it's an experimental. It allows us to experiment with Count abstruction of different EVM chains without having to reach consensus on how a count abstraction works. And the focus is decentralisation. So there are no centralized components anywhere in the system and of course it has some limitations because it's not native. It's less gas efficient. We have to waste some gas on some on overhead that could have been avoided with the native Construction. It cannot migrate EOA existing EOA. It cannot add code. So we'll need a separate EIP for that and there are already a few good proposals. And one big one big issue since who really care about censorship resistance is that it's harder to support with inclusion list if the protocol is not aware of this. So ERC 4337 is launched actually here at East Denver exactly one year ago and since then it's been getting some nice truction. Last time I checked there were 3 million deployed accounts like 11 or 12, actually 12 million userOps. And we see many many great projects, many new wallets being built, many projects that use it. So it's an interesting experiment to work on. Now what is the RIP 7560? This one is a bit seems like an odd animal because it's not meant for we are not fully sure yet about how account abstraction should work at a protocol level and yet we went ahead and wrote it. So why did we do that? Turns out that some layer 2’s were not willing to wait and actually wanted to have native account abstraction already. For example zkSync had it from day one stocknet also did. And the problem is that each of these they all took ERC 4337 but they created an enshrined version of fit in different ways which first of all caused a lot of wallet fragmentation. Suddenly you have wallets like Argent that only support one chain and you cannot use the same wallet on any other which is of course not great for users. And in some cases it introduced attack vectors because we did spend a lot of time on a lot of time on preventing the deneb service vectors and not everyone is and not everyone identifies every such case. So the solution we came up with is to standardize like to have a standard
version that all layer 2s can use. And then wallets only have to be written once and can work anywhere and we can help ensure that it's secure. So in short it's something that's going to happen with or without us. So we may as well help them get it right. Now it's going to be ERC 4337 compatible. So on chains that choose not to implement this RIP or on mainnet. You can use the same account. You'll be able to switch to use to deploy the same account on a different network. In some cases it will work more efficiently with the RIP in others it will use the ERC. And this is all still early work. So it's work in progress and we are seeking feedback
from core devs and from Layer 2s. We are getting a lot of great feedback. Now all of this I think is out of scope for the current discussion because right now we're talking about what can we do for the next Fork? How can we improve things and there is strong demand for some EOA improvements. The most common requirement I've seen is batching in order to remove things like the approve and transfer from flow. So that's something that I think is worth addressing. And there's also things like gas abstraction which is actually much hardle to do in a decentralized way but it's also something that there is a strong demand and we should be thinking about. So I think that in this context it's a I mean if we ignore the really hard stuff like validation because that's where all that's where all those vectors lie. So if we ignore it and we only focus on these two then we right now we have these options we're discussing. The 3074 route and the 5806. So I'm trying to look at them and I mean what do they give us and what risks do we take. And so as I said the most common case is batching and with batching both of them can support batching although I think that the latter is more is a more natural way to support batching because with 3074 if you have a batching invoker the transaction actually has to contain two signatures. You have a signature for the EOA transaction and and the signature for the off and then there's the and also the commit that is a part of the transaction. So the transaction becomes bigger which may be a cost issue on on rollups. But more importantly who is going to sign these two transaction these are two signatures. It's not reasonable to ask the user to sign the batch twice in order to submit it. So it's more likely that it will be used with a relay, like a centralized relay is going to sign the transaction and it has to be centralized because otherwise there are easy ways to grief it. So it's it will have to be permissioned in some way. And then the relay submits the transaction submits the batch on your behalf with the 5806 it works. It works naturally just you just delegate this. I see this EIP as a way to run a script in your account. So the user just signs the normal transaction only once. And it runs the script that does batching Gass sponsorship 
is something that 3074 can do natively. Unlike 5806. 


**Danny** [42:48](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=2568s): Real quick on the batch call Can 3074 be used trustless with 4337 or does that they had with each other. 

**Yoav** [42:58](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=2578s): No it can be. So I wrote a post about the Synergy between 3024 and 4037. They are not mutually exclusive in any way and that's actually that's important something I should have said earlier that we need to make sure that no proposals we introduce now. No count EIPs make it make it hard for us to do a count of suction later. And both of these EIPs are fine in that sense. There are not nothing here preclude us from doing a count abstraction later. So you can use an ERC 4337 account on top of it in order to do batching but then you're basically using 4337.  you're just using a you're using an invoker but it's still going to be a 4337. If you just want to do batching like you know you have an EOA you don't want it to become a 4337 account you just want to send a batch. Most likely you're going to use a relay because it's not reasonable to ask users to sign twice. Does it make sense?


**Danny** [44:04](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=2644s):  Got it.


**Lightclient** [44:06](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=2646s):  Okay so but you can use 3074 with 4337. So it's not centralized gas sponsorship.


**Yoav** [44:14](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=2654s): I'm actually I'm not sure. Other than making it a full 4337 account. Which means you are no longer using it as an EOA. I'm not really sure how you're going to use it for batching. I mean if you have an EOA and you're using a 4337 you want to do batching, what does it look like.

**Lightclient** [44:38](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=2678s): I mean does the invoker not just Implement the interface of a 4337 wallet.

**Yoav** [44:46](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=2686s):  Yeah you could delegate to an invoker that is essentially like that but it's yeah I need to think about it some more but it's I remember when I thought about it's not as trivial as it may sound but it may be possible to do that.

**Ansgar** [45:07](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=2707s): Well you couldn't have a decent mempool then basically right. So you're still in the same position that you have
just pointed out even if you did have the same onchain logic you'd basically have to also replicate the same mempool Logic for these otherwise same problem not decentralized.  


**Ahmad** [45:26](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=2726s): Why I would like to address two things that I noticed on the table first batch call I think the signatures can be aggregated by the wallet. So instead of having the user sign multiple times. The wallet can make the user press a single button to Aggregate and sign all of the all of the signatures at once. That's one thing the second thing is.


**Yoav** [45:54](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=2754s):  Wait how it's two one has to be a signature on the commit on the off commit and the other one is a transaction signature it's not even the same signature format.

**Ahmad** [46:06](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=2766s): Sir I understand but the wallet can take care of that.

**Yoav** [46:11](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=2771s):  But the user let's say you are using a ledger using a hardware wallet you will be prompted to sign twice on your Ledger right.

**Ahmad** [46:20](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=2780s): I mean The Ledger needs to start upping their like instead of like when you're pushing this to ledger to sign. There needs Ledger needs to support this new approach and it needs to or it will fall behind like instead of having to press multiple times approve on Ledger. Ledger needs to batch this information in a single go and have you sign the whole thing in one go or what's the point. That's one thing. The other thing that I wanted to say about this table is the authorization is irrevocable and replayable which is not true with the nonce suggestion that is going to be applied soon.




**Yoav** [47:08](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=2828s): Yeah we can get to that in a minute but regarding batching. I think what you're proposing is not that ledger will support 3074 in general. Because it's hard to do it generally when you don't know about Invokers. It means that ledger needs to be aware of a specific batching invoker because it needs to show the user what I mean, what are you signing. So it's okay it's okay if Ledger prompts the user to sign only once and actually produces two signatures. If it knows what it's what it's signing what to present to the user I'm not sure that every Hardware wallet will want to do that but maybe they will. It's definitely worth exploring. So regarding a revocation yes it's a if we are if it's only valid for the next nonce which is what Matt just proposed in the chat earlier. Then it is much easier to revoke all authorizations by just signing but just submitting one EOA transaction. Of course there are some downsides but it does solve this problem. It's replayable and that's actually a feature not a bug in the 3074 before design. Some use cases you want them to be replayable but as soon but it is revocable so that's H so that's correct and it's and in 5806 it's One Time by definition for better or worse. It's just you know just a transaction. So you have no way of making it replayable whether you want it or not and it's and you don't have anything to revoke because it's a transaction now gas sponsorship is something that can 3074 solves natively but again requires using a
centralized relay because it's really hard to do it in a way that cannot be where the relay cannot be graced. So it will require a lot of design and with 5806 doesn't allow Gas sponsorship in Itself. So it would need it would need the new EIP draft we've seen the 7949 which adds gas sponsorship but it would need since it's a transaction type it means that it would actually have to be merged into a 5806 which adds some complexity but can but then it will be able to have gas abstraction as well. So now there's another use case that people like to talk about is of course account recovery. Now recovery can be the case of lost keys or stolen keys and 3074 does give us a way to recover from a lost key disaster. If my key got destroyed I can have if I signed an invoker that can move the assets out of my account. I'll be able to do that as long as I haven't used the the next nonce. If I'm going to use the EOA as an EOA and send a transaction from it then of course it's going to break this lost key recovery.  5806 does not enable any form of lost key recovery but none of the proposals solve the case of a stolen key or in some cases you don't even know whether I mean you no longer have the key and you don't know whether someone has access to it or not. So this one requires full account abstraction. There's no way to solve it by improving EOA. Now something I don't pay attention to is the principle of least astonishment. It's a principle in user experience where you want to make things as intuitive as possible to the user. And since I'm looking at delegation which both proposals do as a way to run a script in your account then what 3074 ask the user to do is to sign an authorization to authorize a script to run anytime in the future or now any time in the future as long as you haven't sent a transaction from the EOA which burns the nonce. So that's and the 5806 means just I want to run this script in my account right now. I'm going to send a transaction that runs the script and I think that the later is much easier for users to grasp than the formal where you are saying I'm allowing this script to run in my account now or in the future as long as they don't say otherwise. It's a bit I think it can surprise users in some way. Now there's another thing complexity and I think that on all Core devs we often only look at the complexity of the client itself which makes sense since I mean if that's what you're building you want it to be simple but I think that we have to look at the total the entire system. The complexity like in 3074 the implementation is really simple which is great. It's much better for the network but it does add complexity in other components for example wallets will have to White list. We'll have to White list certain invokers. These invokers are not. I mean every wallet will have to audit, decide which invoker it support and keep maintaining this list whereas I think with 5806 because there is no future exposure it's much easier to it's much easier you don't need to maintain this white List thing. Anyway that's the I think both proposals can add a lot of benefit to add a lot of benefit to EOAs. So does anyone has any questions about what we talked here? No one?


**Danny** [53:39](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=3219s):  Yeah  any other comments for Yoav? Tere's a lot in the chat does anybody want to represent anything from there? 

**Yoav** [53:46](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=3226s):  Oh okay I'll have to stop sharing and then I'll see.

**Andrew** [53:53](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=3233s): Yeah I just had a thought so in EIP 3074 it says that a precompile was considered initially but that as a means to prevent replay or what not but it was decided against because there is no precedent of 
precompile with storage. But I think in Cancun oh sorry not in cancun in Prague EIP 7002 actually introduces a stateful precompile. So I was thinking if we actually entertain this idea of a state for precompile. Can it replace invokers. 


**Danny** [54:41](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=3281s): Just real quick 7002 is going to be migrated to look more like the beacon route opcode EIP such that it would be a a predeployment essential a smart contract. 

**Andrew** [54:56](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=3296s):  Okay so it won't be a state precompile. I see but but say like the concern is that we that's that that smart wallets have to white list invokers so can 3074 be redesigned perhaps with a state for precompile. So that we don't like we have a kind of a standard invoker or maybe there is no need for an Envoker at all.

**Danny** [55:30](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=3330s): Lightclient or anyone an author on that one want to take that. 

**Lightclient** [55:34](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=3334s): Yeah I mean it's definitely a possible Avenue and if that's the only way that we can improve EOAs. Maybe it's something to discuss but I think it just goes against my philosophy and probably some other people's philosophy about what we're trying to provide to developers which is a powerful framework for building applications. If we have a pre deployment which is the only context that Auth and Authcall are available to be used and it's something that the All Core devs group is dictating then I think that we're going to miss out on some Innovation that could happen at this layer but again like if that's what we have to do then maybe that's what we have to do I just personally don't think that's the best path to go down for 3074. 


**Gary** [56:22](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=3382s): Yeah I'm wondering since Yoav didn't really speak to 7377. It seems to me that 7377 is a much lighter touch approach for enabling account abstraction and kind of getting users from EOAs to a Smart contract account abstraction future. It allows you know 4337 can develop in parallel and this doesn't have to be enshrined early. It's what we're trying to Target for Prague is light fork and it seems to me that at least 3074 and 5003. In combo would create a lot of test and kind of attack surface that. We need to be careful about that and that's starts to grow the fork starts to grow the prague fork. It seems like in my opinion 7377 is really the aproach that is light touch enough and still future forward but also includable in Prague without making this into a larger feature Fork that is kind of against the principles were set out for having a small feature for before verkle.

**Yoav** [57:37](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=3457s):  Yeah. So I agree this is something that is isogonal to the other two proposals maybe I should have talked about it separately. And it's because 4337 or even 7560 currently don't talk about migrating an existing EA and adding code to it. And the end game for account abstraction does require solving this problem as well. So yeah if it's possible to include an account migration EIP then then I think we should consider it.

**Guillaume** [58:14](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=3494s): I only have a side note for something that had been said before maybe if Vub wants to talk to address what Gary said he should go first. 

**Vub** [58:24](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=3504s): Yeah I mean I think just a kind of response to the general idea of like why not basically yeah give up on EOA improvements entirely and try to Fast Track making like making it easy for while existing EOS to participate in 4337. I think probably the biggest  objections to this are you one is I mean of course there's kind of like general you know like fear of new things and but that's something that's just like so continues to be being drisk with with every passing gear but another a really substantial one is higher gas costs right so 4337 does have significantly higher gas costs than EOS do and this is something that sort of some sense in principle should not be true because you could have a 4337 account that's like literally running the same workflow as in ecdsa based EOA but in practice like basically EOA gas pricing is cheaper than the storage operations that 4337 does. And I think as I mentioned in the chat the this is something that can be fixed by basically overhauling the gas cost system and replacing it with something more principled that charges for storage accesses in a neutral way. And the verkle tree EIP actually does have a component which does exactly that. So that's I mean that so that's one big thing but like the Verkle but that kind of goes against the idea of doing something gives users functionality that becomes available pretty quickly. And before virkle trees do. And then of course the other one is just like cross Layer 2 stuff right like whatever you know if L1 has amazing 4337 but like but layer 2 is did not done like that's also an issue. And like also a thing that's going to contribute to time delaying any attempts like very rapid attempts to get everyone over to Smart contracts. 


**Guillaume** [1:01:05](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=3665s): Yeah so just a side note on what you said earlier that there was another contract that was going to be deployed the 4788 I think way.  7002 yeah right exactly the the issue is this that might not be
clear to everyone but it's going to have a huge impact. Okay at least to have an impact in
Verkle mode is that if you start deploying contracts that are part of regular block execution you find yourself adding code chunks to the Witness. And so the choice actually no longer exists whether you want to use the EVM byte code compile version or if you want to take the shortcut and and go right directly into the the contracts memory. I don't think we should discuss this right now I'm just pointing out you might want to hold off your horses on this one on because I think 4788 should be I mean the contract should still exists but the execution the byte code execution should actually be removed. So that the so that the the witness get smaller.  






**Danny** [1:02:20](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=3740s): I guess I kind of see
that as a feature like when you put anything into the the EVM here then you just get you get it by default but.


**Lightclient** [1:02:31](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=3751s): It does just kind of suck to send the exact same bytes around the network every single block you know. Like if people are interacting with that contract. It makes sense but if it's something that we as developers of the protocol just sort of enshrine this shackle on our Witness. It's a little unfortunate I mean 4788 contract is 86 bytes or something so it's not a huge deal. It's just a weird thing. 


**Danny** [1:03:04](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=3784s): Sure but if you don't then you're now it just becomes an additional input to State transition right. That you have to be carrying around. That's a fun pass blocks rather than just one. 

**Lightclient** [1:03:18](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=3798s): Well it's not a function of past blocks it's just enshrined in the client like the code just lives in the Client.


**Danny** [1:03:26](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=3806s): Oh the code component. Got you.

**Lightclient** [1:03:28](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=3808s): As the binary.

**Danny** [1:03:33](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=3813s): Okay we can pick that up another time. So we are at the hour there is a desire potentially to get small versions that iterate us towards improvements here it's very unlikely that in the next Fork that we're going to hit some sort of I think it's maybe I'll change that from very unlikely to impossible to hit art kind of final account abstraction goals. I do think in the next couple of calls. We do need to hone in on if there's going to be one or two I won't even some amount of small EIPs. So we're going to have to pick up the conversation again I think also in parallel There's A Renewed Vigor to try to hone in on what does the short medium and long term look like. And to make sure that both the EIPs that we might consider today as well as we want to layer in time do help us get there so let's keep the conversation going I don't think we're  going to schedule another breakout at this point but it does seem like there might be an appetite to be regularly touching on this outside of all core devs. So  we'll we'll throw this on the agenda in plus two weeks to at least think a bit more about the strategy and and to
consider a couple of discreet EIPs. Thank you everyone,. We do have half an hour. We'll try to get to what we can. 


### EIP-7623


**Danny** [1:04:57](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=3897s): Next up was EIP 7623. Tony was going to give us a view on this increased call data cost.

**Toni** [1:06:14](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=3974s): Yeah. Hi everyone. Yeah so basically this EIP is the goal of the Reduce maximum possible blocksize by increasing the cost of Call data. And particularly for nonzero call data bytes. And it does so by increasing the cost for call data for those transaction that are mainly using ethereum for data availability. And you can look into the EIP. It has this conditional formula. So with a floor and a standard token cost and if you spend basically enough gas on EVM operations then the call data cost will be yeah it will remain at 16 gas per call data byte and otherwise it will be at 68. Yeah currently the the maximum possible block size is around 2.5 megabyte something like that. And with that EIP one could reduce it to around 0.5 megabyte. I just posted a link into the chat so you can see a lot of more details some analysis which accounts are affected. But basically normal regular users wouldn't be affected at all so they would just continue paying 16 gas per call data byte while the data availability users would pay 68 gas per call databyte. And I did some quick analysis for the last 12 days and it looks like that around 96% of the transactions would have remained unaffected which means only 4% of them would have paid the 68 gas call data. And most of them are data availability or users writing comments in their call data. And those 4% that will be affected it's basically 1% of the users. And the large chunk of them is using call data for data availability. 


**Danny** [1:08:23](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4103s): Are there any clever ways to try to get around this threshold like batching across multiple transactions or just the 21,000 hit break such strategies or are there any other things like that under consideration. 

**Toni** [1:08:41](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4121s): I've actually not
thought about batching. I don't think there should be a possibility to get around that. So the only way to get to the cheaper price would be to spend money on EVM operations which is then yeah counterintuitive. 


**Danny** [1:09:03](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4143s): Right. Ansgar? 

**Ansgar** [1:09:05](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4145s): Yeah I just want to say that I'm strongly in favour of shipping a kind of caldata price increase in general. In the next fork so that we can limit the kind of Maximum worst gas blocksize. And in this case this does this very well by really go by going don from 3 megabyte maximum to.5
megabyte which of course is a huge Improvement. And that way it would give us also room to include an EIP to increase the 4844 throughput like I think I mean ideally I don't know depending on how stable turns out after we ship dencun. Ideally I think something like 8616 or so would be a good Target which still would result in a lower maximum throughput than than we have today. I do think kind of this question around this mechanism for for basically rebating. I mean I know it's a bad word but rebating basically kind of the cost the high cost for call data if transactions also consume more normal. And gas I think it's interesting I could imagine that this is a bit more contentious so so maybe like this is in a way like an optional part of the EIP in my mind at least but it's actually a very clever mechanism and just to give a little bit more context right like so in the past we've looked into multi-dimensional resource
Pricing. And the idea is that it's kind of unfortunate that we always price things for the worst case. And the worst case is that the block only consists of a sing like only consist of using that one resource right. So basically we press compute for the worst case block processing times if you only use compute operations. And we price data for if you only have a block that's full of data and be price storage for if you only access storage like multiple times in a
row right. And the the beautiful thing here is that basically now it it still has this high price for that bad case for the attack case basically. But it gives you lower prices if you actually have a much more realistic mixed use research block and this is actually a mechanism we might be looking into applying even for other types of resource mixes as well. Basically it's a way of kind of elegantly making making the total kind of resource usage BL more efficient. So I personally like that part of the mechanism as well but I feel like basically even if people might take issue with that part I think shipping any form of call data price increases is very important for the next call. 




**Danny** [1:11:23](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4283s): Any other comments or questions I'm not sure if client teams had a chance to look at this before any initial reactions for consideration in the next fork.


**MariusVan Der Wijden** [1:11:41](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4301s): So I've implemented it in geth and it was I like a five line implementation. I did make some mistakes. Thank you vitalic for pointing them out but yeah I fixed it now. 

### EIP-2537

**Danny** [1:12:01](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4321s): Glad we have good code Readers. Any other initial reactions if not we'll probably give everyone a couple weeks to chew on it. And bring it up for more reactions in plus two weeks. Okay thank you Toni. Next on agenda Antonio did put EIP 2537 on up for discussion. I'm not certain if he had seen that it was already line for inclusion in the pneumatic EIP. Was there anything else we wanted to discuss on 2537 or was that it. 

**Danny** [1:12:54](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4374s): Actually you sound like you're in an echoey far away room but we and if you can't get the mic working is there anything else you want to discuss other than just see if it was going to be included is it 

**Antanio** [1:13:22](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4402s): Is it better Danny? Actually yeah I mean finally this this EIP seems to be like getting traction and actually I will have a some forks mean me and some other people started to look at the
at the this text more indeed. And actually I will have a question if you guys have an opinion on kind of not an issue but an implementation Choice basically like this specification is pretty different than EIP 196 in a way because like we have operation like add and scalar multiplication like the BN curve. But that dencun does is a prime order curve and this one is that is not so test Co Factor. So now while it's clear that for pairing we want to do the operation on the magic sub group the one that we are using in the consensus layer it's not clear what we want to do for the scalar multiplication and the addition for this EIP if you want to stay on the Magic's group or or acting on the full order of the curve. And if you choose to stay in the group we have to pay a bit the price of the validating the points. So this is pretty actually I've been writing start to read the test for this specification and it's not clear at all what we want to do here. And I was wondering if anyone has an opinion just like to give another perspective in the consensus layer. We don't have this issue because we are using only the BLS signature scheme but here we have as well adding points and scalar multiplication process. 

 **Danny** [1:15:19](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4519s): If no one has any comments here.  Maybe it's best to write this down and see if we can get some view on it in next couple.

**Maurius** [1:15:26](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4526s): So Antanio,  right now all of the libraries are using are doing the subgroup check right at least that's as
far as I go I saw.


**Antanio** [1:15:40](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4540s): For pairing yes for like the operation of adding and scalar multiplication not all and for sure it's not specified by the spec at the moment. But I agree with Danny that we can talk about, offline. So maybe I will open an issue on the repository. 

**Marius** [1:15:58](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4558s): Okay that' be great. Marc has his hand raised as well.

**Marc** [1:16:01](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4561s): Yeah I just wanted to add one thing on this EIP that I felt that maybe it was missing the ability to do operations in the result of the parent group. So the moment you can do operations in G1 and G2 but then you can't and you can verif the result of two pairings are equal. It doesn't let you do to get the pairing result and do further arithmetic on it which is useful. I think primarily for verifying some like aggregated Snoks. So I felt that this would be an improvement to the EIP.

**Antanio** [1:16:46](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4606s): All right yeah. I will suggest as well to maybe discuss this on the GitHub and we'll follow up there.

### EIP 5920 (PAY) and 7609 (transient storage pricing) temp check

**Danny** [1:16:57](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4617s): Okay. Yeah I think to get the right set of eyes on this a written version of it will be helpful. Thank you. Before we move on Charles wanted to bring up both EIP 5920 and EIP 7609. Both these were
discussed on a previous call but we're looking for a revised kind of temperature check. If anyone client teams had given them more thought or wanted to bring in any comments on those. So EIP 5920(PAY) is payout code. Any comments or further thoughts on that since it was brought up.

**Maurius** [1:17:42](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4662s): Yes we kind of had a team meeting with the ELs team and the east team the executable execution layer specs and the executable test. No spec tests and one of the things that we did was sit down and talk through a random EIP and we picked the pay opcode and kind of discussed all
of the all of the implications it has. And all of the context that it can be  that that we need to think about that we need to test when doing this EIP.  And it turns out it's quite complex the testing the EIP itself was underspecified. But I don't know if Peter is here but he wanted to add some more specification to the EIP. And yeah in theory I think the EIP is okay. It's just a lot of stuff to test for it.

**Danny** [1:19:06](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4746s): Okay and is Peter intend to do the revisions in a PR. Danno? 

**Danno** [1:19:19](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4759s): One minor thing is that the pay opcode and the Auth opcode are currently slotted for the same opcode number. So that needs to be resolved. 

**Danny** [1:19:29](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4769s): Got it. Any other temperature checks on this one?

**Maurius** [1:19:41](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4781s): For the transient storage pricing I don't think we should do it. We should even think about it before we have the transient opcode in the chain and see how it's used and then we
can start having a debate whether it's mispriced. 

**Charles** [1:20:00](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4800s): Well we should have the debate whether it's priced too high right now too low right now but I think this EIP actually wants to price it down. 

**Danny** [1:20:16](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4816s): Okay well we will begin to have data in 15/ 14 days.

**Charles** [1:20:25](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4825s): Yeah I think it's good to wait for data but the data won't be complete in the sense that there's use cases that revising the pricing down enables. Which we won't see in the data. So I mean you can kind of get some benchmarks or some ideas how much resource usage you get. But you won't get clear a clear idea of like how it will be used after the pricing change versus before. And one very important use face is re-entrancy locks. So Viper would like to enable non re entrancy locks by default. It's kind of iffy whether that makes sense if T store is 100 gas but if T store is cheaper. Then it's pretty much a no-brainer and I think that's a big step forward for smart contract development ux on ethereum.

**Danny** [1:21:41](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4901s): Were there any other thoughts or comments on 7609. I guess one we can get data on usage yes that will be incomplete with respect to potentially not unlocked use cases. But also I'm I'd rather it can be here on either of these to kind of better gauge consensus. But any other comments on this before we move on today.

**Charles** [1:22:11](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4931s): Sorry again but I'd like to also point out that the EIP actually improves resource usage in that. For small number of slots the pricing is cheaper but it actually caps the amount the number of transic slots that can be used at a much lower number. So you go from being able to use like I think 10 megabytes with the current pricing to under one megabyte after the after the pricing change. 

**Danny** [1:22:45](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4965s): Sorry and this is just a function of the pricing change or is there another change.

**Charles** [1:22:50](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4970s): It's a function of the pricing change because the pricing is super vinear. So it's cheaper for small numbers of slots and more expensive for large numbers of shots. 


### EIP-7639 - Cease serving history before PoS


**Danny** [1:23:06](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=4986s): Okay we're going to move on lightclient. I did not get this on the agenda. I didn't see it this morning EIP 7639 Cease serving history before PoS. Can you give us some context here?

**Lightclient** [1:23:30](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=5010s): Hey no worries. Yeah so this is really a splintering of EIP 4844. I don't think that we are proposing fork force to be completely realized in the next hard fork. But there does seem to be quite a bit of demand from client teams to improve the situation with how much data they are required to store on disk. And since we have been working quite a bit on a standardized format for sharing Pre merge history. I think that. Trying to target this next Fork as a time where we can stop serving that pre-merge history over the network is a pretty good direction to begin looking. And I just wanted to get it on the call now and to start discussing a bit and see what the appetite is from teams to maybe make the commitment that in 6 / 9 /12 months. That it's not going to be possible to get that information over P2P and you will have to use some external data source. The other big piece of this EIP which I think some people have left some comments on the PR. Maybe we'll split it into a slightly different thing. That I think is important to have a green light from ACD is this header accumulator. The header accumulator is really an interesting pre-merge interesting Pre merge data artifact that is inspired from the historical Routes accumulator on the consensus layer. And it just gives us an efficient way to communicate about the entire pre merge chain with just a hash tree route. And then make proofs about the history of the pre merge chain in log size rather than in linear size. So I want to get agreement both on this is something that we want to do. We want to try and stop surveying this data over the P2P in the next hard fork. And that we have been able to verify that this is what the pre merge chain looks like. So in a sense we're like committing to a later authenticated route per se of the chain. 




**Danny** [1:25:59](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=5159s): Sorry and I haven't looked at the EIP. Where would the the pre merge route show up?  This is just baking
into the client or is this some sort of State transition change?

**Lightclient** [1:26:08](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=5168s): It a lot more up to what clients want to do with this given that there will be other ways to access the
data if your client is going to still provide users the ability to download that historical data. Then it's going to be important for client binaries to include that route hash and then verify
the data they're downloading is authenticated against that route hash.


**Danny** [1:26:34](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=5194s): Okay so this just defines a canonical way to kind of come to that routr hash dictates that route hash in EIP such that it can be easily included and agreed upon in by names.


**Lightclient** [1:26:44](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=5204s): Yeah exactly. I don't know this could possibly live outside of an EIP it may definitely live in a different EIP.  But I think it's probably important that if this is the user story we're going to
provide for downloading history. We should probably as a group agree that's the route that refers to the data before the merge.


**Danny** [1:27:11](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=5231s): I see any questions for lightclient or any initial comments or temperature check on this.

**Mikhail Kalinin** [1:27:19](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=5239s): Yeah I assume that this also about not just blocks but also receipts right like all chain Data before the merge. So I just wanted to say that probably the EIP is kind of like dependent on something like 6110. Yeah and I mean like because otherwise some CL clients will not be
able to reconstruct the deposit Tree because they will logs will no longer be available.


**Lightclient** [1:27:55](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=5275s): That's
True.


**Danny** [1:28:01](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=5281s): Are there any other consensus on either consensus or execution layer that requirements on logs? Or is it the single? I believe that's the single. Okay anything else on this one before we move on? Seems like something that is worth chewing on and surfacing in a call or two to see if there's any additional consensus here?  Okay Mikhail engine API and Jason RPC changes.

## Engine API & JSON RPC changes (context)

**Mikhail** [1:28:42](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=5322s): Yeah so I want to quickly talk about Engine and JSON RPC changes potentially entailed by the confirmation Roof. The confirmation roof as a reminder is a CL construct that under certain assumptions allows to confirm a block within one slot, confirmed block.  Yeah it's assumed that the confirmed block will remain canonical will remain in the canonical chain and eventually get finalized. If those assumptions are true. So this is kind of like quite cool feature for daps and services that use blockchain data to get early block confirmations. And yeah obviously we want to expose these information somehow to those parties who work on daps and services. And the way that is kind of like we can do it is to basically take the confirm block hash from CL propagated to EL as we do with the save block hash and expose this confirmed block from the outside JSON or CPI. So this basically is like the default way to do it and yeah there are a few discussion points due to a lack of time I think we can go over them later on on some later calls. I just want wanted to say that potentially if we decide to you know to propagate this information and to expose this information to users in this particular way we'll have to do these changes to the apis and considering that the confirmation research is being finalized and then we'll be able to to finish the spec work which has already been started I anticipate that this kind of change will probably be required as a part of our work on Electro prog and I just wanted to rise developers awareness that there is yeah potentially we will have this change alongside to the EIP. Yeah and I can answer some quick basic questions through the time or we can move the discussion to you know.


**Danny** [1:31:14](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=5474s): Right. Where the execution layer can be not care about this at all and it's the requirement where you just get it from the RPC on the consensus layer. And then utilize that hash for queries on the execution Layer. 

**Mikhail** [1:31:33](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=5493s): Yeah exactly but probably Beacon APIs aren't the thing that is commonly used by DAPP developers. I don't know, I don't want to claim this more like a question to me. 

**Danny** [1:31:47](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=5507s): I think you know there are plenty of places where they're not accessible or just not commonly use that's
certainly correct. 


**Mikhail** [1:31:55](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=5515s): Yeah we could also use Save block hash change it to expose the confirmed block but was a kind of a point that the save block hash probably is treated by people more as a more safe you know block reference than the confirmation rule can provide. So this why we would probably want to have a new thing.



**Danny** [1:32:20](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=5540s): And that was the intention but I think given the use of that word safe which is probably an abusive terms to begin most people are not my temperature gauge on that has been people are kind of afraid to to undo that. Also given that this might be rolled out at variable times the confirmation role then all of a sudden depending on the client you're using and the version you might end up safe. Might have very very different meanings.




### Light Clients Breakout Room #971

Okay let's pick this up either on the context later call and the execution layer call next time. Thank you Mikhail and the final thing is there will be a lightclients Breakout room March 6 at 2:00PM UTC. There is a link to this agenda in the PM Repo. This is issue 971. Any other notes on that Phil, you would put on the agenda? 

**Phil** [1:33:18](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=5598s): Nope that pretty much covers it thanks Danny.

**Danny** [1:33:24](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=5604s): Okay. Great well we are any final comment we have 30 seconds. 

**Maurius** [1:33:29](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=5609s): Yes I would like to propose in a new ETH client version that where we don't send the bloom filter in the receipts. Basically we figured out that no client is actually storing the bloom filters for the receipts because this data is for the two and a half billion transactions that we have right now or 2.2 billion transactions right now. This data is roughly 550 gigabytes and the problem is whenever someone syncs we will request the receipts with the bloom filters. So the person that we're syncing from hash to pull up the receipts from disk. Generate the bloom filters send it over the syncing Node verifies that the bloom filter that the receipts are correct. And then deletes the bloom filters and stores everything else to disk. So instead of that we can just send the bloom filters with the receipts without the bloom filters. And the node on the other hand has to then generate the bloom filters themselves and not store them just to verify them. This would save us roughly 550 Gigabytes of bandwidth during initial sync and also a bunch of bandwidth during normal block. Oh actually no during normal plock production we generated ourselves. So it  would wouldn't save us any band voice there but yeah so I'm preparing an EIP for a new ETH protocol version I can send the link of the draft and this will also remove two other messages and the TD the total difficulty from the handshake because we don't need the total difficulty in the handshake anymore.


**Danny** [1:35:38](https://www.youtube.com/watch?v=4ioJwNPe6RU&t=5738s): Okay we're going to keep an eye out for that EIP circulate the draft Andrew I see you have a comment but I have to go. I'm not sure other have to go. Take care, thank you everyone. We can discuss on Discord . See you thank you. 


# Attendees
* Danny 
* Potuz
* Lightclient
* Ansgar Dietrichs
* Guillaume
* Justins
* Kolby Moroz Liebl
* PK910
* Ignacio
* Barnabas Basu
* Guillaume
* Andrew Ashikhmin
* Danno Ferrin
* Marius Van Der Wijden
* Potuz
* Richard Meissner
* Anna Thieser
* Ben Edginton
* Ahmad Bitar
* Arik Galansky
* Hadrien Croubois (Open Zappelin)
* Eirik Ulversey
* Vub
* Nazar
* Ignacio
* Josh Davis
* Antonio Sanso
* Pk910
* Anders Holmbjerg
* Kolby
* Jochem
* Guillaume
* Terence
* Ben Edgington
* Barnabas Busa
* Alto
* Phil NGO
* Yoav
* Dror Tirosh
* Charles C
* Toni Wahrstaetter
* Mikhail kalinin

## Next meeting [ Mar 14, 2024, 14:00-15:30 UTC]
