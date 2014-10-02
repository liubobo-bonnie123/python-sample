function imgMotion() {
  this.min_swipe_distance = 50;
  this.max_off_swipe = 50;
  this.images = new Array;
  this.vertical = false;
  this.index = 0;
  this.skipVal = 1;
  
  this.showNextImage = function(direction) {
    if(direction === 1) {
      this.index = ((this.index + this.skipVal) < this.images.length) ? this.index + this.skipVal : this.index;
    } else if(direction === -1) {
      this.index = ((this.index - this.skipVal) >= 0) ? this.index - this.skipVal : this.index;
    }
  };

  this.dragAnimation = function(g) {
    var distance    = this.vertical ? Math.abs(g.startY - g.currentY) : Math.abs(g.startX - g.currentX);
    var offDistance = this.vertical ? Math.abs(g.startX - g.currentX) : Math.abs(g.startY - g.currentY);
    var direction   = this.vertical ? (g.previousY - g.currentY) : (g.previousX - g.currentX);

    if((offDistance < this.max_off_swipe) && (distance > this.min_swipe_distance)) {
      if(direction > 0) {
        this.showNextImage(1);
        g.element.setAttribute("src", this.images[this.index]);
      } else {
        this.showNextImage(-1);
        g.element.setAttribute("src", this.images[this.index]);
      }
    }
  };
}