//함수 모음(check_numbers 제외)
function get_random_nums() {
    const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    const results = [];

    for(let i = 0; i < 3; i++){
        const index = Math.floor(Math.random() * numbers.length);
        results.push(numbers[index]);
        numbers.splice(index, 1);
    }

    return results;
};

function clearInput() {
    const inputs = document.querySelectorAll(".input-field");
    inputs.forEach(function(input) {
        input.value = '';
    });
}

function display_ending(success) {
    //확인하기 버튼 비활성화
    const game_btn = document.querySelector('.submit-button');
    game_btn.classList.add('disabled');
    game_btn.disabled = true;

    //game-result div
    const game_result_div = document.createElement('div');
    game_result_div.className = 'game-result';

    //이미지: id가 game-result-img인 img태그 사용
    const game_result_img = document.createElement('img');
    game_result_img.id = 'game-result-img';

    if(success){
        game_result_img.src = './success.png';
    } else{
        game_result_img.src = './fail.png';
    }
    game_result_div.appendChild(game_result_img);

    //document/result-display 앞에 추가
    const result_display = document.querySelector('.game-board');
    result_display.insertBefore(game_result_div, null);
}

//공통 부분(left_div 생성) 묶기
function display_left_div(user_inputs) {
    const left_div = document.createElement('div');
    left_div.className = 'left';
    left_div.textContent = `${user_inputs[0]} ${user_inputs[1]} ${user_inputs[2]}`;
    return left_div;
}


function display_result(user_inputs, strike_cnt, ball_cnt){
    const check_result_div = document.createElement('div');
    check_result_div.className = 'check-result';
    left_div = display_left_div(user_inputs);

    const right_div = document.createElement('div');
    left_div.className = 'right';

    if(strike_cnt == 0 && ball_cnt == 0){
        right_div.innerHTML = `
        <div class="right">
            <div class="out num-result">O</div>
        </div>
        `;

    } else{
        right_div.innerHTML = `
        <div class="right">
            ${strike_cnt} <div class="strike num-result">S</div>
            ${ball_cnt} <div class="ball num-result">B</div>
        </div>
        `;
    }
    check_result_div.appendChild(left_div);
    check_result_div.appendChild(document.createTextNode(':'));
    check_result_div.appendChild(right_div);

    const result_display = document.querySelector('.result-display');
    result_display.appendChild(check_result_div);
    
    //게임 종료 조건 1: 모두 스트라이크일 경우
    if(strike_cnt == 3){
        display_ending(true);
    }
}

function check_answer(user_inputs) {
    // 숫자와 위치가 전부 틀리면 아웃, O 출력
    // 아웃이 아니면 스트라이크카운트 S 볼카운트 B 출력
    // 숫자는 맞지만 위치가 틀리면 볼카운트 += 1
    // 숫자와 위치가 전부 맞으면 스크라이크 += 1
    let ball_cnt = 0;
    let strike_cnt = 0;
    for(let i = 0; i < user_inputs.length; i++){
        if(user_inputs[i] == answers[i]){
            strike_cnt++;
        } else if(answers.includes(user_inputs[i])){
            ball_cnt++;
        }
    }
    display_result(user_inputs, strike_cnt, ball_cnt);
}


//게임 초기화
//시도 가능 횟수 설정
const try_num = 9;
let try_cnt = 1;

//중복되지 않는 3개의 랜덤한 숫자 설정
const answers = get_random_nums();

//html의 input과 결과창 내용 비우기
document.addEventListener("DOMContentLoaded", function(){
    const start = document.querySelector('.result-display');
    start.innerHTML = '';
    clearInput();
});

//숫자 확인
function check_numbers(){
    num1 = document.getElementById('number1');
    num2 = document.getElementById('number2');
    num3 = document.getElementById('number3');
    //입력되지 않은 input 확인
    if(num1.value == '' || num2.value == '' || num3.value == ''){
        clearInput();
        return;
    }
    else{
        //입력된 숫자들과 정답을 비교하여 결과를 생성하는 로직 만들기
        let user_inputs = [Number(num1.value), Number(num2.value), Number(num3.value)];
        //기회 남아있는지 확인
        //게임 종료 조건 2, 더 이상 기회 없을 때 -> 버튼 9번 누를 수 있음
        if(try_cnt >= try_num){
            display_ending(false);
            }
        else {
            try_cnt++;
            check_answer(user_inputs);
            clearInput();
        }
    }
}