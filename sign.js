function toggleForm() {
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
  
function signIn() {
  // Handle sign in functionality
  alert('Sign In clicked!');
}

function signUp() {

  signinForm.style.display = "block";
  signupForm.style.display = "none";
}