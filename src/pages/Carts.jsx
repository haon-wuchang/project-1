export default function Carts(){
    return (
        <section id="main" className="content-wrap content-wrap-padding">
            <h1>장바구니</h1>   
            <section className="carts-wrap">
                <div className="tabs carts">
                        <ul className="tab">
                            <li>
                                <a href="#tab1" className="on">회원</a>
                            </li>
                            <li>
                                <a href="#tab2" id="noneLogin" >비회원(주문조회)</a>
                            </li>
                            <li>
                                <a href="#tab2" id="noneLogin" >비회원(주문조회)</a>
                            </li>
                            <li>
                                <a href="#tab2" id="noneLogin" >비회원(주문조회)</a>
                            </li>
                        </ul>
                        
                        <div className="order_wrap on all-group">
                            <div className="order_set order_set_head">
                                {/* <p class="null">장바구니에 담긴 상품이 없습니다.</p> */}
                                
                                <table>
                                    <thead>
                                        <tr>
                                            <th style={{textAlign:"left"}}>
                                                <label><input type="checkbox" className="all-check" name="cartAllCheckbox" 
                                                id="cartAllCheckbox0"/><i></i><span>전체선택</span></label>
                                            </th>
                                            <th className="submit">
                                                <a href="#" className="btn" >선택 상품 삭제</a>
                                            </th>
                                        </tr>
                                    </thead>
                                </table>
                            </div>
                            <div className="order_set" id="cartSubGroup1">
                                <table>
                                    {/* <caption>장바구니 일반배송</caption> */}
                                    <colgroup>
                                        <col width="40"></col>
                                        <col width="124"></col>
                                        <col width="*"></col>
                                        <col width="180"></col>
                                        <col width="220"></col>
			                        </colgroup>
                                    <thead>
                                        <tr className="thead">
                                            <th colspan="3" scope="col">상품·혜택 정보</th>
                                            <th scope="col">배송정보</th>
                                            <th scope="col">주문금액</th>
                                        </tr>
			                        </thead>
                                    <tbody>

                                        <tr id="row1">
                                            <td>
                                                <label title="[三無衣服] 스트레치 방한 슬랙스 - 네이비 선택">
                                                    <input type="checkbox" name="check" id="1" /><i></i>
                                                </label>
                                            </td>

                                            <td>
                                                <a className="list_goods" href="#">
                                                    <img src="https://img.ssfshop.com/cmd/RB_100x132/src/https://img.ssfshop.com/goods/HMBR/24/09/04/GM0024090410257_0_THNAIL_ORGINL_20240920105654348.jpg"
                                                     onerror="javascript:this.src='/v3/images/common/noImg_60.gif'" alt=""/>
                                                    <div className="keep">
                                                        <span view-godno="GM0024090410257" view-godturn="1" className="heart on">
                                                            <input type="radio" className="dummy on" title="찜하기"/>
                                                        </span>
                                                    </div>
                                                </a>
                                            </td>

                                            <td style={{textAlign:"left"}}>
                                                <div className="badge">
                                                </div>

                                                <div className="info">
                                                    <span className="brand">GALAXY LIFESTYLE</span>

                                                    <span className="name">
                                                        <a href="#">[三無衣服] 스트레치 방한 슬랙스 - 네이비</a>
                                                    </span>

                                                    <div className="selected_options">
                                                        <ul>
                                                            <li>
                                                                남색 / 096 / 2개
                                                            </li>
                                                        </ul>
                                                    </div>

                                                    <div className="benefits">
                                                        {/* <!-- #137759 [21년 2분기] 사은품 행사 셀링 강화 --> */}
                                                    </div>
                                                        <div className="alter">
                                                            <a href="#" className="btn ">옵션/수량 변경</a>

                                                        </div>
                                                    </div>
                                            </td>

                                            <td>
                                                <div className="shipping">
                                                        <span className="cost" id="dlvCostView1">무료배송</span>
                                                        <span></span>
                                                </div>
                                            </td>

                                            <td>
                                                <a href="#" className="delete">삭제</a>
                                                <div className="price">
                                                        <del>278,000원</del>
                                                        <span>
                                                            166,800원
                                                            <em>40%</em>
                                                        </span>
                                                </div>
                                                <div className="fulfill">
                                                        <a href="#" className="btn bk">바로구매</a>
                                                </div>
                                            </td>
                                        </tr>

                                    </tbody>
                                </table> 
                                {/* table을 컴포넌트로 */}
                                <div className="gray_box">
				                    <h5>스토어 주문금액 합계</h5>
                                    <p>
                                        <span className="accounts">
                                            상품금액 <em id="sub_totalGodAmt">278,000</em>원
                                            &nbsp;&nbsp;+&nbsp;&nbsp;
                                            배송비 <em id="sub_totalDlvAmt">0원</em>
                                            &nbsp;&nbsp;-&nbsp;&nbsp;
                                            <em className="cssf">할인금액 <em id="sub_totalDcAmt">111,200</em>원</em>
                                        </span>
                                        <span className="price">
                                            <em id="sub_totalOrdAmt">166,800</em>원
                                            <span className="shipping_cost" id="subDlvCostPlcInfo4698">39,900원 이상 무료배송</span>
                                        </span>
                                    </p>
                                    {/* <!-- #137759 [21년 2분기] 사은품 행사 셀링 강화 --> */}
                                    <p className="appendix-box" id="subGiftPrm1" name="subGiftPrm1" style={{"display": "none"}}><span>특별혜택</span>
                                        {/* <!-- <a href="javascript:void(0)">null url</a> --></p> */}
                                    {/* <!-- #137759 [21년 2분기] 사은품 행사 셀링 강화 --> */}
                                    </p>
                                </div>
                            </div>

                            <div className="bill" id="cartGroupBill0">
                                <h4>결제 예정 금액 <small>총 <em class="cssf" id="orderCntTxt">1</em>건</small></h4>
                                <div className="calc">
                                    <span className="retail"><em id="totalGodAmt">278,000</em>원<i>상품금액</i></span>
                                    <span className="plus">
                                        <em id="totalDlvAmt">0</em>원
                                        <i>배송비</i></span>
                                    <span className="minus"><em id="totalDcAmt">111,200</em>원<i>할인금액</i></span>
                                    <span className="total"><em id="totalOrdAmt">166,800</em>원<i>총 주문금액</i></span>
                                </div>
                                <div className="submit_order">
                                    <a className="btn bk" href="#">주문하기</a>
                                </div>
                                <section id="memberloginLayer" class="layerNotice">
                                    <h1 class="center">회원만 구매 가능한 상품입니다.<br></br>로그인 후 구매해주세요.</h1>
                                    <div class="btns">
                                        <button class="btn bk" onclick="closeLayer('.layerNotice')">확인</button>
                                    </div>
                                </section>
                            </div>
                            <ul id="cartInfoMessage">
                                    <li>장바구니에 담긴 상품은 30일간 저장됩니다.</li>
                                    <li>SSF SHOP은 자사/입점사 제품별, 주문유형별 배송비 기준에 따라 배송비가 별도 부과됩니다.</li>
                                    <li>SSF SHOP은 동일 고객(ID기준)의 배송지가 일치하는 여러 건의 주문이 있을 경우, 에코 프렌들리 정책 따른 친환경 소비를 위해 출고일을 기준으로<br></br>
                                        자사 상품에 한해 합배송 서비스를 제공합니다. (일부 예외 브랜드 제외)<br></br>
                                        만약 합배송 되어 상품을 수령하셨을 경우, 모든 주문이 배송완료된 후 결제한 배송비를 재계산하여 익일에 퍼플코인으로 돌려드립니다.<br></br>
                                        (단, 무료배송 쿠폰으로 결제한 배송비는 페이백 대상에서 제외)
                                    </li>
                            </ul>
                            
                        </div>    
                </div>


               
            </section>

        </section>
    );
}