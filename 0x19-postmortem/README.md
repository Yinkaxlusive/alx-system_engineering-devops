Postmortem Report: Website Outage on June 1, 2024

Issue Summary
Duration of the Outage:

June 1, 2024, 15:00 - 17:30 WAT
Impact:

The company's main e-commerce website was down, preventing all users from accessing the site. Approximately 100% of users were affected, resulting in an estimated loss of $20,000 in sales revenue during the downtime.
Root Cause:

A misconfiguration in the load balancer caused it to fail under high traffic, preventing traffic from being routed to healthy application servers.
Timeline
15:00 WAT: Issue detected by automated monitoring system alerting high error rates.
15:05 WAT: Engineering team notified via PagerDuty.
15:10 WAT: Initial investigation began; logs reviewed for application errors.
15:20 WAT: Misleading path: suspected database connection issues.
15:35 WAT: Networking team escalated to investigate potential DDoS attack.
15:50 WAT: Determined there was no malicious activity.
16:00 WAT: Focus shifted to load balancer configuration.
16:15 WAT: Root cause identified as load balancer misconfiguration.
16:30 WAT: Configuration update and restart of load balancer initiated.
16:45 WAT: Load balancer back online; traffic routing resumed.
17:00 WAT: Full functionality restored; monitoring closely for further issues.
17:30 WAT: Confirmed system stable, incident closed.
Root Cause and Resolution
Root Cause:

The load balancer was configured with incorrect settings that failed to handle the traffic spike during a promotional event. Specifically, the session persistence setting was misconfigured, causing the load balancer to overload and drop incoming traffic instead of distributing it evenly across the servers.
Resolution:
The configuration was corrected by updating the session persistence settings and adjusting the maximum connection limits. The load balancer was then restarted to apply the new settings.
Corrective and Preventative Measures
Improvements and Fixes:
Configuration Review: Implement a thorough review process for all load balancer configurations before deployment.
Traffic Simulation: Conduct regular traffic simulations to test load balancer configurations under various scenarios.
Monitoring Enhancements: Enhance monitoring to detect misconfigurations early, focusing on load balancer performance metrics.
Tasks:
Update Load Balancer Configuration: Ensure correct session persistence and connection limits settings.
Implement Configuration Review Process: Establish a peer-review system for load balancer configuration changes.
Set Up Traffic Simulations: Use tools like Apache JMeter or Locust to simulate high traffic scenarios regularly.
Enhance Monitoring: Integrate additional monitoring for load balancer metrics, including traffic distribution and error rates.
Training: Conduct training sessions for the engineering team on load balancer configuration best practices.

