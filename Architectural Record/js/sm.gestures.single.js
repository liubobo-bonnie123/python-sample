function Gesture() {
  this.isSingle = false;
  this.hasMoved = false;
  this.startX = 0;
  this.startY = 0;
  this.previousX = 0;
  this.previousY = 0;
  this.currentX = 0;
  this.currentY = 0;
  this.element = null;

  this.touchStart = function(e) {
    var numTouches = e.touches;
    if(numTouches.length === 1) {
      this.isSingle = true;
      this.startX = numTouches[0].pageX;
      this.startY = numTouches[0].pageY;
      this.currentX = this.startX;
      this.currentY = this.startY;
      this.element = e.target;
    }
  };

  this.touchMove = function(e) {
    var numTouches = e.touches;
    if(this.isSingle && numTouches.length === 1) {
      e.preventDefault();
      this.hasMoved = true;
      this.previousX = this.currentX;
      this.previousY = this.currentY;
      this.currentX = numTouches[0].pageX;
      this.currentY = numTouches[0].pageY;
    } else {
      this.isSingle = false;
      this.hasMoved = false;
    }
  };

  this.touchEnd = function(e) {
    if(this.isSingle) {
      e.preventDefault();
    }
  };
}