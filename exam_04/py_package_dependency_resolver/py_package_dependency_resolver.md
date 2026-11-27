# Package Dependency Resolver

> File: `py_package_dependency_resolver.py`

## Description

Write a function that determines a valid package installation order by resolving dependencies. Use topological sorting to ensure dependencies are installed before the packages that require them.

The function should:

- Take a dictionary where keys are package names and values are lists of dependencies.
- Return packages in installation order (dependencies first).
- Return an empty list if no valid order exists (circular dependencies).
- Handle empty input and isolated dependency chains.
- Ignore references to packages not in the input dictionary.

## Function Signature

```python
def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
```

## Algorithm Requirements

- Use topological sorting (e.g., Kahn's algorithm).
- Process packages with no remaining dependencies first.
- Ensure deterministic output when multiple valid orders exist.

## Edge Cases

- Empty input: return an empty list.
- Packages with no dependencies: include them in the output first.
- Multiple independent chains: process all chains.
- Circular dependencies: return an empty list.
- Non-existent dependencies: ignore missing packages.
- Self-dependencies: return an empty list.

## Examples

| # | Input | Output |
| :- | :--- | :--- |
| 1 | `package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []})` | `["driver", "database", "app"]` |
| 2 | `package_dependency_resolver({"A": [], "B": ["A"], "C": ["A", "B"]})` | `["A", "B", "C"]` |
| 3 | `package_dependency_resolver({})` | `[]` |
| 4 | `package_dependency_resolver({"X": ["Y"], "Y": ["X"]})` | `[]` |
| 5 | `package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]})` | `["api", "web", "backend", "frontend"]` |

## Notes

- For deterministic output, process packages alphabetically when choices exist.
- A package cannot be installed until all its dependencies are installed.
- If any circular dependency exists, no valid installation order is possible.
