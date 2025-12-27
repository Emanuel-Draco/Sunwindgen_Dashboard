document.addEventListener("click", (e) => {
  if (e.target.id === "logoutBtn") {
    localStorage.removeItem("token");
    window.location.replace("/");
  }
});
