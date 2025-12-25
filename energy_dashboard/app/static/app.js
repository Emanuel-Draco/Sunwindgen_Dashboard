const token = localStorage.getItem("token");

if (!token) {
  window.location.replace("/");
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

fetch("/api/energy", {
  headers: {
    "Authorization": "Bearer " + token
  }
})
.then(r => {
  if (r.status === 401) location.href = "/";
  return r.json();
})
.then(data => {
  document.getElementById("data").innerHTML = `
    PV: ${data.pv_production}<br>
    Battery: ${data.battery}<br>
    Load: ${data.load}
  `;
});
