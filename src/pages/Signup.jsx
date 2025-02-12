import { useRef, useState } from "react";

export default function Signup(){
    const formData = {
        'id':'', 
        'pwd':'',
        'cpwd':'',
        'name':'',
        'phone':'',
        'emailName':'',
        'emailDomain':''
    };
    const [data, setData] = useState(formData);

    const refs = {
        'idRef':useRef(null),
        'pwdRef':useRef(null),
        'cpwdRef':useRef(null),
        'nameRef':useRef(null),
        'phoneRef':useRef(null),
        'emailNameRef':useRef(null),
        'emailDomainRef':useRef(null)
    };


    const signupValidate = () => {
        if(refs.idRef.current.value === ''){
            alert('아이디를 입력해주세요');
            refs.idRef.current.focus();
        }else  if(refs.pwdRef.current.value === ''){
            alert('비밀번호를 입력해주세요');
            refs.pwdRef.current.focus();
        }else  if(refs.cpwdRef.current.value === ''){
            alert('비밀번호 확인을 입력해주세요');
            refs.cpwdRef.current.focus();
        }else  if(refs.nameRef.current.value === ''){
            alert('이름을 입력해주세요');
            refs.nameRef.current.focus();
        }else  if(refs.phoneRef.current.value === ''){
            alert('전화번호를 입력해주세요');
            refs.phoneRef.current.focus();
        }else  if(refs.emailNameRef.current.value === ''){
            alert('이메일을 입력해주세요');
            refs.emailNameRef.current.focus();
        }else  if(refs.emailDomainRef.current.value === 'default'){
            alert('이메일주소를 선택해주세요');
            refs.emailDomainRef.current.focus();
        }
    }


    const handleSignupForm = (e) => {
        const {name, value} = e.target;
        setData({...data, [name]:value});
    }
    console.log(data);
    
    const handleSubmit = (e) => {
        e.preventDefault();
        signupValidate();
        console.log(data);
        
    }
    return (
        <>
        <div className="signupBox">
            <section className="signup-wrap">
                <h1>회원가입</h1> 
                <form action="" onSubmit={handleSubmit}>
                <ul>
                    <li className="signup-top">
                        <label htmlFor="">아이디</label>
                        <input type="text"  onChange={handleSignupForm} name= 'id'
                            ref={refs.idRef}
                            placeholder="영문/숫자 조합으로 6~20자 사이로 입력해주세요"/>
                        <span>여기에 아디 입력안하면 빨간색뜨게 에러메세지들 만들어</span>
                    </li>
                    <li className="signup-top">
                        <label htmlFor="">비밀번호</label>
                        <input type="text" onChange={handleSignupForm} name= 'pwd'
                            ref={refs.pwdRef}
                            placeholder="영문/숫자 조합으로 8~16자 사이로 입력해주세요"/>
                            <span></span>
                    </li>
                    <li className="signup-top">
                        <label htmlFor="">비밀번호 확인</label>
                        <input type="text"  onChange={handleSignupForm} name = 'cpwd'
                            ref={refs.cpwdRef}
                            placeholder="비밀번호를 한 번 더 입력해주세요"/>
                            <span></span>
                    </li>
                    <li className="signup-top">
                        <label htmlFor="">이름</label>
                        <input type="text"  onChange={handleSignupForm} name="name"
                            ref={refs.nameRef}
                            placeholder="이름을 입력해주세요"/>
                            <span></span>
                    </li>
                    <li className="signup-top">
                        <label htmlFor="">연락처</label>
                        <input type="text"  onChange={handleSignupForm} name="'phone"
                            ref={refs.phoneRef}
                            placeholder="- 없이 입력해주세요"/>
                            <span></span>
                    </li>
                    <li className="signup-top">
                        <label htmlFor="">이메일</label>
                        <input type="text"  onChange={handleSignupForm} name="emailName"
                            ref={refs.emailNameRef}
                            placeholder="이메일 주소를 입력해주세요"/>
                        <span>@</span>
                        <select name="emailDomain" id="" onChange={handleSignupForm}
                            ref={refs.emailDomainRef} >
                            <option value="default">선택</option>
                            <option value="naver">naver.com</option>
                            <option value="gmail">gmail.com</option>
                            <option value="daum">daum.net</option>
                        </select>
                        <span>dddd</span>
                    </li>
                    <li className="signup-top">
                        <label htmlFor="">이용약관</label>
                        <textarea name="" id="">
                            이용약관 내용
                        </textarea>
                    </li>
                </ul>
                    <li className="signup-bottom">
                        <input type="checkbox" className="checkInput" />
                        <span>(필수) 이용약관에 동의 합니다.</span>
                    </li>
                    <li className="signup-bottom">
                        <label htmlFor="">개인정보수집 이용동의</label>     
                    <table>
                        <tr>
                            <th>일시</th>
                            <th>수집항목</th>
                            <th>수집목적</th>
                            <th>보유기간</th>
                        </tr>
                        <tr>
                            <td>가입시</td>
                            <td>아이디(이메일), 비밀번호, 이름, 전화번호</td>
                            <td>회원식별 및 연락</td>
                            <td>회원 탈퇴시 까지</td>
                        </tr>
                        <tr>
                            <td>거리발생시 (추가)</td>
                            <td>주소, 결제수단정보, 수령인, 연락처</td>
                            <td>결제 및 배송, 불만 처리시 본인확인</td>
                            <td>전상법 등 관련 법률에 의한 보관기간</td>
                        </tr>
                    </table>
                    </li>
                    <li className="signup-bottom">
                        <input type="checkbox" name="" id="" className="checkInput"/>
                        <span> (필수) 개인정보수집 이용에 동의합니다.</span>
                        <p>※ 약관 및 개인정보 처리방침은 홈페이지 하단에 전문이 게재되어 있습니다.</p>
                        <p>※ 이용약관 및 개인정보 수집.이용 내용에 대해 동의 거부가 가능하며, 이 경우 회원가입 및 관련 서비스는 이용이 불가합니다.</p>
                    </li>
                    <li className="signup-bottom">
                        <input type="checkbox" name="" id="" className="checkInput"/>
                        <span> (선택) 이메일을 통한 상품 및 이벤트 정보 수신에 동의합니다.</span>
                    </li>
                    <li className="signup-bottom">
                        <input type="checkbox" name="" id=""className="checkInput" />
                        <span>(선택) 휴대폰을 통한 상품 및 이벤트 정보 수신에 동의 합니다. 미동의 시에도 주문 결제와 관련된 정보는 발송됩니다.</span>
                    </li>
                    <li className="signup-bottom">
                        <p>※ 선택 항목으로 동의하지 않아도 불이익을 받지 않습니다.</p>
                        <p>※ 만 14세 미만은 회원가입 및 서비스 이용이 불가합니다.</p>
                    </li>
                <button type="submit">회원가입하기</button>
                </form>
            </section>
        </div>
        </>
    );
}



