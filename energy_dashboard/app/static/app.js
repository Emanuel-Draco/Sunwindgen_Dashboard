const token = localStorage.getItem("token");

if (!token) {
  window.location.replace("/");
}

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
