

// (function(document){
//     var div = document.getElementById('container');
//     var icon = document.getElementById('icon');
//     var open = false;
  
//     div.addEventListener('click', function(){
//         if(open){
//             icon.className = 'fa fa-chevron-down';  
//             console.log("open");
//         } else{
//             icon.className = 'fa fa-chevron-down open';
//         }

//         open = !open;
//         });
    
//   })(document);


var theParent = document.querySelector("#animate-chevron");
theParent.addEventListener("click", doSomething, false);

function doSomething(e) {
    if(e.target !== e.currentTarget) {
        var clickedItem = e.target.id;

        alert("Hello " + clickedItem);
    }

    e.stopPropagation();
}

// var elements = ['jobDescription', 'updateButton', 'equipmentList', 'jobDesc', 'equipRan'];

// for(i = 0; i < elements.length; i++) {
//    document.getElementById(elements[i]).style.display = "block";
// }

// (function(document){
//     var div = document.getElementbyClassName('icon');

//     var open = false;

//     for(i = 0; i < div.length; i++) {

//         div.addEventListener('click', function(){
//             if(open){
//                 icon.className = 'fa fa-chevron-down';  
//                 console.log("open");
//             } else{
//                 icon.className = 'fa fa-chevron-down open';
//             }
        
//             open = !open;
//         });
//     }

//   })(document);