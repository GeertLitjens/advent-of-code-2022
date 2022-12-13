---
layout: default
title: Day 8
description: Treetop Tree House

---

## Day 8

[Return to main page](../)


Simple array iteration and designing the right if statements. Part two was a bit
more challenging in terms of getting a somewhat efficient solution. Pretty happy
with the end result although I think part 2 can be more efficient.


### Part 1
> The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a previous expedition planted these trees as a reforestation effort. Now, they're curious if this would be a good location for a tree house.
>
> First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need to count the number of trees that are visible from outside the grid when looking directly along a row or column.
>
> The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle input). For example:
> ```
> 30373
> 25512
> 65332
> 33549
> 35390
> ```
> Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.
>
> A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.
>
> All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the interior nine trees to consider:
>
> - The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of height 5 are in the way.)
> - The top-middle 5 is visible from the top and right.
> - The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge.
> - The left-middle 5 is visible, but only from the right.
> - The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most height 2 between it and an edge.
> - The right-middle 3 is visible from the right.
> - In the bottom row, the middle 5 is visible, but the 3 and 4 are not.
>
> With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this arrangement.
>
> Consider your map; how many trees are visible from outside the grid?


 Bit more intesive parsing this time, but not a lot. Simply split the lines, determine the array shape from the lines and line length and convert the string input to an int numpy array.
```python
def _parse_data(self: "DaySolution", input_data: str) -> AoCData:
    lines = input_data.splitlines()
    arr_shape = (len(lines), len(lines[0]))
    arr = np.fromstring(
        ",".join(input_data.replace("\n", "")), dtype="int", sep=","
    ).reshape(arr_shape)
    return arr
```

 Iterate over all trees and simply check whether there are trees that are higher in the same row and column (up / down / right left). If not, add a visible tree.
```python
def _solve_part1(self: "DaySolution", parsed_data: AoCData) -> AoCData:
    rows, cols = parsed_data.shape
    nr_vis_trees = 2 * cols + 2 * (rows - 2)
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            cur_height = parsed_data[row, col]
            if (
                cur_height > np.max(parsed_data[:row, col])
                or cur_height > np.max(parsed_data[row + 1 :, col])
                or cur_height > np.max(parsed_data[row, :col])
                or cur_height > np.max(parsed_data[row, col + 1 :])
            ):
                nr_vis_trees += 1
    return nr_vis_trees
```

### Part 2

> Content with the amount of tree cover available, the Elves just need to know the best spot to build their tree house: they would like to be able to see a lot of trees.
>
> To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. (If a tree is right on the edge, at least one of its viewing distances will be zero.)
>
> The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house has large eaves to keep it dry, so they wouldn't be able to see higher than the tree house anyway.
>
> In the example above, consider the middle 5 in the second row:
> ```
> 30373
> 25512
> 65332
> 33549
> 35390
> ```
> - Looking up, its view is not blocked; it can see 1 tree (of height 3).
> - Looking left, its view is blocked immediately; it can see only 1 tree (of height 5, right next to it).
> - Looking right, its view is not blocked; it can see 2 trees.
> - Looking down, its view is blocked eventually; it can see 2 trees (one of height 3, then the tree of height 5 that blocks its view).
>
> A tree's scenic score is found by multiplying together its viewing distance in each of the four directions. For this tree, this is 4 (found by multiplying 1 * 1 * 2 * 2).
>
> However, you can do even better: consider the tree of height 5 in the middle of the fourth row:
> ```
> 30373
> 25512
> 65332
> 33549
> 35390
> ```
> - Looking up, its view is blocked at 2 trees (by another tree with a height of 5).
> - Looking left, its view is not blocked; it can see 2 trees.
> - Looking down, its view is also not blocked; it can see 1 tree.
> - Looking right, its view is blocked at 2 trees (by a massive tree of height 9).
>
> This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the tree house.
>
> Consider each tree on your map. What is the highest scenic score possible for any tree?

 Main trick here is to iterate the arrays in reverse to identify the nearest tree. Probably not doing a max but a traversal would be quicker, but this requires less code :)
```python
def _solve_part2(self: "DaySolution", parsed_data: AoCData) -> AoCData:
    max_score = 0
    rows, cols = parsed_data.shape
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            cur_height = parsed_data[row, col]
            left = parsed_data[row, :col][::-1] >= cur_height
            if left.any():
                left_trees = np.argmax(left) + 1
            else:
                left_trees = left.shape[0]
            right = parsed_data[row, col + 1 :] >= cur_height
            if right.any():
                right_trees = np.argmax(right) + 1
            else:
                right_trees = right.shape[0]
            up = parsed_data[:row, col][::-1] >= cur_height
            if up.any():
                up_trees = np.argmax(up) + 1
            else:
                up_trees = up.shape[0]
            down = parsed_data[row + 1 :, col] >= cur_height
            if down.any():
                down_trees = np.argmax(down) + 1
            else:
                down_trees = down.shape[0]
            cur_score = up_trees * down_trees * left_trees * right_trees
            if cur_score > max_score:
                max_score = cur_score
    return max_score
```

[Return to main page](../)
