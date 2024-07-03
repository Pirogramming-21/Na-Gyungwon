//게임 초기화

//시도 가능 횟수 설정
const try_num = 9;
let try_cnt = 0;
//중복되지 않는 3개의 랜덤한 숫자 설정
function getRandomNums() {
    const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    const results = [];

    for(let i = 0; i < 3; i++){
        const index = Math.floor(Math.random() * 9);
        results.push(numbers[index]);
        numbers.splice(index, 1);
    }

    return results;
};

const answers = getRandomNums();

//html의 input과 결과창 내용 비우기
function clearInput() {
    const inputs = document.querySelectorAll(".input-field");
    inputs.forEach(function(input) {
        input.value = '';
    });
}

document.addEventListener("DOMContentLoaded", function(){
    const start = document.querySelector('.result-display');
    start.innerHTML = '';
    // console.log(answers);
    clearInput();
});

//숫자 확인
function checkAnswer(user_inputs) {
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
    
    if(ball_cnt == 0 && strike_cnt == 0){
        console.log('O');
    }

}

function check_numbers(){
    num1 = document.getElementById('number1');
    num2 = document.getElementById('number2');
    num3 = document.getElementById('number3');
    // console.log(num1.value, num2, num3);
    //입력되지 않은 input 확인
    if(num1.value == '' || num2.value == '' || num3.value == ''){
        clearInput();
        return;
    }
    else{
        //입력된 숫자들과 정답을 비교하여 결과를 생성하는 로직 만들기
        let user_inputs = [num1.value, num2.value, num3.value];
        //기회 남아있는지 확인
        if(try_cnt >= try_num){ console.log('out'); }
        else {
            try_cnt++;
            // console.log(user_inputs);
            checkAnswer(user_inputs);
            clearInput();
        }
    }

}