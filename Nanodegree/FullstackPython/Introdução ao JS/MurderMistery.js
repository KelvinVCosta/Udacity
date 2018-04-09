/*
 * Programming Quiz: Murder Mystery (3-4)
*/

// change the value of `room` and `suspect` to test your code
var room = "billiards room";
var suspect = "Mrs. Sparr";

var weapon = "";
var solved = false;

if (room === "ballroom") {
    weapon = "poison";
} else if (room === "gallery") {
    weapon = "trophy";
} else if (room === "billiards room") {
    weapon = "pool stick";
} else {
    weapon = "knife";
}

if ((suspect == "Mr. Parkes" && room == "dining room") ||
    (suspect == "Ms. Van Cleve" && room == "gallery") ||
    (suspect == "Mrs. Sparr" && room == "billiards room") ||
    (suspect == "Mr. Kalehoff" && room == "ballroom")){
    solved = true;
    }

if (solved) {
  var message = suspect + " did it in the " + room + " with the " + weapon +"!";
	console.log(message);
}
