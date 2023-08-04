# Session 8 : 2/8/2023
## Cases for specified architecture pattern
- Layered Architecture:\
Use Case: A web application with separation of concerns where the presentation layer, business logic, and data access are distinct layers. This promotes modularity and ease of maintenance.
- Microservices Architecture:\
Use Case: Large and complex applications where different components can be developed, deployed, and scaled independently. Ideal for teams working on separate services with their own technology stacks.
- Service-Oriented Architecture (SOA):\
Use Case: Large-scale enterprise applications where different services communicate over a network, promoting reusability and interoperability.
- Model-View-Controller (MVC):\
Use Case: Web applications where a clear separation between data (Model), user interface (View), and control logic (Controller) is needed for better code organization.
- Repository Pattern:\
Use Case: Applications that need a standardized way to access data from various sources, promoting separation of concerns and making data access more maintainable.
## What is EERD ?
EERD stands for "Enhanced Entity-Relationship Diagram." It is an advanced version of the traditional Entity-Relationship Diagram (ERD) used in database design. An EERD extends the concepts of ERDs by adding additional modeling capabilities and features to represent more complex relationships and constraints in a database system.\
Features :
1. Subtypes and Supertypes: EERD allows for modeling inheritance hierarchies, where entities can be organized into subtypes and supertypes. This is useful for representing generalization and specialization relationships.
2. Categories and Attributes Inheritance: EERD supports the inheritance of attributes and categories (relationships) from supertype entities to subtype entities.
3. Overlapping and Disjoint Subtypes: EERD lets you define whether subtypes are exclusive (disjoint) or can overlap (non-disjoint) with each other.
4. Union Types: EERD introduces the concept of a union type, which represents a single entity that is a member of multiple entity types.
5. Derived Attributes: EERD allows for specifying attributes that can be calculated or derived from other attributes.
6. Multi-valued Attributes: EERD supports attributes that can hold multiple values for an entity.
7. Roles and Recursive Relationships: EERD enables modeling of recursive relationships and the assignment of roles to entities in relationships.
8. Weak Entities: EERD includes the concept of weak entities that rely on a strong entity for their existence.
9. Constraints: EERD provides more powerful constraint modeling, such as specifying minimum and maximum cardinalities for relationships.
10. Generalization and Aggregation: EERD enhances the representation of generalization hierarchies and aggregation relationships between entities.
## NoSQL Databases Examples
- MongoDB
- Cassandra
- Couchbase
- Redis
- Amazon DynamoDB
- Neo4j
- CouchDB
- Riak
- HBase
- Elasticsearch
## What is power query ?
Power Query is a data transformation and data preparation tool developed by Microsoft. It is part of the Microsoft Power Platform suite of business intelligence and data analytics tools, which also includes Power BI, Power Pivot, and Power Automate (previously known as Microsoft Flow).

Power Query is designed to help users discover, connect, transform, and combine data from various sources into a format that is suitable for analysis and reporting. It is particularly useful when working with large and complex datasets that require cleaning, shaping, and merging from different sources.
## Compare between Azure, GCP and AWS

| Aspect                        | Azure                                       | GCP                                       | AWS                                          |
|-------------------------------|---------------------------------------------|-------------------------------------------|----------------------------------------------|
| **Pricing Model**             | Pay-as-you-go, reserved instances, cost tools | Pay-as-you-go, sustained use discounts    | Pay-as-you-go, reserved instances, cost tools |
| **Suitable Projects**         |                                             |                                           |                                              |
| Enterprise Applications       | ✓                                           |                                           | ✓                                            |
| Windows-Based Workloads      | ✓                                           |                                           |                                              |
| Hybrid Cloud Scenarios        | ✓                                           |                                           |                                              |
| Data Analytics & ML           |                                             | ✓                                         |                                              |
| Modern App Development        |                                             | ✓ (microservices, containers)             |                                              |
| Data Science & Analytics      |                                             | ✓ (advanced analytics)                   |                                              |
| Scalable Web Applications     |                                             |                                           | ✓                                            |
| E-Commerce Platforms          |                                             |                                           | ✓                                            |
| Startups & Small Businesses   |                                             |                                           | ✓                                            |
| IoT Applications              |                                             |                                           | ✓                                            |

