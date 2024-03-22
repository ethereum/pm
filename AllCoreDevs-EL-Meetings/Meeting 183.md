# Execution Layer Meeting 183 [2024-03-14]
### Meeting Date/Time: Mar 14, 2024, 14:00-15:30 UTC
### Meeting Duration: 95 Mins
#### Moderator: Tim Beiko
###  [GitHub Agenda](https://github.com/ethereum/pm/issues/976)
### [Audio Video of the Meeting](https://www.youtube.com/watch?v=US8T0ZoGF8s) 
### Meeting Notes: Meenakshi Singh

---
 

| S. No  | Summary |
| -------- | -------- |
| 183.1     | **Dencun Upgrade Retrospective:** The Dencun upgrade, which went live on mainnet on March 13, was a significant milestone. It had been in development for over two years. |
| 183.2    |Validator node operators widely upgraded their software in support of the hard fork, resulting in no meaningful disruptions or block processing delays.    |
|  183.3    |The network is processing new transactions and blobs more speedily than expected. Blobs, despite their larger size, are arriving earlier than blocks, likely due to optimizations deployed by “private source” relays for additional MEV rewards. |
 |183.4|Some nodes experienced an increase in one-block reorgs after the upgrade. For instance, it was reported roughly 17 to 18 reorgs per day compared to the previous average of 15 reorgs per day.|
 |185.5| Developers will update the status of the nine Ethereum Improvement Proposals (EIPs) included in the Dencun upgrade to “Final.”|
|183.6|**Pectra and Code Changes:** Developers discussed potential code changes for inclusion in the next major Ethereum upgrade after Dencun, code named Pectra|
|183.7|Controversial EIPs related to account abstraction were among the topics considered.|

____

# Agenda

## Dencun Updates


**Tim Beiko** [1:48](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=108s): And we are live for ACDE number 183. Good job for everyone making it on time with the daylight savings change. I think next one of these the Europeans will have their local times all messed up. For today we'll talk about the fork obviously and then quick shout out to move all the EIPs to Final. If you're an EIP author we should also quickly touch on Goerli as we're shutting this down after the fork. But it looks like it's already sort of falling apart on its own. Then tons of stuff around the next Fork Pectra, so we have Dan on to talk about the impact of 374 on users Alex wanted to talk about some changes and tweaks to the BLS recompile. Mike had some stuff on inclusion lists we have some stuff on call data some. And then a bunch of opcodes if we make it through this and still have time Paradigm has been working on some research around the impact of State growth and how it's distributed both in terms of types of contracts. And then the rate of grow over time. We have these couple retroactively applied EIPs that we had to follow up on. And then lastly we had these testing calls that we've been running up to the fork that gotten shorter and shorter as we got close to the fork and we're seeing if we still want them. Okay I guess to kick this off the fork went well. Great work everyone. We saw a little participation drop for a few minutes that seems to have resolved itself but anyone notice anything interesting or that they wanted to bring up and discuss as things went live.


## Move EIPs to Final [Update EIP-4844: Update blob base fee to blob base fee per gas EIPs#8316.](https://github.com/ethereum/EIPs/pull/8316)


**Danny** [3:50](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=230s): Even just a quick like perspective on blob usage thus far would be interesting. If anyone has it.


**Tim Beiko** [3:58](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=238s): Yeah Terrence you've been manually inspecting every blob that came through I think.

**Terence** [4:02](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=242s): I have two point the first point was that we were kind of worried that the blobs will be arriving later than the block because of their typically heavier than size. And from my first observation for the first 24 hours that hasn't been necessarily the case. I see like 50% of the time blobs are arriving earlier than the block. I suspect typically that made I suspect what happened was that the relayer from MEV boost have some building optimization that just costed the Blob right away. And then while packing the block. But then I try to confirm that with the flash Bots since their relay is open source. They say they don't have an optimization like that. So I suspect there may be some private Source relay or somewhere that has some built- in code that does this. So yeah and then the second observation is the fork choice rate. So I can post a graph after. So the first 24 hours my local note see like an average increase of 3 to 4 reorgs. So yeah I'm curious what everyone's know thinks. But yeah for any my notes is more than 3 to 4 reorgs per day.

**Danny** [5:21](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=261s): Sorry 3 to 4 per day. And what was it before the fork?

**Terence** [5:25](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=325s): Okay so before the fork is on average 15 reorgs per day right now I'm seeing about 17 to 18.

**Danny** [5:32](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=332s): Okay and these are generally deep ones?

**Terence** [5:38](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=338s): Yeah.

**Tim Beiko** [5:45](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=345s): Thanks for sharing. 

**Paritosh** [5:47](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=347s): Maybe I can go next based on the listed satle data we have. We're seeing pretty much the same in terms of there are some we're seeing in terms of reorg that 2 or sometimes 3 but they don't seem to be recurring and neither do they seem to be unique to post f. In terms of blobs we're also seeing blobs arrive within the 2 second Mark mostly. That's really least what the heat map says and this is for ingesting something like 6000/7000 blobs that have come through since the fork but otherwise I think we're not noticing anything unexpected. 

**Tim Beiko** [6:31](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=391s): Nice. Anything else?

**Danny** [6:38](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=398s): Is the base Fee still at the minimum of the blob Base fee? Or has started ramping up?

**Lightclient** [6:50](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=410s): I think it's mostly a minimum still.

**Peter** [6:52](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=412s): The base fees is at minimum but like it's getting close like it's around the point where if there was much more demand the price would go up. 

**Danny** [7:01](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=421s): Got okay yeah its in demand. It’s doing it right now. 

**Tim Beiko** [7:16](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=436s):  Okay. Any other observations comments? Okay well again Great work everyone. This has been a massive massive work that we've worked on for over two years. So very cool to see go live and be so uneventful. Yeah we have the blobs. And again if you have there wasn't just the blobs that shipped bunch of other EIPs. If you are the author of an EIP please move it to the final now. So we can wrap this up spec-wise. I'll start harassing everybody about that next week. 

### [Goerli Shutdown](https://blog.ethereum.org/2023/11/30/goerli-lts-update)

**Tim Beiko** [8:05](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=485s): And then lastly Goerli. So we agreed to deprecate Goerli and shut it down after this Fork. What we originally agreed to was basically at the earliest one month after it went live on mainnet. So you know call that April 15th. It seems like the network is pretty much in a state of chaos already where there's less and less operators on it. I guess does anyone have any objection to just still keeping the date of April 15th as like a heads up for the community letting people know that like in the meantimes it's already not super stable but yeah at least keeping some nodes from lightclient teams and devops running until then. And on April 15 they'll being fine shutting you off yeah. Alex you'd be surprised by the things people do not know. I Heard recently that prysm users didn't know they had to upgrade their execution layer. So  probably worth another round of announcement if yeah just to give a heads up. 

## Prague/Electra EL Proposals

### EIP-2537[(context)](https://github.com/ethereum/pm/issues/976#issuecomment-1986293212)


 
**Tim Beiko** [9:25](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=565s): Okay sweet. Then moving on to the next Fork Prague and Electra. So we've been discussing this for the past couple of calls and just kind of a mix today of people who want to provide additional context perspectives on some EIPs that are being considered. And then I think 2537 is the only one that we actually want to change something that's already been included. So maybe I'll swipe up the agenda a bit. Maybe we start with 2537. Just to get through those questions and then we can cover all the other potential EIPs that aren't that aren't included quite yet and go from there. Alex, do you want to kick it off with 2537.

