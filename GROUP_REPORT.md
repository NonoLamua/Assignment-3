Group Collaboration Report: - Nono Lamua: Created repository and README.md - Pablo Muñoz: Docker-compose configuration. - Francisco Climent: Network explanation. - Rafa Moro: Security documentation and .env setup. - Yago Granada: Troubleshooting documentation. - Narcís Agustí: Group report and review. 

**Challenges the group faced**
- Defining a custom Docker network with static IPs was challenging because it required understanding Docker's IPAM configuration and ensuring that all containers communicated correctly.

- Writing a multi-stage Dockerfile was a new concept for some members. Balancing the size of the production image while ensuring it included all necessary dependencies took several iterations

- Coordinating across the group to ensure all members contributed equally while meeting deadlines was difficult, especially with other coursework.


**Lessons learned from the project**
-Effective communication and task delegation were key to overcoming challenges. Using Git for collaboration helped streamline contributions but required everyone to stay synchronized.

- We learned how to configure multi-service applications using Docker Compose, including the nuances of custom networking, static IPs, and environment variable management.

- Multi-stage Dockerfiles taught us how to optimize Docker images for production while keeping development environments flexible.

- Using .env files and excluding them with .gitignore highlighted the importance of protecting sensitive data in software projects. We now understand the risks of exposing credentials and how to mitigate them.

- Breaking the project into parts and assigning responsibilities made it more manageable. We learned how to approach complex projects methodically, which will be useful in real-world scenarios.
