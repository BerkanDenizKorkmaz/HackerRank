import java.io.*;

class Result {

    /*
     * Complete the 'staircase' function below.
     *
     * The function accepts INTEGER n as parameter.
     */

    public static void staircase(int n) {
        String[] arr = new String[n];
        for (int i = 0; i < n; i++) {
            arr[i] = " ";
        } 
        for (int i = 0; i < n; i++) {
            arr[n-1-i] = "#";
            for(String chr : arr) {
                System.out.print(chr);
            }
            System.out.println("");
        }
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        Result.staircase(n);

        bufferedReader.close();
    }
}
