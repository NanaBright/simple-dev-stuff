function validateEmail(email) {
    // Regular expression pattern to validate email addresses
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailPattern.test(email);
}

// Example usage:
const email = "example@test.com";
if (validateEmail(email)) {
    console.log("Valid email address");
} else {
    console.log("Invalid email address");
}
