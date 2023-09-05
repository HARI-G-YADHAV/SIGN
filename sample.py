from collections import Counter
import heapq

def arrange_items_2d(items, num_rows, num_columns):
    category_count = Counter(items)
    max_heap = [(-count, category) for category, count in category_count.items()]
    heapq.heapify(max_heap)
    
    matrix = [[None] * num_columns for _ in range(num_rows)]
    
    while max_heap:
        neg_count, category = heapq.heappop(max_heap)
        count = -neg_count
        
        for row in range(num_rows):
            for col in range(num_columns):
                if matrix[row][col] is None:
                    valid_placement = True
                    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        r, c = row + dr, col + dc
                        if 0 <= r < num_rows and 0 <= c < num_columns and matrix[r][c] == category:
                            valid_placement = False
                            break
                    if valid_placement:
                        matrix[row][col] = category
                        count -= 1
                        if count == 0:
                            break
        
        if count > 0:
            heapq.heappush(max_heap, (-count, category))
    
    return matrix

# Example usage:
items = [1, 1, 2, 2, 3, 3]
num_rows = 3
num_columns = 2
arranged_matrix = arrange_items_2d(items, num_rows, num_columns)
for row in arranged_matrix:
    print(row)
