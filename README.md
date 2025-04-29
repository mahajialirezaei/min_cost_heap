# Min Cost Heap

## 🧮 Problem Description

Given an array of `n` integers, at each step you can:

- Select **any two elements**,
- Merge them into one element whose value is the **sum of the two**, and
- Pay a **cost equal to that sum**.

Repeat this until only one element remains. The goal is to **minimize the total cost** of all the merge operations.

### Example

Input:
```
[1, 2, 3, 4]
```

Optimal merge sequence:
- Merge 1 + 2 → cost = 3 → new array = [3, 3, 4]
- Merge 3 + 3 → cost = 6 → new array = [6, 4]
- Merge 6 + 4 → cost = 10 → new array = [10]

Total cost: `3 + 6 + 10 = 19`

---

ap)** to always merge the two smallest elements first. This greedy strategy ensures the minimum total cost.

### Time Complexity

- Heap operations (`heappop`, `heappush`): `O(log n)`
- Total complexity: `O(n log n)`

---

## 📂 File Structure

```
min_cost_heap/
├── min_cost.py        # Main implementation
└── README.md          # This file
```


```text
4
1 2 3 4
```

Expected output:

```
Total cost: 19
```


---

## ✍️ Author

[MohammadAmin HajiAlirezaei](https://github.com/mahajialirezaei)
```
