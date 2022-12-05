---
layout: default
title: Day 5
description: Supply Stacks

---

## Day 5

[Return to main page](../)


The difficulty is slowly ramping up, although in this exercise it was mainly
the parsing that was a bit more challenging. Parts 1 and 2 were simply following
the instructions. Although I could imaging that this can be solved in a different
way with less code.


### Part 1
> The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.
>
> The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.
>
> The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.
>
> They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:
> ```
>     [D]
> [N] [C]
> [Z] [M] [P]
>  1   2   3
>
> move 1 from 2 to 1
> move 3 from 1 to 3
> move 2 from 2 to 1
> move 1 from 1 to 2
> ```
> In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.
>
> Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:
> ```
> [D]
> [N] [C]
> [Z] [M] [P]
>  1   2   3
> ```
> In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:
> ```
>         [Z]
>         [N]
>     [C] [D]
>     [M] [P]
>  1   2   3
> ```
> Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:
> ```
>         [Z]
>         [N]
> [M]     [D]
> [C]     [P]
>  1   2   3
> ```
> Finally, one crate is moved from stack 1 to stack 2:
> ```
>         [Z]
>         [N]
>         [D]
> [C] [M] [P]
>  1   2   3
> ```
> The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.
>
> After the rearrangement procedure completes, what crate ends up on top of each stack?


 First split the starting position from the instructions. Then parse the starting positions bottom to top to determine the number of stacks and then the crates per stack in the correct order. The instructions are always the same, so simply parsing the string and storing the relevant ints.
```python
def _parse_data(self: "DaySolution", input_data: str) -> AoCData:
    start_pos, instructions_string = input_data.split("\n\n")
    stacks_strings = start_pos.splitlines()
    nr_stacks = int(stacks_strings[-1][-2:])
    stacks = [[] for x in range(nr_stacks)]
    for i in range(len(stacks_strings) - 2, -1, -1):
        stacks_line = stacks_strings[i]
        for j in range(1, len(stacks_line), 4):
            if stacks_line[j] != " ":
                stacks[j // 4].append(stacks_line[j])
    instructions = []
    for instruction in instructions_string.splitlines():
        first = int(instruction.split("move")[1].split("from")[0])
        second = int(instruction.split("from")[1].split("to")[0])
        third = int(instruction.split("to")[1])
        instructions.append([first, second, third])
    return stacks, instructions
```

 Pretty straightforwar, loop over the instructions then do x times a pop of stack y and add it to stack z. Then read the top crates from all stacks that are not empty.
```python
def _solve_part1(self: "DaySolution", parsed_data: AoCData) -> AoCData:
    stacks, instructions = parsed_data
    for instruction in instructions:
        for _ in range(instruction[0]):
            crate = stacks[instruction[1] - 1].pop()
            stacks[instruction[2] - 1].append(crate)
    top_crates = "".join([stack[-1] for stack in stacks if stack[-1]])
    return top_crates
```

### Part 2

> As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.
>
> Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.
>
> The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.
>
> Again considering the example above, the crates begin in the same configuration:
> ```
>     [D]
> [N] [C]
> [Z] [M] [P]
>  1   2   3
> ```
> Moving a single crate from stack 2 to stack 1 behaves the same as before:
> ```
> [D]
> [N] [C]
> [Z] [M] [P]
>  1   2   3
> ```
> However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:
> ```
>         [D]
>         [N]
>     [C] [Z]
>     [M] [P]
>  1   2   3
> ```
> Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:
> ```
>         [D]
>         [N]
> [C]     [Z]
> [M]     [P]
>  1   2   3
> ```
> Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:
> ```
>         [D]
>         [N]
>         [Z]
> [M] [C] [P]
>  1   2   3
> ```
> In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.
>
> Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?

 Very similar, but store the popped crates in a list and add that list in its entirety to keep the order of the popped crates.
```python
def _solve_part2(self: "DaySolution", parsed_data: AoCData) -> AoCData:
    stacks, instructions = parsed_data
    for instruction in instructions:
        crates = []
        for _ in range(instruction[0]):
            if stacks[instruction[1] - 1]:
                crates.insert(0, stacks[instruction[1] - 1].pop())
        stacks[instruction[2] - 1].extend(crates)
    top_crates = "".join([stack[-1] for stack in stacks if stack[-1]])
    return top_crates
```

[Return to main page](../)
