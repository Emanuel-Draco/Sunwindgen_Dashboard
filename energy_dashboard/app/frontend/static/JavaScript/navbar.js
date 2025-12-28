document.addEventListener("DOMContentLoaded", () => {
  // Load navbar HTML
  fetch("/navbar.html")
    .then(r => {
      if (!r.ok) throw new Error("Navbar not found");
      return r.text();
    })
    .then(html => {
      const nav = document.getElementById("navbar");
      if (nav) nav.innerHTML = html;
    })
    .catch(err => console.error("Navbar load error:", err));

  // Logout handler
  document.addEventListener("click", (e) => {
  if (e.target.id === "logoutBtn") {
    fetch("/api/logout", { method: "POST" })
      .finally(() => {
        window.location.replace("/");
      });
  }
});
});
