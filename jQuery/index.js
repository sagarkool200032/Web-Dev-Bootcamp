var p1 = prompt("Player 1: Enter your name , you will be Blue");
var p1Clr = "rgb(66, 72, 245)";
var p2 = prompt("Player 2: Enter your name , you will be Red");
var p2Clr = "rgb(214, 21, 21)";

var table = $("table tr")
console.log(table);

function reportWin(colN,rowN)
{
  console.log("You Won in this Column and Row");
  console.log(colN);
  console.log(rowN);
}

function changeClr(rIndex,cIndex,color)
{
  var cell = table.eq(rIndex).find("td");
  var button = cell.eq(cIndex).fing("btn").css("background-color",color);
  return button;
}

function reportClr(rIndex,cIndex)
{
  var cell = table.eq(rIndex).find("td");
  var button = cell.eq(cIndex).fing("btn").css("background-color");
  return button;
}
