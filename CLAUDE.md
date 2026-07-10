# Repository Guide

This is a multi-project repository. Each project lives in its own top-level
folder with its own README; the root README indexes them. When adding a new
project, create a new folder and add a row to the root README's table.

## Projects

- `task-crud/` — Python CLI task manager (zero external dependencies,
  stdlib only, Python 3.9+)

## Conventions

- **Architecture**: layered, SOLID-compliant. Dependencies point inward:
  `cli -> services -> ports <- adapters`, with `domain` at the center.
  Services depend on abstract ports, never concrete adapters; concrete
  implementations are chosen only in the composition root.
- **Class size**: keep classes small — fewer than 4 collaborators each.
  No god classes.
- **Complexity**: prefer declarative tables and dispatch via data over
  if/elif chains; prefer immutable entities with `with_changes`-style
  copies over mutation.
- **Imports**: absolute paths (e.g. `crud_app.domain.task`), PEP 8 grouping
  (stdlib, third-party, local). Sibling modules within a package import each
  other by module, not through the package `__init__`, to avoid cycles.
- **Object creation**: construct new entities through factories
  (e.g. `TaskFactory`); services validate and persist.

## Testing

Run tests from inside the project folder:

```bash
cd task-crud && python -m unittest discover tests
```

Repository adapters must pass the shared contract test suite
(`tests/test_repositories.py`) — add new adapters to that suite.
