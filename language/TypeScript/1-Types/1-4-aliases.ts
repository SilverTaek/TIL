{
    /**
     *  Type Aliases
     */
    type Text = string;
    const name: Text = 'taek';
    const address: Text = 'korea';
    type Num = number;
    type Student = {
        name: string;
        age: number;
    };

    const student: Student = {
        name: 'taek',
        age: 30,
    };
 
    /**
     * String Literal Types
     * 
     */
    type Name = 'name';
    let taekName: Name;
    taekName = 'name';
    type JSON = 'json'
    const json: JSON = 'json';
}