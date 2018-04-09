/*
 * Programming Quiz: Laugh (5-4)
 */

var laugh = function(times){
  var risos = "";
  for(var i = 0; i < times; i++){
    risos += "ha";
  }
  risos += "!";
  return risos;
}

console.log(laugh(10));
