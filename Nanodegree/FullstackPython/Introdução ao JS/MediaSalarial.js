/*
no high school diploma (sem diploma de nível médio) ganharam uma média de US$ 25.636/ano,
a high school diploma (com nível médio completo) ganharam uma média de US$ 35.256/ano,
an Associate's degree (com diploma de curso técnico) ganharam uma média de US$ 41.496/ano,
a Bachelor's degree (com superior completo) ganharam uma média de US$ 59.124/ano,
a Master's degree (com mestrado completo) ganharam uma média de US$ 69.732/ano,
a Professional degree (com diploma profissional) ganharam uma média de US$ 89.960/ano,
e a Doctoral degree (com doutorado completo) ganharam uma média de US$ 84.396/ano.
*/

/*
 * Programming Quiz: Back to School (3-9)
 */

// change the value of `education` to test your code
var education = "an Associate's degree";

// set the value of this based on a person's education
var salary;

// your code goes here
switch(education){
    case "no high school diploma": salary = 25636; break;
    case "a high school diploma": salary = 35256; break;
    case "an Associate's degree": salary = 41496; break;
    case "a Bachelor's degree": salary = 59124; break;
    case "a Master's degree": salary = 69732; break;
    case "a Professional degree": salary = 89960; break;
    case "a Doctoral degree": salary = 84396; break;
}

var message = "In 2015, a person with " + education + " earned an average of $" + salary.toLocaleString("en-US") + "/year.";
console.log(message);
