document.addEventListener("DOMContentLoaded", () => {
  const DEV_MODE = true; 
  const token = localStorage.getItem("token");

  if (!DEV_MODE && !token) {
    window.location.replace("/");
    return;
  }

  // =========================
  // NAVBAR
  // =========================
  fetch("navbar.html")
    .then(res => {
      if (!res.ok) throw new Error("Navbar not found");
      return res.text();
    })
    .then(html => {
      const navbar = document.getElementById("navbar");
      if (navbar) navbar.innerHTML = html;
    })
    .catch(err => console.warn("Navbar error:", err));

  // =========================
  // ENERGY DATA
  // =========================
  if (DEV_MODE) {
    // MOCK DATA (DEV)
    setEnergy({
      pv_production: "3.4 kW",
      battery: "82 %",
      load: "1.2 kW"
    });
  } else {
    // REAL API (ADDON)
    fetch("/api/energy", {
      headers: {
        "Authorization": "Bearer " + token
      }
    })
    .then(r => {
      if (r.status === 401) {
        localStorage.removeItem("token");
        window.location.replace("/");
        return;
      }
      return r.json();
    })
    .then(data => setEnergy(data))
    .catch(err => console.error("Energy API error:", err));
  }

});

// =========================
// HELPERS
// =========================
function setEnergy(data) {
  const pv = document.getElementById("pv");
  const battery = document.getElementById("battery");
  const load = document.getElementById("load");

  if (pv) pv.innerText = data.pv_production ?? "–";
  if (battery) battery.innerText = data.battery ?? "–";
  if (load) load.innerText = data.load ?? "–";
}