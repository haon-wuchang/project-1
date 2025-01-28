export default function Login(){
    return (
        <>
        <section id="main" className="content-wrap content-wrap-padding">
            <h1>로그인</h1>
            <section className="login-wrap ">
                <div className="tabs logins">
                    <div>
                        
                    </div>
                    <ul className="tab">
                        <li>
                            <a href="#tab1" className="on">회원</a>
                        </li>
                        <li>
                            <a href="#tab2" id="noneLogin" >비회원(주문조회)</a>
                        </li>
                    </ul>
                    <div id="tab1" className="on">
                        {/* <h1>회원정보 입력</h1> */}
                        <form action="">
                            <div className="signIn-form">
                                <div>

                                    <div className="input-box">
                                        <label for="userId" className="wa-hidden">아이디</label>
                                        <input type="text" id="userId" name="userId" validate="required;xss2;" 
                                        locale="ko" placeholder="아이디" className="reset" title="아이디"/>
                                    </div>

                                    <div className="input-box">
                                        <label for="password" className="wa-hidden">비밀번호</label>
                                        <input type="password" maxlength="20" name="password" id="password"
                                         validate="required" locale="ko" placeholder="비밀번호" title="비밀번호"/>
                                    </div>

                                </div>
                                <button type="button">로그인</button>
                            </div>

                            <div className="save_id">
                                <span className="checkbox">
                                    <input className="checkBox" type="checkbox" id="cb01" name="saveId"/>
                                    <label for="cb01"><i></i>아이디 저장</label>
                                </span>
                            </div>
                        </form>
                        <div className="link">
                            <a href="#">아이디 찾기</a>
                            <a href="#">비밀번호 찾기</a>
                            <a href="#" className="colorDark">회원가입</a>
                        </div>

                        <dl className="login_sns">
                                <dt><span>SNS 계정으로 로그인</span></dt>
                                <dd>
                                    <a href="#" id="oLoginKaKaoLink" className="kakao box" title="새창열림">카카오 로그인</a>
                                    <a href="#" className="naver box" title="새창열림">네이버 로그인</a>
                                </dd>
                        </dl>
                    </div>
                    
                    <div id="tab2" class="">
        	            <h3 class="wa-hidden">비회원(주문조회) 입력</h3>
                        <form action="" method="post" id="nonMemberForm">
                            <input type="hidden" name="_csrf" value="aac16e3e-027a-4a43-be9d-b7d7af254ea4"/>
                            <div className="signIn-form">
                                <div>
                                    <div class="input-box">
                                        <span class="skills">
                                            <i class="reset_txt"></i>
                                        </span>
                                        <label for="cstmrNm" class="wa-hidden">이름</label>
                                        <input name="cstmrNm" id="cstmrNm" value="" validate="required" type="text" 
                                        label="이름" placeholder="이름" class="reset" title="이름"/>
                                    </div>
                                    <div class="input-box">
                                        <span class="skills">
                                            <i class="reset_txt"></i>
                                        </span>
                                        <label for="cstmrMobilNo" class="wa-hidden">휴대폰 번호</label>
                                        <input type="text" name="cstmrMobilNo" id="cstmrMobilNo" value=""
                                        label="휴대폰 번호" validate="required;digit;minlength:10;" maxlength="11" 
                                        placeholder="휴대폰 번호(‘-’ 없이 입력)" title="휴대폰 번호(‘-’ 없이 입력)"/>
                                    </div>
                                    <div class="input-box">
                                        <span class="skills">
                                            <i class="reset_txt"></i>
                                        </span>
                                        <label for="ordNo" class="wa-hidden">주문번호</label>
                                        <input type="text" class="inp_txt" name="ordNo" id="ordNo" value="" 
                                        validate="required" label="주문번호" placeholder="주문번호" title="주문번호"/>
                                    </div>
                                </div>
                                <button type="button" >주문/배송조회</button>
                            </div>
                            <p id="nonMemberPwarn" class="invalid-txt"></p>
                                <div class="center_info">
                                    <span>1599-0007</span>
                                    평일(월~금)<strong> 09:00~18:00</strong> (주말 및 공휴일 휴무)
                            </div>
                        </form>
                    </div>        
                </div>
            </section>
        </section>

        </>
    );
}