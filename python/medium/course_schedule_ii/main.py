from collections import defaultdict, deque


def findOrder(numCourses, prerequisites):
    # Step 1: Build the graph and count prerequisites for each course
    graph = defaultdict(list)         # graph[b] = list of courses that depend on b
    prereq_count = [0] * numCourses   # prereq_count[a] = number of courses that must be done before a

    for a, b in prerequisites:
        graph[b].append(a)            # b → a means: once b is done, a can be unlocked
        prereq_count[a] += 1          # a has one more prerequisite

    # Step 2: Initialize queue with courses that have no prerequisites
    queue = deque([i for i in range(numCourses) if prereq_count[i] == 0])
    order = []                        # this will store the final valid course order

    # Step 3: Process courses in BFS order
    while queue:
        course = queue.popleft()      # take a ready-to-run course
        order.append(course)          # add it to the result

        # Step 4: Unlock dependent courses
        for dependent in graph[course]:
            prereq_count[dependent] -= 1  # one prerequisite is now done
            if prereq_count[dependent] == 0:
                queue.append(dependent)   # course is now ready to run

    # Step 5: Check if all courses were scheduled
    if len(order) == numCourses:
        return order                   # success: return valid order
    else:
        return []                      # failure: cycle detected


# TEST CODE
numCourses = 4
prerequisites = [(2, 0), (2, 1)]
print(findOrder(numCourses, prerequisites))  # Example: [0,1,2,3] or similar

numCourses = 3
prerequisites = [(0, 1), (1, 2), (2, 0)]
print(findOrder(numCourses, prerequisites))  # Example: [] (cycle detected)
