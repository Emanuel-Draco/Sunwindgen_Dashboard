document.addEventListener("DOMContentLoaded", () => {
  const token = localStorage.getItem("token");
  if (!token) {
    window.location.replace("/");
    return;
  }

  loadNavbar();
});

function loadNavbar() {
  fetch("/static/HTML/navbar.html")
    .then(r => r.text())
    .then(html => {
      document.getElementById("navbar").innerHTML = html;
    });
}
