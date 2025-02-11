export default function Signup(){
    // 팀버랜드 참고해서 만들기
    return (
        <>
        <div className="signupBox">
            <section className="signup-wrap">
                <h1>회원가입</h1> 
                <ul>
                    <li>
                        <label htmlFor="">아이디</label>
                        <input type="text"  
                            placeholder="영문/숫자 조합으로 6~20자 사이로 입력해주세요"/>
                    </li>
                    <li>
                        <label htmlFor="">비밀번호</label>
                        <input type="text" 
                            placeholder="영문/숫자 조합으로 8~16자 사이로 입력해주세요"/>
                    </li>
                    <li>
                        <label htmlFor="">비밀번호 확인</label>
                        <input type="text" 
                            placeholder="비밀번호를 한 번 더 입력해주세요"/>
                    </li>
                    <li>
                        <label htmlFor="">이름</label>
                        <input type="text" 
                            placeholder="이름을 입력해주세요"/>
                    </li>
                    <li>
                        <label htmlFor="">연락처</label>
                        <input type="text" 
                            placeholder="- 없이 입력해주세요"/>
                    </li>
                    <li>
                        <label htmlFor="">이메일</label>
                        <input type="text" 
                            placeholder="이메일 주소를 입력해주세요"/>
                    </li>
                    <li>
                        <label htmlFor="">이용약관</label>
                        <textarea name="" id="">
                            이용약관 내용
                        </textarea>
                    </li>
                    <li>
                        <input type="checkbox" />
                        <span>(필수) 이용약관에 동의 합니다.</span>
                    </li>
                    <li>
                    개인정보수집 이용동의
                    </li>
                    <li>
                        <input type="checkbox" name="" id="" />
                        <span> (필수) 개인정보수집 이용에 동의합니다.</span>
                        <p>※ 약관 및 개인정보 처리방침은 홈페이지 하단에 전문이 게재되어 있습니다.</p>
                        <p>※ 이용약관 및 개인정보 수집.이용 내용에 대해 동의 거부가 가능하며, 이 경우 회원가입 및 관련 서비스는 이용이 불가합니다.</p>
                    </li>
                    <li>
                        <input type="checkbox" name="" id="" />
                        <span> (선택) 이메일을 통한 상품 및 이벤트 정보 수신에 동의합니다.</span>
                    </li>
                    <li>
                        <input type="checkbox" name="" id="" />
                        <span>(선택) 휴대폰을 통한 상품 및 이벤트 정보 수신에 동의 합니다. 미동의 시에도 주문 결제와 관련된 정보는 발송됩니다.</span>
                    </li>
                    <li>
                        <p>※ 선택 항목으로 동의하지 않아도 불이익을 받지 않습니다.</p>
                        <p>※ 만 14세 미만은 회원가입 및 서비스 이용이 불가합니다.</p>
                    </li>
                </ul>
                <button>회원가입하기</button>
            </section>
        </div>
        </>
    );
}



