#Assignment3

**Assignment 3: Docker and Git Overview:**

This assignment demonstrates collaborative software development using Git and Docker. It includes setting up a shared Git repository, defining a branching workflow, creating a multi-service Dockerized application, configuring a custom network, implementing environment variables, and deploying the application. The project is divided into four parts:

1. Git Repository Setup and Collaboration
2. Docker Networking and Custom Configuration
3. Environment Variables and Multi-Stage Builds
4. Deployment and Group Report

**Repository Structure**

Assignment-3/

├── README.md                      # Project overview and documentation

├── docker-compose.yml             # Docker Compose configuration for web and database services

├── Dockerfile                     # Multi-stage build for the web service

├── .env                           # Environment variables (excluded in Git)

├── NETWORK_EXPLANATION.txt        # Explanation of custom network configuration

├── SECURITY_EXPLANATION.txt       # Security practices for sensitive files

├── TROUBLESHOOTING.md             # Issues faced during deployment and solutions

├── GROUP_REPORT.md                # Group contributions, challenges, and lessons learned

**Part 1: Git Repository Setup and Collaboration**

- A shared Git repository was created, and all group members cloned it.
- Each member contributed by committing their changes.

**Deliverables:**

Repository URL: git@github.com:NonoLamua/Assignment-3.git

Screenshots (Added in the ZIP file):

1. git log with commits from all members.


**Part 2: Docker Networking and Custom Configuration**


- Defined two services in docker-compose.yml:
- Web Service: A simple Python web server.
- Database Service: PostgreSQL.
- Configured a custom Docker network with static IPs.
- Wrote a detailed explanation of the network configuration in NETWORK_EXPLANATION.txt.

  
Deliverables:

1. docker-compose.yml
2. NETWORK_EXPLANATION.txt

Screenshot of docker network inspect custom_network.

**Part 3: Environment Variables and Multi-Stage Builds**

- Created a .env file for database credentials and web app ports.
- Built a multi-stage Dockerfile for the web service:
- Development stage for installing dependencies.
- Production stage for a lightweight build.
- Documented security considerations in SECURITY_EXPLANATION.txt.

Deliverables:
1. .env file (masked sensitive values).
2. Dockerfile.
3. SECURITY_EXPLANATION.txt.

**Part 4: Deployment and Group Report**

- Deployed the application using docker-compose up.
- Verified communication between services using static IPs and DNS names.
- Documented deployment challenges in TROUBLESHOOTING.md.
- Summarized group collaboration and lessons learned in GROUP_REPORT.md.

Deliverables:

1. TROUBLESHOOTING.md.
2. GROUP_REPORT.md.
3. Screenshot of docker ps showing running containers.


**How to Run the Application**
Prerequisites:

Install Docker and Docker Compose.

Clone this repository:

git clone git@github.com:NonoLamua/Assignment-3.git

cd Assignment-3

Steps to Run:
Create a .env file (or use the provided template):

POSTGRES_USER=user

POSTGRES_PASSWORD=password

POSTGRES_DB=exampledb

WEB_PORT=8000

Build and start the application:

docker-compose up -d

Verify services are running:


docker ps

Access the web service in your browser at:
http://localhost:8000


**Group Members**

- Member 1: [Nono Lamúa] - Git setup and README.md

- Member 2: [Pablo Muñoz] - docker-compose.yml

- Member 3: [Francisco Climent] - NETWORK_EXPLANATION.txt

- Member 4: [Rafael Moro] - .env and SECURITY_EXPLANATION.txt

- Member 5: [Yago Granada] - TROUBLESHOOTING.md

- Member 6: [Narcís Agustí] - GROUP_REPORT.md
