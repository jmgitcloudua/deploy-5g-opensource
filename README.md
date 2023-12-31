# Deployment of 5G Core 
We can deploy 5G Core using open source software like [Open5GS](https://open5gs.org/), [FreeGC](https://free5gc.org/) or [NextEPC](https://nextepc.com/). So, we can deploy it using Dedicated Server, Virtual Machine (VM) or Containerization. <br>
Deploying 5G core using containerization, is more effient and flexible, scalable and, portable than using VM or dedicated server.
## Deploy using VM in OpenStack
OpenStack is a free and open-source cloud computing platform for building and managing public and private clouds. It controls large pools of compute, storage, and networking resources. However, we can deploy 5G Core using VMs in OpenStack. <br>
Please click [here](https://github.com/jmgitcloudua/deploy-5g-opensource/tree/main/vmachine) to follow instructions to deploy open5GS VMs in OpenStack.
## Deploy using Docker 
Docker is an orchestration platform to quickly deploy services like 5G core.<br>
Please click [here](https://github.com/jmgitcloudua/deploy-5g-opensource/tree/main/free5gc) or [here](https://github.com/jmgitcloudua/deploy-5g-container/tree/main/docker) to follow instructions to deploy Free5GC or NextEPC using Docker, respectively .

## Deploy using kubernetes
Kubernetes is also an orchestration platform to quickly deploy services like 5G core. But It's more scalable than using docker. It's has an essential service called HPA (Horizontal Pod Autoscaling) and it is ephemeral.<br>
Please click [here](https://github.com/jmgitcloudua/deploy-5g-opensource/tree/main/open5gs) to follow instructions to deploy open5GS using Kubernetes (K8s).


## Deploy using OpenAirInterface
The goal of the OAI-5G Core Network (CN) project group is to provide a 3GPP-Compliant 5G Standalone (SA) CN implementation with a rich feature set. OAI 5G CN is designed and implemented in a flexible way which can be easily adapted to fulfill the needs of diversified 5G use-cases. All the features of the OAI 5G CN components are continuously tested with professional testers, commercial gNBs (with COTS UE) and open-source RAN simulators.<br>
Please click [here](https://github.com/jmgitcloudua/deploy-5g-opensource/tree/main/oai) to follow instructions to deploy OAI using docker-compose and K8S.

## Memo <br>
Fell free to contact me for any questions you can have.

