import { useRef, useState } from "react";
import { TbAdFilled } from "react-icons/tb";
import { useNavigate } from "react-router-dom";

export default function Signup(){
    // const navigate = useNavigate();
    //체크박스 상태 관리
    const [isChecked1, setIsChecked1] = useState(false);
    const [isChecked2, setIsChecked2] = useState(false);
    const handleChecked1 = (e) => {setIsChecked1(e.target.checked);}
    const handleChecked2 = (e) => {setIsChecked2(e.target.checked);}


// 비밀번호 일치여부, 아이디 중복체크 진행 1.
// 아이디 중복체크는 db에서 현재있는 회원들 아이디 정보가져와서 비교해야함;; 흑
// 화면 지저분하니까 따로 파일에 refs 나 애들 저장해놓고 불러서 쓰기 2.
// 회원가입버튼누르면 서버로 formData 전송 3.

    const formData = {
        'id':'', 
        'password':'',
        'cpwd':'',
        'username':'',
        'phone':'',
        'address':'',
        'email':'',
        'emailDomain':''
    };
    const [data, setData] = useState(formData);

    const refs = {
        'idRef':useRef(null),
        'pwdRef':useRef(null),
        'cpwdRef':useRef(null),
        'usernameRef':useRef(null),
        'phoneRef':useRef(null),
        'addressRef':useRef(null),
        'emailRef':useRef(null),
        'emailDomainRef':useRef(null)
    };
    
    
        const errorMsg = {
            'idErrMsg':useRef(null),
            'pwdErrMsg':useRef(null),
            'cpwdErrMsg':useRef(null),
            'usernameErrMsg':useRef(null),
            'phoneErrMsg':useRef(null),
            'emailErrMsg':useRef(null),
            'addressErrMsg':useRef(null),
        };

    const signupValidate = () => {
        if(refs.idRef.current.value === ''){
            errorMsg.idErrMsg.current.style.setProperty('color','red');
            refs.idRef.current.focus();
        }else if(refs.idRef.current.value.length < 6){
            alert('6자 이상 아이디를 입력해주세요');
            refs.idRef.current.value = '';
            refs.idRef.current.focus();        
        }else  if(refs.pwdRef.current.value === ''){
            errorMsg.pwdErrMsg.current.style.setProperty('color','red');
            refs.pwdRef.current.focus();
        }else  if(refs.cpwdRef.current.value === ''){
            errorMsg.cpwdErrMsg.current.style.setProperty('color','red');
            refs.cpwdRef.current.focus();
        }else  if(refs.usernameRef.current.value === ''){
            errorMsg.cpwdEusernameErrMsgrrMsg.current.style.setProperty('color','red');
            refs.usernameRef.current.focus();
        }else  if(refs.phoneRef.current.value === ''){
            errorMsg.phoneErrMsg.current.style.setProperty('color','red');
            refs.phoneRef.current.focus();
        }else if(refs.phoneRef.current.value.length < 13){
            alert('전화번호 양식에 맞춰 다시 작성해주세요');
            refs.phoneRef.current.value = '';
            refs.phoneRef.current.focus();
        }
        // 전번 left 함수써서 - 얘가 4번째 9번째 자리에 있는지 체크해야햠;;;
        else  if(refs.addressRef.current.value === ''){
            errorMsg.addressErrMsg.current.style.setProperty('color','red');
            refs.addressRef.current.focus();
        }else  if(refs.emailRef.current.value === ''){
            errorMsg.emailErrMsg.current.style.setProperty('color','red');
            refs.emailRef.current.focus();
        }else  if(refs.emailDomainRef.current.value === 'default'){
            refs.emailDomainRef.current.style.setProperty('border','1px solid red');
            refs.emailDomainRef.current.focus();
        }else if(isChecked1 === false){
            alert('이용약관 동의를 진행해주세요');
        }else if(isChecked2 === false){
            alert('개인정보수집 이용에 동의를 진행해주세요');
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
        // navigate('/login');
        console.log(data);
        
    }
    return (
        <>
        <div className="signupBox">
            <section className="signup-wrap">
                <h1>회원가입</h1> 
                <form action="" onSubmit={handleSubmit}>
                <ul>
                    <li className="signup-top ">
                        <label htmlFor="">아이디</label>
                            <div className="dupliBox">
                                <input type="text"  onChange={handleSignupForm} name= 'id'
                                    ref={refs.idRef} className="dupliInput"
                                    placeholder="영문/숫자 조합으로 6~50자 사이로 입력해주세요"/>
                                <button className="dupliId">중복확인</button>
                            </div>
                        <span className="signup-err" ref={errorMsg.idErrMsg}>아이디를 입력해주세요</span>
                    </li>
                    <li className="signup-top">
                        <label htmlFor="">비밀번호</label>
                        <input type="text" onChange={handleSignupForm} name= 'password'
                            ref={refs.pwdRef}
                            placeholder="영문/숫자 조합으로 8~16자 사이로 입력해주세요"/>
                        <span className="signup-err" ref={errorMsg.pwdErrMsg}>비밀번호를 입력해주세요</span>
                    </li>
                    <li className="signup-top">
                        <label htmlFor="">비밀번호 확인</label>
                        <input type="text"  onChange={handleSignupForm} name = 'cpwd'
                            ref={refs.cpwdRef}
                            placeholder="비밀번호를 한 번 더 입력해주세요"/>
                        <span className="signup-err" ref={errorMsg.cpwdErrMsg}>비밀번호 확인을 입력해주세요</span>
                    </li>
                    <li className="signup-top">
                        <label htmlFor="">이름</label>
                        <input type="text"  onChange={handleSignupForm} name="username"
                            ref={refs.usernameRef}
                            placeholder="이름을 입력해주세요"/>
                        <span className="signup-err" ref={errorMsg.usernameErrMsg} >이름을 입력해주세요</span>
                    </li>
                    <li className="signup-top">
                        <label htmlFor="">연락처</label>
                        <input type="text"  onChange={handleSignupForm} name="'phone"
                            ref={refs.phoneRef}
                            placeholder="- 포함 13자리를 입력해주세요"/>
                        <span className="signup-err" ref={errorMsg.phoneErrMsg}>전화번호를 입력해주세요</span>
                    </li>
                    <li className="signup-top">
                        <label htmlFor="">주소</label>
                        <input type="text"  onChange={handleSignupForm} name="'address"
                            ref={refs.addressRef}
                            placeholder="기본 배송주소를 입력해주세요"/>
                        <span className="signup-err" ref={errorMsg.addressErrMsg}>주소를 입력해주세요</span>
                    </li>
                    <li className="signup-top">
                        <label htmlFor="">이메일</label>
                        <input type="text"  onChange={handleSignupForm} name="email"
                            ref={refs.emailRef}
                            placeholder="이메일 주소를 입력해주세요"/>
                        <span className="emailEmt">@</span>
                        <select name="emailDomain" id="" onChange={handleSignupForm}
                            ref={refs.emailDomainRef} >
                            <option value="default">선택</option>
                            <option value="naver">naver.com</option>
                            <option value="gmail">gmail.com</option>
                            <option value="daum">daum.net</option>
                        </select>
                        <span className="signup-err" ref={errorMsg.emailErrMsg}>이메일을 입력해주세요</span>
                    </li>
                    <li className="signup-top">
                        <label htmlFor="">이용약관</label>
                        <div className="textarea">
                        ssf 이용약관<br />
                        제1조(목적) <br />
                        이 약관은 주식회사 브이에프 코리아 (전자상거래 사업자, 이하 "회사"라고 합니다)가 운영하는 팀버랜드 브랜드 – 사이버스토어 (이하 "스토어"라고 합니다)에서 제공하는 인터넷 관련 서비스(이하 "서비스"라고 합니다)를 이용함에 있어 "스토어"와 이용자의 권리·의무 및 책임사항을 규정함을 목적으로 합니다.
                        ※ PC통신, 모바일, 무선, VoIP, IPTV, 데이터방송 등을 이용하는 전자거래에 대해서도 그 성질에 반하지 않는 한 이 약관을 준용합니다.
                        </div>
                    </li>
                    <li className="signup-bottom">
                        <input type="checkbox" className="checkInput" name="checkBox1" 
                            checked={isChecked1} onChange={handleChecked1}/>
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
                        <input type="checkbox" name="checkBox2" className="checkInput"
                            checked={isChecked2} onChange={handleChecked2}/>
                        <span> (필수) 개인정보수집 이용에 동의합니다.</span>
                        <p>※ 약관 및 개인정보 처리방침은 홈페이지 하단에 전문이 게재되어 있습니다.</p>
                        <p>※ 이용약관 및 개인정보 수집.이용 내용에 대해 동의 거부가 가능하며, 이 경우 회원가입 및 관련 서비스는 이용이 불가합니다.</p>
                    </li>
                    <li className="signup-bottom">
                        <input type="checkbox" className="checkInput"/>
                        <span> (선택) 이메일을 통한 상품 및 이벤트 정보 수신에 동의합니다.</span>
                    </li>
                    <li className="signup-bottom">
                        <input type="checkbox"  className="checkInput" />
                        <span> (선택) 휴대폰을 통한 상품 및 이벤트 정보 수신에 동의 합니다. 미동의 시에도 주문 결제와 관련된 정보는 발송됩니다.</span>
                    </li>
                    <li className="signup-bottom">
                        <p>※ 선택 항목으로 동의하지 않아도 불이익을 받지 않습니다.</p>
                        <p>※ 만 14세 미만은 회원가입 및 서비스 이용이 불가합니다.</p>
                    </li>
                </ul>
                <button type="submit">회원가입하기</button>
                </form>
            </section>
        </div>
        </>
    );
}



