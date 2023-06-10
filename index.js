document.addEventListener('DOMContentLoaded', function() {
    var dynamicContent = document.getElementById('signinForm');
    dynamicContent.style.display = 'none';
  });
  
function switchsignin() {
    var signupForm = document.getElementById('signupForm');
    var signinForm = document.getElementById('signinForm');
  
    signupForm.style.display = 'none';
    signinForm.style.display = 'block';
    signinForm.scrollIntoView({ behavior: 'smooth' });
  }
  
  function switchsignup() {
    var signupForm = document.getElementById('signupForm');
    var signinForm = document.getElementById('signinForm');
  
    signupForm.style.display = 'block';
    signinForm.style.display = 'none';
    signupForm.scrollIntoView({ behavior: 'smooth' });
  }
  