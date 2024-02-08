var introVideo = document.getElementById("IntroVideo");
setTimeout(function() { 
introVideo.parentNode.removeChild(introVideo); 

var contentDivision = document.getElementById("ContentDivision");
contentDivision.style.display="block";

var mainDivision = document.getElementById("MainContainer");
mainDivision.style.backgroundColor ="white";
}, 6000);