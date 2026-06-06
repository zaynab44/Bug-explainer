async function explainBug() {
  const bugInput = document.getElementById("bugInput").value.trim();
  const outputBox = document.getElementById("outputBox");
  const explainBtn = document.getElementById("explainBtn");

  if (!bugInput) {
    outputBox.innerHTML = "Please paste your error or buggy code first.";
    return;
  }

  explainBtn.disabled = true;
  explainBtn.textContent = "Analyzing...";
  outputBox.innerHTML = '<span class="loading">AI is analyzing your bug...</span>';

  try {
    const response = await fetch("/explain", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ bug: bugInput })
    });

    const data = await response.json();

    if (data.error) {
      outputBox.innerHTML = "Error: " + data.error;
    } else {
      outputBox.innerHTML = data.answer;
    }
  } catch (err) {
    outputBox.innerHTML = "Something went wrong. Please try again.";
  }

  explainBtn.disabled = false;
  explainBtn.textContent = "🔍 Explain My Bug";
}

function clearAll() {
  document.getElementById("bugInput").value = "";
  document.getElementById("outputBox").innerHTML = "";
}