function loadNavbar() {
  fetch("/static/navbar.html")
    .then(r => r.text())
    .then(html => {
      document.getElementById("navbar").innerHTML = html;
    });
}

function logout() {
  localStorage.removeItem("token");
  location.href = "/";
}

loadNavbar();
