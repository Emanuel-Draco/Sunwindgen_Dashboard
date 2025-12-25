document.addEventListener("DOMContentLoaded", () => {

  const token = localStorage.getItem("token");
  if (!token) {
    window.location.replace("/");
    return;
  }

  // ===== NAVBAR LOADER =====
  fetch("/static/navbar.html")
    .then(r => {
      if (!r.ok) throw new Error("Navbar not found");
      return r.text();
    })
    .then(html => {
      const navbar = document.getElementById("navbar");
      if (navbar) navbar.innerHTML = html;
    });

  // ===== ENERGY DATA =====
  fetch("/api/energy", {
    headers: {
      "Authorization": "Bearer " + token
    }
  })
  .then(r => {
    if (r.status === 401) {
      localStorage.removeItem("token");
      window.location.replace("/");
    }
    return r.json();
  })
  .then(data => {
    const el = document.getElementById("data");
    if (el) {
      el.innerHTML = `
        PV: ${data.pv_production}<br>
        Battery: ${data.battery}<br>
        Load: ${data.load}
      `;
    }
  });

});

