# Use `uv` for Python Tooling

## Status

Accepted

## Context

UV is a new tool for python. It replaces pip, poetry, pyenv, twine, pyenv and more.
It simplifies the python development workflow by providing a single tool for all python development tasks.
It is written in Rust and is faster than the existing tools.
it is supported with MacOS, Linux and Windows.
It install and manages the python versions, enabling the managing of development environments in codebase.

## Decision

We use UV with this repository to manage the python development environment.

## Consequences

The users of the repository will have to install UV to manage the python development environment.
Github actions will have to be updated to use UV.

### Positive

Setting up the development environment will be easier and faster.
Operations are faster.

### Negative

GitHub Dependabot does not support UV yet. Workaround needs to be found.
