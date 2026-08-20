package aula1;

import java.util.ArrayList;
import java.util.Scanner;

public class aula1 {
    static ArrayList<String> lista = new ArrayList<>();
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        for (int i = 0; i < 3; i++) {
            System.out.print("Digite o nome do aluno: ");
            String nome = sc.nextLine();
            lista.add(nome);
        }

        showList();
    }

    static public void showList() {
        System.out.println("----mostando lista----");

        for (String nomeString : lista) {
            System.out.println(nomeString);
        }
    }
}