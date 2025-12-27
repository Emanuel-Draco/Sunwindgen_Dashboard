document.addEventListener("click", (e) => {
  if (e.target.id === "logoutBtn") {
    localStorage.removeItem("token");
    window.location.replace("/");
  }
});

document.addEventListener("DOMContentLoaded", () => {

  fetch("/static/HTML/navbar.html")
    .then(r => {
      if (!r.ok) throw new Error("Navbar HTML not found");
      return r.text();
    })
    .then(html => {
      const el = document.getElementById("navbar");
      if (el) el.innerHTML = html;
    })
    .catch(err => console.error("Navbar load error:", err));

});

