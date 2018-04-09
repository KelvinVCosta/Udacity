/*
Orbiter transfers from ground to internal power (T-50 seconds)
Ground launch sequencer is go for auto sequence start (T-31 seconds)
Activate launch pad sound suppression system (T-16 seconds)
Activate main engine hydrogen burnoff system (T-10 seconds)
Main engine start (T-6 seconds)
Solid rocket booster ignition and liftoff! (T-0 seconds)
*/

/*
 * Programming Quiz: Countdown, Liftoff! (4-3)
 *
 * Using a while loop, print out the countdown output above.
 */

// your code goes here
var count = 60;
var message, task;
while(count > -1){
  message = "T-" + count + " seconds";
  switch (count) {
    case 50:
      task = "Orbiter transfers from ground to internal power";
      message = task;
      break;
    case 31:
      task = "Ground launch sequencer is go for auto sequence start";
      message =  task;
      break;
    case 16:
      task = "Activate launch pad sound suppression system";
      message = task;
      break;
    case 10:
      task = "Activate main engine hydrogen burnoff system";
      message = task;
      break;
    case 6:
      task = "Main engine start";
      message = task;
      break;
    case 0:
      message = "Solid rocket booster ignition and liftoff!";
      break;
  }
  console.log(message);
  count--;
}
