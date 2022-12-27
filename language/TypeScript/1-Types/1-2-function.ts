{
    // JavaScript
    // function jsAdd(num1, num2) {
    //     return num1 + num2;
    // }

    let jsAdd = (num1, num2) => num1 + num2;
    console.log(jsAdd(2,5));

    // function tsAdd(num1: number, num2: number): number {
    //     return num1 + num2;
    // }

    let tsAdd = (num1: number, num2: number): number => num1 + num2;

    console.log(tsAdd(3,3));

    //JavaScript

    function jsFetchNum(id) {
        // code...
        // code...
        // code...
        return new Promise((resolve, reject) => {
            resolve(100);
        });
    }

    // TypeScript

    function tsFetchNum(id: string): Promise<number> {
        return new Promise((resolve, reject) => {
            resolve(100);
        });
    }

    // Optional parameter
    function printName(firstName: string, lastName?: string) {
        console.log(firstName);
        console.log(lastName); // undefined
    }

    printName('Steve', 'Jobs');
    printName('Ellie');
    printName('Anna');

    //Default parameter
    function printMessage(message: string = 'default message') {
        console.log(message);
    }
    printMessage();

    // Rest parameter
    function addNumbers(...numbers: number[]): number {
        return numbers.reduce((a,b) => a + b);
    }

    console.log(addNumbers(1,2));
    console.log(addNumbers(1,2,3));
    console.log(addNumbers(1,2,4,5));
    console.log(addNumbers(1,2,67,10));
}