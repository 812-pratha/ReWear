document.getElementById("login").addEventListener("submit", async function(e) {
  e.preventDefault();

  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  const response = await fetch("http://127.0.0.1:5000/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ email, password })
  });

  const data = await response.json();

  if (response.ok) {
    alert("Login successful!");
    console.log(data.user); // contains idToken and email
    localStorage.setItem("user", JSON.stringify(data.user)); // optional
  } else {
    alert("Login failed: " + data.error);
  }
});

