# Edge Internet Traffic Steering — Streaming Video Use Case

## Sequential Diagram
![Sequential Diagram](Premium-EITS-OAI-TS-Video-UseCase-Sequential-Diagram.png)
<br>
This document describes the steps and flows of an edge internet traffic steering use case for streaming video, as depicted in the sequential diagram above.

## Sequential Flow Description

### Data/User Plane

1. **User Equipment (UE) sends a request**
   - **Step 1**: The UE sends a video request to the GNB.
   - **Step 1.1**: The GNB returns an acknowledgment of the request.

2. **GNB sends request to UPF**
   - **Step 2**: The GNB sends the video request to the UPF through Interface N3.
   - **Step 2.1**: The UPF returns a "200 OK" response, indicating successful receipt.
   - **Step 2.2**: The UPF forwards the request to the external data network (EXT-DN) through Interface N3.
   - **Step 2.3**: The external network returns the data to the UPF.

3. **UPF requests session to EXT-DN**
   - **Step 3**: The UPF requests a session to the external data network through Interface N4.
   - **Step 3.1**: The external network returns handle data traffic instructions.
   - **Step 3.2**: The UPF steers traffic to either LINK1 or LINK2 via Interface N6, depending on KPI.
   - **Step 3.3**: The UPF returns traffic information indicating a change to LINK2 if required.

### Control Plane

4. **Request connection to AMF**
   - **Step 4**: The UPF requests a connection to the AMF through Interface N11.
   - **Step 4.1**: The AMF establishes the connection with the UPF.

5. **Session management**
   - **Step 5**: The AMF creates a session request and initiates the session through Interface N7, using SMF and PCF.
   - **Step 5.1**: The SMF returns an update session with PCC configuration to manage policy and charging rules.

### Management Plane

6. **Monitoring and data metrics**
   - **Step 6**: The monitoring system requests data metrics from the network components using Prometheus/Grafana.
   - **Step 6.1**: The network components return collected data to the monitoring system.

This description provides a detailed step-by-step explanation of the flow in the Edge Internet Traffic Steering (EITS) architecture for video use cases, highlighting interactions between the data/user plane, control plane, and management plane.

### Key Interfaces
- **N3:** Between gNB SIM (client-video) and UPF (server-video)
- **N4:** Between UPF (server-video) and SMF
- **N6:** Between UPF (server-video) and EXT-DN (Internet)
- **N7:** Between SMF and PCF
- **N11:** Between SMF and AMF
