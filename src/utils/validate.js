import axios from 'axios';

export const signupValidate = (refs,msgRefs,isChecked1,isChecked2) => {   
    const refsEntries = Object.entries(refs.current);
    const msgRefsEntries = Object.entries(msgRefs.current);

    for(let i = 0; i<refsEntries.length ; i++){
        const item = refsEntries[i];  
        const name = item[0]; 
        const ref = item [1];         

        let msgItem, msgName, msgRef = null; 

        if(i < refsEntries.length -1 ){     
         msgItem = msgRefsEntries[i];
         msgName = msgItem[0];
         msgRef = msgItem[1];  
        }

        if(name !== 'emailDomainRef'){ 
            if(ref.current.value === ''){
                msgRef.current.style.setProperty('color','red');
                ref.current.focus();
                return false;
            }
            // else{
            //     msgRef.current.style.setProperty('color','white');
            // }
        }else if(name === 'emailDomainRef'){             
            if(ref.current.value === 'default'){
                alert('이메일주소를 선택해주세요');    // 이거도 안뜨는데 💦
                ref.current.focus();
                return false;
            }                     
        }       
    }
    if(isChecked1 === false){
        alert('이용약관 확인을 진행해주세요');
        return false;
    }else if(isChecked2 === false){
        alert('개인정보수집 이용확인을 진행해주세요');
        return false;
    }

    return true;    
}


// 아디 중복체크 함수 /////////////////////////////////////////
export const handleIdCheck = (idRef,idMsgRef,pwdRef,setIdCheckResult,setError,error) => {
    if(idRef.current.value===''){
        setError({...error,['id']:'아이디를 입력해주세요'});
        idMsgRef.current.style.setProperty('color','red');
        idRef.current.focus();
        return false;
    }else {
        //db 연동해서 중복인지 비교하고💦
        axios
            .post('http://localhost:9000/user/idCheck',{'idRef' : idRef.current.value})
            .then(res => console.log(res.data))
            .catch(error => console.log(error));


        const did = 'test';
        if(idRef.current.value===did){
            setError({...error,['id']:'사용중인 아이디입니다'});
            idMsgRef.current.style.setProperty('color','red');
            idRef.current.value = '';
            idRef.current.focus();
        }else{
            setError({...error,['id']:'사용가능한 아이디입니다'});
            idMsgRef.current.style.setProperty('color','blue');
            setIdCheckResult('아이디중복체크완료');
            pwdRef.current.focus();
        }
    }
}

// 비번 일치여부 확인 /////////////////////////////////
// error,setError 쓰면 에러남;;;; 얘도 비번일치하면 파란색으로 뜨게 하고싶은뎅 ㅜㅠㅜㅠㅜ 왜안대지💦
export const handlePasswordCheck = (pwdRef,cpwdRef,nameRef,pwdMsgRef,cpwdMsgRef,setError,error) => {
if(pwdRef.current.value===''){
    // setError({...error,['pwd']:'비밀번호를 입력해주세요'});
    pwdMsgRef.current.style.setProperty('color','red');
    pwdRef.current.focus();
    return false;
} else if(cpwdRef.current.value==='') {
    // setError({...error,['cpwd']:'비밀번호확인을 입력해주세요'});
    cpwdMsgRef.current.style.setProperty('color','red');
    cpwdRef.current.focus();
    return false;
}else {
    if(pwdRef.current.value!==cpwdRef.current.value){   
        // setError({...error,['cpwd']:'비밀번호가 일치하지않습니다'});
        cpwdMsgRef.current.style.setProperty('color','red');
        // alert('비번일치 안함');
        pwdRef.current.value = '';
        cpwdRef.current.value = '';
        pwdRef.current.focus();      
        return false;         
    } else if (pwdRef.current.value===cpwdRef.current.value) {
        // setError({...error,['cpwd']:'비밀번호가 일치합니다'});
        cpwdMsgRef.current.style.setProperty('color','blue');
        nameRef.current.focus();
        return false;
    }
}
}