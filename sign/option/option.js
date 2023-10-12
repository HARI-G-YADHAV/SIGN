 // Function to navigate to the upload website
 document.getElementById("uploadButton").addEventListener("click", function() {
    window.location.href = "upload/upload.html";
});

// Function to navigate to the seating arranger website
document.getElementById("seatingArrangerButton").addEventListener("click", function() {
    window.location.href = "seating_arranger/home.html";
});

// Get the token from localStorage
const authToken = localStorage.getItem('token');

// Check if the token exists
if (authToken) {
    // You can now use authToken for your authentication or other purposes
    console.log('Token:', authToken);

} 
else {
    console.log('Token not found in localStorage');
    window.location.href="../notfound.html";

}
