import { expr } from "jquery";

export const signupValidate = (refs,error,setError,isChecked1,isChecked2) => {   

if(refs.idRef.current.value === ''){
    setError({...error, ['id']:'아이디를 입력해주세요'});
    refs.idRef.current.focus();
    return false;
}else if(refs.idRef.current.value.length < 6){
    alert('6자 이상 아이디를 입력해주세요');
    refs.idRef.current.value = '';
    refs.idRef.current.focus();     
    return false;   
}else  if(refs.pwdRef.current.value === ''){
    setError({...error, ['pwd']:'비밀번호를 입력해주세요'});
    refs.pwdRef.current.focus();
    return false;
}else  if(refs.cpwdRef.current.value === ''){
    setError({...error, ['cpwd']:'비밀번호확인을 입력해주세요'});
    refs.cpwdRef.current.focus();
    return false;
}else  if(refs.usernameRef.current.value === ''){
    setError({...error, ['username']:'이름을 입력해주세요'});
    refs.usernameRef.current.focus();
    return false;
}else  if(refs.phoneRef.current.value === ''){
    setError({...error, ['phone']:'휴대폰번호를 입력해주세요'});
    refs.phoneRef.current.focus();
    return false;
}else if(refs.phoneRef.current.value.length < 13){
    alert('연락처를 양식에 맞춰 다시 작성해주세요');
    refs.phoneRef.current.value = '';
    refs.phoneRef.current.focus();
    return false;
}else if (refs.phoneRef.current.value.slice(3, 4) !== '-') {
    alert('연락처를 양식에 맞춰 다시 작성해주세요');
    refs.phoneRef.current.value = '';
    refs.phoneRef.current.focus();
    return false;
}else if (refs.phoneRef.current.value.slice(8,9) !== '-') {
    alert('연락처를 양식에 맞춰 다시 작성해주세요');
    refs.phoneRef.current.value = '';
    refs.phoneRef.current.focus();
    return false;
}else  if(refs.addressRef.current.value === ''){
    setError({...error, ['address']:'주소를 입력해주세요'});
    refs.addressRef.current.focus();
    return false;
}else  if(refs.emailRef.current.value === ''){
    setError({...error, ['email']:'이메일주소를 입력해주세요'});
    refs.emailRef.current.focus();
    return false;
}else  if(refs.emailDomainRef.current.value === 'default'){
    refs.emailDomainRef.current.style.setProperty('border', '2px solid red', 'important');
    refs.emailDomainRef.current.focus();
    return false;
}else if(isChecked1 === false){
    alert('이용약관 동의를 진행해주세요');
    return false;
}else if(isChecked2 === false){
    alert('개인정보수집 이용에 동의를 진행해주세요');
    return false;
}else {
    return true;
}
}


export const errorCheck = (name,value,error,setError) => {
    const names = [
        {"name":"id", "msg":"아디를 입력해주세요"},
        {"name":"pwd", "msg":"비번을 입력해주세요"},
        {"name":"cpwd", "msg":"비번확인을 입력해주세요"}
        ];

    names.map((item)=>
        (item.name === name) ? (
            (value ==='') ? setError({...error, [item.name]:item.msg}): setError({...error,[item.name]:''})
            ): ''
        );   
}