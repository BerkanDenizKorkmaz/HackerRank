import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'miniMaxSum' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static void miniMaxSum(List<Integer> arr) {
        long min = Long.MAX_VALUE;
        long max = Long.MIN_VALUE;
        long sum = 0;

        for(int i = 0; i < arr.size(); i++) {
            long selected = arr.get(i);
            if (selected > max) { max = selected; }
            if (selected < min) { min = selected; }
            sum += selected;
        }
        
        System.out.printf("%d %d", sum-max, sum-min);
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        Result.miniMaxSum(arr);

        bufferedReader.close();
    }
}
