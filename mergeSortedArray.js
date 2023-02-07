/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function (nums1, m, nums2, n) {
    let result = [];
    let i = 0, j = 0;
    while (i < m && j < n) {
        if (nums1[i] < nums2[j])
            result.push(nums1[i++]);
        else
            result.push(nums2[j++]);
    }

    while (i < m)
        result.push(nums1[i++]);
    while (j < n)
        result.push(nums2[j++]);

    return result;
};

console.log(merge([1,2,3,0,0,0], 3, [2,5,6], 3))