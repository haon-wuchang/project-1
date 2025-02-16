
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
        }else if(name === 'emailDomainRef'){             
            if(ref.current.value === 'default'){
                alert('이메일주소를 선택해주세요');
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
export const handleIdCheck = (idRef,idMsgRef,pwdRef,setIdCheckResult) => {
    if(idRef.current.value===''){
        idMsgRef.current.style.setProperty('color','red');
        idRef.current.focus();
        return false;
    }else {
       //db 연동해서 중복인지 비교하고
       setIdCheckResult('아이디중복체크완료');
    }
}

// 비번 일치여부 확인 /////////////////////////////////
export const handlePasswordCheck = (pwdRef,cpwdRef,nameRef,pwdMsgRef,cpwdMsgRef) => {
if(pwdRef.current.value===''){
    pwdMsgRef.current.style.setProperty('color','red');
    pwdRef.current.focus();
    return false;
} else if(cpwdRef.current.value==='') {
    cpwdMsgRef.current.style.setProperty('color','red');
    cpwdRef.current.focus();
    return false;
}else {
    if(pwdRef.current.value!==cpwdRef.current.value){   
        alert('비번일치 x');
        pwdRef.current.value = '';
        cpwdRef.current.value = '';
        pwdRef.current.focus();      
        return false;         
    } else if (pwdRef.current.value===cpwdRef.current.value) {
        alert('ok');
        nameRef.current.focus();
        return false;
    }
}
}