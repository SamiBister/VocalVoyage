# Use Typing with Python

## Status

Accepted

## Context

To improve the reliability, maintainability, and robustness of our Python codebase, we needed to decide whether to enforce the use of typing (type hints) in our project. Python's dynamic nature allows flexibility but can also introduce runtime errors that could have been prevented through static analysis. Using type hints aligns with our goals of building a robust, scalable, and developer-friendly application.

Key considerations for this decision include:

- **Code Robustness:** Typed code can prevent a significant number of bugs by catching type-related errors during development.
- **Readability:** Type hints improve code readability and make the intent of functions and variables clearer to developers.
- **Tooling:** Modern tools (e.g., MyPy, Pyright) leverage type hints for static analysis, improving developer productivity.
- **Safety:** Strong typing enforces better data handling practices, ensuring safer code in larger, more complex systems.

## Decision

We have decided to enforce the use of **Python typing** in all new code and gradually refactor existing code to include type hints. This decision is based on the following:

1. **Improved Code Quality:** Typing provides early detection of bugs by enabling static type checking.
2. **Enhanced Developer Experience:** Type hints improve IDE support, offering better autocompletion and inline documentation.
3. **Safety and Predictability:** Typed code reduces ambiguity, making it easier for developers to predict the behavior of functions and components.
4. **Scalability:** As the project grows, typing makes it easier to onboard new team members and maintain the codebase.
5. **Community Standards:** Typing is increasingly becoming the standard practice in Python, ensuring long-term compatibility and alignment with best practices.

## Consequences

### Positive

- **Bug Prevention:** Many potential runtime errors are caught during development.
- **Ease of Maintenance:** Type annotations make the code self-documenting and easier to understand.
- **Tool Integration:** Enables the use of tools like MyPy, Pyright, and Pylance for static analysis and error checking.
- **Future-Proofing:** Keeps the project aligned with modern Python development practices.

### Negative

- **Initial Overhead:** Existing code will need to be refactored gradually, requiring additional developer time.
- **Learning Curve:** Team members unfamiliar with typing may need initial training.
- **Complexity in Certain Cases:** For highly dynamic or polymorphic code, adding type hints can be cumbersome.

## Follow-Up Actions

1. **Establish Typing Guidelines:** Define and document standards for using type hints in the codebase (e.g., PEP 484, PEP 561).
2. **Tooling Setup:** Integrate MyPy or similar static type checkers into the CI/CD pipeline.
3. **Team Training:** Provide training for developers unfamiliar with Python typing.
4. **Incremental Refactoring:** Gradually introduce type hints into existing code while enforcing them in all new code.
5. **Review Process:** Update code review guidelines to include checks for appropriate use of type hints.