**Alex Stokes** [10:13](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=613s): Sure. Thanks let's see. So this is the EIP to add functionality for BLS precompiles. So I guess just as a refresher there's like kind of two different things here. There's like precoompiles for the BLS curve. The BLS 1231 curve they're also pre- compiles for essentially this BLS signature scheme and these are like different BLS's which is confusing but good to keep in mind. And either way I've been talking to various people in the community like different cryptographers different rollups a lot of people. And basically there's some things kind of not present in 2537 right now that would be good to have. So I wanted to go through these and kind of get a temperature check today to see kind of what we're thinking. Let's see yeah basically people want more pre- compiles and I know that's been like pushed back historically that there are already a lot in this EIP. But yeah maybe we'll just walk through these different points and I'll see if anyone has any thoughts. So the first one is adding well yeah this is where it could get wild because it's probably well at least two let's say two precomopiles for Point decompression. So this is actually helpful for rollups. I don't know how much we want to get into it but basically right now. There are the APIs right now for the precompiles take points on this curve that are in this like decompressed form. The concern is that if you're at L2 then data is more expensive so you might want to submit the compressed points. But then the concern after that is that it's too expensive to decompress them sort of natively in EVM so we want to add pre-compiles for this. Again this is something where it's really helpful for L2 maybe less helpful for L1 but this is an open question. 


**Antonio Sanso** [12:13](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=733s): As Alex as an alternative can just work only with instead compressed point and so we are doing like consensus does. So changing the current precompiled to work with compressed points.

**Alex Stokes** [12:30](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=750s): Right let's see yeah. I mean I guess the concern then is just that you know we would.

**Vitalik** [12:42](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=762s): Yeah like there would be lots of custom algorithms that call the precompile many times to do lots and
lots of additions and if you add a decompression to each addition it becomes quickly  nonviable. 

**Alex Stokes** [12:56](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=776s): Right so there's this trade-off between like computation and data and yet thinking was like data is more expensive at L2s. So maybe have this here versus you know it's flipped on L1. 

**Tim Beiko** [13:13](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=793s): And is the argument against doing this just that it's like two more pre-compiles and 2.


**Alex Stokes** [13:20](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=800s): For all of this will just be there's way too many pre compiles because I think there's already nine or so. And then this will just keep bumping it up.

**Vitalik** [13:32](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=812s): On the too many precompiled points this is like a bit of a broader topic but I feel like at some point we should revisit the topic of doing EIPs that replace existing precompiles with existing code Implementations. And that would be a path to like actually decreasing the number of precompiler that we have to deal with over time. And especially now that we have M Copy the most obvious one to start with would probably be the identity precompile. And others would be like some of the less used hash functions for example. And that would and then the idea would be that that could no not swap them for new OPcodes like swap them for pieces of solidity code that do the same thing. Yeah so from a user point of view it would stay the same except it would realistically cost more gas and then the argument would be that like if slash when in the future we end up doing modular arithmetic in the EVM. Then like that would be a path for eventually also swapping out a decompression precompile with Solidity code. 

**Antonio Sanso** [14:50](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=890s): Anyway I think that I been thinking yesterday while writing the the vectors test the vector. Sorry it's like if we really want to reduce like number of precompiles for this EIP. Maybe we can merge the scalar multiplication with the multiscalar multiplication. At the moment we have two separates but we can do like we do for pairings I mean you can do like multi pairings and this one precompile. So like we can actually remove the scalar the two scalar multiplication and having the multi the MSM that takes as well one as parameter that is allowed at the moment as well.

**Tim Beiko** [15:29](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=929s): I don't remember why but five years ago when we were talking about BLS. I think the precompiled were all there was like much less of them and then after a bunch of arguing we decided that like different pre-compiled for different operations was a better way to go. So happy to open up that can of worms again if people feel strongly about it. But I don't know that we're bottlenecked by the actual number of addresses used right. It's more about the total complexity of the thing or is there a reason why using more addresses is somehow an issue, it's not more addresses.

**Maurius** [16:16](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=976s):It's just we expose a greater surface for buck basically if we have this the set of pre-compilers that we have right now. We don't care about any bugs and decompression so.
 
**Tim Beiko** [16:39](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=999s): Yeah so the new functionality itself like that's something we should debate but like whether it's exposed through 11 addresses with individual pre-compiled per operations or like say one huge merged address like that sort of orthogonal to like  whether we actually want to do the decompression.

**Alex** [17:10](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1030s): Right so yeah another note on that point is I'll be talking to the layer 2s on the next roll call. I think they might be next month but my plan is to get more direct input from them. Because I think this one impacts them a little bit more directly than another one.

**Peter** [17:28](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1048s): This is also one of these situations where you could split it if we're unsure about the decompression. If we're still arguing about the decompression precompiles when we get to the next hard Fork we could ship BLS in Pectra and then ship the decompression pre-compiles in the following Fork if it comes to that. 

**Alex** [17:46](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1066s): Yeah that's an option. So yeah I mean maybe I can just quickly get through the rest of these open questions here because basically yeah they're just adding more functionality You probably don't care about the exact details but just to round them out. There's  essentially three groups really with BLS12 381. We have precompiles already for first two groups there's a third group and it'd be really nice for cryptographic applications to have this third group. Again more  complexity then there was demand to change how the current pairing precompile works because basically you give it the right inputs. And it just tells you if they are equal essentially under this operation but again for different cryptographic applications you actually want to get the value back not just are these two things equal. Yeah so ultimately if there are any cryptographers on the call that want to argue for this it'd be great to hear from you. Otherwise it sounds like we have to make this decision around just the general complexity of this EIP. 

**Vitalik** [19:01](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1141s): One argument against exposing GT elements and I think this is a the key reason why we've so scrupulously avoided. It is basically because once you expose GT elements you start requiring every implementation to like actually have the same pairing as opposed to requiring every implementation to have a pairing. And that is like that that is a thing that increases the complexity of making a new implementation it increases the complexity of this of the specification.

**Maurius** [19:44](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1184s): And it also kind of locks Us in for the future to this algorithm.

**Vitalik** [19:56](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1196s): Right like there's at least three different ways to computer pairing there's different lots of different ways to represent extension fields. And all of these things and there's like some mathematical way in which they're all equivalents to each other. But if we make an opinionated choice on one there just like there is a lot of stuff that's currently not spec code that becomes spec code.

**Maurius** [20:30](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1230s): Are there are there any use cases that actually require the GT or is it just purely it would be nice to have this?

**Vitalik** [20:42](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1242s): They are definitely are like specific protocol constructions that are like pretty esoteric use cases that I can  think of. The one that comes to mind is basically being able to commit to a set of elliptic curve elements in such a way that you can like multiply the commitment by a constant to get a commitment to something that commits to the elliptic curve points multiplied by a constant. And there's like some use cases of that but like you have to really really dig down the rabbit hole too .

**Antonio** [21:22](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1282s): Not n back is as well one of the things GT.

**Alex** [21:41](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1301s): Okay so I think that was helpful. I'm going to go back to these different stakeholders and try  to understand better how strongly they feel. Otherwise I think that's it for now.

**Tim Beiko** [21:54](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1314s): Awesome! Thanks Alex. Okay.

**Maurius** [21:59](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1319s):  The gass limit changes?

**Alex** [22:02](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1322s): For 2537? Yeah that's on my to-do list. I figured if you know if we're going to change either the interfaces or the actual pre-compile set then we want to do that first but yeah that's on the way.

