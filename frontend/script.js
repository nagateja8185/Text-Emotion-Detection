const submitBtn = document.getElementById("submitBtn");
const textInput = document.getElementById("textInput");
const output = document.getElementById("output");
const originalText = document.getElementById("originalText");
const emotion = document.getElementById("emotion");
const confidence = document.getElementById("confidence");
const probabilitiesDiv = document.getElementById("probabilities");
const themeToggle = document.getElementById("themeToggle");

const toggleHistory = document.getElementById("toggleHistory");
const clearHistory = document.getElementById("clearHistory");
const historyContent = document.getElementById("historyContent");
const historyTable = document.querySelector("#historyTable tbody");
const historySection = document.getElementById("historySection");

const emojiMap = {
  anger: "😡",
  disgust: "🤢",
  fear: "😨",
  joy: "😄",
  neutral: "😐",
  sadness: "😢",
  shame: "😳",
  surprise: "😲",
};

// 🌗 Dark mode toggle
themeToggle.addEventListener("click", () => {
  document.body.classList.toggle("dark");
  themeToggle.textContent = document.body.classList.contains("dark") ? "☀️" : "🌙";
});

// 📜 Collapsible history
toggleHistory.addEventListener("click", () => {
  const expanded = historyContent.classList.toggle("expanded");
  historyContent.classList.toggle("collapsed", !expanded);
  toggleHistory.textContent = expanded
    ? "📜 Prediction History ▲"
    : "📜 Prediction History ▼";
});

// 🧹 Clear history
clearHistory.addEventListener("click", () => {
  historyTable.innerHTML = "";
});

// 🚀 Submit button handler
submitBtn.addEventListener("click", async () => {
  const text = textInput.value.trim();
  if (!text) return alert("Please enter text!");

  output.classList.add("hidden");

  try {
    const res = await fetch("/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });

    const data = await res.json();

    originalText.textContent = data.text;
    emotion.textContent = `${emojiMap[data.prediction]} ${data.prediction}`;
    confidence.textContent = data.confidence.toFixed(3);

    // Probability bars
    probabilitiesDiv.innerHTML = "";
    for (const [emo, val] of Object.entries(data.probabilities)) {
      const percent = (val * 100).toFixed(1);
      const wrapper = document.createElement("div");
      wrapper.innerHTML = `
        <div class="label"><span>${emojiMap[emo]} ${emo}</span><span>${percent}%</span></div>
        <div class="bar-container">
          <div class="bar" data-emotion="${emo}" style="width:0%"></div>
        </div>`;
      probabilitiesDiv.appendChild(wrapper);

      setTimeout(() => {
        wrapper.querySelector(".bar").style.width = `${percent}%`;
      }, 100);
    }

    // History
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${data.text}</td>
      <td>${emojiMap[data.prediction]} ${data.prediction}</td>
      <td>${data.confidence.toFixed(3)}</td>`;
    historyTable.prepend(row);
    historySection.classList.remove("hidden");

    output.classList.remove("hidden");
  } catch (err) {
    alert("❌ Error connecting to server.");
  }
});
