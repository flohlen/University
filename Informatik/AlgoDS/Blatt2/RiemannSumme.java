import java.util.*;

class RiemannSumme{
	public static void main(String[]args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.print("Bitte geben Sie den Grad ihres Polynoms an: ");
		int k = sc.nextInt();
		
		int a[] = new int[k+1];
		
		for (int i = k; i >= 0; i--) {
			System.out.print("\nBitte geben Sie den a wert der hoch " + i + " Potenz an: ");
			a[i] = sc.nextInt();
		}
		
		System.out.print("\nBitte geben Sie den wert der unteren Schranke des Integrals ein: ");
		int c = sc.nextInt();
		
		System.out.print("\nBitte geben Sie den wert der oberen Schranke des Integrals ein: ");
		int d = sc.nextInt();

		/* TEST
		int k = 2;
		int a[] = new int[k+1];
		a[2] = -1;
		a[1] = 0;
		a[0] = 4;
		int c = 0;
		int d = 2;
		*/

		System.out.print("\nDer Integralwert des Polynoms ist: " + berechneIntegral(a, c, d, k) + "\n");
	}

	static double berechneIntegral(int[] a, int c, int d, double n){

		double summe = 0;
		double summeAlt, deltaX;
		
		do {
			
			summeAlt = summe;
			summe = 0;
			deltaX = (d-c)/n;

			for (int i = 0; i <= n; i++) {
				summe += berechneF(a, c + i * deltaX) * deltaX;
			}

			n *= 2;
		
		} while (Math.abs(summe - summeAlt) > 0.01);

		return Math.round(summe * 10) / 10.0;
	}

	static double berechneF(int a[], double t){
		
		double x = a[0];		
		
		for (int i = 1; i < a.length; i++) {
			x += a[i] * t;
			t *= t;
		}

		return Math.abs(x);
	}

}