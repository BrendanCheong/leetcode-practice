function canFinish(numCourses: number, prerequisites: number[][]): boolean {

    // Create and populate adjacency list
    const graph = new Map<number, number[]>();
    for (let i = 0; i < numCourses; i++) {
        graph.set(i, new Array());
    }

    for (const [courseStart, courseEnd] of prerequisites) {
        graph.get(courseStart)?.push(courseEnd);
    }

    const visited = new Set<number>();

    function dfs(course: number): boolean {
        // base case
        if (visited.has(course)) {
            return false;
        }

        if (graph.get(course)?.length === 0) {
            return true;
        }

        visited.add(course);
        // Go through all directions
        for (const crs of graph.get(course) || []) {
            // Early termination
            if (!dfs(crs)) {
                return false;
            }
        }
        visited.delete(course);
        graph.set(course, new Array());

        // default exit statement
        return true;
    }

    for (let crs = 0; crs < numCourses; crs++) {
        if (!dfs(crs)) {
            return false;
        }
    }
    return true;
};
