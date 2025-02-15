import { useRef } from "react";
import React from 'react';


export const initDatas = () => {
    const namesKr = ['아이디','비밀번호','비밀번호확인','이름','휴대폰번호','주소','이메일'];
    const names = ['id','password','cpwd','username','phone','address','email'];

    const placeHolders = ['영문/숫자 조합으로 6~50자 사이로 입력해주세요',
        '영문/숫자 조합으로 6~50자 사이로 입력해주세요 ','비밀번호를 재입력해주세요',
        '이름을 입력해주세요','휴대폰번호를 ( - ) 포함하여 입력해주세요',
        '기본배송주소를 입력해주세요','이메일주소를 입력해주세요'];

    const formData = names.reduce((acc,key)=>{
        acc[key]='';
        return acc;
    },{});

    const labels = names.reduce((acc,name,index)=>{
        acc[name] = namesKr[index];    
        return acc;
    },{});
    // console.log(labels);

    const placehol = names.reduce((acc,name,index)=>{
        acc[name] = placeHolders[index]; 
        return acc;
    },{});

    return {names,placehol,labels, formData};
    }
    

export const useInitRefs = (names) => {
    const refs = useRef (
        names.reduce((acc,name)=>{
            acc[name.concat('Ref')] = React.createRef(); 
            return acc;
        },{})
    )
    refs.current.emaildomainRef = useRef(React.createRef()); 
    // console.log('Refs',refs);    
    
    const msgRefs = useRef(
        names.reduce((acc, name)=>{ //idMsgRef  이렇게 만들거임
        acc[name.concat('MsgRef')] = React.createRef();
        return acc;
        },{})
    );
    // console.log('msg',msgRefs);
    return {refs,msgRefs};
}
    
    



    
