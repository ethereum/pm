
Future of EOA/AA Breakout Room #4
--

**Date**: June 05 2024, 14:00-15:00 UTC

**Agenda**: https://github.com/ethereum/pm/issues/1054

**Recording**: https://youtu.be/gsc_yTdHRig

**Links shared**:
* Working document for [Wallet best practices](https://hackmd.io/@rimeissner/eip7702-best-practices)
* Optional nonce
  * https://ethereum-magicians.org/t/eip-7702-set-eoa-account-code-for-one-transaction/19923/158 
* Signign Address vs Code
https://ethereum-magicians.org/t/eip-7702-set-eoa-account-code-for-one-transaction/19923/157

## Next steps
*  discuss this more in All Core Dev and if we want another call.



(Full Notes in WIP)

**Tim Beiko**: Okay, I guess we probably get started. Had a few things on the agenda for today. basically some spec discussions. Then, following up on what is best practices and the proxy pattern and see how how things go.

Yeah, let's maybe kick this off with the revocability conversation. So Sudeep, I believe you are the one who posted on the Erigon’s behalf on the magicians.

## Optional revocability.

**Tim Beiko**: Do you wanna take maybe a minute to like, walk through your views and concerns.

**Sudeep | Erigon**: Yeah. So we have been considering, the security handling and concerns, and saying that it's the same as a private key or a seed phrase. I disagree there, because once you delete the wallet from your browser, the seed phrase, or the private key is supposed to be gone, and no more with the wallet provider. But with the signatures, it's a different deal like once you make a 7702 transaction,  the authorizations live on the chain. And so let's say, if I don't trust the wallet anymore, and I want to move to a different wallet. Then I should have an option to do something similar to, Sign out of all accounts, or sign out sign out of all devices. There has to be like a mechanism for that. otherwise, there's always a lingering question about Is it safe? There was an authorization that that was there, and it wasn't really revoked. So what what happens there?


**Sudeep | Erigon**: Second point is that the people who are opposed to revocability. I don't think they're opposed to revocability as such. But the constraints that it poses on the wallet providers. and I think the nonce solution, nonce revocability is definitely too constraining for the wallet providers to create a proper ux. So I think we should investigate like more solutions. Certainly, Max nonce is one such option. The nonce manager is one such options. I think we can like come together with come together with more solutions on top of this, which have revocability baked in, and also allow the wallet providers enough sort of breathing room to create the UX that they want.
