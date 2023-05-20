const messages = document.querySelectorAll('.message');

if (messages.length > 0){
    messages.forEach((message) => {
        setTimeout(() => {
            message.classList.add('remove-message')
        }, 800);
    });
}