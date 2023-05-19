const messages = document.querySelectorAll('.message');
console.log(messages);

if (messages.length > 0){
    messages.forEach((message) => {
        setTimeout(() => {
            message.classList.add('remove-message')
        }, 800);
    });
}