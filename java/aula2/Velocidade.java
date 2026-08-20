package aula2;

import java.util.Scanner;

public class Velocidade {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int tempo,distancia,velocidadeMedia;
        System.out.print("Qual o tempo? ");
        tempo = scanner.nextInt();
        System.out.print("Qual a distancia? ");
        distancia = scanner.nextInt();
        velocidadeMedia = distancia/tempo;
        System.out.println("velocidade media e " + velocidadeMedia);
        scanner.close();
    }
}
