export default function Nav(){
    return(
        <>
          <nav className='header-bottom'>
            <div className='nav-left'>
              <ul className='nav-main'>
                  <li>
                    <a href='#'>여성</a>
                  </li>
                  <li>
                    <a href='#'>남성</a>
                  </li>
                  <li>
                    <a href='#'>키즈</a>
                  </li>
                  <li>
                    <a href='#'>럭셔리</a>
                  </li>
                  <li>
                    <a href='#'>백&슈즈</a>
                  </li>
                  <li>
                    <a href='#'>스포츠</a>
                  </li>
                  <li>
                    <a href='#'>골프</a>
                  </li>
                  <li>
                    <a href='#'>뷰티</a>
                  </li>
                  <li>
                    <a href='#'>아울렛</a>
                  </li>
                </ul>
                <span>|</span>
                <ul className='nav-sub'>
                  <li>
                    <a href='#'>랭킹</a>
                  </li>
                  <li>
                    <a href='#'>브랜드</a>
                  </li>
                  <li>
                    <a href='#'>매거진</a>
                  </li>
                  <li>
                    <a href='#'>기획전</a>
                  </li>
                  <li>
                    <a href='#'>이벤트</a>
                  </li>
                </ul>
            </div>
            <div className='nav-right'>
              <ul className='nav-special'>
                <li>
                  <a href='#'>삼성전자</a>
                </li>
              </ul> 
            </div>
          </nav>
        </>
    );
};