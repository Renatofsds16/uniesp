//O aluno deve desenvolver um pequeno programa em JavaScript que recebe dados de um aluno e determina sua situação acadêmica.

//O programa deverá:

//- Criar uma variável para armazenar o nome do aluno.
//- Criar duas variáveis para armazenar as notas da primeira e segunda avaliação.
//- Calcular a média das duas notas.
//- Utilizar uma constante para armazenar a média mínima para a aprovação, que será 7.
//- Utilizar if, else if e else para determinar a situação: média maior ou igual a 7, aluno APROVADO; média maior ou igual a 5 e menor que 7, RECUPERAÇÃO; média menor que 5, REPROVADO.
//- Se o aluno estiver em recuperação, o programa deve solicitar a nota da recuperação, e caso seja menor que 5 o aluno está REPROVADO, caso contrário, o aluno está APROVADO.
//- Exiba no console os seguintes dados: Nome do aluno, Nota 1, Nota 2, Média, Nota de Recuperação (se tiver) e Situação do Aluno.

console.log("programa em js");
alert("programa executado...");
const MEDIAMINIMA = 7;
const nome = prompt('seu nome: ');
const nota1 = parseFloat(prompt('seu nota1: '));
const nota2 = parseFloat(prompt('seu nota2: '));
const media = (nota1 + nota2) / 2;
let situacao = '';
let notaRecuperacao = 0;
if (media >= MEDIAMINIMA){
    situacao = 'Aprovado';
}else if (media >= 5 && media < 7){
    situacao = "recuperacao"
    notaRecuperacao = parseFloat(prompt("digite a nota da recuperaçao: ")) || "";
    if(notaRecuperacao < 5){
    situacao = 'reprovado';
    }else{
        situacao = 'Aprovado';
    }
}else{
    situacao = 'reprovado';
}



console.log(`nome: ${nome} nota1: ${nota1} nota2: ${nota2} media: ${media} nota recuperacao: ${notaRecuperacao} situaçao: ${situacao}`)



