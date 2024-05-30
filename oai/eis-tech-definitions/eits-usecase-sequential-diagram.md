# Edge Internet Traffic Steering — Streaming Video Use Case

## Sequentil Diagram
![Sequential Diagram](Thesis-UA-EITS-OAI-TS-Video-UseCase-Sequential-Diagram.png)

This document describes the steps and flows of an edge internet traffic steering use case for streaming video, as depicted in the sequential diagram above.

## Steps and Flows

### Data/User Plane
1. **UE (User Equipment) to gNB SIM (client-video)**
   - **1:** UE sends a request to the gNB SIM.
   - **1.1:** gNB SIM returns a response to the UE.

2. **gNB SIM (client-video) to UPF (server-video)**
   - **2:** gNB SIM sends a request to the UPF via the N3 interface.
   - **2.1:** UPF returns a response to gNB SIM.

### Control Plane
3. **UPF (server-video) to SMF**
   - **3:** UPF requests a session to be created via the N4 interface.
   - **3.1:** SMF returns a handle to manage data traffic to the UPF.

4. **SMF to AMF**
   - **4:** SMF requests a connection to be established via the N11 interface.
   - **4.1:** AMF establishes a connection with the SMF.

5. **SMF to PCF**
   - **5:** SMF creates a session request and initiates a session via the N7 interface.
   - **5.1:** PCF returns an update session with PCC (Policy Control Configuration) configuration to the SMF.

### Data/User Plane (continued)
3. **UPF (server-video) to EXT-DN (Internet)**
   - **3.2:** UPF steers traffic to the Internet via Interface N6, considering the KPI (Key Performance Indicator) for SITE 1, SITE 2, etc.
   - **3.3:** UPF returns the traffic to the changing consumed video site (SITE 2).

### Management Plane
6. **Monitoring**
   - **6:** Monitoring system requests data metrics from Prometheus/Grafana.
   - **6.1:** Prometheus/Grafana return collected data.

### Key Interfaces
- **N3:** Between gNB SIM (client-video) and UPF (server-video)
- **N4:** Between UPF (server-video) and SMF
- **N6:** Between UPF (server-video) and EXT-DN (Internet)
- **N7:** Between SMF and PCF
- **N11:** Between SMF and AMF
