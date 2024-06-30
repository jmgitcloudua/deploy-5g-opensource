# Edge Internet Traffic Steering Architecture -  Sequential Diagram

![Diagram](Premium-EITS-Architecture-Sequential-Diagram.png)


## Sequential Flow Description

### 1. User Equipment (UE) — LINK1 sends a request
- **Step 1**: UE at LINK1 sends a request to UE at LINK2.
  - The UE can be any user device such as a smartphone, tablet, or laptop connected to the network at LINK1.
- **Step 1.1**: UE at LINK2 returns the requested data to UE at LINK1.
  - This step confirms that UE at LINK1's request has been successfully received and processed by UE at LINK2.
- **Step 1.2**: UE at LINK1 forwards the request data to the PKI Network.
  - This involves transferring the data through the network infrastructure to reach the PKI Network.
- **Step 1.3**: The PKI Network returns a "200 — OK" response to UE at LINK1.
  - This indicates that the PKI Network has successfully received and processed the forwarded request from UE at LINK1.

### 2. User Equipment (UE) — LINK2 sends a request
- **Step 2**: UE at LINK2 sends a request to the PKI Network.
  - The UE at LINK2 is acting as an intermediary to further process or validate the request.
- **Step 2.1**: The PKI Network returns the requested data to UE at LINK2.
  - This step ensures that the PKI Network has received and is processing the request from UE at LINK2.
- **Step 2.2**: UE at LINK2 forwards the request to PKI Computing.
  - This involves routing the request through the network to reach PKI Computing for further processing.
- **Step 2.3**: PKI Computing returns a "200 — OK" response to UE at LINK2.
  - This indicates that PKI Computing has successfully processed the forwarded request from UE at LINK2.

### 3. PKI Network collects data
- **Step 3**: The PKI Network collects data from PKI Computing.
  - This step involves the PKI Network actively requesting and gathering necessary data from PKI Computing.
- **Step 3.1**: PKI Computing returns the collected data to the PKI Network.
  - This step ensures that the data required by the PKI Network has been successfully collected and sent back.
- **Step 3.2**: The PKI Network processes and handles the data received from PKI Computing.
  - This step involves any necessary computation or processing of the data by the PKI Network.
- **Step 3.3**: The PKI Network returns the processed data to the Physical Server.
  - This indicates the data has been processed and is ready for further handling or storage.

### 4. Physical Server collects data
- **Step 4**: The Physical Server collects data from the Virtual Machine (VM).
  - The Physical Server initiates a request to the VM for necessary data.
- **Step 4.1**: The VM returns the requested data to the Physical Server.
  - This step confirms that the VM has received the request and sent the required data back to the Physical Server.
- **Step 4.2**: The Physical Server processes and handles the data received from the VM.
  - This involves any necessary processing or computation of the data by the Physical Server.
- **Step 4.3**: The Physical Server returns the processed data to the 5G CN Container.
  - This indicates that the Physical Server has successfully processed the data and forwarded it to the 5G CN Container for further use or storage.

This sequential flow diagram details the interaction between various components in the Edge Internet Traffic Steering Architecture, highlighting the steps taken for data requests and processing across different network entities.
