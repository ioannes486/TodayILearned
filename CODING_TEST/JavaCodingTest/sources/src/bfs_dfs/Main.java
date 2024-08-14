package bfs_dfs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;


public class Main {
  static int fibo[];
  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    fibo = new int[N+1];
    System.out.println(recurr(N));
    System.out.println(Arrays.toString(fibo));


  }
  static int recurr(int N){
    if (fibo[N]>0) return fibo[N];
    if (N==1) return fibo[N]= 1;
    else if (N==2) return fibo[N] = 1;

    else return fibo[N] = recurr(N-1) + recurr(N-2);

  }
}
