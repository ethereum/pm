# Execution Layer Meeting 164 Notes <!-- omit in toc --> 

### Meeting Date/Time: Thursday 22 June 2023 at 14:00 UTC <!-- omit in toc --> 
### Meeting Duration: 1.50 hours <!-- omit in toc --> 
### [GitHub Agenda](https://github.com/ethereum/pm/issues/808) <!-- omit in toc --> 
## [Audio  Video of the Meeting](https://www.youtube.com/watch?v=09Kzi2x06UM) <!-- omit in toc --> 
### Moderator:: Tim Beiko <!-- omit in toc --> 
### Notes: Avishek Kumar <!-- omit in toc --> 

—-------------------------------------------------------------------------
# Agenda <!-- omit in toc -->

**Tim Beiko** [1:45](https://www.youtube.com/watch?v=09Kzi2x06UM&t=105): Welcome everyone to Execution Layer 164. We have the folks from the execution specs repo that wanted to give a quick presentation on the testing framework today. They have to hop off, so we'll start with trying to time Box it around 10 min, and then. We can do some questions and conversations about it at the end. If we need more time. And then after that we'll discuss a bunch of the Dancun stuff. And finally, the ERC’s EIP’s we both split at the end. Yes. Dan, you're the one.

## [Execution Spec Tests overview](https://github.com/ethereum/execution-spec-tests)

**Dan** [2:33](https://www.youtube.com/watch?v=09Kzi2x06UM&t=153): Yeah. Hi, everyone. Can you see the screen?

**Tim Beiko** [2:37](https://www.youtube.com/watch?v=09Kzi2x06UM&t=157): Yeah. We can. Go for it.

**Dan (danceratopz)** [2:40](https://www.youtube.com/watch?v=09Kzi2x06UM&t=160):  So okay, perfect. Hello. One. Yeah. Thanks a lot for the opportunity for us to show the new execution spec test rapper. So I'm done. I joined the EF testing team just in April, a couple of months ago, working alongside Spencer and Mario and Dimitri who are going to help me with this presentation. So, the testing team just before we jump to the red phone, I mean just to broaden the scope a little bit. We, you know, our aims are really to ensure the input like client implementations for features, for upcoming political upgrades. You know, they meet spec. And, you know, sometimes suspects can be a little bit difficult to interpret, you know. Maybe not so clear when you actually come to implement it. So we also try to provide a source of truth. the client implementations for teams to meet. And just more generally, though, we'd really like to help the entire ecosystem improve the development cycle. So we really want to help all the client teams with a faster cycle for that work. So, you know. I just started April and Spencer started in January. So we have a bit more capacity, and you know we'd love for you to get in touch and then give us ideas and feedback. let us know how we can help you, and if it's in the scope like that, we can scale it in our relatively small team. Then we're happy to do it. 

# Execution-Spec-Tests-Background

**Dan (danceratopz)** [4:04](https://www.youtube.com/watch?v=09Kzi2x06UM&t=244): Okay, moving on to the repo. So just a quick background. I mean, it's a framework and a library that enable the implementation of test cases for execution clients in python as source code and like a client, started the initial development at the end of 2021 just to explore, like a different approach to writing test cases for clients. And then it didn't like receiving initial use adoption. But after discussions in Devcon, people liked the idea a lot and test case development started as early as late last year and the focus being on new tests for Shanghai, So for the upcoming release. And now we think it's a good time to show you the stuff because there's been a lot for you for test coverage added to this framework or to this repo. And there's been a lot of framework improvements and some new online Doc generated, which makes it helpful and good to use. All right.

# Ethereum Test

**Dan (danceratopz)** [5:20](https://www.youtube.com/watch?v=09Kzi2x06UM&t=350): So most people here will be familiar with Ethereum tests. So what's different about this approach? with this repository?  So you're in tests like tester employment is YAML. And here the test cases are implemented as python code. the other differences. The repo itself contains the tooling or the libraries and the framework to and to generate, fix, just using transition tools. and this helps avoid the two-step approach that's used in ethereum tests. where some YAML spec gets checked in which is perhaps generated from some source code which it's often not available. And then from the YAML spec Jason, fixtures are generated generally from I think it's we testy. So why do we like this approach? And I mean, basically, the main reason is we have test cases code. I mean.  from this, we have readability due to the structuring of the repository. We have a single step to generate. Jason fixtures, test clients against as code. The test cases are easily parameterizable with a few lines of code. the test cases and framework a version together, which means you'll never have any clash between like different versions. And it should just work. The code is easy to modify. The documentation is in line with the source code, so you can generate beautiful documentation from the test cases. And all this makes it a lot of fun to implement tests with. And you can drop into a debugger, check the state of your test, and so on. So  we're looking. We're focused on the big, long box in the middle of the execution spec test. So on the right, you have a command line using the framework fill and you refill tests and the test cases here on the left in the test directory. and these use external tooling the Evm binary from Geoff. Currently. So a quick comment about that is the transition tool from Evm. One should soon be integrated. And we'd really love it, like all client teams. to have a transition tool available, and we'd be very happy to integrate it in this framework, if it is  yeah. So this using this stuff we also used to see just to compile some you and based on this, we generate output, which are fixtures. Jason files. We shouldn't be consumed by the test cases and consumed by clients and hives. All that our client excuses was directly.  So now we're gonna have a quick look at more detail about the test cases themselves. So I'll handle it's expensive for an explanation of what kind of tests. We have Spencer

# Types of Test

**Spencer** [8:00](https://www.youtube.com/watch?v=09Kzi2x06UM&t=480): Thanks, Dan. And so, yeah, so those familiar with the theorem test, we know that we have 2 test types, State tests and Blockchain tests to summarise them quickly. State tests are designed to verify the behaviour of a single transaction or operation within a block. Whereas blockchain tests focus on the effects that occur from a box of block interaction in the ethereum state. It's worth highlighting that, thanks to Mario, we now also have transition tests. And these are a branch of blockchain tests, where, for example, block 1 and block 2 could be in Shanghai block 3 in Cancun, highlighting the transition there. So all of the test cases so far have also generated documentation. Many thanks to Dan, which you're showing off here. This example here is probably one of the most basic State test cases that exists which simply verifies 1 plus 2. But it helps us paint the picture a little clearer. So at the top of the test case. We specify from what fork the test is valid from. So here we've specified Homestead. This enables the test to be filled multiple times for each fork from and including Homestead. We have the pre-state where the first account holds some yield compiled byte code for a simple S or of add operation. a transaction from the test address to the first account which executes the and then the expected post state, with the result of the ad operation in storage. So yep. 1 plus 2 equals. 3. Now it's off the page. and we have this command line. And so the python code here can be filled using this command at the top into the client. Consumable. Jason file. Okay, so this is a simple single test case. What if we wanted to expand on this. and, for example, easily specify different parameters for the add operation or even change the opcode we're using well with a new framework. We can use pi test parameterization. And so this test here is for point, evaluation, pre-compiles. And specifically for invalid blocks. And we have a bunch of cases here. And so this test case is marked valid from Cancun. And, as before. if we scroll down to the bottom a little bit of the test. We have the Pre and the post and an individual transaction. But instead of these being defined inside the test function. And they are defined outside the test function as a global pi test fixture. Now, these allow us to use them within other test functions where the values input into the test functions are entirely dependent on the parameterization of the test. So here we can see we're parameterizing by the specific point evaluation vectors. And the main idea. I want to get across how easy it is to add another test. Vector for this case, if anyone here can think of other examples for an invalid precompile call. All you essentially have to do is add to the list of parameters and specify a descriptive test Id. That describes the New Test case added. And so, yeah, super simple. And if anyone is interested, please feel free to contribute. If you want to know more about the specifics of each test from the docs. You can look into the source from the link@thetopofeach.page. So thanks. And yeah, I'll pass you over to Mario.

**Mario Vega** [11:40](https://www.youtube.com/watch?v=09Kzi2x06UM&t=350): Thank you, Spencer. So yeah. Over the course of the last couple of months we've been using this repo sensibly to test the 4844 -EIP, and basically the EVM changes to the 4844. So that comprises the block type (3) Transactions, which is the minimal version of the BLOBHASH opcode of code. The new block headers which are ExcessDataGas, DataGasUsed Header fields, and also the precompile at Point Evaluation that was already highlighted in the example before. So I really want to highlight a great practical example of the efficiency of  And this is our recent spec change in 4844, which is the value of it's maximum blocks per block count. So originally in 4844, the maximum number of blocks was for. and it was just recently It was a day to 6, and with this parameterization we were able to simply update one single line of test code and the test cases for all the new combinations were automatically generated for us. Lauren said. We did need to prepare experimentation, parametrization code beforehand to account for a change like this, and also this side of change. At this moment, this manual, since we are currently from the Python test code, we do not, far as I can from that. But and yet this definitely made the process much quicker at the time of the change. And it's also mentioned that we can do this from this change over and over again. We can just change back to, to forward, or to it, up to 8, or whatever to speck that defines. And here on your left, you. You can see the original number of test cases with for maximum 4 blocks, and on the right you can see the new status. So a great thing about  the new documentation is that you can go inside the doc and see exactly what we have implemented in exactly all the numbers of this thesis. So in this case we have the Block transactions test cases. As you can see, every single test case that was developed, and you can go and and and just look at the test case and and just  if there is any cooperation using, or if there is a particular desktop that you feel that it's not just by this you can definitely, we are open to feedback. And we can. Obviously you add more test cases as much as needed. And just to finalise. Here we have both the links to the repo and and the link to the documentation preview. So please feel free to access these links and so on. As I already mentioned, all this is currently implemented. You can see them in this stuff review. It's very, very cool and if there's any coverage missing it just specifically to reach out, and we will and make sure that we include more, more test cases. So any, I think that's it from us. Are there any questions from anyone?

**Tim Beiko** [15:03](https://www.youtube.com/watch?v=09Kzi2x06UM&t=903): Ruben,

**Ruben** [15:08](https://www.youtube.com/watch?v=09Kzi2x06UM&t=908): Yeah, I just wanted to ask, will there be any? Pre generated Jason files hosted because I noticed that there is a Shanghai Jason files are now in the Ethereum  tests repo. Right?  Yeah, definitely. So

**Mario Vega** [15:20](https://www.youtube.com/watch?v=09Kzi2x06UM&t=920): Definitely, we, we, the current release that we were following. It's up to change if but basically every release, we package all the generated Jason and fixtures, and we back them as in our 5,  and we upload that. Next to the release, we have 2 kinds of releases, which is the current main version. So we have all the tests for the main it for what's making minded now, and we have the upcoming fork release tool. So right now we only have 4844. But we will, We plan to include all the EIP’s for cancun , so we will have a cancun release, which will contain all the all these files. As for when the release is coming. We we are planning to release it very soon, and we are finishing up the change to the framework. So when we, when this is on. We will release the new framework, and we also. We will release all the pretty generated pictures for you.

**Ruben** [16:30](https://www.youtube.com/watch?v=09Kzi2x06UM&t=990): Thank you.

**Tim Beiko** [16:37](https://www.youtube.com/watch?v=09Kzi2x06UM&t=997): Any other questions.?

**Dimitry Khoklov** [16:49](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1009): Hi, this is Dimitri's former pre-tested developer. And I, it's really cool to see what you guys are doing. The pi tests and sink is really cool, especially as a parametrization part. But what I also want to say I would like to deliver the message to client developers to implement that transitional protocol that we are using to generate the test. This is a transition tools used both in python, and currently, in the tested which is still maintained and generates all the tests in the room test repo and as many clients implement the transition tool, we would be able to run the test and generate the tests. And using python, for instance. And I see all this new implementation and new EIP’s because of transitional implementation from a calendar. So I really encourage clients to do that. It's not so difficult. And then, yeah, I would like to see more teams joining in the cloud. Come on.

**Tim Beiko** [17:58](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1078): thanks. any final questions, comments?

**MH Swende** [18:03](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1083): Yes, I have one comment. And yeah, I'm at the market. Just a comment to what Dimitri said. So, at least in the case of Get the t8n, an implementation  does not correspond to get execution. It is written to be correct, and it's written to be and use as a back end tool for generating tests. But it's not as reliable as this executor and test runner as the execution of the State test. So I don't think it should be used to test like get compliance seat. You should not. That's it.  It might be the same for all the clients. I don't know.

**Tim Beiko** [18:53](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1133): Got it.

**Marius Van Der Wijden** [18:54](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1134): Yeah, I agree, but in general it it is very nice for everyone implemented this because then we could start implementing You test in a new EIP’s and other clients right now, it's  basically only really possible and guess and and maybe be so. to implement a new feature and fill these fixtures. So if the clients also implement the t8n tool it would be really nice too. So we can. So like, researchers control to type in their favourite language and don't  always need to rely on Consensus to do it.

**Tim Beiko** [19:48](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1188): Okay, any other comments, questions about application tests.

**Danny** [19:58](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1198): My phone crashed at 1 point. So maybe I missed it. But is there? the ability to fill with eels?

**Marius Van Der Wijden** [20:09](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1209): They're working on it, as far as I know. 

**Mario Vega** [20:16](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1216): Yeah, I think I think there's a gate and support. And as long as they have that we can, we can definitely use them too.

**Danny** [20:29](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1229): cool. Yeah, I mean, I, as most of you know, on the consensus layer, you know, we write kind of the python specs and simultaneously get to do testing and filling out of that. There are certainly drawbacks, but it allows for pretty rapid generation of test vectors along with the spec building.

**Mario Vega** [20:53](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1253): Definitely, I think a deeper integration is definitely possible. and it's something that we should definitely do. it would definitely, for example, right now, we depend on manuals of this, as I mentioned, for 4844 because once the spec is available, we have to manually go inside and change, maybe some one or 2 parameters for the, for it to be up to spec.  But yeah, ideally you should be, you should be able to make it. If we are free of the I'll suspect we should also somehow consume this update in the indexation factors. And also I'll automatically update the test definitely.

**Danny** [21:40](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1300): The other thing is, I'd love to talk to you about the consensus spec test. Just I think they could do some. They could do some documentation. I'm sure there's a lot of things we could clean up so it may be worth chatting soon.

**Mario Vega** [21:58](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1318): Definitely, that is, is the mastermind behind the documentation right now. He was the one that was good of all the python scripting that was necessary to automatically generate from some to the duck strings of each test case. We basically just grab that. And then just your protection.

**Danny** [22:22](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1342): Very cool. I'll still write the test. I promise. I just, I just want some help to make them pretty.

**Tim Beiko** [22:36](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1356): Cool. Anything else. Okay, well, thanks a lot for the presentation guys. and yeah, people can reach you on the or any discord to provide feedback or ask questions. okay. 

# Dencun Updates
### [Update EIP-4844: Update precompile address for 4844 EIPs#7172](https://github.com/ethereum/EIPs/pull/7172)

**Tim Beiko** [22:58](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1378): Next up we have a bunch of Dancun updates. so first just a small change to the 4844 precompile address. Alex, open the PR, I don't know if there is any context, you want to add, but it seems pretty straight.

**Stokes** [23:17](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1378): Yeah. I mean, I was just looking at the compiles for 4788. And I just noticed that basically 4844 was not tightly packed in the sense of just, you know, having the one right after the current last recompile we've added on may not and this EIP, or sorry it's PR to suggest putting it there.

**Tim Beiko** [23:41](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1421): I guess. Does anyone disagree with that? Then, if not, we can have this for the next Devnet. Devnet7.

**Marius Van Der Wijden** [23:52](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1432):  just as a background. It was like, the gap is because of the Bls pre compiles, but I agree we should tightly pack them and the pos 3 compiles on and not going to be on may not. this, folks, looks good to me. 

**Danny** [24:11](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1451):  So we probably should simultaneously adjust the DS precompile EIP, just so that we don't have conflict if there is testing on that.

**Tim Beiko** [24:22](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1462):  Yes.Alex is going to do it.

**Stokes** [24:28](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1468):  Other than me. And I'm not sure that, like 2537 is exactly what we'll even go to in May, not eventually. So I'm not super sure but.

**Danny** [24:38](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1478):  you could even add it like plus 8 or something just good to get out of the conflict zone.If you don't.

**Stokes** [24:45 ](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1485): Sure.

**Tim Beiko** [24:52](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1492):  Okay, so perfect, let's make the change on 4844 and then reflect it on 20. DS EIP as well to not yeah, to not have a conflict there.  and then, Alex, your second PR on 4788. You want to give some context on this one.

### [Update EIP-4788: Bound precompile storage EIPs#7178](https://github.com/ethereum/EIPs/pull/7178)

**Stokes** [25:15](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1515):  Yeah, this one is much more involved than when we just discussed. So we had discussed 4788, as a very quick, brief reminder. This is taking the beacon block route, which is a cryptographic accumulator, so you can make proofs about it to the State taking this route and putting it into the evm. It unlocks a lot of cool applications. you can go to EIP to see a little bit more about that. and we've had a little back and forth on exactly how to implement this with the api looks like. alternatively, there's a pre compile that will expose these roots. And the one thing that was essentially like, yeah, what is the PR of how it look like just going off of, like the data the EL has, they have like a timestamp. And then, like the really handy. So the question becomes, okay. you know, do we keep the essentially Api to the reconciled by, like the timestamp by the routes? How does this work? And there's like some different options here. One option is just to write by a timestamp but there's not a nice way to basically then bound. How much storage this thing uses, which generally is nice. We don't want this unbounded thing growing forever so like 5 - 10 years from now, you know you look at this precompiled storage, and it's, you know. gigabytes something like that. So, anyway. point being I made a pass on changing how these things are stored so that the storage is founded. There's only a certain number that will ever be in the pre-compile storage.  And yeah, the only thing that's a little funny is. Basically, there's 2 ring buffers, simply because if we only had one ring buffer, so if we have a ring buffer. Then we can bound the storage, because basically, for every timestamp there's like one sort of slide goes into the issue. There is that if we have a missed slot on the CL. or just in the chain. Probably. Then, what's gonna happen is you basically have like a prior rights that would then basically correspond to a later timestamp. And this could theoretically be used to like, you know, attack some gap. Let's say, that's like using this. So that's no good. And the way you get around this is just basically record both the timestamp and the route and one more caveat from there, just because you know the storage size of these things is only 32 Byte, and the roots are 32 Byte I can like tightly pack them into one storage slot in the in the state. And so now there's like 2 ring buffers. So if you look at this, there's quite some change. But it's mainly just this complexity around doubling these 2 ring buffers into the evm storage. But otherwise it should be pretty clear. And yeah, I think at this point, I mean, I'm happy to answer any questions if something wasn't clear. But yeah, please take a look. I think this is essentially the best option just based on all the constraints that people invoice. And yeah, I. This looks good. We'll merge it. And this EIP will pretty much resolve for cancun. Okay? Good.

**Danny** [28:33](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1713):  Oh, yeah, it. It's kind of a funny approach when you first look at it. But I do agree with that. given the constraints that it is actually a really solid solution. I guess the other design option could be like instead of 2 ring buffers have ring buffer where it's, you know. and then, and plus our you stagger you, you, stagger them rather than having them is totally separate. But this is totally fine. I like it.

**Tim Beiko** [29:09](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1749):  Any other Questions? Comments?  Okay, so yeah, folks want to review that. And then assuming there's no issues we could get merged in the next couple of days. 

### [Add MCOPY tests tests#1229](https://github.com/ethereum/tests/pull/1229)

**Tim Beiko** [29:33](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1773): Okay, next up Powell just wanted to share. I don't think he's on the call. I think he could make it. But there's the M copy tests that have been merged. So I'll put the PR. Here. But if clients I want to test against that and I see already base you in it. Theorem. JSON, say that they pass the test there. I don't know if anyone else had thoughts, comments on that. 
### [Engine API: Cancun specification  execution-apis#420](https://github.com/ethereum/execution-apis/pull/420)
[https://hackmd.io/@n0ble/deprecate-exchgTC](https://hackmd.io/@n0ble/deprecate-exchgTC)

**Tim Beiko** [29:59](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1799): Okay. And then, if not, Mikhail, you had a PRpr for the Cancun engine Api Spec. You want to give some quick contacts on that.

**Mikhail Kalinin** [30:12](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1812):  Yeah. sure. So yeah, there is a PR open with the and there is thee The aim is to merge to get it merged like next Monday. This kind of last call? yeah? And was. What's in these specifications? Basically, the main thing is blob extension specification. and that everyone is very familiar with. The other one is exchange, resolution, configuration, the application notice, and the most recent thing that was added is the payload attributes version 3, and the fork choice. Updated version 3. This is to accommodate the parent beacon book route and make it into the payload bill process.  because we need a parent beacon block route because of the EIP, that is 4788 so that's basically it. And more eyes on it, would be great. So if you have. look before Monday, that'd be great. Also, yeah. i really appreciate more approvals on that PR. Any questions related to the cancun back of the engine Api

**Danny** [31:32](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1892):  Did the 4788 changes make it in there, or do they still like it?

**Mikhail Kalinin** [31:36](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1896): Yeah, yeah, they are there. So

**Danny** [31:39](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1899):  All right. Good

**Marius Van Der Wijden** [31:45](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1905):  It might be a stupid question. But how do we get this timestamp for the parent beacon block? Can we just take the parent execution. 

**Stokes** [31:59](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1919):  This is for the 4788 question?

**Marius Van Der Wijden** [32:01](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1921):  Yes.

**Stokes** [32:04](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1924):  Well, so you don't like you just have the header that, or has the timestamp, and there's a route, that's all you need to know.

**MariusVanDerWijden** [13:11](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1931):  So we use the parent beacon block.

**Danny** [32:15](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1935):  So it's the current time that the caller needs to map those things together.

**Marius Van Der Wijden** [32:21](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1941):  I see. Okay, perfect. Thank you.

**Mikhail Kalinin** [32:33](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1953):  I don't know if it should be Dancun by the way, because we had Paris and Shanghai before. Yeah, but don't be open to rename it dancun, If People are okay with that.

**Tim Beiko**[32:47](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1967):  Yeah, I don't know if we want to retroactively rename the other ones, but it seems like a given. Both sides use it. and probably makes more sense. But does anything that depends on it? It's also not a big deal.

**Mikhail Kalinin**[33:03](https://www.youtube.com/watch?v=09Kzi2x06UM&t=1983):  Yeah. if we will keep having these kind of like combined names for fork, then it probably makes sense. Yeah, and they are always the server. Yes, that's why it is his name as it is so by why they do that.  It's good for David.

**Tim Beiko** [33:28](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2008):  Okay? And did you want to talk about the deprecation a bit more? I know you had your doc. What did you share? Yeah.

**Mikhail Kalinin** [33:37](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2017):  yeah, sure. So the to deprecate the exchange transition configuration gracefully, we should have a procedure of doing that because if we just drop yeah, because if we just drop the support of this methods in a coordinated fashion, then users might see regret messages and their logs that this added either not being called for some period of time, or it's not exist on the on the EL side when CL calls it. So yeah, I've made this document and the procedure looks really simple. So the first step would be for EL clients to stop walking an error message that if this matter hasn't been called for some period of time for any period of time. and then you all should cut all your clients to release on that. with this change in the release. After that, CL Clients remove this method or just stop calling it. or entirely removing it from the code base and making a release as well. And this release should be either deneb or or or earlier. and after that nothing happens. Yeah, EL clients are pretty to remove it as well. So why, why is this like. Why? Why is this so complicated? At the first round? It's not complicated. If you take a deeper look into that, this is because, just yeah, we should first break the dependence between CL and EL on making these calls, and then we can remove this method. So  this document, yeah, has, like the procedure description, and also has tables with the status of development. So this is how it can be done alternatively, we can do it in a highly coordinated fashion, and say that EL client removes this method, support, and CL client do the same. But these changes are all coming only into the deneb release so strictly into the last release before the fork which I don't think I don't see as a comfortable solution for everyone. But maybe people have different opinions on that. And yeah, whatever we choose, I think that's yeah. Would be great to discuss it here with CL client developers and have their agreement on doing this  deprecation and doing it in the exact way as we come to. So any questions or suggestions.

**Marius Van Der Wijden** [36:33](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2193):  Just a quick thing from us. We already removed this like a long time ago, and no one really complained.

**Marekm** [36:43](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2203):  same plane.

**Mikhail Kalinin** [36:44](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2204):  So the message you mean right?

**Marius Van Der Wijden** [36:45](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2205):  Yes. we only give a message. If we don't receive any updates from the Beacon client, like if the peaking client calls, it doesn't call any method.

**Marekm** [37:01](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2221):  And we are working exactly in the same way. If we don't get any fork choice and a new payload, we print a warning. 

**Mikhail Kalinin** [37:14](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2234):  Cool and to clarify Marius you have removed the message right? But the method handler exists, and if CL Calls.

**Marius Van Der Wijden** [37:23](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2243):  Yeah exactly.

**Mikhail Kalinin** [37:25](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2245):  same for basin. Oh, that's great, basically can if there is no position. So I would say that this is the way we do it, like, remove it from your first. And can you can you guys, mark just make a green check box  on the clients that have already removed the error message I mean, like in these documents would be really useful. So any other EL client developers want to, I mean on that.

**Andrew Ashikhmin** [38:12](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2292):  We've never printed an error message. So yeah. it's already implemented

**Tim Beiko** [38:20](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2300):  So great.

**Mikhail Kalinin** [38:25](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2305):  So we have Besu, Arigon Gath. Never mind. And term JS is one that left right? If it's oh, okay, yeah.

**Tim Beiko** [38:37](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2317):  yeah. So basically, we can just move this to the CL side at this point. And maybe that's great. Yeah.yeah.

**Mikhail Kalinin** [38:47](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2327): Okay, so let's discuss it on this. CL, call next week. Again.

**Tim Beiko** [38:51](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2331):  Cool.

**Mikhail Kalinin** [38:53](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2333):  Thank you.

# Devnet Updates

**Tim Beiko** [38:58](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2338):  Of course. Okay. So next up, I guess I want to do some space. If there are any devnet updates that people wanted to talk about on this. Yeah, anyone want to give us an overview. 

**Parithosh** [39:13](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2353):  Yeah, I want to give a current status. So we had Dvnet6, relaunched on Friday, and where we went through a couple of issues. It's finalising again, but just with the minus upset of clients. So I think the approach we're going to take is to wait for clients to have more stable releases and we launch it cleanly with Devnet7. I can also incorporate the PR, that and yeah, Alex brought up earlier today, and then make a spec list and share it on the interrupt channel.

**Parithosh** [39:46](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2386):  And maybe one of the client teams can talk about the issues we saw.

**Marius Van Der Wijden** [39:52](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2392):  So I can talk about the gas issues. Basically, there were a bunch of them. kind of completely rewrote a lot of the code. So yeah, basically, the devnet is kind of not really indicative of our current code anymore. But the current code should be way better. One thing that kind of led to problems was that we didn't really distinguish between the network or correctly distinguish between the network form and the normal transaction format. And so there were blocks, mind with the transaction in the network format in it. So basically like the block contained the blobs which is wrong.

**Danny** [40:54](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2454):  Even though dev created to get to reject such blocks or acceptance.

**Marius Van Der Wijden** [41:00](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2460):  I'm not it. It was. It was kind of all over the place. I'm pretty sure some clients accepted them. so there was a lot of forking going on at some point.

**Danny** [41:17](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2477):  I see. Alright. I mean, when I hear this kind of stuff I like. can we catch it earlier in the pipeline? Obviously, block production is kind of a weird one. But the acceptance of those she certainly is. Our rejection of those should certainly be in.

**Marius Van Der Wijden** [41:33](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2493):  The problem was that a lot of clients didn't really work 100%. And so, like, there were a lot of things going on. And it wasn't like, okay, only the only guest notes forked off now, but it was more like the whole network was kind of destroyed. Now.

**Paritosh** [41:57](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2517):  And we were kind of relying on Ethereum JS to be like the stable booknotes. But when we started the transaction, so we then had issues with the Ethereum JS as well. So they were kind of like, no stable notes on the network. Yeah. 

**Marius Van Der Wijden** [42:09](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2529):  So now, it's very clear. that this cannot happen anymore on gas. So, but yeah, it's something that I would really like to test out on the, on a, on another devnet and create tests for that. Yes, that's it from my side.

**Danny** [42:42](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2562):  So the question in the chat, I it. It seems very clear that devnet7 should be 4844 for all

**Tim Beiko** [42:54](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2574):  Yeah. does any other client want to share their experience? Or.

**Justin Florentine** [43:02](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2582):  Yeah, just briefly, the basic challenges mostly revolved around RPC interaction and some formatting challenges that we had between the CLs. And there were just a couple of ambiguities. I don't remember anything specific, but they were fairly quickly deduced and streamed out. So That's awesome.

**Danny** [43:25](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2605):  Then hive tests.

**Alexey (@flcl42)** [43:30](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2610):  So continue, please.

**Marius Van Der Wijden** [43:32](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2612):  Yes, this  can be tested by hive tests.

**Mario Vega** [43:37](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2617):  I mean the block with the network type prison section. Right?

**Marius Van Der Wijden** [43:42](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2622): Yes, definitely, definitely, we can. 

**Mario Vega** [43:45](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2625):  I think we can have that index inspectors. And we can consider that. And we should be having a test for that before the next step

**Alexey (@flcl42)** [43:56](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2636):  The pay loads but get the number like that. But we Synchronised and probably it could be a source of such broken phone transactions. I think that for potential  partial devnet 7  it could be probably to make it partially network, because I still think it's not: please our client, or it is fixed little. And to me, if it may appear on devnet 7. There's a same issue.

**Tim Beiko** [45:14](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2714):  I. Your mic wasn't great. but I think I may know most of that. Okay. any other. Oh, sorry. Yeah. Do add something Alexy.

**Alexey (@flcl42)** [45:35](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2735):  Yeah, just so. to confirm that the issue has disappeared. Actually, because now. we're not sure it will not break devnet too.

**Tim Beiko** [45:57](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2757):  So you're not sure about. Sorry. Yeah, you might sort of broke up. You're not sure about what? Exactly.

**Alexe y (@flcl42)** [46:13](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2773):  Because this is a broken form of a transaction netwrok. That's the phone. we'll look for.again. We are still not sure. So  the source is I have open transactions. Which client something?

**Tim Beiko** [46:29](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2789):  Oh, okay, yeah.

**Marius Van Der Wijden** [46:33](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2792):  Yeah, I'm quite sure that it was if but yeah, we just saw too much weirdness going on, for I think only guess to be the issue. So either other clients accepted those transactions. Or it was the other way around that they accepted the transactions without blobs. Like blob transactions without props or something. So yeah, I'm I'm I'm pretty sure we will. We will break another devnet 7. But  that's fine.

**Alexey (@flcl42)** [47:21](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2841):  Okay, but it sounds like this issue.

**Tim Beiko** [47:39](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2859):  Okay? So yeah, I guess devnet 7. we want to restart as a 4844, only devnet and potentially just add this small change for the Precompiler? Or do we even not want to do that, and simply focus on restarting things as they are, and  dealing with the address change after.

**Marius Van Der Wijden** [48:06](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2886):  I think we should deal with the address change when we implement all of the cancun  pieces.

**Tim Beiko** [48:11](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2891):  Okay, so basically keep this thing spec. As for Devnet6, just try to restart it and have it run cleanly.

**Marius Van Der Wijden** [48:21](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2901):  yeah. So what? What's really cool is that Mario created a hive test for 4844. So one thing that would be really nice is if everyone, every client could make sure that they are passing those 5 tests. We are missing one right now. That's the transaction propagation one so transaction propagation is still broken a bit. but yeah. So I would give the devnet another week or something for everyone to  double-check with high, if that they are ping everything that they do. That is like that. We don't see these issues on the Devnet for the first time.

**Mario Vega** [49:18](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2958):  I add the do the link to the PR for this, if you need to help anyone get myself running, just let me know

**Tim Beiko** [49:34](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2974):  Gajinder are you there.

**Gajinder** [49:39](https://www.youtube.com/watch?v=09Kzi2x06UM&t=2979):  Yeah, I can update a little bit about the cmds as well as loadstar. So if cmds had an issue where we were not calculating. The data gets used correctly. so that was how I resolved early on. But most of that, there were no issues in 3mgs apart from the fact that it cmds cannot really have, cannot really handle the ones that can load. So when the team started fuzzing, and you know, put load on it. 3mgs was not able to cope up. So that was primarily the issue with Cmds. so I think next time when we basically fill the network with heavy, heavy blocks we should make sure that you know, there the other EL clients can basically support the network before bringing this. And the second thing about loadstar. Also, today, I discovered a bug in loadstar while Thinking  the blobs. Which sort of I have. Thanks to you guys, I have sort of figured out the fix for it. And but I'm a message loadstar nodes bend down, because we basically wait for Gossip block to see in 32 slots which we didn't see from my debugging at particular points, and then they just you know, the nodes went down and they never came back up again.  because then there was some issues that were fixed by lighthouse guys and then it was still up. So someone's not able to sing from White House. And so these are some of the issues. But I think in the next run of the devnet 7. With the same spec we should be more stable, and hopefully we can have  then my date with the extended deneb features.

**Tim Beiko** [51:47](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3107):  Got it? Enrico, yeah.

**Enrico Del Fante (tbenr)** [51:51](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3111):   Yeah. I just wanted to add from the CL side that most of the sync problems, as far as I know, were mostly caused by rate limiting situations. So once we start removing great limits on lighthouses, and then also on the tech side things were better for the other clients to sync up. So I think it will be a CL discussion, maybe next week to actually start putting some numbers. And I agree on some agreement about the rate limit levels that we want to put.

**Tim Beiko** [52:40](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3160):  Got it? Okay? So anything else on the devnets?  If not, then I guess. Yeah, let's get devnet7 up with the same spec. and we can discuss this more as well on the 4844 call next Monday.

**Justin Florentine** [53:20](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3200): We have a expected ETA for 7 being up.

**Parithosh** [53:25](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3205):  I think the ETA’s wants to have this agreed.

**Justin Florentine** [53:39](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3219): Good. Alright, thanks.

**Tim Beiko** [53:44](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3224):  Okay. Anything else. Okay, Danny. You wanted to give a quick note on the CL aspect.

**Danny** [53:53](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3233):  Hey, yeah, the devnet6 stuff might  complicate this, but the intention right now is to release a CL Spec Tomorrow or Monday, with the full feature build. So that's 4844, but also 4788, 7044, 7045. Yes, Tim. It is nice that I can just say those numbers instead of trying to say the features. So you're right.so that's the intention. So we'll have full test factors for all of those built, but those will not be the target for devnet 7 in. So, we would use the previous release for that, but hopefully it unblock some development on getting the full feature stuff developed. If we need to add more, 4844 tests, or if something is broken and we change, we make a breaking change. Which I don't expect at this point we might have to do some sort of feature branch and special test vector build for 4844. That said, I. Think we're willing to take that risk and potential complexity so that we can get the full Denab feature release out. Because, I know, some people want to get development done. and we need to unblock that. Obviously this is related to consensus layer forks generally. I know there's somebody all here, so if you do have an issue with that, please let us know and we will do the release. And then, if there are issues on the call on Thursday, we can discuss them. But I think that this is the right path. Given the things we're juggling.

**Tim Beiko** [55:42](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3342):  Any comment on your question.

**Danny** [55:49](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3349): Okay? we'll put in the analysis channel. We have a release and test for 5 years for the fully featured Denab.

# [Move ERCs to separate repository EIPs#7206](https://github.com/ethereum/EIPs/pull/7206)

**Tim Beiko** [55:58](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3358):  Awesome. okay. And on a similar note. So the last topic for today is the proposal of splitting out ERC's from EIP’s in the repo. We've discussed this a fair bit for a long, long time. but the client has finally put up a PR which actually proposes or shows what it would look like technically. Yeah. And I guess just for background, like the the main rationale here is like ERC is mostly focused on application layer standards. EIP’s on protocol layer standards. and you know there might be value in having both processes be able to evolve separately. We have a bit more EIP editors now. So I think we have a bit more bandwidth to actually handle doing this split and at least some of the current. The EIP editors would also stay on the ERC side as well. but this would allow for. yeah, having 2 separate processes. so I'll pause here. I don't know my time. Do you want to get some context on this specific PR, if not, if anyone has. yeah, if anyone has comments.

**Lightclient** [57:28](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3448):  Yeah, I can. I could just say quickly. you know, I think the big question is, how will we deal with numbering for these 2 things? And this is still open for debate a little bit, I guess, but ultimately I think that the best plan is to sort of whenever this migration happens to have some sort of external document that EIP editors look at to see what the latest EIP number available is, and just assign that to the ERC and the EIP’S. I know that we talked about, maybe like making core EIP’s like even numbers and ERC's odd numbers. But I think that, given the number of historical EIP’s, we already have those that don't abide by this. It's going to add some confusion. So that's like currently what the proposal and the PR. Is to do with the number, and the rest of the information is pretty straightforward if you want to look at the proposal in the PR.

**Tim Beiko** [58:21](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3501): Got it? So I guess. Yeah, I have you curious the first year, you know, from this time on teams does anyone post this? And I know there's some folks on the EIP editor side who have concerns. but maybe starting with client teams, and then we can go to yeah, EIP Editors who are here.

**Marius Van Der Wijden** [58:44](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3524): I think I was my opinion on this a lot already. I think the EIP process should serve the core developers. And it's not right now. And one big issue with it is that we have an influx of so many ERC’s  that it's not really possible for someone to to stay informed of all the EIP’s that are coming up. and have meaningful reviews on them. So I'm very strongly in favor of splitting the 2 repositories.

**Tim Beiko** [59:31](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3571):  Got it anyone else?

**Justin Florentine** [59:36](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3576): This is Justin. Here? yeah. Same thing. Huge agreement. Just point clarity. I'm assuming we're not intending on reusing any EIP numbers being recovered. Is that correct?

**Lightclient** [59:46](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3586): That's correct.

**Justin Florentine** [59:48](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3588): Fantastic. Thank you.

**Tim Beiko** [59:52](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3592): Okay, so that there's a comment by, never mind as well. And the chat. Yeah, Danny. We could argue next year about saving the numbers, and I guess I don't know from you outside. Does anyone have thoughts now that you've all started using this. We go.

**Stokes** [1:00:31](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3631): Okay. I'd agree with what Marion said. But just like, you know, there's just so much going on with having both the EIP’s and ERC’s. If we can reduce that at all. It's really helpful for people working on EIP’s. So yeah, I definitely support this change and think it's really important to do.

**Tim Beiko** [1:00:53](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3631): Okay, so there is definitely some opposition, the EIP at their size. I don't know if there's anyone here who wants to share their thoughts or review.

**Gajinder** [1:01:04](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3664):  As CL or EL I'm in favour of the change. But as any EIP data I want to. I want to sort of figure out what is the harm that would come to the ERC process because of this? And I mean. would they be at any disadvantage. So that is the point that I think I would consider.

**Tim Beiko** [1:01:30](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3690):  Got it.

**Gcolvin** [1:01:34](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3694):  Yeah, I've there's Greg Colvin here. I've been opposed to splitting the Repos for years now, so I don't. I don't want to go into it right now. It's a premature decision. I'm really glad that that lightclient put this up. But I think it was yesterday, so there'll be a lot more discussion. I'm very sensitive to the process. having become too difficult for people to use. We do need to fix that. But just going. We're going to split. The repo doesn't necessarily fix anything. and I think what we really need is to step back and get a lot more information and consensus from the people using it. As to what are the pain points. what are the problems? if it's just well, it's hard to follow a big repo. Then the answer could be, well, the repo is really just a file cabinet. that we're trying to keep organised. It's not the best place to follow things.  A better place is the pages that the foundation maintained. everything's there by category. If you want to just check there. there's an rss feed we need to get a mailing list feed any other feeds that we can create, that you can follow. Other pain points are that getting a draft in is a pain. We're very picky. And on you know, link policies, everything has to be spelled right. Everything, everything. I lose track. Are these rules too tight? What do we need to do to make it easier to get a draft into the system than the first place, and  I'm sort of the only oh, gee! Editor left. and from my point of view the process has just gotten too rigid. It's no longer strong suggestions that the editors can exercise some judgement on it's become a set of fixed rules that apparently are chasing people. So I just want to start top up. up, you know, top down. Understand really what the problems are.  And then we can get to whether this particular technical change actually answers the problems, it helps to answer the problems we don't start from. Well, let's split the Repos. Create an ERC Ghetto, and then things will be better. We don't know that that's the case. And we've been having this argument for so very long. But at this point I'm still blocking consensus. So that was a long diet tribe, and I could go on it. But I have already been in many places for a long time. So that's all.

**Tim Beiko** [1:04:50](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3890):  Thanks. Oh, sorry.

**Victor Z(xinbenlv@)** [1:04:55](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3895):  Yeah. Yeah. I just want to. Yeah, this is Victor. Yeah. I very much agree with Greg. maybe I'm one of the so-called ERC, EIP editors that him they refers to. But I really resonate more as an identity, more as an author. How many of you in this group like the current EIP process? If you raise your hand, if you think, if you like it. and my question, the next question would be, How many of you are trying to support the split of ERC and the EIP. Anticipating the process to submit. Core the EIP would be easier. Raise your hand if you are supporting because you want to make it easier. it's not many, but that's out of my expectation. But how many are you supporting it because you want to make it trickier?

**Tim Beiko** [1:05:55](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3955):  I don't know how possibly it will be to get like raise hands responses through this. yeah.

**Victor Z(xinbenlv@)** [1:06:04](https://www.youtube.com/watch?v=09Kzi2x06UM&t=3964):  Right? So my argument is that it seems to me that's the proposal we're saying that once we've the ripple, this problem will be solved with the All  core dev. And if you really look into the discussion between the editors and the proposer actually intended to do the split and keep the code EIP submissions. still hard While relaxing the process for ERC which I'm in favour of. But I still think the core problem is that we shouldn't make it so hard for people to contribute to EIP. I heard 2 pains from discussion with Marius. One is the noise from 2 sides. That's gonna happen now that we have more different type of Core EIP as well. So why not split the core and consensus things like that? So we're trying to solve the problem instead of starting with splitting. And my last quick my last comments, if we really need to split, I think the impact on the ERC side would be that links to ERC’s are all going to have to to be broken. So if we are starting a new repo or the core. I think I will be more in favour rather than removing ERC from this existing repo. So I'm curious, like, how many would be in favour if the direction is to move Core  EIP’s. Outside of this we call that would be my question.

**Tim Beiko** [1:07:53](https://www.youtube.com/watch?v=09Kzi2x06UM&t=4073):  I am pretty opposed to that. I think there's a pretty strong understanding in the community that EIP’s tend to refer to core protocol changes. If you look at. You know, people talk about like EIP #4844, EIP#1559. And obviously it's not like a perfect thing, whereas generally when we say EIP, people mean like people understand like consensus changes to the ethereum protocol, whereas an ERC’s has a submitter. I think the connotation that, like the broader community of being like an application layer, changes, like people know? ERC 20, or ERC1155 or whatnot So regardless of what happens on the Github repo level like you could. You know you can choose to move the repos already called the EIP. So that's why I probably make sense to keep that for the core consensus as stuff, but like I think I feel pretty strong. You, that whatever is called the EIP should refer to consensus changes to the protocol whatever it's called the ERC’s is application level standards. And then, you know, there's a couple of categories like interface and what not, that are. you sort of need to figure out. But at a high level, I think this is how the community understands it. And you. you want to maintain that to not confuse everybody about it.

**Marius Van Der Wijden** [1:09:17](https://www.youtube.com/watch?v=09Kzi2x06UM&t=4157):  Yeah. So we are going to like this with the split, we are going to break some Urls. But I think maintaining the core your other way, more important than maintaining the ERC’s. anyway, 1 I wanted to respond to Greg. because I think 1 one thing that you would that you that you touched upon was that the EIP process has become too rigid and I kind of agree. And I kind of think that's big. really, the big pain point for a lot of core developers is that? It's rigid. There are a lot of routes, and a lot of those routes. I feel like we're introduced by mica at some point and the intention behind it was that it wasn't possible for him or for the EIP editors. But then it was. I think it was way smaller set than today.to really go through the go through the EIP’s go through the incoming PR’s and have a really like deep really go into depth and and understand the changes and verify the changes on on technical merit. And so they made up a lot of like rules, so that everything that likes it gets rid of a bunch of spam. And I think that one of the core problems is that you bunch in this very spammy side, the Yourc side, where basically everyone likes everyone that creates an application kind of thing. Okay, we. We have to do an Isc now and and open opens and a PR for the ERC and this, this, these call EIP’s, where you have people like we like, we want to discuss. We want to have the Dprs open as a discussion point so that we can. We can maintain this open discussion more like a request for commons. Instead of like a set standard. And yeah, it's just 2 different things and bunching them together was that decision? And so in order to make it easier for everyone, we should, we should undo this decision and also, I think. It seems like almost everyone is in favour of doing that. I agree that this PR that Matt opened might not be like the solution. but I think there's a very strong agreement. This change needs to happen. and if. In my personal opinion, if one of the EIP editors or some of the EIP editors are against this change, then it's fine, and we have discussions about it. but at some point in this these discussions have been going on for a really long time. And so I think at some point we just need to make the decision. to do this change, even if people object.

**Tim Beiko** [1:13:06](https://www.youtube.com/watch?v=09Kzi2x06UM&t=4386):  Justin?

**Justin Florentine** [1:13:07](https://www.youtube.com/watch?v=09Kzi2x06UM&t=4387):  Yeah, just real quick. I'm in, you know, total agreement with everything that Marius asked, and I would like to kind of call into question. I see a lot of conflation of, you know, discussion of the editorial process and policy itself, which I think we can all pretty much agree is orthogonal to this decision. I don't think we should interpret advocating for a split as endorsement of a current perfect world. of the editorial process and EIP authorship process in general. So I think keeping those 2 separate in our mind leaves us many more options for solving this problem in a way that everyone's happy with.

**Tim Beiko** [1:13:55](https://www.youtube.com/watch?v=09Kzi2x06UM&t=4435):  Yeah. And there's a comment by Victor around like asking the ERC community member. I think you know, there's definitely been some like feedback in the past. But I also there's also a part of me that feels like, you know, for years we've tried to find people from the ERC community to step up and steward this, and, you know, be like maintainers, or you know, like, on this process. And it sort of hasn't happened. and I think that, you know, splitting the EIP’s out so that the people that so that the people who like are focused on EIP’s can just focus on that  the community can arrange on ERC’s as well. there's probably a signal that like if they want to shape their process in a way that's better like someone has to step up and do it And it. It feels a bit weird because they're bundled together. Then the people who want to do EIP’s actually end up have to like doing all the ERC lifting and it's sort of like doesn't lead to anyone showing up and and like making things that are on the ERC side. So I think it's like if everyone and it seems like all the client teams and most of the people who like right EIP’s, are in favour of splitting this. I don't think that, like we necessarily need full buy in from like everyone who's written in the ERc. Like, I think it's fine to say we're splitting this out. You can use this, and you can add editors to the Erc side. But, like the folks who like do most of the EIP’s, want a separate process, and we can move forward with that and there's a okay. There's a couple of Erc authors. If ever that's wanting to change in the chat, I'm sorry I just got someone off.

**Pooja Ranjan** [1:15:59](https://www.youtube.com/watch?v=09Kzi2x06UM&t=4559): : Yeah, I'm sorry. I know I'm not an ERC or EIP editor, but I'm someone who has been involved with the EIP process. I'm helping out with improving the process, trying to identify the pain point. And as a part of item cat headers. We have been working in this direction for the past 3 years. So I would just like to make a few points. here, from the conversation. So far, the 2 biggest problems that we can hear out in support of the PR is the influx of Pr that comes to the repository, and that kind of creates noise for which many people who are interested in Core EIP cannot be able to follow. I don't know if I have a perfect solution. But I was just wondering if RSs, we can help with them. Right? We have ours, and we're for status change and everything. Can we have an Rss for core EIP’s only and suggest this just to maybe help out ERC proposals. What I have noticed in this period is ERC's proposals, in really bad shape a couple of years ago. Thanks to Manganet, who has actively supported the education of the process, and how to document it best. He had also contributed and did the EIP editors apprenticeship meeting for a very long time, I guess over a dozen of meetings we have organised, and it has supported a lot. We do have a dedicated Erc editor, as of now, but we do not have many out of the 6 or 7 EIP editors. Those are listed on EIP one. We do have only one ERC, a data that is fully dedicated for Erc purposes. I still see that there is a shortage of editors. And I feel like that if we just move ERC out of that for badly. That would be harmful for the team, for the ERC people. And the other biggest problem that I have identified during this conversation is about the external link which I believe Samerson has proposed. 5757, and one by one. We are trying to add permission to the external length. I do agree.  Maybe it's a point that there was a lot of strictness imposed by mica and other editors at the time to make the process streamline to make the process even better, and we are reaching in that direction. I'm really requesting people to consider ERC as a part of the ethereum ecosystem, and we can, if we can, extend our support to these people, we should let them be there as well. Had this been a proposal coming out of the ERC team saying that we don't want to be a part of Core EIP or the EIP system at all, because we feel we are different. I think. that would have been more, and I would have been more in favour of going to what they pull requests, having said that. Yeah. So it just

**Marius Van Der Wijden** [1:19:04](https://www.youtube.com/watch?v=09Kzi2x06UM&t=4744):  Just to that point. why should why should the ERC community have the say like that a bunch of people like now discussing this point that like. If the ERC community wants to split out. Then it would be fine. Basically  the way I see it, the EIP  community is trying to split the ERC’s out and and so like. No, I think we should have the same say in this decision.

**Pooja Ranjan** [1:19:41](https://www.youtube.com/watch?v=09Kzi2x06UM&t=4781):  that is right. I do agree. I feel like they are intertwined, and they should be considered together. I have a very good example for 4337. That is an ERC. As of now, but we are working on some proposal that we can eventually in future may be able to have it supported by the Evm and by the main protocol. So I find it hard to actually separate both of them.and I feel like going side by side if they are not creating much trouble to the core EIP process. I do agree that there are certain road blockers for new authors who are trying to document processes, and I feel like working in solving their issues after identifying what are the main problems just like external link policy was one of those. I think we can come to a better place where we can live together.

**Tim Beiko** [1:20:32](https://www.youtube.com/watch?v=09Kzi2x06UM&t=4832):  So I guess I have like my, my thought on this is, it's almost like a tooling question, right? Like you mentioned, and great sort of mentioned this as well, like, okay, if you like too much stuff. And one github is, it's overwhelming. There's a bunch of other things we can do. Yes, we can do our RSs, we can do, you know, like the pages on each side of the but but then the alternative is like, if you know, Github, notifications is the tool that all the cortex use, then that's the thing we should use right like we shouldn't like the the single complaint everyone has is. There's too much friction in this. And if, like all the clients are saying, I want to watch a repo that has less issues in it, and that the issues in it are more relevant. Then we should optimise for that. I also think  I, it's  like at the end of the day. This is just like a repo, and URL split like the idea that, you know, because they're in 2 different repos like, I don't know someone working on account. Abstraction can't be paid attention to like EIP’s or theorem slash E, and the theorem slash Ercs seems a bit weird. Given that, like today, to, you know, contribute to Ethereum. We literally had a presentation earlier about something like a new testing repo. We have the engine Api repo. We have the EL Specs, the CL specs. The EIP’s, like people in practice, already follow, you know, nearly like 10 repos, if they want to follow everything. So I don't know why splitting the repo and spinning the Urls is so big it doesn't seem like a big change in terms of process. It doesn't seem like it is a ton of friction in terms of like. If you want to write an ERC and write any EIP, it's not that different than if you want to write an EIP today and have your spec live in the CL specs repo and people do that, and it seems to work. So I'm much more inclined to just You know that spilling the repos doesn't sever the process and like mean that no one can ever contribute from one to the other. It just gives, like more clarity, the same way that we have, you know, a repo for testing and the repo for like the specs. Yeah, it just keeps things more encapsulated. But it doesn't. It doesn't seem like a huge deal to have 2 repos rather than one. Yeah  Justin.

**Justin Florentine** [1:23:05](https://www.youtube.com/watch?v=09Kzi2x06UM&t=4985): So to sharpen that point a little bit, the repo is actually, I think, the correct thing to collect this in and make that distinguishing on, because the editorial process itself actually manifests itself in a lot of automated ways. And there's a lot of tooling and hooks and things like that that contribute to the processes that we want to refine. So I actually think that's actually saying that there's more of an advantage in going further with this and actually separating them out to allow the people to automate the process the However, they see fit. So I think that's and that's  I was kind of on the pages like, well, mono repo multiple repos! Who really cares at the end of the day there's folders that you look at. And I don't think that's quite correct. I think you're leading a lot of automation potential on the table by not embracing the separate repo.

**Tim Beiko** [1:23:57](https://www.youtube.com/watch?v=09Kzi2x06UM&t=5037):  Yeah, I would agree with that. Yeah, if we do customise things more than having separate 3 calls, obviously makes it much easier.and I think, yeah, I also agree with the point around, like, yeah. And like, protocol development based on application layer concerns as a general principle, like we've haven't really done this in the past. The Ethereum protocol changes are already extremely slow relative to software development in general. So anything, any like an external source of friction. then to be just a bad idea.So I don't know. It seems to me. like all of the client teams, are in favour of this. Some of the folks here who have been ERC Authors as well are in favour of this. There's a couple of people on the EIP editor side who are not in favour but it seems to me like the balance is like we should go ahead and do this change, we've been talking about it for years. It's also something that we can undo. Not like that's not incredibly hard to undo if we realise in the year that it was the wrong thing. but yeah, I think if all of the client teams are in favour, if parts of the IP editors are in favour. Yeah, we should go for it. Craig. So we can't hear you, Greg. You're still on it.

**Gcolvin** [1:25:50](https://www.youtube.com/watch?v=09Kzi2x06UM&t=5150):  I, nonetheless. Still, block consensus. I very much hear you. There's a problem I'm not convinced of, simply splitting the repos helps. and they really are. We really are one community trying to improve the Ethereum that this line is not so strong. and the problems do not seem to me to be with the tooling. I disagree that it is the Court Ofs Repo. I really do.  not seem to me to be with the tooling. I disagree that it is the Court Ofs Repo. I really do.we were a distinct group. and really. if the core Devs found what we were doing useful? Great, if not. we're sorry. But :  it's not. : I'm not rejecting you. I'm just saying, the editors have their own integrity, and the repo in the end is our file cabinet that needs to serve our work and not necessarily the coredev's ability to follow the work Jet hug, repos are not really good for that, and we need and can provide otherwise to notify. Rss needs your old fashioned I don't know technically. Can. Can we feed notifications in the discord. for instance.that that's a question

**Tim Beiko** [1:27:26](https://www.youtube.com/watch?v=09Kzi2x06UM&t=5246):  like, I guess, on your point around blocking. This is a comment in the chat. I don't think : a single person can block this, I think, you know, like 

**Gcolvin** [1:27:36](https://www.youtube.com/watch?v=09Kzi2x06UM&t=5256):  I'm an editor that can block consensus with the editors.they can decide what to do about it. 

**Tim Beiko** [1:27:49](https://www.youtube.com/watch?v=09Kzi2x06UM&t=5269): So I don't know that we need unanimous consent like we do. I don't think we've required unanimous consent, for, like any change.

**Gcolvin** [1:27:58](https://www.youtube.com/watch?v=09Kzi2x06UM&t=5278):  I'm saying, it's a consensus change of the editors. I'm blocking consensus. We editors can decide what to do, I might be convinced. but I'd much rather see. And I've said a complete plan from the top down that yeah, that we've really looked at what the problem is, what are the pain points and know that we're going to solve it. And then, if splitting the repos is just saying, Oh, 2 file cabinets will work better than one, and we've worked out the problems and how to fix them. Numbering is more of a problem that it might seem. For instance, You know. Then, if splitting the repost looks like the way to go, then that's the way to go. But we could split the repos and solve none of the problems. 

**Tim Beiko** [1:28:50](https://www.youtube.com/watch?v=09Kzi2x06UM&t=5330): Yeah, but I think we've agreed to this, and I think all of the client teams still want to go ahead with it. And you know, then it was a comment like consensus doesn't imply unanimity. And I think we're, you know, at a point where we have extremely strong consensus on most of the people who write Core EIP’s and engage with that process.

**Gcolvin** [1:29:15](https://www.youtube.com/watch?v=09Kzi2x06UM&t=5355):  This. what can I say? The editors are an independent group. We'll discuss this as a group.And

**Tim Beiko** [1:29:25](https://www.youtube.com/watch?v=09Kzi2x06UM&t=5365):  So we have discussed this for years, though, and this is kind of the thing, and I guess back to the Jamie's comment is, you know, I personally discuss this. It's probably 2019, you know, on and off through this. And so I think.with the addition of having all the CL folks using this process? having had years of discussion, but hasn't, you know, done much in terms of moving the conversation forward? : I like. I don't know. I I don't know that we learn much more by discussing things for another. You know, 6 months I think we will learn a lot by actually splitting and running the experiment. If it's a bad idea, then worst case, we just reverted back, and it's not the end of the world. But

**Gcolvin** [1:30:20](https://www.youtube.com/watch?v=09Kzi2x06UM&t=5420):  I'm still not the only problem.The only problem that splitting the repos actually solves is that if somebody is using Github notifications to follow things or browsing the repo for following things. it will help the core devs doing that.I don't know how many core devs tried. Try to follow it that way. There's other ways to follow it. We can,

**Tim Beiko** [1:30:28](https://www.youtube.com/watch?v=09Kzi2x06UM&t=5428):  But they do like. We literally have everything else on Github. All the conversations happen there we have Cordevs following, you know, a bunch of different 3 bows from research to like testing the specs. And so it's like, sure, you know, you can say, using an Rss feed, but like no, it doesn't make sense where we go  or whatever else. But like we could just use the same tool like. And again.: this is just like a Github repo and an URL. If it does lead, you know, the processes can evolve differently. But if you know if it's true that, like the processes, are optimal as they are today, and they don't change in the future. Then the worst we've done is we've created an extra repo for people to, you know, follow, and that, you know, duplicated a bunch of automation which is, you know, pretty minor in the grant you of things.and then everything else is the same. But in practice, if we do this change, and then things do start to change from one repo to the other. Then it's a sign. It was a good idea to do it, and I don't thinkI don't think it's like discussing the issue for another 6 months like the EIPIP calls. That'll give us more information at this point. It's like actually trying yet seeing other things we can do and you know, and going from there. So I don't know. I feel like I've had this conversation with many people over the past few years, and it always sort of ends up at the same spot where the vast majority of people want this to happen. They're a bit disengaged from the current process because they feel burnt out by it. And then you have a couple of people who are very engaged with the process, who sort of want more information when there's just like this. General, I don't know. Like discontent that's shared. And I think, yeah, like a bigger step forward, of actually splitting it out and trying to separate repos is probably the best. the best path forward. At this point

**Gcolvin** [1:32:52](https://www.youtube.com/watch?v=09Kzi2x06UM&t=5572):  I believe the best thing : is : the earlier thing, which is, we make it very easy for drafts to get in.

**Tim Beiko** [1:33:01](https://www.youtube.com/watch?v=09Kzi2x06UM&t=5581):  So we can do that. Sure, we can do that for free. Post them. That's not the end of the world. Now

**Lightclient** [1:33:10](https://www.youtube.com/watch?v=09Kzi2x06UM&t=5590): we don't, but it hasn't. That's what we could have done. We've been talking about this exactly. We've been talking about all these things to change about the eip process, but it just doesn't happen. And eventually we just have to do something because the process isn't serving any of the people it's meant to serve. It doesn't serve the EIP editors. This is something that I think is going to alleviate the deadlock that we have in making decisions and changing the process. And let the people who are really involved with their specific parts of the process develop it in a way that they see that.

**Tim Beiko** [1:33:44](https://www.youtube.com/watch?v=09Kzi2x06UM&t=5624): I think. Look, we're already over time. I think what I would suggest is like, it's clear to me at least, that from the core EIP side, like the strong consensus to split this out and there's an EIPIP call next Wednesday. I believe so. What I would suggest is that we spend that call talking about the how rather than like the hip, like, you know, Matt Pr has some, you know, issues with it. There's a couple of issues that came up today. But I think.you know, have any conversation about how we want to go about. This is probably the right next step in like, eip.yeah. Given the strong support here.and and I guess also, if if people feel very strong like, if if the ERC community feels very strongly that this is like a terrible idea, and like we shouldn't do it then they should probably voice that in the next couple of days before, like that the EIPIP call and we can discuss it then. But yeah. Otherwise it seems like from the course side we have pretty strong consensus the this, this the split things.

**Tim Beiko** [1:35:09](https://www.youtube.com/watch?v=09Kzi2x06UM&t=5709):  and yeah, the EIPIP call is Wednesday, 14 Utc. And the agenda. I don't know if someone can post the link to the agenda in the chat here. But it's I. It's in the cat Herders repo okay, I know we're already a bit over time. Was there anything else people wanted to discuss? Okay, well, thanks everyone. Talk to you soon.

**Stokes** [1:35:41](https://www.youtube.com/watch?v=09Kzi2x06UM&t=5741):  Thanks, Tim.

**Trent** [1:35:491](https://www.youtube.com/watch?v=09Kzi2x06UM&t=5749):  Bye, bye.

**Pooja Ranjan** [1:35:52](https://www.youtube.com/watch?v=09Kzi2x06UM&t=5752):  thank you.

—------------------------------------------------------------------------------------------------------------------------------------

# Attendees

* Tim Beiko
* Danno Ferrin
* Spencers
* Maurius Van Der Wijden
* Mikhail Kalinin
* Mario Vega
* Roberto Bayardo
* Dan (danceratopz)
* Karimtaam
* Paritosh
* Marekm
* Pooja Ranjan
* Danny
* Alex Stokes
* Willium Schwab
* Phil Ngo
* Ruben
* Ansgar Diatrichs
* Terence
* Alexey
* Ruben
* Ken NG
* Joshua 
* Gcolvin
* Ben Adams
* Carlbeek
* Hsiao-Wei Wang
* Enrico Del Fanta
* Victor Z
* Guillaume
* Marcin Sobczak
* Andrew Ashikhmin
* Dimitrykhoklow
* Gajinder
* Ahmad Bitar
* Trent
* Justin Florentine

### Next Meeting Date/Time: Thursday 6 July 2023 at 14:00 UTC
