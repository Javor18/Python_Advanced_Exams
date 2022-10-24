from collections import deque

eggs_size = deque(int(x) for x in input().split(", "))
papers_size = deque(int(x) for x in input().split(", "))

boxes = 0

while eggs_size and papers_size:

    egg_size = eggs_size.popleft()
    paper_size = papers_size.pop()

    size = egg_size + paper_size

    if egg_size == 13:
        papers_size.append(paper_size)
        papers_size[0], papers_size[-1] = papers_size[-1], papers_size[0]
        continue

    elif egg_size <= 0:
        papers_size.append(paper_size)

    elif size <= 50:
        boxes += 1

if boxes > 0:

    print(f"Great! You filled {boxes} boxes.")

else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_size:

    print(f'Eggs left: {", ".join(str(x) for x in eggs_size)}')

if papers_size:

    print(f'Pieces of paper left: {", ".join(str(x) for x in papers_size)}')