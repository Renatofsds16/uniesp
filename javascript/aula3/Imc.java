package uniesp.javascript.aula3;

import java.util.Scanner;

public class Imc {
    
    public static void main(String[] args) {
        double peso,altura;
        Scanner sc = new Scanner(System.in);
        String opc = "";

        while (true) {
            System.out.print("Digite seu peso: ");
            peso = sc.nextDouble();
            System.out.print("Digite sua altura: ");
            altura = sc.nextDouble();
            double resultado = calcularImc(peso, altura);
            System.out.println(resultado);
            System.out.println(faixa(resultado));
            System.out.print("Deseja sair? digite sair para encerrar: ");
            sc.nextLine();
            opc = sc.nextLine();
            System.out.println(opc);
            if (opc.equals("sair")) {
                break;
            }
        }
        
        

        
    }

    private static double calcularImc(double peso,double altura){
        return peso / (altura * altura);
    }

    private static String faixa(double resultado){
        if (resultado < 18.5) {
            return "Abaixo do peso";
        }else if (resultado >= 25.0 && resultado <= 29.9) {
            return "Sobre peso";
        }else if (resultado >= 30) {
            return "Obesidade";
        }
        return "Resultado invalido";
    }
}
