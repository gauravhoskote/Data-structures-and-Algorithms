class KDTreeNode:
    def __init__(self, point, index, left=None, right=None):
        self.point = point  # The point stored in this node
        self.index = index  # Index of the point in the original list
        self.left = left    # Left child
        self.right = right  # Right child

class KDTree:
    def __init__(self, points, distance_type):
        self.distance_type = distance_type
        self.points = points
        self.root = self.build_kdtree(points, list(range(len(points))), depth=0)

    def build_kdtree(self, points, indices, depth):
        if not indices:
            return None

        k = len(points[0])
        axis = depth % k

        indices.sort(key=lambda i: points[i][axis])
        median = len(indices) // 2

        # Create node and construct subtrees
        return KDTreeNode(
            point=points[indices[median]],
            index=indices[median],
            left=self.build_kdtree(points, indices[:median], depth + 1),
            right=self.build_kdtree(points, indices[median + 1:], depth + 1)
        )

    def nearest_neighbor(self, point, depth=0, best=None):
        if self.root is None:
            return None

        k = len(point)
        axis = depth % k

        if best is None or self.distance(point, best.point, self.distance_type) > self.distance(point, self.root.point, self.distance_type):
            best = self.root

        next_branch = self.root.left if point[axis] < self.root.point[axis] else self.root.right
        opposite_branch = self.root.right if point[axis] < self.root.point[axis] else self.root.left

        if next_branch:
            best = self.nearest_neighbor(point, depth + 1, best)

        if opposite_branch:
            if abs(point[axis] - self.root.point[axis]) < self.distance(point, best.point, self.distance_type):
                best = self.nearest_neighbor(point, depth + 1, best)

        return best

    def query_ball_point(self, point, radius):
        indices_within_radius = []
        self._query_ball_point(self.root, point, radius, indices_within_radius, depth=0)
        return indices_within_radius

    def _query_ball_point(self, node, point, radius, indices, depth):
        if node is None:
            return

        # Calculate the distance from the point to the current node
        if self.distance(point, node.point, self.distance_type) <= radius:
            indices.append(node.index)

        # Check which side of the tree to explore
        k = len(point)
        axis = depth % k

        # Determine whether to search the left or right subtree
        if point[axis] - radius < node.point[axis]:
            self._query_ball_point(node.left, point, radius, indices, depth + 1)
        if point[axis] + radius >= node.point[axis]:
            self._query_ball_point(node.right, point, radius, indices, depth + 1)

    @staticmethod
    def distance(point1, point2, type):
        if type == 'cosine':
            return sum((p1 * p2) for p1, p2 in zip(point1, point2)) / (sum((p1 ** 2) for p1 in point1) * sum((p2 ** 2) for p2 in point2))
        return sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)) ** 0.5


# Example usage:
points = [[7, 2], [5, 4], [9, 6], [2, 3], [4, 7], [8, 1]]
kdtree = KDTree(points)

# Query points within a radius from a given point
query_point = [5, 5]
radius = 3
indices_within_radius = kdtree.query_ball_point(query_point, radius)

print(f"Indices of points within radius {radius} of {query_point}: {indices_within_radius}")
