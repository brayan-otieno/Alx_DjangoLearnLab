document.addEventListener('DOMContentLoaded', function () {
    // Basic interactivity: alert when the page loads
    console.log("Welcome to the blog!");

    // Example: Adding an event listener to all blog post titles
    const postLinks = document.querySelectorAll('ul li a');
    postLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            alert('You clicked on: ' + link.textContent);
        });
    });
});
