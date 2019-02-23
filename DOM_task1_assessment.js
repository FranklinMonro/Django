//store button in variable
var restart = document.querySelector('#restart');
//store all tables in variable
var squares = document.querySelectorAll('td');


//create function to clear all the squares
function clearAll(){
  for(var i = 0; i < squares.length; i++ ){
    squares[i].textContent = " ";
  }
}


//create event listner to clear all squares when pressing button
restart.addEventListener('click',clearAll)

//create function to change square
function changeBoard(){
  if(this.textContent === ''){
    this.textContent = 'X';
  }else if (this.textContent === 'X') {
    this.textContent = 'O';
  }else {
    this.textContent = '';
  }
}


//create event listener to change square
for(var i = 0; i < squares.length; i++){
  squares[i].addEventListener('click', changeBoard);
}
