# Architectural Decision Records (ADRs)

## What is an ADR?

An **Architectural Decision Record (ADR)** is a document that captures an important architectural decision made along with its context and consequences. ADRs provide a concise and structured way to record the thought process behind significant technical decisions, ensuring that the rationale is preserved for current and future team members.

Each ADR follows a specific template to maintain consistency and clarity. In this repository, we use Michael Nygard's ADR template, which is widely recognized for its simplicity and effectiveness.

## Benefits of Using ADRs

1. **Historical Context:** ADRs provide a documented history of why specific technical decisions were made, aiding future troubleshooting and decision-making.
2. **Knowledge Sharing:** They help onboard new team members by offering insights into the application's architecture and decision-making rationale.
3. **Transparency:** ADRs promote clear communication and transparency within the team.
4. **Change Management:** They help track and manage changes to architectural decisions over time.
5. **Avoid Redundant Discussions:** By documenting past decisions, the team can avoid revisiting the same discussions repeatedly.

## Best Practices for ADRs

1. **One Decision Per ADR:** Each ADR should focus on a single architectural decision to maintain clarity.
2. **Immutable Records:** Old ADRs are never modified. If a decision is changed, a new ADR is created to document the new decision, and the previous one is marked as "superseded."
3. **Sequential Numbering:** Use sequential numbers for ADRs to provide an easy reference (e.g., `0001`, `0002`).
4. **Descriptive Names:** After the number, include a clear and concise name for the ADR (e.g., `0001_use_mysql_as_database.md`).
5. **Collaborative Review:** Encourage team discussions and reviews before finalizing an ADR.
6. **Keep It Short and Clear:** Avoid unnecessary details; focus on the decision, context, and consequences.

## ADR File Naming Convention

We follow a strict naming convention to ensure all ADRs are easily identifiable and organized:

- Format: `[number]_[decision_name].md`
- Example: `0001_use_mysql_as_database.md`

## Directory Structure

All ADRs are stored in the `docs/adrs` directory of this repository. The directory structure looks like this:

```
/docs/adrs/
  ├── index.md
  ├── 0001_use_mysql_as_database.md
  ├── 0002_switch_to_postgresql.md
  └── ...
```

## How to Write an ADR

Follow these steps to create a new ADR:

1. Navigate to the `docs/adrs` directory.
2. Create a new file with the next sequential number and a descriptive name (e.g., `0003_adopt_kubernetes.md`).
3. Use the following template for the content:

   ```markdown
   # [Title of Decision]

   ## Status

   [Proposed | Accepted | Superseded]

   ## Context

   [Describe the issue that prompted this decision. Include relevant background information.]

   ## Decision

   [State the decision that was made and why it was chosen.]

   ## Consequences

   [Describe the positive and negative effects of this decision.]
   ```

4. Commit the new ADR to the repository with a meaningful commit message.

## Superseding Old ADRs

When a new ADR replaces a previous one, mark the old ADR as "Superseded" in the **Status** section and link to the new ADR. For example:

```markdown
## Status

Superseded by [0002_switch_to_postgresql.md]
```

This ensures that the decision history is preserved without modifying the original record.

## Summary

ADRs are an essential tool for documenting architectural decisions in a clear, structured, and transparent manner. By following the practices outlined here, we can ensure that our technical decision-making is well-documented and easily understood by all team members, both current and future.
