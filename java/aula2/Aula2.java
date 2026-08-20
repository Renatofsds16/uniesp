package aula2;
import java.util.Scanner;

public class Aula2 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        float nota1,nota2,nota3,media;
        System.out.print("Digite a 1 nota: ");
        nota1 = scanner.nextFloat();
        System.out.print("Digite a 2 nota: ");
        nota2 = scanner.nextFloat();
        System.out.print("Digite a 3 nota: ");
        nota3 = scanner.nextFloat();

        media = (nota1 + nota2 + nota3) / 3;
        System.out.println("A media e " + media);
        scanner.close();
        
    }
}
