const num: number = 2;
const result = gugu(num);

function gugu(num: number) {
    let i: number;
    for (i = 1; i<=9; i++) {
        console.log(`${num} * ${i} = ${num * i}`)
    }
}

console.log(result);