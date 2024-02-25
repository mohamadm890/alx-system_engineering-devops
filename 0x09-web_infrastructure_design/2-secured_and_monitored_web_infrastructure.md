Reasons for Adding Additional Elements:
Firewalls: Firewalls are added to control incoming and outgoing network traffic based on predetermined security rules. They act as a barrier between trusted internal networks and untrusted external networks, protecting the infrastructure from unauthorized access, malicious attacks, and potential security breaches.
HTTPS Traffic: Traffic is served over HTTPS to encrypt data transmitted between the client (e.g., web browser) and the server, ensuring confidentiality, integrity, and authenticity of the communication. HTTPS protects sensitive information such as login credentials, personal data, and financial transactions from eavesdropping, tampering, and man-in-the-middle attacks.
Monitoring: Monitoring is used to track the performance, availability, and health of the infrastructure components in real-time. It helps identify issues, diagnose problems, optimize performance, and ensure the reliability and stability of the system.
Monitoring Tool and Data Collection: A monitoring tool such as Prometheus or Nagios collects data by periodically querying various metrics and logs from the infrastructure components. These metrics include CPU usage, memory usage, disk space, network traffic, error rates, response times, and other relevant performance indicators.
Monitoring Web Server QPS (Queries Per Second): To monitor web server QPS, you can configure the monitoring tool to collect and analyze metrics related to HTTP requests or transactions processed by the web server over a specific time period. This may involve monitoring the number of requests served, response times, error rates, and throughput.
Issues with the Infrastructure:

Terminating SSL at the Load Balancer Level:

Terminating SSL (HTTPS) at the load balancer level can be an issue because it requires the load balancer to decrypt and then re-encrypt the traffic before forwarding it to backend servers. This adds extra processing overhead on the load balancer and increases the risk of exposing sensitive data if the communication between the load balancer and backend servers is not adequately secured.
Single MySQL Server Capable of Accepting Writes:

Having only one MySQL server capable of accepting writes creates a single point of failure (SPOF) for write operations. If the primary MySQL server fails, it can lead to data loss, service downtime, and potential data inconsistency. Implementing a Primary-Replica (Master-Slave) cluster with multiple replica nodes helps mitigate this risk by providing redundancy, fault tolerance, and data replication.
Uniformity of Server Components:

Having servers with all the same components (database, web server, and application server) might be a problem because it lacks component isolation and diversity. If a critical vulnerability or issue affects one component (e.g., a software bug or security flaw), it can potentially impact all servers simultaneously, leading to widespread service disruption or compromise. Introducing diversity in server components and versions can help reduce the risk of cascading failures and improve overall system resilience.
