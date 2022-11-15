const form = document.querySelector('#guess-form');
const userGuess = document.querySelector('input');
const startBtn = document.querySelector('#start-btn');

const resultsSection = document.querySelector('#results');
const playerScore = document.querySelector('#score');


const resItem = document.createElement('p');
const scoreVal = document.createElement('p');

let score = 0;
$(document).ready(function(){
    $('#guess-form').on('submit', (e) => {
        e.preventDefault();
        $.ajax({
            data: {
                userGuess: $('#guess-input').val(),
            },
                type: 'POST',
                url: '/guess'
            })
    
        .done(function(data){
    
            console.log(data);
            resItem.setAttribute('id', 'results-text');
            resItem.innerHTML = data.result;
            resultsSection.append(resItem);
    
            if(data.result === 'ok'){
                playerScore.innerHTML = ''
                for(let guessCount in userGuess.value){
                    score++
                }
                playerScore.append(`Score:${score}`)
            }
            form.reset();
        });
    })
})