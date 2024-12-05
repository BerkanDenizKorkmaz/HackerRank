import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'plusMinus' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static void plusMinus(List<Integer> arr) {
        int length = arr.size();
        
        double positiveCount = 0;
        double negaativeCount = 0;
        double zeroCount = 0;
        
        for (int i = 0; i< length; i++) {
            if (arr.get(i) > 0) {
                positiveCount += 1;
            }
            
            else if (arr.get(i) < 0) {
                negaativeCount += 1;
            }
            
            else {
                zeroCount += 1;
            }
        }
        System.out.printf("%.6f\n", positiveCount/length);
        System.out.printf("%.6f\n", negaativeCount/length);
        System.out.printf("%.6f", zeroCount/length);
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        Result.plusMinus(arr);

        bufferedReader.close();
    }
}
