
var roster = []

function addElement(name) {
  roster.push(name)
}

function displayElement(){
    console.log(roster);
  }

function removeElement(name){
  var temp = roster.indexOf(name)
  roster.splice(temp,1)
}

x = false
var user = prompt("Start Web App y/n ?")
if(user==="y")
  x = true

while(x===true)
{
  var action = prompt("Select action add ,remove ,display ,quit")
  if(action==="add"){
    var name = prompt("Enter Name")
    addElement(name)}
  else if (action === "remove"){
    var name = prompt("Enter Name")
    removeElement(name)}
  else if(action === "display")
    displayElement()
  else
    x = false
}
