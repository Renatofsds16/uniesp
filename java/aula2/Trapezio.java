package aula2;

import java.util.Scanner;

public class Trapezio {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double baseMaior,baseMenor,altura,area;
        System.out.print("Qual a base maior? ");
        baseMaior = scanner.nextDouble();
        System.out.print("Qual a base menor? ");
        baseMenor = scanner.nextDouble();
        System.out.print("Qual a altura? ");
        altura = scanner.nextDouble();

        area = (baseMaior + baseMenor) / 2 *altura;
        System.out.println("area do trapezio e " + area);



        scanner.close();

    }
}
