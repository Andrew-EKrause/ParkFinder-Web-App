

(function(document){
    var div = document.getElementById('container');
    var icon = document.getElementById('icon');
    var open = false;
  
    div.addEventListener('click', function(){
      if(open){
        icon.className = 'fa fa-chevron-down';  
        console.log("open");
      } else{
        icon.className = 'fa fa-chevron-down open';
      }
  
      open = !open;
    });
  })(document);