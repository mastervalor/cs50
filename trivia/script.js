// script.js

function checkAnswer(button) {
    // Get the selected answer text
    var selectedAnswer = button.textContent.trim();

    // Define the correct answer
    var correctAnswer = "Paris";

    // Get the feedback element
    var feedback = document.getElementById("mc-feedback");

    // Check if the selected answer is correct
    if (selectedAnswer === correctAnswer) {
        // Set correct feedback
        feedback.textContent = "Correct!";
        feedback.style.color = "green";

        // Change button color to green
        button.style.backgroundColor = "green";
    } else {
        // Set incorrect feedback
        feedback.textContent = "Incorrect";
        feedback.style.color = "red";

        // Change button color to red
        button.style.backgroundColor = "red";
    }
}

function checkFreeResponse() {
    // Get the user's answer from the input field
    var userAnswer = document.getElementById("fr-answer").value.trim().toLowerCase();

    // Define the correct answer
    var correctAnswer = "blue whale";

    // Get the feedback element
    var feedback = document.getElementById("fr-feedback");

    // Check if the user's answer is correct
    if (userAnswer === correctAnswer) {
        // Set correct feedback
        feedback.textContent = "Correct!";
        feedback.style.color = "green";

        // Change input field color to green
        document.getElementById("fr-answer").style.backgroundColor = "green";
    } else {
        // Set incorrect feedback
        feedback.textContent = "Incorrect";
        feedback.style.color = "red";

        // Change input field color to red
        document.getElementById("fr-answer").style.backgroundColor = "red";
    }
}
