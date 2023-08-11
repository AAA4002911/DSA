import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * Problem Statement
 * Detailed explanation ( Input/output format, Notes, Images )
 * Sample Input 1:
 * 
 * 7 3
 * 1 2 3 1 1 1 1
 * 
 * Sample Output 1 :
 * 
 * 3
 * 
 * Explanation Of Sample Input 1:
 * 
 * Input: ‘N’ = 7 ‘K’ = 3
 * ‘A’ = [1, 2, 3, 1, 1, 1, 1]
 * 
 * Output: 3
 * 
 * Explanation: Subarrays whose sum = ‘3’ are:
 * [1, 2], [3], [1, 1, 1], [1, 1, 1]
 * Here, the length of the longest subarray is 3, which is our final answer.
 * 
 * Sample Input 2:
 * 
 * 4 2
 * 1 2 1 3
 * 
 * Sample Output 2:
 * 
 * 1
 * 
 * Sample Input 3:
 * 
 * 5 2
 * 2 2 4 1 2
 * 
 * Sample Output 3:
 * 
 * 1
 * 
 * 
 */

public class LongestSubArrWIthSumK {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stt = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(stt.nextToken());
        long k = Long.parseLong(stt.nextToken());
        String[] inputLine = br.readLine().trim().split(" ");
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(inputLine[i]);
        }
        int result = longestSubarrayWithSumK(arr, k);
        System.out.println(result);
    }

    public static int longestSubarrayWithSumK(int[] a, long k) {
        // Write your code here
        int n = a.length;
        int j = 0, i = 0;
        long sum = a[0];
        int result = 0;

        while (i < n) {
            while (j <= i && sum > k) {
                sum -= a[j];
                j++;
            }

            if (sum == k) {
                result = Math.max(result, i - j + 1);
            }

            i++;
            if (i < n) {
                sum += a[i];
            }
        }
        return result;
    }
}