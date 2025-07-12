document.getElementById("login").addEventListener("submit", async function(e) {
  e.preventDefault();

  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const messageDiv = document.getElementById("message"); // <– Message div

  const response = await fetch("http://127.0.0.1:5000/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ email, password })
  });

  const data = await response.json();

  if (response.ok) {
    messageDiv.textContent = "✅ Login successful!";
    messageDiv.style.color = "green";
    localStorage.setItem("user", JSON.stringify(data.user));

    // Optional redirect after 1.5s
    setTimeout(() => {
      window.location.href = "/dashboard";
    }, 1500);
  } else {
    messageDiv.textContent = "❌ Login failed: " + data.error;
    messageDiv.style.color = "red";
  }
});

// 👇 This handles clicking the "Register" link
function redirectToRegister() {
  window.location.href = "/register";
}