**Maurius** [22:19](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1339s): No just to say that there might be gas limit sorry gas cost changes to the pre compiles. 

**Alex** [22:25](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1345s):  Yeah I think there certainly will be. 


**Tim Beiko** [22:28](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1348s): Got it. Okay so yeah let's keep discussing that and then worst case if like we haven't made a decision on this as we start working on devnets and stuff we can always implement the current version with the current pre- compiles and go from there. Okay I think this was the only sort of already included the EIP we had stuff to discuss on. So everything else is stuff that's been considered for the fork. 

### EIP-3074 user perspective

Yeah so I think probably makes sense to go through them one at a time and chat about them but first up we have Dan from metamask to talk about 3074 and specifically the impact it could have on users. Dan, the floor is yours.

**Dan Finlay** [23:27](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1407s): Awesome! Thanks a lot Tim. Yeah I just wanted to make some comments in support of EIP 3074. On behalf of Metamask and Consensus you know some of these will probably be redundant for some of the people here but it bears saying since it sounds like it's getting some pretty favourable support. So I think we all know that EOS have proven to provide an insufficiently flexible system for authorization for many people and people are suffering millions of dollars in fund losses every day. And we believe that 3074 is an opportunity for the protocol layer to bring some opportunities for user safety that can then be implemented at the wallet layer. So 3074 allows EOA holders to adopt smart contracts to authorize their transactions and that could eventually mean taking fully authorized one of one private keys off of hot machines entirely. And ensuring far more people are using patterns that we're continuing to refine for safety and usability in the contract account space. 3074 has had some criticism for involving a dangerous authorization signature and wallet have the ability and duty to ensure that that signature has the same user-facing saliency as exporting a secret recovery phrase. But once signed the wallet will have the opportunity to permanently adopt separate patterns including ones where a user never needs to view or export a key and a single signature can never transfer away all of their funds. We all know contract accounts have a lot of benefits. And 3074 can bring nearly all of them to existing EOA holders batching sponsored transactions approven call multisig session Keys delegation. The EVM is the limit. It doesn't bring the ability to revoke the original signing key. And it seems unclear to me at this time whether that's possible even by EIP 7377 and others since an outstanding signature is often enforced by a third-party contract that could be unknown to the signer. So I'm glad that that goal is beyond the scope of this EIP.  The current draft also has added a mechanism that enables the revocation of the authorization . So a hot signer could keep a revocation message available in case of emergencies found in new contract account even while not keeping the original signing key hot. So contract accounts have hard problems ahead for how to bring the most safety to their users but at least with 3074 we can bring our existing 100 million or so accounts along for the ride. Thanks.

**Tim Beiko** [25:47](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1547s): Thank you. Any reactions, thoughts comments I know we've talked about this a bunch these past couple weeks but yeah.  Hadrien, Yes.

**Hadrien Croubois** [26:02](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1562s): Yeah I was wondering what is your vision for user using this authorization scheme do you expect them to only go through relay your contracts that use this authorization or do you expect them to continue using regular type 2 transactions? 


**Dan Finlay** [26:21](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1581s): Yeah there it would probably involve eventually moving to a relayer system similar to  yeah 4337. Because if we continued using type 2 transactions then the user would still have to have private keys. I guess they could keep a gas key local and you know that's a design space that we'll be continuing to explore but I my impression and suspicion is that we'll be going towards something as similar as possible to whatever becomes the account abstraction Norm.

**Hadrien Croubois** [26:49](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1609s): Because my understanding is that every time a user uses a normal type one or type two or even type three transaction there nonce increases and they authorization got revoked so they need to resign them everytime and you mentioned that this signature is as critical as like exporting your your private key or your seed. So are you expecting users to do that more than once? 

**Dan Finlay** [27:12](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1632s):  Oh no! if the user was using type one transactions directly I would imagine that they're using those to relay their authorizing transactions for the accounts that signed 3074 transactions. because like you say another type one transaction from the same EOA would invalidate the authorization signature.

**Tim Beiko** [27:47](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1667s): Any other?


**Alex Forshtat** [27:48](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1668s):  I want to ask if you have any like particular relay system implmentation in mind. Because I worked on open GSN and 4337. I wanted to hear like how you see because like one of the problems that happens is when a transaction like kind of invalidates the following transaction or even itself and like in 4337 we do a lot of like bending backwards to make sure that it doesn't happen with all the validation rules.


**Dan Finlay** [28:19](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1699s):  Yeah I'm a big fan of two-dimensional nonces for that kind of thing. Obviously you know there's other systems possible too with like you could have like a graph of nonces or something. But I expect that contract accounts need to adopt you know patterns that solve that and 3074 would allow you ways to delegate to schemes that solve that for them. So I suspect two dimensional lances but you know the design space is Open.

**Tim Beiko** [28:51](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1731s):  Vitalic?

**Vitalik** [28:53](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1733s): Yeah I mean one other thing to keep in mind I know that I think Mike is not present here, more about this later but you know I think the ecosystem is moving toward more and more realisation that authorization logic does have to be in some sense kind of explicitly recognized by the protocol. If we want because that's necessary for it to benefit from inclusion lists which are becoming more and more accepted. The most practical solution for ensuring censorship resistance. Especially in the context of continuing growing Builder separation and or Builder censorship and Builder centralization. And so one thing to keep in mind on this is that whatever these schemes that we ends up coming up with like it probably ends up making sense in the longer term so like actually make them protocol features in some form or another.

**Dan Finlay** [30:03](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1803s): Yeah I could see a benefit to including if a account uses is a used to make a call using off call so maybe require including it in the inclusion list. 

**Vitalik** [30:17](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1817s): Right yeah basically think about like making an like some sort of enshrined and more generalized notion of Validation that is of like it's general enough that it covers what can happen in 3074 off calls and general enough to cover what would happen in for in 4337 wallets. But you know like this is still one of those ongoing research areas that I think is valuable to highlight.

**Dan Finlay** [30:48](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1848s): Yeah that makes sense and it's promising to me that it seems like this would work well with inclusion List.

**Vitalik** [30:57](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1857s): Yeah one more thing that I think is just also worth highlighting on the gas 3074 stuff is that I think there is value in making sure that like while EOS and smart contract wallets continue to be like separate classes of entities for any of these new. And like really important functionalities that we give to them like the the path by which EOS get them and the path by which smart contract wallets that get them are parallel as opposed to being two separate ecosystems. And like there's precedents that by what in the existing ecosystem that I kind of worry about ike the even today relatively spotty level of support for ERC 1271 and this is also one of those things that I think would be good to not neglect. So a like EIP 3074 kind of a equivalent for smart contract wallets which I actually looked at the EIP and it seems like that would actually be not even that too difficult to set up. But also just a thing to leg for Relevant for you know fusure medium term stuff. 

**Tim Beiko** [32:24](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1944s): If we have say 3074 if we have like the opCode do is is the is the work to make this smart wallet compatible just like an ERC like it's like a or is there.

**Vitalik** [32:39](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1959s): Yeah I mean so the great thing that 3074 has is that like it doesn't derive the address from the signature it requires you to explicitly specify the address. And so there's like a natural extensibility path for that to be smart contract friendly. 

**Tim Beiko** [33:00](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1980s): Got it. Any other thoughts question comments on 3074.

**Dan Finlay** [33:19](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=1999s):  I see a question in chat how quickly do we think this could be adopted by users wallets Etc? It's a good question. I suspect we could at least have some experiments in metamask this year because we're working on building an account plugin system. And so that'll allow us to kind of iterate and validate pretty quickly as soon as this is ready.

