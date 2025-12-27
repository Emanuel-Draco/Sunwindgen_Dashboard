document.addEventListener("DOMContentLoaded", () => {

  // ===== MOCK DATA =====
  document.getElementById("pv").innerText = "4.8 kW";
  document.getElementById("battery").innerText = "72 %";
  document.getElementById("load").innerText = "3.2 kW";

  loadNavbar();

  function loadNavbar() {
  fetch("/static/HTML/navbar.html")
    .then(r => {
      if (!r.ok) throw new Error("Navbar not found");
      return r.text();
    })
    .then(html => {
      const nav = document.getElementById("navbar");
      if (nav) nav.innerHTML = html;
    })
    .catch(err => console.error("Navbar load error:", err));
}

  // ===== CHART =====
  const ctx = document.getElementById("pvChart");
  if (!ctx) {
    console.error("Canvas pvChart not found");
    return;
  }

  const labels = ["06:00", "08:00", "10:00", "12:00", "14:00", "16:00", "18:00"];
  const values = [0.2, 1.4, 3.2, 4.8, 4.1, 2.6, 0.9];

  new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [{
        data: values,
        backgroundColor: "#2563eb"
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: false }
      },
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });

});
