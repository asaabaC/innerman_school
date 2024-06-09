function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "navbar-lists") {
        x.className += " responsive";
    } else {
        x.className = "navbar-lists";
    }
}

document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form from submitting normally
    var fullName = document.getElementById('fullName').value;
    var email = document.getElementById('email').value;
    var phone = document.getElementById('phone').value;
    var message = document.getElementById('message').value;
    // Add your form submission logic here
    alert("Form submitted successfully!");
});
