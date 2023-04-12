// creating and working with pixels


void setup(){

  size(510, 510);
}

void draw(){

 
loadPixels();

//for(int i = 0; i < pixels.length; i++){
//pixels[i] = color(i, 0, 0);
//}


  int t = millis();  // current time in milliseconds
  println(t);

//for every single x, go though every y etc...
// can cover every single 
// basis behind every single processing algo
for (int x = 0; x < width; x++){
  for (int y = 0; y < height; y++){
    int loc = x + y * width;
    
// spectural
//float d = dist(x, y, width/2, height/2);
    
    
 // The map() function is useful to convert directly from one range of numbers to another. It has five parameters.
  // map(value, low1, high1, low2, high2)
     // compute color based on position and time
  
      float hue = map(x + y + t/10.0, 0, width + height, 0, 255);
      float sat = map(x, 0, width, 0, 255);
      float bri = map(y, 0, height, 0, 255);
      pixels[loc] = color(hue, sat, bri);
      
      
      
      
    
    //pixels[loc] = color(0, y/2, x/2);
    //pixels[loc] = color(0, y+2, x+2);
    //gradient
    //pixels[x + y * width] = color(0, y/2, x/2);
  }
}



updatePixels();

}