**Tim Beiko** [33:44](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2024s):  I guess one thing that's we thinking about is the way we ship this stuff you know we have like usually almost six months if not more of Devnets and then we go to testnet and then we go to mainnet. Obviously this is something where like the user flows matter significantly in a way that like most rather most random opcodes. We add you know they get exposed through solidity and then through contracts like kind of a later part of the pipeline but like if we do whether it's 3074 whether it's something else like how valuable do people think it is to have like invoker contracts or like even like a fork of you know metamask running with some like support for it like super early on in the process or like at what stage do people think we'd have to start seeing that.

**Vitalik** [34:38](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2078s):  One kind of practical path and I think this actually goes even Way Beyond this particular discussion like I advocate doing this for execution tickets for example it would be encourage some layer 2 to adopt a change before mainnet. And you know the principle there would be that that basically becomes something which is sort of halfway between a testnet and a mainnet in a sense that it has real users. And real value but doesn't go all the way up to hundreds of billions of dollars.

**Dan Finlay** [35:13](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2113s):  I think the challenge with that approach is that it kind of creates a lessen incentive for the signers to do the work up front. You know we care the most about where the users are holding the most value today and so while we might optimistically do that development. We tend to keep our focus on who's getting hurt today.


**Vitalik** [35:34](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2134s): Right but and I think like the way I think about this is like the safest thing is where you have like a relatively smooth ladder from you know 0$ depend on it to 500 billion$ depend on it. Right like you know you don't want to have like a step function where you go all the way from 0 to 500 he wants to go from you know first like 0 to 1 and then 1 to 100 and 100 to 500. So that at each level it's already got secured by the level of effort that naturally comes from the previous level. 

**Tim Beiko** [36:06](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2166s):  There's some comments in the chat saying like polygon is working on this. And then and I guess then the biggest risk with those things is like the semantics of the opcode right like is polygon doing the exact same version that we're discussing today or are they doing you know the version from a year ago. So yeah I don't know if anyone has context on that. 


**Lightclient** [36:31](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2191s): As far as I know they're doing the latest version that is specified in EIP at this moment.

**Tim Beiko** [36:37](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2197s): Got it. Arik?

**Arik** [36:43](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2203s):  Yeah I just wanted to join what Dan basically said agree with everything you mentioned. I do think that prioritisation on the wallet space is hard as well. So it is important that this kind of thing is applied in the place where we have the most interest. So that we're able to invest in it. But if it is applied in where the interest is this is definitely going to be a priority. So like the adoption in order to provide user value I believe it's something that will be invested in on our side as well. And to some extent about the risk we also as wallets we also have our own risk mitigation and risk like verification processes. So it's not like we're going to just open it up in the simplest way and everybody do whatever they want we're also going to run through a process where we make sure we minimize risk as we introduce any new technology. So there's another layer of risk mitigation that is going to happen because we also kind of take the responsibility in this process.

**Tim Beiko** [37:56](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2276s): Oh, Dror? 

**Dror Tirosh** [37:59](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2279s):  Yeah I think there's no doubt about the features that 3074 can add to a applications. The problem is not the features it can add but the risks because as we know right now the only way to have it securely is to Whitelist specific implementations that are known to be good. And what we end up is that there is a list of whitelisted implementations, the set of implementations either by the network or by dominant wallets. These are the allowed implementations of 3074.

**Dan Finlay** [38:41](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2321s): I would I would point out that a user choosing any piece of wallet software could then effectively choose the implementation they wanted to choose. So that choice it's not like I mean you could put it at the protocol level and make it a small you know plutarchy deciding it but the default is just that the market would choose users choose wallets choose implementations much the way that contract wallet developers do today. 

**Dror Tirosh** [39:10](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2350s): Yeah but but invokers does more than just being a wallet like if you want to have a pay Master wallet you know you connect with some dapp that simply wants to pay for your transaction. And you use its invoker you basically reelect your implement of wallet giving your entire value of your account to this application just because it's cool and want to give you a feature like pay for your gas.

**Dan Finlay** [39:43](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2383s): Right so kind of re emphasizing that it will be the responsibility of wallets to make sure that this election process is Salient and as safe as possible. And I think one of the strengths of wallet teams making very deliberate choices around which ones they allow list would be in part that they could you know, elect contract accounts that make it easy to let's say add features like batching without having to undergo the entire off signature process again. You know I think that there are lots of off-the-shelf contract accounts today you know no is safe with its modules and you know now the contract account module standard that are making it very trivial to have extensible contract accounts. And so I think it's very likely that most wallet developers will be able to have a very short approval list that allows users to then have the account extensibility they need without having to resort to this pretty dire authorization. 


**Dror Tirosh** [40:45](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2445s):  Yeah I only pointed out that a user actually performs this election of its wallet implementation on each transaction. It's not a question you do once I selected implementation now I'm using safe I switch to Argent or whatever. Doing it on each transaction because.


**Dan Finlay** [41:03](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2463s): That's not accurate. The user signs one authorization signature that authorizes a given invoker as long as that account's nonce doesn't increment and from then on that invoker is able to send messages on behalf of that EOA so as long as the user doesn't sign any more messages from the original EOA message they can now have subscribed to another account authorization logic including two Direct non batching or whatever else.

**Peter** [41:38](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2498s):  Would it be reasonable then to describe  what 3074 does in practice as being a temporary subscription to a Smart contract wallet. so you decide you sign this invoker authorization message that invoker authorization message then temporarily turns your wallet into whatever smart contract wallet that invoke or implements. Until you sign a new send a new  EOA transaction which increments a Nonce and then disables that.

**Dan Finlay** [42:16](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2536s):  That seems like a good metaphor as long as you don't lose your revocation message and a original private key. In which case it would be permanent.

**Tim Beiko** [42:33](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2553s):  Ansgar?

**Ansgar** [42:35](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2555s):  Yeah I just wanted to briefly mention that while indeed on the protocol side. And I hope by the way you can understand me some noise. On the protocol side there's basically indeed. It is this way that authorization could authorize an invoker to send an arbitrary amount of interactions from your account our original intention and that's kind of where this kind of commit hash came in was that we expected one of the dominant patterns to be a kind of signature for a single action only. So it could imagine basically signing over the hash of the specific transactions actions you you you you you you want to perform or something so that it could only be used once. Of course in practice we would have to see which which type of interaction would would actually be used actively whether so maybe the the pattern of basically one time authorization then the invoker always sending in your name could be possible but I'm just I don't think it's it's obvious that that in practice that would be the dominant pattern. So I think it's very likely that we'll see a one signature only authorizes a single one time action from the invoker that would be the Dominent. 

**Dan Finlay** [43:45](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2625s): I think the reason I would suspect that the dominant pattern would be to authorize an account that then performs the messages is that if you don't do that you're keeping the original private key around which is kind of the security Radioactive material that we're really trying to eliminate. So as a wallet developer we have a lot of incentive to get the the scary you know radioactive waste out of the user's hands. so that you know the things they can do with their hot wallet are more constrained to things they might actually intend to do. So I yes you're right many implementations could compete but I think there are some major security benefits to getting the main key off the hot Device. 

**Tim Beiko** [44:27](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2667s): Alex?

**Alex** [44:30](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2670s): Yeah just about the subscription model the analogy that you said if I understand correctly a single wallet like address can be subscribed to as many invokers as it wants at the same point right as long as you sign and don't revoke the rotation is it?

