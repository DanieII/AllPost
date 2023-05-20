const commentIcon = document.querySelector('.fa-comment');
const commentForm = document.querySelector('form')

commentIcon.addEventListener('click', () => {
    commentForm.classList.toggle('form-active');
})
