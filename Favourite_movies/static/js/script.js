
document.addEventListener('DOMContentLoaded', ()=> {
    const currentUrl = window.location.href;
    document.querySelectorAll('.nav-bottom a').forEach((a)=> {
        if (currentUrl.endsWith('movies')) return
        if (currentUrl.includes((a.innerText.toLowerCase())) ) {
            a.classList.add('nav-selected')
        }
    })
})