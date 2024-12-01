package array.temporal_classmonitor;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		// 입력 받기
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[][] arr = new int[N][5];

		for (int i=0; i<N; i ++) {
			String[] a = br.readLine().split(" ");
			for (int j=0; j<5; j++){
				arr[i][j] = Integer.parseInt(a[j]);
			}
		}

		// 솔루션
	}
}
