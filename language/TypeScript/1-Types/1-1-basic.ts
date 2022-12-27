/**
 * JavaSCript
 * Primitive: number, string, boolean, bigint, symbol, null, undefined
 * Object: function, array.....
 */
{
    // num
    const num:number = -6;

    // string
    const str:string = 'hello';

    //boolean
    const boal:boolean = false;

    //undefined

    let name: undefined; // X
    let age: number | undefined;
    age = undefined;
    age = 1;
    function find(): number | undefined {
        return undefined;
    }

    //null
    let person: null; // X
    person = null;
    let person2: string | null;

    // unknown X 

    let notSure: unknown = 0;
    notSure = 'he';
    notSure = true;
    
    //any X
    let anything: any = 0;
    anything = 'hello';

    //void
    function print(): void {
        console.log('hello');
        return;
    }

    let unusable: void = undefined; // X

    // never
    function throwError(message: string): never {
        // message -> server (log)
        // throw new Error(message);
        throw new Error(message);
    }
    let neverEnding: never; // X

    //object
    let obj: object; // X
    function acceptSomeObject(obj: object) {
    }

    acceptSomeObject({name : 'taek'});
    acceptSomeObject({animal: 'dog'});
}