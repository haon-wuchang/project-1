import React from "react";
import { useNavigate } from "react-router-dom";

export default function OrderCertify() {
    const navigate = useNavigate();

    const handleGuestAuth = async (event) => {
        event.preventDefault(); // 기본 링크 동작 방지

        try {
            // `guest_token_`으로 시작하는 토큰 생성
            const guestToken = `guest_token_${Math.random().toString(36)}`;

            // 로컬스토리지에 토큰 저장
            localStorage.setItem("token", guestToken);
            console.log("비회원 인증 성공 - 발행된 토큰:", guestToken);

            // 페이지 새로고침하여 토큰 반영
            window.location.reload();
            
        } catch (error) {
            console.error("비회원 인증 실패:", error);
        }
    };

    return (
        <div id="auth_layer" className="confirm_wrap">
            <h4>본인인증</h4>
            <p className="txt authnotice">
                비회원 구매시 개인정보 보호를 위한 이용자 동의사항에 동의 후 본인인증이 필요합니다.
            </p>
            <div className="certify">
                <a href="#" id="authMobile" className="mobile hp" onClick={handleGuestAuth}>
                    <span>휴대폰 인증</span>
                </a>
            </div>
        </div>
    );
}
