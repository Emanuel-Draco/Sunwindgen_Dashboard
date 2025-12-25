document.addEventListener("DOMContentLoaded", () => {

  const token = localStorage.getItem("token");
  if (!token) {
    window.location.replace("/");
    return;
  }

  // ===== NAVBAR =====
  fetch("/static/navbar.html")
    .then(r => r.text())
    .then(html => {
      const navbar = document.getElementById("navbar");
      if (navbar) navbar.innerHTML = html;
    });

  // ===== ENERGY DATA (tylko na dashboard) =====
  if (document.getElementById("pv")) {
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
      document.getElementById("pv").textContent = data.pv_production;
      document.getElementById("battery").textContent = data.battery;
      document.getElementById("load").textContent = data.load;
    });
  }

});
