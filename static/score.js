scoreDiv = document.querySelector('#score-total');

startBtn.addEventListener('click', () => {
    form.classList.remove('hide');
    playerScore.classList.remove('hide');

    startBtn.classList.add('hide');
    
    score = 0;
    playerScore.innerHTML = '';
    playerScore.append(`Score:${score}`)

    let count = 10;
    timer = document.createElement('p');

    const interval = setInterval(() => {
        timer.innerText = `Time:${count--}`
        scoreDiv.append(timer)

        if ( count < 0 ){
            form.classList.add('hide');
            timer.remove()
            startBtn.classList.remove('hide');
            clearInterval(interval);
        }
    },1000)

});




