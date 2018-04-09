/*
TAMANHOS:
size   width   lenght   sleeve
S       18      28       8.13
M       20      29       8.38
L       22      30       8.63
XL      24      31       8.88
2XL     26      32       9.63
3XL     28      33      10.13

TESTES:
Se shirtWidth é igual a 19, shirtLength é igual a 28 e shirtSleeve é igual a 8.21, então S deve ser impresso no console.
Se shirtWidth é igual a 26, shirtLength é igual a 33 e shirtSleeve é igual a 9.63, então 2XL deve ser impresso no console.
Se shirtWidth é igual a 18, shirtLength é igual a 29 e shirtSleeve é igual a 8.47, então N/A deve ser impresso no console.
*/

/*
 * Programming Quiz: What do I Wear? (3-7)
 */

// change the values of `shirtWidth`, `shirtLength`, and `shirtSleeve` to test your code
var shirtWidth = 18;
var shirtLength = 29;
var shirtSleeve = 8.47;
var size = "";
// your code goes here
//small = (shirtWidth>= 18 && shirtWidth < 20) && (shirtLength >= 28 && shirtLength < 29 ) && (shirtSleeve >= 8.13 && shirtSleeve < 8.38)
if ((shirtWidth >= 18 && shirtWidth < 20) && (shirtLength >= 28 && shirtLength < 29 ) && (shirtSleeve >= 8.13 && shirtSleeve < 8.38)){
  size = "S";
}
//medium = (shirtWidth>= 20 && shirtWidth < 22) && (shirtLength >= 29 && shirtLength < 30 ) && (shirtSleeve >= 8.38 && shirtSleeve < 8.63)
else if((shirtWidth>= 20 && shirtWidth < 22) && (shirtLength >= 29 && shirtLength < 30 ) && (shirtSleeve >= 8.38 && shirtSleeve < 8.63)){
  size = "M";
}
//large = (shirtWidth>= 22 && shirtWidth < 24) && (shirtLength >= 30 && shirtLength < 31 ) && (shirtSleeve >= 8.63 && shirtSleeve < 8.88)
else if((shirtWidth>= 22 && shirtWidth < 24) && (shirtLength >= 30 && shirtLength < 31 ) && (shirtSleeve >= 8.63 && shirtSleeve < 8.88)){
  size = "L";
}
//xLarge = (shirtWidth>= 24 && shirtWidth < 26) && (shirtLength >= 31 && shirtLength < 32 ) && (shirtSleeve >= 8.88 && shirtSleeve < 9.63)
else if((shirtWidth>= 24 && shirtWidth < 26) && (shirtLength >= 31 && shirtLength < 33 ) && (shirtSleeve >= 8.88 && shirtSleeve < 9.63)){
  size = "XL";
}
//x2Large = (shirtWidth>= 26 && shirtWidth < 28) && (shirtLength >= 32 && shirtLength < 33 ) && (shirtSleeve >= 9.63 && shirtSleeve < 10.13)
else if((shirtWidth>= 26 && shirtWidth < 28) && (shirtLength >= 33 && shirtLength < 34 ) && (shirtSleeve >= 9.63 && shirtSleeve < 10.13)){
  size = "2XL";
}
//x3Large = (shirtWidth>= 28) && (shirtLength >= 33 ) && (shirtSleeve >= 10.13)
else if((shirtWidth>= 28) && (shirtLength >= 34 ) && (shirtSleeve >= 10.13)){
  size = "3XL";
}else{
  size = "N/A";
}
console.log(size);
