const btn1 = document.querySelector('#step1-btn')
const btn2 = document.querySelector('#step2-btn')

function nextPage(e) {
    const currentStep = e.target.parentElement;
    const nextStep = e.target.parentElement.nextElementSibling

    currentStep.classList.remove('fadein')
    void currentStep.offsetWidth
    currentStep.classList.add('fadeout')

    currentStep.addEventListener('animationend', () => {
        currentStep.classList.remove('active');
        nextStep.classList.add('active');
    });
}

btn1.addEventListener('click', nextPage);
btn2.addEventListener('click', nextPage);

