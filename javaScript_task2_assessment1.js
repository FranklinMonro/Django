//create array to store names in
var nameArray = []

//create add function
function add(name){
  nameArray.push(name)
}
//create remove function
function remove(name){
  var index = nameArray.indexOf(name)
  nameArray.splice(index,1)
}
//create display function
function display(){
  console.log(nameArray);
}
//create prompt to start if statement
var startApp = prompt("Do you want to start the app (y/n)?")
//create variable to store action in
var action = "empty"
//create variable to store name in
var name = "empty"
//if statement
if(startApp == "y"){
  while(action!== "quit"){
   action = prompt("Please select a action: add, remove, display or quit")
  if(action == "add"){
    name = prompt("Please enter a name you want to add")
    add(name)
  }else if (action == "remove") {
    name = prompt("Pleae eneter a name you want to remove")
    remove(name)
  }else if(action == "display"){
    display()
  }
}
alert("Good Bye")
}
