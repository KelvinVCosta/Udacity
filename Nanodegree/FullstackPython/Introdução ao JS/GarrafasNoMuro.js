/*
 * Programming Quiz: 99 Bottles of Juice (4-2)
 *
 * Use the following `while` loop to write out the song "99 bottles of juice".
 * Log the your lyrics to the console.
 *
 * Note
 *   - Each line of the lyrics needs to be logged to the same line.
 *   - The pluralization of the word "bottle" changes from "2 bottles" to "1 bottle" to "0 bottles".
 */

 var num = 99;
 var word, message, phrase;

 while (num > 0) {
     // 99 bottles of juice on the wall! 99 bottles of juice!
     //Take one down, pass it around... 98 bottles of juice on the wall!
     word = num === 1 ? " bottle of juice" : " bottles of juice";
     phrase = num + word;
     message = phrase + " on the wall!";
     message += " " + phrase + "! Take one down, pass it around... ";
     num--;
     word = num === 1 ? " bottle of juice" : " bottles of juice";
     phrase = num + word;
     message += phrase + " on the wall!";
     console.log(message);
 }
