$('#content').css("min-height", 0);

bodyHeight = 0;
function resizeAndPostSize() {
    if (document.getElementById("content")) {
        if (document.getElementById("content").scrollHeight != bodyHeight) {
            bodyHeight = document.getElementById("content").scrollHeight;
            window.parent.postMessage({height: bodyHeight}, "*");
        }
    }
}

var target = document.querySelector('body');

var observer = new MutationObserver(resizeAndPostSize);

var config = { attributes: true, subtree: true };

observer.observe(target, config);
$(window).ready(function() {
   $('#content').css("min-height", 0);
   setTimeout(resizeAndPostSize, 0);
});