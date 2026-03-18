# Sorting Algorithms Analysis

**Aditi Sinha, 241CS202, S2**

**Neha Kamath, 241CS240, S2**

---

## Overview

This project implements and analyses the performance of seven sorting algorithms across
different input types and sizes. The algorithms studied are:

- Selection Sort
- Bubble Sort
- Insertion Sort
- Merge Sort
- Quick Sort (3 variants):
  - Pivot = first element
  - Pivot = random element
  - Pivot = median of first, middle and last elements
- Heap Sort
- Radix Sort

---

## How to Run

**Step 1 — Install dependencies:**
```bash
pip install -r requirements.txt
```

**Step 2 — Generate test cases:**
```bash
python3 utils/testCaseGenerator.py
```

**Step 2 — Run:**
```bash
python3 main.py
```

Graphs will be saved to the `graphs/` folder.

---

## Datasets

| File | Description | Test Cases |
|---|---|---|
| `ascending_dataset.txt` | Arrays sorted in increasing order | 40 |
| `descending_dataset.txt` | Arrays sorted in decreasing order | 40 |
| `random_dataset.txt` | Randomly shuffled arrays | 200 (5 per size) |

Input sizes range from **n = 50 to n = 2000** in steps of 50.

---

## Project Structure
```
PracticalAssignment/
├── sortingAlgos/
│   ├── bubbleSort.py
│   ├── selectionSort.py
│   ├── insertionSort.py
│   ├── mergeSort.py
│   ├── heapSort.py
│   ├── radixSort.py
│   ├── quickSortFirst.py
│   ├── quickSortRandom.py
│   └── quickSortMedian.py
├── utils/
│   ├── testCaseGenerator.py
│   └── plotter.py
│   
├── testcases/
├── graphs/
├── requirements.txt
├── main.py
└── README.md
```