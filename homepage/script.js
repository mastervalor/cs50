function showAlert() {
    alert('Welcome to the Interactive Website!');
}

function changeBackgroundColor() {
    const colors = ['#f8f9fa', '#dee2e6', '#ced4da', '#adb5bd', '#868e96'];
    let index = 0;

    setInterval(function () {
        document.body.style.backgroundColor = colors[index];
        index = (index + 1) % colors.length;
    }, 2000);
}

function toggleColor() {
    const currentColor = document.body.style.backgroundColor;
    const newColor = currentColor === 'pink' ? 'lightblue' : 'pink';
    document.body.style.backgroundColor = newColor;
}


document.addEventListener('DOMContentLoaded', function () {
    showAlert();

    changeBackgroundColor();

    const colorButton = document.getElementById('colorButton');
    if (colorButton) {
        colorButton.addEventListener('click', toggleColor);
    }
});
