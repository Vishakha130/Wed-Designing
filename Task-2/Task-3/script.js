const contactForm = document.getElementById('contact-form');

if (contactForm) {
  contactForm.addEventListener('submit', (event) => {
    // Prevent the form from submitting by default
    event.preventDefault();

    let isValid = true;

    // Get all form fields
    const name = document.getElementById('name');
    const email = document.getElementById('email');
    const message = document.getElementById('message');

    // Get error message spans
    const nameError = document.getElementById('name-error');
    const emailError = document.getElementById('email-error');
    const messageError = document.getElementById('message-error');

    // Reset error messages
    nameError.textContent = '';
    emailError.textContent = '';
    messageError.textContent = '';

    // Validate name field
    if (name.value.trim() === '') {
      nameError.textContent = 'Name is required.';
      isValid = false;
    }

    // Validate email field
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (email.value.trim() === '') {
      emailError.textContent = 'Email is required.';
      isValid = false;
    } else if (!emailRegex.test(email.value)) {
      emailError.textContent = 'Please enter a valid email address.';
      isValid = false;
    }

    // Validate message field
    if (message.value.trim() === '') {
      messageError.textContent = 'Message is required.';
      isValid = false;
    }

    // If all fields are valid, you can proceed with form submission
    if (isValid) {
      alert('Form submitted successfully!');
      contactForm.reset();
      // In a real-world scenario, you would send the data to a server here.
    }
  });
}
document.addEventListener('DOMContentLoaded', () => {
  const themeToggle = document.getElementById('theme-toggle');
  const body = document.body;

  themeToggle.addEventListener('click', () => {
    // Toggle the 'dark-mode' class on the body
    body.classList.toggle('dark-mode');

    // Change the button text/emoji
    if (body.classList.contains('dark-mode')) {
      themeToggle.textContent = '🌙';
    } else {
      themeToggle.textContent = '☀️';
    }
  });
});