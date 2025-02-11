import React, { useState,useEffect } from 'react';
import Slider from 'react-slick';
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import axios from 'axios';
import SlideWrapFinal from './SlideWrapFinal.jsx';

export default function Slick() {
    const [data, setData] = useState([]);

    useEffect(() => {
        axios.get('/data/slide.json')
            .then((res) => {setData(res.data)})
            .catch((error) => console.log(error));
    }, []);




    const settings = {
        dots: true, // 페이지네이션을 위한 dots 사용 여부
        infinite: true, // 슬라이드가 무한반복하도록 적용
        speed: 1000, // 슬라이드가 넘어가는 속도(ms)
        slidesToShow: 1, // 한 화면에 몇 개의 슬라이드를 보여줄 것인지
        slidesToScroll: 1, // 한번에 넘어갈 슬라이드의 갯수
        arrows: true, // 화살표 표시 여부
        autoplay: true, // 자동 재생 설정
        // autoplaySpeed: 1000, // 자동 재생 속도(ms) 
        // centerMode: true, // 현재 슬라이드를 가운데에 정렬
        // centerPadding: '100px', // 가장자리 슬라이드 사이의 간격
        // className: 'center' // Slider 클래스설정
      };
      
      return (
        <div>
          <Slider {...settings}>
            {data.map((data)=>
            <SlideWrapFinal item={data}/>
            )}
          </Slider>
        </div>
      );
}

