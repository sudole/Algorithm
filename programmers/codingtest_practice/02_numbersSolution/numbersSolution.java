import java.util.Scanner;

public class numbersSolution {
	public static void main(String[] args) {
		int x = 1;
		int n = 1;
		try (Scanner scan = new Scanner(System.in)) {
			System.out.print("input x, n : ");
			x = scan.nextInt();
			n = scan.nextInt();
			
			long[] result = exec(x, n);
			
			
			print(result);
		}
	}
	
	private static long[] exec(int x, int n) {
		long[] answer = new long[n];
		for (int i=0; i < n; i++) {
			answer[i] = (long)x*(i+1);
		}
		return answer;
	}
	
	private static void print(long[] data) {
		for(int i=0; i<data.length; i++) {
			System.out.print(data[i]);
			System.out.print("");
		}
	}
}
