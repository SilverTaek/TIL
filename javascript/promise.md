```
'use strict';

class UserStorage {

    loginUser(id, password) {

        return new Promise((resolve, reject) => {
            setTimeout(() => {
                if(
                    (id === 'euntaek' && password === 'taek') ||
                    (id === 'coder' && password === 'academy')
                ){
                    resolve(id);
                } else {
                    reject(new Error('not found'));
                }
            }, 2000);

        })
    }

    getRoles(user) {
        
        return new Promise((resolve, reject) => {

            setTimeout(()=>{
                if(user === 'euntaek') {
                    resolve({
                        name: 'euntaek', role: 'admin'
                    });
                } else {
                    reject(new Error('no access'));
                }
            }, 1000);
        })
    }
}

const id = prompt('ID를 입력해주세요');
const password = prompt('Password를 입력해주세요');

let userStorage = new UserStorage();

userStorage.loginUser(id, password)
            .then(userStorage.getRoles)
            .then(user => alert(`안녕 ${user.name} 너의 직급은 ${user.role} 이야 축하해`))
            .catch(console.log);

```