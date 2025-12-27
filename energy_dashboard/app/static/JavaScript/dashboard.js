document.addEventListener("DOMContentLoaded", () => {

  // ===== MOCK DATA =====
  const pv = document.getElementById("pv");
  const battery = document.getElementById("battery");
  const load = document.getElementById("load");

  if (pv) pv.innerText = "4.8 kW";
  if (battery) battery.innerText = "72 %";
  if (load) load.innerText = "3.2 kW";

  // ===== CHART =====
  const ctx = document.getElementById("pvChart");
  if (!ctx || typeof Chart === "undefined") {
    console.warn("Chart not available");
    return;
  }

  new Chart(ctx, {
    type: "bar",
    data: {
      labels: ["06:00", "08:00", "10:00", "12:00", "14:00", "16:00", "18:00"],
      datasets: [{
        data: [0.2, 1.4, 3.2, 4.8, 4.1, 2.6, 0.9],
        backgroundColor: "#2563eb"
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: false }
      },
      scales: {
        y: { beginAtZero: true }
      }
    }
  });
});
