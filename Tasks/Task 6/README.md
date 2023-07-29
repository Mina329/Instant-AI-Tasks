# Session 6 : 26/7/2023

## How to apply security in functional programming ?

- Immutability: In functional programming, data is typically immutable, meaning once created, it cannot be modified. By making data immutable, you prevent unintended changes to the data, leading to a more secure and predictable system.
- Pure Functions: Pure functions have no side effects and always produce the same output for the same input. They don't modify any external state, making them easier to reason about and less prone to security vulnerabilities.
- Closures: In functional programming, closures are functions that capture variables from their lexical context. By using closures effectively, you can control access to variables and data, ensuring they are not directly exposed to the outside world.
- Higher-order functions: Functional programming often relies on higher-order functions that take other functions as arguments. By controlling the functions passed as arguments, you can restrict access to certain functionalities.
- Data Hiding: Although functional programming does not have the notion of "private" like in OOP, you can achieve data hiding by limiting the scope of variables and functions using lexical scoping and closures.
- Module Systems: Functional programming languages often have module systems that allow you to define what functions and data are exposed outside of a module. By carefully designing your module's public API, you can control what functionality is accessible from other parts of the codebase.
- Type Systems: Many functional programming languages have robust type systems that allow you to define data structures and enforce certain constraints. By utilizing the type system effectively, you can prevent unintended data manipulation and ensure the correctness of your code.
- Monads and Functors: These are higher-level abstractions that allow controlled access to values within a functional context. They provide a way to manage effects and computations in a safe and controlled manner.
- Functional Purity and Referential Transparency: Emphasizing functional purity and referential transparency ensures that functions behave predictably, and the absence of side effects makes it easier to reason about security aspects.

## How to apply Scalability in functional programming ?

- Stateless Functions: In functional programming, functions are typically stateless and do not rely on shared mutable state. Stateless functions make it easier to scale the system horizontally by distributing computation across multiple nodes or processes.
- Immutability: Functional programming encourages the use of immutable data structures. Immutable data makes it easier to reason about code, facilitates concurrent and parallel processing, and reduces the risk of data inconsistencies during scaling.
- Parallelism and Concurrency: Functional programming languages often provide constructs for parallelism and concurrency, allowing you to take advantage of multi-core processors and distributed systems. Functions designed without side effects can be executed in parallel without causing conflicts.
- Higher-order Functions: Higher-order functions allow for more abstract and reusable code, which can help in managing the complexity of a growing system. They enable the creation of generic functions that can be applied to different data sets, promoting code reusability.
- Functional Data Structures: Functional programming languages often come with specialized data structures optimized for functional operations. These data structures can enhance performance and memory usage, especially when scaling involves handling large amounts of data.
- Distributed Data Processing: Functional programming is well-suited for distributed data processing frameworks. Systems like Apache Spark and Hadoop can leverage functional programming principles to process data efficiently across a cluster of machines.
- Composability: Functional programming encourages composing small, focused functions to build more complex operations. This composability makes it easier to reason about the behavior of the system and maintain it as it scales.
- Lazy Evaluation: Some functional programming languages support lazy evaluation, where expressions are only evaluated when needed. Lazy evaluation can improve performance by avoiding unnecessary computations, especially when dealing with large data sets.
- Message Passing: Functional programming fits well with the actor model, where actors communicate via message passing. This approach enables a scalable, distributed system that can handle high levels of concurrency.
- Cloud Services and Microservices: Functional programming can be combined with cloud services and microservices architecture to achieve greater scalability. Microservices, with their independent and modular nature, align well with the principles of functional programming.

## SOLID principles

```
S -> Single responsibility
O -> Open-Closed
L -> Liskov substitution
I -> Interface segregation
D -> Dependency inversion
```
## What is code injection ?

 it is a type of security vulnerability that occurs when an attacker is able to insert and execute malicious code within a software application. The term "injection" refers to the unauthorized insertion of code into an application's data input, causing the application to process it as valid code and execute it unintentionally.