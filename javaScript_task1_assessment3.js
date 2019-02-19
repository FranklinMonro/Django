var firstName = prompt("What is your first name?");
var lastName = prompt("What is your last name?");
var age = prompt("What is your age?");
var height = prompt("What is your height in cm?");
var petName = prompt("What is your pets name?");

if(firstName[0] == lastName[0] && age > 20 && age < 30 && height >= 170 && petName[petName.length-1] == "y" ){
  console.log("Welcome Comrade! You've passed the Spy Test")
}else{
  console.console.log("There is nothing to see here");
}
