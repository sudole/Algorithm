import java.io.IOException;
import java.util.Scanner;

public class printSqureStar {
	public static void main(String[] args) {
		int w = 1;
		int h = 1;
		Scanner scan = new Scanner(System.in);
		
		System.out.print("Width > ");
		w = scan.nextInt();
		
		scan.nextLine();
		
		System.out.print("Height > ");
		h = scan.nextInt();
		
		printsquare(w, h);
		
		
	}
	
	private static void printsquare(int a, int b) {
		for(int i=0; i < b; i++) {
			for(int j=0; j < a; j++) {
				System.out.print('*');
			}
			System.out.println("");
		}
		
	}
}
