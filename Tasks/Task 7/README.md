# Session 7 : 30/7/2023

## DevOps Tools

1. Version Control Systems:
    - Git: Distributed version control system for tracking changes in source code.
        - Gitlab
        - Github
        - Bitbucket
2. Continuous Integration/Continuous Deployment (CI/CD) Tools:
    - Jenkins: An open-source automation server for building, testing, and deploying applications.
    - Travis CI: A cloud-based CI service that integrates well with GitHub repositories.
    - CircleCI: A cloud-based CI/CD platform that supports various programming languages and environments.
    - GitLab CI/CD: Integrated CI/CD features provided by GitLab.
3. Configuration Management Tools:
    - Chef: A configuration management tool for defining infrastructure as code.
    - Ansible: An open-source automation tool for configuration management, application deployment, and task automation.
    - Puppet: A configuration management tool for automating the provisioning and configuration of servers.
4. Infrastructure as Code (IaC) Tools:
    - Terraform: An open-source tool for provisioning and managing infrastructure resources.
    - CloudFormation: A service provided by AWS to define infrastructure resources in AWS using JSON or YAML.
5. Containerization:
    - Docker: A platform to develop, ship, and run applications in containers.
    - Kubernetes: An open-source container orchestration platform for automating deployment, scaling, and management of containerized applications.
6. Monitoring and Logging:
    - Prometheus: An open-source monitoring and alerting toolkit designed for container environments.
    - Grafana: A data visualization and monitoring tool that works well with Prometheus and other data sources.
    - ELK Stack: Elasticsearch, Logstash, and Kibana stack for centralized logging and analysis.
7. Collaboration and Communication:
    - Slack: A popular team collaboration and messaging tool.
    - Microsoft Teams: A collaboration platform that integrates with various Microsoft services.
8. Cloud Platforms:
    - AWS (Amazon Web Services): A comprehensive cloud computing platform by Amazon.
    - Azure: A cloud computing platform by Microsoft.
    - Google Cloud: A suite of cloud computing services by Google.
## Comparison between DevOps & Agile
| Aspect                 | Agile                                | DevOps                                |
|------------------------|--------------------------------------|---------------------------------------|
| Focus and Purpose      | Software development methodology     | Practices to bridge dev and ops       |
| Scope                  | Development phase of lifecycle      | Entire software delivery pipeline    |
| Collaboration          | Team members and stakeholders       | Dev and ops teams collaboration      |
| Automation             | Some use automation for development  | Core principle, extensive automation  |
| CI/CD                  | May include CI, not mandated CD     | Emphasizes CI/CD practices            |
| Cultural Aspects       | Customer-centric and adaptive        | Collaboration and shared responsibility|
| Metrics and KPIs       | Velocity, burndown, cycle time, etc. | Frequency, success of deployments, MTTR|

## DataOps & MLOps
### DataOps :
DataOps is a set of practices and methodologies that aim to improve the efficiency and collaboration in the data engineering and data analytics lifecycle. It borrows concepts from DevOps, Agile, and Lean principles to streamline data-related processes, making them more automated, agile, and responsive to business needs. The goal of DataOps is to shorten the cycle time from raw data to actionable insights while maintaining data quality, security, and governance.\
Key aspects of DataOps include:
- Version Control: Applying version control practices to manage changes in data pipelines and configurations, similar to software code versioning.
- Automation: Employing automation tools and frameworks to accelerate data processing, validation, and deployment tasks.
- Collaboration: Promoting cross-functional collaboration among data engineers, data scientists, analysts, and business stakeholders to ensure better understanding and alignment of data requirements.
- Continuous Integration and Continuous Deployment (CI/CD): Applying CI/CD practices to data pipelines, making it easier to deliver changes and updates to data processing workflows.
- Monitoring and Logging: Implementing monitoring and logging mechanisms to track data pipeline performance and identify issues promptly.
### MLOps :
MLOps is an extension of DevOps principles that focuses on streamlining the machine learning lifecycle. It aims to improve collaboration between data scientists, machine learning engineers, and operations teams to efficiently build, deploy, and manage machine learning models at scale.\
Key aspects of MLOps include:
- Model Versioning: Applying version control to machine learning models and associated code, ensuring reproducibility and easy rollbacks.
- Continuous Integration and Continuous Deployment (CI/CD) for ML: Automating the process of training, testing, and deploying machine learning models into production environments.
- Model Monitoring: Implementing monitoring mechanisms to track model performance, detect drift, and trigger alerts for retraining as needed.
- Model Governance: Ensuring compliance with regulations and ethical considerations in model development and deployment.
- Infrastructure Orchestration: Using containerization and orchestration tools to manage the infrastructure required for training and serving ML models.

## V-Model

![V-model](https://mina329.github.io/sqa/images/v-model.png)

## Design pattern & Architecture pattern Difference

| Aspect                 | Design Patterns                                      | Architecture Patterns                              |
|------------------------|------------------------------------------------------|-----------------------------------------------------|
| Focus                  | Implementation-level solutions                      | High-level system organization and structure       |
| Granularity            | Lower level of granularity (classes and objects)    | Higher level of granularity (entire system)        |
| Scope                  | Concerned with class interactions and responsibilities | Address system structure, component communication, data flow, and deployment |
| Examples               | Singleton, Factory Method, Factory of Factories | MVVM, MVC |

## OOP Project with class diagram
### Code
[OOP_Project](https://github.com/Mina329/Instant-AI-Tasks/tree/main/Projects/OOP%20Project%20-%20Library%20Management%20System)
### UseCase
![oop-project](https://github.com/Mina329/Instant-AI-Tasks/blob/main/Projects/OOP%20Project%20-%20Library%20Management%20System/library_management_system_usecase.png?raw=true)
### Class Diagram
![oop-project](https://github.com/Mina329/Instant-AI-Tasks/blob/main/Projects/OOP%20Project%20-%20Library%20Management%20System/library_management_system_classdiagram.png?raw=true)