**Dan Finlay** [44:47](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2687s): I believe the latest draft of the EIP actually requires that the authorization includes the latest norms for the EOA. So only a single invoker can be authorised at a time. 

**Alex Forshtat** [44:57](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2697s): But using this authorization does not increment nonce. So like you can sign and sign and sign for as many invokers. Just like wanted to raise the concerns that it like kind of increases the surface like the potential surface of code that the same address can have as opposed to like having an implementation of a wallet one at a time that's it.

**Lightclient** [45:31](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2731s): Yeah I mean I think it is kind of similar to plugins for smart contract wallets like you could have an implementation of a smart contract wallet that you're using. But then you could  authorize many different plugins related to that smart contract wallet I don't really see it being terribly
Different. 

**Tim Beiko** [46:04](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2764s): Okay and I know there were some comments by Anagar in the chat as well around like prototyping an end to end flow for this from like you know a client implementation all the way to

like an actual wallet using an invoker.  How blocked is something like that on us like choosing to move forward with 3074 or some other EIP like. Is this something we can just have like one.  Is it something we can just have like one client team looking at and prototyping alongside the wallet and seeing like okay can we get like a flow that we like or is this something where actually getting everyone to commit to like 3074 or some other proposal or some changes to it is like the right first step.

**Dan Finlay** [47:06](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2826s): I mean I definitely understand Vitalik's point that that like easing in is almost always a beneficial approach. I do think that most of the accounts that will benefit from this need the main chain to adopt. So while I think we're very happy to work on some prototyping with smaller chains like polygon. I think the the big fish is the Big Chain.

**Tim Beiko** [47:30](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2850s): And I guess maybe another way to frame this is like how much value is there in prototyping even on like a devnet and testnet relative to a chain with actual money. Is you know do you get like 80% of your learnings from like there's actual value at stake here or you know is like prototyping just the sort of user flow like what brings most of the clarifying value if that makes sense.


**Dan Finlay** [48:02](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2882s): I do think that in this ecosystem a lot of lessons come from the actual value that's weighed on the designs that we built. 

**Tim Beiko** [48:09](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2889s): Got it and I know yeah we've discussed like other proposals in the past. I think 5806 was the other one that came up and those were pretty much actually 5806 and then there was one about like the one time operation to make an EOA into a smart contract wallet. I forget what the number is for that one 7377. Thanks lightclient but I guess out of those three I'd be curious to hear from just like the different client teams like you know do we still feel like it's worth considering all of them do people then they prefer like 3074 over them. Yeah how the teams feel about the different ones? 

**Dan Finlay** [49:08](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2948s): I see Hadrian's here and I owe him a 5806 review but having gone over it. I think that it follows
it addresses a kind of different issue it allows you to kind of have a delegate call from your EOA and execute code from your account. But it doesn't enable external contracts to kind of add functionality to your account. You're still signing with your EOA as far as I'm aware and can correct me if I'm wrong.

**Handrien** [49:38](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=2978s): No that's correct yeah and then the other ones also you know using new transaction types require the EOA to be continuously signing signatures you know. So oh well at least the initial one. So that means the account has to have ether in it a nice advantage of 3074 is that accounts even with no ether are able to subscribe to contract accounts for additional authorizations. 

**Tim Beiko** [50:11](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3011s): Got it. I guess yeah I'm curious to hear how client teams feel about this there was a comment as well about like making 3074 CFI might be enough to like you know get people to consider it seriously. And start prototyping and send a signal to the community  that like we're seriously considering this. So yeah is that something different EL teams would want to move forward with do we want to look through the other proposals. Yeah I don't know does anyone on the EL side has a strong opinion.  Or okay if there isn't a strong opinion then I think it probably makes sense to then go through the other proposals for Pectra. And then maybe once we've discussed the different ones. Yeah see if there's anything that stands out as being higher priority. 

**Lightclient** [51:23](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3083s): Yeah any what should the next steps be for 3074. 

**Tim Beiko** [51:29](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3089s): So to me there's two questions, one is like do we want 3074 over other potential AA or like EOA Improvement proposals. And then do we want 3074 over all the other things we could do in the fork. And yeah I guess yeah I'm curious to understand like how client teams feel about those two questions.

**Lightclients** [51:55](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3115s): I you know I would like to review the answer of the first question but I think for the second  question I don't really know how important of a question that is to proactively answer. I think it's a question more that we should answer when we feel like we are either missing the target that we're searching for this Fork which hopefully is the end of the year. Or we feel that the complexity of the fork features is too great. I don't think that trying to sort these on priority a priority is the most important. I think we should only  prioritize it and possibly kick it out if we realize that we're not going to be able to deliver on the timeline we wanted. Or with like the complexity that we're hoping for and 3074 is a very simple implementation of an eth the complexity comes in the reasoning about the security model. So I don't think it's like  something that is going to cause us to not be able to do other things that we want to do.

**Tim Beiko** [52:53](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3173s): Got it. Any other teams or people want to speak up? Okay so yeah I guess if there's no other strong opinions? Then yeah I would wait until we've reviewed the other proposals. And then see if there's anything else we want to CFI or include but I think for now. Yeah in terms of next step for 3074 like one making sure people are generally happy with the spec across the ecosystem. So like and it seems like we we've made progress on there two like yeah it  seems like there probably is value in prototyping in prototyping implementations to get a feel for the complex flow but that'll only get us so far but yeah aside from those two things I think it's just a question of do we want to prioritize it. Any other thoughts comments? Okay we only have half an hour left so I'll move on to the next ones. But yeah thanks a lot Dan for coming on and everybody else appreciate you sharing all your perspectives. 

## Inclusion Lists (context(https://notes.ethereum.org/@mikeneuder/il-poc-spec))

**Tim Beiko** [54:23](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3263s):  Okay next big can of worms inclusion lists. 

