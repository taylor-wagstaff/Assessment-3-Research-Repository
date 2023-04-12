float x = 0;
float y = 0;
float spacing = 50;

void setup(){
size(1000, 800);
}

void draw(){
 //background(0);



////insitalisation condition
//x = 0;
////boolean expression, check if true, 
//while (x < width){
//line(x, 0, x, height);
////increamentation oporation
//x = x + 20;
//} 

//y = 0;
//while (y < height){
//line(0, y, width, y);
//y = y + 20;
//} 


// becomes this is a for loop for a grid. 


// nested loops. 
// for every row, 
  // for every col
   // draw all the rectangles. 

for (int y = 0; y < width; y = y + 20){
  for (int x = 0; x < width; x = x + 20){
     
// random colours. 
//fill(random(255), random(255), random(255));

    rect(x, y, height / 20, width / 20);
    
}


}


 
  

  
}
