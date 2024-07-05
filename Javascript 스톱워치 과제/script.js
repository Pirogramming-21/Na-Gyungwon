const StartBtn = document.getElementById('btn__start');
const StopBtn = document.getElementById('btn__stop');
const ResetBtn = document.getElementById('btn__reset');
const display = document.getElementById('stopwatch__display');


let timerInterval;
let millis = 0;
let seconds = 0;
let minutes = 0;

function startTimer() {
    millis++;
    
    if (millis > 99) {
        seconds++;
        millis = 0;
    }

    if (seconds > 59) {
        minutes++;
        seconds = 0;
    }
    
    if (minutes > 0){
        display.innerHTML = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}:${millis.toString().padStart(2, '0')}`;

    } else {
        display.innerHTML = `${seconds.toString().padStart(2, '0')}:${millis.toString().padStart(2, '0')}`;
    }
}

StartBtn.addEventListener('click', () => {
    if (timerInterval) return; // 이미 타이머가 실행 중인 경우 실행하지 않음
    timerInterval = setInterval(startTimer, 10);
});

StopBtn.addEventListener('click', () => {
    clearInterval(timerInterval);
    timerInterval = null;
});

ResetBtn.addEventListener('click', () => {
    clearInterval(timerInterval);
    timerInterval = null;
    millis = 0;
    seconds = 0;
    display.innerHTML = "00:00";
});

