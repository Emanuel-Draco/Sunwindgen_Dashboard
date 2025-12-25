document.addEventListener("DOMContentLoaded", async () => {

  // ===== AUTH CHECK =====
  const token = localStorage.getItem("token");
  if (!token) {
    window.location.replace("/");
    return;
  }

  // ===== LOAD NAVBAR =====
  try {
    const res = await fetch("/static/navbar.html");
    if (!res.ok) throw new Error("Navbar load failed");
    const html = await res.text();

    const navbar = document.getElementById("navbar");
    if (navbar) navbar.innerHTML = html;

    // attach navbar logic
    const script = document.createElement("script");
    script.src = "/static/navbar.js";
    document.body.appendChild(script);
  } catch (e) {
    console.error("Navbar error:", e);
  }

  // ===== ENERGY DATA (ONLY ON DASHBOARD) =====
  const pv = document.getElementById("pv");
  if (pv) {
    const r = await fetch("/api/energy", {
      headers: { Authorization: "Bearer " + token }
    });

    if (r.status === 401) {
      localStorage.removeItem("token");
      window.location.replace("/");
      return;
    }

    const data = await r.json();
    pv.innerText = data.pv_production ?? "–";
    document.getElementById("battery").innerText = data.battery ?? "–";
    document.getElementById("load").innerText = data.load ?? "–";
  }

});
