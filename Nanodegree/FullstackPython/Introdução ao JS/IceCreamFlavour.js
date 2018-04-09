// se flavor é definido como vanilla ou chocolate e
// se vessel é definido como cone ou bowl e
// se toppings é definido como sprinkles ou peanuts

/*
 * Programming Quiz: Ice Cream (3-6)
 *
 * Write a single if statement that logs out the message:
 *
 * "I'd like two scoops of __________ ice cream in a __________ with __________."
 *
 * ...only if:
 *   - flavor is "vanilla" or "chocolate"
 *   - vessel is "cone" or "bowl"
 *   - toppings is "sprinkles" or "peanuts"
 *
 * We're only testing the if statement and your boolean operators.
 * It's okay if the output string doesn't match exactly.
 */

// change the values of `flavor`, `vessel`, and `toppings` to test your code
var flavor = "vanilla";
var vessel = "cone";
var toppings = "walnuts";

// Add your code here
if((flavor === "vanilla" || flavor === "chocolate") &&
(vessel === "cone" || vessel === "bowl") &&
(toppings === "sprinkles" || toppings === "peanuts")){
  var message = "I'd like two scoops of " + flavor +
    " ice cream in a " + vessel + " with " + toppings + ".";
  console.log(message);
}
