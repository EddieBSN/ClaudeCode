# Task CRUD Application

A small command-line task manager built to demonstrate clean, SOLID-compliant
structure with **zero external dependencies** (Python 3.9+ standard library only).

## Usage

```bash
python -m crud_app.cli.main create "Buy milk" -d "2 liters"
python -m crud_app.cli.main list
python -m crud_app.cli.main show 1
python -m crud_app.cli.main update 1 --done      # or --no-done to reopen
python -m crud_app.cli.main update 1 -t "Buy oat milk"
python -m crud_app.cli.main delete 1
```

Tasks are persisted to `tasks.db` (SQLite) in the working directory.

## Running the tests

```bash
python -m unittest discover tests -v
```

## Architecture

Dependencies point inward only; the domain knows nothing about storage or I/O.

```
cli  ─►  services  ─►  ports  ◄─  adapters
  \          │
   ─►      domain
```

| Layer      | Module                          | Responsibility                          | Collaborators |
|------------|---------------------------------|-----------------------------------------|---------------|
| domain     | `Task`                          | Immutable entity                        | 0             |
| domain     | `TaskFactory`                   | Constructs new, unsaved tasks           | 1             |
| domain     | `TaskValidator`                 | Domain invariants                       | 1             |
| ports      | `TaskRepository` (ABC)          | Storage contract                        | 1             |
| adapters   | `InMemoryTaskRepository`        | Dict-backed storage (tests)             | 2             |
| adapters   | `SqliteTaskRepository`          | SQLite persistence                      | 3             |
| services   | `TaskService`                   | CRUD use cases                          | 3             |
| cli        | `TaskPresenter`                 | Output formatting                       | 1             |
| cli        | `TaskCommands`                  | Subcommand handlers                     | 3             |
| cli        | `parser` / `registry`           | Declarative subcommand table            | —             |
| cli        | `main`                          | Composition root (wiring only)          | —             |

### How SOLID is applied

- **S**ingle responsibility — entity, validation, storage, use cases, and
  presentation each live in their own class; no god classes.
- **O**pen/closed — new storage backends are added as new `TaskRepository`
  adapters; no existing code changes.
- **L**iskov substitution — a shared contract test suite
  (`tests/test_repositories.py`) runs identically against every adapter.
- **I**nterface segregation — the port exposes only the five CRUD methods the
  service consumes.
- **D**ependency inversion — `TaskService` depends on the abstract port;
  concrete adapters are chosen only in the composition root (`cli/main.py`).

Cyclomatic complexity stays low throughout: subcommands are declared as data
in `cli/registry.py` and consumed by a generic builder in `cli/parser.py` —
no if/elif dispatch chains and no imperative argparse call spam — and partial
updates use `Task.with_changes` instead of per-field branching.
