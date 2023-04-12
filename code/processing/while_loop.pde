float x = 0;

void setup(){
size(400, 300);
}

void draw(){

   // repeats this code a bunch of times
  x = 0;
  while(x < width){
// increamented over and over again, 
    x = x + 20;
//place inside while loop
    fill(101);
    stroke(255);
    ellipse(x, 150, 16, 160);
  }
  
// must have an exit condition!
 
  

  
}
