# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change.

Please note we have a code of conduct, please follow it in all your interactions with the project.

## **Branch Naming and Commit Message Guidelines for Automated Semantic Versioning**

Our repository uses **GitVersion** in `ContinuousDelivery` mode and follows **Conventional Commits** to automate semantic versioning. This ensures consistent versioning based on the scope and impact of changes while enabling developers to communicate intent through branch names and commit messages.

---

### **Branch Naming Guidelines**

1. **Main Branch**:
   - The `main` branch is our primary branch for production-ready code.
   - Semantic versioning is calculated based on commits merged into `main`.

2. **Feature Branches**:
   - Name feature branches using the format: `feature/<short-description>`.
   - Example:  

     ```
     feature/add-user-search
     feature/upgrade-authentication
     ```

3. **Bugfix Branches**:
   - Name bugfix branches using the format: `bugfix/<short-description>`.
   - Example:  

     ```
     bugfix/fix-null-pointer
     bugfix/correct-alignment
     ```

4. **Other Branches**:
   - Use clear, consistent names for other branches:
     - `hotfix/<short-description>`: Critical fixes for production.
     - `chore/<short-description>`: Maintenance or non-functional updates.
   - Example:  

     ```
     hotfix/critical-memory-leak
     chore/update-dependencies
     ```

---

### **Commit Message Guidelines**

Follow the **Conventional Commits** specification to indicate the type of change and its impact.

#### **Commit Message Format**

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

1. **Type**: Use one of the following:
   - **feat**: Introduces a new feature (increments **MINOR** version).
     - Example: `feat: add user authentication`
   - **fix**: Fixes a bug (increments **PATCH** version).
     - Example: `fix: resolve null pointer exception`
   - **chore**: Updates dependencies, tooling, or other maintenance tasks.
     - Example: `chore: update npm dependencies`
   - **docs**: Updates documentation.
     - Example: `docs: add API usage examples`
   - **refactor**: Code refactoring without functional changes.
     - Example: `refactor: simplify user input validation`
   - **style**: Code style or formatting changes (e.g., lint fixes).
     - Example: `style: reformat dashboard components`
   - **test**: Adds or updates tests.
     - Example: `test: add integration tests for login flow`

2. **Scope** (Optional):
   - Indicate the area of the code affected (e.g., `ui`, `api`, `auth`).
   - Format: `<type>(<scope>): <description>`
   - Example: `feat(auth): add OAuth2 support`

3. **Breaking Changes**:
   - Use `!` after the type or include `BREAKING CHANGE:` in the commit body.
   - **Major version increment**.
     - Example: `feat!: remove support for deprecated API`
     - Example with body:  

       ```
       feat: migrate to new database schema

       BREAKING CHANGE: Old schema support has been removed. Run migration script before deploying.
       ```

4. **Additional Guidelines**:
   - Keep the description concise and in **imperative mood** (e.g., "add", "fix", "update", not "added" or "fixed").
   - Use the **body** for further context or detailed explanations if necessary.
   - Use the **footer** for issues or references (e.g., `Closes #123`).

---

### **Examples**

#### **Feature Commit**

```
feat: add support for user profiles
```

#### **Bugfix Commit**

```
fix(ui): correct alignment issue on login page
```

#### **Breaking Change Commit**

```
feat!: drop support for legacy authentication

BREAKING CHANGE: Applications must now use OAuth2 for authentication.
```

#### **Chore Commit**

```
chore: update dependencies to latest versions
```

---

### **Why This Matters**

1. **Automated Versioning**:
   - Commit messages drive semantic versioning automatically.
   - `feat:` increments the **minor** version (e.g., `1.0.0 → 1.1.0`).
   - `fix:` or other non-breaking changes increment the **patch** version (e.g., `1.0.0 → 1.0.1`).
   - Breaking changes (`feat!:`) increment the **major** version (e.g., `1.0.0 → 2.0.0`).

2. **Clear Communication**:
   - Commit messages and branch names make it easier for developers to understand the purpose and impact of changes.

3. **Consistent Releases**:
   - Ensures accurate and predictable versioning, simplifying dependency management and release tracking.

By following these guidelines, we ensure smooth collaboration, clear communication, and reliable automated versioning in our development process.

## Pull Request Process

1. Ensure any install or build dependencies are removed before the end of the layer when doing a
   build.
2. Update the README.md with details of changes to the interface, this includes new environment
   variables, exposed ports, useful file locations and container parameters.
3. Increase the version numbers in any examples files and the README.md to the new version that this
   Pull Request would represent. The versioning scheme we use is [SemVer](http://semver.org/).
4. You may merge the Pull Request in once you have the sign-off of two other developers, or if you
   do not have permission to do that, you may request the second reviewer to merge it for you.

## Code of Conduct

### Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, gender identity and expression, level of experience,
nationality, personal appearance, race, religion, or sexual identity and
orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment
include:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

- The use of sexualized language or imagery and unwelcome sexual attention or
advances
- Trolling, insulting/derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information, such as a physical or electronic
  address, without explicit permission
- Other conduct which could reasonably be considered inappropriate in a
  professional setting

### Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

### Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at [INSERT EMAIL ADDRESS]. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

### Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at [http://contributor-covenant.org/version/1/4][version]

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/4/
