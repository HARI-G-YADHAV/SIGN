function toggleForm(e) {
    var signupForm = document.getElementById("signupForm");
    var signinForm = document.getElementById("signinForm");
    
    if (signupForm.style.display === "none") {
      signupForm.style.display = "block";
      signinForm.style.display = "none";
    } else {
      signupForm.style.display = "none";
      signinForm.style.display = "block";
    }
}
const userToken = 'your-user-token-value'; 
function signIn() {
  var username = document.getElementById('Username').value;
  var password = document.getElementById('Password').value;

  // Create JSON payload
  var jsonData = {
    username: username,
    password: password
  };

  // Make POST request to sign-in API endpoint
  fetch('http://localhost:8000//api/sign-in/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Token ${userToken}`,
    },
    body: JSON.stringify(jsonData)
  })
    .then(response => response.json())
    .then(data => {
      // Handle the response from the sign-in API
      console.log(data);
      const message = data.message;
      localStorage.setItem("token", data.token);
      // Update the content of the placeholder element
      const messagePlaceholder = document.getElementById('messagePlaceholder');
      messagePlaceholder.textContent = message;
      if (data.token) {
        window.location.href = 'option/option.html';

      } else {
        console.error('Authentication failed:', data);
      }
    })
    .catch(error => {
      // Handle any errors
      console.error(error);
    });
}

function signUp() {
    var username = document.getElementById('username').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;

    // Create the JSON payload
    var jsonData = {
      username: username,
      email: email,
      password: password
    };

    // Make the API request to the Django backend
    fetch('http://localhost:8000//api/sign-up/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(jsonData)
    })
      .then(response => response.json())
      .then(data => {
        // Handle the response from the Django backend
        console.log(data);
        const message = data.message;

        // Update the content of the placeholder element
        const messagePlaceholder = document.getElementById('messagePlaceholder');
        messagePlaceholder.textContent = message;
      })
      .catch(error => {
        // Handle any errors
        console.error(error);
      });

      signinForm.style.display = "block";
      signupForm.style.display = "none";
  }
  