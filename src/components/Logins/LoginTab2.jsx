import React, { useState, useRef } from "react";
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import { useContext } from "react";
import { AuthContext } from "../../auth/AuthContext.js";
import axios from "axios";

export default function LoginTab2({ isActive }) {

    const { isLoggedIn, setIsLoggedIn } = useContext(AuthContext);
    const navigate = useNavigate();

  const [formData, setFormData] = useState({
    guestNm: "",
    mobileNo: "",
    ordNo: "",
  });

  const refs = {
    guestNmRef: useRef(null),
    mobileNoRef: useRef(null),
    ordNoRef: useRef(null),
  };

  const handleChangeForm = (event) => {
    const { name, value } = event.target;
    if (name === "mobileNo") {
      // 입력된 값에서 숫자가 아닌 문자를 제거하여 숫자만 남김
      const cleaned = value.replace(/\D/g, "");
      // 상태(formData) 업데이트 - 숫자만 유지됨
      setFormData({ ...formData, [name]: cleaned });
    } else if (name === "ordNo") {
      // 주문번호는 숫자와 영어만 허용
      const cleaned = value.replace(/[^a-zA-Z0-9]/g, "");
      setFormData({ ...formData, [name]: cleaned });
    } else {
      // 다른 입력 필드는 그대로 값 저장
      setFormData({ ...formData, [name]: value });
    }
    // 콘솔에 현재 입력 필드의 값 출력
    console.log(`${name}: ${value}`);
  };

  const handleGuestLogin = (e) => {
    e.preventDefault();

    // 숫자가 아닌 값이 포함되어 있으면 알림을 띄우고 제출 중지
    if (/\D/.test(formData.mobileNo)) {
        alert("숫자만 입력하시오.");
        return;
    }

    axios.post('http://localhost:9000/user/guestLogin', formData)
        .then(res => {
            console.log('res.data --> ', res.data);

            if (res.data.result_rows === 1) {
                alert('비회원 로그인 성공!');
                localStorage.setItem("token", res.data.token);
                setIsLoggedIn(true);
                navigate('/');
            } else {
                alert("일치하는 주문조회가 없습니다. 다시 입력해주세요.");
            }
        })
        .catch(err => {
            console.error("API 요청 실패:", err);
            alert("서버 오류가 발생했습니다. 다시 시도해주세요.");
        });
};


  
  return (
    <div id="tab2" className={isActive ? "on" : ""}>
      <h3 className="wa-hidden">비회원(주문조회) 입력</h3>
      <form onSubmit={handleGuestLogin}>
        <div className="signIn-form" style={{ backgroundColor: "yellowgreen" }}>
          <div>
            <div className="input-box">
              <label htmlFor="guestNm" className="wa-hidden">이름</label>
              <input
                name="guestNm"
                id="guestNm"
                type="text"
                placeholder="이름"
                ref={refs.guestNmRef}
                onChange={handleChangeForm}
              />
            </div>
            <div className="input-box">
              <label htmlFor="mobileNo" className="wa-hidden">휴대폰 번호</label>
              <input
                type="text"
                name="mobileNo"
                id="mobileNo"
                maxLength="11"
                placeholder="휴대폰 번호(‘-’ 없이 입력)"
                ref={refs.mobileNoRef}
                onChange={handleChangeForm}
                value={formData.mobileNo}
              />
            </div>
            <div className="input-box">
              <label htmlFor="ordNo" className="wa-hidden">주문번호</label>
              <input
                type="text"
                name="ordNo"
                id="ordNo"
                placeholder="주문번호"
                ref={refs.ordNoRef}
                onChange={handleChangeForm}
                value={formData.ordNo}
              />
            </div>
          </div>
          <button type="submit">주문/배송조회</button>
        </div>
        <p id="nonMemberPwarn" className="invalid-txt"></p>
        <div className="center_info">
          <span>1599-0007</span>
          평일(월~금)<strong> 09:00~18:00</strong> (주말 및 공휴일 휴무)
        </div>
      </form>
    </div>
  );
}

    // // 가상의 주문 데이터 (실제 서버와 연결하려면 API 호출 필요)
    // const existingOrders = [
    //     { guestNm: "홍길동", mobileNo: "01012345678", ordNo: "ORD12345" },
    //     { guestNm: "김철수", mobileNo: "01087654321", ordNo: "ORD67890" },
    //     { guestNm: "이영희", mobileNo: "01011223344", ordNo: "ORD54321" }
    //   ];
      
    //   // 이름, 번호, 주문번호가 일치하는지 확인
    //   const match = existingOrders.find(order => 
    //     order.guestNm === formData.guestNm && 
    //     order.mobileNo === formData.mobileNo && 
    //     order.ordNo === formData.ordNo
    //   );