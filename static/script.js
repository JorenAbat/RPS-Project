// script.js
function showContent() {
    // Hide all content
    var contents = document.querySelectorAll('.content');
    contents.forEach(function(content) {
        content.style.display = 'none';
    });

    // Get selected value
    var selectedValue = document.getElementById('choice').value;

    // Show the selected content
    if (selectedValue) {
        document.getElementById(selectedValue).style.display = 'block';
    }
}