**Mikeneuder** [54:31](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3271s): Hey Tim hey everyone. Yeah I'll try and be pretty brief because I know that that EOA discuss or the  3074 discussion ran a little long. So yeah I guess I just wanted to update a few things on the IL side of things. This is EIP 7547 and I thought it would make sense to start with just a couple minutes discussing the rationale like kind of stepping away from the technical details which I think are better hatched out kind of async. And just talking through some of the meta reasons why I think inclusion list in Electra make a lot of sense. Kind of first and foremost the the me landscape continues to evolve super quickly. I think even yesterday after the fork there was kind of some chaos around Titan Builder not necessarily being able to include blobs so then Beaver Builder started building like 75% of blocks. And like kind of this continual evolution of Builders vertically integrating with relays sophistic a timing games etc. Yeah basically trying to make the point that if we commit to not doing inclusion list in Electra we let the me infrastructure continue to evolve for basically the next year and a half to two years without any kind of changes on our side. I think that's a very active decision in itself, like not doing anything is almost as strong of a decision as doing something. So that's kind of the first point I wanted to make. The second is that the scope of the IL change is generally well contained. We've been working on this proof of concept spec POC spec. I'll share the link here. Yeah just trying to kind of drisk and show across both the consensus Layer, execution layer and the engine API that the changes are pretty small. Hopefully to motivate like going for it in this Fork the third thing I wanted to bring up is these out of protocol Solutions. So this is actually something that's being discussed kind of again even though we did discuss it before but it's cool that like people are coming to the same conclusion but at a different time. The thing I wanted to say about the out of protocol stuff is that and I'll link a doc here this is kind of the censorship resistance in me boost doc that I wrote a while ago. But the thing I want to bring up here is that the out of protocol Solutions are actually pretty different in character than the in protocol one. And the main difference here is that in the out of protocol version you can't do this next slot inclusion thing. So basically yeah there's it's not really the situation where we can do something in me boost and collect data on it. And then that like drisks the thing we're going to do in protocol because the thing we're doing in protocol is this next slot inclusion list and the thing we'd be doing out of protocol would be same slot inclusion list. So that's my biggest brief with it but I do think there is value in potentially looking at some of the out of protocol Solutions and potentially doing them in parallel. Just because you know I think this is like a defence in depth thing which is potentially really valuable. And the last thing I wanted to bring up is just that the  current inclusion list spec in the design is super compatible with the end game road map like whether that includes EPBS execution tickets. There's kind of more recent discussions around these committee forced ILs that was a post from Tas and then there's also this idea of maybe multiple inclusion list proposes at the same time. I think all of these fit really nicely with the simple framework laid out with 7547. So doing like the first step along the path of building an in protocol solution to the MEV market. I think it is super valuable. So that's kind of the pitch I'm writing a short Doc kind of based on this set of arguments and few more so that'll come out on I'm hoping to get that published by Monday. And then yeah hopefully we can continue the discussion both async and maybe on the Forum. Yeah I also just wanted to shout out quickly the All Core Devs working in the ETH R&D channel the inclusion list Channel Potuz and Terrence, Dustin, Pawan, Daniel, Sean,  Gajinder,  Enrico,  Marius, Dan & Roman, Franchesco Vitalic Tony, Hsiao -wei and Pintail just like this has been really awesome collaboration over the past few weeks. And there's a ton of activity in there so if you want to learn more if this feels important to you like definitely jump in there's lots to be discussed. And the last thing I wanted to bring up is that we discussed in the last All Core Dev's Consensus call potentially doing another breakout room for inclusion lists. I originally proposed for tomorrow but I think given that I didn't open a issue in the PM repo. And kind of haven't been broadcasting it. Maybe it makes sense for early next week. But yeah just wanted to get a temperature check maybe we can kind of that in the zoom chat about scheduling it I proposed Monday next Monday 18th of March at the regular time I'll just copy that in here so we have a reference to it but yeah thanks Tim for giving me the floor and definitely if any other folks who've been working on inclusion lists want to jump in and and say their piece then would love to hear that otherwise we'll just give the mic back to Tim. Thanks.

**Tim Beiko** [1:00:08](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3608s): Thank you Mike. Yeah I'll start to see if there's any comments or questions on what you just said and then we can talk about the breakout but yeah any thoughts or responses to Mike? I guess anyone from on the client teams either strongly in favor or strongly against considering inclusion list for the next Fork. 

**Roman** [1:00:47](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3647s): Reth would like to Signal support for including it because not as Mike said not doing anything is also a choice.

**Tim Beiko** [1:01:05](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3665s): Got it thanks. Any other teams?

**Dror Tirosh** [1:01:10](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3670s): Yes one small one small thing about inclusion list while they are great. I'm not sure they are compatible with the end game because they're not strictly compatible with the account abstraction, requires some further work.

**Tim Beiko** [1:01:27](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3687s): Why are they not compatible with account abstraction?


**Dror Tirosh** [1:01:32](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3692s): Because if a transaction may become invalid and you add it to an inclusion list then it can't be included but it's force to the way inclusion list work is that they check the basic features of an account like nonce and balance. But with account obstruction they need check on chain validation which might change.

**Tim Beiko** [1:02:02](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3722s): Mike can any thoughts on this?

**Mikeneuder** [1:02:06](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3726s): I'm not as familiar with this. I'm pretty sure Vitalic was saying that it wouldn't be an issue. But maybe Potuz can reply to this.

**Potuz** [1:02:16](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3736s): I think this this statement was false part of the validation of the inclusion list is actually checking that the transaction can be executed in the current block and the next block. So it might be true that you this is not going to solve for intents. But this are but this will solve for censorship of actual transactions. 

**Mikeneuder** [1:02:44](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3764s): Yeah I guess I was curious if it changes it all under account abstraction like a user op versus a transaction I guess being censored. 

**Dror Tirosh** [1:02:57](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3777s): A user operation right now is a transaction that can revert which can be included. You can force a user operation by adding an handle op it will be forced it will be rever on chain for example if some state will Change.

**Tim Beiko** [1:03:15](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3795s): But isn't that true I mean any transaction in an inclusion list could potentially revert based on the updated state of the chain before it gets included right. 

**Dror Tirosh** [1:03:27](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3807s): No I'm saying that with 4337 as an ERC. Yes it will force inclusion of a reverted transaction which is not such a big problem but small one the problem with Native account abstraction where transaction is no longer valid which means it can't be included. Because it depends on the state. Lot of work with account obstruction how to handle such cases but Force inclusion might. 

**Tim Beiko** [1:04:05](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3845s): Yeah Lightclent?

**Lightclient** [1:04:08](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3848s): Yeah I had a question on using ILs with any kind of account abstraction mechanism is it not that case that a any bunder that's using a permission permissionless bundling Network could submit their bundle as an IL like why does the IL need to specifically be concerned with account abstraction.

**Dror Tirosh** [1:04:38](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3878s): Again depends on the model with ERC4337 there's no problem. You can force an inclusion of a bundle and the worst thing is that it's going to revert on chain because the validation doesn't prevent it from being included on chain and ERC. Once validation becomes a part of the validation of the transaction you can't include a transaction that fails validation. 

**Lightclientr** [1:05:10](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3910s): But I mean how this is also true for EOA like you could have an I can you not have an ILthat says you need to include this transaction from EOA during the block it becomes invalidated and then the next block the EO transaction is no longer valid.

**Mikeneuder** [1:05:28](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3928s): So that's why the design only commits to the address of the transaction rather than the full transaction itself like that's the whole point of the no free launch design.

**Dror Tirosh** [1:05:42](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3942s): Okay need to look the latest inclusion list logic.

**Tim Beiko** [1:05:50](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3950s): Ansgar? 

**Ansgar** [1:05:54](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=3954s): Yeah I just wanted to say as the Meta Point given that any form of native account abstraction on layer one is still several years out even optimistically. And that thereby I would not include 3074 that's not that's separate. I mean I think the understanding is general that this kind of inclusion list design might not be one that will be the final design forever but at some point might need adjustment anyway. So I personally don't see an issue with shipping something that then you know ver basically say once we ship native abstraction might or might not require updating.

**Tim Beiko** [1:06:46](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=4006s): Okay and then I guess it seems like there's like General support for inclusion list. And it's more a question of how and when rather than if I don't know that we necessarily have time to flesh out exactly the next steps on this call with 20 minutes left and a bunch of other stuff to go over. But I do think it might be worth a breakout for this. So that we can look a bit more deeply at the different designs, what's the implementation overhead of them. And whether they're realistic to ship this year and whether in protocol designs or starting at the MEV boost level first or doing both in parallel is the right approach. Yeah and then yeah Mike is proposing Monday at 14:00 UTC that seems reasonable to me. Anyone have an objection with that way forward. Okay let's do that then let's do. Okay let's do a breakout next Monday. Go over all of the inclusion list stuff in more detail and then hopefully by either ACDC next week or ACDE,  the week after. We can have like one or maybe two specific proposals that we can make a call on and whatever we want to move forward with. Yeah we'll set up the breakout but Monday 14:00 UTC people can pencil that in. Anything else?  

