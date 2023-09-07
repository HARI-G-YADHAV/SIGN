// Function to remove the token from local storage
function removeTokenFromLocalStorage() {
    localStorage.removeItem('token'); // Replace 'authToken' with the key you use to store the token
  }
  
  // Function to handle the logout action
  function logout() {
    // Remove the token from local storage
    removeTokenFromLocalStorage();
  
    // Perform any other logout actions if needed
    console.log("Token removed from local storage");
  }
  
  // Attach a click event listener to the logout button
  const logoutButton = document.getElementById('logout-button'); // Replace 'logout-button' with the actual ID of your logout button
  if (logoutButton) {
    logoutButton.addEventListener('click', function(event) {
      // Prevent the default behavior of the button (e.g., form submission)
      event.preventDefault();
  
      // Call the logout function to remove the token from local storage
      logout();
      const newWindow = window.open('http://127.0.0.1:5500/sign/sign.html', '_self');
      newWindow.onload = function() {
        newWindow.location.reload();
      };

    });
  }
  