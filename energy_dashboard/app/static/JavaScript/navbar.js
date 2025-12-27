document.addEventListener("click", (e) => {
  if (e.target.id === "logoutBtn") {
    localStorage.removeItem("token");
    window.location.replace("/");
  }
});

document.addEventListener("DOMContentLoaded", () => {
  fetch("/static/HTML/navbar.html")
    .then(r => r.text())
    .then(html => {
      document.getElementById("navbar").innerHTML = html;
    });
});
