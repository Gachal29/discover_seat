function setup() {
  createARCanvas(480, 480, P2D, {markerId: marker_id})
}


function draw() {
  background(0,0,255,1); // R,G,B,A

  fill(0,255,0);
  noStroke();
  rect(10,100,200,300); //x,y,h,w

  noFill();
  strokeWeight(8);
  stroke(255,0,0);
  ellipse(300,240,240); //x,y,r
}
