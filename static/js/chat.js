var isRecording = false;
var recognition;

$("#textInput").keydown(function (e) {
  console.log(e);
  if (e.key == 'Enter') {
    getBotResponse();
  }
});

function toggleRecording() {
  var recordButton = document.getElementById('recordButton');
  if (!isRecording) {
    if (window.hasOwnProperty('webkitSpeechRecognition')) {
      recognition = new webkitSpeechRecognition();

      recognition.continuous = true;
      recognition.interimResults = false;

      recognition.lang = lang;
      recognition.start();

      recognition.onresult = function (e) {
        document.getElementById('textInput').value += e.results[0][0].transcript + ' ';
        recognition.stop();
      };

      recognition.onerror = function (e) {
        console.log('error', e);
        recognition.stop();
      };

      //keeps recording until button pressed
      recognition.onend = function (e) {
        console.log('ended', e);
        if (isRecording){
          recognition.start();
        }
      };
    }
    recordButton.src = 'static/img/stop.svg';
    isRecording = true;
  }
  else {
    recordButton.src = 'static/img/record.svg';
    recognition.stop();
    isRecording = false;
    getBotResponse();
  }
};

function getBotResponse() {
  var rawText = $("#textInput").val();
  var userHtml = '<p class="userText"><span>' + rawText + "</span></p>";
  $("#textInput").val("");
  $("#chatbox").append(userHtml);
  document
    .getElementById("userInput")
    .scrollIntoView({ block: "start", behavior: "smooth" });
  $.get("/get", { msg: rawText }).done(function (data) {
    var botHtml = '<p class="botText"><span>' + data + '</span></p>';
    $("#chatbox").append(botHtml);
    document
      .getElementById("userInput")
      .scrollIntoView({ block: "start", behavior: "smooth" });
      var speech = new SpeechSynthesisUtterance(data);
      speech.lang = lang;
      window.speechSynthesis.cancel();
      window.speechSynthesis.speak(speech);
      
      // prevents tts from cutting off
      let r = setInterval(() => {
        console.log(speechSynthesis.speaking);
        if (!speechSynthesis.speaking) {
          clearInterval(r);
        } else {
          speechSynthesis.pause();
          speechSynthesis.resume();
        }
      }, 14000);
  });
}