# DSA Progress Tracker

This README serves as a structured record of all the Data Structures and Algorithms (DSA) topics I have studied, along with problem-solving approaches, time complexities, and solved problems. This will help in tracking progress, revisiting concepts, and improving problem-solving skills.

---

## 📌 **Table of Contents**
- [Binary Search](#binary-search)
- [Kadane's Algorithm](#kadanes-algorithm)
- [2D Arrays](#2d-arrays)
- [More Topics...](#more-topics)

---

## 🏆 **Tracking Progress**
Each topic has:
- ✅ **Checkmark** to indicate completion.
- 📌 **Priority Level** (High/Medium/Low) to decide importance.
- 📖 **Understanding Section** to summarize key concepts.
- 🔗 **Solved Problems** section to list related problems.

---

## 📂 **Topics**

### 📍 Binary Search  
- [ ] **Status:** _In Progress / Completed_
- 📌 **Priority:** High
- **What is Binary Search?**  
  Binary Search is an efficient searching algorithm that works on sorted arrays by repeatedly dividing the search space in half.
- **Approach:**  
  - Find the middle element.
  - If the target is equal to the middle element, return the index.
  - If the target is smaller, search the left half.
  - If the target is larger, search the right half.
  - Repeat this process until the search space is exhausted.
- **When to Use?**  
  - When the array is **sorted**.
  - When you need a logarithmic time complexity solution.
- **Time Complexity:**  
  - **Best case:** O(1)  
  - **Worst & Average case:** O(log n)
- **Solved Problems:**  
  - [ ] [Leetcode 704: Binary Search](https://leetcode.com/problems/binary-search/)
  - [ ] [Find in Mountain Array] (https://leetcode.com/submissions/detail/1594264486/)
  - [ ] [Peak Index in a Mountain Array] (https://leetcode.com/submissions/detail/1594214185/)
  - [ ] [Find Peak Element] (https://leetcode.com/submissions/detail/1594139855/)
  - [ ] [Ceiling and Floor number] (https://www.geeksforgeeks.org/ceiling-in-a-sorted-array/, https://www.naukri.com/code360/problems/ceiling-in-a-sorted-array_1825401?leftPanelTabValue=SUBMISSION)
  - [ ] [Find First and Last Position of Element in Sorted Array] (https://leetcode.com/submissions/detail/1593118638/)
  - [ ] [Search in Rotated Sorted Array] (https://leetcode.com/submissions/detail/1593897478/)
  - [ ] [Find Smallest Letter Greater Than Target] (https://leetcode.com/submissions/detail/1591697009/)
  - [ ] [Infinite Sorted Array] (https://www.geeksforgeeks.org/find-position-element-sorted-array-infinite-numbers/)

 
  
### 📍 Rotated and Sorted Array
  - [ ] [Find Minimum Element in Sorted and Rotated Array] (https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)
  - [ ] [Leetcode 33: Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
  - [ ] [Find K Rotation] (https://takeuforward.org/arrays/find-out-how-many-times-the-array-has-been-rotated/)
  - [ ] [Check if Array Is Sorted and Rotated] (https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/submissions/)
---



### 📍 Bubble Sort

- 📌 **Priority:** Medium
- **What is Bubble Sort?**\
  Bubble Sort is a simple comparison-based algorithm where each pair of adjacent elements is compared and swapped if they are in the wrong order.
- **Time Complexity:** O(n²), Best Case O(n) when array is already sorted.
- **Solved Problems:**
  - ✅ [Bubble Sort – TakeUForward](https://takeuforward.org/data-structure/bubble-sort-algorithm/)

### 📍 Selection Sort

- 📌 **Priority:** Medium
- **What is Selection Sort?**\
  Selection Sort selects the smallest (or largest) element from the unsorted part and swaps it with the first unsorted element.
- **Time Complexity:** O(n²)
- **Solved Problems:**
  - ✅ [Selection Sort – TakeUForward](https://takeuforward.org/sorting/selection-sort-algorithm/)

### 📍 Insertion Sort

- 📌 **Priority:** Medium
- **What is Insertion Sort?**\
  Insertion Sort builds the sorted array one element at a time by comparing and inserting elements into their correct position.
- **Time Complexity:** O(n²), Best Case O(n)
- **Solved Problems:**
  - ✅ [Insertion Sort – TakeUForward](https://takeuforward.org/data-structure/insertion-sort-algorithm/)

### 📍 Cycle Sort

- 📌 **Priority:** High
- **What is Cycle Sort?**\
  Cycle Sort is an in-place, non-stable sort algorithm optimal for cases where memory writes are costly. It's mainly used when elements range from 1 to n or 0 to n.
- **Time Complexity:** O(n)
- **Solved Problems:**
  - ✅ [Missing Number (LeetCode)](https://leetcode.com/problems/missing-number/)
  - ✅ [Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/submissions/1338369107/)
  - ✅ [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)
  - ✅ [First Missing Positive](https://leetcode.com/problems/first-missing-positive/description/)


### 📍 Kadane's Algorithm
- [ ] **Status:** _In Progress / Completed_
- 📌 **Priority:** High
- **What is Kadane's Algorithm?**  
  Kadane's Algorithm is used to find the maximum sum subarray in an array using a dynamic approach.
- **Approach:**  
  - Initialize `max_sum` and `current_sum` as the first element.
  - Iterate through the array and update `current_sum` by adding the current element or starting fresh.
  - Update `max_sum` whenever `current_sum` is higher.
- **When to Use?**  
  - When finding the largest sum of contiguous elements.
- **Time Complexity:**  
  - O(n)
- **Solved Problems:**  
  - [ ] [Leetcode 53: Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
  - [ ] [] ()
---

### 📍 2D Arrays
- [ ] **Status:** _In Progress / Completed_
- 📌 **Priority:** Medium
- **What are 2D Arrays?**  
  2D arrays are arrays where each element is itself an array, forming a matrix-like structure.
- **Approach:**  
  - Iterating using nested loops.
  - Common operations: searching, transposing, rotating.
- **When to Use?**  
  - When dealing with matrices or grids.
- **Time Complexity:**  
  - Varies based on operation.
- **Solved Problems:**  
  - [ ] [Leetcode 240: Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)

---

## 📌 **More Topics**
- [ ] Two Pointers
- [ ] Sliding Window
- [ ] Recursion & Backtracking
- [ ] Dynamic Programming
- [ ] Graphs & Trees
- [ ] Sorting & Searching Algorithms

---

### 🔍 **How to Use This Tracker?**
- Mark a **checkbox** (✅) when a topic is completed.
- Update **priority levels** based on difficulty.
- Add **new problem links** as you solve more.
- Keep refining your understanding over time.

---

This document will help in revisiting concepts quickly and keeping track of progress systematically. 🚀

