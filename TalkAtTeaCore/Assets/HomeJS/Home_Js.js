var introVideo = document.getElementById("IntroVideo");
function delayFunctionForVideo(){
    introVideo.parentNode.removeChild(introVideo); 

    var contentDivision = document.getElementById("ContentDivision");
    contentDivision.style.display="block";

    var mainDivision = document.getElementById("MainContainer");
    mainDivision.style.backgroundColor ="white";
}

setTimeout(delayFunctionForVideo, 6000);