**Danny** [1:08:40](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=4120s): Supect we will all have a proof of Concepts the coming week or the week after because one of the other things. I just designed was like a better understanding of complexity coming from that.

**Tim Beiko** [1:08:54](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=4134s): And yeah maybe that's actually a good thing to focus the breakout on is like yeah what is the actual engineering overhead of in protocol inclusion lists
what does it look like to do it in MEV boost. 

**Potuz** [1:09:13](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=4153s): Do you want a proof of concept for implementation or for a specification?

**Danny** [1:09:23](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=4163s): I thought there was an intent to do a proof concept implementation but that certainly could not be the case.

**Potuz** [1:09:30](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=4170s): But just like a four days the breakup room is being scheduled like next week.

**Danny** [1:09:37](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=4177s): I'm basing this off of a conversation three weeks ago in ACDC. But that doesn't necessarily mean that a proof concept was working.

**Mikeneuder** [1:09:46](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=4186s): I think there's different client teams working on different branches but maybe we can use this breakout room to kind of like to see where everyone's at. Do a pulse check and then also coordinate on maybe a more like cohesive proof of concept like end to end in both a consensus client and an execution client or multiple.

**Tim Beiko** [1:10:08](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=4208s): Yeah and I don't think obviously we can get like a full implementation done in three days or maybe Maurius can in the chat but then the thing we can maybe get in like 3 to 10 days is at least an understanding of like where we think the complexity would lie. And like you know having people looked at the spec. And then you know understanding their client code and trying to figure out what the issues will be but maybe we'll have a gas loadstar testnet by ACDC as well. Looking at the chat. Okay yeah this feels like an good place to end this and this far as the conversation. We'll have the breakout on Monday day. We'll set up something on the PM repo to detail all of that but 14 UTC. We'll see you there. Thanks Mike for the update. 

### EIP-7623: Increase Calldata - Impact

**Tim Beiko** [1:11:10](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=4270s): Okay another large not necessarily large change but one with big implications Toni's been looking at repricing call data to better discriminate between large users of call data like L2s and people who use just a bit of call data in the process of of doing more regular transactions and has put up a bunch of impact analyses data and charts on this. Toni Do you want to give some background?

**Toni** [1:11:44](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=4304s): Yeah sure. Thank you. Yeah to give you some background it's about EIP 7623 increase call data cost. And the main goal of the EIP was to reduce the maximum possible block size by increasing the cost for nonzero Byte call data. And it is doing that by introducing a flaw price for call data that is currently set to 68 gas per non-zero call data byte. So increasing it from 16 to 68 and over the past week. I've got gathered some feedback and the main concern was just to do more analysis on the impact of the EIP in the agenda. You can also see a post that already analyses the impact of the EIP and the result was like 4.5% of all transactions would be affected and only 1% of the users. And I did some more analysis that I posted in the chat here. It's basically a table with the most used methods and their median and total gas consumption split it in EVM gas and Call data gas. And in the table you can already see which methods would be affected by the EIP and which not and one thing that is currently still under consideration is the exact cost of the call data after increasing it. So should it be at 68 gas per call data byte or maybe lower maybe setting it to 48 or something. Yeah so basically thinking about the 16 * 4 Series here. But yeah open for feedback especially on that number the goal is to not affect regular users and existing applications while still reducing the maximum possible block size. 

**Tim Beiko** [1:13:56](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=4436s): Thanks. Any questions, comments, thoughts on this? 

**Maurius** [1:14:08](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=4448s): Did you decide now whether the deployment cost should go into the calculation or not?

**Toni** [1:14:17](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=4457s): Yeah so as of now the deployment cost is inside the conditional formula. 

**Maurius** [1:14:27](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=4467s): Have you looked like have you did the analysis with both or like do you know what the difference would be for people deploying contracts?

**Toni** [1:14:41](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=4481s): I guess by including the deployment costs within the conditional formula that this helps people  deploying contracts. So it would mean that if you deploy contract with a lot of call data you might still be able to yeah not hit the floor and still get the 16 gas Call data price. If you take it out outside of the conditional formula. I guess then this would get harder. But I think it's only a very very small number that should be affected.

**Maurius** [1:15:14](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=4514s): Makes
Sense. 

**Tim Beiko** [1:15:18](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=4518s): How I guess have you reached out the like L2s like the basically the big users of call data today which extensively have like shifted their usage to blobs but like is anyone going to be really mad at this when it goes live. 

**Toni** [1:15:38](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=4538s):  Yeah so I had contact with a few L2s so far. I'm also planning to introduce the EIP in the rollup call. I think that's the perfect place to get more feedback on that. But so far the only concern was raised by teams that cannot really escape to blobs because they need their call data inside the EVM. And you can think about Stark proving on chain proofs but also Merkle proofs or L2 withdrawals that sometimes take a lot of big Merkle that uses big Merkle proofs that might be affected and cannot escape to blobs. So this is the only concern but yeah I guess I'll still need to analyze how 4844 plays out now and then also how much the final increase in gas would be for those teams that cannot move to blobs.

**Tim Beiko** [1:16:44](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=4604s): Got It. And as I remember like the implementation for this is quite simple right. It's a pretty trivial change in the EVM. 

**Maurius** [1:17:06](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=4626s): Yes.

**Tim Beiko** [1:17:07](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=4627s): Yeah okay. So I guess here it probably makes sense as the next step to just one bring this up on roll call like Tony was saying. Two obviously see sort of how call data and blob usage continues to evolve in the next couple weeks. But if we want to add this to the fork can you know one two calls or even after that it feels like the type of thing that's just like easy to quickly add. And then add the devnets as we're working on them. Yeah, does anyone have any other thoughts or suggestions about how to move this forward? Okay yeah so yeah Toni I guess yeah let us know what L2 say on roll call. And yeah we'll talk about this in a couple weeks. Thanks for sharing all this. 

## [EIP-7645: Alias ORIGIN to SENDER](https://ethereum-magicians.org/t/eip-7645-alias-origin-to-sender/19047/3)

**Tim Beiko** [1:18:08](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=4688s): Okay there was one new EIP I don't know that we've talked about this on All Core Devs before that was discussed in the agenda 7645 aliasing ORIGIN to SENDER. I know I believe Cyrus. I hope I'm getting your name right.  Yeah, do you want to give a bit of context on the EIP? 

