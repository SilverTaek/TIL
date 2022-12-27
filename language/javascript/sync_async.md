class UserStorage {

    loginUser(id, password, onSucess, onError) {
        setTimeout(() => {
            if(
                (id === 'euntaek' && password === 'taek') ||
                (id === 'coder' && password === 'academy')
            ){
                onSucess(id);
            } else {
                onError(new Error('not found'));
            }
        }, 2000)
    }

    getRoles(user, onSucess, onError) {
        setTimeout(()=>{
            if(user === 'euntaek') {
                onSucess({
                    name: 'euntaek', role: 'admin'
                });
            } else {
                onError(new Error('no access'));
            }
        }, 1000);
    }
}

const id = prompt('ID를 입력해주세요');
const password = prompt('Password를 입력해주세요');

let userStorage = new UserStorage();

userStorage.loginUser(id, password,
     user => {
     userStorage.getRoles(user, userWithRoles => {
        alert(`안녕 ${userWithRoles.name} 너의 직급은 ${userWithRoles.role} 이야 축하해`);
     }, 
     error => {
        console.log(error);
     })
});