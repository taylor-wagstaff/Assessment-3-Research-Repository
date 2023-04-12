int[][] angles = {{ 0, 1 }, { 1, 1 }, { 1, 0 }, { 1,-1 },
                  { 0,-1 }, {-1,-1 }, {-1, 0 }, {-1, 1 }};
int numAngles = angles.length;
int x, y, nx, ny;
int dir = 0;
color black = color(0);
color white = color(255);
void setup() { 
  size(800, 800);
  background(255); 
  x = width/2;
  nx = x;
  y = height/2;
  ny = y;
  float woodDensity = width * height * 0.5;
  for (int i = 0; i < woodDensity; i++) {
    int rx = int(random(width));
    int ry = int(random(height));
    set(rx, ry, black);
} }
void draw() {
int rand = int(abs(random(-1, 2)));
  dir = (dir + rand + numAngles) % numAngles;
  nx = (nx + angles[dir][0] + width) % width;
  ny = (ny + angles[dir][1] + height) % height;
  if ((get(x,y) == black) && (get(nx,ny) == white)) {
    // Move the chip one space
    set(x, y, white);
    set(nx, ny, black);
    x = nx;
    y = ny;
    } else if ((get(x,y) == black) && (get(nx,ny) == black)) {
  // Move in the opposite direction
  dir = (dir + (numAngles/2)) % numAngles;
  x = (x + angles[dir][0] + width) % width;
  y = (y + angles[dir][1] + height) % height;
} else {
  // Not carrying
x = nx;
y = ny;
}
nx = x; // Save the current position ny = y;
}







//void setup(){
//background(120, 120, 120);
//size(600, 600);
//}




//void draw() {

//stroke(255, 60);
//for (int i = 0; i < 600; i++) {
  
//  if (i < 600){
  
//  float r = random(10);
//  strokeWeight(r);
//  float offset = r * 5.0;
//  line(i-20, 600, i+offset, 0);
  
//  } else { 
//   float r = random(10);
//  strokeWeight(r);
//  float offset = r * 5.0;
//  line(i, 600, i+offset, 0);
  
    

//}

//}


//}



// learning random path
//float blackX;
//float blackY;

//float whiteX;
//float whiteY;

//void setup() {
//  size(600, 600);
  
//  blackX = width*.25;
//  blackY = height/2;

//  whiteX = width*.75;
//  whiteY = height/2;

//  background(255);
  
//  frameRate(1000);
//}

//void draw() {

//  stroke(0);
  
//  blackX += random(-1, 1);
//  blackY += random(-1, 1);
    
//  if(blackX < 0){
//    blackX = width;
//  }
//  if(blackX > width){
//    blackX = 0;
//  }

//  if(blackY < 0){
//    blackY = height;
//  }
//  if(blackY > height){
//    blackY = 0;
//  }
  
//  point(blackX, blackY);

//  stroke(0);
//  strokeCap(PROJECT);
//  whiteX += random(-1, 1);
//  whiteY += random(-1, 1);
  
//  if(whiteX < 0){
//    whiteX = width;
//  }
//  if(whiteX > width){
//    whiteX = 0;
//  }
  
//  if(whiteY < 0){
//    whiteY = height;
//  }
//  if(whiteY > height){
//    whiteY = 0;
//  }  
  
//  point(whiteX, whiteY);
  
//}
