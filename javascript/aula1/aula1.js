function setNome(){
    nome = document.getElementById("nome")
    console.log(nome.value)
    elemento = document.createElement('h1')
    elemento.textContent = nome.value
    document.body.appendChild(elemento)
}

function setDia() {
    dia = document.getElementById('dia').value
    console.log(dia)
    elemento = document.createElement('table')
    linha = document.createElement('tr')
    elemento.appendChild(linha)
    celula = document.createElement('td')
    celula.textContent = dia
    linha.appendChild(celula)
    document.body.appendChild(elemento)
}