const fileInput = document.getElementById('file-input');
const uploadedImage = document.getElementById('uploaded-image');

fileInput.addEventListener('change', () => {
    const file = fileInput.files[0];
    const reader = new FileReader();

    reader.onload = (event) => {
        uploadedImage.src = event.target.result;
    };

    reader.readAsDataURL(file);
});