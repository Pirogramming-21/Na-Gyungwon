const StartBtn = document.getElementById('btn__start');
const StopBtn = document.getElementById('btn__stop');
const ResetBtn = document.getElementById('btn__reset');
const DeleteBtn = document.getElementById('btn__delete');
const display = document.getElementById('stopwatch__display');
const recordList = document.getElementById('record__list');


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

function addRecords(){
    let recordId = recordList.children.length + 1;
    let checkboxId = `check_btn_${recordId}`; 

    const ListItem = document.createElement('li');
    const currentTime = display.innerHTML; // display의 내용을 가져옴
    
    ListItem.innerHTML = `
        <input type="checkbox" id="${checkboxId}" class="btns"/>
        <label for="${checkboxId}"></label>
        <span>${currentTime}</span>
    `;
    recordList.appendChild(ListItem);
}

StartBtn.addEventListener('click', () => {
    if (timerInterval) return; // 이미 타이머가 실행 중인 경우 실행하지 않음
    timerInterval = setInterval(startTimer, 10);
});

StopBtn.addEventListener('click', () => {
    addRecords();
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

DeleteBtn.addEventListener('click', () => {
    const items = recordList.querySelectorAll('li');
    items.forEach(item => {
        const checkBtn = item.querySelector('input[type="checkbox"]');
        if (checkBtn.checked) {
            item.remove();
        }
    });
});

const checkBtnAll = document.getElementById('check_btn');
checkBtnAll.addEventListener('click', () => {
    const items = recordList.querySelectorAll('li');
    if(checkBtnAll.checked){
        items.forEach(item => {
            const checkBtn = item.querySelector('input[type="checkbox"]');
            checkBtn.checked = true;
        });
    } else {
        items.forEach(item => {
            const checkBtn = item.querySelector('input[type="checkbox"]');
            checkBtn.checked = false;
        });
    }
})
