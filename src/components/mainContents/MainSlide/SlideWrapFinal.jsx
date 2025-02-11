import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { CiPlay1 } from "react-icons/ci";
import { BsPause } from "react-icons/bs";
import { SlArrowLeft } from "react-icons/sl";
import { SlArrowRight } from "react-icons/sl";
import useInterval from './useInterval.jsx';


export default function SlideWrapFinal({item}) {
    const [data,setData] = useState([]);  //  데이터 관리값
    const [isPlay , setIsPlay] = useState(true); // 슬라이드 재생,멈춤 관리
    const [page, setPage] = useState(1);
    const length = data.length;  // 이미지 전체 갯수       
    const [isHover, setIsHover] = useState(false);

    useEffect(() => {
        axios.get('/data/slide.json')
            .then((res) => {setData(res.data)})
            .catch((error) => console.log(error));
    }, []);

    const nextSlide = () => {
        // setCurrent(current === length - 1 ? 0 : current + 1);
        setPage(page + 1 > length  ? 1 : page + 1);        
      };
    
      const prevSlide = () => {
        // setCurrent(current === 0 ? length - 1 : current - 1);
        setPage(page > 1 ? page-1  : length-1);
      };
      const handlePlay = () => {
        setIsPlay(true);
    }
    const handleStop = () => {
        setIsPlay(false);
    }
    const handleEnter = () => {
        setIsHover(true);
    }
    const handleLeave = () => {
        setIsHover(false);
    }
    return (
        <>
        <div className='slide-box'  onMouseEnter={handleEnter} onMouseLeave={handleLeave} >
              <SlArrowLeft onClick={prevSlide}
                            className= {isHover === true ? 'slide-leftBtn-hover': 'slide-leftBtn'} />
                <div >
                <img src={item.item1}/>
                    <div className={item.item1Br[2]==='' ? 
                            (item.item1Br[4] === ''?'top-up':'top-middle')
                            :'original'}>
                        <p className='slide-title'>
                            {item.item1Msg[0]}<br/>{item.item1Br[0]}</p>                    
                        <p className='slide-desc1'>                            
                            {item.item1Msg[1]}<br/>{item.item1Br[2]}</p>
                        <p className='slide-desc2'>
                            {item.item1Msg[2]}<br/>{item.item1Br[4]}</p>
                    </div>
                </div>             
                <div>
                <img src={item.item2}/>
                    <div className={item.item2Br[2]==='' ? 
                            (item.item2Br[4] === ''?'top-up':'top-middle')
                            :'original'}>
                        <p className='slide-title'>
                            {item.item2Msg[0]}<br/>{item.item2Br[0]}</p>
                        <p className='slide-desc1'>
                            {item.item2Msg[1]}<br/>{item.item2Br[2]}</p>
                        <p className='slide-desc2'>
                            {item.item2Msg[2]}<br/>{item.item2Br[4]}</p>
                    </div>
                </div>             
                <div>
                <img src={item.item3}/>
                    <div className={item.item3Br[2]==='' ? 
                            (item.item3Br[4] === ''?'top-up':'top-middle')
                            :'original'}>
                       <p className='slide-title'>
                            {item.item3Msg[0]}<br/>{item.item3Br[0]}</p>
                        <p className='slide-desc1'>
                            {item.item3Msg[1]}<br/>{item.item3Br[2]}</p>
                        <p className='slide-desc2'>
                            {item.item3Msg[2]}<br/>{item.item3Br[4]}</p>
                    </div>
                </div>     
                 <SlArrowRight   onClick={nextSlide}
                    className= {isHover === true ? 'slide-rightBtn-hover': 'slide-rightBtn'}  />    
                {isPlay === true ? 
                    (<BsPause onClick={handleStop}
                        className= {isHover === true ? 'slide-playBtn-hover': 'slide-playBtn'}/>):
                    (<CiPlay1 onClick={handlePlay}
                        className= {isHover === true ? 'slide-stopBtn-hover': 'slide-stopBtn'}/> )                                 
                }           
        </div>
        </>
    );
}

