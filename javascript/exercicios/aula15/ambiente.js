let num = [5, 8, 2, 9, 3]
num.push(1) //Adiciona o número 1 no final do vetor
num.sort() //Organiza o vetor

/*
num[3] = 6 //Adicona o número 6 na posição 3
num.length //Mostra o tamanho do vetor
*/

console.log(num)
console.log(`O vetor tem ${num.length} posições`)
console.log(`O primeiro valor do vetor é ${num[0]}`)
let pos = num.indexOf(4) //Se não tiver o número no vetor, irá retornar -1

if (pos == -1) { //Posso fazer essa validação para mostrar uma mensagem personalizada
    console.log('O valor não foi encontrado')    
} else {
    console.log(`O valor 8 está na posição ${pos}`)
}
