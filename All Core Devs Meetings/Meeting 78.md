 ## All Core Devs Meeting 78    

 ### Meeting Date/Time: Thursday 2019/12/5 at 14:00 GMT

 ### Meeting Duration: ~ 1.17 hours
 ### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/147)
 ### [Audio/Video of the meeting](https://www.youtube.com/watch?v=snEdgekxJto)

 #### Moderator: Hudson Jameson
 #### Notes: Sachin Mittal
 
 ---

 # Summary

 ## EIP Status

 EIP | Status
 --|--

EIP - 2456. EIP - 1962, EIP - 2348| Discussed under EFI. Discussion to be continued in EthMagician thread 


 ## Decisions Made

 Decision Item | Description
 --|--
 
 78.1 | EIP-2387 - Ropsten will be moved forward, ahead of mainnet. 
 
 78.2 | EIP-2456 - Time based approach will be better 
 
 78.3 | EIP 1962 - Discussion to be continued in EthMagician thread.
 
 78.4 | EIP 2348 - Discussion to be continued in EthMagician thread.
 
 78.5 | EIPIP Meetings will start from next week. 
  



 ## Actions Needed

 Action Item | Description
 --|--

 78.1 | ECH and James will do postmortem on Nuir Glacier, and Istanbul fork. 
 
 78.2 | Peter will add new messages (announcing transactions) to solve the transaction 
 propagation problem.
 
 78.3 | Peter will look into the issue of geth sending bad blocks. 



 **Hudson**: Welcome everyone! 

 ## 1. EIP 2387 Muir glacier updates

 - **Hudson:** I think ECH is reviewing it, pooja and tim can talk about it.
 - **James:** I can talk about that, so at block 9,200,000 we had the muir glacier. 3 out of 4 clients were perfect, and 4th client had a quick update after the fork without any negative effects. And that fork included the EIP for pushing back Ice Age. Now block time are reduced to fastest, then it took a day for block time to reduce to normal. 
 - **Hudson:** Alright, also is anybody from ECH is doing a postmortem?
 - **Pooja:** I am not aware about the postmortem of istanbul, but we were discussing to work on that. 
 - **James:** I am doing one for Muir Glacier, we should also do one for Istanbul. 
 - **Pooja:** Muir Glacier did really good, as percentage of readiness was more than Istanbul, 
 it was 92% at the time of the fork and it has further increased to 99.5%. 
 - **Hudson:** Alright. Any other comments?
 - **Tomansz:** We should move the ropsten block forward, incase we realize ropsten will be faster than mainnet. 
 - **Hudson:** Good call, like it should be earlier in general?
 - **Tomansz:** Yeah, testnet before mainnet!
 - **Hudson:** Actually we didn't care for this one much, since it didn't really affected the testnet. 
 - **Pooja:** Expected window for both mainnet and testnet was 48 hours, but ropsten got delayed and it is now coming around on Monday. 

 ## 2. Testing updates

 - **Hudson:** Any updates?

 * No response. 

 ## 3. Eligibility for Inclusion (EFI) EIP Review

 ### [EIP-2456](https://github.com/ethereum/EIPs/pull/2456)

 - **Danno:** It is about moving the upgrades from being block based to time based. Time based fork is a tricky issue, there's a plently of ways to introduce Noatak vectors and ways to make things more complicated. My main motivation for these is the past two fork blocks, because of the ropsten and mainnet proof-of-work forks. They were all off by atleast three days and as I mentioned earlier in the call, ropsten at its current rate is going to fork probably next monday which is about a week after our intended fork time and there were times where it was forecasted 2 week afterwards the intended timeline. This type of unpredictability is incredibly bad for our downstream partners as they have to maintain nodes and run exchanges. 

 - **Danno:** Forking on timestamps create some problems though, there is issue of reorders as if we forego specific time and there's a reorder that includes the block number, giving miners the opportunity to force forward a fork. Although geth parity only accept block fifteen seconds in future, but I don't know about others. Otherwise also, there are all sorts of difficulty as we are trying to fork a specific block which could have been random. 

 - **Danno:** First proposal: The network upgrade only transition at block numbers that are round by thousand. Second Proposal: We do a two-phase commit i.e we do a transition at the second opportunity where block number is thousand after the fork. So this gives us a big window where we can say that upgrade will happen at an average of 1500 blocks. Following this, there are some calcualtions which suggest upgrade will happen between 2 to 20 hours post the fork which is a lot narrower and more manageable. Theoritically, you can have someone working full time over this window rather than putting someone all the time for 20 hours. 

  - **Danno:** Ethereum Magicians were concerned about the armors, that if there are additional rules that might change the header validation. How the manlicious minor might do the ommer of transitioning eligible blocks. Luckily, two-phase commit is going to limit that window. And then again there are economic limitations on its effectiveness. 

   - **Peter:** I just want to stress that my main concerns are malicious miners doing wierd things. For eg. If one block is forked and goes onto the next block, but the uncle block remains in the previous one. Or else, where uncle is already forked but the block itself is not forked yet. Since the uncle and block timestamps aren't really tied together. I think problem is to identify a behaviour between block and uncle timestamps so we don't accidentally get into a situation where one client rejects something and other doesnt't. 

   - **Martin:** The issue peter brought up, I have wrote it on fellowship and I have edited it since I realised that it is based on a misconception. If I understand it correctly now, your proposal still activates on block number so an ommer would never activate before the block. And the whole timestamp just opens up the window saying from 1000-2000 block forking will happen. Essentially, once the fork has happened we don't even have to pretend that we had a timestamp rule. We can just set the fork number and hard code it there. 

   - **Danno:** Yeah, because we never had a 1000 block rewind so that's going back and forth on the decision whether to make the number canonical or sticking to the date. 

   - **Peter:** Yeah, but is there a reason of removing dates?

   - **Martin:** Yes, because it makes the process easier. Where we can do checks on the specific block if the peer has them or not. We can check if it is on the right side of the fork. 

   - **Danno:** The reason I went back to dates is because it needs a permanent number and it has to deal with 21-24 interactions and since we don't know the future block, we will be advertising a future time. This how, we don't have to change our has nearly as often. Otherwise, there might be difficult time theory based on that identifier and I did mention in the blog that clients might want to include both the fork number and the fork time. So, during a fast sink, you could use block number to make sure that you are doing it correctly but in all the synchronization methods right now everyone's getting all of its header anyways and since you are checking every 1000th header it shouldn't be too much of a validation burden on fastings. 

   - **Peter:** Oh, you do have a point but if we type working to timestamps then the fork id gets messed up because the fork id is designed to work on block only so it will have to be redesigned. 

   - **Danno:** Yeah, so I think we can just put unit seconds past epoch until we hit block number one billion or something, we will be fine. 

   - **Peter:** It's not too hard to fix but it is something we need to address. 

   - **Hudson:** Alright. Any other comments?

   - **James:** If I look on the etherscan, the block timings are very irregular so I suppose this will help us get more consistent block time. 

   - **Danno:** So, What's hitting us on ropsten is that, hash rate is much more highly variable then it is on mainnet. There's no economic incentive to keep your hashes pointing to make money. Essentially, the hash rate is unpredictable. Also, there has been previous evidences where due to time difference and unpredictable hash rate, there is a big window of when fork will happen. 

   - **Tim:** We can create a 2-step alert model around 2000 block delay of this proposal. And make  the window of predictability of fork smaller. 

   - **Hudson:** I think time-based approach will be better if we can pull it off. 


   ### [EIP-1962](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1962.md)

   - **Alex:** So, C++ and Rust implementation are complete, both feature and testing wise. Rust is used in-between for gas estimates. The remaining part is to how to implement it in existing clients. I know only parity and geth. For parity, its easy to implement but for geth it is difficult to implement either in C++/ Rust. It would require some additions into the existing continuous integration pipeline. So advices around are welcome. 

   - **Peter:** From ethereum-go team perspective, we can easily integrate C++ code into GO. But not rust, it will nuke the entire project. Otherwise, while using GO as a build tool, it will require make and custom files which we definitely don't want to build. 

   - **Alex:** I faced some problems in the C++ implementation. Maybe there is compiler version/ linux distribution issue. 

   - **Peter:** For the compiler, GO just uses GCC and there is no issue there. But if you have any other issue.

   - **Martin:** Alex, I just read the comments that map 10 separate operations with compiler address (10 pre-compiled addresses) and I looked at the EIP but I haven't seen those changes on the EIP. 

   - **Alex:** Okay, I will make a correspondence thread in Ethereum Magicians. Also, how can I collect those pre-compiled addresses?

   - **Hudson:** Is there a process of deciding these pre-compiled addresses? To All on the call? Is that something we just decide and call?

   - **Danno:** Typically, this is how it has been done.  

   - **Hudson:** I am just thinking of the pros and cons, how soon do you need it Alex?

   - **Alex:** Its required by the clients, but I will just leave a placeholder for now. My another question is about the performance margins, i.e. when different implementations come in future and someone want to integrate my implementation so can I just give the performance margin to them?

   - **Peter:** Problem with them is, For instance the margin is 10% and nobody is cares but when you start entering the 2x, 3x territory, it will look as a DoS attack and you would want to double the gas price. 

   - **Alex:** Yeah, I need advice on this. Maybe can I compare with the current PM curve? Or maybe I can put a placeholder of 1.5/2. 

   - **Peter:** SO current way of deciding the gas prices, is to run multiple implementations on multiple benchmarks on multiple different machines. Get all the numbers, and then just try to compare it to the existing op code. But just to be on safe side, if we have a code with a benchmark, we can quickly dream some numbers. I think martin has some benchmarks.

   - **Martin:** Yeah, but the whole thing requires us to be fairly certain as the worst cases are not that trivial. 

   - **Alex:** This is large part of my work, because I did the gas schedule i.e. I have the formula having independent input paramaters which I have narrowed down to 4 parameters. For eg, if you multiply the elliptic curve point by a number which is in a certain range of bit width, worst case is all bits are 1. So, having addition and multiplications actions on this basically doublings. All those numbers were used in gas estimate and are worst case right now, I can just give a margin on top of this. 

   - **Martin:** But now there is another problem as gas scheduling alters the model of worst cases. Now there will be new worst cases due to the gas schedules.

   - **Alex:** What new worst cases?
    
   - **Martin:** Worst cases - talking the most time per gas. So, previously we used to compare the relative gas per second. For eg, easy to recover. 

   - **Alex:** Okay, I used the standard measure off 15 million gas per second in my gas schedule. 

   - **Martin:** Yeah, but when you do that you get heavily tied to the processor. So, you can calculate pre-compiles like easy to recover on the machine. 

   - **Alex:** Can you please point me to some example, like some existing code?

   - **Martin:** Yeah I can send you the example repo. 

   - **Alex:** Yeah, I will then just measure these constants and make adjustments. 


   ### [EIP-2348](https://github.com/ethereum/EIPs/pull/2348?) 

   - **Danno:** I just now gave responses to the concern in the Ethereum Magicians [Forum](https://ethereum-magicians.org/t/eip-2348-validated-evm-contracts/3756/8). The first concern was about "Validating in Transactions" and my principal arguement was that contract can't be too long. I have put numbers to support my arguement. Second arguement was about "why header and not some other mechanism to identify contracts subjected to validation rules. Strongest arguement was to change the delegate call to take off 6 instead of 7 arguements from the stack and if you were to put that EVM, things would break whereas if you use version header. Things would be much more quicker, and more effective. So I am not ready for a vote on this till next month. So that I can solicite the responses. 

 ## 4. EIPIP (EIP Improvement Proposal) Meeting
    
   - **Hudson:** This is meeting going to start from the next week. It will organised on telegram. Reach out to hudson@ethereum.org if you want to get included. 

   * Purpose of these meeting - Look over and streamline some of the EIP processes and also create guidelines and actionable ways to attract EIP editors. 

 ## 5. Review previous decisions made and action items

   - **Hudson:** All clear!

 ## 6. Next Call 

   - **Hudson:** Anyone wants to add anything?

   - **Louis:** Discussion about max transaction size to get accepted in mempool, this limitation can be problamatic for the layer 2 solutions in the future. Martin is getting it solved. 
   
   - **Peter:** Upon today, geth refused to propagate transactions larger than 32 Kb. Since there 
   may be transactions having large amount of data, but they are not deploying anything. And this will result in larger tx size, and will be refused by geth. But we don't want any DoS. So, Important memo is geth will allow larger transactions from the next release. 
   Currently, method of propagating transactions by nodes is horrible. Actually, node relays 
   every transaction to every peer. So, in case of some wierd connection, someone may miss the transactions. And current ethereum networking protocol doesn't have a mean to request transactions if missed. We would propose adding two new message types, to propagate a block and to just announce and request a block. Same way, We would like to extend the date of transaction so that beside the current message, so that we can propagate and announce that transaction. This will drastically reduce the ethereum network bandwidth. 

   - **Tomasz:** When we connect nodes to each other, I think geth is sending all the trasactions to the connection. So, is it possible  to change it so it only sends hashes. 

   - **Peter:** Exactly, so if we support announcing transactions. Then it will enough to announce them on connection and not propagate them. 

   - **Tomasz:** That will be perfect, I think it is about 80-90% traffic on the network. 

   - **Peter:** Solving the transaction propagation problem is very trivial. So, we can a new version protocol released and see if it actually works. And then we can look into block propagation, as it is not really issue though we can make it optimal but transaction propagation is annoying. 

   - **James:** We need to come up with a better design for keeping track on EIPs. 
   
   - **Hudson:** We have ACD gitter, and Ethereum magicians thread. But I totally agree, I think we should include this in EIPIP meeting. 

   - **Louis:** I was wondering if the Ethereum networking issues are standarized or discussed as a part of protocol itself? My impression from outside is that, they are designed adhoc by the clients. I am correct?

   - **Peter:** I don't think so, since the whole networking protocol was pretty much standarized even before frontier, and we generally use IP processes to make the changes to it. Other discoveries like e5 were pursued independently of the core dev call.

   - **Tomasz:** There are couple of things in networking which will benefit if standarised. Very particular eg from nethermind. So, when we are sending request from the node in the fast sync mode, the requests are handled both by parity and geth. The way we are optimizing it is, we create request patches first and then we decide whether to send it to parity or geth. Limit for the size of request in parity is around 1024, and it geth handles 192-256 requests. TLDR, there are small small details which are not specified. So, we should introduce some meaningful messages on this connection. Right now, we have to run to debuggers incase node gets disconnectedd and we don't know the reason. And that is extremely time consuming. So, I think we should improve this and add more detailed specifications. 

   - **Peter:** Just reacting to one thing, so we definetely don't want more data than a limit. For eg, if you request 1000 state entries, you only get 330 in return. 

   - **Tomasz:** So, I am talking about node getting disconnected. Not the data. 

   - **Peter:** So, you probably want to open an issue. Since we never intend to disconnect just because you have requested more data. 

   - **Tomasz:** Sure. Also, I would suggest we inspect such details and build a better communication when it comes to client like geth. And include core devs in the process. 

   - **Peter:** That's why we had this fork idea, as we wanted to bring it as an EIP to address this transaction propagation issue. 

   - **Louis:** Continuing on this discussion, I feel core dev didn't discuss the reports on the attack that occured just before new years eve.

   - **Peter:** Was there a attack?

   - **Hudson:** Yeah, the attack on parity. 

   - **Tomasz:** Yeah, it affected both nethermind and parity. And there is a separate forum of 10-20 people discussing it. So, the attack was that there was an incorrect block being sent and then parity was adding it to the cache of the incorrect blocks as the hash of the header. Then block was validated but it was blowing the processing and it was added to the hash as the invalid block. But there were perfectly valid blocks on the network with the same hash. So different hashing mechanism has to be introduced. 
   Though same thing affected nethermind, it was slightly different in our case. As we missed the validation of some of the new incoming blocks and we added that and it solves it as well. 
   And parity already has a fix, where they has the raw content of the block and stores it separately, and discards the block if hash of the invalid block is exactly the same. 

   - **Martin:** Essentially, geth is picking up bad blocks and storing them in bad block cache. And I guess parity flags a particular hash as bad but difference is that we don't actually use that blacklist in the future. We just keep a view from the outside. And once we get the correct body content for that header, we import it. 

   - **Tomasz:** Do you blacklist them before or after the transaction propagation?

   - **Martin:** No.

   - **Tomasz:** Okay, so we blacklist and never propagate them. And we blacklist it after full processing and if everything matches. 

   * I am pretty sure that attacker was using modified code to generate the connections and send the blocks because they were definetely coming from the geth nodes but they might have been modified. 

   - **Peter:** I will look into it. 

   - **Tomasz:** I will share the discussion from telegram channel about the same. And we will try to figure this out in two three weeks time. 

   - **Hudson:** Great! I am going on a trip for next two weeks, so tim will be taking over. 


 ## Attendees

* Hudson Jameson
* Alex Vlasov
* Daniel Ellison
* Danno Ferrin
* Gandalf
* James Hancock
* Louis Guthmann
* Martin Holst
* Pawel Bylica
* Peter
* Tomasz
* Trent
* Tim