# Edge Internet Traffic Steering (EITS) Sequential Diagram - From EITS Deployment/Diagram

## EITS Deployment Diagram
![EITS Deployment Diagram](Premium-EITS-OAI-Traffic-Steering-PCC-Diagram.png "EITS Deployment Diagram")
<br>
## EITS Sequential Diagram From Deployment Diagram
![EITS Sequential Diagram From Deployment Diagram](Premium-EITS-OAI-TS-Sequential-Diagram.png "EITS Sequential Diagram From Deployment Diagram")

## Description of Sequential Steps/Flows

1. **User Equipment (UE) to GNBSIM**
    - **Step 1:** The User Equipment (UE) sends a request to the GNBSIM.
    - **Step 1.1:** GNBSIM returns a response to the UE.

2. **GNBSIM to User Plane Function (UPF)**
    - **Step 2:** GNBSIM sends a request to the API decision controller at the UPF (Interface N3).
    - **Step 2.1:** The UPF returns a response to the GNBSIM.

3. **UPF to Control Plane (AMF, SMF)**
    - **Step 3:** The UPF requests a session via Interface N4 to the Session Management Function (SMF).
    - **Step 3.1:** The SMF handles the data traffic and returns a response to the UPF.
    - **Step 3.2:** The SMF steers traffic to the specified site or service (Link1/Link2— KPI) via Interface N6.
    - **Step 3.3:** The traffic is returned to the UPF.

4. **SMF to Access and Mobility Management Function (AMF)**
    - **Step 4:** The SMF requests a connection to the AMF via Interface N11.
    - **Step 4.1:** The AMF establishes a connection and returns a response to the SMF.

5. **SMF to Policy Control Function (PCF)**
    - **Step 5:** The SMF creates a session request to initiate a session via Interface N7 to the Policy Control Function (PCF).
    - **Step 5.1:** The PCF updates the session and returns it using the PCC (Policy and Charging Control) configuration to the SMF.

6. **Control Plane (SMF) to Management Plane (Monitoring)**
    - **Step 6:** The SMF requests data metrics from Prometheus/Grafana (part of the Monitoring system) for the Management Plane.
    - **Step 6.1:** The Monitoring system returns collected data metrics to the SMF.

These steps illustrate the interactions between different network functions and how they cooperate to handle and steer internet traffic within an EITS environment. The process involves setting up connections, managing sessions, and collecting data metrics for monitoring purposes.


