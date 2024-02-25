What is a server?

A server is a computer system or software program that provides functionality or resources to other computers or programs, typically over a network.
What is the role of the domain name?

A domain name serves as a human-readable label that represents the IP address of a server or group of servers on the internet, allowing users to easily access websites or services.
What type of DNS record is www in www.foobar.com?

The "www" in a domain name like www.foobar.com typically corresponds to a DNS record called a CNAME (Canonical Name) record, which is used to alias one domain name to another.
What is the role of the web server?

The web server's role is to handle incoming HTTP requests from clients (such as web browsers) and serve web pages, files, or other content in response.
What is the role of the application server?

An application server hosts and manages applications or software services, handling tasks such as business logic processing, data access, and application execution for client applications or users.
What is the role of the database?

The database stores, manages, and retrieves data in a structured format, providing a persistent data storage solution for applications and services to access and manipulate data as needed.
What is the server using to communicate with the user's computer requesting the website?

The server communicates with the user's computer via the HTTP or HTTPS protocol, which allows for the transfer of web pages, files, and other content over the internet.
Issues with the Infrastructure:

SPOF (Single Point of Failure): This refers to a component in the infrastructure that, if it fails, will cause the entire system to fail. For example, if there's only one web server and it goes down, the website will become inaccessible. To mitigate this, redundancy and failover mechanisms can be implemented, such as having multiple servers or using load balancers.

Downtime during maintenance: When performing maintenance tasks like deploying new code that requires restarting the web server, the website may experience downtime, resulting in temporary unavailability for users. To minimize downtime, strategies like rolling deployments and blue-green deployments can be used to deploy updates with minimal disruption to service.

Scalability limitations: If the infrastructure cannot handle a sudden influx of incoming traffic, the system may become overloaded, leading to degraded performance or downtime. To address scalability limitations, techniques such as horizontal scaling (adding more servers) and vertical scaling (increasing server capacity) can be employed, along with implementing auto-scaling policies to automatically adjust resources based on demand.