**Cyrus** [1:20:00](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=4800s): All good my name is Cyrus Adkisson. I've been around ethereum since 2014 when the network went live. In 2015 I wrote some early documentation stack Overflow Q&A some instructional videos and I presented my project at Devcon one all that said I am definitely the dumbest person on this call when it comes to the EVM. So please bear with me.  7645 so origin is an OPcode that is sort of a relic. It represents the account that originated the action and paid for the gas for the transaction which is and until we get true AA always the same thing. In mid 2016 it became generally acknowledged that TX origin for anything was bad news for a variety of reasons. There's an epic Peter Bora thread in the solidity repo that goes over these issues. One origin can be used in a sort of cross-site scripting way to steal assets or misuse Authority. If that Authority is delineated in TX origin terms origin breaks compatibility since your contract can't be used by other contracts and origin is almost never useful. It's still an outstanding question is are there any legitimate cases of TX origin. So since then documentation audits compilers everything has warned against using TX origin. And it should it has been considered deprecated since mid 2016. I guess note that for those searching that Peter bore thread removing TX origin from solidity is a completely different thing than adjusting the EVM assembly for one thing. So keep that in mind if you're reading the replies. Since people still used TX origin one of the common  illegitimate uses of origin is a lazy hack smart contracts used to determine if the caller has code and can do bad things. If origin equals a Caller is supposed to ensure that the caller is an EOA but an in an AA future that might not be the case. So AA seeks to separate the pair of the gas and the originator of a transaction into two identities one of which is so then the question is which one is origin either way you go it creates problems. So in 3074 for instance an EOA can trigger a smart contract to do an off call is that smart contract the origin or is TX origin or sorry is the EOA that initiated the transaction origin. For another in some AA proposals EOAs can have opcode thus origin can have opcode thus these origin equal caller checks break. So bottom line origin is a tech Debt Relic that no legitimate use cases. And it's standing the way of robust account abstraction. So one solution and this is 7645 first floated by Micah though he can speak for himself on his views of it now is to Simply Alias origin to Sender. That is everywhere origin appears would be treated as Sender this would seamlessly fix some misuses of origin because the alignment of EOAs to Smart contracts and breaks the alignment of EOAs the smart contracts and nullifies origin as an impediment to account abstraction. The downside is it breaks backwards compatibility for some other issues of origin. These patterns were already broken and that we have no obligation to protect them. Especially if it's holding back EVM Evolution and future capabilities. So 7645 is a straightforward proposal to do this aliasing. If 7645 proves too harsh for the community to adopt immediately. I flowded a precursor plan no EIP yet to Simply ban any new appearances of the origin opcode in new smart contracts as a pectra which I guess is a consensus layer thing I guess the idea is to put a full stop to all uses of origin tease out misuses of origin that have been going on. And educate the community and then eventually do the aliasing of 7645 later. Yesterday Danno Ferrin said that this pre-deployment check for origin is not possible until we get EOF but I'm not knowledgeable enough to know to be able to confirm or deny that myself. So that's the pitch. And I was hoping to get feedback. 

**Tim Beiko** [1:24:23](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=5063s): Thanks thanks for sharing and yeah we have Danno with his ends up. So please Danno.

**Danno Ferrin** [1:24:29](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=5069s): Yeah so the the problem with the predeployment check is there's multiple uses for the code not just EVM code people are using it for whether they think it's legitimate or not they're using the code just as data contracts that's one use. And the second because of the way solidity compiles EVM it puts signature data after the code and even some cases without the signature data there's just some code data that exists in the EVM there is no reliable way to differentiate the code from the data and that's part of the problem that EOF is meant to solve is to separate the code from the data. So if banning origin is something that's valuable that something that can very easily be added to the EOF spec I had considered it frozen to this point. But that's a very small addition and a very small change to the reference tests. I guess I didn't put my request in to speak about it on this call in the agenda but you know quick update on EOF it's you know the specs Frozen we're doing final implementations reference tests are being written. So that's a quick update there but I don't think that banning an OP code in Legacy EOF Legacy EVM is in any way possible. Increase in the gas cost is one way to make it unprofitable. That's the tricks we would have to do. 

**Tim Beiko** [1:25:45](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=5145s): Thanks. Peter?

**Peter Davies** [1:25:49](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=5149s): Yeah firstly I'd like to say I thought you explained is be well there. I think that trying to ban it as Danon has explained is just really complicated whereas turning it into sender is like pretty much the most trivial change you could make like it's hard to imagine a more trivial change to the EVM. So I would be tempted to do that and the main question is like to what extent have you investigated the patterns that are going to be broken because the challenge you're going to have is someone's going to say well potentially there might be some contract somewhere that is broken if origin always equal sender. And I wondered how much he'd investigated that.

**Cyrus** [1:26:28](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=5188s): The auditing firm  Dedaoub did a study on this when it was investigating 3074. So you can probably Google search that pretty quickly Dedaoub was the company although. I think there's been some disagreement about the conclusions they reached on that. And honestly that gets beyond my knowledge to be able to defend or whatever. 


**Tim Beiko** [1:27:00](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=5220s):Okay thank you. We only have two oh Charles yeah last.

**Charles C** [1:27:05](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=5225s): Oh I was to say that I think generally changing semantics of opcodes is pretty dangerous because you know people could be relying on it for some particularly important thing. And something else like just increasing the cost so that people know that it's like quote unquote deprecated output is like a maybe a Slicker change from a compatibility standpoint.

**Tim Beiko** [1:27:40](https://www.youtube.com/watch?v=US8T0ZoGF8s&t=5260s): Right okay we have two minutes left. I think it's probably worth pushing back the state growth analysis at the next call. So that we have time to properly go over it. So I have a link the agenda. I can put it here. I strongly recommend everyone have a read at this it's really good work by the Paradigm team. And I think it probably makes sense to have this high in the agenda next call. So that we can go over any questions or comments on the research but with one minute left before we close. I guess the one last thing I want to cover is we've had these Fork testing calls happening every two weeks that have sort of petered out as we got closer to the fork. Does it make sense to keep doing them now would we rather cancel them and and start them up again when we're sort of farther in the fork process? Any thoughts there? I'd rather cancel. Okay, perfect. Cancel confirmed in the chat. We'll do that then. So on Monday there's the I breakout but we won't have the interop testing call. I'll delete that after this is over. And everything else on the agenda that we couldn't quite get to today. I'll just bump to the next call. So again State growth research couple EIPs for EVM changes and then this discussion of like they retroactively applied EIPs. And hopefully yeah by the next ACDE we have a good feel for what inclusion lists are looking like, maybe a better sense of like the community is ready. Yes, around 3074 or something like that. And then I think it probably makes sense to make decisions about additions to Pectra on the EL side then rather than in overtime today. And we'll see we might even get a experimental devnet by then looking at the chat. Yeah thanks everyone for coming on again. Congrats on the fork ethereum still running smoothly. Yeah excited for this and talk to you all on the breakout Monday. 

--- 
# Attendees
* Terence
* Tim Beiko
* Cyrus
* Hadrien Croubois
* Marcello
* Ignacio
* Antonio Sansa 
* Kolby Moroz Liebl
* Potuz
* Josh
* Roman
* Eirik Ulversoy
* Maurius Van Der Wijden
* Lightclient
* Danno Ferrin
* Paritosh
* Enrico Del Fante
* Toni Wahrstaetter
* Ben Adams
* Echo
* Draganrakita
* Guillaume
* Justine Florentine
* Guruprasad Kamath
* Danceratopz
* Pooja Ranjan
* Mikhail Kalinin
* Ahmad Bitar
* Gary Rong
* Scorbajjo
* Sean
* Peter
* Daniel Rocha
* Karim T.
* Amirulashraf
* NC
* Danny Ryan
* Mario Vega
* Lindsay Gilbert
* Nazar
* Alex Jupiter
* Marcin Sobczak
* Stokes
* Gajinder
* Kamil Chodola
* Marek
* Den Finlay
* Ansgar Dietrichs
* Phil NGO
* Alex Forshtat
* Mikeneuder
* Rudolf
* Gary Rong
* Piotr
* Lightclient
* Charles C
* Vasiliy Shapovalov
* Matt Nelson
* Peter Davies
* Ruben
* Barnabas Busa
* Plasmacorral
* Peter Garamvolgyi
* Hsiao -Wei Wang
* Dror Tirosh
* Anders HK
* Carl Beekhuizen

# Next meeting [ Thursday March 28, 2024, 14:00-15:30 UTC]

___










