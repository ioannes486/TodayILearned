package candy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {

    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for(int A=0; A<=(N+1); A++){
            for(int B=0; B<=(N+1); B++){
                for(int C=0; C<=(N+1); C++){
                    if(A + B + C == N){
                        if(A==B+2){
                            if(A!=0 & B!=0 & C!=0){
                                if(C%2 == 0){
                                    answer ++;
                                }
                            }

                        }
                    }
                }
            }
        }

        System.out.println(answer);

    }
}
