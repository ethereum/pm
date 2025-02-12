# Eth_Simulate Meeting Meeting 36

Note: This file is copied from [here](https://github.com/ethereum/pm/issues/1273#issuecomment-2631171565)

### Meeting Info

- Agenda: [ethereum#1273](https://github.com/ethereum/pm/issues/1273)
- Date & Time: February 03, 2025, 12:00 UTC
- Recording: [here](https://youtu.be/i2JBDF_MBVU?si=zBjWUwY4F_WfLzrw)
## Notes
### Summary 
# Intern Tracing Refactoring Project  

- The tracing component is being prototyped by Nethermind with assistance from their intern.  
- The task primarily involves refactoring to get tracers working.  
- Progress is on track, and the intern is expected to complete the refactoring by the end of the current week.  
- The project is well-defined and serves as a suitable internship task, focusing on modular and reusable design.  

## Hash Implementation and Testing  

- The Besu implementation is progressing, with the majority of Hive tests passing. However, around 15-16 tests are still failing.  
- A discrepancy in hash values compared to Geth has been identified. Initial investigations suggest that passing the parent hash to the next block resolves the mismatch.  
- A patch will be shared for further review to address the hash matching issues.  
- Besu also plans to test against Nethermind. Nethermind tests are already running for cross-client hash comparison.  
- There are ongoing investigations into differences in block size definitions between implementations.  

## Other Updates  

- Sina has not yet reviewed the tracing component due to other commitments, including work on gas estimation.  
- Rohit reported no updates due to other commitments.  

## Next Steps  

- Complete tracing refactoring by Nethermind intern.  
- Investigate and resolve hash discrepancies between Besu, Geth, and Nethermind implementations.  
- Share and review patches to address hash and block size issues.  
- Conduct cross-client testing with Hive for further validation.  
