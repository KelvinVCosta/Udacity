/*
Escreva um loop while que:

Faça um loop dos números 1 a 20
Se o número for divisível por 3, exiba "Julia"
Se o número for divisível por 5, exiba "James"
Se o número for divisível por 3 e 5, exiba "JuliaJames"
Se o número não for divisível por 3 nem 5, exiba o número
*/

/*
 * Programming Quiz: JuliaJames (4-1)
 */

var x = 1;
var result = "";

while (x < 21) {
    result = (x % 3 === 0 && x % 5 === 0) ? "JuliaJames" : (x % 3 === 0) ? "Julia" : (x % 5 === 0) ? "James" : x;
    console.log(result);
    x++;
}
