 var imgMotion = {
    
    config : {
        MIN_SWIPE_DISTANCE : 40,
        startY : -1000,
        startXY : -1000,        
        containerElem : "",
        images : [],
        index : 0,
        vertical : true
    },
    
    init : function (elem, imgArray, vertical) {
        this.config.containerElem = elem;
        this.config.images = imgArray;
        this.config.vertical = vertical;
        
        $(this.config.containerElem).append('<div class="imgmotion_show"><img src="'+this.config.images[0]+'"/></div>');
        
        $(this.config.containerElem).get(0).addEventListener("touchstart", this.touchStart, true);
        $(this.config.containerElem).get(0).addEventListener("touchmove",  this.touchMove, true);            
        $(this.config.containerElem).get(0).addEventListener("touchend",  this.touchEnd, true);            
    },
        
    showNextImage : function(direction)
    { 
      try{
          if (direction === 1){ 
              this.config.index = ((this.config.index + 1) < this.config.images.length) ? this.config.index + 1 : this.config.index;
          }
          
          if (direction === -1){ 
              this.config.index = ((this.config.index - 1) >= 0) ? this.config.index - 1 : this.config.index;
          }

          $('div.imgmotion_show img').attr("src", this.config.images[this.config.index]);

      }catch(err){
          $('div#mmath').append('<h1>Exception'+err.description+'</h1>');    
      }   
    },    
        
    touchStart : function (event) {
//       imgMotion.config.startY = this.scrollTop + event.touches[0].pageY;
       imgMotion.config.startXY = this.scrollTop + imgMotion.config.vertical ? event.touches[0].pageY : event.touches[0].pageX;
    },
 
    touchMove : function (event) {    
        var delta = 0, distance = 0, pageXY=0;

        pageXY = imgMotion.config.vertical ? event.touches[0].pageY : event.touches[0].pageX;
        delta = pageXY - imgMotion.config.startXY;
        distance = Math.sqrt(delta*delta);

        if (distance >= imgMotion.config.MIN_SWIPE_DISTANCE) {               
           imgMotion.showNextImage(imgMotion.config.startXY < pageXY ? 1 : -1);
           imgMotion.config.startXY = pageXY;
        }

        event.preventDefault();    
    },        
    
    touchEnd : function (event) {
        pageXY = imgMotion.config.vertical ? event.touches[0].pageY : event.touches[0].pageX;
        
        alert(pageXY);
    }        
    
/*
    touchMove : function (event) {    
        var delta = 0, distance = 0;
    
        delta    = event.touches[0].pageY - imgMotion.config.startY;
        distance = Math.sqrt(delta*delta);

        if (distance >= imgMotion.config.MIN_SWIPE_DISTANCE) {               
           imgMotion.showNextImage(imgMotion.config.startY < event.touches[0].pageY ? 1 : -1);
           imgMotion.config.startY = event.touches[0].pageY;
        }

        event.preventDefault();    
    }        

*/
};