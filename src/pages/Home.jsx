import SectionWrap from "../components/SectionWrap.jsx";
import Events from "../components/Events.jsx";
import Brand from "../components/Brand.jsx";
import Outer from "../components/Outer.jsx";
import Rank from "../components/Rank.jsx";
import Issue from "../components/Issue.jsx";
export default function Home(){

    const sectionList = [
        {
          id: "event",
          title: "이벤트",
        },
        {
          id: "outer",
          title: "아우터로 더하는 한 겹의 포근함",
        },
        {
          id: "rank",
          title: "랭킹",
        },
        {
          id: "brands",
          title: "주목할 브랜드",
        },
        {
          id: "issue",
          title: "이 주의 브랜드 이슈",
        },
      ];
      
      const componentMap = {
        event: Events,
        outer: Outer,
        rank: Rank,
        brands: Brand,
        issue: Issue,
      };
      
      const renderComponent = (childObj) => {
        const Component = componentMap[childObj.id];
        if (!Component) return null;
      
        return (
          <Component
            key={childObj.id}
            {...(childObj.props || {})} // Spread `props` if they exist
          >
            {/* Children rendering can be omitted since children key is unused */}
          </Component>
        );
      };
      
    return (
<main id='content'>
  <div className="key-visual">
    <div className="swiper swiper-initialized swiper-horizontal swiper-pointer-events swiper-watch-progress" data-component="[object Object]">
      <div className="swiper-wrapper" id="swiper-wrapper-816f92e3f693e1c3" aria-live="off"
                  style={{"transition-duration": "0ms", "transform": "translate3d(-3372px, 0px, 0px)"}}>
                    
          <div className="swiper-slide"
                style={{"width": "1686px"}}>
            <div className="slide-lists">
                <div className="slide-item">
                      {/* <!-- case1: 3분할 1세트 --> */}
                  <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트10(28~30)','151','/special/101010/view');javascript:location.href='/special/101010/view?utag=ref_tpl:111942$ref_cnr:23357$set:1$dpos:1';">
                      <div className="brand-info-area">
                          <p className="brand-name">TORY BURCH</p>
                          <p className="brand-tit">더할 나위 없이<br/>더 누리는 할인</p>
                          <p className="brand-desc">인기 상품 품절 임박 ~50%</p>
                      </div>
                      <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345843_151_KOR_20250124113317.jpg"/>
                  </a>
                </div>
                <div className="slide-item">
                    {/* <!-- case1: 3분할 1세트 --> */}
                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트10(28~30)','161','/special/103142/view');javascript:location.href='/special/103142/view?utag=ref_tpl:111942$ref_cnr:23357$set:2$dpos:1';">
                      <div className="brand-info-area">
                          <p className="brand-name">FORMEL CAMELE</p>
                          <p className="brand-tit">닳지 않는 사랑스러움</p>
                          <p className="brand-desc">포멜카멜레 론칭 기념 ~58% + 사은품</p>
                      </div>
                      <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345843_161_KOR_20250124113353.jpg"/>
                    </a>
                </div>
                <div className="slide-item">
                    {/* <!-- case1: 3분할 1세트 --> */}
                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트10(28~30)','157','/special/103158/view');javascript:location.href='/special/103158/view?utag=ref_tpl:111942$ref_cnr:23357$set:3$dpos:1';">
                      <div className="brand-info-area">
                          <p className="brand-name">SAND SOUND</p>
                          <p className="brand-tit">미리 보는 봄의 소리</p>
                          <p className="brand-desc">샌드사운드 25 S/S PRE-DROP</p>
                      </div>
                      <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345843_157_KOR_20250110115831.jpg"/>
                    </a>
                </div>
              </div>
          </div>

            <div className="swiper-slide" style={{"width": "1686px"}}>
                <div className="slide-lists">
                        <div className="slide-item">
                            {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트1(1~3)','196','/event/EV202501020146327/view');javascript:location.href='/event/EV202501020146327/view?utag=ref_tpl:111942$ref_cnr:23357$set:1$dpos:1';">
                                                <div className="brand-info-area">
                                                    </div>
                                                <img src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345842_196_KOR_20250117112951.jpg"/>
                                                </a>
                                        </div>
                                    <div className="slide-item">
                                        {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트1(1~3)','201','/event/EV202501130146509/view');javascript:location.href='/event/EV202501130146509/view?utag=ref_tpl:111942$ref_cnr:23357$set:2$dpos:1';">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">EVENT</p>
                                                    <p className="brand-tit">다시, 새롭게<br/>할인의 축제</p>
                                                    <p className="brand-desc">아울렛 슈퍼위크 ~92% + 추가 2종 쿠폰</p>
                                                    </div>
                                                <img src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345842_201_KOR_20250117114230.jpg"/>
                                                </a>
                                        </div>
                                    <div className="slide-item">	
                                      {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트1(1~3)','193','/special/103324/view');javascript:location.href='/special/103324/view?utag=ref_tpl:111942$ref_cnr:23357$set:3$dpos:1';">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">BEAKER</p>
                                                    <p className="brand-tit">누구든지<br/>취향 저격</p>
                                                    <p className="brand-desc">초콜릿부터 에코백까지<br/>선물 지원 10% 쿠폰으로 마음을 전하세요</p>
                                                    </div>
                                                <img src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345842_193_KOR_20250124105839.jpg"/>
                                                </a>
                                        </div>
                                    </div>
                </div>
            <div className="swiper-slide"
              style={{"width": "1686px"}}>
                <div className="slide-lists">
                        <div className="slide-item">
                            {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트2(4-6)','168','/special/91014/view');javascript:location.href='/special/91014/view?utag=ref_tpl:111942$ref_cnr:23357$set:1$dpos:1';">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">THEORY</p>
                                                    <p className="brand-tit">행운처럼 다가온<br/>스페셜 오퍼</p>
                                                    <p className="brand-desc">설 한정 특가<br/>23 F/W 아울렛 최대 60%</p>
                                                    </div>
                                                <img src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345836_168_KOR_20250124110027.jpg"/>
                                                </a>
                                        </div>
                                    <div className="slide-item">	
                                      {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트2(4-6)','170','/special/103054/view');javascript:location.href='/special/103054/view?utag=ref_tpl:111942$ref_cnr:23357$set:2$dpos:1';">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">8 SECONDS</p>
                                                    <p className="brand-tit">팔초빅데이</p>
                                                    <p className="brand-desc">이월 상품 최대 70%</p>
                                                    </div>
                                                <img src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345836_170_KOR_20250124110209.jpg"/>
                                                </a>
                                        </div>
                                    <div className="slide-item">
                                        {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트2(4-6)','169','/special/101154/view');javascript:location.href='/special/101154/view?utag=ref_tpl:111942$ref_cnr:23357$set:3$dpos:1';">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">MLB</p>
                                                    <p className="brand-tit">유용하고 편안한<br/>데일리 라인업</p>
                                                    <p className="brand-desc">MLB 베이직 라인 론칭 <br/>최대 60% + 사은품 증정</p>
                                                    </div>
                                                <img src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345836_169_KOR_20250124110245.jpg"/>
                                                </a>
                                        </div>
                                    </div>
                </div>
            <div className="swiper-slide" style={{"width": "1686px"}}>
                <div className="slide-lists">
                        <div className="slide-item">
                            {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트3(7~9)','3','/special/92060/view');javascript:location.href='/special/92060/view?utag=ref_tpl:111942$ref_cnr:23357$set:1$dpos:1';">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">CDGCDGCDG</p>
                                                    <p className="brand-tit">새 계절<br/>벌써 개시</p>
                                                    <p className="brand-desc">아우터, 후드, 백팩 등<br/>신상 출시</p>
                                                    </div>
                                                <img src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_409446_3_KOR_20250124110403.jpg"/>
                                                </a>
                                        </div>
                                    <div className="slide-item">	
                                      {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트3(7~9)','2','/special/103191/view');javascript:location.href='/special/103191/view?utag=ref_tpl:111942$ref_cnr:23357$set:2$dpos:1';">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">KODAK &amp; LEVI'S 외</p>
                                                    <p className="brand-tit">멋을 품은 설 <br/>선물이 될 혜택</p>
                                                    <p className="brand-desc">코닥, 리바이스 등 <br/>매일 쿠폰팩 + 인기 상품 특가</p>
                                                    </div>
                                                <img src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_409446_2_KOR_20250124110501.jpg"/>
                                                </a>
                                        </div>
                                    <div className="slide-item">
                                        {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트3(7~9)','8','/special/95788/view');javascript:location.href='/special/95788/view?utag=ref_tpl:111942$ref_cnr:23357$set:3$dpos:1';">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">WOMEN</p>
                                                    <p className="brand-tit">추위는 아직 한창</p>
                                                    <p className="brand-desc">더엣지, 셀렙샵 등 베스트 아이템 ~80% 특가</p>
                                                    </div>
                                                <img src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_409446_8_KOR_20250124110539.jpg"/>
                                                </a>
                                        </div>
                                    </div>
                </div>
            <div className="swiper-slide" style={{"width": "1686px"}}>
                <div className="slide-lists">
                        <div className="slide-item">
                            {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트4(10~12)','158','/special/103265/view');javascript:location.href='/special/103265/view?utag=ref_tpl:111942$ref_cnr:23357$set:1$dpos:1';">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">ANOTHER#</p>
                                                    <p className="brand-tit">사랑 받는 이유</p>
                                                    <p className="brand-desc">안살 이유 없는 단독 할인<br/>15% 쿠폰 추가 할인까지</p>
                                                    </div>
                                                <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345840_158_KOR_20250124110759.jpg"/>
                                                </a>
                                        </div>
                                    <div className="slide-item">
                                        {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트4(10~12)','150','/special/103481/view');javascript:location.href='/special/103481/view?utag=ref_tpl:111942$ref_cnr:23357$set:2$dpos:1';">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">ANOTHER#</p>
                                                    <p className="brand-tit">일상을 특별하게 해줄</p>
                                                    <p className="brand-desc">눈부신 포인트 룩 최대 64%</p>
                                                    </div>
                                                <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345840_150_KOR_20250124110846.jpg"/>
                                                </a>
                                        </div>
                                    <div className="slide-item">
                                        {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트4(10~12)','151','/special/102806/view');javascript:location.href='/special/102806/view?utag=ref_tpl:111942$ref_cnr:23357$set:3$dpos:1';">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">BEANPOLE</p>
                                                    <p className="brand-tit">설렘으로 물들고<br/>마음까지 채우는</p>
                                                    <p className="brand-desc">명절 기프트 제안서<br/>랜덤 쿠폰 등 설 맞이 풍성한 혜택</p>
                                                    </div>
                                                <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345840_151_KOR_20250124111056.jpg"/>
                                                </a>
                                        </div>
                                    </div>
                </div>
            <div className="swiper-slide" style={{"width": "1686px"}}>
                <div className="slide-lists">
                        <div className="slide-item">
                            {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트5(13~15)','163','/special/103164/view');javascript:location.href='/special/103164/view?utag=ref_tpl:111942$ref_cnr:23357$set:1$dpos:1';">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">KUHO PLUS</p>
                                                    <p className="brand-tit">다가올 봄날</p>
                                                    <p className="brand-desc">설레는 봄맞이 스타일링</p>
                                                    </div>
                                                <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345837_163_KOR_20250124111213.jpg"/>
                                                </a>
                                        </div>
                                    <div className="slide-item">
                                        {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트5(13~15)','161','/special/102528/view');javascript:location.href='/special/102528/view?utag=ref_tpl:111942$ref_cnr:23357$set:2$dpos:1';">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">MEN</p>
                                                    <p className="brand-tit">다시 만나는<br/>위시리스트</p>
                                                    <p className="brand-desc">시프트지, 갤럭시, 로가디스 등<br/>클리어런스 최대 70%</p>
                                                    </div>
                                                <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345837_161_KOR_20250124111310.jpg"/>
                                                </a>
                                        </div>
                                    <div className="slide-item">
                                        {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트5(13~15)','164','/special/103341/view');javascript:location.href='/special/103341/view?utag=ref_tpl:111942$ref_cnr:23357$set:3$dpos:1';">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">BEAKER ORIGINAL</p>
                                                    <p className="brand-tit">입어볼까, 신상</p>
                                                    <p className="brand-desc">언제나 편안하고, 세련되게<br/>비이커 감성으로 재해석한 에센셜 아이템</p>
                                                    </div>
                                                <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345837_164_KOR_20250124111402.jpg"/>
                                                </a>
                                        </div>
                                    </div>
                </div>
            <div className="swiper-slide" style={{"width": "1686px"}}>
                <div className="slide-lists">
                        <div className="slide-item">
                            {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트6(16~18)','172','/special/103490/view');javascript:location.href='/special/103490/view?utag=ref_tpl:111942$ref_cnr:23357$set:1$dpos:1';">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">DESCENTE</p>
                                                    <p className="brand-tit">소중한 시작을<br/>함께해요</p>
                                                    <p className="brand-desc">인플루언서가 착용한 <br/>데상트 신상 백팩 &amp; 슈즈</p>
                                                    </div>
                                                <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345838_172_KOR_20250124111854.jpg"/>
                                                </a>
                                        </div>
                                    <div className="slide-item">
                                        {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트6(16~18)','174','/special/103237/view');javascript:location.href='/special/103237/view?utag=ref_tpl:111942$ref_cnr:23357$set:2$dpos:1';">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">POLO &amp; CHAMPION 외</p>
                                                    <p className="brand-tit">가치 있는 편안함<br/>여기서만 특가</p>
                                                    <p className="brand-desc">폴로, 챔피언 등 오직 SSF샵에서만<br/>기간 한정 단독 특가 + 추가 할인</p>
                                                    </div>
                                                <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345838_174_KOR_20250124112013.jpg"/>
                                                </a>
                                        </div>
                                    <div className="slide-item">
                                        {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트6(16~18)','168','/special/102863/view');javascript:location.href='/special/102863/view?utag=ref_tpl:111942$ref_cnr:23357$set:3$dpos:1';">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">KUHO</p>
                                                    <p className="brand-tit">블랙으로 설계한<br/>새로운 계절</p>
                                                    <p className="brand-desc">25 S/S New Collection</p>
                                                    </div>
                                                <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345838_168_KOR_20250124112050.jpg"/>
                                                </a>
                                        </div>
                                    </div>
                </div>
            <div className="swiper-slide" style={{"width": "1686px"}}>
                <div className="slide-lists">
                        <div className="slide-item">
                            {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트7(19~21)','195','/special/103154/view');javascript:location.href='/special/103154/view?utag=ref_tpl:111942$ref_cnr:23357$set:1$dpos:1';">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">LEMAIRE</p>
                                                    <p className="brand-tit">본연의 모습을<br/>더욱 돋보이게 할</p>
                                                    <p className="brand-desc">25 S/S 신규 컬렉션 출시</p>
                                                    </div>
                                                <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345835_195_KOR_20250124112252.jpg"/>
                                                </a>
                                        </div>
                                    <div className="slide-item">
                                        {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트7(19~21)','217','/special/102567/view');javascript:location.href='/special/102567/view?utag=ref_tpl:111942$ref_cnr:23357$set:2$dpos:1';">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">AMI</p>
                                                    <p className="brand-tit">봄에도 함께할 <br/>마지막 겨울 찬스</p>
                                                    <p className="brand-desc">시즌오프 ~30 + 10% 쿠폰</p>
                                                    </div>
                                                <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345835_217_KOR_20250124112332.jpg"/>
                                                </a>
                                        </div>
                                    <div className="slide-item">
                                        {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트7(19~21)','218','/special/103333/view');javascript:location.href='/special/103333/view?utag=ref_tpl:111942$ref_cnr:23357$set:3$dpos:1';">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">SHOES</p>
                                                    <p className="brand-tit">새로운 순간을<br/>아름답게 딛는 법</p>
                                                    <p className="brand-desc">부츠, 구두 등 단독 할인</p>
                                                    </div>
                                                <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345835_218_KOR_20250124112417.jpg"/>
                                                </a>
                                        </div>
                                    </div>
                </div>
            <div className="swiper-slide" style={{"width": "1686px"}}>
                <div className="slide-lists">
                        <div className="slide-item">
                            {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트8(22-24)','153','/special/103168/view');javascript:location.href='/special/103168/view?utag=ref_tpl:111942$ref_cnr:23357$set:1$dpos:1';">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">LEBEIGE</p>
                                                    <p className="brand-tit">밀도 있는 삶</p>
                                                    <p className="brand-desc">2025 Jan. LEFINE</p>
                                                    </div>
                                                <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345839_153_KOR_20250124112557.jpg"/>
                                                </a>
                                        </div>
                                    <div className="slide-item">
                                        {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트8(22-24)','162','/special/103402/view');javascript:location.href='/special/103402/view?utag=ref_tpl:111942$ref_cnr:23357$set:2$dpos:1';">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">SONGZIO &amp; PYRENEX </p>
                                                    <p className="brand-tit">겨울 속<br/>피어난 봄</p>
                                                    <p className="brand-desc">다가온 봄을 위한 <br/>간절기 아우터 최대 84%</p>
                                                    </div>
                                                <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345839_162_KOR_20250124112845.jpg"/>
                                                </a>
                                        </div>
                                    <div className="slide-item">
                                        {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트8(22-24)','158','/special/103409/view');javascript:location.href='/special/103409/view?utag=ref_tpl:111942$ref_cnr:23357$set:3$dpos:1';">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">GENERAL IDEA</p>
                                                    <p className="brand-tit">황금연휴 반짝세일, <br/>봄맞이 아이디어</p>
                                                    <p className="brand-desc">제너럴아이디어 연휴 특가 <br/>~63 + 10% 혜택</p>
                                                    </div>
                                                <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345839_158_KOR_20250124112926.jpg"/>
                                                </a>
                                        </div>
                                    </div>
                </div>
            <div className="swiper-slide" style={{"width": "1686px"}}>
                <div className="slide-lists">
                        <div className="slide-item">
                            {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트9(25~27)','167','/special/102293/view');javascript:location.href='/special/102293/view?utag=ref_tpl:111942$ref_cnr:23357$set:1$dpos:1';">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">BEANPOLE</p>
                                                    <p className="brand-tit">마지막 혜택에<br/>응답할 차례</p>
                                                    <p className="brand-desc">아울렛 클리어런스 최대 64%</p>
                                                    </div>
                                                <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345844_167_KOR_20250124113039.jpg"/>
                                                </a>
                                        </div>
                                    <div className="slide-item">
                                        {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트9(25~27)','168','/special/100873/view');javascript:location.href='/special/100873/view?utag=ref_tpl:111942$ref_cnr:23357$set:2$dpos:1';">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">ANOTHER#</p>
                                                    <p className="brand-tit">감각의 시대</p>
                                                    <p className="brand-desc">인기 브랜드의 시즌오프 ~92%<br/>로르서울·두낫플랜·미바이와이</p>
                                                    </div>
                                                <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345844_168_KOR_20250124113227.jpg"/>
                                                </a>
                                        </div>
                                    <div className="slide-item">	
                                      {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="javascript:undefined;" onclick="cnrClickLoging('23357','세트9(25~27)','170','/special/103233/view');javascript:location.href='/special/103233/view?utag=ref_tpl:111942$ref_cnr:23357$set:3$dpos:1';">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">THE APERTURE</p>
                                                    <p className="brand-tit">Aperture's <br/>Favorite 1970s</p>
                                                    <p className="brand-desc">25 Spring 1st Drop</p>
                                                    </div>
                                                <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345844_170_KOR_20250124113143.jpg"/>
                                                </a>
                                        </div>
                                    </div>
                </div>
            <div className="swiper-slide" style={{"width": "1686px"}}>
                <div className="slide-lists">
                        <div className="slide-item">	
                          {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="#">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">TORY BURCH</p>
                                                    <p className="brand-tit">더할 나위 없이<br/>더 누리는 할인</p>
                                                    <p className="brand-desc">인기 상품 품절 임박 ~50%</p>
                                                    </div>
                                                <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345843_151_KOR_20250124113317.jpg"/>
                                                </a>
                                        </div>
                                    <div className="slide-item">
                                        {/* <!-- case1: 3분할 1세트 --> */}
                                        <a href="#">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">FORMEL CAMELE</p>
                                                    <p className="brand-tit">닳지 않는 사랑스러움</p>
                                                    <p className="brand-desc">포멜카멜레 론칭 기념 ~58% + 사은품</p>
                                                    </div>
                                                <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345843_161_KOR_20250124113353.jpg"/>
                                                </a>
                                        </div>
                                    <div className="slide-item">
                                        {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="#">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">SAND SOUND</p>
                                                    <p className="brand-tit">미리 보는 봄의 소리</p>
                                                    <p className="brand-desc">샌드사운드 25 S/S PRE-DROP</p>
                                                    </div>
                                                <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345843_157_KOR_20250110115831.jpg"/>
                                                </a>
                                        </div>
                                    </div>
                </div>
            <div className="swiper-slide" style={{"width": "1686px"}}>
                <div className="slide-lists">
                        <div className="slide-item">
                            {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="#">
                                                <div className="brand-info-area">
                                                    </div>
                                                <img src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345842_196_KOR_20250117112951.jpg"/>
                                                </a>
                                        </div>
                                    <div className="slide-item">
                                        {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="#">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">EVENT</p>
                                                    <p className="brand-tit">다시, 새롭게<br/>할인의 축제</p>
                                                    <p className="brand-desc">아울렛 슈퍼위크 ~92% + 추가 2종 쿠폰</p>
                                                    </div>
                                                <img src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345842_201_KOR_20250117114230.jpg"/>
                                                </a>
                                        </div>
                                    <div className="slide-item">	
                                      {/* <!-- case1: 3분할 1세트 --> */}
                                    <a href="#">
                                                <div className="brand-info-area">
                                                    <p className="brand-name">BEAKER</p>
                                                    <p className="brand-tit">누구든지<br/>취향 저격</p>
                                                    <p className="brand-desc">초콜릿부터 에코백까지<br/>선물 지원 10% 쿠폰으로 마음을 전하세요</p>
                                                    </div>
                                                <img src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23357_345842_193_KOR_20250124105839.jpg"/>
                                                </a>
                                        </div>
                                    </div>
                </div></div>
                
        {/* <div className="swiper-button-prev" tabindex="0" role="button" aria-label="Previous slide" aria-controls="swiper-wrapper-816f92e3f693e1c3"></div>
        <div className="swiper-button-control">
            <div className="swiper-button-next" tabindex="0" role="button" aria-label="Next slide" aria-controls="swiper-wrapper-816f92e3f693e1c3"></div>
            <div className="swiper-button-pause" role="button" aria-label="pause"></div>
        </div> */}
    <span className="swiper-notification" aria-live="assertive" aria-atomic="true"></span></div>
  </div>{/* slide 끝 */}

  {/* 컨텐츠 시작 */}
  <div className='contents content-wrap'>
  <div className="corner-section">
    <section className="our-picks-gods" cnr="23360" id="ourPickOURPICK_AType23360" utag="utag=ref_tpl:111942$ref_cnr:23360">
                <div className="swiper swiper-initialized swiper-horizontal swiper-pointer-events swiper-backface-hidden">
                        <div className="swiper-wrapper" id="swiper-wrapper-17c64f0812c5c608" aria-live="polite">
                            <div className="swiper-slide swiper-slide-active" role="group" aria-label="1 / 8" style={{"width": "692px", "marginRight": "16px"}}>
                                            <div className="gods-area">
                                                <div className="gods-main">
                                                        <a href="/special/102822/view?&amp;utag=ref_tpl:111942$ref_cnr:23360$set:2$dpos:1" onclick="cnrClickLoging('23360','세트 2','1','/special/102822/view');">
                                                            <div className="gods-img">
                                                            <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23360_346911_90_KOR_20250117141038.jpg"/>
                                                            <div className="gods-desc">
                                                                <p className="tit">HAPPY NEW SEASON<br/>2매 이상 구매 시 추가 10%</p> <p className="desc">8 SECONDS</p> </div>
                                                        </div>
                                                        </a>
                                                    </div>

                                                    <div className="gods-list">
                                                            <div className="gods-item" view-godno="GM0024122750066">
                                                                    <a href="javascript:goToProductDetailCorner('8-seconds', 'GM0024122750066', '', 'ourPickOURPICK_AType23360',1,'23360','세트 2');">
                                                                        <div className="gods-img">
                                                                            <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/cmd/LB_220x293/src/https://img.ssfshop.com/goods/8SBR/24/12/27/GM0024122750066_0_THNAIL_ORGINL_20250106110846024.jpg"/>
                                                                        </div>
                                                                        <div className="gods-info">
                                                                            <p className="brand"> 8 seconds</p>
                                                                            <p className="name">부클 버클 숏 자켓 - 블랙</p>
                                                                            <p className="price">
                                                                                <span className="wa_hidden">판매가</span>
                                                                                                        89,900<span className="wa_hidden">원</span>
                                                                                                
                                                                                            </p>
                                                                        </div>
                                                                    </a>
                                                                </div>
                                                            <div className="gods-item" view-godno="GM0024122750054">
                                                                    <a href="javascript:goToProductDetailCorner('8-seconds', 'GM0024122750054', '', 'ourPickOURPICK_AType23360',2,'23360','세트 2');">
                                                                        <div className="gods-img">
                                                                            <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/cmd/LB_220x293/src/https://img.ssfshop.com/goods/8SBR/24/12/27/GM0024122750054_0_THNAIL_ORGINL_20250109143711267.jpg"/>
                                                                        </div>
                                                                        <div className="gods-info">
                                                                            <p className="brand"> 8 seconds</p>
                                                                            <p className="name">하이넥 스트링 패딩 푸퍼 - 아이보리</p>
                                                                            <p className="price">
                                                                                <span className="wa_hidden">판매가</span>
                                                                                                        109,900<span className="wa_hidden">원</span>
                                                                                                
                                                                                            </p>
                                                                        </div>
                                                                    </a>
                                                                </div>
                                                            </div>
                                                    </div>
                                        </div>
                                    <div className="swiper-slide swiper-slide-next" role="group" aria-label="2 / 8" style={{"width": "692px", "marginRight": "16px"}}>
                                            <div className="gods-area">
                                                <div className="gods-main">
                                                        <a href="/special/103140/view?&amp;utag=ref_tpl:111942$ref_cnr:23360$set:2$dpos:1" onclick="cnrClickLoging('23360','세트 1','1','/special/103140/view');">
                                                            <div className="gods-img">
                                                            <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23360_361952_65_KOR_20250124141411.jpg"/>
                                                            <div className="gods-desc">
                                                                <p className="tit">사랑 가득 담은 설맞이 선물<br/>10% 쿠폰 + 신상 5% 함께할인</p> <p className="desc">BEANPOLE</p> </div>
                                                        </div>
                                                        </a>
                                                    </div>

                                                    <div className="gods-list">
                                                            <div className="gods-item" view-godno="GM0024102903194">
                                                                    <a href="javascript:goToProductDetailCorner('BEANPOLE-KIDS', 'GM0024102903194', '', 'ourPickOURPICK_AType23360',1,'23360','세트 1');">
                                                                        <div className="gods-img">
                                                                            <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/cmd/LB_220x293/src/https://img.ssfshop.com/goods/BPBR/24/10/29/GM0024102903194_0_THNAIL_ORGINL_20241128111716323.jpg"/>
                                                                        </div>
                                                                        <div className="gods-info">
                                                                            <p className="brand"> BEANPOLE KIDS</p>
                                                                            <p className="name">블링 사첼 여아 책가방 세트 - 라이트 핑크</p>
                                                                            <p className="price">
                                                                                <del><span className="wa_hidden">원가</span>
                                                                                                    209,000<span className="wa_hidden">원
                                                                                                </span></del>
                                                                                                <em className="sale"><span className="wa_hidden">할인율</span>
                                                                                                    10%</em><span className="wa_hidden">판매가</span>188,100<span className="wa_hidden">원</span>
                                                                                                
                                                                                            </p>
                                                                        </div>
                                                                    </a>
                                                                </div>
                                                            <div className="gods-item" view-godno="GM0024102903196">
                                                                    <a href="javascript:goToProductDetailCorner('BEANPOLE-KIDS', 'GM0024102903196', '', 'ourPickOURPICK_AType23360',2,'23360','세트 1');">
                                                                        <div className="gods-img">
                                                                            <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/cmd/LB_220x293/src/https://img.ssfshop.com/goods/BPBR/24/10/29/GM0024102903196_0_THNAIL_ORGINL_20241118155019516.jpg"/>
                                                                        </div>
                                                                        <div className="gods-info">
                                                                            <p className="brand"> BEANPOLE KIDS</p>
                                                                            <p className="name">[산리오] 마이멜로디 블링 책가방 세트 - 라이트 핑크</p>
                                                                            <p className="price">
                                                                                <del><span className="wa_hidden">원가</span>
                                                                                                    209,000<span className="wa_hidden">원
                                                                                                </span></del>
                                                                                                <em className="sale"><span className="wa_hidden">할인율</span>
                                                                                                    10%</em><span className="wa_hidden">판매가</span>188,100<span className="wa_hidden">원</span>
                                                                                                
                                                                                            </p>
                                                                        </div>
                                                                    </a>
                                                                </div>
                                                            </div>
                                                    </div>
                                        </div>
                                    <div className="swiper-slide" role="group" aria-label="3 / 8" style={{"width": "692px", "marginRight": "16px"}}>
                                            <div className="gods-area">
                                                <div className="gods-main">
                                                        <a href="/special/103471/view?&amp;utag=ref_tpl:111942$ref_cnr:23360$set:2$dpos:1" onclick="cnrClickLoging('23360','세트 4','1','/special/103471/view');">
                                                            <div className="gods-img">
                                                            <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23360_345998_133_KOR_20250124141835.jpg"/>
                                                            <div className="gods-desc">
                                                                <p className="tit">사은품으로 더하는 쇼핑의 즐거움<br/>인기 쿡웨어부터 조리도구까지</p> <p className="desc">WAGENSTEIGER</p> </div>
                                                        </div>
                                                        </a>
                                                    </div>

                                                    <div className="gods-list">
                                                            <div className="gods-item" view-godno="GQW924042940175">
                                                                    <a href="javascript:goToProductDetailCorner('WAGENSTEIGER', 'GQW924042940175', '', 'ourPickOURPICK_AType23360',1,'23360','세트 4');">
                                                                        <div className="gods-img">
                                                                            <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/cmd/LB_220x293/src/https://img.ssfshop.com/goods/LIFE/24/04/29/GQW924042940175_0_ORGINL_20240429153314446.jpg"/>
                                                                        </div>
                                                                        <div className="gods-info">
                                                                            <p className="brand"> WAGENSTEIGER</p>
                                                                            <p className="name">네오 멀티팟 4.3L</p>
                                                                            <p className="price">
                                                                                <del><span className="wa_hidden">원가</span>
                                                                                                    52,900<span className="wa_hidden">원
                                                                                                </span></del>
                                                                                                <em className="sale"><span className="wa_hidden">할인율</span>
                                                                                                    52%</em><span className="wa_hidden">판매가</span>25,330<span className="wa_hidden">원</span>
                                                                                                
                                                                                            </p>
                                                                        </div>
                                                                    </a>
                                                                </div>
                                                            <div className="gods-item" view-godno="GQW923081672649">
                                                                    <a href="javascript:goToProductDetailCorner('WAGENSTEIGER', 'GQW923081672649', '', 'ourPickOURPICK_AType23360',2,'23360','세트 4');">
                                                                        <div className="gods-img">
                                                                            <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/cmd/LB_220x293/src/https://img.ssfshop.com/goods/LIFE/23/08/16/GQW923081672649_0_THNAIL_ORGINL_20240618151610694.jpg"/>
                                                                        </div>
                                                                        <div className="gods-info">
                                                                            <p className="brand"> WAGENSTEIGER</p>
                                                                            <p className="name">KILN 킬른 통3중 스텐 미니화로</p>
                                                                            <p className="price">
                                                                                <del><span className="wa_hidden">원가</span>
                                                                                                    33,500<span className="wa_hidden">원
                                                                                                </span></del>
                                                                                                <em className="sale"><span className="wa_hidden">할인율</span>
                                                                                                    43%</em><span className="wa_hidden">판매가</span>19,220<span className="wa_hidden">원</span>
                                                                                                
                                                                                            </p>
                                                                        </div>
                                                                    </a>
                                                                </div>
                                                            </div>
                                                    </div>
                                        </div>
                                    <div className="swiper-slide" role="group" aria-label="4 / 8" style={{"width": "692px", "marginRight": "16px"}}>
                                            <div className="gods-area">
                                                <div className="gods-main">
                                                        <a href="/special/103411/view?&amp;utag=ref_tpl:111942$ref_cnr:23360$set:2$dpos:1" onclick="cnrClickLoging('23360','세트 3','1','/special/103411/view');">
                                                            <div className="gods-img">
                                                            <img alt="" className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23360_346009_56_KOR_20250124141724.jpg"/>
                                                            <div className="gods-desc">
                                                                <p className="tit">일상 그리고 나를 위한 선택<br/>이월 특가 + 15% 쿠폰</p> <p className="desc">K2 &amp; EIDER</p> </div>
                                                        </div>
                                                        </a>
                                                    </div>

                                                    <div className="gods-list">
                                                            <div className="gods-item" view-godno="GQ0EA24082832355">
                                                                    <a href="javascript:goToProductDetailCorner('EIDER', 'GQ0EA24082832355', '', 'ourPickOURPICK_AType23360',1,'23360','세트 3');">
                                                                        <div className="gods-img">
                                                                            <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/cmd/LB_220x293/src/https://img.ssfshop.com/goods/SPRT/A2/40/82/GQ0EA24082832355_0_ORGINL_20240828101542341.jpg"/>
                                                                        </div>
                                                                        <div className="gods-info">
                                                                            <p className="brand"> EIDER</p>
                                                                            <p className="name">[EIDER공식] 남성 POP ON 퀼팅 남성 슬림 다운 자켓 (TKC)_DMW24593Z8</p>
                                                                            <p className="price">
                                                                                <del><span className="wa_hidden">원가</span>
                                                                                                    245,000<span className="wa_hidden">원
                                                                                                </span></del>
                                                                                                <em className="sale"><span className="wa_hidden">할인율</span>
                                                                                                    39%</em><span className="wa_hidden">판매가</span>149,000<span className="wa_hidden">원</span>
                                                                                                
                                                                                            </p>
                                                                        </div>
                                                                    </a>
                                                                </div>
                                                            <div className="gods-item" view-godno="GQ0EA24082832363">
                                                                    <a href="javascript:goToProductDetailCorner('K2', 'GQ0EA24082832363', '', 'ourPickOURPICK_AType23360',2,'23360','세트 3');">
                                                                        <div className="gods-img">
                                                                            <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/cmd/LB_220x293/src/https://img.ssfshop.com/goods/SPRT/A2/40/82/GQ0EA24082832363_0_ORGINL_20240828101718552.jpg"/>
                                                                        </div>
                                                                        <div className="gods-info">
                                                                            <p className="brand"> K2</p>
                                                                            <p className="name">[K2공식] 공용 E_벤치다운_GMW24595Z1</p>
                                                                            <p className="price">
                                                                                <del><span className="wa_hidden">원가</span>
                                                                                                    382,000<span className="wa_hidden">원
                                                                                                </span></del>
                                                                                                <em className="sale"><span className="wa_hidden">할인율</span>
                                                                                                    57%</em><span className="wa_hidden">판매가</span>165,450<span className="wa_hidden">원</span>
                                                                                                
                                                                                            </p>
                                                                        </div>
                                                                    </a>
                                                                </div>
                                                            </div>
                                                    </div>
                                        </div>
                                    <div className="swiper-slide" role="group" aria-label="5 / 8" style={{"width": "692px", "marginRight": "16px"}}>
                                            <div className="gods-area">
                                                <div className="gods-main">
                                                        <a href="/special/103149/view?&amp;utag=ref_tpl:111942$ref_cnr:23360$set:2$dpos:1" onclick="cnrClickLoging('23360','세트 5','1','/special/103149/view');">
                                                            <div className="gods-img">
                                                            <img data-src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23360_346022_178_KOR_20250127103352.jpg" alt="" className="swiper-lazy"/>
                                                            <div className="gods-desc">
                                                                <p className="tit">혜택으로 채우는 풍요로운 설<br/>연휴 한정 13, 18% 더블 쿠폰</p> <p className="desc">ANOTHER#</p> </div>
                                                        </div>
                                                        </a>
                                                    </div>

                                                    <div className="gods-list">
                                                            <div className="gods-item" view-godno="GQKZ24052598667">
                                                                    <a href="javascript:goToProductDetailCorner('HAI', 'GQKZ24052598667', '', 'ourPickOURPICK_AType23360',1,'23360','세트 5');">
                                                                        <div className="gods-img">
                                                                            <img data-src="https://img.ssfshop.com/cmd/LB_220x293/src/https://img.ssfshop.com/goods/ORBR/24/05/25/GQKZ24052598667_0_THNAIL_ORGINL_20240525171459483.jpg" className="swiper-lazy"/>
                                                                        </div>
                                                                        <div className="gods-info">
                                                                            <p className="brand"> HAI</p>
                                                                            <p className="name">[공식] Little Silk Bag Pink</p>
                                                                            <p className="price">
                                                                                <del><span className="wa_hidden">원가</span>
                                                                                                    148,000<span className="wa_hidden">원
                                                                                                </span></del>
                                                                                                <em className="sale"><span className="wa_hidden">할인율</span>
                                                                                                    30%</em><span className="wa_hidden">판매가</span>103,600<span className="wa_hidden">원</span>
                                                                                                
                                                                                            </p>
                                                                        </div>
                                                                    </a>
                                                                </div>
                                                            <div className="gods-item" view-godno="GQ5924121824966">
                                                                    <a href="javascript:goToProductDetailCorner('Victoria', 'GQ5924121824966', '', 'ourPickOURPICK_AType23360',2,'23360','세트 5');">
                                                                        <div className="gods-img">
                                                                            <img data-src="https://img.ssfshop.com/cmd/LB_220x293/src/https://img.ssfshop.com/goods/ORBR/24/12/18/GQ5924121824966_0_THNAIL_ORGINL_20241219112420262.jpg" className="swiper-lazy"/>
                                                                        </div>
                                                                        <div className="gods-info">
                                                                            <p className="brand"> Victoria</p>
                                                                            <p className="name">🔥15%쿠폰🔥빅토리아 슈즈 라인 프렌즈 브라운 카사 리본 오다 메리제인 CRUDO</p>
                                                                            <p className="price">
                                                                                <del><span className="wa_hidden">원가</span>
                                                                                                    79,000<span className="wa_hidden">원
                                                                                                </span></del>
                                                                                                <em className="sale"><span className="wa_hidden">할인율</span>
                                                                                                    30%</em><span className="wa_hidden">판매가</span>55,300<span className="wa_hidden">원</span>
                                                                                                
                                                                                            </p>
                                                                        </div>
                                                                    </a>
                                                                </div>
                                                            </div>
                                                    </div>
                                        </div>
                                    <div className="swiper-slide" role="group" aria-label="6 / 8" style={{"width": "692px", "marginRight": "16px"}}>
                                            <div className="gods-area">
                                                <div className="gods-main">
                                                        <a href="/special/103025/view?&amp;utag=ref_tpl:111942$ref_cnr:23360$set:2$dpos:1" onclick="cnrClickLoging('23360','세트 6','1','/special/103025/view');">
                                                            <div className="gods-img">
                                                            <img data-src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23360_346026_113_KOR_20250124142502.jpg" alt="" className="swiper-lazy"/>
                                                            <div className="gods-desc">
                                                                <p className="tit">무궁한 사랑<br/>태극당과 비이커의 달콤한 만남</p> <p className="desc">BEAKER</p> </div>
                                                        </div>
                                                        </a>
                                                    </div>

                                                    <div className="gods-list">
                                                            <div className="gods-item" view-godno="GM0025011482333">
                                                                    <a href="javascript:goToProductDetailCorner('BEAKER-X-TAEGEUKDANG', 'GM0025011482333', '', 'ourPickOURPICK_AType23360',1,'23360','세트 6');">
                                                                        <div className="gods-img">
                                                                            <img data-src="https://img.ssfshop.com/cmd/LB_220x293/src/https://img.ssfshop.com/goods/MCBR/25/01/14/GM0025011482333_0_THNAIL_ORGINL_20250121144812549.jpg" className="swiper-lazy"/>
                                                                        </div>
                                                                        <div className="gods-info">
                                                                            <p className="brand"> BEAKER X TAEGEUKDANG</p>
                                                                            <p className="name">Multi Charm Key Ring - Pink</p>
                                                                            <p className="price">
                                                                                <del><span className="wa_hidden">원가</span>
                                                                                                    35,000<span className="wa_hidden">원
                                                                                                </span></del>
                                                                                                <em className="sale"><span className="wa_hidden">할인율</span>
                                                                                                    5%</em><span className="wa_hidden">판매가</span>33,250<span className="wa_hidden">원</span>
                                                                                                
                                                                                            </p>
                                                                        </div>
                                                                    </a>
                                                                </div>
                                                            <div className="gods-item" view-godno="GM0025011482289">
                                                                    <a href="javascript:goToProductDetailCorner('BEAKER-X-TAEGEUKDANG', 'GM0025011482289', '', 'ourPickOURPICK_AType23360',2,'23360','세트 6');">
                                                                        <div className="gods-img">
                                                                            <img data-src="https://img.ssfshop.com/cmd/LB_220x293/src/https://img.ssfshop.com/goods/MCBR/25/01/14/GM0025011482289_0_THNAIL_ORGINL_20250121144822089.jpg" className="swiper-lazy"/>
                                                                        </div>
                                                                        <div className="gods-info">
                                                                            <p className="brand"> BEAKER X TAEGEUKDANG</p>
                                                                            <p className="name">Mugunghwa Chocolate 12 Set</p>
                                                                            <p className="price">
                                                                                <del><span className="wa_hidden">원가</span>
                                                                                                    34,000<span className="wa_hidden">원
                                                                                                </span></del>
                                                                                                <em className="sale"><span className="wa_hidden">할인율</span>
                                                                                                    5%</em><span className="wa_hidden">판매가</span>32,300<span className="wa_hidden">원</span>
                                                                                                
                                                                                            </p>
                                                                        </div>
                                                                    </a>
                                                                </div>
                                                            </div>
                                                    </div>
                                        </div>
                                    <div className="swiper-slide" role="group" aria-label="7 / 8" style={{"width": "692px", "marginRight": "16px"}}>
                                            <div className="gods-area">
                                                <div className="gods-main">
                                                        <a href="/special/103543/view?&amp;utag=ref_tpl:111942$ref_cnr:23360$set:2$dpos:1" onclick="cnrClickLoging('23360','세트 8','1','/special/103543/view');">
                                                            <div className="gods-img">
                                                            <img data-src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23360_346032_92_KOR_20250127103430.jpg" alt="" className="swiper-lazy"/>
                                                            <div className="gods-desc">
                                                                <p className="tit">일상 속 향기로운 휴식<br/>단독 최저가 + 10% 쿠폰</p> <p className="desc">HUXLEY</p> </div>
                                                        </div>
                                                        </a>
                                                    </div>

                                                    <div className="gods-list">
                                                            <div className="gods-item" view-godno="GQCZ24080272205">
                                                                    <a href="javascript:goToProductDetailCorner('Huxley', 'GQCZ24080272205', '', 'ourPickOURPICK_AType23360',1,'23360','세트 8');">
                                                                        <div className="gods-img">
                                                                            <img data-src="https://img.ssfshop.com/cmd/LB_220x293/src/https://img.ssfshop.com/goods/BETY/24/08/02/GQCZ24080272205_0_THNAIL_ORGINL_20250101070803669.jpg" className="swiper-lazy"/>
                                                                        </div>
                                                                        <div className="gods-info">
                                                                            <p className="brand"> Huxley</p>
                                                                            <p className="name">🥇SSF 립밤 부문🥇[10%추가쿠폰] 헉슬리 립밤 리브 비하인드 듀오</p>
                                                                            <p className="price">
                                                                                <del><span className="wa_hidden">원가</span>
                                                                                                    28,000<span className="wa_hidden">원
                                                                                                </span></del>
                                                                                                <em className="sale"><span className="wa_hidden">할인율</span>
                                                                                                    36%</em><span className="wa_hidden">판매가</span>18,060<span className="wa_hidden">원</span>
                                                                                                
                                                                                            </p>
                                                                        </div>
                                                                    </a>
                                                                </div>
                                                            <div className="gods-item" view-godno="GQCZ24071425308">
                                                                    <a href="javascript:goToProductDetailCorner('Huxley', 'GQCZ24071425308', '', 'ourPickOURPICK_AType23360',2,'23360','세트 8');">
                                                                        <div className="gods-img">
                                                                            <img data-src="https://img.ssfshop.com/cmd/LB_220x293/src/https://img.ssfshop.com/goods/BETY/24/07/14/GQCZ24071425308_0_THNAIL_ORGINL_20241224155326429.jpg" className="swiper-lazy"/>
                                                                        </div>
                                                                        <div className="gods-info">
                                                                            <p className="brand"> Huxley</p>
                                                                            <p className="name">[10%추가쿠폰] 헉슬리 에센스 커버 쿠션 언씬 레이어</p>
                                                                            <p className="price">
                                                                                <del><span className="wa_hidden">원가</span>
                                                                                                    38,000<span className="wa_hidden">원
                                                                                                </span></del>
                                                                                                <em className="sale"><span className="wa_hidden">할인율</span>
                                                                                                    27%</em><span className="wa_hidden">판매가</span>27,630<span className="wa_hidden">원</span>
                                                                                                
                                                                                            </p>
                                                                        </div>
                                                                    </a>
                                                                </div>
                                                            </div>
                                                    </div>
                                        </div>
                                    <div className="swiper-slide" role="group" aria-label="8 / 8" style={{"width": "692px", "margin-right": "16px"}}>
                                            <div className="gods-area">
                                                <div className="gods-main">
                                                        <a href="/special/103195/view?&amp;utag=ref_tpl:111942$ref_cnr:23360$set:2$dpos:1" onclick="cnrClickLoging('23360','세트 7','1','/special/103195/view');">
                                                            <div className="gods-img">
                                                            <img data-src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23360_346036_31_KOR_20250124142614.jpg" alt="" className="swiper-lazy"/>
                                                            <div className="gods-desc">
                                                                <p className="tit">황금연휴에 더 큰 혜택으로<br/>우리집 살림 장만 ~72%</p> <p className="desc">LIFE</p> </div>
                                                        </div>
                                                        </a>
                                                    </div>

                                                    <div className="gods-list">
                                                            <div className="gods-item" view-godno="GQ9N24022819215">
                                                                    <a href="javascript:goToProductDetailCorner('STAUB', 'GQ9N24022819215', '', 'ourPickOURPICK_AType23360',1,'23360','세트 7');">
                                                                        <div className="gods-img">
                                                                            <img data-src="https://img.ssfshop.com/cmd/LB_220x293/src/https://img.ssfshop.com/goods/LIFE/24/02/28/GQ9N24022819215_0_THNAIL_ORGINL_20240228172804417.jpg" className="swiper-lazy"/>
                                                                        </div>
                                                                        <div className="gods-info">
                                                                            <p className="brand"> STAUB</p>
                                                                            <p className="name">[스타우브] 세라믹 미니 꼬꼬떼 10cm 블루</p>
                                                                            <p className="price">
                                                                                <del><span className="wa_hidden">원가</span>
                                                                                                    54,000<span className="wa_hidden">원
                                                                                                </span></del>
                                                                                                <em className="sale"><span className="wa_hidden">할인율</span>
                                                                                                    57%</em><span className="wa_hidden">판매가</span>23,000<span className="wa_hidden">원</span>
                                                                                                
                                                                                            </p>
                                                                        </div>
                                                                    </a>
                                                                </div>
                                                            <div className="gods-item" view-godno="GQ9N21122854068">
                                                                    <a href="javascript:goToProductDetailCorner('CORELLE', 'GQ9N21122854068', '', 'ourPickOURPICK_AType23360',2,'23360','세트 7');">
                                                                        <div className="gods-img">
                                                                            <img data-src="https://img.ssfshop.com/cmd/LB_220x293/src/https://img.ssfshop.com/goods/ORBR/21/12/28/GQ9N21122854068_0_ORGINL_20211228150821464.jpg" className="swiper-lazy"/>
                                                                        </div>
                                                                        <div className="gods-info">
                                                                            <p className="brand"> CORELLE</p>
                                                                            <p className="name">[코렐] 스누피 더홈 원형접시세트 11P</p>
                                                                            <p className="price">
                                                                                <del><span className="wa_hidden">원가</span>
                                                                                                    98,700<span className="wa_hidden">원
                                                                                                </span></del>
                                                                                                <em className="sale"><span className="wa_hidden">할인율</span>
                                                                                                    31%</em><span className="wa_hidden">판매가</span>68,000<span className="wa_hidden">원</span>
                                                                                                
                                                                                            </p>
                                                                        </div>
                                                                    </a>
                                                                </div>
                                                            </div>
                                                    </div>
                                        </div>
                                    </div>
                        <div className="swiper-button-control">
                            <div className="swiper-button-prev swiper-button-disabled" tabindex="-1" role="button" aria-label="Previous slide" aria-controls="swiper-wrapper-17c64f0812c5c608" aria-disabled="true"></div>
                            <div className="swiper-pagination swiper-pagination-fraction swiper-pagination-horizontal"><span className="swiper-pagination-current">1</span> / <span className="swiper-pagination-total">4</span></div>
                            <div className="swiper-button-next" tabindex="0" role="button" aria-label="Next slide" aria-controls="swiper-wrapper-17c64f0812c5c608" aria-disabled="false"></div>
                        </div>
                    <span className="swiper-notification" aria-live="assertive" aria-atomic="true"></span></div>
                </section>


        <section className="hot-brand">
            <div className="swiper swiper-initialized swiper-horizontal swiper-pointer-events swiper-autoheight swiper-backface-hidden">
                <div className="swiper-wrapper" id="swiper-wrapper-513dfba940703eb2" aria-live="polite" style={{"height": "260px"}}>
                <div className="swiper-slide swiper-slide-active" role="group" aria-label="1 / 3" style={{"width": "1400px"}}>
                            <div className="brand-lists" style={{border:"1px solid red"}}>
                                <ul>
                                <li>
                                        <a href="/BEANPOLE/main?dspCtgryNo=&amp;brandShopNo=BDMA01&amp;brndShopId=BPBR&amp;utag=ref_tpl:111942$ref_cnr:23368$set:1$dpos:1" onclick="cnrClickLoging('23368','1','1','/BEANPOLE/main?dspCtgryNo=&amp;brandShopNo=BDMA01&amp;brndShopId=BPBR');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346054_1_KOR_20240306165740.png"/>
                                                    </div>
                                                    <span className="tit">빈폴</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/8seconds/main?dspCtgryNo=&amp;brandShopNo=BDMA07A01&amp;brndShopId=8SBSS&amp;utag=ref_tpl:111942$ref_cnr:23368$set:1$dpos:2" onclick="cnrClickLoging('23368','1','2','/8seconds/main?dspCtgryNo=&amp;brandShopNo=BDMA07A01&amp;brndShopId=8SBSS');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346054_2_KOR_20240306165827.png"/>
                                                    </div>
                                                    <span className="tit">에잇세컨즈</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/beaker/main?brandShopNo=BDMA09&amp;brndShopId=MCBR&amp;utag=ref_tpl:111942$ref_cnr:23368$set:1$dpos:3" onclick="cnrClickLoging('23368','1','3','/beaker/main?brandShopNo=BDMA09&amp;brndShopId=MCBR');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346054_3_KOR_20240306165900.png"/>
                                                    </div>
                                                    <span className="tit">비이커</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/Maison-Kitsune/main?dspCtgryNo=&amp;brandShopNo=BDMA07A22&amp;brndShopId=BQMKT&amp;utag=ref_tpl:111942$ref_cnr:23368$set:1$dpos:4" onclick="cnrClickLoging('23368','1','4','/Maison-Kitsune/main?dspCtgryNo=&amp;brandShopNo=BDMA07A22&amp;brndShopId=BQMKT');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346054_5_KOR_20240306170026.png"/>
                                                    </div>
                                                    <span className="tit">메종키츠네</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/KUHO/main?dspCtgryNo=&amp;brandShopNo=BDMA07A02&amp;brndShopId=WMBKF&amp;utag=ref_tpl:111942$ref_cnr:23368$set:1$dpos:5" onclick="cnrClickLoging('23368','1','5','/KUHO/main?dspCtgryNo=&amp;brandShopNo=BDMA07A02&amp;brndShopId=WMBKF');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346054_6_KOR_20240306170202.png"/>
                                                    </div>
                                                    <span className="tit">구호</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/kuho%20plus/main?dspCtgryNo=&amp;brandShopNo=BDMA07A28&amp;brndShopId=ECBKE&amp;utag=ref_tpl:111942$ref_cnr:23368$set:1$dpos:6" onclick="cnrClickLoging('23368','1','6','/kuho%20plus/main?dspCtgryNo=&amp;brandShopNo=BDMA07A28&amp;brndShopId=ECBKE');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346054_8_KOR_20240306170407.png"/>
                                                    </div>
                                                    <span className="tit">구호플러스</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/Theory/main?dspCtgryNo=&amp;brandShopNo=BDMA07A30&amp;brndShopId=ECBTM&amp;utag=ref_tpl:111942$ref_cnr:23368$set:1$dpos:7" onclick="cnrClickLoging('23368','1','7','/Theory/main?dspCtgryNo=&amp;brandShopNo=BDMA07A30&amp;brndShopId=ECBTM');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346054_4_KOR_20240306165934.png"/>
                                                    </div>
                                                    <span className="tit">띠어리</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/AMI/main?dspCtgryNo=&amp;brandShopNo=BDMA07A19&amp;brndShopId=ECBCH&amp;utag=ref_tpl:111942$ref_cnr:23368$set:1$dpos:8" onclick="cnrClickLoging('23368','1','8','/AMI/main?dspCtgryNo=&amp;brandShopNo=BDMA07A19&amp;brndShopId=ECBCH');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346054_14_KOR_20240401153332.png"/>
                                                    </div>
                                                    <span className="tit">아미</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/ISSEY-MIYAKE/main?dspCtgryNo=&amp;brandShopNo=BDMA24&amp;brndShopId=IMIM&amp;leftBrandNM=&amp;utag=ref_tpl:111942$ref_cnr:23368$set:1$dpos:9" onclick="cnrClickLoging('23368','1','9','/ISSEY-MIYAKE/main?dspCtgryNo=&amp;brandShopNo=BDMA24&amp;brndShopId=IMIM&amp;leftBrandNM=');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346054_9_KOR_20240306170453.png"/>
                                                    </div>
                                                    <span className="tit">이세이미야케</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/THE-NORTH-FACE/main?brandShopNo=BDMA29AP3&amp;brndShopId=RTTNF&amp;utag=ref_tpl:111942$ref_cnr:23368$set:1$dpos:10" onclick="cnrClickLoging('23368','1','10','/THE-NORTH-FACE/main?brandShopNo=BDMA29AP3&amp;brndShopId=RTTNF');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346054_16_KOR_20240830132450.png"/>
                                                    </div>
                                                    <span className="tit">노스페이스</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/ULLALA/main?dspCtgryNo=&amp;brandShopNo=BDMA19Y36&amp;brndShopId=RTULL&amp;utag=ref_tpl:111942$ref_cnr:23368$set:1$dpos:11" onclick="cnrClickLoging('23368','1','11','/ULLALA/main?dspCtgryNo=&amp;brandShopNo=BDMA19Y36&amp;brndShopId=RTULL');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346054_17_KOR_20250103161410.png"/>
                                                    </div>
                                                    <span className="tit">울랄라</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/General%20Idea/main?dspCtgryNo=&amp;brandShopNo=BDMA19K98&amp;brndShopId=GRGNI&amp;utag=ref_tpl:111942$ref_cnr:23368$set:1$dpos:12" onclick="cnrClickLoging('23368','1','12','/General%20Idea/main?dspCtgryNo=&amp;brandShopNo=BDMA19K98&amp;brndShopId=GRGNI');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346054_18_KOR_20250103161449.png"/>
                                                    </div>
                                                    <span className="tit">제너럴아이디어</span>
                                                </a>
                                        </li>
                                    </ul>
                            </div>
                        </div>
                    <div className="swiper-slide swiper-slide-next" role="group" aria-label="2 / 3" style={{"width": "1400px"}}>
                            <div className="brand-lists">
                                <ul>
                                <li>
                                        <a href="/DUVETICA/main?dspCtgryNo=&amp;brandShopNo=BDMA25B46&amp;brndShopId=GFDUG&amp;utag=ref_tpl:111942$ref_cnr:23368$set:2$dpos:1" onclick="cnrClickLoging('23368','2','1','/DUVETICA/main?dspCtgryNo=&amp;brandShopNo=BDMA25B46&amp;brndShopId=GFDUG');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346055_13_KOR_20250103161604.png"/>
                                                    </div>
                                                    <span className="tit">듀베티카</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/LACOSTE%20/main?dspCtgryNo=&amp;brandShopNo=BDMA19X86&amp;brndShopId=RTLCT&amp;utag=ref_tpl:111942$ref_cnr:23368$set:2$dpos:2" onclick="cnrClickLoging('23368','2','2','/LACOSTE%20/main?dspCtgryNo=&amp;brandShopNo=BDMA19X86&amp;brndShopId=RTLCT');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346055_21_KOR_20240805144610.png"/>
                                                    </div>
                                                    <span className="tit">라코스테</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/GOBI/main?dspCtgryNo=&amp;brandShopNo=BDMA19BLL&amp;brndShopId=ACGB&amp;utag=ref_tpl:111942$ref_cnr:23368$set:2$dpos:3" onclick="cnrClickLoging('23368','2','3','/GOBI/main?dspCtgryNo=&amp;brandShopNo=BDMA19BLL&amp;brndShopId=ACGB');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346055_26_KOR_20250103161709.png"/>
                                                    </div>
                                                    <span className="tit">고비</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/Tory%20Burch/main?dspCtgryNo=&amp;brandShopNo=BDMA07A14&amp;brndShopId=ECBTB&amp;utag=ref_tpl:111942$ref_cnr:23368$set:2$dpos:4" onclick="cnrClickLoging('23368','2','4','/Tory%20Burch/main?dspCtgryNo=&amp;brandShopNo=BDMA07A14&amp;brndShopId=ECBTB');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346055_5_KOR_20240306171237.png"/>
                                                    </div>
                                                    <span className="tit">토리버치</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/COMME-DES-GARCONS/main?dspCtgryNo=&amp;brandShopNo=BDMA33&amp;brndShopId=CGCG&amp;utag=ref_tpl:111942$ref_cnr:23368$set:2$dpos:5" onclick="cnrClickLoging('23368','2','5','/COMME-DES-GARCONS/main?dspCtgryNo=&amp;brandShopNo=BDMA33&amp;brndShopId=CGCG');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346055_27_KOR_20250103161825.png"/>
                                                    </div>
                                                    <span className="tit">꼼데가르송</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/JUUNJ/main?dspCtgryNo=&amp;brandShopNo=BDMA07A11&amp;brndShopId=ECBJC&amp;utag=ref_tpl:111942$ref_cnr:23368$set:2$dpos:6" onclick="cnrClickLoging('23368','2','6','/JUUNJ/main?dspCtgryNo=&amp;brandShopNo=BDMA07A11&amp;brndShopId=ECBJC');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346055_28_KOR_20250103161921.png"/>
                                                    </div>
                                                    <span className="tit">준지</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/SHIFTG/main?dspCtgryNo=&amp;brandShopNo=BDMA34&amp;brndShopId=GSGS&amp;utag=ref_tpl:111942$ref_cnr:23368$set:2$dpos:7" onclick="cnrClickLoging('23368','2','7','/SHIFTG/main?dspCtgryNo=&amp;brandShopNo=BDMA34&amp;brndShopId=GSGS');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346055_29_KOR_20250103162023.png"/>
                                                    </div>
                                                    <span className="tit">시프트지</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/10-Corso-Como/main?brandShopNo=BDMA23&amp;brndShopId=CCPB&amp;&amp;gnb=true&amp;utag=ref_tpl:111942$ref_cnr:23368$set:2$dpos:8" onclick="cnrClickLoging('23368','2','8','/10-Corso-Como/main?brandShopNo=BDMA23&amp;brndShopId=CCPB&amp;&amp;gnb=true');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346055_10_KOR_20240306171547.png"/>
                                                    </div>
                                                    <span className="tit">텐 꼬르소 꼬모</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/LEBEIGE/main?dspCtgryNo=&amp;brandShopNo=BDMA07A06&amp;brndShopId=ECBVF&amp;utag=ref_tpl:111942$ref_cnr:23368$set:2$dpos:9" onclick="cnrClickLoging('23368','2','9','/LEBEIGE/main?dspCtgryNo=&amp;brandShopNo=BDMA07A06&amp;brndShopId=ECBVF');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346055_4_KOR_20240306171155.png"/>
                                                    </div>
                                                    <span className="tit">르베이지</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/SONY/main?dspCtgryNo=&amp;brandShopNo=BDMA36A01&amp;brndShopId=RTSNY&amp;utag=ref_tpl:111942$ref_cnr:23368$set:2$dpos:10" onclick="cnrClickLoging('23368','2','10','/SONY/main?dspCtgryNo=&amp;brandShopNo=BDMA36A01&amp;brndShopId=RTSNY');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346055_30_KOR_20250103162232.png"/>
                                                    </div>
                                                    <span className="tit">소니</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/WAGENSTEIGER%20/main?dspCtgryNo=&amp;brandShopNo=BDMA26AOP&amp;brndShopId=RTWSG&amp;utag=ref_tpl:111942$ref_cnr:23368$set:2$dpos:11" onclick="cnrClickLoging('23368','2','11','/WAGENSTEIGER%20/main?dspCtgryNo=&amp;brandShopNo=BDMA26AOP&amp;brndShopId=RTWSG');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346055_31_KOR_20250103164559.png"/>
                                                    </div>
                                                    <span className="tit">바겐슈타이거</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/ALLSAINTS/main?dspCtgryNo=&amp;brandShopNo=BDMA19Z06&amp;brndShopId=RTAST&amp;utag=ref_tpl:111942$ref_cnr:23368$set:2$dpos:12" onclick="cnrClickLoging('23368','2','12','/ALLSAINTS/main?dspCtgryNo=&amp;brandShopNo=BDMA19Z06&amp;brndShopId=RTAST');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy swiper-lazy-loaded" src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346055_32_KOR_20250103162347.png"/>
                                                    </div>
                                                    <span className="tit">올세인츠</span>
                                                </a>
                                        </li>
                                    </ul>
                            </div>
                        </div>
                    <div className="swiper-slide" role="group" aria-label="3 / 3" style={{"width": "1400px"}}>
                            <div className="brand-lists">
                                <ul>
                                <li>
                                        <a href="/LEVIS%20/main?dspCtgryNo=&amp;brandShopNo=BDMA19AEG&amp;brndShopId=RTLVS&amp;utag=ref_tpl:111942$ref_cnr:23368$set:3$dpos:1" onclick="cnrClickLoging('23368','3','1','/LEVIS%20/main?dspCtgryNo=&amp;brandShopNo=BDMA19AEG&amp;brndShopId=RTLVS');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy" data-src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346056_29_KOR_20250103163639.png"/>
                                                    </div>
                                                    <span className="tit">리바이스</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/Koy/main?dspCtgryNo=&amp;brandShopNo=BDMA28AQ2&amp;brndShopId=RTKOY&amp;utag=ref_tpl:111942$ref_cnr:23368$set:3$dpos:2" onclick="cnrClickLoging('23368','3','2','/Koy/main?dspCtgryNo=&amp;brandShopNo=BDMA28AQ2&amp;brndShopId=RTKOY');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy" data-src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346056_33_KOR_20250103163813.png"/>
                                                    </div>
                                                    <span className="tit">코이</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/LITTLE-DEPT/main?dspCtgryNo=&amp;brandShopNo=BDMA31B51&amp;brndShopId=KDLD&amp;utag=ref_tpl:111942$ref_cnr:23368$set:3$dpos:3" onclick="cnrClickLoging('23368','3','3','/LITTLE-DEPT/main?dspCtgryNo=&amp;brandShopNo=BDMA31B51&amp;brndShopId=KDLD');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy" data-src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346056_39_KOR_20250116094502.png"/>
                                                    </div>
                                                    <span className="tit">리틀뎁</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/GANNI/main?dspCtgryNo=&amp;brandShopNo=BDMA07A99&amp;brndShopId=BQCGN&amp;utag=ref_tpl:111942$ref_cnr:23368$set:3$dpos:4" onclick="cnrClickLoging('23368','3','4','/GANNI/main?dspCtgryNo=&amp;brandShopNo=BDMA07A99&amp;brndShopId=BQCGN');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy" data-src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346056_35_KOR_20250103163942.png"/>
                                                    </div>
                                                    <span className="tit">가니</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/beaker/Danton/main?dspCtgryNo=&amp;brandShopNo=BDMA09F02&amp;brndShopId=BQMDT&amp;utag=ref_tpl:111942$ref_cnr:23368$set:3$dpos:5" onclick="cnrClickLoging('23368','3','5','/beaker/Danton/main?dspCtgryNo=&amp;brandShopNo=BDMA09F02&amp;brndShopId=BQMDT');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy" data-src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346056_36_KOR_20250103164017.png"/>
                                                    </div>
                                                    <span className="tit">단톤</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/LEMAIRE/main?dspCtgryNo=&amp;brandShopNo=BDMA07A39&amp;brndShopId=ECBLR&amp;utag=ref_tpl:111942$ref_cnr:23368$set:3$dpos:6" onclick="cnrClickLoging('23368','3','6','/LEMAIRE/main?dspCtgryNo=&amp;brandShopNo=BDMA07A39&amp;brndShopId=ECBLR');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy" data-src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346056_37_KOR_20250103164054.png"/>
                                                    </div>
                                                    <span className="tit">르메르</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/Rogatis/main?dspCtgryNo=&amp;brandShopNo=BDMA04A05&amp;brndShopId=HMBRX&amp;utag=ref_tpl:111942$ref_cnr:23368$set:3$dpos:7" onclick="cnrClickLoging('23368','3','7','/Rogatis/main?dspCtgryNo=&amp;brandShopNo=BDMA04A05&amp;brndShopId=HMBRX');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy" data-src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346056_6_KOR_20240306172201.png"/>
                                                    </div>
                                                    <span className="tit">로가디스</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/Galaxy%20Lifestyle/main?dspCtgryNo=&amp;brandShopNo=BDMA04A02&amp;brndShopId=HMBGC&amp;utag=ref_tpl:111942$ref_cnr:23368$set:3$dpos:8" onclick="cnrClickLoging('23368','3','8','/Galaxy%20Lifestyle/main?dspCtgryNo=&amp;brandShopNo=BDMA04A02&amp;brndShopId=HMBGC');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy" data-src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346056_11_KOR_20240306172508.png"/>
                                                    </div>
                                                    <span className="tit">갤럭시라이프스타일</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/Galaxy/main?dspCtgryNo=&amp;brandShopNo=BDMA04A01&amp;brndShopId=HMBGA&amp;utag=ref_tpl:111942$ref_cnr:23368$set:3$dpos:9" onclick="cnrClickLoging('23368','3','9','/Galaxy/main?dspCtgryNo=&amp;brandShopNo=BDMA04A01&amp;brndShopId=HMBGA');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy" data-src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346056_10_KOR_20240521103738.png"/>
                                                    </div>
                                                    <span className="tit">갤럭시</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/kotelo/main?dspCtgryNo=&amp;brandShopNo=BDMA07A61&amp;brndShopId=EBCWE&amp;utag=ref_tpl:111942$ref_cnr:23368$set:3$dpos:10" onclick="cnrClickLoging('23368','3','10','/kotelo/main?dspCtgryNo=&amp;brandShopNo=BDMA07A61&amp;brndShopId=EBCWE');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy" data-src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346056_38_KOR_20250103164150.png"/>
                                                    </div>
                                                    <span className="tit">코텔로</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/Studio-Nicholson/main?dspCtgryNo=&amp;brandShopNo=BDMA07A97&amp;brndShopId=BQSN&amp;leftBrandNM=&amp;utag=ref_tpl:111942$ref_cnr:23368$set:3$dpos:11" onclick="cnrClickLoging('23368','3','11','/Studio-Nicholson/main?dspCtgryNo=&amp;brandShopNo=BDMA07A97&amp;brndShopId=BQSN&amp;leftBrandNM=');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy" data-src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346056_2_KOR_20240306171918.png"/>
                                                    </div>
                                                    <span className="tit">스튜디오니콜슨</span>
                                                </a>
                                        </li>
                                    <li>
                                        <a href="/rag%20＆%20bone/main?dspCtgryNo=&amp;brandShopNo=BDMA07A40&amp;brndShopId=RAB&amp;utag=ref_tpl:111942$ref_cnr:23368$set:3$dpos:12" onclick="cnrClickLoging('23368','3','12','/rag%20＆%20bone/main?dspCtgryNo=&amp;brandShopNo=BDMA07A40&amp;brndShopId=RAB');">
                                            <div className="brand-box">
                                                        <img className="swiper-lazy" data-src="https://img.ssfshop.com/display/category/THM/A30/A16/contents/23368_346056_28_KOR_20241204152243.png"/>
                                                    </div>
                                                    <span className="tit">랙앤본</span>
                                                </a>
                                        </li>
                                    </ul>
                            </div>
                        </div>
                    </div>
                <div className="swiper-button-control">
                    <div className="swiper-button-prev swiper-button-disabled" tabindex="-1" role="button" aria-label="Previous slide" aria-controls="swiper-wrapper-513dfba940703eb2" aria-disabled="true"></div>
                    <div className="swiper-pagination swiper-pagination-fraction swiper-pagination-horizontal"><span className="swiper-pagination-current">1</span> / <span className="swiper-pagination-total">3</span></div>
                    <div className="swiper-button-next" tabindex="0" role="button" aria-label="Next slide" aria-controls="swiper-wrapper-513dfba940703eb2" aria-disabled="false"></div>
                </div>
            <span className="swiper-notification" aria-live="assertive" aria-atomic="true"></span></div>
        </section>
    {/* <!-- #174180: promotion/event --> */}
    {sectionList && sectionList.map((section) => (
          <SectionWrap
            key={section.id}
            id={section.id}
            title={section.title}
           >
            {/* Render children if they exist */}
          {Array.isArray(section.children) &&
            section.children.map((child) => renderComponent(child))}
          </SectionWrap>
      ))}    


    </div>
  </div>
</main>
    );
}