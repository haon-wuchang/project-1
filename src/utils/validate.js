
export const signupValidate = (refs,msgRefs,isChecked1,isChecked2) => {
    const refsEntries = Object.entries(refs);
    const msgRefsEntries = Object.entries(msgRefs);

    for(let  i = 0 ; i < refsEntries.length ; i++){  
        const item = refsEntries[i];  //itme = ['id':~~~]
        const name = item[0];
        const ref = item[1];
        
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
        }else{          
            if(ref.current.value === 'default'){
                 alert('이메일주소 선택');
                ref.current.focus();
                return false;
            }  
        }
    }
    if(isChecked1 === false){
        alert('이용약관 동의를 진행해주세요');
        return false;
    }else if(isChecked2 === false){
        alert('개인정보수집 이용에 동의를 진행해주세요');
        return false;
    }
    return true; 
}
// if(refs.idRef.current.value === ''){
//     setError({...error, ['id']:'아이디를 입력해주세요'});
//     refs.idRef.current.focus();
//     return false;
// }else if(refs.idRef.current.value.length < 6){
//     alert('6자 이상 아이디를 입력해주세요');
//     refs.idRef.current.value = '';
//     refs.idRef.current.focus();     
//     return false;   
// }else  if(refs.pwdRef.current.value === ''){
//     setError({...error, ['password']:'비밀번호를 입력해주세요'});
//     refs.pwdRef.current.focus();
//     return false;
// }else  if(refs.cpwdRef.current.value === ''){
//     setError({...error, ['cpwd']:'비밀번호확인을 입력해주세요'});
//     refs.cpwdRef.current.focus();
//     return false;
// }else  if(refs.usernameRef.current.value === ''){
//     setError({...error, ['username']:'이름을 입력해주세요'});
//     refs.usernameRef.current.focus();
//     return false;
// }else  if(refs.phoneRef.current.value === ''){
//     setError({...error, ['phone']:'휴대폰번호를 입력해주세요'});
//     refs.phoneRef.current.focus();
//     return false;
// }else if(refs.phoneRef.current.value.length < 13){
//     alert('전화번호 양식에 맞춰 다시 작성해주세요');
//     refs.phoneRef.current.value = '';
//     refs.phoneRef.current.focus();
//     return false;
// }// 전번 left 함수써서 - 얘가 4번째 9번째 자리에 있는지 체크해야햠;;;
// else  if(refs.addressRef.current.value === ''){
//     setError({...error, ['address']:'주소를 입력해주세요'});
//     refs.addressRef.current.focus();
//     return false;
// }else  if(refs.emailRef.current.value === ''){
//     setError({...error, ['email']:'이메일주소를 입력해주세요'});
//     refs.emailRef.current.focus();
//     return false;
// }else  if(refs.emailDomainRef.current.value === 'default'){
//     refs.emailDomainRef.current.style.setProperty('border','1px solid red'); // 이건 왜 안먹냐
//     refs.emailDomainRef.current.focus();
//     return false;
// }else if(isChecked1 === false){
//     alert('이용약관 동의를 진행해주세요');
//     return false;
// }else if(isChecked2 === false){
//     alert('개인정보수집 이용에 동의를 진행해주세요');
//     return false;
// }else {
//     return true;
// }