## Installation
The library requries Python>=3.8 and to install the package simply run:
```bash
pip install levenshtein_matching
```

## Why
Performing string matching between to lists is an $n\times m$ operation. Depending on your use case and the size of the lists you want to match this becomes unfeasible. This library exists to leverage Rust's performance to decrease run time for such operations.

## Example
```python
from levenshtein_matching import find_best_match_levenshtein

target = [("String 1", 1), ("String 2", 2)]
query = [("String 2", 0.8), ("String 1", 0.5)]
threshold = 0.9

target_values, query_values = find_best_match_levenshtein(target, query, threshold)
print(f"Target values: {target_values}")
print(f"Query values: {query_values}")
```
Output:
```
Target values: [2, 1]
Query values: [0.8, 0.5]
```
