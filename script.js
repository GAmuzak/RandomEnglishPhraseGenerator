let phrases = [];
let shuffledPhrases = [];
let currentIndex = 0;

async function loadPhrases() {
    const response = await fetch('phrases.json');
    phrases = await response.json();
    shufflePhrases();
}

function shufflePhrases() {
    shuffledPhrases = [...phrases];
    for (let i = shuffledPhrases.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffledPhrases[i], shuffledPhrases[j]] = [shuffledPhrases[j], shuffledPhrases[i]];
    }
    currentIndex = 0;
}

function showRandomPhrase() {
    if (shuffledPhrases.length === 0) return;
    if (currentIndex >= shuffledPhrases.length) {
        shufflePhrases();
    }
    const newPhrase = shuffledPhrases[currentIndex];
    currentIndex++;
    document.getElementById('phrase-container').innerText = newPhrase;
}

window.onload = async () => {
    await loadPhrases();
    showRandomPhrase();
};

window.onclick = () => {
    showRandomPhrase();
};

window.onkeydown = (event) => {
    if (event.code === 'Space') {
        showRandomPhrase();
    }
};