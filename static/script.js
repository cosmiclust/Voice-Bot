let voices = [];

function loadVoices(callback) {
  voices = speechSynthesis.getVoices();

  if (voices.length > 0) {
    callback();
  } else {
    setTimeout(() => loadVoices(callback), 100);
  }
}

function getPreferredVoice() {
  return voices.find(v =>
    /female|zira|samantha|karen|eva|linda|woman|natural/i.test(v.name)
  ) || voices[0];
}

function speak(text) {
  if (!text) return;

  const utterance = new SpeechSynthesisUtterance(text);
  utterance.voice = getPreferredVoice();
  utterance.rate = 1.2;    // 🔊 Slightly faster
  utterance.pitch = 1.6;   // 💖 Higher pitch for cute/young tone
  utterance.volume = 1.0;

  speechSynthesis.speak(utterance);
}

window.onload = () => {
  const responseText = document.getElementById("response");

  loadVoices(() => {
    if (responseText && responseText.innerText.trim()) {
      speak(responseText.innerText.trim());
    }
  });
};
