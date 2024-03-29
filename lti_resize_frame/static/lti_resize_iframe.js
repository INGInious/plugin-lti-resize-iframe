$('#main-content').css("min-height", 0);

bodyHeight = 0;
function resizeAndPostSize() {
    if (document.getElementById("main-content")) {
        if (document.getElementById("main-content").scrollHeight != bodyHeight) {
            // Get scrollHeight and add the side menu height
            bodyHeight = document.getElementById("main-content").scrollHeight + 50;
            window.parent.postMessage({height: bodyHeight}, "*");
        }
    }
}

var target = document.querySelector('body');

var observer = new MutationObserver(resizeAndPostSize);

var config = { attributes: true, subtree: true };

observer.observe(target, config);
$(window).ready(function() {
   $('#main-content').css("min-height", 0);
   setTimeout(resizeAndPostSize, 0);
});
