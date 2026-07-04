// =======================================
// Hand Gesture Recognition
// script.js
// =======================================

console.log("Hand Gesture Recognition Started");

// Future feature:
// Display detected gesture from FastAPI

function showMessage(message) {
    console.log(message);
}

// Future feature:
// Start Camera

function startCamera() {
    console.log("Camera Started");
}

// Future feature:
// Stop Camera

function stopCamera() {
    console.log("Camera Stopped");
}

// Future feature:
// Full Screen

function fullScreen() {

    if (document.documentElement.requestFullscreen) {
        document.documentElement.requestFullscreen();
    }

}

// Future feature:
// Exit Full Screen

function exitFullScreen() {

    if (document.exitFullscreen) {
        document.exitFullscreen();
    }

}

// Future feature:
// Speak Gesture

function speak(text){

    let speech = new SpeechSynthesisUtterance();

    speech.text = text;

    speech.rate = 1;

    speech.volume = 1;

    speech.pitch = 1;

    window.speechSynthesis.speak(speech);

}