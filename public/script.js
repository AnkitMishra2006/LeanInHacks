document
  .getElementById("predictForm")
  .addEventListener("submit", async function (event) {
    event.preventDefault();
    const year = document.getElementById("year").value;
    const co2 = document.getElementById("co2").value;

    // const response = await fetch("http://localhost:5000/predict", {
    //   method: "POST",
    //   headers: { "Content-Type": "application/json" },
    //   body: JSON.stringify({ year: parseInt(year), co2: parseFloat(co2) }),
    // });

    // const data = await response.json();
    // document.getElementById(
    //   "predictionResult"
    // ).innerText = `Predicted Temperature: ${data.predicted_temp.toFixed(2)}°C`;
  });
