package uniesp.javascript.aula3;

import java.util.Scanner;

public class Tarefa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        float tempo,distancia;
        String continuar;
        do{
            System.out.print("Distancia do atleta: ");
            distancia = sc.nextFloat();
            System.out.print("Qual o tempo: ");
            tempo = sc.nextFloat();
            double resultado = velocidadeMedia(distancia, tempo);
            System.out.println("a velocidade media e " + resultado);
            sc.nextLine();
            System.out.print("deseja encerra? sim ou nao: ");
            continuar = sc.nextLine();
            

        }while (continuar.equals("sim"));
    }
    private static double velocidadeMedia(float distancia,float tempo){
        return distancia / tempo;
    }
}
