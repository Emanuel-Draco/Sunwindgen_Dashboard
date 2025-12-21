if (!localStorage.getItem("logged")) {
  window.location.href = "/login.html";
}

fetch("/api/energy")
  .then(r => r.json())
  .then(data => {
    document.getElementById("data").innerHTML = `
      PV: ${data.pv_production}<br>
      Battery: ${data.battery}<br>
      Load: ${data.load}
    `;
  });
