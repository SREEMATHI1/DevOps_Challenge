1. Saw issues while running the application in Docker. 
Issue: It wasn't connecting when i connect host machine to docker service but when i ssh to the container & did a curl it worked.

Solution: Re-installed the docker on windows 10 to fix the network issue.

2. Time of the docker container & the system time was different so i got AWS invalid SignatureException.

Solution: Rebooted docker & the machine.

*Along the road learnt a lot about Travis-CI & troubleshooted more issues in Docker* 
