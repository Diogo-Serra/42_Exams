def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:

    order = []
    remaining = set(packages)

    while remaining:
        ready = sorted(
            p for p in remaining
            if all(d in order for d in packages[p] if d in packages)
        )
        if not ready:
            return []
        order.extend(ready)
        remaining.difference_update(ready)

    return order
