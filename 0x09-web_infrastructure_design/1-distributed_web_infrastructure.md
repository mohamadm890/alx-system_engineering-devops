Load Balancer (HAProxy): Added to distribute incoming traffic across multiple web servers for improved performance, scalability, and availability.
Database Primary-Replica Cluster: Implemented to enhance database performance, scalability, and fault tolerance by replicating data from the primary node to replica nodes.
Load Balancer Distribution Algorithm:

The load balancer is configured with a Round Robin distribution algorithm, which evenly distributes incoming requests among the backend servers in a cyclic manner.
Active-Active or Active-Passive Setup:

The load balancer is configured for an Active-Active setup, where both servers actively handle incoming requests simultaneously. In contrast, an Active-Passive setup would involve one server actively serving traffic while the other remains on standby.
Primary-Replica (Master-Slave) Database Cluster:

In a Primary-Replica cluster, the primary node (master) handles write operations, while replica nodes (slaves) replicate data from the primary node and handle read operations. This setup improves scalability, fault tolerance, and read performance.
Difference Between Primary and Replica Nodes:

The primary node is responsible for handling write operations and maintaining the authoritative copy of the database. Replica nodes replicate data from the primary node and serve read operations, improving overall performance. In regard to the application, the primary node is used for write-intensive operations, while replica nodes are used for read-intensive operations.
Issues with the Infrastructure:

Single Point of Failure (SPOF):

The primary point of failure lies in the absence of redundancy for critical components such as the load balancer, web server, application server, and database. If any of these components fail, it could lead to downtime or service disruption.
Security Issues:

Without a firewall and HTTPS encryption, the infrastructure is vulnerable to attacks, data breaches, or unauthorized access. Implementing firewalls, SSL/TLS certificates, and secure communication protocols is essential to ensure data security and protect against threats.
Lack of Monitoring:

Without proper monitoring tools, it's challenging to detect and troubleshoot issues proactively. Implementing monitoring solutions allows for real-time visibility into system performance, availability, and security, enabling timely response to potential issues and minimizing downtime.
