/*
Find Nearest Point That Has the Same X or Y Coordinate
Easy
684
140
Companies

You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y). You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi). A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.

Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location. If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.

The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).

 

Example 1:

Input: x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
Output: 2
Explanation: Of all the points, only [3,1], [2,4] and [4,4] are valid. Of the valid points, [2,4] and [4,4] have the smallest Manhattan distance from your current location, with a distance of 1. [2,4] has the smallest index, so return 2.

Example 2:

Input: x = 3, y = 4, points = [[3,4]]
Output: 0
Explanation: The answer is allowed to be on the same location as your current location.

Example 3:

Input: x = 3, y = 4, points = [[2,3]]
Output: -1
Explanation: There are no valid points.

 

Constraints:

    1 <= points.length <= 104
    points[i].length == 2
    1 <= x, y, ai, bi <= 104


*/

/**
 * @param {number} x
 * @param {number} y
 * @param {number[][]} points
 * @return {number}
 */
var nearestValidPoint = function (x, y, points) {
    let min = Infinity;
    for (let i = 0; i < points.length; i++) {
        if (x == points[i][0] || y == points[i][1]) {
            let manhattan_distance = Math.abs(x - points[i][0]) + Math.abs(y - points[i][1]);
            if (manhattan_distance < min) min = manhattan_distance;
            points[i].push(manhattan_distance);
        }
    }
    // console.log(points);
    for (let i = 0; i < points.length; i++) {
        if ((points[i][2] || points[i][2] == 0) && min == points[i][2]) return i;
    }
    return -1;
};

